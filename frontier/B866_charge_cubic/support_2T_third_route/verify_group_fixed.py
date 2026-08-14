#!/usr/bin/env python3
"""B858 verification -- an INDEPENDENT third route to dim Cent(2T) and its bracket structure.

nonprincipal_2T.py gets Cent(2T) two ways that share the sl2-decomposition:
  (a) character theory on the ad(h)-spectrum,
  (b) explicit 2T-invariant binary forms transported into e6 by ad(f)^k.
This script uses NEITHER.  It builds the actual group elements rho(g) in Aut(e6) -- factoring
each generator of 2T into elementary matrices over Q(i) and exponentiating ad(e), ad(f) -- and
takes the honest fixed-point space {x : rho(g) x = x for the generators}.  Over Q, because
rho(g) = A + iB and invariance of a rational vector is (A-I)x = 0 AND Bx = 0.

Run on the principal orbit (must reproduce B854: dim 4, abelian) and on the two orbits the
main script flags as su(2)+u(1), plus the su(3)+su(2) orbit.
"""
from fractions import Fraction as F
from itertools import product
import random
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

C = [[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
     [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]]
N = 6


def ip(a, b):
    return sum(a[i] * b[j] * C[i][j] for i in range(N) for j in range(N))


pos = [tuple(a) for a in product(range(4), repeat=N) if any(a) and ip(a, a) == 2]
ROOTS = pos + [tuple(-x for x in a) for a in pos]
IDX = {r: k for k, r in enumerate(ROOTS)}
DIM = N + len(ROOTS)
E0 = [[(-1 if i == j else ((-1) ** C[i][j] if i < j else 1)) for j in range(N)] for i in range(N)]


def eps(a, b):
    s = 1
    for i in range(N):
        if a[i] == 0:
            continue
        for j in range(N):
            if b[j] == 0:
                continue
            if E0[i][j] == -1 and (a[i] * b[j]) % 2:
                s = -s
    return s


def bracket_basis(p, q):
    if p < N and q < N:
        return {}
    if p < N:
        b = ROOTS[q - N]
        c = sum(b[j] * C[p][j] for j in range(N))
        return {q: F(c)} if c else {}
    if q < N:
        a = ROOTS[p - N]
        c = -sum(a[j] * C[q][j] for j in range(N))
        return {p: F(c)} if c else {}
    a, b = ROOTS[p - N], ROOTS[q - N]
    s = tuple(a[i] + b[i] for i in range(N))
    if not any(s):
        sg = eps(a, tuple(-v for v in a))
        return {i: F(sg * a[i]) for i in range(N) if a[i]}
    if s in IDX:
        return {N + IDX[s]: F(eps(a, b))}
    return {}


BB = [[bracket_basis(p, q) for q in range(DIM)] for p in range(DIM)]


def br(u, v):
    out = {}
    for p, up in u.items():
        row = BB[p]
        for q, vq in v.items():
            c = up * vq
            for k, rk in row[q].items():
                w = out.get(k, 0) + c * rk
                if w:
                    out[k] = w
                elif k in out:
                    del out[k]
    return out


def bvec(k):
    return {k: F(1)}


def addv(u, v):
    out = dict(u)
    for k, x in v.items():
        w = out.get(k, 0) + x
        if w:
            out[k] = w
        elif k in out:
            del out[k]
    return out


def smul(c, u):
    return {k: c * x for k, x in u.items()} if c else {}


def rref(rows, ncol):
    rows = [r[:] for r in rows]
    m = len(rows)
    piv = []
    r = 0
    for col in range(ncol):
        pr = None
        for k in range(r, m):
            if rows[k][col] != 0:
                pr = k
                break
        if pr is None:
            continue
        rows[r], rows[pr] = rows[pr], rows[r]
        iv = F(1) / rows[r][col]
        rows[r] = [x * iv for x in rows[r]]
        for k in range(m):
            if k != r and rows[k][col] != 0:
                fq = rows[k][col]
                rows[k] = [a - fq * b for a, b in zip(rows[k], rows[r])]
        piv.append(col)
        r += 1
        if r == m:
            break
    return rows[:r], piv


def nullspace(rows, ncol):
    R, piv = rref(rows, ncol)
    free = [c for c in range(ncol) if c not in piv]
    out = []
    for fc in free:
        v = [F(0)] * ncol
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][fc]
        out.append(v)
    return out


def rank_of(vecs):
    rows = []
    for v in vecs:
        r = [F(0)] * DIM
        for k, x in v.items():
            r[k] = x
        rows.append(r)
    return len(rref(rows, DIM)[0]) if rows else 0


def solve(cols, b, ncol):
    rows = [[cols[j].get(i, F(0)) for j in range(ncol)] + [b.get(i, F(0))] for i in range(DIM)]
    R, piv = rref(rows, ncol + 1)
    if ncol in piv:
        return None
    x = [F(0)] * ncol
    for i, pc in enumerate(piv):
        x[pc] = R[i][ncol]
    return x


def cartan_inverse():
    M = [[F(C[i][j]) for j in range(N)] + [F(1) if i == k else F(0) for k in range(N)]
         for i in range(N)]
    R, piv = rref(M, 2 * N)
    return [[R[i][N + j] for j in range(N)] for i in range(N)]


CINV = cartan_inverse()


def triple(L):
    g2 = [r for r in ROOTS if sum(r[i] * L[i] for i in range(N)) == 2]
    gm2 = [r for r in ROOTS if sum(r[i] * L[i] for i in range(N)) == -2]
    u = [sum(CINV[i][j] * L[j] for j in range(N)) for i in range(N)]
    H = {i: u[i] for i in range(N) if u[i]}
    rnd = random.Random(5)
    for _ in range(12):
        e = {N + IDX[r]: F(rnd.randint(1, 9)) for r in g2}
        x = solve([br(e, bvec(N + IDX[r])) for r in gm2], H, len(gm2))
        if x is None:
            continue
        f = {N + IDX[r]: x[j] for j, r in enumerate(gm2) if x[j]}
        if br(e, f) == H and br(H, e) == smul(F(2), e) and br(H, f) == smul(F(-2), f):
            return H, e, f
    raise RuntimeError("no triple")


# ---------------- Gaussian-rational vectors: dict {index: (re, im)} ----------------
def gadd(u, v):
    out = dict(u)
    for k, (a, b) in v.items():
        p, q = out.get(k, (F(0), F(0)))
        p, q = p + a, q + b
        if p or q:
            out[k] = (p, q)
        elif k in out:
            del out[k]
    return out


def gscale(c, u):
    cr, ci = c
    out = {}
    for k, (a, b) in u.items():
        p, q = a * cr - b * ci, a * ci + b * cr
        if p or q:
            out[k] = (p, q)
    return out


def gbr(X, u):
    """[X, u] with X a rational sparse vector, u Gaussian-rational."""
    out = {}
    for p, xp in X.items():
        row = BB[p]
        for q, (a, b) in u.items():
            for k, rk in row[q].items():
                c = xp * rk
                pr, pi = out.get(k, (F(0), F(0)))
                pr, pi = pr + c * a, pi + c * b
                if pr or pi:
                    out[k] = (pr, pi)
                elif k in out:
                    del out[k]
    return out


def expad(X, t, u):
    """exp(t ad X) u, X ad-nilpotent, t Gaussian rational."""
    term = dict(u)
    acc = dict(u)
    n = 1
    while term:
        term = gscale(t, gbr(X, term))
        term = {k: (a / n, b / n) for k, (a, b) in term.items()}
        acc = gadd(acc, term)
        n += 1
        if n > 60:
            raise RuntimeError("not nilpotent")
    return acc


def cmulq(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cinv(a):
    d = a[0] * a[0] + a[1] * a[1]
    return (a[0] / d, -a[1] / d)


def factor_sl2(M):
    """[[a,b],[c,d]] -> list of ('U'|'L', t) with M = product in order.
       U(x)L(c)U(y) = [[1+xc, b],[c, d]] with x=(a-1)/c, y=(d-1)/c (uses ad-bc=1)."""
    a, b, c, d = M
    if c == (F(0), F(0)):
        # M = (M . L(1)) . L(-1) ;   M.L(1) = [[a+b, b],[c+d, d]]
        Mp = ((a[0] + b[0], a[1] + b[1]), b, (c[0] + d[0], c[1] + d[1]), d)
        return factor_sl2(Mp) + [("L", (F(-1), F(0)))]
    ci = cinv(c)
    x = cmulq((a[0] - 1, a[1]), ci)
    y = cmulq((d[0] - 1, d[1]), ci)
    return [("U", x), ("L", c), ("U", y)]


def caddq(u, v):
    return (u[0] + v[0], u[1] + v[1])


def mm(P, Q):
    return (caddq(cmulq(P[0], Q[0]), cmulq(P[1], Q[2])),
            caddq(cmulq(P[0], Q[1]), cmulq(P[1], Q[3])),
            caddq(cmulq(P[2], Q[0]), cmulq(P[3], Q[2])),
            caddq(cmulq(P[2], Q[1]), cmulq(P[3], Q[3])))


GENS = [((F(0), F(1)), (F(0), F(0)), (F(0), F(0)), (F(0), F(-1))),                 # i
        ((F(1, 2), F(1, 2)), (F(1, 2), F(1, 2)), (F(-1, 2), F(1, 2)), (F(1, 2), F(-1, 2)))]

ALL_TARGETS = {"222222 principal (B854 control)": (2, 2, 2, 2, 2, 2),
               "121011 D5(a1)": (1, 2, 1, 0, 1, 1),
               "001010 A2+2A1": (0, 0, 1, 0, 1, 0),
               "000100 3A1": (0, 0, 0, 1, 0, 0),
               "020000 A2": (0, 2, 0, 0, 0, 0),
               "020200 D4": (0, 2, 0, 2, 0, 0),
               "010000 A1 minimal": (0, 1, 0, 0, 0, 0)}
if len(sys.argv) > 1:
    TARGETS = {k: v for k, v in ALL_TARGETS.items() if k.split()[0] in sys.argv[1:]}
else:
    TARGETS = ALL_TARGETS

P = 2147483647          # 2^31 - 1


def independent_basis(vecs):
    rows, keep = [], []
    for v in vecs:
        r = [F(0)] * DIM
        for k, x in v.items():
            r[k] = x
        cand = rows + [r]
        if len(rref(cand, DIM)[0]) > len(rows):
            rows = cand
            keep.append(v)
    return keep


def coords_in(basis):
    k = len(basis)
    rows, chosen = [], []
    for i in range(DIM):
        r = [b.get(i, F(0)) for b in basis]
        if len(rref(rows + [r], k)[0]) > len(rows):
            rows.append(r)
            chosen.append(i)
        if len(chosen) == k:
            break
    aug = [rows[i][:] + [F(1) if i == j else F(0) for j in range(k)] for i in range(k)]
    R, _ = rref(aug, 2 * k)
    inv = [[R[i][k + j] for j in range(k)] for i in range(k)]

    def fn(v):
        b = [v.get(i, F(0)) for i in chosen]
        return [sum(inv[i][j] * b[j] for j in range(k)) for i in range(k)]
    return fn


def n_invariant_forms_modp(ssb, nx=None):
    """#simple ideals of a semisimple ss = dim of its space of invariant symmetric forms.
    Computed mod p: nullity_p >= nullity_Q, so this is a rigorous UPPER bound."""
    n = len(ssb)
    co = coords_in(ssb)
    A = [[[int(c.numerator) * pow(int(c.denominator), P - 2, P) % P for c in co(br(ssb[x], ssb[j]))]
          for j in range(n)] for x in range(n)]
    pairs = [(a, b) for a in range(n) for b in range(a, n)]
    pidx = {q: i for i, q in enumerate(pairs)}
    m = len(pairs)
    rows = []
    import random as _rd
    xs = range(n) if nx is None else _rd.Random(3).sample(range(n), min(nx, n))
    for x in xs:
        Ax = A[x]
        for (a, b) in pairs:
            row = [0] * m
            for i in range(n):
                if Ax[a][i]:
                    row[pidx[(min(i, b), max(i, b))]] = (row[pidx[(min(i, b), max(i, b))]]
                                                         + Ax[a][i]) % P
                if Ax[b][i]:
                    row[pidx[(min(a, i), max(a, i))]] = (row[pidx[(min(a, i), max(a, i))]]
                                                         + Ax[b][i]) % P
            if any(row):
                rows.append(row)
    r = 0
    for col in range(m):
        pr = next((k for k in range(r, len(rows)) if rows[k][col]), None)
        if pr is None:
            continue
        rows[r], rows[pr] = rows[pr], rows[r]
        iv = pow(rows[r][col], P - 2, P)
        rows[r] = [x * iv % P for x in rows[r]]
        pivrow = rows[r]
        for k in range(len(rows)):
            if k != r and rows[k][col]:
                fq = rows[k][col]
                rows[k] = [(a - fq * b) % P for a, b in zip(rows[k], pivrow)]
        r += 1
        if r == len(rows):
            break
    return m - r

for name, L in TARGETS.items():
    H, e, f = triple(list(L))
    mats = []
    for M in GENS:
        fac = factor_sl2(M)
        # verify the factorization reproduces M
        acc = ((F(1), F(0)), (F(0), F(0)), (F(0), F(0)), (F(1), F(0)))
        for kind, t in fac:
            E = (((F(1), F(0)), t, (F(0), F(0)), (F(1), F(0))) if kind == "U"
                 else ((F(1), F(0)), (F(0), F(0)), t, (F(1), F(0))))
            acc = mm(acc, E)
        assert acc == M, (name, acc, M)
        cols = []
        for j in range(DIM):
            v = {j: (F(1), F(0))}
            for kind, t in fac:
                v = expad(e if kind == "U" else f, t, v)
            cols.append(v)
        mats.append(cols)
    rows = []
    for cols in mats:
        for i in range(DIM):
            rows.append([cols[j].get(i, (F(0), F(0)))[0] - (F(1) if i == j else F(0))
                         for j in range(DIM)])
            rows.append([cols[j].get(i, (F(0), F(0)))[1] for j in range(DIM)])
    ns = nullspace(rows, DIM)
    Cb = [{k: w[k] for k in range(DIM) if w[k]} for w in ns]
    brs = [br(Cb[i], Cb[j]) for i in range(len(Cb)) for j in range(i + 1, len(Cb))]
    brs = [x for x in brs if x]
    dd = rank_of(brs)
    extra = ""
    if dd and dd == len(Cb):
        ssb = independent_basis(brs)
        extra = f"   #simple ideals of [C,C] <= {n_invariant_forms_modp(ssb, 4 if len(ssb) > 20 else None)}"
    print(f"{name:<32} dim Cent(2T) = {len(Cb):>2}   dim [C,C] = {dd:>2}   "
          f"{'ABELIAN' if dd == 0 else 'NON-ABELIAN'}{extra}", flush=True)
