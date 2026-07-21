# FINDINGS — B747: the √5 MIRROR sweep — MIRROR-SILENT: no child re-sees the hearing (0/78)

cc banking seat, 2026-07-21. The golden ledger's door #1 (B746), run on the owner's go.
Prereg sealed 09cef416 BEFORE the sweep; sealed input = cc2's two-seat-verified degree/field
table (sha 77818016, hash-matched to cc2's SEALS.txt, copied into this arc). Gate 5;
nothing to CLAIMS.

## Verdict: MIRROR-SILENT — 0/78 fillings' invariant trace fields contain √5

- **Stage 1 (theorem):** 54 odd-degree slopes — no quadratic subfield at all (odd degree ⇒
  no index-2 subfield), closed from the sealed two-seat degree table.
- **Stage 2 (exact):** all 24 even-degree slopes (degrees 4–30, incl. the a-priori-flagged
  (±5,1) and (±7,1)): invariant trace field recomputed via the B740 pipeline, computed
  degree REQUIRED to match the sealed two-seat degree (all matched), then the exact root
  test x²−5 in K — **all 24 False**. The (3,8) degree-30 straggler closed TWO ways: the
  verified amphichirality isometry 4₁(3,8) ≅ 4₁(−3,8) (shared field, √5-free) AND the
  direct field recovery at prec 6000 (degree 30 matches, √5 False).
- **Controls (all pass, run before the sweep):** ℚ(√5) and ℚ(√φ) routine-positive;
  ℚ(√−3), ℚ(∛2) routine-negative; m004 pipeline control (contains √−3, not √5).

## Reading (arithmetic only)

The golden-slope children (±5,1) — where B437 found golden traces in the child's ABELIAN
tower — do NOT carry √5 in their trace fields: the golden content of that observation
lives in a different object (the abelian/Alexander tower), not in the child's arithmetic
identity. Combined with B288/B740 (no child re-sees √−3), the two-column law sharpens:
closing silences BOTH columns tested so far. Completed to the full V₄ by B748.

Artifacts: `b747_sweep.py` + `b747_out.txt` (controls + full table), `b747_closure.py` +
`b747_closure_out.txt` (the (3,8) double closure), the sealed input copy. Locks in
`tests/test_b747_b748_sweeps.py`.
