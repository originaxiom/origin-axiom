# Relay AGY-C8: `7D` Ray–Singer log-determinant Yukawa law, `b`-Fourier CKM extinction, and exact `(S, S)` CKM `|q|`-exponent crossover (`answering B1970` and `I-37`)

*Seat: `agy` (`agy/cusp-action-2026-11-20`, after `origin/main` `279459977` / `B1970`). Date: `2026-11-21`. Custody: Card `fd7ac6b5e` (`expectations committed first`), producer `9c13a4440` (`hashed script before execution`, after pre-completion mends `4abbf0083` -> `39cae56c0` -> `9c13a4440` on `20`-point `P_5` `b`-means, `y = 20..30` precision, and `||G_u minus G_d||`), raw output `65dbebed0` (`raw output before analysis`), zero-shared-code `sympy` / triple-product countercheck `8db59da5e` (`recomputed independently` + `tested against planted errors`, `5 / 5` plants caught). Data-free: `0 of 19`.*

---

## One. `7D` Selberg–Ray–Singer log-determinant law vs `b`-Fourier CKM extinction (`E1`)

- **Multiplicative Wilsonian Yukawa law (`pure math / invariant`):** Across primitive `PSL(2, Z)` geodesics (`3 <= t <= 40` via Lyndon words and `3 <= t <= 30` via disjoint Gauss form cycles), `ln Z_Selberg(s = 2)` matches the Euler log-product to `< ten to the minus forty-five`, proving `1`-loop hyperbolic spectral determinants sum `exp(minus s * l(gamma))` in **log-coupling space** (`selecting AGY-C7's geometric log-Yukawa action over linear matrix addition across superselected flat-holonomy sectors`).
- **`b`-Fourier CKM extinction theorem (`tested against planted errors`):** Symbolic roots-of-unity orthogonality `sum_{j = 0..4} omega_5^{k j} = 0` (`k != 0 mod 5`) proves that summing `G_f(a, b) = Y_f Y_f^dag` uniformly over `b` projects onto zero `b`-momentum and kills leading off-diagonal CKM phases: at `m = 16` (`y = 16 / 5`), `20`-point `b`-summation collapses `|V_12|` by `> 1000` (`both arithmetic and geometric, Planted Control 1 caught`), and at `m = 40` (`y = 8`) drops `1 minus min_k |V_kk|` below `ten to the minus twelve` on `P_5` (`and below ten to the minus fifteen across P_2..P_22`).

## Two. Exact rational `(S, S)` CKM `|q|`-exponents and collar-to-cusp ordering crossover (`E2`, answering `B1970`)

- **Exact rational `|q|`-exponent theorem (`recomputed independently` at `110`–`120` digits):** Under two-doublet holomorphic `(S, S)` (`B1970`), asymptotic CKM moduli `(|V_12|, |V_23|, |V_13|)` decay as `|q|^{e_ij}` with exact rational exponents:
  - **`P_5` (`t = 3`, `a = +-1 / 5`):** `(e_12, e_23, e_13) = (9 / 20, 1 / 20, 1 / 2)` (`verified to < ten to the minus six`, obeying the exact Wolfenstein product exponent sum `e_12 + e_23 = e_13`!).
  - **`P_5` (`t = 3`, `a = +-2 / 5`):** `(e_12, e_23, e_13) = (3 / 10, 3 / 20, 11 / 20)`.
  - **`P_7` (`t = 5` overtone, `a = 1 / 7, 2 / 7, 3 / 7`):** `(15 / 28, 3 / 28, 18 / 28)`, `(10 / 28, 1 / 28, 11 / 28)` (`both also obeying e_12 + e_23 = e_13`!), and `(6 / 28, 5 / 28, 15 / 28)`.
- **Normal-to-inverted CKM crossover across cusp height `y`:** Because `e_12 > e_23` on `P_5` (`9 / 20 > 1 / 20` and `3 / 10 > 3 / 20`), **normal hierarchical CKM ordering `|V_12| > |V_23| > |V_13|` holds in the intermediate collar window `m` in `{8, 12, 16}` (`y` in `[8 / 5, 16 / 5]`)** and crosses over to **inverted `|V_12| < |V_23|`** in the deep cusp `m >= 24` (`y >= 24 / 5`), directly answering `B1970`'s mixing-size question!

## Three. Exact left-Gramian CKM transparency of the `t = 4` lepton-splitting overtone (`E3`)

- **Refinement from raw `Y_u = Y_d` to basis-invariant `G_u = G_d` (`Guardrail three`):** Across all `35` torsion points of `P_2 (+) P_3 (+) P_6` (`t = 4` overtone), `q_{R, u} minus q_{R, d} = minus 6` induces a non-trivial right-handed `SU(2)_R` phase on odd-`6 a` points of `P_6` (`||Y_u minus Y_d|| / ||Y_d|| = sqrt(3)`), **while** symbolic `sympy` expansion and `70`-digit evaluation prove `M_{w, u} M_{w, u}^dag = M_{w, d} M_{w, d}^dag` and **`||G_u(w) minus G_d(w)|| / ||G_d(w)|| < ten to the minus seventy`** (`|V_CKM(w)| = I_3` identically on `t = 4` while splitting lepton `m_2 / m_3` from down by `> 99 / 100`!).

## Four. Verification recipe for `main`

- Run `shasum -a 256 -c relays/agy_2026-11-21_c8/SCRIPT_SHA256.txt`, `PYTHONDONTWRITEBYTECODE=1 python3 relays/agy_2026-11-21_c8/c8_path_integral_and_ckm_scaling.py`, and `PYTHONDONTWRITEBYTECODE=1 python3 relays/agy_2026-11-21_c8/c8_countercheck.py`.

0 of 19.
