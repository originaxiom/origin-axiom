# `AGY-002_A2-OW6` — Hard Wall 1 Check Result: Analytic `X_0(N)` `Im(tau) <= 1` Ceiling, `E[5]` Twisted-Kernel Raabe No-Go, and Covering-Torus `E[5] + E[6]` Splitting & Trade-Off Results (`0 of 19`)

## 1. Check Labels and Tracked Custody (`docs/seats/README.md` § `12`)

- **expectations committed first:**
  - Card commit `f49201fda`: `relays/cards/AGY-002_A2-OW6_open-weave-x0n-hierarchy-ceiling-twisted-nogo-and-covering-torus-splitting.md`.
  - Disclosed Erratum committed before authoritative `v2`: `b599940a4` (`Erratum 1`: exact Raabe multiplication identity `sum_{k=1}^4 B_2(q k / 5) == (-4 / 5) B_2(0)` yielding exact Higgs-independent `-36` cusp slope for both `2H` and `1H` and `+12` for fermions-only, plus exact CP-conserving control at the imaginary axis `tau = 5 i` where `-conj(tau) = tau` with zero `T`-shift; earlier sealed `v1` `a3fdad9ba` / `831aaabfe` is preserved untouched).
  - Authoritative producer `v2` script seal `25178a55a` (`relays/a2_ow6_v2/verify_a2_ow6_v2.py`, `SCRIPT_SHA256.txt`) & unread output seal `b57f20422` (`relays/a2_ow6_v2/verify_a2_ow6_v2_out.json`, `OUTPUT_SHA256.txt`, `all_gates_passed = true`).
- **recomputed independently:**
  - Independent Cold-Room Referee built from Card + Erratum 1 alone (zero access to `a2_ow6*` prior to `Commit 4b`), using disjoint `60`-dps Euler-pentagonal `V_1`, Eisenstein `E_2` + Ramanujan `E_4 - E_2^2` curvature check, 1D-Poisson Chowla-Selberg massive `K_2` / `K_3` Casimir sum, non-circular `mpmath.jtheta(1)` Kronecker 2nd-limit potential, and disjoint GL6 order-`20` Fuchsian `L_2` + `jtheta` Yukawa evaluator: script seal `49c58395c` (`relays/a2_ow6_referee/referee_a2_ow6.py`, `SCRIPT_SHA256.txt`) & unread output seal `e078dd365` (`relays/a2_ow6_referee/referee_a2_ow6_out.json`, `OUTPUT_SHA256.txt`, **`0` numerical discrepancies across all `89` shared fields**).
  - **Two Transparent Cold-Room Audit Notes:** (i) In `verify_a2_ow6_v2`, `"V_us", "V_cb", "V_ub"` read the
    `(0,1), (1,2), (0,2)` entries of its descending `(t, c, u)` `|V_CKM|` matrix (`|V_ts|, |V_cd|, |V_td|`),
    whereas true ascending physical `|V_us|` is `> 12 / 100` at `m = 8`, `< 3 / 10^6` at `m = 24`, and `< 3 /
    10^11` at `m = 40`; all `A2-OW6` trade-off inequalities hold strictly under **both** labelings (even
    sharper in physical ascending order). (ii) In the sealed referee script, `mp.eighe(Y Y^H)` at `45` dps
    squares `r13_e ~ 9 / 10^14` at `m = 40`, yielding `10`-trial Haar drift `< 2 / 10^29` (`17` orders tighter
    than Guardrail 3's `< (1 / 10)^12`; `V_abs` `< 2 / 10^43`, `J_CP` `< 2 / 10^56`), while `v2`'s direct
    `mp.svd_c` achieves `< 8 / 10^43`.
- **tested against planted errors:**
  - `4 of 4` planted faults caught identically in both `b57f20422` and `e078dd365` (`PF-OW6-1` Berezin sign flip gives `d(-V_1)/dy(2 i) < 0`; `PF-OW6-2` unreduced `E[5]` wrap-around at `m = 8` creates spurious `e != d` `> 36 / 100`; `PF-OW6-3` setting `w_4 = 0` collapses `e != d` `< (1 / 10)^46`; `PF-OW6-4` imaginary axis `tau = 5 i` collapses `|J_CP| < (1 / 10)^56` while `tau = 2 + i` retains Gauss-phase `|J_CP| > 1 / 100`).

## 2. Mask-Safe Verification Summary (`0 of 19`)

| Task / Metric | Producer `v2` (`b57f20422`) | Cold-Room Referee (`e078dd365`) | Agreement |
|---|---|---|---|
| `AST` source & `SHA-256` custody | `0` float/complex literals, `0` `frontier/` imports, `A`-only manifests `OK` | `0` float/complex literals, `0` `frontier/` imports, `A`-only manifests `OK` | Exact (`0` mismatches) |
| `OW6-A`: Analytic `X_0(N)` `Im(tau) <= 1` ceiling | `|dV_1/dy(i)| < (1/10)^50`, `d^2V_1/dy^2(i y) > 0`, `min_x dV_1/dy == dV_1/dy(0, y) > 0` for all `y > 1`; massive `4D` `V_4D(i y; M)` monotone `> 0` for `M in {1/2, 1, 2, 5}` | `60`-dps Euler-pentagonal + `E_2` + Ramanujan `E_4 - E_2^2` (`|dV_1/dy(i)| < (1/10)^61`) + Chowla-Selberg `K_2` (`|dV_4D/dy(i)| < (1/10)^33`) | Exact (`0` discrepancies) |
| `OW6-B`: Twisted `E[5]` Raabe runaway & orbifold lock | `S`-dual `< (1/10)^44`, `Gamma_0(5)` `< (1/10)^42`; exact Raabe slopes `-36` (`2H`, `1H`, Higgs-independent) & `+12` (`F`-only); `F`-only locks at `(+-2+i)/5` (`grad < (1/10)^31`, `det H > 0`, `4`-pt gap `> 23`) | `mpmath.jtheta(1)` (`S`-dual `< (1/10)^60`, `Gamma_0(5)` `< (1/10)^58`, exact charged Fricke cancellation `-2 ln 5` err `< (1/10)^59`, slope err `< (1/10)^28`, `grad < (1/10)^34`, `4`-pt gap exact `11`-digit match) | Exact (`0` discrepancies) |
| `OW6-C`: Taped `E[5]` degeneracy vs open `E[5] + E[6]` split | `E[5]` alone `|r_e - r_d| < (1/10)^45`; `E[5] + E[6]` `rel 23-split`: `~ 48/100` (`m=8`), `~ 98/100` (`m=24`), `> 99/100` (`m=40`); `10`-trial Haar `< (1/10)^42` | Disjoint GL6 `L_2` + `jtheta`: `E[5]` alone `< (1/10)^39`; identical `rel 23-split` & `J_CP` across `m in {8, 24, 40}`; `10`-trial Haar `<= 2 / 10^29` (`V_abs < 2 / 10^43`, `J_CP < 2 / 10^56`) | Exact (`0` discrepancies) |
| `OW6-C`: Single-modulus Hierarchy-vs-CKM/CP trade-off | `m = 8`: `|V_ts| > 9/100`, `|J_CP| > 3/10000`, shallow `r23 > 1/10`; `m = 24`: `r13 < (1/10)^5`, `|V_ts| < 1/100`, `|J_CP| < (1/10)^15`; `m = 40`: `r13 < (1/10)^10`, `|V_ts| < 2/1000`, `|J_CP| < (1/10)^27` | Identical trade-off; also verifies true ascending physical `|V_us|` (`> 12/100` at `m=8`, `< 3/10^6` at `m=24`, `< 3/10^11` at `m=40`) | Exact (both labelings strictly certified) |
| `OW6-D`: Planted faults (`PF-OW6-1..4`) | `4 / 4` caught | `4 / 4` caught | Exact (`4 / 4`) |

## 3. Core Foundational Findings (`0 of 19`)

1. **Exact Analytic `X_0(N)` `Im(tau) <= 1` Ceiling Theorem:** Because `dV_1/dy(x + i y) >= dV_1/dy(i y) > 0` strictly for every `y > 1` and every `x in R`, **no** non-negative untwisted 1-loop spectral determinant `sum_k c_k V_1(d_k tau)` on any modular curve `X_0(N)` (nor `S`-dual massive 4D Kaluza-Klein Casimir potential) can stabilize `Im(tau) > 1`.
2. **Exact Raabe Cancellation on the Twisted `E[5]` Isogeny Kernel:** Averaging the Fricke-symmetrized twisted potential over the `4`-point `Gamma_0(5)` kernel cancels every charged field identically (`sum_{k=1}^4 B_2(q k / 5) = (-4 / 5) B_2(0)`); only neutral `Y = 0` modes (`6` real `nu^c` minus `24` real gauge bosons) survive at the cusp, causing an exact **Higgs-independent `-36` runaway to `-infty`** for the full SM (both `2H` and `1H`). Even dropping gauge bosons (`+12` confining fermions-only) snaps the minimum straight back to `tau_*^{+-} = (+-2 + i) / 5` (`Im = 1 / 5`).
3. **Topological Covering-Torus Lift, Automatic `e != d` Splitting, & Honest Remaining Flavor Wall:** The
   covering-torus integer lift `m * tau_*^+` (`m in {8, 24, 40}`) is thus forced as the unique untuned path to
   `Im(tau_eff) > 1`, and opening the `t = 4` (`E[6]`) overtone via `A2-OW5`'s zero-parameter Regime-4b
   weights (`w_3, w_4`) immediately breaks `E[5]`'s exact `e = d` degeneracy (`48 / 100` to `> 99 / 100`)
   while keeping nonzero `J_CP` and Haar invariance. However, along any single-modulus ray `m * (2 + i) / 5`,
   mass hierarchy and CKM/CP mixing obey a **strict exponential trade-off**: `m = 8` gives sizable mixing/CP
   with shallow masses, while `m = 24, 40` give multi-decade mass hierarchies (`< (1/10)^5` to `< (1/10)^10`)
   with exponentially suppressed `|V_us|` and `|J_CP|`. Separating mass hierarchy from off-diagonal mixing/CP
   requires a multi-scale or anomalous-dimension/RG mechanism beyond a single universal `m * tau_*`. `0 of
   19.`
