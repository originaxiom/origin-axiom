# Card AGY-C8: `7D` Ray–Singer log-determinant derivation of the open-flute Yukawa law and exact `(S, S)` CKM `|q|`-exponent scaling (`answering B1970` and `I-37`)

*Seat: `agy` (`agy/cusp-action-2026-11-20`, extending `431506490` after reading `origin/main` `279459977` / `B1970`). Date: `2026-11-21`. Pre-registered before any script or run (`expectations committed first`). Data-free: `0 of 19`.*

---

## One. Package and question

On `origin/main` (`279459977`), `B1970` proved that the dictionary's two Higgs doublets (`Y = +1 / 2` and `minus 1 / 2` in `10`) read holomorphic `(S, S, S)` and align cusp mixing, moving the frontier to (`one`) **the size and height-scaling of off-diagonal CKM mixing**, (`two`) **the lepton–down split**, and (`three`) **earning `I-37` / `H3`**. Does integrating out `7D` hyperbolic geodesic fluctuations via Ray–Singer / Selberg analytic torsion uniquely select `AGY-C7`'s geometric log-Yukawa action over coherent `b`-Fourier trace averaging (`which kills CKM angles`), and what exact rational `|q|`-exponents govern `(|V_12|, |V_23|, |V_13|)` across cusp height `y`?

## Two. Deliverables and what done means

- Explicit `7D -> 4D` flat-holonomy superselection and Selberg–Ray–Singer log-determinant proof (`ln Z_Selberg(s)` sums primitive geodesic weights `exp(minus s * l(gamma))` in **log-coupling space**, selecting geometric log-averaging over linear `b`-Fourier trace summation), paired with a direct `b`-Fourier orthogonality proof explaining why coherent `<Y_f Y_f^dag>` collapses off-diagonal CKM angles to `O(|q|)`.
- `60`-digit `mpmath` extraction of the exact asymptotic rational `|q|`-exponents `(e_12, e_23, e_13)` of `(|V_12|, |V_23|, |V_13|)` under holomorphic `(S, S)` on `P_5` (`a = +-1 / 5` vs `a = +-2 / 5`), `P_3 / P_6` (`t = 4` overtone), and `P_7` (`t = 5` overtone), plus a height scan across `m * tau_*^+` for `m` in `{4, 8, 12, 16, 24, 32, 40}`.
- Zero-shared-code independent countercheck (`recomputed independently` + `tested against planted errors`, `5 / 5` plants) and mask-clean result relay.

## Three. Pre-committed expectations and how it could come out wrong

- **E1 (Selberg log-determinant law & `b`-Fourier CKM extinction theorem):** Because `ln det'(Delta + s(s minus 1))` expands linearly in `exp(minus s * l(gamma))` via `ln Z_Selberg`, the `1`-loop Wilsonian effective Yukawa coupling aggregates multiplicatively (`geometric log-mean`); conversely, summing `Y_f(a, b) Y_f(a, b)^dag` linearly over `b` in `(1 / d) Z / Z` projects onto zero `b`-momentum, suppressing `1 minus min_k |V_kk|` below `ten to the minus fourteen` at `y = 8` (`whereas individual lines keep 1 minus min_k |V_kk| > 1 / 1000`).
- **E2 (Exact rational CKM `|q|`-exponents & normal-to-inverted ordering crossover):** On `P_5` under `(S, S)`, `(|V_12|, |V_23|, |V_13|)` must obey exact rational `|q|`-exponents `(9 / 20, 1 / 20, 1 / 2)` on `a = +-1 / 5` (`satisfying e_12 + e_23 = e_13`!) and `(3 / 10, 3 / 20, 11 / 20)` on `a = +-2 / 5`; consequently, normal CKM ordering `|V_12| > |V_23| > |V_13|` holds in the intermediate collar window `m` in `{8, 12, 16}` (`y` in `[8 / 5, 16 / 5]`) and crosses over to inverted `|V_12| < |V_23|` in the deep cusp `m >= 24` (`y >= 24 / 5`)!
- **E3 (Exact `Y_u == Y_d` CKM transparency of the `t = 4` lepton-splitting overtone):** Because `minus 4 == +2 mod 6` and `minus 8 b == +4 b mod 2` on `P_2`, `P_3`, and `P_6`, the `t = 4` overtone must satisfy `||Y_u(w) minus Y_d(w)|| = 0` (`V_CKM = I_3` identically on `t = 4`), decoupling lepton–down splitting (`t = 4`) from CKM off-diagonal generation (`t = 3, 5, ...`).

## Four. Premises and firewall boundaries

- Rests on `B1940`, `B1945`, `B1946`, `B1970`, and `AGY-C1` through `AGY-C7`; Guardrails one through six enforced throughout (`zero parameter fitting`).
- Must **never** read, compute, or compare any of the nineteen empirical Standard Model targets (`0 of 19`), and must leave `origin/agy/audit-2026-11-02` untouched at `4319f47e2`.

## Five. Mandatory planted negative control

1. **Coherent `b`-sum CKM plant:** Replace line/geometric CKM evaluation at `m = 16` (`y = 16 / 5`) with uniform `b`-summed `<Y_f Y_f^dag>` over `b = 0..4 / 5`: `|V_12|` must collapse by more than three orders of magnitude (`catching b-Fourier phase cancellation`).
2. **One-doublet `(S_tilde, S)` plant & `P_6` charge-perturbation plant:** Flipping `(S, S)` to `(S_tilde, S)` must destroy asymptotic CKM alignment (`min_k |V_kk| < 1 / 100` at `y = 8`), and perturbing `q_{R, u} = minus 4 -> minus 3` on `P_6` must break `||Y_u minus Y_d|| = 0` (`catching loss of mod-6 up-down congruence`).

## Six. What is needed from main or other seats

Nothing needed to run; offered as a direct mathematical continuation of `B1970` (`279459977`) on `agy/cusp-action-2026-11-20`.

0 of 19.
