---
type: rule
title: Hexploration
description: 'A hexcrawl ruleset for 5th Edition kept with the random rules: 24-mile
  world hexes and 3-mile regional hexes, travel speeds and terrain modifiers, navigation
  checks and getting lost, the wilderness day and forced marches, downtime activities
  and jobs, permanent injuries in place of death, and excursion resting. Third-party
  text copied into the vault, not Praxia lore.'
status: draft
generated:
  by: recall/claude-opus-5
  at: '2026-11-07T17:43:53Z'
  method: read-and-extract
sources:
- id: source
  resource: file:///Users/i.lurie/praxia/_sourcebooks/random-rules/Hexploration.md
  title: 'Original: _sourcebooks/random-rules/Hexploration.md'
content_hash: 55ab5f1268a6b8bd
evidence:
  description: '''Hexploration is a simple ruleset to run hexcrawls in 5th Edition.
    In here you''ll find guidance on World Maps, Regional Maps, Exploring Hexes, Downtime
    Jobs, Rolling for Weather, and Rolling for Random Encounters.'''
confidence: stated
---

# Hexploration

> By layering a hex grid over a map you’ve created, you can convert distances into measurements of time. This allows you, the GM, to quickly determine how long any given journey will take.
> When players ask how far they are from their destination, you can simply count the hexes.

Hexploration is a simple ruleset to run hexcrawls in 5th Edition. In here you’ll find guidance on World Maps, Regional Maps, Exploring Hexes, Downtime Jobs, Rolling for Weather, and Rolling for Random Encounters.

#### The Two Scales
In Hexploration, maps are sorted into two categories of scale:

* World maps have 24-mile hexes.
* Regional maps have 3-mile hexes.

#### Travel Speed
Regardless of the map scale, a character or a party of characters, travelling on foot in ideal conditions, can move at a speed of up to 3 miles per hour, or a total of 24 miles over an 8-hour day. 

- 2 miles/hour / 16 miles per day: Stealth, lower chance of surprise
- 3 miles/hour / 24 miles per day: Standard, no stealth
- 4 miles/hour / 32 miles per day: Passive perception -4, no stealth


## World Map
> On the world map, one hex is 24 miles across.
  
The world map scale is ideal for calculating travel time for long journeys. It doesn’t have to be a map of the whole world, just a large area.

***It’s Just Reference.*** This scale is typically best used to offhandedly solve the math of travel time over longer distances, quickly and easily. If you want something more granular, take a look at the Regional Map.

***Dangers on the Way.*** Instead of using Random Encounters, if you wish to make the journey take more time, consider building an exciting encounter and make it take place at an interesting point on the route to the destination.

***Timeskip The Journey.*** Journeys of this length are usually best skimmed over, only stopping to highlight settlements or points of interest. Travel is the focus here, rather than exploration. 

> “You all set off for Blackguard. Four days later,    you see the Obsidian Palace over the horizon.”

#### Travelling as a Party
Use the following measurements and modifiers to adjudicate travel times on the world map for a character or a party of characters.

***Along a Road.*** Entering a road hex on foot takes a day’s march.

***On Horseback.*** Entering hills, plains, or road hexes on horseback takes half as long as walking.

***Trackless Wilderness.*** Entering a hex with no roads or meaningful tracks takes twice as long.

***Difficult Terrain.*** Entering a forest, mountain, or swamp hex takes twice as long.

#### Stack Modifiers
If multiple factors are modifying your travel time, stack those modifiers together to get the final result. For example, if you enter a trackless wilderness in a mountain hex, you double the travel time twice. So,  it takes 4 days to enter that hex. Or, if you enter a trackless wilderness hills hex on horseback, it takes 1 day to enter the hex.

#### Travel in a Vehicle
Use the following measurements and modifiers to determine travel times on the world map for a vehicle that can be operated day and night for more efficient travel.

***Rowboats and Keelboats.*** Move 1 hex in a day.
***By Galley.*** Moves 4 hexes in a day.
***By Ship.*** Moves 5 hexes in a day.
***By Airship.*** Moves 8 hexes in a day.
***By Train.*** Moves 1 hex in an hour.

## Regional Map
On the regional map, one hex is 3 miles across.
  
When the players enter a region worth exploring in detail, GMs might move them onto a new map: this is the regional map. This more granular approach allows you to break down travel and exploration into finer chunks. All travel on this scale is measured in hexes and hours. 

***No Fractions.*** There’s no such thing as traveling half a hex or for half an hour. You always move in whole increments.

***Create Features.*** Somewhere between a tenth and a third of the hexes on a regional map should contain a feature of some kind. It doesn’t have to be a dungeon, but there might be landmarks, or other points of interest. This can be a useful tool for navigation and orientation when a party inevitably gets lost, or perhaps a clue to the location of a dungeon. 

***Mounted Travel.*** A party on horseback moves twice as fast when entering a road, plains or hills hex.

> A distance of 3 miles can be referred to as a League. By referring to your hexes as leagues, the players and GM can give themselves a way to talk about hexes in character.

### Creating a Regional Map
To create and use a regional map, start with a simple grid of hexes. Choose a terrain type for each hex, fill around half the hexes with some features, then do as much decorating as you want. This will be the GM’s version of the regional map.

***Features.*** A feature could be a settlement, a ruin, a dungeon, or just a point of interest. Make a simple list of ideas to start, then create more detailed content your players explore closer.

***Terrain.*** A terrain denotes how tricky the hex is to explore. The terrain types are forest, swamp, mountain, plains, or hills hex.

#### The Empty Map
Once the GM has created their version of the regional map with all the details, they can then create a second version with only obvious or known landmarks drawn in. These could be mountains or large monuments that are either common knowledge or just visible from a distance.
The GM then leaves all the other hexes blank for their players to discover.

#### Filling in the Map
As players explore the wilderness, they’ll draw their own version of the regional map by filling in the empty hexes they’ve explored with their own symbols for features and terrains.

This process will inevitably inspire more play, as most players tend to find filling in the map to be a deeply satisfying experience. 

### Entering a Hex
Travel along the regional map begins by leaving your current hex and entering an adjacent hex.

#### Determining Time
How long it takes to enter a hex is determined by the hex’s terrain type. See the Hexes by Type table.

#### Navigating the Wilderness
To enter a forest, swamp, or mountain hex, the player leading the party’s exploration must make a navigation check. This is usually a Wisdom (Survival) check, but it could be any other skill the GM deems to be relevant.

***Setting the DC.*** The GM determines the check’s difficulty class by selecting a number between 10 and 20 based on the surrounding hexes.
If the adjacent hexes all share the same terrain type, you can make the check more difficult by increasing the DC.
If landmarks are visible, you can make the check easier by reducing the DC.
***Automatic Success.*** When the party is travelling along a reliable route, like following a river, you could chose to have the player automatically succeed any checks made.

#### Inside the Hex
When the party enters a hex, they learn the following things:

- The terrain and features of this hex.
- The terrain of adjacent hexes.
- Features in adjacent hexes that would be visible from a distance, such as structures.
- Whether or there is obviously something to discover here by searching this hex.

#### Trailblaze
Once you’ve entered a hex by making a successful navigation check, you automatically succeed on all future navigation checks made to enter that hex.

#### Getting Lost
When a player fails a navigation check, they lead the party into an adjacent hex before realizing that they’re lost. 
While lost, the party can continue travelling but the GM should not confirm their location on the map again until they’ve confidently reoriented themselves by navigating to a previously explored hex or a known feature, or by some other means the GM deems appropriate.

### Searching a hex
To search a hex, the party spends time determined by the Hex’s Type, see the Hexes by Type table. When the search is completed, the party learns about any hidden features present in the hex.

### Wilderness Day
A full 24-hour day in the wilderness generally consists of the following phases.

***Rolling for Weather.*** The GM rolls for weather and determines any applicable modifiers to the day’s checks.

***Exploring.*** The party spends 8 hours traveling between hexes, resolving encounters and exploring features.

***Camping.*** The party spends four hours setting up camp at their destination, relaxing, unwinding, and planning their next day. During this phase, every character must consume one ration or an equivalent amount of food.

***Rest.*** Every character rests for 8 hours.

***Downtime.*** Any unused hours can be used in-between the other phases for downtime activities.

#### Forced March
Whenever a party finishes entering or searching a hex, if they have spent more than 8 hours exploring that day, tally up the additional hours spent and ask each character in the party to make a marching check.

***Marching Checks.*** Constitution Saving Throw, DC 10 + 1 for each hour spent past 8. Each character that fails suffers one level of exhaustion.

## Campaign Rules
You can use the additional campaign rules presented in this section to bring a long-term Hexploration campaign to life.

### Downtime Activities
At the end of each day, most parties will find themselves with around 4 hours for downtime activities. Unused time from the rest of the day can be used to gain additional downtime, to a maximum of 8 hours total.

You can do the following with your downtime:

#### Craft a Magic Item
You spend your downtime crafting a magic item. You reduce the item’s remaining crafting time by the hours you spend on it. 

#### Craft a Mundane Item
You spend your downtime crafting a mundane item. You reduce the item’s remaining crafting time by the hours you spend on it. 

#### Craft a Healing Potion
You spend four hours creating a potion. You grind a Honeymint Herb into powder with a mortar and pestle and make a DC 15 Wisdom (Survival) check.  On a success, you create a Potion of Healing.

#### Forage for Food
You spend  four hours foraging. Roll a Wisdom (Survival) check. A result of 10 provides you with enough food to forego the use of one ration today. Each increment of 5 above that allows you to forego an additional ration. You can spend two hours foraging instead. If you do, make the check with disadvantage.

#### Forage for Honeymint
You spend four hours foraging for herbs while in a forest hex. Make a DC 15 Wisdom (Survival) check.  On a success, you find one Honeymint Herb.

#### Other Activity
You can spend your downtime doing another activity, such as scouting ahead, setting up traps or bells to reduce the chance of a random encounter. You could also use this downtime for activities built into your class, such as a wizard writing new spells in their spellbook, or scribing scrolls.

### Downtime Jobs
Any activity can be turned into a downtime activity by creating a downtime job out of it. To create a downtime job, the GM determines the job’s reward, the difficulty of making breakthroughs, required hours to complete the job, cost of required materials, and any prerequisites.

***Prerequisite.*** A character cannot make progress on a task unless they meet the prerequisite.
***Required Hours.*** Players track the hours they spend on a job. When they meet or exceed the required hours, they get the job’s reward. 
***Breakthrough.*** Whenever a character spends 8 consecutive hours working on a job, they can roll for a breakthrough, using an ability check the GM deems appropriate for the job. On a success, they gain an additional 8 hours of progress.

#### Learn a Language
Prerequisite: You’re being tutored by someone with proficiency in the language you’re studying. 
Reward: You learn a new language.

Breakthrough DC: 20		Hours: 100

#### Train with a Weapon or Armor
Prerequisite: You’re being tutored by someone with proficiency in the weapon or armor you’re studying.
Reward: You gain proficiency with a specific weapon or a specific armor.

Breakthrough DC: 20		Hours: 200

#### Gain a Skill Proficiency
Prerequisite: You’re being tutored by someone with proficiency in the skill you’re studying. 
Reward: You gain proficiency in a skill.

Breakthrough DC: 20		Hours: 800

#### Overcome a Permanent Injury
Prerequisite: Vary based on the nature of the injury.
Reward: You’ve learned to overcome the mechanical effects of your permanent injury.

Breakthrough DC: 20		Hours: 150

#### Write a Book
Prerequisite: You have a book to write in. 
Reward: You write a book and have advantage on checks related to the specific subject of the book.

Breakthrough DC: 15		Hours: 60

### Permanent Injury
When a character would otherwise die, the GM might decide to give the character a Permanent Injury instead.
***Tutorial Levels.*** A group might agree to use these rules during the lower levels of a campaign to compensate for the deadly nature of low level play in 5th edition.
When the party reaches 5th level, you can return to running death as normal.

#### Bad Shoulder
Your shoulder hinders quick movement. You have disadvantage on Dexterity saving throws.

#### Cracked Ribs
Your ribs hurt when you run. When you take the Dash action, you take 1d6 piercing damage.

#### Fractured Skull
Your mind fails you at the worst of times. You have disadvantage on Wisdom saving throws.

#### Irregular Heart
Your heart can skip a beat. You have disadvantage on Constitution saving throws.

#### Limping
Your leg isn’t what it used to be. Your speed is reduced by 5 feet.

#### One-Eyed
You’re missing an eye. You have disadvantage on attack rolls against targets beyond 30 feet.

#### Phantom Pain
Your wound keeps acting up. When you take damage, you take 1d6 extra damage of the same type.

#### Spinal Injury
Your spine buckles under pressure. Your carrying capacity is halved.

#### Trauma
You startle easily. You have disadvantage on initiative rolls.

#### Tremors
Your hands won’t stop shaking. You have disadvantage on attack rolls that don’t use Strength.

### Excursion Resting
Excursion resting is an alternative set of resting rules. The following rules replace the Short Rest and Long Rest rules in the Rules Glossary.

#### Taking A Rest
A rest is a period of extended downtime—at least 8 hours—available to any creature. During a Rest, you sleep for at least 6 hours and perform no more than 2 hours of light activity, such as reading, talking, eating, or standing watch. During sleep, you are unconscious. After you finish a rest, you must wait at least 16 hours before starting another one.

***Interrupting the Rest.*** Any rest is stopped by the following interruptions:

- Rolling initiative
- Casting a spell other than a cantrip
- Taking any damage

You can resume a rest immediately after an interruption. If you do so, the rest requires 1 additional hour per interruption to finish.

***Benefits of the Rest.*** The benefits of the rest change depending on if it was a night’s rest or a good rest.

#### Night’s Rest
When you finish a night’s rest, you gain the following benefits:

***Spend Hit Point Dice.*** You can spend one or more of your hit point dice to regain hit points. For each hit point die you spend in this way, roll the die and add your Constitution modifier to it. You regain hit points equal to the total (minimum of 1 hit point). You can decide to spend an additional hit point die after each roll.

***Special Feature.*** If you have a feature that recharges or interacts with a short rest, it recharges  or interacts in the way specified in its description.

#### Good Rest
Taking 3 consecutive night’s rests in the same location is a good rest. When you finish a good rest you gain the following benefits:

***Regain All HP.*** You regain all lost hit points and all spent hit point dice. If your hit point maximum was reduced, it returns to normal.

***Ability Scores Restored.*** If any of your ability scores were reduced, they return to normal.

***Exhaustion Reduced.*** If you have the exhaustion condition, its level decreases by 1.

***Special Feature.*** If you have a feature that recharges or interacts with a long rest, it recharges  or interacts in the way specified in its description.

#### Safe Haven
Taking a night’s rest in a safe haven turns that night’s rest into a good rest. A safe haven is a location that makes the characters feel safe and secure by virtue of some form of protection, while simultaneously being comfortable enough for the characters to feel at home and indulge in their usual creature comforts. Ultimately, the GM determines whether a location qualifies as a safe haven.

#### Holy Days
Magic Items that recharge on dawn instead recharge on the dawn of the next Sunday.

#### Knocking Out A Creature
When you would reduce a creature to 0 hit points with a melee attack, you can instead reduce the creature to 1 hit point and give it the unconscious condition. The creature loses the condition in 1d4 hours.

#### Relaxing
You can spend four hours of downtime relaxing to regain a spent hit point die.

#### Sanctuary
If you leave a ritual offering of 100 gold pieces at an active holy site, you can take a night’s rest there in 10 minutes instead of a whole night.

#### Symbol of God  ·  Wonderous Item, Legendary
This elaborate golden cross is a symbol of the Mother. It has nine charges, when there are no charges left in the cross, it crumbles to dust. You can take the Magic action to spend a charge and create one of the following 20-foot Emanations for 10 minutes:

***Quick Rest.*** Creatures staying within the emanation for the duration can gain the benefits of a Night’s Rest.

***Greater Rest.*** Creatures that are in the process of taking a Night’s Rest within the Emanation instead gain the benefits of a Good Rest at the end of the night.

### Random Encounters 
At the start of the day, the GM rolls for random encounters by rolling a d6. 

***In the Wilderness.*** On a 6, the GM rolls on the Random Encounter Table.

***In Dangerous Areas.*** On a roll of a 5 or a 6, the GM rolls on the Random Encounter Table.

***In a Treacherous Area.*** On a roll of a 4, 5, or 6, the GM rolls on the Random Encounter Table.

#### Building a Random Encounter Table
GMs should build a random encounter table by listing types of encounters on one side and the results of a die roll on the other. Below is a Random Encounter Table for a gothic horror setting. You could use it as reference for how to build your own table for your own wilderness. You create an entry for each encounter which outlines how the encounter could be used as an encounter for simple combat, deadly combat, exploration, or dialogue.

#### Using Random Encounter Table
Rolling on a random encounter table, a GM uses the result as an inspiration for what happens next, not as a directive. For example, the result for a roll of a 6  is Wolves, the GM might write the following notes to themselves to outline possible outcomes of a random wolf encounter.

#### 6. Wolves.
A wolfpack circles the camp and charges the characters if they think they can take them on. Each of the beasts bears the singed mark of Strahd on their paws, indicating his control over the beasts.

The pack consists mostly of wolves, but there might be some dire wolves, or a werewolf pack leader. If the party is particularly high level, consider adding a dire worg!

Alternatively, they might find a single wounded wolf pup. A character could, with a successful DC 18 Animal Handling check, spend a ration to endear the wolf to themselves. This might lead to the wolf becoming a sidekick!

#### Updating the Table
The GM could choose to change and update the table depending on the region the characters are travelling through to make sure the results always include fun, exciting, and fitting options.

### Random Weather
While exploring, the weather can have a huge effect on how progress is made day-to-day. Use the following tables to introduce random weather by the seasons.

***What are these months?*** These random weather tables are based off of the Orethon calendar. Which starts in Springsdawn and ends in Wintersdusk. You can rename the tables to fit your own campaign setting, or use these as written.

***How to read the tables.*** The weather determines the effect on the Navigation Checks and Marching Checks made in the Regional Map section. 

***Advantage and Disadvantage.*** (A) means you have advantage on the listed checks, whereas (D) means you have disadvantage on the listed checks.

***Not all months are equal.*** As you would expect, the weather in some months make exploration more difficult. Parties may want to limit their exploration to the more convenient months.

***Weather as Damage.*** In extreme weather, GMs might rule that party staying o vernight on a mountainside in cold tempertures, or in a clearing in blistering winds takes 1d6 cold damage when they finish their rest.

#### Springsdawn & Firstseed

|1d6|Weather|Effect|
|---|---|---|
|1|Heavy rain|(D) March & Navigation|
|2|Occasional showers|(D) Navigation|
|3–4|Mild temperatures|None|
|5–6|Clear skies|(A) March & Navigation|

#### Monsoon

|1d6|Weather|Effect|
|---|---|---|
|1–2|Thunderstorms|(D) March & Navigation|
|3–4|Heavy rain|(D) March & Navigation|
|5|Intermittent showers|(D) Navigation|
|6|Cloudy|None|
#### Midnight Sun

|1d6|Weather|Effect|
|---|---|---|
|1–2|Intermittent showers|(D) Navigation|
|3|Mild temperatures|(A) March|
|4–5|Hot and humid|(D) March|
|6|Scorching heat|(D) March|
#### **Drywind

|1d6|Weather|Effect|
|---|---|---|
|1|Dust storms|(D) March & Navigation|
|2|Hot and dry|(D) March|
|3–5|Warm with dry winds|None|
|6|Boiling hot|(D) March & Navigation|
#### Midyear

|1d6|Weather|Effect|
|---|---|---|
|1|Slightly too hot|(D) March|
|2|Pleasantly warm|None|
|3–4|Cooling breezes|(A) March|
|5–6|Clear skies and mild|(A) March & Navigation|
#### Harvestfall & Last Seed

|1d6|Weather|Effect|
|---|---|---|
|1|Autumn rain|(D) Navigation|
|2–3|Crisp and clear|None|
|4–5|Warm days|(A) March|
|6|Pleasant|(A) March & Navigation|
#### Coldwinds

|1d6|Weather|Effect|
|---|---|---|
|1|Strong winds|(D) March & Navigation|
|2|Overcast|None|
|3–4|Cool and clear|(A) March|
|5–6|Occasional snow|(D) Navigation|
#### Snowfall & Evernight

|1d6|Weather|Effect|
|---|---|---|
|1–2|Snowstorms|(D) March & Navigation|
|3–4|Heavy snows|(D) March & Navigation|
|5|Light snows|(D) Navigation|
|6|Clear with snowy ground|(D) Navigation|
#### Wintersdusk

|1d6|Weather|Effect|
|---|---|---|
|1|Light snow|(D) March & Navigation|
|2|Frosted ground|(D) Navigation|
|3–4|Mild days, chilly nights|None|
|5–6|Occasional showers|(D) March|