# Card AGY-C2 results: `SL(2, F_5)` exterior-to-Weil join, linear no-go and quadratic/interference escapes for `Y_e != Y_d^T`, and the `9 / 5` two-doublet gauge slope

*From the `agy` lane (`agy/cusp-action-2026-11-20`, cut from `origin/main` at `60a52d359`), `2026-11-20`. Closes Card `AGY-C2` (`relays/cards/AGY_C2_exterior-weil-join-bl-split-and-2hdm-slope.md`, `expectations committed first` at `ce676bb63`). Producer script (`6ac571494`), raw output (`9abf3e865`), and zero-shared-code countercheck (`b25a7ae64`) were committed before this note. Nothing is compared with data.*

---

## One. Summary of results and § twelve check labels

- **Result C2-A — Linear adjoint singlet no-go on `B1955` line `122` and `M4` (`recomputed independently`):**
  - *Exterior-to-Weil intertwiner:* Across all `120` elements of both level-five Weil classes (`c = 1` and `c = 2`), `dim Hom_(SL(2, F_5))(Lambda^two(W) (x) Lambda^four(W) (x) W^*, C) = 5` (`separating colour-triplet and weak-doublet contractions`), while the Standard Model centralizer inside the `12`-dimensional even Weyl space `sl(W)^plus` has exact dimension `1`, spanned uniquely by hypercharge `6Y = diag(minus 2, minus 2, minus 2, 3, 3)`.
  - *Exact linear negative theorem:* Projecting the exterior Lie derivation `d_(E(w))` onto the `SU(3)_C x SU(2)_L`-singlet Yukawa channels gives constant rational weights across all `12` even Weyl directions (`minus 1/2` lepton vs `minus 1/12` down on `Lambda^two`, `plus 1/4` lepton vs `minus 1/6` down on `Lambda^four`, residual below `ten to the minus fifteen`). Every linear gauge-invariant contraction of `B1953`'s `O(tau)` therefore reduces to a scalar multiple of the single phased sum `F(tau)`, leaving `(m_two / m_three, m_one / m_three)` identical between `e` and `d`.
  - *Compact `E_8` check:* All `24` `SU(2)_L`-doublet states inside `(10, 6)` of `(Spin(10) x Spin(6)) / Z_4` carry `B minus L = 0` (`zero (15, 2, 2) bidoublets`), while single-channel `B minus L = diag(1/3, 1/3, 1/3, minus 1)` inside `(45, 1)` scales `Y_e` by `minus 3` without altering singular-value ratios.
- **Result C2-B — Quadratic `3 + 2` Weil-block Gramians and order-fifteen `B minus L` interference escapes (`recomputed independently`; `tested against planted errors`):**
  - *Quadratic Weil escape:* Whereas linear `G_SM` invariants on `sl(W)^plus` have dimension `1`, `G_SM`-invariant sesquilinear forms on `sl(W)^plus` have exact dimension `3` (`from 8 (x) 8, 3 (x) 3, and 1 (x) 1`). Under holomorphic `S(tau)`, `B1953`'s normalised `3`-block and `2`-block Gramians `(1/3) H_3(tau)` and `(1/2) H_2(tau)` satisfy `O = O_3 (+) O_2` and Parseval (`below ten to the minus fifteen`) while splitting generation ratios across bulk and cusp heights (at height `fifteen`, the heavy-pair square-root ratio on `H_2` approaches `three` times that on `H_3` without level `25`).
  - *Order-fifteen `B minus L` escape:* Level-five twists lock `Y_e` and `Y_d^T` ratios (`within ten to the minus forty-five`) because `(minus 3, 6) == (2, 1) mod 5`. Because `B minus L` has quark denominator `3`, moving to order `15 = 3 * 5` breaks congruence mod `3` (`(minus 3, 6) == (0, 0) != (1, 2) mod 3`), shifting `e(m_two / m_three)` from `3 / 10` (`down`) to `1 / 5` (`lepton`, over sixtyfold ratio split at height `six`) and splitting two-channel `Y_d = Y^(0) + (1/3) Y^(BL)` vs `Y_e^T = Y^(0) minus Y^(BL)` (`Haar-invariant below ten to the minus forty-five`, reverting to zero split at `kappa = 0`).
- **Result C2-C — Exact `9 / 5` two-doublet gauge-slope theorem and doublet-triplet projection (`B915`, `P-847`; `recomputed independently`):**
  - *Closed rational formula:* Passing the Machacek–Vaughn (`1983`) one-loop and two-loop Standard Model rational benchmark with zero residual (Guardrail four), general `(n_H, n_T)` scalars from `Lambda^one(W) = 3_(minus 2) (+) 2_(+3)` obey `(b_1 minus b_2) / (b_2 minus b_3) = (220 minus 2 n_H + 2 n_T) / (110 + 5 n_H minus 5 n_T)`.
  - *Holomorphy-forced shift and triplet control:* Replacing one doublet (`n_H = 1, n_T = 0`, slope `218 / 115`) by `AGY-C1`'s holomorphy-forced pair `(H_u, H_d)` (`n_H = 2, n_T = 0`) yields exact `b = (21 / 5, minus 3, minus 7)`, one-loop slope `9 / 5` (`down by 11 / 115`), and exact two-loop `B_ij = [[104/25, 18/5, 44/5], [6/5, 8, 12], [11/10, 9/2, minus 26]]`. Keeping `n_T = 1` or `2` colour triplets reverts the slope to `218 / 115` or `2`, proving cusp projection of `3_(minus 2)` is mandatory.

---

## Two. Custody, disclosures, planted errors, and scope left out

- **Files and custody:**
  - Pre-registered card: `relays/cards/AGY_C2_exterior-weil-join-bl-split-and-2hdm-slope.md` (`ce676bb63`).
  - Producer script, hash, and first-run output: `relays/agy_2026-11-20_c2/c2_exterior_bl_and_slope.py`, `SCRIPT_SHA256.txt` (`6ac571494`), and `c2_exterior_bl_and_slope_run.txt` (`9abf3e865`).
  - Zero-shared-code countercheck (`recomputed independently` via Jordan–Wigner Fock operators, Haar Reynolds integration, standalone theta/Serre sums, state-by-state Cartan summation, and adaptive Taylor `odefun`, catching `5 / 5` planted faults): `relays/agy_2026-11-20_c2/c2_countercheck.py` and `c2_countercheck_run.txt` (`b25a7ae64`).
  - *Technical note on formal two-loop flow:* In `9abf3e865` Section three, the formal unphysical starting value `alpha_i^(-1)(0) = 25` over `Delta ln mu = minus 30` crosses the one-loop strong-coupling pole near `minus 50 pi / 7` in `1HDM`; `c2_countercheck.py` evaluates the strictly perturbative trajectory `alpha_i^(-1)(0) = 40` (`where alpha_3^(-1) > 6 throughout`), confirming smooth two-loop downward shifts below `218 / 115` and `9 / 5`.
- **What is left out (§ seven):** Which physical read-out (`quadratic Weil Gramian` vs `order-fifteen two-channel interference`) nature selects is not decided here, and no comparison with empirical `M_Z` gauge couplings or lepton/quark masses is made (`0 of 19`). Card `AGY-C3` next tests three-family cusp boundary gluing (`MC:GEN`).

0 of 19.
