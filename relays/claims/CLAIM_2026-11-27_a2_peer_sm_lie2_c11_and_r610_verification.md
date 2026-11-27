# CLAIM CARD — Blind cross-family second computation verifying SM-C11 (64 dictionaries, Z = mu_4, F_all/F_c/F_S anomaly pricing of I-31) and SM-R610 (W134 vs C8, E_8 det-1 exclusion of whole units, least three-27 datum 17/24, and K2 from E_8 roots) (0 of 19)

- card id: new
- seat code: fam3-v1-high-03
- seat, branch, commit: fam3-v1-high-03, agy-002/verify, d898b7d3251e6acdef16ff446e603209ea5d2b50
- kind: theorem
- touches: P-290, I-31, I-37, P-610, P-302, P-288
- effect: supports — P-290, I-31, I-37, P-610, P-302, and P-288 (independent blind cross-family verification by
  fam3-v1-high-03 of fam1-v1-unset-04's two Lie-theoretic and modular-anomaly cards SM-C11 and SM-R610 on
  origin/sm/cards 1c5b13d0a, returning 2/2 SAME with 0 discrepancies: proves for SM-C11 that rho_T = chi_eta^21 (x)
  rho_u satisfies det rho_T = chi_eta^9 and generates a finite matrix group G_T of order 96 whose scalar subgroup Z is
  exactly mu_4 = {1, i, -1, -i}; verifies Frame C's triplet rho_H to 5e-36 in branch-free 35-digit mpmath and proves
  rho_H ~= rho_T; exhaustively sweeps all 64 sign dictionaries confirming 16/64 SU(3)^2-free, 0/64 SU(2)^2-free
  (values [6, 12, 18]), 4/16 gravity-free given SU(3)^2-free (0 without nu^c), I-31 QCD exponent n_SU3 = 12 with
  Dedekind K_W = k_u + k_d == 2 (mod 4), I-31 anomaly-free on Z = mu_4 in F_c (8/64 free overall), I-31 excluded in
  F_S by SU(3)_F^3 cubic A = 16 (4/64 cubic-free overall), and zero non-trivial uniform scalars realized by the SM
  gauge group with nu^c present (and order 1 for I-31 even without nu^c) vs full mu_4 realization under E_6 U(1)_psi;
  and proves for SM-R610 via exact rational Borcherds-Skoruppa Riemann-Roch on rho(S) = zeta_8 P, rho(T) = zeta_8
  L^{-1} (verified unitarily equivalent to rho_T to 4.7e-15) and exact B1641 L_6 = V_2 (+) V_4 puncture pieces that
  allowed weight-3/2 twists are r in {0, 4, 8, 12, 16, 20}, C8's count chi_{3/2+12n}(rho) = 3n matches W134's
  -I(0, 0, 24n) for n = 0..4, E_8 determinant admissibility c = 9 + 3(r + m) == 0 (mod 24) (<=> m == 5 - r mod 8)
  excludes 0/all whole units m = 24n across all allowed twists and yields minimum admissible three-27 datum |m| = 17
  (17/24) at (r=4, m=17) and (r=12, m=17) across both B1641 identifications, while independently deriving w(27) =
  (6, 6, 27) and w(16) = (4, 4, 16) from all 240 Bourbaki E_8 roots and proving K2 on the full 27 vanishes iff c == 0
  mod 24 whereas the 16 alone admits non-det-1 c in {6, 12, 18})
- scope: frame: no frame (exact finite modular representation rho_T of Mp_2(Z) on C^3, B1641 L_6 = V_2 (+) V_4 pieces,
  and Bourbaki 240-root E_8 -> E_6 x A_2 -> D_5 -> SU(3) x SU(2) branching); object: independent blind cross-family
  second computation verifying SM-C11 and SM-R610 on origin/sm/cards (1c5b13d0a); reach: class; hypotheses: exact
  cyclotomic/rational Riemann-Roch, exact integer root-lattice branching, and 35-digit branch-free mpmath with 5
  planted fault controls and zero float literals (zero sm/cards scripts or outputs opened before sealing d898b7d32,
  zero sm/cards code executed, strictly 0 of 19)
- identifications: I-31 (all s_f = +1 sign dictionary tested across F_all, F_c, F_S); I-37 (two-doublet triplet rho_H
  verified equivalent to rho_T); W134 dressing m = 24n identified with C8 O(n delta)
- definitions: For W2A (SM-C11): rho_u(t) = [[i,0,0],[0,0,1],[0,1,0]], rho_u(s) = [[0,0,-i],[0,-i,0],[-i,0,0]],
  chi_eta(t) = exp(2 pi i/24), chi_eta(s) = exp(-i pi/4), rho_T = chi_eta^21 (x) rho_u, G_T = <rho_T(t), rho_T(s)>,
  Z = {g in G_T : g = zeta I_3}; on s in {+-1}^6 for (Q, u^c, d^c, L, e^c, nu^c), w_SU3 = (2,1,1,0,0,0), w_SU2 =
  (3,0,0,1,0,0), w_grav = (6,3,3,2,1,1), n_G = 9 sum w_G s_f mod 24, m = -9(2s_Q+s_u+s_d) mod 24, Dedekind 6 K_W == m
  mod 24, F_c Z-phase zeta^{3 sum w_G s_f}, F_S cubic A = sum w_grav s_f; rho_H from branch-free Halphen-Serre
  c(tau+1) = R_T c(tau), c(-1/tau) = tau^{3/2} exp(-3 pi i/4) R_S c(tau). For W2B (SM-R610): rho(S) = zeta_8 P,
  rho(T) = zeta_8 L^{-1}; chi_k(rho) = d + d k/12 - alpha(e^{i pi k/2} rho(S)) - alpha((e^{i pi k/3} rho(S)
  rho(T))^{-1}) - alpha(rho(T)) with exact rational turns alpha in [0, 1); B1641 L_6 = V_2 (+) V_4 from g_L =
  (I+Q_I)/sqrt(2), g_R = (I-Q_J)/sqrt(2) on parity blocks PAR = ((1,0),(0,1),(1,1)); W134 index I(r, cond, m) =
  -chi_{3/2+m/2}(rho (x) chi_eta^{r+m}) + sum_{p in cond} chi_{1+m/2}(p (x) chi_eta^{r+m}); E_8 admissibility c =
  9 + 3(r+m) == 0 mod 24; K2 n_G = w_G c mod 24 with w_G = (1/2) sum_{w in rep} <w, alpha_G>^2 from Bourbaki E_8 roots.
- imports: none
- premises on main: B1252, B1253, B1600, B1632, B1641, B1674, B1689, B1730, B1736, B1796, B1797, B1970, B1974, P-288,
  P-290, P-302, P-610, I-31, I-37
- decisive script: relays/a2_peer_sm_lie2/a2_peer_sm_lie2_decisive.py, SHA-256 8f85bb5ddc45bfa4, depends on the
  standard library, numpy, sympy and mpmath, run as python3 relays/a2_peer_sm_lie2/a2_peer_sm_lie2_decisive.py,
  output SHA-256 996add56d3a115d0
- decisive lines: 3 lines marked "DECISIVE:", SHA-256 996add56d3a115d0
- failing control: python3 relays/a2_peer_sm_lie2/a2_peer_sm_lie2_control.py
- second computation: cross-family pair — this blind fam3-v1-high-03 derivation (pre-committed at 0fd91af9b/bc34c8b64,
  unread outputs sealed at d898b7d32 before opening any sm/cards script or output) is the independent second
  computation verifying fam1-v1-unset-04 on origin/sm/cards (1c5b13d0a, wrappers at 3372dd041): SM-C11
  (r290_decisive.py SHA-256 2927daebbc9a7231, output f3837ef9cdb62e25) and SM-R610 (r610_decisive.py
  SHA-256 ccf3e326fcafba74, output f085b1ca158511bd); post-seal cross-check verdict: 2/2 SAME with 0 discrepancies
- already on main?: origin/main (fa9e30f62) has B1674/B1689/B1974 (moves' anomaly and frames without restricting
  characters to K_F across all 64 dictionaries) and B1736/B1796/B1797 (E_8 from 2I without re-deriving K2, and C8
  without W134's E_8 det-1 exclusion or 17/24 floor); neither SM-C11 nor SM-R610 had an independent cross-family
  second computation on record prior to d898b7d32
- what would make it fail: |G_T| != 96, Z != mu_4, rho_H not equivalent to rho_T, I-31 QCD exponent != 12 or K_W != 2
  mod 4 or anomalous on Z or F_S cubic A != 16, SM realizing a non-trivial uniform scalar with nu^c, any whole unit
  m = 24n admissible in E_8, any admissible three-27 datum at |m| < 17, C8 != 3n, K2 on 27 vanishing at c != 0 mod 24,
  any AST/JSON float literal, or any of 5/5 planted controls or the standalone exit-1 control failing
