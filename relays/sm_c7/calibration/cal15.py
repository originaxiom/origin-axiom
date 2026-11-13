# calibration C15 (outside the population): F_u against a direct regularised lattice difference; c_s - F_u is u-free
# (tau-only); the kernel's multiplier point u = (alpha, -beta) as an affine function of ubar's coordinates, per channel
import sys, pathlib, math, cmath, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import numpy as np, b1656_kernel as B, sm_c7_lib as L
def mult(x, y, t, R, s):
    z = np.array([0.11 + 0.07j]); K = lambda zz: B.pairs(x, y, zz, t)[s] / R[s]
    a = cmath.phase(complex(K(z + 1)[0] / K(z)[0])) / (2 * math.pi); b = cmath.phase(complex(K(z + t)[0] / K(z)[0])) / (2 * math.pi)
    return a % 1.0, b % 1.0
t = 0.21 + 1.13j
# F_u differences against the brute lattice difference (Parseval-type): F_u1 - F_u2 = y sum (1/|l+u1'|^2 - 1/|l+u2'|^2)
def latdiff(u1, u2, t, Rm=1500):
    m = np.arange(-Rm, Rm + 1); tot = 0.0
    for mm in range(-Rm, Rm + 1):
        lam = mm * t + m
        tot += np.sum(1/np.abs(lam + (u1[0]*t + u1[1]))**2 - 1/np.abs(lam + (u2[0]*t + u2[1]))**2)
    return tot * t.imag
for u1, u2 in [((0.13, 0.4), (0.31, 0.77)), ((0.0, 0.25), (0.5, 0.1))]:
    print("F_u1 - F_u2 = %.7f   lattice %.7f" % (L.F_shift(u1, t) - L.F_shift(u2, t), latdiff(u1, u2, t)))
print("reduction:", abs(L.F_shift((0.13, 0.4), complex(0.3, 0.09)) - L.F_shift_reduced((0.13, 0.4), complex(0.3, 0.09))))
random.seed(5)
for t in [0.21 + 1.13j, -0.37 + 0.92j, 0.05 + 1.6j]:
    hs = {s: [] for s in "1ijk"}; maps = {s: [] for s in "1ijk"}
    for _ in range(4):
        p1, p2 = random.uniform(0.05, 0.45), random.uniform(0.05, 0.95)
        w = B.line_w(p1, p2, t); x, y = B.sector_twists(w, t, 1, 0); R = B.residues(x, y, t); c = B.cA(x, y, t, R)
        a1 = w.imag / t.imag; a2 = w.real - a1 * t.real
        for s in "1ijk":
            if c[s] is None: continue
            al, be = mult(x, y, t, R, s); u = (al, -be)
            hs[s].append(c[s] - L.F_shift(u, t)); maps[s].append(((a1 % 1, a2 % 1), (u[0] % 1, u[1] % 1)))
    print("tau", t)
    for s in "1ijk":
        print("   channel %s  h = c_s - F_u: %s  spread %.1e   (ubar coords -> u): %s" % (s, " ".join("%.8f" % v for v in hs[s]),
              max(hs[s]) - min(hs[s]), [tuple(round(q, 4) for q in pr[0] + pr[1]) for pr in maps[s][:2]]))
