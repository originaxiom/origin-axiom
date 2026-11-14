# Three probes of main's, mended in R80b

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

**The two mended scripts are main's but for their marked blocks.** Each block gives the lines main wrote after `#| `;
with the blocks put back and the note taken out, the file is main's byte for byte. The arc's lock holds that.

**The runs kept here are of 2026-11-12, on main's `a15516d43` with R80b's parts 2 to 5 and the first five patches of
its part 6.** The two probes of the package answer for the package as it stood there. A series that mends a row
changes its answer; the lock does not run them again.

**What the second probe cannot say:** that each case is the case main ran. Main's lines give a case in a few words.
Where a line leaves the case open (rows 50, 51 and 53), the script's comment says that the case is the builder's
reading of it.
