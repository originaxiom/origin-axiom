# CARD `X-NEG`: INDEPENDENT SECOND COMPUTATIONS OF `B1868` AND `B1855`, AND WHAT EACH WALL TEACHES

- **Seat:** `agy-exp` (branch `origin/agy/self-consistent-loop-2026-11-11`)
- **Card:** `X-NEG` (assigned on `docs/seats/agy-exp.md` in `M14` at `origin/main` `b1bcc7f50`, under `P-842` and `B1923`)
- **Date:** `2026-11-14`
- **Mask and firewall discipline:** pure mathematics only; prose written in words, exact integers, and exact rationals only (zero floating-point or scientific-notation literals, zero measured values or held-out targets, zero vendor or model tokens; `0 of 19`).

---

## 1. The Questions, Stated Before Any Code or Run

1. **`B1868` (under a uniform count of moves no value of `tau` holds weight):**
   - **Existence of a density:** Does the move-count `tau`-law on the non-compact modular orbifold `PSL(2, Z) \ H` possess a genuine Radon–Nikodym density with respect to hyperbolic area (`dx dy / y^2`), without assuming compactness of the base surface (`Ledrappier–Lindenstrauss`)?
   - **The five off-axis points:** Using deterministic two-dimensional Stern–Brocot / Minkowski Stieltjes quadrature (zero random sampling) across all three entry sides of the Farey triangle `(0, 1, infinity)` via the order-three rotation `z -> 1 / (1 - z)` — a method that works off the imaginary axis as well as on it — do the local density-ratio scaling slopes over `epsilon = 2^-5 .. 2^-11` and the half-turn correlation (`Jensen`) exponents at all five off-axis CM points (`exp(i pi / 3)`, `(1 + i sqrt(7)) / 2`, `Q1 = 21/50 + 123/100 i`, `Q2 = 2/25 + 33/25 i`, `Q3 = 3/25 + 93/50 i`), alongside the on-axis controls (`i`, `i sqrt(2)`, `i sqrt(3)`, `Q4 = 67/50 i`), come out `the same` as `B1868`?
2. **`B1855` (the charge law holds for `lcm(S) <= 10` and fails from `lcm(S) >= 12`):**
   - **The exhaustive search re-derived:** Using this seat's own backward `J`-conjugation shortest-path graph on `SL(2, Z / L Z)` (which eliminates the Pisano-phase factor from the state space) together with `A*` branch-and-bound on the exact Rayleigh excess `2 log(v^T E v / v^T v)`, does the single run `lcm(S) + 1` uniquely minimize excess length over all defects of arbitrary run count, run lengths, and gaps for every `S` subset of `{2, 3, 4, 5}` with `lcm(S) <= 10`, and fail for every `S` with `lcm(S) >= 12`?
   - **The structure of the failure set:** What are the exact global minimizers (not merely upper-bound counterexamples) at `lcm(S) >= 12`, and how does the failure set separate across the three distinct group conditions conflated or bundled under "charge":
     1. *Per-rung sign freedom* (`E == +-_n I mod n` independently at each `n in S`, which introduces mixed-sign Chinese-Remainder scalars `5 I mod 12`, `4 I mod 15`, `9 I mod 20`, `11 I mod 30`, and `{11, 19, 29} I mod 60` starting at `lcm(S) = 12`),
     2. *Global sign freedom* (`E == +I mod L` or `E == -I mod L` uniformly across all rungs), and
     3. *Strict identity superselection* (`E == +I mod L`, `B1862`'s parity-free invisibility condition, evaluated both on the divisors of `60` and on prime levels `p` where Chinese-Remainder sign splitting cannot occur)?

---

## 2. Expectations Committed Before Any Code or Run

### Part A — Expectations for `B1868`

1. **Unconditional proof that a density exists (`mu_tau << dx dy / y^2`):**
   - Expected to **hold unconditionally as a theorem** without compact-surface assumptions, verified both analytically and numerically:
     - Every depth-`m` Stern–Brocot interval on `[0, 1]` has denominator product bounded above by consecutive Fibonacci numbers, giving Salem's uniform Hölder bound `nu([x - r, x + r]) <= C r^alpha_min` with `alpha_min = log(2) / (2 log(phi))`, which strictly exceeds `1/2` (since `2^2 = 4 > phi^2 = (3 + sqrt(5))/2`, i.e. `8 > 3 + sqrt(5)` because `25 > 5`).
     - Consequently, on every compact parameter box `B_k` in `((0, 1) union (1, infinity)) x (0, infinity)`, Minkowski's measure has strictly finite Riesz one-half energy `I_{1/2}(nu|_{B_k}) < infinity`.
     - For any two geodesics `gamma_1 = (-zeta_1, xi_1)` and `gamma_2 = (-zeta_2, xi_2)` in `B_k`, their `epsilon`-tubular parameter-square overlap inside the Farey triangle is bounded by `C_k epsilon^2 / max(|xi_1 - xi_2| + |zeta_1 - zeta_2|, epsilon)`, whose expectation against `(nu x nu)^2` is bounded by `I_{1/2}(nu|_{B_k})^2 < infinity`.
     - By `L^2` weak compactness (`Alaoglu`), each box measure `mu_k` has an `L^2` density with respect to `dx dy`, and countable exhaustion `k -> infinity` implies `mu_tau << dx dy / y^2` globally on `PSL(2, Z) \ H` with an `L^1` density `f(tau)` (locally `L^2` even across `i`, since `2 D_2 - 1 > 0`).
2. **Deterministic off-axis and on-axis scaling (`epsilon = 2^-5 .. 2^-11`):**
   - All five off-axis points (`exp(i pi / 3)`, `(1 + i sqrt(7)) / 2`, `Q1`, `Q2`, `Q3`) satisfy `d_H(z_0, boundary(F)) > 2^-5`, so their `epsilon`-disks lie strictly inside the interior of the Farey triangle across the entire fit range and the three-side rotation sum `M_epsilon(z_0) + M_epsilon(rho_3^-1 z_0) + M_epsilon(rho_3^-2 z_0)` divided by `12 sinh^2(epsilon / 2)` is exact.
   - Expected outcomes at the five off-axis points:
     - `exp(i pi / 3)` (half-turn degree `3`): flat scaling (slope near zero, within four hundredths of zero), half-turn `Jensen` exponent strictly above `1` (near six fifths);
     - `(1 + i sqrt(7)) / 2` (half-turn degree `7`): **falling / depleted** density ratio as `epsilon -> 0` (positive slope near two twenty-fifths), half-turn `Jensen` exponent strictly above `3/2`;
     - `Q1`, `Q2`, `Q3` (rational-coordinate CM points of half-turn degrees between six hundred thousand and one hundred and fifty million): flat scaling (slopes within four hundredths of zero), half-turn `Jensen` exponents strictly above `4`;
     - On-axis positive controls (`i`, `i sqrt(2)`, `i sqrt(3)`, `Q4`) and Pollicott's constant `lambda = int_0^infinity log(1 + u) d nu(u)` and `D_2`: expected to agree with `B1868` (`i` spiked with slope near `D_2 - 1`, `i sqrt(2)` spiked near minus two twenty-fifths, `i sqrt(3)` and `Q4` flat).

### Part B — Expectations for `B1855`

1. **Exhaustive search for `S` subset of `{2, 3, 4, 5}`:**
   - Using the backward `J`-conjugation graph on `SL(2, Z / L Z)` (`H -> J H J^-1` at zero `B`-cost for golden steps, `H -> L^s H` at `B`-cost `log(1 + s / phi^2)`), expected **`the same`** on all seven subsets with `lcm(S) <= 10` (`{2}`, `{3}`, `{4}`, `{5}`, `{2, 3}`, `{2, 4}`, `{2, 5}`): the least multi-run `B`-cost strictly exceeds `log(1 + L / phi^2)` and in fact guarantees `B > 1 + L / sqrt(5)`, proving `lcm(S) + 1` uniquely minimal over all defects.
   - Expected **`the same`** on the refutation for all eight subsets with `lcm(S) >= 12` (`{3, 4}`, `{2, 3, 4}`, `{3, 5}`, `{4, 5}`, `{2, 4, 5}`, `{2, 3, 5}`, `{3, 4, 5}`, `{2, 3, 4, 5}`), with exact `A*` search finding the true global minimizers of `2 log Q(E)` at each `S`.
2. **Expected structure of the failure set:**
   - **Mechanism 1 (Chinese-Remainder sign splitting at `lcm(S) >= 12`):** Among `S` subset of `{2, 3, 4, 5}`, `lcm(S) <= 10` holds if and only if the per-rung condition `E == +-_n I mod n` introduces **zero** mixed-sign central scalars in `SL(2, Z / L Z)` (because modulo `2`, `+I == -I`), whereas every `lcm(S) >= 12` introduces non-trivial involutive scalars `c I` (`c != +-1 mod L`, `c^2 == 1 mod L`, `det(c I) == 1 mod L`), starting with `+-5 I mod 12` at `{3, 4}`. Because a single unipotent shear `L^s` has trace `2` and can hit only `+I`, multi-run defects exploit both `-I` and mixed Chinese-Remainder scalars (`5 I mod 12` already at `{3, 4}`!).
   - **Mechanism 2 (Strict `+I mod L` and global `+-I mod L`):** We will compute the exact `A*` global minimum separately for (i) per-rung `+-_n I`, (ii) global `+-I mod L`, and (iii) strict `+I mod L` across all divisors `L | 60` (`2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60`) and prime levels `p in {2, 3, 5, 7, 11, 13}`:
     - At small composite `L` (such as `L = 12`), restricting from per-rung `+-_n I` to strict `E == +I mod L` raises the multi-run cost sharply (testing whether `13` is restored at `L = 12` under strict `+I` or still beaten!);
     - At sufficiently large `L` (including large `L | 60` and/or primes `p >= 7`), we test whether hyperbolic `J`-conjugation allows multi-run words to reach even strict `+I mod L` at logarithmic `B`-cost below `2 log(1 + L / sqrt(5))`, separating the arithmetic sign-splitting failure from the asymptotic hyperbolic-diameter failure.

---

## 3. Deliverables and Commit-Order Seal

1. **Card committed first:** `relays/cards/AGY-EXP_X-NEG_b1868-and-b1855-second-computations.md`.
2. **Standalone verifier committed before its one run:** `relays/x_neg_verify/verify_x_neg.py` and `relays/x_neg_verify/SCRIPT_SHA256.txt` (zero imports from `frontier/`, `src/`, or any seat's scripts; syntax-checked only before commit).
3. **Unread output committed before reading:** `relays/x_neg_verify/verify_x_neg_out.json` and `relays/x_neg_verify/OUTPUT_SHA256.txt`.
4. **Closing note and status update:** `relays/AGY_EXP_TO_CC_2026-11-14_X_NEG_RESULTS.md` (reporting the results in mask-safe prose and writing **What the wall teaches** after `B1868` and after `B1855`, per `M14` and `P-842`) and `relays/STATUS_AGY-EXP.md`.

---

## 4. Planted Controls That Must Fail If the Work Is Broken

1. **`PC_B1868_liouville_flat` (positive normalization / planted wrong side count):** Replacing Minkowski's measure `nu x nu` by the exact Liouville measure `d xi d zeta / (xi + zeta)^2` with `lambda_L = pi^2 / 3` must yield `f_epsilon([z_0]) = 1` identically at every off-axis point (`exp(i pi / 3)`, `(1 + i sqrt(7)) / 2`, `Q1`, `Q2`, `Q3`); omitting the two rotated Farey entry sides `rho_3^-1` and `rho_3^-2` is planted and must fail that unit-density check by missing two thirds of the directions.
2. **`PC_B1868_atomic_measure` (planted singular Riesz blow-up):** Replacing `nu` by a planted measure with an atom (or Hölder exponent `0`) must violate the Riesz `1/2`-energy bound and drive the density ratio at `i` as `epsilon^-2` rather than `epsilon^(D_2 - 1)`, firing the control.
3. **`PC_B1855_drop_crt_or_sign` (planted wrong premise):** Confusing `E == +I mod 12` with `E == +-_n I mod n` at `S = {3, 4}` (planting `E == +I mod 12` as if `5 I mod 12` did not satisfy `{3, 4}`) must reject `{3, 4}`'s `7`-run defect `(2, 1, 1, 3, 1, 1, 2)` whose matrix modulo `12` is `5 I`, firing the control.
4. **`PC_B1855_wrong_eigenvector` (planted transposed `LR` eigenvector):** Replacing `v = (phi, 1)` by the transposed convention `(1, phi)` on `L = [[1, 1], [0, 1]], R = [[1, 0], [1, 1]]` must fail the `k = 20` hyperbolic trace excess check on `R1` defects, firing the control.

---

## 5. What It Rests On, and What It Must Not Touch

- **Rests on:** `origin/main` (`@ b1bcc7f50`: `B1868`, `B1853`, `B1855`, `B1923`, `docs/seats/agy-exp.md` `M14`) and the prose definitions in `e5cc47e96` and `91119a381` (no `.py` script of `main` or any seat is imported or executed).
- **Touches only:** `relays/` on `agy/self-consistent-loop-2026-11-11`. Zero measured values, zero frame outputs (`0 of 19`).

`0 of 19.`
