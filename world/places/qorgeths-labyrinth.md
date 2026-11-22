---
type: poi
title: Qorgeth's Labyrinth
description: A tunnel complex in the upper-left corner of Avernus, formerly the Darking
  Way, that passes under the River Styx and comes up beside Arkhan's Tower. The demon
  lord Qorgeth's Suffragans built it around a portal to his realm, meaning to move
  a demonic army by worm; the worms multiplied, collapsed tunnels and nested near
  the exit ramp. Its Styx-laden mud, ten Demonic Worms, Suffragan patrols, lost wanderers
  and cave-ins are the hazards; the note carries a 13-area key.
aka:
- The Darking Way
- qorgeths-labryinth
date: '2026-11-21'
praxian_date: 8 The Rotting 07 FR
praxian_date_basis: first_seen
located_in:
- Avernus
founded_by:
- Qorgeth
status: draft
generated:
  by: recall/claude-opus-5
  at: '2026-11-22T22:47:15Z'
  method: read-and-extract
sources:
- id: source
  resource: file:///Users/i.lurie/praxia/_sourcebooks/places/pois/qorgeths-labryinth.md
  title: 'Original: _sourcebooks/places/pois/qorgeths-labryinth.md'
content_hash: 795c1d30a26726bb
evidence:
  located_in: '''Qorgeth''s Labyrinth is a tunnel complex in the upper-left corner
    of Avernus. It passes under the River Styx, and its exit ramp (area 9) comes out
    right next to Arkhan''s Tower. It was formerly known as the Darking Way.'''
  founded_by: '''The demon lord Qorgeth launched an incursion into Avernus, using
    his Suffragans to build a complex around a portal to his realm.'' Qorgeth, the
    Suffragans and the Demonic Worms have no notes of their own; named but unwritten.'
  description: '''The worms multiplied, collapsed part of the tunnels, and set up
    a nest near the exit ramp''; ''Any creature not immune to the effects that spends
    more than two rounds in the mud is affected as if it were in the River itself'';
    ''There are ten Demonic Worms in the labyrinth''; ''Arkhan knows of the place
    but assumes it''s no threat, because Qorgeth and Tiamat are loosely allied.'''
confidence: stated
---

!qorgethslabryinth.png

Qorgeth's Labyrinth is a tunnel complex in the upper-left corner of [Avernus](/world/places/avernus.md). It passes under the River Styx, and its exit ramp (area 9) comes out right next to Arkhan's Tower. It was formerly known as the Darking Way.

## Origins

The demon lord Qorgeth launched an incursion into [Avernus](/world/places/avernus.md), using his Suffragans to build a complex around a portal to his realm.

The plan was to flood the tunnels from the River Styx, then use worms as slithering "subways" to move a demonic army quickly from the portal to the surface of Avernus.

It didn't go as planned. The worms multiplied, collapsed part of the tunnels, and set up a nest near the exit ramp. The Suffragans have been struggling to regain control of the project ever since.

## Hazards

The muddy floor of the passageways, laid down to ease the worms' passage, is laden with the magic of the River Styx. Any creature not immune to the effects that spends more than two rounds in the mud is affected as if it were in the River itself.

## Creatures

The labyrinth is populated mainly by the worms and the Suffragans. Lemures sometimes emerge from the muck at the bottom of the tunnels, and Hellwasps have built a nest in area 11.

Participants in the Blood War haven't found the entrances yet. Arkhan knows of the place but assumes it's no threat, because Qorgeth and [Tiamat](/world/people/tiamat.md) are loosely allied.


### Lost Creatures

There are also a few hapless creatures wandering the tunnels, lost after falling under the influence of the Styxian mud:

- [Earth elementals](https://www.dndbeyond.com/monsters/5194980-earth-elemental)
- A chaotic evil halfling assassin who doesn't remember their name or story. They're suspicious of the players and will run away at any opportunity
- Two suffragans who are wandering, lost (suffragans are undead, not demons)

### Bore Worms

Like the [DND Bore Worms](https://www.dndbeyond.com/monsters/183868-bore-worm) but huge, 100hp, and only 20 STR. They do less damage and aren't useful as cargo carriers.

### Demonic Worms

There are ten Demonic Worms in the labyrinth.

Demonic worms are monstrous hybrids created by exposing purple worms to demon ichor.  They are smaller, more intelligent, and more vicious than their cousins. Because of their demonic nature, they are unaffected by the River Styx or demon ichor.

The worms move around the built tunnels through their own burrows. They are carnivores and hunt continuously. When they burrow, they leave partially-collapsed tunnels behind. The players will come across soft mounts of dirt like mole hills. Those are where worms have tunneled down into the rock and dirt.

> You find a low, five-foot mound of soft earth. It's warm to the touch, as if recently turned over. It smells faintly of sulfur.

Worms will attempt to catch and kill their prey, then bring the corpses back to the hatchery in Area 8. This is a standard worm. Their young will burrow away and never attack:

```statblock
layout: Basic 5e Layout
name: Demonic Worm
size: huge
type: demon
ac: 15
hp: 250
speed: burrow 30 ft., walk 30 ft.
senses: Tremorsense 150 ft
languages: abyssal
damage_resistances: "bludgeoning, piercing, and slashing from nonmagical attacks"
damage_immunities: "poison, acid"
condition_immunities: "confused, charmed, frightened, grappled, poisoned, restrained"
stats: 
 - 27
 - 14
 - 25
 - 16
 - 15
 - 10
saves:
 - constitution: 14
 - strength: 18
actions:
- name:  Bite
  desc: _Melee Weapon Attack:_ +14 to hit, reach 10 ft., one target. _Hit:_ 22 (3d8 + 9) piercing damage. If the target is a Large or smaller creature, it must succeed on a DC 19 Dexterity saving throw or be swallowed by the worm. A swallowed creature is [blinded](https://www.dndbeyond.com/sources/dnd/free-rules/rules-glossary#BlindedCondition) and [restrained](https://www.dndbeyond.com/sources/dnd/free-rules/rules-glossary#RestrainedCondition), it has [total cover](https://www.dndbeyond.com/sources/basic-rules/combat#Cover) against attacks and other effects outside the worm, and it takes 21 (6d6) acid damage at the start of each of the worm's turns.|If the worm takes 30 damage or more on a single turn from a creature inside it, the worm must succeed on a DC 21 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, which fall [prone](https://www.dndbeyond.com/sources/dnd/free-rules/rules-glossary#ProneCondition) in a space within 10 feet of the worm. If the worm dies, a swallowed creature is no longer [restrained](https://www.dndbeyond.com/sources/dnd/free-rules/rules-glossary#RestrainedCondition) by it and can escape from the corpse by using 20 feet of movement, exiting [prone](https://www.dndbeyond.com/sources/dnd/free-rules/rules-glossary#ProneCondition).
- name: Constrict
  desc: The worm may constrict a grappled opponent, causing 3d10 crushing damage

```


## Random encounters

Every dungeon turn, roll a d6 and add it to the counter die. When the counter die reaches 20, roll 2d6.

1-2: 1d6 Lemures emerge from the muck and begin moaning. They increase the chances a partrol will show up.
3-4: A lost creature appears 
11-12: 1-2 worms explode from the ground and attack without hesitation

## Adversary roster

| Group          | Members                                                                                                                                                                                                                                                                                                                   | Starting Location | Movement    |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------- |
| Worms          | See Demonic Worms, above. Emerging worms may be preceded by frantically fleeing Suffragans.                                                                                                                                                                                                                               |                   | Random      |
| Patrols        | 6 Wormhearted Suffragans, but with +10 to hit on melee attacks, spell save DC 15. Patrols are hunting for worms and carry large bags of bait, in an effort to lure the worms back to the main tunnels. Groups may be beat up.                                                                                             | 2, 3, 4, 7, 13    | Patrolling  |
| Repair crews   | 1 [Bore Worm](https://www.dndbeyond.com/monsters/183868-bore-worm) plus 4 suffragans, plus [4 Duergar Warlords](https://www.dndbeyond.com/monsters/2560798-duergar-warlord) on 1 in 1d4                                                                                                                                   | 11, 12            | At location |
| Lost creatures |                                                                                                                                                                                                                                                                                                                           |                   | Random      |
| Qorgeth        | Only appears if players disturb the portal in area 10                                                                                                                                                                                                                                                                     | 10                | None        |
| Cave-ins       | The tunneling worms have rendered the entire area unstable. Roll 2d6. On a 10-11, the tunnel is partially collapsed, and the characters have to pick their way over rubble. On a 12, the tunnel collapses as they're moving through, risking that they fall into the mud or take 2d6 bludgeoning (DC 14 DEX save halves). |                   | Random      |
|                |                                                                                                                                                                                                                                                                                                                           |                   |             |


## Area key

1. Entryway
2. Patrol quarters
3. Patrol quarters
4. Patrol quarters
5. Large cave in
6. Workshop containing 1 broken bore worm, and 10 suffragans, all hard at work planning the next construction move. It also includes several broken platforms designed to attach to the back of the demonic worms, turning the worms into cargo carriers
7. The station platform. This is where the worms are supposed to pick up their cargo
8. Worm hatchery
9. Exit ramp. Emerges right next to Arkhan's Tower
10. The portal: Currently inactive, waiting for the suffragans to fix the damaged tunnels
11. Hellwasp nest, cave in and repair crew (mostly caught by hell wasps)
12. Cave in and repair crew
13. Patrol post

## Related
**Located in:** [Avernus](../places/avernus.md)
**Founded by:** Qorgeth
