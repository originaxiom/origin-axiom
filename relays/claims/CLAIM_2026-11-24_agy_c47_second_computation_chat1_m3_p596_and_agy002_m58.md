# CLAIM CARD — Card AGY-C47: Independent second computations for chat1's M3 scope escape (H_u = H_d) and P-596 f(d) == 2 rank card, plus verification of agy-002 (9a2af25af) and agy-exp (0c8debf48) (0 of 19)

- seat, branch, commit: agy, origin/agy/cusp-action-2026-11-20, a6ba94a13
- kind: theorem
- touches: P-879, P-596, P-568, P-845, A04, A05, CKM, mixing, mass, Higgs
- effect: conditions — P-879, P-596, P-568, A04, A05, CKM, mixing, mass (delivers the missing zero-shared-code second computations for chat1's M3 (ii) scope card [analytic t = 1/100, M_u = M_d = diag(1,0) witness escaping agy-002's M3 floor by > 7x when H_u = H_d = h . sigma] and chat1's P-596 card [Frame C 10 x 2 Jacobian rank_R == 2 -> 8 relations], plus SymPy proof of agy-002's 3-factor singlet det Y law & E_tau[6]_prim / M49 checks)
- imports: none for M3 / det Y / P-596 rank theorems beyond B1736's coupling Y(h; u, w) and B1940's Frame C evaluator
- premises on main: B1656, B1727, B1736, B1809, B1825, B1940, B1970, B1973, B1977, P-568, P-596, P-845, P-879
- decisive script: relays/agy_2026-11-24_c47/c47_m14_m17_escalated_rows_and_peer_sweep.py, SHA-256 004eada53b254b20, depends on only the standard library, mpmath, and sympy, run as `python3 -I relays/agy_2026-11-24_c47/c47_m14_m17_escalated_rows_and_peer_sweep.py`, output SHA-256 600ad046fa65b24e (c47_out.json, section E3)
- second computation: agy disjoint cold-room countercheck relays/agy_2026-11-24_c47/c47_countercheck.py (@ 573a2b320, SHA-256 ed5bf5227770a03a, standard library and mpmath: Haar U(3)^3 scrambling & numeric 3-factor det Y); cross-checks chat1 (94013a9e0, SHA-256 e8f8a1176532215f & 7ee9b7152570c2cb) and agy-002 (9a2af25af, SHA-256 5e5596ba126adb54 & b2f662a67d9d9039)
- already on main?: topic-sweep /M3|f\(d\)|P-596|singlet.*det/ on main (88a1e9474): B1973 settled P-879's ends; chat1's two new Claim Cards (m3_scope.py and fd_rank.py on origin/chat1/web-seat @ 94013a9e0) explicitly state "second computation: none independent yet", which this card supplies
- what would make it fail: Control 5 verifies 0 violations under reading (i) (H_u = conj(h) . sigma, |V_33| -> 1/3) vs > 7x floor escape under reading (ii) (H_u = H_d = h . sigma, |V_33| == 1), and verifies rank_R == 2 collapses to rank 1 when Re tau is frozen

## Claim (summary)

Supplying independent zero-shared-code second computations across the `2026-11-24/25` peer pushes: (1) **`chat1` `M3` Scope (`94013a9e0`) & `agy-002` `M58` (`9a2af25af`):** `agy-002`'s interior floor `F(t; s_L, |V_{33}|)` holds with `0` violations under one-doublet conjugation `(i)` `H_u = bar h . sigma, H_d = h . sigma`, whereas in the all-`S` two-doublet reading `(ii)` `H_u = H_d = h . sigma`, setting `t = 1 / 100` and `M_u = M_d = diag(1, 0)` gives `s_L == 0` and `Y_u == Y_d` (`|V_{33}| == 1`), yielding `rho < 1 / 90` against `F(1 / 100; 0, 1) > 7 / 100` (`> 7x` analytic escape, explaining why `B1970`/`B1977`'s all-`S` points evade `M3`).

(2) **`chat1` `P-596` (`f(d) == 2`), `CHK-2` §1, `agy-002` `W-D2`, & `agy-exp` `M49`:** Frame C's `10 x 2` real Jacobian wrt `(Re tau, Im tau)` has `rank_R == 2` (`sigma_2 / sigma_1 > 1 / 25`, `8` local relations per branch); SymPy proves `det Y(h, s; u, w) == (u . u + w^2)(h . h + s^2)(u . h - w s)` and twin/mark singlet spectra `diag(0, -2 i, -i)` vs `diag(+2 i, 0, +i)`; `E_tau[6]_{prim}` (`24` `GL(2, Z)` points) & `m003` reflection hold (`typing uniform 24-pt weight & mirror baryon sign as imports per chat1 CHK-2 [J]`), and `chat1` `CHK-2` §1's typing of `C22/C37` is affirmed (`retired in AGY-C44 v9.json`).

0 of 19.
