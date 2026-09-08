#!/usr/bin/env python3
"""Build praxia-recall from graph.yaml + the read-only source vault.

The graph in graph.yaml was derived by READING ~/praxia, not by mapping its
frontmatter. Source frontmatter was treated as a hint and is not imported:
every field written here comes from the graph, with the sentence it came from
recorded in `evidence`.

  world/<kind>/<slug>.md   one concept per entity, organised by kind
  review.md                every entity + relation + evidence + confidence

Usage: python3 scripts/build.py [--dry-run]
"""
import re, sys, shutil, hashlib, datetime as dt
from pathlib import Path
from urllib.parse import quote
import yaml

BUNDLE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from graphlib import load_graph
GRAPH = load_graph()
SRC = Path(GRAPH["source"]).expanduser()
ACTOR = GRAPH.get("actor", "recall/claude-opus-5")
FM_RE = re.compile(r"\A---\n(.*?)\n---\n?(.*)\Z", re.S)
WIKI_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")

# relation -> (heading shown in ## Related, inverse relation for the review index)
RELATIONS = yaml.safe_load((BUNDLE / "relations.yaml").read_text(encoding="utf-8"))
ATTRIBUTES = ["species", "alignment"]   # closed-set properties, emitted as fields

def now():
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

def body_of(src_rel):
    """Body text of a source file, frontmatter stripped. Source is never written to."""
    p = SRC / src_rel
    if not p.exists():
        return None, None
    raw = p.read_text(encoding="utf-8", errors="replace")
    m = FM_RE.match(raw)
    body = m.group(2) if m else raw
    return body.strip(), hashlib.sha256(raw.encode()).hexdigest()[:16]

def concept_index():
    return {c["id"]: c for c in GRAPH["concepts"]}

def path_of(c):
    return f"{c['kind']}/{c['id']}.md"

def link(from_c, to_c):
    depth = from_c["kind"].count("/") + 1
    return quote("../" * depth + path_of(to_c))

def flatten(v, idx, by_name):
    """Wikilinks are not valid OKF links, so no emitted string may contain one —
    frontmatter values included, not just bodies."""
    if isinstance(v, str):
        return strip_wikilinks(v, idx, by_name)
    if isinstance(v, list):
        return [flatten(x, idx, by_name) for x in v]
    if isinstance(v, dict):
        return {k: flatten(x, idx, by_name) for k, x in v.items()}
    return v

def strip_wikilinks(text, idx, by_name):
    """Source wikilinks point at source paths. Re-point the ones we can resolve
    at bundle concepts; flatten the rest to plain text (never leave [[...]])."""
    def sub(m):
        target, label = m.group(1), m.group(2)
        name = (label or target.split("/")[-1]).strip()
        cid = by_name.get(name.lower())
        if cid:
            return f"[{name}](/world/{quote(path_of(idx[cid]))})"
        return name
    return WIKI_RE.sub(sub, text)

def main():
    dry = "--dry-run" in sys.argv
    idx = concept_index()
    by_name = {}
    for c in GRAPH["concepts"]:
        for n in [c["title"]] + (c.get("aka") or []):
            by_name.setdefault(n.lower(), c["id"])

    # Incremental: a concept file is rewritten only when its content changes.
    # Unchanged concepts keep their generated.at, so a rebuild touches only what
    # moved and git/sync/Obsidian see real deltas instead of 560 timestamps.
    NOW = now()
    AT_RE = re.compile(r"^  at: '?([0-9T:Z-]+)'?$", re.M)
    expected = set()
    counts = {"from_source": 0, "authored": 0, "relations": 0,
              "written": 0, "unchanged": 0, "removed": 0}
    for c in GRAPH["concepts"]:
        fm = {"type": c["type"], "title": c["title"],
              "description": c.get("description", "")}
        if c.get("aka"):
            fm["aka"] = c["aka"]
        if c.get("date"):
            fm["date"] = c["date"]
        if c.get("praxian_date"):
            fm["praxian_date"] = c["praxian_date"]
            fm["praxian_date_basis"] = c.get("praxian_date_basis", "occurred")
        # species and alignment are attributes of a being, not categorisations,
        # so they are plain frontmatter fields — the same shape the source vault
        # uses. There is no tag layer: the graph carries the meaning.
        if c.get("resource"):
            fm["resource"] = c["resource"]
        for attr in ATTRIBUTES:
            if c.get(attr):
                fm[attr] = c[attr]
        if c.get("tags"):
            fm["tags"] = sorted(c["tags"])

        rels, related_lines = c.get("relations") or {}, []
        for rel, targets in rels.items():
            names = []
            for t in targets:
                if t in idx:
                    names.append(f"[{idx[t]['title']}]({link(c, idx[t])})")
                else:
                    names.append(str(t))          # named but not yet a concept
                counts["relations"] += 1
            fm[rel] = [idx[t]["title"] if t in idx else t for t in targets]
            related_lines.append(f"**{RELATIONS[rel]['label']}:** " + ", ".join(names))

        body, chash = (None, None)
        if c.get("source"):
            body, chash = body_of(c["source"])
        if body is None:
            body = (c.get("body") or "").strip()
            counts["authored"] += 1
        else:
            counts["from_source"] += 1
            body = strip_wikilinks(body, idx, by_name)

        fm["status"] = "draft"
        fm["generated"] = {"by": ACTOR, "at": NOW, "method": "read-and-extract"}
        if c.get("source"):
            fm["sources"] = [{"id": "source",
                              "resource": f"file://{quote(str(SRC / c['source']))}",
                              "title": f"Original: {c['source']}"}]
            if chash:
                fm["content_hash"] = chash
        if c.get("evidence"):
            fm["evidence"] = c["evidence"]
        if c.get("confidence"):
            fm["confidence"] = c["confidence"]
        if c.get("as_of"):
            # Volatile assertions (alive/dead, owns, member_of) are true as of a
            # date. Without this the vault's 2018-2026 span contradicts itself.
            fm["as_of"] = c["as_of"]

        fm = flatten(fm, idx, by_name)
        out = f"---\n{yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).rstrip()}\n---\n\n"
        if c.get("thumbnail"):
            # kind folders sit under world/, so assets need one extra hop
            depth = c["kind"].count("/") + 2
            t = "../" * depth + c["thumbnail"].lstrip("/")
            body = (f"![{c['title']}]({quote(t)})\n\n"
                    f"*Thumbnail, 1200px. The full-resolution original is at "
                    f"`{c['resource'].replace('file://', '')}` — see `resource`.*\n"
                    + (body or ""))
        out += body if body else f"*No prose in the source; this concept was written from references elsewhere.*\n"
        if related_lines:
            out += "\n\n## Related\n" + "\n".join(related_lines) + "\n"

        dest = BUNDLE / "world" / path_of(c)
        expected.add(dest)
        if dest.exists():
            old = dest.read_text(encoding="utf-8")
            m = AT_RE.search(old)
            if m and out.replace(NOW, m.group(1)) == old:
                counts["unchanged"] += 1
                continue
        counts["written"] += 1
        if not dry:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(out, encoding="utf-8")

    # Concepts no longer in the graph are removed (index.md files belong to review.py).
    for stale in sorted((BUNDLE / "world").rglob("*.md")):
        if stale.name != "index.md" and stale not in expected:
            counts["removed"] += 1
            if not dry:
                stale.unlink()
    if not dry:
        for d in sorted((BUNDLE / "world").rglob("*"), key=lambda x: -len(x.parts)):
            if d.is_dir() and not any(d.iterdir()):
                d.rmdir()

    if not dry:
        # OKF v0.2 s9: flat list of date-grouped entries, newest first,
        # dates as ISO 8601 YYYY-MM-DD.
        log = BUNDLE / "log.md"
        today = dt.date.today().isoformat()
        entry = (f"- Rebuilt from graph.yaml: {len(GRAPH['concepts'])} concepts, "
                 f"{counts['relations']} relations, {counts['from_source']} source files; "
                 f"{counts['written']} concept file(s) written, {counts['unchanged']} unchanged, {counts['removed']} removed.")
        groups, cur = [], None
        if log.exists():
            for line in log.read_text(encoding="utf-8").splitlines():
                if line.startswith("## "):
                    cur = (line[3:].strip(), []); groups.append(cur)
                elif line.startswith("- ") and cur:
                    cur[1].append(line)
        prior_today = next((g[1] for g in groups if g[0] == today), [])
        groups = [g for g in groups if g[0] != today]
        # Newest first within the day: the rebuild line goes on top of earlier entries.
        groups.insert(0, (today, [entry] + [x for x in prior_today if not x.startswith("- Rebuilt from graph.yaml")]))
        out = ["# Log", ""]
        for day, entries in groups:
            out += [f"## {day}", ""] + list(dict.fromkeys(entries)) + [""]
        log.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")

    print(f"concepts: {len(GRAPH['concepts'])}  "
          f"(from source: {counts['from_source']}, authored: {counts['authored']})")
    print(f"relations: {counts['relations']}")
    print(f"files: {counts['written']} written, {counts['unchanged']} unchanged, {counts['removed']} removed")

main()
