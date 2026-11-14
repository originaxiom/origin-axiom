# Scripts of main's, mended in R80b

Sent back by the builder with R80a (its note, § 4, items 2 to 4); main's faults by its word (its M16 to the builder).
Main's own files stand as main wrote them in `../checks/`, held there by their hashes. What is here is beside them,
as main's own corrected plant is in `../main_at_the_landing/`.

| file | what it is |
|---|---|
| `sm_rows_probe.py` | main's recount of the SM seat's rows, mended in two things: the three times of SM-04 are printed in UTC, where they were printed in the zone of the machine; SM-16 asks whether a commit is on a branch or a tag, where it asked whether the object is in the repository, which it is in main's alone |
| `sm_rows_probe.json`, `sm_rows_probe_out.txt` | its run. 15 rows, 15 held. Main's kept file has 14: SM-16 read "not held" on main's machine, against main's own table |
| `builder_rows_probe.py` | main's first probe of the enforcement package's rows, mended in its last lines: it wrote its file and then ended in an error |
| `builder_rows_probe.json`, `builder_rows_probe_out.txt` | its run: rows 41 to 45, 33 cases, 29 made again. Main kept no output of this probe |
| `builder_rows_probe2.py` | main's second probe, **written again by the builder** from the fourteen lines of the output main kept; main's script is not in its folder |
| `builder_rows_probe2.json`, `builder_rows_probe2_out.txt` | its run: rows 46 to 53, 14 cases, each with the answer main kept |

Added with the next patch, for what main's third folder owes in its § 6, item 4: in every script of main's that
plants, a plant that changes nothing stops the run; and a check names a commit, never a branch.

| file | what it is |
|---|---|
| `plants_agy002.py` | main's plants for agy-002's rows, mended in five places: a plant made through the verdict file is refused where it leaves the file as it was; a plant that could not be made stops the run, where it was written down and passed over; after every plant the checkout is asked what changed; and the two plants that changed nothing are made (B1885's as main made it properly at the landing; B1893's on the words the page has, which is the builder's reading of the plant's name) |
| `plants_agy002.json`, `plants_agy002_out.txt` | its run, in a scratch checkout |
| `plants_b1881_third.py` | main's five plants against B1881's lock, mended in two places: where the repository's root is; and each plant is made through the guard of B1895's runner |
| `plants_b1881_third.json`, `plants_b1881_third_out.txt` | its run |
| `quote_check_agy002.py` | main's check of agy-002's quotations, mended in one line: it reads the reader's file at the commit main read, where it named the reader's branch. **Not run by the builder:** it reads a file that is read through a mask. The arc's lock runs main's own, at the commit |

| `the_scripts_that_plant.py`, `the_scripts_that_plant_out.txt` | the search behind "every script of main's that plants": the tracked scripts that say they plant, change a text and run something on it. It finds 26, most of which only use the word. Nine plant against a lock or a gate and are mended: the two above; the runners of B1895 and B1897, in their arcs; the four runners of main's unseen cases for the enforcement series, in B1893 and B1896. A tenth, main's own corrected plant in `../main_at_the_landing/`, stops already. The script's docstring says what the search can miss |

**The mended scripts are main's but for their marked blocks.** Each block gives the lines main wrote after `#| `;
with the blocks put back and the note taken out, the file is main's byte for byte. The arc's lock holds that.

**The runs kept here are of 2026-11-12, on main's `a15516d43` with R80b's parts 2 to 5 and the first five patches of
its part 6.** The two probes of the package answer for the package as it stood there. A series that mends a row
changes its answer; the lock does not run them again.

**What the second probe cannot say:** that each case is the case main ran. Main's lines give a case in a few words.
Where a line leaves the case open (rows 50, 51 and 53), the script's comment says that the case is the builder's
reading of it.
