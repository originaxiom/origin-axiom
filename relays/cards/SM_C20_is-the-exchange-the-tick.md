# SM-C20 — is the antiunitary that flips frame D1's Higgs bit the tick itself?

*Card of the SM seat, 2026-11-18, following SM-C19, on the author's "go". Committed and pushed before any check.
Data-free; main's B1957 instrument (`checks/level6_higgs.py`) imported unchanged.*

## 1. The derivation, before any check

- The tick σ = [[1, 1], [1, 0]] (a ↦ ab, b ↦ a; det −1) factors as σ = T·S·R₀:
  - T = [[1, 1], [0, 1]], S = [[0, −1], [1, 0]], and R₀ = diag(1, −1);
  - T·S = [[1, −1], [1, 0]], and T·S·R₀ = [[1, 1], [1, 0]].
- R₀ is τ → −τ̄, z → z̄. On the flux-6 modes θ[k/6, 0](6z, 6τ), whose Fourier coefficients are real, it acts as plain
  complex conjugation K, with no permutation of k.
- So the tick acts on the six modes as the antiunitary Σ = ρ(T)ρ(S)·K = T₆S₆·K.
- **SM-C19 found A = T₆S₆ among the four antiunitaries that exchange v₊ and v₋.** So Σ exchanges the ground pair.
- **It remains to check that Σ is the tick and not merely an element like it.** Its square must be the golden act's
  transport:
  - σ² = [[2, 1], [1, 1]] = M;
  - with K·ρ(h)·K = ρ(R₀hR₀), so that conj(T₆) = T₆⁻¹ and conj(S₆) = S₆⁻¹, Σ² = T₆S₆T₆⁻¹S₆⁻¹ = ρ(TST⁻¹S⁻¹);
  - and TST⁻¹S⁻¹ = M as matrices. So Σ² should equal U_M, up to the representation's central phase.

## 2. What is checked

- **C0:** conj(T₆) = T₆⁻¹ and conj(S₆) = S₆⁻¹ (the antiunitary rule).
- **E1:** Σ² = U_M up to a phase, with main's U_M.
- **E2:** Σ·v₊ ∝ v₋ (and Σ·v₋ ∝ v₊), with v± the ±π/6 eigenvectors.
- **E3 (consistency):**
  - the other factorisations of σ with det −1 (σ = T·J with J = swap = S·R₀) give the same Σ;
  - and the mirror tick σ′ = [[1, 1], [1, 0]]ᵀ, the same matrix, gives the same answer. This is noted, not separately
    run.

## 3. Expectations

| | expectation | prior |
|---|---|---|
| C0 | the antiunitary rule holds for T₆ and S₆ | 95% |
| E1 | Σ² = U_M up to a phase | 75% |
| E2 | Σ exchanges v₊ and v₋ | 90% |

## 4. What it means

- **If E1 and E2 hold:** the tick, acting on the six Higgs modes, is an antiunitary square root of the golden act's
  transport, and it flips frame D1's Higgs ground bit.
- So the Higgs vacuum bit is the tick's orientation itself: one bit, carried by one move of the genesis.
- Which sign is realised stays open. A history with an odd number of ticks flips it, and one with an even number keeps
  it. That ties it to the even-tick condition (the author's ruling of 2026-11-11, B1926).

## 5. Files

relays/sm_c20/, with its script, output and run. The page will be relays/SM_C20_THE_EXCHANGE_IS_THE_TICK.md.
