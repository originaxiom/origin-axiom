# B1651 — WHERE A HIGGS CAN COUPLE THE ZERO MODES: no harmonic Higgs in the bulk; every point coupling is isotropic, so a single-point Higgs anywhere leaves one generation massless; the moves carry the pairing's triplet exactly at every point; only the half-periods' triplets are independent of τ; the puncture is not forced

> *Audited 2026-10-15 by main (P-152, B1655): STANDS ONLY AS SCOPED: "not forced" holds for a point or density Higgs (premise P1). The grades, the corrected wording and the checks are in `frontier/B1655_main_audits_its_negatives/FINDINGS.md`.*

**Verdict: PROVED.** Every cell holds as sealed. cc (main), 2026-10-14. Sealed `6d6f7f660` before the run (6.1 s). No
data. **0 of 19.** POINT_REGISTER P-131 (Step 4 of the field's genesis); P-129's first premise.

## 0. Seen first

As sealed: `VERDICT topic-sweep /half.period|2.torsion|fixed point.*involution|elliptic involution|pillowcase|where a Higgs|bulk Higgs|Riemann.Roch|residue.*canonical|Higgs.*localis/: 29 of 1422 arcs on main match`.
- These are mostly word matches. The nearest precedents:
  - B343: the deck ℤ/3 on the object's Klein 2-torsion forces a mixing pattern;
  - B353: the hyperelliptic involution induces E₆'s diagram involution;
  - B1649 and B1650;
  - B1600's convention for the moves and lifts.
- None asks where a Higgs can couple the zero modes. Also read before the seal:
  - the web seat's O1, O6 and C6, and its first-row check (`67821b8ea`);
  - the SM seat's W64, W65, W71 and W72;
  - the audit lane's field map.
- **Literature:** Riemann–Roch on an elliptic curve; SL(2, ℤ) on the 2-torsion points through SL(2, ℤ/2) ≅ S₃; the
  thetas' transformation laws under T and S, and the identities of Whittaker–Watson §21.2; the residue theorem; the
  rotation group of the cube and its Klein normal subgroup. Nothing there asks this arc's question.
- **Known on the record and not claimed here:**
  - θ₂², θ₃², θ₄² generate the modular forms of Γ(4) (B1634);
  - R is Γ(4)'s weight-1 triplet (B1640, after Novichkov–Penedo–Petcov);
  - the web seat's C6: R reaches the coordinate-plane null lines only at the modular cusps.

## 1. The sealed run (`verification/where_a_higgs_couples.py`, unchanged; `where_a_higgs_couples.json`, `_run.txt`)

| cell | prediction | prior | result |
|---|---|---|---|
| **U1** | the one-form's residue is invariant under z = λw + μw² (to 1e-15 relative), and the quadratic differential's w⁻¹ coefficient over the residue is λ (the control); ∣λ/μ∣ > 5 × the contour's radius | 95% | **HOLDS:** 3.9·10⁻³⁰ and 4.2·10⁻³⁰; the smallest ∣λ/μ∣ is 10.9 radii |
| **U2** | each unit's pairing has multipliers ±1 under z ↦ z + π and z ↦ z + πτ, never both +1 | 95% | **HOLDS:** to 5.4·10⁻³⁰. The units i, j, k carry (+, −), (−, +), (−, −): the three non-trivial characters |
| **U3** | (a) isotropy ∣v·v∣/∣v∣² < 1e-25 at the four fixed points and three generic points (an identity, checked); (b) the half-period directions agree across 4 τ up to V₄ (> 1 − 1e-12); (c) the control: the puncture and the generic points do not (< 1 − 1e-6) | 95% | **HOLDS:** (a) 3.2·10⁻³¹ at the fixed points and 7.4·10⁻³¹ at the generic ones; (b) 1 − 2·10⁻¹⁶; (c) the best overlaps are 0.9930 (the puncture), 0.9974, 0.9992 and 0.9947 |
| **U4** | the exact law with no V₄ element, for L (τ ↦ τ + 1) at s = −1 and R (τ ↦ τ/(τ + 1)) at s = +1, at all four fixed points at 3 τ (> 1 − 1e-12); the images in the predicted classes, within 1e-12 of the half-lattice; the swapped-matrix control at the puncture < 1 − 1e-6 | 90% | **HOLDS:** 1 − 2·10⁻¹⁶ for both moves at all twelve rows; every image as predicted; the half-lattice distance is 1.7·10⁻³¹; the control is 0.9976 for both |
| **U5** | 24 rotations; commutant 1; no untwisted common line (smallest σ > 1e-6) and the untwisted best overlap ½; exactly 4 twisted shared lines, each of joint dimension 1, all body diagonals, real and distinct; the kernel on the half-period classes is V₄, with 6 permutations | 90% | **HOLDS:** 24; 1; no line (smallest σ 0.874), overlap 0.5000000000000002; exactly 4 lines, from exactly the four half-turn pairs (Ad(j g_L), Ad(i g_R)), (j, k), (k, i), (k, k), each with eigenvalues (−1, −1), joint dimension 1, real and distinct; the kernel is V₄, with 6 permutations |
| **U6** | read-out: single-point null vectors' overlaps, one fixed point per sector, for each V₄ sign (not the orbit's mixing) | — | the half-periods pairwise: ½ for every sign. The puncture against ½, τ/2 and (1 + τ)/2 at Im τ = 0.90: (0.192, 0.808), (0.212, 0.788), (0.231, 0.769). The two values per pair sum to 1, as the hand formula (1 ± θ₄²/θ₃²)/2 says for ½ |

**Read-outs beside U4** (no prediction; consistent with the hand derivation):
- The other power passes up to the move's axis unit: i for L at s = +1, and j for R at s = −1.
- At the half-periods the attaining set is that unit times the image line's own half-turn.
- The exact power needs no Klein element anywhere. Its only ties are the half-period lines' own half-turns.

## 2. What it says

- **No flat or harmonic Higgs couples the zero modes in the bulk.** Every non-zero pairing carries a non-trivial
  character (U2), and a flat non-trivial degree-0 line bundle on the torus has h⁰ = h¹ = 0. What remains are couplings
  at points.
- **Every point coupling is isotropic** (U3a, an identity: θ₄(z)²θ₄² + θ₂(z)²θ₂² = θ₃(z)²θ₃²).
  - So at one τ, a Higgs at any single point leaves one generation exactly massless.
  - B1649's first-generation zero is a property of a single point at a single τ, not of the puncture.
  - Lifting it needs couplings at two or more distinct points, or the τ-integration of the surface frame (W72), or
    what P-128 names.
- **The moves carry the pairing's triplet exactly, at every point** (U4).
  - L acts as Ad(g_L)⁻¹ and R as Ad(g_R), with no Klein element, at the puncture and at every half-period. In B1600's
    lifts this is the lift twisted by the Klein element i on L.
  - The half-periods' triplet lines go wherever the half-periods go: L fixes ½ and swaps the other two; R fixes τ/2
    and swaps the other two.
- **Only the half-periods' triplets are independent of τ** (U3b, with the control U3c). They are (0, −1, i), (i, 0, 1)
  and (i, −1, 0), the six isotropic points with a zero coordinate. By hand, not a cell: they are R's values at the
  cusps, (0, −1, i) at i∞ and, by S, (i, 0, 1) at 0.
- **Step 4 answered: the puncture is not forced.**
  - **Covariance** keeps three loci among the fixed points in the surface frame: the puncture, the half-period orbit,
    and both. In the fibre frame at one τ it keeps any of them.
  - **Isotropy** holds everywhere, so it does not pick the puncture either.
  - **The bulk** gives nothing.

  What distinguishes the puncture is that its datum is a residue, needing no frame (U1), and that its triplet moves with
  τ. What distinguishes the half-periods is that theirs does not. **P-129's first premise ("the Higgs at the
  puncture") is a choice.**
- **No constant direction in M is covariant** (U5: O is irreducible). Modulo the Klein group, which is the intrinsic
  ambiguity of the character sections (U2), the only covariant constant directions are the four body diagonals, the
  democratic class. They are real, so maximally far from the isotropic cone, and B1646 gives no hierarchy there.
  - A hierarchy needs a direction that varies with τ (the section, H-sec), or a breaking, or couplings at several
    points.

## 3. Scope and premises

- **Frame:** the weave's fibre (B1642's zero modes, given Λ); the surface frame where covariance is invoked.
- **Premise P1, stated in the preregistration and tested by no cell:** the Higgs is even under −I and sits at one
  point. It is what confines the couplings to the four fixed points.
  - An odd Higgs would couple at pairs {z₀, −z₀}.
  - The parity is lift- and frame-dependent. B1600's lift of −I is k, which makes the i and j directions odd. The SM
    seat's reading after W71 is that in Λ's frame the even factor is forced.
- **Not shown here:**
  - the punctured, parabolic version of the bulk statement;
  - whether fields localised at the half-periods are legal on the weave (W60; P-108).

## 4. Corrected twice before the seal

The preregistration discloses both corrections in full:
- main's own line-by-line review found a defect in the draft instrument, which could have hidden a shared line, and two
  false claims ("no twisted line", "the puncture is the only covariant locus");
- a read-only reviewing agent then found that the localisation was a premise, that the covariant subsets are three,
  that the isotropy cell could not fail (E82), and several tolerance and read-out defects.

Main checked every item and took it. The run was the first evaluation of U4–U6 by any instrument. U3's quantities at the
fixed points had been seen numerically before the seal, which the preregistration discloses.

## 5. Owed (registered)

- **The half-period orbit's mass structure.**
  - Its three null vectors differ, so at one τ a Higgs on the whole orbit generically gives all three generations mass,
    with triplets that do not depend on τ.
  - If covariance and the characters fix the directions at the three points and their relative Klein signs, the
    pattern would be a set of geometric numbers rather than functions of τ.
  - This is structure, not data, but it produces ratios. Owed to the frame tribunal (P-136), not computed here.
- the legality of half-period fields on the weave (W60; P-108);
- the parabolic bulk statement;
- the odd Higgs's pair couplings;
- the Klein sign of a Higgs's own character transformation, which fixes the representative ambiguity (U6) and decides
  any leading-order mixing between sectors at different points.

## 6. Instruments

`verification/where_a_higgs_couples.py` (sealed `6d6f7f660`, unchanged); `verification/controls.py` and
`controls_output.json` (run before the seal, on known cases only); outputs `where_a_higgs_couples.json` and
`where_a_higgs_couples_run.txt`; hashes in `ARTIFACT_HASHES.txt`; lock `tests/test_b1651_where_a_higgs_can_couple.py`.
