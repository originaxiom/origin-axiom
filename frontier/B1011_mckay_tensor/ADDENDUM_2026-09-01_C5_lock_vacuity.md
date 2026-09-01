# ADDENDUM (2026-09-01, fresh physics seat; finding for the banking seat to re-verify) — the C5 forced-count lock (992 / 284) is an arithmetic tautology as committed; the numbers themselves are confirmed cell-by-cell by independent code

**Scope.** This note concerns the *lock*, not the numbers. C5's counts 992 (θ-odd forced) and
284 (θ-even forced) and C6's 15-value mirror set all **reproduce** under an independent
criterion (Ring R3 cell R26,
`reports/fresh_physics_seat_2026-09-01/recompute/R26_b1080_b1011/`). The banked files are left
unedited; nothing here is banked by this seat.

## What the committed lock checks (R3_REPORT V18)

`b1011_match.py` lines 137–142 set `kerchi, ZI, ZT = 8, 2, 2` as literals and assert
`8·120 + 24·2 − 8·2 == 992` and `2·120 + 24·2 − 2·2 == 284`; `tests/test_b1011_mckay_tensor.py`
lines 58–59 assert the same two integer identities. Nothing committed enumerates the 2880
cells or evaluates a forcing criterion on them; FINDINGS line 49–50 "matching the incoming
enumeration" refers to an enumeration that is not in the committed tree. The lock could not
have failed for any reason other than a typo in the inclusion–exclusion.

The inputs 8 / 2 / 2 (|ker χ| = |Q₈|, |Z(2I)| = |Z(2T)| = 2) are separately verified (Ring R1
cell R02), so the counts are right; only the *lock* is vacuous.

## What R26 supplies

Over the exact tower ℚ(√5)(√3, i), for every one of the 2880 = |2T × 2I| cells the actual
representing matrices are formed and a Hermitian-scalar forcing criterion evaluated: 992 θ-odd
and 284 θ-even forced cells, agreeing with the arc's definition **cell-by-cell** (asserted in
both directions). That is the falsifiable version of C5 the arc lacked
(`blind_forced_counts.py`, `blind_B_output.txt`).

## Scope clause for C6 (semantics, not an error)

The C6 mirror value set {0, ±¼, ±1/(4φ), ±½, ±1/(2φ), ±φ/4, ±φ/2, ±1} (15 values) is over all
2880 cells. Restricted to the 284 forced θ-even cells it has **9** members: the quarter values
±¼, ±1/(4φ), ±φ/4 occur only when both A and B are non-central, i.e. exactly where the
listener-independent (forced) reading does not apply. The mirror-law statement should carry
that scope clause.

**Proposal (owner / banking-seat action):** replace the literal-arithmetic lock with the
cell-by-cell enumeration (or land the "incoming enumeration" it refers to), and add the scope
clause to C6. Error-class: lock vacuity (same class as E27/E40).

## CORRECTION (2026-09-01, later the same day; owner's rule "sweep the repo before concluding we don't have something")

The sentence above *"Nothing committed enumerates the 2880 cells or evaluates a forcing
criterion on them"* over-claims. Sweep (all seven remote heads, filenames `b1011`, content
`forced|992|284|incoming enumeration`; deleted-file history): **`b1011_cells.py` does enumerate
the 2880 elements of 2T × 2I** (`enumerate_group(p)`, mod-61 / mod-241 exact, `assert
len(seen1) == len(seen2) == 2880`, conjugacy classes via `conj_classes`; exercised by
`tests/test_b1011_mckay_tensor.py`). What no committed file on any head does is **evaluate a
forcing criterion on those elements** — the only committed occurrences of 992 / 284 are the
inclusion–exclusion literals in `b1011_match.py:139–142` and `tests/test_b1011_mckay_tensor.py:
58–59`. The finding (V18: the C5 *lock* is literal arithmetic; the counts are right) is unchanged;
the corrected sentence reads: *"the enumeration exists (`b1011_cells.py`); nothing committed
evaluates a forcing criterion on it, so the 992 / 284 lock never touches the cells."* Same
correction applies to R3_REPORT V18 wherever it repeats the original wording.
