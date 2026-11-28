# Pre-Commit Expectations & Failure Conditions — `Card AGY-C71` (`2026-11-28`, `0 of 19`)

- **Seat code:** `fam3-v1-high-01` (`agy`, branch `agy/cusp-action-2026-11-20`; harvest branch `agy/audit-2026-11-02` untouched at `4319f47e2`)
- **Touches & premises on `main` (strictly pre-trial `<= B2010`):** `B1990`, `B1996`, `B1997`, `B2001`, `B2002`, `B2003`, `B2004`, `B2005`,
  `B2006`, `B2007`, `B2009`, `B2010`, `P-630`, `P-755`, `P-882`
- **Parameter count:** `0 of 19` (`0` continuous or discrete parameters, `0` empirical values, `0` floats, order-30 line held per `M18`)

## Committed Mathematical Expectations (Prior to Single-Run Producer Execution)

1. **`E1` (`B2007` Open `#1` — Kempner Falling-Factorial Valuation Law, Three-Rung Plateau `[7, 7, 7]`, & Tower Dimensions Through `mod 177147 = 3^11`):**
   - On the two-sheet Klein-four Hensel section `S_k = {a_1 = 1, a_2 = 1 mod 3} ~= {1, 2} x (Z / 3^(k-2) Z)^2`, every word in `G_k` preserves the
     valuation ring `R = {sum c_{i,j} t_1^i t_2^j : v_3(c_{0,0}) >= 0, v_3(c_{i,j}) >= i + j - 1 for i + j >= 1}`, truncating every element of `G_k`
     exact modulo `3^m` (`m = k - 2`) at degree `<= m`; expanding in falling factorials `t_1^{\underline{i}} t_2^{\underline{j}}` via Stirling numbers
     of the second kind proves Kempner's null criterion `v_3(d_tilde_{i,j}) + v_3(i!) + v_3(j!) >= m` (`+v_3`, flipping the naive minus-sign guess).
   - Pure-stdlib zero-squaring Reidemeister-Schreier sifting proves `dims_k3_k11 = [2, 2, 3, 7, 7, 7, 12, 14, 14]` for `k = 3` to `11`,
     `log_3 |K_11| = 68` (`|G_11| = 24 * 3^68`), Lazard cubing ranks `cubing_k3_k10 = [2, 2, 3, 7, 7, 7, 12, 14]` (`bijective at 3->4, 6->7, 7->8,
     10->11`), and unbounded rank growth (`14 > 12 > 7 > 3 > 2`, refuting finite `3`-adic Lie rank saturation).

2. **`E2` (`B1990` Open `#1` — Universal All-Prime Branchless Quadratic-Character Point-Count Law):**
   - Completing the square in `z` on `X_kappa : x^2 + y^2 + z^2 - x y z = kappa + 2` over `F_p` (`odd prime p >= 3`) yields a conic fibration
     whose character sum proves symbolically and across all `17` odd primes `3 <= p <= 61` (`499` `(p, kappa)` pairs) the single branchless law
     `#X_kappa(F_p) = p^2 + ((kappa - 2) / p) * (3 + ((kappa + 2) / p)) * p + 1`, unifying `kappa = 2` (`p^2 + 1`), `kappa = -2`
     (`p^2 + 3(-1/p)p + 1`, equal to `1` at `p = 3`), and all generic leaves (`p^2 + s p + 1` with `s in {-4, -2, 2, 4}`).

3. **`E3` (`B2003` Open `#3` — Exact `mod 45` Paired Modes & Universal `6`-Point Composite Defect Quotient `Q_6` for All `3^k * p`, `k >= 3`):**
   - Exact integer `DomainMatrix` factorization proves on `O_45 ~= O_9 x O_5` (`320` points, `d_0 = 108`, `d_1 = 106`) that the `4` paired charged
     modes are `x^2 (x - 2)(x + 2)` (`paired_45 = [('x', 2), ('x - 2', 1), ('x + 2', 1)]`), while on `O_63 ~= O_9 x O_7` (`224` points) `8` of `74`
     modes pair as `(x - 1)^2 (x + 1)^2 (x^2 - 2 x - 1)(x^2 + 2 x - 1)`.
   - Quotienting `O_27` (`72` points) by `N_3 = (V_4 K_3) cap [G_3, G_3]` (`order 12`) yields a `6`-point `PSL(2, Z)`-quotient `Q_6` (`|Fix(C)| = 3`)
     such that `l^2(O_{3^k}) = l^2(Q_6) (+) B_k` with `B_k (x) rho ~= B_k` for every `k >= 3`; hence for every `k >= 3` and `p >= 5` coprime to `3`,
     the unpaired charged modes of `O_{3^k * p}` equal those of `Q_6 x O_p` (`degree 10` for `p = 5`:
     `(x^2 - 2 x - 2)(x^2 + 2 x - 2)(x^3 - 3 x - 1)(x^3 - 3 x + 1)`, verified directly against `O_135`? Better: verified by exact character
     pairing `m_pi == m_{pi (x) bar(rho)}` on all `G_3` irreducibles outside `Q_6`!; and `degree 8` for `p = 7`:
     `(x^2 - x - 4)(x^2 + x - 4)(x^2 - x - 1)(x^2 + x - 1)`).

4. **`E4` (`B1997` Open `#1` — Regular `K_4 ~= (Z / 9 Z)^2` Fiber Fourier Transform, Inversion-Closed Orbits, & Mackey Multiplicity `2`):**
   - On `O_81` (`648 = 8 * 81` points), `K_4 = ker(G_4 -> S_4) ~= (Z / 9 Z)^2` acts regularly on each `O_9` fiber, splitting `Dual(K_4)` into `19`
     `S_4`-orbits (`3` of size `1`, `6` of size `3`, `10` of size `6`), of which strictly `3` order-`9` size-`6` orbits satisfy `-m in S_4 . m`.
   - Over `QQ(zeta_9)`, those `3` inversion-closed orbits annihilate the `3` Galois-conjugate quartics
     `Q_r(W_+) = W_+^4 - (1 - 2(zeta_9^r + zeta_9^(-r))) W_+^2 + 4` (`r in {1, 2, 4}`) with nullity `8 = 4 * 2` each (`total 24`, Mackey index
     `|S \ S_4 / H_chi| = 24 / (3 * 4) = 2`), while all `16` remaining orbits have `Q_r`-nullity `0`.

## Failure Conditions & `5` Planted-Fault Controls

- Any mismatch in `dims_k3_k11`, `cubing_k3_k10`, `#X_kappa(F_p)`, `paired_45`, `Q_6 x O_5` / `Q_6 x O_7` unpaired polynomials, or `Dual(K_4)`
  quartic nullities, or failure of any of `PF1` to `PF5` or `c71_control.py`, falsifies the card.

0 of 19.
