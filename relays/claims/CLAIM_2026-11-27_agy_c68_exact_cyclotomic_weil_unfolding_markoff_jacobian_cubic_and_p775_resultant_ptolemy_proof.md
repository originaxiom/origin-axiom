# CLAIM CARD — Exact cyclotomic non-commutative two-counts Weil unfolding (mod-4 mirror dichotomy and all-3^k chiral index +2), universal Markoff tree Jacobian cubic, and resultant/Ptolemy proof of P-775 across metallic grounds (0 of 19)

- card id: new
- seat code: fam3-v1-high-01
- seat, branch, commit: fam3-v1-high-01, agy/cusp-action-2026-11-20, c636884fabf0b4d1c8dc3902ff4c4e4eb9cb4dbb
- kind: theorem
- touches: S02, P-374, P-630, P-775, P-882
- effect: conditions — S02, P-374, P-630, P-775, and P-882 (proves on the non-commutative two-counts Weil register C^N for odd
  N >= 3 that [W_hat_+, W_hat_-] = 0 and [W_hat_6, rho_{N,r}(C_{3,omega})] = 0, with q = 1 and q = 2 pairing iso-spectrally on
  W_hat_6 across odd primes p in {3..23} iff p == 1 mod 4 (p in {5, 13, 17}) while splitting 2 -> 1 + 1 natively under fixed
  symplectic orientation r = 1 (S02) for all p == 3 mod 4 (p in {3, 7, 11, 19, 23}) and preserving constant chiral index
  d_1 - d_2 = +2 across all N = 3^k; proves all 18 closed-form W_hat_6 sector polynomials P_q(x) at N in {3, 5, 7, 9, 15, 27}
  with zero error in QQ(zeta_{lcm(N,3)}); proves the universal Markoff Jacobian cubic (t - 2)(t - 2 - (x + y + z))^2 - 4 x y z
  and AM-GM uniqueness of (3, 3, 3) on the tree with outward fixed-x ray limit lambda_3 -> (6 x + 4)/(x + 2); and blows up
  (0, 0, 0) on S_{kappa=-2} via (u, v) = (x / z, y / z) preserving Omega = -du ^ dv / (u v) to prove Silver V_2 = 4 * Catalan
  via exact anharmonic shapes [1 + i, (1 + i)/2, i, (1 + i)/2], Bronze trace quartic u^4 - 114 u^3 + 4264 u^2 - 58910 u +
  192359 = 0 via exact Z-resultant, and P-775 step-ratio settling across Golden, Silver, and Bronze with zero SnapPy)
- scope: frame: no frame (foundational non-commutative two-counts Weil register on C^N, 6-move trace walk W_{6,tr} on the
  positive Markoff tree, and parabolic punctured-torus character surface S_{kappa=-2} across metallic grounds L^m R^m); object:
  finite Weil representations rho_{N,r} for odd primes p in {3, 5, 7, 11, 13, 17, 19, 23}, 3^k for k >= 1 (explicitly k <= 5),
  and N in {3, 5, 7, 9, 15, 27}, the 3 x 3 Jacobian J_{W_6}(x, y, z) on all positive Markoff triples (explicitly all 65 sorted
  triples to depth 7), and excess Bloch-Wigner volume step ratios for departures on L^m R^m (m in {1, 2, 3}); reach: class;
  hypotheses: exact integer, rational, cyclotomic number-field QQ(zeta_{lcm(N,3)}), polynomial resultant over ZZ, and 45-digit
  residual-certified arithmetic scoped to the stated sets where not all-N or all-tree
- identifications: none
- definitions: For odd integer N >= 3, inv2 = (N + 1) / 2, zeta_N = exp(2 pi i / N), and Heisenberg multiplier r in (Z/NZ)^x,
  define shift (X_+ psi)_j = psi_{(j + 1) mod N} and clock (Z_r psi)_j = zeta_N^{r j} psi_j on C^N (so X_+ Z_r = zeta_N^r Z_r
  X_+). Define Gauss sum G_{N,r} = sum_{b=0}^{N-1} zeta_N^{-r * inv2 * b^2}, clock shear rho_{N,r}(L) = diag_{0 <= j < N}(
  zeta_N^{r * inv2 * j^2}), symplectic transform (rho_{N,r}(S_{inv}))_{a,c} = G_{N,r}^{-1} zeta_N^{r a c} representing S^-1 =
  [[0, 1], [-1, 0]] in SL(2, Z), rho_{N,r}(R) = rho_{N,r}(S_{inv}) rho_{N,r}(L)^dagger rho_{N,r}(S_{inv})^dagger representing
  R = [[1, 0], [1, 1]], rho_{N,r}(C_omega) = rho_{N,r}(L) rho_{N,r}(R)^dagger, and order-3 charge operator rho_{N,r}(C_{3,omega})
  = rho_{N,r}(S_{inv})^2 rho_{N,r}(C_omega) = rho_{N,r}(S_{inv})^dagger rho_{N,r}(L)^dagger. Define stereo walks W_hat_+ =
  sum_{j=0}^2 C_omega^j L C_omega^{-j} (in rho_{N,r}), W_hat_- = sum_{j=0}^2 C_omega^j R C_omega^{-j} = W_hat_+^dagger, W_hat_6 =
  W_hat_+ + W_hat_-, and W_hat_{ch} = -i (W_hat_+ - W_hat_-). At r = 1, hom_comm_ok asserts exact algebraic equality over
  QQ(zeta_{lcm(N,3)}) for all N in {3, 5, 7, 9, 15, 27} of X_+ Z_1 = zeta_N Z_1 X_+, S_{inv} S_{inv}^dagger = I_N, L S_{inv} L =
  S_{inv} L^dagger S_{inv}, C_{3,omega}^3 = I_N, [W_hat_+, W_hat_-] = 0, and [W_hat_6, C_{3,omega}] = 0, together with
  infinity-norm residuals <= 10^-30 across all 8 odd primes p in {3, 5, 7, 11, 13, 17, 19, 23}. For omega = exp(2 pi i / 3) and
  q in {0, 1, 2}, H_q = ker(rho_{N,1}(C_{3,omega}) - omega^q I_N) has dimension d_q = dim H_q and monic characteristic polynomial
  P_{N,q}(x) = det(x I_{d_q} - W_hat_6|_{H_q}). Across p in {3..23} at r = 1, paired_mod4_eq1 lists primes with d_1 = d_2 and
  P_{p,1} = P_{p,2} (within 10^-30), chiral_split_mod4_eq3 is its complement in {3..23}, and all_3k_index_plus2 asserts
  tr rho_{3^k,1}(C_{3,omega}) = +i sqrt(3) (exact in QQ(zeta_{3^k}) for k in {1, 2, 3} and within 10^-30 for k in {1..5}) and
  (d_0, d_1, d_2) = (3^{k-1}, 3^{k-1} + 1, 3^{k-1} - 1) (d_1 - d_2 = +2, with dims_3_9_27 = [[1, 2, 0], [3, 4, 2], [9, 10, 8]]
  recording [d_0, d_1, d_2] at k = 1, 2, 3). Here exact_spectra_ok asserts exact zero-error equality det(x I_N - P_q W_hat_6) =
  x^{N - d_q} P_{N,q}(x) in QQ(zeta_{lcm(N,3)})[x] against all 18 closed-form polynomials: at N = 3, P_{3,0} = x, P_{3,1} =
  x^2 - 9, P_{3,2} = 1; at N = 5, P_{5,0} = x + 2 sqrt(5), P_{5,1} = P_{5,2} = (x - (3 - sqrt(5))/2)(x + (3 + 3 sqrt(5))/2);
  at N = 7, P_{7,0} = x^2 (x + 4), P_{7,1} = x^2 - 2 x + (-9 + sqrt(21))/2, P_{7,2} = x^2 - 2 x + (-9 - sqrt(21))/2; at N = 9,
  P_{9,0} = x (x - 4)(x - 6), P_{9,1} = (x^2 - x - 3)(x^2 - 3 x - 9) (reported factored as weil9_q1), P_{9,2} = (x - 1)(x - 3);
  at N = 15 (with [d_0, d_1, d_2] reported as weil15_dims), P_{15,0} = x^3 (x - sqrt(5) + 1)(x + sqrt(5) + 3), P_{15,1} =
  (x - (3 + sqrt(5))/2)(x - (3 - 3 sqrt(5))/2)(x^2 - (21 - 3 sqrt(5))/2)(x^2 + (1 - sqrt(5)) x - (3 + 3 sqrt(5))/2), P_{15,2} =
  (x + sqrt(5))(x - (1 - sqrt(5))/2)(x^2 - ((3 + 3 sqrt(5))/2) x - (3 - 3 sqrt(5))/2); and at N = 27, P_{27,0} = x^5 (x^4 -
  24 x^2 - 16 x + 48), P_{27,1} = x^2 (x^8 - 30 x^6 - 10 x^5 + 300 x^4 + 126 x^3 - 1179 x^2 - 324 x + 1620), P_{27,2} = x^8 -
  27 x^6 + 14 x^5 + 174 x^4 - 180 x^3 - 171 x^2 + 270 x - 81. On C^3, L_{tr}(x, y, z) = (x, z, x z - y), R_{tr}(x, y, z) =
  (z, y, y z - x), C_{tr}(x, y, z) = (y, z, x), W_{6,tr} = sum_{j=0}^2 C_{tr}^j (L_{tr} + R_{tr}) C_{tr}^{-j}, and J_{W_6}(x, y,
  z) = d W_{6,tr} / d(x, y, z). With D = diag(sqrt(x), sqrt(y), sqrt(z)), cubic_sos_amgm_ok asserts D^{-1}(J_{W_6} - 2 I_3) D
  equals the 3-square SOS form (sqrt(y) v_1 + sqrt(x) v_2)^2 + (sqrt(z) v_1 + sqrt(x) v_3)^2 + (sqrt(z) v_2 + sqrt(y) v_3)^2,
  det(t I_3 - J_{W_6}) = (t - 2)(t - 2 - (x + y + z))^2 - 4 x y z identically, and its peak at t = 2 + (x + y + z)/3 equals
  (4 / 27)((x + y + z)^3 - 27 x y z); across all sorted positive Markoff triples 3 <= a <= b <= c satisfying a^2 + b^2 + c^2 =
  a b c to Vieta-flip BFS depth 7 from (3, 3, 3) (count triples_checked = 65), degenerate_on_tree lists triples with fewer than
  3 distinct eigenvalues, and cp_336 and cp_3615 give factored det(t I_3 - J_{W_6}) at (3, 3, 6) and (3, 6, 15). On S_{kappa=-2}
  = {(x, y, z) : x^2 + y^2 + z^2 = x y z}, T_1(x, y, z) = (z, y, y z - x) and T_2(x, y, z) = (x, z, x z - y) correspond in
  rational coordinates (u, v) = (x / z, y / z) (inverse z = (u^2 + v^2 + 1)/(u v), x = u z, y = v z) to F_L(u, v) = (u / (v^2 +
  1), u v / (v^2 + 1)) with shape w_L(v) = v^2 / (v^2 + 1) and F_R(u, v) = (u v / (u^2 + 1), v / (u^2 + 1)) with shape w_R(u) =
  1 / (u^2 + 1); blowup_ok asserts exact conjugacy, invariance of Goldman-Poincare Omega = dx ^ dy / (2 z - x y) = -du ^ dv /
  (u v), and metallic amphichirality S^{-1}(L^m R^m) S = (L^m R^m)^{-1} for 1 <= m <= 5. A word W = c_1 ... c_n in {L, R}^n acts
  right-to-left as F_W = F_{c_1} o ... o F_{c_n}, so a closed orbit of W is z_0, ..., z_{n-1} in (C^*)^2 with (z_{j+1}, w_j) =
  (F_{c_{n-j}}(z_j), w_{c_{n-j}}(z_j)) for 0 <= j < n and z_n = z_0; its volume is V(W) = sum_{j=0}^{n-1} D_{BW}(w_j) where
  D_{BW}(w) = Im Li_2(w) + arg(1 - w) log|w| and Catalan = D_{BW}(i) = sum_{m >= 0} (-1)^m / (2 m + 1)^2. For ground P in {LR,
  LLRR, LLLRRR}, the geometric cycle is the closed orbit of P with Im w_j > 0 for all 0 <= j < |P|; sil_4catalan asserts both
  exact symbolic equality (w_0, w_1, w_2, w_3) = (1 + i, (1 + i)/2, i, (1 + i)/2) = (1 - 1/i, 1/(1 - i), i, 1/(1 - i)) along
  LLRR (where D_{BW}(1 - 1/i) = D_{BW}(1/(1 - i)) = D_{BW}(i) = Catalan) and |V(LLRR) - 4 * Catalan| < 10^-36. Here
  bronze_tr_minpoly gives the monic Z[u] coefficients of the square-free factor of Res_z(fac_8(z), u - tr_z(z)), where fac_8(z)
  = z^8 - z^7 + 6 z^6 - 5 z^5 + 21 z^4 + 15 z^3 + 7 z^2 - 3 z + 3 is the degree-8 lex Groebner factor of T_1^3 T_2^3(x, y, z) =
  (x, y, z) on S_{kappa=-2} and tr_z(z) is tr(d(T_1^3 o T_2^3)/d(x, y, z)) - 1 reduced modulo that lex Groebner basis, and
  u_{max} is the unique real root in (54, 55) of u^4 - 114 u^3 + 4264 u^2 - 58910 u + 192359 = 0. For W_k = H P^k (with integer
  offset b_0 = 1 for H = LLLLLLR, b_0 = 2 for H in {LLRRLLR, LLLRRRRLLLR}, b_0 = 0 for H in {LLLR, LLLLRR}) on the geometric
  neck-spliced closed orbit (Im w_j > 0 on the first (k - 1)|P| neck steps, V(W_k) > (k + b_0) V(P) - 1/2, |V(W_k) - (k + b_0)
  V(P)| > 10^-6, residual <= 10^-32), excess volume is Delta V_k = V(H P^k) - (k + b_0) V(P) (step difference Delta V_k -
  Delta V_{k-1} = V(H P^k) - V(H P^{k-1}) - V(P) independent of b_0), and gold_sil_brz_settled asserts |(Delta V_{k-1} -
  Delta V_{k-2})/(Delta V_k - Delta V_{k-1}) - lambda_+| < 10^-7 at k = 12 with lambda_+ = (5 + sqrt(21))/2 for LLLLLLR,
  LLRRLLR, LLLRRRRLLLR on LR, at k = 9 with lambda_+ = 9 + 4 sqrt(5) for LLLR on LLRR, and at k = 8 with lambda_+ = (u_{max} +
  sqrt(u_{max}^2 - 4))/2 for LLLLRR on LLLRRR (controls, ast_floats, json_floats report planted-fault and float counts).
- imports: none
- premises on main: B98, B371, B377, B381, B1876, B1881, B1983, B1985, B1993, B1994, B2000, B2001, B2004, B2008, P-374, P-630,
  P-775, P-882
- decisive script: relays/agy_2026-11-27_c68/c68_exact_cyclotomic_weil_markoff_jacobian_and_p775_producer.py,
  SHA-256 a8a9d41d32c57f00, depends on the standard library, sympy and mpmath, run as
  python3 relays/agy_2026-11-27_c68/c68_exact_cyclotomic_weil_markoff_jacobian_and_p775_producer.py,
  output SHA-256 81589cc623545210
- decisive lines: 4 lines marked "DECISIVE:", SHA-256 41679863f6056a8d
- failing control: python3 relays/agy_2026-11-27_c68/c68_control.py
- second computation: fam3-v1-high-01 disjoint cold-room countercheck relays/agy_2026-11-27_c68/c68_countercheck.py
  (SHA-256 f66cba8b4f9e030f, output SHA-256 ad08a7b7cb946bac, zero shared imports, Fourier-dual momentum-basis exact cyclotomic
  DomainMatrix over QQ(zeta_{lcm(N,3)}) for N in {3, 5, 7, 9, 15} and 48-digit mpmath eigh for N = 27 and p in {3..23},
  dual-number dW_{6,tr} Jacobian and Sturm root count, and reciprocal cluster X-chart (alpha, beta) = (z / x, z / y) exact
  Silver anharmonic shapes, symmetric half-step T_1^-3 = T_2^3 Groebner resultant over ZZ[u], and 48-digit shooting, agrees with
  0 discrepancies)
- already on main?: topic_sweep.py "P-775|B1876|B2000|B2008|Weil" on origin/main (ae7defd04): closest arcs B371, B377, B381
  (finite Weil representations at primes 3 and 5 before the 6-move walk), B1876 (proves (t - 1)(t^2 - 5 t + 1) on m004 and
  observes Golden step-ratio settling to 4 digits via SnapPy, leaving higher precision and non-Golden grounds open in P-775),
  B2000 (evaluates (14, 5, 5) only at root (3, 3, 3), leaving outward tree behavior open), and B2008 (shows classical commuting
  unfolding stays mirror-symmetric, leaving non-commutative Weil unfolding and mod-4 chiral split unrun)
- what would make it fail: hom_comm_ok=False, or paired_mod4_eq1 differing from [5, 13, 17] or chiral_split_mod4_eq3 differing
  from [3, 7, 11, 19, 23], or all_3k_index_plus2=False, or exact_spectra_ok=False, or degenerate_on_tree differing from
  [[3, 3, 3]], or gold_sil_brz_settled=False, or sil_4catalan=False, or bronze_tr_minpoly differing from
  [1, -114, 4264, -58910, 192359]
