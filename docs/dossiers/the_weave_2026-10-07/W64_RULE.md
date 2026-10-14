# W64 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before the code that reads it exists. What the seat worked by hand while
drafting is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **The owner said "lets follow that lead properly"** (2026-10-14), about GENESIS FK10's tagged unit at the cusp read as
  a vector in M (main's P-113). The seat wrote a reading first (the dossier's "Reading: the cusp's unit as a vector in
  M") and checked the literature.
- **The owner then chose "Both frames"** for this arc:
  - the surface frame, where the weave's surface is the internal space (W45–W48; GENESIS FK11) and the unit is end data
    at the cusp;
  - the fibre frame, where τ is one number per vacuum (W59–W63) and the cusp can act only through the Higgs's
    potential.
- **This arc computes the geometry common to both frames,** then each frame's question.

## Weave or thread?

- **Weave-type.** It uses the weave's whole group acting on M, every eigenline of the cusp's monodromy, every placement
  of units in a stated range, and every orbit of special points, none chosen.
- **The tags.** Given Λ (GENESIS FK11). The surface frame and B1644's Higgs in M at the puncture are hypotheses (P-108's
  parent map owed). GENESIS FK10's unit is a tagged working postulate.

## Seen before the rule (disclosed)

- **The reading's facts, by hand.**
  - The record's L (a ↦ a, b ↦ ab) acts on the units by i ↦ i, j ↦ k, k ↦ −j: a quarter-turn about e_i. R
    (a ↦ ab, b ↦ b) is a quarter-turn about e_j. Together they give the cube's rotation group O.
  - L's eigenlines in M ⊗ ℂ are e_i, v₊ = e_j − √−1 e_k (eigenvalue √−1) and v₋ = e_j + √−1 e_k (eigenvalue −√−1).
    v₊ and v₋ are isotropic, and complex conjugation exchanges them.
- **R's transformation, by hand from the theta functions' laws.**
  - R(τ + 1) = e^{iπ/4} A_T R(τ) with A_T = L⁻¹.
  - R(−1/τ) = (−iτ)^{−½} P R(τ), where P swaps the i and j components. −P is the half-turn about e_i − e_j, in O.
  - So R is a vector-valued modular form of weight −½ for a representation ρ_R whose T-exponents are 1/8 on e_i, 7/8 on
    v₊ and 3/8 on v₋. These are the matter triplet's own exponents (⅛, ⅜, ⅞; W41, W46), and ρ_R(S)² = e^{−iπk} holds
    at k = −½ as at 3/2.
- **An exact link, by hand: R carries one unit at the cusp, on the isotropic eigenline v₊.**
  - Along v₊, R's leading term is −(θ₃² + θ₄²)/(2πη³) ~ q^{−1/8}, with q = e^{2πiτ}. That is the canonical exponent
    7/8 minus one.
  - Along e_i and v₋, R's leading exponents are the canonical 1/8 and 3/8.
  - So R = Δ⁻¹ η²¹ (−θ₂², −θ₄², √−1 θ₃²)/(2π), with Δ⁻¹ as W47's unit, is a section with end data (0, 1, 0) on
    (e_i, v₊, v₋): one unit on the isotropic eigenline that R tends to at the cusp, and none elsewhere.
  - So the coupling main found at the puncture (B1644) already uses one unit of end data at the cusp, placed on an
    isotropic line.
- **The fibre frame, by hand.**
  - |a* × a|² = |a|⁴ − |a·a|² gives B1646's dichotomy: an SO(3)- and phase-invariant quartic λ₂|a·a|² puts the minimum
    on the cone for λ₂ > 0 and on the real locus for λ₂ < 0.
  - The lowest phase-invariant quartic that O keeps and SO(3) does not is A(a) = Σ_u |a_u|⁴. On the cone, A/|a|⁴ is
    1/2 on the six lines e_j ± √−1 e_k (the quarter-turns' fixed lines), 1/3 on the eight lines like (1, ω, ω²)/√3 (the
    three-fold rotations' fixed lines), and 3/8 on the twelve two-fold lines. So a term cA with c < 0 picks the cusp's
    lines and c > 0 the eight. All of them are on the cone, where B1645 gives m = 0.
- **The literature after the repo** (recorded in the reading): hierarchies near the cusp at level N go as powers of
  e^{−2π Im τ/N}; the polar against ferromagnetic split of a complex triplet; an SO(3) flavour model with isotropic
  vacua (Barbieri, Hall, Kane and Ross); the octahedral orbits of 6, 8 and 12 on the cone.

## The method (fixed here)

- **Exact arithmetic for the group.** The moves' action on M comes from the record's AUT and quaternion multiplication,
  as signed permutation matrices. O is the closure of L and R. Eigenlines are found exactly. The special isotropic lines
  are the fixed lines on the cone of every non-trivial element of O.
- **R at 30 digits** from mpmath's jtheta, with W63's closed form R = (−θ₂², −θ₄², √−1 θ₃²)/(πθ₂θ₃θ₄).
- **ρ_R** is read from R's own transformation at ten τ (W63's set): the signed permutation and scalar that fit
  R(τ + 1) and R(−1/τ).
- **End data per eigenline.** A placement u = (u_i, u₊, u₋) ∈ {0, 1}³ allows each eigen-component to start at its
  canonical exponent minus u. The dimension of holomorphic sections at weight k is counted two ways:
  - by W45's collocation method (`dims`, with each column's series starting at n = −u);
  - by W45's χ formula plus Σu, for comparison (χ counts dim M_k − dim S_{2−k}(ρ*)).
- **The fibre frame's potentials** are minimized numerically from 200 seeded random starts each (BFGS on ℂ³ ≅ ℝ⁶, at
  fixed |a| = 1 and with a phase-invariant quartic).

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **K1, the moves on M** | L and R act as quarter-turns about e_i and e_j, and generate O (24 rotations, every signed permutation of determinant +1). L's eigenlines are e_i, v₊ and v₋. Exactly two of them are isotropic, and conjugation exchanges them. The fixed isotropic lines of O's non-trivial elements form three orbits of sizes 6, 8 and 12. The 6 are the lines kept by the quarter-turns. | 97% |
| **K2, R's law** | At the ten τ, R(τ + 1) = e^{iπ/4} A_T R(τ) with A_T = L⁻¹, and R(−1/τ) = (−iτ)^{−½} P R(τ) with P the i–j swap, to 10⁻²⁵ relative. −P is in O. | 85% |
| **K3, R's end data** | Along τ = iy, y = 4 to 10, the leading exponents of R's components on (e_i, v₊, v₋) are 1/8, −1/8 and 3/8 to 10⁻⁶. So R has one unit on v₊ and none on e_i or v₋. R/\|R\| → v₊/√2 up to a phase, with the e_i part falling as e^{−πy/2} and the v₋ part as e^{−πy}. | 85% |
| **K4, the Higgs's sections (surface frame)** | At weight −½, by collocation: no section with canonical end data (u = 0). Exactly one with u = (0, 1, 0), and it is R (its q-expansion matches R's to 10⁻⁸ after scaling). | 70% |
| **K5, the fermions' sections (surface frame)** | At weight 3/2 in ρ_R (the matter's representation), dim M_{3/2}(u) = Σu for every u ∈ {0, 1}³, by collocation and by χ + Σu. So the chiral three needs Σu = 3, the uniform unit, while R needs only (0, 1, 0). | 70% |
| **K6, the potential's dichotomy (fibre frame)** | The identity \|a* × a\|² = \|a\|⁴ − \|a·a\|² holds exactly. Minimizing λ₂\|a·a\|² at \|a\| = 1 from 200 starts gives \|a·a\| < 10⁻⁸ for λ₂ = +1, and a real vector up to a phase (to 10⁻⁸) for λ₂ = −1. | 95% |
| **K7, the weave's anisotropy on the cone (fibre frame)** | The phase-invariant quartics that O keeps form a space of dimension 3: \|a\|⁴, \|a·a\|² and A = Σ\|a_u\|⁴. On the cone A/\|a\|⁴ ∈ [1/3, 1/2], with the minimum exactly on the 8-orbit and the maximum on the 6-orbit, and 3/8 on the 12-orbit. Minimizing \|a·a\|² + cA at \|a\| = 1 lands on the 6-orbit for c = −0.1 and the 8-orbit for c = +0.1. | 85% |

**The read-outs (no prior).**
- **m at the special points.** B1645's m and the heavy state at each orbit's lines, at τ = i, 2i and ω. On the cone
  m = 0 everywhere, so what is read is the heavy state's direction and mass.
- **Every placement u ∈ {0, 1}³ at weight −½:** the dimension, and the generic section's direction at the cusp. That
  direction is the eigenline with the lowest shifted exponent; it is isotropic exactly when that eigenline is v₊ or v₋.
- **The image of S̃ = L R⁻¹ L on M** against −P.

## The reading, written before the run (predicted)

- **The cone that a hierarchy needs is the cusp's own geometry,** and B1644's coupling already uses it. The residue
  triplet R is the one section of the matter's bundle with a single unit of end data at the cusp, placed on the
  isotropic eigenline R tends to. GENESIS FK10's unit, read as a vector in M, is in main's coupling already.
- **But one datum does not give both.** The chiral three needs three units, the uniform placement. R needs one, on one
  isotropic eigenline. With the uniform placement the generic Higgs section's cusp direction is the real fixed unit
  e_i, not the cone. So P-113's "one postulate for the ±3 and the flavour structure" does not follow from the end data
  alone.
- **In the fibre frame the weave's own anisotropy picks points on the cone,** the cusp's six lines or the eight lines
  like (1, ω, ω²), by the sign of one coefficient. Either way the Yukawa has rank one: one heavy generation and two
  massless. The second generation's mass needs a departure from the cone that nothing computed supplies.
- **So the lead gives the leading-order pattern (one heavy generation) from the cusp's geometry, in both frames, and
  locates the second generation's mass in one missing datum:** a departure from the cone of the size |a·a|/|a|² ≈ m₂/m₃.
- **The count stays all 19 of the 19 free** (18 if I-18 is earned). 0 of 19.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
