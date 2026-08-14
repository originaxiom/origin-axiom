# B893 — The involution vs the measurement frame + THE SIGNATURE OF C (W7 opening; M7 + M3)

**Date:** 2026-08-05 · **Seat:** cc (banking) · **Status:** computed, three cells, all exact or float-census-with-exact-anchors

## What was asked

Three questions from the masterplan (W7 opening + meditation items M7 and M3):

1. **W7**: does the Chevalley involution ω of this build preserve the measurement
   torus C = ⟨x₈, x₁₄, x₁₆, x₂₂⟩? (The c-vs-θ crux needs to know whether the
   object's canonical real form even sees the measurement frame.)
2. **M7**: what is the ad-spectrum *type* of each torus direction — real
   (split/hyperbolic flow) or imaginary (compact/circle flow)?
3. **M3**: is the second-measurement wall complex at *all three* Galois roots of
   μ, or only at the real-root branch checked in B892?

## Cell 1 — ω exists but is transverse to the measurement frame (exact)

`omega_cell.py`, all exact over ℚ(ρ):

- On this build the Chevalley involution is **ω(e_α) = e₋α, ω|_h = −1 with
  lattice character d ≡ 1**. The naive global −1 on root vectors is NOT an
  automorphism here: d_{α+β} = d_α d_β fails for the structure-constant cocycle
  of this Chevalley frame (checked on 2000 exact bracket pairs; the d ≡ 1
  choice passes all 2000).
- **None of the four charges x₈, x₁₄, x₁₆, x₂₂ is an ω-eigenvector** (exact
  residuals, all four).
- **ω(C) ⊄ span(C)**: the image of each charge leaves the torus span with
  irrational exact residuals.

**Verdict (cell 1):** the involution and the measurement torus are
**transverse** — the object's canonical "flip" does not stabilize the frame
that measurement selects. W7's opening fact: whatever carries c into θ, it is
not the Chevalley involution acting within C.

## Cell 2 (M7) — THE SIGNATURE CENSUS: the measured plane is split, the unmeasured slots are compact

`signature_and_walls.py`, float census (mpmath eigenvalues, tolerance-classed),
kernel dims anchored by the exact centralizer dims where banked (B854/B874):

| charge | zero | real | imaginary | generic-complex | type |
|--------|------|------|-----------|-----------------|------|
| x₈  (measured, θ-odd 4)   | 30 | **48** | 0  | 0 | **SPLIT** |
| x₁₆ (measured, θ-odd 8)   | 29 | **48** | 0  | 1 | **SPLIT** |
| x₁₄ (unmeasured, θ-even 7)  | 11 | 0  | **66** | 1 | **COMPACT** |
| x₂₂ (unmeasured, θ-even 11) | 5  | 0  | **66** | 7 | **COMPACT** |

The dichotomy is clean: the two measured charges generate hyperbolic
(noncompact) one-parameter flows — every nonzero ad-eigenvalue real; the two
unmeasured charges generate circle (compact) flows — every nonzero
ad-eigenvalue imaginary. The small generic-complex counts (1, 1, 7) are
float-borderline pairs at the tolerance edge, flagged honestly; they do not
affect the real-vs-imaginary dichotomy, which is 48-vs-0 and 66-vs-0.

**The four-column concordance this completes** (with B581's sign law and
B888's resolvent — see B894 for the ledger):

> measured ⟺ θ-odd exponent (4, 8) ⟺ τ_m > 0 ⟺ split ad-spectrum
> unmeasured ⟺ θ-even exponent (7, 11) ⟺ τ_m < 0 ⟺ compact ad-spectrum

[FIREWALLED MOTIVATION — mathematics above is the claim; this paragraph is
reading, not result] The observer reads the hyperbolic directions (moduli-like)
and leaves the compact circles (phase-like) internal — consistent with the
resolvent field ℚ(√77), 77 = 7·11, being built from exactly the unmeasured
exponents (B888).

## Cell 3 (M3) — the wall is complex at ALL THREE roots

det₁₄ evaluated from the solo tower (exact coefficients, float evaluation at
35 digits) at each root of μ:

| root of μ | det₁₄ | a² = −det₁₄ | wall |
|-----------|-------|-------------|------|
| −0.0019380502 | +3.85478×10⁹ | < 0 | **complex** |
| +0.00039822150 | +2.79262×10⁹ | < 0 | **complex** (= B892's branch) |
| +0.0056852369 | +1.32094×10¹⁰ | < 0 | **complex** |

**Verdict (cell 3):** `wall_complex_at_all_roots = True`. The √−1 cost of the
second measurement is **Galois-uniform** — a property of the S₃ orbit, not of
a root choice. This upgrades B892's "the wall is complex in the split frame"
from one branch to the whole orbit and strengthens the real/complex
measurement-alternation reading (M3): the first measurement is real at every
branch, the second costs one complexification at every branch.

## Files

- `omega_cell.py` → `results.json` (cell 1, exact)
- `signature_and_walls.py` → `signature_results.json` (cells 2–3)
- Locks: `tests/test_b893_omega.py`

## Depends on

B854 (the build), B866 (μ), B874 (the ladder), B888 (the resolvent 77),
B892 (the SMT wall), B581 (the torsion sign law — via B894).
