---
type: reference
title: NPC Directory
description: TABLE WITHOUT ID file.link AS "Name", alignment, city, organization
status: draft
generated:
  by: recall/claude-opus-5
  at: '2026-09-08T20:50:58Z'
  method: read-and-extract
sources:
- id: source
  resource: file:///Users/i.lurie/praxia/_sourcebooks/NPC%20Directory.md
  title: 'Original: _sourcebooks/NPC Directory.md'
content_hash: c11fce5f7088fa4b
confidence: unknown
---

```dataview
TABLE WITHOUT ID file.link AS "Name", alignment, city, organization 
WHERE type = "npc"
AND file.name != "npc"
SORT file.name
```