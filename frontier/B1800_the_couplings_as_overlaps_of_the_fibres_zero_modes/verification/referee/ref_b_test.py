"""Referee B1800, claim (b): is 'B1636's entries are not the overlaps with any fixed Higgs' robust to
  (1) the six labellings of the three off-diagonal couplings against theta_r^2 (and to using the odd characteristic),
  (2) continuous matter Wilson lines (the Higgs in each pair's sector then has two modes, both kept free),
with a positive control (functions that do follow B1636) and a near-control.
Test: B1636 needs, for two off-diagonal pairs P, P' with targets theta_A^2, theta_B^2, a nonzero function in
span{C_P,m / theta_A^2} that also lies in span{C_P',m / theta_B^2} (the common factor lambda(tau) and the constant
Higgs components eliminated).  Measured by the sine of the smallest principal angle between the two spans over N
sampled tau (0 iff they share a function on the sample).
    python3 -B ref_b_test.py"""
import itertools, math
import numpy as np
rng = np.random.default_rng(11)

def thc(a, b, T, N=30):
    T = np.atleast_1d(T); n = np.arange(-N, N + 1)[:, None] + a
    return np.exp(1j*np.pi*n*n*T[None, :] + 2j*np.pi*n*b).sum(0)

TAUS = np.array([complex(x, y) for x, y in zip(rng.uniform(-0.5, 0.5, 60), rng.uniform(0.7, 2.2, 60))])
TH = {"2": thc(0.5, 0, TAUS), "3": thc(0, 0, TAUS), "4": thc(0, 0.5, TAUS)}

def span_basis(cols, tol=1e-10):
    A = np.array(cols).T
    A = A / np.linalg.norm(A, axis=0, keepdims=True).clip(1e-300)
    U, s, _ = np.linalg.svd(A, full_matrices=False)
    return U[:, s > tol*s[0]]

def min_angle_sine(cols1, cols2):
    Q1, Q2 = span_basis(cols1), span_basis(cols2)
    s = np.linalg.svd(Q1.conj().T @ Q2, compute_uv=False)
    c = min(1.0, float(s.max())); return math.sqrt(max(0.0, 1 - c*c))

def pair_funcs(d):
    """the two Higgs-mode couplings of a pair whose characteristic difference is d = (da, db): theta[(da+m)/2, db](0, 2 tau)."""
    da, db = d
    return [thc((da + m)/2, db, 2*TAUS) for m in (0, 1)]

def b1636_score(d32, d34, d24, target):
    """target: dict pair -> theta label r whose square B1636 puts there.  Score = max over the two independent pair
    comparisons of the smallest principal-angle sine (both must vanish for B1636)."""
    F = {"32": pair_funcs(d32), "34": pair_funcs(d34), "24": pair_funcs(d24)}
    G = {P: [f/TH[target[P]]**2 for f in F[P] if np.max(np.abs(f)) > 1e-12] for P in F}
    return max(min_angle_sine(G["32"], G["34"]), min_angle_sine(G["24"], G["34"]))

PAIRS = ["32", "34", "24"]
B1636 = {"32": "4", "34": "2", "24": "3"}
labellings = [dict(zip(PAIRS, perm)) for perm in itertools.permutations(["4", "2", "3"])]

# positive control: functions that ARE theta_r^2 times a common factor give 0
lam = thc(0.3, 0.1, TAUS)
def pc(target):
    G = {P: [lam*TH[target[P]]**2/TH[target[P]]**2] for P in PAIRS}
    return max(min_angle_sine(G["32"], G["34"]), min_angle_sine(G["24"], G["34"]))
print("positive control (exact B1636 functions): %.1e" % pc(B1636))
# near-control: B1636 functions perturbed by 1% of another theta function
G = {P: [lam*(1 + 0.01*thc(0.1, 0.2, TAUS)*(P == "32"))] for P in PAIRS}
print("near-control (1%% perturbation of one entry): %.1e" % max(min_angle_sine(G["32"], G["34"]), min_angle_sine(G["24"], G["34"])))

# (1) even characteristics: the arc's matter. Differences: 3-2 = (-1/2, 0), 3-4 = (0, -1/2), 2-4 = (1/2, -1/2)
d32, d34, d24 = (-0.5, 0.0), (0.0, -0.5), (0.5, -0.5)
for lab in labellings:
    print("even characteristics, labelling %s: score %.3f" % (lab, b1636_score(d32, d34, d24, lab)))
# with the odd characteristic replacing theta3 (matter at [1/2,0], [0,1/2], [1/2,1/2]): same three difference classes
d_alt = {"32": (0.5 - 0.5, 0.0 - 0.5), "34": (0.5 - 0.0, 0.5 - 0.5), "24": (0.5 - 0.0, 0.0 - 0.5)}
print("odd replacing theta3, worst-best over labellings: %.3f" % min(b1636_score(d_alt["32"], d_alt["34"], d_alt["24"], lab) for lab in labellings))

# (2) continuous Wilson lines: c3, c2, c4 arbitrary (a, b) in [0,1)^2; only differences matter
best = (9, None)
grid = np.linspace(0, 1, 9, endpoint=False)
cnt = 0
for a2, b2, a4, b4 in itertools.product(grid, grid, grid, grid):
    c3, c2, c4 = (0.0, 0.0), (a2, b2), (a4, b4)
    D = lambda x, y: (x[0] - y[0], x[1] - y[1])
    for lab in labellings:
        s = b1636_score(D(c3, c2), D(c3, c4), D(c2, c4), lab); cnt += 1
        if s < best[0]: best = (s, (c2, c4, lab))
print("grid of %d (Wilson lines x labellings): best score %.4f at c2=%s c4=%s labelling %s" % (cnt, best[0], best[1][0], best[1][1], best[1][2]))
# local refinement from random starts (Nelder-Mead, own implementation-free: scipy if present)
try:
    from scipy.optimize import minimize
    res_best = 9
    for lab in labellings:
        for _ in range(25):
            x0 = rng.random(4)
            f = lambda x: b1636_score((-x[0], -x[1]), (-x[2], -x[3]), (x[0] - x[2], x[1] - x[3]), lab)
            r = minimize(f, x0, method="Nelder-Mead", options={"xatol": 1e-6, "fatol": 1e-8, "maxiter": 600})
            res_best = min(res_best, r.fun)
    print("Nelder-Mead from 150 random starts: best score %.4f" % res_best)
except ImportError:
    print("scipy absent: grid only")
print("ref_b_test exit 0")
