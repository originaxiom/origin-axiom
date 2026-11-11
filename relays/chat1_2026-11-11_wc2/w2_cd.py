#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
W-C2, THEOREMS C AND D OF THE AGY LANE'S NOTE (8ef2df5ac), COMPUTED BY THIS SEAT'S OWN ROUTE.   The web seat
(chat1), 2026-11-11.  Exact integer and rational arithmetic.  None of the lane's code was run or opened.

C2  In E8 (D8 with its half-integer coset of even coordinate sum, roots of norm 2): (0,0,0,0,0,1,1,1) is not in the
    lattice; H = (0,0,0,0,0,2,2,2) is, and is the shortest lattice vector on that line; H is orthogonal to the roots of
    d5 (on the first five coordinates) and a2 (on the last three); on the half-integer roots whose first five
    coordinates carry an even number of minus signs, H pairs as +3 on the 16 with last three signs (+,+,+) and as -1
    on each of the 3 x 16 with two minus signs among the last three.
C3  On the A4 lattice {h in Z^5, sum 0} (roots of norm 2): the nonzero vectors with (1/2)|h|^2 <= 12 number 1020; the
    least (1/2)|h|^2 with |h_1| = N is N(N+1)/2 for N = 1..4.  Rademacher's function, |Phi| of L^6 R L R and of
    L^5 R L^2 R^2: 5 and 4.
C4  dP9: H_2 = I_{1,9}; F = 3H - sum E_i has F^2 = 0; Sigma_0 = E_9 has Sigma_0^2 = -1 and Sigma_0.F = 1; the eight
    classes E1-E2, ..., E7-E8, H-E1-E2-E3 are orthogonal to F and Sigma_0, their intersection matrix is minus the
    Cartan matrix of E8, of determinant 1, and the reflections they generate give 240 roots; chi = 12;
    C = 5 Sigma_0 + 6F has C^2 = 35, C.K = -5 (K = -F), genus 16, and as a 5-sheeted cover of P^1 ramification 40;
    the pairs (k_m, k_l) in F5^2 with k_m k_l = 0: 9.
D   The extended Dynkin diagram of E8 with the node of mark 5 removed is A4 + A4; its roots are 40 of the 240; the
    remaining 200 fall in four grades of 50 by the removed node's coefficient modulo 5; for some orientation of the two
    chains, the grades' weights are those of (10, 5), (10b, 5b), (5, 10b), (5b, 10).  With q(10) = 1, q(5b) = 2,
    phi charges 3 and 2: 1 + 1 + 3 = 0 and 1 + 2 + 2 = 0 modulo 5; and 2 q_S = 0 forces q_S = 0, with
    2 + 0 + 3 = 0 for the singlet's coupling to the 5b and phi of charge 3.

WHAT WOULD COUNT AS NOT REPRODUCING (written before the run): any of the statements above failing exactly.
CONTROLS that must fail: (1, 1, 1, 0, 0, 0, 0, 0)... a vector of odd coordinate sum is not in E8; removing the node of
mark 6 instead does not give four grades of 50.
DISCLOSED: the lane's statement of the singlet's trilinear coupling stands on a starred line; the seat checks the
readable part, the bilinear condition, and the coupling to the phi of charge 3.  The phrase "positive chirality" is
taken as an even number of minus signs among the first five coordinates.
"""
import itertools
import sys
from fractions import Fraction as Fr


def e8_roots():
    roots = []
    for i, j in itertools.combinations(range(8), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [0] * 8
                v[i] = si
                v[j] = sj
                roots.append(tuple(Fr(x) for x in v))
    for signs in itertools.product((1, -1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.append(tuple(Fr(s, 2) for s in signs))
    return roots


def in_e8(v):
    v = [Fr(x) for x in v]
    allint = all(x.denominator == 1 for x in v)
    allhalf = all((2 * x).denominator == 1 and x.denominator == 2 for x in v)
    return (allint or allhalf) and sum(v) % 2 == 0


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def det_frac(m):
    a = [[Fr(x) for x in r] for r in m]
    n = len(a)
    d = Fr(1)
    for i in range(n):
        p = next((r for r in range(i, n) if a[r][i] != 0), None)
        if p is None:
            return Fr(0)
        if p != i:
            a[i], a[p] = a[p], a[i]
            d = -d
        d *= a[i][i]
        for r in range(i + 1, n):
            f = a[r][i] / a[i][i]
            for c in range(i, n):
                a[r][c] -= f * a[i][c]
    return d


def rademacher(m):
    """Rademacher's Phi on SL(2,Z), by Dedekind sums"""
    a, b = m[0]
    c, d = m[1]
    def s(h, k):
        k = abs(k)
        tot = Fr(0)
        for r in range(1, k):
            x = Fr(r, k)
            y = Fr(h * r, k)
            def saw(z):
                fl = z.numerator // z.denominator
                return Fr(0) if z == fl else z - fl - Fr(1, 2)
            tot += saw(x) * saw(y)
        return tot
    if c == 0:
        return Fr(b, d)
    sign = 1 if c > 0 else -1
    return Fr(a + d, c) - 12 * sign * s(a, c)


def matw(w):
    L = ((1, 0), (1, 1))
    R = ((1, 1), (0, 1))
    m = ((1, 0), (0, 1))
    for ch in w:
        x = L if ch == 'L' else R
        m = ((m[0][0] * x[0][0] + m[0][1] * x[1][0], m[0][0] * x[0][1] + m[0][1] * x[1][1]),
             (m[1][0] * x[0][0] + m[1][1] * x[1][0], m[1][0] * x[0][1] + m[1][1] * x[1][1]))
    return m


def main():
    out = []
    roots = e8_roots()
    print('C2')
    a = (0, 0, 0, 0, 0, 1, 1, 1)
    H = (0, 0, 0, 0, 0, 2, 2, 2)
    c2a = (not in_e8(a)) and in_e8(H) and (not in_e8(tuple(Fr(1, 2) * x for x in a))) and not in_e8((0, 0, 0, 0, 0, Fr(3, 2), Fr(3, 2), Fr(3, 2)))
    d5 = [r for r in roots if all(x == 0 for x in r[5:]) and all(x.denominator == 1 for x in r)]
    a2 = [r for r in roots if all(x == 0 for x in r[:5]) and sum(r[5:]) == 0]
    orth = all(dot(H, r) == 0 for r in d5 + a2)
    spin = [r for r in roots if r[0].denominator == 2 and sum(1 for x in r[:5] if x < 0) % 2 == 0]
    one = [r for r in spin if all(x > 0 for x in r[5:])]
    three = [r for r in spin if sum(1 for x in r[5:] if x < 0) == 2]
    p1 = {dot(H, r) for r in one}
    p3 = {dot(H, r) for r in three}
    print('    roots %d; d5 roots %d; a2 roots %d; H orthogonal to both: %s' % (len(roots), len(d5), len(a2), orth))
    print('    (0,..,1,1,1) in E8: %s; H in E8: %s; spinor roots with even minus signs in the first five: %d = %d + %d; H pairs %s and %s'
          % (in_e8(a), in_e8(H), len(spin), len(one), len(three), sorted(p1), sorted(p3)))
    c2 = c2a and orth and len(d5) == 40 and len(a2) == 6 and len(one) == 16 and len(three) == 48 and p1 == {3} and p3 == {-1}
    out.append(('C2', c2))
    print('C3')
    vecs = [h for h in itertools.product(range(-5, 6), repeat=5) if sum(h) == 0 and any(h) and sum(x * x for x in h) <= 24]
    mins = {}
    for N in range(1, 5):
        mins[N] = min(Fr(sum(x * x for x in h), 2) for h in itertools.product(range(-5, 6), repeat=5) if sum(h) == 0 and abs(h[0]) == N)
    phi6 = rademacher(matw('LLLLLLRLR'))
    phi5 = rademacher(matw('LLLLLRLLRR'))
    print('    nonzero A4 vectors with (1/2)|h|^2 <= 12: %d; least (1/2)|h|^2 with |h_1| = N: %s; Phi(L^6RLR) = %s, Phi(L^5RL^2R^2) = %s'
          % (len(vecs), {N: str(v) for N, v in mins.items()}, phi6, phi5))
    c3 = len(vecs) == 1020 and [mins[N] for N in range(1, 5)] == [1, 3, 6, 10] and abs(phi6) == 5 and abs(phi5) == 4
    out.append(('C3', c3))
    print('C4')
    Q = [[1] + [0] * 9] + [[0] * i + [0] + [0] * 0 for i in range(0)]
    Q = [[0] * 10 for _ in range(10)]
    Q[0][0] = 1
    for i in range(1, 10):
        Q[i][i] = -1
    def ip(x, y):
        return sum(Q[i][j] * x[i] * y[j] for i in range(10) for j in range(10))
    Hc = [1] + [0] * 9
    E = [[0] * 10 for _ in range(10)]
    for i in range(1, 10):
        E[i][i] = 1
    F = [3] + [-1] * 9
    S0 = E[9]
    al = [[E[i][k] - E[i + 1][k] for k in range(10)] for i in range(1, 8)] + [[Hc[k] - E[1][k] - E[2][k] - E[3][k] for k in range(10)]]
    G = [[ip(x, y) for y in al] for x in al]
    cartan_e8 = [[2, 0, -1, 0, 0, 0, 0, 0], [0, 2, 0, -1, 0, 0, 0, 0], [-1, 0, 2, -1, 0, 0, 0, 0], [0, -1, -1, 2, -1, 0, 0, 0],
                 [0, 0, 0, -1, 2, -1, 0, 0], [0, 0, 0, 0, -1, 2, -1, 0], [0, 0, 0, 0, 0, -1, 2, -1], [0, 0, 0, 0, 0, 0, -1, 2]]
    negG = [[-x for x in r] for r in G]
    detG = det_frac(negG)
    # roots by closing the simple roots under the simple reflections, in the coordinates of the alpha basis
    simple = [tuple(1 if i == j else 0 for j in range(8)) for i in range(8)]
    def refl(v, i):
        c = sum(negG[i][j] * v[j] for j in range(8))   # <v, alpha_i> with the positive form -G
        return tuple(v[j] - (c if j == i else 0) for j in range(8))
    rootset = set(simple)
    frontier = list(simple)
    while frontier:
        nxt = []
        for v in frontier:
            for i in range(8):
                w = refl(v, i)
                if w not in rootset:
                    rootset.add(w)
                    nxt.append(w)
        frontier = nxt
    sig = (sum(1 for i in range(10) if Q[i][i] > 0), sum(1 for i in range(10) if Q[i][i] < 0))
    C = [5 * S0[k] + 6 * F[k] for k in range(10)]
    K = [-x for x in F]
    C2v = ip(C, C)
    CK = ip(C, K)
    g = (C2v + CK) // 2 + 1
    deg = ip(C, F)
    ram = (2 * g - 2) - deg * (-2)
    pairs = sum(1 for km in range(5) for kl in range(5) if (km * kl) % 5 == 0)
    print('    signature %s; det Q = %s; F^2 = %d; S0^2 = %d; S0.F = %d; alphas orthogonal to F and S0: %s; Gram = -Cartan(E8) up to order: %s; det = %s; roots %d'
          % (sig, det_frac(Q), ip(F, F), ip(S0, S0), ip(S0, F), all(ip(x, F) == 0 and ip(x, S0) == 0 for x in al),
             sorted(sorted(r) for r in negG) == sorted(sorted(r) for r in cartan_e8), detG, len(rootset)))
    print('    chi = 3 + 9 = %d; C^2 = %d; C.K = %d; genus %d; C.F = %d; ramification over P^1 = %d; flux pairs %d' % (3 + 9, C2v, CK, g, deg, ram, pairs))
    c4 = (sig == (1, 9) and det_frac(Q) == -1 and ip(F, F) == 0 and ip(S0, S0) == -1 and ip(S0, F) == 1
          and all(ip(x, F) == 0 and ip(x, S0) == 0 for x in al) and detG == 1 and len(rootset) == 240
          and C2v == 35 and CK == -5 and g == 16 and deg == 5 and ram == 40 and pairs == 9)
    out.append(('C4', c4))
    print('D')
    # Bourbaki simple roots of E8 in the even coordinates
    s = [None] * 9
    s[1] = tuple(Fr(x, 2) for x in (1, -1, -1, -1, -1, -1, -1, 1))
    s[2] = tuple(Fr(x) for x in (1, 1, 0, 0, 0, 0, 0, 0))
    s[3] = tuple(Fr(x) for x in (-1, 1, 0, 0, 0, 0, 0, 0))
    s[4] = tuple(Fr(x) for x in (0, -1, 1, 0, 0, 0, 0, 0))
    s[5] = tuple(Fr(x) for x in (0, 0, -1, 1, 0, 0, 0, 0))
    s[6] = tuple(Fr(x) for x in (0, 0, 0, -1, 1, 0, 0, 0))
    s[7] = tuple(Fr(x) for x in (0, 0, 0, 0, -1, 1, 0, 0))
    s[8] = tuple(Fr(x) for x in (0, 0, 0, 0, 0, -1, 1, 0))
    marks = {1: 2, 2: 3, 3: 4, 4: 6, 5: 5, 6: 4, 7: 3, 8: 2}
    theta = tuple(sum(marks[i] * s[i][k] for i in range(1, 9)) for k in range(8))
    s0 = tuple(-x for x in theta)
    rs = set(roots)
    simple_ok = all(r in rs for r in s[1:]) and theta in rs and all(dot(s[i], s[i]) == 2 for i in range(1, 9))
    # coefficients of each root in the simple basis
    B = [[s[i][k] for i in range(1, 9)] for k in range(8)]
    def coeffs(r):
        a = [row[:] + [r[k]] for k, row in enumerate(B)]
        n = 8
        for i in range(n):
            p = next(rr for rr in range(i, n) if a[rr][i] != 0)
            a[i], a[p] = a[p], a[i]
            for rr in range(n):
                if rr != i and a[rr][i] != 0:
                    f = a[rr][i] / a[i][i]
                    a[rr] = [x - f * y for x, y in zip(a[rr], a[i])]
        return [a[i][n] / a[i][i] for i in range(n)]
    def grades(removed):
        g = {}
        for r in roots:
            c = coeffs(r)[removed - 1]
            g.setdefault(int(c) % marks[removed], []).append(r)
        return {k: len(v) for k, v in sorted(g.items())}, g
    gsz, g = grades(5)
    ctrl, _ = grades(4)
    chain1 = [s[1], s[3], s[4], s[2]]
    chain2 = [s[6], s[7], s[8], s0]
    sub = len(g[0])
    def labels(r, chain):
        return tuple(int(dot(r, a)) for a in chain)
    # A4 representations in the standard model, Dynkin labels by e_i - e_{i+1}
    def a4_weights(kind):
        e = [tuple(1 if i == j else 0 for j in range(5)) for i in range(5)]
        if kind == '5':
            ws = e
        elif kind == '5b':
            ws = [tuple(-x for x in v) for v in e]
        elif kind == '10':
            ws = [tuple(e[i][k] + e[j][k] for k in range(5)) for i, j in itertools.combinations(range(5), 2)]
        else:
            ws = [tuple(-e[i][k] - e[j][k] for k in range(5)) for i, j in itertools.combinations(range(5), 2)]
        return sorted(tuple(w[i] - w[i + 1] for i in range(4)) for w in ws)
    def tensor(k1, k2):
        return sorted((x, y) for x in a4_weights(k1) for y in a4_weights(k2))
    target = sorted([tensor('10', '5'), tensor('10b', '5b'), tensor('5', '10b'), tensor('5b', '10')])
    found = False
    for o1, o2 in itertools.product((False, True), repeat=2):
        c1 = chain1[::-1] if o1 else chain1
        c2 = chain2[::-1] if o2 else chain2
        got = sorted(sorted((labels(r, c1), labels(r, c2)) for r in g[j]) for j in (1, 2, 3, 4))
        if got == target:
            found = True
            print('    the four grades match (10,5), (10b,5b), (5,10b), (5b,10) with the chains %s and %s'
                  % ('reversed' if o1 else 'as listed', 'reversed' if o2 else 'as listed'))
    q = {'10': 1, '5b': 2}
    yuk = ((q['10'] + q['10'] + 3) % 5 == 0, (q['10'] + q['5b'] + 2) % 5 == 0)
    qs = [x for x in range(5) if (2 * x) % 5 == 0]
    sing = (2 + qs[0] + 3) % 5 == 0 if qs else False
    print('    simple roots valid: %s; grade sizes by the coefficient of the node of mark 5 modulo 5: %s; roots in grade 0: %d; control (node of mark 6): %s'
          % (simple_ok, gsz, sub, ctrl))
    print('    charges: 10 x 10 x phi(3): %s; 10 x 5b x phi(2): %s; 2 q_S = 0 forces q_S in %s; 5b x S x phi(3): %s' % (yuk[0], yuk[1], qs, sing))
    d = simple_ok and gsz == {0: 40, 1: 50, 2: 50, 3: 50, 4: 50} and found and all(yuk) and qs == [0] and sing
    out.append(('D', d))
    ctrl_ok = in_e8((1, 1, 1, 0, 0, 0, 0, 0)) is False and set(ctrl.values()) != {50, 40}
    print()
    for n, ok in out:
        print('%s: %s' % (n, 'REPRODUCED' if ok else 'NOT REPRODUCED'))
    print('CONTROLS: %s' % ('as they must' if ctrl_ok else 'BROKEN'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
