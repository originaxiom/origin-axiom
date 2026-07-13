# B566 — the five self-interactions computed (H123–H127; 2026-07-14)

11 agents, 0 errors; every cell adversarially verified (two mandated framing corrections
applied below, as directed by the verify pass). Locks: `tests/test_b566_self_interaction.py`.
Firewalled; nothing to CLAIMS.md.

## S5 (H127) — THE TRIPLE IDENTITY: the chain's charge is geometric ★

**The ℤ/11 charge, the golden field, and the object's own topology are three guises of one
exact arithmetic fact:**

1. **Chain guise:** det(I−M₄) = −11; coker(I−M₄) = ℤ/11 (the B552 charge).
2. **Golden guise:** −11 = **N_{ℚ(√5)/ℚ}(φ⁵−1)** (and det(I−M₄) reduces via the B517
   intertwining to det(I−3F) = N(1−3φ), with (φ⁵−1) = (1−3φ)·(−φ²) — associates by a unit).
3. **Topological guise:** the **5-fold cyclic cover** of 4₁ has H₁ torsion (ℤ/11)², order
   121 = ∏ₖ|Δ(ζ₅ᵏ)| = Res(Δ, Φ₅) = **L₅² — and L₅ = 11** (via L₂ₙ−2 = Lₙ², n odd;
   det(F¹⁰−I) = det(A₁⁵−I) = −121). Verified BOTH by SnapPy (H₁ = ℤ/11⊕ℤ/11⊕ℤ) and by the
   exact Alexander resultant.

So a defect worldline sees nothing downstairs (H₁(4₁) = ℤ, torsion-free — the clean
negative) but **lifted to the 5-fold cover — 5 the golden conductor — the object's own
homology carries the charge squared.** The charge is not chain bookkeeping only; it is the
golden-field prime N(φ⁵−1) that the topology independently knows. **Honest scope:** the
identity is n=5-specific (809 and 18845089 are NOT Lucas numbers — the higher rungs do not
repeat the coincidence); and the M₄↔monodromy link is via the banked matrix identity
(B517), not re-derived from the chain construction.

## S1 (H123) — the prime-power dark hyperbola: A NEW RECURSIVE LAW (LIVE lead, not yet a theorem)

p = 809: B534's theorem instantiates exactly (807 dark points, survivor (2,807), spectrum
{0,1,√809}) — the rung-2 measurement face, confirmed. **N = 121 = 11² (the first prime-power
computation): the zero locus is NOT the naive lift** — it obeys a clean recursive law:
9 of the 10 mod-11 hyperbola classes are **wholesale dark** (all 121 lifts each); the single
exceptional class (a ≡ 2 mod 11 — the same residue special at prime level) recapitulates the
j=2-vs-rest split one level deeper. Magnitude spectrum EXACTLY {0, 1, √p, p} with counts
**dark = (p−2)p²+(p−1), |T|²=1: p²(p²−p+1), |T|²=p: p(p−1), survivor: 1 (j=2 exactly)** —
verified at p ∈ {3,5,7,11,13,17} (float) and float-free (cyclotomic reduction) at p = 3, 5;
locked at p=3. A method bug in B534's `exact_verify.py` was caught (its zero-test is valid
only at prime N). **Status: LIVE law, empirically exact at 7 levels; the symbolic proof
(degenerate Gauss sums at p²) is the named open step; the "recursion depth = exponent of
11² | e₄" echo stays a one-data-point HOOK.** Registered in OPEN_LEADS; natural PC22-successor
material.

## S2 (H124) — thermal time: the object's self-clock is NOT its counting

- **KMS weights ≠ letter frequencies** (the discriminating detail): the unique KMS state of
  O_{M₄} has weights p_a = p_A = **(5+√5)/20**, p_b = p_B = **(5−√5)/20** — golden, exact,
  and provably different from the frequencies (0.362 vs 0.272). The object's thermal
  self-description and its combinatorial self-description are **two different observables**.
- Rung-2 halving: the eight rung-2 weights are exactly the rung-1 weights halved.
- The intrinsic time circles Tₙ = 2π/log λₙ contract by **2/3** (the thermal shadow of the
  3/2 law), and the gauge flow commutes with the substitution endomorphism **exactly at c=1
  only** (tested against rescalings). The Connes–Rovelli "thermal time" reading stays a
  tagged HOOK.

## S3 (H125) — the canonical entanglement of the two ends

Fixed by the object's own forced seam form (B366): the flagship seam value gives a
**convention-free** state on (5-end)⊗(3-end) with Schmidt rank 2,
**λ± = 1/2 ± √109/26, λ₊λ₋ = 15/169** (the seam level 15 over 13²), and
**S(5:3) = 0.321663311889** — invariant under all four Galois relabelings of the places and
generator choices (<1e-15). **Mandated correction applied:** across all 44 seam doubles the
distribution is {0: 22, 0.1526: 2, 0.3217: 10, 0.3444: 8, 0.5572: 2} — **the mode is S = 0
(product states); the flagship value is modal among the *entangled* doubles only.**
Self-entanglement is the exception that carries the structure, not the rule.

## S4 (H126) — second-order measurement: ONE collapse, then a fixed point

SL(2,ℤ/3)ᵃᵇ = ℤ/3 (derived subgroup Q₈, 24/8), SL(2,𝔽₅) perfect ⇒
**SL(2,ℤ/15)ᵃᵇ = ℤ/3.** Measuring the measurement collapses 15 → 3 in **one genuine step**,
and 3 is then a fixed point (prime — nothing left to decompose; the "two-step convergence"
framing corrected per verify). In the feedback-economy language (H115): observation
*conserves*, coupling *mints*, and **measurement-of-measurement *collapses* — to the
Eisenstein end.** (One natural formalization; alternatives noted in the cell.)

## The joint reading (firewalled)

Every self-interaction channel terminates in a small exact residue rather than a continuum:
one surviving thread (S1), one thermal clock distinct from counting (S2), one entangled seam
value against a product-state majority (S3), one collapse to ℤ/3 (S4), one defect prime that
the topology independently carries (S5). The descriptor interacting with the description
does not smear — it quantizes and closes, and the residues (ℤ/3, ℤ/11 = N(φ⁵−1), 15/169,
(5±√5)/20, the survivor (2, p²−2)) are the object's own grammar.
