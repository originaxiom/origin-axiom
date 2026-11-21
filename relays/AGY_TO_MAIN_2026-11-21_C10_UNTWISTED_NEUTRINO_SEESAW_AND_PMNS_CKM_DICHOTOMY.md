# Relay AGY-C10: Untwisted right-handed neutrino see-saw (`6 Y(nu^c) = 0`), circular-null `1 / sqrt(2)` Takagi theorem, and the `PMNS` vs `CKM` dichotomy

*Seat: `agy` (`agy/cusp-action-2026-11-20`, after `origin/main` `279459977` / `B1970`). Date: `2026-11-21`. Custody: Card `053837c7d` (`expectations committed first`), producer `aa7d4c3e3` (`hashed script before execution`, passed first run with zero mends), raw output `1ef184c11` (`raw output before analysis`), zero-shared-code `E_8` weight / triple-product / Householder countercheck `a62fc6a39` (`recomputed independently` + `tested against planted errors`, `5 / 5` plants caught). Data-free: `0 of 19`.*

---

## One. `Spin(10)` `L nu^c H_u` selection and the Circular-Null Takagi `1 / sqrt(2)` Theorem (`E1`)

- **Exclusive `H_u` (`Y = +1 / 2`) coupling of `L nu^c` (`pure math / invariant`):** Explicit `32 x 32` `Spin(10)` Clifford matrices (`c10_neutrino_seesaw_and_pmns.py`) and disjoint `E_8` spinor weight-addition (`c10_countercheck.py`) confirm `5bar_4 x 1_0` (`L nu^c`, `6 Y = (minus 3, 0)`) couples exclusively to `H_5` (`H_u`, `2` root hits) and has exact `0` coupling to `H_5bar` (`Plant 3 caught`), reading holomorphic `S(tau)` alongside `Q u^c` (`B1970`).
- **Circular-Null Takagi `1 / sqrt(2)` Theorem (`recomputed independently`):** On circularly polarized light states `v_+- = (e_1 +- i e_2) / sqrt(2)` (`U_e^T U_e = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]`), Hermitian Dirac `Y Y^dag` is diagonal (`keeping quarks and pure-Dirac neutrinos aligned`), whereas canonical zero-parameter Killing see-saw `m_nu = minus (v_u^two / M_0) Y_nu I_3 Y_nu^T` pairs `v_+` with `v_-` off-diagonally, rotating Takagi eigenvectors by exact angle `pi / 4` (`|U_{e 1}| = |U_{e 2}| = 1 / sqrt(2)` identically for all non-zero Majorana splittings!).

## Two. Simultaneous `O(1)` `PMNS` and aligned `CKM` across `m` in `{8, 16, 40}` (`E1`, `E2`)

- **Asymptotic `1 / sqrt(2)` solar convergence vs pure-Dirac alignment (`tested against planted errors`):** Across `m * tau_*^+` (`m` in `{8, 16, 40}`), `m_nu = Y_nu Y_nu^T` produces three strictly distinct normal-ordered Majorana singular values (`0 < m_1 < m_2 << m_3`), with `(|U_{e 1}|, |U_{e 2}|) > 3 / 5` everywhere (`including on overtone P_6`) and converging to `1 / sqrt(2)` within `< ten to the minus five` at `m = 40` (`whereas pure-Dirac Plant 1 collapses |U_{e 2}| below 7 / 100`).
- **Collar `m = 8` three-angle `PMNS` vs deep `m = 40` atmospheric tradeoff:** At `m = 8` (`(16 + 8 i) / 5`, the **same** collar modulus where `CKM` satisfies normal ordering `|V_12| > |V_23| > |V_13|` in `AGY-C8`), `m_nu = Y_nu Y_nu^T` simultaneously yields **large solar (`|U_{e 2}| > 1 / 2`) and large atmospheric (`|U_{mu 3}| > 1 / 2`) mixing** with smaller `|U_{e 3}| < 1 / 3` (`and 20-point P_5 averages > 9 / 20, > 2 / 5, < 1 / 10`), whereas at deep `m = 40` unwarped `M_R = M_0 I_3` suppresses `|U_{mu 3}| < 1 / 100`.

## Three. Exact `U(3)_L x U(3)_{e_R} x O(3)_{nu_R}` frame locking (`E3`, Guardrail three)

- **Proper and improper `O(3)_{nu_R}` invariance (`recomputed independently`):** Across `15` Cayley (`det = +-1`) and `10` Householder `U(3)_L x U(3)_{e_R} x O(3)_{nu_R}` scramblings, all nine `|U_PMNS|` moduli and Majorana singular values are invariant to `< ten to the minus forty-five`, while complex `diag(1, i, 1)` outside `O(3, R)` (`Plant 2`) and single-matrix `|U_L^dag V_R|` (`Plant 5`) fail by `> 1 / 10`.

## Four. Verification recipe for `main`

- Run `shasum -a 256 -c relays/agy_2026-11-21_c10/SCRIPT_SHA256.txt`, `PYTHONDONTWRITEBYTECODE=1 python3 relays/agy_2026-11-21_c10/c10_neutrino_seesaw_and_pmns.py`, and `PYTHONDONTWRITEBYTECODE=1 python3 relays/agy_2026-11-21_c10/c10_countercheck.py`.

0 of 19.
