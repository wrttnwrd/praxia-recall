---
type: reference
title: Types
description: The type taxonomy — what a concept IS. Parents and their subtypes.
status: draft
---

# Types

Governs the `type:` field. There is no tag layer in this bundle. Individuals never appear here: Aventine is
not a type, it is a `city` concept with a page. Relations live in `relations.yaml`.

# place

- world — the world itself
- region — a continent, range, or broad area
- nation — a polity with a government
- city — a settlement with its own internal geography
- district — a named quarter or ward within a city
- poi — a named point of interest: tavern, shop, ruin, landmark
- temple — a place of worship
- plane — a plane of existence

# being

- pc — a player character
- npc — a named individual run by the GM
- deity — a god, demigod, or aspect of one
- creature — a monster or beast

# group

- party — an adventuring company of PCs
- house — one of the great houses
- guild — a trade or criminal guild
- organization — any other standing body
- cult — a religious following of a single power
- temple — an order attached to a place of worship
- pantheon — a group of gods treated as one body

# vehicle

- airship — a flying vessel, named and crewed
- ship — a waterborne vessel

# thing

- item — an object, mundane or magical
- arcana — a spell, ritual, or magical artefact

# event

- event — something that happened at a time and place

# prep

Material written for play but not itself a record of play: dungeon rooms,
puzzles, encounter notes, GM planning. Kept separate from `record` so that
what was *prepared* is never mistaken for what *happened*.

- adventure-note — unplayed material for a specific arc

# media

A concept *about* an asset. OKF bundles hold markdown only (§4.1, §6.2), so the
image is never itself a concept: the concept carries `resource:`, a URI pointing
at the original, and a downsampled thumbnail for reading in place.

- map — a map, plan or floorplan

# rules

House rules and mechanics — not tied to any one arc, and not world facts.

- rule — a house rule or mechanic
- glossary — a terms list

# record

- session — a record of a session played (the recap)
- transcript — a verbatim recording of a session as captured (Otter); the
  session concept is the recap, the transcript is the evidence behind it
- storyline — an arc spanning sessions
- reference — lore, notes, and other written material

# Attributes

Not types — closed-set properties recorded as plain frontmatter fields on the
concepts that have them, in the same shape the source vault uses.

`species:` — human, dwarf, elf, gray-elf, half-elf, half-orc, half-ogre,
halfling, gnome, goblin, goliath, orc, tiefling, dragonborn, aasimar,
aaracocra, tabaxi, tortle, giff, kenku, beholder, bugbear, gnoll, vampire,
werebear, green-abishai, sicaari.

`alignment:` — lawful-good, lawful-neutral, lawful-evil, neutral-good,
true-neutral, neutral-evil, chaotic-good, chaotic-neutral, chaotic-evil.

The vault writes alignment eleven different ways. These are the shorthands it
uses, recorded here so a future ingest can fold them correctly:

    LG = lawful-good      LN = lawful-neutral    LE = lawful-evil
    NG = neutral-good     NE = neutral-evil
    CG = chaotic-good     CN = chaotic-neutral   CE = chaotic-evil
    N, TN, Neutral        = true-neutral
    "Lawful" alone        = ambiguous; left unmapped
