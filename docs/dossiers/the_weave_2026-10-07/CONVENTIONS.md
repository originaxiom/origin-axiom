# The weave dossier's conventions

Every convention the dossier's scripts use, in one place, each enforced by a test (`tests/test_weave_conventions.py`).
Written 2026-10-08 as step 2 of the assurance plan the owner approved, because most of the day's errors were convention
errors, not mathematical ones:
- a sign label (relay §36);
- a double-counted phase (relay §40);
- a theta-function branch (W41's stopped launch).

Nothing here changes a result.

## 1. Words and automorphisms

- **Generators.** F₂ = ⟨a, b⟩, written 1 = a, 2 = b, negative = inverse (`the_common_point.py`, `AUT`):
  - L: a ↦ a, b ↦ ab;
  - R: a ↦ ab, b ↦ b;
  - P: a ↦ b, b ↦ a;
  - −I: a ↦ a⁻¹, b ↦ b⁻¹.
- **Composition.** `word_aut(w, sign)` composes left to right as maps: `word_aut("LR") = L ∘ R`, so R is applied first.
  The sign −I is composed on the left.
- **H₁ matrices.** `MAT` takes the images of a and b as columns. It is a homomorphism:
  - `h1(φ ∘ ψ) = h1(φ) · h1(ψ)`;
  - `h1(word_aut("LR")) = MAT[L] · MAT[R] = [[2, 1], [1, 1]]`.
  - Main's seat states the opposite order for its own matrices (B1617's Z0: "M(L∘R) = M_R M_L"). Translate between the
    seats' conventions before comparing words longer than three letters.

## 2. Lifts and the action on V

- **Lifts.** A move φ acts through a lift g ∈ 2O ⊂ SU(2) with g ρ_Q(x) g⁻¹ = ρ_Q(φ(x)). `extend(φ)` returns exactly
  two lifts, ±g. The lift of φ ∘ ψ is g_φ g_ψ.
- **The action on V.** `on_V(φ, g)` is z ↦ g⁻¹ (z ∘ φ), a pull-back. It is a **right** action:
  `on_V(φ ∘ ψ) = ± on_V(ψ) · on_V(φ)`.
- **The two string conventions.**
  - `the_mixing_patterns_verified.word(lifts, w)` multiplies the matrices left to right. So `word(lifts, "LR")` is
    `on_V(L) · on_V(R)`, the action of the automorphism R ∘ L, which is `word_aut("RL")`.
  - **The string in `word` is the reverse of the string in `word_aut`.**
  - For the words used so far (L, R, RL, RRL) the reverse is a cyclic rotation, so it names the same conjugacy class and
    no result changes.
  - For longer words the reverse can be a different thread, as the reversal pairs of W34 are. Any new arc that names a
    word of length six or more must say which convention it uses.

## 3. The modulus

- **The geometric action (corrected 2026-10-08, after the independent foundation review).**
  - W21's τ is the period ratio τ = ∫_b dz / ∫_a dz, with the a-period 1; F's second component is f(z + τ).
  - A move with H₁ matrix M = [[α, β], [γ, δ]] (the images of a and b as columns) sends the periods to
    ∫_{φ(a)} = α + γτ and ∫_{φ(b)} = β + δτ.
  - So it acts on τ by **τ ↦ (δτ + β)/(γτ + α)**, the period rule. This is an anti-homomorphism.
- **The rule used before the correction.**
  - The first version of this section, W40 and main's B1617 all used the standard Möbius rule τ ↦ (ατ + β)/(γτ + δ).
  - The two rules agree on L and on R separately. On a word, the standard rule equals the period rule on the reversed
    word.
  - Under the standard rule U = [[0, −1], [1, 1]] (a ↦ b, b ↦ a⁻¹b) fixes ω = e^{2πi/3}. Under the period rule U fixes
    e^{iπ/3} = ω + 1, which is the same torus.
  - The move that fixes ω under the period rule is L U L⁻¹, with matrix [[1, −1], [1, 0]].
- **What is affected.**
  - Group-level results (orders, characters, eigenvalues, invariants) are unchanged by conjugation, so they stand.
  - Anything that evaluates τ-dependent objects at a fixed point must take the stabiliser under the period rule. That
    covers theta functions, modular forms and the zero modes.
  - W41's checks use the whole of SL(2, ℤ) (K1) and the standard theta laws (K2, K3), so they do not depend on the
    choice.
- **Fixed points.**
  - L = [[1, 1], [0, 1]] fixes the cusp ∞, and R = [[1, 0], [1, 1]] fixes the cusp 0.
  - A positive word with both letters has trace at least 3, so it fixes no point of ℍ.

## 4. Theta functions

- θ_n(z | τ) with nome e^{iπτ}: θ₁(z | τ) = 2 Σ (−1)ⁿ e^{iπτ(n+½)²} sin((2n+1)πz), and similarly θ₂ and θ₃.
- `mpmath.jtheta(n, πz, q)` takes the nome q and uses the principal q^{1/4}. It agrees with the series in τ only when
  |Re τ| < 1, or |Re 2τ| < 1 for a theta at 2τ.
- Anywhere τ can leave that strip, sum the series in τ, as `the_zero_modes_weight.th` does. Moduli such as |θ|² are
  unaffected.

## 5. The matter triplet

- **The basis.** T's basis is orthonormal for W21's Hodge–Riemann form (the Cholesky factor in
  `the_couplings_verified.the_group`).
- **The normal form.** In the basis of the normal Klein group's axes, every element of G is c(g) S(g), with S(g) a
  signed permutation of determinant one (W38's addendum).
  - For `the_holomorphic_triplet.lift_choices()[0]`: c(L) = e^{−iπ/4}, c(R) = e^{iπ/4}, c(RL) = 1 and c(RRL) = e^{iπ/4}
    (with `word` as in §2).
  - The other lift signs change c by ±1.

## 6. Physics labels

- **Hypercharge.** Y = diag(−⅓, −⅓, −⅓, ½, ½) on SU(5)_g's 5, so the audit lane's Z = T/2 = (−2, −2, −2, 3, 3) is +6Y.
- **Masses.** Masses are singular values. On T̄ ⊗ T the action is M ↦ g M g†; on T ⊗ T and Sym² T it is M ↦ g M gᵀ.

## 7. Output hygiene

- JSON files carry plain booleans: wrap numpy booleans in `bool()` (W40's disclosed rerun).
- A tolerance-based rank decision reports its gap, or is redone exactly when it is load-bearing.
