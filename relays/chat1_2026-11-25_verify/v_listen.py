#!/usr/bin/env python3
"""V-LISTEN (chat1, 2026-11-25, evening; data-free): an independent recomputation of the exact claims of main's B1980,
B1983-B1986, B1988, B1990, B1991, B1993, B1994 and B1997, on the seat's own code. Nothing from main is imported; main's
claims were read (arc_verdict.json directly, FINDINGS through the mask) before this was written, so the checks are not
blind to the values, only independent of main's code.

Conventions (written here before computing; B1988's are the same up to naming): readings (x, y, z) = (tr a, tr b, tr ab);
L: (a, b) -> (a, ab) gives L(x, y, z) = (x, z, xz - y); R: (a, b) -> (ab, b) gives R(x, y, z) = (z, y, yz - x);
kappa = x^2 + y^2 + z^2 - xyz - 2 = tr[a, b]; the cusp's leaf is kappa = -2, i.e. x^2 + y^2 + z^2 = xyz; the common
point is (0, 0, 0); 'nothing' is (2, 2, 2). Orbits are those of the group <L, R> (finite sets: forward closure suffices).

CONDITION (each item passes or fails on its own; no item is re-run with a changed rule):
 C0  the trace identity: on 20 random SL(2, C) pairs, L and R as written reproduce (tr a, tr ab, tr a.ab) and
     (tr ab, tr b, tr ab.b) to 1e-9.
 C1  (B1988) over Q-bar the points fixed by both L and R are exactly (0,0,0) and (2,2,2); over F_p, every prime p <= 47,
     exactly those two mod p.
 C2  (B1983/B1990) for every prime 5 <= p <= 47 the cusp's leaf mod p has p^2 + 3(-1/p)p + 1 points and its nonzero
     points form ONE orbit of <L, R>; at p = 3 the leaf mod 3 is the common point alone.
 C3  (B1990) for every prime 5 <= p <= 47 and every kappa mod p: the leaf's count minus (p^2 + 1), divided by p, is an
     integer in {-4, -2, 0, 2, 4}, except the cusp (kappa = -2), where it is 3(-1/p); 'nothing' (kappa = 2) gives 0.
 C4  (B1984/B1986/B1991) the linear parts dL, dR at the common point generate a group of order 24 in SO(3) (signed
     permutation matrices of determinant 1); mod 9 the 27 points over the common point split into orbits 1, 6, 8, 12;
     mod 2 the linear parts generate S3 (order 6). The 3-dimensional block of dL + dR has eigenvalues 1 and
     (1 +- i sqrt 7)/2 (modulus sqrt 2).
 C5  (B1993) integer solutions of x^2 + y^2 + z^2 = xyz with max |entry| <= 3000: all entries = 0 mod 3; the nonzero
     ones fall into exactly two <L, R>-classes when connectivity is read inside the box (edges L, R and inverses between
     points both in the box): the all-positive class containing (3,3,3), and one class containing all three two-negative
     sign patterns. (Inside-the-box connectivity can only split a true orbit, never merge two; so "two" is an upper bound
     on the true count of orbits meeting the box, and the positive class is closed under the moves exactly.)
 C6  (B1994) R^-1 o L (first L, then R^-1) acts as (x, y, z) -> (y, z, x), symbolically.
 C7  (B1997) on the cusp's leaf mod 81, among points = (0,0,0) mod 3, the largest <L, R>-orbit; W+ = P_L + P_R
     (permutation matrices). Its exact characteristic polynomial over Z has x^12 - 3x^10 + 3x^8 - 21x^6 + 12x^4 - 48x^2 + 64
     as an irreducible factor; the largest-modulus eigenvalue other than +-2 is real, 1.915298 to 6 decimals, and is a
     root of that factor; sqrt(w + sqrt(w^2 - 4)), w = (1 + 4 cos(pi/9))/2, has that factor as its minimal polynomial.
 C8  (B1980) M = [[2,1],[1,1]] has order 60 in SL(2, Z/30) and also in SL(2, Z/30)/{+-1}; no power M^k, 1 <= k <= 59, has
     trace = 0, 1 or -1 mod 30 (a necessary condition for M^k to fix a point of X(30) off the cusps).

Reading: report PASS/FAIL per item; the summary line counts passes. A FAIL is reported to main as a discrepancy, with
the seat's convention named, before any re-reading.

    python3 -B v_listen.py > v_listen_out.txt        (about one to three minutes)
"""
import random, cmath, itertools, sys
from math import isqrt
import sympy as sp

def L(p, m=None):
    x, y, z = p
    r = (x, z, x * z - y)
    return tuple(v % m for v in r) if m else r

def R(p, m=None):
    x, y, z = p
    r = (z, y, y * z - x)
    return tuple(v % m for v in r) if m else r

def Linv(p):  # L(x,y,z) = (x, z, xz - y)  =>  inverse (X, Y, Z) -> (X, XY - Z, Y)
    X, Y, Z = p
    return (X, X * Y - Z, Y)

def Rinv(p):  # R(x,y,z) = (z, y, yz - x)  =>  inverse (X, Y, Z) -> (XY - Z, Y, X)
    X, Y, Z = p
    return (X * Y - Z, Y, X)

def primes(n):
    return [q for q in range(2, n + 1) if all(q % d for d in range(2, isqrt(q) + 1))]

def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

def orbits(points, m):
    pts, seen, out = set(points), set(), []
    for s in sorted(pts):
        if s in seen:
            continue
        comp, stack = {s}, [s]
        while stack:
            q = stack.pop()
            for nb in (L(q, m), R(q, m)):
                if nb not in comp:
                    comp.add(nb); stack.append(nb)
        assert comp <= pts
        seen |= comp
        out.append(comp)
    return out

res = {}

# C0
random.seed(1)
def rnd_sl2():
    a, b, c = (complex(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(3))
    return [[a, b], [c, (1 + b * c) / a]]
def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
tr = lambda A: A[0][0] + A[1][1]
err = 0
for _ in range(20):
    A, B = rnd_sl2(), rnd_sl2()
    p = (tr(A), tr(B), tr(mul(A, B)))
    err = max(err, max(abs(u - v) for u, v in zip(L(p), (tr(A), tr(mul(A, B)), tr(mul(A, mul(A, B)))))))
    err = max(err, max(abs(u - v) for u, v in zip(R(p), (tr(mul(A, B)), tr(B), tr(mul(mul(A, B), B))))))
res["C0"] = err < 1e-9
print("C0 trace identity, max error %.1e -> %s" % (err, res["C0"]))

# C1
X, Y, Z = sp.symbols("X Y Z")
eqs = [a - b for a, b in zip(L((X, Y, Z)), (X, Y, Z))] + [a - b for a, b in zip(R((X, Y, Z)), (X, Y, Z))]
sol = sp.solve(eqs, [X, Y, Z], dict=True)
qbar = sorted({(s[X], s[Y], s[Z]) for s in sol})
okp = all(sorted(q for q in itertools.product(range(p), repeat=3) if L(q, p) == q and R(q, p) == q)
          == sorted({(0, 0, 0), (2 % p, 2 % p, 2 % p)}) for p in primes(47))
res["C1"] = qbar == [(0, 0, 0), (2, 2, 2)] and okp
print("C1 common fixed points over Q-bar %s; over F_p (p <= 47) exactly the two: %s -> %s" % (qbar, okp, res["C1"]))

# C2, C3
c2, c3 = True, True
for p in primes(47):
    counts = {}
    leaf = []
    for q in itertools.product(range(p), repeat=3):
        x, y, z = q
        k = (x * x + y * y + z * z - x * y * z - 2) % p
        counts[k] = counts.get(k, 0) + 1
        if k == (-2) % p:
            leaf.append(q)
    if p == 3:
        c2 &= leaf == [(0, 0, 0)]
        print("C2 p = 3: the leaf is %s" % leaf)
        continue
    if p == 2:
        continue
    want = p * p + 3 * legendre(-1, p) * p + 1
    orb = orbits([q for q in leaf if q != (0, 0, 0)], p)
    ok2 = len(leaf) == want and len(orb) == 1
    c2 &= ok2
    for k in range(p):
        d, r = divmod(counts.get(k, 0) - (p * p + 1), p)
        if k == (-2) % p:
            ok3 = r == 0 and d == 3 * legendre(-1, p)
        elif k == 2 % p:
            ok3 = r == 0 and d == 0
        else:
            ok3 = r == 0 and d in (-4, -2, 0, 2, 4)
        if not ok3:
            print("C3 p = %d kappa = %d: count %d" % (p, k, counts.get(k, 0)))
        c3 &= ok3
    print("C2 p = %2d: leaf %4d points (formula %4d), nonzero orbits %d" % (p, len(leaf), want, len(orb)))
res["C2"], res["C3"] = c2, c3
print("C2 -> %s; C3 -> %s" % (c2, c3))

# C4
dL = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
dR = sp.Matrix([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
assert dL == sp.Matrix([[sp.diff(e, v).subs({X: 0, Y: 0, Z: 0}) for v in (X, Y, Z)] for e in L((X, Y, Z))])
assert dR == sp.Matrix([[sp.diff(e, v).subs({X: 0, Y: 0, Z: 0}) for v in (X, Y, Z)] for e in R((X, Y, Z))])
def gen_group(gens, red=lambda M: M):
    G, frontier = {tuple(red(sp.eye(3)))}, [red(sp.eye(3))]
    while frontier:
        M = frontier.pop()
        for g in gens:
            N = red(g * M)
            t = tuple(N)
            if t not in G:
                G.add(t); frontier.append(N)
    return G
G = gen_group([dL, dR])
signed_perm = all(sorted(abs(v) for v in g) == [0] * 6 + [1] * 3 for g in G) and all(sp.Matrix(3, 3, list(g)).det() == 1 for g in G)
G2 = gen_group([dL, dR], red=lambda M: M.applyfunc(lambda v: v % 2))
mod9 = [q for q in itertools.product(range(0, 9, 3), repeat=3)]
assert all((x * x + y * y + z * z - x * y * z) % 9 == 0 for x, y, z in mod9)
o9 = sorted(len(o) for o in orbits(mod9, 9))
ev = sp.Matrix(dL + dR).eigenvals()
evs = sorted(ev, key=lambda e: (sp.re(e), sp.im(e)))
want_ev = sorted([sp.Integer(1), (1 + sp.I * sp.sqrt(7)) / 2, (1 - sp.I * sp.sqrt(7)) / 2], key=lambda e: (sp.re(e), sp.im(e)))
okev = all(sp.simplify(a - b) == 0 for a, b in zip(evs, want_ev))
res["C4"] = len(G) == 24 and signed_perm and o9 == [1, 6, 8, 12] and len(G2) == 6 and okev
print("C4 |<dL, dR>| = %d (signed permutations, det 1: %s); mod 9 orbits %s; mod 2 group order %d; eigenvalues of dL + dR %s -> %s"
      % (len(G), signed_perm, o9, len(G2), evs, res["C4"]))

# C5
import numpy as np
N = 3000
sols = {(0, 0, 0)}
ys = np.arange(-N, N + 1, dtype=np.int64)
for x in range(-N, N + 1):
    D = x * x * ys * ys - 4 * (x * x + ys * ys)       # <= 8.1e13 < 2^53: exact in int64 and float64
    cand_y = ys[D >= 0]
    Dp = D[D >= 0]
    s = np.rint(np.sqrt(Dp.astype(np.float64))).astype(np.int64)
    for y, d, r in zip(cand_y.tolist(), Dp.tolist(), s.tolist()):
        r = next((t for t in (r - 1, r, r + 1) if t >= 0 and t * t == d), None)
        if r is None:
            continue
        for z in {(x * y + r) // 2, (x * y - r) // 2}:
            if abs(z) <= N and x * x + y * y + z * z == x * y * z:
                sols.add((x, y, z))
nz = sorted(q for q in sols if q != (0, 0, 0))
all3 = all(v % 3 == 0 for q in nz for v in q)
inbox = set(nz)
seen, classes = set(), []
for s in nz:
    if s in seen:
        continue
    comp, stack = {s}, [s]
    while stack:
        q = stack.pop()
        for nb in (L(q), R(q), Linv(q), Rinv(q)):
            if nb in inbox and nb not in comp:
                comp.add(nb); stack.append(nb)
    seen |= comp
    classes.append(comp)
sig = lambda q: tuple(1 if v > 0 else -1 for v in q)
pats = [sorted({sig(q) for q in c}) for c in classes]
pos_closed = all(min(L(q)) > 0 and min(R(q)) > 0 for q in nz if min(q) > 0)
res["C5"] = all3 and len(classes) == 2 and sorted(map(len, pats)) == [1, 3] and pos_closed \
    and [(1, 1, 1)] in pats and (3, 3, 3) in next(c for c in classes if (3, 3, 3) in c)
print("C5 %d nonzero integer readings (max |entry| <= %d); all = 0 mod 3: %s; classes %d with sign patterns %s; "
      "positives closed under L, R: %s -> %s" % (len(nz), N, all3, len(classes), pats, pos_closed, res["C5"]))

# C6
cyc = Rinv(L((X, Y, Z)))
res["C6"] = tuple(sp.expand(e) for e in cyc) == (Y, Z, X)
print("C6 R^-1(L(x, y, z)) = %s -> %s" % (tuple(sp.expand(e) for e in cyc), res["C6"]))

# C7
m = 81
over = [q for q in itertools.product(range(0, m, 3), repeat=3) if (q[0] ** 2 + q[1] ** 2 + q[2] ** 2 - q[0] * q[1] * q[2]) % m == 0]
orbs = sorted(orbits(over, m), key=len, reverse=True)
big = sorted(orbs[0])
idx = {q: i for i, q in enumerate(big)}
n = len(big)
from flint import fmpz_mat, fmpz_poly
W = [[0] * n for _ in range(n)]
for q in big:
    W[idx[q]][idx[L(q, m)]] += 1
    W[idx[q]][idx[R(q, m)]] += 1
cp = fmpz_mat(W).charpoly()
target = fmpz_poly([64, 0, -48, 0, 12, 0, -21, 0, 3, 0, -3, 0, 1])
fac = cp.factor()[1]
has = any(f == target and True for f, e in fac)
import numpy as np
eig = np.linalg.eigvals(np.array(W, dtype=float))
cand = sorted((e for e in eig if abs(abs(e) - 2) > 1e-6), key=lambda e: -abs(e))
lam = cand[0]
tx = sp.Symbol("t")
tpoly = sp.Poly(tx ** 12 - 3 * tx ** 10 + 3 * tx ** 8 - 21 * tx ** 6 + 12 * tx ** 4 - 48 * tx ** 2 + 64, tx)
root_ok = abs(complex(tpoly.eval(sp.Float(lam.real, 30)))) < 1e-6 * max(1, abs(lam) ** 12) and abs(lam.imag) < 1e-9
w = (1 + 4 * sp.cos(sp.pi / 9)) / 2
cf = sp.sqrt(w + sp.sqrt(w ** 2 - 4))
mp_ = sp.minimal_polynomial(cf, tx)
cf_ok = sp.Poly(mp_, tx) == tpoly and abs(float(cf) - abs(lam.real)) < 1e-9
irr = sp.Poly(tpoly).is_irreducible
res["C7"] = has and irr and root_ok and cf_ok and abs(abs(lam.real) - 1.915298) < 5e-7
print("C7 mod 81: %d points over the common point, orbit sizes %s; W+ is %d x %d; factor present and irreducible: %s, %s; "
      "slowest non-undamped eigenvalue %.12f%+.1ei (root: %s); closed form %.12f with that minimal polynomial: %s -> %s"
      % (len(over), [len(o) for o in orbs], n, n, has, irr, lam.real, lam.imag, root_ok, float(cf), cf_ok, res["C7"]))

# C8
def mm(A, B, q):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % q, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % q],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % q, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % q]]
M, P, I, mI = [[2, 1], [1, 1]], [[1, 0], [0, 1]], [[1, 0], [0, 1]], [[29, 0], [0, 29]]
order = order_pm = None
bad = []
for k in range(1, 61):
    P = mm(P, M, 30)
    if order_pm is None and (P == I or P == mI):
        order_pm = k
    if order is None and P == I:
        order = k
    if k < 60 and (P[0][0] + P[1][1]) % 30 in (0, 1, 29):
        bad.append(k)
res["C8"] = order == 60 and order_pm == 60 and not bad
print("C8 order of M mod 30: %s; modulo +-1: %s; powers with trace 0, +-1 mod 30: %s -> %s" % (order, order_pm, bad, res["C8"]))

print("SUMMARY: %d of %d items pass: %s" % (sum(res.values()), len(res), res))
