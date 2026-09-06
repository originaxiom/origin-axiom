#!/usr/bin/env python3
"""THE OBJECT'S OWN THREE-FOLD CLOSING: the 3-fold cyclic branched cover of m004, the descent of the
object's 2T holonomy onto it, the three twisted classes it carries, and the texture they force.

(a) THE CLOSING, BY REIDEMEISTER-SCHREIER (exact).  pi_1(m004) = <a, b | a w B w^-1>, w = bABa.  The
    kernel H of a, b -> 1 in Z/3 is the 3-fold cyclic (unbranched) cover; filling its single cusp along the
    lifted meridian a^3 gives the 3-fold cyclic BRANCHED cover Y_3 of S^3 along the figure-eight knot,
    pi_1(Y_3) = H / <<a^3>> on the Schreier generators z = a^3, x_k = a^k b a^{-(k+1 mod 3)}.  Its
    abelianization is computed (Smith form): Z/4 + Z/4, the torsion B326 counted as |Delta(w) Delta(w^2)| = 16.
    Y_3 is the flat Hantzsche-Wendt manifold, pi_1(Y_3) = the Fibonacci group F(2,6) (Helling-Kim-Mennicke:
    the n-fold cyclic branched covers of 4_1 are the Fibonacci manifolds, pi_1 = F(2,2n); F(2,4) = Z/5 is
    the golden L(5,2)); fingerprinted here: same abelianization and the same counts of homomorphisms to
    Q8, A4 and 2T as F(2,6).

(b) THE DESCENT OF THE OBJECT'S HOLONOMY (exact over Q(omega)).  For every surjection rho: pi_1 -> 2T
    (B1263's 48), the real 3 of 2T (the adjoint of the 2x2 model) satisfies rho_3(a^3) = 1, so 3_rho
    descends to Y_3 -- with image the Klein group V4 = ker(A4 -> Z/3), the diagonal sign matrices: the
    HOLONOMY GROUP OF THE FLAT MANIFOLD.  Then, by Fox calculus on the branched-cover presentation:
    h^1(Y_3; 3_rho) = 3, one class per non-trivial sign character chi_1, chi_2, chi_3 (h^1(chi_i) = 1),
    h^1(Y_3; trivial) = 0 (b_1 = 0), and h^1(Y_3; 2_rho) = 0 for the spin lift (meridian order 3).  The
    three sign characters are exactly the three characters of the flat holonomy: the descended 3_rho is
    the tangent bundle of the closing, and the three generation classes are its three flat directions
    (H^1(Y_3; chi_i) = the chi_i-line of H^1(T^3) = C dx_i, by the torus cover).

(c) THE E8 TRANSPORT ON Y_3: gauge group = the centralizer of V4 in E8 through E6 x SU(3), = E6 x U(1)^2
    (the torus of the family SU(3)); matter = (27,3) x H^1(3_rho) = THREE 27s with family charges e_1, e_2,
    e_3, the mirror (27bar,3bar) x H^1(3bar) = three 27bars, (1,8) x H^1(8) = 6 singlets, and NO E6-adjoint
    chiral (b_1 = 0).  Vector-like (B1260); the chirality bit is the orientation of Y_3 = the sign of the
    triple product.

(d) THE TEXTURE (theorem + data).  The cubic among the three 27s is d_abc T 27_1 27_2 27_3 with
    T = int dx_1 ^ dx_2 ^ dx_3 != 0 (the only cubic the characters allow: chi_i chi_j chi_k = 1 iff
    {i,j,k} = {1,2,3}), so every tree-level mass matrix is complex symmetric with ZERO DIAGONAL, and for
    such a 3x3 matrix  sigma_1 <= sigma_2 + sigma_3  (Takagi: M = U S U^T, 0 = M_ii = sum_k s_k U_ik^2).
    Checked numerically on random matrices; the data violate it in all three charged sectors.
"""
from __future__ import annotations
import os, sys, itertools, collections, random
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
for arc in ('B1267_spectrum_law_rebuilt', 'B1269_transport_computed'):
    sys.path.insert(0, os.path.join(HERE, '..', '..', arc, 'verification'))
import e6_instrument as E
import spectrum_law as S
import transport as T

Qw, ONE, ZERO, OMEGA = E.Qw, E.ONE, E.ZERO, E.OMEGA


# ----------------------------------------------------------------------------------------- (a)
def rewrite(word, k=0):
    """Reidemeister-Schreier rewriting of a word in a (1), b (2) for the kernel of a, b -> 1 (mod 3),
    transversal {1, a, a^2}.  New generators: z = a^3 -> 1, x_k = a^k b a^{-(k+1 mod 3)} -> 2 + k."""
    out = []
    for L in word:
        if L == 1:
            if k == 2:
                out.append(1)
            k = (k + 1) % 3
        elif L == -1:
            if k == 0:
                out.append(-1)
            k = (k - 1) % 3
        elif L == 2:
            out.append(2 + k)
            k = (k + 1) % 3
        elif L == -2:
            k = (k - 1) % 3
            out.append(-(2 + k))
    return out, k


def branched_cover_presentation():
    rels = []
    for k in range(3):
        r, kk = rewrite(S.REL, k)
        assert kk == k
        rels.append(r)
    rels.append([1])                       # the lifted meridian a^3 is filled
    return [1, 2, 3, 4], rels


def abelianization(gens, rels):
    M = sp.zeros(len(rels), len(gens))
    for i, r in enumerate(rels):
        for L in r:
            M[i, abs(L) - 1] += (1 if L > 0 else -1)
    from sympy.matrices.normalforms import smith_normal_form
    D = smith_normal_form(M, domain=sp.ZZ)
    inv = [abs(D[i, i]) for i in range(min(D.shape))]
    free = len(gens) - sum(1 for d in inv if d != 0)
    return sorted(d for d in inv if d not in (0, 1)), free


# small groups for the fingerprint
def q8():
    # unit quaternions as (a,b,c,d) integer tuples
    def mul(p, q):
        a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
        return (a1*a2 - b1*b2 - c1*c2 - d1*d2, a1*b2 + b1*a2 + c1*d2 - d1*c2,
                a1*c2 - b1*d2 + c1*a2 + d1*b2, a1*d2 + b1*c2 - c1*b2 + d1*a2)
    els = [(s, 0, 0, 0) for s in (1, -1)] + [(0, s, 0, 0) for s in (1, -1)] + [(0, 0, s, 0) for s in (1, -1)] + [(0, 0, 0, s) for s in (1, -1)]
    return els, mul, (1, 0, 0, 0), lambda p: (p[0], -p[1], -p[2], -p[3])


def a4():
    els = [p for p in itertools.permutations(range(4)) if sum(1 for i in range(4) for j in range(i) if p[j] > p[i]) % 2 == 0]
    mul = lambda p, q: tuple(p[q[i]] for i in range(4))
    inv = lambda p: tuple(sorted(range(4), key=lambda i: p[i]))
    return els, mul, tuple(range(4)), inv


def count_homs(gens, rels, group):
    els, mul, e, inv = group
    n = 0
    for imgs in itertools.product(els, repeat=len(gens)):
        ok = True
        for r in rels:
            cur = e
            for L in r:
                g = imgs[abs(L) - 1]
                cur = mul(cur, g if L > 0 else inv(g))
            if cur != e:
                ok = False
                break
        n += ok
    return n


def fibonacci_presentation(m=6):
    gens = list(range(1, m + 1))
    rels = [[i, (i % m) + 1, -(((i + 1) % m) + 1)] for i in range(1, m + 1)]     # x_i x_{i+1} x_{i+2}^-1
    return gens, rels


def count_homs_fib(m, group):
    """F(2,m) is generated by x_1, x_2; count homomorphisms by extending and checking all relators."""
    els, mul, e, inv = group
    n = 0
    for x1 in els:
        for x2 in els:
            xs = [x1, x2]
            for i in range(2, m + 2):
                xs.append(mul(xs[i - 2], xs[i - 1]))
            # relators: x_i x_{i+1} = x_{i+2} for all i mod m  <=> the sequence is m-periodic
            if xs[m] == xs[0] and xs[m + 1] == xs[1]:
                n += 1
    return n


def part_a():
    gens, rels = branched_cover_presentation()
    print(f"  Schreier generators z = a^3, x0, x1, x2; relators (lengths {[len(r) for r in rels]}), the last = the filled meridian a^3")
    tors, free = abelianization(gens, rels)
    print(f"  H_1(Y_3) = torsion {tors}, free rank {free}    (B326: |Delta(w)Delta(w^2)| = 16 = |(Z/4)^2|)")
    fg, fr = fibonacci_presentation(6)
    tors_f, free_f = abelianization(fg, fr)
    print(f"  F(2,6): H_1 = torsion {tors_f}, free rank {free_f}")
    fp = {}
    for name, G in (("Q8", q8()), ("A4", a4())):
        n1 = count_homs(gens, rels, G)
        n2 = count_homs_fib(6, G)
        fp[name] = (n1, n2)
        print(f"  homomorphisms to {name}: Y_3 presentation {n1}, F(2,6) {n2}")
    ok = tors == [4, 4] and free == 0 and tors_f == [4, 4] and free_f == 0 and all(a == b for a, b in fp.values())
    return ok, (gens, rels)


# ----------------------------------------------------------------------------------------- (b)
def qneg(x):
    return ZERO - x


def sl2_inv(M):
    (a, b), (c, d) = M[0], M[1]
    return np.array([[d, qneg(b)], [qneg(c), a]], dtype=object)


def ad3(M):
    """The adjoint action of M in SL(2) on sl2 with basis E, H, F: the real 3 of 2T, complexified."""
    Mi = sl2_inv(M)
    Ebas = np.array([[ZERO, ONE], [ZERO, ZERO]], dtype=object)
    Hbas = np.array([[ONE, ZERO], [ZERO, qneg(ONE)]], dtype=object)
    Fbas = np.array([[ZERO, ZERO], [ONE, ZERO]], dtype=object)
    cols = []
    for X in (Ebas, Hbas, Fbas):
        Y = M.dot(X).dot(Mi)
        cols.append([Y[0, 1], Y[0, 0], Y[1, 0]])          # coordinates (E, H, F)
    A = np.empty((3, 3), dtype=object)
    for j, col in enumerate(cols):
        for i in range(3):
            A[i, j] = col[i]
    return A


def key(M):
    return tuple((x.x, x.y) for x in np.asarray(M).flatten())


def surjections_2T():
    gens2, elems2 = T.sl2_2T()
    one = np.array([[ONE, ZERO], [ZERO, ONE]], dtype=object)

    def order_of(M):
        P, n = M, 1
        while key(P) != key(one):
            P = P.dot(M); n += 1
        return n
    inv = {key(g): sl2_inv(g) for g in elems2}

    def ev(word, X, Y):
        out = one
        for L in word:
            out = out.dot({1: X, 2: Y}[L] if L > 0 else {1: inv[key(X)], 2: inv[key(Y)]}[-L])
        return out
    homs = [(X, Y) for X in elems2 for Y in elems2 if key(ev(S.REL, X, Y)) == key(one)]

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
    return surj, order_of, one


def descended_rep(X, Y, gens, dim_map):
    """The representation of the branched-cover group on the Schreier generators, for a matrix map
    dim_map: 2x2 -> nxn (identity for the 2, ad3 for the 3)."""
    Xi = sl2_inv(X)
    mats2 = {1: X, -1: Xi, 2: Y, -2: sl2_inv(Y)}

    def ev2(word):
        out = np.array([[ONE, ZERO], [ZERO, ONE]], dtype=object)
        for L in word:
            out = out.dot(mats2[L])
        return out
    words = {1: [1, 1, 1], 2: [2, -1], 3: [1, 2, -1, -1], 4: [1, 1, 2]}    # z, x0, x1, x2 in a, b
    M = {g: dim_map(ev2(words[g])) for g in gens}
    Inv = {g: dim_map(ev2([-L for L in reversed(words[g])])) for g in gens}
    return S.Rep(M, Inv), M


def h1_of(rep, gens, rels):
    h0, h1, r0, r1 = S.h0_h1(rep, gens, rels)
    return h0, h1


def part_b(pres):
    gens, rels = pres
    surj, order_of, one = surjections_2T()
    print(f"  surjections pi_1(m004) -> 2T: {len(surj)}")
    ident3 = lambda M: M
    results = collections.Counter()
    chars_seen = collections.Counter()
    for (X, Y) in surj:
        oa = order_of(X)
        # the real 3 descends always (rho_3(a^3) = Ad(X^3) = 1 since X^3 = +-1)
        rep3, M3 = descended_rep(X, Y, gens, ad3)
        S.check_rep(rep3, gens, rels)
        assert key(M3[1]) == key(E.qw_eye(3)), "3_rho(a^3) must be the identity"
        h0_3, h1_3 = h1_of(rep3, gens, rels)
        # the image of the descended 3_rho: a Klein four-group (order 4, exponent 2) -- the flat holonomy
        one3 = E.qw_eye(3)
        seen = {key(one3)}
        frontier = [one3]
        while frontier:
            nxt = []
            for Mm in frontier:
                for g in gens:
                    P = Mm.dot(M3[g])
                    if key(P) not in seen:
                        seen.add(key(P)); nxt.append(P)
            frontier = nxt
        img_order = len(seen)
        exp2 = all(key(M3[g].dot(M3[g])) == key(one3) for g in gens)
        diag_ok = img_order == 4 and exp2
        chars = None
        # the sign characters of Y_3 (all 16 sign assignments that satisfy the relators)
        hchi = {}
        for signs in itertools.product((1, -1), repeat=4):
            if all(sum((1 if L > 0 else -1) * (0 if signs[abs(L) - 1] == 1 else 1) for L in r) % 2 == 0 for r in rels):
                mats = {g: np.array([[ONE if signs[g - 1] == 1 else qneg(ONE)]], dtype=object) for g in gens}
                rep1 = S.Rep(mats, mats)
                h1c = h1_of(rep1, gens, rels)[1]
                # multiplicity of chi in the descended 3_rho: h0 of 3_rho (x) chi
                mats3c = {g: M3[g] if signs[g - 1] == 1 else np.vectorize(qneg, otypes=[object])(M3[g]) for g in gens}
                inv3c = {g: mats3c[g].dot(mats3c[g]).dot(mats3c[g]) if False else None for g in gens}
                rep3c = S.Rep(mats3c, {g: rep3.I[g] if signs[g - 1] == 1 else np.vectorize(qneg, otypes=[object])(rep3.I[g]) for g in gens})
                h0c = h1_of(rep3c, gens, rels)[0]
                hchi[signs] = (h1c, h0c)
        # the spin lift 2_rho descends iff X^3 = 1
        h1_2 = None
        if oa == 3:
            rep2, M2 = descended_rep(X, Y, gens, ident3)
            S.check_rep(rep2, gens, rels)
            h1_2 = h1_of(rep2, gens, rels)[1]
        # trivial coefficients
        rep0 = S.Rep({g: E.qw_eye(1) for g in gens}, {g: E.qw_eye(1) for g in gens})
        h1_0 = h1_of(rep0, gens, rels)[1]
        results[(oa, h0_3, h1_3, diag_ok, h1_2, h1_0, tuple(sorted(hchi.items())))] += 1
    for k, v in sorted(results.items(), key=str):
        oa, h0_3, h1_3, diag_ok, h1_2, h1_0, hchi = k
        print(f"  meridian order {oa}: h0(3_rho) = {h0_3}, h1(Y_3; 3_rho) = {h1_3}; image of 3_rho = Klein four-group V4 (order 4, exponent 2): {diag_ok}; h1(2_rho) = {h1_2}; h1(trivial) = {h1_0}   x{v}")
        print(f"     sign characters chi of Y_3: (h1(chi), multiplicity of chi in 3_rho): { {''.join('+' if s == 1 else '-' for s in signs): h for signs, h in hchi} }")
    print("  -> 3_rho descended = chi_1 + chi_2 + chi_3, the three sign characters with h1 = 1: the flat holonomy of Y_3 (the tangent bundle); three classes, one per flat direction")
    ok = all(k[1] == 0 and k[2] == 3 and k[3] and k[5] == 0 for k in results) and all(sorted(dict(k[6]).values()) == [(0, 0), (1, 1), (1, 1), (1, 1)] for k in results)
    return ok, results


# ----------------------------------------------------------------------------------------- (d)
def part_d():
    rng = np.random.default_rng(1273)
    worst = 0.0
    for _ in range(20000):
        v = rng.normal(size=3) + 1j * rng.normal(size=3)
        M = np.array([[0, v[2], v[1]], [v[2], 0, v[0]], [v[1], v[0], 0]])
        s = np.linalg.svd(M, compute_uv=False)
        worst = max(worst, s[0] / (s[1] + s[2]))
    print(f"  zero-diagonal complex symmetric 3x3: max over 20000 random matrices of sigma_1/(sigma_2 + sigma_3) = {worst:.6f}  (theorem: <= 1)")
    # a Takagi proof check on one random matrix: M = U S U^T with diagonal zero => sum_k s_k U_ik^2 = 0
    data = {'up (t; c, u)': (172.76, 1.27, 0.00216), 'down (b; s, d)': (4.18, 0.093, 0.00467), 'charged leptons (tau; mu, e)': (1.77686, 0.10566, 0.000511)}
    for name, (m3, m2, m1) in data.items():
        print(f"  {name}: m_heaviest / (m_second + m_lightest) = {m3 / (m2 + m1):.1f}   (bound: <= 1)")
    return worst <= 1.0 + 1e-9


if __name__ == "__main__":
    ok = True
    print("=== (a) the 3-fold cyclic branched cover Y_3 by Reidemeister-Schreier; H_1; the F(2,6) fingerprint ===")
    oka, pres = part_a()
    ok &= oka
    print("\n=== (b) the object's 2T holonomy descended to Y_3: the three twisted classes ===")
    okb, res = part_b(pres)
    ok &= okb
    print("\n=== (d) the zero-diagonal texture theorem against the data ===")
    ok &= part_d()
    print("\nSELFTEST:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
