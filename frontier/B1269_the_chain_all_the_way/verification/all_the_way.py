#!/usr/bin/env python3
"""THE CHAIN TAKEN ALL THE WAY: three generations as the Eisenstein triplet of the golden E8, the
rank reduction by the 27's own singlets, and the Yukawa E8 forces on the triplet -- which is zero.

(a) THE TRIPLET AND ITS FAMILY TENSOR (exact, on the icosian E8 of B1268).  The 162 non-E6, non-A2
    roots are (27,3) + (27bar,3bar): three classes of 27 on each side, indexed by the Eisenstein weights
    (which sum to zero) and cycled by the founding ratio g.  The E8 bracket restricted to (27,3) x (27,3)
    lands in (27bar,3bar) and its family tensor is eps_ijk: two roots of the SAME class never sum to a root
    (2 e_i is not a weight of the 3bar); roots of classes i != j sum to a root 270 = 6 x 45 times, always
    in the class -e_l of the THIRD index l (e_i + e_j = -e_l).  By Schur (Lambda^2(27 x 3) contains
    27bar x 3bar once, in Sym^2(27) x Lambda^2(3), since Lambda^2(27) = 351 and Sym^2(27) = 27bar + 351')
    the bracket is d_abc eps_ijk: E6's symmetric cubic times the antisymmetric family tensor.

(b) THE RANK REDUCTION 6 -> 4 BY THE 27'S SINGLETS (exact, on B1252's descent).  The 27 has exactly two
    SM singlets (weights with zero SU(3)xSU(2) charges and Y = 0): nu^c in the 16 and the SO(10)
    singlet.  Their charges under the two extra U(1)s of the rank-6 Levi (the complement of Y in the
    Levi's centre) are linearly independent, so VEVs for both leave exactly su(3)+su(2)+u(1)_Y -- the
    step the adjoint cannot take (B952, B1267's double-centralizer theorem) is taken by the 27s that the
    two faces supply.  Structure only: the VEVs' values are not supplied.

(c) THE YUKAWA E8 FORCES ON THE TRIPLET IS ZERO (exact, symbolic on the 45-triple support of d).  A 4d
    superpotential is a polynomial in commuting superfields; W = Y^{ijk} d_abc 27^a_i 27^b_j 27^c_k sees
    only the totally symmetric part of the family tensor Y (d_abc X^a_i X^b_j X^c_k is symmetric in ijk),
    and E8's family tensor is eps^{ijk}: W == 0 identically, monomial by monomial, for EVERY symmetric d
    (checked with generic rational d on the support; the control with a symmetric Y is nonzero).  This
    is E8 having no cubic invariant (Casimir degrees 2, 8, 12, 14, 18, 20, 24, 30) seen from E6 x SU(3):
    Sym^3(27 x 3) has no singlet because Sym^3(3) = 10.  All tree-level masses of the triplet vanish; no
    texture, no mixing, no hierarchy.  The wall B632/B1036 met on the object (an antisymmetric pairing,
    hence no Yukawa) is the same zero, seen on the lattice.

(d) THE CUBIC'S SO(10) CONTENT (exact, on B883's weights): the 45 weight-triples of the 27 summing to
    zero split 40 (10.16.16) + 5 (1.10.10); no 16.16.16 and no 1.16.16, so the cubic that a SYMMETRIC
    family tensor would switch on has no Majorana term for nu^c.
"""
from __future__ import annotations
import os, sys, json, random, itertools, collections
from fractions import Fraction as F
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
for arc in ('B1265_spectrum_law_rebuilt', 'B1267_transport_computed', 'B1268_e6_from_the_two_faces'):
    sys.path.insert(0, os.path.join(HERE, '..', '..', arc, 'verification'))
import e6_instrument as E
import transport as T
import e6_from_the_two_faces as TF


def part_a():
    units = TF.unit_icosians()
    roots = TF.e8_roots(units)
    one = (TF.Q5(1), TF.Q5(0), TF.Q5(0), TF.Q5(0))
    w = next(u for u in units if TF.orders_of(u, one, TF.key) == 3)
    rk = {TF.key(r) for r in roots}
    cls = {}
    for r in roots:
        cls[TF.key(r)] = (TF.bil(r, one), TF.bil(r, w))
    counts = collections.Counter(cls.values())
    triplet = [c for c, n in counts.items() if n == 27]
    assert len(triplet) == 6
    # the two triples: orbits of left multiplication by w
    def wimg(c):
        r = next(x for x in roots if cls[TF.key(x)] == c)
        return cls[TF.key(TF.qmul(w, r))]
    orbits = []
    seen = set()
    for c in triplet:
        if c in seen:
            continue
        orb = [c]
        seen.add(c)
        nxt = wimg(c)
        while nxt not in seen:
            orb.append(nxt)
            seen.add(nxt)
            nxt = wimg(nxt)
        orbits.append(orb)
    assert len(orbits) == 2 and all(len(o) == 3 for o in orbits)
    three, threebar = orbits
    # the three Eisenstein pairings of a triplet are the weights of a 3: they sum to zero
    assert all(sum(c[t] for c in three) == 0 for t in range(2)) and all(sum(c[t] for c in threebar) == 0 for t in range(2))
    # conjugation must swap the two orbits
    def cimg(c):
        r = next(x for x in roots if cls[TF.key(x)] == c)
        return cls[TF.key(TF.qconj(r))]
    assert all(cimg(c) in threebar for c in three) and all(cimg(c) in three for c in threebar)
    byclass = collections.defaultdict(list)
    for r in roots:
        byclass[cls[TF.key(r)]].append(r)
    print(f"  (27,3): the classes {three} (cycled by g);  (27bar,3bar): {threebar};  conjugation swaps them")
    # the texture: same-class sums are never roots; cross-class sums that are roots land in the third class' conjugate
    same = 0
    landing = collections.defaultdict(collections.Counter)
    for i in range(3):
        for r in byclass[three[i]]:
            for s in byclass[three[i]]:
                if TF.key(tuple(a + b for a, b in zip(r, s))) in rk:
                    same += 1
        for j in range(3):
            if j == i:
                continue
            for r in byclass[three[i]]:
                for s in byclass[three[j]]:
                    t = tuple(a + b for a, b in zip(r, s))
                    if TF.key(t) in rk:
                        landing[(i, j)][cls[TF.key(t)]] += 1
    print(f"  same-class root sums (27,3)_i + (27,3)_i that are roots: {same}   (must be 0: 2e_i is not a weight of the 3bar)")
    ok = same == 0
    neg = lambda c: tuple(-x for x in c)
    for (i, j), cnt in sorted(landing.items()):
        l = 3 - i - j
        target = neg(three[l])
        ks = list(cnt)
        ok &= ks == [target] and sum(cnt.values()) == 270 and target in threebar
        print(f"  (27,3)_{i} + (27,3)_{j}: {sum(cnt.values())} root sums, all in (27bar,3bar)_{threebar.index(target)} = -(27,3)_{l}, l the third index")
    print("  the family tensor of the bracket is eps_ijk (e_i + e_j = -e_l); 270 = 6 x 45: the support of E6's cubic d")
    return ok


def part_b():
    import sympy as sp
    sub, Y, rts, Mf = T.sm_subalgebra()
    wts = __import__('json').load(open(E.REP27))['weights']
    ip = lambda a, b: sum(F(a[i]) * Mf[i][j] * F(b[j]) for i in range(6) for j in range(6))
    Ms = sp.Matrix([[sp.Rational(Mf[i][j]) for j in range(6)] for i in range(6)])
    # the Levi's centre: the 3-dim orthogonal complement of the A2+A1 roots (in weight coordinates)
    centre = [[F(sp.Rational(x)) for x in n] for n in (sp.Matrix([list(r) for r in sub]) * Ms).nullspace()]
    assert len(centre) == 3
    # the two extra U(1)s: a basis of the complement of Y inside the centre (w.r.t. the metric)
    def orth(vs):
        # Gram-Schmidt-free: pick two centre vectors and project out Y
        out = []
        for v in vs:
            c = ip(v, Y) / ip(Y, Y)
            u = [v[i] - c * Y[i] for i in range(6)]
            if any(u) and all(abs(ip(u, o)) != 0 or True for o in out):
                out.append(u)
        # reduce to two independent
        M = sp.Matrix([[sp.Rational(x) for x in u] for u in out])
        rref, piv = M.T.rref()
        return [out[k] for k in piv][:2]
    extra = orth(centre)
    assert len(extra) == 2 and all(ip(z, Y) == 0 for z in extra)
    # SM singlets of the 27
    singlets = []
    for idx, w in enumerate(wts):
        if all(ip(a, w) == 0 for a in sub) and ip(Y, w) == 0:
            singlets.append(idx)
    print(f"  SM singlets in the 27 (zero SU(3)xSU(2) charges, Y = 0): weights {singlets}   (expect 2: nu^c and the SO(10) singlet)")
    # their charges under the two extra U(1)s
    Q = sp.Matrix([[sp.Rational(ip(z, wts[idx])) for z in extra] for idx in singlets])
    print(f"  charge matrix under the two extra U(1)s:\n{Q}")
    print(f"  rank = {Q.rank()}   (2: VEVs of both singlets break both extra U(1)s and nothing else -> exactly su(3)+su(2)+u(1)_Y)")
    # which SO(10) block each singlet sits in (B1250's stabiliser blocks)
    import importlib.util, pathlib
    spec = importlib.util.spec_from_file_location("dd", pathlib.Path(E.ROOT) / "frontier" / "B1250_d2_decode" / "verification" / "d2_decode.py")
    dd = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dd)
    _, _, blocks = dd.stabiliser_blocks()
    where = {idx: next(name for name, blk in zip(("1", "10", "16"), blocks) if idx in blk) for idx in singlets}
    print(f"  SO(10) block of each singlet: {where}   (the SO(10) singlet and nu^c in the 16)")
    return len(singlets) == 2 and Q.rank() == 2 and sorted(where.values()) == ["1", "16"]


def part_c():
    import sympy as sp
    wts = json.load(open(E.REP27))['weights']
    support = [t for t in itertools.combinations(range(27), 3)
               if all(wts[t[0]][k] + wts[t[1]][k] + wts[t[2]][k] == 0 for k in range(6))]
    assert len(support) == 45
    rng = random.Random(1269)
    dval = {t: sp.Rational(rng.randint(1, 97), rng.randint(1, 97)) for t in support}   # a generic symmetric d on the support
    X = [[sp.Symbol(f'x{a}_{i}') for i in range(3)] for a in range(27)]

    def cubic(Y):
        W = sp.Integer(0)
        for t, dv in dval.items():
            for a, b, c in itertools.permutations(t):                      # d symmetric: every ordering carries dv
                for (i, j, k), y in Y.items():
                    W += dv * y * X[a][i] * X[b][j] * X[c][k]
        return sp.expand(W)

    eps = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
    W_eps = cubic(eps)
    W_sym = cubic({(i, i, i): 1 for i in range(3)})                         # control: a symmetric family tensor
    W_one = cubic({(0, 0, 0): 1})                                           # one generation's self-coupling d_abc 27^3
    n_sym = len(W_sym.as_ordered_terms())
    print(f"  W = d_abc eps^ijk X^a_i X^b_j X^c_k on the 45-triple support with generic symmetric d: expands to {W_eps}")
    print(f"  control, symmetric family tensor delta_iii: {n_sym} monomials, nonzero;  one generation alone (d_abc 27^3): {len(W_one.as_ordered_terms())} monomials")
    ok = W_eps == 0 and W_sym != 0 and W_one != 0 and n_sym == 3 * 45
    # every mass matrix is a second derivative of W: with W == 0 all tree-level masses of the triplet vanish
    print("  -> the E8-forced Yukawa among the three 27s vanishes identically (E8 has no cubic invariant; Sym^3(3) = 10 has no singlet):")
    print("     all tree-level masses of the triplet are zero -- no texture, no mixing, no hierarchy; the mirror (27bar,3bar) likewise")
    return ok


def part_d():
    wts = __import__('json').load(open(E.REP27))['weights']
    import importlib.util, pathlib
    spec = importlib.util.spec_from_file_location("dd", pathlib.Path(E.ROOT) / "frontier" / "B1250_d2_decode" / "verification" / "d2_decode.py")
    dd = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dd)
    _, _, blocks = dd.stabiliser_blocks()
    name = {}
    for nm, blk in zip(("1", "10", "16"), blocks):
        for i in blk:
            name[i] = nm
    triples = collections.Counter()
    n = 0
    for a, b, c in itertools.combinations(range(27), 3):
        if all(wts[a][k] + wts[b][k] + wts[c][k] == 0 for k in range(6)):
            n += 1
            triples[tuple(sorted((name[a], name[b], name[c])))] += 1
    print(f"  weight triples of the 27 summing to zero: {n}; by SO(10) block: {dict(triples)}")
    return n == 45 and triples[("10", "16", "16")] == 40 and triples[("1", "10", "10")] == 5 and len(triples) == 2


if __name__ == "__main__":
    ok = True
    print("=== (a) the triplet (27,3) in the golden E8 and its family tensor eps_ijk ===")
    ok &= part_a()
    print("\n=== (b) rank 6 -> 4 by the 27's own singlets (B1252's descent) ===")
    ok &= part_b()
    print("\n=== (c) the Yukawa E8 forces on the triplet: zero ===")
    ok &= part_c()
    print("\n=== (d) the cubic's SO(10) content (B883 weights, B1250 blocks) ===")
    ok &= part_d()
    print("\nSELFTEST:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
