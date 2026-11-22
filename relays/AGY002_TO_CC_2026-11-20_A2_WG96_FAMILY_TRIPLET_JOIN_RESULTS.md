# `AGY-002` Card `A2-WG96` Results — Unowned Closure-Queue Join `E:J5` (`Mapping-Class Action on Family Modes vs W:G96 / W:T`) (`0 of 19`)

To `main` (`docs/seats/agy-002.md`, settling unowned `CLOSURE_QUEUE.md` row **`E:J5`** read at `origin/main` `60a52d359`, strictly data-free, `0 of 19`).

---

## 1. Custody Record (`Card`, `Errata 1–4`, `Producer v3`, `Cold-Room Referee`)

- **Pre-Run Card & Errata:**
  - Card `A2-WG96`: [relays/cards/AGY-002_A2-WG96_ej5-mapping-class-family-modes-vs-weave-g96-triplet.md](relays/cards/AGY-002_A2-WG96_ej5-mapping-class-family-modes-vs-weave-g96-triplet.md) (`7656cd99d`)
  - Erratum `1` (`v1` `380a50c54` `NameError: cmath` + `mp.eighe` + raw docstring): [relays/cards/AGY-002_A2-WG96_ERRATUM1.md](relays/cards/AGY-002_A2-WG96_ERRATUM1.md) (`b747a92c2`)
  - Erratum `2` (`W3` `S^2` parity `[-1, -1, 1]` & self-contained `W4` `Gate F-U2` `24`-pt `O_1` equations): [relays/cards/AGY-002_A2-WG96_ERRATUM2_FU2_FORMULA_AND_W3_PARITY.md](relays/cards/AGY-002_A2-WG96_ERRATUM2_FU2_FORMULA_AND_W3_PARITY.md) (`a53997adb`)
  - Erratum `3` (`W1` split-chirality center `Z(W:G96)` & `G/Z`, `SVD` `Vh.conj()`, `S(c_3) = -(-i\tau)^{3/2} P_{01} c_3`): [relays/cards/AGY-002_A2-WG96_ERRATUM3_CENTER_CONJ_AND_S_AUTOMORPHY.md](relays/cards/AGY-002_A2-WG96_ERRATUM3_CENTER_CONJ_AND_S_AUTOMORPHY.md) (`61a5ebf56`)
  - Erratum `4` (`B1610` order-`3` lift `g^3 = +I_2 -> {1/6, 1/2, 5/6}` vs order-`6` lift `g^3 = -I_2 -> {0, 1/3, 2/3}`): [relays/cards/AGY-002_A2-WG96_ERRATUM4_B1610_SPIN_LIFT.md](relays/cards/AGY-002_A2-WG96_ERRATUM4_B1610_SPIN_LIFT.md) (`c3cfc2f4f`)
- **Final Authoritative Producer (`v3`, `all_gates_passed = true`):**
  - Script (`0` float/complex AST literals, `0` `frontier/` imports): `relays/a2_wg96_v3/verify_a2_wg96_v3.py` (`Commit 2c`, `1fe409150`, `SCRIPT_SHA256 = 1c0fbb88aa8e1b24c49215668d1eb18a50cd09f64b15ccb19ea851f18103b567`)
  - Output (`committed unread`): `relays/a2_wg96_v3/verify_a2_wg96_out.json` (`Commit 3c`, `9d3ec76ec`, `OUTPUT_SHA256 = e4906a3de9dedcbed2cb9dbc6e28e8ed41f7e3b739c69583de00c3717d4346fa`)
- **Independent Cold-Room Zero-Trust Referee (`v1`, `all_gates_passed = true`, `A`-only manifests):**
  - Read ONLY the Card + Errata (`zero producer/frontier files opened`); uses an independent `3`-stage `6`th-order Gauss–Legendre + fine explicit `RK4` punctured-torus `L_2` ODE propagator (`agreeing to < 4 * 10^{-15}`):
  - Script (`0` float/complex AST literals): `relays/a2_wg96_referee/referee_a2_wg96.py` (`Commit 4a`, `9045633ea`, `SCRIPT_SHA256 = c408e4b6dfebd542166212775147dfea503cd250090c19c37f304de0de99a54e`)
  - Output (`committed unread`): `relays/a2_wg96_referee/referee_a2_wg96_out.json` (`Commit 4b`, `b8ec928ed`, `OUTPUT_SHA256 = 9b47bcbdcb3a6dafc5415d7663d107a8510816d3e6af31fcaff361e07dcd5a95`)
- **Prior Iterative Producer Records Preserved Untouched:** `380a50c54` (`v1`), `1053d2355` / `7af361ec7` (`v2`).

---

## 2. Classification Across All Three `E:J5` Candidates & Producer / Referee Cross-Check

Both Producer `v3` (`58 s`) and the independent Cold-Room Referee (`757 s`) agree on every algebraic invariant, group order, character inner product, intertwiner, and physical-ratio invariance check:

1. **`W1` (`First-Principles Cohomology W:G96, H_Q, W:T, W:\overline{T}, & B1610 Torsor`):**
   - `V = \bigoplus_{p\in\text{PAR}} H^1(F_2; \chi_p \otimes \rho_Q)` (`dim 6`) with Bar-resolution cup Hermitian form `H_Q` (`SIGN = +1` calibration exact; coboundary annihilation `< 2 * 10^{-15}` producer, `< 3 * 10^{-16}` referee; Hermiticity `< 5 * 10^{-16}`) has exact spectrum **`{-4, -4, -4, +4, +4, +4}`** (`signature (3, 3)`).
   - $\langle M_L, M_R \rangle$ generates `W:G96` of order **`96`**, **`20`** conjugacy classes, commutant dim **`2`**, true centralizer **`Z(W:G96) = \{g : [g, M_L] = [g, M_R] = 0\} \cong C_4`** of order **`4`** (`acting as scalar phases \pm i on the two chiral subspaces rather than scalars on V`), coset quotient **`W:G96 / Z \cong S_4`** of order **`24`** (`referee S_4 order histogram {1: 1, 2: 9, 3: 8, 4: 6}`), and exact `3`-strand braid residual `< 3 * 10^{-15}` (`< 5 * 10^{-16}` referee).
   - `L, R, S_\iota` preserve `H_Q` (`< 6 * 10^{-15}` producer, `< 2 * 10^{-15}` referee); `P` reverses `H_Q` (`< 6 * 10^{-15}` / `< 9 * 10^{-16}`) and swaps `W:T <-> W:\overline{T}`. Both `W:T` (`H_Q > 0`) and `W:\overline{T}` (`H_Q < 0`) have order **`96`**, commutant dim **`1`**, `tr(T_L) = e^{-i\pi/4}`, `tr(\overline{T}_L) = e^{+i\pi/4}`, `det(T_L) = e^{-3\pi i/4}` (`turn 5/8`), `det(\overline{T}_L) = e^{+3\pi i/4}` (`turn 3/8`).
   - All `4` `B1610` founding-torsor rules (`\sigma, C(\sigma), \mathrm{rev}(\sigma), C(\mathrm{rev}(\sigma))`) reverse `H_Q` at single tick (`< 7 * 10^{-15}` / `< 4 * 10^{-15}`), preserve `H_Q` & `W:T, W:\overline{T}` at double tick (`< 7 * 10^{-15}`), and satisfy `M_2^3 = -I_6` (`turns {1/6, 1/2, 5/6}`, both seats) under the order-`3` lift `g^3 = +I_2` and `M_2^3 = +I_6` (`turns {0, 1/3, 2/3}`, referee) under the order-`6` lift `g^3 = -I_2`.

2. **`W2` (`Candidate I: Fixed Torsion Wilson Line w_0 != 0 -> Outcome [3]`):**
   - For both `N = 3` (`8` nonzero points) and `N = 5` (`24` nonzero points), $\langle L, R \rangle \pmod N$ (`both row and column conventions checked in referee`) acts transitively in a single orbit (`size 8` and `24`) with **`0` common fixed points**, establishing **`Outcome [3]` (`background not kept; thread-selecting`)**.

3. **`W3` (`Candidate II: Untwisted CIM Level-3 Odd Spin (1/2, 1/2) -> Outcome [2]`):**
   - Point- and modulus-independent $3\times 3$ unitary `(M_T^{CIM}, M_S^{CIM}, M_R^{CIM})` (`tau / z` independence `< 7 * 10^{-36}` producer, `< 5 * 10^{-45}` referee; unitarity & braid `< 10^{-15}`) has `M_T^{CIM}` phase turns `[1/24, 1/24, 3/8]` (`err < 6 * 10^{-17}`).
   - Charge conjugation `(M_S^{CIM})^2` commutes with `M_T^{CIM}` and `M_R^{CIM}` (`< 5 * 10^{-16}`) with eigenvalues **`[-1, -1, +1]`** (`2` odd modes + `1` even mode). Across **all `24` Dedekind twists `k = 0..23`**, commutant dim is identically **`2`** (`2 + 1` reducible split) and character inner product against both `W:T` and `W:\overline{T}` is **`0`** (`< 2 * 10^{-16}` producer, `< 8 * 10^{-17}` referee), establishing **`Outcome [2]`**.

4. **`W4` (`Candidate III: Covariant Half-Period Spin Modes & Gate F-U2 24-Pt O_1(\tau) -> Outcome [1]`):**
   - Direct `E_\tau` check at `\tau_1 = 17/100 + 13/10 i` and `\tau_2 = -2/7 + 19/10 i`: `R_h(\tau)` (`weight -1/2`) and covariant derivative `c_3(\tau)` (`weight +3/2`, with `S(c_3) = \tau^2 (-i\tau)^{-1/2} P_{01} c_3(\tau) = -(-i\tau)^{3/2} P_{01} c_3(\tau)`) obey `T, S, R` modularity to `< 2 * 10^{-38}` (`< 10^{-45}` referee).
   - Full `Gate F-U2` `24`-point `E[5]\setminus\{0\}` `O_1(\tau)` operator (`m = 1`, `S` reading, `tau_0 = 13/100 + 17/10 i`, both `phased_sum` and `base_w0`):
     * Independent punctured-torus `L_2(\tau_0)`: Gauss–Legendre `6`th-order `24486434709834122 / 10^{16}` vs fine `RK4` (`diff < 4 * 10^{-15}`; horocycle `L/R` covariance `< 4 * 10^{-43}` Chebyshev producer, `< 3 * 10^{-15}` GL6 referee).
     * Both singular-value ratios `(r_u, r_d, r_e)` AND `|V_{CKM}|` are invariant under both `L: \tau_0 \mapsto \tau_0 + 1` and `R: \tau_0 \mapsto \tau_0 / (\tau_0 + 1)` to **`< 4 * 10^{-28}`** (`both ODE L_2 and seed 5/2` in producer; **`< 10^{-15}`** on `ODE GL6` and **`< 3 * 10^{-38}`** on `seed 5/2` in referee), proving the `24`-pt background is kept by `B_3 = <L, R>`.
   - **`24`-Twist Scan `k = 0..23` (`W:T` vs `W:\overline{T}` Exact Isomorphism Theorem):**
     * **At `k = 0` (`holomorphic S reading`):** `|\rho_0(G)| = 96`, commutant dim `1`, $\langle\chi_{\rho_0}, \chi_{W:\overline{T}}\rangle = 1$, $\langle\chi_{\rho_0}, \chi_{W:T}\rangle = 0$ (`< 4 * 10^{-17}` referee), unique (`nullspace 1` vs `0` on `W:T`) unitary intertwiner `U_0` onto **`W:\overline{T}` (`H_Q < 0`)** (`residual < 2 * 10^{-15}` producer, `< 9 * 10^{-16}` referee).
     * **At `k = 18 \equiv -6 \pmod{24}` (`conjugate \tilde{S} reading`):** `(\overline{r_T}, \overline{R_0}) = (\rho_{18}(L), \rho_{18}(R))` (`err < 2 * 10^{-15}` both), `|\rho_{18}(G)| = 96`, commutant dim `1`, $\langle\chi_{\rho_{18}}, \chi_{W:T}\rangle = 1$, $\langle\chi_{\rho_{18}}, \chi_{W:\overline{T}}\rangle = 0$, unique unitary intertwiner `U_{18}` onto **`W:T` (`H_Q > 0`)** (`residual < 2 * 10^{-15}` both).
     * **All other `22` twists $k \notin \{0, 18\}$:** character inner products with both `W:T` and `W:\overline{T}` vanish identically (`< 5 * 10^{-15}` both).
     * **`B1736` `\det = 1` Diagnosis:** Imposing `\det = 1` selects `k in {5, 13, 21} \pmod{24}` with group orders **`{5: 72, 13: 72, 21: 24}`**, quotienting out $Z(W:G96) \cong C_4$ at `k = 21` (`S_4` of order `24`) and explaining why `B1736`'s `det = 1` constraint missed the order-`96` spin-lifted isomorphism.

5. **`Guardrail 3` & `5` Planted Faults (`PF1`–`PF5`):**
   - `10`-trial random Haar $\mathrm{U}(6) \times \mathrm{U}(3)$ basis-scrambling invariance passes with max residual `< 2 * 10^{-14}` producer (`< 9 * 10^{-15}` referee).
   - All **`5 / 5`** planted faults (`PF1` `k = 21` `det = 1` -> order `24`; `PF2` chirality swap `k = 0` vs `W:T` -> nullspace `0`; `PF3` `CIM` `S^2` reducibility `cdim = 2`; `PF4` broken `g_R` / parity lift; `PF5` unaveraged `N = 5` `w_0` moved) are caught cleanly by both seats.

---

## 3. Check Result for `CLOSURE_QUEUE.md` Row `E:J5`

**`E:J5` is settled across all three outcomes on `origin/agy-002/verify` (`0 of 19`):** fixed single torsion
Wilson line $w_0 \neq 0$ (`Candidate I`) realizes **`Outcome [3]`** (`thread-selecting`); untwisted Level-`3`
odd-spin `(1/2, 1/2)` `CIM` modes at $w_0 = 0$ (`Candidate II`) realize **`Outcome [2]`** (`2 + 1` split,
`(M_S^{CIM})^2` parity `[-1, -1, 1]`, `0` overlap across all `24` twists); and the `Gate F-U2` `24`-pt
$E[5]\setminus\{0\}$ orbit-summed covariant spin modes `(Q_J, Q_I, Q_K)` (`Candidate III`) keep `B_3 = <L, R>`
(`L/R` drift `< 4 * 10^{-28}`) and carry **`Outcome [1]`** canonically — realizing **`W:\overline{T}` (`H_Q <
0`) at `k = 0` (`S` reading)** and **`W:T` (`H_Q > 0`) at `k = 18` (`\tilde{S}` reading)** inside
$\mathrm{U}(3)$, with `B1736` `\det = 1` quotienting `C_4` to `{72, 72, 24}` (`S_4`). `0 of 19.`

---

### Dated Correction (`2026-11-22`, `R-AGY002-V1`)

**2026-11-22 (`R-AGY002-V1` Erratum, `F-A2-12`):** Producer `verify_a2_wg96_v3.py` (`W1`-`W4`, `|W:G96| = 96`, `k = 0, 18` half-period join) held `the same` in `R-AGY002-V1`, while `referee_a2_wg96.py:397-449` collapsed the `2D` punctured-torus problem to a `1D` radial disk BVP giving `pi - 1 - (1/2) ln(17 / (10 pi)) = 2.44864347...` (offset `0.04483` from true Fuchsian `L_2(13/100 + 17/10 i) = 2.4934722835041529...`, verified in `A2-OW18 v3`).
