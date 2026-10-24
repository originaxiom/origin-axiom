# W149 — the cone and the defect: M's isotropic conic as the level-4 curve, R's line map, the quarter-turn bound on every section's on-cone coordinate, and the quartic census in the record's frame (the rule, committed before the script)

The SM-derivation seat, 2026-10-24. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The breaking chain** (`THE_BREAKING_CHAIN_2026-10-24.md`, section 6a) read B1743's target as a point of M's
  isotropic cone, moved along the cone by δ and off it by a small constant defect. It named the identification of the
  cone with X(4), R's line map and the on-cone exponent of every section as W149's first content.
- **The owner approved the order** ("lets address all these", 2026-10-24: the rule-first computations, vacuum alignment
  first).
- **The selection principle (P-139) is the web seat's, by the owner's assignment of 2026-10-14.** This arc is data-free
  structure, relayed to the web seat in §252 so that neither duplicates the other.

## The objects

- **M = ℂ³ with the record's ρ.** ρ(S) = z·P and ρ(T) = z·L, with z = e^{iπ/4}, P the swap of e₁ and e₂, and L the
  quarter-turn about e₁ (W134's `rho_exact`; W146's `rho_T` is the same ρ(T)). Projectively they generate O, the
  cube's rotations, acting by signed permutations.
- **The isotropic conic** C = {[h] : h·h = 0} ⊂ ℂP², and on it the chart through h₀ = (0, 1, i)/√2:
  h = h₀ + s e₁ − (s²/2) h̄₀, with h₀·h̄₀ = e₁·e₁ = 1.
- **For a vector h near h₀:** δ = e₁'s coefficient over h₀'s, and ε = h̄₀'s over h₀'s (B1743's definitions). Its defect
  off the cone is I = |h·h|/|h|², with h·h = 2(ε + δ²/2) h₀-coefficient².
- **The forms,** all from W146's committed instrument (explicit theta series, CONVENTIONS §4; no principal nome root):
  - R and ∂R (`R_and_DR`);
  - the F_a for a in W146's list (`F_a`).
- **The quartic potential** of one triplet with the phase symmetry: V = −|a|² + |a|⁴ + λ|a·a|² + cA, with
  A = Σ_u |a_u|⁴ on the units.

## Weave or thread

**WEAVE-type for C1, C3 and C4.** Their objects are the joint family group's action, every section of ρ ⊗ χ, and every
coefficient pair. **C2 is about R,** one object of the joint frame (the family group's weight −½ section), not a
thread.

## The cells, with predictions, priors and pre-mortems

| cell | prediction | prior |
| --- | --- | --- |
| C1 | **The special lines (exact).** The 24 projective elements of ⟨ρ(S), ρ(T)⟩ preserve C. Its points with a non-trivial stabilizer are exactly 26 lines: 6 with stabilizer ℤ₄ (the isotropic eigenlines of the three 4-fold axes; h₀ among them), 8 with ℤ₃, 12 with ℤ₂ (sympy). On 2 000 random points of C the stabilizer is trivial | 98% |
| C2 | **R's line map is X(4)'s equivariant map, with local degree 1 at the cusp** (30 digits). R·R = 0 to 10⁻²⁵ at 20 random τ. [R(τ + 1)] = ρ(T)[R(τ)] and [R(−1/τ)] = ρ(S)[R(τ)] projectively to 10⁻²⁰. [R(i)] is a ℤ₂-line, [R(ω)] a ℤ₃-line, and [R(iy)] tends to a ℤ₄-line. Along τ = iy, y = 2, …, 6: \|s_R\|/\|q₄\| → 2√2 and R's far-null part over its leading one → \|s_R\|²/2, each to 2 × 10⁻⁵ at y = 2 and 10⁻⁶ at y = 3 | 95% |
| C3 | **The quarter-turn bound (exact, then checked).** In ρ(T)'s line coordinates the eigenvalues are e^{2πi/8}, e^{2πi·3/8} and e^{2πi·7/8} (sympy). So e₁'s exponent differs from each null line's by ±1/4 mod 1, for every scalar character χ. So every single holomorphic section of ρ ⊗ χ is either null-led, with \|δ\| ≤ C e^{−π Im τ/2}, or e₁-led, with \|δ\| ≥ c e^{π Im τ/2}: a dichotomy for the position along the cone, as W146's is for I. On W146's null-led and exactly null forms (R, F₂, ∂R and F_a for a = 6, …, 26), the slope of ln\|δ\| against Im τ over y ∈ [4, 8] lies within 10⁻³ of −π/2 − kπ, with k = 0 for R, F₂ and ∂R and k = (a − 2)/4 for F_a. And ∂R's \|δ\| over R's tends to 2, by the covariant derivative's exponent ratio (1/8 + 1/24)/(−1/8 + 1/24) = −2 | 95% |
| C4 | **The quartic census in the record's frame.** On 400 draws of (λ, c) uniform in [−0.45, 0.45]², the global minimum of V (BFGS, 20 starts each) lies, to 10⁻⁶ in (\|a·a\|², A), at one of four classes: the 6-orbit ((0, 1, i)-type, y = 0, A = ½), the 8-orbit ((1, ω, ω²)-type, y = 0, A = ⅓), (1, 0, 0)-type (y = 1, A = 1), or (1, 1, 1)-type (y = 1, A = ⅓). None is a 12-orbit line or a generic point. The class is the vertex of the orbit-space image that minimizes λy + cA: the 6-orbit exactly when c < 0 and λ > −c/2 (by hand: the four vertices give c/2, c/3, λ + c and λ + c/3; the top edge A = (1 + y)/2 is attained by (cos t, i sin t, 0)) | 90% |
| R | **Read-outs** (no prediction; against a fitted target, not a test and not a trial). B1743's target rows, read through W146's sha-checked loader: δ, ε, I, and the decomposition ε + δ²/2; the slope of ln\|δ\| against Im τ on the L₂ rows, beside C3's −π/2. The 26 lines' (y, A). R's ℤ₄-line at the cusp: h₀ or h̄₀ | — |

**Pre-mortems** (how each cell could fail for a reason that is not the finding):
- **C1.** A numerical stabilizer test on near-special random points could misclassify. The 26 are found exactly, and the
  random points are tested with a margin of 10⁻⁸.
- **C2.**
  - The theta functions must be W146's direct sums; mpmath's jtheta takes the principal nome root (W144's lesson).
  - S's weight factor makes the S-law projective only; it is compared projectively.
  - The limit y → ∞ is read at y ≤ 6. The tolerances were set after seeing the scratch values (2.8284074 and
    3.9999442 at y = 2), so they are informed, and disclosed as such.
- **C3.**
  - Which null line leads depends on the form. The bound counts both.
  - The F_a with a < 2 are e₁-led, and are excluded by the cell's own words.
  - The e₁ part of F_a is θ₂^a, about 10⁻⁷⁰ at a = 26 and y = 8. It is a product, not a difference, so 30 digits
    suffice. A slope failure at large a would point to the instrument first.
  - Slopes over [4, 8] carry q-corrections of relative size e^{−π·4/2}, which is below 2 × 10⁻³. That is near the
    10⁻³ tolerance, so a failure there is a tolerance failure, to be diagnosed as such.
- **C4.**
  - BFGS can stop at a local minimum. The global minimum is the least of 20 starts.
  - At |c| or |λ| near an edge's degeneracy the classification is ambiguous. Draws within 10⁻³ of a degenerate line
    are counted and set aside, not classified.
  - The top-edge claim A = (1 + y)/2 is by hand. If the true top edge bulges outward, minima on it would be a finding,
    not an instrument error.

## What the outcomes mean (fixed now)

- **C1 and C2 hold.** The breaking chain's identification stands as computed. M's isotropic cone, with O acting, is the
  octahedral sphere. R's line map sends i, ω and the cusp to the ℤ₂-, ℤ₃- and ℤ₄-lines, as X(4)'s points over them.
  The record's "special lines" are X(4)'s special points.
- **C3 holds.** Every single holomorphic section of ρ ⊗ χ, at any weight or character, has its on-cone coordinate
  fall at least as fast as e^{−π Im τ/2}, or grow at least as fast as e^{π Im τ/2}. W146 bounds the defect I, and C3
  bounds the position along the cone. The target's δ, near 0.3 across its band, then lies outside every such section
  in both coordinates. Anything that reaches it is not one holomorphic section of ρ ⊗ χ. It is a non-holomorphic
  section, a sum of sections with different multipliers, a field's vev, or a representation in which T is not O's
  quarter-turn.
- **C4 holds.** In the record's frame the literature's classification holds for one triplet with the phase symmetry,
  and the minimum at h₀ is rigid. A τ-independent quartic cannot move it.
- **Any cell fails:** the failure is the finding, and it is diagnosed before anything else is said.
- **This is data-free.** The read-outs use a fitted target; they are no test and no trial.

## What stays out

- **Out of C3:** non-holomorphic sections (W146's F̄ + κF), sums of sections with different multipliers (pencils with
  different η-powers), and the two doublets' bilinear.
- **Out of C4:** sextic terms, a second triplet, the joint (τ, h) potential, and any coefficient forced by the record.
- R's global degree. By hand it is 1: the weight-1 forms θ₂², θ₃², θ₄² have no common zero, and their bundle on X(4)
  has degree 2, the conic's. It is stated, not run. Any comparison with data beyond the read-outs.

## Seen before the rule (disclosed)

- **Read:** B1743's FINDINGS table (δ, ε and I on five rows); S204's description under P-357; the literature sweep's
  notes and the papers checked for the breaking chain.
- **Run in scratch** for the breaking chain, and locked in its test:
  - R·R at three random τ, 10⁻⁴¹ or below;
  - |s_R|/|q₄| and the far-null ratio: 2.8284074 and 3.9999442 at y = 2; 2.8284271 and 3.9999999 at y = 3.
  - **A correction found while writing this rule,** before the breaking chain was pushed. Its section 6a said both
    hold "to 10⁻⁵ at Im τ 2", but the far-null ratio is off by 1.4 × 10⁻⁵ there. The page was corrected before its
    push.
- **By hand:**
  - the eigenvalue argument for C3;
  - the exponent ratio −2 for ∂R;
  - the orbit-space vertices for C4, and the top edge (cos t, i sin t, 0);
  - B1743's best row: ε + δ²/2 = 0.003 − 0.009i, giving I = 0.0177.
- **Not run:** no script exists.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
