# CLAIM CARD — Klein-four Hensel section, Legendre divided-power gap law, and mod-2187 plateau for B2007, diagonal Weil quantum bundles (+6 chiral index), and curved-Moser secular cancellation for P-775 (0 of 19)

- card id: new
- seat code: fam3-v1-high-01
- seat, branch, commit: fam3-v1-high-01, agy/cusp-action-2026-11-20, d35d04e4fee1cc521395f0de939a2fd87a901427
- kind: theorem
- touches: P-775, P-845, P-882
- effect: conditions — P-775, P-845, and P-882 (proves on O_{3^k} that the normal Klein-four sign gauge V_4 has order 4 coprime to 3 so
  K_k = ker(G_k -> S_4) embeds faithfully into Sym(O_{3^k} / V_4), whose global section S_k = {a_1 = 1, a_2 = 1 mod 3} is bijective
  with {1, 2} x (Z / 3^(k-2) Z)^2 via a 3-adic Hensel height Phi_eps(b_1, b_2) obeying v_3(coeff b^alpha) >= |alpha| - 1; derives the
  Legendre divided-power wake-up levels k_wake(d) = 2 d + 1 - v_3(d!) = [3, 5, 6, 8, 10, 11] with gaps at k = 4 and k = 7, and proves
  in pure stdlib without GAP or Sage that dim_{F_3}(L_k) = [2, 2, 3, 7, 7] for k = 3 to 7 (|G_7| = 24 * 3^21 = 251048476872) with
  bijective Lazard cubing maps L_4 = (L_3)^3 and L_7 = (L_6)^3; proves over exact cyclotomic rings on O_{3^k} (x) Weil(N, 1) that both
  monoid and Hermitian chiral walks commute ([W_+, W_-] = 0) and satisfy d_1^tot - d_2^tot = (d_0^base - d_1^base)(d_1^fiber -
  d_2^fiber), locking universal chiral index +6 = 3 * 2 across all O_{3^k} (x) Weil(3^m, 1) vs 0 on O_27 (x) Weil(5, 1) with exact
  sector trace moments; and proves symbolically in SymPy for P-775 that curved holomorphic Moser normal form Phi_{1,1} = (I_2 - J)^(-1)
  D^2 F(p_*)[e_+, e_-] cancels Silver's non-zero naive linear mixed derivative LN2*(276 - 52*I) identically to 0, eliminating the
  first-order secular drift D_1 k lambda_+^(-k) while leaving a non-zero second-order Birkhoff twist D_2 k lambda_+^(-2k) across
  Golden, Silver, and Bronze)
- scope: frame: no frame (3-adic Markoff congruence groups G_k on O_{3^k}, diagonal non-commutative Weil quantum bundles l^2(O_{3^k})
  (x) C^N, and symplectic parabolic punctured-torus surface S_{kappa=-2}); object: polycyclic F_3-layers L_3 to L_7 through mod 2187 =
  3^7, diagonal chiral walks on O_{3^k} (x) Weil(3^m, 1) (k in {3, 4, 5}, m in {1, 2, 3}) and O_27 (x) Weil(5, 1), and second-order
  Moser saddle jets and neck volume asymptotics on RL, RRLL, and RRRLLL; reach: class; hypotheses: exact integer, polynomial over ZZ,
  and cyclotomic DomainMatrix arithmetic over QQ(zeta_{lcm(N,3)}) for E1, E2, and Golden/Silver Moser secular cancellation, paired with
  52-digit mpmath evaluation for Bronze Moser cancellation and 5-term neck fits (strictly 0 of 19)
- identifications: none
- definitions: In scaled Markoff coordinates a_i = x_i / 3 mod 3^(k-1) on a_1^2 + a_2^2 + a_3^2 = 3 a_1 a_2 a_3 mod 3^(k-1) (k >= 2),
  O_{3^k} is the orbit of (1, 1, 1) under L_s(a_1, a_2, a_3) = (a_1, a_3, 3 a_1 a_3 - a_2) and R_s(a_1, a_2, a_3) = (a_3, a_2, 3 a_2
  a_3 - a_1), G_k = <L_s, R_s> <= Sym(O_{3^k}) (G_2 ~= S_4 of order 24 on O_9), K_k = ker(G_k -> G_2), and L_k = ker(G_k -> G_{k-1}) ~=
  F_3^(d_k) for k >= 3. With V_4 = {(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)}, S_k = {(a_1, a_2, a_3) in O_{3^k} : a_1 = 1 mod 3, a_2 =
  1 mod 3} ~= {1, 2} x (Z / 3^(k-2) Z)^2 via a = (1 + 3 b_1, 1 + 3 b_2, eps + 3 Phi_eps(b_1, b_2)). Here wake = [2 d + 1 - v_3(d!) for
  d = 1, 2, 3, 4, 5, 6], gaps = [k in {3, 4, 5, 6, 7, 8, 9} : k not in wake], dims_k3_k7 = [d_3, d_4, d_5, d_6, d_7], log3K =
  [log_3|K_3|, ..., log_3|K_7|], G7 = |G_7| = 24 * 3^(log_3|K_7|), and cubing_ranks = (rk_34, rk_67) where rk_{j,j+1} is the F_3-rank
  in L_{j+1} of {g^3 : g in L_j}. On unscaled O_{3^k} (orbit of (3, 3, 3) mod 3^k under L_tr(x, y, z) = (x, z, x z - y) and R_tr(x, y,
  z) = (z, y, y z - x)), C_tr(x, y, z) = (y, z, x) = R_tr^(-1) o L_tr. For odd N >= 3, inv2 = (N + 1)/2, zeta_N = exp(2 pi i / N), and
  r in Z / N Z, Weil(N, r) on C^N has L_w = diag_{0 <= j < N}(zeta_N^(r * inv2 * j^2)), (S_inv)_{a,c} = G_{N,r}^(-1) zeta_N^(r a c)
  with G_{N,r} = sum_{b=0}^{N-1} zeta_N^(-r * inv2 * b^2) (or L_w = R_w = g_{3,w} = I_N when r = 0 mod N), R_w = S_inv L_w^dagger
  S_inv^dagger, and g_{3,w} = S_inv^2 R_w^dagger L_w (g_{3,w}^3 = I_N). On l^2(O_{3^k}) (x) C^N at r = 1, G = C_tr (x) g_{3,w}, L_tot =
  L_tr (x) L_w, R_tot = R_tr (x) R_w, W_+(L) = sum_{j=0}^2 G^j L_tot G^(-j), W_-(R) = sum_{j=0}^2 G^j R_tot G^(-j), W_-(L^(-1)) =
  sum_{j=0}^2 G^j L_tot^dagger G^(-j), W_{6,H} = W_+(L) + W_-(L^(-1)), and H_q = ker(G - omega^q I) for omega = exp(2 pi i / 3) and q
  in {0, 1, 2}. Here grid_3k_3m_idx6 asserts across all (k, m) in {3, 4, 5} x {1, 2, 3} that C_tr = R_tr^(-1) o L_tr, |Fix(C_tr)| = 3,
  |O_{3^k}| = 8 * 3^(2k - 4), and (dim H_0, dim H_1, dim H_2) = (8 * 3^(2k+m-5), 8 * 3^(2k+m-5) + 3, 8 * 3^(2k+m-5) - 3) (index +6) on
  O_{3^k} (x) Weil(3^m, 1); for N in {3, 5}, O27xWN_dims = [dim H_0, dim H_1, dim H_2] on O_27 (x) Weil(N, 1) (with exact cyclotomic
  verification of [W_+(L), W_-(R)] = 0, [W_+(L), W_-(L^(-1))] = 0, and [W_{6,H}, G] = 0), and O27xWN_m1_m4 = (M_0, M_1, M_2) with M_q =
  [tr(W_{6,H}|_{H_q}^n) for n = 1, 2, 3, 4]. On S_{kappa=-2} in (u, v) = (x / z, y / z), step maps are F_L(u, v) = (u / (v^2 + 1), u v
  / (v^2 + 1)) with shape w_L(v) = v^2 / (v^2 + 1) and F_R(u, v) = (u v / (u^2 + 1), v / (u^2 + 1)) with shape w_R(u) = 1 / (u^2 + 1).
  For saddle sequence S_word = s_0 ... s_{m-1} in {RL, RRLL, RRRLLL} applied sequentially (z_{r+1} = F_{s_r}(z_r), w_r = w_{s_r}(z_r)
  for 0 <= r < m, so F = F_{s_{m-1}} o ... o F_{s_0}) at its positively oriented fixed point p_* (Im w_r > 0: p_* = ((1 - i sqrt(3))/2,
  1) for RL; p_* = (x_2/z_2, y_2/z_2) with z_2 = sqrt(2)(1 + i), y_2 = sqrt(2 + 2 i), x_2 = -y_2 z_2^3 / 8 for RRLL; and the Im w_r >
  0 cycle from z^8 - z^7 + 6 z^6 - 5 z^5 + 21 z^4 + 15 z^3 + 7 z^2 - 3 z + 3 = 0 of T_1^3 T_2^3(x, y, z) = (x, y, z) on x^2 + y^2 + z^2
  = x y z with T_1(x, y, z) = (z, y, y z - x), T_2(x, y, z) = (x, z, x z - y) for RRRLLL), V_per(u, v) = sum_{r=0}^{m-1} D_{BW}(w_r(u,
  v)) with D_{BW}(w) = Im Li_2(w) + arg(1 - w) ln|w|, J = dF/d(u, v)|_{p_*}, lambda_+ = (tr J + sqrt((tr J)^2 - 4))/2, lambda_- =
  (tr J - sqrt((tr J)^2 - 4))/2, unnormalized eigenvectors e_+ = (J_{0,1}, lambda_+ - J_{0,0})^T and e_- = (J_{0,1}, lambda_- -
  J_{0,0})^T, Phi_lin(xi, eta) = p_* + xi e_+ + eta e_-, and curved Moser map Phi(xi, eta) = p_* + xi e_+ + eta e_- + Phi_{1,1} xi eta
  with Phi_{1,1} = (I_2 - J)^(-1) D^2 F(p_*)[e_+, e_-]. With LN2 = ln 2, gold_sym_zero asserts tr J = 5 and exact symbolic d^2(V_per o Phi)/(d xi d conj(eta))|_{(0,0)} = d^2(V_per o
  Phi)/(d xi d eta)|_{(0,0)} = 0 on RL; sil_lin records exact symbolic d^2(V_per o Phi_lin)/(d xi d eta)|_{(0,0)} on RRLL in basis
  (e_+, e_-); sil_moser_zero asserts tr J = 18 and exact symbolic vanishing of both mixed derivatives for Phi on RRLL; brz_moser_ok
  asserts in unit-norm (e_+/||e_+||, e_-/||e_-||) on RRRLLL that max_{a,b in {1, i}} |d^2 V_per/(d(a xi) d(b eta))| is > 1 for Phi_lin
  and < 10^(-13) for Phi; and D1_zero_D2_nonzero asserts for right-to-left closed words W_k = H P^k (LLR (LR)^k for k = 6 to 14 with
  lambda_+ = (5 + sqrt(21))/2; LLLR (LLRR)^k for k = 2 to 11 with lambda_+ = 9 + 4 sqrt(5); LLLLRR (LLLRRR)^k for k = 2 to 9 with
  lambda_+ = (u_max + sqrt(u_max^2 - 4))/2, u_max in (54, 55) solving u^4 - 114 u^3 + 4264 u^2 - 58910 u + 192359 = 0) that fitting
  Delta V_k = V(W_k) - k V(P) = C_0 + C_1 lambda_+^(-k) + D_1 k lambda_+^(-k) + C_2 lambda_+^(-2k) + D_2 k lambda_+^(-2k) on the
  penultimate 5 values of k gives |D_1| < 10^(-15), |D_2| > 10^(-5), and final-k residual < 10^(-22) across all 3 families (ast_floats,
  json_floats, planted_faults_caught, payload_sha16 report script float/control counts and output SHA-256 prefix).
- imports: none
- premises on main: B1876, B1993, B2004, B2006, B2007, B2008, B2009, B2010, P-775, P-845, P-882
- decisive script: relays/agy_2026-11-28_c69/c69_3adic_legendre_gap_weil_bundles_and_curved_moser_producer.py,
  SHA-256 85fd93d2f682efda, depends on the standard library, sympy and mpmath, run as
  python3 relays/agy_2026-11-28_c69/c69_3adic_legendre_gap_weil_bundles_and_curved_moser_producer.py,
  output SHA-256 f192537a904e62ce
- decisive lines: 4 lines marked "DECISIVE:", SHA-256 ffe3443b46718446
- failing control: python3 relays/agy_2026-11-28_c69/c69_control.py
- second computation: fam3-v1-high-01 disjoint cold-room countercheck relays/agy_2026-11-28_c69/c69_countercheck.py
  (SHA-256 c3e6212390541518, output SHA-256 1dddbdfcdfcb62cf, zero shared imports, disjoint V_4 section a_2 = 1, a_3 = 1 mod 3 solving
  b_1 = Psi_delta(b_2, b_3) with base-3 digit-sum Legendre valuations through mod 2187, explicit C_tr-orbit compressed H_q subspace
  DomainMatrix operators over QQ(zeta_{lcm(N,3)}), and reciprocal cluster chart (alpha, beta) = (z / x, z / y) exact symbolic Moser
  secular cancellation on Golden and Silver, agrees with 0 discrepancies and 5/5 referee planted faults caught)
- already on main?: topic_sweep.py "B2007|L_7|2187|Moser|Weil.*O_27|Legendre.*gap" on origin/main (54929ecf5): B2007 stopped at k = 6
  (mod 729) via GAP/Sage leaving k = 7 (mod 2187) and the layer-dimension law open (#1); B2006 and B2009 tested permutation fibers
  where q = 1 and q = 2 pair with index 0 rather than non-commutative Weil bundles with universal index +6; B1876 and P-775 observed
  step-ratio settling without proving curved-Moser cancellation of D_1 k lambda_+^(-k) or isolating the second-order twist D_2
- what would make it fail: wake differing from [3, 5, 6, 8, 10, 11] or dims_k3_k7 differing from [2, 2, 3, 7, 7] or cubing_ranks
  differing from (2, 7), or grid_3k_3m_idx6=False or O27xW3_dims differing from [72, 75, 69] or O27xW5_dims differing from [118, 121,
  121], or gold_sym_zero=False or sil_lin differing from LN2*(276 - 52*I) or sil_moser_zero=False or brz_moser_ok=False or
  D1_zero_D2_nonzero=False, or any of the 5/5 planted faults or standalone exit-1 control failing
