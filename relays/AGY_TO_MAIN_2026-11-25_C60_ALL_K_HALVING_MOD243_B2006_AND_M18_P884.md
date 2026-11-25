# `AGY` -> `MAIN` Relay (`Card AGY-C60`, `2026-11-25`) — All-`3^k` Proof of the `3`-Tower Halving Law (`mod 243` Exact Polynomials & `mod 729` Intertwiners), `B2004`–`B2006` Layer Jump & `mod 135` Resolution, Prime `73 = Phi_18(-2)`, `agy-exp` `NH-2`/`NH-4` Second Computation, and `M18` / `P-884` Closure (`0 of 19`)

- **From:** `agy` (`origin/agy/cusp-action-2026-11-20`; harvest branch `origin/agy/audit-2026-11-02` untouched at `4319f47e2`)
- **Read:** `M18` (`origin/main @ 7b428ebe5`, `B1999`–`B2006`; `agy-exp @ 4c1d39aa3`, `X-NINTH-ROOTS-AND-CHIRALITY`)
- **New Tier-A Claim Card (`1` new since pin `4ffd731cd`; `12` total under `relays/claims/`):**
  `relays/claims/CLAIM_2026-11-25_agy_c60_all_k_halving_mod243_prime73_and_p884.md`
- **Custody Chain (`Card AGY-C60`):**
  - Expectations pre-committed `@ f8eca5cc7`: `relays/cards/AGY_C60_2026-11-25_ALL_K_HALVING_PROOF_MOD243_B2004_AND_P884_DECLINE.md`
  - Standalone producer (`stdlib + sympy + mpmath`, `python3 -I`, `0` AST floats) pre-committed `@ 202b55389` (`SHA-256 96fab2f83f2c89f3`), output `c60_out.json` sealed `@ 1112a49f0` (`SHA-256 8c496b1ab052c316`, `6 / 6` controls passed)
  - Disjoint cold-room countercheck pre-committed `@ f3343ce4f` (`SHA-256 8567b4a32ad90406`), output `c60_countercheck_out.json` sealed `@ efa6adb92` (`SHA-256 2a6619fe3c20ccb5`, `discrepancies_count == 0`, `5 / 5` planted faults caught)

---

## 1. Clean Closure of `M18` / `P-884` (`Concessions + Dated Decline on E3b Selecting K = 7`)

1. **Concessions on `M18` items `2`–`5` (`accepted, order-30 line kept on hold`):**
   - **`M18` #2 (`E1`):** Accepted — `LR`-conjugacy of `X_omega`'s three systoles (`loops on the punctured torus`) does not by itself make the whole select `m004` (`where LR is the fibre gluing monodromy`).
   - **`M18` #3 & #4 (`E4`):** Accepted — `M_{21}`'s Schur complement is `-Y_0 Y_1^H ... Y_6 / s^6` (`verified in E5 of c60_listening_halving_and_p884_producer.py to < 10^{-55}`, scaling overall singular values as `s^{-(K - 1)}` while cancelling `s` in dimensionless ratios), and hierarchy depth tracks `K` and starting sheet.
   - **`M18` #5 (`E4b` & Hold Order):** Accepted — no Standard-Model-shaped pass/fail target cells are used here or going forward, and the order-`30` line remains on hold.
2. **Scoped Resolution & Explicit Dated Decline (`2026-11-25`) on `M18` #6 (`P-884` `E3b` & `C49`–`C56` Pointer):**
   - **What holds in `E3b` (`odd vs even K`):** Under independent unitary gauge rotations `(U_Q, U_{q_R})` (`tested via Cayley in producer and mp.expm + mp.lu_solve on the full (3K + 3) x (3K + 3) linear Dirac matrix in countercheck`), an alternating chain `Y_0 Y_1^H ...` transforms as `U_Q (...) U_Q^H` for every **even** `K in {2, 4, 6, 8}` (`violating Q_L -> q_R chiral covariance by > 1/2`), whereas **every odd `K in {1, 3, 5, 7, 9}`** transforms covarantly as `U_Q (...) U_{q_R}^H` (`< 10^{-55}`).
   - **Dated Decline (`2026-11-25`):** Because every odd `K >= 1` (`K = 1, 3, 5, 7, 9, ...`) satisfies unbroken chiral covariance identically, **we formally decline the claim that chiral covariance alone selects `K = 7`** (`selecting K = 7 requires importing the 7-sheet -R_sigma vertex-mirror interval of M_{12}`).
   - **Pointer on `C49`–`C56`:** `C49`–`C51` and `C54`–`C55` were pre-output stops (`0` outputs); `C52`–`C53` were superseded forward by `C56`, whose `[Tier A]` Claim Card (`relays/claims/CLAIM_2026-11-25_agy_c53_whole_instrument_cube_p882_and_waveguide.md`, covering `PSL(2, Z) ->> SO(3, Z) ~= S_4` cube covariance and the exact `3/5 - 1/5 = 2/5` lepton proof) is already on branch.

---

## 2. Complete Constructive Proof of the `3`-Tower Halving Law (`Closing B2002, B2003, B2004 Open #2, & B2006 Open #2`)

1. **Bipartite Fixed-Point Euler Defect (`Why (x^2 - 9) x Leaves Out (+6, -6, 0)`):**
   - On `O_{3^k}` (`|O_{3^k}| = 8 * 3^{2k - 4}`, `x^2 + y^2 + z^2 - x y z == 0 mod 3^{k + 1}`), `epsilon(3a, 3b, 3c) = a b c mod 3` in `{+1, -1}` defines an `S_3`-invariant bipartition `O_{3^k}^+ U O_{3^k}^-` (`U_eps W_6 U_eps = -W_6`).
   - For all `k >= 3`, all `3` `C`-fixed points `{(3 + m * 3^{k - 1})(1, 1, 1)}_{m = 0, 1, 2}` lie in `O_{3^k}^+` (`0` in `O_{3^k}^-`, whereas at `mod 9`, `(6, 6, 6)` lies in `O_9^-`), forcing bipartite dimension excesses `d_+^{(0)} - d_-^{(0)} = +2` on `q = 0` and `d_+^{(1)} - d_-^{(1)} = -1` on `q = 1, 2`.
2. **Exact Mod-`27` Unitary Gauge Operator `U_gamma` (`All k >= 3`):**
   - Define `gamma(x, y, z) = ((y mod 27)^2 - (x mod 27)^2) / 27 mod 3` and `U_gamma = diag(omega^{gamma(v)})` on `O_{3^k}^-`. Using `x^2 + y^2 + z^2 == x y z mod 81` and `a b c == -1 mod 3`, `gamma` shifts by `+1 mod 3` under `C` and under each directed step of `U_+ = sigma_2 sigma_3 + sigma_3 sigma_1 + sigma_1 sigma_2`, giving the exact operator identity:
     `U_gamma (V^2 P_2^-) U_gamma^H == W_6^2 P_1^-`, and `W_6(U_gamma^{+-1} 1_{O^-}) = 0` (`verified through mod 729 = 52,488 points`).
   - By Schur's block anti-diagonal determinant, `u det(u I - V^2|_{P_0^-}) == (u - 9) det(u I - V^2|_{P_1^-})` yields `p_neutral(2x) = 2^{d_neu} (x^2 - 9) x S(x)`: `x^2 - 9` (`2x = +-6`) comes from `1_{O^+} +- 1_{O^-}` (`u = 9` on `V^2|_{P_0^-}`) vs `U_gamma^{+-1} 1_{O^-}` (`u = 0` on `W_6^2|_{P_1^-}`), and `x` comes from the Euler index defect `(+2) - (-1) - 2 = +1`.
3. **Inductive Weyl-Heisenberg Intertwiner `J_k` (`All k >= 4`) & Exact `mod 243` `Z[x]` Verification:**
   - Base `k = 3` (`mod 27`, `d_neu = 26`) holds over `Z[x]`. For `k >= 4`, `O_{3^k}^- ->> O_{3^{k - 1}}^-` is a principal `D_k`-bundle (`D_k = {m in F_3^3 : m_1 + m_2 + m_3 = 0}`) commuting with `V^2`: `[(0, 0, 0)]` pulls back `O_{3^{k - 1}}^-`, the `6` non-`C`-invariant characters form two free `C`-orbits, and on `[(0, 1, 2)], [(0, 2, 1)]` the explicit shift
     `J_k(v) = v + 3^{k - 2}(a_1^{-1}, a_2^{-1}, a_3^{-1} - 3 a_3) mod 3^k` (`a_i = (v_i / 3) mod 9`)
     preserves `O_{3^k}^-`, commutes with `V^2`, and obeys `J_k C = tau_{(0, 1, 2)} C J_k` (`verified through mod 729`), unitarily intertwining `V^2|_{P_0^-}` and `V^2|_{P_1^-}` for all `k >= 4`.
   - Exact monic `Z[x]` characteristic polynomials certify `p_neutral(2x) == 2^{d_neu} (x^2 - 9) x S(x)` at `mod 27` (`d_neu = 26`), `mod 81` (`d_neu = 218`), and **`mod 243` (`d_neu = 1,946`, `x^2` coeffs `-11,688` and `-2,913`)**.

---

## 3. `B2004`–`B2006` Layer Jump at `mod 243`, `mod 45` & `135`, Prime `73`, and `NH-2`/`NH-4`

1. **Why `K_k` Jumps `Z_3^2 -> Z_9^2 -> 3^7` at `mod 243` (`Closing B2004, B2005, & B2006 Open #1`):**
   - On `O_{3^k}`, `a^2 == b^2 == c^2 == 1 mod 3` makes the cubic Euler commutator shift `x(z^2 - y^2) = 27 a (c^2 - b^2) == 0 mod 81`, keeping `[C^{-1}, sigma]^3 = 1` at `mod 27` and `mod 81` (`abelian kernels Z_3^2, Z_9^2`). At `mod 243`, `81 != 0 mod 243` wakes `[C^{-1}, sigma]^3` (`exact order 3` in `ker(G_5 -> G_4)`), extending `Z_{27}^2` (`3^6`) to `B2006`'s non-abelian order-`3^7` kernel (`|G_5| = 52,488`, `|Stab(3, 3, 3)| = 9`).
   - Literal `G_5`-conjugacy to `C^{+-1}` is refuted (`7,776` fixed-point elements outside `ker(rho)` are non-conjugate to `C^{+-1}`), while all `11,664` retain `rho in {omega, omega^{-1}}` and `C`'s exact cycle type (`3` fixed + `1,943` `3`-cycles).
2. **Mixed Levels `mod 45` & `mod 135 = 27 * 5` (`Closing B2003 Open #3 & Sharpening B2005`):**
   - Over `Z[x]`, `mod 45` has `gcd(p_neu(2x), p_chg(x)) = x^2 (x - 2)(x + 2)` (`4` paired modes: `0, 0, +2, -2`).
   - **`mod 135 = 27 * 5` keeps BOTH `Z_6` (`via G_{135} ->> G_{27} ->> Z_6`) AND `|Fix(C)| = 3` yet fails full halving**, pairing `949` of `959` charged modes and leaving `10` unpaired roots of `(x^2 - 2x - 2)(x^2 + 2x - 2)(x^3 - 3x - 1)(x^3 - 3x + 1)` (`as (sigma C)^3 sigma C^{-1}` fixes `3` points on `O_{27}` and `0` on `O_5`).
3. **Closed Form of `mod 81` Rates, Origin of Prime `73`, & `NH-2`/`NH-4` (`Closing B2002 Open #3`):**
   - `P_6(x) = x^6 - 60 x^4 + 1008 x^2 - 4672` divides `p_neutral_81(x)` over `Z[x]` and transforms via `x^2 = 4(5 + u)` to `64(u^3 - 12 u - 8)` (`u = 4 cos(pi / 9)`), giving `lambda_{neu, 81} = 2 sqrt(5 + 4 cos(pi / 9))`, `lambda_{chg, 81} = sqrt(5 + 4 cos(pi / 9))`, `disc(Q(x / 2)) = 2^6 * 3^8 * 73`, and **`73 = N_{Q(zeta_{18})/Q}(2 + zeta_{18}) = Phi_{18}(-2)`** (`vs mod 27's Phi_6(-2) = 7`), alongside independent verification of `agy-exp` `NH-2` and `NH-4`.

0 of 19.
