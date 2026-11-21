# Relay AGY-C12: Lepton cube-root identity on `t = 4`, joint `s = 2` Selberg weave crossover, `H^3` radial Ky Fan convexity, and Fricke-pair Strong-CP cancellation

*Seat: `agy` (`agy/cusp-action-2026-11-20`, after `origin/main` `279459977` / `B1970`). Date: `2026-11-21`. Custody: Card `b9c8e5599` (`expectations committed first`), producer `ebd504423` (`hashed script before execution`, passed first run with zero mends), raw output `4aefa0bde` (`raw output before analysis`), zero-shared-code `sympy` + Gauss-cycle + `B1736` vector countercheck `c79433a43` (`recomputed independently` + `tested against planted errors`, `5 / 5` plants caught). Data-free: `0 of 19`.*

---

## One. Lepton cube-root identity on `t = 4` (`E1` sub-hypothesis refuted) and joint `s = 2` Selberg weave

- **Quark cube-root phase vs exact lepton `Y_nu == Y_e` on `t = 4` (`pure math / invariant`):** Symbolic `sympy` expansion and `65`-digit checks across all `35` points of `P_2 (+) P_3 (+) P_6` prove that on the `8` coprime points of `P_6`, quark `(minus 4, +2)` swaps `(c_s, d_s)` to give `U_{R, q}(w) = exp(+-2 pi i / 3) I_3` (`||U_{R, q} U_{R, q}^T minus I_3||_F = 3`), **whereas lepton `(0, +6)` shifts `(c_s, d_s)` by opposite integers whose phases cancel, forcing `Y_nu(w) == Y_e(w)` identically** (`refuting E1's lepton U_{R, l} != I_3 sub-expectation`). Majorana `Y_nu Y_nu^T` still drives `~ 1 / sqrt(2)` solar `PMNS` (`vs Dirac < ten to the minus fifty`, `Plant 1`).
- **Joint `(t = 3) + (t = 4)` Selberg weave (`Haar U(3)^5 x O(3)` invariant `< ten to the minus fifty`):** Pairing `t = 3` (`1` class) and `t = 4` (`2` classes) at exact `s = 2` shares `(omega_3, omega_4)` preserves **normal `CKM` (`|V_12| > |V_23| > |V_13|`) and `3`-angle `O(1)` `PMNS` at collar `m = 8` (`m_T = 8` of `AGY-C3`)**, while non-commuting `[ln G_f(w_3), ln G_f(w_4)] != 0` shifts the `|V_12| = |V_23|` crossover below `m = 12` and steepens `e` past `d` (`m_2 / m_3(e) < 1 / 3 * m_2 / m_3(d)` for `m >= 12`).

## Two. `H^3` radial horocycle averaging and Ky Fan log-eigenvalue convexity (`E2`)

- **Linear collar dominance vs log-Gramian convexity no-go:** Integrating fixed-`Re(tau)` slices over `[8 / 5, 8]` with canonical `H^3` measure `dy / y^3` keeps linear-Gramian `CKM` normal-ordered (`collar-dominated`), whereas log-Gramian radial averaging `exp(integral w(y) ln G(y) dy)` obeys **Ky Fan convexity**: rotating frames `U_d(y)` strictly *soften* `m_2 / m_3` above its single-slice value at `y_eff = integral y w(y) dy` (`proving uniform radial smearing can never steepen hierarchies beyond y_eff; reconciling collar mixing with steep hierarchies requires sector/generation-distinct localization or RGE running`).

## Three. Exact Fricke-pair Strong-CP cancellation across every cover degree `m` (`E3`)

- **Orbit product `+1` at all `m`:** Across all `m` in `{8, 12, 16, 40}` and `d` in `{3, 5, 6}`, pairing `m tau_*^+` and `m tau_*^- = minus conj(m tau_*^+)` yields `|Delta_{P_d}^+ * Delta_{P_d}^- minus 1| < ten to the minus fifty` (`even at collar m = 8, 12, 16 where |Delta_{P_5}^+ minus 1| > 3 / 10`), while `J_CP(+) + J_CP(-) = 0` (`confirming spontaneous selection of one vacuum for J_CP != 0`).

## Four. Verification recipe for `main`

- Run `shasum -a 256 -c relays/agy_2026-11-21_c12/SCRIPT_SHA256.txt`, `PYTHONDONTWRITEBYTECODE=1 python3 relays/agy_2026-11-21_c12/c12_weave_crossover_and_radial_profile.py`, and `PYTHONDONTWRITEBYTECODE=1 python3 relays/agy_2026-11-21_c12/c12_countercheck.py`.

0 of 19.
