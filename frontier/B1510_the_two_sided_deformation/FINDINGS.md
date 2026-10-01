# B1510 — THE TWO-SIDED DEFORMATION: SEALED, NOT RUN. The 16's and the 16*'s singlets switched on together

**Date:** 2026-10-01 · **Seat:** cc (the SM-derivation branch) · **Status:** SEALED, NOT RUN. This document holds no two-sided
outcome. · **Price:** unchanged, 0 of 19 · **Numbering:** B1510.

## 1. What is sealed

- **The question (B1509's lead 1, at the owner's "do the recomendation for next").** B1509 switched on one singlet direction at a
  time on the audit lane's harmonic vacuum ρ₀ = A ⊕ 1, A = μρ_q:
  - c (the 16's singlet) gives index −1 at μ = −1, one 10′;
  - c* (the 16*'s singlet) gives +1.

  This arc switches both on together, with first-order term s c + t c* (s t ≠ 0). Do they hold without a source? Can the trivial
  line keep its cusp eigenvalues (1, 1)? What do they count?
- **Computed before the seal, and disclosed there.**
  - The controls C0–C6 (`verification/controls_run.txt`). B1509's indices are reproduced through this arc's own F((ε)) ranks-only
    index (54 rows).
  - The GL(2) and GL(3) analogues at simple roots exist and count 0.
  - The meridian's Jordan type (3, 1) at the six points.
  - No two-sided term and no adjoint cohomology was computed at the six points.
- **Proved at seal.**
  - **Theorem A:** given cusp rigidity and a regular cusp pair, every sl(4) obstruction vanishes at every order.
  - **Lemmas R and C:** those hypotheses hold here, given the audit lane's F15/R55 data.
  - **Corollary A″:** every deformation with s t ≠ 0 is absolutely irreducible, so its orbit is closed.
  - **Theorem B:** the line's longitude moves at order two by s t κ̂_ℓ, with κ̂_ℓ = ±⟨e ∪ c, c*⟩. It is zero exactly at the
    double root μ = −1.
  - **Proposition F:** the fixed-end class is F15's matter-retention row, which is R56's F-term F_S = λ Q·Q̃. It is nonzero.
  - **Theorem C:** main's index is 0 on every two-sided deformation. The proof uses upper semicontinuity of H², the Euler
    characteristic and the annihilator identity.
  - **Theorem D:** parity, and the shifted longitude condition at a double root.
- **Decided at design time**, D1–D6:
  - cusp rigidity;
  - no sl(4) obstruction;
  - κ̂_ℓ = 0 at μ = −1 only;
  - the fixed end obstructed;
  - no chiral branch at ±i;
  - the count zero on every branch reached.
- **The predictions.**
  - P1: the free-end branch exists to order 10 (±i ~90%, μ = −1 ~70%).
  - P2: the odd obstructions lie on one line (~70%).
  - P3: the chiral branch at μ = −1 reaches order 10 (~65%).
  - P4: a1 = b1 = 0 on the free-end branch (~65%).
  - P5: at μ = −1 the free-end branch moves the line's longitude first at order four (~70%).

## 2. Why this document exists before the run

Every arc carrying a verdict carries a findings document, and a seal commit ships its findings stub with it (the E50 practice of
2026-09-28). This page holds no two-sided result.

The design-time sweep found that the audit lane's F15 and R55 decide two items an earlier draft carried as open. The
preregistration says so and lists everything seen before the seal.

`PREREGISTRATION.md` (sha256 in SEAL_LEDGER). 0 of 19.
