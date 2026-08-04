# B898 — N3: the EXACT signature census — the dichotomy is a theorem; the float borderlines were all kernel

**Date:** 2026-08-05 · **Seat:** cc (banking) · **Status:** exact over ℚ (charpoly + factorization + Sturm), no floats anywhere

## What was computed

B893's census was float-with-tolerance and carried borderline
"generic-complex" counts (1, 1, 7). Here: the characteristic polynomial of
ad(x_n) for each torus charge, computed exactly over ℚ (the ad matrices are
rational), factored over ℚ, each irreducible factor classified exactly —
all-real (Sturm count = degree), purely imaginary (even polynomial whose
s = t² roots are all real negative), or neither.

## The exact table (replaces B893's census)

| charge | zero | real | imaginary | complex | signature |
|--------|------|------|-----------|---------|-----------|
| x₈  (measured)   | **30** | **48** | 0 | **0** | split, centralizer 30 |
| x₁₆ (measured)   | **30** | **48** | 0 | **0** | split, centralizer 30 |
| x₁₄ (unmeasured) | **12** | 0 | **66** | **0** | compact, centralizer 12 |
| x₂₂ (unmeasured) | **12** | 0 | **66** | **0** | compact, centralizer 12 |

Three upgrades over the float census:

1. **Every borderline resolved into the kernel.** x₁₆'s "29 zero + 1
   complex" is exactly 30 zero; x₂₂'s "5 zero + 7 complex" is exactly 12
   zero. No generic-complex eigenvalue exists anywhere on C — the float
   artifacts were tolerance noise on kernel directions.
2. **The two measured charges have IDENTICAL type signatures, and so do the
   two unmeasured ones.** The dichotomy is not merely "each direction has a
   type" — the pairs are type-twins: {0³⁰, 48 real} vs {0¹², 66 imaginary}.
3. **The kernel dimensions are structural:** 30 = dim z(x₈) = dim(so(8)⊕u(1)²)
   (the FMT centralizer) for the measured pair; **12 = the floor dimension**
   (B874's Cent(C) ambient... the generic-C centralizer) for the unmeasured
   pair — the compact charges see exactly the floor, the split charges see
   the first-breaking centralizer.

**The signature dichotomy theorem (exact):** the superselection torus C
splits 2+2 by ad-spectrum type — the measured plane is purely split
(hyperbolic flows, kernel 30), the unmeasured slots purely compact (circle
flows, kernel 12), with no mixed or generic-complex directions. B894's
four-column ledger's third column is now exact.

## Files

- `exact_census.py` → `results.json` (counts + the classified factor lists)
- Locks: `tests/test_b898_census.py`

## Depends on

B854 (the frame), B893 (the float census this upgrades), B894 (the ledger
this hardens).
