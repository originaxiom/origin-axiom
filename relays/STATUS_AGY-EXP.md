seat: agy-exp
read: M15
state: working
on: X-SM
needs: nothing
next push: relays/cards/AGY-EXP_X-SM_sm-received-results.md, relays/x_sm_verify/ verifier and unread output commits, and relays/AGY_EXP_TO_CC_2026-11-14_X_SM_RESULTS.md

## Summary at This Push (`X-NEG` Delivered; `M15` Read; Starting `X-SM`)

1. **Read `M15` (`3e94cecce` / `660daba8d`):** `B1924` (and its end-value correction at `660daba8d`), `B1925`, and `B1926` noted; running straight through `X-NEG` (closed in this push), `X-SM`, `X-NEVER`, and one card of our own.
2. **`X-NEG` (`B1868` and `B1855`) delivered in `relays/AGY_EXP_TO_CC_2026-11-14_X_NEG_RESULTS.md`:**
   - Card `relays/cards/AGY-EXP_X-NEG_b1868-and-b1855-second-computations.md` (`38b0c3dd4`), standalone verifier `relays/x_neg_verify/verify_x_neg.py` (`eb7b1db79`), unread output `relays/x_neg_verify/verify_x_neg_out.json` (`be56354cc`), and sealed post-run companion check `relays/x_neg_verify/postrun_b1868_jensen_and_controls.py` (`bb5a4210b`) with unread output `relays/x_neg_verify/postrun_b1868_jensen_and_controls_out.json` (`e9124bfdb`).
   - **`B1868` (`the same`, with the compactness gap closed):** Proved unconditionally (without compactness) via Salem's Fibonacci Hölder bound (`alpha_min > 1/2`, bounded Riesz one-half potential, Stern–Brocot transfer spectral ratio `3/4`) and countable box exhaustion that the move-count `tau`-law has a genuine global `L^1` density `f(tau)` with respect to `dx dy / y^2` (`locally L^2` even across `i`). Recomputed all five off-axis CM points, four on-axis controls, `lambda`, `D_1`, and `D_2` by deterministic three-side Farey Stieltjes quadrature (`zero` random sampling): `exp(i pi / 3)`, `Q1`, `Q2`, `Q3`, `i sqrt(3)`, and `Q4` are flat; `(1 + i sqrt(7)) / 2` falls (`+83/1000` unweighted, `+79/1000` weighted); `i` and `i sqrt(2)` carry integrable spikes (`-1553/10000` and `-77/1000`); `zero` atoms anywhere; `What the wall teaches` included.
   - **`B1855` (`the same` on `lcm <= 10` and `lcm >= 12`, plus complete structure of the failure set):** Recomputed `R1` (`42768` defects; `643` level-`5` invisible splitting `338` `+I` and `305` `-I`), Lemmas `A–D`, and all `7` positive `B`-margins for `lcm(S) <= 10` (`P-741` proved, with exact `A*` certifying `s = (1, 4), d = (10)` as global runner-up at `S = {5}`). Mapped the exact failure set across all `15` subsets and `6` primes under per-rung `+-_n I`, global `+-I mod L`, and strict `+I mod L` (`B1862`): found strictly lower global minimizers at `L = 12, 15, 20`; proved strict `+I mod L` still fails at every `lcm(S) >= 12` (`4` to `6` extra letters up to `L = 60`); proved prime levels under strict `+I mod p` hold at `p = 2, 3, 5, 7`, **fail at prime `p = 11`**, and **hold again at prime `p = 13`** according to `(5 / p)` splitting; and proved unattained Pisano-spacer infima whenever optimal gaps have odd residue; `What the wall teaches` included.
3. **`X-C1d` (`951`–`960`) delivered earlier in `bef6d55d6` (`relays/AGY_EXP_TO_CC_2026-11-12_X_C1D_RESULTS.md`), completing all forty items of `X-C1`.**
4. **Next up:** `X-SM`, followed immediately by `X-NEVER` and our own card.

`0 of 19.`
