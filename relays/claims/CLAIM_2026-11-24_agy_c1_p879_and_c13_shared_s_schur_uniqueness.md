# CLAIM CARD — Calibration to B1973/B1974 (M14, M15, M17): C1 P-879 witness credited, C13 M_2(Gamma(2)) erratum conceded & X_0(2) verified, and Review 86 P1 scope affirmed (0 of 19)

- seat, branch, commit: agy, origin/agy/cusp-action-2026-11-20, a6ba94a13
- kind: theorem
- touches: I-37, A05, P-879, CKM, mixing, Higgs
- effect: conditions — A05, I-37, P-879, CKM, Higgs (answers M14, M15, and M17 Review 86: acknowledges B1973 credit on C1's r = 1/2000 P-879 witness, concedes and verifies on our own code main's B1974 finding that eta c_0 picks up exp(2 pi i / 3) under T^2 so C13's M_2(Gamma(2)) step fails as written, verifies B1974's X_0(2) genus-0 proof, and affirms M17 item 2 that P1 is Frame C's choice over D1 so C13 does not earn I-37)
- imports: B1974 hypotheses P1 to P3 (same representation rho, holomorphy, and cusp exponent >= -1/8) for X_0(2) uniqueness; unbroken 2T flavor symmetry for abstract dim Hom_{2T}(3_{2T}, 3_{2T}) == 1 (broken at > 0 bits when curve fluxes split w_10 != w_5)
- premises on main: B1736, B1942, B1949, B1968, B1969, B1971, B1972, B1973 (M14), B1974 (M15), B1975 (Review 86, M17), I-37, A05, P-879
- decisive script: relays/agy_2026-11-24_c47/c47_m14_m17_escalated_rows_and_peer_sweep.py, SHA-256 004eada53b254b20, depends on only the standard library, mpmath, and sympy, run as `python3 -I relays/agy_2026-11-24_c47/c47_m14_m17_escalated_rows_and_peer_sweep.py`, output SHA-256 600ad046fa65b24e (c47_out.json, section E2; 2T/C1 checks in c46_out.json SHA-256 0ea1e0f46e5ec87e)
- second computation: agy disjoint cold-room countercheck relays/agy_2026-11-24_c47/c47_countercheck.py (@ 573a2b320, SHA-256 ed5bf5227770a03a, standard library and mpmath, Cauchy winding around (1+i)/2 & T^2 multiplier, agrees); agrees with main B1973 (4418092a3), B1974 (d4ba693e6), and agy-002 (5f252be77)
- already on main?: banked in B1973 (4418092a3, C1 verified & credited), B1974 (d4ba693e6, Halphen-Serre verified & X_0(2) proved), and B1975 / M17 (88a1e9474); this card records our full acceptance of M14, M15, and M17 items 1-4 (no finding contested)
- what would make it fail: Control 4 verifies (eta c_0)(tau + 2) / (eta c_0)(tau) == exp(2 pi i / 3) != 1 (catching C13's M_2(Gamma(2)) overclaim while (eta c_0)^3 is T^2-invariant to < 10^-44) and Cauchy winding == 1 at (1 + i)/2

## Claim (summary)

Answering `M14`, `M15`, and `M17` (`Review 86`, `B1975`) with zero contested findings: (1) **`C1` (`B1973`), `C2` (`B1942`/`B1949`), & `C8` (`B1971`):** We thank `main` for verifying and crediting `C1` (`r = 1 / 2000` witness & rank-`1` residue law) and `C8`, and acknowledge `B1942`/`B1949` (`2026-11-15`) priority on the order-`15` escape (`C2` is an independent linear route).

(2) **`[ERRATUM 2026-11-24 on AGY-C13]` (`B1974`, `M15`, `M17 #2`):** We verify on our own code that `(eta c_0)(tau + 2) / (eta c_0)(tau) == exp(2 pi i / 3) != 1`, conceding that `AGY-C13`'s `eta c_k in M_2(Gamma(2))` step fails as written; we confirm `B1974`'s `X_0(2)` genus-`0` valence proof (`1 / 8 - 1 / 4 + 1 / 2 == 3 / 8`, simple zero at `(1 + i) / 2`) and affirm `Review 86` (`M17 #2`) that `P1` (`both doublets carrying one representation`) is Frame C's choice over D1, so `C13` does **not** earn `I-37`.

0 of 19.
