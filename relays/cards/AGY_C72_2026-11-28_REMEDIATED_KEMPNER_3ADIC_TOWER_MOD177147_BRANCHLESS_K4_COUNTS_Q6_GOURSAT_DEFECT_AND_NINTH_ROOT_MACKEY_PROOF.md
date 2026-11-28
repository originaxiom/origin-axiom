# Pre-Commit Expectations & Failure Conditions — `Card AGY-C72` (`2026-11-28`, Forward-Remediating Unpushed `AGY-C71`, `0 of 19`)

- **Seat code:** `fam3-v1-high-01` (`agy`, branch `agy/cusp-action-2026-11-20`; harvest branch `agy/audit-2026-11-02` untouched at `4319f47e2`)
- **Supersedes forward:** Unpushed `Card AGY-C71` (`a7e1203fc` to `3adb8e23d`, kept unrewritten in git history), remediating pre-push cold-room
  audit items `D1` (non-vacuous computed `c72_control.py`), `D2` (zero-file-write default CLI invocation for read-only sandboxes), `D3` (complete
  Hall polycyclic sifting over all `G_k`-conjugates, cubes, and all `2278` basis-basis commutators in `E1`, plus all-`k >= 3` Hensel/character
  and Goursat `|G_p / G_p'| = 2` proof at `p in {5, 7}` and direct `O_189` verification in `E3`), `D4` (citing `B2011` and `B2014` in premises
  and `already on main?:`), `D5` (aligned referee controls and docstring), and `D6` (basis-free `Dual(K_4)` conjugation and `x_0 = (3, 3, 3) mod 9`
  definitions).
- **Touches & premises on `main`:** `B1990`, `B1996`, `B1997`, `B2001`, `B2002`, `B2003`, `B2004`, `B2005`, `B2006`, `B2007`, `B2009`, `B2010`,
  `B2011`, `B2014`, `P-630`, `P-755`, `P-882`
- **Parameter count:** `0 of 19` (`0` continuous or discrete parameters, `0` empirical values, `0` floats, order-30 line held per `M18`)

## Committed Mathematical Expectations (Prior to Single-Run Producer Execution)

1. **`E1` (`B2007` Open `#1` & `B2014` — Full Hall-Sifted Kempner Falling-Factorial Tower Law Through `mod 177147 = 3^11`):**
   - Integral Hensel composition bound `v_3(c_{i,j}) >= i + j - 1` (`i + j >= 1`) truncates `G_k` on `S_k ~= {1, 2} x (Z / 3^m Z)^2` (`m = k - 2`)
     at degree `<= m`, where Kempner's falling-factorial null ideal adds `+v_3(i!) + v_3(j!)` rather than subtracting `v_3(d!)`.
   - Complete Hall polycyclic sifting (sifting all forward and inverse Schreier generators, all `G_k`-conjugates `g b g^(-1)`, cubes `b^3`, and
     all `2278` basis-basis commutators `[b_1, b_2]`) proves `dims_k3_k11 = [2, 2, 3, 7, 7, 7, 12, 14, 14]` (`verifying unchecked k = 8, 9 =
     [7, 12] registered in B2014 and establishing k = 10, 11 = [14, 14]`), `cubing_k3_k10 = [2, 2, 3, 7, 7, 7, 12, 14]`, `log_3 |K_11| = 68`
     (`|G_11| = 24 * 3^68 = 6675081346648644270174858629562264`), and unbounded rank growth.

2. **`E2` (`B1990` Open `#1` — Universal All-Prime Branchless Quadratic-Character Point-Count Law):**
   - Affine conic fibration `(2 z - x y)^2 - (x^2 - 4)(y^2 - 4) - 4(kappa - 2) = 4(x^2 + y^2 + z^2 - x y z - (kappa + 2))` proves symbolically
     and across all `17` odd primes `3 <= p <= 61` (`499` sectors; `20` odd primes `3 <= p <= 73` in countercheck) the single branchless law
     `#X_kappa(F_p) = p^2 + ((kappa - 2)/p)(3 + ((kappa + 2)/p)) p + 1` (`p3_cusp = #X_{-2}(F_3) = 1`).

3. **`E3` (`B2003` Open `#3`, `B2010` Open `#1`, & `B2011` — `mod 63`/`mod 189` Pairing, `6`-Point Quotient `Q_6`, & All-`k >= 3` Goursat/Hensel Proof):**
   - Alongside `B2011`'s `mod 45` (`4` paired: `x^2(x - 2)(x + 2)`) and `mod 135` (`10` unpaired), proves `mod 63` pairs `8` of `74` modes as
     `(x^2 - 1)^2(x^2 - 2 x - 1)(x^2 + 2 x - 1)` and direct `O_189` (`2016` vertices) pairs `663` of `671` modes leaving `8` unpaired
     `(x^2 - x - 4)(x^2 + x - 4)(x^2 - x - 1)(x^2 + x - 1)`.
   - Constructs `Q_6 = O_27 / N_3` (`N_3 = (V_4 K_3) cap [G_3, G_3]` of order `12`, `|Q_6| = 6`, `|Fix(C)| = 3`), verifies that all `9` elements
     of `L_4 = ker(G_4 -> G_3) = L_3^3` act on `S_4` with identity linear Jacobian (`pure constant shifts mod 9`) so Hensel's lemma locks
     `|Fix_{O_{3^k}}(g)| = |Fix_{Q_6}(g)|` for all `g notin pi_k^(-1)(N_3)` (`verified across all 204 elements of G_3 \ N_3 and all 1836 elements
     of G_4 \ pi_4^(-1)(N_3)`), proving `B_k (x) rho ~= B_k` for all `k >= 3` (`closing B2010 Open #1 and proving k-independent unpaired modes on
     O_{3^k} x O_p for every (L, R, C)-set O_p`).
   - Proves via `PermutationGroup` that `|G_5 / G_5'| = 2` and `|G_7 / G_7'| = 2` (`3` does not divide `|G_p^ab|`) with `|O_{9p}| = 8 |O_p|`, so
     by Goursat's lemma `O_{3^k * p} = O_{3^k} x O_p` holds unconditionally for all `k >= 3` at `p = 5` (`10` unpaired) and `p = 7` (`8` unpaired).

4. **`E4` (`B1997` Open `#1` — Regular `K_4 ~= (Z / 9 Z)^2` Fiber Fourier Transform, Inversion-Closed Orbits, & Mackey Multiplicity `2`):**
   - `K_4 ~= (Z / 9 Z)^2` acts regularly on the `8` fibers of `O_81 -> O_9`, splitting `Dual(K_4) = Hom(K_4, mu_9)` under `(g . chi)(k) =
     chi(g^(-1) k g)` into `19` `S_4`-orbits (`3` of size `1`, `6` of size `3`, `10` of size `6`), of which strictly `3` inversion-closed (`chi^(-1)
     in S_4 . chi`) order-`9` size-`6` orbits annihilate `Q_r(W_+) = W_+^4 - (1 - 2(zeta_9^r + zeta_9^(-r))) W_+^2 + 4` (`r in {1, 2, 4}`) over
     `Q(cos 2 pi / 9)` with nullity `8 = 4 * 2` each (`mackey_dc = |S \ S_4 / H_chi| = 2` for `S = Stab_{S_4}(x_0)`, `x_0 = (3, 3, 3) mod 9`).

0 of 19.
