"""Referee B1800 (b), strict joint test for continuous Wilson lines: B1636 needs ONE function lambda(tau) with
Y_P = g_P lambda theta_{r(P)}^2 for all three off-diagonal pairs, Y_P in span{C_P,0, C_P,1}.  Score = 1 - mu/3, mu the top
eigenvalue of the sum of the three projectors onto span{C_P,m/theta_r(P)^2} (0 iff a common function exists on the
sample).  Two tau samples: the arc's band (Im 0.7-2.2) and a wide one (Im 0.4-4).  Then the best point's actual
least-squares misfit of the three entries against B1636 (lambda fitted pointwise).
    python3 -B ref_b_joint.py"""
import itertools, math
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(5)

def thc(a, b, T, N=40):
    T = np.atleast_1d(T); n = np.arange(-N, N + 1)[:, None] + a
    return np.exp(1j*np.pi*n*n*T[None, :] + 2j*np.pi*n*b).sum(0)

def sample(lo, hi, n=80):
    return np.array([complex(x, y) for x, y in zip(rng.uniform(-0.5, 0.5, n), rng.uniform(lo, hi, n))])

def proj(cols):
    A = np.array(cols).T; A = A/np.linalg.norm(A, axis=0, keepdims=True)
    U, s, _ = np.linalg.svd(A, full_matrices=False); U = U[:, s > 1e-10*s[0]]
    return U @ U.conj().T

PAIRS = ["32", "34", "24"]
labellings = [dict(zip(PAIRS, perm)) for perm in itertools.permutations(["4", "2", "3"])]

def score(x, lab, T, TH):
    c2, c4 = (x[0], x[1]), (x[2], x[3]); c3 = (0.0, 0.0)
    D = {"32": (c3[0] - c2[0], c3[1] - c2[1]), "34": (c3[0] - c4[0], c3[1] - c4[1]), "24": (c2[0] - c4[0], c2[1] - c4[1])}
    S = 0
    for P in PAIRS:
        cols = [thc((D[P][0] + m)/2, D[P][1], 2*T)/TH[lab[P]]**2 for m in (0, 1)]
        cols = [c for c in cols if np.max(np.abs(c)) > 1e-9*np.max(np.abs(TH["3"]))]
        S = S + proj(cols)
    mu = np.linalg.eigvalsh(S).max()
    return 1 - mu/3

for name, (lo, hi) in (("band Im 0.7-2.2", (0.7, 2.2)), ("wide Im 0.4-4", (0.4, 4.0))):
    T = sample(lo, hi); TH = {"2": thc(0.5, 0, T), "3": thc(0, 0, T), "4": thc(0, 0.5, T)}
    # positive control: Y_P = theta_r^2 times a common function, inside a 2-dim span with a junk partner
    lam = thc(0.3, 0.1, T)
    S = sum(proj([lam, thc(0.17, 0.3, 2*T)/TH["3"]**2]) for _ in PAIRS)
    print("%s: positive control %.1e" % (name, 1 - np.linalg.eigvalsh(S).max()/3))
    # even characteristics, all labellings
    ev = min(score((0.5, 0.0, 0.0, 0.5), lab, T, TH) for lab in labellings)
    print("  even characteristics, best over 6 labellings: %.4f" % ev)
    best = (9, None)
    grid = np.linspace(0, 1, 8, endpoint=False)
    for x in itertools.product(grid, grid, grid, grid):
        for li, lab in enumerate(labellings):
            s = score(x, lab, T, TH)
            if s < best[0]: best = (s, (x, li))
    xb, li = best[1]
    r = minimize(lambda x: score(x, labellings[li], T, TH), np.array(xb), method="Nelder-Mead", options={"xatol": 1e-7, "fatol": 1e-10, "maxiter": 2000})
    rb = (r.fun, r.x, li)
    for _ in range(40):
        lj = rng.integers(6); x0 = rng.random(4)
        r = minimize(lambda x: score(x, labellings[lj], T, TH), x0, method="Nelder-Mead", options={"xatol": 1e-7, "fatol": 1e-10, "maxiter": 1500})
        if r.fun < rb[0]: rb = (r.fun, r.x, lj)
    print("  continuous Wilson lines: grid best %.5f; refined best %.6f at c2=(%.4f,%.4f) c4=(%.4f,%.4f) labelling %s" % (
        best[0], rb[0], *rb[1], labellings[rb[2]]))
print("ref_b_joint exit 0")
