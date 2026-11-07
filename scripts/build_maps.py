#!/usr/bin/env python3
"""Generate map concepts and 1200px thumbnails.

OKF holds markdown only (SPEC §4.1, §6.2), so an image is never a concept.
Each map gets a concept document whose `resource:` is a URI pointing at the
untouched original in the read-only vault, plus a downsampled thumbnail in
assets/ so the map can be read without leaving the bundle.

Usage: python3 scripts/build_maps.py [--dry-run]
"""
import re, sys, subprocess, hashlib, collections
from pathlib import Path
from urllib.parse import quote
import yaml

B = Path(__file__).resolve().parent.parent
SRC = Path(yaml.safe_load((B / "graph.yaml").read_text(encoding="utf-8"))["source"]).expanduser()
OUT = B / "assets" / "maps"
CAP = 1200

# Images outside the map folders that are still maps (vault-relative paths),
# and display names for files whose own name says nothing.
EXTRA = ["_sourcebooks/attachments/Pasted image 20260918141425.png"]
NAMES = {"Pasted image 20260918141425.png": "Avernus Hunt point crawl"}

# filename fragment -> concept id(s) the map depicts
DEPICTS = [
    ("20260918141425", ["avernus-hunt"]),
    ("cryptofamenopophis", ["the-crypt-of-amenopophis"]), ("thecrypt", ["the-crypt-of-amenopophis"]),
    ("crypt-3-loom", ["the-crypt-of-amenopophis"]), ("amenopophis-door", ["the-crypt-of-amenopophis"]),
    ("notorious-manor", ["rbg-bastion"]), ("bournier-observatory", ["aventine"]),
    ("greenslaad", ["the-green-slaad"]), ("hull ward", ["hull-ward"]), ("hull-ward", ["hull-ward"]),
    ("undercity", ["the-undercity"]), ("cauldron", ["the-cauldron"]),
    ("aventine", ["aventine"]), ("silgorin-below", ["silgorin-below"]),
    ("shadowmir", ["shadowmuir"]), ("nigh-darul", ["nigh-darul"]), ("ironstead", ["ironstead"]),
    ("essedria", ["essedria"]), ("avernus", ["avernus"]), ("diron", ["dirion"]),
    ("silidria-w-urdun", ["silidria", "urdun"]), ("silidria", ["silidria"]),
    ("underdark", ["underdark"]), ("praxia-all-runes", ["praxia"]), ("praxia-just-map", ["praxia"]),
    ("map-pharos", ["praxia"]), ("praxia_old", ["praxia"]), ("praxia", ["praxia"]),
    ("thecamp", ["the-mining-camp"]), ("thecave", ["the-mining-camp"]),
    ("neighborhood", ["hull-ward"]), ("outskirts", ["the-outskirts"]),
]

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]

def main():
    dry = "--dry-run" in sys.argv
    files = [p for p in SRC.rglob("*")
             if p.is_file() and p.suffix.lower() in (".png", ".jpg", ".jpeg")
             and ".obsidian" not in str(p)
             and (re.search(r"(/maps?/|themaps|_pro-maps|/_aventine/|/_shamharan/)", str(p))
                  or str(p.relative_to(SRC)) in EXTRA)]

    # the vault keeps two copies of the Deven Rue set; keep one, record the other
    seen, entries, dupes = {}, [], collections.defaultdict(list)
    for p in sorted(files):
        key = (p.name.lower(), p.stat().st_size)
        if key in seen:
            dupes[seen[key]].append(str(p.relative_to(SRC))); continue
        seen[key] = p
    OUT.mkdir(parents=True, exist_ok=True)

    # ids are the filename, disambiguated by parent folder only when two maps
    # share a name. Truncating a full path collided 12 crypt maps onto one id.
    ids, taken = {}, set()
    stem_of = lambda p: NAMES.get(p.name, p.stem)
    for p in sorted(seen.values()):
        base = "map-" + slug(stem_of(p))
        if base in taken:
            base = "map-" + slug(f"{p.parent.name}-{stem_of(p)}")
        n = 2
        while base in taken:
            base = f"map-{slug(p.parent.name)}-{slug(p.stem)}-{n}"; n += 1
        taken.add(base); ids[p] = base

    made = 0
    for p in sorted(seen.values()):
        rel = p.relative_to(SRC)
        cid = ids[p]
        thumb = OUT / f"{cid}.jpg"
        if not dry and not thumb.exists():
            subprocess.run(["sips", "-Z", str(CAP), "-s", "format", "jpeg",
                            str(p), "--out", str(thumb)],
                           capture_output=True, check=False)
            made += 1
        depicts = next(([d for d in ids] for frag, ids in DEPICTS
                        if frag in str(rel).lower()), [])
        pretty = re.sub(r"[-_]+", " ", stem_of(p)).strip()
        pretty = pretty[:1].upper() + pretty[1:]
        # "Map:" prefix keeps a map's title distinct from the place it depicts —
        # otherwise the Aventine map and the city of Aventine collide.
        title = f"Map: {pretty}"
        if cid != "map-" + slug(stem_of(p)):
            title += f" ({p.parent.name.lstrip('_')})"
        mb = p.stat().st_size / 1048576
        e = {"id": cid, "kind": "maps", "type": "map", "title": title,
             "description": f"{title} — {mb:.1f} MB original in the source vault.",
             "resource": "file://" + quote(str(p)),
             "thumbnail": f"/assets/maps/{cid}.jpg",
             "confidence": "stated"}
        if depicts:
            e["relations"] = {"depicts": depicts}
        if dupes.get(p):
            e["evidence"] = {"resource": "Also present in the vault at: "
                             + "; ".join(dupes[p]) + "."}
        entries.append(e)

    txt = ("# Generated by scripts/build_maps.py — do not hand-edit.\n"
           "# One concept per map. The image itself is never a concept: OKF bundles\n"
           "# hold markdown only, so `resource` points at the untouched original and\n"
           "# `thumbnail` at a 1200px copy in assets/.\nconcepts:\n"
           + yaml.safe_dump(entries, sort_keys=False, allow_unicode=True, width=100))
    if not dry:
        (B / "graph-maps.yaml").write_text(txt, encoding="utf-8")
    print(f"{len(entries)} map concepts, {made} thumbnails generated, "
          f"{sum(len(v) for v in dupes.values())} duplicate files folded")

main()
