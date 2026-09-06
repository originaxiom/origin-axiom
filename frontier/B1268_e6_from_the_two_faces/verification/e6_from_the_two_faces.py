#!/usr/bin/env python3
"""E6 FROM THE TWO FACES.

(1) LATTICE.  The golden face gives E8 as the icosian ring (the Z[phi]-span of the 120 unit icosians
    = 2I, Conway-Sloane: E8 under the Euclidean norm EN(q) = x + y for QN(q) = x + y*sqrt5).
    The Eisenstein face gives A2 = Z[omega], realised inside the icosians by an order-3 unit
    (every order-3 element of 2I generates a copy).  THEOREM (computed here, exact over Q(sqrt5)):
        E6  =  Z[omega]^perp  inside  E8(icosians),
    with 72 roots, determinant 3, and E8 / (A2 + E6) = Z/3; the remaining 162 roots project onto the
    A2 plane to the six minimal vectors of A2*, 27 for each -- the 27 and the 27bar of E6 are the
    slices of the golden roots by the Eisenstein weights, the Z/3 is left multiplication by omega,
    and theta (27 <-> 27bar) is quaternion conjugation restricted to the Eisenstein plane.

(2) COEFFICIENTS.  In the transport E8 > E6 x SU(3) (the E8 singularity along Q with an SU(3) flat
    connection -- the heterotic standard-embedding mechanism, which the corpus scoped at B315), the
    27s on Q are counted by h1(Q; 3_rho) and the 27bars by h1(Q; 3bar_rho) for rho: pi_1(Q) -> SU(3).
    The object's own SU(3) coefficient systems through its Eisenstein quotient 2T are the complex
    ones 2' + omega and 2'' + omega-bar (2' = 2 (x) omega, the Eisenstein twists of the quaternionic
    2), which are NOT self-dual.  For each of the 48 surjections pi_1(m004) -> 2T (B1263), compute
        h1(m004; 2), h1(2'), h1(2''), the cusp data, rank(res), and N = h1(2') - h1(2'').
"""
from __future__ import annotations
import os, sys, itertools, collections
from fractions import Fraction as F
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'B1265_spectrum_law_rebuilt', 'verification'))   # the instrument
sys.path.insert(0, os.path.join(HERE, '..', '..', 'B1267_transport_computed', 'verification'))     # 2T in SL(2,Q(omega))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'B1266_cusped_net_chirality_bound', 'verification'))  # the lemma rows
import e6_instrument as E
import spectrum_law as S
import transport as T

Qw, ONE, ZERO, OMEGA = E.Qw, E.ONE, E.ZERO, E.OMEGA


# =============================================================== (1) the lattice
class Q5:
    """x + y*sqrt5, exact."""
    __slots__ = ('x', 'y')

    def __init__(self, x, y=F(0)):
        self.x, self.y = F(x), F(y)

    def __add__(self, o):
        o = o if isinstance(o, Q5) else Q5(o)
        return Q5(self.x + o.x, self.y + o.y)
    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, Q5) else Q5(o)
        return Q5(self.x - o.x, self.y - o.y)

    def __neg__(self):
        return Q5(-self.x, -self.y)

    def __mul__(self, o):
        o = o if isinstance(o, Q5) else Q5(o)
        return Q5(self.x * o.x + 5 * self.y * o.y, self.x * o.y + self.y * o.x)
    __rmul__ = __mul__

    def __eq__(self, o):
        o = o if isinstance(o, Q5) else Q5(o)
        return self.x == o.x and self.y == o.y

    def __hash__(self):
        return hash((self.x, self.y))

    def EN(self):                       # the Euclidean-norm functional x + y
        return self.x + self.y

    def __repr__(self):
        return f"({self.x}+{self.y}r5)"


PHI = Q5(F(1, 2), F(1, 2))
PHI_INV = Q5(F(-1, 2), F(1, 2))         # phi - 1
HALF = Q5(F(1, 2))


def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return (a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
            a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
            a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2)


def qconj(p):
    return (p[0], -p[1], -p[2], -p[3])


def QN(p):
    return sum((x * x for x in p), Q5(0))


def bil(p, q):
    """B(p,q) = EN-part of Re(p qbar), times 2 so roots have norm 2."""
    r = qmul(p, qconj(q))[0]
    return 2 * r.EN()


def unit_icosians():
    """The 120 unit icosians = 2I: 24 Hurwitz units + 96 even permutations of (±phi, ±1, ±phi^-1, 0)/2."""
    out = set()
    one, zero = Q5(1), Q5(0)
    for s in (1, -1):
        for k in range(4):
            v = [zero] * 4
            v[k] = Q5(s)
            out.add(tuple(v))
    for signs in itertools.product((1, -1), repeat=4):
        out.add(tuple(Q5(F(s, 2)) for s in signs))
    base = [PHI, Q5(1), PHI_INV, Q5(0)]
    even_perms = [p for p in itertools.permutations(range(4)) if perm_sign(p) == 1]
    for perm in even_perms:
        for signs in itertools.product((1, -1), repeat=3):
            v = [None] * 4
            vals = [base[0] * Q5(signs[0]), base[1] * Q5(signs[1]), base[2] * Q5(signs[2]), Q5(0)]
            for pos, k in enumerate(perm):
                v[k] = vals[pos] * HALF
            out.add(tuple(v))
    return sorted(out, key=lambda t: tuple((x.x, x.y) for x in t))


def perm_sign(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def e8_roots(units):
    roots = set(units)
    for u in units:
        roots.add(tuple(PHI_INV * x for x in u))
    return sorted(roots, key=lambda t: tuple((x.x, x.y) for x in t))


def gram_det(vectors):
    import sympy as sp
    G = sp.Matrix([[sp.Rational(bil(a, b)) for b in vectors] for a in vectors])
    return G.det(), G


def lattice_basis_from_roots(roots):
    """A Z-basis of the lattice spanned by the given roots, via integer row reduction (sympy)."""
    import sympy as sp
    # coordinates: each root as an 8-vector over Q (x,y parts of the four Q5 coordinates)
    M = sp.Matrix([[sp.Rational(c.x) for c in r] + [sp.Rational(c.y) for c in r] for r in roots])
    # scale to integers
    den = sp.ilcm(*[sp.Rational(v).q for v in M])
    Mi = (M * den).applyfunc(lambda v: sp.Integer(v))
    H = Mi.T.rref()[0]  # not HNF; use rank + Smith later; here just the rank
    return M, den


def key(q):
    return tuple((c.x, c.y) for c in q)


def part1():
    units = unit_icosians()
    assert len(units) == 120, len(units)
    assert all(QN(u) == Q5(1) for u in units)
    roots = e8_roots(units)
    assert len(roots) == 240
    assert all(bil(r, r) == 2 for r in roots)
    # the icosian ring is closed: check the 120 units form a group of order 120 with an order-3 element
    uset = {key(u) for u in units}
    assert all(key(qmul(a, b)) in uset for a in units[:20] for b in units)
    orders = collections.Counter()
    order3 = []
    for u in units:
        p, n = u, 1
        one = (Q5(1), Q5(0), Q5(0), Q5(0))
        while key(p) != key(one):
            p = qmul(p, u)
            n += 1
        orders[n] += 1
        if n == 3:
            order3.append(u)
    print(f"  unit icosians: 120, element orders {dict(sorted(orders.items()))}  (2I: 1,1,30,20,24,20,24)")
    # E8 check: the 240 roots span a lattice of determinant 1 (compute a basis by Gaussian elimination
    # over Q of the 8-dim coordinate vectors, then the Gram determinant of a Z-basis via Smith form)
    import sympy as sp
    coords = sp.Matrix([[sp.Rational(c.x) for c in r] + [sp.Rational(c.y) for c in r] for r in roots])
    # Gram matrix of ALL roots and the lattice determinant via a maximal-rank subset + index test:
    # simpler: the E8 lattice determinant is 1 iff the Gram matrix of a Z-basis has det 1.  Extract a
    # Z-basis with integer HNF on the coordinate lattice scaled by 2 (all coordinates are in (1/2)Z[phi]).
    Z = (coords * 2).applyfunc(lambda v: sp.Integer(v))     # integer 240 x 8 (coordinates in Z[phi]/2 -> Z^8/… )
    # Smith/HNF: use sympy's hermite normal form of Z^T
    from sympy.matrices.normalforms import hermite_normal_form
    Hn = hermite_normal_form(Z.T)                            # 8 x 8 basis of the coordinate lattice (columns)
    basis = [tuple(Q5(Hn[k, j] / 2, Hn[4 + k, j] / 2) for k in range(4)) for j in range(Hn.shape[1])]
    d, G = gram_det(basis)
    print(f"  Z-basis of the root lattice: {len(basis)} vectors, Gram determinant = {d}   (E8: 1)")
    # the Eisenstein plane: Z[omega] generated by an order-3 unit w
    w = order3[0]
    one = (Q5(1), Q5(0), Q5(0), Q5(0))
    w2 = qmul(w, w)
    assert key(qmul(w2, w)) == key(one)
    A2 = [one, w]
    dA2, GA2 = gram_det(A2)
    print(f"  Eisenstein plane {{1, w}} with w of order 3: Gram = {GA2.tolist()}, det = {dA2}   (A2: [[2,-1],[-1,2]], 3)")
    # the orthogonal complement among the roots
    perp = [r for r in roots if bil(r, one) == 0 and bil(r, w) == 0]
    print(f"  roots orthogonal to the Eisenstein plane: {len(perp)}   (E6: 72)")
    # Dynkin type: find a base of simple roots (six roots with pairwise products 0/-1 forming the E6 graph)
    # via the Cartan matrix of a positive system
    import random
    rng = random.Random(3)
    while True:
        h = [rng.randint(-97, 97) for _ in range(8)]
        def ht(r):
            return sum(hh * float(v) for hh, v in zip(h, [c.x for c in r] + [c.y for c in r]))
        if all(abs(ht(r)) > 1e-9 for r in perp):
            break
    pos = [r for r in perp if ht(r) > 0]
    simple = [r for r in pos if not any(bil(r, s) > 0 and key(r) != key(s) and
                                      any(key(tuple(a - b for a, b in zip(r, s))) == key(t) for t in pos) for s in pos)]
    # simpler simple-root extraction: a positive root is simple iff it is not a sum of two positive roots
    posk = {key(r) for r in pos}
    simple = [r for r in pos if not any(key(tuple(a - b for a, b in zip(r, s))) in posk for s in pos if key(s) != key(r))]
    C = [[bil(a, b) for b in simple] for a in simple]
    print(f"  simple roots of the complement: {len(simple)}; Cartan matrix rows: {C}")
    degs = sorted(sum(1 for x in row if x == -1) for row in C)
    print(f"  Dynkin degrees {degs}   (E6: [1,1,1,2,2,3] -- one branch node of degree 3, three legs)")
    dP = sp.Matrix([[sp.Rational(x) for x in row] for row in C]).det()
    print(f"  Cartan determinant of the complement's simple roots = {dP}   (E6: 3)")
    # every complement root is an integer combination of the six simple roots (the root lattice IS E6)
    Msimple = sp.Matrix([[sp.Rational(c.x) for c in r] + [sp.Rational(c.y) for c in r] for r in simple]).T
    ok_span = 0
    for r in perp:
        v = sp.Matrix([sp.Rational(c.x) for c in r] + [sp.Rational(c.y) for c in r])
        sol = Msimple.gauss_jordan_solve(v)[0]
        if all(sp.Rational(x).q == 1 for x in sol):
            ok_span += 1
    print(f"  complement roots that are integral combinations of the simple roots: {ok_span}/72")
    print(f"  index [E8 : A2 + E6] = sqrt(det(A2) det(E6) / det(E8)) = sqrt({dA2}*{dP}/{d}) = {sp.sqrt(dA2 * dP / d)}   (Z/3, the Eisenstein prime)")
    # the 27 slices: projections of the remaining roots onto the A2 plane
    rest = [r for r in roots if not (bil(r, one) == 0 and bil(r, w) == 0) and key(r) not in {key(x) for x in (one, w, w2)} and
            key(tuple(-c for c in r)) not in {key(x) for x in (one, w, w2)}]
    proj = collections.Counter()
    for r in rest:
        proj[(bil(r, one), bil(r, w))] += 1
    print(f"  the other {len(rest)} roots, by their A2-pairings (B(r,1), B(r,w)): {dict(sorted(proj.items()))}")
    print("     -> six classes of 27: the three weights of the 3 (27 each) and the three of the 3bar (27 each)")
    # Z/3 = left multiplication by w permutes the three weights of each sign; theta = conjugation swaps 3 <-> 3bar
    cls = {}
    for r in rest:
        cls[key(r)] = (bil(r, one), bil(r, w))
    def img_class(f, r):
        return cls[key(f(r))]
    w_perm = collections.Counter((cls[key(r)], img_class(lambda x: qmul(w, x), r)) for r in rest)
    conj_perm = collections.Counter((cls[key(r)], img_class(qconj, r)) for r in rest)
    print(f"  left multiplication by w maps classes: {sorted(set(w_perm))}")
    print(f"  quaternion conjugation maps classes:   {sorted(set(conj_perm))}")
    # ---- the two letters: R, L mod 5 generate SL(2,F5) = 2I; g = -R L^-1 has order 3
    print("  --- the founding identity inside the icosians ---")
    def m5(M):
        return tuple(x % 5 for x in M)
    def mul5(A, B):
        p, q, r, s_ = A; t, u, v, w_ = B
        return ((p*t + q*v) % 5, (p*u + q*w_) % 5, (r*t + s_*v) % 5, (r*u + s_*w_) % 5)
    R5, L5 = (1, 1, 0, 1), (1, 0, 1, 1)
    I5 = (1, 0, 0, 1)
    # generate SL(2,F5) from R5, L5 with words
    seen = {I5: ()}
    frontier = [I5]
    while frontier:
        nxt = []
        for M in frontier:
            for lab, g in (("R", R5), ("L", L5)):
                P = mul5(M, g)
                if P not in seen:
                    seen[P] = seen[M] + (lab,)
                    nxt.append(P)
        frontier = nxt
    print(f"  <R, L> mod 5 has order {len(seen)}   (SL(2,F5) = 2I: 120)")
    Linv5 = (1, 0, 4, 1)
    g5 = m5(tuple(-x for x in mul5(R5, Linv5)))          # g = -R L^-1
    g5_3 = mul5(mul5(g5, g5), g5)
    print(f"  g = -R L^-1 mod 5 = {g5}, g^3 = {g5_3}   (order 3)")
    # find unit icosians r, l of order 5 such that R -> r, L -> l extends to an isomorphism onto 2I
    units_by_key = {key(u): u for u in units}
    ord5 = [u for u in units if orders_of(u, one, key) == 5]
    iso = None
    for r in ord5:
        for l in ord5:
            # build the image of every element by its word; check well-definedness by BFS closure
            img = {I5: one}
            frontier = [I5]
            good = True
            while frontier and good:
                nxt = []
                for M in frontier:
                    for g, gi in ((R5, r), (L5, l)):
                        P = mul5(M, g)
                        Q = qmul(img[M], gi)
                        if P in img:
                            if key(img[P]) != key(Q):
                                good = False
                                break
                        else:
                            img[P] = Q
                            nxt.append(P)
                    if not good:
                        break
                frontier = nxt
            if good and len(img) == 120 and len({key(v) for v in img.values()}) == 120:
                iso = img
                break
        if iso:
            break
    assert iso is not None, "no isomorphism SL(2,F5) -> 2I found"
    gq = iso[g5]
    print(f"  an isomorphism SL(2,F5) -> 2I (unit icosians) exists; it sends g = -R L^-1 to the order-{orders_of(gq, one, key)} unit {tuple(str(c) for c in gq)}")
    print(f"  minimal polynomial check: g_q^2 + g_q + 1 = {tuple(str(c) for c in tuple(a + b + cc for a, b, cc in zip(qmul(gq, gq), gq, one)))}   (zero: g_q generates Z[omega])")
    # E6 from the founding ratio: the complement of Z[g_q]
    perp_g = [x for x in roots if bil(x, one) == 0 and bil(x, gq) == 0]
    print(f"  roots orthogonal to the Eisenstein plane {{1, g_q}} of the founding ratio: {len(perp_g)}   (E6: 72)")
    return True


def orders_of(u, one, key):
    p, n = u, 1
    while key(p) != key(one):
        p = qmul(p, u)
        n += 1
    return n


# =============================================================== (2) the coefficient systems
def part2():
    gens2, elems2 = T.sl2_2T()
    key = lambda M: tuple((x.x, x.y) for x in M.flatten())
    one = np.array([[ONE, ZERO], [ZERO, ONE]], dtype=object)
    def order_of(M):
        P, n = M, 1
        while key(P) != key(one):
            P = P.dot(M); n += 1
        return n
    Q8 = [g for g in elems2 if order_of(g) in (1, 2, 4)]
    assert len(Q8) == 8
    c0 = next(g for g in elems2 if order_of(g) == 3)
    cos_id = {key(q) for q in Q8}
    cos_w = {key(c0.dot(q)) for q in Q8}
    def chi(g):
        k = key(g)
        return ONE if k in cos_id else (OMEGA if k in cos_w else OMEGA.conj())
    # the surjections in the 2T <= SL(2,Q(omega)) model: pairs (X, Y) with the relator and generating 24
    def ev(word, X, Y, Xi, Yi):
        out = one
        for L in word:
            out = out.dot({1: X, 2: Y}[L] if L > 0 else {1: Xi, 2: Yi}[-L])
        return out
    inv = {}
    for g in elems2:
        o = order_of(g)
        P = one
        for _ in range(o - 1):
            P = P.dot(g)
        inv[key(g)] = P
    homs = []
    for X in elems2:
        for Y in elems2:
            if key(ev(S.REL, X, Y, inv[key(X)], inv[key(Y)])) == key(one):
                homs.append((X, Y))
    def generated(X, Y):
        seen = {key(one)}
        frontier = [one]
        while frontier:
            nxt = []
            for M in frontier:
                for g in (X, Y):
                    P = M.dot(g)
                    if key(P) not in seen:
                        seen.add(key(P)); nxt.append(P)
            frontier = nxt
        return len(seen)
    surj = [(X, Y) for (X, Y) in homs if generated(X, Y) == 24]
    print(f"  homomorphisms pi_1(m004) -> 2T (2T as unit quaternions over Q(omega)): {len(homs)}, surjective {len(surj)}")

    import cusped_bound as CB
    results = collections.Counter()
    rows = []
    for (X, Y) in surj:
        Xi, Yi = inv[key(X)], inv[key(Y)]
        out = {}
        for name, tw in (("2", ONE), ("2'", None), ("2''", None)):
            if name == "2":
                cx, cy = ONE, ONE
            elif name == "2'":
                cx, cy = chi(X), chi(Y)
            else:
                cx, cy = chi(X).conj(), chi(Y).conj()
            mats = {1: S.qw_scale(X, cx), 2: S.qw_scale(Y, cy)}
            invs = {1: S.qw_scale(Xi, cx.inv()), 2: S.qw_scale(Yi, cy.inv())}
            rep = S.Rep(mats, invs)
            S.check_rep(rep, [1, 2], [S.REL])
            out[name] = CB.lemma_row(rep, f"    {name:3}", quiet=True)
        N = out["2'"]['h1'] - out["2''"]['h1']
        k = (order_of(X), order_of(Y), out["2"]['h1'], out["2'"]['h1'], out["2''"]['h1'],
             out["2'"]['h0t'], out["2'"]['rank_res'], out["2''"]['h0t'], out["2''"]['rank_res'], N)
        results[k] += 1
        rows.append((X, Y, out))
    print("  (ord a, ord b, h1(2), h1(2'), h1(2''), h0(dM;2'), rank(res 2'), h0(dM;2''), rank(res 2''), N) -> count")
    for k, v in sorted(results.items()):
        print("   ", k, "->", v)
    # ---- the commutant of the Eisenstein image inside E8 > E6 x SU(3), by characters of 2T
    # 2T classes (size): 1(1), -1(1), i(6), order-6(8), order-3(8); characters on (1,-1,i,ord6,ord3)
    import cmath
    w = cmath.exp(2j * cmath.pi / 3)
    sizes = [1, 1, 6, 8, 8]
    chars = {"1": [1, 1, 1, 1, 1], "w": [1, 1, 1, w, w * w], "wb": [1, 1, 1, w * w, w],
             "3": [3, 3, -1, 0, 0], "2": [2, -2, 0, 1, -1], "2'": [2, -2, 0, w, -w * w], "2''": [2, -2, 0, w * w, -w]}
    def mult_triv(chi):
        return round(sum(sz * c for sz, c in zip(sizes, chi)).real / 24)
    def tensor(a, b):
        return [x * y for x, y in zip(a, b)]
    def conj(a):
        return [x.conjugate() if isinstance(x, complex) else x for x in a]
    def add(a, b):
        return [x + y for x, y in zip(a, b)]
    print("  --- the surviving gauge algebra in E8 > E6 x SU(3), 248 = (78,1)+(1,8)+(27,3)+(27bar,3bar) ---")
    for name, three in (("3 (irreducible, real)", chars["3"]), ("2' + w (complex)", add(chars["2'"], chars["w"])),
                        ("2 + 1 (quaternionic + trivial)", add(chars["2"], chars["1"]))):
        eight = [x - 1 for x in tensor(three, conj(three))]
        n8, n3, n3b = mult_triv(eight), mult_triv(three), mult_triv(conj(three))
        extra = 27 * n3 + 27 * n3b
        print(f"   2T -> SU(3) via {name}: invariants in (1,8): {n8}, in (27,3): {27*n3}, in (27bar,3bar): {27*n3b}"
              f"  ->  commutant = e6 + u(1)^{n8} + {extra} root vectors  ->  " +
              ("E6 exactly" if (n8, extra) == (0, 0) else ("E6 x U(1)" if extra == 0 else "larger than E6 (E7 for 2+1)")))
    return results


if __name__ == "__main__":
    print("=== (1) E6 = Z[omega]^perp inside the golden E8 (icosians), exact over Q(sqrt5) ===")
    part1()
    print("\n=== (2) the Eisenstein twists 2', 2'' of 2T on m004: the net 27-count under E8 > E6 x SU(3) ===")
    part2()
