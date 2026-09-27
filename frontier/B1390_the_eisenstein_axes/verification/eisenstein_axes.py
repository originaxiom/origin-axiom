#!/usr/bin/env python3
"""B1390 -- THE EISENSTEIN AXES: the fixed set of every orientation-preserving isometry of finite order, on m004's commensurability
class and on controls outside it.

The theorem (FINDINGS section 2).  Every member of m004's class has pi_1 inside the commensurator PGL(2, K), K = Q(sqrt-3) (Skolem-Noether),
and its cusp points are P^1(K).  An element of PGL(2, K) of order 3 has t^2 = det, so its fixed points (a - d +- t sqrt-3) / 2c lie in
P^1(K); of order 6, t^2 = 3 det, fixed points (a - d +- t sqrt-3 / 3) / 2c, again in P^1(K); of order 4, t^2 = 2 det, discriminant -t^2,
never a square in K.  Hence an isometry of order 3 or 6 fixes only proper arcs running from cusp to cusp (never a closed geodesic),
rotates every cusp such an arc enters, and, if it rotates no cusp, acts freely.  An isometry of order 4 never fixes a point on a cusp
torus.  Order 2 is unconstrained.

The instrument.  SnapPy's canonical retriangulation is an isometry invariant, so its combinatorial automorphisms are the isometries
(checked: |Aut| = |Isom|).  An automorphism g acts on each tetrahedron it maps to itself by a vertex permutation p; for g orientation-
preserving (p even), g's fixed set there is the segment joining the barycentres of p's two orbits.  A face class whose two sides g
exchanges carries the segment joining the barycentres of g's orbits on its three vertices; an edge class g maps to itself with its ends
kept is fixed pointwise.  The fixed set of g is the graph so assembled: its nodes are barycentres of g-invariant simplices, and every
incidence at an ideal vertex is an END (a fixed point on that cusp torus).  Self-tests: every interior node has degree 2 (a 1-manifold),
every component is an arc (two ends) or a closed curve (none), and the ends on each cusp torus equal |det(A - I)| of SnapPy's cusp map,
compared as multisets over the group.

Usage: python3 eisenstein_axes.py algebra
       python3 eisenstein_axes.py family            (B1186's 112 census members of the class, and the controls)
       python3 eisenstein_axes.py covers D LO HI    (ocube06_08812's degree-D covers LO..HI-1, B1386's family; D = 1: the base)"""
import random
import sys
import time
import json
import warnings
from collections import Counter
from fractions import Fraction as Fr
from pathlib import Path

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BITS = (1, 2, 4, 8)


# ================================================================ (A) the algebra, exact in K = Q(sqrt-3)
class K:
    """p + q s, s = sqrt(-3), p and q rational"""
    __slots__ = ("p", "q")

    def __init__(self, p, q=0):
        self.p, self.q = Fr(p), Fr(q)

    def __add__(self, o): o = o if isinstance(o, K) else K(o); return K(self.p + o.p, self.q + o.q)
    def __sub__(self, o): o = o if isinstance(o, K) else K(o); return K(self.p - o.p, self.q - o.q)
    def __neg__(self): return K(-self.p, -self.q)
    def __mul__(self, o):
        o = o if isinstance(o, K) else K(o)
        return K(self.p * o.p - 3 * self.q * o.q, self.p * o.q + self.q * o.p)
    __rmul__ = __mul__
    def norm(self): return self.p * self.p + 3 * self.q * self.q
    def inv(self): n = self.norm(); return K(self.p / n, -self.q / n)
    def __truediv__(self, o): o = o if isinstance(o, K) else K(o); return self * o.inv()
    def __eq__(self, o): o = o if isinstance(o, K) else K(o); return self.p == o.p and self.q == o.q
    def iszero(self): return self.p == 0 and self.q == 0


S = K(0, 1)


def is_square_in_K(x):
    """x = (u + v s)^2 = u^2 - 3 v^2 + 2 u v s: decided exactly (the norm must be a rational square, then solve)"""
    if x.iszero():
        return True
    n = x.norm()
    rn = _rat_sqrt(n)
    if rn is None:
        return False
    for sgn in (1, -1):                       # u^2 - 3 v^2 = p, u^2 + 3 v^2 = +-sqrt(N) (N(u + v s) = u^2 + 3 v^2 >= 0)
        u2 = (x.p + sgn * rn) / 2
        v2 = (sgn * rn - x.p) / 6
        if u2 < 0 or v2 < 0:
            continue
        u, v = _rat_sqrt(u2), _rat_sqrt(v2)
        if u is None or v is None:
            continue
        for su in (1, -1):
            for sv in (1, -1):
                if K(su * u, sv * v) * K(su * u, sv * v) == x:
                    return True
    return False


def _rat_sqrt(r):
    r = Fr(r)
    if r < 0:
        return None
    a, b = r.numerator, r.denominator
    ra, rb = _isqrt(a), _isqrt(b)
    return Fr(ra, rb) if ra is not None and rb is not None else None


def _isqrt(n):
    if n < 0:
        return None
    x = int(n ** 0.5)
    for y in (x - 1, x, x + 1):
        if y >= 0 and y * y == n:
            return y
    return None


def rand_K(rnd, h=6):
    return K(Fr(rnd.randint(-h, h), rnd.randint(1, 3)), Fr(rnd.randint(-h, h), rnd.randint(1, 3)))


def run_algebra():
    rnd = random.Random(1390)
    print("=== (A) the fixed points of elliptic elements of PGL(2, K), K = Q(sqrt-3), exact ===")
    print("order k in PGL(2) <=> eigenvalue ratio a primitive k-th root of unity <=> t^2 = (2 + 2 cos(2 pi/k)) det:"
          " k = 2: t = 0; 3: t^2 = det; 4: t^2 = 2 det; 6: t^2 = 3 det.")
    print("fixed points of [[a, b], [c, d]]: z = (a - d +- sqrt(D)) / 2c, D = t^2 - 4 det:"
          " k = 3: D = -3 t^2 = (t s)^2; k = 6: D = -t^2/3 = (t s/3)^2; k = 4: D = -t^2, a square iff -1 is: never in K.")
    assert not is_square_in_K(K(-1)), "-1 a square in Q(sqrt-3)?"
    assert is_square_in_K(K(-3)) and is_square_in_K(K(-3) * K(5) * K(5))
    tally = Counter()
    for k, factor in ((3, Fr(1)), (6, Fr(1, 3)), (4, Fr(1, 2)), (2, None)):
        for _ in range(2000):
            a, c, d = rand_K(rnd), rand_K(rnd), rand_K(rnd)
            if c.iszero():
                continue
            if k == 2:
                d = -a
                b = rand_K(rnd)
            else:
                t = a + d
                if t.iszero():
                    continue
                b = (a * d - factor * (t * t)) / c          # makes t^2 = det / factor, i.e. order k
            det = a * d - b * c
            if det.iszero():
                continue
            t = a + d
            D = t * t - 4 * det
            sq = is_square_in_K(D)
            if k in (3, 6):
                root = t * S if k == 3 else t * S / 3
                assert root * root == D
                for r in (root, -root):
                    z = (a - d + r) / (2 * c)
                    assert (c * z * z + (d - a) * z - b).iszero(), "not a fixed point"
                assert sq
            if k == 4:
                assert (D + t * t).iszero() and not sq
            tally[(k, sq)] += 1
    for k in (3, 6, 4, 2):
        print("  order %d: %4d random elements; fixed points in P^1(K) for %4d, outside for %4d"
              % (k, tally[(k, True)] + tally[(k, False)], tally[(k, True)], tally[(k, False)]))
    assert tally[(3, False)] == tally[(6, False)] == tally[(4, True)] == 0 and tally[(2, True)] > 0 and tally[(2, False)] > 0
    print("  -> orders 3 and 6: always cusp points (the axis runs cusp to cusp); order 4: never; order 2: either, as the theorem says.")
    print("  control: over Q(i) an order-3 element has D = -3 t^2, a square in Q(i) iff -3 is: never -- so order-3 axes there end off the"
          " cusp set and closed fixed geodesics can occur (the Borromean control, part B).")


# ================================================================ (B) the fixed-set instrument
class FixedSets:
    def __init__(self, M):
        import snappy
        from snappy.snap import t3mlite
        self.M = M
        self.T = M.canonical_retriangulation()
        self.mc = t3mlite.Mcomplex(self.T)
        self.tets = self.mc.Tetrahedra
        self.n = len(self.tets)
        ci = self.T._get_cusp_indices_and_peripheral_curve_data()[0]
        self.vcusp = {}
        for v in self.mc.Vertices:
            ks = {ci[c.Tetrahedron.Index][BITS.index(c.Subsimplex)] for c in v.Corners}
            assert len(ks) == 1, "a vertex class with two cusp indices"
            self.vcusp[v.Index] = ks.pop()
        self.finite = sum(1 for k in self.vcusp.values() if k < 0)
        self.edge_end0 = {}
        for e in self.mc.Edges:
            c = e.Corners[0]
            self._walk_edge(c.Tetrahedron, c.Subsimplex, c.Subsimplex & -c.Subsimplex)
        self.auts = []
        for a in self.mc.isomorphisms_to(self.mc):
            self.auts.append(tuple((a[i][0].Index, tuple(a[i][1].tuple())) for i in range(self.n)))
        self.ident = tuple((i, (0, 1, 2, 3)) for i in range(self.n))

    def _walk_edge(self, t, eb, x):
        stack = [(t, eb, x)]
        while stack:
            t, eb, x = stack.pop()
            key = (t.Index, eb)
            if key in self.edge_end0:
                assert self.edge_end0[key] == x, "an edge identified with itself reversed"
                continue
            self.edge_end0[key] = x
            for F in (14, 13, 11, 7):
                if (F & eb) == eb:
                    g = t.Gluing[F]
                    stack.append((t.Neighbor[F], g.image(eb), g.image(x)))

    # ---- automorphism arithmetic
    def compose(self, a2, a1):
        """a2 after a1"""
        out = []
        for i in range(self.n):
            s, p = a1[i]
            s2, p2 = a2[s]
            out.append((s2, tuple(p2[p[j]] for j in range(4))))
        return tuple(out)

    def order(self, a):
        k, x = 1, a
        while x != self.ident:
            x = self.compose(a, x)
            k += 1
            assert k <= 1000
        return k

    @staticmethod
    def parity(p):
        inv = sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j])
        return inv % 2

    def orientation(self, a):
        par = {self.parity(p) for (_, p) in a}
        assert len(par) == 1, "mixed parities"
        return +1 if par.pop() == 0 else -1

    @staticmethod
    def img_bits(p, bits):
        out = 0
        for j in range(4):
            if bits & BITS[j]:
                out |= BITS[p[j]]
        return out

    def cusp_perm(self, a):
        perm = {}
        for v in self.mc.Vertices:
            k = self.vcusp[v.Index]
            if k < 0:
                continue
            c = v.Corners[0]
            s, p = a[c.Tetrahedron.Index]
            w = self.tets[s].Class[self.img_bits(p, c.Subsimplex)]
            perm[k] = self.vcusp[w.Index]
        return perm

    # ---- the fixed set
    def fixed_set(self, a):
        adj = {}
        ends = Counter()
        counter = [0]

        def node_of_vertex(v):
            k = self.vcusp[v.Index]
            if k >= 0:
                counter[0] += 1
                ends[k] += 1
                return ("end", k, counter[0])
            return ("V", v.Index)

        def link(x, y):
            adj.setdefault(x, []).append(y)
            adj.setdefault(y, []).append(x)

        def node_of(t, bits):
            m = bin(bits).count("1")
            cl = t.Class[bits]
            if m == 1:
                return node_of_vertex(cl)
            return ("E" if m == 2 else "F", cl.Index)

        anomalies = []
        # invariant tetrahedra
        for i, (s, p) in enumerate(a):
            if s != i:
                continue
            seen, orbits = set(), []
            for j in range(4):
                if j in seen:
                    continue
                orb, x = [], j
                while x not in orb:
                    orb.append(x)
                    x = p[x]
                seen.update(orb)
                orbits.append(orb)
            if len(orbits) == 4:
                anomalies.append(("tet fixed pointwise", i))
                continue
            if len(orbits) != 2:
                anomalies.append(("tet with %d orbits" % len(orbits), i))
                continue
            for orb in orbits:
                if len(orb) == 4:
                    anomalies.append(("4-cycle", i))
                    continue
                link(("T", i), node_of(self.tets[i], sum(BITS[j] for j in orb)))
        # face classes whose two sides are exchanged
        for f in self.mc.Faces:
            c0, c1 = f.Corners
            t0, F0 = c0.Tetrahedron, c0.Subsimplex
            s, p = a[t0.Index]
            if (s, self.img_bits(p, F0)) != (c1.Tetrahedron.Index, c1.Subsimplex):
                continue
            g = t0.Gluing[F0]
            back = {g.image(BITS[j]): j for j in range(4) if F0 & BITS[j]}
            verts = [j for j in range(4) if F0 & BITS[j]]
            sigma = {j: back[BITS[p[j]]] for j in verts}
            seen, orbits = set(), []
            for j in verts:
                if j in seen:
                    continue
                orb, x = [], j
                while x not in orb:
                    orb.append(x)
                    x = sigma[x]
                seen.update(orb)
                orbits.append(orb)
            if len(orbits) != 2:
                anomalies.append(("side-exchanged face with %d orbits" % len(orbits), f.Index))
                continue
            for orb in orbits:
                link(("F", f.Index), node_of(t0, sum(BITS[j] for j in orb)))
        # edge classes mapped to themselves with their ends kept: fixed pointwise
        for e in self.mc.Edges:
            c = e.Corners[0]
            t, eb = c.Tetrahedron, c.Subsimplex
            s, p = a[t.Index]
            eb2 = self.img_bits(p, eb)
            if self.tets[s].Class[eb2] is not e:
                continue
            x = self.edge_end0[(t.Index, eb)]
            if self.edge_end0[(s, eb2)] == self.img_bits(p, x):
                y = eb ^ x
                link(("E", e.Index), node_of_vertex(t.Class[x]))
                link(("E", e.Index), node_of_vertex(t.Class[y]))
        # components
        arcs = closed = 0
        visited = set()
        for x in adj:
            if x in visited:
                continue
            comp, stack = [], [x]
            visited.add(x)
            while stack:
                y = stack.pop()
                comp.append(y)
                for z in adj[y]:
                    if z not in visited:
                        visited.add(z)
                        stack.append(z)
            ne = sum(1 for y in comp if y[0] == "end")
            bad = [y for y in comp if (y[0] == "end" and len(adj[y]) != 1) or (y[0] != "end" and len(adj[y]) != 2)]
            if bad:
                anomalies.append(("not a 1-manifold", bad[:3]))
            if ne == 2:
                arcs += 1
            elif ne == 0:
                closed += 1
            else:
                anomalies.append(("component with %d ends" % ne, comp[:3]))
        return arcs, closed, dict(ends), anomalies


def analyse(label, M):
    FS = FixedSets(M)
    G = M.symmetry_group()
    assert len(FS.auts) == G.order(), "%s: |Aut| %d != |Isom| %d" % (label, len(FS.auts), G.order())
    rows = []
    for a in FS.auts:
        k = FS.order(a)
        o = FS.orientation(a)
        if o == -1:
            rows.append((k, o, None))
            continue
        perm = FS.cusp_perm(a)
        fixed_cusps = [c for c in perm if perm[c] == c]
        arcs, closed, ends, anomalies = FS.fixed_set(a) if k > 1 else (0, 0, {}, [])
        rotated = [c for c in fixed_cusps if ends.get(c, 0) > 0]
        rows.append((k, o, dict(arcs=arcs, closed=closed, ends=ends, rotated=rotated, fixed_cusps=fixed_cusps,
                                cycled=[c for c in perm if perm[c] != c], anomalies=anomalies)))
    # the cross-check: per orientation-preserving element, the fixed-point counts on the cusp tori it fixes, as a multiset over the
    # group -- SnapPy's |det(A - I)| from its cusp maps against the instrument's ends
    snappy_or = Counter()
    for iso in G.isometries():
        maps, imgs = iso.cusp_maps(), iso.cusp_images()
        dets, row = [], []
        for c, im in enumerate(imgs):
            m = maps[c]
            A = [[int(m[0, 0]), int(m[0, 1])], [int(m[1, 0]), int(m[1, 1])]]
            dets.append(A[0][0] * A[1][1] - A[0][1] * A[1][0])
            if im == c:
                row.append(abs((A[0][0] - 1) * (A[1][1] - 1) - A[0][1] * A[1][0]))
        if dets[0] == 1:
            snappy_or[tuple(sorted(row))] += 1
    comb_or = Counter()
    for (k, o, r) in rows:
        if o == 1:
            comb_or[tuple(sorted(r["ends"].get(c, 0) for c in r["fixed_cusps"]))] += 1
    return FS, rows, snappy_or == comb_or


def summarise(label, M, FS, rows, agree, out):
    for (k, o, r) in rows:
        if o != 1 or k == 1:
            continue
        key = k
        out.setdefault(key, Counter())
        c = out[key]
        c["elements"] += 1
        c["closed components"] += r["closed"]
        c["arc components"] += r["arcs"]
        c["elements with a closed fixed curve"] += (r["closed"] > 0)
        c["elements rotating no cusp"] += (not r["rotated"])
        c["of those, acting freely"] += (not r["rotated"] and r["arcs"] == 0 and r["closed"] == 0)
        c["anomalies"] += len(r["anomalies"])
        if k in (3, 6) and not r["rotated"]:
            c["no-rotation elements with a translated cusp"] += bool(r["fixed_cusps"])
    return out


def fmt(out):
    lines = []
    for k in sorted(out):
        c = out[k]
        lines.append("    order %d: %5d elements | arcs %5d, closed curves %4d (elements with one: %d) | rotating no cusp %d, of which free %d"
                     " | anomalies %d" % (k, c["elements"], c["arc components"], c["closed components"],
                                          c["elements with a closed fixed curve"], c["elements rotating no cusp"],
                                          c["of those, acting freely"], c["anomalies"]))
    return "\n".join(lines)


def nonintegral_witness(M, maxlen=3):
    """a word g of length <= maxlen in the generators (and inverses) with tr(g^2) not in Z[omega], or None.  tr(g^2) lies in the invariant
    trace field Q(sqrt-3); integrality of tr(g^2) on these words makes tr(g) integral on them, and by the trace-ring lemma (generated by
    the traces of products of at most three generators) all of tr(Gamma) -- with the shape field Q(sqrt-3), that is arithmeticity
    (Maclachlan-Reid Thm 8.3.2).  One non-integral value is a witness of non-arithmeticity."""
    from mpmath import mp, mpf, sqrt as msqrt
    import itertools
    mp.dps = 50
    G = M.fundamental_group()
    gens = G.generators()
    letters = gens + [g.upper() for g in gens]
    for L in range(1, maxlen + 1):
        for w in itertools.product(letters, repeat=L):
            w = "".join(w)
            A = G.SL2C(w)
            A2 = A * A
            tt = A2[0, 0] + A2[1, 1]
            re = mpf(str(tt.real()).replace(" ", ""))
            im = mpf(str(tt.imag()).replace(" ", ""))
            y = 2 * im / msqrt(3)
            x = re + y / 2                                         # tr(g^2) = x + y omega
            fx, fy = Fr(mp.nstr(x, 45)).limit_denominator(10 ** 6), Fr(mp.nstr(y, 45)).limit_denominator(10 ** 6)
            tol = mpf(10) ** -25
            assert abs(mpf(fx.numerator) / fx.denominator - x) < tol * max(1, abs(x)), (w, str(tt))
            assert abs(mpf(fy.numerator) / fy.denominator - y) < tol * max(1, abs(y)), (w, str(tt))
            if fx.denominator > 1 or fy.denominator > 1:
                return w, fx + fy * Fr(-1, 2), fy                   # (word, rational part, sqrt(-3)/2-coefficient)
    return None


def run_family():
    import snappy
    t0 = time.time()
    fam = json.load(open(ROOT / "frontier" / "B1186_family_is_112" / "verification" / "family_census.json"))
    members = fam["members_B"]
    regular = set(fam["members_A"])
    print("=== (B) B1186's %d census members (shape field in Q(sqrt-3)): arithmeticity, and the fixed set of every orientation-"
          "preserving isometry ===" % len(members))
    nonarith = {}
    for name in members:
        w = nonintegral_witness(snappy.ManifoldHP(name))
        if w:
            nonarith[name] = w
    print("  non-integral traces (non-arithmetic, so NOT commensurable with m004): %d of %d, all non-regular: %s"
          % (len(nonarith), len(members), all(n not in regular for n in nonarith)))
    for n, (w, a, b) in nonarith.items():
        print("    %-11s tr(%s^2) = %s + %s sqrt(-3)/2... in Q(sqrt-3) but not integral" % (n, w, a, b))
    print("  arithmetic (integral traces; commensurable with m004): %d = %d regular + %d non-regular"
          % (len(members) - len(nonarith), len(regular), len(members) - len(nonarith) - len(regular)))
    out = {True: {}, False: {}}
    disagree, finite_members, detail = [], 0, []
    for name in members:
        M = snappy.Manifold(name)
        FS, rows, agree = analyse(name, M)
        if not agree:
            disagree.append(name)
        ar = name not in nonarith
        finite_members += (FS.finite > 0 and ar)
        summarise(name, M, FS, rows, agree, out[ar])
        for (k, o, r) in rows:
            if o == 1 and k > 1:
                detail.append((name, ar, k, len(r["rotated"]), r["arcs"], r["closed"], FS.finite))
    print("  the arithmetic members (%d):" % (len(members) - len(nonarith)))
    print(fmt(out[True]))
    print("  the non-arithmetic members (%d):" % len(nonarith))
    print(fmt(out[False]))
    print("  arithmetic members whose canonical retriangulation has finite vertices (where a closed order-3 fixed curve is"
          " combinatorially possible): %d; their order-3/6 elements: %d, closed fixed curves among them: %d"
          % (finite_members, sum(1 for d in detail if d[1] and d[2] in (3, 6) and d[6] > 0),
             sum(d[5] for d in detail if d[1] and d[2] in (3, 6) and d[6] > 0)))
    print("  SnapPy's fixed-point counts on the cusp tori agree with the instrument's ends on %d of %d members%s"
          % (len(members) - len(disagree), len(members), "" if not disagree else " (disagree: %s)" % disagree))
    assert not disagree
    A = out[True]
    for k in (3, 6):
        assert A[k]["closed components"] == 0 and A[k]["anomalies"] == 0
        assert A[k]["elements rotating no cusp"] == A[k]["of those, acting freely"]
    assert A[4]["arc components"] == 0
    for k in list(out[True]) + list(out[False]):
        if k not in (2, 3, 4, 6):
            for ar in (True, False):
                if k in out[ar]:
                    assert out[ar][k]["arc components"] == out[ar][k]["closed components"] == 0
    exc = sorted({d[0] for d in detail if d[2] in (3, 6) and d[5] > 0})
    print("  -> arithmetic members: no order-3/6 isometry fixes a closed curve, every one rotating no cusp acts freely, order 4 fixes no"
          " arc, and orders 5, 8, 10 act freely -- as the theorem says.  Order-3/6 closed fixed curves in the whole family: on %s only"
          " (%s)." % (exc, "non-arithmetic" if all(e in nonarith for e in exc) else "ARITHMETIC -- the theorem fails"))
    assert all(e in nonarith for e in exc)
    for n in ("s960", "o10_143602"):
        rows = [(d[2], d[3], d[4], d[5]) for d in detail if d[0] == n and d[2] in (3, 6)]
        print("  %s (%s): order-3/6 elements (order, rotated cusps, arcs, closed curves) = %s"
              % (n, "arithmetic" if n not in nonarith else "non-arithmetic", rows))
    # ---- controls
    print("\n=== (B') controls ===")
    ctl = [("L6a4 (the Borromean rings; Q(i), outside the class)", "L6a4"),
           ("m004 (the class's own involutions)", "m004"),
           ("L5a1 (the Whitehead link; Q(i))", "L5a1")]
    for lab, name in ctl:
        M = snappy.Manifold(name)
        FS, rows, agree = analyse(name, M)
        o = summarise(name, M, FS, rows, agree, {})
        print("  %s: |Isom| %d, finite vertices %d, fixed-point counts agree with SnapPy: %s" % (lab, len(FS.auts), FS.finite, agree))
        print(fmt(o))
    print("  outside the family, the orientable census up to 7 tetrahedra: order-3 isometries and their fixed sets")
    fam_set = set(members)
    tot, withc, norot, norot_free, norot_closed = 0, 0, 0, 0, 0
    examples = []
    skipped = 0
    for ntet in range(1, 8):
        for M in snappy.OrientableCuspedCensus(num_tets=ntet):
            if M.name() in fam_set:
                continue
            try:
                if M.symmetry_group().order() % 3:
                    continue
                FS, rows, agree = analyse(M.name(), M)
            except (AssertionError, ValueError, RuntimeError):
                skipped += 1
                continue
            for (k, o, r) in rows:
                if o == 1 and k == 3:
                    tot += 1
                    withc += r["closed"] > 0
                    if not r["rotated"]:
                        norot += 1
                        norot_free += (r["arcs"] == 0 and r["closed"] == 0)
                        norot_closed += (r["closed"] > 0)
                    if r["closed"] and len(examples) < 6:
                        examples.append((M.name(), len(r["rotated"]), r["arcs"], r["closed"]))
    print("    order-3 elements: %d; with a closed fixed curve: %d; rotating no cusp: %d (free %d, with a closed fixed curve %d);"
          " manifolds skipped (no symmetry group or canonical retriangulation): %d" % (tot, withc, norot, norot_free, norot_closed, skipped))
    print("    first examples (name, rotated cusps, arcs, closed curves): %s" % examples)
    assert withc > 0
    print("  -> the instrument sees closed order-3 fixed curves wherever they exist; in the arithmetic class there are none.")
    print("(%.0fs)" % (time.time() - t0))


def run_covers(d, lo, hi):
    import snappy
    t0 = time.time()
    base = snappy.Manifold("o10_150725").covers(3)[4]
    if d == 1:
        cands = [("ocube06_08812", base)]
    else:
        covs = base.covers(d)
        hi = min(hi, len(covs))
        cands = [("cube~%d.%d" % (d, i), covs[i]) for i in range(lo, hi)]
    print("=== (C) B1386's family: %s ===" % (", ".join(c[0] for c in cands[:3]) + (" ... (%d members)" % len(cands) if len(cands) > 3 else "")))
    out, disagree, fin, hexfree = {}, [], 0, []
    for name, M in cands:
        FS, rows, agree = analyse(name, M)
        if not agree:
            disagree.append(name)
        fin += FS.finite > 0
        summarise(name, M, FS, rows, agree, out)
        shapes = M.cusp_info("shape")
        for (k, o, r) in rows:
            if o == 1 and k == 3 and not r["rotated"] and r["fixed_cusps"]:
                hexfree.append((name, tuple(r["fixed_cusps"]), r["arcs"] + r["closed"]))
    print(fmt(out))
    print("  members with finite vertices in the canonical retriangulation: %d of %d; fixed-point counts agree with SnapPy on %d"
          % (fin, len(cands), len(cands) - len(disagree)))
    print("  order-3 elements rotating no cusp but translating one: %d, fixed-set components on them: %d"
          % (len(hexfree), sum(h[2] for h in hexfree)))
    assert not disagree
    for k in (3, 6):
        if k in out:
            assert out[k]["closed components"] == 0 and out[k]["anomalies"] == 0
            assert out[k]["elements rotating no cusp"] == out[k]["of those, acting freely"]
    print("(%.0fs)" % (time.time() - t0))


if __name__ == "__main__":
    what = sys.argv[1]
    if what == "algebra":
        run_algebra()
    elif what == "family":
        run_family()
    elif what == "covers":
        run_covers(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    print("DONE")
