# W65 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before the code that reads it exists. What the seat worked by hand while
drafting is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **W64 ended on one missing datum.** The weave's anisotropy puts the Higgs on the cusp's isotropic lines, where the
  Yukawa has rank one. The second generation's mass needs a departure from the cone of size |a·a|/|a|² ≈ m₂/m₃ (0.004,
  0.02 and 0.06 in the up, down and lepton sectors; W63's read-out). Nothing computed supplied it.
- **The owner's order is "we look what fixes τ then we count free numbers".** This arc asks what supplies the
  departure, where in τ it vanishes, and what it costs in free numbers.
- **The candidate is W64's own sections.** Read the Higgs's direction in M as a section of the matter's bundle at weight
  −½ (W64's K4), evaluated at the vacuum's τ. Then the departure is a function on the modular curve, fixed by end data,
  not a new input.

## Weave or thread?

- **Weave-type.** It takes every placement of end data u ∈ {0, 1}³ at weight −½ (none chosen), the whole group O acting
  on M, all three special points of the modular curve (i∞, i, ω), and τ across the fundamental domain.
- **The tags.** Given Λ (GENESIS FK11). Two hypotheses, stated:
  - B1644's coupling at the puncture (P-108's parent map owed; Review 63's P-122 scopes the identification it rests on);
  - **H-sec (new):** the Higgs's direction in M is a section of weight −½ in ρ_R evaluated at the vacuum's τ.
  GENESIS FK10's unit is a tagged working postulate.

## Seen before the rule (disclosed; by hand, no numerics)

- **Three one-unit sections generate everything.** W64's post hoc found dim = Σu for every u ∈ {0, 1}³ at weight −½.
  The one-unit placements give one section each:
  - E for (1, 0, 0), leading along e_i;
  - R for (0, 1, 0), main's residue triplet, leading along v₊;
  - R′ for (0, 0, 1), leading along v₋.
  They lead on different eigenlines, so every placement's space is spanned by the sections of its units.
- **The negative-weight lemma.** For sections f and g, f·g is a scalar form of weight −1 with the multiplier of η⁻¹⁸
  (T: √−1; S: √−1 τ⁻¹, from ρ_R's scalar e^{iπ/4} and O ⊂ SO(3)). So η¹⁸ f·g is a weakly holomorphic form of weight 8
  for SL(2, ℤ), and its pole order at the cusp is read from the eigenline exponents (⅛ − u_i on e_i, ⅞ − u₊ on v₊,
  ⅜ − u₋ on v₋; v₊·v₋ = 2, v±·v± = 0):
  - R·R and R′·R′ have order ¼ > 0, so they vanish identically: R and R′ are isotropic at every τ, not only at the cusp;
  - R·R′, E·R and E·R′ have order −¾, so each is a constant times Φ = E₄²/η¹⁸;
  - E·E has order −7/4, so E·E = (a j + b) Φ, affine in Klein's j.
  - With each section normalized by its leading coefficient (1 on its unit's eigenline), the leading terms give
    R·R′ = 2Φ and E·R = 4Φ. R is then −2π times main's R, whose e_i part leads as −(2/π) q^{1/8}.
- **The special points.**
  - **ω.** ST fixes ω, and ρ_R(ST) acts on M as a three-fold rotation with three distinct eigenvalues. So every section
    of weight −½, in every placement, takes its value at ω on one eigenline. R(ω) ≠ 0 is isotropic, so that line is an
    isotropic line of a three-fold rotation: an 8-orbit line. Φ has a double zero at ω, as E₄ does.
  - **i.** S fixes i, so every section's value at i lies in the +1 eigenspace of the swap P, the plane spanned by
    e_i + e_j and e_k. Its two isotropic lines are the 12-orbit lines of the half-turn about e_i − e_j, exchanged by
    conjugation. R·R′(i) = 2Φ(i) ≠ 0, so R(i) and R′(i) lie on different isotropic lines: one each.
  - **i∞.** E → e_i, R → v₊, R′ → v₋ (W64).
- **The masses.** With coupling R, Y(a) = aRᵀ + Raᵀ − (a·R)𝟙 has Y R = 0 (B1644).
  - If a is parallel to R, Y = 2μRRᵀ has rank one. At ω every Higgs section is parallel to R. So **m(ω) = 0 for every
    Higgs section**: the second generation is massless at ω.
  - If a is isotropic, Y has rank one (B1645). So a = R and a = R′ give m ≡ 0, and E gives m = 0 wherever
    j(τ) = j₀ = −b/a.
  - At the cusp, a = E → e_i and R → v₊ give Y = e_i v₊ᵀ + v₊ e_iᵀ, with two equal singular values: m_E → 1.
  - For a = αR + βR′ (αβ ≠ 0), Y = 2α RRᵀ + β nnᵀ/(R·R′) with n = R × R′. Near the cusp the two pieces grow as
    e^{πy/2} and e^{3πy/2}, so m ∝ e^{−πy}: the level-2 small parameter, as the reading's correction says.
- **The mixing.** Y(a)R = 0 for every Higgs a. So with R the coupling in two sectors, both massless states are R̄/|R|,
  and the first generation does not mix.
- **The literature, after the repo** (the W64 reading's point 6, read then): hierarchies near the fixed points set by
  residual symmetry (Novichkov, Penedo and Petcov, JHEP 04 (2021) 206); a rank-one matrix at τ = i (Feruglio,
  Gherardi, Romanino and Titov, JHEP 05 (2021) 242). The rank one at ω here is the same mechanism, read on ρ_R.

## The method (fixed here)

- **R** from the theta series summed directly (W64's post hoc; no branch of the nome), at 40 digits.
- **E, R′ and a check copy of R** by W64's collocation on the arc |τ| = 1, done at 40 digits in mpmath: 120 points,
  30 coefficients per eigenline, each section normalized by its leading coefficient, solved by least squares (QR). The
  basis is exactly e_i, v₊ = e_j − √−1 e_k and v₋ = e_j + √−1 e_k, with exponents ⅛, ⅞ and ⅜.
- **E₄, η and j** from their q-series at 40 digits.
- **The sample.** Twenty τ in the fundamental domain: i, ω, 2i, 4i, and sixteen fixed points listed in the script.
- **m** = s₂/s₁ of Y(a) with coupling R (main's normalization), by mpmath's complex SVD.
- **The orbits** of special isotropic lines from W64's K1.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **H1, the instrument and the generators** | The 40-digit collocation solves for E, R′ and R with residual below 10⁻²⁰, and its R equals −2π times the direct series to 10⁻²⁰ at the sample. | 90% |
| **H2, the pairings** | Over the sample, to 10⁻¹⁵ relative: R·R = R′·R′ = 0; R·R′ = 2Φ; E·R = 4Φ; E·R′/Φ constant; E·E/Φ affine in j (fit at two points, checked at the rest). | 80% |
| **H3, the special points** | At ω, E, R and R′ are nonzero and parallel (to 10⁻¹⁵), on one 8-orbit line. At i all three lie in the plane spanned by e_i + e_j and e_k; R(i) and R′(i) lie on its two isotropic lines, one each; E(i) is not isotropic. At y = 8 the directions of E, R and R′ are e_i, v₊ and v₋ (the sine of the Hermitian angle below 10⁻⁴). | 85% |
| **H4, the second generation at ω** | With coupling R: m(ω) < 10⁻¹² for E, for R′ and for the fixed combinations of every placement (coefficients listed in the script). m > 10⁻⁹ for E and for αR + βR′ at every sample point at least 0.05 from ω and from E's cone point τ₀. | 85% |
| **H5, the cusp** | Along τ = iy, for αR + βR′ with each of the script's four (α, β): the slope of log m between y = 5 and y = 6 is −π within 1%. m_E(iy) → 1: 1 − m_E(8i) < 10⁻³. | 70% |
| **H6, the first generation does not mix** | With coupling R in two sectors and every pair of the script's rank-two Higgs sections (E and its αR + βR′), the mixing matrix of the left states, ordered by mass, has its massless row and column equal to (1, 0, 0) up to phases, to 10⁻¹², at every sample point at least 0.05 from ω and τ₀. | 95% |

**The read-outs (no prior).**
- **The constants** E·R′/Φ, a and b; j₀ = −b/a; whether j₀ is real; τ₀ in the fundamental domain with j(τ₀) = j₀.
- **m_E** along τ = iy (y from 1 to 8) and along the arc from i to ω. Where m_E equals 0.004, 0.02 and 0.06 on each
  path (context, not a fit).
- **The exponent near ω:** the slope of log m against log |τ − ω| for E and for R + R′, between |τ − ω| = 10⁻³ and
  10⁻².
- **The cusp constant:** lim m e^{πy} / |α/β| for αR + βR′.
- **The first-generation overlap** |⟨R, R′⟩|/(|R||R′|) (Hermitian) along τ = iy and the arc. It is the mixing if one
  sector's coupling were R and the other's R′.

## The reading, written before the run (predicted)

- **The modular curve's three special points carry O's three orbits of special lines.**
  - At the cusp, R and R′ lie on the conjugate pair of the four-fold axis's isotropic lines (the 6-orbit).
  - At i, they lie on the conjugate pair of a two-fold axis's lines (the 12-orbit).
  - At ω, every section lies on one three-fold line (the 8-orbit).
  W64's two signs of the anisotropy (the 6-orbit and the 8-orbit) are the cusp's and ω's.
- **At ω the second generation is massless for every Higgs section.** The record's τ = ω (W60, W62) gives masses
  0 : 0 : m₃. The departure from the cone is the distance from ω (and from E's cone point τ₀), not a new datum.
- **So the second generation's mass is a function of τ, and the count does not drop.**
  - The parameter-free Higgs E gives one m₂/m₃ = m_E(τ) for all three sectors at the vacuum's one τ. The data's 0.004,
    0.02 and 0.06 cannot all hold.
  - The two-unit Higgs αR + βR′ adds one complex number per sector.
- **One coupling for every sector gives no first-generation mixing** (H6). A Cabibbo angle needs the sectors' couplings
  to differ, for example R against R′.
- **The count stays all 19 of the 19 free** (18 if I-18 is earned). 0 of 19.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
