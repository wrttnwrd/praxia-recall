---
type: reference
title: "Reading notes: Read notes — Aventine sourcebook (23 files)"
description: Raw notes taken while reading the source vault, before the graph was written.
status: draft
generated: { by: recall/claude-opus-5, method: read-and-extract }
---

# Read notes — Aventine sourcebook (23 files)

## Data-quality findings (only visible by reading)
- `Gritch.md` frontmatter says `name: Artemis Hasp` — copy-paste error. Body is Cora/Gritch, Aasimar assassin.
- `Valana.md` frontmatter says `name: Corwin Dunsbane` — copy-paste error. Body is Valana, half-orc cleric.
- `Blong Hrusto.md` says `name: Blung Hrusto`. Body uses "Blong", female ("she will tell").
- `grimshaw shadowplank.md` has NO frontmatter — one Dataview line: `captain of:: The Wave Serpent`.
- `Kaelen Varrus.md` carries a hand-built JSON-LD graph: person.livesIn/memberOf/friendsWith + `prefixes:`.
  Evidence the user already wanted this graph. Title: Lord Commander, age 203, Aventine Guard.
- `Ringling's Collectibles.md` type is `po` (typo for poi).
- Marta's Fury == The Kestrel (Oriana's ship, two names).

## Entities
place/city: Aventine (founded -300 FR by Ahmad Azari; pop 500k + 15k elven refugees; monarchy; in Camadan, Silidria)
place/district: Hull Ward, Axiat, The Docks, Taelian (aka Diaspora), The High Ward, Zuppek Bazaar,
  Sword's Cross, Merchant Ward, Temple District, The Underground, Naphtha Caves, Royal Grounds
place/poi: The Green Slaad, The Mekanikum, The Cauldron, The Flagrant Farce, Renney's Remedies,
  The Wink And Kiss, Temple of Pelor (Hull Ward), Ringling's Collectibles, Lumpkin's Fine Foods,
  Hull Ward Bakery, The Palace, Conclave Extent, University of Aventine, Buoyant Sea, Lumpkin's Meats,
  The Laughing Luff, The Woodwright, Ink Inc, Threaded Ways, Bartholemew's Tomes, The Diabolist's Diadem,
  Mildred's Armory, Pop's Blasting & Oddities, The Brimming Tankard, House Umbra
vehicle/airship: The Wave Serpent (-17 FR, 450hp, 65000gp, crew 10), The Villain's Discontent,
  Marta's Fury (aka The Kestrel)
group/house: Royal House, Bluestrike, Highfury, House Umbra, House Belos, House Drace, Fel House,
  The Sicarii, The Shadow Veil, Court of Guthra Ghuul, Marta's Marauders, Temple Of Helm, Aventine Guard
group/temple: Amoth (defunct), Bahamut, Erathis, Gond, Ioun, Pelor, Raven Queen, Shar, Waukeen

## Characters (Aventine)
Ahmad Azari (founder, -300FR), Feyd Azari (prince), Fidelia Azari, Siliib Azari, Fatimah Azari (dead),
Aisha Azari, Xavis/Zavvis (domestic advisor = spymaster), Osdryn Bluestrike, Oriana Valtova,
Grimshaw Shadowplank, Eledra, Mevvic (dead, secret head Cult Of Eight), Lumpkin, Bataar Highfury,
Gart, Angus Bloodstone, Marta Valtova (dead), Tasha Quan, Panovar Flynt, Marceline, Eldari Belos,
Parwairt, Iridian Drace, Artemis Hasp, Vek Azar, Ma'ayaat (changeling), Gritch (b. Cora),
Marcus Vane (general), Vardra, Timogen, Elethar, Riley Whentworth, Dahc, Whendolen, Pablo Nailhammer,
Borin Thunderfist, Mira Greenbottle, Bartholemew, Ezelbeth, Szat (imp), Pop, Guthra G'huul,
Elenara Silverleaf, Loss (High Priestess of Shar), Armak Rockfist, Blong Hrusto, Corwin Dunsbane,
Erzohd Baendi, Iric, Kaelen Varrus, Lysander, Roxlycheh, Thud, Valana, Wom Taits, Venkat,
Lucretia Borova, Magon Ezodar, Agonar Mangler, Hadigak, Turbin, Heribert, Artemis Killgrave,
Narinda Shadomantle, Faendal

## Relations (stated in text)
Aventine located_in Camadan; Camadan located_in Silidria
Hull Ward located_in Aventine (oldest neighborhood); Green Slaad located_in Hull Ward
Ahmad Azari founded Aventine (-300 FR)
Feyd Azari rules Aventine; Fidelia+Siliib children; Aisha wife; Fatimah first wife (dead, plague)
Xavis serves Royal House (spymaster)
Bluestrike based_in Merchant Ward, led_by Osdryn Bluestrike; members Oriana Valtova, Grimshaw
  Shadowplank, Eledra, Mevvic, Lumpkin
Highfury based_in Axiat, led_by Bataar Highfury; members Gart, Angus Bloodstone, Marta Valtova
House Belos based_in Hull Ward, led_by Tasha Quan, founded_by Eldari Belos (-300 FR);
  members Tasha Quan, Panovar Flynt, Marceline; keeps petty crime down in Hull Ward
House Drace based_in The Docks, led_by Parwairt, founded_by Iridian Drace (-150 FR); member Artemis Hasp
Fel House based_in Docks underground, led_by Vek Azar, serves The Raven Queen
The Sicarii led_by Ma'ayaat; member Gritch; possibly controlled_by House Belos
Court of Guthra Ghuul founded_by Guthra G'huul (4 FR, Pandora Crisis); controls The Underground;
  protects House Umbra + Temple of Helm; G'huul patron = Mystra
Marta's Marauders led_by Marta Valtova (dead); members Angus Bloodstone, Armak Rockfist,
  Oriana Valtova, Artemis Hasp; disbanded
Armak Rockfist owns The Green Slaad (secret); Blong Hrusto manages/bartends it and funnels money
  to "Gravelthumb" (Armak's alias); Roxlycheh host; Thud bouncer; Wom Taits performs there
Artemis Hasp owns The Mekanikum; member_of House Drace; rival_of Pop
Oriana Valtova captains Marta's Fury/The Kestrel; adopted daughter of Marta Valtova;
  protege of Grimshaw Shadowplank; pirate hunter
Grimshaw Shadowplank captains The Wave Serpent; 1st officer Artemis Killgrave
Lysander captains The Villain's Discontent; organization Notorious RBG
Valana leads Temple Of Helm (lead cleric); Corwin Dunsbane Paladin Lt, Order of Helm
Gritch member_of Sicarii; enemies Aventine guard, Notorious RBG; ally Faendal
Iric druid of The Druidfel; enemy The Obsidian Wing; ally Notorious RBG
Kaelen Varrus Lord Commander, member_of Aventine Guard, friendly_with Notorious RBG, lives_in Aventine
Blong Hrusto now manages Notorious RBG's bar at Wyldwood
Panovar Flynt owns The Cauldron; wants The Green Slaad back
Marceline runs Ringling's Collectibles
Lumpkin runs Lumpkin's Meats + Lumpkin's Fine Foods; nephews Turbin, Heribert
Hadigak owns Hull Ward Bakery; partnered with Lumpkin
Venkat set up Temple of Pelor in Hull Ward
Lucretia Borova owns The Flagrant Farce; Magon Ezodar owns The Wink And Kiss (security Agonar Mangler)
Pablo Nailhammer was carpenter of The Wave Serpent; owns The Woodwright
Elethar leads Taelian; Mevvic died during "the-engine"
Wave Serpent allies: Villain's Discontent, The Kestrel, Notorious RBG

## Events referenced
The Fall (major, resets calendar to FR), Ten Years War (BR 95, vs Fel House), Pandora Crisis (4 FR),
Battle of Swords' Cross, student demonstrations vs House Umbra (3 FR), plague (killed Fatimah)
