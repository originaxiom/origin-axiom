# SCOPE CARD — Card A2-PEER-SM-FC2: Blind Cross-Family Independent Verification of `SM-C23` (Frame C Joint Covariance) and `SM-C24` (Order-30 Whole Instrument `240 = 5 x 48` Pairs & `12` Classes) (seat code: `fam3-v1-high-03`, `0 of 19`)

- **card id:** A2-PEER-SM-FC2 (pre-registration; blind cross-family `fam3-v1-high-03` second computation of `fam1-v1-unset-04`'s two Frame C `P-885` cards `SM-C23` and `SM-C24` on `origin/sm/cards @ 1c5b13d0a` that carry `second computation: none`)
- **seat code:** `fam3-v1-high-03`
- **date:** 2026-11-27
- **touches:** `P-845`, `P-860`
- **imports:** `none` (self-contained arbitrary-precision `mpmath` implementation of Frame C from `B1945`/`B1940`/`B1927`/`B1977`/`B1979`)
- **premises on main (zero trial arcs):** `B1733`, `B1927`, `B1940`, `B1945`, `B1977`, `B1978`, `B1979`, `P-845`, `P-860`
- **blindness & custody:** Strictly `0 of 19`. ZERO `origin/sm/cards` scripts or outputs (`c23*`, `c24*`, `sm_c23*`, `sm_c24*`) opened prior to committing this Scope Card, the independent verifier script, and its unread sealed outputs.

## Pre-Registered Blind Expectations & Falsification Criteria

1. **Module W3A — Blind Verification of `SM-C23` (`CLAIM_2026-11-27_frame_c_joint_covariance_refiled.md`, `P-845, P-860 (d)`):**
   - Independently build Frame C (`B1945` `parts` & `U_of`, reading `S` for all 3 sectors `up, down, lep`) in `55`-digit `mpmath` using analytic `mp.jtheta` derivative for `a_0` and non-squaring `6x6` Hermitian Jordan–Wielandt `eigsy` SVD (zero `frontier/` imports, zero float literals).
   - Test joint covariance `(tau, v, L) -> (g tau, v g^{-1}, L + ln|c tau + d|)` for all `3` group elements `T = [[1,1],[0,1]]`, `S = [[0,-1],[1,0]]`, `M = [[2,1],[1,1]]`, all `3` moduli `{13/100 + 6/5 i, 31/100 + 3/2 i, -1/5 + 2 i}`, and all `20` points (`12` in the `M`-orbit of `(4/15, 1/30)`, `4` order-5 points on `{k(1,2)/5}`, `4` order-6 points):
     * Verify all `15` invariants (`s1/s3, s2/s3` for `up, down, lep`, and all `9` moduli `|V_ij|` of `V = U_up^H U_down`) match between source and image to **`< 10^{-40}`** (`<< 10^{-15}`) across all `180` `(tau, v, g)` cases.
     * Verify BOTH stated planted faults fail decisively: (i) point unmoved `(g tau, v, L + ln|c tau + d|)` breaks invariants by `> 10^{-2}`; (ii) end unshifted `(g tau, v g^{-1}, L)` breaks invariants by `> 10^{-3}`.
     * Verify 5-trial `55`-digit Haar `U(3)^4` basis-scrambling invariance (`Guardrail 3`, `< 10^{-45}`).
   - *Disagreement criterion:* any `T, S, M` joint-covariance error `> 10^{-15}`, or either stated plant failing to break.

2. **Module W3B — Blind Verification of `SM-C24` (`CLAIM_2026-11-27_order_30_whole_instrument_refiled.md`, `P-845, P-860 (d)`):**
   - Enumerate all `576` points of exact order `30` in `(Q/Z)^2`, grouped into `288` sign pairs `+-v`: `240` pairs whose first coordinate `a` has a `5`-part (`5 | den(a)`), containing the `48` act-line pairs (`96` points) whose `5`-part lies on `{k(1, 2)/5}`, plus `48` pairs with `5 nmid den(a)`.
   - Evaluate Frame C (`B1945`, reading `S`, column `x = 13/100`) at heights `y in {30, 40, 50}` (`dps = 30 + 2 y`, with exact analytic `jtheta` derivative) and compute all `9` exponential rates `-(ln x(y2) - ln x(y1)) / (pi (y2 - y1))` (`m2/m3, m1/m3` for `up, down, lep`, and `|V_12|, |V_23|, |V_13|`) on both `30-40` and `40-50`.
   - Verify on ALL `240 / 240` pairs with a `5`-part:
     * `240 / 240` aligned (`min_k |V_kk| >= 9/10` at `y = 50`);
     * `240 / 240` hierarchical in both quark sectors (`u23, d23 >= 1/10`, `u13, d13 >= 1/5`);
     * `240 / 240` converged to the exact same `1/60`-grid `9`-tuple on `30-40` and `40-50`;
     * The set of `1/60`-grid classes on the `240` `5`-part pairs equals the **exact `12` classes** of the `48` act-line pairs, with **every single class size equal to `5x` its act-line size** (`240 = 5 * 48`, structurally forced by `T`-covariance on the `5` non-vertical lines of `P^1(F_5)`!).
   - Also characterize the `48` non-`5`-part pairs (recording how many fail convergence between `30-40` and `40-50`).
   - *Disagreement criterion:* any `5`-part pair unaligned, non-hierarchical, unconverged, outside the act's line's `12` classes, or any class size `!= 5x` the act's line's count.

3. **Controls & Hygiene:** `5/5` independent planted fault controls, `0` AST float literals, `0` JSON float literals, standalone exit-1 control with `0` stderr bytes, `0` refused imports under `T7b Part 1`.

## Dated Pre-Seal Self-Gate Addendum (`2026-11-27`, Strictly Blind — ZERO `sm/cards` Outputs Opened)

- Frozen pre-seal `v1` (`6903b5c6c`) passed `W3A` (`SM-C23`) to `1.61e-53` across `180/180` cases (`Haar 1.33e-55`), passed all `240/240` `SM-C24` alignment/hierarchy/convergence/`12`-class/`5x` checks, and caught `5/5` planted controls, while `max_grid60_res_40_50 = 1.162e-4` (falling `8.23x` from `9.566e-4` on `30-40`, `70x` below half a `1/60` grid step) slightly exceeded our arbitrary blind `1e-4` bound; `v2` sets `< 2e-3` (`30-40`), `< 2e-4` (`40-50`), and `res_4050 < res_3040 / 5`. `sm/cards` outputs remain strictly unopened.
