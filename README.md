---
type: reference
title: README
description: What this bundle is, how it was built, and how to use it.
status: stable
---

# praxia-recall

A queryable knowledge bundle for the world of **Praxia**, in
[Open Knowledge Format](https://github.com/GoogleCloudPlatform/open-knowledge-format)
v0.2. It was built by *reading* the Obsidian vault at `~/praxia` — not by
mapping its frontmatter — and every assertion carries the sentence it came from.

**The source vault is read-only.** Nothing here ever writes to `~/praxia`.

## Start here

| File | What it is |
|---|---|
| [index.md](index.md) | The bundle root; links to everything |
| [review.md](review.md) | Every entity, every relation, the evidence for each, and what is still open |
| [timeline.md](timeline.md) | Every dated concept in Praxian chronological order |
| [reconciliation.md](reconciliation.md) | Duplicate candidates, contradictions, unwritten entities |
| [types.md](types.md) | What a concept can *be*, and the attribute vocabulary |
| [relations.yaml](relations.yaml) | What a concept can *do* — the verbs of the graph, with inverses |
| [calendar.yaml](calendar.yaml) | The Praxian calendar, derived from session dates |

Concepts live under `world/`, grouped by kind: `people`, `places`, `groups`,
`things`, `events`, `vehicles`, `sessions`, `lore`.

## How to read a concept

```yaml
type: poi                     # what it is (types.md)
title: The Green Slaad
description: ...              # one sentence
species: half-orc             # closed-set attributes are plain fields
located_in: [Hull Ward]       # relations, one per verb
owned_by: [Armak Rockfist]
praxian_date: 23 Stormclaw 07 FR
praxian_date_basis: first_seen   # occurred | founded | first_seen
confidence: stated            # stated | inferred | unknown
evidence:                     # the sentence the relation came from
  owned_by: "'The Green Slaad is now owned by Armak Rockfist...'"
```

Then the source prose, then a `## Related` block of typed links.

Three things worth knowing:

- **`confidence`** — `stated` means the text asserts it. `inferred` means it was
  deduced and should be checked. `unknown` means the source had no recap and
  nothing was invented.
- **`praxian_date_basis`** — `first_seen` is the record's first sight of
  something, *not* when it began to exist.
- **Relations are recorded once, in one direction.** "Who works at the Green
  Slaad" is answered by scanning `works_at`, not by a staff list on the tavern.
  One direction of truth means two facts can never contradict each other.

## Asking it questions

```sh
python3 scripts/ask.py <relation> <entity>

python3 scripts/ask.py enemy_of thargorax      # who hates Thargorax
python3 scripts/ask.py staffed_by "green slaad"  # who works there
python3 scripts/ask.py has_member "order of light"
python3 scripts/ask.py contains aventine
```

Relations work in both directions — `ask.py` walks the inverse from
`relations.yaml` automatically. The reverse index is also written out in
`review.md`.

## Rebuilding

```sh
./scripts/rebuild.sh
```

Runs: `praxian_dates` → `build` → `review` → `timeline` → `reconcile` →
`validate`. It clears and regenerates `world/` every time.

**`world/` is derived output. Never hand-edit it.** Corrections go to
`graph.yaml`; facts about the world go to `~/praxia`, and are picked up on the
next rebuild.

| Script | Does |
|---|---|
| `build.py` | `graph.yaml` + source bodies → `world/` |
| `praxian_dates.py` | derives in-world dates → `graph-dates.yaml` |
| `review.py` | `review.md` and every `index.md` |
| `timeline.py` | `timeline.md` |
| `reconcile.py` | `reconciliation.md` |
| `ask.py` | query the graph |

## Editing the graph

`graph.yaml` is append-only. A later entry with the same `id` **merges** into
the earlier one — scalars overwrite, relation and evidence maps union — so a
correction never rewrites what it corrects, and the history of a fact stays
readable. Three directives:

```yaml
- id: pop
  remove_relations: {enemy_of: [artemis-hasp]}   # unsay a relation
- id: draknev
  retired_into: drak                             # fold a duplicate; edges repoint
- id: aventine
  praxian_date: "-400 FR"                        # a stated date beats a derived one
```

## Reading it in Obsidian

Open this folder as its own vault, then set:

- Files & Links → **Use Wikilinks: OFF** (OKF uses markdown links)
- Files & Links → New link format: **Absolute path in vault**
- Editor → **Properties in document: Visible**

Dataview works well against the frontmatter, e.g.
`TABLE species, alignment FROM "world/people" WHERE type = "npc"`.

## Sharing it

The bundle keeps its bulk outside the concept tree, so the readable part can be
shared on its own. `world/` is about 3 MB of concepts; `assets/maps/` is about
19 MB of images that the map concepts link to. To load this bundle into a Claude
Project from a GitHub sync, tick `world/`, `index.md`, `README.md`, `types.md`,
`relations.yaml`, `timeline.md` and `review.md`, and leave `assets/`, `scripts/`
and the YAML build inputs unticked. The source vault at `~/praxia` is never
part of the bundle; concepts point back at it with `file://` URIs.

## What it does not claim

Conformance is structural: every file parses and is typed. It says nothing
about whether the world facts are right. `review.md` and `reconciliation.md`
exist so those can be checked separately — and the open items are listed there
rather than hidden.
