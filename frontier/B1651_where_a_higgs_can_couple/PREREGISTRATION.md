# B1651 — PREREGISTRATION: WHERE A HIGGS CAN COUPLE THE ZERO MODES — no harmonic Higgs in the bulk; every point coupling is isotropic (an identity), so a point Higgs anywhere leaves one generation massless; the moves carry the pairing's triplet exactly at every point; only the half-periods' triplets are independent of τ; so the puncture is not forced (Step 4 answered: a choice)

cc (main), 2026-10-14. **Sealed before `where_a_higgs_couples.py` runs.** No data. 0 of 19. POINT_REGISTER P-131
(Step 4 of the field's genesis, `speculations/S_THE_FIELDS_GENESIS.md`); P-129's first premise.

**Why it matters.** Today's readings showed that B1644–B1649's first-generation zero and the identity of "the Higgs in
M" depend on the frame (B1649's addendum). Step 4 asks where a Higgs can couple the zero modes at all, and whether
anything forces the puncture. If something does, P-129's first premise is not a choice. If nothing does, the record
must say so before the frame tribunal (P-136) tables it.

**The derivation, by hand, written before the run.**
1. **The boundary datum.** The zero modes are spinors (W21), and the moves force their square-root end condition at the
   puncture (W22, verified by B1606). Two of them pair to a one-form g(z) dz with a simple pole, where
   g = c_r θ_r(0)θ_r(z)/θ₁(z) (B1642's sealed R2). A one-form's residue is invariant under every local coordinate change
   z = λw + μw² + …. Read instead as a quadratic differential g dz², the coefficient of w⁻¹ scales by λ, so it is not
   canonical. At a regular point the datum is a value, canonical given the flat frame dz, which is unique up to one
   overall scale on an elliptic curve.
2. **The bulk, and the premise that localises the Higgs.**
   - Every non-zero pairing g carries a non-trivial 2-torsion character (B1642's R5). A flat non-trivial degree-0 line
     bundle on an elliptic curve has h⁰ = h¹ = 0 (Riemann–Roch). So **no flat or harmonic bulk Higgs couples**; the web
     seat's O1 is the same fact. The punctured, parabolic version of this statement is owed, not shown here.
   - What remains are couplings at points. The pairing is odd, g(−z) = −g(z), and the monodromy contains −I. So a point
     Higgs's locus is −I-invariant, a union of pairs {z₀, −z₀}. On a pair it couples as (1 − ε)·Y(a; v(z₀)), where ε is
     the Higgs's parity under −I.
   - **Premise P1 (stated, not derived; no cell tests it): the Higgs is even under −I and sits at a single point.**
     Under P1 it couples only at the involution's four fixed points: the puncture and the three half-periods. An odd
     Higgs (ε = −1) would couple at generic pairs. The parity is lift- and frame-dependent: B1600's lift of −I is k,
     and Ad(k) = diag(−1, −1, 1) makes the i and j directions odd. That is the SM seat's W71 point that the frame
     decides the Higgs's parity.
   - N-torsion orbits are finite covariant systems for every N. P1's single point and −I-invariance are what select
     N = 2.
3. **Isotropy is everywhere; τ-independence is the half-periods' own.**
   - By the theta identity θ₄(z)²θ₄² + θ₂(z)²θ₂² = θ₃(z)²θ₃² (Whittaker–Watson §21.2), v(z) = c_r θ_r(0)θ_r(z)/θ₁(z)
     satisfies v·v = 0 at **every** z. So a point Higgs anywhere leaves one generation exactly massless at one τ;
     B1649's zero is not special to the puncture.
   - At the half-periods v has one component zero: ∝ (0, −1, i), (i, 0, 1), (i, −1, 0) for ½, τ/2, (1 + τ)/2. These
     directions are independent of τ up to the Klein group V₄ of component sign flips. V₄ is the representative
     ambiguity: z₀ + π flips θ₂ and θ₁ (the half-turn about e_i), z₀ + πτ the half-turn about e_j, and V₄'s elements
     are exactly the three characters' sign patterns. The puncture's R(τ) and a generic point's triplet vary with τ.
4. **The moves carry the triplet function exactly, at every z.**
   - In B1600's convention (`w10_check.py`), L: a ↦ a, b ↦ ab is τ ↦ τ + 1 (z ↦ z), and R: a ↦ ab, b ↦ b is
     τ ↦ τ/(τ + 1) (z ↦ z/(τ + 1)). On the 2-torsion classes (a/2 = ½, b/2 = τ/2), L fixes ½ and swaps τ/2 and
     (1 + τ)/2; R fixes τ/2 and swaps ½ and (1 + τ)/2; both fix the puncture.
   - **Under L:** θ₂ ↦ e^{iπ/4}θ₂, θ₁ ↦ e^{iπ/4}θ₁ and θ₃ ↔ θ₄. With c = (−1, −1, i) this gives
     v′ = e^{iπ/4}(v_i, v_k, −v_j) = e^{iπ/4}·Ad(g_L)⁻¹v.
   - **Under R = S T⁻¹ S⁻¹:** S swaps θ₂ and θ₄ with c_i = c_j, which is minus the half-turn about (1, −1, 0).
     Conjugating gives v′ ∝ Ad(g_R)v.
   - So the theta action is L ↦ Ad(g_L)⁻¹ = Ad(i·g_L) and R ↦ Ad(g_R): B1600's lift, twisted by the V₄ element i on L.
     At the transformed point, the triplet is exactly the old one moved by this law, with no V₄ element, at all four
     fixed points.
   - **Covariance.** In the surface frame, where the moves act, the move-invariant non-empty subsets of the four fixed
     points are three: the puncture alone, the half-period orbit alone, and both. In the fibre frame at one τ the moves
     are already broken by τ, and covariance imposes nothing.
5. **The lifts' group and its constant directions.**
   - g_L = (1 + i)/√2 and g_R = (1 − j)/√2 act on M as the quarter-turns about e_i and about e_j (the second clockwise).
     They generate the cube's rotation group O (24 elements), irreducible on M ⊗ ℂ. So no line in M is invariant under
     the moves, even up to a character.
   - Modulo V₄, the twisted moves are D·Ad(g_L) and D·Ad(g_R) for D ∈ V₄. These are quarter-turns about e_i (D = 1, i),
     half-turns about (0, 1, ∓1) (D = j, k), quarter-turns about e_j (D = 1, j), and half-turns about (1, 0, ∓1)
     (D = i, k).
   - A half-turn about (0, 1, ∓1) has the −1 plane {w_j = ±w_k}, and one about (1, 0, ∓1) has {w_i = ±w_k}. Each of
     the four half-turn pairs meets in one line (ρ, σ, 1), with ρ, σ = ±1: the four body diagonals, with both
     eigenvalues −1. The 12 pairs involving a quarter-turn share no line.
   - So the twisted moves share exactly the four body diagonals. These are real, maximally far from the isotropic cone
     (∣a·a∣ = ∣a∣²), where B1646 places no hierarchy.
   - V₄ is the kernel of O's action on the three half-period classes (the coordinate axes), and the image is
     S₃ = SL(2, ℤ/2).

## Two corrections before the seal (disclosed)

- **Main's own (2026-10-14, afternoon).**
  - The first draft (unsealed) predicted that the V₄-twisted moves share no eigenline, and read "where the moves act,
    the puncture is the only locus".
  - Its instrument took eigenvectors from `np.linalg.eig`. That can miss a shared line inside a twisted half-turn's −1
    plane, so the cell could have passed falsely.
  - By hand, both claims fail (steps 4 and 5). The design notes had already listed the half-period orbit as a covariant
    option; the draft preregistration had dropped it.
- **A pre-seal review** (a read-only reviewing agent of main's, by hand and by reading; it computed no cell). Main
  checked every item and took it:
  - step 2's localisation to the fixed points is a premise (P1), not a derivation;
  - the covariant subsets are three, and only in the surface frame;
  - U3's isotropy holds at every z by an identity (E82: as a test of the fixed points it could not fail), so it is now
    labelled an identity and paired with a negative control on τ-independence;
  - the second draft's U4 tolerated V₄, so at the half-periods it tested only the class permutation. It now predicts
    the exact law with no V₄ element, plus a swapped-matrix control;
  - the V₄ read-out recorded one argmax among ties; it now records every attaining element;
  - one tolerance used default rtol; isotropy was computed in double precision; the half-lattice distance was not
    asserted; U1 had no aliasing guard; U6 duplicated its pairs and was cited for the orbit's mixing, which it does not
    measure; step 5's plane equations were misstated.

## Seen first

`VERDICT topic-sweep /half.period|2.torsion|fixed point.*involution|elliptic involution|pillowcase|where a Higgs|bulk Higgs|Riemann.Roch|residue.*canonical|Higgs.*localis/: 29 of 1422 arcs on main match`
— mostly word matches. The nearest precedents:
- B343: the deck ℤ/3 acts irreducibly on the object's Klein 2-torsion and forces a mixing pattern (θ₁₃ = 0); 2-torsion
  structure in mixing, from an earlier era;
- B353: the hyperelliptic involution induces E₆'s diagram involution;
- B1649 and B1650: the kernel at the puncture, and chat1's O1 and O6;
- B1600 (`w10_check.py`): the moves' convention and lifts, used as given.

None asks where a Higgs can couple the zero modes. Also read before the seal:
- the web seat's O1, O6 and C6 (verified in part, B1650), and its first-row check at `67821b8ea` (an isotropic and a
  real direction overlap by at most ½; it lists "a complex non-R neutrino direction" among the escapes);
- the SM seat's W64, W65, W71, W72, and its reading after W71 (the frame decides the Higgs's parity);
- the audit lane's field map (the puncture's −1 is the weak centre in its E₈ frame).

**Literature:** Riemann–Roch on an elliptic curve; SL(2, ℤ) on the 2-torsion points through SL(2, ℤ/2) ≅ S₃; the
thetas' transformation laws under T and S, and the identities of Whittaker–Watson §21.2; the residue theorem; the
rotation group of the cube and its Klein normal subgroup.

## Disclosed

- **Seen before the seal:**
  - **Numerical, not by hand:** main evaluated U3's quantities at the four fixed points (isotropy, and the half-periods'
    τ-independence) at 4 random τ, to 10⁻³¹. So U3(a) and U3(b) were seen before the seal.
  - main's and the reviewer's hand derivations of steps 3–5. The reviewer's hand check finds every one of U4's eight
    exact-law rows matched with no V₄ element.
  - main's by-hand estimate that one representative pairing (the puncture against ½ on τ = iy) matches the observed
    ∣V_ud∣ near Im τ ≈ 1.6. With τ free that is a fit, and V₄ makes it representative-dependent. U6 is a read-out of
    single-point overlaps, not a prediction, and no data are read.
- **The nome root.** Under τ + 1 with Re τ > 1, mpmath's principal q^{1/4} puts a factor −i on θ₁ and θ₂, which would
  break U4 spuriously. So the instrument builds θ₁ and θ₂ from θ₄ and θ₃ with q^{1/4} := e^{iπτ/4}.
- **The plumbing was run before the seal on known cases only** (`controls.py`, output in `controls_output.json`):
  - a known Laurent series, to 6·10⁻³³;
  - the explicit-root thetas against mpmath's at ∣Re τ∣ < ½ (8·10⁻³²), and against the direct series at Re τ = 1.37
    (6·10⁻³²);
  - the puncture triplet equal to banked R, and its isotropy as Jacobi's identity at a control τ;
  - the lattice reduction on four constructed points;
  - the joint-eigenspace finder on four pairs known by construction;
  - Ad(g_L)e_j = e_k;
  - a constructed V₄ tie, ['1', 'i'].

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **U1** | for each unit at two τ and three random (λ, μ) with ∣λ/μ∣ > 5 × the contour's radius: the one-form's residue is unchanged to 1e-15 relative; the quadratic differential's w⁻¹ coefficient over the residue equals λ to 1e-15 (the control) | 95% |
| **U2** | each unit's pairing function has multipliers ±1 (to 1e-15) under z ↦ z + π and z ↦ z + πτ, never both +1 (a non-trivial character) | 95% |
| **U3** | (a) an identity, checked: ∣v·v∣/∣v∣² < 1e-25 in mpmath at the four fixed points and at three generic points (fixed lattice coordinates) at 4 random τ; (b) each half-period triplet's direction agrees across the 4 τ up to V₄ and a phase (overlap > 1 − 1e-12); (c) the negative control: for the puncture and each generic point, every pair of τ has best overlap over V₄ < 1 − 1e-6 | 95% |
| **U4** | at 3 random τ: for L at s = −1 and R at s = +1, the triplet at the transformed point z/(cτ + d) on the fibre at γτ has overlap > 1 − 1e-12 with Ad(g_γ)^s of the old triplet with no V₄ element, at all four fixed points; the transformed half-periods lie in the predicted classes, within 1e-12 of the half-lattice; the negative control (each move's transformation against the other move's matrix, either power, best over V₄) has overlap < 1 − 1e-6 at the puncture at all 3 τ | 90% |
| **U5** | the lifts generate 24 rotations; their commutant on ℂ³ has dimension 1; the untwisted moves share no eigenline (smallest σ > 1e-6), and an L-eigenline's best overlap with its R-image is ½ (to 1e-12); over the 16 V₄-twisted pairs there are exactly 4 shared lines, each of joint dimension 1, all body diagonals (to 1e-12, no relative tolerance), real (imaginary part < 1e-12 after one phase), and 4 distinct; the group's elements that fix all three half-period classes are exactly V₄, and it induces 6 permutations of them | 90% |
| **U6** | read-out: single-point null vectors' overlaps, one fixed point per sector, for each unordered pair of fixed points and each V₄ sign at one τ. This is not the orbit's mixing (on the orbit no generation is massless) | — |

Read-outs recorded beside U4, with no prediction: for each power, the V₄ elements that attain the overlap at each point.
By hand the other power passes with the move's axis unit, and at the half-periods also with that point's own
half-turn.

**The reading (the cells can only lower what they test; P1 is a premise, and no cell tests it).** If U1–U5 hold:
- **No flat or harmonic Higgs couples the zero modes in the bulk.** Under P1 (an even, single-point Higgs) a Higgs
  couples at the involution's four fixed points: at the puncture by the residue, canonical with no frame (U1), and at a
  half-period by the value, canonical given dz up to one common scale. An odd Higgs would couple at pairs {z₀, −z₀};
  that is not tested here.
- **Every point coupling is isotropic** (an identity, U3a). So at one τ, a single point Higgs anywhere leaves one
  generation massless. B1649's zero is a property of a single point at a single τ, not of the puncture.
- **The moves carry the triplet function exactly** (U4). In the surface frame the covariant loci among the fixed points
  are three: the puncture, the half-period orbit, and both. In the fibre frame at one τ covariance imposes nothing.
- **Step 4 answered: the puncture is not forced.** Nothing computed here forces it:
  - not covariance (U4);
  - not isotropy (U3a);
  - not the bulk (step 2).

  What distinguishes it is that its datum is a residue, needing no frame, and that its triplet varies with τ (U3c).
  What distinguishes the half-periods is that theirs does not (U3b). P-129's first premise ("the Higgs at the
  puncture") is a choice.
- **No constant direction in M is covariant** (U5). Modulo the Klein group only the democratic class (the four body
  diagonals) is, and it is real, so a covariant constant Higgs direction gives no hierarchy (B1646). A hierarchy needs a
  direction that varies with τ (the section, H-sec), or a breaking.
- **Owed, not computed here:**
  - whether fields localised at the half-periods are legal on the weave (the pillowcase's twisted sectors; the SM seat's
    W60; P-108);
  - the punctured, parabolic version of the bulk statement;
  - the odd Higgs's pair couplings;
  - the half-period orbit's mass structure: its three null vectors differ, so generically it gives all three
    generations mass, which is not computed here. Owed to the frame tribunal (P-136).

## Instruments

`verification/where_a_higgs_couples.py`; `verification/controls.py` (run before the seal) with
`verification/controls_output.json`; hashes in `ARTIFACT_HASHES.txt`.
