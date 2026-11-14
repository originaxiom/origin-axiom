# CARD `X-SM` (`AGY-EXP`): INDEPENDENT SECOND COMPUTATIONS OF THE FIVE RECEIVED `SM`-SEAT RESULTS (`M15`)

- **Seat:** `agy-exp` (branch `origin/agy/self-consistent-loop-2026-11-11`)
- **Assigned by:** `M15` on `docs/seats/agy-exp.md` at `origin/main` `660daba8d`
- **Date:** `2026-11-14`
- **Protocol:** expectations committed in this card before any verifier script is written or run; standalone script `relays/x_sm_verify/verify_x_sm.py` committed with `SCRIPT_SHA256.txt` before its single run; unread output `relays/x_sm_verify/verify_x_sm_out.json` committed with `OUTPUT_SHA256.txt` before reading; closing report written in words, exact integers, and exact fractions only (`0 of 19`).

---

## 1. Scope and Exact Commits Read (Prose Only; Zero Producer Scripts Read or Imported)

1. **Item 1 — `SM-C6 E1` (harvest rows `1747` and `1762`):** `relays/SM_C6_E1_THE_BASED_COUNT.md` at `9fa6475f8` and `4dc13acae`.
2. **Item 2 — `SM-C6 E2` (harvest row `1756`):** `relays/SM_C6_E2_THE_RANK_OF_THE_BITS.md` at `141bb0ad6`.
3. **Item 3 — `SM-C6 E5 part 1` and `E6 steps 1–2` (harvest row `1757`):** `relays/SM_C6_E5_THE_DECKS_ANOMALY.md` and `relays/SM_C6_E6_FILLING_DESCENT.md` at `c7b363a6a`.
4. **Item 4 — `M22` answer on `W31` (harvest rows `1758` and `949`; register `P-843`):** `relays/SM_ANSWER_M22_W31.md` at `2f634be02`, together with `docs/dossiers/the_weave_2026-10-07/W31_RULE.md` and `docs/dossiers/the_weave_2026-10-07/the_z5_twist_eater.json` at `1fabfa960`.
5. **Item 5 — Scope note on closed-join duality (harvest row `1760`):** `relays/SM_SCOPE_NOTE_CLOSED_JOINS.md` at `987532239` (and its cited derivation in `relays/SM_LITERATURE_NOTE_1.md` at `bebbc7019`).

Reference definitions taken from banked `origin/main` prose only (`frontier/B1432_the_three_fold_cover_fires_off_the_lift/FINDINGS.md`, `frontier/B1434_the_architecture_census/FINDINGS.md`, `frontier/B1438_the_slope_law/FINDINGS.md`, `frontier/B1881_the_whole_and_the_value_verified/FINDINGS.md`, `frontier/B1895_the_mends_of_b1881_read_and_what_its_second_convention_is/FINDINGS.md`). Zero `.py` files from `frontier/`, `src/`, or any seat branch are read or imported.

---

## 2. Committed Expectations Before Writing or Running Code

### Item 1 (`SM-C6 E1`: the based count and its three owed steps)
- **Expectation (`the same` across all deciding counts, with one watchful check on step 3's reversal convention):**
  1. Across all `24` levels (`+LR` and `-LR` `1..5`, `+LLR` and `-LLR` `1..4`, `+LLLR` and `-LLLR` `1..3`; `136176` non-degenerate sector modules total), computing exact slopes `s(chi)` from the `2 x 2` Fox Jacobian of `G = <x, y, mu | mu x mu^-1 = phi(x), mu y mu^-1 = phi(y)>` normalised on `lambda = [x, y]` (cross-checked in exact cyclotomic / modular prime-field arithmetic at two distinct primes `p == 1 mod N`) will reproduce all `24` rows of `(modules, (0, 0), (1, 0), (0, 1), (1, 1))`, with `(1, 1)` non-empty on `18` of `24` levels and `(1, 0) = (0, 1)` on every level (`118164` modules with `n = n*`, `18012` with `n != n*`).
  2. At lengths `6` and `7`, up to cyclic rotation and `L <-> R` swap there are exactly three word pairs whose reverse is not a rotation (`LLRLRR` at length `6` with level-`2` exponent `N = 221` and `220` non-trivial characters; `LLRLRRR` and `LLLRLRR` at length `7` with level-`2` exponent `N = 198` and `395` non-trivial characters). Across both signs and both levels `1` and `2`, the coordinate-labelled based count differs between `w` and `reverse(w)` (`6` of `6` at level `1`, `6` of `6` at level `2`), while the unlabelled census and slope multiset agree (`6` of `6` at both levels).
  3. On the `16275` even-length run sequences (`2, 4, 6`, runs `1..5`; `5575` letter-preserving rotation classes), heights and apex are invariant under reversal on all `16275`, whereas keeping the mark `v = (1, 3) mod 5` under letter-word reversal (`L <-> R` transpose without coordinate swap) differs on `3372` of `16275` (`1456` of `5575` classes) and is constant across all rotations on `10931` of `16275` — *how it could come out wrong:* if `E1` defined run-sequence reversal differently (for example tuple reversal keeping `L` first, which is invariant on all `16275` by `B1881` § 5, or a one-step cyclic shift after reversing), our verifier will compute all candidate definitions side by side and report if any count differs.
  4. Exhaustive check over all `91840` small deterministic systems (`n in {2, 3, 4}` with `1` update and `n in {2, 3}` with `2` updates, binary output, and all set-partition quotients `B_n`) will confirm that `AR1` (updates + output descend) is `100%` sufficient (`0` failures), largest-bisimulation inclusion is `100%` necessary and sufficient, and `8664` systems have all observations descending while an update fails to descend (smallest example at `n = 3`).

### Item 2 (`SM-C6 E2`: rank of the three named bits)
- **Expectation (`the same`):** On the `23` levels with non-empty character sets (`24` minus `+LR 1`), the mirror `c` (`L <-> R`) acts non-trivially on the slope set of all `14` chiral levels (`s -> -s` modulo an integer meridian shift) and trivially on all `9` amphicheiral `+-LR` levels (`0` of `23` on the unlabelled counts); exchange `X` (`chi -> chi^-1`) acts trivially everywhere (`s(chi^-1) = s(chi)` on all `23` levels); and piece-order `O` (`(n, n*) -> (n*, n)`) leaves slopes untouched while acting non-trivially on the `21` of `23` levels having at least one `(1, 0)` module (all except `+LLR 1` and `+LLLR 1`). Joint rank on `{slopes, based counts}` is `2`, with `D = O * X` acting identically to `O`.

### Item 3 (`SM-C6 E5 part 1` and `E6 steps 1–2`)
- **Expectation (`the same`):**
  1. **`E5 part 1`:** Independent enumeration of `s961` (`+LR` level `3`, torsion `(Z / 4 Z)^2`, `16` loci of which `12` are non-square of order `4` with slopes `+-1` and `3` are squares of order `2` with slope `0`) yields `72` firing modules and `48` generation-shaped backgrounds (`24` of `+1`, `24` of `-1`, `0` lifted) falling into `16` free `Z / 3 Z` deck orbits of size `3`. Because each free orbit carries charges `(0, 1, 2)` (`sum q = 3`, `sum q^3 = 9`, permutation determinant `+1`), per-orbit `Z_3–SU(3)^2 = 6`, `Z_3–SU(2)^2 = 6`, `Z_3–gravity^2 = 48`, and `Z_3^3 = 144` all vanish `mod 3` (`Z_3–U(1)_Y^2 = 10 == 1 mod 3` per orbit, `160` total).
  2. **`E6 steps 1–2`:** Using exact modular Fox calculus over two large primes `p == 1 mod N` (free of floating-point singular-value thresholds!), across all `136176` sector modules on the `24` levels, exactly `46618` modules (on `18` of `24` levels) have rational slope `s(ell) = a / b` (`gcd(|a|, b) = 1, b >= 1`), satisfy `rho_V(mu^b lambda^-a) = I_2` identically, satisfy `dim H^1(M; V) = 1 + [s(beta) = s(ell)]` and `I(V) = n(V) - n(V*) = dim H^1(M; V*) - dim H^1(M; V)` on all `46618`, and after Dehn filling along `gamma = mu^b lambda^-a` give `(0, 0) -> 0` (`39424`), `(1, 0) -> 1` (`3000`), `(0, 1) -> 1` (`3000`), `(1, 1) -> 2` (`810`), and `(1, 1) -> 1` (`384`) — *how it could come out wrong:* if double-precision SVD in `E6` misclassified any near-singular Fox coboundary matrix at high level, exact `F_p` Gaussian elimination at two primes will catch the exact discrepancy.

### Item 4 (`M22` answer on `W31`, rows `1758` and `949`, `P-843`)
- **Expectation (`the same`):**
  1. Rebuilding `W31` (`E_8` branching `(SU(5)_g x SU(5)_b) / Z_5`, `C_5^m` and `S_5` with commutator `zeta^m I_5` for `m = 1, 2, 3, 4`) from scratch reproduces `W31` cells `F1–F6` (`|<C_5, S_5>| = 125`, `E_8` centraliser mean `24`, projective lift order `120` splitting `3 + 2` as `2I`'s `SO(3)` triplet plus spinor doublet, `(L R^-1 L)^2` giving `k -> 4 - k`, bare `-I` giving `k -> -k` enlarging projective order to `3000`, `Lambda^2 C^5 = 1 + 3 + 6`, and `zero` `SU(5)^3`-anomaly-free threes for any `m`).
  2. `W31`'s `C^5` is canonically the `SL(2, F_5)` Weil representation for additive character `psi_m(x) = zeta^(m x)`; the `SO(3)`-normalised order-`5` lift of `L` on the `3`-piece has trace `1 + zeta^(2m) + zeta^(3m)`, which equals `1 - phi` for `m in {1, 4}` (squares `mod 5`) and `phi` for `m in {2, 3}` (non-squares `mod 5`), so `m -> 2m` exchanges `3` and `3'`.
  3. Meanwhile the `SU(5)^3`-anomaly-free net generation counts (`n(10) = n(5-bar)`) under the moves are `{-1, 2}` for `m in {1, 3}` and `{-2, 1}` for `m in {2, 4}`, negated under `m -> -m` (the swap `P`) and **not** a function of the quadratic residue class `{1, 4}` versus `{2, 3}`. Hence `P-843` is answered negatively inside `W31`.

### Item 5 (`Closed-join duality` restatement with three hypotheses, row `1760`)
- **Expectation (`the same`):**
  1. Under `(H1)` orientable closed `3`-manifold `Q`, `(H2)` `h^0(Q; V) = h^0(Q; V*) = 0`, and `(H3)` smooth local system (`no` singular locus), Poincaré duality plus `chi(Q; V) = 0` proves `h^1(Q; V) = h^1(Q; V*)`, verified across all `46618` closed fillings of `E6` (`0` exceptions).
  2. Testing each hypothesis failure directly in code:
     - Dropping `(H1)` on a non-orientable `3`-manifold (`m025`, the three-tick mapping torus of `(LP)^3` with nontrivial orientation character `omega`) satisfies twisted duality `h^1(Q; V) = h^1(Q; V* tensor omega)` while breaking untwisted `h^1(Q; V) = h^1(Q; V*)`;
     - Dropping `(H2)` (allowing `alpha = 1` or `beta = 1` on a closed filling so `h^0(Q; V) - h^0(Q; V*) = +-1`) produces `h^1(Q; V) - h^1(Q; V*) = +-1 != 0`;
     - On every one-cusped level (`§ 5`), peripheral restriction `[[1, s(ell)], [0, 1]]` on `mu` and `[[1, 1], [0, 1]]` on `lambda` gives core holonomy `[[1, b s(ell) - a], [0, 1]]`, which over characteristic zero is either `+I_2` (`s(ell) = a / b`) or infinite-order parabolic (`s(ell) != a / b`), ruling out finite-order orbifold closings on one-cusped levels.

---

## 3. Five Planted-Fault Controls (All Five Must Fire)

1. **`PC_E1_wrong_slope_role`:** Replace `s(alpha) = s(ell)` with `s(beta) = s(ell)` in `n(V)` -> must alter the `24`-level `(n, n*)` census on at least `20` levels.
2. **`PC_E2_reverse_as_mirror`:** Replace the mirror `c` (`L <-> R` then reverse, or `L <-> R`) with plain word reversal -> must fail to negate chiral slopes (`0` of `14` levels changed instead of `14` of `14`).
3. **`PC_E5_fixed_orbit_anomaly`:** Replace a free `(0, 1, 2)` deck orbit on `s961` with a fixed charge-`1` background or `(0, 0, 1)` -> must produce non-zero `Z_3–SU(3)^2`, `Z_3–SU(2)^2`, `Z_3–gravity^2`, and `Z_3^3` modulo `3`.
4. **`PC_E6_wrong_filling_curve`:** Shift the filling curve from `mu^b lambda^-a` to `mu^b lambda^(-a + 1)` -> must fail `rho_V(gamma_bad) = I_2` on `100%` of the `46618` modules (including all `8094` slope-`0` modules where `E6`'s own `mu^2` plant was degenerate!).
5. **`PC_M22_triplet_vs_conjugate`:** Assert `P-843`'s positive hypothesis that `W31`'s anomaly-free counts are constant on `{m = 1, 4}` and `{m = 2, 3}` -> must fail (`{-1, 2} != {-2, 1}`).

`0 of 19.`
