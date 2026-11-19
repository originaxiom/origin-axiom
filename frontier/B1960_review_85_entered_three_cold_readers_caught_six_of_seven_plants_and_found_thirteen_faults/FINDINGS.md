# B1960 — Review 85 entered: three cold readers caught six of the seven plants and found thirteen faults in main's own arcs

**Verdict: PROVED (a process arc).** Main, 2026-11-19. Register row P-877. 0 of 19.

## Seen first

- **Swept:** `VERDICT topic-sweep /Review 85|plant|reading copy|cold reader/: 46 of 1701 arcs on main match (NEGATIVE 1, OPEN 2, PROVED 42, RETRACTED 1); 63 register rows match (DECLINED 1, DONE 24, QUEUED 38)`.
  These are the earlier reviews' entries and their rows; this arc is the next of them and copies Review 84's method
  (B1958).
- **The literature:** none applies; this is a review of the record's own window.

## Why this review ran when it did

- **The gate fired a fourth time.** Main's landing of 2026-11-19 (three debts: P-540, P-517, P-542) was the fortieth
  commit since Review 84's anchor 1fc1e224e, and its push was refused. Main had not counted the commits before
  landing. That is its own rule, and Review 84's action item R84-4. A summary of the session's context had dropped the
  count, and the pre-landing commands did not carry it.
- **No waiver was asked.** Main ran the review. The refused commit, 49c7bdf08, stayed local and is the anchor of this
  entry.

## What was read

- **The window:** 1fc1e224e to 49c7bdf08, 40 commits on the first-parent line, two arcs with a verdict: B1958
  (Review 84's own arc) and B1959. The rest of the window is the claims register's landings (B1957, open; harvest rows
  1904 to 1974), two computations on main's frame D1 (P-871, P-873), P-528's note and the three debts.
- **The sample, drawn by the tool from the anchor:** B1958 and B1959, each read in full. A third part was added by
  main: the window's checks of 2026-11-19 (P-517's decode, P-540's pairing source, P-542's midpoints, P-528's note on
  I-26, and B1957's FINDINGS block for rows 1958 to 1974).
- **The reading copy:** the paths the three parts read, at 49c7bdf08, with seven planted faults
  (`verification/plants.json`; its sha256, 9408f5f7…, was fixed before the readers started, and the file was kept
  outside the copy's folder). A plain folder, not a branch: the push was blocked.
- **The readers:** three sessions of main's own model family, each started cold with the same brief and none of
  main's conclusions. Reader A took B1958 and Review 84's entry, reader B took B1959, and reader C took the window's
  checks of 2026-11-19. Their reports are `verification/READING_A.md`, `READING_B.md` and `READING_C.md`, as
  delivered.
- **This is weaker than Reviews 82 and 83,** whose readers were sessions of the other model family. That reading of
  this window is owed (R85-4, with R84-2).
- **Quotations** (`verification/quote_check.py`, run file beside it): all 19 are in the file their finding cites, and
  17 are within two lines of the line cited. The script is B1958's, re-pointed at 49c7bdf08; it now also reads a
  report's last block, which has no heading after it.

## The plants

**Six of the seven were caught.** The miss was a wording plant.

| plant | where | what was planted | kind | caught by |
|---|---|---|---|---|
| P1 | B1958 | "the other twenty" → "twenty-one" | number | A1 |
| P2 | B1958 | "This is weaker than Reviews 82 and 83" → "as strong as" | wording | **missed** |
| P3 | B1959 | β = 0.572 → 0.527 | number | B7 |
| P4 | B1959 | "No novelty is claimed" → "This is the first proof of the statement" | wording | B2 |
| P5 | B1811 | a₀ against F₆: 2.352 → 2.532 | number | C1 |
| P6 | B1667 | 4.4 × 10⁻³ in L_2 → 4.4 × 10⁻⁴ | number | C5 |
| P7 | B940 | "with I, σ₁ or σ₃ in place of σ₂ it does not" → "with σ₁ in place of σ₂ it does too" | wording | C4 |

P2 contradicted R84-2 in the same entry and the page's own "weaker" elsewhere. Reader A said it could not read the
arcs B1958 cites, which were outside the copy, and read for numbers and counts. A wording plant against the page's own
other lines was not caught.

## The findings

Nineteen: six are the plants. Main checked each of the other thirteen on its own tree, and **each is right**. Each is
mended in this entry. Two of them (B6, B8) are mended by making the words match the lock; the lock itself owes K5 and
K6 (R85-3).

### In main's mathematics pages

| finding | what was wrong | the mend |
|---|---|---|
| B1 | B1959 called Lockhart and McOwen's theory of cylindrical ends "the frame". The cusp is not a cylindrical end: its circle shrinks, and only the zero-frequency part has that form | the page: cited for orientation, not used; the papers were not read |
| B3 | B1959's form bound (1/4 + ℓ²c_j)‖u‖² holds for sections supported in the cusp, as Persson's formula needs, and not on the half-line with a free cut. K2's eigenvalue 0.9031 under the threshold is such a state | the page |
| B4 | B1959's zero-frequency step used an interior maximum where the supremum could be approached at infinity | the page: a barrier e^(γt) with γ in (δ, 1 + β + δ), which (∗)'s operator maps to a positive multiple, and ε → 0 |
| B5 | B1959 gave the bound's growth as the reason K is increasing beyond T₁; the reason is that each V_m is | the page |
| C2 | B933's DESIGN § 5a still called the J argument proven. J commutes with D (S274), and the symmetry comes from P-540's U | a dated note in B933's FINDINGS: DESIGN.md is sealed, and main's first mend, an edit of it, was refused by the seal gates |
| C3 | B933's new note said spec(D) = −spec(D) holds "as a theorem". The closing operator step is main's derivation from the identities `pairing_source.py` checks | the note |

### In what main's pages say main checked

| finding | what was wrong | the mend |
|---|---|---|
| A2 | B1958 said four of Review 83's items were closed. One was (R82-4), as the entry and its eighteen carried items say | the page |
| A3 | B1958 said "four statements" and named three. The fourth is C10's coefficients | the page |
| A4 | R84-1's counts (238; 136 and 114) were taken at different moments and not said to be. At the commit that landed the pass the register held 264 VERIFIED records, 138 of them the web lane's | a dated bracket on the item |
| A5 | B1958 and the entry gave only the file-level count of quotations (27 of 27). At the cited line it was 23 | both |
| B6 | B1959's table said each formula had "the change that breaks it". K4 and K7 have one in the script and K1, K3 and K4 in the lock; K2, K5 and K6 have none | the page and the script's docstring |
| B8 | B1959's lock said it recomputes "the computable steps of the proof, each with the change that breaks it". K5, K6 and K2's eigenvalue count are not in it | the docstring; R85-3 owes them |
| C6 | B1957's bullet for row 1968 gave 7 verified and 1,210 conditional of 1,248 and left out the 31 noted | the page |

## What it teaches

- **The same fault as Review 84's, again in main's newest pages.** A page that says more than the output behind it.
  That covers a frame that does not fit, controls that are not there, "as a theorem" over a derivation, and a note
  left in one file and not the other. This is R81-7's candidate class, still not entered in the error ledger.
- **A proof read cold had a gap at infinity** (B4). The gap is repairable, and it is repaired here. A proof checked
  only by numbers on examples does not show such a gap; a reader of the argument does.
- **Wording plants are the weaker catch.** Across Reviews 84 and 85 all nine number plants were caught, and four of the
  five wording plants. The one missed here contradicted other lines of the same page, which a reader looking for
  numbers did not hold together.
- **A mend can break a seal.** Main's first mend of C2 edited B933's sealed DESIGN.md, and the seal gates refused
  the landing. A sealed arc takes corrections in its FINDINGS only.
- **The count before landing failed the fourth time** because it lived in memory and not in the commands. It is now in
  the pre-landing commands themselves (R85-1).

## The loop

Review 84's block held 23 items: R84-1 to R84-5 and eighteen carried. None is closed in this entry. R84-4 failed again;
its next step is written in R85-1. The ten items of the R81 lineage are past their fourth carry with no disposition.
The entry in `docs/progress/REVIEWS.md` states each line.

## Files

- `verification/plants.json`, `plants_sha256.txt`: the seven plants, sealed before the readers started.
- `verification/READING_A.md`, `READING_B.md`, `READING_C.md`: the readers' reports, as delivered.
- `verification/quote_check.py` and `quote_check_run.txt`: each quotation held at its cited path in the reading copy,
  rebuilt from 49c7bdf08 and the plants.

0 of 19.
