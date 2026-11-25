# B1981 — The canonical order-6 shell read on frame C at order 30 picks no class: averaged over the shell, the frame loses its 2–3 hierarchy and its alignment, and the sectors become alike

**Verdict: NEGATIVE, PROVISIONAL (the shell as P-845's rule, in either declared reading, as sealed; no second computation yet).** Main, 2026-11-25. Data-free.
Register row P-845. **0 of 19.**

*Dated relabel (2026-11-25, P-883, at the author's word):* by THE_WEAVE's test (all threads, none chosen; defined by the joint
action; about all threads at once), this is a **thread** result, not a weave result: frame C over blocks cut by m004's act's line. It was first labelled "the weave (the order-30 rates)".

## Seen first

- **The claim tested:** agy-exp's `CLAIM_2026-11-24_canonical_e6_prim_lepton_down_split.md` (256f4294c, read at source;
  harvest row 2000).
  - The 24-point primitive order-6 shell E_τ[6]_prim is preserved by all of GL(2, ℤ).
  - Averaged uniformly in a two-doublet construction, it breaks the lepton–down tie.
- **The web seat's CHK-2 (§ 0 item 6, harvest row 1997):**
  - the shell is the set of the 24 values of the 6-part of B1976's points;
  - averaging over it is one rule for P-845, and the uniform weight is an import.
- **The record:**
  - B1979: twelve converged classes;
  - B1978: the act's orbits;
  - B1944: the average over the surface washes out the hierarchy.
- **Swept:** `VERDICT topic-sweep /E_tau\[6\]|order-6 shell|primitive order-6|shell average|average over the 24|24-point/: 1 of 1720 arcs on main match (PROVED 1); 1 register rows match (QUEUED 1)`. The matches are B1928 and P-845, neither on the shell in frame C.
- **The literature:** none needed. The question is a computation in the record's own frame.

## Custody

- **The card** (`CARD.md`) and the script (`verification/shell.py`) were drafted before B1979 landed. They were put in
  the tree renumbered from B1980 to B1981, unchanged otherwise, and hashed before the run (`EXPECTATIONS_HASHED.md`).
- **There was no separate seal commit,** the same custody as B1976 and B1977.
- **One post hoc script,** labelled: `g_precision_posthoc.py`, below.

## The results (`verification/shell.py`, `shell_run.txt`, `shell_run.json`)

- **Blocks.** At each of the 4 points p₅ of the act's line, the 24 points p₅ + p₆ form a block; a fifth block is all 96.
- **Reading L** is a weighted sum of the Y; **reading G** is a weighted sum of Y Y†.
- **The rates are read on 40–50.**

| cell | outcome |
|---|---|
| H1 (the weight does no work) | **fails** for L: three other positive weightings move rates by up to 1.6e-2. For G it failed as run (3.2e-1), but that is a precision artefact of the run (below) |
| H2 (L has full rank) | holds |
| H3 (each block's rates are one of B1979's 12 classes) | **fails** in both readings, at every block |
| H4 (the 4 blocks agree) | **fails** in both readings |
| H5 (L aligned and hierarchical) | **fails**. The least diagonal is 0.86 and 0.74 at the blocks; up m₂/m₃ has rate 0 at two blocks; V₂₃ has rate 0 (an order-one 2–3 mixing) at every block |
| H6 (the lepton m₂/m₃ rate is 2/5) | holds for L at the four blocks. It fails for L over all 96 (rate 0) and for G (rate 0) |
| H7 (on the grid of 1/60) | **fails**. Under L, the up m₂/m₃ rate is 0.0777 at two blocks |
| H8 (L and G agree) | fails |

- **Post hoc, labelled** (`g_precision_posthoc.py`, `g_precision_posthoc_run.txt`).
  - Reading G's Gramian squares the dynamic range, so at heights 40 and 50 its least eigenvalue fell below the run's
    30 + 2y digits.
  - Redone at 30 + 5y digits, reading G gives, in every sector and every block, **m₂/m₃ at rate 0 and m₁/m₃ at rate 1**,
    on 30–40 and on 40–50 alike. The values near 0.9 in `shell_run.txt` are that artefact.

## What it means

- **The shell does not pick a class.** In either declared reading, the frame read over the whole canonical shell gives
  rates off B1979's menu.
- **It also loses what single points had.**
  - Reading G erases the 2–3 hierarchy and makes the three sectors alike.
  - Reading L loses the alignment, makes the 2–3 mixing order one, and loses the up hierarchy at half the blocks.
  - This is B1944's washing-out again, now on a finite canonical set.
- **The uniform weight is an import that does work** (L, H1). This confirms the web seat's typing.
- **agy-exp's claim is not tested here as made.** Its frame (two doublets, H_u on K₅ alone, H_d on K₅ plus the shell)
  is not frame C. What is closed is the shell as a rule for P-845 in frame C under these two readings.

## What the wall teaches

- **The family of selection tested** is a finite classification with a test of membership: B1979's 12 classes,
  with membership meaning every rate within 1e-3.
- **The wall:** a canonical set is not a canonical reading. GL(2, ℤ) preserves the shell, but how the frame is read over
  it (a sum of Y, a sum of Y Y†, the weights) is still chosen. Every choice tried here mixes the points with no regard to
  their relative phases, and the structure each single point carries cancels.
- **The whole instrument (the author, 2026-11-25; P-882)** is one object covariant under all the moves. It is not a
  sum over its points.

## What is open

- **P-845 stays open.** B1980 records that B1976's 96 points are the act's own cusps on X(30), so the menu is the act's,
  but the class within it is not fixed.
