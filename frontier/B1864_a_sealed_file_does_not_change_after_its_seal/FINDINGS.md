# B1864 — A sealed file does not change after its seal: the second of the audit's two critical findings, closed with its planted tests

*Main, 2026-11-10 (S306o). The advisor seat's finding G2 (harvest row 1629; P-757; the closure programme's WP-0.7), with
G3 and G4: an edit of a sealed file after its seal was undetected for most sealed files; the seal ledger certified
itself; and the seal-order gate read one file name. Reproduced on main by main's own reading of the gates and by main's
reader's planted run (PV3 to PV8). This arc is the fix and its tests. No physical value is computed. 0 of 19.*

## 1. The answer first

- **What was wrong.**
  - The digest gate recomputed only the ledger's hand-written rows, a few dozen of the sealed files. For every other
    sealed file, the candidate's pre-registration among them, nothing compared the file with what was sealed.
  - A sentence appended to a sealed pre-registration and committed passed every gate. So did deleting a sealed file,
    and editing one while regenerating its ledger row in the same commit.
  - The ledger gate checked that each sealed file had a row. It did not check the row. A hash changed by hand passed.
  - The ledger's column "recorded elsewhere" read the previous ledger as evidence, and every untracked file on the
    machine. So each hash was vouched for by its own earlier row, and the answer depended on the machine.
- **What holds now.**
  - **A new gate, `seal-immutable`, reads history.** After its first commit, no commit on main's first-parent line may
    edit, delete or move a sealed-style file. A seal is added once. An amendment is a new file beside it.
  - It covers every seal name the ledger's generator knows (`PREREG*`, `*DESIGN*.md`, `SEALED*.md`, `DECLARATION.md`),
    not the two names the older gates read.
  - It fails closed where history cannot be read, and a violation stays visible until the owner waives it by commit
    and path. The waiver list is empty.
  - **The ledger gate recomputes every generated row** from its file, refuses a listed file that is not in the tree,
    and requires a row for every sealed-style file by the generator's own patterns.
  - **The ledger no longer vouches for itself.** Its generator reads tracked files only, and not the ledger.
  - **The seal-order gate reads every seal name.** Thirty arcs whose rule and record were first committed together,
    under names the gate did not read, are entered by name on the list of seals whose order git cannot show.

## 2. What the corrected ledger shows

- **Of 432 sealed-style files, 156 have a hash that no other tracked file records:** 145 that were never changed after
  banking, and 11 that were. Before, the ledger said "yes" in all 432 rows.
- **That is the audit's own count** (156), reached on main with the corrected generator.
- **A second run gives the same numbers,** which is the audit's planted test PV7. Before, a second run reported none.
- **What an unrecorded hash means.** The file's present content is what git holds. Nothing outside the file states
  what it was when it was sealed. For the 145, git's single commit is that statement. For the 11, the ledger's column
  says they changed after banking, and each arc's own trail has to carry the reason.
- **71 of the 432 are sealed under a name the older gates did not read** (`DESIGN.md`, `PREREG.md` and their variants,
  in 49 arcs). The new gate and the ledger gate read them all.

## 2b. What the rule finds when read back over recent history

The gate's rule starts today. Read back over the last 300 commits, for the record, it finds three changes to a sealed
file, all to one: `frontier/B1840_the_principled_ends/DECLARATION.md`, the menu of ends that the candidate's price
rests on.

| commit | time (2026-11-05) | what changed |
|---|---|---|
| `83c52cb0c` | 09:21 | the declaration first committed |
| `749e49477` | 09:35 | two rows reworded and the record sweep added |
| `7ab1624aa` | 10:36 | a dated note: the list closes; a fourth end entered, the one the candidate's row uses |
| `063b01302` | 13:05 | a dated note: proposals received after the list closed, not entered |

- **This is the factual core of the audit's finding V4,** reproduced on main: the end that won was entered 75 minutes
  after the first declaration. The note that entered it says the look had not yet run.
- **Nothing here says the candidate is wrong.** It says its declaration was changed after it was declared, and that
  until today no gate would have noticed. The audit's two figures for the screen, and its remark on the fitted
  factor, are not yet checked on main.
- **From here** such a change is refused. A later entry is a new file beside the declaration.

## 3. The tests (`tests/test_seal_immutable.py`)

Each builds a small repository, commits the violation, and runs the check on the clean tree at that commit.

| test | what is planted | result required |
|---|---|---|
| PV3 | a sentence appended to a sealed file, committed; the tree clean | refused: "edits the sealed file" |
| PV4 | a sealed file deleted | refused: "deletes the sealed file" |
| PV5 | a sealed file edited, and a ledger row with the new hash written in the same commit | refused: no row can launder the edit |
| other names | four seals named `PREREG.md`, `…DESIGN….md`, `SEALED….md`, `DECLARATION.md`, then each edited | four refusals |
| a move | a sealed file renamed | refused, naming the sealed path |
| not a seal | an arc's findings corrected | passes |
| a restored edit | the text put back in a later commit | both commits refused, until each is waived by commit and path |
| unreadable history | a clone of depth one; a plain directory | "cannot verify" |
| the gate itself | the gate function pointed at a repository whose history holds the violation | fails: the registered control |
| PV6 | one generated row's hash changed by hand; a row for a file that is not in the tree | the ledger gate refuses each |
| PV7 | the generator run twice in a small repository; a hash quoted in an untracked note, then in a tracked file | both runs report the hash unrecorded; the untracked note does not record it; the tracked file does |
| PV8 | two arcs sealed as `PREREG.md` and `DESIGN.md`, each committed together with its findings; a third sealed first | the two are in the class and refused when not listed; the third is not in it |

## 4. The seal-order list, widened

- **Read under every seal name, 110 arcs have their rule and their record first committed in one commit.** The gate's
  single name saw 80. The other thirty are entered once on `docs/SEAL_ORDER_UNSHOWN.md`, by name, with the sealed file
  and the commit. The audit's own example, B1297, is among them.
- **What the list says is unchanged:** git cannot show whether the rule preceded the result. It does not say either
  way. From here the list may only shrink, as before.
- **Seventeen of the thirty are `DESIGN.md` files** of harvest arcs, whose designs were sealed by hash elsewhere and
  committed on main with their findings.

## 5. What is not done here

- **History before the rule's first commit is not read.** The rule starts at `76a4ff388` (2026-11-10). The ledger's
  own column "commits" shows which sealed files were changed after banking before that; they stay as the ledger
  describes them.
- **The provenance gate still reads the narrower list of two file names.** It asks that a seal carry the two halves
  of the provenance rule in its own text. Widening it would put the other 71 files under that rule; that is not done
  here.
- **The hand-written digest rows and the generated rows are still two systems.** The audit's proposal of one
  machine-readable manifest with a full hash per sealed file is not built. The eight-character hash of a generated row
  is recomputed, which detects an edit; a full hash would also resist a constructed collision.
- **The gate's own source can be edited in the violating commit** (the audit's G12, open).

## Seen first

- **The repo sweep:** the four seal gates read in full (`seal-provenance`, `seal-digests`, `seal-ledger-current`,
  `seal-order-unshown`) and `scripts/seal_ledger.py`; their registered controls in `tests/test_gate_failing_paths.py`,
  each of which replaces the gate's inputs and none of which commits a violation. ERROR_LEDGER's E47 and E48 are the
  digest classes the digest gate was built for; neither is this one.
- **The literature:** none needed.

## Disclosed

- **The audit found this; main did not.** The candidate's own pre-registration was among the files with no check.
- **Main's first correction of the generator was incomplete.** With the ledger alone removed from the evidence, two
  hashes read as unrecorded where the audit had found 142: the generator was also reading every untracked file under
  the working directory. It now reads tracked files only.
- **The rule is stricter than the record's past practice.** Some sealed files were amended in place before their runs.
  From here an amendment is a new file, or a waiver by name.

## Reproduce

```
python3 -m pytest -q tests/test_seal_immutable.py
python3 scripts/gates/gates.py | grep seal
python3 scripts/seal_ledger.py          # slow: it asks git for each sealed file's history
```

The generator's two runs at this landing are in `verification/ledger_runs.txt`.
