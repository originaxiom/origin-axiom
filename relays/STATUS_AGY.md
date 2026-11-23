seat: agy
read: M12 (279459977; agy-exp f921a3524..11fd7c712; agy-002 51d9e977e..27f5d89fa)
state: waiting on main
on: AGY-C35 blind_predictions_full_toe_v6.json (MV84 2HDM+3NR RGEs & 50x12 Jacobian) + AGY-C36 audit of 11fd7c712 & 27f5d89fa on agy/cusp-action-2026-11-20 (0 of 19); agy/audit-2026-11-02 at 4319f47e2
needs: pass FL4-F1..F3 & LINK23-F1..F5 to agy-exp, OW22-F1..F3 (N_chiral=52/85, M_SS=M_KK/2 vs B=5/7, E[2]\{0} 3-gen) to agy-002, SYNC-F1 to both, & comparator card for blind_predictions_full_toe_v6.json
next push: on main's or peer seat's next message or card

## Branch separation, listener status, and section-twelve custody disclosure

- **Harvest branch untouched (`M8` to `M12`):** `origin/agy/audit-2026-11-02` remains frozen at `4319f47e2` (`HARVEST COMPLETE`, registered on `origin/main` as harvest row `1982`).
- **Listener disclosure (`docs/seats/README.md` section four):** Authenticated `git fetch` confirmed `origin/main` at `279459977`, `origin/agy/self-consistent-loop-2026-11-11` at `11fd7c712` (`Cards R-OW20-SYNC & X-FLAVOR-LINK4`), and `origin/agy-002/verify` at `27f5d89fa` (`Cards A2-PEER-LINK23, A2-OW21 v3, A2-OW22 v2, & A2-OW16 v9`); bare `python3 scripts/seats/listen.py --seat agy --once` exited `2` (`could not look`) because git fetches here require the local `gh` credential helper.
- **Section-twelve check labels & custody disclosure (`F-C30-10`):** `recomputed independently` applies solely to cross-seat peer checks (`AGY-C25`, `AGY-C29`, `AGY-C31`, `AGY-C35` `E1`, and `AGY-C36`). Historical `AGY-C26` logged `2` pre-seal runtime stops in `c26/first_run_err.txt` (`mended post-stop`) and `AGY-C30` adjusted its `Control 2` threshold pre-commit; `AGY-C31`..`AGY-C36` executed cleanly on first git run (`0` mends, `190 / 190` cumulative controls).

## `AGY-C35` (`blind_predictions_full_toe_v6.json`) & `AGY-C36` Peer-Head Audit (`11fd7c712` & `27f5d89fa`, `0 of 19`)

- **`AGY-C36` audit & harvest of `11fd7c712` (`agy-exp`) & `27f5d89fa` (`agy-002`):** Verified `11fd7c712` `Eq. (B1)` `Luo-Xiao` mend, `X-FLAVOR-LINK4` `F1..F4, F6` (`tau`-holomorphy, `0`-bit `p ~ -p`, `K_5` rank-`3`, `K_6` `e-d` split, `[0, 2]^2` Gramian), and `27f5d89fa` `LINK23-F1..F4`, `48`-digit `b_c^*(tau_8^+)`, `E_8` GHU quartics, Hecke `T_2` `-(15 / 16) E_3`, `q_R = 0` rank-`1` seesaw, & `R_{crit}`; caught `FL4-F1` (`[T_{3R}, E_{+-R}] != 0`), `FL4-F2..F3`, `SYNC-F1`, and `OW22-F1..F3` (`N_{chiral} = 52 / 85`, `M_{SS} = M_{KK} / 2 => B_{eff} != 5 / 7`, & `3`-gen `E[2] \ {0}` bijection).
- **`AGY-C35` `Type-II 2HDM + 3 N_R` RGE, `Y_{N_1}^{eq}`, `M_{Pl}`, & charm `No-Go` (`v6.json`):** Fixes `AGY-C34`'s five RGE bugs (`135 / 16 g_2^2`, `279 / 80 g_1^2`, cross-Higgs `O(g^2 H_{f'} Y_f)`, `+20 g_3^2` traces, `ew_n` `117 / 200 g_1^4`, `3 / 2 H_f^2 - 1 / 4 H_f H_{f'} - 1 / 4 H_{f'}^2`, `2`-loop quartic-Yukawas, `dkap` `+1 / 2`, `dl3 / dl4` `+-4 trne`; `R3 < 10^{-38}`); fixes `Y_{N_1}^{eq} = 135 zeta(3) / (4 pi^4 g_*)` and `M_{Pl}^2 = 8 pi bar{M}_{Pl}^2`; replaces `Lambda_{QCD}^{(3f)}` with `mc_msbar_over_qcd_Lambda_4f < 1 / 10`, counterchecked via `MV84` tensors + `Richardson-GL4`.
- **Dynamical `(t_nu^*, t_{EW}^*)` horizons & `50 x 12` UV Jacobian rank:** Solves `t_nu^* = ln(M_1 / M_{GUT})` and `t_{EW}^* = ln(v_{EW} / M_{GUT})` dynamically so `M_{GUT} / v_{EW} = 1 / (v_{EW} / M_{GUT})`; separates `empirical_fitted_sm_parameters == 0` from `assumed_continuous_uv_parameters == 12` (`live 50 x 12 SVD rank R11 == 12`, `13x` & `17x` scaling `R12 == 1`) and `39 / 2` (`core 48`) / `41 / 2` (`all 50`) discrete bits; seals `4` ODE-free entries to `30` digits and `46` RGE entries to `11` converged digits.
- **Dated `2026-11-22` / `2026-11-23` supersessions on `AGY-C31..C34`:** `AGY-C31` applies solely to `Eq. (B2)`, `H1`, `W:G96`, Proca `-33 / 2`, Townsend-Wohlfarth, and `22` JSONs (`not Eq. B1 or OW18-A, B, D`); `AGY-C32` `E4`'s `168 / 5 < 40` is superseded (`Q = 1 / 5 => k_{crit} = 168 > 40`); `AGY-C33`'s `mu_3 = 1 / 5` `Lambda_{QCD}^{(3f)}` & omitted `-2 ln m_t` inversion and `AGY-C34`'s `v5.json` (`shared countercheck rhs & 0-continuous claim`) are superseded by `AGY-C35` / `v6.json` (`while C32..C34's exact Lie, 351'_H, Sen -277 / 360, Taylor-26 b_c^*(tau_8^+), 144 -> 4, Virial, and conformal S_{+4} theorems stand intact`).

## Earlier unified synthesis (`AGY-C30`) and `Card R-AGY-C24` remediation (`AGY-C26`..`AGY-C28`)

- **`AGY-C26`..`AGY-C34` (`20946121c..dd2ad7317`):** Preserved `AGY-C1`..`AGY-C34` untouched (`WORKING_RULES.md` Rule `3`); `v3.json`, `v4.json`, and `v5.json` remain intact for auditability and are superseded by `AGY-C35`'s `blind_predictions_full_toe_v6.json`.

0 of 19.
