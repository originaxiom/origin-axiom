# W41 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-08. Committed before the code that reads it runs. The predictions below were derived by
hand before this was written. Nothing here is a result.

## Why this route

- **Main's S95 asks** for "the weights the weave's zero modes carry", as the input to its weighted cell (B1618, sealed).
- **Relay §40 gave the weight as a reading.** f = θ₃(z | 2τ)/√θ₁(z | τ) has weight ¼ and index 0. The one-form F = f dz
  has weight −¾.
- **One line of §40 is withdrawn here, before any run.** Its point 3 ended: "So the modes' U-phases at ω are W40's
  eigen-turns shifted by that." That double-counts.
  - At ω, U is an automorphism of the punctured curve E_ω, and pullback by a holomorphic automorphism commutes with the
    comparison between holomorphic forms and cohomology.
  - So U's action on the holomorphic modes at ω is its topological action on H^{1,0} = T: W40's eigen-turns, with the
    automorphy factor already inside.
  - In a split into weight × representation, the representation part at U carries the compensating phase. The split is
    ε(γ)(cτ + d)^{−3/4} times c ⊗ S, with ε(U)(1 + ω)^{−3/4} = 1, since the modes' periods at ω are not zero.

## Weave or thread?

- The quantity is the triplet of zero modes' transformation under the moves, all of SL(2, ℤ) at once. It is a property
  of the joint action, about all threads at once: weave-type.
- Nothing here is chosen by hand except the sample points, which are fixed below.

## The objects

- **The form** (W21's second route, `the_holomorphic_triplet_periods.py`): F = (f(z), f(z + τ)) dz, with
  f(z) = θ₃(z | 2τ)/√θ₁(z | τ).
- **Its norm.** N(τ) = 2 ∫_E (|f(z)|² + |f(z + τ)|²) dx dy, which is the periods script's `l2_norm`. It is free of the
  square root's branch, and it equals the Hodge–Riemann form Q on the mode (W21: to 8 × 10⁻¹⁵).
- **The moves on τ**, τ ↦ (aτ + b)/(cτ + d), for:
  - T = [[1, 1], [0, 1]];
  - S = [[0, −1], [1, 0]];
  - U = [[0, −1], [1, 1]];
  - the record's L = [[1, 1], [0, 1]] and R = [[1, 0], [1, 1]];
  - the words RL and LRR.
- **The base points.** τ₀ = 0.23 + 1.07i (W21's first) and τ₁ = −0.41 + 0.83i (its second).

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **K1** | the weight, by the norm: g(τ) = N(τ)/(Im τ)^{3/4} takes the same value at τ and at γτ for every γ listed, at both base points, to relative 10⁻⁶. With exponents ¼ or 1 in place of ¾ it fails by more than 10⁻² for S at τ₀. | 90% |
| **K2** | the numerator pair (θ₃(z \| 2τ), θ₂(z \| 2τ)) obeys (θ₃, θ₂)(z′ \| 2γτ) = (cτ + d)^{1/2} e^{iπcz²/(2(cτ + d))} W(γ) (θ₃, θ₂)(z \| 2τ), with z′ = z/(cτ + d) and W(γ) a constant 2 × 2 unitary matrix, for γ = T, S, U. W is fitted at two z and checked at three others and at the other base point, to 10⁻¹⁰. | 90% |
| **K3** | θ₁ obeys θ₁(z′ \| γτ) = ε₁(γ)(cτ + d)^{1/2} e^{iπcz²/(cτ + d)} θ₁(z \| τ), with ε₁(γ) an eighth root of unity, for T, S and U (a control of the known law). | 99% |
| **K4** | from K2 and K3, f has weight ¼ and index 0: the exponentials cancel and M_f(γ) = W(γ)/√ε₁(γ) is constant. So the one-form F has weight −¾. | 90% |

**The reading, written before the run.**
- If K1 to K4 hold, the weave's zero modes are a vector-valued modular form of weight −¾ (as one-forms; ¼ for the
  coefficient), and their normalised Kähler weight is ¾.
- The moves act on them by the automorphy factor times ε ⊗ c ⊗ S (W38's normal form).
- At ω the total action is W40's: eigen-turns ¼, 7/12 and 11/12, nothing added.
- B1618 sweeps every phase, so its verdict does not wait on this. What this adds is which phase is the weave's.

## Discipline

- One run. A failed launch (a crash before the read-out) is disclosed and fixed, not counted as a run.
- Each cell is recorded as computed; a failed prediction is recorded as failed.
- Post-hoc checks are labelled.
