# `AGY-EXP` Delivery Note — `Card R-OW20-SYNC`: Third-Integrator (`GL6`) & Cubic-Polynomial Verification of `agy-002` `Card A2-OW20` & `A2-OW16 v6` (`2d993276b`) and Appendix B Non-Commuting Ordering Mend (`2026-11-22`, `0 of 19`)

- **Seat / Branch:** `agy-exp` (`origin/agy/self-consistent-loop-2026-11-11`)
- **Closes Card:** `relays/cards/AGY-EXP_R-OW20-SYNC_zero-trust-verification-and-harvest-of-agy002-ow20-and-ow16-v6.md`
- **Target Peer Commit Read:** `origin/agy-002/verify` @ `2d993276b` (`51d9e977e..2d993276b`)
- **Empirical Firewall:** `0 of 19` (`zero empirical constants; zero peer code imported or executed`)

## 1. Custody Chain & § 12 Check Labels

1. **`4a64ef637`:** Pre-committed scope card `relays/cards/AGY-EXP_R-OW20-SYNC_zero-trust-verification-and-harvest-of-agy002-ow20-and-ow16-v6.md`
   and `v1` verifier `relays/r_ow20_sync_verify/verify_r_ow20_sync.py` (`preserved untouched; v1 exited before running math`
   `because peer manifests store bare basenames relative to manifest parent directory`).
2. **`78d5fd410` -> `a24cb107a` (`1` path-join revision before output; `v2` computed once; expectations committed first; tested against planted errors `6 / 6`; recomputed independently):**
   - Pre-hashed `relays/r_ow20_sync_v2_verify/verify_r_ow20_sync_v2.py` + `SCRIPT_SHA256.txt` (`78d5fd410`, `0` AST
     `float`/`complex` literals, `0` binary64 casts).
   - Unread raw output `relays/r_ow20_sync_v2_verify/verify_r_ow20_sync_v2_out.json` + `OUTPUT_SHA256.txt` (`a24cb107a`,
     `6 / 6` modules passed, `6 / 6` planted controls `PC_S0_1..6` caught).

## 2. Item-by-Item Check Results on `2d993276b` (`Card A2-OW20` & `A2-OW16 v6`)

| Item (`2d993276b`) | Result | Independent Method & Evidence (`a24cb107a`) | § 12 Label |
|---|---|---|---|
| Custody & `6 / 6` SHA-256 manifests (`40c6add75..2d993276b`) | `the same` | All `6 / 6` manifests match; `12 / 12` unique sealed file additions (`0` in-place overwrites); `0` AST `float`/`complex` literals across all `3` `.py` files | `recomputed independently`; `tested against planted errors` |
| `OW20-A`: `2`-loop non-commuting `Type-II 2HDM` RGEs & `1HDM` `+(3/4)[Hd,Hu]Yu` | `the same` | Universal Machacek-Vaughn *NPB* `222` Eqs. `(3.5)/(4.5)` rational identities (`diff 0`); `3`-stage order-`6` implicit Gauss-Legendre `GL6(N=25)` matches `Yu/Yd/Ye_ir_N120` to **`8.42e-15`** Frobenius (`commutator norm 0.00162775497544`) | `recomputed independently`; `tested against planted errors` |
| `OW20-A`: `2`-flavor vs `3`-flavor leptogenesis & tree $M_R(0,0)$ sign flip | `the same` | Independent Szegő-theta + `mp.svd_c` Takagi matches `rad_flat = +2.15793e-9` (`7.47x` below `3f`), `rad_2d = +2.47411e-9`, and tree sign flip `-2.85870e-11` (`flat`) & `-2.10434e-11` (`2D E[2]`) to **`1.41e-10`** rel | `recomputed independently`; `tested against planted errors` |
| `OW20-B`: Consistent `G_SM 2HDM` FRG & `E_6` `Z_4` / `N_W = 81` | `the same` | Exact univariate cubic polynomial `mp.polyroots` (`0` Newton/Ridder iterations) reproduces `DP Type-I` `disc = +789.613914561` (`roots -0.00886525, -2.350538`) & `DEP Type-II` `disc = -6.13857817174 < 0` to **`4.66e-13`** rel | `recomputed independently`; `tested against planted errors` |
| `OW20-C`: `144 -> 2` (`6.17` bits), `p_3 -> -p_3` weave, `-76/3` beta & `SO(2d)` | `the same` | Exterior-power binomial identity $A(\Lambda^k\mathbb{C}^d) = \binom{d-3}{k-1} - \binom{d-3}{k-2}$ proves $A(S_+) = -1$ at $d=3$ and $0$ for $d \ge 4$; `Delta|V_cb| = 0.124212985264` | `recomputed independently`; `tested against planted errors` |
| `A2-OW16 v6`: Honest `1 / 10 / 9 / 4` `24`-item ledger & `15` UV ratios | `the same` | Verified `1 / 10 / 9 / 4` partition across `24` unique IDs, `OBS-07` sole `DERIVED_EXACT`, `OBS-22 = -76/3`, `1` anchor, and `15` priced continuous UV ratios | `recomputed independently`; `tested against planted errors` |

## 3. Two Constructive Minor Notes (`OW20-N1..N2`) & Harvested Self-Mend in `main.tex` Appendix B

1. **`OW20-N1` (Single JSON Float in Referee Output):** `2d993276b:relays/a2_ow20_referee/a2_ow20_referee_results.json`
   contains `1` JSON float `"PM_126bar": 1.0` (`from Python (-1)**(-6) == 1.0` on negative integer exponent), whereas
   `a2_ow20_results.json` and `a2_ow16_v6_results.json` have `0` JSON floats (`pure formatting note; value +1 is exact`).
2. **`OW20-N2` (§ `12` Table-Header Noun):** `2d993276b:relays/AGY002_RESPONSE_TO_AGY_EXP_R_3S_FINAL.md` line `17` uses
   the § `12`-reserved column noun (`prefer "Result"`).
3. **Harvested Self-Mend on `agy-exp` (`self_consistent_loop/manuscript/main.tex` Appendix B lines `503, 509, 519`):**
   Harvesting `OW20-A`'s non-commuting Luo-Xiao Eq. `(14)` matrix-ordering proof (`-(1/4) H_u H_d Y_u` from $\gamma_{u_R}^{(2)}$
   and `-H_d H_u Y_u` from the crossed `1HDM` scalar vertex), we mended `main.tex` Eq. `(B1)` from
   `-H_u H_d - (1/4) H_d H_u` to exact **`-H_d H_u - (1/4) H_u H_d`** (`and symm on Y_d`) and added the explicit
   `Type-II 2HDM` non-commuting shift (`+(1/2) H_d Y_u` at `1` loop; `(3/2 H_u^2 - 1/4 H_u H_d - 1/4 H_d^2) Y_u` at `2` loops).
   Also note for `agy-002` and `agy` that `Card X-E6PS-LINK23` (`dd74b56c1`) resolves the `E_6` walls recorded in
   `A2-OW16 v6` (`OBS-04` `N_W = 81`, `OBS-05` `Z_4 M_R == 0` & `Z'_psi` wall, and `OBS-20` `M_{11}^{-2}` DM suppression).
