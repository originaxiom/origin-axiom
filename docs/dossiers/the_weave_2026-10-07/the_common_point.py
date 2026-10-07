#!/usr/bin/env python3
"""W2-W4 of the weave (docs/THE_WEAVE.md). The common point and the triplet: what the joint action of the grammar's
moves forces on every allowed object (every thread) at once,
with no object chosen. Exact (sympy and rational arithmetic); the quaternion closures are numerical, rounded at 1e-9 on a
group of 48 elements.

The fibre group is F_2 = <a, b> (the two records), the puncture loop is [a, b], and the moves are the automorphisms
  L: (a, b) -> (a, ab),   R: (a, b) -> (ab, b),   P: (a, b) -> (b, a),   -I: (a, b) -> (a^-1, b^-1),
inducing L = [[1, 1], [0, 1]], R = [[1, 0], [1, 1]], P = [[0, 1], [1, 0]] and -I on the records.
  (1) The common point. On the fibre's characters (x, y, z) = (tr a, tr b, tr ab) the moves act by polynomial maps.
      With the puncture parabolic (GENESIS GM4: tr [a, b] = -2, the Markov surface x^2 + y^2 + z^2 = xyz) the only point
      every move fixes is the origin: the quaternion representation a -> i, b -> j, ab -> k, [a, b] -> -1. Without the
      cusp condition the moves fix one more point, (2, 2, 2), where the puncture is trivial. Each object fixes the
      origin and its own geometric points besides (listed for the named objects).
  (2) Its trace on every object. The quaternion point extends to every object's group F_2 x|_phi Z, with t sent to an
      element g of the binary octahedral group 2O (g i g^-1 = rho(phi(a)), g j g^-1 = rho(phi(b))). The image is
      2T = SL(2, F_3) (order 24) exactly when phi cycles the three non-zero parities, Q_16 when it fixes one, and Q_8
      when it fixes all three; mod +-1 it is the fibre-parity group A_4, D_4 or V_4. Every hyperbolic word in L, R, P
      to length 8, both signs.
  (3) The triplet. The fibre's parity-twisted cohomology, the sum over the three non-trivial parity characters chi of
      H^1(F_2; chi), is three-dimensional, one line for each non-zero parity. The moves and the fibre's own inner
      automorphisms act on it by signed permutations; the group they generate, its character, and for every object
      the group its monodromy and the fibre generate, with the irreducibility test sum |tr|^2 / |G| = 1. Compared with
      the adjoint of the quaternion point (the rotations of the axes i, j, k).

    python3 the_common_point.py   ->  the_common_point.json beside this file"""
import itertools
import json
from collections import Counter
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent

# ---- words in F_2: 1 = a, 2 = b, -1 = a^-1, -2 = b^-1 ----
AUT = {"L": {1: [1], 2: [1, 2]}, "R": {1: [1, 2], 2: [2]}, "P": {1: [2], 2: [1]}, "-I": {1: [-1], 2: [-2]}}
MAT = {"L": ((1, 1), (0, 1)), "R": ((1, 0), (1, 1)), "P": ((0, 1), (1, 0)), "-I": ((-1, 0), (0, -1))}


def reduce(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return out


def inv(w):
    return [-x for x in reversed(w)]


def apply(alpha, w):
    """the image of the word w under the automorphism alpha (a dict on the generators)"""
    out = []
    for x in w:
        out += alpha[x] if x > 0 else inv(alpha[-x])
    return reduce(out)


def compose(alpha, beta):
    """alpha o beta"""
    return {g: apply(alpha, beta[g]) for g in (1, 2)}


def inner(u):
    return {g: reduce(u + [g] + inv(u)) for g in (1, 2)}


def word_aut(word, sign):
    """the automorphism of a state: the moves composed in the word's order, times -I for the sign -"""
    phi = {1: [1], 2: [2]}
    for c in word:
        phi = compose(phi, AUT[c])
    return compose(AUT["-I"], phi) if sign < 0 else phi


def mat(word, sign):
    M = np.eye(2, dtype=int)
    for c in word:
        M = M @ np.array(MAT[c])
    return sign * M


PAR = [(1, 0), (0, 1), (1, 1)]


def parity_kind(M):
    p = [tuple(int(v) % 2 for v in M @ np.array(q)) for q in PAR]
    fixed = sum(1 for q, r in zip(PAR, p) if q == r)
    return {3: "fixes all three", 1: "fixes one", 0: "cycles all three"}[fixed]


# ---- (1) the common point on the character variety ----
x, y, z = sp.symbols("x y z")
TR = {"L": (x, z, x * z - y), "R": (z, y, y * z - x), "P": (y, x, z), "-I": (x, y, z)}
KAPPA = x ** 2 + y ** 2 + z ** 2 - x * y * z - 2           # tr [a, b]


def trace_map(word, sign):
    """traces of rho o phi in terms of the traces of rho (the sign acts trivially on traces)"""
    T = (x, y, z)
    for c in word:      # rho o (alpha o beta) = (rho o alpha) o beta
        T = tuple(sp.expand(e.subs({x: TR[c][0], y: TR[c][1], z: TR[c][2]}, simultaneous=True)) for e in T)
    return T


def groebner(maps, cusp=True):
    """the lex Groebner basis of the fixed-point equations of the maps (with the cusp condition if asked);
    sympy's solve drops roots it cannot write in radicals, so the points are read from the basis"""
    eqs = [sp.expand(m[i] - v) for m in maps for i, v in enumerate((x, y, z))]
    if cusp:
        eqs.append(sp.expand(KAPPA + 2))
    return sp.groebner(eqs, x, y, z, order="lex")


def points(G):
    """the finitely many points of a zero-dimensional basis in shape position (x - f(z), y - g(z), h(z)), exact"""
    assert G.is_zero_dimensional
    h = sp.Poly(G.exprs[-1], z)
    pts = []
    for z0 in sp.roots(h, multiple=False) or {}:
        sub = [sp.simplify(e.subs(z, z0)) for e in G.exprs[:-1]]
        sol = sp.solve([e for e in sub if e != 0], [x, y], dict=True) if any(e != 0 for e in sub) else [{}]
        for d in sol:
            pts.append((d.get(x, x), d.get(y, y), z0))
    return pts


def part1():
    out = {}
    for m in ("L", "R", "P", "-I"):
        assert sp.expand(KAPPA.subs({x: TR[m][0], y: TR[m][1], z: TR[m][2]}, simultaneous=True) - KAPPA) == 0
    out["every move preserves tr [a, b]"] = True
    allm = [TR["L"], TR["R"], TR["P"], TR["-I"]]
    Gc = groebner(allm, cusp=True)
    out["every move's fixed-point ideal with the puncture parabolic (lex basis)"] = [str(e) for e in Gc.exprs]
    out["the points every move fixes, puncture parabolic"] = [str(p) for p in points(Gc)]
    Ga = groebner(allm, cusp=False)
    out["the points every move fixes, any puncture (with tr [a, b])"] = [
        f"{p}: {sp.simplify(KAPPA.subs({x: p[0], y: p[1], z: p[2]}))}" for p in points(Ga)]
    GL = groebner([TR["L"]], cusp=True)
    out["the points L alone fixes, puncture parabolic"] = [str(p) for p in points(GL)]
    per = {}
    for name, (w, s_) in {"m004 (+LR)": ("LR", 1), "m003 (-LR)": ("LR", -1), "+LLR": ("LLR", 1),
                          "+LLLR": ("LLLR", 1), "+LLRR": ("LLRR", 1), "m000 (LP)": ("LP", 1)}.items():
        G = groebner([trace_map(w, s_)], cusp=True)
        h = sp.factor_list(G.exprs[-1])
        per[name] = {"the eliminant in z = tr ab": str(sp.factor(G.exprs[-1])),
                     "points besides the origin (distinct roots of the eliminant other than 0)":
                         int(sum(sp.degree(f, z) for f, _ in h[1] if f != z)),
                     "the basis is in shape position": bool(all(sp.degree(e, x) + sp.degree(e, y) <= 1
                                                                 for e in G.exprs[:-1]))}
    out["each thread's fixed points on the Markov surface (orientation-reversing threads: their geometric point is "
        "fixed by the map followed by complex conjugation, not by the map)"] = per
    return out


# ---- (2) the quaternion point extended to every object ----
def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return (a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2, a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2, a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2)


def qconj(p):
    return (p[0], -p[1], -p[2], -p[3])


def key(p):
    return tuple(round(v + 0.0, 9) + 0.0 for v in p)


ONE, QI, QJ, QK = (1.0, 0.0, 0.0, 0.0), (0.0, 1.0, 0.0, 0.0), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0)
RHO = {1: QI, 2: QJ, -1: qconj(QI), -2: qconj(QJ)}


def rho(w):
    p = ONE
    for g in w:
        p = qmul(p, RHO[g])
    return p


def closure(gens):
    G = {key(ONE): ONE}
    fr = [ONE]
    while fr:
        nx = []
        for p in fr:
            for g in gens:
                r = qmul(p, g)
                if key(r) not in G:
                    G[key(r)] = r
                    nx.append(r)
        fr = nx
    return G


s2 = 2 ** -0.5
TWO_O = closure([QI, QJ, (s2, s2, 0.0, 0.0), (0.5, 0.5, 0.5, 0.5)])
assert len(TWO_O) == 48


def extend(phi):
    """the elements g of 2O with g rho(x) g^-1 = rho(phi(x)) for x = a, b"""
    out = []
    for g in TWO_O.values():
        if all(key(qmul(qmul(g, RHO[x]), qconj(g))) == key(rho(phi[x])) for x in (1, 2)):
            out.append(g)
    return out


def part2(nmax=8):
    tab, named = Counter(), {}
    seen = set()
    for n in range(2, nmax + 1):
        for t in itertools.product("LRP", repeat=n):
            w = "".join(t)
            c = min(w[i:] + w[:i] for i in range(n))
            if c in seen:
                continue
            seen.add(c)
            for sign in (1, -1):
                M = mat(c, sign)
                tr, det = int(M.trace()), int(round(np.linalg.det(M)))
                if not ((abs(tr) > 2) if det == 1 else (tr != 0)):
                    continue
                gs = extend(word_aut(c, sign))
                assert len(gs) == 2 and key(gs[0]) == key(tuple(-v for v in gs[1]))
                orders = {len(closure([QI, QJ, g])) for g in gs}
                assert len(orders) == 1
                k = (det, parity_kind(M), orders.pop())
                tab[k] += 1
                lab = {("LR", 1): "m004 (+LR)", ("LR", -1): "m003 (-LR)", ("LP", 1): "m000 (LP)",
                       ("LLLR", 1): "+LLLR"}.get((c, sign))
                if lab:
                    named[lab] = {"trace": tr, "det": det, "parity action": k[1], "image order": k[2]}
    by_kind = {}
    for (det, kind, order), v in sorted(tab.items()):
        by_kind.setdefault(f"det {det}, {kind}", {})[str(order)] = v
    return {"every hyperbolic word in L, R, P to length 8, both signs: (det, parity action) -> image order -> objects":
            by_kind, "the named objects": named,
            "the image's order is 24 (2T) exactly for the 3-cycles": all(
                (o == 24) == (kind == "cycles all three") for (_, kind, o) in tab)}


# ---- (3) the triplet ----
CHARS = [(1, -1), (-1, 1), (-1, -1)]          # (chi(a), chi(b)); chi is trivial on the parity (1,0), (0,1), (1,1)


def chi_of(c, w):
    s = 1
    for g in w:
        s *= c[abs(g) - 1]
    return s


def cocycle(chi, ca, cb, w):
    """c(w) for the chi-cocycle with c(a) = ca, c(b) = cb"""
    tot, pre = Fr(0), 1
    for g in w:
        cg = (ca, cb)[abs(g) - 1]
        val = cg if g > 0 else -chi[abs(g) - 1] * cg
        tot += pre * val
        pre *= chi[abs(g) - 1]
    return tot


def lam(chi, ca, cb):
    return (chi[1] - 1) * ca - (chi[0] - 1) * cb


REP = {(1, -1): (Fr(-1, 2), Fr(0)), (-1, 1): (Fr(0), Fr(1, 2)), (-1, -1): (Fr(0), Fr(1, 2))}


def tmat(alpha):
    """the matrix of alpha^* on the sum of the H^1(F_2; chi): column chi -> row chi o alpha"""
    M = [[0] * 3 for _ in range(3)]
    for j, chi in enumerate(CHARS):
        assert lam(chi, *REP[chi]) == 1
        ca, cb = cocycle(chi, *REP[chi], alpha[1]), cocycle(chi, *REP[chi], alpha[2])
        chi2 = (chi_of(chi, alpha[1]), chi_of(chi, alpha[2]))
        M[CHARS.index(chi2)][j] = lam(chi2, ca, cb)
    return tuple(tuple(int(v) for v in r) for r in M)


def mmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def mclosure(gens):
    I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    G, fr = {I}, [I]
    while fr:
        nx = []
        for A in fr:
            for g in gens:
                B = mmul(A, g)
                if B not in G:
                    G.add(B)
                    nx.append(B)
        fr = nx
    return G


def ad(g):
    """the adjoint of g on the axes (i, j, k): column e is the axis g e g^-1"""
    cols = [qmul(qmul(g, e), qconj(g))[1:] for e in (QI, QJ, QK)]
    return tuple(tuple(int(round(cols[j][i])) for j in range(3)) for i in range(3))


def transpose(A):
    return tuple(tuple(A[j][i] for j in range(3)) for i in range(3))


def part3():
    INN = {"inner by a": inner([1]), "inner by b": inner([2])}
    gens = {**{m: AUT[m] for m in ("L", "R", "P", "-I")}, **INN}
    mats = {n: tmat(a) for n, a in gens.items()}
    G = mclosure(list(mats.values()))
    tr = Counter(sum(A[i][i] for i in range(3)) for A in G)
    det = Counter(int(round(np.linalg.det(np.array(A)))) for A in G)
    G0 = mclosure([mats[m] for m in ("L", "R", "inner by a", "inner by b")])
    out = {"the matrices (columns: the lines trivial on a, on b, on ab)": {n: [list(r) for r in M] for n, M in mats.items()},
           "the group the moves and the fibre generate": {"order": len(G), "traces": dict(sorted(tr.items())),
                                                           "determinants": dict(det),
                                                           "sum tr^2 / order": str(Fr(sum(sum(A[i][i] for i in range(3)) ** 2 for A in G), len(G)))},
           "the group L, R and the fibre generate": {"order": len(G0), "sum tr^2 / order": str(
               Fr(sum(sum(A[i][i] for i in range(3)) ** 2 for A in G0), len(G0)))}}
    # the same triplet as the adjoint of the quaternion point?
    pair_gens = []
    for n, a in gens.items():
        gs = extend(a)
        pair_gens.append((mats[n], transpose(ad(gs[0]))))      # alpha^* is contravariant: Ad(g)^T = Ad(g)^-1
    pairs, fr = {(((1, 0, 0), (0, 1, 0), (0, 0, 1)),) * 2}, [(((1, 0, 0), (0, 1, 0), (0, 0, 1)),) * 2]
    while fr:
        nx = []
        for (A, B) in fr:
            for (g, h) in pair_gens:
                C = (mmul(A, g), mmul(B, h))
                if C not in pairs:
                    pairs.add(C)
                    nx.append(C)
        fr = nx
    firsts = Counter(A for A, _ in pairs)
    out["against the adjoint of the quaternion point"] = {
        "pairs (cohomology, adjoint) generated": len(pairs),
        "a function of the cohomology matrix (one adjoint for each)": max(firsts.values()) == 1,
        "equal traces at every pair": all(sum(A[i][i] for i in range(3)) == sum(B[i][i] for i in range(3))
                                          for A, B in pairs),
        "traces equal up to the determinant": all(sum(A[i][i] for i in range(3)) ==
                                                  int(round(np.linalg.det(np.array(A)))) * sum(B[i][i] for i in range(3))
                                                  for A, B in pairs)}
    per = {}
    for name, (w, s_) in {"m004 (+LR)": ("LR", 1), "m003 (-LR)": ("LR", -1), "m000 (LP)": ("LP", 1),
                          "+LLLR": ("LLLR", 1), "+LLRR": ("LLRR", 1), "+LLR": ("LLR", 1)}.items():
        phi = word_aut(w, s_)
        Mphi = tmat(phi)
        H = mclosure([Mphi, mats["inner by a"], mats["inner by b"]])
        g = extend(phi)[0]
        pg = [(Mphi, transpose(ad(g))), (mats["inner by a"], transpose(ad(QI))), (mats["inner by b"], transpose(ad(QJ)))]
        prs, fr2 = {(((1, 0, 0), (0, 1, 0), (0, 0, 1)),) * 2}, [(((1, 0, 0), (0, 1, 0), (0, 0, 1)),) * 2]
        while fr2:
            nx = []
            for (A, B) in fr2:
                for (u, v) in pg:
                    C = (mmul(A, u), mmul(B, v))
                    if C not in prs:
                        prs.add(C)
                        nx.append(C)
            fr2 = nx
        dphi = int(round(np.linalg.det(np.array(Mphi)))) * int(round(np.linalg.det(np.array(transpose(ad(g))))))
        per[name] = {"parity action": parity_kind(mat(w, s_)), "order": len(H),
                     "sum tr^2 / order": str(Fr(sum(sum(A[i][i] for i in range(3)) ** 2 for A in H), len(H))),
                     "against the quaternion axes: pairs generated": len(prs),
                     "the same representation (equal traces at every pair)":
                         all(sum(A[i][i] for i in range(3)) == sum(B[i][i] for i in range(3)) for A, B in prs),
                     "det of the monodromy on the cohomology over its det on the axes": dphi}
    out["each object's group (its monodromy and the fibre) on the triplet"] = per
    return out


def main():
    out = {"(1) the common point": part1(), "(2) its trace on every object": part2(), "(3) the triplet": part3()}
    (HERE / "the_common_point.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
