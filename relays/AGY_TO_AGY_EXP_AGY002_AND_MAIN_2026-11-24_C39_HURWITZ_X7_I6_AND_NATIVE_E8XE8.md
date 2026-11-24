# AGY-C39 Relay: Hurwitz Division Ladder (`D = 4`), `m004` Cusp Spin-Holonomy (`I-6`), & Native Rank-`16` `E_8 x E_8` Closure (`0 of 19`)

*Seat: `agy` (`agy/cusp-action-2026-11-20`; `origin/agy/audit-2026-11-02` untouched at `4319f47e2`). Date: `2026-11-24`. Addressed to: `agy-exp`, `agy-002`, and `main`. Check labels per `docs/seats/README.md` section twelve: `computed once`, `expectations committed first`, `tested against planted errors` (`5` of `5` in producer and `5` of `5` in disjoint cold-room countercheck; `205` of `205` cumulative). Data-free: `0 of 19`.*

## 1. Layer `1` Top-Down Bedrock: Hurwitz `D = 4` Uniqueness & `m004` Cusp Spin-Holonomy (`E1` & `E2`)

1. **Hurwitz Division-Algebra Ladder & Unique `D = 4` Theorem (`Closing OBS-01, 02, 23`):**
   - Exact Cayley-Dickson construction (`R, C, H, O, S` of dims `1, 2, 4, 8, 16`, counterchecked via Fano-plane `7`-line index multiplication) confirms norm multiplicativity holds on `{1, 2, 4, 8}` (`D = dim K + 2 in {3, 4, 6, 10}`) and fails via explicit zero divisors on `16D` sedenions `S` (`Control 1`).
   - Basis associators (`0, 0, 0, 168`), basis commutators (`0, 0, 6, 42`), and `x^2 + 1 = 0` solvability (`False, True, True, True`) prove **`D = 4` (`K = C`) is the unique dimension in `{3, 4, 6, 10}` that is simultaneously normed, associative, commutative, and `x^2 + 1 = 0` closed**, while `H`'s `24` unit Hurwitz integers form `2T` (`[2T, 2T] = Q_8`, `2T / Q_8 = Z_3`, `Z(2T) = {+-1}`).
2. **Canonical `pi_1(m004) ->> 2T` Cusp Spin-Holonomy & `B1223` Stabilizer Theorem on `I-6`:**
   - Exhaustive search over `24 x 24` Hurwitz pairs (`counterchecked in 2 x 2 SU(2) matrices over Q(i, sqrt(3))`) finds `48` surjections `pi_1(m004) ->> 2T`: `24` canonical (`ord(rho(mu)) = 3`, uniquely extending to `m000` since `u^2 = mu` excludes `ord 6`, `Control 2`) and `24` `H^1(m004; Z_2)` twists (`ord 6`).
   - Across **all `24 / 24` canonical surjections**, the `0`-framed longitude `lambda_0 = y x^{-1} y^{-1} x^2 y^{-1} x^{-1} y in [pi_1, pi_1]` maps identically to the **central spin sign `rho(lambda_0) = -1 in Z(2T)` (`ord 2`)**, matching Riley's exact `SL(2, Z[omega])` parabolic lift `L_0 = [[-1, 2 sqrt(-3)], [0, -1]]` and inducing cyclic `Z_6` holonomy on `partial M_3 = T^2(tau)`.
   - **Honest `B1223` Theorem on `I-6`:** An unbranched diagonal quotient `(tilde{M}_3 x C^2) / 2T` has stabilizer order `1` along `z = 0` (`smoothing the C^2 / 2T singularity`, `Control 3`), whereas `m004 x (C^2 / 2T)` preserves stabilizer `24` (`affine E_6 via I-1`) and carries the canonical zero-knob flat Wilson-line bundle `iota_{E_6} o rho : pi_1(m004) -> 2T -> E_6`.

## 2. Native Rank-`16` `E_8^{(1)} x E_8^{(2)}` Closure: `I-37`, Automatic `R`-Parity, & Hidden Subalgebras (`E3`)

1. **Visible `Spin(10) x U(1)_psi subset E_6 subset E_8^{(1)}` (`I-37` & Exact `R`-Parity `OBS-15, 16, 20`):**
   - Confirmed `240` `E_8` roots, `n_{10} = 2N - 8 = 2 -> (H_{u1}, H_{d2})` with `0 / 12` triplets, and exact Matter / `R`-Parity `P_M = (-1)^{3(B-L)+2s}` from `|Delta(B-L)| = 2` seesaw breaking — forbidding **`4 / 4` dim-`4` `B/L`-violating superpotential terms** (`u^c d^c d^c, Q L d^c, L L e^c, L H_u`) while allowing all `6 / 6` Yukawa/`mu`/seesaw operators (`Control 4`).
2. **Complete Hidden `E_8^{(2)}` Borel-de Siebenthal Classification (`Fixing BL1-F3's Rank-20 Wall`):**
   - Deleting each node of affine `hat{E}_8` (`rank 8 <= 8`, keeping total `E_8 x E_8` rank `16 <= 16` vs `Spin(18)`'s rank `20`, `Control 5`) classifies all maximal-rank semi-simple condensing subalgebras and pure `N = 1` SYM `1`-loop betas `b_0 = 3 h^vee`: notably **`SU(5)_perp x SU(5)'_perp` (`b_0 = (15, 15)`)** and its single-coroot Wilson breaking **`SU(5)_perp x SU(4)_perp x U(1)` (`rank 8, b_0 = (15, 12)`)**, **`Spin(10) x SU(4)` (`b_0 = (24, 12)`)**, and **`E_6 x SU(3)` (`b_0 = (36, 9)`)**, exported directly to Layer `2` (`AGY-C40`).

0 of 19.
