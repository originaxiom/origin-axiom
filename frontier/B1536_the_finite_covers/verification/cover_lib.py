#!/usr/bin/env python3
"""B1536 -- the population: the states, their finite covers, the Q8 tower, and the covers' cusps.  Shared by both routes (it
defines what is read, not how).  Nothing is computed on import.

THE STATES.  m004 = +LR and m003 = -LR on sm:B1527's presentation (family_lib.word_group): Gamma = F x| <t>, F = <a, b>,
t g t^-1 = phi(g), the cusp <l, t'> with l = abAB and t' = t (+) or abt (-).  Their exact holonomy over Q(omega) is sm:B1530's
exact_states.eisenstein_sl2 (banked; the relators are checked there and again here).

A COVER is a transitive permutation representation of Gamma on X = {0, ..., d-1} with base point 0, as low_index returns it:
perms[g][x] = x^g, a RIGHT action (x^(gh) = (x^g)^h).  The matrix P(g)_{x,y} = [x^g = y] then satisfies P(gh) = P(g) P(h), so
g -> P(g) is a representation on column vectors, isomorphic to C[Gamma / H] with H = Stab(0) (g . e_y = e_{y^(g^-1)}).

THE CUSPS of the cover are the orbits O of <l, t'> on X.  For a point x of O the stabiliser {(i, j) : x^(l^i t'^j) = x} is a
lattice in Z^2 (l and t' commute in Gamma); its basis (HNF) gives the cusp's two peripheral elements, and j0(O), the gcd of the
second coordinates, is the cusp's t-period.

THE Q8 TOWER.  K = ker(F -> Q8), a -> i, b -> j, is characteristic in F (Aut(Q8) acts simply transitively on the 24 generating
pairs, so every surjection F -> Q8 has kernel K).  So phi induces beta in Aut(Q8), and H_m = K x| <t^m> has index 8m.  Its cosets
H f t^s are the pairs (fK, s), 0 <= s < m, with
    (q, s)^a = (q beta^s(i), s),   (q, s)^b = (q beta^s(j), s),   (q, s)^t = (q, s + 1) for s + 1 < m,  (beta^-m(q), 0) otherwise,
from H f t^s a = H f phi^s(a) t^s and H f t^m = H t^m phi^-m(f) = H phi^-m(f)."""
import importlib.util
import sys
import warnings
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1530V = ROOT / "frontier" / "B1530_the_interior_extensions" / "verification"
STATES = {"m004": ("+", "LR"), "m003": ("-", "LR")}


def _exact():
    if str(B1530V) not in sys.path:
        sys.path.insert(0, str(B1530V))
    import exact_lib as E          # noqa: E402
    import exact_states as X       # noqa: E402
    return E, X


SILVER = {"m135": "-LLRR", "m136": "+LLRR"}


def state(name):
    """the group (exact_lib.Group), phi's images, the exact holonomy over Q(zeta_24) and the four, with the checks.  The
    Eisenstein states (m004, m003 and m004's levels) use sm:B1530's exact_states.eisenstein_sl2; the silver squares m135, m136
    (controls only) use sm:B1534's silver_lib.holonomy (Q(i))"""
    E, X = _exact()
    if name in SILVER:
        sign, word = SILVER[name][0], SILVER[name][1:]
    else:
        sign, word = STATES[name] if name in STATES else (name[0], name[1:])
    G, img, chars, D = X.group(sign, word)
    if name in SILVER:
        spec = importlib.util.spec_from_file_location(
            "b1534_silver_lib", ROOT / "frontier" / "B1534_the_silver_covers" / "verification" / "silver_lib.py")
        SL = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(SL)
        g2 = SL.holonomy(SILVER[name])
    else:
        g2 = X.eisenstein_sl2(sign, word)
    chk = X.check_sl2(G, g2)
    assert all(chk.values()), (name, chk)
    rho = X.four_module(g2)
    assert rho.check(G.rels), name
    return {"name": name, "sign": sign, "word": word, "G": G, "img": img, "fibre characters": chars, "D": D, "g2": g2,
            "rho": rho}


# ============================================================================================ words and permutations
def inv_word(w):
    return "".join(c.swapcase() for c in reversed(w))


def act(perms, w, x):
    """x^w for the right action (upper case = inverse)"""
    for c in w:
        if c.islower():
            x = perms[c][x]
        else:
            x = perms["_inv"][c.lower()][x]
    return x


def with_inverses(perms):
    d = len(next(iter(perms.values())))
    out = dict(perms)
    out["_inv"] = {}
    for g, p in perms.items():
        q = [0] * d
        for x, y in enumerate(p):
            q[y] = x
        out["_inv"][g] = q
    return out


def check_cover(G, perms):
    """the relators act trivially and the action is transitive"""
    P = with_inverses(perms)
    d = len(perms[G.gens[0]])
    ok = all(act(P, r, x) == x for r in G.rels for x in range(d))
    seen, todo = {0}, [0]
    while todo:
        x = todo.pop()
        for g in G.gens:
            for y in (P[g][x], P["_inv"][g][x]):
                if y not in seen:
                    seen.add(y)
                    todo.append(y)
    return ok and len(seen) == d


# ============================================================================================ the covers of degree <= D
def low_index_covers(G, D):
    """every transitive permutation representation of degree <= D up to conjugacy (low_index, Culler-Dunfield), as
    {gen: list}; low_index names the generators a, b, c, ... in G.gens order, so the relators are spelled in those letters"""
    import low_index
    gens = G.gens
    letters = "abcdefgh"[:len(gens)]
    tr = {}
    for g, x in zip(gens, letters):
        tr[g], tr[g.upper()] = x, x.upper()
    rels = ["".join(tr[c] for c in r) for r in G.rels]
    out = []
    for h in low_index.permutation_reps(len(gens), rels, [], D):
        perms = {g: list(h[i]) for i, g in enumerate(gens)}
        assert check_cover(G, perms)
        out.append(perms)
    return out


def canonical(perms, gens):
    """a canonical form of the transitive action up to relabelling (the lexicographically least BFS relabelling over every
    base point), so that two routes' covers can be matched as Gamma-sets"""
    P = with_inverses(perms)
    d = len(perms[gens[0]])
    best = None
    for x0 in range(d):
        lab, order = {x0: 0}, [x0]
        i = 0
        while i < len(order):
            x = order[i]
            i += 1
            for g in gens:
                for y in (P[g][x], P["_inv"][g][x]):
                    if y not in lab:
                        lab[y] = len(order)
                        order.append(y)
        key = tuple(tuple(lab[P[g][x]] for x in order) for g in gens)
        if best is None or key < best:
            best = key
    return best


# ============================================================================================ the Q8 tower
Q8 = ["1", "-1", "i", "-i", "j", "-j", "k", "-k"]
_MUL = {("i", "j"): "k", ("j", "k"): "i", ("k", "i"): "j", ("j", "i"): "-k", ("k", "j"): "-i", ("i", "k"): "-j",
        ("i", "i"): "-1", ("j", "j"): "-1", ("k", "k"): "-1"}


def qmul(x, y):
    sx, ux = (-1, x[1:]) if x.startswith("-") else (1, x)
    sy, uy = (-1, y[1:]) if y.startswith("-") else (1, y)
    s = sx * sy
    if ux == "1":
        u = uy
    elif uy == "1":
        u = ux
    else:
        r = _MUL[(ux, uy)]
        if r.startswith("-"):
            s, u = -s, r[1:]
        else:
            u = r
    return ("-" if s < 0 else "") + u


def qinv(x):
    return x if x in ("1", "-1") else (x[1:] if x.startswith("-") else "-" + x)


def qword(w, images):
    out = "1"
    for c in w:
        out = qmul(out, images[c] if c.islower() else qinv(images[c.lower()]))
    return out


def q8_beta(img):
    """beta in Aut(Q8) induced by phi (a -> i, b -> j): beta(i) = pi(phi(a)), beta(j) = pi(phi(b)); returns beta on all of Q8"""
    pi = {"a": "i", "b": "j"}
    bi, bj = qword(img["a"], pi), qword(img["b"], pi)
    beta = {"1": "1", "-1": "-1", "i": bi, "j": bj, "k": qmul(bi, bj)}
    for x in ("i", "j", "k"):
        beta["-" + x] = qinv(beta[x])
    assert sorted(beta.values()) == sorted(Q8), ("phi does not induce an automorphism of Q8", beta)
    return beta


def q8_tower(img, m):
    """the coset action of Gamma on Gamma / H_m, H_m = K x| <t^m>, points (q, s) numbered q-major within s"""
    beta = q8_beta(img)
    binv = {v: k for k, v in beta.items()}
    pts = [(q, s) for s in range(m) for q in Q8]
    idx = {p: n for n, p in enumerate(pts)}

    def bpow(q, s):
        for _ in range(s):
            q = beta[q]
        return q

    def bnegm(q):
        for _ in range(m):
            q = binv[q]
        return q
    perms = {"a": [], "b": [], "t": []}
    for (q, s) in pts:
        perms["a"].append(idx[(qmul(q, bpow("i", s)), s)])
        perms["b"].append(idx[(qmul(q, bpow("j", s)), s)])
        perms["t"].append(idx[(q, s + 1)] if s + 1 < m else idx[(bnegm(q), 0)])
    return perms


# ============================================================================================ the cusps
def _hnf2(vectors):
    """a basis of the lattice spanned by integer 2-vectors (rank 2 expected), in Hermite normal form"""
    rows = [list(v) for v in vectors if v != (0, 0)]
    # column 0
    def reduce_col(rows, c):
        piv = None
        while True:
            nz = [r for r in rows if r[c] != 0]
            if len(nz) <= 1:
                piv = nz[0] if nz else None
                break
            nz.sort(key=lambda r: abs(r[c]))
            p = nz[0]
            for r in nz[1:]:
                q = r[c] // p[c]
                r[0] -= q * p[0]
                r[1] -= q * p[1]
            rows = [r for r in rows if r != [0, 0]]
        return rows, piv
    rows, p0 = reduce_col(rows, 0)
    rest = [r for r in rows if r is not p0 and r[0] == 0]
    rest, p1 = reduce_col(rest, 1)
    out = []
    if p0 is not None:
        out.append(tuple(p0) if p0[0] > 0 else (-p0[0], -p0[1]))
    if p1 is not None:
        out.append(tuple(p1) if p1[1] > 0 else (-p1[0], -p1[1]))
    return out


def cusps(G, perms):
    """[(base point x, orbit, [(i1, j1), (i2, j2)] the stabiliser lattice of x in <l, t'> ~ Z^2, j0 the t-period)]"""
    P = with_inverses(perms)
    l, tp = G.cusp
    d = len(perms[G.gens[0]])
    out, done = [], set()
    for x in range(d):
        if x in done:
            continue
        coord = {x: (0, 0)}
        todo, rel = [x], []
        while todo:
            y = todo.pop()
            i, j = coord[y]
            for w, (di, dj) in ((l, (1, 0)), (inv_word(l), (-1, 0)), (tp, (0, 1)), (inv_word(tp), (0, -1))):
                z = act(P, w, y)
                c = (i + di, j + dj)
                if z in coord:
                    if coord[z] != c:
                        rel.append((c[0] - coord[z][0], c[1] - coord[z][1]))
                else:
                    coord[z] = c
                    todo.append(z)
        basis = _hnf2(rel)
        assert len(basis) == 2, ("the stabiliser is not a rank-two lattice", basis)
        index = abs(basis[0][0] * basis[1][1] - basis[0][1] * basis[1][0])
        assert index == len(coord), ("orbit size != lattice index", index, len(coord))
        j0 = gcd(basis[0][1], basis[1][1])
        out.append({"x": x, "orbit": sorted(coord), "lattice": basis, "j0": j0})
        done |= set(coord)
    return out


def periph_word(G, i, j):
    """l^i t'^j as a word"""
    l, tp = G.cusp
    return (l * i if i >= 0 else inv_word(l) * (-i)) + (tp * j if j >= 0 else inv_word(tp) * (-j))


def t_degree(G, w):
    """the image of w in H_1(Gamma) -> Z (t has degree 1, a and b degree 0)"""
    return w.count("t") - w.count("T")
