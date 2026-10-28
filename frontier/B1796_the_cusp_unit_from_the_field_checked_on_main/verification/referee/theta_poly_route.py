"""Referee B1796 -- W123 by a route independent of the free-module theorem and of B1691's code.
F (weight k = d - 3/2 for rho_R)  <->  G = theta2 theta3 theta4 * F = 2 eta^3 F, a vector of weight d whose components are
in M_d(Gamma(4)) = C[a, b, c]_d / (b^2 - a^2 - c^2), a = th2^2, b = th3^2, c = th4^2 (Jacobi).  G obeys the laws of
u' = (-a, -c, i b) (= 2 eta^3 R):  G(T tau) = M_T G,  G(S tau) = -i tau^d M_S G  (M_S the 0<->1 swap), and on the ring
a(T) = i a, b(T) = c, c(T) = b;  (a, b, c)(S) = (-i tau)(c, b, a).
Every holomorphic G has line orders >= (2, 0, 4) automatically (residues 2, 0, 4 mod 8), i.e. F >= (1, -1, 3): so the
equivariant space with no order condition IS the Lambda-module, and its dimension tests the free module's completeness.
d(m) at weight 3/2 + 12N:  orders of F's lines >= (1,7,3) + 8(N - m)  <->  G's lines >= that + 1.
    python3 -B theta_poly_route.py"""
import itertools
from fractions import Fraction as Fr


class Gi:
    """Q(i) element (re, im) with Fractions"""
    __slots__ = ("r", "i")
    def __init__(self, r=0, i=0): self.r, self.i = Fr(r), Fr(i)
    def __add__(s, o): o = cg(o); return Gi(s.r + o.r, s.i + o.i)
    __radd__ = __add__
    def __sub__(s, o): o = cg(o); return Gi(s.r - o.r, s.i - o.i)
    def __rsub__(s, o): return cg(o) - s
    def __neg__(s): return Gi(-s.r, -s.i)
    def __mul__(s, o): o = cg(o); return Gi(s.r * o.r - s.i * o.i, s.r * o.i + s.i * o.r)
    __rmul__ = __mul__
    def __truediv__(s, o):
        o = cg(o); n = o.r * o.r + o.i * o.i
        return s * Gi(o.r / n, -o.i / n)
    def __pow__(s, k):
        if k < 0: return Gi(1) / (s ** (-k))
        out = Gi(1)
        for _ in range(k): out = out * s
        return out
    def __eq__(s, o): o = cg(o); return s.r == o.r and s.i == o.i
    def __hash__(s): return hash((s.r, s.i))
    def __bool__(s): return s.r != 0 or s.i != 0


def cg(o): return o if isinstance(o, Gi) else Gi(o)


I = Gi(0, 1)


def rank(rows, nv):
    rows = [r for r in rows if any(bool(v) for v in r)]
    rk = 0
    for col in range(nv):
        piv = next((k for k in range(rk, len(rows)) if rows[k][col]), None)
        if piv is None: continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        p = rows[rk][col]; prow = [v / p for v in rows[rk]]; rows[rk] = prow
        for k in range(len(rows)):
            if k != rk and rows[k][col]:
                f = rows[k][col]
                rows[k] = [a - f * b for a, b in zip(rows[k], prow)]
        rk += 1
        if rk == len(rows): break
    return rk


def nullspace(rows, nv):
    """basis of {x : rows x = 0} over Q(i), by RREF"""
    rows = [list(r) for r in rows if any(bool(v) for v in r)]
    piv_cols = []; rk = 0
    for col in range(nv):
        piv = next((k for k in range(rk, len(rows)) if rows[k][col]), None)
        if piv is None: continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        p = rows[rk][col]; prow = [v / p for v in rows[rk]]; rows[rk] = prow
        for k in range(len(rows)):
            if k != rk and rows[k][col]:
                f = rows[k][col]
                rows[k] = [a - f * b for a, b in zip(rows[k], prow)]
        piv_cols.append(col); rk += 1
        if rk == len(rows): break
    free = [c for c in range(nv) if c not in piv_cols]
    basis = []
    for fc in free:
        x = [Gi(0)] * nv; x[fc] = Gi(1)
        for r, pc in enumerate(piv_cols):
            x[pc] = -rows[r][fc]
        basis.append(x)
    return basis

PREC = 140


def ser_mul(A, B):
    out = [0] * (PREC + 1)
    for i, x in enumerate(A):
        if x:
            for j, y in enumerate(B[: PREC + 1 - i]):
                if y: out[i + j] += x * y
    return out


th2 = [0] * (PREC + 1); th3 = [0] * (PREC + 1); th4 = [0] * (PREC + 1)
n = 0
while (2 * n + 1) ** 2 <= PREC: th2[(2 * n + 1) ** 2] = 2; n += 1
th3[0] = th4[0] = 1; n = 1
while 4 * n * n <= PREC: th3[4 * n * n] = 2; th4[4 * n * n] = 2 * (-1) ** n; n += 1
A_, B_, C_ = ser_mul(th2, th2), ser_mul(th3, th3), ser_mul(th4, th4)
assert ser_mul(B_, B_) == [x + y for x, y in zip(ser_mul(A_, A_), ser_mul(C_, C_))]  # Jacobi's quadric, to x^PREC


def basis(d):  # normal form: a^i c^j b^e, e in {0,1}
    return [(i, d - e - i, e) for e in (0, 1) for i in range(d - e + 1)]


def reduce_poly(p):  # p: dict (i, j, e) -> coeff with any e; b^2 -> a^2 + c^2
    out = {}
    stack = list(p.items())
    while stack:
        (i, j, e), cf = stack.pop()
        if not cg(cf): continue
        if e <= 1:
            out[(i, j, e)] = out.get((i, j, e), 0) + cf
        else:
            stack.append(((i + 2, j, e - 2), cf)); stack.append(((i, j + 2, e - 2), cf))
    return {k: v for k, v in out.items() if cg(v)}


def act_s(mon): i, j, e = mon; return {(j, i, e): 1}                       # (a,b,c) -> (c,b,a)


def act_t(mon): i, j, e = mon; return reduce_poly({(i, e, j): I ** i})    # (a,b,c) -> (i a, c, b): a^i c^j b^e -> i^i a^i c^e b^j


def series_of(mon, cache={}):
    if mon in cache: return cache[mon]
    i, j, e = mon; s = [1] + [0] * PREC
    for _ in range(i): s = ser_mul(s, A_)
    for _ in range(j): s = ser_mul(s, C_)
    for _ in range(e): s = ser_mul(s, B_)
    cache[mon] = s
    return s


def space(d, bounds_G=None):
    """nullity of the linear system on (P0, P1, P2) in the normal-form basis of degree d."""
    bs = basis(d); nb = len(bs); idx = {m: k for k, m in enumerate(bs)}
    nv = 3 * nb
    rows = []
    epsS = (-I) ** (1 - d)          # P_j o s = epsS * P_{sigma j}
    # S constraints
    for j in range(3):
        sj = {0: 1, 1: 0, 2: 2}[j]
        # coefficient vector of (P_j o s) - epsS * P_sj  in basis
        M = {}
        for k, mon in enumerate(bs):
            for m2, cf in act_s(mon).items():
                M.setdefault(idx[m2], {})[j * nb + k] = M.setdefault(idx[m2], {}).get(j * nb + k, 0) + cf
        for k in range(nb):
            M.setdefault(k, {})[sj * nb + k] = M.setdefault(k, {}).get(sj * nb + k, 0) - epsS
        for k, r in M.items(): rows.append(r)
    # T constraints: P_j o t = (M_T P)_j, M_T = [[i,0,0],[0,0,i],[0,-i,0]]
    MT = {0: [(0, I)], 1: [(2, I)], 2: [(1, -I)]}
    for j in range(3):
        M = {}
        for k, mon in enumerate(bs):
            for m2, cf in act_t(mon).items():
                M.setdefault(idx[m2], {})[j * nb + k] = M.setdefault(idx[m2], {}).get(j * nb + k, 0) + cf
        for (jj, ph) in MT[j]:
            for k in range(nb):
                M.setdefault(k, {})[jj * nb + k] = M.setdefault(k, {}).get(jj * nb + k, 0) - ph
        for k, r in M.items(): rows.append(r)
    if bounds_G == "basis":
        dense = [[Gi(0)] * nv for _ in rows]
        for ri, r in enumerate(rows):
            for c, v in r.items(): dense[ri][c] = cg(v)
        return bs, nullspace(dense, nv)
    # order constraints on the lines of G: P = G0, M = G1 + i G2, N = G1 - i G2
    if bounds_G is not None:
        ser = [series_of(m) for m in bs]
        for li, bd in enumerate(bounds_G):
            assert bd < PREC - 5
            for kx in range(0, bd):
                r = {}
                for k in range(nb):
                    v = ser[k][kx]
                    if v == 0: continue
                    if li == 0: r[0 * nb + k] = v
                    elif li == 1: r[1 * nb + k] = v; r[2 * nb + k] = I * v
                    else: r[1 * nb + k] = v; r[2 * nb + k] = -I * v
                if r: rows.append(r)
    dense = [[Gi(0)] * nv for _ in rows]
    for ri, r in enumerate(rows):
        for c, v in r.items(): dense[ri][c] = cg(v)
    return nv - rank(dense, nv)


def dimM(w): return 0 if w < 0 or w % 2 else (w // 12 + (0 if w % 12 == 2 else 1))


print("completeness (no order condition): dim of the equivariant space vs the free-module count")
for d in (1, 3, 5, 7, 9, 11, 13, 15, 17, 27):
    k2 = 2 * d - 3                          # 2k, k = d - 3/2
    fm = dimM(d - 1) + dimM(d - 3) + dimM(d - 5)
    print("  d=%2d (k=%s/2): equivariant %d, free module %d" % (d, k2, len(space(d, "basis")[1]), fm), flush=True)
_eq = {}


def line_series(d):
    """for the equivariant basis at degree d: each basis vector's three G-line series (P, M, N) to x^PREC"""
    if d in _eq: return _eq[d]
    bs, B = space(d, "basis"); nb = len(bs)
    ser = [series_of(m) for m in bs]
    out = []
    for x in B:
        G = []
        for j in range(3):
            s = [Gi(0)] * (PREC + 1)
            for k in range(nb):
                cf = x[j * nb + k]
                if cf:
                    for e, v in enumerate(ser[k]):
                        if v: s[e] = s[e] + cf * v
            G.append(s)
        out.append((G[0], [a + I * b for a, b in zip(G[1], G[2])], [a - I * b for a, b in zip(G[1], G[2])]))
    _eq[d] = out
    return out


def d_theta(m, Nn=None):
    if Nn is None: Nn = max(0, max(m))
    d = 3 + 12 * Nn; L = line_series(d)
    bounds = [b + 8 * (Nn - mi) + 1 for b, mi in zip((1, 7, 3), m)]
    rows = []
    for li in range(3):
        for kx in range(0, bounds[li]):
            rows.append([L[v][li][kx] for v in range(len(L))])
    return len(L) - (rank(rows, len(L)) if rows else 0)


bad = []
for m in itertools.product((-1, 0, 1, 2), repeat=3):
    val = d_theta(m)
    if val != max(0, sum(m)): bad.append((m, val))
print("per-line {-1..2}^3 by the theta-polynomial route: mismatches with max(0, sum m):", bad)

print("uniform O(n delta):")
for Nn in range(0, 3):
    print("  n=%d: dim=%d (3n=%d)" % (Nn, d_theta((Nn, Nn, Nn)), 3 * Nn))
