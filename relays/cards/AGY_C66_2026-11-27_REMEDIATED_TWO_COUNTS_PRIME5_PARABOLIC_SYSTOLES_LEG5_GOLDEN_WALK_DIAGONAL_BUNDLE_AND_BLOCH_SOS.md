# `Card AGY-C66` (`2026-11-27`) — Forward Remediation of Unpushed `AGY-C65`: Equal-Footing Two-Counts Remainder Scan Across Primes `p`, Unique `3 + 3` `(3, 3, 3)` Parabolic Systole Split at `p = 5`, Thread-Free `6`-Move Golden Polynomial on `Leg(5)`, Diagonal `O_{27} x Fiber_p` Bundles, & Full-Bloch-Sphere `PF5` `SOS` Systole Selection (`0 of 19`)

- **Seat / Code / Branch / Base Commit:** `agy` (`fam3-v1-high-01`) / `origin/agy/cusp-action-2026-11-20` / `d85143d13`
  (superseding unpushed local `AGY-C65` `81086e884..d85143d13` forward without history rewrite per custody rules;
  remote `origin/agy/cusp-action-2026-11-20` stands at `0d3fd5209` [`AGY-C64`, row `2038`]; frozen harvest branch
  `origin/agy/audit-2026-11-02` untouched at `4319f47e2`; sealed `AGY-C1..C65` files untouched)
- **Pre-Push Custody & Defect Disclosure (`AGY-C65` -> `AGY-C66`):** Pre-push audit of unpushed `AGY-C65` caught five
  defects before push: (`D1`) `P_3` in `c65` tested `P_3^-1 = [[2, -1], [1, 0]]` rather than `P_3 = C_omega^2 L C_omega^-2
  = [[0, 1], [-1, 2]]`; (`D2`) `E4` evaluated only the real equator and chiral poles rather than proving global `CP^1`
  bounds across all `(theta, alpha)` on the Bloch sphere; (`D3`) `c65_countercheck.py` ran Faddeev–LeVerrier on `1` of
  `12` `(p, mode)` pairs due to loop indentation, omitted an independent `Leg(5)` `6 x 6` polynomial check, echoed one
  producer flag, and did not compute `RPF3`/`RPF5` from its own objects; (`D4`) `definitions:` in the Claim Card needed
  explicit `L_diag`, `R_diag`, `H_q`, `r_i^+`, `T_leg`, and Bloch `psi(theta, alpha)` formulas for blind banking seats;
  (`D5`) stale `(28, 10, 10)` code comments alongside the true `(14, 5, 5)` Jacobian eigenvalues. `AGY-C66` closes all five.
- **Synced Premises:** `origin/main @ 1ac86a821` (`M22`, `M21`, Review `88` `B2018`, `P-885`, `B1983`, `B1989`,
  `B1993`–`B1995`, `B1998`, `B2000`–`B2017`), `agy-exp @ f250ed349`, `agy-002 @ 765c453a7`, `chat1 @ 19bc14af9`
- **Strict Scope (`0 of 19`):** Exact integer, rational, and symbolic algebraic listening on the foundational pair of
  integer counts `(a, b) in Z^2` (`GENESIS GM1, GM2, GM5b`) read modulo primes `p` on `(Z/pZ)^2 \ {(0, 0)}`, rays
  `((Z/pZ)^2 \ {(0, 0)}) / {+-1}`, and `P^1(F_p)`, plus diagonal `SL(2, Z)` bundles `O_{27} x Fiber_p` and parameter-free
  `S_3 = <C_omega, tau>` participation functionals across the full complex Bloch sphere `CP^1` of the `2`-dimensional
  golden eigenspace `E_{phi^2} subset Leg(5)`. Zero empirical constants, zero added parameters, zero hand-picked primes
  or threads; order-`30` line kept on hold per `M18` item `5`.

---

## Pre-Committed Expectations (`E1`–`E4`) and Falsification Controls (`PF1`–`PF5`)

1. **`E1` (`Equal-Footing All-Prime Classification of P^1(F_p) & Unique (3, 3, 3) Systole Parabolicity at p = 5`):**
   - **Expectation `E1a` (`Universal Cusp Triplet & Unique 3 + 3 Dual-Triplet Split at p = 5`):** On `(a, b)^T in Z^2`,
     `L = [[1, 1], [0, 1]]` and `R = [[1, 0], [1, 1]]` generate `C_omega = L R^-1 = [[0, 1], [-1, 1]]` (`C_omega^3 = -I_2`,
     order `3` on `P^1(F_p)` and rays) and the three `C_omega`-cycled parabolic cusp shears `P_1 = L`, `P_2 = C_omega L
     C_omega^-1 = R^-1 = [[1, 0], [-1, 1]]`, and `P_3 = C_omega^2 L C_omega^-2 = C_omega^-1 L C_omega = [[0, 1], [-1, 2]]`
     (`all det = 1, tr = 2`). For **every** prime `p >= 2`, `P_1, P_2, P_3` fix `T_{cusp} = {[1 : 0], [0 : 1], [1 : 1]}`
     (`size 3`), leaving `|R_p| = p - 2` lines (`0 at p = 2; 1 fixed line [1 : 2] at p = 3; uniquely 3 lines forming a
     single complementary C_omega-triplet T_{sys} = {[1 : 2], [1 : 3], [1 : 4]} at p = 5; and p - 2 >= 5 at all p >= 7`).
   - **Expectation `E1b` (`Exact (3, 3, 3) Systole Identification & Linearized 14 : 5 Tangent Split` + `PF1`):** The three
     `C_omega`-cycled systoles at `(3, 3, 3)`, `U_1 = L R = [[2, 1], [1, 1]]`, `U_2 = [[2, -1], [-1, 1]]`, and `U_3 =
     [[0, 1], [-1, 3]]` (`all det = 1, tr = 3, discriminant Delta = 3^2 - 4 = 5`), become parabolic modulo `p` (`(U_i +-
     I_2)^2 == 0 mod p` with `U_i != +-I_2 mod p`) **if and only if `p = 5`** (`certified across all 9 primes p in {2, 3,
     5, 7, 11, 13, 17, 19, 23}`), where `(U_i + I_2)^2 == 0 mod 5` fixes `[1 : 3], [1 : 4], [1 : 2] = T_{sys}`, while the
     `3 x 3` Jacobian of `W_{6,tr}` at `(t, t, t)` has exact eigenvalues `(4 t + 2, t + 2, t + 2) = (14, 5, 5)` at `t = 3`
     (`ratio 14 / 5`). Replacing `U_1 = L R` (`tr = 3`) by `L^2 R = [[3, 1], [1, 1]]` (`tr = 4`) yields `0` matches (`PF1`).

2. **`E2` (`Thread-Free 6-Move Spectrum on Two-Counts Remainders Across Primes p in {2, 3, 5, 7, 11, 13, 17, 19, 23}`):**
   - **Expectation `E2a` (`Universal Mirror Pairing on Count Remainders` + `PF2`):** Under `W_{6,omega} = sum_{j=0}^2
     C_omega^j (L + R) C_omega^-j` and order-`3` `C_{3,omega} = -C_omega = C_omega^4`, mirror `tau = [[0, 1], [1, 0]]`
     satisfies `tau L tau = R`, `tau C_{3,omega} tau = C_{3,omega}^2`, and `tau W_{6,omega} tau = W_{6,omega}`, forcing
     **`100%` exact `q = 1 ~= q = 2` charged pairing over `Z[x]` for every prime `p >= 2`** on `P^1(F_p)`, `Rays(p)`, and
     `Vecs(p)` (`dropping inverse/mirror partners to the chiral 3-move half-walk breaks q = 1 == q = 2 on P^1(F_5)`, `PF2`).
   - **Expectation `E2b` (`Exact Z[x] Factorizations & Pure-Cover Golden Mode Emergence at p = 5` + `PF3`):** At `p = 5`,
     on `P^1(F_5)`: `P_{neu}(x) = (x - 6)(x - 2)` (`+2` mode `1_{T_{sys}} - 1_{T_{cusp}}`), `P_{chg}(x) = x^2 + x - 3`; on
     `6`-dim `Leg(5)` (`(2 / 5) = -1, (-1 / 5) = +1`): `det(x I - W_{6,omega}|_{Leg(5)}) = (x^2 - 20)(x^2 - 3 x + 1)^2`;
     on `Rays(5)`: `P_{neu}(x) = (x - 6)(x - 2)(x^2 - 20)`, `P_{chg}(x) = (x^2 - 3 x + 1)(x^2 + x - 3)`; on `Vecs(5)`:
     `P_{neu}(x) = x^4 (x - 6)(x - 2)(x^2 - 20)`, `P_{chg}(x) = (x^2 - 3 x - 3)^2 (x^2 - 3 x + 1)(x^2 + x - 3)`. Across
     `p in {2, 3, 5, 7, 11, 13, 17, 19, 23}` (`scoped explicitly`), `dim ker_Q(W_{6,omega}^2 - 3 W_{6,omega} + I) > 0` on
     `Vecs(p)` holds only at `p in {5, 23}`, and **`p = 5` is unique in `{2..23}` with `dim = 0` on `P^1(F_p)` and `dim = 4`
     on `Rays(p)`/`Vecs(p)`** (`whereas p = 23 has dim = 4 already on P^1(F_23)`, `PF3`).

3. **`E3` (`Diagonal SL(2, Z) Bundle O_{27} x Fiber_p Across p in {2, 3, 5, 7}`):**
   - **Expectation `E3` + `PF4`:** Under `L_{diag} = (L_{tr}, L)`, `R_{diag} = (R_{tr}, R)` and order-`3` `g_{C_3} = S^2
     R^-1 L = (C_{tr}, -C_0)` (`C_0 = R^-1 L = L^-1 C_omega L`; misaligning `(C_{tr}, -C_omega)` breaks `[W_6, C_{diag}]
     == 0`, `PF4`), all tested bundles form `1` transitive `<L, R>`-orbit with `100%` `q = 1 ~= q = 2` pairing: `p = 2`
     (`216` pts) is `(a')` (`72 / 72`); `p = 3` lines (`288` pts) is `(a)` (`95 / 95`); at `p = 5`, `O_{27} x P^1(F_5)`
     (`d_0 = d_1 = 144`) halves `136 / 144` leaving monic `Z[y]` (`y = 2 x`) unpaired **`(y^2 - 2 y - 12)^2 (y^2 + 2 y -
     12)^2`**, `O_{27} x Leg(5)` (`d_0 = d_1 = 144`) halves `136 / 144` leaving **`(y^2 - 6 y + 4)^2 (y^2 + 6 y + 4)^2 =
     2^8 (x^2 - 3 x + 1)^2 (x^2 + 3 x + 1)^2`**, and odd-parity `Vecs(5)` (`d_0 = d_1 = 288`) halves `0 / 288`; at `p = 7`
     lines (`576` pts), `182 / 190` halve leaving `(y^2 - 4 y - 4)(y^2 - 2 y - 4)(y^2 + 2 y - 4)(y^2 + 4 y - 4)`.

4. **`E4` (`Exact Full-Bloch-Sphere CP^1 Sum-of-Squares Hierarchy on E_{phi^2} subset Leg(5)`):**
   - **Expectation `E4` + `PF5`:** Across the **entire complex Bloch sphere** `psi(theta, alpha) = cos(theta) e_+ +
     exp(i alpha) sin(theta) e_- in E_{phi^2}` (`(theta, alpha) in R^2`):
     1. `W_{sys}(theta, alpha) = (5 + sqrt(5)) / 10`, `W_{cusp}(theta, alpha) = (5 - sqrt(5)) / 10`, and
        **`W_{sys} / W_{cusp} = (3 + sqrt(5)) / 2 = phi^2`** identically;
     2. **`3/10 - I_4(theta, alpha) = (1/10) sin^2(alpha) sin^2(2 theta) >= 0`** (`global CP^1 minimum 1/5 at the 2 chiral
        poles alpha = +-pi/2, theta = pi/4; global CP^1 maximum 3/10 identically along the continuous real mirror-equator
        sin(alpha) = 0`, where `d I_4 / d theta == 0`, `PF5`);
     3. **`11/90 - I_6(theta, alpha) = (1/45)[sin(theta)(4 cos^2(theta) - 1)]^2 + (2/15)(sin(alpha) sin(theta) cos(theta))^2
        + (4/15)(sin(alpha) sin^2(theta) cos(theta))^2 >= 0`** (`chiral poles 2/45; real equator 1/9 + (1/90) cos(6 theta)
        with equator minimum 1/10 on the mirror-odd orbit and strict global CP^1 maximum 11/90 iff [psi] lies on the single
        3-element C_omega-orbit of mirror-even single-systole-peaked states`).

0 of 19.
