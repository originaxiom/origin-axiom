# SM-C2 closed: the physical lane's twenty results of 2026-11-03 and 04 (batch V2) — twenty REPRODUCED

*Closes the card `relays/cards/SM_C2_physical-lane-batch-V2.md` (M1 on main's docs/seats/sm.md). The checks and their
outputs, with the lane's controls run as found, are in `relays/sm_c2/`, committed before this note. Firewall kept: no
coupling, mass or angle was evaluated against a measured value, and no file with agy_ in its path, no file auditing
another lane's values and no target file was opened.*

## The verdicts

Every verdict is conditional on the source constructions each item names (the curved action, the parallel phase, the
physical mass map, the complete-domain realisations), as every item states.

| row | item (the lane's branch, commit read) | verdict | why, in one line | where |
|---|---|---|---|---|
| 1517 | T-NORM intake (ce2a3a6e3) | REPRODUCED | its corrections are right: main's B1822 record makes H = I a CHOSEN input; the lane's coefficient-metric note confines its scalar result to the constant, fibre-parallel, move-invariant class and exhibits a positive nonconstant family; the receipt's 40 source pins and 6 artifact digests match the git objects; P210's ten tests start and pass once each, recounted from its log | `relays/sm_c2/row1517_tnorm_intake.py` |
| 1518 | light cubic, rescaling invariant, two-loop running (8f4d100ad) | REPRODUCED | B (eq. 9) and G = wB, ∝ (2, −37, 33) at κ = 1, the c_r table and both equal-coupling sums; the β function (11) from (1), with its pure-SYM limit; w·b = w·C = 0 and I = 2πC + 3 log(g₃²/g₂²) + W_Z; the frame shift −2 log abs(det A); κ(u, [a, cQ₀]) = 0 on all of ker ad Q₀ | `relays/sm_c2/row1518_two_loop.py`, `relays/sm_c2/row1518_invariant_and_cubic.py` |
| 1519 | CP¹ orbit metric and the W_eff = 0 lemma (0dc9e65f9) | REPRODUCED | N₀ = 10π/g₆²; (5) gives t/2 in the 3-, 4- and 5-dimensional irreps; κ(H²) = 2κ(E†E) and 2N₀/Z_t = 1; Fubini–Study from (4) in both charts, with A = Im z†dz; W's shear invariance; both hand controls (W_eff = 0 with K_eff as stated, and −cl³). The lemma stays conditional on its admission (9), as the item says | `relays/sm_c2/row1519_orbit_metric.py` |
| 1520 | full centralizer, flat family and metric (609c21c5b) | REPRODUCED | the cited Di Bella–de Graaf Table 5 (arXiv:2407.11801v1, p. 18, read here) lists E₈ orbit A4 with c′₁ = A4, dim t = 0, component group S2, so K = SU5_g ⋊ ℤ₂ as applied; own: J X J⁻¹ = −Xᵀ, dim Lie(K) = 24 from the 248's grading, the θ-fixed algebra so5, the one-form norm (5), det M_τ = 1, the two-dimensional SM stratum and its 25 SU5 points, no S5 element acting as −1 | `relays/sm_c2/row1520_flat_family.py` |
| 1521 | generic roster, level-four map, 16 controls (ac28256fc) | REPRODUCED | N_j from the line formula; the uniform-roster condition equals χ³ ≠ 1 and χ¹⁰ ≠ 1 on every torsion point of order ≤ 60; 108 exceptions (1, 3, 8, 24, 72 by order), least admissible order 4; packets 12 → 6 and 48 → 24, each one orbit; the permutations (10) and intertwiner (11); the rejecting controls. Controls: 16 of 16 OK | `relays/sm_c2/row1521_generic_roster.py` |
| 1522 | order-ten cubic (b710d69c0) | REPRODUCED | the Lie coefficient −5 for every colour and weak pair, charges ±5; the endpoint law (7), dimensions 1/1 and 1/2, profile powers; the root-action charges; 104 → 128 chiral, R 1 → 13; β (10, 6, 4) + (10, 6, 4) = (20, 12, 8) with zero w-contraction, from this seat's field table | `relays/sm_c2/row1522_1524_cubics.py` |
| 1523 | three-lens intake (b77117f6b) | REPRODUCED | its six corrections hold: GL(1,ℤ) = {±1}, with n ↦ n + 1 beyond it; F is symmetric, and enumeration gives F and PFP as the only cost-3 minimisers ([[2,1],[1,1]] and its exchange at det +1, cost 5); MᵀJM = det M·J for every M; xy on F₂ is skew but not alternating; Q8 and D4 share the pairing and differ in q; 0708.0669 assumes q odd, and 0808.1664 is the characteristic-two Weil representation | `relays/sm_c2/row1523_three_lens.py` |
| 1524 | order-three R doublets, √(8/5) (1cc2b94de) | REPRODUCED | exact order three ⟺ χ³ = 1, χ² ≠ 1: 8 characters, 4 after inversion; 100 + 12κ; ε(b₀,Z,Z) = −2√6/5 and ε(b₄, b₀∧b₁, Z) = −√(3/5) by literal wedges; u, r, a are roots, sum zero, QY +1, −3, +2, grades −2, +1, +1; the normalisation cancels I_j: (4√3/5)g₄, √(6/5)g₄, ratio √(8/5); the up grade sum +1; (11) gives −12/5 | `relays/sm_c2/row1522_1524_cubics.py` |
| 1525 | exact classical EW branch (e181282de) | REPRODUCED | the root grades; G = √10·Y₀ with [E, G] = 0, [G, G†] = H, κ(E†G) = 0; the vacuum equation (6) for all a, b; the stabilizer's dimension 9 (su3 ⊕ u1_em) from row 1528's (0,0) count | `relays/sm_c2/row1525_ew_branch.py` |
| 1526 | eight EW-branch controls, unrun (d355ff9a1) | REPRODUCED | the package is as stated (eight tests); run as found, 8 of 8 OK; its subject matter is reproduced by this seat's row 1525 check | `relays/sm_c2/lane_controls/MANIFEST.json` |
| 1527 | W/Z matching with the heavy response (7f59ec2b9) | REPRODUCED (algebra); comparison with a measured weak angle: CANNOT CHECK | eigenvalues 0 and 8/ℓ², so m_W² = 5s/ℓ², m_Z² = 8s/ℓ², sin²θ = 3/8 as the leading SU(5) relation; κ(t_Z²) = 1/2; d_⊥ with κ = 14/25, its graded form the spin-two m = 0 member; 56/15 and 4/3; ρ = 1 + s/5. The item makes no measured comparison, and none is made here: it is outside M1's firewall | `relays/sm_c2/row1527_vector_matching.py` |
| 1528 | complete two-field kernel (f5f1042d6) | REPRODUCED | B_Z J₅ = E₅/√10 and the frame identities (1); two commuting triples; the whole 248 from E₈'s roots, split by source and decomposed under the two triples exactly as the table; the diagonal 24V₀ + 11V₁ + 21V₂ + 11V₃ + V₄, also from row 1525's w; the module counts; flat lines single-valued from QY; the roster per spin, 63/87 chiral, 9 vectors, 72/96 | `relays/sm_c2/row1528_two_triple_kernel.py` |
| 1529 | six kernel controls, unrun (d5c06027b) | REPRODUCED | the package is as stated (six tests); run as found, 6 of 6 OK; its subject matter is reproduced by this seat's row 1528 check | `relays/sm_c2/lane_controls/MANIFEST.json` |
| 1530 | an existing neutral field lifts the up kernel (b061fd9a9) | REPRODUCED | the generator change (2); the source coefficients ad − bc and ad + bc, equal to −2abκ₋ and 2abκ₊; the pole bounds; the first-order block determinant ∝ (ad − bc)²(ad + bc)²; the block elimination (6) as an exact determinant identity, with F(ε)/ε → A | `relays/sm_c2/row1530_neutral_lift.py` |
| 1531 | four neutral-lift controls, unrun (bd0e1eb09) | REPRODUCED | the package is as stated (four tests); run as found, 4 of 4 OK; its subject matter is reproduced by this seat's row 1530 check | `relays/sm_c2/lane_controls/MANIFEST.json` |
| 1532 | the neutral family's whole charged kernel (76941fbf4) | REPRODUCED | the chain elimination f = (−1)^(N−1) t^N/∏c (N ≤ 6), with no division by t; the line dimensions; the long exact sequences (up 2 on one exceptional plane, down 2 always, leptons H¹ = H² = 2 through rank-one maps); the charged A3 lines acyclic; 87/71/59 and 96/80/68 | `relays/sm_c2/row1532_neutral_family.py` |
| 1533 | five neutral-family controls, unrun (64b89a473) | REPRODUCED | the package is as stated (five tests); run as found, 5 of 5 OK; its subject matter is reproduced by this seat's row 1532 check. The lane's own sub-agent review (52e6571dd) was not relied on | `relays/sm_c2/lane_controls/MANIFEST.json` |
| 1534 | register quadratic form to the odd spin (4996400b9) | REPRODUCED | with the lift rule (1), ξ_q is well defined and linear for all four refinements; Arf = αβ; q ≡ 1 is q₍₁,₁₎, the only refinement fixed by SL(2,F₂), the other three one orbit; invariant classes 4/2/1 = 2^dim ker(Mᵀ − I) by order; LR, L²R, L²R² with 1, 2, 4 classes; q₍₁,₁₎ is periodic/periodic on the flat framing | `relays/sm_c2/row1534_1535_spin.py` |
| 1535 | spin/flavour twist as a global isometry (76a14763a) | REPRODUCED | the 16 pairs fall into 4 orbits of size 4, labelled by ε_S + ε_F; the combined centre is +1 in every row of the slot table; the gauge-only Ad(g) = −I fails on a nonzero bracket; the isometry argument, built only from unchanged tensor structures, reviewed | `relays/sm_c2/row1534_1535_spin.py` |
| 1537 | register/flavour joint, Gram and quartic test (e19aa4ddc) | REPRODUCED | [Q′, R′] = det U·[Q, R] and UᵀεU = det U·ε; [D, F_i] = [D, F_j] = 0 forces D = N·I₂ (one generator does not); on the EW branch abs(a) = abs(b) = 1/√2, N = 5/(2ℓ²); traces 10, 10, 20, 20, 0; C = (5/(8ℓ⁴))(r₂² + s²) with s = s_x, s_y, s_z as polynomials; the readout [[2,1,1],[1,2,1],[1,1,2]]; all Grams N·I₂. Controls: 5 of 5 OK (the agy lane's report of running them was not opened) | `relays/sm_c2/row1537_register_flavour.py` |

## The card's planted errors

Both were caught. Row 1530's block with one entry's sign flipped gives (ad − bc)(ad + bc)³, not the claimed law. Row
1521's roster condition without χ¹⁰ ≠ 1 disagrees with the uniform-roster condition at 99 torsion points. Every other
script also runs a planted error of its own, and each was caught (RUN_LOG.txt and the JSONs).

## The lane's controls

Six packages, 44 tests, were run once each as found, at the commits the rows name. Each checks.py's sha256 matches the
lane's blob. All 44 pass. By § 8 of the protocol this is a fact about the lane's code. Each item's verdict above rests
on this seat's own check.

## What was not done

- **The source constructions** the items rest on were not re-derived, as for SM-C1.
- **The analytic steps were reviewed in writing, not computed.** These are the Fredholm, graph-compact and closed-range
  transfers (rows 1528, 1530 and 1532), the Hodge and Serre pairings, the cusp profile bounds, ∫ω∧ω̄ ≠ 0 (row 1522),
  and the whole-operator isometries (rows 1535 and 1537).
- **Two results were applied rather than re-proved.** Johnson's 1980 bijection (row 1534) is cited, not re-read.
  Row 1520's component group is read from the cited table, not reproduced, as the item itself says.
- **Not computed separately:** row 1524's bundle weights of u, r, a (b₀, b₁ + b₄, b₂ + b₃). They agree with the
  coordinate order (6, 4, 7, 5, 8) and with the computed grades.
- **Literature read for rows 1520 and 1523:** arXiv:2407.11801v1, 0708.0669v3 and 0808.1664v1, fetched here. Their
  digests are in the JSONs, and the files are not committed.
- **Fixes to this seat's own code before its in-tree run:**
  - Row 1517: a misread log field name, and a reflowed line.
  - Row 1523: a characteristic-two helper written wrong, and a planted error that did not bite. The plant was replaced
    by the source's own phrase.

  No value of the lane's changed.

## For main

Twenty REPRODUCED. Row 1527's comparison with a measured weak angle is CANNOT CHECK under the firewall, and neither the
item nor this seat makes it. The lane's 44 controls pass as found. With SM-C1, M1 is complete: thirty items, thirty
verdicts. Nothing is needed from main or the lane for this batch.

0 of 19.
