# CLAIM CARD — Non-commutative two-counts Weil unfolding (mod-4 mirror dichotomy and all-3^k chiral index +2), universal outward Markoff tree Jacobian cubic, and rational Ptolemy proof of P-775 across metallic grounds (0 of 19)

- card id: new
- seat code: fam3-v1-high-01
- seat, branch, commit: fam3-v1-high-01, agy/cusp-action-2026-11-20, 806eeaedd515e14196ba0a619f06454e0e26c978
- kind: theorem
- touches: S02, P-374, P-630, P-775, P-882
- effect: conditions — S02, P-374, P-630, P-775, and P-882 (proves on the non-commutative two-counts Weil register C^N for odd
  N >= 3 that [W_hat_+, W_hat_-] = 0 and [W_hat_6, rho_{N,r}(C_{3,omega})] = 0, with q = 1 and q = 2 pairing iso-spectrally on
  W_hat_6 across odd primes p in {3..23} iff p == 1 mod 4 (p in {5, 13, 17}) while splitting 2 -> 1 + 1 natively under fixed
  symplectic orientation r = 1 (S02) for all p == 3 mod 4 (p in {3, 7, 11, 19, 23}) and preserving constant chiral index
  d_1 - d_2 = +2 across all N = 3^k; determines exact algebraic W_hat_6 polynomials at N in {3, 5, 7, 9, 15, 27}; proves the
  universal Markoff Jacobian cubic (t - 2)(t - 2 - (x + y + z))^2 - 4 x y z and AM-GM uniqueness of (3, 3, 3) on the tree with
  outward fixed-x ray limit lambda_3 -> (6 x + 4)/(x + 2); and blows up (0, 0, 0) on S_{kappa=-2} via (u, v) = (x / z, y / z)
  preserving Omega = -du ^ dv / (u v) to certify P-775 across Golden, Silver V_2 = 4 * Catalan at rate 9 + 4 sqrt(5) = phi^6,
  and Bronze irreducible quartic u^4 - 114 u^3 + 4264 u^2 - 58910 u + 192359 = 0 with zero SnapPy)
- scope: frame: no frame (foundational non-commutative two-counts Weil register on C^N, 6-move trace walk W_{6,tr} on the
  positive Markoff tree, and parabolic punctured-torus character surface S_{kappa=-2} across metallic grounds L^m R^m); object:
  finite Weil representations rho_{N,r} for odd primes p in {3, 5, 7, 11, 13, 17, 19, 23}, 3^k for k >= 1 (explicitly k <= 5),
  and N in {3, 5, 7, 9, 15, 27}, the 3 x 3 Jacobian J_{W_6}(x, y, z) on all positive Markoff triples (explicitly all 65 sorted
  triples to depth 7), and excess Bloch-Wigner volume step ratios for departures on L^m R^m (m in {1, 2, 3}); reach: class;
  hypotheses: exact integer, rational, symbolic algebraic, and 45-digit residual-certified arithmetic scoped to the stated sets
  where not all-N or all-tree
- identifications: none
- definitions: For odd integer N >= 3, inv2 = (N + 1) / 2, zeta_N = exp(2 pi i / N), and Heisenberg multiplier r in (Z/NZ)^x
  (with X Z = zeta_N^r Z X on C^N), define Gauss sum G_{N,r} = sum_{b=0}^{N-1} zeta_N^{-r * inv2 * b^2}, clock shear
  rho_{N,r}(L) = diag_{0 <= j < N}(zeta_N^{r * inv2 * j^2}), symplectic transform (rho_{N,r}(S_{inv}))_{a,c} = G_{N,r}^{-1}
  zeta_N^{r a c} representing S^-1 = [[0, 1], [-1, 0]] in SL(2, Z), rho_{N,r}(R) = rho_{N,r}(S_{inv}) rho_{N,r}(L)^dagger
  rho_{N,r}(S_{inv})^dagger representing R = [[1, 0], [1, 1]], rho_{N,r}(C_omega) = rho_{N,r}(L) rho_{N,r}(R)^dagger, and
  order-3 charge operator rho_{N,r}(C_{3,omega}) = rho_{N,r}(S_{inv})^2 rho_{N,r}(C_omega) = rho_{N,r}(S_{inv})^dagger
  rho_{N,r}(L)^dagger. Define stereo walks W_hat_+ = sum_{j=0}^2 C_omega^j L C_omega^{-j} (evaluated in rho_{N,r}), W_hat_- =
  sum_{j=0}^2 C_omega^j R C_omega^{-j} = W_hat_+^dagger, W_hat_6 = W_hat_+ + W_hat_-, and W_hat_{ch} = -i (W_hat_+ - W_hat_-)
  (hom_comm_ok asserts ||L S_{inv} L - S_{inv} L^dagger S_{inv}||_inf <= 10^-30, ||C_{3,omega}^3 - I_N||_inf <= 10^-30,
  ||[W_hat_+, W_hat_-]||_inf <= 10^-30, and ||[W_hat_6, C_{3,omega}]||_inf <= 10^-30 across all 8 odd primes p in {3, 5, 7, 11,
  13, 17, 19, 23}). For omega = exp(2 pi i / 3) and q in {0, 1, 2}, H_q = ker(rho_{N,r}(C_{3,omega}) - omega^q I_N) has
  dimension d_q = dim H_q and monic characteristic polynomial P_q(x) = det(x I_{d_q} - W_hat_6|_{H_q}). At fixed orientation
  r = 1, paired_mod4_eq1 is the list of p in {3..23} with d_1 = d_2 and P_1 = P_2, chiral_split_mod4_eq3 is its complement in
  {3..23}, all_3k_index_plus2 asserts tr rho_{3^k,1}(C_{3,omega}) = +i sqrt(3) and (d_0, d_1, d_2) = (3^{k-1}, 3^{k-1} + 1,
  3^{k-1} - 1) (so d_1 - d_2 = +2) for k in {1, 2, 3, 4, 5} (with dims_3_9_27 listing [d_0, d_1, d_2] at k = 1, 2, 3), and
  exact_spectra_ok asserts max coefficient error <= 10^-30 against closed-form algebraic P_q(x) at N in {3, 5, 7, 9, 15, 27}
  (reporting factored P_1(x) at N = 9 as weil9_q1 and [d_0, d_1, d_2] at N = 15 as weil15_dims). On C^3, L_{tr}(x, y, z) =
  (x, z, x z - y), R_{tr}(x, y, z) = (z, y, y z - x), C_{tr}(x, y, z) = (y, z, x), W_{6,tr} = sum_{j=0}^2 C_{tr}^j (L_{tr} +
  R_{tr}) C_{tr}^{-j}, and J_{W_6}(x, y, z) = d W_{6,tr} / d(x, y, z) is its 3 x 3 Jacobian. Here cubic_sos_amgm_ok asserts
  that D^{-1}(J_{W_6} - 2 I_3) D (for D = diag(sqrt(x), sqrt(y), sqrt(z))) equals the 3-square SOS form (sqrt(y) v_1 + sqrt(x)
  v_2)^2 + (sqrt(z) v_1 + sqrt(x) v_3)^2 + (sqrt(z) v_2 + sqrt(y) v_3)^2, that det(t I_3 - J_{W_6}) = (t - 2)(t - 2 - (x + y +
  z))^2 - 4 x y z identically, and that its peak at t = 2 + (x + y + z)/3 is (4 / 27)((x + y + z)^3 - 27 x y z). Across all
  sorted positive Markoff triples 3 <= a <= b <= c satisfying a^2 + b^2 + c^2 = a b c to Vieta-flip BFS depth 7 from (3, 3, 3)
  (count triples_checked = 65), degenerate_on_tree lists all triples with fewer than 3 distinct eigenvalues, and cp_336 and
  cp_3615 give factored det(t I_3 - J_{W_6}) at (3, 3, 6) and (3, 6, 15). On S_{kappa=-2} = {(x, y, z) : x^2 + y^2 + z^2 =
  x y z}, T_1(x, y, z) = (z, y, y z - x) and T_2(x, y, z) = (x, z, x z - y) correspond in rational coordinates (u, v) =
  (x / z, y / z) (inverse z = (u^2 + v^2 + 1)/(u v), x = u z, y = v z) to F_L(u, v) = (u / (v^2 + 1), u v / (v^2 + 1)) with
  shape w_L = v^2 / (v^2 + 1) and F_R(u, v) = (u v / (u^2 + 1), v / (u^2 + 1)) with shape w_R = 1 / (u^2 + 1) (blowup_ok
  asserts exact conjugacy, invariance of Goldman-Poincare Omega = dx ^ dy / (2 z - x y) = -du ^ dv / (u v), and metallic
  amphichirality S^{-1}(L^m R^m) S = (L^m R^m)^{-1} for 1 <= m <= 5). With Bloch-Wigner D(w) = Im Li_2(w) + arg(1 - w) log|w|
  and Catalan = sum_{n >= 0} (-1)^n / (2 n + 1)^2, sil_4catalan asserts |V_{L^2 R^2} - 4 * Catalan| < 10^-36, bronze_tr_minpoly
  gives the monic Z[u] minimal-polynomial coefficients of tr(D(F_L^3 o F_R^3)) on the geometric degree-8 Groebner branch of
  L^3 R^3, and gold_sil_brz_settled asserts consecutive excess-volume step ratios (Delta V_{k-1} - Delta V_{k-2})/(Delta V_k -
  Delta V_{k-1}) agree to < 10^-7 with (5 + sqrt(21))/2 at k = 12 across LLLLLLR, LLRRLLR, LLLRRRRLLLR on LR, with 9 + 4 sqrt(5)
  at k = 9 for LLLR on LLRR, and with (u_{max} + sqrt(u_{max}^2 - 4))/2 at k = 8 for LLLLRR on LLLRRR (controls, ast_floats,
  json_floats report planted-fault count and AST/JSON float counts).
- imports: none
- premises on main: B98, B371, B377, B381, B1876, B1881, B1983, B1985, B1993, B1994, B2000, B2001, B2004, B2008, P-374, P-630,
  P-775, P-882
- decisive script: relays/agy_2026-11-27_c67/c67_weil_unfolding_markoff_jacobian_and_p775_ptolemy_producer.py,
  SHA-256 7a9ed02cb7a6b66c, depends on the standard library, sympy and mpmath, run as
  python3 relays/agy_2026-11-27_c67/c67_weil_unfolding_markoff_jacobian_and_p775_ptolemy_producer.py,
  output SHA-256 232b5bafadc69a86
- decisive lines: 4 lines marked "DECISIVE:", SHA-256 41679863f6056a8d
- failing control: python3 relays/agy_2026-11-27_c67/c67_control.py
- second computation: fam3-v1-high-01 disjoint cold-room countercheck relays/agy_2026-11-27_c67/c67_countercheck.py
  (SHA-256 e0f31fc1dc812ca1, output SHA-256 e07f968219e84901, zero shared imports, Fourier-dual momentum-basis Weil
  representation, dual-number W_{6,tr} Jacobian and Sturm root count, and reciprocal cluster X-chart (alpha, beta) = (z / x,
  z / y) shooting with symbolic 3D Chebyshev trace elimination, agrees with 0 discrepancies)
- already on main?: topic_sweep.py "P-775|B1876|B2000|B2008|Weil" on origin/main (ae7defd04): closest arcs B371, B377, B381
  (finite Weil representations at primes 3 and 5 before the 6-move walk), B1876 (proves (t - 1)(t^2 - 5 t + 1) on m004 and
  observes Golden step-ratio settling to 4 digits via SnapPy, leaving higher precision and non-Golden grounds open in P-775),
  B2000 (evaluates (14, 5, 5) only at root (3, 3, 3), leaving outward tree behavior open), and B2008 (shows classical commuting
  unfolding stays mirror-symmetric, leaving non-commutative Weil unfolding and mod-4 chiral split unrun)
- what would make it fail: hom_comm_ok=False, or paired_mod4_eq1 differing from [5, 13, 17] or chiral_split_mod4_eq3 differing
  from [3, 7, 11, 19, 23], or all_3k_index_plus2=False, or degenerate_on_tree differing from [[3, 3, 3]], or
  gold_sil_brz_settled=False, or sil_4catalan=False, or bronze_tr_minpoly differing from [1, -114, 4264, -58910, 192359]
