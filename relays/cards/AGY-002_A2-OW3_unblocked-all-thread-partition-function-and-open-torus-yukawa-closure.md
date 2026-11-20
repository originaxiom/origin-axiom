# Pre-Registration Card `A2-OW3` — Unblocked All-Thread Volume Partition Function (Whitehead Hagedorn Wall) and Open-Torus `Spin(10)` Holomorphic Two-Higgs Closure (`0 of 19`)

## 1. Purpose and Open-Weave Scope

This card completes the Open-Weave Foundation Campaign (`A2-OW1`, `A2-OW2`, `A2-OW3`, dropping `G:SE1`, `G:SE2`, and hand-picked `m004`) by answering two exact data-free (`0 of 19`) foundational questions:

1. **All-Thread Dynamical Weight Audit (`Z(s, beta)` & Whitehead Accumulation Wall):**
   When all threads of the open punctured-torus weave (orientable `+`, orientable `-`, and non-orientable `P`) are kept open and weighted by physical hyperbolic volume and word-length actions `Z(s, beta) = sum_M exp(-s * L(M) - beta * Vol(M))`, what actually dominates, does a pure volume sum `Z(0, beta)` even converge, and does volume alone ever isolate `m004`?
2. **Open-Torus Yukawa Closure (`Path-A` Single-Higgs `15 x 15` No-Go & `32 x 32` `Spin(10)` `X:HOL` Two-Higgs Theorem):**
   Directly on the open weave's top finite rung `N = 5` (`W_5 = W_3^+ (+) W_2^-` from Card `A2-OW1`), prove algebraically and numerically why single-Higgs linear contractions of the `15 x 15` operator `O_1(tau)` collapse to one `3 x 3` matrix (`Path-A` no-go), and verify from explicit `32 x 32` `Cl(10)` spinor matrices how holomorphic `Spin(10)` `10_C = 5_H (+) 5bar_H` cleanly separates `H_u` (`Q u^c`, `L nu^c`) from `H_d` (`Q d^c`, `L e^c`) with exact `11 / 12` `tan(beta)` invariance and `10`-trial Haar basis-scrambling invariance.

All computations are strictly data-free (`0 of 19`, zero empirical constants, zero `frontier/` imports, zero float or complex `AST` literals in Python source).

## 2. Exact Pre-Registered Tasks and Pass Bars

### Task `OW3-A`: Unblocked All-Thread Partition Function `Z(s, beta)` and Whitehead-Link Hagedorn Accumulation Wall

- Enumerate the complete unblocked census of primitive hyperbolic punctured-torus bundles across all three branches:
  - Branch `+` (`b++w`, orientable, word length `2..7`),
  - Branch `-` (`b+-w`, orientable, word length `2..7`),
  - Branch `P` (`b-+w`, non-orientable, word length `1..6`).
- Compute exact `SnapPy` hyperbolic volumes across all census threads AND across the three infinite cusp-accumulation sequences `b++L^k R`, `b+-L^k R`, and `b-+L^k` for `k = 1..25`, alongside the exact Catalan-constant Whitehead-link volume `Vol(Whitehead) = 4 G = 4 * sum_{n>=0} (-1)^n / (2 n + 1)^2` (cross-checked directly against `SnapPy` `Manifold("5^2_1").volume()`).
- **Pre-Registered Checks & Bar `OW3-A`:**
  1. **Absolute ground state without `G:SE2`:** Verify `m000` (`b-+L`, non-orientable Gieseking) has strictly minimal volume across all tested threads, with `|2 * Vol(m000) - Vol(m004)| < (1/10)^10` (exact `2 : 1` orientation double-cover ratio), capturing `> 99 / 100` of the Boltzmann weight over the census as `beta` grows (`beta = 10`).
  2. **Exact tie even with `G:SE2`:** On the orientable sub-ensemble (`+` and `-` combined), verify `|Vol(m003) - Vol(m004)| < (1/10)^10` (`50 / 50` tie between `m003` and `m004`, proving hyperbolic volume alone never singles out `m004` from `m003`).
  3. **Whitehead-Link Hagedorn Accumulation Wall (`Z(0, beta) = +infty`):** Verify `|Vol(5^2_1) - 4 G| < (1/10)^10`, prove strictly across all `k = 1..25` that `Vol(b++L^k R)` and `Vol(b+-L^k R)` increase monotonically while staying strictly below `4 G` and converging to `4 G` (`|Vol(b++L^25 R) - 4 G| < 1 / 100`), proving rigorously that the pure-volume sum `Z(0, beta) = sum_M exp(-beta Vol(M))` diverges for every finite `beta >= 0`! Also report honestly the exact limit of the non-orientable sequence `Vol(b-+L^k)` as `k -> 25`.
  4. **Regulated `2D` Phase Behavior `Z(s, beta)`:** Evaluate the ground-state dominance share of `m000` (all threads) and `m003 + m004` (orientable threads) across a `(s, beta)` grid (`s in {0, 1/2, 1, 2}`, `beta in {0, 1, 5, 10}`), proving that word-length regulation `s > 0` restores convergence along the Whitehead family while leaving `m000` dominant unconditionally (`m003` tied with `m004` on orientable threads).

### Task `OW3-B`: Open-Torus Yukawa Closure (`Path-A` `15 x 15` No-Go & `32 x 32` `Spin(10)` `X:HOL` Two-Higgs Theorem)

- **Part 1 (`Path-A` Single-Higgs `15 x 15` Trace Collapse):**
  - Directly from the open weave's `N = 5` Weyl-Heisenberg operators `D(a, b) = zeta_5^{3 a b} X^a Z^b` (`(a, b) in (Z/5)^2 \ {(0, 0)}`) and the `P`-eigenbasis projectors `B_3` (`W_3^+`, `dim 3`) and `B_2` (`W_2^-`, `dim 2`) from Card `A2-OW1`:
  - Prove **BOTH** in exact cyclotomic arithmetic mod `Phi_5(w)` **AND** in `65`-digit `mpmath` (`< (1/10)^50`) that for **all `24`** nonzero shifts `(a, b)`:
    `Tr(B_3^H D(a, b) B_3) == +1 / 2` and `Tr(B_2^H D(a, b) B_2) == -1 / 2` identically!
  - Verify numerically on explicit random complex `3 x 3` matrices `Y(a, b)` that every `G_SM`-invariant linear trace contraction of `O_1 = sum_{w != 0} ph(w) Y(w) (x) D(w)` collapses identically to `+(1/2) S_ph` on `W_3^+` and `-(1/2) S_ph` on `W_2^-` (`< (1/10)^50`).
- **Part 2 (`32 x 32` `Spin(10)` Holomorphic `X:HOL` `16 x 16 x 10_C` Coupling & `11 / 12` `tan(beta)` Invariance):**
  - Construct explicit `32 x 32` `Cl(10)` Hermitian gamma matrices `Gamma_1, ..., Gamma_10` directly from the `Berezin`-`CAR` creation/annihilation operators `c_k^dag, c_k` (`k = 1..5`) on `Lambda^*(W_5)` (`{Gamma_mu, Gamma_nu} = 2 delta_{mu nu} I_32`).
  - Construct the exact `32 x 32` charge-conjugation matrix `C_10` and verify directly by matrix multiplication (zero hard-coded flags!): `C_10^H C_10 == I_32`, `C_10^T == +C_10` or `-C_10` (exact computed sign), and `C_10 Gamma_mu C_10^-1 == -Gamma_mu^T` (or `+Gamma_mu^T` per exact `Cl(10)` convention, verified explicitly for all `10` matrices!) with `0` errors.
  - Project the `10` holomorphic / anti-holomorphic combinations `Gamma_k^+ = c_k^dag` (`5_H`) and `Gamma_k^- = c_k` (`5bar_H`) into the `16 x 16` chiral spinor Yukawa matrices `M_k^{+-} = P_{16} (C_10 Gamma_k^{+-}) P_{16}^T` on `Lambda^{even}(W_5)` (`(-1)^F = +1`).
  - Verify directly from the explicit `16 x 16` matrices that:
    1. Every `M_k^{+-}` is **exact symmetric** (`M^T == M`, required for Majorana/Weyl `16 x 16 -> 10_S` bilinear!).
    2. For weak-doublet components `k in {4, 5}`: `M_k^+` (`H_u`, `6Y = +3`) has nonzero entries **exclusively** on `(Q, u^c)` (`6Y: +1, -4`) and `(L, nu^c)` (`6Y: -3, 0`) and **exact zero** on `(Q, d^c)` and `(L, e^c)`; `M_k^-` (`H_d`, `6Y = -3`) has nonzero entries **exclusively** on `(Q, d^c)` (`6Y: +1, +2`) and `(L, e^c)` (`6Y: -3, +6`) and **exact zero** on `(Q, u^c)` and `(L, nu^c)`!
    3. Verify exact **`11 / 12` `tan(beta)` invariance** across `tan(beta) in {1/5, 1, 3, 10, 50}` on explicit `3`-generation complex Yukawa matrices `(Y_u, Y_d, Y_e)`: all `11` dimensionless ratios (`m_u/m_t`, `m_c/m_t`, `m_d/m_b`, `m_s/m_b`, `m_e/m_tau`, `m_mu/m_tau`, `|V_us|`, `|V_cb|`, `|V_ub|`, `J_CP`, `m_b/m_tau`) stay invariant to `< (1/10)^14`, while `m_t / m_b` scales linearly with `tan(beta)` to `< (1/10)^14`!
    4. **Mandatory `Guardrail 3` `10`-Trial Haar Basis-Scrambling Test:** Apply `10` independent random Haar unitary transformations `U_L, U_{Ru}, U_{Rd}, U_{Le}, U_{Re} in U(3)` to the `Spin(10)` `H_u / H_d` Yukawa sector and assert invariance of all `12` physical observables to `< (1/10)^12`!

### Task `OW3-C`: Four Planted Faults (`PF-OW3-1` through `PF-OW3-4`)

1. `PF-OW3-1`: False volume-uniqueness claim `Vol(m004) < Vol(m000)` or `Vol(m004) < Vol(m003)` must be refuted (`m000` is strictly half `m004`, and `m003` ties `m004`).
2. `PF-OW3-2`: False convergence claim for pure-volume sum `Z(0, beta)` at `beta = 10` must be refuted by the `25`-term Whitehead sequence `b++L^k R` staying strictly below `4 G` (non-decaying terms `> exp(-40 G)`).
3. `PF-OW3-3`: False Path-A variation claim that `Tr_{W_3^+}(D(a, b))` varies across `(a, b)` must be refuted (exact constant `+1/2` on all `24` nonzero shifts).
4. `PF-OW3-4`: False holomorphic cross-coupling claim that `H_u` couples to `(Q, d^c)` or `H_d` couples to `(Q, u^c)` inside `16 x 16 x 10_C` must be refuted (`0` nonzero entries).

## 3. Custody and Cold-Room Discipline

- Producer script sealed pre-run in `relays/a2_ow3/verify_a2_ow3.py` with `relays/a2_ow3/SCRIPT_SHA256.txt` (`A`-only).
- Output `relays/a2_ow3/verify_a2_ow3_out.json` and `relays/a2_ow3/OUTPUT_SHA256.txt` (`A`-only) committed unread before inspection.
- Independent Cold-Room Referee subagent built from this Card alone (never reading `verify_a2_ow3.py` or its output) seals `relays/a2_ow3_referee/referee_a2_ow3.py`, runs independently, and commits unread output + `SHA-256` manifest.
- Results relay `relays/AGY002_A2_OW3_RESULTS.md` reports Producer vs Cold-Room Referee honestly. `0 of 19.`
