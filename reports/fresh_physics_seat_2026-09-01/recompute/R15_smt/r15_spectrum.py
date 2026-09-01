#!/usr/bin/env python3
"""R15 stage 2: my own censuses + joint C-weight table + wall discovery.

Still blind to the arc's solvers. Method: root-evaluation — decompose e6 under the
toral C = span(g8,g14,g16,g22); a weight-line survives a measurement x iff the weight
evaluates to zero on x. Discovery numerics at high precision; exact certification of
the headline dims over Q and mod p happens in stage 3.
"""
import pickle, random, json
from fractions import Fraction
import numpy as np
import mpmath as mp

random.seed(7)
mp.mp.dps = 60

D = pickle.load(open(__file__.rsplit("/", 1)[0] + "/r15_e6_data.pkl", "rb"))
DIM = D["TAB_dims"]
ads = {}
for n, M in D["ads"].items():
    ads[int(n)] = [[Fraction(x) for x in row] for row in M]

# rescale each charge to a primitive integer matrix (scale is immaterial for
# centralizers; record the factor for convention diffs)
scales = {}
ads_int = {}
for n, M in ads.items():
    from math import gcd, lcm
    dens = [f.denominator for row in M for f in row if f]
    L = 1
    for d in dens:
        L = lcm(L, d)
    nums = [abs(int(f * L)) for row in M for f in row if f]
    g = 0
    for x in nums:
        g = gcd(g, x)
    fac = Fraction(L, g)
    scales[n] = fac  # g_scaled = fac * g_original
    ads_int[n] = np.array([[int(f * fac) for f in row] for row in M], dtype=object)
print("scale factors applied (g_int = fac * g_defn):", {n: str(scales[n]) for n in scales})

A8, A14, A16, A22 = (ads_int[n] for n in (8, 14, 16, 22))

def to_mp(M):
    return mp.matrix([[mp.mpf(int(M[i, j])) for j in range(DIM)] for i in range(DIM)])

A8m, A14m, A16m, A22m = map(to_mp, (A8, A14, A16, A22))

# ---- exact rational censuses via numpy-free integer rank (use fractions/sympy) ----
import sympy as sp
S8, S14, S16, S22 = (sp.Matrix([[int(ads_int[n][i, j]) for j in range(DIM)] for i in range(DIM)])
                     for n in (8, 14, 16, 22))
def nullity(M):
    return M.cols - M.rank()
cen = {}
cen["x8"] = nullity(S8); cen["x14"] = nullity(S14); cen["x16"] = nullity(S16); cen["x22"] = nullity(S22)
cen["x8+x16"] = nullity(sp.Matrix.vstack(S8, S16))
Call = sp.Matrix.vstack(S8, S14, S16, S22)
cen["C_joint"] = nullity(Call)
print("[exact /Q] censuses:", cen)

# Cent(C) basis over Q, derived dim, center
ker = Call.nullspace()
centC = sp.Matrix.hstack(*ker)
assert centC.cols == cen["C_joint"]

# ---------------- numeric joint diagonalization ----------------
c = [3, -7, 5, 11]
T = c[0] * A8 + c[1] * A14 + c[2] * A16 + c[3] * A22
Tf = np.array(T, dtype=float)
w, V = np.linalg.eig(Tf)

# refine each eigenpair with mpmath inverse iteration
Tm = c[0] * A8m + c[1] * A14m + c[2] * A16m + c[3] * A22m

def refine(lam0, v0, iters=25):
    lam = mp.mpc(lam0)
    v = mp.matrix([mp.mpc(x) for x in v0])
    v = v / mp.norm(v)
    I = mp.eye(DIM)
    for _ in range(iters):
        try:
            vn = mp.lu_solve(Tm - lam * I, v)
        except ZeroDivisionError:
            lam = lam + mp.mpf("1e-25")
            vn = mp.lu_solve(Tm - lam * I, v)
        v = vn / mp.norm(vn)
        Av = Tm * v
        # Rayleigh
        num = sum(Av[i] * mp.conj(v[i]) for i in range(DIM))
        den = sum(v[i] * mp.conj(v[i]) for i in range(DIM))
        lam_new = num / den
        if abs(lam_new - lam) < mp.mpf("1e-52"):
            lam = lam_new
            break
        lam = lam_new
    return lam, v

def weight_of(v, M):
    i = max(range(DIM), key=lambda k: abs(v[k]))
    Av = M * v
    return Av[i] / v[i]

# cluster eigenvalues; zero cluster = Cent(C)
zero_idx = [i for i in range(DIM) if abs(w[i]) < 1e-7]
nz_idx = [i for i in range(DIM) if abs(w[i]) >= 1e-7]
print("numeric: dim zero-eigenspace of generic C-combo =", len(zero_idx))

weights = []  # (w8, w14, w16, w22) refined, per nonzero line
for i in nz_idx:
    lam, v = refine(w[i], V[:, i])
    tup = tuple(weight_of(v, M) for M in (A8m, A14m, A16m, A22m))
    # residual check
    res = max(float(mp.norm(M * v - t * v)) for M, t in zip((A8m, A14m, A16m, A22m), tup))
    assert res < 1e-40, (i, res)
    weights.append(tup)
print("refined", len(weights), "nonzero weight lines; residuals < 1e-40")

# save for later stages
with open(__file__.rsplit("/", 1)[0] + "/r15_weights.pkl", "wb") as fh:
    pickle.dump({"weights": [[mp.nstr(x, 50) for x in tup] for tup in weights],
                 "scales": {n: str(scales[n]) for n in scales},
                 "censuses": cen}, fh)

# ---------------- analysis: Pi-plane, enhancement cubic ----------------
def z(x):
    return complex(float(mp.re(x)), float(mp.im(x)))

# weights vanishing on the whole plane (w8 = w16 = 0): core beyond Cent(C)
core_extra = [t for t in weights if abs(t[0]) < 1e-45 and abs(t[2]) < 1e-45]
nzPi = [t for t in weights if not (abs(t[0]) < 1e-45 and abs(t[2]) < 1e-45)]
print("core extra weight-dims (w8=w16=0):", len(core_extra), " => dim z(Pi) =",
      len(zero_idx) + len(core_extra))
print("nonzero-Pi-weight dims:", len(nzPi))

# enhancement ratios r = -w8/w16
from collections import defaultdict
groups = defaultdict(list)
vals = []
for t in nzPi:
    if abs(t[2]) < 1e-45:
        key = "inf"
        groups[key].append(t)
        continue
    r = -t[0] / t[2]
    placed = False
    for k, (rv, lst) in enumerate(vals):
        if abs(r - rv) < 1e-40:
            lst.append(t)
            placed = True
            break
    if not placed:
        vals.append((r, [t]))
print("distinct finite ratios -w8/w16 on nonzero-Pi lines:", len(vals))
for rv, lst in sorted(vals, key=lambda p: (abs(mp.im(p[0])), mp.re(p[0]))):
    print("  r =", mp.nstr(rv, 30), " mult:", len(lst))

# the three 16-dim enhancement lines should be the ratios with mult 16
big = [(rv, lst) for rv, lst in vals if len(lst) == 16]
print("ratios with multiplicity 16:", len(big))
rs = [rv for rv, _ in big]
# minimal polynomial of each via PSLQ (degree 3 expected, real)
for rv in rs:
    assert abs(mp.im(rv)) < mp.mpf("1e-45")
    rr = mp.re(rv)
    rel = mp.pslq([mp.mpf(1), rr, rr**2, rr**3], maxcoeff=10**15, maxsteps=10**6)
    print("minpoly coeffs (c0,c1,c2,c3) for r =", mp.nstr(rr, 20), ":", rel)
