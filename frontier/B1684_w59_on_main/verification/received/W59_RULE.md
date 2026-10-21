# W59 — the rule, recorded before the code

The SM-derivation seat, 2026-10-13. Committed before the code that reads it exists. What the seat worked by hand while
drafting is listed under "Seen before the rule", and the priors it touched are set after that. Nothing here is a
result.

## Why this arc

- **The owner ruled "D1 first" (2026-10-13)**, after C0 (the dossier's "Reading: couplings as overlaps on the shared
  fibre").
- **The dossier's "Reading: the one-loop potential on the shared fibre"** set out D1's design. Its points 2 to 4 are
  exact or derived by hand. This arc computes what can be computed of them now:
  - the closed forms, checked by a second route;
  - the stationary points in τ for every sector with a closed form;
  - the stationary points in the Wilson line for the sectors where it is abelian;
  - which fields see which symmetric line.
- **What it cannot compute.** The matter's sector ρ_Q with a Wilson line on top: its determinant needs the genus-3
  cover's theta function (Fay's formula). Its six-dimensional sum has no closed form here. Both are named as open, and
  are not guessed.

## Weave or thread?

- **Weave-type.** The sectors are the weave's local systems on the shared fibre, all three parities at once (THE
  WEAVE's rule: none hand-picked).
- **The content is a dictionary datum** (GENESIS FK11): which fields, how many, bosons or fermions. So every cell
  holds for each sign separately, or for every content that treats the parities alike.
- **The tags.** On the ruled branch; given Λ.

## Seen before the rule (disclosed)

- **The Chowla–Selberg route to the twisted determinant,** worked by hand to the closed form
  det Δ_w = |θ₁(w | τ)/η(τ)|² · exp(−2π (Im w)²/y). K1 checks it numerically.
- **The joint parity identity at s = 3:** the coefficients Σ_p (−1)^{2(m p₁ + n p₂)} are 3 for (m, n) both even and
  −1 otherwise, so the joint sum is −(15/16) E(τ, 3) (K3c).
- **The leading-shell picture of K4.**
  - At ω the six shortest vectors are all odd, so a joint-parity boson's potential is +2[cos 2πφ₁ + cos 2πφ₂ +
    cos 2π(φ₁ + φ₂)] at leading order: largest at 0 and smallest at (⅓, ⅓) and (⅔, ⅔).
  - At τ₀ = 0.17 + 1.13i the smallest value is at (½, ½).
- **K5's arithmetic,** by hand.
- **The holomorphic-differential count of K2(a),** by hand.

## The definitions

- **The torus and the twists.** E_τ = ℂ/(ℤ + τℤ), y = Im τ, at fixed area. A flat U(1) twist is a pair of holonomy
  phases φ = (φ₁, φ₂) ∈ (ℝ/ℤ)², along 1 and along τ.
  - **The parities** are p ∈ {(½, 0), (0, ½), (½, ½)} (W21's labels), as phases.
  - **A field of charge q** in parity sector p under a line w sees φ = p + q w.
- **The two-dimensional term** is log det Δ_φ = −ζ′(0). It is computed two ways:
  - (i) the Chowla–Selberg series for the shifted Epstein sum, with the shift w = a + bτ in the dual picture: Z′(0) =
    2πy B₂(b) − Σ_n log|1 − exp(2πi(a + (n + b)x) − 2π|n + b|y)|²;
  - (ii) |θ₁(a + bτ | τ)/η(τ)|² e^{−2πyb²}, with W51's series for θ₁ and η.
- **The six-dimensional term** (the Casimir sum, up to a positive constant) for a boson with phases φ:
  V(φ; τ) = −Σ′_{(m,n)} cos 2π(m φ₁ + n φ₂) · y³/|m + nτ|⁶. A fermion has the opposite sign.
  - E(τ, 3) = Σ′ y³/|m + nτ|⁶, by the Chowla–Selberg expansion and checked against a direct lattice sum.
- **Stationary points in τ** are found by W51's census, in the fundamental domain up to y = 6, with corners and
  boundary pieces.
- **Stationary points in φ** are found on the torus [0, 1)².
  - Method: a 72 × 72 grid of starts; minimize |∇V|² to below 10⁻¹⁰ with the analytic gradient; deduplicate modulo 1.
  - Each point is typed by its analytic Hessian.
  - The lattice sum is truncated at |m|, |n| ≤ 48 (tail below 10⁻⁶ of the leading term).

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **K1** | At eight sample (τ, w), route (i) equals route (ii) to 10⁻¹⁰. At five sample τ, the three parity sectors' determinants multiply to 4 by both routes. | 90% |
| **K2** | The derivation's checkable steps hold. (a) The quaternion cover is a degree-8 cover of E branched over one point with four ramification points of index 2, so genus 3 by Riemann–Hurwitz. Its model w⁴ = 4x³ − g₂x − g₃ has exactly three holomorphic differentials of the form xᵃ dx/wᵇ: dx/w², dx/w³ and x dx/w³. (b) ζ_Σ(0) = −3/2 from the cone coefficients, (1/12)(1/k − k) with k = 2 at four points, minus 1 for the zero mode. It equals −1 − p with p = (1/12)·Σ d(d + 2)/(d + 1) = ½, exactly. (c) y^{1/2}\|η\|² and (y\|η\|⁴)^{−1/4} are invariant under S and T at four sample points, to 10⁻¹². | 95% |
| **K3** | (a) log(y\|η\|⁴) is stationary in the fundamental domain only at i (a saddle) and ω (its maximum). (b) E(τ, 3) is stationary only at i (a saddle) and ω (its minimum), and grows toward the cusp. (c) The joint parity sum Σ_p Σ′ cos 2π(m p₁ + n p₂) y³/\|m + nτ\|⁶ equals −(15/16) E(τ, 3) at five sample τ, to 10⁻⁹ relative. | 90% |
| **K4** | For a joint-parity boson of charge 1, V(φ) = Σ_p V(p + φ). (a) At τ₀ = 0.17 + 1.13i and τ₁ = 0.05 + 1.40i its stationary points on the torus are exactly the four 2-torsion points, with its minimum at one of the three nonzero ones. (b) At τ = ω they are the four 2-torsion points and the two nonzero fixed points of the order-3 rotation, (⅓, ⅓) and (⅔, ⅔): the minimum at both 3-torsion points (equal values), the maximum at 0, and saddles at the three nonzero 2-torsion points. (c) For a fermion (the opposite sign) the minimum is at 0 in all three cases. | 70% |
| **K5** | In units of 6Y (Q 1, u^c −4, d^c 2, L −3, e^c 6, H 3): at a nonzero 3-torsion line the fields with q·w ∉ ℤ² are exactly Q, u^c and d^c. At each nonzero 2-torsion line they are exactly Q, L and H. So no 2-torsion line tells d^c from e^c or Q from L. The colourless fields' sums at a 3-torsion line equal their sums at 0. | 99% |

**The read-outs (no prior).**
- **The Higgs alone at ω.** A joint-parity boson of charge 3, as C0 requires of the Higgs (it carries a parity): the
  lines w where its potential is smallest. At those lines, the twist each Standard Model field sees, and whether d^c
  and e^c differ.
- **At τ₀,** K4 for charges 2, 3, 4 and 6, stated in φ = q w.
- **The two-dimensional term with a line** has a logarithmic singularity wherever a sector becomes untwisted (a zero
  mode). The singular lines for the joint parity sum are reported, not used.

## The reading, written before the run (predicted)

- **τ.** Every sector with a closed form gives, in two dimensions and in six, a multiple of one function: log(y|η|⁴)
  or E(τ, 3). The matter's sector does too in two dimensions (the D1 reading's Kokotov step). So τ sits at ω, runs to
  the cusp, or is flat. Which one depends on the content's net sign, a dictionary datum. A generic τ is never selected.
- **The line.**
  - At ω, charged bosons in the parity sectors prefer the 3-torsion lines and fermions prefer none. At a generic τ
    they prefer a 2-torsion line, which cannot split d from e.
  - But the colour-centre line is invisible to every colourless field. So only coloured fields can select it, and
    they live in the matter's sector ρ_Q, whose determinant with a line is not computed here.
  - The arc that would decide it, W60, is the genus-3 cover's theta function by Fay's formula.
- **The Higgs alone** (charge 3, a boson carrying a parity) would put the line where d^c and e^c see different twists.
  That would be a discrete d–e split, if the Higgs's term dominated, which nothing here shows.
- **The count stays all 19 of the 19 free** (18 if I-18 is earned). 0 of 19.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
