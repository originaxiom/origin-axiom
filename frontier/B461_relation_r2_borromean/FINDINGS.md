# B461 — Relation R2: the Borromean rings — the ladder run to its floor, the fields exact, one deflation, one hardness contrast

**Status: banked (frontier). Firewalled. Prereg: `PREREGISTRATION.md` (PR #610, before
computation; the budget ladder with STOP criteria was the design and it executed exactly
as written). Verdict: ℚ(i)-class arithmetic confirmed; no relational invariant escapes;
the L6a4 SL(3) census is the ladder's named partial result; one important deflation
(√−7 on a control). No H1.**

## Rung 1 (banked earlier): the incoming-claims table — all verified

vol(L6a4) = 2·v_oct exact (the "8 octahedra" and "3.61×" claims corrected per the
campaign prereg); tetrahedra shapes have minimal polynomials of disc −4 ⟹ the ℚ(i)
arithmetic gate PASSES; H₁ = ℤ³; the linking matrix is zero and μ̄(123) = ±1 (the
classical Brunnian detectors — cited, textbook); the geometric SL(3) component dimension
expectation dim = #cusps (Thurston, cited).

## The SL(2) exact elimination table (`rung3_sl2.sage`) — the arithmetic register

| manifold | zero-dim classes | fields | other classes |
|---|---|---|---|
| **L6a4** (Borromean) | 2 | **ℚ(i)** (disc −1) | 2 classes of dim 1; rest empty |
| **m129** (Whitehead, control) | 2 | **ℚ(i)** ✓ (its known trace field — control passes) | rest empty |
| **s776** (non-Brunnian chain, control) | 3 | **ℚ(√−7)** | rest empty |

**The deflation (recorded prominently):** ℚ(√−7) — the program's "chirality field," now
with appearances in B444 (fig-8 SL(3)), B448 (period-4 orbits), BR3 (m=3 breath) — turns
up as the SL(2) Ptolemy field of the UNRELATED non-Brunnian control (the chain-link's own
classical arithmetic). **Any cumulative "√−7 keeps finding the object" reading is dead**:
each appearance requires its own mechanism; the field also belongs to class-external
objects. (The burden-inversion discipline working in the deflationary direction.)

## The SL(3) rung: the control completes, the target defines the boundary

- **s776: COMPLETE** — per-class F_p dimensions (p = 31991): class 0 dim 3 (= #cusps,
  the geometric component, as expected), classes 1–12 dim 0, class 13 dim 1.
- **L6a4: ALL 14 classes hit the 20-minute per-class cap** at the same rung where the
  same-size control (3 cusps, 8 tetrahedra, comparable variable counts) completes in
  minutes — a uniform, reproducible **hardness contrast** (honest caveat attached:
  ideal-theoretic hardness may be triangulation-dependent, not topological).
- The numeric fallback (rung 4): random-Gaussian seeding fails in 32 complex dims
  (recorded); unit-modulus seeding works — class 0 shows POSITIVE-dimensional structure
  (Jacobian ranks 29–30 < 32, consistent with the dim-3 geometric component), class 1
  yields an ISOLATED point (rank = nv). **The full per-class census + field recognition
  is the named partial result** (rung 5): priced at a multi-hour dedicated compute
  (≈10³ seeded starts × 14 classes + PSLQ recognition), machinery in `rung4_numeric.py`.

## The Brunnian two-register verdict (per prereg)

- **Link register (LIVE, as prereg'd)**: the discriminating invariants are the classical
  ones — zero linking matrix + μ̄(123) = ±1 + sublink triviality. Verified/cited; nothing
  object-specific rides on them.
- **Manifold register (prereg'd EXPECTED-BLIND)**: no Brunnian-specific manifold
  invariant emerged — the SL(2) fields separate the manifolds but as their own arithmetic
  (ℚ(i) vs ℚ(√−7)), not as a Brunnian detector. The SL(3) hardness contrast is recorded
  as an OBSERVATION adjacent to this register, explicitly not banked as a detector.

## Reproduce
```
python3 rung1_claims_sl2.py     # the verified claims table
sage rung3_sl2.sage             # the SL(2) elimination table
python3 run_rung2.py            # the F_p dimension sweep (per-class 20-min caps)
python3 rung4_numeric.py        # the numeric fallback (+ the seeded retry pattern)
pytest ../../tests/test_b461.py
```

## Addendum (2026-07-08): the census boundary COMPUTED (numeric, 1000 seeded starts/class)

| class | result |
|---|---|
| 0 | 10 solutions, ALL on-family (the positive-dimensional geometric component) |
| 5 | 31 solutions, ALL on-family (a second large positive-dimensional class) |
| 3, 6, 7, 8, 9, 10, 11 | **14 isolated points total** (1, 2, 4, 3, 1, 1, 2) |
| 1, 2, 4, 12, 13 | nothing found (empty or hard basins — UNRESOLVED, honest bin; s776 also had empty classes) |

The structural contrast with s776 sharpens: the control is almost entirely 0-dimensional
(12 point-classes + one dim-3 + one dim-1); the Borromean shows at least TWO large
positive-dimensional classes plus scattered isolated points. Field recognition at the
isolated points FAILED at this precision (1e-12 Newton cannot support degree-10 PSLQ) —
the residual: high-precision polish (mpmath dps 40 refinement per point) then minpoly
recognition; machinery in `census_full.py`. The census's structure table is the banked
deliverable; the fields are the priced remainder.
