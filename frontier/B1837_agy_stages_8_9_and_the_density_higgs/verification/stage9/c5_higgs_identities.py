"""S303 check c5 (value-free; Higgs-only quantities and matrix-identity residuals; main's B, Z and mpmath).
Theorem 72 (the doublet index's reading distance) and Theorem 75 ('P-666 DR / F_10 null-cone unification'):
 (A) min_phi ||S~ - e^{i phi} S||^2 = 2(||S||^2 - |det S|), ||S||^2 = tr(S^H S)/2, on main's units and eps (random S);
 (B) R . R = 0 (Jacobi), DR . DR = eta^6/4 (main's direction 'DR'), F_a . F_a for the census F_a = eps(th2^a, th4^a, i th3^a):
     F_6 . F_6 = -48 eta^12, F_10 . F_10 = -80 eta^12 E_4, and eta^12 divides F_a . F_a for every positive census a (n = a/2 odd);
 (C) rho = |h.h| / ||h||^2 for all 13 census directions at Im tau 1.6-6 (Re tau 0.25; inside the strip, P-670);
 (D) the 'shared' laws are properties of every Higgs: Y_e(S) = lam D Y_d(Sigma10 S)^T D (c1 (a)) and, on order-5 lines,
     Y_e(S) = c Y_d(S)^T for every 3-D Higgs (B1827 V3 with a0 = 0): matrix residuals on random h and on DR, F_10;
     and DR's QI component is nonzero (|h_I| / ||h||), so its same-Higgs lepton/down relations move at first order (c1 (b)).
Nothing about any sector's masses is printed."""
import cmath, math, pathlib, sys
import numpy as np
import mpmath as mp
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier/B1827_the_framing_ledger/verification/recheck"))
from identities_and_order5 import M_of, S_of, B
from mirror_rule_probe import Z
mp.mp.dps = 30
rng = np.random.default_rng(3031105)

# (A)
units = [np.eye(2, dtype=complex), B.QI, B.QJ, B.QK]
gram = np.array([[np.trace(u.conj().T @ v) / 2 for v in units] for u in units])
pr = max(np.abs(B.EPS @ u.conj() @ B.EPS.T - u).max() for u in units)
worst = 0.0; rho_rng = [1, 0]
for _ in range(400):
    a0 = complex(*rng.normal(size=2)); h = rng.normal(size=3) + 1j * rng.normal(size=3)
    S = S_of(a0, h); St = B.EPS @ S.conj() @ B.EPS.T
    n2 = np.trace(S.conj().T @ S).real / 2; dS = np.linalg.det(S)
    phis = np.linspace(0, 2 * np.pi, 4001)
    dmin = min(np.trace((St - np.exp(1j * p) * S).conj().T @ (St - np.exp(1j * p) * S)).real / 2 for p in phis[::50])
    ps = -cmath.phase(dS); dstar = np.trace((St - np.exp(1j * ps) * S).conj().T @ (St - np.exp(1j * ps) * S)).real / 2
    worst = max(worst, abs(dstar - 2 * (n2 - abs(dS))), max(0.0, dstar - dmin - 1e-12))
    rho = abs(dS) / n2; rho_rng = [min(rho_rng[0], rho), max(rho_rng[1], rho)]
print("(A) units orthonormal (dev %.1e), pseudoreal under eps (dev %.1e); reading distance identity worst %.1e over 400 S "
      "(min attained at phi* = -arg det S); rho in [%.3f, %.3f] within [0, 1]" % (np.abs(gram - np.eye(4)).max(), pr, worst, *rho_rng))


# (B)
def thetas(tau):
    q = mp.exp(1j * mp.pi * mp.mpc(tau.real, tau.imag))
    return mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)


def eta(tau):
    t = mp.mpc(tau.real, tau.imag); q = mp.exp(2j * mp.pi * t)
    return mp.exp(2j * mp.pi * t / 24) * mp.qp(q)


def E4(tau):
    t2, t3, t4 = thetas(tau); return (t2 ** 8 + t3 ** 8 + t4 ** 8) / 2


def dot(v): return sum(x * x for x in v)


worstB = {}
for tau in (0.25 + 1.6j, 0.1 + 2.3j, 0.6 + 3.1j, 0.45 + 1.2j):
    R = [mp.mpc(x) for x in Z.direction("R", tau)]; DR = [mp.mpc(x) for x in Z.direction("DR", tau)]
    e = eta(tau); t2, t3, t4 = thetas(tau)
    nR = sum(abs(x) ** 2 for x in R)
    worstB["R.R/||R||^2"] = max(worstB.get("R.R/||R||^2", 0), float(abs(dot(R)) / nR))
    worstB["DR.DR vs eta^6/4"] = max(worstB.get("DR.DR vs eta^6/4", 0), float(abs(dot(DR) / (e ** 6 / 4) - 1)))
    # main's R against F_2 / (2 pi eta^3)
    F2 = [-(t2 ** 2), -(t4 ** 2), 1j * t3 ** 2]
    cst = [R[k] / (F2[k] / (2 * mp.pi * e ** 3)) for k in range(3)]
    worstB["R vs F_2/(2 pi eta^3) (ratio spread)"] = max(worstB.get("R vs F_2/(2 pi eta^3) (ratio spread)", 0), float(max(abs(c - cst[0]) for c in cst)))
    for a, form in ((6, lambda: -48 * e ** 12), (10, lambda: -80 * e ** 12 * E4(tau))):
        v = [mp.mpc(x) for x in Z.direction("F_%d" % a, tau)]
        key = "F_%d.F_%d vs closed form" % (a, a)
        worstB[key] = max(worstB.get(key, 0), float(abs(dot(v) / form() - 1)))
    for a in (-10, -6, -2, 14, 18, 22, 26):
        v = [mp.mpc(x) for x in Z.direction("F_%d" % a, tau)]
        x, y = t2 ** 4, t4 ** 4; n = mp.mpf(a) / 2
        # F_a . F_a = x^n + y^n - (x+y)^n (eps^2 = 1 for a = 2 mod 4); divisible by xy(x+y) = 16 eta^12
        key = "F_a.F_a = x^n+y^n-(x+y)^n, a in {-10,-6,-2,14,18,22,26}"
        worstB[key] = max(worstB.get(key, 0), float(abs(dot(v) / (x ** n + y ** n - (x + y) ** n) - 1)))
for k, v in worstB.items(): print("(B) %-60s worst %.1e" % (k, v))
print("    (eta^12 = xy(x+y)/16 with x = th2^4, y = th4^4; x^n + y^n - (x+y)^n vanishes on x = 0, y = 0, x = -y for odd n, so")
print("     every POSITIVE-weight census F_a (a = 6..26) is off the null cone by eta^12 times a holomorphic modular form; the")
print("     negative-weight F_a are not near-null (c5b): near-nullness is shared by DR and F_6..F_26, not a DR/F_10 property)")

# (C)
print("(C) rho = |h.h|/||h||^2 for the 13 census directions, Re tau = 0.25:")
for im in (1.6, 2.4, 3.2, 4.5, 6.0):
    tau = complex(0.25, im); rr = []
    for d in Z.DIRS:
        h = np.array(Z.direction(d, tau)); rr.append(abs(h @ h) / np.vdot(h, h).real)
    print("   Im tau %.1f: median %.2e, max %.2e (%s)" % (im, np.median(rr), max(rr), Z.DIRS[int(np.argmax(rr))]))

# (D)
def sig(h):
    g = np.array(h, dtype=complex).copy(); g[0] = -g[0]; return g


D = np.diag([1, -1, 1])
w10 = 0.0; w5 = 0.0; hI = []
for tau in (0.3 + 2.6j, 0.62 + 1.9j):
    L = Z.radii(tau)[0]
    hs = [rng.normal(size=3) + 1j * rng.normal(size=3) for _ in range(3)] + [np.array(Z.direction(d, tau)) for d in ("DR", "F_10")]
    hI.append(abs(np.array(Z.direction("DR", tau))[0]) / np.linalg.norm(Z.direction("DR", tau)))
    for line in [(0.4, (2 * j + 1) / 10) for j in range(5)]:
        Md, _ = M_of(tau, line, L, "down"); Me, _ = M_of(tau, line, L, "lepton")
        for h in hs:
            Ye = B.coupling(S_of(0, h), Me); Bm = D @ B.coupling(S_of(0, sig(h)), Md).T @ D
            lam = np.vdot(Bm.ravel(), Ye.ravel()) / np.vdot(Bm.ravel(), Bm.ravel()).real
            w10 = max(w10, np.linalg.norm(Ye - lam * Bm) / np.linalg.norm(Ye))
    for line in [(0.4, 0.2), (0.4, 0.6), (0.2, 0.4), (0.6, 0.8)]:
        Md, _ = M_of(tau, line, L, "down"); Me, _ = M_of(tau, line, L, "lepton")
        for h in hs:
            Ye = B.coupling(S_of(0, h), Me); Bm = B.coupling(S_of(0, h), Md).T
            c = np.vdot(Bm.ravel(), Ye.ravel()) / np.vdot(Bm.ravel(), Bm.ravel()).real
            w5 = max(w5, np.linalg.norm(Ye - c * Bm) / np.linalg.norm(Ye))
print("(D) order-10 reflection Y_e(h) = lam D Y_d(Sigma10 h)^T D for 3 random h, DR and F_10: worst %.1e (holds for every Higgs)" % w10)
print("    order-5 Y_e(h) = c Y_d(h)^T on 4 order-5 lines for the same h: worst %.1e (every 3-D Higgs; B1827 V3)" % w5)
print("    DR's QI share |h_I|/||h|| at the two tau: %s (nonzero: DR is not QI-free)" % ", ".join("%.3f" % x for x in hI))
