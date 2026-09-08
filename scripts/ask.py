#!/usr/bin/env python3
"""Query the graph. Usage: python3 scripts/ask.py <relation> <entity-substring>"""
import sys, collections, yaml
from pathlib import Path
B = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from graphlib import load_graph
G = load_graph()
R = yaml.safe_load((B/"relations.yaml").read_text())
C = {c["id"]: c for c in G["concepts"]}
fwd = collections.defaultdict(lambda: collections.defaultdict(list))
rev = collections.defaultdict(lambda: collections.defaultdict(list))
for c in G["concepts"]:
    for rel, ts in (c.get("relations") or {}).items():
        for t in ts:
            fwd[c["id"]][rel].append(t)
            rev[t][R.get(rel,{}).get("inverse",rel)].append(c["id"])
def nm(t): return C[t]["title"] if t in C else str(t)
def find(q): return [i for i in C if q.lower() in C[i]["title"].lower() or q.lower() in i]
if __name__ == "__main__":
    rel, q = sys.argv[1], sys.argv[2]
    for i in find(q):
        hits = sorted(set(fwd[i].get(rel, []) + rev[i].get(rel, [])))
        if hits:
            print(f"{C[i]['title']} — {R.get(rel,{}).get('label',rel)}: " + ", ".join(nm(h) for h in hits))
