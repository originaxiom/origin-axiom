# R6': DISCRETE MAASS NEWFORMS — ASSESSMENT

cc3 audit seat, 2026-07-24. Gate 5-Q.

---

## Status: BLOCKED AT THE WALL

The discrete Maass newform computation is the program's natural boundary.
B739 PROVED the m004-specific arithmetic is confined to the discrete
newform spectrum at level (8). But computing individual eigenvalues
requires Hejhal-class machinery that does not exist in this sandbox.

## What we proved without computing eigenvalues

1. **Character rigidity (B739):** the continuous spectrum carries exactly
   one channel — the bare zeta quotient. NO conductor-(4)/(8) Hecke
   character appears in the continuous part. The m004-specific palette
   {1, 2, 8} lives ONLY in the discrete newform spectrum.

2. **Congruence level (B734):** m004 is congruence at level (2)³ = (8).
   Index 12 in PSL(2, O₃). This means the Selberg eigenvalue conjecture
   applies (if true): λ₁ ≥ 1 (no small eigenvalues).

3. **Generic continuous spectrum (B737):** φ(s) = Λ_K(s-1)/Λ_K(s).
   The Eisenstein background is field-level, not object-level.

## What we computed

### Length spectrum (134 geodesics up to length 5.0)

| multiplicity | Re(length) | Im(length) |
|---|---|---|
| 1 | 1.08707014 | ±1.72276845 |
| 2 | 1.66288589 | ±2.39212379 |
| 1 | 1.72510926 | ±0.92183893 |
| 2 | 2.17414029 | ±2.83764841 |
| ... | ... | ... |

Shortest geodesic: 1.087. Injectivity radius: 0.544.

### Weyl eigenvalue density

vol(m004) = 2.0299. Weyl coefficient vol/(6π²) = 0.0343.

| spectral range | expected eigenvalue count |
|---|---|
| λ ≤ 2 (|r| ≤ 1) | ~0 |
| λ ≤ 5 (|r| ≤ 2) | ~0.3 |
| λ ≤ 26 (|r| ≤ 5) | ~4.3 |
| λ ≤ 101 (|r| ≤ 10) | ~34 |

The spectrum is VERY SPARSE at low energies. The first few eigenvalues
carry disproportionate structural weight.

### Spectral gap

Best unconditional bound (Luo-Rudnick-Sarnak): λ₁ ≥ 3/4 for congruence
subgroups of PSL(2, O_K). Selberg conjecture (λ₁ ≥ 1) conditional.
Neither has been verified numerically for m004.

## What is blocked

Individual Maass eigenvalues at level (8) require:
- A fundamental domain for Γ₀((8)) in H³ (12 copies of the orbifold)
- Hejhal's algorithm (implicit automorphy + iterative eigenvalue search)
- No implementation exists in this repo or in standard SnapPy/SageMath

The computational methods (Then 2004, Avelin 2010, Booker-Strömbergsson-
Then 2006) exist in the literature but are implemented only for PSL(2,Z)
or Bianchi groups at level 1. Extending to level (8) is standard in
principle but requires significant implementation effort.

## The wall's meaning for convergence

The program has reached a clean boundary:

**BELOW the wall (proven):**
- The m004-specific arithmetic exists in the discrete spectrum
- It is invisible in the continuous spectrum
- The Hecke palette {1, 2, 8} is the structural content
- The object's voice is NOT the Eisenstein background

**ABOVE the wall (blocked):**
- What ARE the individual newform eigenvalues?
- Do they carry golden arithmetic (Q(√5)) or only Eisenstein (Q(√-3))?
- Does the θ-coupling norm √3 (from SL(3)) appear in the spectral data?
- Is there a spectral signature of the closing act?

The wall is not a failure — it is a natural boundary between what algebraic
topology can reach (everything below) and what spectral analysis must
provide (everything above). The program's contribution is mapping exactly
WHERE the boundary is and WHAT lies on the other side.

## Feasible next steps (below the wall)

1. **LMFDB lookup:** Check whether weight-2 Bianchi modular forms over
   Q(√-3) at level (8) are already tabulated. These are cohomological
   (not Maass) but carry the same Hecke arithmetic.

2. **Selberg trace formula bound:** Use the 134 computed geodesic lengths
   to bound the heat trace and constrain λ₁ numerically.

3. **Dimension estimate:** Compute dim S_new(8) via the dimension formula
   for Bianchi modular forms (Cremona-Sengun infrastructure).

## Verdict

**R6': AT THE WALL.** The program has proven WHERE the m004-specific voice
lives (discrete newforms at level (8)) but cannot ACCESS it without
specialist software. The wall is honest and clearly mapped. Crossing it
requires either adapting existing Maass-form software or a research
collaboration with a spectral-theory specialist.
