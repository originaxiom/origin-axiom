# Cold-Room Zero-Trust Referee Verdict — `Card A2-LEG5-TOWER-MODULAR-BRIDGE`

- **VERDICT**: **`PASS`**
- **Discrepancies Count**: **`0`** (`125 / 125` cross-diff checks passed across `B1`–`B5`)
- **Seat Code**: `fam3-v1-high-03`
- **Branch**: `agy-002/verify`
- **Empirical Parameter Firewall**: Strictly `0 of 19` (zero empirical inputs; purely dimensionless mathematical bridge)
- **Producer Sealed Commit**: `3b22ec97c920ade12fd6ed73c0a48c1757881d26` (`3b22ec97c`)

---

## 1. Cold-Room Custody Chain & SHA-256 Manifests

All four cold-room referee files were authored, hashed, executed once, and committed BEFORE any Producer file in `relays/a2_leg5_tower_modular_bridge/` was read, listed, grepped, or imported. None of the four sealed cold-room files was modified after committing.

| Artifact | Git Commit | 16-Hex SHA-256 | Full 64-Hex SHA-256 |
| --- | --- | --- | --- |
| `referee_a2_leg5_tower_modular_bridge.py` | `765d441f9117ac84e5c6ee46e52b55ae5ae6c2eb` | `e5a376a70143a719` | `e5a376a70143a71908e8293efc491b635908e136a104b05a2b1ef17c6804e615` |
| `referee_a2_leg5_tower_modular_bridge_out.json` | `6021cd6d28f961c8d0c4657e1842990c698c3a1a` | `ede9d390a725fdb7` | `ede9d390a725fdb73d303ebe7718e860e8247ab5f5b4fee9b517097423659520` |
| `compare_referee_vs_producer.py` | post-seal commit | `d2e844cd83f9fb8c` | `d2e844cd83f9fb8c5d085083e14178b26db8fbbc6e53dbb46e9eafd17422ee6c` |
| `referee_vs_producer_diff.json` | post-seal commit | `dd63d1e9499854fa` | `dd63d1e9499854fa5aa7136b599f50980d72220e804e65b992c85d021f1cc8ca` |

Producer sealed hashes (verified against `relays/a2_leg5_tower_modular_bridge/SCRIPT_SHA256.txt` and `OUTPUT_SHA256.txt`):
- `a2_leg5_tower_modular_bridge_decisive.py`: `7f51c721fde94bba` (`7f51c721fde94bba67c102a14c7f972895ef2ef8e7847da9a633ff0514f6889d`)
- `a2_leg5_tower_modular_bridge_control.py`: `dfb519ed6c688093` (`dfb519ed6c6880931a3226af80f61a643f0bcbe905c3680f673294abbd2c322d`)
- `a2_leg5_tower_modular_bridge_out.json`: `b876876dff814ac4` (`b876876dff814ac49b0bf89d52dac5554ad8cb37fd0b5b23bb596c661c88d9e0`)
- `a2_leg5_tower_modular_bridge_stdout.txt`: `834cc3029354e3cc` (`834cc3029354e3cc5cfae0b962929660c47eafa6c3f1677ec5e97a44ffa88c56`)

---

## 2. Disjoint Algorithm Independence Matrix (Guardrail 6)

| Component | Producer Algorithm | Independent Referee Algorithm |
| --- | --- | --- |
| `Leg(5)` representation | Direct Legendre symbol `leg5_char(s)` on 6 lines of `P^1(F_5)` | `12 x 12` unsigned permutation action on `Rays(5) = (F_5^2 \ {0})/{+-1}` projected onto the 6-dim `(-1)`-eigenspace of scalar multiplication by `2` (`e_i = (\|r_i^+> - \|r_i^->)/sqrt(2)`) |
| `B1` Markoff orbits | BFS under `<L_tr, R_tr, Li_tr, Ri_tr>` | BFS under `<C_tr, sigma_tr>` (with independent equivalence cross-check) |
| `B1` `Q_6 x Leg(5)` polynomials | SymPy `.charpoly()` on `36 x 36` & `12 x 12` + `p_full // p_neu_x` + `sp.factor_list` | Exact integer `12 x 12` `H_0` and `24 x 24` real `H_1 (+) H_2` matrices from free 3-cycles, pure-integer **Faddeev-LeVerrier** trace recursion over `Z`, and exact algebraic `Z[y]` polynomial square root |
| `B1` halving trace defects `Delta_{2m}` | Full-space traces `tr(W_6^{2m})` and `tr(C W_6^{2m})` | Explicit sparse `C`-orbit sector matrices `H_0` over `Z` and `H_1` over `Z[omega]`, computing `tr(H_0^{2m}) - 4^m tr(H_1^{2m})` directly |
| `B2` chiral walk & Pauli algebra | SymPy `.charpoly()` and `.nullspace()` with normalized radicals | Pure-integer Faddeev-LeVerrier + nested-radical-free orthogonal bases over `Q(sqrt(3), sqrt(5))` |
| `B3` Siegel unit `\|g_{a,b}(tau)\|` | Bernoulli `B_2(a)` infinite product | Jacobi `theta_1` sine series + Euler pentagonal Dedekind `eta`: `\|g_{a,b}\| = exp(-pi y a^2) \|theta_1(pi(a tau + b), tau) / eta(tau)\|` (verified quasi-periodic to `< 1e-60`) |
| `B3` root-finding & 2D stabilization | Bisection for `y_odd*`; 3-point FD damped Newton (`h_n = 1e-6`) + 3-point Hessian | Illinois secant method (`tol = 1e-45`) for `y_odd*`; golden-section search (`tol = 1e-26`) + 5-point Richardson 2D Hessians (`O(h^6)`) + 121-point 2D fundamental-domain sweep |
| `B4` Weierstrass `wp(z; tau)` | Lambert series `w/(1-w)^2` + divisor-sum `E_2` | `-(theta_1''/theta_1 - (theta_1'/theta_1)^2) - (pi^2/3) E_2` via `theta_1` derivatives and Euler pentagonal `E_2 = 1 + 24 q P'/P` |
| `B4` 5-division polynomial at `omega_+` | Classical division-polynomial recurrence `psi_5 = psi_4 psi_2^2 - psi_3^3` + quadratic factorization | Direct chord-and-tangent elliptic-curve group law `x([2]P) = x([3]P)` on `y^2 = 4x^3 - 1`, followed by exact resultant `Res_u(P(u), d(4u-1)^3 - 27 u(u-1)^3) ~ 5 d^4 - 270 d^2 + 729` over `Z[u, d]` |
| `B5` planted controls | `PF1`–`PF5` (decisive + standalone `control.py` exit code 1) | `RPF1`–`RPF5` computed independently inside the cold-room referee script |

---

## 3. Module-by-Module Cross-Verification Summary (`125 / 125` PASS)

### `B1`: All-$k$ Universal Tensor-Halving, `Q_6 x Leg(5)`, & Level-30 Exact Halving
- **Orbits & Quotients**: `|O_27^{(3,3,3)}| = 72` (`|Fix(C_tr)| = 3`), `|O_27^{(3,3,12)}| = 72` (`3`), `|O_27^{(3,3,15)}| = 72` (`0`), `|O_81^{(3,3,3)}| = 648` (`3`), unique 6-pt congruence `|Q_6| = 6` (`|Fix(C_tr)| = 3`, `|M_6| = 36`, index `6` in `G_3`), and mod-9 control `|Q_8| = 8` (`|Fix(C_tr)| = 2`).
- **Exact `Q_6 x Leg(5)` Polynomials** (Faddeev-LeVerrier over `Z`, terminal `B_n = 0`):
  - `P_neu(y) = (y^2 - 20)^2 (y^2 - 8)^4`
  - `P_{2,chg}(y) = (y^2 - 8)^2 (y^2 - 6y + 4)^2 (y^2 + 6y + 4)^2`
  - `gcd = (y^2 - 8)^2`, `UNPAIRED = (y^2 - 6y + 4)^2 (y^2 + 6y + 4)^2`, `LEFTOVER = (y^2 - 20)^2 (y^2 - 8)^2` — exact match.
- **Exhaustive Character Fixed-Point Theorem**: `|G_3| = 216`, `|G_4| = 1944`; for `rho != 1` (`rho(C_tr) = omega`, `rho(sigma_tr) = -1`): `0/216` mismatches for `O_27^{(3,3,3)}` vs `Q_6` (and `0/216` for `O_27^{(3,3,12)}` vs `Q_6`), `0/1944` for `O_81^{(3,3,3)}` vs `Q_6`, `0/216` nonzero fixed points on `O_27^{(3,3,15)}` and `Q_6 x P^1(F_2)`, and `54/216` mismatches for `Q_8` (`RPF1`).
- **Halving Trace-Moment Defects**: `[W_+, W_-] = 0` on all spaces; `Delta_{2,4,6,8} = (0, -1152, -48384, -1603584)` identically on `Q_6`, `O_27^{(3,3,3)}`, `O_27^{(3,3,12)}`, and `Delta_{2,4,6} = (0, -1152, -48384)` on `O_81^{(3,3,3)}`; identically `(0, 0, 0, 0)` on `O_27^{(3,3,15)}` and Level-30 `P^1(F_2) x O_27^{(3,3,3)} x Leg(5)`.

### `B2`: Exact Chiral Walk Algebra on `Leg(5)`
- Exact symbolic proofs over `Q(sqrt(3), sqrt(5))`: `W_R = W_L^T`, `[W_L, W_R] = 0`, `[W_L, C_3] = 0`, `tau_mir W_L tau_mir = W_R`.
- Exact charpolys via Faddeev-LeVerrier: `W_{6,om} -> (x^2 - 20)(x^2 - 3x + 1)^2`, `W_L -> (x^2 - 5)(x^4 - 3x^3 + 8x^2 - 3x + 1)`, `i(W_L - W_R) -> x^2(x^4 - 21x^2 + 9)`.
- Exact Pauli & chiral pole identities: `i(W_L - W_R)|_{E_{phi^2}} = sqrt(3) phi^2 sigma_y`, `i(W_L - W_R)|_{E_{phi^-2}} = sqrt(3) phi^{-2} sigma_y`, `W_L|_{E_{phi^2}} = -phi^2 C_3^2`, and chiral poles `[1, +-i]/sqrt(2)` yield exact `I_4 = 1/5`, `I_6 = 2/45`.

### `B3`: Mirror-Lock Theorem, Siegel Map, & Zero-Parameter Interior Stabilization
- Symbolic Mirror-Lock: `|tau| = 1`, `Re(tau) = 1/2`, and `|tau - 1| = 1` map to `tau_mir`, `C_3 tau_mir C_3^-1`, `C_3^2 tau_mir C_3^-2` (all commuting with `W_{6,om}`), while `R_0` (`Re(tau) = 0`) breaks `[rho(R_0), W_{6,om}] = 0` (`Frob^2 = 24`); both cusp asymptote vectors `[1,0,1,1,1,1]` and `[0,1,0,0,0,0]` project after `rho(S)` to exact `c_-/c_+ = -sqrt(3)` (`-60 deg`).
- Quasi-periodicity of `F_Siegel(a, b; tau)` verified to `7.97e-61`; `SL(2,Z)` equivariance at `tau_0 = 3/10 + 13/10 i` verified to `T_err = 2.68e-61`, `S_err = 3.44e-61`, invariance diffs `< 2e-61`.
- Special moduli: `omega_+` (`gold_frac = 1.08e-121`, `norm2 = 0.3632875795`), `i` (`I6_gold = 11/90` to `0.0` at 60 digits, `norm2 = 0.3850301401 > omega_norm2`), `exp(i 5pi/12)` (`I6_gold = 11/90` to `0.0`), `tau_tot*(70)` (`theta = -60.0 deg`, `I6_gold = 11/90` to `3.89e-62`), `y_odd* = 1.29456081040442...` (`I6_gold = 1/10` to `1.94e-62`, diff vs Producer `2.09e-14`).
- Zero-parameter 2D global interior minima:
  - `tau_{I4}^*` on `x = 1/2`: `y* = 2.272675592858818...` (`I4* = 0.171948124413676...`, `I4_xx = +1.3923641e-5 > 0`, `I4_yy = +0.041324481 > 0`, `|I4_xy| = 2.78e-43`; `x = 0` saddle has `I4_xx = -1.3915984e-5 < 0`; cusp `15i` gives `0.19871343`).
  - `tau_{I6}^*` on `x = 0`: `y* = 2.305223081019497...` (`I6* = 0.0304118993915641...`, `I6_xx = +1.1985682e-5 > 0`, `I6_yy = +0.016412497 > 0`, `|I6_xy| = 1.57e-42`; `x = 1/2` saddle has `I6_xx = -1.1955586e-5 < 0`; cusp `15i` gives `0.039611529`).

### `B4`: Weight-2 Holomorphic Weierstrass Map & Exact 5-Division Polynomial Proofs
- Chord-and-tangent `x([2]P) = x([3]P)` yields `5x^{12} - 95x^9 - 15x^6 + 25x^3 - 1 = 0`; resultant in `d = (x - x([2]P))^3` yields `5d^4 - 270d^2 + 729 = 0`, proving `u_s / u_c = phi^{-1}`, `u_c^2 + u_s^2 = 3 * 5^{1/3}`, exact `0 : 0 : 4/5 : 1/5` norm partition, chiral pole (`theta = 45 deg, alpha = -90 deg, I_4 = 1/5, I_6 = 2/45`), and `V_wp(omega_+) = (27/8) 5^{1/3} |g_3(omega_+)|^{2/3} = 505.937996877952...` (relative residual `3.15e-61`, matching Producer `505.937996878`).
- Lemniscate `tau = i`: probabilities match `((5+sqrt(5))/24, (5+sqrt(5))/24, (5-sqrt(5))/24, 1/12, 1/12, (5-sqrt(5))/24)` to `3.11e-61`, `I_4 = 2/9` (`1.36e-61`), `I_6 = 17/288` (`8.26e-62`), `V_wp(i) = 507.335345879711...` (matching Producer `507.33534588`).
- Weight-2 equivariance at `tau_0 = 3/10 + 13/10 i`: `T_err = 1.06e-59`, `S_err = 1.13e-59`, `V_wp` invariance `< 4.55e-61`; unit-arc `alpha = -90.0 deg` locked to `0.0`; `Re(tau) = 1/2` flow matches Producer at `tau_tot*(70)` (`alpha = -165.8815194 deg`, `I4_gold = 0.2954700573`, `I6_gold = 0.1184558858`) and `1/2 + 5i` (`I4_gold = 0.2999076842`) to all 10 printed Producer digits.

### `B5`: 5/5 Planted Controls & Hygiene / Custody Audits
- All 5 planted controls (`RPF1`..`RPF5`) independently triggered (`5 / 5`), matching Producer `PF1`..`PF5`.
- Producer standalone control script (`a2_leg5_tower_modular_bridge_control.py`) executed read-only and exited with code `1` and empty stderr as required.
- AST/JSON hygiene: `0` float literals, `0` complex literals, `0` float/complex casts, `0` forbidden imports, and `0` JSON floats across both Producer and Referee scripts/outputs.
- Repository custody: `384 / 384` `*SHA256*.txt` manifests (`396 / 396` file entries) across `relays/` verified with `0` missing and `0` mismatches; `0` non-relay edits relative to `origin/main`.

---

## 4. Documented Nuances (Non-Discrepancies)

1. **Sealed Referee `B3.special_moduli.checks` precision-switch artifact**: Inside `run_module_b3()` of the sealed referee script, `I6_gold` and its exact 60-digit residuals were computed at `mp.mp.dps = 60` (`I6_gold_minus_11_90 = 0.0`, `0.0`, `3.89e-62`; `I6_gold_minus_1_10 = 1.94e-62`). Before building the final `checks` dict, `mp.mp.dps` was lowered to `30` for the 121-point fundamental-domain sweep without restoring `dps = 60`, so `mp.mpf(11)/90` in the boolean predicate rounded to 30 digits (`~1e-31 > 1e-40`), flipping those four summary booleans to `false` even though the sealed 60-digit residuals in the same JSON are `< 1e-61`. Under zero-overwrite custody, the sealed referee files were left untouched and the 60-digit residuals were verified directly in `compare_referee_vs_producer.py`.
2. **Producer Newton FD bias on `y_star`**: Producer's `I4_min.y_star = 2.2726755928594` and `I6_min.y_star = 2.3052230810201` differ from Referee's `tol = 1e-26` golden-section values (`2.272675592858818...` and `2.305223081019497...`) by `5.82e-13` and `6.03e-13`, respectively — consistent with `O(h^2)` derivative truncation from Producer's `h_n = 1e-6` central-difference Newton step, well inside the `< 1e-10` threshold.
3. **Producer 8-digit display rounding**: Producer serializes `B3` Hessian entries and `cusp_15i` values to 8 significant digits; Referee's 40-digit values round identically to every printed Producer digit.
4. **PF4/RPF4 residual norm convention**: Producer reports relative `L_inf` residual (`1.52499`) while Referee reports absolute `L_2` residual (`47.87269477...`); both decisively confirm weight-2 `S`-equivariance violation when `tau^2` is dropped.
