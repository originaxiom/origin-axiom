# B1883 — Where we stand: how far the record is from the final reading, as one generated page

*Main, 2026-11-11 (S306p). The owner asked a seat, the same morning: "how far are we from ... 100% ready for the final
reading? the dynamic scoreboard we talked?" The advisor seat answered with a script that reads main's own generated
files (its `tools/where_we_stand.py` @ `3dcc6319`). This arc makes that answer main's: one generated page, compared
with its builder at every push, and quoted in every report to the owner. It is an instrument. It computes nothing
about the object. 0 of 19.*

## 1. The answer first

**Ready for the final reading: no.** The page is `WHERE_WE_STAND.md` in this folder. Its numbers are not copied here,
because they move at every landing; the page and its data file are the place to read them.

- **What "ready" means on the page.** The sealed card is done, and every package it must wait on is done. Nothing
  softer is counted.
- **What the page is built from.** The closure programme's data (B1861), the closure map (B1858), the scoreboard's
  data file, and the point register. Each of the first two is itself generated and gated.
- **Nothing is typed in the builder.** It refuses to write where two of its sources disagree.

## 2. What it shows

| section | what is read | from |
|---|---|---|
| the final reading | values earned; the sealed card; the comparison; each package the card waits on | the scoreboard; the programme |
| the three milestones | packages done, started and not started under each | the programme's own milestones |
| the work order | packages by state and by obligation; packages with no owner; map nodes that still need a path; debts | the programme; the map |
| what is put in by hand | the independent choices by kind; how each could leave; the conditional headlines | the programme's budget |
| the audit | findings by state; which carry the auditing seat's verdict; what main changed since | the programme |
| the record's own list | open points by kind; the calls that are the owner's | the register |
| what it does not know | unread seat work; the planted-violation count; that the count is still typed | — |

## 3. What it refuses

| the builder refuses to write when | why |
|---|---|
| the scoreboard's page and its data file give different counts of values earned | one of them is stale |
| the programme's count of packages by state is not a recount of its packages | a count typed somewhere |
| the sealed card waits on a package the programme does not hold | a dangling name |
| the programme does not hold exactly one package each for the card, the comparison and the count as an output | the page would read the wrong row |
| the map's node count is not the one the programme read | the programme was built on another map |

Each refusal is planted in this arc's lock and fires.

## 4. What it is not

- **It is not the count as an output.** The owner's ruling asks that the headline be computed from each value's
  ancestry on the map (package WP-0.12). This page reads the programme's own counts. It says so in its last section.
- **Its denominator is still a typed constant** of the scoreboard's checker. The page prints how many rows the data
  file lists beside it.
- **It does not judge.** A package marked started is counted as started, on main's own word in the programme.

## Seen first

- **The repo sweep:** the context card and the reviewer's view (`docs/views/`) give the state of the record's arcs,
  and the scoreboard gives the count of values and joints. No page gave the distance to the sealed card. The
  programme (B1861) holds every number used here, spread over a long page.
- **The advisor seat's script** is the direct source of the idea and of the sections' order. Main read it and wrote
  its own builder; none of the seat's code is run or copied.

- **The literature:** none applies. It is a page about the record's own state.

## Disclosed

- **The seat's script reads any commit of main and needs nothing of main's.** Main's page is generated at a landing
  and is as old as the landing. For the state between landings the seat's script is the better instrument.
- **The page was built the morning the owner asked for it, after he had asked a seat and not main.**

## Reproduce

```
python3 frontier/B1883_where_we_stand/verification/build_where_we_stand.py
python3 -m pytest -q frontier/B1883_where_we_stand/verification/ tests/test_closure_generated.py
```
