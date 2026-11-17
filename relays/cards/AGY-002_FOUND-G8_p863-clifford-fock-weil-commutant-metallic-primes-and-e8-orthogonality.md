# Card `AGY-002_FOUND-G8` — Complete Resolution of `P-863` (`B1951`): `CAR`/`Clifford` Derivation of `Postulate D`, Continuous-Colour Commutant Dichotomy, Metallic Rivals, and Prime-`3` / Prime-`5` Orthogonality in `E_8` (`0 of 19`)

## 1. Package and Question

Addressing `P-863` `Q1(a)-(d)` (`B1951` on `origin/main` `ff8e1ca57`) under strict `0 of 19` firewall, `Guardrails 1-6`, and `100%` mask-safe rational/integer prose:
1. **`P-863(a)`:** Does canonical anticommutation (`CAR`) quantization `{c_a, c_b^dag} = delta_{ab}` of the `5`-dimensional Level-`5` `Weil` space `W_5 = L^2(F_5)` generate `Cl(10, C) ~= End(Lambda^*(W_5))` (`dim 32 = 16_+ (+) 16_-` graded by `(-1)^F`), deriving `Postulate D`'s `Lambda^{even}(W_5)` `1`-generation `6Y` spectrum `[-4^3, -3^2, 0^1, +1^6, +2^3, +6^1]` (`with zero normal-ordering ambiguity since Tr(6Y) = 0`) and `Lambda^1(W_5)` `[-2^3, +3^2]` from standard fermionic Fock quantization?
2. **`P-863(c)`:** What is the exact Lie-algebra commutant inside `su(5)` of the full `120`-element `Weil` group `rho(SL(2, F_5))` versus its centre `rho(-I) = P`, and what are the exact `Frobenius-Schur` indicators on `3_+` and `2_-`?
3. **`P-863(d)`:** Across metallic-mean equations `x^2 - k x - 1 = 0` (`D_k = k^2 + 4`, `k = 1..12`), is the Golden field `Q(sqrt(5))` (`Delta_K = 5`) the unique quadratic field of odd prime discriminant yielding the `3 + 2` split?
4. **`P-863(b)`:** Inside `248D` `E_8 supset (A_2^{fam} (+) A_2^{(c)} (+) A_2^{(L)} (+) A_2^{(R)})`, does placing Prime `5` (`Weil 3_c + 2_w`) inside `E_6^{GUT}` and Prime `3` (`m004` `Z[zeta_6]` Eisenstein cusp + `CIM` `H^0(E, L^3)`) on the commuting `A_2^{fam} = C_{E_8}(E_6^{GUT})` deliver `3` chiral families without clashing with the `Weil` colour `3` (`while clarifying E_6^{cent} cap E_6^{GUT} = 16D and order(W_swap) = 4`)?

## 2. Deliverables and Definition of Done

1. **`CAR` / `Cl(10)` Fock Derivation of `Postulate D` (`P-863(a)`):**
   - Construct exact `5 x 5` `SL(2, F_5)` `Weil` matrices (`order = 120`, `(S T)^3 = S^2 = P`) and `32 x 32` `CAR` operators `c_a, c_a^dag`; verify `{c_a, c_b^dag} = delta_{ab} I_{32}`, `Cl(10)` `10`-gamma product basis span `== 1024`, zero normal-ordering shift `Tr(6Y) = 0`, `Lambda^{even}(W_5)` `6Y` spectrum `[-4^3, -3^2, 0, +1^6, +2^3, +6]` (`sum = 0, sum^3 = 0`), and `Lambda^1(W_5)` `[-2^3, +3^2]`.
2. **Continuous-Colour Commutant Dichotomy & `Frobenius-Schur` Indicators (`P-863(c)`):**
   - Prove `dim_R C_{su(5)}(rho(SL(2, F_5))) == 1` (`U(1)_Y` only) with exact `Frobenius-Schur` indicators `(+1, -1)` on `(3_+, 2_-)` (`real A_5 subset SO(3)` vs `quaternionic 2.A_5 subset SU(2)`), whereas `dim_R C_{su(5)}(rho(-I)) == 12` (`su(3)_c (+) su(2)_L (+) u(1)_Y`), proving continuous complex colour requires promoting `W_5` to a spacetime unitary bundle whose central `-I` monodromy is `P`.
3. **Metallic-Mean Fundamental-Discriminant Control (`P-863(d)`):**
   - Compute fundamental field discriminants `Delta_K` of `Q(sqrt(k^2 + 4))` for `k = 1..12` (`noting k = 4 gives D_4 = 20 = 4 * 5 -> same Golden field Q(sqrt(5)), phi^3`) and verify `rho(-I)` eigenspace splits `(p+1)/2 + (p-1)/2` across odd primes `p in {3, 5, 7, 11, 13, 29}`, proving `p = 5` (`Delta_K = 5`) uniquely gives `(3, 2)`.
4. **Prime-`3` Family vs Prime-`5` Gauge Orthogonality in `248D` `E_8` (`P-863(b)`):**
   - Verify on the `240` `E_8` roots: `dim(E_6^{cent} cap E_6^{GUT}) == 16` (`12` roots + `4` Cartans = `su(3)_L (+) su(3)_R`), `dim(E_6^{cent} cap G_{422}) == 7`, `W_swap in W(E_8) cap SO(8)` has exact order `4` (`W_swap^2 != I_8, W_swap^4 == I_8`), `[A_2^{fam}, E_6^{GUT}] == 0`, `(3_{fam}, 27_{GUT})` has `81 = 3 x 27` states carrying `3` commuting copies of `16_+ subset 27_{GUT}`, and `Z_{15} ~= Z_3^{fam} x Z_5^{gauge}` `CRT` bijection holds.

## 3. Five Planted Fault Controls That Must Fail When Broken

1. **`PF8.1` (`Wrong-Chirality Odd Fock Projection`):** Projecting onto `Lambda^{odd}(W_5)` yields `+4^3` and `-6^1` instead of `-4^3` and `+6^1`.
2. **`PF8.2` (`Full-Weil Commutator With Non-Abelian SU(3)_c`):** A traceless off-diagonal generator on `3_+` commutes with `P` (`0`) but fails `[G_c, rho(S)] == 0` (`norm > 1/2`).
3. **`PF8.3` (`Bronze-Mean Prime p = 13 Control`):** `rho_{13}(-I)` gives eigenspaces `(7, 6) != (3, 2)`.
4. **`PF8.4` (`False Involution Claim W_swap^2 == I_8`):** `W_swap^2` is non-identity (`order 4 != 2`).
5. **`PF8.5` (`Conflating Generation Triplet With Colour Triplet`):** Identifying `3_{fam}` with `3_c` inside `E_6^{GUT}` produces non-vanishing `[G_{fam}, G_c]` (`> 1`).

## 4. Dependencies and Firewall Boundaries

Addresses `P-863` (`B1951`) on `origin/main` (`ff8e1ca57`). Strict `0 of 19` firewall; touches only `relays/`. Expectations committed first (`0 of 19`).
