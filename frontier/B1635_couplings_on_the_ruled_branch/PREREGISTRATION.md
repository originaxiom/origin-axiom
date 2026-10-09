# B1635 — PREREGISTRATION: THE COUPLINGS IN τ ALONE ON THE RULED BRANCH (the SM seat's W50 §3 on main) AND THE FIRST COUNT

cc (main), 2026-10-09, after S112. **Sealed before `couplings_on_the_ruled_branch.py` runs.** No data. 0 of 19.

**Why it matters.** B1634 verified that on the owner's ruled branch the modulus τ is the state that breaks the weave's
group, so couplings in τ alone are vector-valued modular forms for the theta constants' multiplier and the flavour numbers
are their values at τ. The SM seat's W50 §3 says these couplings give non-permutation mixing at a generic τ and are
degenerate at i and ω. Its second ask is the count of free numbers once the weights are fixed. The owner's restated goal
is the SM's structure and how many free numbers the principle leaves. This arc verifies §3 by main's own route and gives
the first count.

## Seen first

`VERDICT topic-sweep /couplings in tau alone|vector-valued modular|ruled branch|free numbers|modular flavour/: 2 of 1406 arcs on main match (PROVED 2)` — B1634 (T-RULED-INNER, T-WEAVE-LIFT-IS-THETA; P4's polynomial route), B1620, B1625, B1630, the
SM seat's W50 (its N4/N5 numbers and its extra read-outs at i and ω, read before this seal), W41, W39. **Literature:** the
ring of modular forms of Γ(4) (polynomials in θ₂², θ₃², θ₄² modulo θ₃⁴ = θ₂⁴ + θ₄⁴); modular flavour symmetry (couplings
as vector-valued modular forms of the field weights; Feruglio 2017 and its sequels), for the shape of the count.

## Disclosed

- **Not blind.** The seat's W50 numbers were read before this seal, and several predictions are its numbers. The seat's
  stored read-out at i shows one generic symmetric coupling at k = 5 that is NOT degenerate (smallest relative gap
  0.059), against its sentence "at i and ω every coupling is degenerate". K5 is sealed on the stored numbers, not the
  sentence.
- **The route is main's own.** The pieces are polynomial maps in θ₂², θ₃², θ₄² modulo the quadric, equivariant under the
  weight-one multiplier, with η¹⁸ cleared for T ⊗ T and the cusp condition imposed on exact q-series. The
  Borcherds–Skoruppa formula runs beside it as a cross-check.
- **An antisymmetric 3 × 3 matrix always has singular values (s, s, 0).** So O⁻ couplings are degenerate everywhere by
  algebra. K3 excludes them, and K5 counts them only as degenerate.
- **The weights are not fixed by the principle.** The count is a function of the sectors' weights. Which sector sits at
  which weight (the field-theory dictionary for the zero modes' and the Higgs's weights) is not earned here.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **K1** | T ⊗ T, k = 1, 3, …, 11: the algebraic dimensions equal the formula's; by piece D 0, 0, 1, 1, 2, 2; O⁺ 1, 1, 2, 2, 3, 3; O⁻ 0, 1, 1, 2, 2, 3; the forms pass the transformation laws (< 10⁻¹⁰) and a random non-equivariant control fails them (> 10⁻²) | 85% |
| **K2** | T̄ ⊗ T, k = 0, 2, …, 10: algebraic = formula at every allowed weight; at k = 0 the only coupling is the identity | 85% |
| **K3** | at three generic τ, every D and O⁺ coupling with k ≤ 7 and every generic symmetric combination at k = 5 and 7 has three distinct masses (smallest relative gap > 0.05); every O⁻ coupling is (s, s, 0) | 70% |
| **K4** | at τ₀ = 0.17 + 1.13i: (a) O⁺ at k = 3 against D at k = 5 has distance 0.6709 ± 0.001 from the permutations; (c) D at k = 5 against D at k = 7 has distance < 10⁻⁸ | 80% |
| **K5** | (i) at ω every T ⊗ T coupling read is degenerate; (ii) at i every single-piece T ⊗ T coupling is degenerate; (iii) at i at least one generic symmetric combination at k = 5 is not | 60% |
| **K6** | d_sym = 1, 1, 3, 3, 5, 5 for k = 1, …, 11; two sectors at the lowest symmetric weights (k = 1, 3; d = 1 each) leave 2 + 1 + 1 = 4 free real numbers; at the three generic τ their masses are non-degenerate and their mixing is not a permutation (distance > 0.05) | 55% |

**The reading, written before the run (the cells can only lower it).**
- **If K1–K4 hold,** the seat's W50 §3 is verified on main. On the ruled branch, couplings in τ alone give three distinct
  masses and non-permutation mixing at a generic τ.
- **K5 decides** whether "degenerate at i and ω" is a property of the points or of the couplings read.
- **If K6 holds,** the first count stands. Given the sectors' weights, the flavour sector leaves 2 + Σ_s (2 d(k_s) − 1)
  free real numbers. At the lowest weights, two sectors leave 4 numbers (τ and two normalizations) for the 10
  observables of a quark-like pair, which is 6 relations if the dictionary holds.
- **None of this fixes a value.** τ and the weights are not fixed by the principle, and the dictionary is unearned. The
  count is the first answer to "how many", and its values are not compared with data here.

## Instruments

`verification/couplings_on_the_ruled_branch.py`; hashes in `ARTIFACT_HASHES.txt`.
