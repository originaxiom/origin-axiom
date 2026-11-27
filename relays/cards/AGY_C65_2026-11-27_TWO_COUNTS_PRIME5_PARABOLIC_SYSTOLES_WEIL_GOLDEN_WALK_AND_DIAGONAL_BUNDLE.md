# `Card AGY-C65` (`2026-11-27`) — Equal-Footing Two-Counts Remainder Scan Across Primes `p`, Unique `3 + 3` `(3, 3, 3)` Parabolic Systole Split at `p = 5`, Thread-Free `6`-Move Golden Polynomial on `Leg(5)`, Diagonal `O_{27} x Fiber_p` Bundles, & `PF5` Sixth-Order Systole Orbit Selection (`0 of 19`)

- **Seat / Code / Branch / Base Commit:** `agy` (`fam3-v1-high-01`) / `origin/agy/cusp-action-2026-11-20` / `0d3fd5209`
  (continuing cleanly after `AGY-C64`; frozen harvest branch `origin/agy/audit-2026-11-02` untouched at `4319f47e2`;
  sealed `AGY-C1..C64` untouched)
- **Synced Premises:** `origin/main @ a3494f066` (`M21`, `P-885` `T1`–`T6`, `B1983`, `B1989`, `B1993`–`B1995`, `B1998`,
  `B2000`–`B2017`), `agy-exp @ f250ed349`, `agy-002 @ 765c453a7`, `chat1 @ 19bc14af9`
- **Strict Scope (`0 of 19`):** Exact integer, rational, and symbolic algebraic listening on the foundational pair of
  integer counts `(a, b) in Z^2` (`GENESIS GM1, GM2, GM5b`) read modulo primes `p` on `(Z/pZ)^2 \ {(0, 0)}`, rays
  `((Z/pZ)^2 \ {(0, 0)}) / {+-1}`, and `P^1(F_p)`, plus diagonal `SL(2, Z)` bundles `O_{27} x Fiber_p` and parameter-free
  `S_3 = <C_omega, tau>` participation functionals on the `2`-dimensional golden eigenspace of `Leg(5)`. Zero empirical
  constants, zero added parameters, zero hand-picked primes or threads (`equal-footing scan across primes`), zero Standard
  Model pass/fail cells; order-`30` line kept on hold per `M18` item `5`.

---

## Pre-Committed Expectations (`E1`–`E4`) and Falsification Controls (`PF1`–`PF5`)

1. **`E1` (`Equal-Footing All-Prime Classification of P^1(F_p) & Unique (3, 3, 3) Systole Parabolicity at p = 5`):**
   - **Expectation `E1a` (`Universal Cusp Triplet & Unique 3 + 3 Dual-Triplet Split at p = 5`):** On `(a, b)^T in Z^2`,
     `L = [[1, 1], [0, 1]]` and `R = [[1, 0], [1, 1]]` generate `C_omega = L R^-1 = [[0, 1], [-1, 1]]` (`C_omega^3 = -I_2`,
     order `3` on `P^1(F_p)` and rays) and the three `C_omega`-cycled parabolic cusp shears `P_1 = L`, `P_2 = C_omega L
     C_omega^-1 = R^-1`, and `P_3 = C_omega^2 L C_omega^-2 = [[2, -1], [1, 0]]` (`all det = 1, tr = 2`). For **every**
     prime `p >= 2`, `P_1, P_2, P_3` fix the pairwise-distinct `C_omega`-triplet `T_{cusp} = {[1 : 0], [0 : 1], [1 : 1]}`
     of size `3`, leaving `|R_p| = (p + 1) - 3 = p - 2` lines (`0 at p = 2; 1 fixed line [1 : 2] at p = 3; uniquely 3
     lines forming a single complementary C_omega-triplet T_{sys} = {[1 : 2], [1 : 3], [1 : 4]} at p = 5; and p - 2 >= 5
     at all p >= 7, never a single C_omega-orbit since ord_{P^1}(C_omega) = 3`).
   - **Expectation `E1b` (`Exact (3, 3, 3) Systole Identification & Linearized 14 : 5 Tangent Split` + `PF1`):** The three
     `C_omega`-cycled systoles at `(3, 3, 3)`, `U_1 = L R = [[2, 1], [1, 1]]`, `U_2 = [[2, -1], [-1, 1]]`, and `U_3 =
     [[0, 1], [-1, 3]]` (`all det = 1, tr = 3, discriminant Delta = 3^2 - 4 = 5`), become parabolic modulo `p` (`(U_i +-
     I_2)^2 == 0 mod p` with `U_i != +-I_2 mod p`) **if and only if `p = 5`** (`verified across all 9 primes p in {2, 3, 5,
     7, 11, 13, 17, 19, 23}`), where `(U_i + I_2)^2 == 0 mod 5` fixes `[1 : 3], [1 : 4], [1 : 2]` — **identically matching
     `R_5 = T_{sys}`** — while the `3 x 3` Jacobian of the `6`-move trace sum `W_{6,tr}` at `(3, 3, 3)` has exact
     eigenvalues `(14, 5, 5)` (`ratio 14 / 5`). Replacing `U_1 = L R` (`trace 3`) by `L^2 R = [[3, 1], [1, 1]]` (`trace 4`)
     yields `0` parabolic systole matches across `{2..23}` (`PF1`).

2. **`E2` (`Thread-Free 6-Move Spectrum on Two-Counts Remainders Across Primes p in {2, 3, 5, 7, 11, 13, 17, 19, 23}`):**
   - **Expectation `E2a` (`Universal Mirror Pairing on Count Remainders` + `PF2`):** Under `W_{6,omega} = sum_{j=0}^2
     C_omega^j (L + R) C_omega^-j` and order-`3` charge generator `C_{3,omega} = -C_omega = C_omega^4`, mirror `tau =
     [[0, 1], [1, 0]]` satisfies `tau L tau = R`, `tau C_{3,omega} tau = C_{3,omega}^-1`, and `tau W_{6,omega} tau =
     W_{6,omega}`, forcing **`100%` exact `q = 1 ~= q = 2` charged pairing over `Z[x]` for every prime `p >= 2`** on
     `P^1(F_p)`, rays, and `(Z/pZ)^2 \ {(0, 0)}` (`contrasted with scalar trace orbits O_p where 0 modes pair for p >= 5`;
     dropping inverse/mirror partners to the chiral `3`-move half-walk breaks `q = 1 == q = 2` on `P^1(F_5)`, `PF2`).
   - **Expectation `E2b` (`Exact Z[x] Factorizations & Pure-Cover Golden Mode Emergence at p = 5` + `PF3`):** At `p = 5`:
     - `P^1(F_5)` (`6` lines): `P_{neu}(x) = (x - 6)(x - 2)` (`+2` eigenvector `1_{T_{sys}} - 1_{T_{cusp}}`),
       `P_{chg}(x) = x^2 + x - 3`;
     - `6`-dim even-parity Legendre quadratic-character block `Leg(5)` (`chi_2(2) = -1`):
       `det(x I - W_{6,omega}|_{Leg(5)}) = (x^2 - 20)(x^2 - 3 x + 1)^2`;
     - `Rays(5)` (`12` rays): `P_{neu}(x) = (x - 6)(x - 2)(x^2 - 20)`, `P_{chg}(x) = (x^2 - 3 x + 1)(x^2 + x - 3)`;
     - `F_5^2 \ {(0, 0)}` (`24` vectors): `P_{neu}(x) = x^4 (x - 6)(x - 2)(x^2 - 20)`,
       `P_{chg}(x) = (x^2 - 3 x - 3)^2 (x^2 - 3 x + 1)(x^2 + x - 3)`.
     Across all `9` primes `p in {2, 3, 5, 7, 11, 13, 17, 19, 23}` (`scoped explicitly per Review 87`), `ker_Q(W_{6,omega}^2
     - 3 W_{6,omega} + I)` is nonzero only at `p in {5, 23}` (`0` across all `7` primes `{2, 3, 7, 11, 13, 17, 19}`), and
     **`p = 5` is the unique prime in `{2..23}` where the golden kernel vanishes on `P^1(F_p)` (`dim 0`) and emerges purely
     in the quadratic cover `Leg(5)` (`dim 4` on rays/vectors; whereas `p = 23` already has `dim 4` on `P^1(F_23)` via
     genus-`2` `X_0(23)`, `PF3`)**.

3. **`E3` (`Diagonal SL(2, Z) Bundle O_{27} x Fiber_p Across p in {2, 3, 5, 7}`):**
   - **Expectation `E3` + `PF4`:** On Markoff traces, `C_{tr} = R_{tr}^-1 o L_{tr}` pairs in `SL(2, Z)` with `g_{C_3} =
     S^2 R^-1 L = -C_0 = [[-1, -1], [1, 0]]` (`exact order 3 in SL(2, Z)`, where `L C_0 L^-1 = C_omega` and `L W_{6,C_0}
     L^-1 = W_{6,omega}`; misaligning `(C_{tr}, -C_omega)` breaks `[W_6, C_{diag}] == 0`, `PF4`). Across `p in {2, 3, 5, 7}`:
     all diagonal bundles form **`1` single transitive `<L, R>`-orbit with `100%` `q = 1 ~= q = 2` pairing**; `p = 2`
     (`216` pts) satisfies `100%` Category-`(a')` halving (`72 / 72`); `p = 3` lines & rays (`288` pts) satisfy `100%`
     Category-`(a)` halving (`95 / 95`); at `p = 5`, `O_{27} x P^1(F_5)` (`432` pts, `d_0 = d_1 = 144`) halves `136 / 144`
     leaving exact monic `Z[y]` (`y = 2 x`) unpaired **`(y^2 - 2 y - 12)^2 (y^2 + 2 y - 12)^2`**, `O_{27} x Leg(5)` (`d_0 =
     d_1 = 144`) halves `136 / 144` leaving **`(y^2 - 6 y + 4)^2 (y^2 + 6 y + 4)^2 = 2^8 (x^2 - 3 x + 1)^2 (x^2 + 3 x +
     1)^2`**, and the `12`-dim odd-parity spinor sector (`d_0 = d_1 = 288`) halves `0 / 288`; at `p = 7` lines (`576` pts),
     `182 / 190` halve leaving `(y^2 - 4 y - 4)(y^2 - 2 y - 4)(y^2 + 2 y - 4)(y^2 + 4 y - 4)` (`0` golden factors).

4. **`E4` (`Exact PF5 Symmetry-Breaking Hierarchy on the 2D Golden Eigenspace E_{phi^2} of Leg(5)`):**
   - **Expectation `E4` + `PF5`:** On the `2`-dim eigenspace `E_{phi^2} = ker(W_{6,omega}|_{Leg(5)} - ((3 + sqrt(5))/2) I_6)`,
     every unit state satisfies **`W_{sys} / W_{cusp} = (3 + sqrt(5)) / 2 = phi^2`**; `2`-body quartic participation
     `I_4(psi) = sum_{i=1}^6 |psi_i|^4` equals **`1/5`** at the two chiral poles `q = 1, 2` and hits an exact continuous
     `U(1)` ceiling **`3/10`** identically along the real mirror-equator (`d I_4 / d theta == 0`, `PF5`); `3`-body
     sixth-order participation `I_6(psi) = sum_{i=1}^6 |psi_i|^6` equals **`2/45`** at the chiral poles and **`1/9 +
     (1/90) cos(6 theta)`** along the real equator, achieving its global maximum **`11/90`** strictly on the single
     `3`-element `C_omega`-orbit of mirror-even single-systole-peaked states (`and equator minimum 1/10 on the dual
     mirror-odd orbit`).

0 of 19.
