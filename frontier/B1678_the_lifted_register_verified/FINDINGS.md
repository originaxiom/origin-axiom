# B1678 — THE LIFTED REGISTER, VERIFIED ON MAIN: the four wordings lift coherently through a central double cover that keeps each operation with its coefficient action; the record's pointwise lift is not a group section, and the sign audit finds one banked number moved and no verdict that the record had not already corrected

**Verdict: PROVED (a verification arc).** cc (main), 2026-10-20. POINT_REGISTER P-207 and P-204. 0 of 19.
- **What this arc re-banks.** The audit lane's word-architecture audit, 41 commits from c5c467891 to 17cdad33a on its
  branch, written 2026-10-17 to 10-20 after the owner's question about wordings. The lane labels its results
  analytical and unreviewed, and says in more than twenty places that no physical input is paid. That statement is
  accurate.
- **How it was verified.** One reading pass for main re-implemented every algebraic claim from its stated definitions
  with its own code (`verification/main_check/s1–s9`), without running the lane's packages. A second pass, the sign
  audit, re-ran every main arc that uses B1617's lift, with the multiplicative lift substituted. Main rechecked the
  decisive numbers itself.

## 0. Seen first

`VERDICT topic-sweep /lifted register|central (lift|extension)|lift_of|point.push|intertwin|Gate 12|composition law/: 19 of 1450 arcs on main match (NEGATIVE 3, OPEN 1, PROVED 15)`
— chiefly B1641 (W46 on main: the point-pushes act by parity signs; Gate 12 open), B1672 (Gate 12 closed to shear-word
length 7 after an odd η-twist), B1600, B1606. **Literature:** central extensions and lifting obstructions; Aut⁺(F₂) as
the pure mapping class group of the twice-marked torus (Bridson and Wade).

## 1. What holds (`verification/main_check/`)

| claim | result |
|---|---|
| the lifted register E = {(φ, g): ρ∘φ = Ad_g ∘ ρ} is a central double cover of Aut⁺(F₂), each elementary wording with an SU(2) intertwiner (L: (1 + i)/√2, R: (1 − j)/√2, and their mirrors) | **holds:** the intertwining error is 3 × 10⁻¹⁶ on 300 random words, and the cocycle on V holds to 10⁻¹⁵ |
| **the composition law resolves the commutator conflict** | **holds.** Δ⁴ lifts to (I_c, +1) = ε·J_c. The commutator of the inner lifts is J_c, with D_ε = −I and D_{J_c} = +I on V. This replaces B1672's census to word length 7 by a structure |
| its corrected relation s⁴ = ε J_c⁻¹; the cover does not split | **holds** |
| finite refinements: the lifts' local quotient is 2O (order 48), onto Aut(Q₈) (order 24); (I_c, +1) has trivial local image yet is a non-trivial automorphism | **holds** |
| the joint image of the matter triplets V and the boundary module W has order 192 | **holds, with scope:** a subdirect product of two reducible modules (commutants 2, 2; joint 4), matching B1672 (96 on V, 48 on W). It does **not** supply irreducibility, and the parity matrices are not in W's image. B1672's "the extreme domain is chosen" stands |
| the coupling's transport needs a phase that quaternion transport misses: Y ↦ O Y Oᵀ exactly, with αβ = z⁻²; averaging rotated copies manufactures rank (Y₀ of rank one averages to −2I/3) | **holds**, a guard against a bad join |
| the theta field's automorphy: F(τ + 1) = e^{iπ/8} g_L F and F(−1/τ) = e^{−3iπ/8} τ^{1/4} g_S F | **holds** to 30 digits |
| the puncture's connecting map, F = z^{−1/2} b + O(z^{3/2}) with b ≠ 0, and the kernel table (3, 3), (3, 0), (0, 3), (0, 0) for Λ = U, ℂ⁶, 0, U^⊥ | **holds:** the expansion to 10⁻³¹. The table is conditional on the lane's finite-distance Fredholm application, which was not checked independently |
| a state-dependent rank-3 boundary family is covariant on an open set but cannot extend to the symmetric state, where Q₈'s stabiliser makes every invariant subspace even-dimensional | **holds** |
| B1043's triangle group has H³ = ℂ³ although its presentation complex has none (a scope correction to W4's "no triple product") | **holds,** by hand |
| the projective end law: the residue vanishes exactly at d = 0 or 6 | **holds as algebra.** The degree −3 + 6q leaves the integer and the side free; it selects no count and no chirality |

## 2. The sign audit (P-207)

- **The finding.** B1617's pointwise lift `M_of` is not a group section. For 55 of 200 random pairs of positive words
  (62 of 200 in the sign audit's own draw), the lift of the composite is minus the product of the factors' lifts.
- **The audit.** Every main arc that calls it (B1617, B1618, B1620, B1621, B1630, B1632, B1634, B1641) was re-run with the
  multiplicative lift substituted. The unpatched run reproduces all twelve stored outputs exactly.
  - **Unaffected:** B1617, B1618, B1620, B1621, B1641.
  - **B1630, one number moves, the result stands:** S̃ = R L⁻¹ R has eigen-turns (⅜, ⅞, ⅞) under the multiplicative lift,
    not the (⅜, ⅜, ⅞) its FINDINGS states. Main rechecked: the two lifts differ by exactly −1. Order 8, the group order
    and every ℤ₃ cell are unchanged. A dated note is added.
  - **B1632, a verdict moves, and the record already corrects it:** its C1 ("no identification satisfies the Mp₂(ℤ)
    relations") becomes 4 of 8 under the multiplicative lift. Its claim line already reads "REFUTED IN PART by
    B1634", and B1634 disclosed this sign itself (its P6). A dated note names the mechanism.
  - **B1634:** its sealed half-turns move, as it disclosed. Its banked claim rests on its post-seal word-lift
    computation, which does not move.
  - **B1641:** its "the record's uniform lift acts on Δ⁴ by −1" is the lift of the automorphism. The non-homomorphic
    inner lifts are the central extension it reports, not an artefact. A wording note is added.
- **Not covered:** words longer than 7 in the patched tabulation; arcs outside the eight.

## 3. What it says

- **Gate 12 is closed by a structure.** Keeping each operation with its coefficient action (the "registering
  relation" of the owner's argument, P-204) gives one coherent action of the four wordings. B1672's census to word
  length 7 is superseded by the central double cover.
- **No physical input is paid.**
  - The joint 192-element image is reducible.
  - The extreme boundary domain stays chosen.
  - The projective end law leaves the integer and the side free.
  - The covariant end family dies at the symmetric state.
- **The lead it opens (the audit lane's, and main's choice for next).** A state-dependent rank-3 end family exists on an
  open set but not at the symmetric state, while the extreme domains d = 0 and 6 are the projectively regular ones. What
  happens as the family approaches the stabiliser locus, and what its index is there, is a computable question.

## 4. Files

- `verification/main_check/`: the reading pass's scripts and logs (s1–s9), its report, and the sign audit's report.
- The lock: `tests/test_b1678_the_lifted_register_verified.py`.
