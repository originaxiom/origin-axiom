# CLAIM CARD — All-k universal tensor-halving and frozen golden defect on O_{3^k} x Leg(5), Level-30 exact halving, Leg(5) chiral walk Pauli algebra, zero-parameter Siegel I4/I6 interior stabilization, and exact 5-division chiral-pole theorem on H (0 of 19)

- card id: new
- seat code: fam3-v1-high-03
- seat, branch, commit: fam3-v1-high-03, agy-002/verify, 8556e7942de3e07c14cc507565d6713fbae6f7fd
- kind: theorem
- touches: P-629, P-845, P-882
- effect: conditions — P-629, P-845, and P-882 (proves via the 6-point minimal quotient Q_6 of O_{3^k}^{(3,3,3)} and
  exhaustive G_3 (216) and G_4 (1944) character-defect vanishing that V_new^(k) ~= rho (x) V_new^(k), freezing the
  unpaired golden defect of O_{3^k}^{(3,3,3)} x Leg(5) identically onto Q_6 x Leg(5) as (y^2 - 6 y + 4)^2
  (y^2 + 6 y + 4)^2 with leftover neutral (y^2 - 20)^2 (y^2 - 8)^2 for all k >= 3 while proving exact 100% halving
  (0 unpaired modes) on sister O_27^{(3,3,15)} x Leg(5) and all Level-30 bundles P^1(F_2) x O_{3^k} x W; proves
  commuting chiral walks [W_L, W_R] = 0 on Leg(5) with exact Pauli identity i(W_L - W_R)|_{E_{phi^2}} = sqrt(3) phi^2
  sigma_y selecting the exact chiral poles; proves the exact anti-holomorphic mirror-lock theorem mapping |tau| = 1,
  Re(tau) = +1/2, and |tau - 1| = 1 onto the C_3-conjugacy class of tau_mir so every real weight-0 equivariant map
  locks on Re(tau) = +1/2 to the global maximum I_6 = 11/90 while vanishing at omega_+; proves ZERO-PARAMETER
  SL(2, Z)-invariant interior modulus stabilization of I4_Siegel(tau) on Re(tau) = 1/2 at y* = 2.2726755929 (x = 0
  saddle) and opposite-phase I6_Siegel(tau) on Re(tau) = 0 at y* = 2.3052230811 (x = 1/2 saddle); and proves
  symbolically from the 5-division polynomial of y^2 = 4 x^3 - 1 that the weight-2 holomorphic Weierstrass map
  Phi^{wp}(omega_+) lands at the exact chiral pole I_4 = 1/5, I_6 = 2/45 with exact 0:0:4/5:1/5 norm split and
  V_wp(omega_+) = (27/8) 5^(1/3) |g_3(omega_+)|^(2/3), and at tau = i hits exact rational I_4 = 2/9, I_6 = 17/288)
- scope: frame: exact finite group representations of SL(2, Z) on O_{3^k}, Q_6, P^1(F_2), and Leg(5), plus weight-0
  Siegel and weight-2 Weierstrass vector-valued modular maps from H into Leg(5); object: diagonal bundles
  Q_6 x Leg(5), O_27^{(3,3,3)/(3,3,12)/(3,3,15)} x Leg(5), Level-30 P^1(F_2) x O_27 x Leg(5), O_81 x Leg(5), chiral
  walk operators W_L and W_R on Leg(5), and SL(2, Z)-equivariant analytic maps Phi^{Siegel}_{Leg(5)} and
  Phi^{wp}_{Leg(5)} over the fundamental domain F; reach: class; hypotheses: exact integer, rational, and algebraic
  arithmetic over Q(omega, sqrt(5)) in modules B1, B2, and the symbolic proofs of B3-B4, paired with 45-digit mpmath
  evaluation for the analytic maps and 2D Hessians on F (strictly 0 of 19)
- identifications: none
- definitions: On Z^2, L = [[1, 1], [0, 1]], R = [[1, 0], [1, 1]], S = [[0, -1], [1, 0]], C_om = L R^(-1) =
  [[0, 1], [-1, 1]], C_3 = -C_om = [[0, -1], [1, -1]], C_0 = R^(-1) L = [[1, 1], [-1, 0]], negC_0 = -C_0 (order 3),
  and mirror tau_mir = [[0, 1], [1, 0]]. On A^3 mod 3^k, L_tr(x, y, z) = (x, z, x z - y), R_tr(x, y, z) =
  (z, y, y z - x), C_tr(x, y, z) = (y, z, x), sigma_tr(x, y, z) = (y, x, x y - z), O_{3^k}^{(a,b,c)} is the
  <L_tr, R_tr>-orbit of (a, b, c) mod 3^k, and Q_6 is the unique 6-point block quotient of O_27^{(3,3,3)} with
  |Fix(C_tr)| = 3 (G_3 / M_6, |G_3| = 216, |G_4| = 1944, rho : G_k -> mu_6 with rho(C_tr) = omega = exp(2 pi i/3),
  rho(sigma_tr) = -1). On P^1(F_5) ordered as l_1..l_6 = ((1,0),(0,1),(1,1),(1,2),(1,3),(1,4)), Leg(5) is the 6-dim
  signed-line representation M e_i = (s / 5) e_j when M l_i = s l_j mod 5 (Legendre symbol (s / 5) in {+1, -1}), and
  P^1(F_2) has the 3 lines ((1,0),(0,1),(1,1)). On any diagonal bundle B x Leg(5) (or B x P^1(F_2) x Leg(5)),
  g_{C_3} = (C_tr, negC_0), W_+ = sum_{j=0}^2 g_{C_3}^j (L_tr, L) g_{C_3}^(-j), W_- = sum_{j=0}^2 g_{C_3}^j
  (R_tr, R) g_{C_3}^(-j), W_6 = W_+ + W_-, H_q = ker(g_{C_3} - omega^q I), P_neu(y) = det(y I - W_6|_{H_0}),
  P_{2,chg}(y) = 2^(d_1) det((y/2) I - W_6|_{H_1}), and integer trace-moment halving defect is
  Delta_{2m} = tr(W_6|_{H_0}^{2m}) - 2^(2m) tr(W_6|_{H_1}^{2m}). On Leg(5) alone, W_L = sum_{j=0}^2 C_om^j L C_om^(-j),
  W_R = sum_{j=0}^2 C_om^j R C_om^(-j), W_{6,om} = W_L + W_R, phi = (1 + sqrt(5))/2, E_{phi^2} = ker(W_{6,om} - phi^2 I)
  with real orthonormal tau_mir-eigenbasis (e_+, e_-) (tau_mir e_+ = +e_+, e_{+,6} > 0, tau_mir e_- = -e_-,
  e_{-,4} = e_{-,5} > 0), and Pauli matrix sigma_y = [[0, -i], [i, 0]]. For any normalized vector psi in C^6 with
  p_i = |psi_i|^2 / sum_j |psi_j|^2, I_4(psi) = sum_{i=1}^6 p_i^2 and I_6(psi) = sum_{i=1}^6 p_i^3. For tau = x + i y
  in H and (a, b) in (1/5 Z)^2 \ {(0, 0)}, F_Siegel(a, b; tau) = -ln|g_{a,b}(tau)| where ln|g_{a,b}(tau)| =
  -pi y B_2(a mod 1) + ln|1 - q_z| + sum_{n>=1}(ln|1 - q^n q_z| + ln|1 - q^n / q_z|) (q = exp(2 pi i tau),
  q_z = exp(2 pi i (a tau + b)), B_2(u) = u^2 - u + 1/6), and F_wp(a, b; tau) = wp(a tau + b; tau) =
  -(pi^2/3) E_2(tau) - 4 pi^2 (w/(1-w)^2 + sum_{n>=1}(q^n w/(1 - q^n w)^2 + q^n w^(-1)/(1 - q^n w^(-1))^2)). The
  column-aligned SL(2, Z)-equivariant Leg(5) maps are Phi^{Siegel}_{Leg(5)}(tau) = rho(S) v^{Siegel}(tau) and
  Phi^{wp}_{Leg(5)}(tau) = rho(S) v^{wp}(tau) where v_i = (F(l_i/5; tau) - F(2 l_i/5; tau)) / sqrt(2), with
  SL(2, Z)-invariant shape ratios I4_Siegel(tau) = I_4(Phi^{Siegel}(tau)), I6_Siegel(tau) = I_6(Phi^{Siegel}(tau)),
  and modular weight-0 density V_wp(tau) = y^2 ||Phi^{wp}(tau)||^2. The equianharmonic 5-division polynomial for
  y^2 = 4 x^3 - 1 (g_2 = 0, g_3 = 1) is psi_5(x) = 5 x^12 - 95 x^9 - 15 x^6 + 25 x^3 - 1 = P(x^3).
- imports: none
- premises on main: B1992, B1993, B2014, B2016, B2017, P-629, P-845, P-882
- decisive script: relays/a2_leg5_tower_modular_bridge/a2_leg5_tower_modular_bridge_decisive.py, SHA-256
  7f51c721fde94bba, depends on the standard library, mpmath and sympy, run as
  python3 relays/a2_leg5_tower_modular_bridge/a2_leg5_tower_modular_bridge_decisive.py, output SHA-256 834cc3029354e3cc
- decisive lines: 4 lines marked "DECISIVE:", SHA-256 ff2e7d4ce87f3c5a
- failing control: python3 relays/a2_leg5_tower_modular_bridge/a2_leg5_tower_modular_bridge_control.py
- second computation: fam3-v1-high-03 disjoint cold-room referee
  relays/a2_leg5_tower_modular_bridge_referee/referee_a2_leg5_tower_modular_bridge.py (SHA-256 e5a376a70143a719, output
  ede9d390a725fdb7, cross-diff dd63d1e9499854fa, pre-committed at 765d441f9, unread output sealed at 6021cd6d2, verdict
  at 8556e7942) using 12-ray involution projection on Rays(5), <C_tr, sigma_tr> orbits, pure-integer Faddeev-LeVerrier
  recursion on H_0 and real H_1 (+) H_2, sparse C-orbit sector matrices, Jacobi theta_1 / Euler pentagonal eta Siegel
  units, Illinois root + golden-section + 5-point Richardson 2D Hessians, theta_1 logarithmic derivative wp, and
  chord-and-tangent x([2]P) = x([3]P) resultant 5-division proof: 125/125 matched, 0 discrepancies (VERDICT: PASS)
- already on main?: topic_sweep.py "Leg\(5\)|O_81 x Leg|5-division|Siegel.*Leg|I4_Siegel|Q_6 x Leg|chiral pole" on
  origin/main (ae7defd04): VERDICT 0 of 1759 arcs match and 1 register row matches (P-846 QUEUED); B2014-B2017 studied
  scalar trace orbits without Leg(5) diagonal tensor-halving, chiral walk Pauli algebra, equivariant Siegel/Weierstrass
  maps, or zero-parameter I4/I6 stabilization on F
- what would make it fail: any character-defect mismatch on G_3 (216) or G_4 (1944) or non-zero Level-30/sister-15
  defect, or any failure of [W_L, W_R] = 0 or i(W_L - W_R)|_{E_{phi^2}} = sqrt(3) phi^2 sigma_y, or any mirror-lock
  commutator failure on |tau|=1, Re(tau)=+1/2, or |tau-1|=1, or any Siegel/Weierstrass SL(2, Z) equivariance error
  above 1e-35, or failure of I4_xx(1/2) > 0 / I4_xx(0) < 0 at y* = 2.2726755929 or I6_xx(0) > 0 / I6_xx(1/2) < 0 at
  y* = 2.3052230811, or any failure of the exact 5-division polynomial 0:0:4/5:1/5 / (2/9, 17/288) identities, or any
  of 5/5 planted controls or the standalone exit-1 control failing
