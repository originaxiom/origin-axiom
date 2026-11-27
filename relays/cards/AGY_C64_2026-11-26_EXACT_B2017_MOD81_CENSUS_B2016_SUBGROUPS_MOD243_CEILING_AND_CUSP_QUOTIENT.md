# `Card AGY-C64` (`2026-11-26`) — Exact `B2017` Census Closure & `mod 81` Off-Cusp Halving Orbits, `B2016` Subgroup-Lattice & `rho`-Intertwining Theorems, `B2015` Float-Free `mod 243` New-Fiber Minimal Polynomial, & Maximal Honeycomb-Abelian Quotient Law (`0 of 19`)

- **Seat / Branch / Base Commit:** `agy` / `origin/agy/cusp-action-2026-11-20` / `e4cd4c7eb`
  (continuing cleanly after `AGY-C63`; frozen harvest branch `origin/agy/audit-2026-11-02` untouched at `4319f47e2`;
  sealed `AGY-C1..C63` untouched)
- **Synced Premises:** `origin/main @ ed9660a9d` (`M19`, `M20`, `B2011`–`B2017`, `P-885`),
  `agy-exp @ f250ed349` (`X-MIXED-TOWERS-AND-HASSE`), `agy-002 @ 765c453a7` (`A2-P629-VEFF-MODULUS`),
  `chat1 @ 19bc14af9` (`A84`)
- **Strict Scope (`0 of 19`):** Exact rational Newton–trace and `Z[x]` polynomial classification of finite Markoff
  `<L, R>`-orbits, finite solvable subgroup-lattice classification and `Z[omega]` operator-intertwining theory on
  `G_3` and `G_4`, `Z`-module nullspace and closed-walk trace inequalities on the `mod 243` covering fiber, and
  commutator-quotient Bloch dispersion on finite honeycomb tori. Zero empirical constants, zero added parameters,
  zero Standard Model pass/fail cells; order-`30` line kept on hold per `M18` item `5`.

---

## Pre-Committed Expectations (`E1`–`E4`) and Falsification Controls (`PF1`–`PF5`)

1. **`E1` (`Closing B2017 Disclosures #1 & #2 — Complete Exact Q/Z Census at mod 9, 27, 49, & mod 81, Uncovering 15 Off-Cusp-Leaf Halving Orbits at mod 81`):**
   - **Expectation `E1a` (`Aut(A^3)` Generator Equivalence & Exact Closure of `B2017`'s `41` Non-Exact/Left-Out Orbits):**
     In `Aut(A^3)`, `R^{-1} L(x, y, z) = (y, z, x) = C` and `R L^{-1} R(x, y, z) = (y, x, x y - z) = sigma`, so
     `<L, R> = <C, sigma>` preserves every orbit on every leaf over every commutative ring, with `d_0 - d_1 = |Fix(C)|`.
     Whenever `S(x)` divides `h(x) = 2^{-d_0} p_{neu}(2 x)` in `Z[x]`, the monic quotient `R(x) = h(x) / S(x)` of
     degree `r = |Fix(C)|` has real roots in `[-3, 3]`, forcing exact integer power sums `p_m = 2^{-m} tr(Q^m) -
     tr(M_{chg}^m)`, `0 <= p_2 <= 9 r`, `0 <= p_4 <= 81 r`, Cauchy–Schwarz `p_1^2 <= r p_2`, `p_2^2 <= r p_4`, and
     Newton integrality `k | sum_{j=1}^k (-1)^{j-1} e_{k-j} p_j` (`with e_k = 0 for k > r`). Applying this exact `Q`
     filter eliminates **all `6` double-precision orbits at `mod 27`** (`> 1,200` pts), **all `14` double-precision
     orbits at `mod 49`** (`1,200 < n <= 2,400`), and **all `21` left-out orbits at `mod 49`** (`> 2,400` pts, where
     `|Fix(C)| in {0, 1}`), upgrading `B2017`'s `417`-orbit census to **`100%` exact over `Q/Z` with `0` left-out
     orbits**; at `mod 9` (`729` residues, `24` orbits), all `24` lie in Category `(c)`.
   - **Expectation `E1b` (`Complete Exact All-Residue Census at mod 81` & `PF1`–`PF2`):** Across all `531,441`
     residues (`489` orbits) at `mod 81`: all `63` large orbits (`> 2,400` pts) fail exact rational Newton–trace
     identities (`63/63`), `408` smaller orbits lie in `(c)` (`verified over Z[x]`), `0` lie in strict `(b)`, and
     **exactly `18` orbits halve — `15` of them OFF the cusp's leaf `k == 0 mod 81`** (`correcting B2017 C3's scope
     beyond mod 27`, while all `18` remain inside the `3`-adic core `3 | v_i`, `9 | k`):
     - **`6` in `(a)` (`648` pts, `d_0 = 218, d_1 = 215, |Fix(C)| = 3`):** `3` on `k = 0` (`(3,3,3), (3,3,30),
       (3,3,33)`) and **`3` lifts of `(3,3,12)` on `k = 54 mod 81`** (`(3,3,12), (3,3,24), (3,3,39)`).
     - **`12` in `(a')` (`no left-out modes`, `h(x) = S(x)`, `|Fix(C)| = 0`):** `3` lifts of `(3,3,15)` (`648` pts)
       on **`k = 27 mod 81`** (`(3,3,15), (3,3,21), (3,3,42)`), plus **`9` newly emerging `216`-point orbits (`d_0 =
       d_1 = 72`) on leaves `k in {9, 36, 63} mod 81`** (`(3,9,9), (9,9,24), (9,9,30)` on `k = 9`; `(6,9,9),
       (9,9,21), (9,9,33)` on `k = 36`; `(9,9,12), (9,9,15), (9,9,39)` on `k = 63`), whose `24`-pt `mod 27`
       projections on `k = 9 mod 27` lie in `(c)` at `mod 27`.
     - **Controls `PF1` & `PF2`:** Replacing `9 -> 4` in `x(x^2 - 9)` rejects `(3,3,3) mod 27` (`PF1`); filtering
       `mod 81` only on `k == 0 mod 81` finds `3 != 18` (`PF2`).

2. **`E2` (`Closing B2016's Subgroup & Coset Questions — Operator-Intertwining Theorem for (a') and Exhaustive G_3, G_4 Lattice Classification`):**
   - **Expectation `E2a` (`All-Group Category-(a') Intertwining Theorem` & `PF3`):** For any finite group `G = <C,
     sigma>` admitting `rho: G -> mu_6` with `rho(C) = omega, rho(sigma) = -1` and any subgroup `H <= ker(rho)`,
     pointwise multiplication `(M_rho f)(H g) = rho(g) f(H g)` on `l^2(G / H)` satisfies `R_C M_rho = omega M_rho R_C`
     (`forcing |Fix_{G/H}(C)| = 0 and d_0 = d_1`) and, since `-(omega + omega^2) = +1` on each move pair `{sigma C^2,
     sigma C}`, `{C sigma, C sigma C}`, `{C^2 sigma, C^2 sigma C^2}`, satisfies the exact operator similarity
     `2 W_6|_{H_1} M_rho = M_rho W_6|_{H_0}` (`2 M_1 D_rho = D_rho Q` over `Z[omega]^x`), forcing `h(x) = S(x)`
     (`Category (a')`). Flipping `rho(sigma) = -1 -> +1` breaks `2 W_{chg} - W_{neu} == 0` (`PF3`).
   - **Expectation `E2b` (`Exhaustive G_3 and G_4 Subgroup Lattice Classification`):** Separating `(a')` from `(b)`
     across all `45` subgroup classes of `G_3` (`order 216`) and all `100` classes of `G_4` (`order 1,944`) yields:
     - `G_3` (`mod 27`): `4` in `(a)`, **`10` in `(a')`**, **`0` in strict `(b)`**, `31` in `(c)`.
     - `G_4` (`mod 81`): `8` in `(a)`, **`28` in `(a')`**, **`0` in strict `(b)`**, `64` in `(c)`.
     Thus **zero coset spaces of `G_3` or `G_4` pair without halving** (`all 10 and 28 of B2016's row (b) halve in
     (a')`), with **`G_k / H in (a') <=> H <= ker(rho)` (`0` mismatches)** and **`G_k / H in (a) <=> H` contains a
     conjugate of `C` and `6 | [G_k : H]` (`<=> g H g^{-1} in [<C>, M_6]`, `0` mismatches; the `4` failing `<C>`-
     overgroups at both levels have indices `8, 4, 2, 1`, factoring through the `8`-pt `mod 9` cube `{3, 6}^3` where
     `|Fix(C)| in {1, 2} != 3`)**.

3. **`E3` (`Closing B2015 R2 Double-Precision Gap — Exact Degree-36 Minimal Polynomial & Float-Free Closed-Walk Ceiling at mod 243`):**
   - **Expectation `E3` & `PF4`:** On `O_{243}` (`5,832` pts), the normal closure `K = <<[C^{-1}, sigma]^3>>_{G_5}` has
     exact order `9`, is abelian, and acts freely on every `mod 81` fiber. The top `mod 243` new-fiber eigenvalue has
     **irreducible degree-`18` minimal polynomial in `v = (x / 2)^2`** (`irreducible degree 36 in x`):
     `g_{new}(v) = v^{18} - 63 v^{17} + 1809 v^{16} - 31359 v^{15} + 366453 v^{14} - 3053187 v^{13} + 18711432 v^{12}
     - 85809456 v^{11} + 296843940 v^{10} - 775628381 v^9 + 1524253446 v^8 - 2231533503 v^7 + 2396964081 v^6 -
     1846648809 v^5 + 986438304 v^4 - 346325130 v^3 + 72709677 v^2 - 7444224 v + 180361`,
     certified over `Z` by a nonzero `{-1, 0, +1}` witness vector (`38` nonzeros in `tau_{12} = +1`, zero sum on all
     `108` `mod 81` fibers, `f_{new}(S_{243}) z_0 == 0`), with Sturm isolation `321725642458145 / 10^{13} < 4 v_{max}
     < 321725642458146 / 10^{13}` (`0` roots above). Across all `5,184` new-fiber modes, exact integer closed-walk
     trace difference `Delta_{64} = tr(S_{243}^{32}) - tr(S_{81}^{32})` satisfies `Delta_{64} < 35^{32}` (`while
     8(15/16)^3 - 6(15/16) - 1 = -17/512 < 0` proves `35 < 20 + 16 cos(pi / 9)`, and halving bounds charged modes by
     `x^2 <= 9 < 35`; `PF4: 32^{32} < Delta_{64}`).

4. **`E4` (`Maximal Honeycomb-Abelian Quotient Formula M_{ab}, Exact Z[x] Proof of B2015 R1 at mod 625, & Continuum Cusp Gap`):**
   - **Expectation `E4` & `PF5`:** Quotienting by the Hofstadter plaquette commutator `O_{ab} := O / <<[L^2, R^2]>>`,
     **`M_{ab} := ord_{O_{ab}}(L^2) / 2`** equals `{3, 9, 9, 5, 25, 7}` across all six computed cusp-cone levels
     `(27, 81, 243, 125, 625, 343)` (`scoped explicitly to the six levels run per Review 87`): at `mod 243`,
     `<<[L^2, R^2]>>` has fiber size `9`, collapsing `O_{243,ab} -> O_{81}` (`648` pts, `M_{ab} = 9`, whereas
     unquotiented `ord(L^2) / 2 = 27` fails, `PF5`); at `mod 625` (`3,000` pts), `<<[L^2, R^2]>>` has fiber size `5`,
     leaving a `600`-point bipartite quotient `O_{625,ab}` (`M_{ab} = 25`) on which an exact integer witness vector
     certifies `minpoly(20 + 16 cos(pi / 25)) | charpoly(W_6^2)` **over `Z[u]`** (`upgrading B2015 R1 at mod 625 from
     mod-3-primes to exact Z`). On universal `T_{2M}`, `6 - 2 sqrt(5 + 4 cos(pi / M)) = (2 / 3) pi^2 M^{-2} -
     (1 / 54) pi^4 M^{-4} + O(M^{-6})`.

0 of 19.
