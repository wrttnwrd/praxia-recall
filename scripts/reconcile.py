#!/usr/bin/env python3
"""Reconciliation pass: find likely duplicate concepts, dangling relation
targets, and every recorded contradiction. Writes contradictions.md.

Entity resolution across batches is the main risk in a build this size, so this
runs last and reports rather than merging on its own.
"""
import re, sys, difflib, collections
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from graphlib import load_graph
import yaml

B = Path(__file__).resolve().parent.parent
G = load_graph()
ACC = yaml.safe_load((B / "accepted.yaml").read_text(encoding="utf-8")) if (B / "accepted.yaml").exists() else {}
ACCEPTED = {tuple(sorted(x["pair"])): x["reason"] for x in (ACC.get("fuzzy_pairs") or [])}
C = {c["id"]: c for c in G["concepts"]}

def norm(s):
    return re.sub(r"[^a-z0-9]", "", str(s).lower())

# 1. near-duplicate titles across different ids
names = {}
for c in G["concepts"]:
    for n in [c["title"]] + (c.get("aka") or []):
        names.setdefault(norm(n), set()).add(c["id"])
dupes = {k: v for k, v in names.items() if len(v) > 1}
fuzzy = []
keys = sorted(names)
for i, a in enumerate(keys):
    for b in keys[i+1:]:
        if abs(len(a) - len(b)) > 3 or a == b:
            continue
        if difflib.SequenceMatcher(None, a, b).ratio() > 0.87:
            ida, idb = sorted(names[a])[0], sorted(names[b])[0]
            if ida == idb:
                continue
            if ACC.get("suppress_numeric_variants") and \
               re.sub(r"\d+", "", ida) == re.sub(r"\d+", "", idb):
                continue          # differ only in digits: distinct by construction
            if tuple(sorted((ida, idb))) in ACCEPTED:
                continue          # reviewed and dismissed, see accepted.yaml
            fuzzy.append((C[ida]["title"], C[idb]["title"], ida, idb))

# 2. dangling targets
dangling = collections.Counter()
for c in G["concepts"]:
    for rel, ts in (c.get("relations") or {}).items():
        for t in ts:
            if t not in C:
                dangling[str(t)] += 1

# 3. contradictions / temporal notes
temporal = [(c["id"], c["title"], c["as_of"]) for c in G["concepts"] if c.get("as_of")]
conflicts = []
for c in G["concepts"]:
    blob = (c.get("body") or "") + " " + " ".join(str(v) for v in (c.get("evidence") or {}).values())
    for marker in ("CONTRADICTION", "Source conflict", "Attribution conflict", "Open question"):
        if marker.lower() in blob.lower():
            conflicts.append((c["title"], marker))
            break

L = ["---", "type: reference", "title: Reconciliation",
     "description: Duplicate candidates, unwritten entities, and every recorded contradiction.",
     "status: draft", "---", "", "# Reconciliation", "",
     f"{len(G['concepts'])} concepts. Run after every batch; it reports rather than merges.", ""]

L += ["## Same name, different concept", ""]
if dupes:
    for k, v in sorted(dupes.items()):
        L.append(f"* `{k}` → " + ", ".join(sorted(v)))
else:
    L.append("*None — every title and alias is unique.*")

L += ["", f"## Reviewed and dismissed ({len(ACCEPTED)})", "",
      "Checked once, recorded here so they stop reappearing as open items. "
      "Numeric-variant pairs (adjacent session numbers, part-1..part-8 notes) "
      "are suppressed automatically.", ""]
for (a, b), why in sorted(ACCEPTED.items()):
    na = C[a]["title"] if a in C else a
    nb = C[b]["title"] if b in C else b
    L.append(f"* **{na}** vs **{nb}** — {why}")

L += ["", "## Near-identical names (possible duplicates)", ""]
if fuzzy:
    for a, b, ia, ib in sorted(set(fuzzy)):
        L.append(f"* **{a}** (`{ia}`) vs **{b}** (`{ib}`)")
else:
    L.append("*None found above 0.87 similarity.*")

# kind must follow the type's parent in types.md
import re as _re
_parent, _cur = {}, None
for _l in (B / "types.md").read_text(encoding="utf-8").splitlines():
    if _l.startswith("# "):
        _cur = _l[2:].strip(); continue
    _m = _re.match(r"\s*-\s+([a-z0-9-]+)\s+—", _l)
    if _m and _cur and _cur not in ("Types", "Attributes"):
        _parent[_m.group(1)] = _cur
_PK = {"place": "places", "being": "people", "group": "groups", "vehicle": "vehicles",
       "thing": "things", "event": "events", "prep": "prep", "rules": "rules",
       "record": "lore"}
_undeclared = sorted({c["type"] for c in G["concepts"] if c["type"] not in _parent})
_misfiled = [c for c in G["concepts"]
             if c["type"] in _parent and c["type"] not in ("temple", "session", "storyline",
                                                           "reference", "glossary", "note")
             and _PK.get(_parent[c["type"]]) and _PK[_parent[c["type"]]] != c["kind"]]
L += ["", "## Type and folder agreement", ""]
L.append(f"* **{len(_undeclared)} types in use but not declared in types.md**"
         + (": " + ", ".join(f"`{t}`" for t in _undeclared) if _undeclared else " — none."))
L.append(f"* **{len(_misfiled)} concepts whose folder disagrees with their type's parent**"
         + (": " + ", ".join(f"{c['title']} (`{c['type']}` in {c['kind']}/)" for c in _misfiled[:10])
            if _misfiled else " — none."))

L += ["", "## Recorded contradictions and open questions", ""]
for t, m in sorted(set(conflicts)):
    L.append(f"* **{t}** — {m}")

L += ["", f"## Facts with an as-of date ({len(temporal)})", "",
      "These change over the vault's 2018-2026 span; the graph records when.", ""]
for i, t, a in sorted(temporal, key=lambda x: x[1]):
    L.append(f"* **{t}** — {a}")

L += ["", f"## Named but unwritten ({len(dangling)})", "",
      "Referenced by a relation but having no concept; they render as plain text.", ""]
for n, k in dangling.most_common():
    L.append(f"* {n} ({k})")

(B / "reconciliation.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"reconciliation.md — {len(dupes)} exact name collisions, {len(set(fuzzy))} fuzzy pairs, "
      f"{len(set(conflicts))} contradictions, {len(temporal)} dated facts, {len(dangling)} unwritten")
