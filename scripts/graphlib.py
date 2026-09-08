"""Shared graph loader. A later entry with the same id MERGES into the earlier
one, so each batch can enrich concepts written by an earlier batch without
editing them: scalars overwrite, relation/evidence maps union."""
import re
from pathlib import Path
import yaml

WIKI = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?(?:\]\]|$)")
# The trailing `|$` catches wikilinks truncated by a description cut-off,
# which a closing-bracket-only pattern silently leaves behind.

def _flatten(v):
    """Wikilinks are not valid OKF links. Strip them from every graph string
    once, at load, so no consumer can emit one."""
    if isinstance(v, str):
        return WIKI.sub(lambda m: (m.group(2) or m.group(1).split('/')[-1]).strip(), v)
    if isinstance(v, list):
        return [_flatten(x) for x in v]
    if isinstance(v, dict):
        return {k: _flatten(x) for k, x in v.items()}
    return v

B = Path(__file__).resolve().parent.parent

def load_graph(with_dates=True):
    g = yaml.safe_load((B / "graph.yaml").read_text(encoding="utf-8"))
    # generated praxian dates merge in like any other later entry
    for name in ("graph-maps.yaml", "graph-dates.yaml"):
        if name == "graph-dates.yaml" and not with_dates:
            continue
        f = B / name
        if f.exists():
            extra = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
            g["concepts"] = g["concepts"] + (extra.get("concepts") or [])
    merged, order = {}, []
    for c in g["concepts"]:
        i = c["id"]
        if i not in merged:
            merged[i] = c; order.append(i); continue
        base = merged[i]
        for k, v in c.items():
            if k in ("relations", "evidence") and isinstance(v, dict):
                tgt = base.setdefault(k, {})
                for rk, rv in v.items():
                    if isinstance(rv, list):
                        tgt[rk] = list(dict.fromkeys((tgt.get(rk) or []) + rv))
                    else:
                        tgt[rk] = rv
            elif k == "aka":
                # an explicit empty list CLEARS aliases (used to undo a bad alias)
                base["aka"] = [] if v == [] else list(dict.fromkeys((base.get("aka") or []) + v))
            elif k != "id":
                base[k] = v
    concepts = [_flatten(merged[i]) for i in order]

    # `retired_into: <id>` folds a duplicate concept into its canonical twin:
    # the duplicate is dropped and every relation pointing at it is repointed.
    # Used when reconciliation shows two concepts were always one thing.
    # `remove_relations: {rel: [ids]}` deletes relations a merge cannot unsay,
    # since merging unions lists. Needed when a correction replaces a relation
    # rather than adding one (enemy_of -> rival_of).
    for c in concepts:
        for rel, ts in (c.pop("remove_relations", None) or {}).items():
            cur = (c.get("relations") or {}).get(rel)
            if cur:
                c["relations"][rel] = [t for t in cur if t not in ts]
                if not c["relations"][rel]:
                    del c["relations"][rel]

    retired = {c["id"]: c["retired_into"] for c in concepts if c.get("retired_into")}
    def resolve(i):
        seen = set()
        while i in retired and i not in seen:
            seen.add(i); i = retired[i]
        return i
    for c in concepts:
        for rel, ts in (c.get("relations") or {}).items():
            c["relations"][rel] = list(dict.fromkeys(
                resolve(t) for t in ts if resolve(t) != c["id"]))
    # A coverage-only concept describes itself with its own opening line of
    # prose — a quotation, not a summary, so nothing is invented.
    src = Path(g.get("source", "")).expanduser()
    for c in concepts:
        d = str(c.get("description", ""))
        if not d.startswith("Source file `") or not c.get("source"):
            continue
        f = src / c["source"]
        if not f.exists():
            continue
        raw = f.read_text(encoding="utf-8", errors="replace")
        m = re.match(r"\A---\n.*?\n---\n", raw, re.S)
        body = raw[m.end():] if m else raw
        first = next((l.strip() for l in body.splitlines()
                      if l.strip() and not l.strip().startswith(("#", "!", "|", ">", "```"))
                      and len(l.strip()) > 15), "")
        first = _flatten(first)
        c["description"] = (first[:170] + ("…" if len(first) > 170 else "")) if first \
            else "No prose in the source; carried for coverage."

    g["concepts"] = [c for c in concepts if c["id"] not in retired]
    g["retired"] = retired
    return g
