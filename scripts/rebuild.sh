#!/bin/sh
# Rebuild praxia-recall from graph.yaml + the read-only source vault.
#   praxian_dates  -> graph-dates.yaml (in-world dates)
#   build      graph.yaml + graph-dates.yaml + source bodies -> world/
#   review     -> review.md, index.md files
#   timeline   -> timeline.md (Praxian chronology)
#   reconcile  -> reconciliation.md (duplicates, contradictions, unwritten)
#   validate   OKF conformance
set -e
cd "$(dirname "$0")/.."
python3 scripts/praxian_dates.py
python3 scripts/build.py
python3 scripts/review.py
python3 scripts/timeline.py
python3 scripts/reconcile.py
python3 "$HOME/.claude/skills/recall/scripts/validate.py" . --allow-broken-links | tail -1
