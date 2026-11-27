# CLAIM CARD — Full boson plus fermion SL(2, Z) effective potential V_eff(tau) phase diagram over F and zero-sculpting non-conformal radiative EWSB and Majorana unfolding across canonical vacua (0 of 19)

- card id: new
- seat code: fam3-v1-high-03
- seat, branch, commit: fam3-v1-high-03, agy-002/verify, 932f3fddcf19bd538f901b7179131f87950ee974
- kind: theorem
- touches: P-629, P-882, mass, mixing, coupling, Higgs
- effect: conditions — P-629 and P-882 (maps the full boson plus fermion SL(2, Z) effective potential V_eff(tau) phase
  diagram over the fundamental domain F: establishes pure bosonic E(tau, 3), E(tau, 2), V_RS, and zero-parameter N=1
  SUGRA V_{FILQ, n}(tau) minima on Re(tau) = 0; proves P2-A trace-renormalized global stabilization of V_CW^(tr)(tau)
  at tau = i with local minimum at omega_+ and arc barrier; proves P2-B polynomial Casimir No-Go against fermion cusp
  runaway plus first-order orbifold flip at c_B^crit = 0.0318659172; proves P2-C globally bounded coupled potential
  V_tot(tau; c_F) = V_{FILQ, 3}(tau) + c_F V_CW^(all-288)(1; tau) undergoing a first-order transition above
  c_F^crit ~ 61.1 from x = 0, y = 1.1554 to a strict 2D minimum on Re(tau) = 1/2 at y* = 3.380451106 with
  V_xx(1/2) = +542.05 > 0 vs saddle V_xx(0) = -541.82 < 0; and establishes zero-sculpting UV-to-IR gauge-Higgs D-term
  stability, universal soft-mass radiative EWSB, curved Dirac G_{s=1/2}, and 10^8x covariant geometric Majorana
  splitting across all three canonical vacua omega_+, tau_{FILQ, 1}^*, and tau_tot^*(70))
- scope: frame: SL(2, Z) upper half-plane H with fundamental domain F, level-30 Frame C Fuchsian torus E_tau with all
  288 primitive order-30 torsion points, and coupled Type-II 2HDM plus universal soft-mass RG flow from t = 0 to
  t = -35; object: bosonic Epstein and FILQ potentials, all-288 fermion Coleman-Weinberg potentials V_CW(1) and
  V_CW^(tr), coupled potential V_tot(tau, c_F), curved spin-1/2 Dirac Kahler metric G_{s=1/2}, UV-to-IR D-term quartic
  positivity and soft-mass radiative EWSB, and covariant Majorana seesaw PMNS observables across 3 vacua x 3 branches;
  reach: class; hypotheses: arbitrary-precision mpmath and exact sympy arithmetic with zero empirical constants (0 of 19)
  and explicit literature imports for the SUGRA modular ansatz, 2-loop Type-II 2HDM beta functions, D-term quartic
  boundaries, and 1-loop universal soft-mass RGEs
- identifications: identifies the level-30 Frame C weight-0 Yukawa trace squares Tr(Y^dag Y) summed over all 288
  primitive points of E_tau[30] as 1-loop Coleman-Weinberg fermion mass-squared entries; identifies the three canonical
  modular vacua (omega_+, tau_{FILQ, 1}^*, tau_tot^*(70)) with UV boundary scales of a Type-II 2HDM with gauge-Higgs
  D-term quartics, universal soft masses m_0^2 = 1 (M_a = 0, A_f = 0), and U(3)_L-covariant Weinberg operator
  kappa_nu = Y_nu M_R^{-1} Y_nu^T (strictly data-free, 0 of 19)
- definitions: For tau = x + i y in H (y > 0, q = exp(2 pi i tau)), Dedekind eta(tau) = q^(1/24) prod_{n>=1}(1 - q^n),
  E_2(tau) = 1 - 24 sum_{n>=1} n q^n / (1 - q^n), non-holomorphic E2_hat(tau) = E_2(tau) - 3 / (pi y),
  V_RS(tau) = -ln(y |eta(tau)|^4), real-analytic Eisenstein E(tau, s) = sum'_{(m,n) != (0,0)} y^s / |m tau + n|^(2 s)
  (Chowla-Selberg expansion), and zero-parameter N=1 SUGRA modular potentials V_{FILQ, n}(tau) = (2 y)^(-3 n)
  |eta(tau)|^(-12 n) ((n pi^2 y^2 / 3) |E2_hat(tau)|^2 - 3) for n in {1, 2, 3} (from K = -3 n ln(2 y),
  W = eta(tau)^(-6 n)). On E_tau, L_2(tau) is the unique Fuchsian accessory parameter of the Lame-type equation
  u'' + (wp(z; tau) / 4 + L_2(tau)) u = 0 with unitary monodromy on the fundamental torus cycles, reduced covariantly
  via L_2(-1/tau) = tau^2 L_2(tau) + tau^2 wp-scaling and L_2(tau + 1) = L_2(tau) using the fundamental-domain cocycle.
  For every primitive order-30 torsion point w = (a, b) in E_tau[30] (exact order 30, 288 pairs), Frame C constructs
  weight-0 3x3 Yukawa matrices Y_f(w; tau) (f in {up, down, lep, nu}) and normalized scalar trace squares m_w^2(tau) =
  sum_f Tr(Y_f(w; tau)^dag Y_f(w; tau)) (all 288 pairs summed with equal weight, zero target tau* embedded):
  Tr2(tau) = sum_w m_w^2(tau), V_4(tau) = sum_w m_w^4(tau), fixed-scale fermion 1-loop Coleman-Weinberg potential
  V_CW^(all-288)(1; tau) = -sum_w m_w^4(tau) (ln(m_w^2(tau)) - 3/2), trace-scale V_CW^(tr)(tau) = -sum_w m_w^4(tau)
  (ln(m_w^2(tau) / Tr2(tau)) - 3/2), and coupled potential V_tot(tau; c_F) = V_{FILQ, 3}(tau) + c_F V_CW^(all-288)(1; tau).
  The orbifold flip coupling is c_B^crit = (V_CW(1; omega_+) - V_CW(1; i)) / (E(i, 3) - E(omega_+, 3)). The curved
  spin-1/2 Dirac Kahler metric G_{s=1/2}(tau) = diag(G_J, G_I, G_K) is normalized to mean 1 from the hyperbolic metric
  e^(2 phi) solving Liouville's equation with Gauss-Bonnet integral checked against 2 pi. At each canonical vacuum
  (V1: omega_+ = 1/2 + i sqrt(3)/2; V2: tau_{FILQ, 1}^* = i y_1^*; V3: tau_tot^*(70) = 1/2 + i y_{70}^*) and canonical
  mark w_mark = (4/15, 1/30) (with 2 w_mark mod 1), three UV branches are unfolded with zero sculpting: Static_FLAT
  (flat Kahler, static Higgs), Static_CURVED_s12 (canonical rescaling Y -> G_{s=1/2}^(-1/2) Y G_{s=1/2}^(-1/2)), and
  DynamicV4_ferro_CURVED_s12 (canonical kinetic rescaling applied first, then minimizing 2-doublet all-S
  V_4(h_u, h_d) - (1/4)|V_4(S^can)| |h_u^dag h_d|^2 on unit spheres S^5 x S^5 with Y_nu(w) and Y_nu(2 w) coupled to
  h_u^*). Overall UV Yukawa normalization sets max_f sigma_3(Y_f) = 1, UV gauge couplings g_1 = g_2 = g_3 = 1/2
  (g_Y^2 = (3/5) g_1^2), UV Branco/CE D-term quartics l1_D = l2_D = (g_2^2 + g_Y^2)/4 = 1/10, l3_D = (g_2^2 - g_Y^2)/4
  = 1/40, l4_D = -g_2^2/2 = -1/8 (saturating l3_D + l4_D + sqrt(l1_D l2_D) = 0 at t = 0), and universal UV soft masses
  m_{H_u}^2 = m_{H_d}^2 = 1, M_Q^2 = M_u^2 = M_d^2 = M_L^2 = M_e^2 = I_3, integrated downward from t = 0 to t = -35
  (RK4, n = 80 and n = 160 steps with all-step Branco/CE stability checks l1 > 0, l2 > 0, l3 + sqrt(l1 l2) > 0,
  l3 + l4 + sqrt(l1 l2) > 0). Majorana seesaw kappa_nu = Y_nu M_R^(-1) Y_nu^T is diagonalized via Autonne-Takagi
  factorization for M_R in {I_3, sym(Y_nu(w)), sym(Y_nu(2 w))} and tested under 10 random Haar U(3)^5 x U(3)_{nuR}
  basis transformations.
- imports: (1) Font-Ibanez-Lust-Quevedo (1990), Nucl. Phys. B 345, 389 and Phys. Lett. B 245, 401 (N=1 SUGRA modular
  potential V_{FILQ, n} from K = -3 n ln(2 y), W = eta^(-6 n)); (2) Branco et al. (arXiv:1106.0034) and
  Chowdhury-Eberhardt (arXiv:1503.08216, Appendix A) Type-II 2HDM 2-loop Yukawa beta functions (specifically -41/240
  g_1^2 H_d in beta_{Y_u}^(2) and -53/240 g_1^2 H_u in beta_{Y_d}^(2) in GUT normalization), 1-loop quartic beta
  functions, and tree-level gauge-Higgs D-term quartic boundary conditions and positivity bounds; (3) Martin
  (hep-ph/9709356, Eqs. 6.5.24-6.5.30) 1-loop universal soft-mass RGEs and hypercharge S-invariant; (4) Xing-Zhou
  (arXiv:1804.01925) opposite CKM running sign benchmark (2HDM-II vs 1HDM). Zero empirical constants imported (0 of 19).
- premises on main: B1957, B1980, B1992, B1993, P-629, P-882
- decisive script: relays/a2_p629_veff_modulus_p885/a2_p629_veff_modulus_decisive.py, SHA-256 6f49c92d931116a7, depends
  on the standard library, mpmath and sympy, run as python3 relays/a2_p629_veff_modulus_p885/a2_p629_veff_modulus_decisive.py,
  output SHA-256 27686c50c4734297
- decisive lines: 6 lines marked "DECISIVE:", SHA-256 df78d7d13876ce8b
- failing control: python3 relays/a2_p629_veff_modulus_p885/a2_p629_veff_modulus_control.py
- second computation: fam3-v1-high-03 disjoint cold-room referee v2
  relays/a2_p629_veff_modulus_referee_v2/referee_a2_p629_veff_modulus_v2.py (SHA-256 c7516b78764f077a, output
  b22ce2a6a0849d54, cross-diff 63fea22f37816c34) using Euler pentagonal eta and log-derivative E_2, Jacobi theta_1
  wp/4, explicit 15-stage 6th-order Yoshida-Suzuki L_2, real-split 6x6 mp.eigsy, Voronoi Clenshaw-Curtis G_{s=1/2},
  implicit GL4 RGEs, and 10-trial Cayley Haar: 841/841 matched, 0 discrepancies against the identical mathematical core
  of Producer v4 (9c4595859 -> dc9180fee; full custody chain disclosed: pre-output frozen v1, sealed v2/v3, Referee v1
  FAIL c553a9947 catching BUG-1/BUG-2/CONV-3, all three remediated in v4 and certified PASS in Referee v2 f10c79db7;
  this P-885 decisive script preserves v4's mathematical core verbatim while adding deterministic DECISIVE lines and a
  standalone exit-1 failing control)
- already on main?: topic_sweep.py "P-629|V_FILQ|boson\+fermion|radiative EWSB|Martin soft-mass|3\.38045|c_B\^crit" on
  origin/main (ae7defd04): VERDICT 1 of 1759 arcs match (B1833 PROVED) and 15 register rows match (P-629, P-882 QUEUED);
  B1957 and B1992-B1993 checked only pure bosonic Casimir potentials without fermion loops, SUGRA cusp walls, coupled
  V_eff(tau) phase transitions, non-conformal D-term plus soft-mass radiative EWSB, or geometric Majorana seesaw
- what would make it fail: any bosonic or fermion SL(2, Z) T/S invariance error above 1e-32 / 1e-25, or failure of
  V_CW^(tr)(i) < V_CW^(tr)(omega_+) < V_CW^(tr)(arc), or c_B^crit differing from 0.031865917, or failure of
  V_xx(1/2, y*) > 500 or V_xx(0, y*) < -500 at y* = 3.380451106, or any arXiv:1503.08216 3-sector or Martin 7-eq
  benchmark error above 1e-38, or any UV-to-IR D-term instability across 160 steps, or any 10-trial Haar
  U(3)^5 x U(3)_{nuR} drift above 1e-25, or any of the 6/6 planted controls or standalone exit-1 control failing
