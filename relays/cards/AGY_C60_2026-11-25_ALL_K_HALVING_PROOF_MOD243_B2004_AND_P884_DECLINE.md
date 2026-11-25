# Card `AGY-C60` — Constructive All-`3^k` Proof of the `3`-Tower Halving Law (`mod 243` Exact Polynomials & `mod 729` Intertwiners), `B2004`–`B2005` Group & `mod 135` Resolution, Cyclotomic Origin of Prime `73`, `agy-exp` `NH-2`/`NH-4` Second Computation, and `P-884` `E3b` Scoped Decline (`0 of 19`)

- **Seat / Branch:** `agy` on `agy/cusp-action-2026-11-20` (`origin/agy/audit-2026-11-02` untouched at `4319f47e2`;
  `AGY-C1..C59` and `v1..v9.json` preserved untouched on disk per `WORKING_RULES.md` Rule `3`; synced to
  `origin/main @ ccbca22e1` [`M18`, `B1999`–`B2005`] and `agy-exp @ 4c1d39aa3` [`X-NINTH-ROOTS-AND-CHIRALITY`]).
- **Package & Scope:** Advances `P-882` (`B2001`–`B2005`) strictly in the pure-listening weave with **zero Standard
  Model scaffolding, zero pass/fail target cells, and zero empirical values** (`keeping the order-30 line on hold per
  M18 item 5`), while closing `M18` / `P-884` with explicit concessions on items `2`–`5` and a decisive script plus
  dated decline on `E3b` as a selector of `K = 7`.
- **Empirical Firewall & Section-Twelve Check Labels:** `0 of 19` (`strictly data-free`); `computed once`,
  `expectations committed first`, `tested against planted errors` (`6` producer + `5` countercheck; `303 / 303`
  cumulative across active `C31..C48`, `C56`, `C59`, and `C60`), and `recomputed independently` strictly on cross-seat
  items (`B2001`–`B2005` & `agy-exp` `NH-2` / `NH-4`).

## Pre-Committed Mathematical Expectations (`E1`–`E5` & `Controls 1`–`6`, Plain Words & Exact Rationals)

1. **`E1a` (Bipartite Fixed-Point Euler Defect & Mod-`27` Gauge Operator `U_gamma` for All `k >= 3`, Closing `B2004`
   Open #2):** On `O_{3^k}` from `(3, 3, 3)` (`|O_{3^k}| = 8 * 3^{2k - 4}`, `x^2 + y^2 + z^2 - x y z == 0 mod 3^{k+1}`),
   `epsilon(3a, 3b, 3c) = a b c mod 3` in `{+1, -1}` gives an `S_3`-invariant bipartition `O_{3^k}^+ U O_{3^k}^-`
   (`U_eps W_6 U_eps = -W_6`). For all `k >= 3`, all `3` `C`-fixed points `{(3 + m * 3^{k - 1})(1, 1, 1)}_{m = 0, 1, 2}`
   lie in `O_{3^k}^+` (`0` in `O_{3^k}^-`, whereas at `mod 9`, `(6, 6, 6)` lies in `O_9^-`), giving `d_+^{(0)} - d_-^{(0)}
   = +2` and `d_+^{(1)} - d_-^{(1)} = -1`. Setting `gamma(x, y, z) = ((y mod 27)^2 - (x mod 27)^2) / 27 mod 3` and
   `U_gamma = diag(omega^{gamma(v)})` on `O_{3^k}^-`, `x^2 + y^2 + z^2 == x y z mod 81` forces `+1 mod 3` shifts under
   `C` and all three directed steps of `U_+`, proving `U_gamma (V^2|_{P_1^-}) U_gamma^H == W_6^2|_{P_2^-}` and
   `W_6(U_gamma^{+-1} 1_{O^-}) = 0` (`verified through mod 729 = 52,488 points`). Schur's bipartite determinant derives
   the three left-out neutral modes `(+6, -6, 0)` from `u det(u I - V^2|_{P_0^-}) == (u - 9) det(u I - V^2|_{P_1^-})`.
2. **`E1b` (Inductive Weyl-Heisenberg Intertwiner `J_k` for All `k >= 4` & Exact `mod 243` Integer Polynomials, Closing
   `B2002`, `B2003`, & `B2005` Open #1):** Base `k = 3` (`mod 27`, `d_neu = 26`) holds over `Z[x]`. For `k >= 4`,
   `O_{3^k}^- ->> O_{3^{k - 1}}^-` is a principal `D_k`-bundle (`D_k = {m in F_3^3 : m_1 + m_2 + m_3 = 0}`) commuting
   with `V^2`: `[(0, 0, 0)]` pulls back `O_{3^{k - 1}}^-`, the `6` non-`C`-invariant characters form two free `C`-orbits,
   and on `[(0, 1, 2)], [(0, 2, 1)]` the explicit shift `J_k(v) = v + 3^{k - 2}(a_1^{-1}, a_2^{-1}, a_3^{-1} - 3 a_3)
   mod 3^k` (`a_i = (v_i / 3) mod 9`) preserves `O_{3^k}^-`, commutes with `V^2`, and obeys `J_k C = tau_{(0, 1, 2)} C J_k`
   (`verified through mod 729`), unitarily intertwining `V^2|_{P_0^-}` and `V^2|_{P_1^-}` for all `k >= 4`. Exact monic
   `Z[x]` characteristic polynomials verify `p_neutral(2x) == 2^{d_neu} (x^2 - 9) x S(x)` at `mod 27` (`d_neu = 26`),
   `mod 81` (`d_neu = 218`), and `mod 243` (`d_neu = 1,946`, upgrading `B2003`'s float eigensolver check to exact `Z[x]`;
   `Controls 1`–`3`: `mod 9` `gcd = 1`; `+` in `gamma` fails `U_gamma`; symmetric `J` without `-3 a_3` commutes with `C`).
3. **`E2` (`B2004` Open #1 & `B2005` Open #2 Group Jump at `mod 243`, Plus `mod 45` & `mod 135` Counterexample to
   "`Z_6` Alone"):** At `mod 27` (`|G_3| = 216`) and `mod 81` (`|G_4| = 1,944`), `Stab_{G_k}(3, 3, 3) = <C>`, because the
   Euler commutator shift `x(z^2 - y^2) = 27 a (c^2 - b^2) == 0 mod 81` keeps `[C^{-1}, sigma]^3 = 1` inside the
   metabelian honeycomb quotient `(Z / (2 * 3^{k - 2}) Z)^2 |x S_3`. At `mod 243`, `81 != 0 mod 243` wakes `[C^{-1},
   sigma]^3` (`order 3` in `ker(G_5 -> G_4)`), jumping `|G_5|` by `27` to `52,488 = 9 |O_{243}|` (`|Stab(3, 3, 3)| = 9`):
   `7,776` elements outside `ker(rho)` fix `3` points without lying in `Conj_{G_5}(C^{+-1})` (`Control 4`, refuting literal
   `G_k`-conjugacy), while all `11,664` still obey `rho in {omega, omega^{-1}}` and `C`'s cycle type. Over `Z[x]`, `mod 45`
   gives `gcd = x^2 (x - 2)(x + 2)` (`4` modes), while **`mod 135 = 27 * 5` keeps BOTH `Z_6` (`via G_{135} ->> G_{27} ->>
   Z_6`) AND `|Fix(C)| = 3` yet fails full halving**, pairing `949` of `959` modes and leaving `10` unpaired roots of
   `(x^2 - 2x - 2)(x^2 + 2x - 2)(x^3 - 3x - 1)(x^3 - 3x + 1)` (`as (sigma C)^3 sigma C^{-1}` fixes `3` on `O_{27}` and
   `0` on `O_5`), sharpening `B2005`'s `Z_6` criterion.
4. **`E3` (Closed Cyclotomic Form of `mod 81` Rates & Origin of Prime `73`, Closing `B2002` Open #3 & `B2001` Open #2):**
   Substituting `x^2 = 4(5 + u)` into `P_6(x) = x^6 - 60 x^4 + 1008 x^2 - 4672` gives `64(u^3 - 12 u - 8)` (`u = 4 cos(pi/9)`),
   proving `lambda_{neu, 81} = 2 |2 + zeta_{18}| = 2 sqrt(5 + 4 cos(pi / 9))` and `lambda_{chg, 81} = sqrt(5 + 4 cos(pi / 9))`
   (`residual < 10^{-50}`). Setting `y = x / 2` gives `y^6 - 15 y^4 + 63 y^2 - 73 = 0`, with exact field discriminant
   `disc(Q(y)) = 2^6 * 3^8 * 73`, where `3^8 = disc(Q(cos(2 pi / 9)))^2` and **`73 = N_{Q(zeta_{18})/Q}(2 + zeta_{18}) =
   Phi_{18}(-2)`** (`generalizing mod 27's Phi_6(-2) = 7`; `Control 5`: `Phi_{18}(+2) = 57` does not divide `disc`).
5. **`E4` & `E5` (`agy-exp` `NH-2`/`NH-4` Second Computation & `M18` / `P-884` `E3b` Scoped Decline):** Symbolically
   verifies `det(mu I_6 - W_+^2(theta)) == (mu - 1)^2 (mu^2 - (1 + 4 cos theta) mu + 4)^2` and all `5` odd-prime benchmarks
   (`M in {3, 9, 5, 25, 7}`) plus `(4 s + 6) / (s + 6) -> 4 : 1` across `7` Markoff nodes. Under independent `U(3)`
   rotations `U_Q != U_{q_R}` across `K = 1..9`, alternating products fail chiral covariance for all even `K in {2, 4, 6, 8}`
   (`defect > 1/2`) and satisfy exact `U_Q (...) U_{q_R}^H` covariance (`< 10^{-45}`) for **every odd `K in {1, 3, 5, 7, 9}`**
   (`Control 6`), establishing our dated decline on `E3b` selecting `K = 7` without importing the `-R_sigma` vertex-wall
   interval (and confirming `M_21` Schur scaling `M_0^{-(K - 1)}`), with disjoint countercheck achieving `discrepancies == 0`.

0 of 19.
