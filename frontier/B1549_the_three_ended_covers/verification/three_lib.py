#!/usr/bin/env python3
"""sm:B1549 -- the three-ended covers: library. Nothing is computed on import.

THE OBJECTS. For a generated state M (sm:B1527's presentation: a, b, t, two relators, the cusp <l, t'>), a three-ended cover
is one of sm:B1538's fibre-direction covers of degree 3 with three cusps: a lattice Lam of index 3 with M Lam = Lam, and a
class wbar. Its deck group Z/3 permutes the three ends.

THE FRAME (sm:B1515 at nu^4 = 1). rho is the four (H -> g H g*), nu a character of the cover N of order dividing 4, so
L = nu^-4 = 1, nu^5 = nu and b0 = 1. A class c of H^1(N; nu (x) rho) gives W1 = [[nu rho, c], [0, 1]]; the count is
(I(W1), I(Lambda^2 W1)), I(E) = n(E) - n(E*), n = h1 - r1, r1 the rank of the restriction to every cusp.

TWO ROUTES, sharing only the cover's action, the character's definition and the holonomy:
  - route P: N's own presentation (sm:B1538's punct_present), the module on its Schreier generators;
  - route S: Shapiro on M. A class z of H^1(M; Ind nu (x) rho) gives the class c(h) = z(h)_0 on N (the coset-0 block), then
    Ind W1(g)_{x,y} = W1(u_x g u_y^-1) and Ind(Lambda^2 W1) on M; N's cusps are read through M's one cusp (Mackey).
Each route draws its own generic interior class.

PRECISION. The holonomy is sm:B1527's family_lib.hyperbolic_sl2 at 60 digits; everything is computed with mpmath at 50
digits. Ranks by Gauss-Jordan elimination with column pivoting; an entry is zero below 1e-30 of the matrix's largest. The
gap (the least live pivot, the largest dead entry, both relative) is recorded at every rank."""
import importlib.util
import itertools
import random
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent


def _root():
    """the repository: the first parent holding frontier/ (or ORIGIN_AXIOM_ROOT when run outside it)"""
    for p in HERE.parents:
        if (p / "frontier").is_dir():
            return p
    import os
    return Path(os.environ["ORIGIN_AXIOM_ROOT"])


ROOT = _root()
B1538V = ROOT / "frontier" / "B1538_the_puncture_characters" / "verification"
B1527V = ROOT / "frontier" / "B1527_the_cusp_decides" / "verification"
DPS = 50
REL = mp.mpf(10) ** -30


def load(alias, path):
    if alias not in sys.modules:
        if str(path.parent) not in sys.path:
            sys.path.append(str(path.parent))
        spec = importlib.util.spec_from_file_location(alias, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[alias] = mod
        spec.loader.exec_module(mod)
    return sys.modules[alias]


PC = load("punct_covers", B1538V / "punct_covers.py")
RP = load("punct_present", B1538V / "punct_present.py")


def family_lib():
    return load("b1527_family_lib", B1527V / "family_lib.py")


# ================================================================================================ the states and covers
def canon(w):
    rots = [w[i:] + w[:i] for i in range(len(w))]
    sw = w.translate(str.maketrans("LR", "RL"))
    rots += [sw[i:] + sw[:i] for i in range(len(sw))]
    return min(rots)


def primitive(w):
    n = len(w)
    return all(w != w[k:] + w[:k] for k in range(1, n) if n % k == 0)


def states(nmax=8, dmax=12):
    out = set()
    for n in range(2, nmax + 1):
        for t in itertools.product("LR", repeat=n):
            w = "".join(t)
            if "L" in w and "R" in w and primitive(w):
                out.add(canon(w))
    res = []
    for w in sorted(out, key=lambda x: (len(x), x)):
        for sign in "+-":
            (a, b), (c, d_) = PC.State(sign + w).M
            d = abs(2 - (a + d_))
            if d <= dmax:
                res.append((sign + w, d))
    return res


def three_covers(nmax=8, dmax=12):
    """every (state, ends of its companion, lattice, wbar) with a degree-3 fibre-direction cover with three cusps"""
    out = []
    for sw, d in states(nmax, dmax):
        st = PC.State(sw)
        for lat in PC.lattices(st.M, 3, 3):
            for wl in range(3):
                if len(PC.Cover(st, lat, wl).cusps) == 3:
                    out.append((sw, d, tuple(lat), wl))
    return out


def deck_action(C, ez, es, m):
    out = {}
    for x in range(C.d):
        ux = C.u[x]
        ez2 = []
        for y in C.gword:
            vec = C.abelian(C.rewrite(PC.inv_word(ux) + y + ux))
            ez2.append(sum(e * v for e, v in zip(ez, vec)) % m)
        k = PC.inv_word(ux) + C.st.phi(C.w + ux + PC.inv_word(C.w))
        vec = C.abelian(C.rewrite(k))
        out[x] = (tuple(ez2), (es + sum(e * v for e, v in zip(ez, vec))) % m)
    return out


def orbits(C, m):
    chars = [(ez, es) for ez in C.characters(m) for es in range(m)]
    acts = {c: deck_action(C, c[0], c[1], m) for c in chars}
    seen, out = set(), []
    for c in chars:
        if c not in seen:
            orb = sorted({acts[c][x] for x in range(C.d)})
            assert set(orb) <= set(acts), "a deck image is not a character"
            seen |= set(orb)
            out.append(orb)
    return out


def char_order(c, m):
    for k in range(1, m + 1):
        if m % k == 0 and all((e * k) % m == 0 for e in c[0]) and (c[1] * k) % m == 0:
            return k


# ================================================================================================ the four, at 50 digits
_HOL = {}


def four_mp(g):
    E = [mp.matrix([[1, 0], [0, 0]]), mp.matrix([[0, 0], [0, 1]]), mp.matrix([[0, 1], [1, 0]]),
         mp.matrix([[0, 1j], [-1j, 0]])]
    gs = g.transpose_conj()
    M = mp.matrix(4, 4)
    for k, Ek in enumerate(E):
        X = g * Ek * gs
        col = [mp.re(X[0, 0]), mp.re(X[1, 1]), mp.re(X[0, 1]), mp.im(X[0, 1])]
        for i in range(4):
            M[i, k] = col[i]
    return M


def holonomy(sw):
    """the four on a, b, t, from sm:B1527's hyperbolic_sl2 at 60 digits"""
    if sw not in _HOL:
        mp.mp.dps = 60
        A, B, T, _ = family_lib().hyperbolic_sl2(sw[0], sw[1:])
        F = {"a": four_mp(A), "b": four_mp(B), "t": four_mp(T)}
        mp.mp.dps = DPS
        _HOL[sw] = F
    mp.mp.dps = DPS
    return _HOL[sw]


def root(e, m):
    e %= m
    if m == 4:
        return [mp.mpc(1), mp.mpc(0, 1), mp.mpc(-1), mp.mpc(0, -1)][e]
    if m == 2:
        return [mp.mpc(1), mp.mpc(-1)][e]
    return mp.expjpi(mp.mpf(2 * e) / m)


# ================================================================================================ linear algebra (lists)
def eye(n):
    return [[mp.mpc(1) if i == j else mp.mpc(0) for j in range(n)] for i in range(n)]


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    Bt = list(zip(*B))
    return [[mp.fsum(A[i][l] * Bt[j][l] for l in range(k)) for j in range(m)] for i in range(n)]


def matinv(A):
    n = len(A)
    M = [list(A[i]) + eye(n)[i] for i in range(n)]
    piv, R, _ = rref(M, n, full=True)
    assert piv == list(range(n)), "singular"
    return [row[n:] for row in R]


def to_list(M):
    return [[mp.mpc(M[i, j]) for j in range(M.cols)] for i in range(M.rows)]


def rref(A, ncols=None, full=False):
    """Gauss-Jordan with column pivoting: (pivot columns, the pivot rows, (least live, largest dead) relative)"""
    A = [list(r) for r in A]
    m = len(A)
    n = ncols if ncols is not None else (len(A[0]) if A else 0)
    amax = max((abs(x) for r in A for x in r[:n]), default=mp.mpf(0))
    if amax == 0:
        return [], [], (None, 0.0)
    tol = amax * REL
    pivots, row = [], 0
    least, dead = None, mp.mpf(0)
    for col in range(n):
        if row >= m:
            break
        bi, best = -1, mp.mpf(0)
        for i in range(row, m):
            v = abs(A[i][col])
            if v > best:
                bi, best = i, v
        if best <= tol:
            dead = max(dead, best)
            continue
        least = best if least is None else min(least, best)
        A[row], A[bi] = A[bi], A[row]
        inv_p = 1 / A[row][col]
        prow = [x * inv_p for x in A[row]]
        A[row] = prow
        width = len(prow)
        for i in range(m):
            if i != row:
                f = A[i][col]
                if f != 0:
                    Ai = A[i]
                    for j in range(col, width):
                        if prow[j] != 0:
                            Ai[j] -= f * prow[j]
        pivots.append(col)
        row += 1
    for i in range(row, m):
        for j in range(n):
            dead = max(dead, abs(A[i][j]))
    return pivots, A[:row], (float(least / amax) if least is not None else None, float(dead / amax))


def rank(A, ncols=None):
    p, _, gap = rref(A, ncols)
    return len(p), gap


def nullspace(A, n):
    """columns (as a list of vectors of length n) spanning the kernel of A (rows of length n)"""
    if not A:
        return [[mp.mpc(1) if i == j else mp.mpc(0) for i in range(n)] for j in range(n)], (None, 0.0)
    piv, R, gap = rref(A, n)
    free = [c for c in range(n) if c not in piv]
    basis = []
    for f in free:
        v = [mp.mpc(0)] * n
        v[f] = mp.mpc(1)
        for k, pc in enumerate(piv):
            v[pc] = -R[k][f]
        basis.append(v)
    return basis, gap


def hstack(*blocks):
    return [sum((list(b[i]) for b in blocks), []) for i in range(len(blocks[0]))]


def vstack(*blocks):
    return [list(r) for b in blocks for r in b]


def matvec(A, v):
    return [mp.fsum(a * x for a, x in zip(row, v)) for row in A]


# ================================================================================================ module cohomology
class Pres:
    """a presentation for cohomology: number of generators, relators and peripheral pairs as words [(index, +-1)]"""

    def __init__(self, ngen, rels, periph):
        self.ngen, self.rels, self.periph = ngen, rels, periph


class Mod:
    def __init__(self, mats):
        self.M = [list(map(list, m)) for m in mats]
        self.e = len(mats[0])
        self.Mi = [matinv(m) for m in self.M]

    def word(self, w):
        X = eye(self.e)
        for j, s in w:
            X = matmul(X, self.M[j] if s == 1 else self.Mi[j])
        return X

    def fox(self, w, ngen):
        """the e x (ngen e) block of z -> z(w) for left cocycles, and the word's matrix"""
        e = self.e
        out = [[mp.mpc(0)] * (ngen * e) for _ in range(e)]
        Pre = eye(e)
        for j, s in w:
            if s == 1:
                for i in range(e):
                    for k in range(e):
                        out[i][j * e + k] += Pre[i][k]
                Pre = matmul(Pre, self.M[j])
            else:
                Pre = matmul(Pre, self.Mi[j])
                for i in range(e):
                    for k in range(e):
                        out[i][j * e + k] -= Pre[i][k]
        return out, Pre

    def dual(self):
        return Mod([[list(r) for r in zip(*mi)] for mi in self.Mi])


def relator_defect(mod, P):
    worst = mp.mpf(0)
    I = eye(mod.e)
    for r in P.rels:
        W = mod.word(r)
        worst = max(worst, max(abs(W[i][j] - I[i][j]) for i in range(mod.e) for j in range(mod.e)))
    return worst


def cohom(mod, P, want_interior=False):
    """h0, h1, r1, n; with want_interior also a basis of interior cocycles modulo coboundaries"""
    e, ng = mod.e, P.ngen
    assert relator_defect(mod, P) < mp.mpf(10) ** -35, "a relator is not 1 in the module"
    fox = vstack(*[mod.fox(r, ng)[0] for r in P.rels])
    rk, g1 = rank(fox, ng * e)
    I = eye(e)
    dg = vstack(*[[[mod.M[j][i][k] - I[i][k] for k in range(e)] for i in range(e)] for j in range(ng)])
    r0, g0 = rank(dg, e)
    h0 = e - r0
    h1 = ng * e - rk - (e - h0)
    Z, gz = nullspace(fox, ng * e)
    rowsR, BPb = [], []
    for (w1, w2) in P.periph:
        F1, W1 = mod.fox(w1, ng)
        F2, W2 = mod.fox(w2, ng)
        rowsR += [F1, F2]
        BPb.append(vstack([[W1[i][k] - I[i][k] for k in range(e)] for i in range(e)],
                          [[W2[i][k] - I[i][k] for k in range(e)] for i in range(e)]))
    nc = len(P.periph)
    BP = [[mp.mpc(0)] * (e * nc) for _ in range(2 * e * nc)]
    for c, b in enumerate(BPb):
        for i in range(2 * e):
            for k in range(e):
                BP[2 * e * c + i][e * c + k] = b[i][k]
    R = vstack(*rowsR)
    rBP, g2 = rank(BP, e * nc)
    RZ = [[mp.fsum(R[i][l] * z[l] for l in range(ng * e)) for z in Z] for i in range(len(R))] if Z else [[] for _ in R]
    rboth, g3 = rank(hstack(BP, RZ), e * nc + len(Z)) if Z else (rBP, None)
    r1 = rboth - rBP
    out = {"h0": h0, "h1": h1, "r1": r1, "n": h1 - r1, "gaps": [g0, g1, g2, g3]}
    if want_interior:
        out["interior"] = interior(Z, RZ, BP, mod, P) if Z else []
    return out


def interior(Z, RZ, BP, mod, P):
    """cocycles z = Z alpha with R z in col(BP), modulo the coboundaries; a basis"""
    e, ng = mod.e, P.ngen
    nz = len(Z)
    M = hstack(RZ, [[-x for x in row] for row in BP])
    K, _ = nullspace(M, nz + len(BP[0]))
    I_cocycles = []
    for k in K:
        alpha = k[:nz]
        I_cocycles.append([mp.fsum(alpha[j] * Z[j][l] for j in range(nz)) for l in range(ng * e)])
    I = eye(e)
    cob = [[mod.M[j][i][k] - I[i][k] for k in range(e)] for j in range(ng) for i in range(e)]      # z(s_j) = (A_j - 1) v
    # columns: the coboundary space first, then the interior cocycles; the cocycle columns that pivot are a complement
    cols = [list(r) for r in cob]                               # (ng e) x e
    Mtx = [cols[i] + [v[i] for v in I_cocycles] for i in range(ng * e)]
    piv, _, _ = rref(Mtx, e + len(I_cocycles))
    return [I_cocycles[p - e] for p in piv if p >= e]


# ================================================================================================ the frame
def wedge2(X):
    n = len(X)
    idx = [(i, j) for i in range(n) for j in range(i + 1, n)]
    return [[X[i][k] * X[j][l] - X[i][l] * X[j][k] for (k, l) in idx] for (i, j) in idx]


def frame_mats(A, cvals):
    """W1 on each generator: [[A_j, c_j], [0, 1]]"""
    out = []
    for Aj, cj in zip(A, cvals):
        e = len(Aj)
        X = [list(Aj[i]) + [cj[i]] for i in range(e)] + [[mp.mpc(0)] * e + [mp.mpc(1)]]
        out.append(X)
    return out


def count_of(W1, P):
    """the count (I(W1), I(Lambda^2 W1)) and the four readings"""
    m1 = Mod(W1)
    m2 = Mod([wedge2(X) for X in W1])
    reads = {"W1": cohom(m1, P), "W1*": cohom(m1.dual(), P), "L2": cohom(m2, P), "L2*": cohom(m2.dual(), P)}
    return (reads["W1"]["n"] - reads["W1*"]["n"], reads["L2"]["n"] - reads["L2*"]["n"]), reads


def generic(basis, rng):
    coef = [mp.mpc(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in basis]
    n = len(basis[0])
    return [mp.fsum(coef[k] * basis[k][l] for k in range(len(basis))) for l in range(n)]


# ================================================================================================ route P
def presentation_P(C):
    Pr = RP.Presentation(C)
    return Pr, Pres(len(Pr.gens), Pr.rels, Pr.periph)


def word_four(F, w):
    X = mp.eye(4)
    for c in w:
        X = X * (F[c] if c.islower() else F[c.lower()] ** -1)
    return X


def module_P(sw, C, Pr, ez, es, m):
    F = holonomy(sw)
    vals = Pr.values(ez, es, m)
    return [[[root(v, m) * x for x in row] for row in to_list(word_four(F, w))] for v, (_, _, w) in zip(vals, Pr.gens)]


def _summ(reads):
    return {k: {kk: v[kk] for kk in ("h0", "h1", "r1", "n", "gaps")} for k, v in reads.items()}


def read_P(sw, C, ez, es, m, rngs=None):
    """route P: the structure of nu (x) rho and, for each rng, a generic interior class's count"""
    Pr, P = presentation_P(C)
    A = module_P(sw, C, Pr, ez, es, m)
    s = cohom(Mod(A), P, want_interior=bool(rngs))
    out = {"structure": {k: s[k] for k in ("h0", "h1", "r1", "n", "gaps")}}
    if rngs:
        out["interior dimension"] = len(s["interior"])
        out["draws"] = []
        for rng in rngs:
            if not s["interior"]:
                break
            z = generic(s["interior"], rng)
            cvals = [z[4 * j:4 * j + 4] for j in range(P.ngen)]
            cnt, reads = count_of(frame_mats(A, cvals), P)
            out["draws"].append({"count": list(cnt), "reads": _summ(reads)})
    return out


# ================================================================================================ route S
def ind_blocks(sw, C, ez, es, m):
    """route S's module Ind nu (x) rho on a, b, t: block (x, y) = nu(u_x g u_y^-1) rho(g), y = x.g"""
    F = holonomy(sw)
    vals = C.rs_values(ez, es, m)
    d = C.d
    mats = []
    for g in "abt":
        Fg = to_list(F[g])
        X = [[mp.mpc(0)] * (4 * d) for _ in range(4 * d)]
        for x in range(d):
            y = C.perms[g][x]
            z = root(C.chi_exp(C.u[x] + g + PC.inv_word(C.u[y]), vals, m), m)
            for i in range(4):
                for j in range(4):
                    X[4 * x + i][4 * y + j] = z * Fg[i][j]
        mats.append(X)
    return mats


def presentation_S(st):
    idx = {"a": 0, "b": 1, "t": 2}

    def conv(w):
        return [(idx[c.lower()], 1 if c.islower() else -1) for c in w]
    return Pres(3, [conv(r) for r in st.G.rels], [[conv(w) for w in st.G.cusp]]), conv


def read_S(sw, C, ez, es, m, rngs=None):
    """route S: the structure of Ind nu (x) rho on M and, for each rng, a generic interior class's count"""
    st = C.st
    P, conv = presentation_S(st)
    A = ind_blocks(sw, C, ez, es, m)
    modA = Mod(A)
    s = cohom(modA, P, want_interior=bool(rngs))
    out = {"structure": {k: s[k] for k in ("h0", "h1", "r1", "n", "gaps")}}
    if rngs:
        out["interior dimension"] = len(s["interior"])
        out["draws"] = []
    for rng in (rngs or []):
        if not s["interior"]:
            break
        z = generic(s["interior"], rng)
        F = holonomy(sw)
        vals = C.rs_values(ez, es, m)
        d = C.d
        e = 4 * d

        def zword(w):
            """z(w) on M by the cocycle rule (left cocycles)"""
            tot = [mp.mpc(0)] * e
            Pre = eye(e)
            for j, s_ in conv(w):
                if s_ == 1:
                    zj = z[j * e:(j + 1) * e]
                    tot = [t + v for t, v in zip(tot, matvec(Pre, zj))]
                    Pre = matmul(Pre, modA.M[j])
                else:
                    Pre = matmul(Pre, modA.Mi[j])
                    zj = z[j * e:(j + 1) * e]
                    tot = [t - v for t, v in zip(tot, matvec(Pre, zj))]
            return tot

        def W1_of(word):
            """W1(h) on N for a closed word h at the coset 0: [[nu(h) rho(h), c(h)], [0, 1]], c(h) = z(h)_0"""
            nuh = root(C.chi_exp(word, vals, m), m)
            rh = to_list(word_four(F, word))
            ch = zword(word)[:4]
            return [[nuh * rh[i][k] for k in range(4)] + [ch[i]] for i in range(4)] + [[mp.mpc(0)] * 4 + [mp.mpc(1)]]

        def ind_of(fn, size):
            mats = []
            for g in "abt":
                X = [[mp.mpc(0)] * (size * d) for _ in range(size * d)]
                for x in range(d):
                    y = C.perms[g][x]
                    B = fn(C.u[x] + g + PC.inv_word(C.u[y]))
                    for i in range(size):
                        for k in range(size):
                            X[size * x + i][size * y + k] = B[i][k]
                mats.append(X)
            return mats
        W1 = ind_of(W1_of, 5)
        L2 = ind_of(lambda w: wedge2(W1_of(w)), 10)
        m1, m2 = Mod(W1), Mod(L2)
        reads = {"W1": cohom(m1, P), "W1*": cohom(m1.dual(), P), "L2": cohom(m2, P), "L2*": cohom(m2.dual(), P)}
        out["draws"].append({"count": [reads["W1"]["n"] - reads["W1*"]["n"], reads["L2"]["n"] - reads["L2*"]["n"]],
                             "reads": _summ(reads)})
    return out


# ================================================================================================ the flavor group (exact)
def mono_mul(A, B, m):
    (pa, ea), (pb, eb) = A, B
    n = len(pa)
    return (tuple(pb[pa[x]] for x in range(n)), tuple((ea[x] + eb[pa[x]]) % m for x in range(n)))


def mono_inv(A, m):
    p, e = A
    q, f = [0] * len(p), [0] * len(p)
    for x in range(len(p)):
        q[p[x]], f[p[x]] = x, (-e[x]) % m
    return (tuple(q), tuple(f))


def mono_one(n):
    return (tuple(range(n)), (0,) * n)


def mono_closure(gens, m):
    one = mono_one(len(gens[0][0]))
    G, frontier = {one}, [one]
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = mono_mul(x, g, m)
                if y not in G:
                    G.add(y)
                    nxt.append(y)
        frontier = nxt
    return G


def mono_order(x, m):
    one, k, y = mono_one(len(x[0])), 1, x
    while y != one:
        y, k = mono_mul(y, x, m), k + 1
    return k


def _sign(p):
    s, seen = 1, set()
    for i in range(len(p)):
        if i not in seen:
            j, L = i, 0
            while j not in seen:
                seen.add(j)
                j, L = p[j], L + 1
            s *= -1 if L % 2 == 0 else 1
    return s


def mono_det_one(x, m):
    tot = sum(x[1]) % m
    return (_sign(x[0]) == 1 and tot == 0) or (_sign(x[0]) == -1 and m % 2 == 0 and tot == m // 2)


def group_invariants(G, m):
    G = list(G)
    Z = [z for z in G if all(mono_mul(z, g, m) == mono_mul(g, z, m) for g in G)]
    comms = {mono_mul(mono_mul(mono_inv(x, m), mono_inv(y, m), m), mono_mul(x, y, m), m) for x in G for y in G}
    D = mono_closure(list(comms), m)
    orders = {}
    for x in G:
        k = mono_order(x, m)
        orders[k] = orders.get(k, 0) + 1
    return {"order": len(G), "centre": len(Z), "derived": len(D),
            "element orders": {str(k): v for k, v in sorted(orders.items())}}


def ind_mono(C, ez, es, m):
    vals = C.rs_values(ez, es, m)
    out = {}
    for g in "abt":
        perm = tuple(C.perms[g][x] for x in range(C.d))
        ex = tuple(C.chi_exp(C.u[x] + g + PC.inv_word(C.u[perm[x]]), vals, m) for x in range(C.d))
        out[g] = (perm, ex)
    return out


def flavor_group(C, ez, es, m):
    """the image of pi_1(M) under Ind chi (monomial, exact), its determinant-one part, the cusp's image, irreducibility"""
    import cmath
    I = ind_mono(C, ez, es, m)
    one = mono_one(C.d)
    for r in C.st.G.rels:
        X = one
        for c in r:
            X = mono_mul(X, I[c] if c.islower() else mono_inv(I[c.lower()], m), m)
        assert X == one, "Ind chi is not a representation"
    G = mono_closure(list(I.values()), m)
    tr2 = sum(abs(sum(cmath.exp(2j * cmath.pi * x[1][i] / m) for i in range(C.d) if x[0][i] == i)) ** 2 for x in G)
    G1 = [x for x in G if mono_det_one(x, m)]
    cusp = []
    for w in C.st.G.cusp:
        X = one
        for c in w:
            X = mono_mul(X, I[c] if c.islower() else mono_inv(I[c.lower()], m), m)
        cusp.append(X)
    return {"G": group_invariants(G, m), "irreducible": abs(tr2 / len(G) - 1) < 1e-9,
            "G n SL": group_invariants(G1, m), "cusp image": group_invariants(mono_closure(cusp, m), m)}


def is_A4(inv):
    return inv == {"order": 12, "centre": 1, "derived": 4, "element orders": {"1": 1, "2": 3, "3": 8}}
