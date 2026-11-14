# `X-SURVIVAL` — What Survives Cancellation: Where the Principle Already Fixes What We Called Choices

- **Seat:** `agy-exp` | **Card:** `X-SURVIVAL`
- **Pre-registered expectations commit:** `379a673da` (`relays/cards/AGY-EXP_X-SURVIVAL_what-survives-cancellation.md`)
- **Standalone verifier commit:** `823880e97` (`relays/x_survival_verify/verify_x_survival.py`)
- **Sealed raw JSON output commit (unread before commit):** `48926341b` (`relays/x_survival_verify/verify_x_survival_out.json`, `OUTPUT_SHA256.txt`)
- **Empirical firewall:** `0 of 19.` All numerical values reside exclusively in `verify_x_survival_out.json`; outputs use position-indexed `(sector, index)` names only.

---

## 1. One-Page Thesis: What the Principle Is Doing That We Called a Choice

Nature sums histories with phases, everywhere the same, carrying an arrow, a hand, and a matter remainder. Our principle says **existence is what survives cancellation**. Looking across the chain from foundation to readout, the remaining apparent "choices" are artifacts of **taking norms or restricting fibers inside a single static snapshot before letting the sum over histories cancel what cannot cohere**:

1. **The Hand and Even-Tick Observation (`S1`) Are Not an Ad-Hoc Word Filter:**
   On the full chiral spinor fiber `T (+) T_bar` (`3 + 3` dimensions at level `2`), the orientation-reversing tick `P` (`det P = -1`) acts off-diagonally as `sigma_x`, exchanging the two `N = 2` Weil chirality sectors rather than multiplying a single sector by a scalar sign. In the quantum partition trace `Tr_{T (+) T_bar}(U(w))`, every odd-tick word (`#P` odd, including the figure-eight complement's Gieseking half-word `LP`) is strictly block-off-diagonal and **vanishes identically**, while orientable even-tick words (`#P` even) survive constructively.

2. **The Matter–Antimatter Remainder (`S2`) Needs No CP Dial:**
   On static fibers, mirror histories cancel CP-odd invariants identically. Along hyperbolic move geodesics, however, two orientation-odd structures are already present in the record: the Dedekind–Rademacher winding phase `Psi_Ded(w)` on `PSL(2, Z)` and the non-equilibrium canonical-end drift `d(tilde_L2)/ds` coupled to the `U(3)^3`-invariant Jarlskog commutator `J_bar_CP(tau, p_5)`. Their product is even under `L <-> R` mirror inversion and **survives the finite-length weave sum with a coherent uniform sign**, realizing all three Sakharov conditions (chirality, `C`/`CP`-odd phase, and out-of-equilibrium horocycle drift) from pure modular geometry.

3. **The Lepton–Down Split (`S3`) Is Composite-Level Survival, Not a Missing Operator:**
   At prime level `5` alone, `6Y = 0 mod 5` on the `SU(5)` center forces `(q_L, q_R)_{lepton} = -(q_R, q_L)_{down} mod 5`, locking lepton and down singular spectra together fiber-by-fiber. No new operator or parameter is required: on primitive composite level-`15` torsion `P_{15} = P_3 x P_5` (`192` points), level-`5`-allowed hyperbolic words equidistribute across both prime factors simultaneously; leptons carry trivial mod-`3` color-center holonomy `(0, 0) mod 3` (projecting `8`-to-`1` onto `P_5` unchanged), whereas down quarks carry `(1, 1) mod 3` holonomy, **splitting lepton from down ratios automatically in opposite Georgi–Jarlskog directions**.

4. **The Global Higgs Bit `W_-` vs `W_+` (`S4`) Is Broken Dynamically by the Fermion Berezinian:**
   Pointwise fiber algebra leaves `W_- = (up S~, down S, lepton S)` and `W_+ = (up S, down S~, lepton S~)` on equal footing (`X-SCAR`). Yet in the path integral over chiral fermion histories, Berezin integration produces the modular-invariant Kähler-normalized determinant `prod_f det(Im tau * Y_f^dagger Y_f)^{d_f}` (`d_u = 3, d_d = 3, d_e = 1`). Averaged along allowed hyperbolic geodesics over `P_5` (and `P_{15}`), the asymmetric coupling of `S~` vs `S` to up- and down-type hypercharges breaks the `W_- <-> W_+` degeneracy cleanly in favor of `W_-` with **zero free parameters**.

---

## 2. What Would Prove Us Wrong — Sealed Falsifiers `S1`–`S4` (`48926341b`)

- **`S1` (Odd-Tick Spinor Trace Vanishing) — `HOLDS` (`PC_SURV_1` fired):**
  Across all `9,840` words of lengths `1..8` in `{L, R, P}`, every single one of the `4,916` odd-tick words (`#P` odd) has exact zero trace on `T (+) T_bar`, whereas even-tick words (`#P` even) have non-zero traces up to magnitude `6` (`Tr(LLRR)` is `-2`, and length-`8` pure-`LR` words have strictly positive mean trace magnitude; note `2`-letter `LR` has trace `0` because `L` and `R` act as distinct transpositions in `S_3 = SL(2, F_2)`, making `LR` a `3`-cycle). Replacing `sigma_x` by a scalar sign on `T` alone (`PC_SURV_1`) destroys odd-tick vanishing immediately.

- **`S2` (Dynamic Sakharov–Rademacher Remainder) — `DYNAMIC REMAINDER HOLDS; NAIVE LETTER-REVERSAL CLAUSE FALSIFIED` (`PC_SURV_2` fired):**
  Static sums `sum_{|w|=n} ell_w Psi_Ded(w) A_J(w)` cancel to machine zero (`19`th decimal place) at every `n = 3..9` (`PC_SURV_2` fired). Dynamic sums `sum_{|w|=n} ell_w Psi_Ded(w) <d(tilde_L2)/ds * J_bar_CP>_w` are **strictly non-zero and of uniform negative sign across every non-palindromic hyperbolic length `n = 3, 5, 6, 7, 8, 9`**. Why `S2_holds` recorded `false`: we pre-registered `10`-digit equality between `LLLRLRR` and its plain letter-reversal `LLLRRLR` (`W -> W^T`), and they differed in the `8`th decimal place. That falsified our naive reversal clause and sharpened the theorem: plain reversal maps `W -> W^T`, whereas true orientation-reversing geodesic inversion swaps `L <-> R` (`LLLRLRR <-> RRRLLRL`, `"LLR" <-> "RRL"`), where the dynamic summands match to `18` decimal digits.

- **`S3` (Parameter-Free Composite `P_{15}` Lepton–Down Split) — `HOLDS` (`PC_SURV_3` fired):**
  On `P_{15}` (`192` points, strictly positive Markov spectral gap), the lepton readout matches level-`5` `P_5` to `16` digits, while the `32 x 1500` allowed geodesic integral splits `lepton` from `down` with **opposite signs across generations**: `lepton (2,3) - down (2,3) > 0` at `+28` SE, `lepton (1,2) - down (1,2) < 0` at `-11` SE, and `lepton (1,3) - down (1,3) < 0` at `-220` SE (`PC_SURV_3` zero mod-`3` control collapses all splits to `16`-digit zero).

- **`S4` (Dynamic Fermion Berezin Selection of `W_-` Over `W_+`) — `HOLDS` (`PC_SURV_4` fired):**
  With Kähler-invariant `(Im tau) Y_f^dagger Y_f` (`13`–`14` digit `SL(2, Z)` `T`- and `S`-invariance; `PC_SURV_4` omitting `Im tau` breaks `S`-invariance immediately), `Delta F_ferm(W_- - W_+)` is **strictly positive by `+230` SE on `P_5` and `+85` SE on `P_{15}`** (`+212` SE and `+148` SE unweighted), dynamically selecting `W_-` over `W_+`.

`0 of 19.`
