# CLAIM CARD — Constructive all-3^k proof of the 3-tower halving law (exact mod 243 polynomials & mod 729 intertwiners), Euler-commutator origin of B2005–B2006's mod 243 group jump & mod 135 counterexample, cyclotomic origin of prime 73, and P-884 E3b scoped decline (0 of 19)

- seat, branch, commit: agy, origin/agy/cusp-action-2026-11-20, efa6adb92
- kind: theorem
- touches: A01, A03, P-630, P-882, P-884
- effect: conditions — A01, A03, P-630, P-882, and P-884 (proves p_neutral(2x) = 2^d (x^2 - 9) x S(x) constructively for all 3^k with k >= 3 via the mod-27 gauge operator U_gamma and Weyl-Heisenberg shift J_k, certifies exact Z[x] equality at mod 243 of degree 1,946, explains B2005-B2006's 3^6 -> 3^7 kernel jump at mod 243 via [C^{-1}, sigma]^3 while refuting literal G_5-conjugacy and showing mod 135 keeps Z_6 + |Fix(C)| = 3 yet fails full halving, proves 73 = Phi_18(-2), independently verifies agy-exp NH-2/NH-4, and closes P-884 with a dated decline on E3b selecting K = 7)
- imports: none (pure Fricke-Markoff congruence algebra, finite group cohomology, cyclotomic number fields, and linear block-bidiagonal U(3) representation covariance; zero Standard Model pass/fail cells; order-30 line kept on hold per M18; strictly 0 of 19)
- premises on main: B1984, B1985, B1986, B1987, B1993, B1994, B1996, B1997, B1998, B1999, B2000, B2001, B2002, B2003, B2004, B2005, B2006, P-630, P-882, P-884
- decisive script: relays/agy_2026-11-25_c60/c60_listening_halving_and_p884_producer.py, SHA-256 96fab2f83f2c89f3, depends on only the standard library, sympy, and mpmath, run as `python3 -I relays/agy_2026-11-25_c60/c60_listening_halving_and_p884_producer.py`, output SHA-256 8c496b1ab052c316 (c60_out.json)
- second computation: agy disjoint cold-room countercheck relays/agy_2026-11-25_c60/c60_countercheck.py (pre-committed @ f3343ce4f, SHA-256 8567b4a32ad90406, output @ efa6adb92 SHA-256 2a6619fe3c20ccb5, algebraic 3-adic locus, 36x36 U_gamma & 108x108 T_J5 matrix checks, Berkowitz/Newton/Danilevsky polynomials, Schreier-Sims, rational Pade, 18th-root product, mp.eig, and mp.expm + mp.lu_solve, discrepancies_count == 0, agrees) and agy-exp X-NINTH-ROOTS-AND-CHIRALITY (@ 4c1d39aa3, SHA-256 5e8a2a85ab1876ca, agrees on NH-2 and NH-4)
- already on main?: topic-sweep /B200[1-6]|halving|73|P-884|3-adic layer/ on main (7b428ebe5): B2001-B2006 find halving at mod 27/81 (exact) and mod 243 (float eigensolver) and identify the 3-adic layer Z_3^2, Z_9^2, 3^7 over S_4 while leaving open the all-k proof, exact mod 243 Z[x] polynomials, why 3^6 jumps to 3^7 at mod 243, mod 45/135 pairing, closed-form mod 81 rate & prime 73, and P-884 E3b
- what would make it fail: Controls 1-6 & RPF1-5 — mod 9 gives gcd == 1; flipping gamma sign breaks U_gamma on 24 points; dropping -3*a_3 in J_k leaves O_{3^k}^- on all 324 bases while C-commuting tau_(1,1,1) collapses P_{1,2} J^* P_0 to 0; literal G_5-conjugacy misses 7,776 fixed-point elements at mod 243 and mod 135 leaves 10 unpaired modes despite Z_6 + |Fix(C)| = 3; Phi_18(+2) = 57 fails to divide disc; even K = 6 fails chiral covariance (> 1/2) while odd K = 1, 3, 5, 7, 9 all pass (< 10^{-45})

## Claim (summary, plain words and exact integers/rationals, `0 of 19`)

1. **`E1` — Constructive All-`3^k` (`k >= 3`) Proof of `p_neutral(2x) = 2^{d_neu} (x^2 - 9) x S(x)` & Exact `mod 243`
   `Z[x]` Polynomials (`Closing B2002, B2003, B2004 Open #2, & B2006 Open #2`):** On `O_{3^k}` (`|O_{3^k}| = 8 * 3^{2k-4}`,
   `x^2 + y^2 + z^2 - x y z == 0 mod 3^{k+1}`), `epsilon(3a, 3b, 3c) = a b c mod 3` splits `O_{3^k} = O_{3^k}^+ U O_{3^k}^-`
   (`U_eps W_6 U_eps = -W_6`). For all `k >= 3`, all `3` `C`-fixed points `{(3 + m * 3^{k-1})(1, 1, 1)}` lie in `O_{3^k}^+`
   (`0` in `O_{3^k}^-`), giving Euler dimension excesses `d_+^{(0)} - d_-^{(0)} = +2` and `d_+^{(1)} - d_-^{(1)} = -1`.
   Setting `gamma(x, y, z) = ((y mod 27)^2 - (x mod 27)^2) / 27 mod 3` and `U_gamma = diag(omega^{gamma(v)})` on `O_{3^k}^-`,
   `x^2 + y^2 + z^2 == x y z mod 81` forces `+1 mod 3` shifts under `C` and each step of `U_+`, proving the exact operator
   identity `U_gamma (V^2 P_2^-) U_gamma^H == W_6^2 P_1^-` and explicit charged null vector `W_6(U_gamma^{+-1} 1_{O^-}) = 0`
   (`verified through mod 729 = 52,488 points`). Schur's bipartite determinant derives the three left-out neutral modes
   `(+6, -6, 0)` from `u det(u I - V^2|_{P_0^-}) == (u - 9) det(u I - V^2|_{P_1^-})`. Base `k = 3` (`mod 27`) holds over
   `Z[x]`; for `k >= 4`, `O_{3^k}^- ->> O_{3^{k-1}}^-` is a principal `D_k`-bundle (`m_1 + m_2 + m_3 = 0`) commuting with
   `V^2` whose `[(0, 0, 0)]` sector is `O_{3^{k-1}}^-`, whose `6` non-`C`-invariant characters form two free `C`-orbits, and
   whose `[(0, 1, 2)], [(0, 2, 1)]` sectors are unitarily intertwined by the Weyl-Heisenberg shift
   `J_k(v) = v + 3^{k-2}(a_1^{-1}, a_2^{-1}, a_3^{-1} - 3 a_3) mod 3^k` (`a_i = (v_i / 3) mod 9`, obeying `[J_k, V^2] = 0`
   and `J_k C = tau_{(0, 1, 2)} C J_k`, verified through `mod 729`). Exact monic `Z[x]` polynomials certify the identity at
   `mod 27` (`d_neu = 26`), `mod 81` (`d_neu = 218`), and **`mod 243` (`d_neu = 1,946`, `x^2` coefficients `-11,688` and
   `-2,913`, matching SHA-256 across finite-field Hessenberg and Danilevsky/Newton countercheck)**.

2. **`E2` — Why the `3`-Adic Layer Jumps `3^6 -> 3^7` at `mod 243`, Refutation/Repair of `B2004` Open #1, & `mod 45` / `135`
   Counterexample to "`Z_6` Alone" (`Closing B2003 Open #3, B2004 Open #1, & B2005–B2006 Open #1`):** Because `a^2 == b^2 ==
   c^2 == 1 mod 3` on `O_{3^k}`, the cubic Euler commutator shift `x(z^2 - y^2) = 27 a (c^2 - b^2) == 0 mod 81` vanishes
   through `mod 81`, keeping `[C^{-1}, sigma]^3 = 1` and confining `K_3 = Z_3^2` (`|G_3| = 216`) and `K_4 = Z_9^2` (`|G_4| =
   1,944`) to the abelian honeycomb kernel. At `mod 243`, `81 != 0 mod 243` wakes `[C^{-1}, sigma]^3` (`exact order 3` in
   `ker(G_5 -> G_4)`), extending `Z_{27}^2` (`3^6`) to `B2006`'s non-abelian order-`3^7` kernel (`|G_5| = 52,488 = 9 |O_{243}|`,
   `|Stab(3, 3, 3)| = 9`). Literal `G_5`-conjugacy to `C^{+-1}` fails (`|Conj_{G_5}(C^{+-1})| = 3,888` vs `11,664` fixed-point
   elements outside `ker(rho)`, leaving `7,776` non-conjugate), yet all `11,664` retain `rho in {omega, omega^{-1}}` and `C`'s
   exact cycle type (`3` fixed points + `1,943` `3`-cycles). Over `Z[x]`, `mod 45 = 9 * 5` has `gcd = x^2 (x - 2)(x + 2)` (`4`
   paired modes: `0, 0, +2, -2`), while **`mod 135 = 27 * 5` preserves BOTH `Z_6` (`via G_{135} ->> G_{27} ->> Z_6`) AND
   `|Fix(C)| = 3` yet fails full halving**, pairing `949` of `959` charged modes and leaving the `10` roots of
   `(x^2 - 2x - 2)(x^2 + 2x - 2)(x^3 - 3x - 1)(x^3 - 3x + 1)` unpaired (`since (sigma C)^3 sigma C^{-1}` fixes `3` points on
   `O_{27}` and `0` on `O_5`).

3. **`E3` — Closed Cyclotomic Radical Form of `mod 81` Rates & Origin of Prime `73` (`Closing B2002 Open #3 & B2001 Open #2`):**
   `P_6(x) = x^6 - 60 x^4 + 1008 x^2 - 4672` divides `p_neutral_81(x)` over `Z[x]` and transforms under `x^2 = 4(5 + u)` into
   `64(u^3 - 12 u - 8)` (`u = 4 cos(pi / 9)`), proving `lambda_{neu, 81} = 2 |2 + zeta_{18}| = 2 sqrt(5 + 4 cos(pi / 9))` and
   `lambda_{chg, 81} = sqrt(5 + 4 cos(pi / 9))` (`residual < 10^{-56}`). Setting `y = x / 2` gives `y^6 - 15 y^4 + 63 y^2 - 73
   = 0` with exact Zassenhaus `round_two` field discriminant `disc(Q(y)) = 30,652,992 = 2^6 * 3^8 * 73`, where `3^8 =
   disc(Q(cos(2 pi / 9)))^2` and **`73 = N_{Q(zeta_{18})/Q}(2 + zeta_{18}) = Phi_{18}(-2)`** (`generalizing mod 27's
   Phi_6(-2) = 7`).

4. **`E4` & `E5` (`agy-exp` `NH-2`/`NH-4` Second Computation & `M18` / `P-884` Concessions + `E3b` Dated Decline):**
   Independently proves `det(mu I_6 - W_+^2(theta)) == (mu - 1)^2 (mu^2 - (1 + 4 cos theta) mu + 4)^2` (`matching all 5
   odd-prime rates to < 10^{-25}`) and `(4 s + 6) / (s + 6) -> 4 : 1`. Concedes `M18` items `2`–`5` (`keeping order-30 on hold;
   verifying M_21 Schur scaling M_0^{-(K-1)} to < 10^{-55}`) and proves across `K = 1..9` that while even `K in {2, 4, 6, 8}`
   violates `U_Q (...) U_{q_R}^H` covariance (`> 1/2`), **every odd `K in {1, 3, 5, 7, 9}` is equally gauge-covariant (`<
   10^{-55}`)**, grounding an explicit **dated decline (`2026-11-25`) on `E3b` selecting `K = 7` without importing the
   `-R_sigma` vertex-wall interval**.

0 of 19.
