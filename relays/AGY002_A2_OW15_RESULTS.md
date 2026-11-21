# AGY-002 Results Relay: Card `A2-OW15` — Deep Foundations: Explicit `Cl(t, s)` Lorentzian `(1, 3)` Selection (`X22`), Conformal `xi = 1/6` Induced Black-Hole Entropy (`X2`), and `X1` / `X37` Boundary Ledger (`0 of 19`)

- **Seat / Branch:** `AGY-002` on `agy-002/verify`
- **Empirical Inputs:** **`0 of 19`** (pure `Cl(t, s)` matrix representation theory over `Z[i]`, hyperbolic PDE principal-symbol analysis, conical-defect heat-kernel replica calculus, and finite-dimensional unitary / `D_5` Lie-algebra topological audits).
- **Custody Chain:**
  - Pre-Registration Card: `relays/cards/AGY-002_A2-OW15_clifford-lorentzian-signature-conformal-bh-entropy-and-qm-gerbe-boundary.md` (`b1df97a64`)
  - Authoritative `v1` Producer (`all_gates_passed = true`, zero errata): `relays/a2_ow15/verify_a2_ow15.py` (`c213aef6a`, `SCRIPT_SHA256 = ea4ed0fa5f8b2f31c6462a40f663e825e23ba1d8705466f0e620a5172232d857`) and `relays/a2_ow15/a2_ow15_results.json` (`98be8ec13`, `OUTPUT_SHA256 = e35ac5f00b3c787273a23a4ab7e206e5724f139239b45a049b83518ca4bfd66e`)
  - Independent Cold-Room Zero-Trust Referee (`all_gates_passed = true`, `20 / 20` gates, strictly cold-room sealed unread): `relays/a2_ow15_referee/referee_a2_ow15.py` (`26dd32a4d`, `SCRIPT_SHA256 = 64b47c280ab854341c5266dd5ea74bd07e1f2cf36623d058902635d17f8d23ae`) and `relays/a2_ow15_referee/a2_ow15_referee_results.json` (`0f4380af3`, `OUTPUT_SHA256 = 4d8f05b63a9f9fad7b829f81ac6abd76b00799d2b7c17f09a049e5f3c584b878`)
  - **Cross-Check Verdict:** **`0` mismatches across all `257 / 257` compared fields** (`180` in `OW15-A`, `41` in `OW15-B`, `24` in `OW15-C`, `11` in `OW15-D`, `1` global) plus `4 / 4` planted faults (`PF-OW15-1..4`) detected identically. Disjoint referee methods: Weyl/chiral block-off-diagonal recursive Bott construction + `sympy.Matrix.nullspace()` on `d^2`-dim Sylvester equations for both `B` and `H_norm` (disjoint from `Z^k X/Y` Pauli chains & bitmask search), Hurwitz zeta `zeta_H(-1, a)` at `60` dps + direct `t -> 0` Bessel-Laplace conical Laurent series, `10`-trial `U(3)` Cayley transform `U = (I - i H)(I + i H)^{-1}` at `60` dps (`p = 2` drift `< 2 / 10^61`, disjoint from Ginibre/QR), and explicit `45`-dim skew-symmetric `so(10)` basis + `D_5` Cartan Smith Normal Form `[1, 1, 1, 1, 4]` + explicit `P^vee / Q^vee` weight enumeration on `16_+, 16_-, 10, 45` (closing producer `v1`'s integer literal `center_order_spin10 = 4` by explicit matrix/lattice proof). Exact `0` discrepancy across all algebraic/symbolic/boolean fields and `<= 5 / 10^18` on the `3` printed Schwarzschild display strings.

---

## 1. Task `OW15-A`: Explicit `Cl(t, s)` Lorentzian `(1, 3)` Signature Selection (`X22`)

1. **Exhaustive `11`-Signature Matrix Table (`D = 4, 6, 7`, `0` Clifford Residual Across All `11`):**
   - `D = 4`:
     - `(0, 4)` Euclidean (`4 x 4`): `vol^2 = +1`, `Weyl = H` (symplectic, `L^* = L`), elliptic (`0` time), `pos_kin = False`.
     - **`(1, 3)` Lorentzian (`4 x 4`)**: `vol^2 = -1`, **`Weyl = C` (complex chiral, `L^* = R`, `B gamma_5^* B^{-1} = -gamma_5`)**, strictly hyperbolic (`w = +-1`), **`pos_kin = True`**.
     - `(2, 2)` Kleinian (`4 x 4`): `vol^2 = +1`, `Weyl = R` (Majorana-Weyl, `L^* = L`), ultrahyperbolic (`w = +-i sqrt(3)`), `pos_kin = False`.
   - `D = 6`:
     - `(0, 6)`: `vol^2 = -1`, `Weyl = C`, elliptic, `pos_kin = False`.
     - **`(1, 5)` Lorentzian (`8 x 8`)**: `vol^2 = +1`, **`Weyl = H` (self-conjugate symplectic-Weyl, enabling chiral `6D` `I_8` anomaly inflow `A2-OW5`/`OW11`)**, strictly hyperbolic, **`pos_kin = True`**.
     - `(2, 4)`: `vol^2 = -1`, `Weyl = C`, ultrahyperbolic, `pos_kin = False`.
     - `(3, 3)`: `vol^2 = +1`, `Weyl = R`, ultrahyperbolic, `pos_kin = False`.
   - `D = 7`:
     - `(0, 7)`: `Dirac = R`, elliptic, `pos_kin = False`.
     - **`(1, 6)` Lorentzian (`8 x 8`)**: `Dirac = H`, strictly hyperbolic, **`pos_kin = True`**.
     - `(2, 5)`: `Dirac = H`, ultrahyperbolic, `pos_kin = False`.
     - `(3, 4)`: `Dirac = R`, ultrahyperbolic, `pos_kin = False`.
2. **Exact `8 x 8` Chirality Factorization `(1, 5) = (1, 3) + (0, 2)`:**
   - Verified `Gamma_{(1,5)} == +(gamma_5^{(1,3)} kron gamma_3^{(0,2)})` with `0` matrix residual (and independently via explicit unitary intertwiner from Bott to KK basis by the referee).
3. **Unique Selection Theorem (`X22`):**
   - **`(1, 3)` is uniquely selected (`1 of 3`) in `D = 4`** even by pure Clifford spinor reality alone (`Weyl = C`, `L^* = R`), and **`(1, 3) -> (1, 5) -> (1, 6)` is uniquely selected (`1 of 48` towers)** across `D = 4, 6, 7` by positive-definite Dirac kinetic norm, strictly hyperbolic Cauchy evolution, Euclidean internal `T^2/Z_2` `(0, 2)` & `H^3/Gamma` `(0, 3)`, and `6D` chiral `I_8` anomaly inflow.

---

## 2. Task `OW15-B`: Conformal `xi = 1/6` Induced Black-Hole Entropy (`X2`)

1. **Exact Conical-Defect Replica Calculus (`(alpha d/d_alpha - 1)|_{alpha=1}`):**
   - Exact Bernoulli cone coefficients `B_2(0) = +1/6` (boson) and `B_2(1/2) = -1/12` (antiperiodic fermion) verified both algebraically and via `60`-dps Hurwitz zeta `zeta_H(-1, a) = -B_2(a)/2` (`0` error), yielding exact weights matching bulk `1 / G_ind` (`A2-OW4` & `A2-OW8`) identically across all `4` species:
     - Real scalar (`xi`): `w_ent = 1/6`, `w_contact = -xi`, `w_tot = 1/6 - xi` (`0` at conformal `xi = 1/6`).
     - Weyl / Majorana fermion: `w_ent = 1/6`, `w_contact = 0`, `w_tot = 1/6`.
     - Massive Proca vector (`3` dof): `w_ent = 1/2`, `w_contact = -1` (Kabat edge term), `w_tot = -1/2`.
     - Massless gauge vector (`2` dof): `w_ent = 1/3`, `w_contact = -1` (Kabat edge term), `w_tot = -2/3`.
2. **Exact Equality `S_ent + S_contact == A / (4 G_ind)` at `A2-OW8`'s `c_log = +16` Spectrum:**
   - On `33` massive `Spin(10)` Proca vectors + `3` heavy Majorana `nu^c` + `8` conformal `xi = 1/6` `2H` scalars:
     - Entanglement piece alone: `c_log_ent = -55/3 < 0` (wrong sign without contact terms!).
     - Contact / Wald-Noether piece (`33` Kabat vector edge `+33` + `8` conformal scalar `+4/3`): `c_log_contact = +103/3 > 0`.
     - **Exact sum:** **`c_log_ent + c_log_contact = -55/3 + 103/3 = +16 == c_log(1 / G_ind)`**, certifying `S_BH == A / (4 G_ind)` identically!
3. **Exact `4D` Schwarzschild (`chi = 2`, Ricci-flat `C^2 = E_4`) Matter Logarithmic Correction `2 (c - a) ln(A / l_Pl^2)`:**
   - IR `G_SM 2H` (`45` light Weyl): `c = 287/120`, `a = 1999/720`, `2(c - a) = -277/360`.
   - IR `G_SM 2H` (`48` Weyl incl `nu^c`): `c = 37/15`, `a = 127/45`, `2(c - a) = -32/45`.
   - UV `Spin(10) real-10`: `c = 347/60`, `a = 383/45`, `2(c - a) = -491/90`.

---

## 3. Task `OW15-C`: Theorem-Grade Boundary Ledger for `X1` (QM) & `X37` (`H^2` Gerbe)

1. **`X1` Quantum Mechanics Boundary:**
   - Exact algebraic `3 x 3` DFT `F_3` (`Q(i, sqrt(3))`) AND `10`-trial `U(3)` Haar (producer, `< 1 / 10^54`) / Cayley (referee, `< 2 / 10^61`) ensembles prove `p = 2` (Born `L^2` rule) is the **unique** unitarily conserved `L^p` norm among `p in {1, 2, 3, 4}` (`|drift(F_3)| > 1/3` and Haar/Cayley drift `> 1/5` for all `p != 2`).
   - Honest boundary verdict: `X1_L2_born_norm_given_unitarity = PROVED`, whereas `X1_hilbert_space_superposition_and_measurement = EXTERNAL_AXIOM` (not derived from `7D` geometry).
2. **`X37` `H^2` / `H^3` Gerbe Boundary:**
   - Explicit `so(10)` (`dim = 45`, `rank = 5`, `D_5` Cartan SNF `[1, 1, 1, 1, 4]`, `center(Spin(10)) = Z_4`, `ker(Spin(10) -> SO(10)) = Z_2`, `pi_1(Spin(10)) = pi_2(Spin(10)) = 0`, `pi_3(Spin(10)) = H^3(Spin(10), Z) = Z`) certifies `X37_abelian_7d_cs_3form_inflow_gerbe = DERIVED` (`A2-OW5`), while `X37_nonabelian_2form_gerbe_uv_quantization = OPEN_UV_BOUNDARY`.

---

## 4. Task `OW15-D`: `4 / 4` Planted Faults (`PF-OW15-1..4`)

- `PF-OW15-1` (`D = 4` Kleinian `(2, 2)`): **CAUGHT** — real `Majorana-Weyl` (`R`, `L^* = L`) and ultrahyperbolic (`w = +-i sqrt(3)`).
- `PF-OW15-2` (omit Kabat Proca contact term): **CAUGHT** — `c_log_total` plunges from `+16` to `-17 < 0`.
- `PF-OW15-3` (shift `8` `2H` scalars to minimal `xi = 0`): **CAUGHT** — `c_log_total` shifts from `+16` to `44/3 != 16`.
- `PF-OW15-4` (`L^4` norm under exact `F_3`): **CAUGHT** — exact `drift = -2/3 != 0`.
