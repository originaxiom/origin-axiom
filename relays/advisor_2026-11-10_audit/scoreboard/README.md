# The scoreboard page: where its numbers come from

**From:** the advisor seat. **Kind:** `verify:`. Nothing on main is changed.

The owner asked this seat for a visual scoreboard (his word and what it answered: `OWNER_RULINGS_2026-11-10.md`). The
page is a private page on his account. This folder holds what it is made from.

| file | what it is |
|---|---|
| `scoreboard_snapshot.py` | reads four of main's files at one commit and writes one data file. It types nothing |
| `scoreboard_snapshot_main_8f0b03814.json` | its output at main `8f0b03814`: the file the page shows |

```
python3 relays/advisor_2026-11-10_audit/scoreboard/scoreboard_snapshot.py --ref origin/main --out FILE
```

## What it reads

| main's file | written by | what the page takes from it |
|---|---|---|
| `frontier/B1861_the_closure_programme/PROGRAMME.json` | main's builder; a gate compares | the packages, what each needs, the findings' states, the input budget |
| `frontier/B1858_the_closure_map/NODES.json` | main's builder; a gate compares | every statement, its layer and grade; which joints feed which value |
| `frontier/B1858_the_closure_map/EDGES.json` | main's builder; a gate compares | every relation between two statements |
| `docs/total_inputs_scoreboard.json` | typed by main; a gate compares its page | the values, the count earned, what each frame says of each value |

The one table that is not main's is the planted-violation run, read from `tools/planted_violations_main_<commit>_out.txt`.

## What it refuses

The script stops without writing if main's files do not add up: a grade it does not know; a count of statements that
still need a path, or of conditional results, that is not main's own; obligations that do not cover the packages; an
input budget that does not add up; the scoreboard's page and data file disagreeing on what is earned; an edge that
names a statement not on the map; a package that needs one not in the programme; a joint whose count of values fed
differs from its list.

## What the page is not

- **Not the repository's scoreboard.** On main, the count as an output and the map on the desk are one package
  (WP-0.12), not started. The page prints main's typed count, 0 of 19. It does not compute a count from ancestry.
- **Not live.** It is a copy at one commit and changes when the script is run again and the new file attached.
- **Not in this folder.** The page's source is kept with the page. Its style names carry a vendor's name, which the
  attribution rule keeps out of tracked files. Its address is left out for the same reason.

## What "ready for the final reading" counts

The packages that main's comparison package (WP-6.1) rests on, by main's own `rests_on` list, and how many are done.
A count, with no weights. At `8f0b03814`: 40 packages, 1 done, 14 started, 25 not started.
