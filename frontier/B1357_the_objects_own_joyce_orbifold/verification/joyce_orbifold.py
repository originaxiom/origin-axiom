#!/usr/bin/env python3
"""B1357 — the object's own Joyce orbifold: (T^3 x H/Lambda) / (Pi x| 2T), Lambda the Hurwitz order.

The E_6 fibre C^2/2T is compactified by the Hurwitz torus T^4 = H/Lambda (the D_4-lattice torus), on which 2T acts by left
multiplication; the Hantzsche-Wendt group Pi acts on T^3 = R^3/Z^3 affinely and on T^4 by right multiplication by the lifts
l in Q_8 of its holonomy (the SO(4) c G_2 element (l, r) acts on Im H + H as (x, y) -> (l x l^, r y l^), B1356); the deck adds
(l0, 1) with l0 = (1+i+j+k)/2 and the P2_1 3 rotation.  Everything is exact (Fractions; sympy for ranks).

Stage 1  the singular points of T^4/2T: fixed points of every g in 2T on H/Lambda, their stabilisers, the 2T-orbits, the
          orbifold Euler characteristic and the Euler characteristic of the minimal resolution (24 = K3).
Stage 2  the seven-dimensional loci of the cover orbifold and of the descent: how Q_8 (right multiplication) and l0 permute
          the singular orbits; each locus is T^3 / (stabiliser subgroup) — identified by its holonomy image and covering
          degree over Y_3 (V_4: Hantzsche-Wendt; Z_2: the dicosm; 1: T^3); the fibre monodromy on the root lattice.
Stage 3  b_2 and b_3 of the orbifolds from invariant forms (the point group on Lambda^2 R^7 and Lambda^3 R^7), the invariant
          vectors (spinor count), the deck's action on the invariant 3-forms.
Stage 4  rigidity: for each locus the invariant part of R^3 under the locus's holonomy (the hyperkaehler rotation) — the
          resolution/deformation parameter of C^2/Gamma along it lives in h(Gamma) x (R^3)^{hol}; Joyce's count of what a
          resolution would add to b_2 and b_3 where it is allowed.
Stage 5  the descent's collision loci along the knot: fixed sets on T^4 of y -> g y l0^ for g in 2T (2-tori), compact.
"""
from fractions import Fraction as Fr
import itertools, sys
from collections import Counter, defaultdict
import sympy

class Q:
    __slots__ = ("a", "b", "c", "d")
    def __init__(self, a, b=0, c=0, d=0):
        self.a, self.b, self.c, self.d = Fr(a), Fr(b), Fr(c), Fr(d)
    def __mul__(s, o):
        return Q(s.a*o.a - s.b*o.b - s.c*o.c - s.d*o.d,
                 s.a*o.b + s.b*o.a + s.c*o.d - s.d*o.c,
                 s.a*o.c - s.b*o.d + s.c*o.a + s.d*o.b,
                 s.a*o.d + s.b*o.c - s.c*o.b + s.d*o.a)
    def __add__(s, o):
        return Q(s.a+o.a, s.b+o.b, s.c+o.c, s.d+o.d)
    def __sub__(s, o):
        return Q(s.a-o.a, s.b-o.b, s.c-o.c, s.d-o.d)
    def __neg__(s):
        return Q(-s.a, -s.b, -s.c, -s.d)
    def conj(s):
        return Q(s.a, -s.b, -s.c, -s.d)
    def norm2(s):
        return s.a*s.a + s.b*s.b + s.c*s.c + s.d*s.d
    def tup(s):
        return (s.a, s.b, s.c, s.d)
    def __eq__(s, o):
        return s.tup() == o.tup()
    def __hash__(s):
        return hash(s.tup())
    def __repr__(s):
        return "(" + ",".join(str(x) for x in s.tup()) + ")"
    def scale(s, k):
        return Q(s.a*k, s.b*k, s.c*k, s.d*k)

ONE = Q(1); I = Q(0, 1); J = Q(0, 0, 1); K = Q(0, 0, 0, 1); ZERO = Q(0)
H2 = Q(Fr(1, 2), Fr(1, 2), Fr(1, 2), Fr(1, 2))

def hurwitz_units():
    U = []
    for i in range(4):
        for s in (1, -1):
            v = [0] * 4; v[i] = s; U.append(Q(*v))
    for signs in itertools.product((1, -1), repeat=4):
        U.append(Q(*[Fr(s, 2) for s in signs]))
    return U

TT = hurwitz_units()
def order(g):
    m = g; n = 1
    while m != ONE:
        m = m * g; n += 1
    return n

# Lambda coordinates: y = a*1 + b*i + c*j + d*h, h = (1+i+j+k)/2  ->  (x0,x1,x2,x3) = (a + d/2, b + d/2, c + d/2, d/2)
def to_lambda_coords(y):
    d = 2 * y.d
    return (y.a - y.d, y.b - y.d, y.c - y.d, d)
def from_lambda_coords(a, b, c, d):
    return Q(a + d/2, b + d/2, c + d/2, d/2)
def reduce_mod_lambda(y):
    a, b, c, d = to_lambda_coords(y)
    r = tuple(x - (x.numerator // x.denominator) for x in (a, b, c, d))
    return from_lambda_coords(*r)
def in_lambda(y):
    return all(x.denominator == 1 for x in to_lambda_coords(y))

def stage_1():
    print("=" * 100)
    print("STAGE 1 — the singular points of T^4/2T, T^4 = H/Lambda (Hurwitz), 2T by left multiplication")
    print("=" * 100)
    # every left multiplication by a Hurwitz unit preserves Lambda (the order is closed under multiplication)
    basis = [ONE, I, J, H2]
    ok = all(in_lambda(g * b) and in_lambda(b * g) for g in TT for b in basis)
    print(f"  left and right multiplication by the 24 units preserve Lambda: {ok}")
    D = 12
    grid = [Fr(k, D) for k in range(D)]
    candidates = [from_lambda_coords(a, b, c, d) for a in grid for b in grid for c in grid for d in grid]
    fixed = {}   # y -> stabiliser (set of g)
    counts = {}
    for g in TT:
        if g == ONE:
            continue
        F = [y for y in candidates if in_lambda(g * y - y)]
        counts[g] = len(F)
        for y in F:
            fixed.setdefault(y, set()).add(g)
    by_order = defaultdict(list)
    for g, n in counts.items():
        by_order[order(g)].append(n)
    print("  fixed points on T^4 of the non-identity elements, by order: " +
          ", ".join(f"order {o}: {sorted(set(v))} ({len(v)} elements)" for o, v in sorted(by_order.items())))
    # the Lefschetz count |Fix(g)| = |det(g - 1)| = N(g-1)^2
    lef = all(counts[g] == (g - ONE).norm2() ** 2 for g in counts)
    print(f"  |Fix(g)| = N(g - 1)^2 for every g (Lefschetz): {lef}")
    chi_orb = Fr(sum(counts.values()), 24)
    print(f"  chi(T^4/2T) = (1/24) sum_g chi(Fix g) = {chi_orb}")
    # stabilisers and orbits
    pts = {y: frozenset(S | {ONE}) for y, S in fixed.items()}
    def stab_type(S):
        n = len(S)
        return {2: "Z2 (A1)", 3: "Z3 (A2)", 4: "Z4 (A3)", 6: "Z6 (A5)", 8: "Q8 (D4)", 24: "2T (E6)"}.get(n, f"order {n}")
    orbits = []
    seen = set()
    for y in pts:
        if y in seen:
            continue
        orb = set(reduce_mod_lambda(g * y) for g in TT)
        seen |= orb
        orbits.append((y, orb))
    types = Counter(stab_type(pts[y]) for y, _ in orbits)
    print(f"  singular points of T^4 (non-identity fixed points): {len(pts)}; 2T-orbits: {len(orbits)}: {dict(types)}")
    rank = {"Z2 (A1)": 1, "Z3 (A2)": 2, "Z4 (A3)": 3, "Z6 (A5)": 5, "Q8 (D4)": 4, "2T (E6)": 6}
    chi_res = chi_orb + sum(rank[stab_type(pts[y])] for y, _ in orbits)
    print(f"  chi(minimal resolution) = chi(T^4/2T) + sum of ranks = {chi_orb} + {sum(rank[stab_type(pts[y])] for y, _ in orbits)} = {chi_res}"
          f"  (K3: {chi_res == 24})")
    for y, orb in sorted(orbits, key=lambda t: -len(pts[t[0]])):
        print(f"    representative {y}: stabiliser {stab_type(pts[y])}, orbit size {len(orb)}")
    return pts, orbits

def right_mult_perm(l, orbits, pts):
    """the permutation of the 2T-orbits induced by y -> y l^ (must map singular points to singular points)."""
    idx = {}
    for n, (y, orb) in enumerate(orbits):
        for z in orb:
            idx[z] = n
    perm = []
    for n, (y, orb) in enumerate(orbits):
        z = reduce_mod_lambda(y * l.conj())
        assert z in idx, "right multiplication must preserve the singular set"
        perm.append(idx[z])
    return tuple(perm)

def stage_2(pts, orbits):
    print("\n" + "=" * 100)
    print("STAGE 2 — the seven-dimensional loci: the Hantzsche-Wendt lifts Q_8 and the deck l0 acting by right multiplication")
    print("=" * 100)
    l0 = H2
    labels = []
    for y, orb in orbits:
        n = len(pts[y])
        labels.append({2: "A1", 3: "A2", 8: "D4", 24: "E6"}[n])
    print(f"  orbits (index: type): {list(enumerate(labels))}")
    perms = {}
    for name, l in (("i", I), ("j", J), ("k", K), ("l0", l0)):
        perms[name] = right_mult_perm(l, orbits, pts)
        print(f"  right multiplication by {name}^ permutes the orbits as {perms[name]}")
    # the cover: Pi acts through V_4 = <i, j> (mod sign) on the orbit set; orbits of that action, with stabilisers
    def group_orbits(gens, n):
        seen = [False] * n
        out = []
        for s in range(n):
            if seen[s]:
                continue
            orb = {s}; frontier = [s]
            while frontier:
                x = frontier.pop()
                for p in gens:
                    z = p[x]
                    if z not in orb:
                        orb.add(z); frontier.append(z)
            for x in orb:
                seen[x] = True
            out.append(sorted(orb))
        return out
    n = len(orbits)
    def holonomy_stab(s, gens):
        # the subgroup of V_4 = {1, i, j, k} (as permutations) fixing s
        V = {"1": tuple(range(n)), "i": gens["i"], "j": gens["j"], "k": gens["k"]}
        return [name for name, p in V.items() if p[s] == s]
    cover_loci = group_orbits([perms["i"], perms["j"]], n)
    print("\n  THE COVER (T^3 x T^4)/(Pi x| 2T): loci = Pi-orbits of the singular orbits; each locus is T^3 / Pi_[y]")
    identify = {4: "Hantzsche-Wendt (holonomy V_4, b_1 = 0)", 2: "the dicosm (holonomy Z_2, b_1 = 1)", 1: "T^3 (b_1 = 3)"}
    summary_cover = []
    for L in cover_loci:
        s = L[0]
        hol = holonomy_stab(s, perms)
        deg = len(L)
        print(f"    type {labels[s]}: orbit of singular orbits {L} (covering degree {deg} over Y_3), holonomy image {hol} "
              f"-> locus = {identify[len(hol)]}")
        summary_cover.append((labels[s], deg, len(hol)))
    # the descent: add l0
    desc_loci = group_orbits([perms["i"], perms["j"], perms["l0"]], n)
    print("\n  THE DESCENT (T^3 x T^4)/(P2_1 3 x| 2T): loci over the singular orbits (the collision loci along the knot are stage 5)")
    summary_desc = []
    for L in desc_loci:
        s = L[0]
        # stabiliser in T = A_4 generated by i, j, l0 as permutations: enumerate the group
        gens = [perms["i"], perms["j"], perms["l0"]]
        G = {tuple(range(n))}
        frontier = list(G)
        while frontier:
            new = []
            for a in frontier:
                for b in gens:
                    c = tuple(b[a[x]] for x in range(n))
                    if c not in G:
                        G.add(c); new.append(c)
            frontier = new
        stab = [p for p in G if p[s] == s]
        print(f"    type {labels[s]}: orbit {L} (covering degree {len(L)} over S^3(4_1;3)), point-group image of the stabiliser has "
              f"order {len(stab)} of {len(G)} -> locus = T^3 / (a subgroup of P2_1 3 of index {len(L)})")
        summary_desc.append((labels[s], len(L), len(stab)))
    # the fibre monodromy on the root lattice: for each cover locus, the elements g of 2T with y l^ = g y (mod Lambda) for the
    # stabilising l's; g modulo the stabiliser Gamma_y; whether g normalises Gamma_y through inner elements only
    print("\n  fibre monodromy along each cover locus: the g in 2T with y l^ = g y for the l in the holonomy stabiliser")
    for L in cover_loci:
        s = L[0]
        y = orbits[s][0]
        Gy = pts[y]
        mono = {}
        for name, l in (("i", I), ("j", J), ("k", K)):
            if perms[name][s] != s:
                continue
            z = reduce_mod_lambda(y * l.conj())
            gs = [g for g in TT if reduce_mod_lambda(g * y) == z]
            mono[name] = gs
        desc = []
        for name, gs in mono.items():
            orders = sorted(set(order(g) for g in gs))
            in_stab_times_centre = all((g in Gy) or (-g in Gy) for g in gs)
            desc.append(f"{name}: g of orders {orders}, in Gamma_y.{{+-1}}: {in_stab_times_centre}")
        print(f"    type {labels[s]} (stabiliser order {len(Gy)}): " + "; ".join(desc))
    return perms, cover_loci, desc_loci, labels, summary_cover, summary_desc

# ---- the seven-dimensional point group and invariant forms ----
def mat7_of(l, r):
    """(x, y) -> (l x l^, r y l^) on Im H + H, as a rational 7x7 matrix (columns = images of the basis)."""
    basis = [(I, ZERO), (J, ZERO), (K, ZERO), (ZERO, ONE), (ZERO, I), (ZERO, J), (ZERO, K)]
    cols = []
    for (x, y) in basis:
        xi = l * x * l.conj(); yi = r * y * l.conj()
        cols.append([xi.b, xi.c, xi.d, yi.a, yi.b, yi.c, yi.d])
    return sympy.Matrix(7, 7, lambda i, j: cols[j][i])

def exterior_power_matrix(M, k):
    n = M.shape[0]
    idx = list(itertools.combinations(range(n), k))
    pos = {c: i for i, c in enumerate(idx)}
    E = sympy.zeros(len(idx), len(idx))
    for j, cols in enumerate(idx):
        sub = M[:, list(cols)]
        for i, rows in enumerate(idx):
            E[i, j] = sub[list(rows), :].det()
    return E

def invariant_dim(gens, k):
    mats = [exterior_power_matrix(M, k) if k > 1 else M for M in gens]
    N = mats[0].shape[0]
    A = sympy.Matrix.vstack(*[m - sympy.eye(N) for m in mats])
    return N - A.rank(), A

def stage_3():
    print("\n" + "=" * 100)
    print("STAGE 3 — the point group on Lambda^2 R^7 and Lambda^3 R^7: b_2, b_3 of the flat orbifolds; invariant vectors")
    print("=" * 100)
    l0 = H2
    fibre_gens = [mat7_of(ONE, g) for g in (I, H2)]          # i and (1+i+j+k)/2 generate 2T
    hw_gens = [mat7_of(l, ONE) for l in (I, J)]              # the Hantzsche-Wendt lifts (k = ij)
    deck = mat7_of(l0, ONE)
    # sanity: the fibre generators generate 24 elements, the HW lifts act on Im H by V_4
    cover = fibre_gens + hw_gens
    desc = cover + [deck]
    for name, gens in (("cover", cover), ("descent", desc)):
        d1, _ = invariant_dim(gens, 1)
        d2, _ = invariant_dim(gens, 2)
        d3, A3 = invariant_dim(gens, 3)
        print(f"  {name}: invariant 1-forms {d1} (invariant spinors = 1 + {d1} = {1 + d1}: N = 1), b_2 = {d2}, b_3 = {d3}")
    # the four invariant 3-forms of the cover and the deck's action on them
    d3, A3 = invariant_dim(cover, 3)
    null = A3.nullspace()
    Dk = exterior_power_matrix(deck, 3)
    # deck acts on the invariant space: express Dk v in the basis
    B = sympy.Matrix.hstack(*null)
    rep = []
    for v in null:
        w = Dk * v
        coeffs = B.solve_least_squares(w)
        assert B * coeffs == w
        rep.append(list(coeffs))
    R = sympy.Matrix(rep).T
    ev = R.eigenvals()
    print(f"  the deck on the {d3} invariant 3-forms of the cover: eigenvalues {dict(ev)} -> invariant part {sum(m for e, m in ev.items() if e == 1)}"
          f" (= b_3 of the descent)")
    return

def stage_4(cover_loci, labels, perms, pts, orbits):
    print("\n" + "=" * 100)
    print("STAGE 4 — rigidity: the resolution parameter of C^2/Gamma along a locus lives in h(Gamma) x (R^3)^{holonomy}")
    print("=" * 100)
    # the holonomy image acts on R^3 = Im H by conjugation by l; (R^3)^{V_4} = 0, (R^3)^{Z_2} = 1, (R^3)^{1} = 3
    rank = {"A1": 1, "A2": 2, "D4": 4, "E6": 6}
    b1 = {4: 0, 2: 1, 1: 3}
    inv3 = {4: 0, 2: 1, 1: 3}
    add2 = 0; add3 = 0
    for L in cover_loci:
        s = L[0]
        hol = [name for name, p in {"1": tuple(range(len(orbits))), "i": perms["i"], "j": perms["j"], "k": perms["k"]}.items() if p[s] == s]
        h = len(hol)
        r = rank[labels[s]]
        print(f"  locus {labels[s]} (holonomy image of order {h}): (R^3)^hol has dimension {inv3[h]} -> "
              + ("RIGID: no resolution or deformation compatible with the monodromy" if inv3[h] == 0 else
                 f"resolvable with parameter in h x R^{inv3[h]}; Joyce's resolution would add {r} to b_2 and {r * b1[h]} to b_3"))
        if inv3[h] > 0:
            add2 += r; add3 += r * b1[h]
    print(f"  total a full Joyce resolution could add: b_2 += {add2}, b_3 += {add3}")
    return add2, add3

def stage_5():
    print("\n" + "=" * 100)
    print("STAGE 5 — the descent's collision loci along the knot: fixed sets on T^4 of y -> g y l0^, g in 2T")
    print("=" * 100)
    l0 = H2
    D = 12
    grid = [Fr(k, D) for k in range(D)]
    candidates = [from_lambda_coords(a, b, c, d) for a in grid for b in grid for c in grid for d in grid]
    results = Counter()
    planes = {}
    for g in TT:
        # linear part: the fixed subspace of y -> g y l0^ on H
        M = sympy.Matrix(4, 4, lambda i, j: 0)
        basis = [ONE, I, J, K]
        for j, b in enumerate(basis):
            im = g * b * l0.conj()
            for i, x in enumerate(im.tup()):
                M[i, j] = x
        ker = (M - sympy.eye(4)).nullspace()
        dim = len(ker)
        if dim == 0:
            F = [y for y in candidates if in_lambda(g * y * l0.conj() - y)]
            results[(order(g), dim, len(F))] += 1
        else:
            # the fixed set is a union of translates of the torus V/(V cap Lambda); count the translates by sampling the
            # candidates that satisfy the congruence and grouping them modulo V
            F = [y for y in candidates if in_lambda(g * y * l0.conj() - y)]
            # project to a complement of V: use a rational basis of V and reduce; count distinct classes mod (V + Lambda)
            Vb = [sympy.Matrix(v) for v in ker]
            # a linear functional vanishing on V: rows of the left nullspace of [V]
            Vmat = sympy.Matrix.hstack(*Vb)
            comp = Vmat.T.nullspace()   # vectors w with w . v = 0 for v in V
            classes = set()
            for y in F:
                yv = sympy.Matrix(list(y.tup()))
                key = tuple((w.T * yv)[0] for w in comp)
                # reduce modulo the projections of Lambda (which is a lattice in the quotient)
                classes.add(key)
            # classes mod the projected lattice: compute the projected lattice generators and reduce
            lam_gens = [sympy.Matrix(list(b.tup())) for b in [ONE, I, J, H2]]
            proj = [tuple((w.T * v)[0] for w in comp) for v in lam_gens]
            # 2-dim quotient: reduce keys modulo the lattice spanned by proj (rank 2) — use Smith-style reduction via lattice basis
            Pm = sympy.Matrix(proj)  # 4 x 2
            # find a basis of the lattice generated by the rows
            Lb = Pm.T  # 2 x 4 columns generate
            # Hermite: use sympy's Matrix over integers after clearing denominators
            den = 1
            for x in Lb:
                den = sympy.ilcm(den, sympy.Rational(x).q)
            Li = (Lb * den).applyfunc(lambda x: int(x))
            # column HNF via smith_normal_form is overkill; brute force: reduce each key by integer combos of the 4 generators
            gens2 = [tuple(int(Li[i, j]) for i in range(2)) for j in range(4)]
            def reduce_key(key):
                k = [sympy.Rational(x) * den for x in key]
                best = None
                for coeffs in itertools.product(range(-3, 4), repeat=4):
                    cand = [k[i] - sum(c * gg[i] for c, gg in zip(coeffs, gens2)) for i in range(2)]
                    t = tuple(cand)
                    # canonical: smallest lexicographically among |.| minimal
                    score = (sum(abs(x) for x in cand), t)
                    if best is None or score < best[0]:
                        best = (score, t)
                return best[1]
            reduced = set(reduce_key(k) for k in classes)
            results[(order(g), dim, f"{len(reduced)} tori")] += 1
            planes[g] = (ker, len(reduced))
    for (o, dim, cnt), num in sorted(results.items(), key=lambda t: (t[0][0], str(t[0][2]))):
        print(f"  g of order {o}: fixed subspace of the linear part of dimension {dim}; fixed set on T^4: {cnt}  ({num} elements)")
    print("  the elements with a 2-dimensional fixed plane give the two A_2 loci of B1356 along the knot; on the torus they are "
          "closed 2-tori, so in the compact descent the A_2 loci along the knot are compact (circle x torus, modulo the group).")

# ---- stage 6: the enhanced local groups along the descent's cone circles ----
def omul(x, y):
    a, b = x; c, d = y
    return (a*c - d.conj()*b, d*a + b*c.conj())

def stage_6(pts, orbits, perms, labels):
    print("\n" + "=" * 100)
    print("STAGE 6 — the descent's cone circles: the local group <Gamma_y, deck> at each deck-fixed singular point, its strata and ages")
    print("=" * 100)
    import numpy as np, math
    l0 = H2
    e7 = np.array([1., 1., 1., 0, 0, 0, 0]) / math.sqrt(3)
    basis7 = [(I, ZERO), (J, ZERO), (K, ZERO), (ZERO, ONE), (ZERO, I), (ZERO, J), (ZERO, K)]
    ef = (I + J + K, ZERO)
    Jm = np.zeros((7, 7))
    for j, b in enumerate(basis7):
        im = omul(ef, b)
        Jm[:, j] = np.array([float(x) for x in [im[0].b, im[0].c, im[0].d, im[1].a, im[1].b, im[1].c, im[1].d]]) / math.sqrt(3)
    Pperp = np.eye(7) - np.outer(e7, e7)
    Jp = Pperp @ Jm @ Pperp
    v1 = np.array([1., -1., 0, 0, 0, 0, 0]) / math.sqrt(2)
    v2 = np.array([0, 0, 0, 1., 0, 0, 0]); v3 = np.array([0, 0, 0, 0, 0, 1., 0])
    cb = [v1, v2, v3]
    B = np.column_stack([v1, Jp @ v1, v2, Jp @ v2, v3, Jp @ v3])
    def cmat(Mq):
        M = np.array(Mq.tolist(), dtype=float)
        assert np.allclose(M @ e7, e7, atol=1e-9) and np.allclose(M @ Jp, Jp @ M, atol=1e-9)
        C = np.zeros((3, 3), dtype=complex)
        for j, v in enumerate(cb):
            coeff = np.linalg.lstsq(B, M @ v, rcond=None)[0]
            for k in range(3):
                C[k, j] = coeff[2*k] + 1j * coeff[2*k + 1]
        return C
    def age(Mq):
        w = np.linalg.eigvals(cmat(Mq)); a = Fr(0)
        for lam in w:
            t = (np.angle(lam) / (2 * math.pi)) % 1.0
            t12 = round(t * 12); assert abs(t * 12 - t12) < 1e-6
            a += Fr(t12 % 12, 12)
        return a
    Id = sympy.eye(7)
    e_col = sympy.Matrix([1, 1, 1, 0, 0, 0, 0])
    def gen_group(gens):
        G = {tuple(g): g for g in gens}
        frontier = list(gens)
        while frontier:
            new = []
            for a in frontier:
                for b in gens:
                    c = a * b
                    k = tuple(c)
                    if k not in G:
                        G[k] = c; new.append(c)
            frontier = new
        return list(G.values())
    def fixed_plane(M):
        # fixed vectors in e^perp
        A = sympy.Matrix.vstack(M - Id, e_col.T)
        return A.nullspace()
    results = {}
    for s, (y, orb) in enumerate(orbits):
        if perms["l0"][s] != s:
            continue
        Gy = pts[y]
        deck_g = [g for g in TT if reduce_mod_lambda(g * y * l0.conj()) == y]
        gens = [mat7_of(ONE, g) for g in Gy] + [mat7_of(l0, g) for g in deck_g[:1]]
        G = gen_group(gens)
        Gset = set(tuple(g) for g in G)
        # the whole coset is in the group?
        coset_ok = all(tuple(mat7_of(l0, g)) in Gset for g in deck_g)
        # strata
        planes = []
        for M in G:
            if M == Id:
                continue
            ns = fixed_plane(M)
            if len(ns) == 2:
                P = sympy.Matrix.hstack(*ns)
                # canonical: reduced row echelon of P^T
                key = tuple(P.T.rref()[0])
                if key not in [p[0] for p in planes]:
                    planes.append((key, P))
        # classify planes: in Im H (x-part only) or not; pointwise stabilisers; orbits
        def pw_stab(P):
            return [M for M in G if M * P == P]
        info = []
        for key, P in planes:
            in_imH = all(P[r, c] == 0 for r in range(3, 7) for c in range(P.shape[1]))
            st = pw_stab(P)
            info.append((in_imH, len(st), key))
        # orbits of planes under G
        def img_key(M, P):
            return tuple((M * P).T.rref()[0])
        keys = [k for k, _ in planes]
        seen = set(); orbs = []
        for key, P in planes:
            if key in seen:
                continue
            o = set()
            for M in G:
                o.add(img_key(M, P))
            seen |= o
            orbs.append((len(o), [im for (im, st, k) in info if k in o][0], [st for (im, st, k) in info if k in o][0]))
        # conjugacy classes and ages
        classes = []; cseen = set()
        Ginv = {tuple(M): M.inv() for M in G}
        for M in G:
            if tuple(M) in cseen:
                continue
            cl = set(tuple(N * M * Ginv[tuple(N)]) for N in G)
            cseen |= cl; classes.append(cl)
        ages = Counter(age(sympy.Matrix(7, 7, list(next(iter(cl))))) for cl in classes)
        b2 = ages.get(Fr(1), 0); b4 = ages.get(Fr(2), 0)
        n_e6 = sum(1 for (im, st, k) in info if im)
        print(f"  {labels[s]} point y = {y}: |Gamma_y| = {len(Gy)}, deck lifts (g with g y l0^ = y): {len(deck_g)}; local group order "
              f"{len(G)} (= 3|Gamma_y|: {len(G) == 3 * len(Gy)}; the whole deck coset lies in it: {coset_ok})")
        print(f"      fixed planes: {len(planes)}; orbits (size, in Im H?, pointwise stabiliser order): "
              f"{[(n, im, st) for (n, im, st) in orbs]}")
        print(f"      conjugacy classes {len(classes)}, ages {dict(sorted(ages.items()))} -> crepant b_2 = {b2}, b_4 = {b4}, "
              f"non-compact divisors {b2 - b4}")
        results[labels[s]] = (len(G), orbs, b2, b4)
    # which singular points lie on the knot's A_2 tori (fixed by some deck-coset element with a 2-dim fixed plane)?
    print("\n  singular points of T^4 fixed by a deck-coset element (g, l0) whose linear part has a 2-dimensional fixed plane:")
    hits = Counter()
    for s, (y, orb) in enumerate(orbits):
        for z in orb:
            for g in TT:
                if order(g) != 6:
                    continue
                if reduce_mod_lambda(g * z * l0.conj()) == z:
                    hits[labels[s]] += 1
                    break
    print(f"      by type: {dict(hits)}  (orbit sizes: E6 1, A1 12, D4 3, A2 8 each)")
    # the two compact collision loci: the 8 tori T_g (g of order 6) fall into the two conjugacy classes of order-6 elements
    # (h T_g = T_{h g h^-1}); which singular points lie on the union of each class's tori?
    six = [g for g in TT if order(g) == 6]
    classes6 = []
    for g in six:
        cl = frozenset(h * g * h.conj() for h in TT)
        if cl not in classes6:
            classes6.append(cl)
    print(f"\n  the order-6 elements form {len(classes6)} conjugacy classes of {[len(c) for c in classes6]}: two compact A_2 loci Sigma_1, Sigma_2")
    for n, cl in enumerate(classes6):
        inc = Counter()
        for s, (y, orb) in enumerate(orbits):
            for z in orb:
                if any(reduce_mod_lambda(g * z * l0.conj()) == z for g in cl):
                    inc[labels[s]] += 1
        print(f"      Sigma_{n+1} (tori of the class containing {min(cl, key=lambda q: q.tup())}): singular points on it by type {dict(inc)}")
    return results

def stage_7(add2, add3):
    print("\n" + "=" * 100)
    print("STAGE 7 — Betti numbers after Joyce's resolution of the untwisted A_2 locus, with the deck")
    print("=" * 100)
    print(f"  cover: b_2 = 0 + {add2} = {add2} (the A_2 root lattice x H^0(T^3)), b_3 = 4 + {add3} = {4 + add3} "
          f"(4 flat moduli: the three T^3 radii and the fibre scale; {add3} = A_2 roots x H^1(T^3))")
    print(f"  deck on the added classes: on b_2 through the A_2 fibre's normaliser (in U(1)_L x Sp(1)_R, connected: trivial), on b_3 "
          f"through H^1(T^3) = 1 + (2-dim irreducible): invariant 2 x 1 = 2")
    print(f"  descent (resolvable in R^3^Z_3 = the axis): b_2 = 2, b_3 = 2 + 2 = 4; the deck's two-dimensional irreducible occurs on "
          f"3-forms (4 of the cover's 10) and never on 2-forms: no C-field U(1) carries it in the flat background or its resolution")

if __name__ == "__main__":
    pts, orbits = stage_1()
    perms, cover_loci, desc_loci, labels, sc, sd = stage_2(pts, orbits)
    stage_3()
    add2, add3 = stage_4(cover_loci, labels, perms, pts, orbits)
    stage_5()
    stage_6(pts, orbits, perms, labels)
    stage_7(add2, add3)
    print("\nDONE")
