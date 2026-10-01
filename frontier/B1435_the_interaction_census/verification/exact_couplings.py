#!/usr/bin/env python3
"""The couplings of B1435 in exact arithmetic over Q(zeta_N): a second implementation, cell by cell.

Nothing is shared with the prime-field instrument except the chain (relcup.Bundle.fundamental, an identity of integer
chains) and the list of backgrounds (their characters, read from the census at the first prime).  Modules, extension
cocycle, classes, relative lifts and the sum over cells are recomputed here over the cyclotomic field.
"""
import sys, json, itertools, pathlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import interaction_census as ic
from relcup import Bundle, X, Y, inv as winv
import sympy

class Cyc:
    """Q(zeta_N) as polynomials modulo the cyclotomic polynomial"""
    def __init__(self, N):
        z = sympy.Symbol("z"); self.N = N
        self.phi = [Fr(int(c)) for c in reversed(sympy.Poly(sympy.cyclotomic_poly(N, z), z).all_coeffs())]   # low -> high, monic
        self.deg = len(self.phi) - 1
    def red(self, c):
        c = list(c)
        while len(c) > self.deg:
            t = c.pop()
            if t:
                off = len(c) - self.deg
                for i in range(self.deg): c[off + i] -= t * self.phi[i]
        return tuple(c + [Fr(0)] * (self.deg - len(c)))
    def el(self, c): return E(self, self.red(c))
    def zeta(self, e):
        e %= self.N; return self.el([Fr(0)] * e + [Fr(1)])
    def const(self, q): return self.el([Fr(q)])

class E:
    __slots__ = ("F", "c")
    def __init__(self, F, c): self.F, self.c = F, c
    def _co(self, o): return o if isinstance(o, E) else self.F.const(o)
    def __add__(s, o): o = s._co(o); return E(s.F, tuple(a + b for a, b in zip(s.c, o.c)))
    __radd__ = __add__
    def __neg__(s): return E(s.F, tuple(-a for a in s.c))
    def __sub__(s, o): return s + (-s._co(o))
    def __rsub__(s, o): return s._co(o) - s
    def __mul__(s, o):
        o = s._co(o); d = s.F.deg; out = [Fr(0)] * (2 * d - 1)
        for i, a in enumerate(s.c):
            if a:
                for j, b in enumerate(o.c):
                    if b: out[i + j] += a * b
        return s.F.el(out)
    __rmul__ = __mul__
    def iszero(s): return not any(s.c)
    def __eq__(s, o): return s.c == s._co(o).c
    def __hash__(s): return hash(s.c)
    def inv(s):
        d = s.F.deg                                         # solve s * x = 1 as a rational linear system
        cols = []
        for j in range(d):
            b = s * s.F.el([Fr(0)] * j + [Fr(1)]); cols.append(b.c)
        M = [[cols[j][i] for j in range(d)] + [Fr(1 if i == 0 else 0)] for i in range(d)]
        for c in range(d):
            k = next(i for i in range(c, d) if M[i][c]); M[c], M[k] = M[k], M[c]
            iv = 1 / M[c][c]; M[c] = [v * iv for v in M[c]]
            for i in range(d):
                if i != c and M[i][c]:
                    f = M[i][c]; M[i] = [v - f * w for v, w in zip(M[i], M[c])]
        return E(s.F, tuple(M[i][d] for i in range(d)))

# ---------------------------------------------------------------- linear algebra over the field
def nullspace(rows, n, F):
    R = [list(r) for r in rows]; piv = []; rk = 0
    for c in range(n):
        k = next((i for i in range(rk, len(R)) if not R[i][c].iszero()), None)
        if k is None: continue
        R[rk], R[k] = R[k], R[rk]; iv = R[rk][c].inv(); R[rk] = [v * iv for v in R[rk]]
        for i in range(len(R)):
            if i != rk and not R[i][c].iszero():
                f = R[i][c]; R[i] = [v - f * w for v, w in zip(R[i], R[rk])]
        piv.append(c); rk += 1
    NS = []
    for fc in [c for c in range(n) if c not in piv]:
        v = [F.const(0)] * n; v[fc] = F.const(1)
        for i, pc in enumerate(piv): v[pc] = -R[i][fc]
        NS.append(v)
    return rk, NS
def rank(rows, n, F): return nullspace(rows, n, F)[0] if rows else 0
def solve(rows, rhs, F):
    n = len(rows[0]); R = [list(r) + [b] for r, b in zip(rows, rhs)]; piv = []; rk = 0
    for c in range(n):
        k = next((i for i in range(rk, len(R)) if not R[i][c].iszero()), None)
        if k is None: continue
        R[rk], R[k] = R[k], R[rk]; iv = R[rk][c].inv(); R[rk] = [v * iv for v in R[rk]]
        for i in range(len(R)):
            if i != rk and not R[i][c].iszero():
                f = R[i][c]; R[i] = [v - f * w for v, w in zip(R[i], R[rk])]
        piv.append(c); rk += 1
    if any(not r[n].iszero() for r in R[rk:]): return None
    v = [F.const(0)] * n
    for i, c in enumerate(piv): v[c] = R[i][n]
    return v
def mmul(A, B): return [[sum((A[i][l] * B[l][j] for l in range(1, len(B))), A[i][0] * B[0][j]) for j in range(len(B[0]))] for i in range(len(A))]
def mvec(A, v): return [sum((A[i][j] * v[j] for j in range(1, len(v))), A[i][0] * v[0]) for i in range(len(A))]
def minv2(A):
    if len(A) == 1: return [[A[0][0].inv()]]
    d = (A[0][0] * A[1][1] - A[0][1] * A[1][0]).inv()
    return [[A[1][1] * d, -A[0][1] * d], [-A[1][0] * d, A[0][0] * d]]
def tr(A): return [list(r) for r in zip(*A)]

class XMod:
    def __init__(self, B, F, mx, my, mt):
        self.B, self.F, self.d = B, F, len(mx); self.M = {X: mx, Y: my, -X: minv2(mx), -Y: minv2(my)}; self.Mt = mt
        self.I = [[F.const(int(i == j)) for j in range(self.d)] for i in range(self.d)]
        for g in (X, Y): assert self._eq(mmul(mmul(mt, self.M[g]), minv2(mt)), self.rhoF(B.Phi[g])), "not a representation"
    def _eq(self, A, Bm): return all(a == b for r, s in zip(A, Bm) for a, b in zip(r, s))
    def rhoF(self, w):
        R = self.I
        for g in w: R = mmul(R, self.M[g])
        return R
    def rho(self, el):
        f, n = el; R = self.rhoF(f)
        for _ in range(n): R = mmul(R, self.Mt)
        return R
    def dual(self): return XMod(self.B, self.F, tr(minv2(self.M[X])), tr(minv2(self.M[Y])), tr(minv2(self.Mt)))

class XCo:
    def __init__(self, V, vx, vy, vt): self.V, self.v, self.vt = V, {X: vx, Y: vy}, vt
    def onF(self, w):
        V = self.V; out = [V.F.const(0)] * V.d; pre = V.I
        for g in w:
            if g > 0: out = [a + b for a, b in zip(out, mvec(pre, self.v[g]))]; pre = mmul(pre, V.M[g])
            else: pre = mmul(pre, V.M[g]); out = [a - b for a, b in zip(out, mvec(pre, self.v[-g]))]
        return out
    def __call__(self, el):
        f, n = el; out = self.onF(f); pre = self.V.rhoF(f)
        for _ in range(n): out = [a + b for a, b in zip(out, mvec(pre, self.vt))]; pre = mmul(pre, self.V.Mt)
        return out

def classes(V):
    F, d = V.F, V.d; n = 3 * d
    def resid(vec):
        c = XCo(V, vec[:d], vec[d:2 * d], vec[2 * d:]); out = []
        for g in (X, Y):
            lhs = [a + b - q for a, b, q in zip(c.vt, mvec(V.Mt, c.v[g]), mvec(V.rhoF(V.B.Phi[g]), c.vt))]
            out += [l - r for l, r in zip(lhs, c.onF(V.B.Phi[g]))]
        return out
    cols = [resid([F.const(int(i == j)) for j in range(n)]) for i in range(n)]
    rk, Z = nullspace([list(r) for r in zip(*cols)], n, F)
    Bb = []
    for i in range(d):
        v = [F.const(int(i == j)) for j in range(d)]
        dv = lambda M: [a - b for a, b in zip(mvec(M, v), v)]
        row = dv(V.M[X]) + dv(V.M[Y]) + dv(V.Mt)
        if any(not q.iszero() for q in row): Bb.append(row)
    cur = list(Bb); r0 = rank(cur, n, F); reps = []
    for zc in Z:
        r2 = rank(cur + [zc], n, F)
        if r2 > r0: cur.append(zc); r0 = r2; reps.append(XCo(V, zc[:d], zc[d:2 * d], zc[2 * d:]))
    return reps
def lift(a):
    V = a.V; lam = (V.B.lam, 0); Rl = V.rho(lam)
    A1 = [[V.Mt[i][j] - V.I[i][j] for j in range(V.d)] for i in range(V.d)]; A2 = [[Rl[i][j] - V.I[i][j] for j in range(V.d)] for i in range(V.d)]
    return solve(A1 + A2, a(V.B.T) + a(lam), V.F)
def fox1(word, val, F):                                     # the extension cocycle: Fox row of a relator for a character
    D = [F.const(0)] * 3; pre = F.const(1)
    for L in word:
        g = abs(L) - 1
        if L > 0: D[g] = D[g] + pre; pre = pre * val[g]
        else: pre = pre * val[g].inv(); D[g] = D[g] - pre
    return D
def ext_cocycle(lc, rels, F):
    val = [F.zeta(e) for e in lc]; rk, NS = nullspace([fox1(r, val, F) for r in rels], 3, F)
    b = [v - 1 for v in val]
    for zc in NS:
        if all(q.iszero() for q in b) or rank([b, zc], 3, F) == 2: return zc
    raise AssertionError("no extension class")

def couplings(eps, word, k, limit=None, pick=None):
    o, bgs, I, chars, N, rels, tau = ic.level_census(eps, word, k)
    B = Bundle(ic.Phi_of(eps, word, k)); C, z, _ = B.fundamental(); F = Cyc(N)
    add = lambda x, y: tuple((a + b) % N for a, b in zip(x, y)); neg = lambda x: tuple((-a) % N for a in x)
    out = []
    for n, (key, cnt) in enumerate(sorted(bgs.items())):
        if pick is not None and n not in pick: continue
        if limit and len(out) >= limit: break
        lc = key[0]; al = dict(zip(ic.SECT, key[1:])); sg = cnt[0]; ct = ext_cocycle(lc, rels, F)
        mods = {}
        for s, c in zip(ic.SECT, cnt):
            if c != sg: continue
            mats = []
            for i in range(3):
                a = F.zeta(al[s][i]); b = F.zeta(al[s][i] - lc[i]); mats.append([[a, ct[i] * b], [F.const(0), b]])
            V = XMod(B, F, *mats); V = V.dual() if sg < 0 else V
            reps = classes(V); assert len(reps) == 1; e = lift(reps[0]); assert e is not None
            mods[s] = (V, reps[0], e)
        row = {}
        for A, Bs in itertools.combinations_with_replacement([s for s in ic.SECT if s in mods], 2):
            if not ic.partner(A, Bs): continue
            eta = add(add(al[A], al[Bs]), neg(lc)); eta = neg(eta) if sg > 0 else eta
            Vh = XMod(B, F, [[F.zeta(eta[0])]], [[F.zeta(eta[1])]], [[F.zeta(eta[2])]]); hs = classes(Vh); assert len(hs) == 1
            h = hs[0]; (VA, a, e), (VB, b, _) = mods[A], mods[Bs]; tot = F.const(0)
            for (g1, g2, g3), kk in C.items():
                av = a(g1); bv = mvec(VB.rho(g1), b(g2)); w = Vh.rho(B.mul(g1, g2))[0][0] * h(g3)[0]
                tot = tot + (av[0] * bv[1] - av[1] * bv[0]) * w * kk
            for (g1, g2), kk in z.items():
                bv = b(g1); w = Vh.rho(g1)[0][0] * h(g2)[0]
                tot = tot - (e[0] * bv[1] - e[1] * bv[0]) * w * kk
            row["%s.%s" % (A, Bs)] = (not tot.iszero(), [str(q) for q in tot.c], not h.vt[0].iszero())
        out.append(dict(key=[list(c) for c in key], counts=list(cnt), pairs=row))
        print(n, cnt[0], " ".join("%s:%s" % (nm, "Y" if v[0] else "0") for nm, v in row.items()), flush=True)
    return dict(state=("+" if eps > 0 else "-") + word, k=k, N=N, field="Q(zeta_%d)" % N, backgrounds=out)

if __name__ == "__main__":
    st, k = sys.argv[1], int(sys.argv[2]); lim = int(sys.argv[3]) if len(sys.argv) > 3 else None
    res = couplings(1 if st[0] == "+" else -1, st[1:], k, limit=lim)
    json.dump(res, open(HERE / ("exact_%s_%d.json" % (st.replace("+", "p").replace("-", "m"), k)), "w"), indent=1)
