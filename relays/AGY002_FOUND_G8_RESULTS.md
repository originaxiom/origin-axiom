# `AGY-002_FOUND-G8` — Gate 8 Results (`P-863` / `B1951` Complete Resolution, `0 of 19`)

## 1. Check Labels and Tracked Evidence (`docs/seats/README.md` § 12)

- **expectations committed first:**
  - Card commit `84cbee4e7`: `relays/cards/AGY-002_FOUND-G8_p863-clifford-fock-weil-commutant-metallic-primes-and-e8-orthogonality.md`
  - First script seal `19441c260` & unread output `5cca7fa26`: `relays/agy002_found_g8/verify_found_g8.py`, `relays/agy002_found_g8/verify_found_g8_out.json`
  - Character-sign & orthogonal-involution erratum `64eea46d0` & unread output `4ef9ddbba` (`preserving 19441c260..5cca7fa26 untouched`): `relays/cards/AGY-002_FOUND-G8-ERRATUM_weil-character-and-orthogonal-involution.md`, `relays/agy002_found_g8_fixed/verify_found_g8_fixed.py`, `relays/agy002_found_g8_fixed/verify_found_g8_fixed_out.json`
- **recomputed independently:**
  - Cold-room second script seal `7dea11ada` (`built over exact QQ(zeta_5) and full 248D integer Frenkel-Kac e_8 Lie brackets from the card + erratum alone without reading verify_found_g8*.py`) & unread output `fa868eda9`: `relays/agy002_found_g8_referee/referee_found_g8.py`, `relays/agy002_found_g8_referee/referee_found_g8_out.json`
- **tested against planted errors:**
  - `5 of 5` planted cases caught in both `4ef9ddbba` and `fa868eda9` (`PF8.1` odd Fock projection flips `+6^1, -4^3` to `-6^1, +4^3`; `PF8.2` off-diagonal `SU(3)_c` generator commutes with `P` to `0` while `||[G_c, rho(S)]||_F > 1/2`; `PF8.3` bronze-mean `p = 13` gives `(7, 6) != (3, 2)`; `PF8.4` non-orthogonal `(0 4 1 3)(2 5)` has order `4 != 2` whereas `4` orthogonal root reflections have exact order `2`; `PF8.5` conflating `3_{fam}` with `3_c` inside `E_6^{GUT}` breaks `[G_{fam}, G_c] = 0`).

## 2. Mask-Safe Rational Verification Summary (`0 of 19`)

| Check | First Computation (`4ef9ddbba`) | Cold-Room Second Computation (`fa868eda9`) | Sealed Rational Bar |
|---|---|---|---|
| `AST` source lock & `SHA-256` custody | `0` float literals, `0` complex literals, `0` repo imports | `0` float literals, `0` complex literals, `4 / 4` prior + self `SCRIPT_SHA256` matched | Exact (`0` mismatches) |
| `P-863(a)` `CAR` / `Cl(10)` derivation of `Postulate D` | `|SL(2, F_5)| = 120`, `Cl(10)` span `1024`, `Tr(6Y) = 0`, `Lambda^{even}` `[-4^3, -3^2, 0, +1^6, +2^3, +6]`, `Lambda^1` `[-2^3, +3^2]` | Exact `QQ(zeta_5)` `120`-homomorphism, `Jordan-Wigner` `CAR`, `1024` `Cl(10)` rank, `Haar` `< (1/10)^12`, exact `16` & `5` spectra | Exact integers |
| `P-863(c)` `su(5)` commutant & `Frobenius-Schur` | `dim C_{su(5)}(SL(2, F_5)) = 1`, `dim C_{su(5)}(P) = 12`, `FS(3_+, 2_-) = (+1, -1)` | Exact `QQ(zeta_5)` `DomainMatrix` `(1, 12)`, `FS = (+1, -1)`, explicit `SO(3, R)` symmetric vs `J_-` symplectic forms | Exact `(1, 12)` & `(+1, -1)` |
| `P-863(d)` metallic discriminants `k = 1..12` | `Delta_K = 5` unique odd prime giving `(3, 2)` (`k = 4, 11` give `phi^3, phi^5` in same `Q(sqrt(5))`) | Exact `(D_k, Delta_K)` table across `k = 1..12` & rival primes `p in {3, 5, 7, 11, 13, 17, 29, 37, 53}`: `p = 5` unique | Exact `{5}` |
| `P-863(b)` Prime-`3` family vs Prime-`5` gauge in `248D` `E_8` | `dim(E_6^{cent} cap E_6^{GUT}) = 16`, `cap G_{422} = 7`, `order(W_inv) = 2`, `[A_2^{fam}, E_6^{GUT}] = 0`, `162 = 2 x (3 x 27)`, `CRT` `Z_{15} ~= Z_3 x Z_5` | Full `248D` integer `Frenkel-Kac` `e_8` brackets: `624 / 624` `[A_2^{fam}, E_6^{GUT}] = 0`, `16D` & `7D` intersections, `order(W_inv) = 2` vs `order(W_{4cyc}) = 4` | Exact (`0` clash) |

## 3. Theorems Locked in Gate 8 (`Resolving P-863 Q1(a)-(d)`)

1. **`CAR` / `Clifford` Reduction of `Postulate D` (`P-863(a)`):** Canonical fermionic quantization `{c_a, c_b^dag} = delta_{ab}` of the `5`-dimensional Level-`5` `Weil` space `W_5 = L^2(F_5)` generates `Cl(10, C) ~= End(Lambda^*(W_5))` (`32 = 16_+ (+) 16_-`), where fermion-number parity `(-1)^F` isolates `Lambda^{even}(W_5) = 16_+` with exact `1`-generation `6Y` charges (`zero normal-ordering ambiguity since Tr(6Y) = 0`) and `Lambda^1(W_5) = 3_{-2} (+) 2_{+3}`.
2. **Continuous-Colour Bundle Condition (`P-863(c)`):** Full `rho(SL(2, F_5))` has `Frobenius-Schur` indicators `(+1, -1)` (`real A_5 subset SO(3)` on `3_+` vs `quaternionic 2.A_5 subset SU(2)` on `2_-`) and `1`-dimensional commutant `u(1)_Y` in `su(5)`, whereas the centre `rho(-I) = P` has `12`-dimensional commutant `su(3)_c (+) su(2)_L (+) u(1)_Y`; thus continuous complex colour arises specifically from a spacetime `SU(5)`/`Spin(10)`/`E_6` bundle whose central `-I` monodromy is `P`.
3. **Unique Metallic Field & Prime-`3` / Prime-`5` Orthogonality (`P-863(b, d)`):** Among metallic fields `Q(sqrt(k^2 + 4))`, `Q(sqrt(5))` (`Delta_K = 5`) uniquely yields `(3, 2)`. Embedding Prime `5` (`Weil 3_c + 2_w`) inside `E_6^{GUT}` and Prime `3` (`m004` `Z[zeta_6]` discriminant `-3` + `CIM` `H^0(E, L^3)`) on the commuting `A_2^{fam} = C_{E_8}(E_6^{GUT})` in `248D` `E_8` delivers `3` chiral generations with `[A_2^{fam}, E_6^{GUT}] = 0` (`zero clash with the Weil colour 3`), while `4` orthogonal root reflections give an exact order-`2` `W(E_8) cap SO(8)` involution between `E_6^{cent}` and `E_6^{GUT}`. Gate 8 is locked. `0 of 19.`
