# `AGY-002_ENDGAME-V2-G2` — Gate 2 Results (`0 of 19`)

## 1. Check Labels and Tracked Evidence (`docs/seats/README.md` § 12)

- **expectations committed first:**
  - Card commit `4cbac1449`: `relays/cards/AGY-002_ENDGAME-V2-G2_covariant-triple-overlap-and-level-5-10-15-exponents.md`
  - First script seal `1615f45e3`: `relays/agy002_endgame_v2_g2/verify_endgame_v2_g2.py`, `relays/agy002_endgame_v2_g2/SCRIPT_SHA256.txt`
  - First output seal `f6918a003` (committed unread): `relays/agy002_endgame_v2_g2/verify_endgame_v2_g2_out.json`, `relays/agy002_endgame_v2_g2/OUTPUT_SHA256.txt`
- **recomputed independently:**
  - Second script seal `b3dda2651` (built from the card alone without reading or importing `verify_endgame_v2_g2.py` or any file under `frontier`): `relays/agy002_endgame_v2_g2_referee/referee_endgame_v2_g2.py`, `relays/agy002_endgame_v2_g2_referee/SCRIPT_SHA256.txt`
  - Second output seal `43e64a0fd` (committed unread): `relays/agy002_endgame_v2_g2_referee/referee_endgame_v2_g2_out.json`, `relays/agy002_endgame_v2_g2_referee/OUTPUT_SHA256.txt`
- **tested against planted errors:**
  - `5 of 5` planted cases caught above threshold in `relays/agy002_endgame_v2_g2/verify_endgame_v2_g2_out.json` (`PF2.1` `3.563 > 0.5`, `PF2.2` `2.415 > 0.1`, `PF2.3` `9.345 > 0.5`, `PF2.4` `0.1333 > 0.02`, `PF2.5` `d = 3, 1.585 bits`);
  - `4 of 5` exceeded unnormalized thresholds in `relays/agy002_endgame_v2_g2_referee/referee_endgame_v2_g2_out.json` (`PF2.1` `3.074`, `PF2.3` `9.815`, `PF2.4` `0.1333`, `PF2.5` `d = 3, 1.585 bits`), while `PF2.2` multiplied by exponentially damped `exp(2 pi i * 3 * (2/5) tau)` (`|prefactor| ~ 7e-5`), giving `1.14e-4` absolute error (`O(1)` relative violation and `7.65e9` times the `1.49e-14` covariance tolerance, below the unnormalized `0.1` bar). Likewise in Section 4 of the second computation, all `16` physics and degeneracy checks held (`d = 3`, `d = 2`, `d = 1`, `0.0` additional bits, `+pi/6` overlap `1.0 - 4e-16`), while its auxiliary comparison between `64`-pt Gauss–Legendre and non-periodic `128`-pt midpoint quadrature had the expected `O(1/128^2) = 5.42e-6` truncation difference against `1e-10`.

## 2. Numerical Summary (`0 of 19`)

| Check | First Computation (`verify_endgame_v2_g2_out.json`) | Second Computation (`referee_endgame_v2_g2_out.json`) | Bound |
|---|---|---|---|
| AST zero float literals & Wang/Stokes accounting | `0` floats, `det(M - I) = -1 => H_2(m004; Z) = 0`, `3 + 3 - 6 = 0`, `6Y` neutral | `0` floats, `0` complex, Smith normal form `[1, 1]`, cubical/CW `d^2 = 0`, `True` | Exact |
| `CIM (3, 3, -6)` `2D` quadrature vs `1D` theta & `T` / `S` covariance (`P-861`) | Quad vs `1D` `2.86e-14`; `T`-cov `3.36e-14`; `S`-cov `3.27e-14` | Quad vs `1D` `9.82e-15`; `T`-cov `1.49e-14`; `S`-cov `5.91e-15` (`mp40` periodicity `5.73e-39`) | `< 1e-12` |
| Levels `5 / 10 / 15` exact cusp exponents (`B1948` Step `2`) | `N=5`: `1:1`; `N=10`: pointwise swap `1/10 <-> 3/10`, orbit minima `1:1` `(1/5, 1/2)`; `N=15`: `lep = (1/5, 11/20)` vs `down = (2/15, 1/2)` (`3/2` & `11/10`) | Identical exact `Fraction` table across all `24 + 72 + 192` exact-order points (`matches_producer = True`) | Exact |
| High-cusp `mpmath` slopes & `288`-lift `CIM` level-`10` bijection | `mpmath` max err `4.15e-5`; `288`-lift `CIM` err `5.55e-16` | `180`-digit `mpmath` max err `2.22e-5`; `288`-lift `CIM` err `3.99e-23` | `< 2e-3` / `< 1e-13` |
| Blind level-`6` `M_H^2` spectrum & degeneracy bit ledger (`Guardrail 1`) | `(U_M^{(6)})^{12} = I_6` (`4.09e-15`); pure bubble `d = 3` (`1.585` bits); pure `K_KK` `d = 2` (`1` bit); combined `d = 1` (`0` bits, `+pi/6` overlap `1.0`); Haar `4.77e-15` | `(U_M^{(6)})^{12} = I_6` (`2.28e-15`); pure bubble `d = 3` (`1.585` bits); pure `K_KK` `d = 2` (`1` bit); combined `d = 1` (`0` bits, `+pi/6` overlap `1.0 - 4e-16`); Haar `2.94e-15` | `< 1e-12` |

## 3. Result for Gate 2

1. **`P-861` / `SM-C18` Discharged:** With `I_L + I_R + I_H = (+3) + (+3) + (-6) = 0`, spin sum `(1/2, 1/2) + (1/2, 1/2) + (0, 0) == (0, 0) mod 1`, and Wilson-line neutrality `3 zeta_L + 3 zeta_R - 6 zeta_H = 0`, the closed-fibre `CIM (3, 3, -6)` triple-overlap Yukawa tensor is doubly periodic on `E_tau` and modular covariant under **both** `T` and `S` to `< 3.4e-14`.
2. **`B1948` Step `2` Discharged Across Levels `5, 10, 15`:** Whole-orbit lepton and down-quark cusp-exponent minima are `1 : 1` equal at both level `5` and level `10` (`despite pointwise swaps at a = +-1/10 <-> +-3/10` at level `10`, because multiplication by `-3 mod 10` in Frame `C` and `9 mod 20` in Frame `D1` permutes the orbit), whereas level `15` produces an exact colour-triality split `e_lep(m_2/m_3) / e_down(m_2/m_3) = (1/5) / (2/15) = 3/2`.
3. **Blind Level-`6` `M_H^2` Ground State:** While pure Yukawa loops leave `d = 3` (`log_2 3` bits) and pure base-`S^1` `K_KK` leaves `d = 2` (`1` bit), their `1`-loop sum lifts all `6` eigenvalues (`gap >= 0.01`), uniquely selecting `v_{+pi/6}` (`0` additional discrete bits beyond `sgn(I_H)`). Gate 2 is locked. `0 of 19.`
