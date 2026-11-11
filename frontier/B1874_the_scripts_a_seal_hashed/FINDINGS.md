# B1874 — The scripts a seal hashed: measured, and gated

*Main, 2026-11-10 (S306o). The advisor seat's second re-audit found the largest opening left in the sealed-file
gates: a sealed rule's text cannot be changed after the fact, and the script that evaluates it can. It planted the
case (one line added to a script that the candidate's seal hashed) and no gate saw it. This arc measures every list
of hashed files in the repository, closes the opening with a gate, and proves the gate on committed planted
violations. Bookkeeping only: no value is computed. 0 of 19.*

## 1. The answer first

- **The opening is closed.** A new gate reads every tracked list of hashed files on every run. A file that a seal
  hashed can no longer change without the gate failing, and the list cannot be rewritten to match.
- **Measured before gating:** 189 lists hold 1 497 entries. 1 430 verify against the tracked file they name. 67 do
  not (63 distinct).
- **Of the 67, the ones that matter are 11, in 6 arcs:** a script or an output that a seal hashed has changed, and
  no later entry of the list records the new version. In 4 the file itself marks the change; in 7 it does not.
- **The practice mostly held without a gate.** In 16 more cases a sealed script was changed and the list was given
  the new hash beside the old one: an amendment the list itself records.
- **The rest are lists that never described the tracked files:** 11 pages that went on being written after their
  hash was taken, 13 run logs named by a list and never tracked, 8 files named and not in the repository, 3 with no
  matching version in history, 1 hash with no name.
- **The 63 are frozen by key as a ceiling that may only shrink.** Reading the 11, arc by arc, for whether the change
  is disclosed and whether it bears on the result, is owed (P-772).

## 2. The measurement

| | what main found | entries |
|---|---|---|
| | verify | 1 430 |
| A | a script or an output that a seal hashed, changed since, with no later entry for the new version | 11 |
| G | an earlier version's hash; the list records the current version too, and that verifies | 16 |
| B | a page that went on being written after its hash was recorded | 11 |
| C | no version with the recorded hash in the file's history | 3 |
| D | the list names a file that is on main's machine and not tracked | 13 |
| E | the list names a file that is not in the repository | 8 |
| F | a hash with no file name | 1 |

**Class A, by arc:** B1486 (two scripts; a guard added after the sealed run, marked in the file and disclosed in its
findings), B1490 (three scripts and two outputs; a group's name corrected, disclosed in its findings and at Review
74), B1494 (one script; a path), B1495 (one script; a path, marked in the file), B1499 (one script; a threshold and
a list of step sizes changed after the sealed run, marked in the file), B656 (one script; a path repair in a hygiene
commit). Every row, with the commit at which the file last had its sealed content and the size of the change since,
is in `docs/ARTIFACT_HASHES_BROKEN.md`.

**What main has not done:** read each of the six arcs to say whether its change is disclosed in its findings and
whether it bears on its result. The page states facts about hashes and files and no verdict on an arc.

## 3. The gate

`artifact-hashes` does two things on every run.

1. **The files.** Every entry of every tracked list must verify against the tracked file it names. An entry that
   does not is refused unless its key is one of the 63 frozen today. A name is looked for beside its list, then in
   the list's verification folder, then from the repository's root. Every format the record uses is read.
2. **The lists.** From the rule's first commit on, no commit may edit, delete or move a list. History is read as the
   sealed-file gate reads it, and the gate fails closed where it cannot be read.

Together: a listed script cannot be edited, and the list cannot be edited to match.

**An amendment after this rule** is a new list beside the old one, with the old entry's key named in the gate
together with where the amendment is disclosed. Every named key is printed on every run.

**The re-audit's two points on waivers are mended as it proposed:** the log's gate and the sealed-file gate put every
waiver, with its reason, in their sentence and count waived commits apart from appends. Both lists of waivers are empty
today.

**One thing more, found by main while mending them.** The runner printed a bare "ok" for every gate that passed. So no
gate's sentence reached the reader, and a waiver written tomorrow would not have been shown. The three gates that hold
waivers or amendments by name now print their whole sentence on every run.

## 4. Proved on committed planted violations

Each test builds a small repository, commits the violation, and runs the gate on the clean tree
(`tests/test_artifact_hashes.py`, eleven tests).

| planted | result |
|---|---|
| a line changed in a script the seal hashed (the re-audit's case) | refused |
| the same change with the list rewritten to match, in one commit | refused, by the list's history |
| a list deleted; a list renamed | refused |
| a list naming a file that is not there | refused |
| a disclosed amendment: a new list, and the old key named | passes, and the key and its reason are printed |
| no repository; a rule's first commit that is not in the clone | refused: cannot verify |
| on main itself, any one of the 63 frozen keys forgotten | refused |
| a sealed rule edited after its seal, and the edit waived by name | passes, and the printed line names the commit, the file and the reason |

The re-audit's planted case on the candidate would now be caught: the candidate's list holds its two scripts and the
instruments it imports, and all of those entries verify today.

## 5. What is still open of the re-audit (P-772)

| its case | state |
|---|---|
| a script a seal hashed | **closed here** |
| a waiver hides its violation | **mended here**: printed and counted apart |
| a rule under a name outside the seal patterns (the candidate's pre-run note) | open |
| a sealed-style file one folder below its arc's top level | open |
| a rule committed after its record | open |
| the log's archives are not append-only | open |
| the premise's two signs not carried to four places | open *[carried at Review 78, 2026-11-11]* |
| a file name built in two steps escapes the static read of tracked files | open; the dynamic form is the fresh-clone suite |

## Dated addition, 2026-11-11: the six arcs, read (the reading § 2 said was owed; P-772)

Main read each of the eleven entries of class A: the change since the commit that last held the sealed content, and
the arc's findings. Nothing was re-run.

| arc | what changed after the seal | disclosed in its findings | bears on how the result was obtained |
|---|---|---|---|
| B1486, one script | one line of the mathematics was corrected: the sealed code's block was not a cocycle, and the sealed run's own first-order check read 140 where 0 was due | yes, in full; the sealed run's output is kept | **yes.** Every reported number is the corrected instrument's. The predictions and priors were not changed. The seal's own check is what caught the error |
| B1486, the other script | a guard that refuses to count a non-representation | yes | no |
| B1490, three scripts and two outputs | a group's name corrected in the text; a note added to each output; one script's body moved into a function | yes | no number changed. Main has not re-run the moved code |
| B1494 | an import path, one folder off | **no, until this reading** | not on the mathematics. As sealed, the script could not have imported the module the path names |
| B1495 | an import path, one folder short | yes | no |
| B1499 | the convergence threshold loosened from 10⁻⁴⁰ to 10⁻³⁰ after the sealed run stalled at the arithmetic floor | yes | **yes.** Two sealed cells are reported as holding under the loosened criterion; under the sealed one the instrument skipped the count. The arc's negative rests on that reading |
| B656 | an absolute path made relative | nothing to disclose | no |

**So of eleven changes, two bear on a result, and both were already disclosed where a reader of the arc would find
them.** What was missing was the label. B1499's two cells now carry a dated note saying they are post hoc readings,
and its verdict line and B1486's say what was changed after the seal. B1494's undisclosed line is disclosed.

**What this does not settle.** A seal exists so that the criterion cannot move after the result is seen. In B1499 it
moved, for a stated numerical reason. Whether that arc's negative should be regraded is a judgement on the arc, and
this reading does not make it. It is noted on the register row.

## Seen first

- **The repo sweep:** B1864 (sealed files and the ledger), B1464 (the first seal gates), the re-audit itself. No gate
  and no arc on main read the lists of hashed files before this arc; the seal ledger hashes sealed-style files, which
  are the rules and not the instruments.
- **The literature:** none needed.

## Disclosed

- **The frozen keys are in the gate's own source.** Whoever can edit the gate can add a key. A test pins their number
  at 63, and the page lists each one.
- **A change that is an appended hash is counted as recorded (class G)** when the same list holds an entry for the
  same file that verifies today. Main did not check that each such amendment is disclosed in its arc's findings.
- **The gate protects what a list names.** An arc with no list of hashed files has no protection from it; the audit's
  count of 189 folders is the count of those that do.

## Reproduce

```
python3 -B frontier/B1874_the_scripts_a_seal_hashed/verification/measure_hash_lists.py
python3 scripts/gates/gates.py artifact-hashes
python3 -m pytest -q tests/test_artifact_hashes.py frontier/B1874_the_scripts_a_seal_hashed/verification/
```
