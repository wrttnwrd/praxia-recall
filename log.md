# Log

## 2026-09-08

- Otter ingest by recall/claude-fable-5-1 after the user approved the plan: 39 D&D session recordings (Aug 2024 to Sep 2026, 37 game nights) pulled read-only via the Otter MCP. Verbatim speaker transcripts written to `raw/otter/<YYYY-MM>/` (4.3 MB); one card per recording under `items/otter/<YYYY-MM>/` as the new `transcript` type, drafted from Otter's machine summaries, play content only, `status: draft`, `confidence: inferred`. 31 linked to a session concept by date (`about:`), 8 left unlinked (7 dates, one of them recorded in two parts) because no session note exists for that date; all listed in `otter-ingest-review.md`. Config: `otter` added to adapters in recall.yaml; `transcript` added under `# record` in types.md; `scripts/review.py` now keeps the `items/otter/` link in the root index across rebuilds. Month indexes written, root index regenerated, `views/graph.html` regenerated (610 concepts). Validate: 0 errors, 24 pre-existing warnings. Conformant.
- Aligned with the skill's bulk-outside-concepts layout rule. No files moved: concepts already live in `world/`, map images in `assets/maps/`, and the source vault stays outside behind `file://` URIs. Added a "Sharing it" section to README.md naming which folders to tick for a Claude Project GitHub sync, and a `.gitignore` for Finder and Python cache files. Validate and conformance unchanged (0 errors, 24 pre-existing warnings).

## 2026-09-05

- Rebuilt from graph.yaml: 562 concepts, 1456 relations, 286 source files.

## 2026-09-04

- Rebuilt from graph.yaml: 561 concepts, 1446 relations, 285 source files.

