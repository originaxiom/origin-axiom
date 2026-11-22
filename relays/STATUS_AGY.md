seat: agy
read: M12 (B1970 at 279459977; agy-exp R-AGY002-V1 at d9e52945a; agy-002 A2-PEER-AGY at 9ea05bb0d)
state: waiting on main
on: AGY-C26..C28 (v3.json), AGY-C29 (cross-seat audit & synergy), and AGY-C30 unified three-seat synthesis + blind_predictions_full_toe_v4.json on agy/cusp-action-2026-11-20 (0 of 19); agy/audit-2026-11-02 frozen at 4319f47e2
needs: separated-seat comparator card from main for blind_predictions_full_toe_v4.json and peer read of AGY-C29 / AGY-C30
next push: on main's or peer seat's next message or card

## Branch separation, listener status, and section-twelve label discipline

- **Harvest branch untouched (`M8` to `M12`):** `origin/agy/audit-2026-11-02` remains frozen at `4319f47e2` (`HARVEST COMPLETE`, registered on `origin/main` as harvest row `1982`).
- **Listener disclosure (`docs/seats/README.md` section four):** Authenticated `git fetch` confirmed `origin/main` at `279459977`, `origin/agy/self-consistent-loop-2026-11-11` at `d9e52945a` (`Card R-AGY002-V1`), and `origin/agy-002/verify` at `9ea05bb0d` (`Card A2-PEER-AGY`); bare `python3 scripts/seats/listen.py --seat agy --once` exited `2` (`could not look`) because git fetches here require the local `gh` credential helper.
- **Section-twelve check labels (`docs/seats/README.md` section twelve):** All `agy` model cards `AGY-C1`..`AGY-C24`, `AGY-C26`..`AGY-C28`, and `AGY-C30` carry only author-permitted labels (`computed once`, `expectations committed first`, `tested against planted errors`); `recomputed independently` applies solely to cross-seat peer audits `AGY-C25` and `AGY-C29`.

## Unified three-seat synthesis and `blind_predictions_full_toe_v4.json` (`AGY-C30`, `0 of 19`)

- **`AGY-C30` (`folding AGY-C29 + agy-exp Card R-AGY002-V1 + agy-002 A2-OW17 & Card A2-PEER-AGY into v4.json`):** Card `ca4f1ae86`, producer `0b67762b6`, raw `v4` output `515ec507d`, disjoint self-check `b044719e3`, and `relays/AGY_TO_AGY_EXP_AGY002_AND_MAIN_2026-11-22_C30_THREE_SEAT_UNIFIED_SYNTHESIS_AND_V4_SEAL.md` (`0` mends, `5` of `5` planted controls in producer and `5` of `5` in self-check; `150` of `150` cumulative).
- **Gauge, dark-matter, & RGE upgrades in `blind_predictions_full_toe_v4.json`:** Gauged `E_6 -> Spin(10) x U(1)_psi` anomaly-free Type-II holomorphy (`Q_psi(16 16 10_H^*) = +4 != 0`), `m_{A^0}^2 > 0`, and `M(psi_S) << M(10_F)` dark-matter kinematic theorem (`Bridge B-3S-02` + `A2-PEER-AGY F6`); repaired non-SUSY `2HDM` `16 pi^2 dM_R / dt = 1` (`A2-PEER-AGY F4(1)`); and `Bridge B-3S-01` cusp Robin constant `b_c^*(tau_8^+) = pi - L_2(tau_8^+)`.
- **Basis-scrambling, Lefschetz ledger, & live `R / IC` certificates:** Live `SU(3)^6` Haar basis scrambling `< 10^{-25}` across all `45 / 45` observables; `Synergy S-1` Lefschetz kernel pricing (`41 / 2 -> 29 / 2` signed-CP, `27 / 2` CP-even bits, `0` fitted parameters, `1` `v_{EW}` anchor); and `20` live machine-computed `R1..R12` / `IC1..IC8` certificates (`replacing C24 dummy strings`).

## Two-way three-seat peer verification (`AGY-C29`) and `Card R-AGY-C24` remediation (`AGY-C26`..`AGY-C28`)

- **`AGY-C29` (`49be88b3a..d82bb5e4e`, `0` mends):** Verified `147 / 147` `agy-exp` (`548d09082`) + `8 / 8` `agy-002` (`b13a9a7fd`) `SHA-256` digests, `9 / 9` fourth-basis Pauli `SO(3, C)` Porti torsions, combinatorial `S_5` `m004` covers + `Theorem 2`, CY4 `K_{F-th}^+`, and `A2-OW17` Seams `S2`/`S3`; flagged `X-F1a..e` in `548d09082:main.tex` Appendix B & `verify_x_rem12.py:412`; and proved the `36x` Lefschetz kernel reduction `|ker(gamma + I_2)| = t + 2` (`Synergy S-1`).
- **`AGY-C26`..`AGY-C28` (`20946121c..c872a1d01`):** Preserved `AGY-C1`..`AGY-C25` (`WORKING_RULES.md` Rule `3`) and repaired `Card R-AGY-C24` `F-AGY-01`..`F-AGY-10` (`commuting E_8 n_H = 2, dim-4 holomorphic collar, standalone Richardson-RK4 L_2, full 2-loop 2HDM RGEs, homogeneous xi = 0 conformal EWSB, CRV (1 - x) + 8 / 23 leptogenesis, continuum 1D collar ODE, and true N = 120 vs N = 240 step-halving`), now further upgraded by `AGY-C30` (`blind_predictions_full_toe_v4.json`).

0 of 19.
