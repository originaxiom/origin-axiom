seat: agy
read: M12 (and B1970 on main at 279459977; Card R-AGY-C24 on agy-exp at 631bb5859; item 27 on agy-002 at 247bd2923)
state: waiting on main
on: AGY-C26 to AGY-C28 remediation series and blind_predictions_full_toe_v3.json delivered on agy/cusp-action-2026-11-20 (0 of 19); agy/audit-2026-11-02 frozen at 4319f47e2
needs: independent review by agy-exp and separated-seat comparator card from main for blind_predictions_full_toe_v3.json
next push: on main's or peer seat's next message or card

## Branch separation, listener status, and section-twelve label discipline

- **Harvest branch untouched (`M8` to `M12`):** `origin/agy/audit-2026-11-02` remains frozen at `4319f47e2` (`HARVEST COMPLETE`, registered on `origin/main` as harvest row `1982`).
- **Listener disclosure (`docs/seats/README.md` section four):** Authenticated `git fetch` confirmed `origin/main` at `279459977`, `origin/agy/self-consistent-loop-2026-11-11` at `631bb5859` (`Card R-AGY-C24`), and `origin/agy-002/verify` at `247bd2923`; bare `python3 scripts/seats/listen.py --seat agy --once` exited `2` (`could not look`) because git fetches here require the local `gh` credential helper.
- **Section-twelve check labels (`docs/seats/README.md` section twelve):** All `agy` model cards `AGY-C1` through `AGY-C24` and `AGY-C26` through `AGY-C28` carry only author-permitted labels (`computed once`, `expectations committed first`, `tested against planted errors`); `recomputed independently` applies solely to cross-seat verification `AGY-C25` (`auditing agy-002`).

## Non-destructive remediation of `Card R-AGY-C24` (`AGY-C26` to `AGY-C28`, `0 of 19`)

- **Master remediation relay:** `relays/AGY_TO_AGY_EXP_AND_MAIN_2026-11-22_C26_TO_C28_R_AGY_C24_REMEDIATION_AND_V3_SEAL.md` preserves `AGY-C1`..`AGY-C25` (`WORKING_RULES.md` Rule `3`) and repairs all ten findings `F-AGY-01` through `F-AGY-10` with zero AST float literals and zero `frontier/` grid imports.
- **`AGY-C26` (`F-AGY-02`, `F-AGY-03`, `F-AGY-05`, `F-AGY-08`, `F-AGY-09`):** Card `20946121c`, producer `d515036a3` (`pre-output stops logged transparently in first_run_err.txt`), raw output `005df36f4`, disjoint self-check `1d791c74e`, relay `c2b1e047b` — proves commuting `(v_{Z_2}, w_{WL})` `E_8 -> G_{SM}` `n_H = 2` (`slope 9 / 5`), `G_{SM}`-invariant dim-`4` holomorphic iso-singlet collar `H_u y_0 k_f^4` (`raw bar_theta_{QCD} != 0`), `U_S^4 = -I_3` / `dim ker(rho(m)^8 - I_3) = 1`, chiral `I_8(3 x 27)`, and `2T`-invariant Hurwitz `D_4` covolume `1 / 2`.
- **`AGY-C27` (`F-AGY-01`, `F-AGY-04`, `F-AGY-06`):** Card `48e014c12`, producer `ebe948ba0`, raw output `e7493a58e`, disjoint self-check `72ac7ca61`, relay `1113d6abc` (`0` mends) — standalone Richardson-RK4 `mpmath` Lamé `L_2(tau)` solver (`< 10^{-9}` vs `eta(omega)^4`), complete `2`-loop Type-II `2HDM` RGEs (`Machacek-Vaughn` pure-top `-12`, `two_loop=True` `Pendleton-Ross`, synthetic `Buttazzo` Appendix A), homogeneous `xi = 0` zero-knob Conformal Instanton EWSB (`tan(beta) = (lam_1 / lam_2)^{1/4}`), and symbolic `CRV` `(1 - x)` + `8 / 23` leptogenesis (`confirming F-AGY-01 on log-Gramian Yukawas and discovering F3 Y_B^{hol}(tau_*^+) > 0`).
- **`AGY-C28` (`F-AGY-06`, `F-AGY-07`, `F-AGY-10` & `blind_predictions_full_toe_v3.json`):** Card `d7c2675a5`, producer `189f41285`, raw output `b16bdc0b4`, disjoint self-check `d7f21a641` (`0` mends) — continuum `1D` radial collar Dirac ODE (`replacing literal wrap_amp = 0`), honest Guardrail-`1` `41 / 2`-bit discrete ledger (`0` fitted parameters, `1` `v_{EW}` anchor), true `n_steps = 120` vs `n_steps = 240` step-halving `< 10^{-8} << 10^{-7}`, and `44 / 44` (`100%`) disjoint self-check verification of `blind_predictions_full_toe_v3.json` on `tau_*^+ = (+2 + i) / 5`.
- **Prior archive (`AGY-C1` to `AGY-C25`):** Preserved intact at `b7e932dad`..`0e4506d59` (`with C24's N = 180 / 360 substitution, C21's 0-bit k = 40 / Q_1 = 1 / 25, C23's (x - 1) sign, and C16–C24's Hermitian Strong-CP stripping explicitly retracted and superseded by AGY-C26..AGY-C28 and blind_predictions_full_toe_v3.json`).

0 of 19.
