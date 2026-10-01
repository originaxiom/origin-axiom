#!/usr/bin/env python3
"""controls for relcup.py -- no background of the census is touched here"""
import sys, random, pathlib
REPO = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "frontier/B1434_the_architecture_census/verification"))
import architecture_census as ac
from relcup import *

def Phi_of(eps, word, k):
    phi = ac.monodromy(eps, word); P = ac.IDENT
    for _ in range(k): P = ac.compose(phi, P)
    return {X: P[ac.X], Y: P[ac.Y]}

p = 10007
# 1. the chain identity dC = z, on many monodromies (integer chains, no module)
for (eps, w, k) in [(1, "LR", 1), (1, "LR", 2), (1, "LR", 3), (1, "LR", 6), (-1, "LR", 1), (-1, "LR", 3), (1, "LLR", 2), (-1, "LLRLR", 1), (-1, "LLLRLR", 1), (1, "LLRR", 3)]:
    B = Bundle(Phi_of(eps, w, k)); C, z, sigma = B.fundamental()
    print("chain ok", eps, w, k, "cells of C:", len(C), "max word", max(len(g[0]) for cell in C for g in cell))
# identity monodromy
Bid = Bundle({X: (X,), Y: (Y,)}); C, z, sigma = Bid.fundamental(); print("identity: cells", len(C))

# 2. the product F x S^1, trivial coefficients: x* u y* u t* on the fundamental class must be +-1
one = [[1]]
V = Module(Bid, one, one, one, p)
xs = Cocycle(V, [1], [0], [0]); ys = Cocycle(V, [0], [1], [0]); ts = Cocycle(V, [0], [0], [1])
T = lambda u, v, w: u[0] * v[0] * w[0] % p
def Yv(B, C, z, a, b, h, T=T):
    e = relative_lift(a); assert e is not None, "a is not interior"
    return triple(B, C, z, a, b, h, T, e)
vals = {n: Yv(Bid, C, z, *abc) for n, abc in dict(xyt=(xs, ys, ts), yxt=(ys, xs, ts), xxt=(xs, xs, ts), xyx=(xs, ys, xs), xty=(xs, ts, ys)).items()}
print("product control:", {k: (v if v < p // 2 else v - p) for k, v in vals.items()})
assert vals["xyt"] in (1, p - 1) and (vals["xyt"] + vals["yxt"]) % p == 0 and vals["xxt"] == 0 and vals["xyx"] == 0

# 2b. the bite: the two-term chain [x|y] - [y|x] in place of sigma is not a relative cycle -- the instrument must refuse it
bad = Bid.norm({(Bid.F((X,)), Bid.F((Y,))): 1, (Bid.F((Y,)), Bid.F((X,))): -1})
print("two-term chain boundary (must be non-zero and not -[lam]):", Bid.boundary(bad))
assert Bid.boundary(bad) != {(Bid.F(Bid.lam),): -1}

# 3. the sign bundle: Phi = iota (-I), coefficients k_sigma (t -> -1): x*, y* are twisted interior classes
Bm = Bundle(Phi_of(-1, "LR", 1)) if False else Bundle({X: ac.IOTA[ac.X], Y: ac.IOTA[ac.Y]})
C2, z2, _ = Bm.fundamental()
Vs = Module(Bm, one, one, [[p - 1]], p); V1 = Module(Bm, one, one, one, p)
xs = Cocycle(Vs, [1], [0], [0]); ys = Cocycle(Vs, [0], [1], [0]); ts = Cocycle(V1, [0], [0], [1])
v = Yv(Bm, C2, z2, xs, ys, ts); w = Yv(Bm, C2, z2, ys, xs, ts)
print("sign-bundle control:", v if v < p // 2 else v - p, w if w < p // 2 else w - p)
assert v in (1, p - 1) and (v + w) % p == 0

# 4. invariance under coboundaries and under the choice of relative lift, on a twisted module over the product
#    (rank-2 unipotent on x; trivial on y, t) -- a module with invariants on P, so the lift is not unique
random.seed(1)
U = [[1, 1], [0, 1]]; I2 = [[1, 0], [0, 1]]
VU = Module(Bid, U, I2, I2, p)
# cocycles of the product with values in VU: f(t) = 0, f(y) arbitrary in ker(U-1)... build by solving the cocycle conditions
import itertools
def cocycles(V):
    """basis of Z^1(G;V) by brute linear algebra on (f(x), f(y), f(t))"""
    d = V.d; n = 3 * d; rows = []
    basis = []
    for i in range(n):
        vec = [0] * n; vec[i] = 1
        basis.append(vec)
    # condition is linear: residual(vec) = 0
    def resid(vec):
        fx, fy, ft = vec[:d], vec[d:2 * d], vec[2 * d:]
        c = Cocycle(V, fx, fy, ft, check=False); out = []
        for g in (X, Y):
            lhs = [(a + b - cc) % V.p for a, b, cc in zip(c.vt, mvec(V.Mt, c.v[g], V.p), mvec(V.rhoF(V.B.Phi[g]), c.vt, V.p))]
            out += [(l - r) % V.p for l, r in zip(lhs, c.onF(V.B.Phi[g]))]
        return out
    Mrows = list(zip(*[resid(b) for b in basis]))            # rows: conditions, cols: coordinates
    sys.path.insert(0, str(REPO / "frontier/B1427_the_towers_generation_count_verified/verification"))
    from myindex import rank_and_null
    rk, NS = rank_and_null([list(r) for r in Mrows], n, V.p, want_null=True)
    return [Cocycle(V, v[:d], v[d:2 * d], v[2 * d:]) for v in NS]
Z = cocycles(VU); print("dim Z^1(product; unipotent) =", len(Z))
eps2 = lambda u, v, w: (u[0] * v[1] - u[1] * v[0]) * w[0] % p
from myindex import rank_and_null
def interior_combos(V, Z):
    """coefficient vectors c with sum c_i Z_i restricting to a coboundary on P"""
    d = V.d; lam = (V.B.lam, 0); I = eye(d)
    A1 = [[(V.Mt[i][j] - I[i][j]) % p for j in range(d)] for i in range(d)]
    Rl = V.rho(lam); A2 = [[(Rl[i][j] - I[i][j]) % p for j in range(d)] for i in range(d)]
    cols = [zc(V.B.T) + zc(lam) for zc in Z] + [[(-(A1 + A2)[i][j]) % p for i in range(2 * d)] for j in range(d)]
    rows = [list(r) for r in zip(*cols)]
    rk, NS = rank_and_null(rows, len(cols), p, want_null=True)
    return [v[:len(Z)] for v in NS if any(v[:len(Z)])]
def comb(V, Z, cs):
    d = V.d
    fx = [sum(c * zc.v[X][i] for c, zc in zip(cs, Z)) % p for i in range(d)]
    fy = [sum(c * zc.v[Y][i] for c, zc in zip(cs, Z)) % p for i in range(d)]
    ft = [sum(c * zc.vt[i] for c, zc in zip(cs, Z)) % p for i in range(d)]
    return Cocycle(V, fx, fy, ft)
IC = interior_combos(VU, Z); print("interior cocycles (dim of the span):", len(IC))
ok = 0; tested = 0; nonzero = 0
Vone = Module(Bid, one, one, one, p)
for trial in range(40):
    ca = [sum(random.randrange(p) * v[i] for v in IC) % p for i in range(len(Z))]
    cb = [sum(random.randrange(p) * v[i] for v in IC) % p for i in range(len(Z))]
    a, b = comb(VU, Z, ca), comb(VU, Z, cb)
    ea = relative_lift(a); assert ea is not None and relative_lift(b) is not None
    tested += 1
    h = Cocycle(Vone, [random.randrange(p)], [random.randrange(p)], [random.randrange(p)])
    y0 = triple(Bid, C, z, a, b, h, eps2, ea)
    y1 = triple(Bid, C, z, a, b, h, eps2, [(ea[0] + 5) % p, (ea[1] + 11) % p])      # P acts trivially: any vector is invariant
    va = [random.randrange(p), random.randrange(p)]; vb = [random.randrange(p), random.randrange(p)]
    a2 = a.plus_coboundary(va); b2 = b.plus_coboundary(vb); h2 = h.plus_coboundary([random.randrange(p)])
    y2 = triple(Bid, C, z, a2, b2, h2, eps2, relative_lift(a2))
    ok += (y0 == y1 == y2); nonzero += (y0 != 0)
print("invariance (lift, coboundaries) on interior pairs:", ok, "of", tested, "; non-zero values:", nonzero)
assert ok == tested and tested > 0 and nonzero > 0
# 4b. the bite: with b NOT interior the value must depend on the lift (so the invariance above is not vacuous)
dep = 0
for trial in range(20):
    ca = [sum(random.randrange(p) * v[i] for v in IC) % p for i in range(len(Z))]
    a = comb(VU, Z, ca); b = comb(VU, Z, [random.randrange(p) for _ in Z])
    h = Cocycle(Vone, [random.randrange(p)], [random.randrange(p)], [random.randrange(p)])
    ea = relative_lift(a)
    dep += triple(Bid, C, z, a, b, h, eps2, ea) != triple(Bid, C, z, a, b, h, eps2, [(ea[0] + 5) % p, (ea[1] + 11) % p])
print("lift-dependence when b is not interior:", dep, "of 20 (must be > 0)")
assert dep > 0
print("ALL CONTROLS PASS")
