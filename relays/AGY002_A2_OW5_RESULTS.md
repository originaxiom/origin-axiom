# `AGY-002_A2-OW5` — Open-Weave `6D -> 7D` Chirality & Triple-Locked `I_8` Inflow Theorem and Five-Regime Open-Flute Selberg `s = 2` Audit Results (`0 of 19`)

## 1. Check Labels and Tracked Custody (`docs/seats/README.md` § `12`)

- **expectations committed first:**
  - Card commit `c9d3cc05a`: `relays/cards/AGY-002_A2-OW5_open-weave-6d-7d-chirality-inflow-and-five-regime-selberg-audit.md`.
  - Producer script seal `72c607c61` (`relays/a2_ow5/verify_a2_ow5.py`, `SCRIPT_SHA256.txt`) & unread output seal `b47f02450` (`relays/a2_ow5/verify_a2_ow5_out.json`, `OUTPUT_SHA256.txt`, `all_gates_passed = true`, first-shot pass, `0` errata).
- **recomputed independently:**
  - Independent Cold-Room Referee built from Card `c9d3cc05a` alone (zero access to `relays/a2_ow5/` prior to
    `Commit 4b`), using disjoint `3`-mode fermionic creation-annihilation Fock bitmask `Cl(6)` over `Z[i]`
    with non-diagonal `Q[i]` `U(8)` basis-scrambling, direct `16`-state Cartan-weight `Fraction` polynomial
    expansion of `sum exp(i F) A_hat(R)` in `Q[h_1, h_2, w_2, F_Y, x_1, x_2]` (with `SU(4)` negative control),
    and disjoint Lagrange-Gauss reduced indefinite binary quadratic form cycles (`D = t^2 - 4` and `D = t^2 +
    4`, zero continued-fraction DFS): script seal `39c40b850` (`relays/a2_ow5_referee/referee_a2_ow5.py`,
    `SCRIPT_SHA256.txt`) & unread output seal `efeabdbc7` (`relays/a2_ow5_referee/referee_a2_ow5_out.json`,
    `OUTPUT_SHA256.txt`, **`0` discrepancies across `75+` cross-checked fields**).
- **tested against planted errors:**
  - `4 of 4` planted faults caught identically in both `b47f02450` and `efeabdbc7` (`PF-OW5-1` omitting `-i` in spin-lift gives `R(pi)^2 = -I_8 != +I_8`; `PF-OW5-2` dropping `u^c` from `16_+` breaks `Tr(Y)`, `Tr(Y^3)`, `A(SU(3)^3)`; `PF-OW5-3` dropping the `7` odd-square `PSL(2, Z)` classes reduces census `363 -> 356`; `PF-OW5-4` unfiltered `SL(2, Z)` collapses `m004` into an exact `50 / 50` tie with `m003`).

## 2. Mask-Safe Verification Summary (`0 of 19`)

| Task / Metric | Producer (`b47f02450`) | Cold-Room Referee (`efeabdbc7`) | Agreement |
|---|---|---|---|
| `AST` source & `SHA-256` custody | `0` float/complex literals, `0` `frontier/` imports, `A`-only manifests `OK` | `0` float/complex literals, `0` `frontier/` imports, `A`-only manifests `OK` | Exact (`0` mismatches) |
| `OW5-A`: Universal `T^2 / Z_2` across `547` threads | `0` `(-I_2) M` commutation failures; `PSL` orbits `{(3,): 121, (1,2): 184, (1,1,1): 58}`; `det=-1` `{(3,): 63, (1,2): 92, (1,1,1): 29}` | Identical via disjoint Lagrange-Gauss automorphs (`0` failures, exact orbit match; `m000, m004 = (3,)`, both `t = 4 = (1, 2)`) | Exact (`0` discrepancies) |
| `OW5-A`: Explicit `8 x 8` `Cl(6)` & `(48_L, 0_R)` projection | `3`-fold Pauli `Z[i]`: `0 / 36` anticommutator errs, `hat_iota^2 = +I_8`, `Gamma_7 = +1` projects under `hat_iota = +1` to `(2_L, 0_R) -> (48_L, 0_R)`, unorbifolded `index = 0` | Disjoint `3`-mode Fock `a_k, a_k^dag` + `U(8)` basis-scrambling: identical `(2_L, 0_R) -> (48_L, 0_R)`, unorbifolded `index = 0` | Exact |
| `OW5-B`: Triple-locked `6D` `G_SM` `I_8(16_+)` & `7D` CS inflow | `4D` anomalies all `0`; `SU(2)/SU(3)` `tr(H^4) == (1/2)(tr H^2)^2` `< (1/10)^25`; `c(F_3^3 F_Y) = 1 / 9`, `c(R^4) = 1 / 360`, `det(Q_3) = -11 / 23328` (`rank 3`), `det(Q_4) = 1 / 1679616` (`rank 4`), `12 / 12` `7D` CS terms exact | Disjoint `16`-state Cartan polynomial expansion (`0` residual across all monomials, `SU(4)` negative control caught): identical `1 / 9`, `1 / 360`, `Q`, `det(Q_3)`, `det(Q_4)`, `12 / 12` graded-Leibniz `d omega_7^{CS} == I_8` | Exact (`0` discrepancies) |
| `OW5-C`: `547`-class `s = 2` five-regime Selberg audit | `363` `PSL` (`first 12: [1,2,2,3,2,4,2,6,3,4,4,6]`) + `184` `det=-1`, `7` odd squares (`m004 = m000^2`); `(R1)` `m004 > 1 / 2`; `(R2)` `m004 == m003`; `(R3)` `m000 > 62 / 100` beats `m004 < 1 / 10` by exact `phi^4`; `(R4a)` `t=2, det=-1` beats `m004` (`> 138 / 100`); `(R4b)` `m004` `#1` (`> 1 / 3`, `> 4x` single `t = 4`) paired with `4` signed `t = 4` (`96/100 < w4/w3 < 98/100`, combined `> 66/100`) | Disjoint Lagrange-Gauss (`50`-dps `mpmath`): `363 + 184 = 547`, `7` odd squares `half_M^2 == M`, all `5` regimes match (`phi^4` err `0`, `(R4a)` err `< 10^-50`) | Exact (`0` discrepancies) |
| `OW5-D`: Planted faults (`PF-OW5-1..4`) | `4 / 4` caught | `4 / 4` caught | Exact (`4 / 4`) |

## 3. Core Foundational Findings (`0 of 19`)

1. **Universal Open-Weave `T^2 / Z_2` Chirality Without `m004`:** Because the hyperelliptic involution `iota = -I_2` commutes with every monodromy `M in GL(2, Z)`, the `6D` pillowcase orbifold `T^2 / Z_2` extends globally across the entire open weave (zero `m004` assumption). Its four fixed points decompose universally into the cusp puncture `0 in E[2]` plus the three `W:T` parities `E[2] \ {0}` permuted by `M mod 2 in S_3` (`(3,)` for `m000, m004`; `(1, 2)` for `t = 4`). Explicit `8 x 8` `Cl(6)` spin-lift `hat_iota = (-i) R(pi)` projects `3 x 16_+` strictly to pure 4D chiral `(48_L, 0_R)`.
2. **Triple-Locked Impossibility of `6D` Green-Schwarz (Forcing `7D` Bulk Inflow):** Even inside `G_SM = SU(3)
   x SU(2) x U(1)_Y` (without `Spin(10)`), the exact `6D` anomaly polynomial `I_8(3 x 16_+)` carries **three**
   independent obstructions to `6D` Green-Schwarz cancellation: (i) an irreducible mixed gauge `6`-form `^`
   `2`-form anomaly `(+1 / 3) tr_3(F_3^3) F_Y != 0` (un-cancellable by any number of `6D` 2-form tensors
   `B_2`), (ii) pure gravitational anomaly `(+1 / 120) tr(R^4) != 0`, and (iii) full-rank quadratic block `Q`
   (`rank 3` gauge / `rank 4` full, `det(Q_4) = 1 / 1679616 != 0`). Thus `6D` cannot close standalone and
   strictly forces `7D` bulk Chern-Simons inflow (`d omega_7^{CS} = I_8` on `M_4 x X_3`), dynamically coupling
   the `2D` orbifold fiber back to the `3D` hyperbolic open-weave bulk.
3. **Five-Regime Open-Flute Audit of `AGY-C7`:** On the truly unblocked open flute (`GL(2, Z)` including `det
   = -1`), non-orientable `m000` (`> 62 / 100`) crushes `m004` (`< 1 / 10`) by exact `phi^4` (and `m004 =
   m000^2` is not even primitive in `PGL(2, Z)`), while pure `SL(2, Z)` ties `m004 == m003` (`50 / 50`).
   Requiring both orientability (`SL(2, Z)`, needed for 4D chirality) and non-trivial spinor-twisted torsion
   (`|det(M + I)| > 1`) automatically drops both `m000` and `m003` (`|det(-LR + I)| = 1`) without `G:SE1`,
   elevating `m004` (`+LR`, `Smith = (1, 5)`) to unique `#1` (`> 1 / 3`) paired almost `1 : 1` with the `4`
   signed `t = 4` (`Smith = (1, 6)`) overtones (`combined share > 66 / 100`, naturally exciting `lcm(5, 6) =
   30`). `0 of 19.`

---

### Dated Correction (`2026-11-22`, `R-AGY002-V1`)

**2026-11-22 (`R-AGY002-V1` Erratum, `F-A2-09`):** Negative-trace lifts `-L^2 R, -LR^2` (`tr = -4`) satisfy `Smith(-M + I_2) = (1, 2)` (`E[2]`, not `(1, 6)` `E[6]`), halving the `t = 4` `E[6]` share from `59.4%` to `29.7%`. Also separates `2D` modular geodesics (`delta_{H^2} = 1`, `s = 2` convergent) from `3D` hyperbolic manifolds (`delta_{H^3} = 2`, `s = 2` divergent); see `A2-OW18 v3` `c4b79467c`.
