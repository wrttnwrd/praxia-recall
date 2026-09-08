#!/usr/bin/env python3
"""Generate review.md (the judgment-call surface) plus OKF index.md files.

review.md is the point of the exercise: every entity, every relation, the
sentence it came from, and how confident the pass was — so the graph can be
checked without reading 188 files.

Usage: python3 scripts/review.py
"""
import collections, sys
from pathlib import Path
from urllib.parse import quote
import yaml

BUNDLE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from graphlib import load_graph
G = load_graph()
REL = yaml.safe_load((BUNDLE / "relations.yaml").read_text(encoding="utf-8"))
C = {c["id"]: c for c in G["concepts"]}

def path_of(c): return f"{c['kind']}/{c['id']}.md"
def title(t):   return C[t]["title"] if t in C else str(t)

def main():
    kinds = collections.defaultdict(list)
    for c in G["concepts"]:
        kinds[c["kind"]].append(c)

    # reverse index: every relation, both directions
    reverse = collections.defaultdict(lambda: collections.defaultdict(list))
    dangling = collections.Counter()
    n_rel = 0
    for c in G["concepts"]:
        for rel, targets in (c.get("relations") or {}).items():
            for t in targets:
                n_rel += 1
                if t not in C:
                    dangling[str(t)] += 1
                    continue
                inv = REL.get(rel, {}).get("inverse", rel)
                reverse[t][inv].append(c["id"])

    L = ["---", "type: reference", "title: Review",
         "description: Every entity, relation, and judgment call in the graph, with the evidence for each.",
         "status: draft", "---", "",
         "# Review", "",
         f"**{len(G['concepts'])} concepts, {n_rel} relations**, derived by reading "
         f"{sum(1 for c in G['concepts'] if c.get('source'))} source files in `~/praxia`. "
         "Source frontmatter was a hint, not an import; every field here came from the text.", "",
         "`confidence: stated` = asserted in the prose. `inferred` = deduced — check these first.", ""]

    inferred = [c for c in G["concepts"] if c.get("confidence") == "inferred"]
    # `unknown` means the source had no recap and nothing was invented. Sessions
    # are the ones worth chasing; the rest are prep files kept for coverage.
    unknown_sessions = [c for c in G["concepts"]
                        if c.get("confidence") == "unknown" and c["kind"] == "sessions"]
    coverage_only = [c for c in G["concepts"]
                     if c.get("confidence") == "unknown" and c["kind"] != "sessions"]

    L += ["## Open items", ""]
    if inferred:
        L.append(f"* **{len(inferred)} inferred** — deduced rather than stated: "
                 + ", ".join(f"[{c['title']}](world/{quote(path_of(c))})" for c in inferred))
    if unknown_sessions:
        L.append(f"* **{len(unknown_sessions)} sessions with no recap and no transcript** — "
                 "no description was written rather than guessing from prep notes: "
                 + ", ".join(sorted(c["title"] for c in unknown_sessions)))
    if not inferred and not unknown_sessions:
        L.append("*Nothing open.*")
    L += ["",
          "## Settled", "",
          f"* **{len(G['concepts']) - len(inferred) - len(unknown_sessions) - len(coverage_only)} "
          "concepts** are `stated` — asserted in the source text, with the sentence "
          "recorded in `evidence` wherever a relation needed defending.",
          f"* **{len(coverage_only)} prep and reference files** are carried for coverage "
          "with no summary invented for them. Not a gap: the vault text is the content.",
          "* Duplicate candidates, contradictions and unwritten entities: see "
          "[reconciliation.md](reconciliation.md).", ""]

    if dangling:
        L += ["", "### Named but not yet a concept", "",
              "They appear as plain text and become links the moment someone writes the page.", ""]
        for name, n in dangling.most_common(20):
            L.append(f"* {name} ({n} reference{'s' if n > 1 else ''})")
        L.append("")

    L += ["## Reverse index", "",
          "Each relation is stored once; these are the questions the other direction answers.", ""]
    for probe, label in [("enemy_of", "Who hates ___"), ("staffed_by", "Who works at ___"),
                         ("has_member", "Who belongs to ___"), ("contains", "What is inside ___")]:
        rows = []
        for tid, rels in sorted(reverse.items()):
            if probe in rels:
                rows.append(f"* **{title(tid)}** ← " + ", ".join(sorted(title(s) for s in rels[probe])))
        if rows:
            L += [f"### {label}", ""] + rows[:14] + [""]

    L += ["## Every concept", ""]
    for kind in sorted(kinds):
        L += [f"### {kind} — {len(kinds[kind])}", ""]
        for c in sorted(kinds[kind], key=lambda x: x["title"]):
            L.append(f"#### [{c['title']}](world/{quote(path_of(c))}) · `{c['type']}` · {c.get('confidence','—')}")
            if c.get("aka"):
                L.append(f"*Also:* {', '.join(c['aka'])}")
            if c.get("description"):
                L.append(f"{c['description']}")
            for rel, targets in (c.get("relations") or {}).items():
                lbl = REL.get(rel, {}).get("label", rel)
                L.append(f"* **{lbl}:** " + ", ".join(title(t) for t in targets))
                ev = (c.get("evidence") or {}).get(rel)
                if ev:
                    L.append(f"  > {ev}")
            L.append("")
    (BUNDLE / "review.md").write_text("\n".join(L), encoding="utf-8")

    # OKF index.md per directory + bundle root
    for kind in kinds:
        d = BUNDLE / "world" / kind
        lines = [f"# {kind}", ""]
        for c in sorted(kinds[kind], key=lambda x: x["title"]):
            lines.append(f"* [{c['title']}]({quote(c['id'])}.md) - {c.get('description','')}".rstrip(" -"))
        (d / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    root = ["---", 'okf_version: "0.2"', "---", "# praxia-recall", "",
            "* [README](README.md) - what this is, how to use it, how to rebuild it",
            "* [Review](review.md) - every entity, relation and judgment call, with evidence",
            "* [Reconciliation](reconciliation.md) - duplicates, contradictions, open items",
            "* [Timeline](timeline.md) - every dated concept in Praxian order",
            "* [Types](types.md) - the type taxonomy and the attribute vocabulary",
            "* [Relations](relations.yaml) - the relation vocabulary",
            "* [Calendar](calendar.yaml) - the Praxian calendar, derived from the vault",
            "* [Accepted](accepted.yaml) - reconciliation findings reviewed and dismissed",
            ""]
    for kind in sorted(kinds):
        root.append(f"* [{kind}](world/{kind}/) - {len(kinds[kind])} concept(s)")
    items = BUNDLE / "items" / "otter"
    if items.is_dir():
        n = sum(1 for p in items.rglob("*.md") if p.name != "index.md")
        root.append(f"* [transcripts](items/otter/) - {n} concept(s), Otter session recordings")
    (BUNDLE / "index.md").write_text("\n".join(root) + "\n", encoding="utf-8")

    print(f"review.md: {len(G['concepts'])} concepts, {n_rel} relations, "
          f"{len(inferred)} inferred, {len(dangling)} named-but-unwritten")

main()
