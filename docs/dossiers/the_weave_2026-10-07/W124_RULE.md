# W124 — the graviton spectrum of the ground-state universe: the transverse traceless modes of the Weeks manifold, and of the Meyerhoff manifold, by the trace formula, calibrated against two outside sources (the rule, committed before the script)

The SM-derivation seat, 2026-10-22. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The owner's choice** (2026-10-22): the graviton spectrum on the ground-state universe, alongside the Higgs route
  (W123).
- **Where the gravity line left it.**
  - Every thread is the space of an exact 4d vacuum universe, the Milne cone −dτ² + τ²g (W120). Its gravitons are the
    transverse traceless (TT) modes of g.
  - The least closed universe filled from the record's threads is the Weeks manifold, from −LR. The next is the
    Meyerhoff manifold, a filling of the tick +LR itself as well as of −LR (W122).
  - The gravity line named the graviton spectrum there and did not compute it.
- **Why a new instrument.** SnapPy's length spectrum on Weeks took over ten minutes at length 4. Its alternative took
  260 s at length 3, and failed at the default precision. The trace formula needs lengths near 6. So this seat
  enumerates the group itself and uses the unfolding identity below, which needs no list of conjugacy classes.

## Weave or thread

**A thread result, labelled so.** Two closed universes, each one filled thread. They are chosen by W122's stated rule,
least volume over every thread and slope in its box, so none is hand-picked. The filling slope is a choice, and each
spectrum is one manifold's.

## The object (by hand, to be checked)

- **The mode equation on the cone.** Write a perturbation of the Milne cone as δg = τ²T(τ)h, with h TT on g and
  ∇*∇h = μh. The linearized vacuum equations give τ²T'' + 3τT' + (μ − 2)T = 0.
  - With μ = ν² + 3, the exponents are p = −1 ± iν. Every graviton is τ^{−1}cos(ν log τ + φ): a damped oscillation in
    log τ whose frequency is the mode's spectral parameter.
  - The same exponents follow from the standard tensor equation of an open FLRW universe in conformal time,
    h'' + 2h' + (ν² + 1)h = 0.
- **The three sectors, in one parametrization** (K-type of the frame bundle, helicity m):
  - m = 0, scalars: −Δ = r² + 1;
  - m = ±1, coexact 1-forms: the Hodge Laplacian is t²;
  - m = ±2, TT tensors: ∇*∇ = ν² + 3, the Einstein operator Δ_E = ν² + 1 and Lichnerowicz's Δ_L = ν² − 3.
- **The densities.** The identity term's density is (vol/2π²)(t² + m²) for each helicity pair, and (vol/4π²)t² over
  t ∈ ℝ for scalars.
  - Checked by hand: on the trace-free symmetric tensors (helicities −2 to 2, with ∇*∇ = t² − m² + 7), the heat trace
    comes out as 5(1 − s) vol/(4πs)^{3/2}. That is Gilkey's coefficient for a rank-5 bundle with R = −6.
- **The trace formula,** for even h with g(u) = (1/2π)∫h(t)e^{−itu}dt:
  - scalars: Σ_j h(r_j) = (vol/4π²)∫h(t)t²dt + G₀, where the sum includes the constant mode at r = i;
  - coexact: Σ_j h(t_j) = (vol/2π²)∫h(t)(t² + 1)dt + G₁ + h(0). This is Lin and Lipnowski's Theorem 4 (arXiv
    1810.06346; J. Amer. Math. Soc. 35 (2022)) with b₁ = 0, doubled to sum both helicities;
  - TT: Σ_k h(ν_k) = (vol/2π²)∫h(t)(t² + 4)dt + G₂.
  - Here G_m = Σ_{γ ∈ Γ∖1} |axis(γ) ∩ D| · c_m(θ_γ) · g(ℓ_γ) / (2(cosh ℓ_γ − cos θ_γ)), with c₀ = 1, c₁ = 2cos θ and
    c₂ = 2cos 2θ.
- **Why the TT formula has no correction here** (by hand). Lin and Lipnowski's h(0) comes from the constant function:
  it has no exact 1-form, and at the trivial point the scalar series' transform equals the helicity-1 transform at 0.
  Run the same bookkeeping on the trace-free symmetric tensors: the scalar part loses the constant, and the coexact part
  carries Lin and Lipnowski's term. The two cancel, leaving the TT formula as written when b₁ = 0. Both manifolds have
  b₁ = 0, with homology ℤ/5 + ℤ/5 and ℤ/5.
- **The unfolding identity** (by hand). For a class [γ] with primitive γ₀, the elements of the class whose axes meet a
  fundamental domain D contribute Σ|axis ∩ D| = ℓ(γ₀). So summing over every element of Γ, weighted by the length of
  its axis inside D, counts each oriented closed geodesic once with the factor ℓ(γ₀). No class has to be identified.
- **The enumeration.**
  - D is SnapPy's Dirichlet domain, centred at x₀, with the face pairings as O(3,1) matrices.
  - Elements are reached breadth first by right multiplication by face pairings, pruned at d(x₀, γx₀) ≤ R + 3r_out.
  - An element is kept when d(x₀, γx₀) ≤ R + 2r_out, ℓ(γ) ≤ R, and its axis is within r_out of x₀. The axis distance
    δ follows from cosh d(x₀, γx₀) = cosh ℓ + sinh²δ (cosh ℓ − cos θ).
  - ℓ and cos θ come from tr γ = 2cosh ℓ + 2cos θ and tr γ² = 2cosh 2ℓ + 2cos 2θ. |axis ∩ D| comes from the axis's
    two light-like eigenvectors and D's half-spaces ⟨x, γ_i x₀ − x₀⟩ ≥ 0.
  - **R = 6.0.**
- **The window.** h_T(t) = G(t − T) + G(t + T), with G(t) = e^{−t²/(2w²)} and w = 4/R = 2/3. Its g is
  (w/√(2π))·2cos(Tu)·e^{−w²u²/2}, cut at |u| ≤ R, a relative error of e^{−8}.
  - S_m(T) is the formula's value: Σ over the spectrum of h_T, so an isolated eigenvalue of multiplicity k gives a
    peak of height k.
  - The smoothed count is N_m(T) = ∫₀^T S_m / (w√(2π)).
  - The grid is T from 0 to 10 in steps of 0.01. Peaks closer than about 1.3 merge, and their masses add.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| G0 | the instrument: D's vertices satisfy every face inequality to 10⁻⁹ and lie within r_out; no element is found twice; the number of orbit points within ρ = 5, 6 and 7 is within 5% of π(sinh 2ρ − 2ρ)/vol, on both manifolds | 90% |
| G1 | exact (sympy): for h = φ(z)(dx dy + dy dx) on the upper half-space, which is TT for every φ, with φ = z^{a−2} an eigentensor of ∇*∇, the linearized Ricci of −dτ² + τ²(g + εT(τ)h) vanishes iff τ²T'' + 3τT' + (μ(a) − 2)T = 0, with μ(a) the eigenvalue | 90% |
| G2 | the scalar calibration: (a) on both manifolds S₀(0) equals the constant mode's h₀(i) = 2e^{1/(2w²)} to 10⁻³ relative; (b) on Weeks, S₀ minus the constant's term agrees with Cornish and Spergel's Table III (74 eigenvalues; r = √(λ − 1)), smoothed by the same window, to within 0.3 at every T in [0, 7]; (c) on Meyerhoff, N₀ without the constant reaches 0.5 between T = 4.8 and 5.6 (Inoue's k₁ = 5.40, r₁ = 5.31) | 65% |
| G3 | the coexact calibration (Lin and Lipnowski: Weeks has λ₁* > 8.9, Meyerhoff λ₁* ≈ 0.33): on Weeks, S₁ ≤ 0.05 on [0, 1.0]; on Meyerhoff, S₁(0) ≥ 1.0; on both, S₁ ≥ −0.05 on [0, 10] | 70% |
| G4 | TT positivity: S₂ ≥ −0.05 on [0, 10] on both manifolds | 75% |
| G5 | the lowest graviton on Weeks: N₂ reaches 0.5 at some ν₁ in [1.0, 4.0] | 55% |
| G6 | Weyl: on both manifolds N₂(8) is within 25% of (vol/π²)(8³/3 + 32) | 80% |
| G7 | read-out: for both manifolds, the TT peaks below T = 8 with their masses, ν₁, Δ_E = ν₁² + 1, ∇*∇ = ν₁² + 3 and the Milne log-period 2π/ν₁; S₂(0); the scalar and coexact peaks; the counts of elements and of kept axes | — |

## What the outcomes mean (fixed now)

- **G0 to G4 hold.** The instrument is calibrated against two outside sources, Cornish–Spergel with Inoue, and Lin–
  Lipnowski. G4 says the TT formula is consistent. The TT read-out is then the graviton spectrum of the ground-state
  universe and of the tick's own closed universe.
  - Every graviton on the Milne cone over them is τ^{−1}cos(ν_k log τ + φ). The spectrum is discrete, with no free
    number except the filling slope, which is a choice.
  - The lowest frequency ν₁ is a pure number of that universe. A thread result.
- **No growing graviton.** If G4 holds with no weight at imaginary ν (such weight would show as oscillation or
  negativity in S₂ at small T), every graviton decays. That agrees with Andersson and Moncrief's stability of the
  Milne universe over closed hyperbolic slices, here at the linear level and computed, not cited.
- **G2 or G3 fails.** Then the instrument is not calibrated. The TT read-out is recorded but not banked, and the
  failure is recorded.
- **G4 fails.** Then the TT normalization, or the absence of a correction, is wrong; recorded as failed.
- **A phantom.** An isolated peak centred at T = 0 with S₂(0) near 2 or a multiple of it would be flagged as the
  likely trace of a missed correction term, not read as a graviton, and recorded.

## What stays out

- The de Sitter and anti-de Sitter slicings.
- The cusped threads, whose spectrum is continuous.
- Other closed fillings, and the scale G.

## Seen before the rule (disclosed)

- **Read:**
  - Cornish and Spergel (arXiv math/9906017), Table III: Weeks's eigenvalues 27.8, 32.9 (×2), 43.0, 59.7, 66.3,
    67.6 (×2), …, 74 in all;
  - Inoue (arXiv math-ph/0011012), Table II: k₁ = 5.27 (DBEM) and 5.10 for Weeks, 5.40 and 5.34 for m003(−2,3), each
    of multiplicity 1, with E = k² = p² + 1;
  - Lin and Lipnowski (arXiv 1810.06346): Theorem 4, with λ₁* > 8.9 for Weeks and λ₁* ≈ 0.33 for Meyerhoff.
- **Instrument checks:**
  - SnapPy's length spectrum on Weeks to length 2 (0.5846 ×3, 0.7941 ×3, 1.2899 ×3) and its slowness above 3;
    length_spectrum_alt's 33 geodesics in 260 s at length 3 with 212 bits, and its failure at 106;
  - the Dirichlet domains: 18 and 16 faces, out-radii 0.7525 and 0.7485, homology ℤ/5 + ℤ/5 and ℤ/5.
- **By hand:** the densities and their heat-kernel check, the mode equation, the unfolding identity and the absence of
  a TT correction when b₁ = 0.
- **No spectral computation** for this arc has been run.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
