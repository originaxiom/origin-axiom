# STEP A v2 — the plan, written before the main runs (main's model-builder, 2026-10-30; data-free)

**Disclosed before the plan.** Prototype runs preceded this page (scratchpad `proto1`–`proto5`):
- the forms' checks;
- the scale table of the singlet and triplet masses, which set the normalisation conventions below;
- one exploratory vacuum search, on menu Z for n = 1–4 at (μ², m₀², λv) = (0.5, 0.005, 0.3), 12 starts each.

What it showed:
- for n = 1, a fixed τ with several directions at one value;
- for n ≥ 2, a unique direction, with τ on Re τ = ½.

The criteria below were not tuned to it.

## 1. The construction (model.py; labels in DESIGN.md)

- **Modular group and actions.** Mp(2, ℤ) acts on (τ, Ŝ) through the frame's own ρ_R: T: (τ + 1, L⁻¹Ŝ), S: (−1/τ, PŜ).
- **Heavy copies.** Copy i holds (L_i, L̄_i, E_i, Ē_i) with
  W_i = M Y_L,i L L̄ + M Y_E,i E Ē + λ (Hᵀ Y₃,i) L Ē.
- **Masses.** Charged [[a, b], [0, d]] and neutral a, where a² = M²(2y)^{w_L}|Y_L|², d² = M²(2y)^{w_E}|Y_E|² and
  b² = (λv)²(2y)^{w₃}|ŜᵀY₃|².
- **The potential.** V = Σ over the 3n eigenvalues of F(m²). F is the supertrace Coleman–Weinberg function, with one
  shared μ, m₀, M and λ.

## 2. Declared menus and conventions (fixed now)

- **Singlets** (copy i takes entries 2i − 1 and 2i):
  - η¹²E₄ (W150), η¹²E₆;
  - η²⁰, η²⁴;
  - η⁸E₆, η¹⁶E₄;
  - η⁸E₄², η²⁰E₄;
  - η¹⁶E₆, η¹²E₄²;
  - η⁸E₄E₆, η²⁴E₄;
  - η²⁰E₆, η¹⁶E₄²;
  - η¹²E₄E₆, η⁸E₄³.

  These are cusp forms with s ≥ 8, of weights 10–16.
- **Triplets:**
  - **menu Z** (B1730's one-unit lines, ordered by |a|, then sign): F₂, F₆, F₋₂, F₁₀, F₋₆, F₁₄, F₋₁₀, F₁₈;
  - **menu H** (H-cov's DR first): DR, F₂, F₆, F₋₂, F₁₀, F₋₆, F₁₄, F₋₁₀.
- **The tie's normalisation, primary.** The singlets are divided by their sup norm (max of (2y)^w|Y|² = 1), and F_a by
  2^{a/3}, so that N(F_a) = iη⁹, the family's own invariant. DR is cusp-normalised (24·DR).
- **The tie's normalisation, alternative.** Cusp normalisation for everything: leading |coefficient| 1, B1730's F_a.
- **Parameters.** M = 1; μ² ∈ {0.3, 0.5, 0.8}; m₀² = 0.01 μ² (primary) and 0.1 μ² (check); λv ∈ {0.1, 0.3, 1.0}.

## 3. What is computed and the criteria (fixed now)

1. **Invariance.** Each copy's three eigenvalues under T and S at random points (30 digits): pass at < 10⁻²⁰ relative.
   Controls that must fail (> 10⁻³): B1818's θ₃^{2m} singlet; a triplet with permuted components; a wrong exponent;
   B1818's additive coupling.
2. **Phase.** The eigenvalues at e^{iα}Ŝ must equal those at Ŝ (< 10⁻²⁵). Control: B1818's additive coupling moves
   with α.
3. **Rank.** At 12 random points, for n = 1–8 and both menus: the rank of d(log m²) on the six local coordinates,
   counting singular values > 10⁻⁹ (absolute, row-scaled), with two step sizes.
   - Expected generic: min(n + 2, 6).
   - Control: one shared triplet form caps the rank at 3.
4. **Vacua.** For each (menu, n, parameters): 24 seeded random starts of a local minimisation on the six coordinates
   (BFGS on ℂ³ ⊃ S⁵; τ reduced to F), then clustering modulo the group and the mirror.
   - **Isolated:** the 6 × 6 Hessian in local coordinates (τ; a Hermitian-orthogonal chart on CP²) has every eigenvalue
     > 10⁻⁶ × the largest, stable between two step sizes.
   - **Flat:** an eigenvalue below 10⁻⁹ × the largest and stable. The valley is then followed, and its dimension is the
     number of such eigenvalues.
5. **Free numbers.** At each global minimum, dx*/d(log μ², log m₀², log λv) by the implicit-function theorem,
   −H⁻¹ ∂ₚ∇V, checked by re-minimisation at one point.
   - Its numerical rank (singular values > 10⁻⁶ × the largest) is the number of free numbers that move the vacuum.
6. **Leading order (λv → 0).** τ₀* = argmin V₀ (the singlets), and Ŝ* is the lowest eigenvector of Q(τ₀*), compared
   with the exact vacua at small λv.
   - For n = 2: Ŝ* = Y₃,₁ × Y₃,₂ when both c_i > 0.
7. **Symmetric configurations.** The gradient (zero by symmetry) and the Hessian at (i, (1, −1, 0)/√2) and at
   (ω, the eigenvectors of PL⁻¹). Is any of them the global minimum?
8. **Untied control.** Per-copy levels planted at a random point. The vacuum's dimension and the levels spent.

**The reading, fixed now:** "tied ratios fix the direction" means that the global minimum is isolated (§3.4) for the n
in question, at every primary parameter point. The number of free numbers is the rank of §3.5.
