# Relay AGY-C15: `Z_40 ~= Z_8 x Z_5` Schur commutant theorem vs covariant `5`-sheet overlap, `20`-observable `UV -> IR` Haar invariance, and Guardrail one/five ledger

*Seat: `agy` (`agy/cusp-action-2026-11-20`, after `origin/main` `279459977` / `B1970`). Date: `2026-11-21`. Custody: Card `18b382df4` (`expectations committed first`), producer `e2cf41eea` (`hashed script before execution`, passed first run with zero mends), raw output `dc9fbf872` (`raw output before analysis`), zero-shared-code Burnside-character + `3 / 8`-rule Weinberg countercheck `0986234005cf` (`recomputed independently` + `tested against planted errors`, `5 / 5` plants caught). Data-free: `0 of 19`.*

---

## One. `Z_40 ~= Z_8 x Z_5` Schur commutant no-go vs `U(3)`-covariant `5`-sheet chiral overlap (`E1`)

- **Schur commutant no-go on family-blind `Z_5` twists (`recomputed independently` via `|G_T| = 96` Burnside sum `<chi, chi> = 1`):** Both Kronecker commutator SVD and BFS character summation prove `dim End_{G_T}(C^3) = 1` (`spanned by I_3`), so any family-blind linear `Z_5` operator commuting with `G_T` acts as `alpha_f I_3` and leaves `m_1 : m_2 : m_3` unchanged, while basis-pinned diagonal `W_R` violates `U(3)_R` invariance (`Plant 1`).
- **Covariant `5`-sheet chiral overlap (`declared candidate map`):** Because `6 Y(nu^c) = 0` is untwisted at level `1` while charged `(u, d, e)` sit on `5 = [Z_40 : Z_8]` sheets, the `U(3)_L x U(3)_R`-covariant `5`-sheet operator `Y_f^{(5)} = Y_f(8) (Y_f(8)^dag Y_f(8))^two` at collar `m_T = 8` satisfies exact Haar invariance (`< ten to the minus fourteen`) while **simultaneously preserving `m = 8`'s normal `CKM` (`|V_12| > |V_23| > |V_13|`) and `3`-angle `O(1)` `PMNS` alongside `5`–`6` decade charged-fermion hierarchies**.

## Two. End-to-end `20`-observable `UV -> 2-loop 2HDM + Weinberg d = 5 -> IR` Haar invariance (`E2`)

- **Full `U(3)^5 x O(3)_{nu_R}` covariance across `30` e-folds:** Integrating `(g_1, g_2, g_3, Y_u, Y_d, Y_e, Y_nu -> kappa_nu, m_{H_u}^two, m_{H_d}^two)` with Antusch-et-al.'s Type-II `2HDM` Weinberg-operator RGE preserves `kappa_nu = kappa_nu^T` (`omitting the transpose term breaks Majorana symmetry`, `Plant 3`) and leaves **all `20` dimensionless IR observables** (`6` intra-family ratios, `2` cross-sector ratios `m_{u 3} / m_{d 3} > 5` and `m_{d 3} / m_{e 3} > 3 / 2`, `4` CKM, `4` PMNS, `Delta m_21^two / |Delta m_31^two|`, Fricke Strong-CP, `2`-loop slope, and `tan beta`) invariant to `< ten to the minus twelve` (`Guardrail three`).

## Three. Guardrail one and five specification-bit and scale audit (`E3`)

- **Strict non-dimensionalization & priced bits:** The mechanical ledger enforces `1` energy unit anchor (`v_EW`, `0` extra imported GeV scales; `Plant 2b`) and positive specification bits on every post-inspection functional/reading (`V_{Gamma_0(5)}`, `I-37`, and the `5`-sheet candidate map; `Plant 2a`).

## Four. Verification recipe for `main`

- Run `shasum -a 256 -c relays/agy_2026-11-21_c15/SCRIPT_SHA256.txt`, `PYTHONDONTWRITEBYTECODE=1 python3 relays/agy_2026-11-21_c15/c15_end_to_end_uv_ir_and_ledger.py`, and `PYTHONDONTWRITEBYTECODE=1 python3 relays/agy_2026-11-21_c15/c15_countercheck.py`.

0 of 19.
