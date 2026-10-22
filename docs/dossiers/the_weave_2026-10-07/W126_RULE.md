# W126 — the read-out on the physical spacetime (main's C10), for the ground-state universes: the Lorentzian index of the triplet-twisted Dirac operator on the Milne universe over the Weeks and Meyerhoff manifolds (the rule, committed before the script)

The SM-derivation seat, 2026-10-22. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The owner's goal, as main's completion map states it** (`docs/THE_COMPLETION_MAP.md` on main, S187).
  - C10 asks for the read-out on a physical spacetime: the APS or L² index of the Dirac operator twisted by the
    triplet's representation on the Milne cone over a thread, W120's exact 4d vacuum.
  - Main lists it as never computed.
- **Why this seat.** The gravity line built the Milne cone (W120), chose the closed universes (W122) and computed
  their graviton spectra (W124). This arc takes C10 on the two ground-state universes, where everything is compact.
- **B1604 does not settle it.** T-NO-INDEX-IN-THREE concerns flat-module Euler characteristics on a 3-manifold. The
  index here is a four-dimensional Lorentzian one, and as shown below it is the dimension of a Dirac kernel, which is
  not an Euler characteristic.

## The object (by hand, to be checked)

- **Bär and Strohmaier's theorem** (Amer. J. Math. 141 (2019); arXiv 1506.00959, Main Theorem and §4).
  - M is compact and globally hyperbolic, with spacelike Cauchy boundary Σ₋ ⊔ Σ₊. The Dirac operator under
    Atiyah–Patodi–Singer conditions is Fredholm.
  - Its index is ∫_M Â + ∫_∂M TÂ − (h(A₋) + h(A₊) + η(A₋) − η(A₊))/2. Here A± is the Dirac operator of Σ±, h the
    dimension of its kernel and η its η-invariant. Equivalently, the spectral flow of A_t equals ind + h(A₊).
  - It extends to twisting by a flat unitary bundle E (their §7).
- **On the Milne universe over a closed hyperbolic N**, M = [t₁, t₂] × N with g = −dt² + t²g_N.
  - The metric is flat, a quotient of the inside of Minkowski space's light cone, and ch(E) = rank E for a flat E.
    So ∫Â∧ch(E) = 0.
  - Each slice is umbilic, with second fundamental form g_t/t. By Codazzi the transgression form vanishes.
  - The slice operator is A_t = D_N^E/t, which has the same kernel and η-invariant for every t. So the spectral flow
    is 0, and **ind = −h(D_N^E)** for every pair of slices.
  - The physical read-out on the Milne universe is therefore minus the number of E-twisted harmonic spinors on the
    spatial universe. That number is a spectral quantity, not a topological one.
- **The triplet's bundle over a thread.**
  - The triplet's representation is W123's ρ = (e^{iπ/4}P, e^{iπ/4}L⁻¹), main's ρ_T, a representation of the
    metaplectic group.
  - Over the thread A it gives the flat bundle E_A over N_A, whose holonomy around the circle is ρ(Ã) for a lift Ã
    of A. The lift is a choice of sign, ρ(S⁴) = −1.
  - E_A is the sum of line bundles L_ζ, one for each eigenvalue ζ of ρ(Ã), each a character of π₁ through the circle.
  - **On a closed filling, a line extends only if its character factors through the filled manifold's H₁.** The
    Weeks manifold has H₁ = ℤ/5 ⊕ ℤ/5 and the Meyerhoff manifold ℤ/5. So only lines with ζ⁵ = 1 can extend.
  - If no eigenvalue of ρ has order divisible by 5, only the eigenvalue-1 lines extend, and they are trivial. Then
    E restricted to N is ℂ^{m₁}, with m₁ the multiplicity of the eigenvalue 1, and **ind = −m₁·h(D_N)**, m₁ ≤ 3.
- **h(D_N) by the spinor trace formula**, extending W124's instrument (its enumeration and its unfolding identity,
  unchanged).
  - The density is (vol/2π²)(t² + ¼) over t ∈ ℝ for the spectrum of D². The heat-kernel check: it gives
    2vol/(4πs)^{3/2}·(1 + s/2), which is Gilkey's a₁ = −rank·R/12 = 1 for R = −6.
  - The geodesic weight is 2cos(θ̃/2)/(2(cosh ℓ − cos θ)). Here e^{(ℓ + iθ̃)/2} is the larger eigenvalue of the
    element's spin lift in SL(2, ℂ), so 2cos(θ̃/2) carries the spin structure.
  - There is no correction term; the spinor bundle has no trivial constituent.
  - S_{1/2}(T) = Σ_j h_T(λ_j) over the Dirac eigenvalues. The window h_T is W124's, with R = 6 and w = 2/3.
  - A harmonic spinor puts 2G(T) into S_{1/2}(T), so **S_{1/2}(0) ≥ 2h**. Every term is non-negative, so
    S_{1/2}(0) < 2 forces h = 0.
- **The spin lift.**
  - Both manifolds have H¹(N; ℤ/2) = 0, so each has exactly one spin structure.
  - SnapPy's SL(2, ℂ) matrices for the unsimplified presentation are a projective lift. Exactly one assignment of
    generator signs makes every relator +I (seen; disclosed below).
  - Each Dirichlet face pairing is a word in those generators. Its lift is the signed product. The enumeration carries
    the lifted product alongside W124's O(3,1) product.

## Weave or thread

**A thread result, labelled so.**
- Two closed universes, chosen by W122's stated rule (least volume over every thread and slope in its box), each one
  thread's filling.
- The weave question, C10 on every thread with its cusp's end condition, is named below and not answered here.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| D0 | the instrument: (a) exactly one sign assignment makes every relator +I on each manifold; (b) one matrix conjugates SnapPy's O(3,1) words to the Dirichlet pairings, residual < 10⁻¹⁰; (c) on every kept element \|tr γ̃\|² equals the O(3,1) trace to 10⁻⁸ relative; (d) the enumeration reproduces W124's counts of visited elements and kept axes exactly, and its S₂ on the grid to 10⁻⁹ | 90% |
| D1 | Weyl for spinors: on both manifolds N_{1/2}(8) is within 25% of (vol/π²)(8³/3 + 8/4) | 80% |
| D2 | positivity: S_{1/2} ≥ −0.05 on [0, 10] on both manifolds | 75% |
| D3 | no harmonic spinor on the Weeks manifold: S_{1/2}(0) < 1.9, so h(D_Weeks) = 0 | 70% |
| D4 | no harmonic spinor on the Meyerhoff manifold: S_{1/2}(0) < 1.9 | 65% |
| D5 | the triplet's lines, exact: the group generated by ρ(S) and ρ(T) is finite, and none of its elements has an eigenvalue of order divisible by 5 | 95% |
| D6 | read-out: S_{1/2}(0); the peaks below T = 8 with their masses; the positivity lower bound on the least \|λ_D\| at ε = 0, 0.01 and 0.02; N_{1/2}(8); the order of ρ's image group; ρ(Ã)'s eigenvalues and m₁ for both lifts of +LR and of −LR; the counts | — |

## What the outcomes mean (fixed now)

- **D0 to D5 hold.** Then on the Milne universe over the Weeks manifold, the Lorentzian index of the Dirac operator
  twisted by the triplet's bundle is −m₁·h(D_Weeks) = 0, for either lift and every pair of Cauchy slices. The same
  holds over the Meyerhoff manifold.
  - So C10's read-out on the ground-state universes is zero generations. This is a thread result.
  - It is not a failure of the reduction: the index there is a Dirac kernel, and that kernel is empty.
  - C10's open case is then the cusped threads themselves, with L² spinors. Bär (J. Differential Geom. 54 (2000))
    shows the Dirac spectrum of a finite-volume hyperbolic manifold is discrete when the spin structure, here twisted
    by the line's character, is non-trivial on every cusp, and is all of ℝ otherwise. That is the natural form of the
    cusp's end condition, and the next arc's question.
- **D3 or D4 fails.** Then S_{1/2}(0) ≥ 1.9: either a harmonic spinor, or eigenvalues closer to 0 than the window
  resolves.
  - h is not decided at this resolution, and the index may be non-zero.
  - It is recorded with the positivity bound, and m₁ then matters.
- **D5 fails.** Then some triplet line of order divisible by 5 could extend. It is recorded, and the reduction to
  ℂ^{m₁} fails.
- **D1 or D2 fails.** Then the spinor normalization or the lift is wrong. It is recorded, and nothing in D3 or D4 is
  read until it is resolved post hoc, labelled so.

## What stays out

- The cusped threads, where C10 asks for an L² index with the cusp's end condition. Other closed fillings.
- Twists by characters of H₁ other than the triplet's lines; non-abelian twists.
- The η-invariant itself, and the scale.

## Seen before the rule (disclosed)

- **Read:**
  - Bär and Strohmaier, arXiv 1506.00959: the Main Theorem, §4's spectral-flow form, and the extension to twisted
    operators.
  - Lin and Lipnowski's text, searched for Dirac results; it has none of this kind.
  - Main's completion map (S187) and B1604's findings.
- **Instrument checks:**
  - With SnapPy's simplified presentation, the raw lift sends one Weeks relator to −I.
  - With the unsimplified presentations, exactly one sign assignment makes every relator +I: (1, −1, 1) on Weeks and
    (−1, −1, −1) on Meyerhoff.
  - The Dirichlet pairing words are in the unsimplified generators.
  - One conjugation relates SnapPy's O(3,1) words to the Dirichlet pairings: residuals 6 × 10⁻¹⁵ and 9 × 10⁻¹⁵, with
    traces equal to 10⁻¹⁴.
- **By hand:** the reduction to −h(D_N^E), the extension lemma, the spinor density's heat-kernel check, and the
  criterion S_{1/2}(0) < 2.
- **No spinor sum, eigenvalue order or ρ image** has been computed.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
