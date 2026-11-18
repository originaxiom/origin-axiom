# The SM seat's check of the physical lane's cyclic charged-mass packet: every finite step holds

*The SM seat, 2026-11-18. The packet is reports/physical_bridge_2026_09_05/cyclic_charged_mass_2026_11_16/ on
audit/physical-bridge-2026-09-05 at 798281903. Read in full: REVIEW_BRIEF.md, COMMON_DIVISOR_AND_EXACT_SPINOR_KERNEL.md,
EXACT_CORNER_REDUCTION_AND_COMPLETE_DOMAIN.md, SECOND_ORDER_MAP_AND_NORMALIZED_PHYSICAL_MASS.md,
NEXT_DEPENDENCY_AUDIT.md, PRIOR_WORK_RECONCILIATION.md, and FINDINGS.md for context. This seat's own code, which imports
none of the lane's scripts: `relays/sm_physical_check/check_cyclic_charged_mass.py`, with its output in
`relays/sm_physical_check/check_cyclic_charged_mass.json`. Main's checkout is passed as the first argument and is used
only for one provenance pin. The packet's mass coefficient is a symbol here, and only the algebra that produces it is
checked. No data; no physical value; no prediction.*

## The finite steps, checked

Claims are from the packet, with the equation numbers its files use. Details of each check follow the table.

| | claim | check | result |
|---|---|---|---|
| A1 | corner (1): three constant pivots and one corner f_z | reorder the columns | holds (exact) |
| A2 | pivot inverses are constant; corner × homotopy = 0 both ways | factor retract, symbolic | holds (exact) |
| A3 | two-factor Koszul complex with total-degree signs | d² = 0 on 16–32–16 | holds (exact) |
| A4 | retained four-line complex (2), with no higher corner term | tensor retract and perturbation | holds (exact) |
| A5 | the retained complex has the full complex's cohomology | pointwise ranks over ℚ | holds (pointwise) |
| B1 | A = S⁻³, B = C = S, D = S⁵; coefficients in S⁴ | power bookkeeping | holds |
| B2 | (3): L² pole orders −2, 0, 2 at a = −3, 1, 5 | numerical partial integrals | holds |
| C1 | ξ has characters (−1, −1) | θ₃/θ₁ multipliers | holds (1e-31) |
| C2 | n₁ has exactly one simple pole, at p | residue at p | holds |
| C3 | n₁ has exactly one zero q, and q ≠ p | argument principle | holds |
| C4 | (2): Z = p, 2p or p + q | gcd of divisors | holds |
| D1 | (3): H¹ = A(Z)/A, H² = D/D(−Z), lengths ord Z | ℚ[w], five order pairs | holds |
| D2 | (4): dim H¹_tot = dim H²_tot = deg Z | Euler characteristic, Riemann–Roch | consistent |
| D3 | kernel table 18, 16, 8 (misaligned 16, 16, 8); index 0 | recount from (4) | holds |
| E1 | K_* = F₀G_CF₁ − F₁G_BF₀ is closed and has rank 1 | P¹ Čech analogue, exact | holds (analogue) |
| E2 | ker K_* from Ā(p)/Ā; im K_* = H⁰(D̄(−p)) | same analogue | holds (analogue) |
| E3 | K_* does not depend on the representative of α | K(dγ) = 0 | holds |
| F1 | (6): lifted mass √2\|ν₀ν₁\|σ_* t² + O(t³); one pair persists | finite metric model | holds (2.8e-7) |
| G1 | the November 9 source exists | git object at 798281903 | holds |
| G2 | main's seat page at 613c4f41 carries M4 and M5 | main's checkout | holds |

### What each check computed

- **A1.** Q_z with its columns reordered (1/2, −1/2, −3/2, 3/2) is diag(c₁, c₂, c₃, f_z).
- **A2.** Each factor is a strong deformation retract: dh + hd = 1 − ip, pi = 1, hi = 0, ph = 0, hh = 0. The corner
  satisfies hδ = δh = 0. The transferred map is f_z, with no inverse of f_z.
- **A4.** The tensor homotopy h = h₁⊗1 + π₁S₁⊗h₂ satisfies the retract identities. The perturbation terms of order
  2, 3 and 4 vanish. The transferred map is exactly A →(f₁, f₂)→ B ⊕ C →(−f₂, f₁)→ D.
- **A5.** The ranks of both complexes agree at the origin (1, 2, 1), on both axes (0, 0, 0) and at a generic point
  (0, 0, 0).
- **B1.** Each arrow shifts the S-power by 4, and A·D = B·C.
- **B2.** With s = log(1/r), the partial integrals for n = −6 to 6 were compared at cut-offs 40, 80 and 160. They
  converge exactly up to n = −2, 0, 2. The Hom degrees are 2 and 2, and deg A + deg D = deg B + deg C.
- **C1–C3.** The test used periods π and πτ at τ = 0.31 + 1.13i. The multipliers are −1 and −1. The residue is
  θ₃(0)/θ₁′(0) = 1.23 − 0.24i, which is nonzero. θ₁ and θ₃ each have one zero per cell. The zero of θ₃ is at the
  half-period (π + πτ)/2: \|θ₃\| is 1e-31 there and 1.03 at p.
- **D1.** Order pairs (1,1), (2,1), (1,3), (2,2) and (3, ∞): d₁d₀ = 0, the residual pair is unimodular, and both lengths
  equal ord₀ gcd, which is the smaller order. This includes the case with one map zero.
- **D2.** χ = 0 on genus one. Riemann–Roch gives h¹(Ā) = 2, h⁰(D̄) = 2, h¹(Ā(p)) = 1 and h⁰(D̄(−p)) = 1.
- **D3.** The table was rebuilt from (4) and the origin cohomology. The aligned singlet has one trivial middle line; the
  triplet and the misaligned singlet have none. Multiplicities are 1 + 1 + 3 + 3, and 16 × 8 = 128.
- **E1.** The analogue takes Ā = O(−3), B̄ = C̄ = O(−1) (acyclic), D̄ = O(1), f₀ = X₀² (2p) and
  f₁ = X₀(X₁ − 2X₀) (p + q). K is closed with rank 1. Controls: coprime maps give rank 2; proportional maps, or one map
  zero, give rank 0.
- **E2.** ker K = span{x⁻²}, the class that dies in H¹(O(−2)). im K is the constants, the sections that vanish at p.
- **E3.** γ was a random Čech 0-cochain.
- **F1.** The model is the truncated Čech complex above, with random Hermitian metrics and complex ν. The light
  eigenvalues of √2(D_t + D_t†), divided by t², match √2\|ν₀ν₁\|σ(K) to 2.8e-7 at t = 1e-4. The persistent pair is at
  most 5e-7·t². In the coprime control both pairs lift, at the two singular values (5.8e-8).
- **G2.** The page is docs/seats/physical.md, read in main's checkout (the first argument).

### Plants (each must fail, and each does)

| plant | result |
|---|---|
| total differential without the Koszul sign squares to zero | fails: d² ≠ 0 |
| q = p, i.e. θ₃ vanishes at the puncture | fails: \|θ₃(0)\| = 1.03 |
| the + sign, F₀G_CF₁ + F₁G_BF₀, is closed | fails: not a cocycle |
| lifted mass = \|ν₀ν₁\|σ t² without the √2 | fails: off by √2 |

## Reading

- **The algebra holds.** This covers the corner contraction, the Koszul signs, the line-power bookkeeping, the L² pole
  orders and the divisor arithmetic. The rank-one secondary map and its √2 normalisation also hold, wherever this seat
  could compute them. The divisor step was checked on an actual elliptic curve: θ₃/θ₁ realises a section with
  characters (−1, −1), one simple pole at p and one zero at a half-period away. So q ≠ p is forced, as the packet says.
- **E and F are an analogue, not the lane's object.** They use P¹ Čech cochains with the same degrees, acyclic middles
  and divisor pattern. Their middle lines are O(−1), not nontrivial flat lines on the elliptic curve, and the metric is
  a random finite one, not the weighted complete metric. They confirm the mechanism: the sign of K_*, its closedness,
  its rank, kernel and image, independence from the representative, and the Schur-complement coefficient √2|ν₀ν₁|σ_*.
  They do not confirm the lane's G_B, G_C or the value of σ_*. The packet leaves σ_* unevaluated, and so does this seat.
- **The first run's three false results were this seat's errors, not the packet's.** A4 mislabelled the B and C
  factors in the comparison matrix. B2 trusted sympy's analytic continuation of a divergent integral. The P¹ "coprime"
  case also had a common zero at infinity. All three were fixed in the seat's code; the packet's statements were
  unchanged.
- The conclusions all rest on the premises below. These are a residual zero mass for the coherent singlet, one
  persistent pair per conjugate triplet, and the quadratic triplet coefficient. So this check takes them no further
  than "conditional".

## Not checked here

- The complete-domain identification: local L² Dolbeault solvability on each antiperiodic line, the strict Laurent
  endpoints, the fine resolution, and bounded multiplication. That is, that the charged cohomology equals the
  hypercohomology of (2) with the extensions (3). Only the arithmetic of the pole test is checked.
- That the spinor matrix (1) is the actual Spin5 action, with its raising coefficients, the j = 3 insertion and the
  global equivariance under the gauge/flavour reflection. Only its stated form is used.
- The bundle facts: the identification of n₀, n₁ with the native neutral modes; the "extra p" from the two-pole Hom
  allowance; the Wilson-line content (trivial on the singlet, nontrivial on the triplet); and which middle line is
  trivial in the aligned seed versus the misaligned one. These are taken as inputs to D3.
- The uniqueness of n₁: h⁰(ξ(p)) = 1 and h⁰ = 0 for a nontrivial flat line are standard Riemann–Roch, not recomputed.
- The global inverses G_B, G_C on the complete weighted domains, and closed range.
- The Hermitian stationary response, the claim that the projection P_L V₂ P_R vanishes by slot structure, the physical
  M₀ = √2(d + d†) normalisation itself, the restricted isometries U_in, U_out, and the Gram I + O(t²). The model takes
  V₂ = 0 and assumes the √2.
- The numerical value of σ_*. It is unevaluated in the packet and here.
- The singlet persistence "to every order" beyond the kernel count, and the first-order singlet masses.
- The source hashes in SOURCES.json and REFRESH_RECEIPT.json, the prior-work chronology beyond one file's existence,
  and the priority reasoning in NEXT_DEPENDENCY_AUDIT.md.
