## W62. What holds τ at the selected state: the matter's six-dimensional term is not a multiple of E(τ, 3) but keeps its critical points, the Higgs's copies break the modular group, and every content on record runs to a cusp (`the_matter_and_the_shape.py`; `W62_RULE.md`; post hoc `the_matter_and_the_shape_posthoc.py`)

**Why.**
- The owner chose "W62, as recommended" (2026-10-13), after "Reading A1–W61 together".
- That reading asked whether the matter's six-dimensional term, through the puncture's diffraction, could hold τ at a
  generic point. Drafting the rule found a correction (points 3 and 4 of the reading, recorded under it): at the line
  W60 selected, the Higgs's copies are not parity-symmetric.

**The order.**
- **The rule first** (`W62_RULE.md`, 90272b45b). It disclosed the correction, the comb identity, a paraxial estimate,
  the cusp coefficients, the design enumeration and a timing.
- **The script** (f89cb3a98), committed before its one run. Before the run: a smoke test of the gauge construction
  alone, as the rule allows (plaquettes on five tiny tori), and a line wrap (4b54d7b20). No logic changed.
- **The run.** One run; its output committed unread (b5810d240).
- **The post hoc** (labelled; script committed before its run; no new spectrum): A1 traced, D's shape fitted with
  extrapolation, the content window read against the cusp.

**The method.**
- One triangular lattice for every shape (W60's six-point Laplacian, unit spacing, the half flux at a triangle's
  centroid). The tori are its index-8400 sublattices with shapes on the imaginary axis (11, y from 1.031 to 2.021), on
  the arc between i and ω (6) and the hexagonal reference. With one lattice and one index, every local term of the heat
  trace cancels between shapes.
- The same shapes at index 4n = 33600 are the same tori at half the spacing.
- The periodic part is subtracted exactly as the comb −½ Σ_{Λ̂[2]} + ¼ Σ_{Λ̂[4]} of abelian twisted tori, in closed
  form. What is left, D, is the diffraction at the puncture.

**The read-out (COMPUTED; M0 to M6, A2 and A3 as predicted; A1 failed as worded).**
- **M0, the construction (as predicted).**
  - On every torus exactly one triangle has holonomy −1, with deviation 0.
  - Kramers pairs to 6 × 10⁻¹⁴.
  - W60's N = 96 torus, built by the new code, gives W60's lowest ten eigenvalues to 3 × 10⁻¹³.
  - The rank-1 operator matches the closed-form spectrum to 4 × 10⁻¹³.
  - λ_K t₀ ≥ 48 everywhere.
  - The other hexagonal sublattice agrees with the reference to 10⁻¹¹, so no orientation artefact.
- **M1, the control (as predicted).** The comb on the lattice matches (31/1024)[E(τ, 3) − E(ω, 3)] to 1.5 × 10⁻⁴ at n
  and 3.6 × 10⁻⁵ at 4n, against differences up to 0.401 (W59's units).
- **M2, the diffraction is there (as predicted).** max |ΔD| = 0.147 at 4n, 400 times the control's error.
- **M3, its sign and size (as predicted).** ΔD has the sign opposite to the periodic part's variation at every member.
  The ratio ΔD/ΔV_per is −0.477 on the arc and near i, falling to −0.37 at y = 2.02. The diffraction cancels about half
  the periodic part's τ-dependence near ω and i.
- **M4, not a multiple of E(τ, 3) (as predicted).** The best multiple is 0.0188 E(τ, 3), against the periodic part's
  31/1024 = 0.0303. Its largest residual, 0.0057 at y = 2.02, is 4.5 times that member's uncertainty.
- **M5, the critical points stay at i and ω (as predicted).** V_ρ rises along the axis from 0.0085 (y = 1.031) to 0.254
  (y = 2.021), and along the arc from ω toward i from 0.0011 to 0.0082. It is lowest at ω, with a saddle at i.
- **M6, convergence (as predicted).** n and 4n agree to 1% (−0.1455 against −0.1466 at y = 2.02). Extrapolations move
  ΔD by less than 1%.
- **A1, the Higgs's copies (failed as worded).**
  - The identity Σ_copies S = (1/16) E(τ, 3) − S_{(½,½)} holds at all five points to 2.5 × 10⁻¹².
  - S_{(½,½)} is unchanged by τ → −1/τ and τ → τ + 2 to 10⁻¹⁵.
  - Under τ → τ + 1 it changes by 3.06, 1.21, 0.24 and 1.09 at four points, but by 0 at ω. There ω + 1 = −ω̄ is ω's
    mirror image, and S_{(½,½)} is mirror-symmetric. The sample point was badly chosen; the post hoc (PH1) confirms the
    mirror identity there.
- **A2, the selected state is not stationary (as predicted).** At ω the Higgs's copies' boson term is −1.553 with
  gradient (−7.52, −4.34). It falls monotonically along the arc to −3.785 at i.
- **A3, the cusps (as predicted).** S_c/y³ at 8i equals κ_c to 4 × 10⁻⁵ of 2ζ(6) for every sector, and to 10⁻⁶ for the
  comb.

**The read-outs (no prior).**
- **The contents.** Every one is unstable at the cusp, for every line choice. Σ W κ in units of ζ(6), for the lines
  (½, ½), (½, 0) and (0, ½):
  - (a) W60's, the matter and the Higgs's copies: 9.57, 9.57, 1.70;
  - (b) with the gauge bosons: 57.6, 57.6, 49.7;
  - (c) with the graviton: 66.6, 66.6, 58.7;
  - (d) the matter alone: 5.45 for each.
  - Among the members the lowest total is at y = 2.02, toward the cusp, for (a) to (d). For (a) on the line (0, ½)
    the lowest member is ω, but its cusp coefficient is still positive: it rises first and then runs to the cusp.
- **The shape of D.**
  - E(τ, 2) alone fits ΔD to 0.56% rms; E(τ, 3) and E(τ, 2) together to 0.05%.
  - The paraxial estimate's E(τ, 2) shape correlates at 0.99998; its amplitude is 1.38 times too small.
- **The content window.** For a content of the trivial sector and ρ_Q alone, the ratio r = ΔV_ρ/ΔE₃ per axis interval
  rises from 0.0171 to 0.0208 between y = 1.03 and 2.02. It is about 0.0158 on the arc.

**Post hoc (labelled; from the stored values; no new spectrum).**
- **PH1.** A1 holds at every point where τ → τ + 1 is not the mirror: |S(ω + 1) − S(−ω̄)| = 0.
- **PH2, an observation, not a claim.** The E(τ, 2) coefficient of ΔD over 31/1024 is −0.980 at n, −0.988 at 4n,
  −0.995 extrapolated as O(h) and −0.990 as O(h²). So, within 1%, D = −(31/1024) E(τ, 2) + const and
  V_ρ = (31/1024)[E(τ, 3) − E(τ, 2)] + const. Whether that is exact is not established.
- **PH3, the window against the cusp.**
  - With the matter's weight W_ρ < 0 (fermions), a content of the trivial sector and ρ_Q is stable at the cusp only if
    W_triv/W_ρ > 31/1024.
  - Every measured r is below 31/1024, which is r's cusp limit. So a cusp-stable content of this kind rises from i up
    the axis and from ω to i on the arc: its minimum is at ω.
  - A content inside the window has a stationary point on the axis, but it is a maximum, and the content runs to the
    cusp. This assumes r keeps rising beyond y = 2.02, which was not computed.

**What it shows (a READING; given Λ, GENESIS FK11; at the line W60 selected).**
- **The reading's question is answered.** The matter's six-dimensional τ-dependence is not a multiple of E(τ, 3): the
  diffraction cancels about half of the periodic part's variation, with an E(τ, 2) shape. But both functions have their
  critical points at i and ω only, and the sum keeps E's shape. So the matter cannot hold τ at a generic point.
- **Mixing the matter with the trivial sector gives no generic minimum either** (PH3): cusp-stable contents sit at ω,
  and contents with a stationary point on the axis have a maximum there and run to the cusp.
- **At the selected line the Higgs's copies break the modular group to the theta group.** The state W60 selected is not
  stationary in τ: the Higgs's term pushes τ from ω toward i (A2).
- **Every content on record runs to a cusp.** Its six-dimensional term is unbounded below as one cycle of the fibre
  shrinks.
  - The trivial sector's bosons and the matter's fermions both push τ to the cusp: in ρ_Q the shrinking cycle carries
    the unit i, so the double windings act like antiperiodic ones.
  - Holding τ needs net fermions in the trivial sector (W_triv/W_ρ > 31/1024) or bosons twisted along the shrinking
    cycle. That is a dictionary datum (GENESIS FK11), and even then the computed sectors put τ at ω, not at a generic
    point.
- **So the owner's first question, what fixes τ, has this answer: nothing computed holds τ for the contents on
  record, and no content of the computed sectors holds it at a generic point.**
- **For flavour.** At a half-period line W61's algebra does not depend on τ, so the overlaps are zero (T ⊗ T, the
  record's dictionary, as main confirmed in S118) or degenerate at every τ. The hierarchy needs a datum acting on M,
  which is main's B1644 question.
- **A caution from the audit lane** (P-108, relayed in S118): in the E₈ embedding the weak doublets have odd quaternion
  centre, so W60's parity Higgs needs a parent map. A1 to A3 hold sector by sector either way. The content read-outs
  (a) to (c) assume W60's parity Higgs.
