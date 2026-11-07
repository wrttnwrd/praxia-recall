---
type: reference
title: Otter ingest review
description: Every Otter recording ingested as a transcript concept, how it was matched to a session, and what still needs a human decision.
status: draft
generated: { by: recall/claude-fable-5-1, at: 2026-09-08T13:11:07-07:00 }
---

# Otter ingest review

39 recordings from Otter were ingested on 2026-09-08 as `transcript` concepts, and two more (21 Sep and 5 Oct 2026) on 2026-11-07, under `items/otter/`, with verbatim text under `raw/otter/`. Cards were drafted from Otter's machine summaries, play content only; the transcripts were saved but not read in full, so every card is `status: draft`, `confidence: inferred`. Nothing is marked verified.

## How matching worked

A recording is linked (`about:`) to the session concept whose ID carries the same date, or a date one day off where the concept's own `date` field agrees. Where two session files share a date, the first is linked and the second noted. Recordings with no session concept on their date are left unlinked and listed below as a to-write queue.

## Matches

| Recording | Length | Match | Session concept |
|---|---|---|---|
| [2024-08-05-rbg-part1](/items/otter/2024-08/2024-08-05-rbg-part1.md) | 1h 42m | exact | [029-08-05-2024-rbg](/world/sessions/029-08-05-2024-rbg.md) |
| [2024-08-05-rbg-part2](/items/otter/2024-08/2024-08-05-rbg-part2.md) | 1h 9m | exact | [029-08-05-2024-rbg](/world/sessions/029-08-05-2024-rbg.md) |
| [2024-09-02-rbg](/items/otter/2024-09/2024-09-02-rbg.md) | 1h 42m | exact | [031-09-02-2024-rbg](/world/sessions/031-09-02-2024-rbg.md) |
| [2024-09-16-rbg-part1](/items/otter/2024-09/2024-09-16-rbg-part1.md) | 1h 36m | none | — |
| [2024-09-16-rbg-part2](/items/otter/2024-09/2024-09-16-rbg-part2.md) | 1h 39m | none | — |
| [2025-01-06-rbg](/items/otter/2025-01/2025-01-06-rbg.md) | 2h 49m | adjacent-day | [033-01-05-2025-rbg](/world/sessions/033-01-05-2025-rbg.md) |
| [2025-01-20-rbg](/items/otter/2025-01/2025-01-20-rbg.md) | 2h 46m | exact | [034-01-20-2025-rbg](/world/sessions/034-01-20-2025-rbg.md) |
| [2025-02-17-rbg](/items/otter/2025-02/2025-02-17-rbg.md) | 3h 1m | none | — |
| [2025-03-03-rbg](/items/otter/2025-03/2025-03-03-rbg.md) | 2h 27m | exact | [035-03-03-2025-rbg](/world/sessions/035-03-03-2025-rbg.md) |
| [2025-03-17-rbg](/items/otter/2025-03/2025-03-17-rbg.md) | 2h 23m | exact | [036-03-17-2025-rbg](/world/sessions/036-03-17-2025-rbg.md) |
| [2025-03-31-rbg](/items/otter/2025-03/2025-03-31-rbg.md) | 2h 3m | exact | [037-03-31-2025-rbg](/world/sessions/037-03-31-2025-rbg.md) |
| [2025-04-14-rbg](/items/otter/2025-04/2025-04-14-rbg.md) | 2h 53m | exact | [038-04-14-2025-rbg](/world/sessions/038-04-14-2025-rbg.md) |
| [2025-05-26-rbg](/items/otter/2025-05/2025-05-26-rbg.md) | 2h 53m | exact | [039-05-26-2025-rbg](/world/sessions/039-05-26-2025-rbg.md) |
| [2025-06-09-rbg](/items/otter/2025-06/2025-06-09-rbg.md) | 3h 11m | exact | [040-06-09-2025-rbg](/world/sessions/040-06-09-2025-rbg.md) |
| [2025-06-23-rbg](/items/otter/2025-06/2025-06-23-rbg.md) | 2h 32m | exact | [041-06-23-2025-rbg](/world/sessions/041-06-23-2025-rbg.md) |
| [2025-07-07-rbg](/items/otter/2025-07/2025-07-07-rbg.md) | 3h 1m | exact | [042-07-07-2025-rbg](/world/sessions/042-07-07-2025-rbg.md) |
| [2025-07-21-rbg](/items/otter/2025-07/2025-07-21-rbg.md) | 2h 53m | exact | [043-07-21-2025-rbg](/world/sessions/043-07-21-2025-rbg.md), [044-07-21-2025-rbg](/world/sessions/044-07-21-2025-rbg.md) |
| [2025-08-18-rbg](/items/otter/2025-08/2025-08-18-rbg.md) | 3h 3m | exact | [045-08-18-2025-rbg](/world/sessions/045-08-18-2025-rbg.md) |
| [2025-09-01-rbg](/items/otter/2025-09/2025-09-01-rbg.md) | 2h 55m | exact | [046-09-01-2025-rbg](/world/sessions/046-09-01-2025-rbg.md) |
| [2025-09-29-rbg](/items/otter/2025-09/2025-09-29-rbg.md) | 2h 59m | exact | [047-09-29-2025-rbg](/world/sessions/047-09-29-2025-rbg.md) |
| [2025-10-13-rbg](/items/otter/2025-10/2025-10-13-rbg.md) | 2h 35m | exact | [048-10-13-2025-rbg](/world/sessions/048-10-13-2025-rbg.md) |
| [2025-11-10-rbg](/items/otter/2025-11/2025-11-10-rbg.md) | 2h 53m | exact | [049-11-10-2025-rbg](/world/sessions/049-11-10-2025-rbg.md) |
| [2025-11-24-rbg](/items/otter/2025-11/2025-11-24-rbg.md) | 2h 48m | exact | [050-11-24-2025-rbg](/world/sessions/050-11-24-2025-rbg.md) |
| [2025-12-08-rbg](/items/otter/2025-12/2025-12-08-rbg.md) | 2h 55m | none | — |
| [2025-12-22-rbg](/items/otter/2025-12/2025-12-22-rbg.md) | 2h 39m | exact | [051-12-22-2025-rbg](/world/sessions/051-12-22-2025-rbg.md) |
| [2026-01-05-rbg](/items/otter/2026-01/2026-01-05-rbg.md) | 3h 2m | exact | [052-01-05-2026-rbg](/world/sessions/052-01-05-2026-rbg.md) |
| [2026-01-26-rbg](/items/otter/2026-01/2026-01-26-rbg.md) | 3h 3m | exact | [053-01-26-2026-rbg](/world/sessions/053-01-26-2026-rbg.md) |
| [2026-02-02-rbg](/items/otter/2026-02/2026-02-02-rbg.md) | 2h 36m | none | — |
| [2026-02-11-rbg](/items/otter/2026-02/2026-02-11-rbg.md) | 1h 2m | none | — |
| [2026-02-16-rbg](/items/otter/2026-02/2026-02-16-rbg.md) | 2h 55m | adjacent-day | [054-02-15-2026-rbg](/world/sessions/054-02-15-2026-rbg.md) |
| [2026-03-16-rbg](/items/otter/2026-03/2026-03-16-rbg.md) | 2h 27m | exact | [055-03-16-2026-rbg](/world/sessions/055-03-16-2026-rbg.md) |
| [2026-04-13-rbg](/items/otter/2026-04/2026-04-13-rbg.md) | 3h 2m | none | — |
| [2026-05-11-rbg](/items/otter/2026-05/2026-05-11-rbg.md) | 2h 58m | exact | [056-05-11-2026-rbg](/world/sessions/056-05-11-2026-rbg.md) |
| [2026-05-25-rbg](/items/otter/2026-05/2026-05-25-rbg.md) | 1h 56m | exact | [057-05-25-2026-rbg](/world/sessions/057-05-25-2026-rbg.md) |
| [2026-06-08-rbg](/items/otter/2026-06/2026-06-08-rbg.md) | 2h 54m | none | — |
| [2026-06-22-rbg](/items/otter/2026-06/2026-06-22-rbg.md) | 2h 44m | exact | [058-06-22-2026-rbg](/world/sessions/058-06-22-2026-rbg.md) |
| [2026-07-13-rbg](/items/otter/2026-07/2026-07-13-rbg.md) | 3h | exact | [059-07-13-2026-rbg](/world/sessions/059-07-13-2026-rbg.md) |
| [2026-08-17-rbg](/items/otter/2026-08/2026-08-17-rbg.md) | 2h 55m | exact | [060-08-17-2026-rbg](/world/sessions/060-08-17-2026-rbg.md) |
| [2026-09-07-rbg](/items/otter/2026-09/2026-09-07-rbg.md) | 3h 4m | exact | [061-09-07-2026-rbg](/world/sessions/061-09-07-2026-rbg.md) |
| [2026-09-21-rbg](/items/otter/2026-09/2026-09-21-rbg.md) | 2h 23m | none | — |
| [2026-10-05-rbg](/items/otter/2026-10/2026-10-05-rbg.md) | 2h 59m | exact | [062-10-05-2026-rbg](/world/sessions/062-10-05-2026-rbg.md) |

## No session concept on the recording's date

These sessions were played and recorded but have no note in the vault. Writing them is the natural next step; each card carries a summary to start from.

- 2024-09-16 (1h 36m): [2024-09-16-rbg-part1](/items/otter/2024-09/2024-09-16-rbg-part1.md) — First half of 16 Sep 2024: a dungeon crawl beneath the island, a secret door, a drow and a bug-like creature, and the load-bearing crystals.
- 2024-09-16 (1h 39m): [2024-09-16-rbg-part2](/items/otter/2024-09/2024-09-16-rbg-part2.md) — Second half of 16 Sep 2024: Dura rescued, Morwena destroyed by fireball, the island's crystals explained, and the party reaches level 13.
- 2025-02-17 (3h 1m): [2025-02-17-rbg](/items/otter/2025-02/2025-02-17-rbg.md) — A bar brawl with shadar-kai and the dealer Felbro, an interrogation that names Malachi and Kazani Noctis, and a portal in the temple of Shar.
- 2025-12-08 (2h 55m): [2025-12-08-rbg](/items/otter/2025-12/2025-12-08-rbg.md) — The Battle of Urdun concludes: sahuagin, a High Priestess and a Deep Diver defeated, a rescue on the Albion's deck, and the ship mysteriously repaired.
- 2026-02-02 (2h 36m): [2026-02-02-rbg](/items/otter/2026-02/2026-02-02-rbg.md) — The dragon fight goes wrong: Nilthrax and the red dragon Urush Gûl, Drak taken captive, and heavy fire damage all round.
- 2026-02-11 (1h 2m): [2026-02-11-rbg](/items/otter/2026-02/2026-02-11-rbg.md) — Solo interlude for Drak: captive in Urush Gûl's crater, the dragon's terms, and release under scrying.
- 2026-04-13 (3h 2m): [2026-04-13-rbg](/items/otter/2026-04/2026-04-13-rbg.md) — Robbing the necromancer Obaris: bone hands, a brain in a jar, a six-second kill, and a library of loot.
- 2026-06-08 (2h 54m): [2026-06-08-rbg](/items/otter/2026-06/2026-06-08-rbg.md) — A skull-eyed tree and its blights, a soul contract naming Vanity Luck, a standoff with Anthraxis, and the party takes roles to move civilians through the fighting.
- 2026-09-21 (2h 23m): [2026-09-21-rbg](/items/otter/2026-09/2026-09-21-rbg.md) — Bitter guides the party out of Bel's forge; orthon sniper killed, Urush Gûl decoyed, the Wandering Emporium sighted, Bitter killed by a bone storm, abishai dive in. The 028 note's 'Recap (9/21)' section describes this night.

## Judgment calls

- 2025-07-21: two session files carry this date (043 and 044). The recording is linked to 043, matching the earlier graph build.
- 2024-09-02 and 2024-09-30: session 032 carries `date: 2024-09-02` in its frontmatter but ID date 09-30. The 2 Sep recording is linked to 031 by ID date only.
- 2025-01-06 and 2026-02-16: linked to concepts whose ID date is one day earlier (033, 054) because the concept's own date field matches the recording.
- Speaker names are Otter's display labels (players' Zoom names, often in-character jokes). They are recorded as `participants` verbatim and not resolved to characters.
- Two nights (2024-08-05, 2024-09-16) were recorded in two parts; each part is its own concept, both linked to the same session.
- 2026-02-11 is a one-player interlude (Drak captive) rather than a full session.
- 2026-07-13: the recording also contains a real-world discussion about a player leaving the group. Excluded from the card by rule; it is in the raw transcript.
- 2026-09-21: no note of its own, but the 7 Sep note carries a 'Recap (9/21)' section. Left unlinked by the date rule; the card's Related block points at that recap. Only two Otter speaker labels were names on this recording; the rest were 'Speaker N' and are not listed as participants.
- 2026-10-05: a hand-pasted Otter export of the same recording had been committed to `raw/otter/2026-10/` earlier on 2026-11-07 in Otter's web format. It was replaced with the MCP transcript in the bundle's timestamped format so every raw file reads the same; the previous version is in git history.
