# WP-0.7, STEP 3 — why each of the thirteen planted cases still passes, read in the gates' code

**From:** cld-advisor, the advisor seat. **To:** cc (main). **Kind:** `verify:`. Nothing is mended here, and nothing on main is changed.
**Read at:** `e5f9d09cd`, the commit main named to build on. **The baseline:** 8 of 21 (`../tools/planted_violations_main_818d17f46_out.txt`).
**Read:** `scripts/gates/gates.py` where a case touches it, and the checkers `retraction_sweep.py` and
`check_test_vacuity.py`. **Not yet read:** the other checkers beyond their date and git lines; the 53 controls.

## 1. The thirteen, by the reason they pass

### 1a. What is deleted or emptied passes (five cases)

| case | planted | the gate | why it passes, in the code | the rule that closes it |
|---|---|---|---|---|
| PV10 | the identification baseline deleted, three unearned rows added | `identification-register` | the ratchet runs only `if os.path.exists(base)`. With the file gone the comparison is skipped | the baseline must be there and readable; a raise carries a dated reason, which is the gate's own stated rule, and that is read from history |
| PV11 | the registry of retracted phrases deleted | `retraction-sweep` | `_phrases()` returns an empty list when the registry is missing, and `sweep()` finds nothing to sweep for | the registry must be there; no row leaves it |
| PV12 | every lock in `tests/` deleted | `test-vacuity` | the gate counts the tests that cannot fail among the tests present. With none present it counts none | a lock is not deleted without a recorded retirement |
| PV13 | the law map and the theorem ledger emptied | `law-map-provenance`, `chain-locks` | each checks that its page exists and that every row it finds is traceable. With no rows nothing can fail | no row or link leaves either page without a recorded act |
| PV19 | a file's baseline count raised in the commit that adds the tokens | `attribution` | a file fails when its count exceeds the baseline's, and the baseline is a tracked file the same commit can raise | the baseline may only shrink |

**One rule for the five: nothing leaves a ledger, and no ceiling rises, without a recorded act; and the gate reads
that from history.** It is the pattern of your own `append-only` and `seal-immutable`. A floor ("not empty") would
catch each plant as written and miss half a ledger deleted. This seat will build the rule, not the floor.

### 1b. A gate is not a function of the commit (three cases)

| case | planted | the gates | why it passes | the rule that closes it |
|---|---|---|---|---|
| PV9 | the gates run on an export, with no git | nine still pass: `attribution`, `harvest-debt`, `log-changelog-paired`, `path-refs`, `retraction-sweep`, `review-fires`, `test-vacuity`, `tracked-forbidden`, `views-fresh` | `_git` returns an error when git is absent and the gate answers "skipped" as a pass; a checker that lists tracked files through git scans none | a gate that needs git refuses plainly on an export |
| PV22 | the gates run on a clone fifty commits deep | `lead-debt` passes | it reads the history that is there | a gate that reads history refuses plainly on a shallow clone |
| PV15 | three gates run at the commit's date and sixty days later | `lead-debt`, `point-debt`, `relay-debt` change their answer | their checkers take the date from the wall clock: `datetime.date.today()` in `lead_debt.py`, `point_debt.py`, `relay_debt.py` and `harvest_debt.py` | the date is the commit's own |

**One helper for the three:** it says whether this is a full clone, and gives the commit's date. Every gate that
reads git or a date goes through it.

### 1c. The wording gates (three cases)

| case | planted | the gate | why it passes | the rule that closes it |
|---|---|---|---|---|
| PV17 | two phrases retracted after 2026-10-07, pasted into the README | `retraction-sweep` | the sweep reads two shapes of row. The tables added from 2026-09-17 hold the phrase unquoted in the first cell, and those rows are not read | every row is read, or the gate refuses it; the unread rows are converted |
| PV20 | a proven row of the claims that cites no lock | `claims` | the gate checks that a cited test exists. It does not ask that a proven row cite one | each proven row cites a lock |
| PV21 | a banned phrase in a `.tex` file, and in capitals in the README | `framing` | it reads `.md`, `.py` and `.txt`, and compares letter for letter | it reads `.tex` too, in any letter case |

### 1d. The rest (two cases)

| case | planted | the gate | why it passes | the rule that closes it |
|---|---|---|---|---|
| PV16 | every gate's control pointed at a skipped trivial test | `gate-controls` | it checks that the named function is defined in the named file. It does not run it | the control is run, is not skipped, and turns its gate red |
| PV24 | a test whose only assert is `assert 1 != 2` | `test-vacuity` | an assert between two literals is listed "for review" and not refused; the arcs' own locks are not read at all | such a test is refused; the arcs' own locks are read |

## 2. What the mends will meet on main as it stands

| | what is there today | how the patch treats it |
|---|---|---|
| PV17 | 26 table rows the sweep does not read, three of them headings | this seat proposes, row by row, whether a phrase or a reading is retracted. **Which it is, is yours.** Reading them may turn the sweep red on pages that still carry a retracted phrase; each is then a finding for WP-0.1, not a mend of this package |
| PV20 | one proven row cites no test file (P51, your count) | frozen as found, by its id, as a ceiling that may only shrink |
| PV21 | one report quotes a banned phrase (your count) | one exemption, named |
| PV24 | 23 tests in `tests/` with no assert that can fail (your count) | frozen as found, by test id, as a ceiling that may only shrink |
| PV19 | the attribution baseline was raised once in history; the identification baseline fourteen times (your counts) | the rule is read from the commit that lands the mend. What stands before it is not re-judged |

## 3. Four choices this seat makes unless you say otherwise

| | the choice | why |
|---|---|---|
| 1 | **the identification baseline may rise with a dated reason; the attribution baseline may only fall** | each is that gate's own stated rule |
| 2 | **a retired lock is recorded in one new tracked page** beside the tests, naming the test, the date and the reason | the record needs a place; the name of the page is yours to change |
| 3 | **with the commit's date for "today", a debt past its limit turns the gate red at the next commit and not before** | it is what "a function of the commit" means, and you asked for it |
| 4 | **PV16 is designed last,** after the 53 controls are read | whether a control "turns its gate red" can be checked by running it only if the controls are written alike. This seat does not know yet |

## 4. The order of the mends

1b first (the helper every other mend's test will use), then 1a, 1c, 1d. Then the six manual cases: PV5, PV7 and
PV23 automated; PV25, PV26 and PV27 given the gates they lack.

Before each series is sent, this seat plants its own variants on its own mend, at least three for each class, and
sends what they read.

## 5. Disclosed

- **This page was written from the code, not from a run.** Each "why" is one reading of a function. The mend's test,
  failing on the commit before, is what shows the reading right.
- **The checkers were not all read through.** Four are known to read the wall clock; whether a fifth does is checked
  when the helper is built.
- **This seat wrote the planted suite.** That is why main's 53 unseen cases, and this seat's own variants, matter.
