# Card AGY-C39: Hurwitz Division Ladder (`D = 4`), `m004` Cusp Spin-Holonomy (`I-6`), & Native Rank-`16` `E_8 x E_8` Closure (`0 of 19`)

1. **The package and the question, in a sentence:** Executing Layer `1` of the Top-Down Synthesis, do Cayley-Dickson division algebras (`dim in {1, 2, 4, 8}`) uniquely select `D = 4`, what peripheral cusp holonomy `rho: pi_1(m004) ->> 2T` and `B1223` stabilizer structure govern `I-6`, and which native rank-`<= 8` condensing subalgebras live inside `E_8^{(2)}` (`total rank <= 16`, `0 of 19`)?

2. **What will be delivered, and what done means:** Pre-registered zero-float producer `relays/agy_2026-11-24_c38/c39_hurwitz_x7_i6_and_native_e8xe8_closure.py`, `SCRIPT_SHA256.txt`, first-run `c39_out.json` with `OUTPUT_SHA256.txt` (`computed once`, `expectations committed first`), disjoint cold-room `c39_countercheck.py` (`tested against planted errors`), updated `relays/STATUS_AGY.md`, and relay testing:
   - **Expectation E1 (Hurwitz Division-Algebra Ladder `{1, 2, 4, 8} <-> D in {3, 4, 6, 10}` & Unique `D = 4` Theorem):**
     - Construct exact rational Cayley-Dickson algebras `R, C, H, O` (`dim 1, 2, 4, 8`) and `16D` sedenions `S`. Prove norm multiplicativity holds on `{1, 2, 4, 8}` and fails via explicit zero divisors on `16D` `S`; prove `O` has `168` nonzero basis associators, `H` & `O` have `6` & `42` nonzero basis commutators, and `R` has `0` roots of `x^2 + 1 = 0` — uniquely selecting `D = dim K + 2 = 4` (`K = C`) as normed, associative, commutative, and `x^2 + 1 = 0` closed (`closing OBS-01, 02, 23`).
     - Enumerate all `24` unit Hurwitz integers `2T subset H^x` (`D_4` root shell), verifying `[2T, 2T] = Q_8` (`order 8`), `2T / Q_8 = Z_3`, and unique central involution `-1`.
   - **Expectation E2 (`pi_1(m004) ->> 2T` Cusp Spin-Holonomy `(ord 3, -1)` & `B1223` Stabilizer Theorem on `I-6`):**
     - Prove `Hom(pi_1(m004), 2T)` has exactly `48` surjections: `24` canonical (`meridian ord 3`, extending over `m000` via `u^2 = mu`) and `24` `H^1(m004; Z_2)` twists (`meridian ord 6`).
     - Prove all `24 / 24` canonical surjections map the `0`-framed longitude `lambda_0 in [pi_1, pi_1]` identically to central `rho(lambda_0) = -1 in Z(2T)` (`ord 2`, matching Riley's `SL(2, Z[omega])` parabolic lift `L_0 = [[-1, 2 sqrt(-3)], [0, -1]]` and inducing `Z_6 = <rho(mu), -1>` on `partial M_3 = T^2(tau)`).
     - Prove per `B1223` that an unbranched diagonal quotient `(tilde{M}_3 x C^2) / 2T` has zero-section stabilizer order `1` (`smoothing C^2 / 2T`), whereas `m004 x (C^2 / 2T)` preserves stabilizer `24` (`affine E_6 via I-1`) and carries the canonical flat Wilson-line bundle `iota_{E_6} o rho`.
   - **Expectation E3 (Native Rank-`16` `E_8^{(1)} x E_8^{(2)}`: Visible `n_{10} = 2` + Exact `R`-Parity & Hidden Borel-de Siebenthal Subalgebras):**
     - Verify visible `Spin(10) x U(1)_psi subset E_6 subset E_8^{(1)}`: `n_{10} = 2N - 8 = 2 -> (H_{u1}, H_{d2})` with `0 / 12` triplets (`I-37`) and exact `P_M = (-1)^{3(B-L)+2s}` forbidding all `4` dim-`4` `B/L`-violating superpotential terms while allowing all `6` Yukawa/`mu`/seesaw couplings (`OBS-15, 16, 20`).
     - Via affine `hat{E}_8` node deletion (`Borel-de Siebenthal`), classify all `8` maximal-rank (`rank = 8`) regular semi-simple subalgebras of hidden `E_8^{(2)}` (`total rank 16 <= 16`, fixing `BL1-F3`), verifying `SU(5)_perp x SU(5)'_perp` (`b_0 = (15, 15)`), `SU(5)_perp x SU(4)_perp x U(1)` (`b_0 = (15, 12)`), `Spin(10) x SU(4)` (`b_0 = (24, 12)`), and `E_6 x SU(3)` (`b_0 = (36, 9)`).

3. **How it could come out wrong, written before any run:**
   - **F1:** Another dimension in `{3, 4, 6, 10, 18}` could be normed, associative, commutative, and `x^2 + 1 = 0` closed.
   - **F2:** Canonical `ord(rho(mu)) = 3` surjections could map `lambda_0` to `+1` instead of `-1`, or unbranched `(tilde{M}_3 x C^2) / 2T` could retain nontrivial `z = 0` stabilizer.
   - **F3:** `SU(5)_perp` (`b_0 = 15`) or two-factor racetracks might require `rank > 8` outside `E_8^{(2)}`, or `P_M` might allow dim-`4` proton decay.

4. **What it rests on, and what it must not touch:** Rests on `AGY-C35..C39`, `main` `B1223 / B1273 / B1970` (`279459977`), `639a5d46b`, and `27f5d89fa`. Must not touch sealed past files, `main`, `agy/audit-2026-11-02`, peer branches, or empirical constants (`0 of 19`).

5. **Controls that must fail if the work is broken:**
   - **Control 1 (`16D` sedenion zero divisors vs `{1, 2, 4, 8}` Hurwitz composition):** `16D` Cayley-Dickson `S` must exhibit nonzero `u, v` with `u * v == 0`.
   - **Control 2 (`H^1(m004; Z_2)` meridian-`6` twist vs `m000` orientation cover):** Squaring in `2T` (`orders {1, 2, 3, 4, 6}`) can never yield order `6`, rejecting all `24` meridian-`6` twists on `m000`.
   - **Control 3 (Unbranched free cover vs branched orbifold stabilizer on `I-6`):** Unbranched `(tilde{M}_3 x C^2) / 2T` must give stabilizer `1` at `z = 0` (`smoothing E_6`), whereas `M_3 x (C^2 / 2T)` gives `24`.
   - **Control 4 (Broken `Delta(B-L) = +-1` seesaw vs `Delta(B-L) = +-2` `R`-parity):** `Delta(B-L) = 1` breaking must allow all `4` dim-`4` proton-decay operators (`u^c d^c d^c, Q L d^c, L L e^c, L H_u`), whereas `Delta(B-L) = 2` forbids `4 / 4`.
   - **Control 5 (`Spin(18)` rank-`9` overflow vs native rank-`8` `E_8^{(2)}` Borel-de Siebenthal subalgebras):** `rank(E_6 x Spin(18)) = 15 > 8` must fail `E_8^{(2)}` embedding, while all `8` Borel-de Siebenthal deletions have exact `rank == 8`.

6. **What is needed from main or from another seat:** Review the `rho(lambda_0) = -1` cusp spin-holonomy & `B1223` stabilizer theorem on `I-6` and the native rank-`8` `E_8^{(2)}` (`b_0 = (15, 12)` / `(15, 15)`) racetrack classification replacing `Spin(18)`.

0 of 19.
