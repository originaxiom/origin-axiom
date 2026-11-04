"""agy:B1765/B1771 (eta numbers), agy:B1767/B1768 (the genus-3 curve w^4 = 4x^3 - g2 x - g3 at tau*), agy:B1779 (the Ray-Singer
torsion of E_tau*), from first principles (mpmath); no lane code.  tau* = (1 + i sqrt 84)/3, lattice Z + Z tau.
 1. |eta(tau*)|, 2 y |eta|^4 (B1765: 0.249250), -ln(2 y |eta|^4) (1.389298), |q| = e^{-2 pi y}, e^{-pi y}.
 2. g2 = (4 pi^4/3) E4, g3 = (8 pi^6/27) E6 (B1768: 129.878716 + 0.000124i, 284.856388 - 0.000573i); the roots e1, e2, e3 from theta
    constants (e1 = (pi^2/3)(th3^4 + th4^4) = wp(1/2), e2 = (pi^2/3)(th2^4 - th4^4) = wp(tau/2), e3 = -(pi^2/3)(th2^4 + th3^4)) against
    B1768's 6.579736, -3.292548 - 0.004642i, -3.287188 + 0.004641i and its labels 'e1 ~ pi^2/3', 'e2,3 ~ -pi^2/6'.
 3. int_{e2}^{e3} dx / sqrt(4x^3 - g2 x - g3) = +-1/2 (B1768: 0.500000000), by quadrature on the straight segment.
 4. det' of the scalar Laplacian on the flat torus C/(Z + Z tau) (area y): zeta_Delta(s) = (4 pi^2 / y)^{-s} E(tau, s); zeta'(0) by
    differentiating the Fourier (Chowla-Selberg) expansion at s = 0; against y^2 |eta|^4 (Kronecker's first limit formula).
    Then B1779's stated definition T = -1/2 ln det' Delta_0 + 1/2 ln det Delta_1 (on a flat torus Delta_1 = Delta_0 (x) 1_2, so
    T = 1/2 ln det' Delta_0) and the holomorphic (Ray-Singer 1973) convention ln T = -1/2 ln det' Delta_dbar (Delta_dbar = Delta/2),
    against B1779's T(E) = -ln(2 pi) - ln(2 y) - 2 ln|eta|^2 = -0.448579.
 5. Riemann-Hurwitz: the double cover Y -> E branched at the four 2-torsion points, and the Q8 cover of E branched at one point with
    ramification 2; the central involution's action on dx/w^2, dx/w^3, x dx/w^3 and the Hodge orthogonality by the sheet sum."""
import json, math, pathlib
import mpmath as mp
mp.mp.dps = 30
OUT = {}
y = mp.sqrt(84) / 3; x = mp.mpf(1) / 3; tau = mp.mpc(x, y)
q2 = mp.exp(2j * mp.pi * tau)          # e^{2 pi i tau}
qn = mp.exp(1j * mp.pi * tau)          # nome for jtheta
eta = mp.exp(2j * mp.pi * tau / 24) * mp.qp(q2)
ae = abs(eta)
r1 = {"|eta|": ae, "|eta|^2": ae ** 2, "2y|eta|^4": 2 * y * ae ** 4, "-ln(2y|eta|^4)": -mp.log(2 * y * ae ** 4), "|q|": abs(q2), "e^{-pi y}": mp.exp(-mp.pi * y)}
OUT["eta"] = {k: str(v) for k, v in r1.items()}
print("1. " + "; ".join("%s = %s" % (k, mp.nstr(v, 10)) for k, v in r1.items()))

def Eis(k):
    s = mp.fsum(mp.mpf(n) ** (k - 1) * q2 ** n / (1 - q2 ** n) for n in range(1, 40))
    return 1 + (240 if k == 4 else -504) * s
g2 = 4 * mp.pi ** 4 / 3 * Eis(4); g3 = 8 * mp.pi ** 6 / 27 * Eis(6)
th2, th3, th4 = (mp.jtheta(n, 0, qn) for n in (2, 3, 4))
e1 = mp.pi ** 2 / 3 * (th3 ** 4 + th4 ** 4); e2 = mp.pi ** 2 / 3 * (th2 ** 4 - th4 ** 4); e3 = -mp.pi ** 2 / 3 * (th2 ** 4 + th3 ** 4)
cub = lambda X: 4 * X ** 3 - g2 * X - g3
OUT["curve"] = {"g2": str(g2), "g3": str(g3), "e1": str(e1), "e2": str(e2), "e3": str(e3), "residuals": [str(abs(cub(e))) for e in (e1, e2, e3)],
                "2pi^2/3": str(2 * mp.pi ** 2 / 3), "pi^2/3": str(mp.pi ** 2 / 3), "pi^2/6": str(mp.pi ** 2 / 6)}
print("2. g2 = %s ; g3 = %s" % (mp.nstr(g2, 10), mp.nstr(g3, 10)))
print("   e1 = %s ; e2 = %s ; e3 = %s ; |cubic(e_i)| = %s" % (mp.nstr(e1, 8), mp.nstr(e2, 8), mp.nstr(e3, 8), [mp.nstr(abs(cub(e)), 2) for e in (e1, e2, e3)]))
print("   for comparison: 2 pi^2/3 = %s, pi^2/3 = %s, pi^2/6 = %s" % (mp.nstr(2 * mp.pi ** 2 / 3, 8), mp.nstr(mp.pi ** 2 / 3, 8), mp.nstr(mp.pi ** 2 / 6, 8)))

# 3. the half period, with continuous branch tracking along the segment
def seg_integral(a, b):
    """X = a + (b - a) sin^2(th): with cubic = 4 (X - e1)(X - a)(X - b) the integrand dX/sqrt(cubic) becomes d th / sqrt(e1 - X) up to
    one overall sign (fourth root of unity); sqrt(e1 - X) is smooth on the segment (e1 - X ~ 9.87, far from the cut)"""
    return mp.quad(lambda th: 1 / mp.sqrt(e1 - (a + (b - a) * mp.sin(th) ** 2)), [0, mp.pi / 2])
I23 = seg_integral(e2, e3)
OUT["half_period"] = str(I23)
print("3. int_{e2}^{e3} dx/sqrt(cubic) on the straight segment = %s" % mp.nstr(I23, 12))

# 4. det' Laplacian on the flat torus
def sigma(n, a): return mp.fsum(mp.mpf(d) ** a for d in range(1, n + 1) if n % d == 0)
def E(s, nmax=25):
    c = 2 * mp.zeta(2 * s) * y ** s + 2 * mp.sqrt(mp.pi) * mp.gamma(s - 0.5) * mp.zeta(2 * s - 1) * mp.rgamma(s) * y ** (1 - s)
    f = 8 * mp.pi ** s * mp.sqrt(y) * mp.rgamma(s) * mp.fsum(mp.mpf(n) ** (s - 0.5) * sigma(n, 1 - 2 * s) * mp.besselk(s - 0.5, 2 * mp.pi * n * y) * mp.cos(2 * mp.pi * n * x) for n in range(1, nmax + 1))
    return c + f
zeta_D = lambda s: (4 * mp.pi ** 2 / y) ** (-s) * E(s)
z0 = zeta_D(mp.mpf("1e-25")); zp = mp.diff(zeta_D, 0)
det_num = mp.exp(-zp); det_kron = y ** 2 * ae ** 4
T_lane_def = mp.log(det_num) / 2
T_holo = -mp.log(2 * det_num) / 2                     # det'(Delta/2) = 2^{-zeta(0)} det' Delta = 2 det' Delta (zeta(0) = -1)
T_lane_formula = -mp.log(2 * mp.pi) - mp.log(2 * y) - 2 * mp.log(ae ** 2)
OUT["torsion"] = {"zeta(0)": str(z0), "zeta'(0)": str(zp), "det'_numeric": str(det_num), "y^2|eta|^4": str(det_kron),
                  "T_by_B1779's_definition=1/2 ln det'": str(T_lane_def), "T_holomorphic=-1/2 ln det'(Delta/2)": str(T_holo),
                  "B1779_formula_value": str(T_lane_formula)}
print("4. zeta_Delta(0) = %s ; det' Delta_0 = exp(-zeta'(0)) = %s ; Kronecker y^2|eta|^4 = %s" % (mp.nstr(z0, 8), mp.nstr(det_num, 15), mp.nstr(det_kron, 15)))
print("   torsion under B1779's own definition (1/2 ln det' Delta_0) = %s ; holomorphic convention = %s ; B1779's formula gives %s"
      % (mp.nstr(T_lane_def, 8), mp.nstr(T_holo, 8), mp.nstr(T_lane_formula, 8)))

# 5. Riemann-Hurwitz and the involution
g_double = (2 * (2 * 1 - 2) + 4 * (2 - 1)) // 2 + 1            # 2g - 2 = 2(2*1 - 2) + sum (e - 1), four points, e = 2
g_q8 = (8 * (2 * 1 - 2) + 8 * (1 - mp.mpf(1) / 2)) / 2 + 1       # one branch point, ramification 2 over it (8/2 points, e - 1 = 1 each)
g_q8_four = (8 * (2 * 1 - 2) + 4 * 8 * (1 - mp.mpf(1) / 2)) / 2 + 1  # if branched (e = 2) over FOUR points of E
# differentials x^i dx / w^j on w^4 = cubic: holomorphic iff 1 <= j <= 3 (branch points) and 3j >= 4(i + 1) + 1 (infinity)
diffs = [(i, j) for j in range(1, 4) for i in range(0, 4) if 3 * j >= 4 * (i + 1) + 1]
# sheet sum for the Hodge product of omega_a = x^i dx / w^j: sheets w -> i^k w multiply omega by i^{-jk}
def sheet(j1, j2): return sum((1j) ** (-j1 * k) * ((1j) ** (-j2 * k)).conjugate() for k in range(4))
OUT["rh"] = {"genus_double_cover_of_E_branched_at_4": g_double, "genus_Q8_cover_branched_at_1": float(g_q8), "genus_Q8_cover_branched_at_4": float(g_q8_four),
             "holomorphic_differentials_(i,j)": diffs, "sheet_sum_(j=2,j=3)": abs(sheet(2, 3)), "sheet_sum_(3,3)": abs(sheet(3, 3)), "sheet_sum_(2,2)": abs(sheet(2, 2))}
print("5. genus of the double cover of E branched at the four 2-torsion points: %d ; Q8 cover of E branched at one point (e=2): %s ; at four points: %s"
      % (g_double, mp.nstr(g_q8, 3), mp.nstr(g_q8_four, 3)))
print("   holomorphic x^i dx/w^j: %s ; Hodge sheet sums |sum_k|: (dx/w^2, dx/w^3) %.1e, (w^3, w^3) %.1f, (w^2, w^2) %.1f"
      % (diffs, abs(sheet(2, 3)), abs(sheet(3, 3)), abs(sheet(2, 2))))
json.dump(OUT, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1, default=str)
print("exit 0")
