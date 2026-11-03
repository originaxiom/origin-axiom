# THE FRAMING LEDGER — what the programme excludes by the way it is framed (main, 2026-11-03; B1827)

*The owner's question, 2026-11-03: "what are we excluding by the way we frame the program?" — and "do it comprehensively and
properly, log everything so we clarify this once for all". This ledger is the consolidation; the raw inventory (five readers,
about 200 entries, every one citing the record) is kept in full in frontier/B1827_the_framing_ledger/verification/readers/.*

**How it was made.** Four readers inventoried the record in parallel — A1 the foundations and the bar (60 entries), A2 the
frame's construction including its code (39), A3 the tests' conventions (40), A4 the walls of the kill graph and the open
register mapped back to their causes (15 clusters, 14 groups of hatches) — and a fifth (A5) read blind, without the others'
lists, as an outside physicist. Main checked a sample of each reader's citations (all held: GENESIS line 370's "173
value-kills, 107 on flat premises"; SE2 CHOSEN at GENESIS line 191; B1790's NEGATIVE; P-489's typing conflict; cm_zero_line's
radii from the Re τ = 1/4 column), merged the entries below, and ranked them. **The ledger states commitments and tests; it
claims nothing.** The rule: a reframing must state what it newly predicts that the present frame cannot, and price its new
choices in bits, before any comparison with a measured value; one that adds a free parameter is a bigger menu, not an
explanation.

**Status words.** FORCED (proved), CHOSEN (recorded as a choice), READING, UNEARNED (an identification not earned),
UNSTATED (made implicitly — in a definition or in code — and never recorded as a choice). Reader ids: F- (A1), C- (A2),
T- (A3), W-/H- (A4), FC (A5).

## A. Foundations: what the object is, and how it is read as physics

| id | commitment | status | excludes | evidence it costs us | readers |
|---|---|---|---|---|---|
| FL-01 | Every physics reading of an object quantity is an identification (the listener map u); 37 ledger rows, 28 UNEARNED, none EARNED | UNEARNED; partly UNSTATED ("performed implicitly and for free") | nothing in particular: it is the price of every result | every value claim is conditional on a row of the identification ledger | F-18, F-26–F-30 |
| FL-02 | All frames are flat bundles on a 3-manifold (GAP6): they reach counts and signs, not continuous values | OPEN (GAP6) | curvature, flux and continuous moduli supplied by the geometry | **107 of the record's 173 value-kills sit on flat premises** (GENESIS l. 370); hatches H-09 (a coupling that sees hypercharge on one leg; curvature, flux) never tried | F-17, W-06, W-07, W-12, H-09 |
| FL-03 | Orientation: of m004 and its parent m000 take the orientable one, which is amphichiral (SE2) | CHOSEN (SE2) | chiral objects; an orientation-odd source of CP and chirality | eight banked walls pass through amphichirality (no dimensionful quantity, CS = 0, chirality not self-supplied, the CP sign external); "what dropping SE2 would break is not computed" | F-11, F-08, F-09, W-11 |
| FL-04 | The fibre modulus τ is free and detached from m004 (LR's apex Im τ = 1.12; no fixed line, det(LR − 1) = −1); the object is read through one fibre | CHOSEN / FITTED | τ placed by the object (a thread's apex, a torsion that matches the line's order); the family instead of one member | B1720 (the thread fixes the point: factor 1.80, 1.65% vs 1%, graded negative); the record's own rule "the object is the family" (FK13) | F-15, F-34, FC4, W-10, H-06 |
| FL-05 | No action: no dynamics for τ, no normalisation of the couplings, no gauge kinetic function, no scale | the record's working state (no action on record) | the gauge couplings, y_t, the Higgs mass and vev, the overall scale: about nine of the 19 have no frame at all | W-12 (the dimensional firewall), W-13 (no dynamics); F-35 (the observer supplies the unit) | F-35, C-07, C-08, FC7, W-12, W-13, H-08, H-11 |

## B. The frame's construction (FR-FIB, B1656's point coupling)

| id | commitment | status | excludes | evidence it costs us | readers |
|---|---|---|---|---|---|
| **FL-06** | **The Higgs's internal orientation S is built from i, j, k only (adjoint, no singlet channel), untwisted, one direction shared by the three sectors; the Higgs carries the flavour index** | UNSTATED in code (C-04, C-05); H-cov a tagged hypothesis | a singlet (identity-channel) component; a sector-dependent Higgs | the lock of both quark sectors' light states to the Higgs's null vector (B1739) and the CKM's corner inversion (B1826; at B1825's address ∣V_ub∣/∣V_td∣ = 11.3, sin δ 0.08). **Tonight (§ D):** a singlet component ODD between up and down lifts nature's corner order with ∣V_ud∣ > 0.9 from 2% to 33–47% of nature-like frame points at every phase; an even singlet does nothing; the frame's own twisted Higgs is even (B1744) | C-04–C-06, C-21–C-23, C-25, F-32, W-02, FC2, FC6, H-01 |
| FL-07 | One address: one τ, one line, one point coupling for all sectors | UNSTATED in code (C-09, C-10); stated as the down–lepton wall | separate loci for up and down (the CKM as a relative rotation); matter at different depths | masses and mixing never meet at one address (B1713, B1720, B1825: the six alone 1.36, the four alone 0.35, together 291); each sector wants its own depth (B1694: up 3.1, down 2.5, leptons 2.1); a point coupling has rank ≤ 2 (B1653) | C-09, C-10, C-31, T-20, W-03, FC1, H-02 |
| FL-08 | The lines are "flat lines of order ≤ 12", priced uniformly (8.06 bits), rather than centre Wilson lines | CHOSEN (reach); the reading UNSTATED | the lines' group theory: Z₅ of SU(5), Z₂ of SU(2)_L, Z₃ of colour (orders dividing 30) | A5: on order-5 lines the frame is minimal SU(5) — Y_u symmetric (R₁(up) = θ₁(5w) = 0), Y_e = Y_dᵀ — and "c = 3" is the Georgi–Jarlskog Clebsch put in by hand; the Z₅ × Z₃ lines (orders 15, 30) lie outside the sealed reach. **Main's check (B1827, order5_check.py):** on the order-5 lines (2/5, 0) and (1/5, 3/5), R₁(up) = 0 (to 3 × 10⁻¹⁶), Y_u is symmetric (to 10⁻¹⁶) and the down and lepton spectra are identical (on (2/5, 0) Y_e = Y_dᵀ to 2 × 10⁻¹⁵): minimal SU(5)'s Yukawa structure exactly; the order-10 lines that won the six's fits, e.g. (2/5, 1/10), break it slightly (Y_u not symmetric, 0.4–0.7; spectra within 1–17%); an order-7 control has none of it | C-11, T-21, T-36, FC3, FC5 |
| FL-09 | No electroweak doublet index: the "doublet" is the fibre's rank-2 flat bundle with Q₈ monodromy; the SM's reading (conjugate Higgs for up) is imported by hand | UNSTATED (C-02); the reading not derived (B1790, NEGATIVE) | a derived H / H̃ assignment | the eight readings are a menu (3 bits); the mixed reading orthogonalises the light states (B1739) | C-02, C-26, C-27, F-32 |
| FL-10 | The generations are three quaternion images of one doublet value at one point; no generation charge | partly stated (C-01); FK14 READING | generation charges (Froggatt–Nielsen); generations as ends, cover sheets or points of one history | rank ≤ 2 and V = 1 ⊕ U(2) at leading order (B1649); P-564 (the cover), the web seat's door D | C-01, C-19, F-19, F-27, FC3, H-06 |
| FL-11 | Normalisation: the kinetic metric H = I; channel weights √(2πL + c_s) mixing a flat norm and cut with a hyperbolic radius; the radii read off B1667's Re τ = 1/4 column | H = I CHOSEN (B1822); the rest UNSTATED | an underived metric's 8 real parameters per field; a consistent single metric | a democratic H of 0.1 moves the mass ratios 0.045 decades and the moduli 0.08 (B1822); the exact end shifts c_s 35–38% and the six then fail (S238, P-421) | C-13–C-18, C-36, F-30 |
| FL-12 | The lepton factor c = 3 is inserted by hand | CHOSEN (by hand) | a derived lepton/down factor | B1789, B1793, B1817 (not derived in the frame); B1798 prices the choice | C-28, F-33, T-24, W-04, H-09 |

## C. The tests

| id | commitment | status | excludes | evidence it costs us | readers |
|---|---|---|---|---|---|
| FL-13 | The frame's tree-level outputs are compared at M_Z with no renormalisation-group running and a flat 10% allowance in quadrature | the scale CHOSEN ("a human convention"); **no running UNSTATED** | a frame defined at another scale; structured theory errors | caps the information: the six can never compress (at most +6.98 bits before τ's price, against an 18.81-bit address; C_six < 0 at every address, P-554); the four carry at most 19.08 bits against the frame's own marginal (P-555); P-363: a and b run about 10% to the GUT scale | C-33, T-04, T-05, T-38, F-36, F-38, H-04 |
| FL-14 | Only the ten flavour numbers are graded; inter-sector ratios (y_b/y_t, y_τ/y_t), gauge couplings, the Higgs, PMNS and θ̄ never are | CHOSEN (THE FINAL ACT'S BAR's V list, not run) | a true answer whose content lies in the ungraded numbers | the inter-sector third-generation ratios are rigid outputs of a one-Higgs frame, never read (A5 #7; y_τ = y_b on order-5 lines) | T-01–T-03, F-37, FC9, FC10 |
| FL-15 | A value at σ, or nothing: the bar grades values, not relations | CHOSEN (THE_BAR) | the form of explanation flavour physics has — relations (b–τ, Georgi–Jarlskog, a symmetric Y_u), exponent patterns with one fitted scale | the honest "n of 19" in the relational sense (the number of relations the frame forces: a Jacobian co-rank) has never been computed | FC5, FC12, T-28, F-42, F-43 |
| FL-16 | θ̄ is a nineteenth unknown, not a constraint | UNSTATED as a framing | the locus arg det(Y_u Y_d) = 0 as a selector (it could fix Re τ and predict ∣J∣), or a strong-CP kill of the J ≠ 0 addresses | P-323: arg det = 0.177π at the best six-row | FC8 |
| FL-17 | Specificity against random hierarchies, with the frame's own CKM marginal as the null for the four, at the joint look count | CHOSEN (THE_BAR; B1825's card) | — (a sound null; it sets what can ever pass) | X2 was unreachable before the seal (p₂ 3/2000 against 1.89 × 10⁻⁴); the four's ceiling is set by the frame's own marginal | T-13–T-15, T-26, F-39, F-40, W-05 |
| FL-18 | Reach cutoffs: lines of order ≤ 12, Im τ ∈ [1, 4], nine values of c | CHOSEN (labelled cutoffs) | everything beyond them | B1825 is NOT FOUND, not EXCLUDED, beyond them; A5: the Z₅ × Z₃ lines (15, 30) lie outside | C-11, T-21, F-46, H-14 |

## D. Computed tonight (data-free, exploration tier; two coarse facts of the measured world disclosed: the hierarchy, and up steeper than down)

Scripts and outputs: frontier/B1827_the_framing_ledger/verification/scans/.
- **The mirror rule cannot lift the corner inversion** (P-555): it keeps the six and the Higgs's distance from the null cone,
  r = ∣h·h∣/∣h∣², exactly (every direction); where up is steeper than down, nature's corner order with ∣V_ud∣ > 0.9 holds at
  1.7% of the frame's points and at 0 of 303 under the rule.
- **A singlet Higgs component at natural magnitude (∣a₀∣² = ∣h·h∣), the SAME sign in up and down: no effect** at any of ten
  phases (0.7–4.0%; median ∣V_ub∣/∣V_td∣ 20–29; the frame alone 2.1%, median 27).
- **The same singlet with OPPOSITE signs in up and down: 33–47% at every one of the ten phases; median ∣V_ub∣/∣V_td∣
  0.91–1.0.** The inversion is lifted generically and independently of the phase; the corner ratio becomes balanced (~0.9),
  not the measured 0.43 — half the inversion's distance. **Robust (singlet_robustness.py, fresh seeds 1200–1439, four phases):** at ∣a₀∣² = 0.25, 1 and 4 × ∣h·h∣ the rate is 29–38%, 34–48% and 33–42% (the frame alone 2.2%, median 21), the median ∣V_ub∣/∣V_td∣ 1.03–1.11, 0.91–1.02 and 0.83–0.93: the effect holds over a factor 16 in the singlet's size, and a larger singlet moves the corner ratio further towards nature's side.
- **Correction disclosed:** main first expected opposite signs from a Higgs twisted like the matter (θ₁ odd); B1744 had
  shown the frame's twisted residue quaternion is EVEN (T0(3w) = T0(−3w); H_u = H_d), so oddness must come from elsewhere.

## E. Ranked: what to test, data-free first

1. **FL-06 — what in the object makes the Higgs's singlet component odd between up and down?** Candidates: the Higgs's
   hypercharge sign (q_L + q_R is −3 for up, +3 for down); the amphichiral involution (τ, a₀) → (−τ̄, −ā₀); a single
   twisted section (θ₁(ū), θ₂(ū), θ₃(ū), θ₄(ū)) at ū = ∓3w, whose θ₁ alone is odd. One definition written first, then the
   corner order, ∣V_ud∣ and the six at the frame's points, data-free; a card only within P-555's 3.63 bits.
2. **FL-08 — the lines as centre Wilson lines:** verify the order-5 SU(5) relations (Y_u symmetric, Y_e = Y_dᵀ), compute
   the lepton/down factor on the (2/5 + j/3, k/30) lines with c = 1 (A5 expects no centre line gives 3: the Clebsch would then
   need a non-abelian Higgs component).
3. **FL-15 and FL-14 — the relations and the rigid outputs:** the Jacobian co-rank of the frame's outputs in its continuous
   data (how many relations it forces); the inter-sector ratios m_t : m_b : m_τ at the strip.
4. **FL-07 — two loci** within P-555's budget (a rule, never a free second address).
5. **FL-16 — the det-real locus** arg det(Y_u Y_d) = 0 through the strip.
6. **FL-13 — running:** design a card whose frame is read at its own scale (P-363), the allowance structured.
7. **FL-02 and FL-03 — the flat premise and SE2:** which of the 107 flat-premise value-kills, and which of the eight SE2
   walls, would change under curvature or the chiral choice (data-free re-reads first).
8. **FL-05 — no action:** about nine of the 19 have no frame; they need new structure (an action, a normalisation), not
   extraction from the present frames.

## F. Assessment

**Main, with the blind reader (A5 § 4).** The exercise does not find a hidden ToE in the present framing; it finds where the
framing itself blocks the programme. The flavour sector's sharpest wall (the CKM corners) is a construction choice (FL-06),
and tonight's scan shows it is liftable by one structural ingredient, a sector-odd singlet Higgs component — what in the
object supplies it is the next question. About nine of the 19 (the gauge couplings, the Higgs sector, the scale) are not
blocked by framing but absent: no action, normalisation or dynamics exists on record (FL-05). The blind reader's judgement:
what this object can plausibly give is flavour structure — SU(5)-type relations, a symmetric Y_u, the down–lepton
transposition up to a Clebsch, exponent patterns, the corner order, the det-real locus, the inter-sector ratios — perhaps
5–8 relations among the 13 flavour parameters, with two or three fitted numbers declared as such. The ledger's order (§ E)
tests that claim, data-free first. **0 of 19.**
