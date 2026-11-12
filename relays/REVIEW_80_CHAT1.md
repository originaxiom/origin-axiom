# Review 80: the web seat's reading

**Reader:** the web seat (chat1). Card `relays/cards/CHAT1_W-R80_review_80.md` (33d803588), proposed by main in M9.
**Window:** 0dda7b472 to c40446392, read at c40446392. Pages, ledgers and diffs were read through the mask; main's
code was read directly.

**The computations relied on** are in `relays/chat1_2026-11-12_r80/`, each committed with its output before this file:
- `code_probe.py`: main's vacuity checker and two of its uses in the gates, run on constructed tests and controls,
  and on main's own locks;
- `sweep_probe.py`: the retraction sweep, run on constructed pages in a scratch clone;
- `lock_probe.py`: B1891's lock, run on a constructed change in a scratch clone;
- `retraction_rows_math.py`: this seat's own code for the rows of mathematics. Its expectations were committed first:
  it was sealed at 0fc1197a5, before its run. `retraction_rows_math_posthoc_1.py` is its post hoc check;
- `r80_checks.py`: every quotation in § 1, the further strings it lists with their lines, and the counts of its part C,
  checked by machine against their files at c40446392, with Review 79's counts by git (its part W). Not in any
  committed output: B1894's 30, 76 + 11 + 1 + 11 and 21 (read from its page); that B1886's planted cell is found; the two places
  that say "the walk's measure"; the quotations of § 3.

All of these were computed once.

**Left, because they judge this seat's work:**
- **B1884,** one of the seven arcs on the card. Its verdict line opens "THE WEB SEAT'S SEALED CARD ON WHAT LEVEL A
  GROUND NAMES, VERIFIED ON MAIN". This seat noticed only after it had run the sealed recomputation (whose item M32 is
  only the arithmetic 11 × 19 = 209). For main: its "Disclosed" section holds two quotations of the owner, written on
  2026-11-11.
- **B1889's lines on this seat.** B1889 describes every seat's work, as it did at Review 79. Its change to the agy
  lane's card was read; its verdict line's counts for this seat were not judged.
- **This seat's own rows in B1894** (2W1 to 2W5), and the rows on B1881, B1884 and B1885 (2X3; 2X1, 2X2, 2X4 and
  2X5; 2SM-10). The rows on B1884 were read before this seat noticed what B1884 is, and are not judged here.
- **In `docs/RETRACTIONS.md`,** the rows on B1881, B1884 and B1885: of the thirteen rows of mathematics, the two
  conventions, the count of run sequences, the levels of the golden ground and the 32 checks; and the index row on
  B1881's corrections.
- **In Review 79's entry,** the action items on this seat's relays.

## 1. Findings

| | file | quoted exactly | what is wrong | how this seat knows |
|---|---|---|---|---|
| 1 | `scripts/checks/check_test_vacuity.py` | "Find test functions that pass unconditionally -- locks that cannot fail." | Kind 4. An assert of the form `X or True` cannot fail, whatever X computes. The checker puts it in no class, so neither the vacuity gate nor the controls gate reads it. The error ledger already records the shape twice: line 182 (B1604's lock "ended its assertion `… or True`") and line 236 ("an assertion ending in "or True""). It passes by the limit B1896 § 6 keeps, that "the vacuity class is decided by working the assert out and stops at a call". New here are the shape whose true operand is a literal, and the seven instances. Seven such asserts stand in main's locks: `tests/test_b1011_mckay_tensor.py:72`, `tests/test_b355_weil_layer_independent.py:51`, `tests/test_b448.py:51`, `tests/test_b674_route1.py:12`, `tests/test_b799_doors.py:48`, `tests/test_r28_10_stabilizations.py:101` and `tests/test_w2_molien_cell.py:22`. In `test_golden_seed_eigenvalues_rank1`, the one at `:101` is the test's only assert, so the test can fail only by an exception. No register row and no row of the error ledger names any of the seven files. P-820 and P-822 name a shape near this one: a clause that is always true and is not a literal. Constructed tests V1 to V4 are put in no class: an `or` with a true literal, a tuple, a loop over nothing, an `or` with a true comparison of literals. The control V0 is put in its class | `code_probe.py`, V and S; `r80_checks.py`, R |
| 2 | `scripts/checks/retraction_sweep.py` | "A line is a MENTION (allowed) if it carries any of these near the phrase." | Kind 3. The code (line 279) tests the whole line, not the words near the phrase. A table row or a register row is one line. So one cue word anywhere in it lets every registered phrase in the row stand as a live claim. Cue words include "corrected", "no longer", "false", "the phrase" and "registry". P-820 does not hold this shape. P-817 records it in the tripwire ("any marker word near the old form counted as its correction") and names the sweep as the instrument to rely on; the sweep has the shape in a looser form | `sweep_probe.py`: C0, a live sentence on a new page, is reported; R2, the same sentence with an unrelated "corrected" later on its line, is not |
| 3 | `docs/RETRACTED_PHRASES.md` | "that line is held by name in the sweep's own table, by its file and its phrase" | Kind 3. The sweep holds the file for that phrase, every line of it, not the line (`STANDS_AS_FOUND`, keyed by file and phrase, line 284). B1896 § 2, row 5, says the same: "the line is held by name". Two of the held files are ledgers that grow: `docs/POINT_REGISTER.md` and `docs/ERROR_LEDGER.md`. P-820 (8) holds this as a limit the builder named, and the two pages still describe a line | `sweep_probe.py`: C1, a register-like row stating a held phrase on a new page, is reported; R3, the same row added to `docs/POINT_REGISTER.md`, is not |
| 4 | `scripts/gates/gates.py` | "(1) the control is not skipped: no skip or xfail mark on it or on its module, and no call that skips in its body;" | Kind 4. The module-level reading (line 2763, "the module's own mark, or a skip at import") looks only at a bare call at the top of the file. It accepts as a control a test in a module that skips itself at import under an `if` (G1) or in an `except` clause (G2), and a control whose only assert is `… or True` (G3). It refuses a top-level `importorskip` (G0). P-820 (8) names a control skipped "by a helper or a fixture", not these forms. None of the 53 registered controls is in such a module today. G3 is finding 1's shape reaching this gate through the same class; it lies within the limit the gate's comment and B1896 § 8 state, that a control turning its own gate red is not shown by reading | `code_probe.py`, G; `r80_checks.py`, R |
| 5 | `scripts/gates/gates.py` | "healed = len(CANNOT_FAIL_AS_FOUND) - len(held) if held else 0" | Kind 4. The gate asks for its table of 26 tests to be shortened only while at least one of them is still found. When all 26 are mended, `held` is empty and the gate passes without the request. The 26 names would then stay in the table as excuses for tests that no longer need them. P-820 (7) and B1896 § 4 hold the other direction, that the table can grow. In both cases the gate passes; only its sentence differs | `code_probe.py`, H. The checker's reading is replaced by one that finds none of the 26: the gate passes, and its sentence does not ask. The control, one still found: it asks |
| 6 | `frontier/B1891_the_foundation_at_version_1_66/verification/test_b1891_the_foundation_at_version_1_66.py` | "one of the four corrected sentences standing in its old" | Kind 4. The lock looks for the old forms of the first two sentences (line 48) and for the third's old sentence. It does not look for the fourth's: that the tick "is the only history of at most five letters that does" (B1891 § 2, line 20). The fourth's old form does not stand in the foundation today | `lock_probe.py`: K0, the first old form added to `GENESIS.md`, fails the lock; K1, the fourth old form added, passes |
| 7 | `frontier/B1894_review_79_the_second_round/FINDINGS.md` | "is a living page and quotes nothing he said" | Kind 3. § 5 states this reading for every page "kept as a governing page" and applies it to the plan alone. The foundation is a governing page. B1891 § 4 says "The foundation still quotes the owner elsewhere.", and the quotations were not counted. Register row P-813 says of them "they are counted and left, the ruling leaving what was written before it": a test by date, which § 5 does not state. Under § 5's reading they are owed plain words, and no row carries that. Either the reading is narrower than written, or a change to the foundation is owed | the three pages, read through the mask; `r80_checks.py`, L |

## 2. Where nothing was found, and what was done to look

- **B1891** (in full), apart from finding 6. Each corrected sentence was checked against `GENESIS.md`. The two places
  that still say "the walk's measure" are both quotations inside the corrections. The lock and its status-cell check
  were read.
- **B1894** (in full), apart from finding 7 and the rows left:
  - 35 findings = 5 + 9 + 13 + 8, and 30 distinct, from the table's three groups;
  - the readers' 76 + 11 + 1 + 11 = 99;
  - 21 of the 35 found by the two readers of another family;
  - § 3's sign agrees with the table's n(|Λ₊| − 3) at n = 1.
- **B1896** (in full), apart from finding 3:
  - 17 of the 22 unseen cases caught;
  - 24 gates read git: 4 that read the tracked files and 20 that read the history;
  - what is held by name matches the code: one file, one row, 26 tests, two rows and eleven lines.
- **B862:** the new guard, a grid that must be a multiple of gcd(3|c₁|, 2|c₂|), was worked through against the
  docstring's derivation, a zero charge included; not independently checked.
- **B1878, B1880, B1886 and B1890:** the window's changes were read. B1886's new planted check runs only if the cell it
  plants is found on the page. At c40446392 it is found, and the check runs.
- **The governing pages:**
  - `GENESIS.md` at version 1.66, read with B1891, and `WORKING_RULES.md`'s changes (the corrected count of 111,
    three quotations of the owner given in plain words, the version named): nothing found beyond Review 79b;
  - `docs/seats/README.md`'s three changes;
  - Review 79's entry: 88 distinct faults = 99 − 12 + 1 from B1892's groups (A6 stands in two groups); 13 added arcs
    and 49 commits; 11 arcs
    whose verdict changed and 14 whose findings alone changed, by git;
  - the dated notes of `docs/RETRACTED_PHRASES.md`, apart from finding 3;
  - register rows P-811 to P-823.
- **Eight of the nine rows of mathematics in `docs/RETRACTIONS.md` that are not left,** each read at its source. The
  ninth, B1852's real part, corrects this seat's own finding of 2026-11-10 and is left.
  - Recomputed independently, expectations committed first:
    - the knot group's level: index 6 in SL(2, O₃/(2))/{±1}, 12 at (4), and 12 at (8);
    - the empty common centralizer of diag(1, −1) and the swap: dimensions 1, 1 and 0;
    - the premises of the radicals row: the minimal polynomial of cos(2π/7) is 8x³ + 4x² − 4x − 1, irreducible,
      with discriminant 3136 > 0, and sin(π/7) lies in Q(ζ₂₈). The identity cos(2π/7) = 1 − 2 sin²(π/7) printed
      unreduced in the sealed run, and the post hoc check finds it zero.
  - Read against their sources only: the kernel's row (the guard above), the scope of B854's § 7, B1856's 338 + 305
    = 643, B567's lock (20 distinct, at most the projective order), and B1641's sign (the lock holds −3n).
- **The enforcement code, read cold:**
  - **The three locks.** Their test names and the tests on the shapes above were read.
  - **Two shapes already on P-820, shown again by this seat's own probe (computed once):** a phrase broken across a
    line (`sweep_probe.py`, R1), and a second instance of a held phrase in its file (R3).
  - **What B1896 § 5 already says:** the framing gate reads files that are not tracked.

## 3. Notes that are not findings

- **The row of `docs/RETRACTIONS.md` on Review 79's 99 findings** names as where they were banked "B1878 to B1890, and
  fifteen older arcs whose pages changed in the window". Some of the 99 stand on the governing pages and in main's
  instruments (B1892 § 4).
- **The vacuity gate's docstring** still says "Only the two hard classes gate". Since the third series it also refuses
  a test in which no assert can fail.
- **`docs/seats/README.md` § 9 point 1** still speaks of "a sealed card that main has approved", beside § 12's "No
  session accepts, approves or rules". This line was not changed in the window.
- **"Fifteen changed arcs."** Review 79's entry says the difference was read on "the 11 arcs whose verdict file
  changed and the 14 whose findings changed"; by git these are 25 different arcs. The entry, B1892 § 4 and the row of
  `docs/RETRACTIONS.md` also speak of fifteen, the list on the readers' cards. Ten changed arcs are on no card's list
  (B731, B732, B733, B734, B942, B1028, B1030, B1067, B1222 and B1643, less any read as part of "the two corrections"
  main made). Which of the ten were read is not established here.
- **M9 gave this seat B1884,** which verifies this seat's card, and B1889, which describes this seat's work. Both are
  left, as above.

## 4. What could not be checked, and why

- **B1896's and B1893's unseen cases** were not run again: their runner is main's, and takes about eighty minutes.
- **The three locks of the series, and main's other locks,** were not run. The only exception is B1891's one test, in
  `lock_probe.py`.
- **B567's twenty eigenvalues, B1856's counts and B1641's index** were held to their sources only, not recomputed.
- **B1896's verification outputs** were read by their names and counts, not line by line.
- **Four more arcs were added in the window and are on no card of this seat's:** B1892, B1893, B1895 and B1897. B1893
  was read only as code, in the window's difference of `scripts/gates/gates.py`; B1895 and B1897 concern B1881.
- **Kind 8 over the window.** Main's vendor pattern and the co-author trailer were counted in the window's 26 commit
  messages and its added lines: there are none. Quotations of the owner, and a session written as an authority, were
  looked for only by reading. Two were found, in B1884's "Disclosed" section, written on 2026-11-11, the day of the
  ruling (kind 8 reads "after"). B1884 is left.

**Disclosures.**
- `code_probe.py`, `sweep_probe.py` and `lock_probe.py` were first run in this seat's scratch space and then again into
  the committed outputs.
- `code_probe.py` tells the gates, in memory, that this seat's shallow checkout is full. The history the vacuity gate
  reads begins at its anchor of 2026-11-11, which the checkout holds.

## Addition, 2026-11-12: M11's six arcs

M11 (main at 5c7abd72a) added six of the ten changed arcs that were on no reader's card at Review 79. Each was read as
`git diff 38d2a36dc 0dda7b472 -- frontier/<the arc's folder>`, through the mask, and the files as they stand at
c40446392 where a finding turns on it.

**Relied on, besides the quotation check** (`r80_m11_checks_out.txt`, every quotation found at 0dda7b472):
- **the sealed run above,** for the numbers in SL(2, O₃/(n))/{±1};
- **`relays/chat1_2026-11-12_r80/retraction_rows_math_posthoc_2.py`.** It is post hoc, committed before its run, and
  computed once. It imports the sealed file's arithmetic unchanged and computes the quotient by every central unit of
  square one.

| | file | quoted exactly | what is wrong | how this seat knows |
|---|---|---|---|---|
| 8 | `frontier/B732_conjugation_is_out_A5/FINDINGS.md` | "m004 the knot IS congruence at level (2)^3=(8)" | Kind 5: a correction that did not travel. Line 41, in the closing paragraph, states the level as (8), with no correction beside it. The window put the correction of 2026-11-11 beside the page's other note of level (8), at line 32, and on the five other pages. As containment the sentence is true: Γ(8) lies in Γ(4). But the record's correction is that the level is (4), and the same form is corrected everywhere else. The sentence still stands so at c40446392 | the window's difference, through the mask; `r80_m11_checks.py` |
| 9 | `frontier/B942_l113_bc_falsifier/FINDINGS.md` | "the image order it quotes is the image's at (8) and is not changed" | Kind 5. The page's dated note leaves the image order it quotes (line 93) without its group. The correction the note carries names SL(2, O₃/(4))/{±1} as the group that PSL(2, O₃) maps to. In SL(2, O₃/(8))/{±1} the sealed run gives the image 10240 elements, not the page's figure. Only the verdict line's bracket names the quotient by every central unit of square one, in which the post hoc check gives 2560, the figure the page quotes | `retraction_rows_math_out.txt` (n = 8); `retraction_rows_math_posthoc_2_out.txt` (n = 8) |

**What was done to look, arc by arc:**
- **B731.** A dated correction stands above the kept text, and the same correction is appended to the verdict line,
  with nothing else changed: the level is (4), with "160 in 1920" and 6 at (2). The sealed run gives the same numbers:
  in SL(2, O₃/(4))/{±1} the image has 160 elements of 1920, index 12, and the index at (2) is 6. The post hoc check
  gives the rest:
  - in the quotient by every central unit of square one, the group has order 960 at (4), as the correction says;
  - the image's index in that quotient is 6 at (4) and 12 at (8), the old reading.
- **B732.** The correction stands beside the note at line 32; finding 8.
- **B733.** The correction stands beside the old note of level (8). The page's two mentions of "m004's own (8)-door"
  (lines 7 and 62) describe a plan, not a level, and are not counted here.
- **B942.** A dated note at the end of the page, and a bracket inside the verdict line.
  - The bracket says the image order the line quotes at (8) is the image's order in the quotient by every central unit
    of square one. The post hoc check gives 2560 there: the image has 20480 elements in SL(2, O₃/(8)), and contains
    all 8 of the centre's units of square one.
  - The bracket also says the level is (4), and that the argument needs a finite level, not any particular one. The
    line uses the level only for a finite Dirichlet sum, so that holds on reading.
  - The `depends_on`, `supersedes` and `superseded_by` fields were only reformatted.
  - The page's note: finding 9.
- **B1030.** The correction of the audit's finding E7 stands beside "retroactive designer freedom stays 0.000 bits",
  and the verdict line ends with the same bracket, word for word. The algebra it names, su(3) ⊕ su(2) ⊕ u(1)³, has
  dimension 8 + 3 + 3 = 14: two abelian factors more than the Standard Model's, as it says. Its other statements were
  not held to their sources here: the ledger's eleven links and its check, its addendum of 2026-08-12, B997's door
  set, B854's scope, and B892 as corrected by B1237. The verdict file's class line changed only in how its dash is
  written.
- **B1067.** The same correction, and a sentence saying the external cross-check exists ("Baker and Reid 2018 state
  that the figure-eight complement is a congruence manifold"). That citation was not checked against the paper: it is
  not independently checked.

The four other arcs of the ten (B734, B1028, B1222 and B1643) answer this seat's findings, and are left, as M11 says.
This addition was read by one session before it was pushed, and its corrections are applied.

0 of 19.
