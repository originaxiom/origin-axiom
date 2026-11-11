#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
W-C1, FINDING E2: THE FIGURE-EIGHT KNOT GROUP'S CONGRUENCE LEVEL, COMPUTED AGAIN BY THIS SEAT'S OWN ROUTE.
The web seat (chat1), 2026-11-11.  Data-free: exact arithmetic in Z[w], w^2 + w + 1 = 0, and SnapPy for one volume.

Written before the seat has read main's lock (tests/test_b734_m004_congruence.py), main's mend (c61dc18e6, 95988c96b)
or the advisor seat's re-audit 6.  The seat had read the finding (row E2 of the advisor seat's findings page, its digits
masked), its acceptance row ("The lock asserts index 12 at level (4), computed in SL/{+-1}"), and the subject of main's
commit c61dc18e6, which prints the orders 10, 320 and 20,480 and the indices 6 and 12.  So X2 and X3 are not blind.

THE ROUTE
  G is the image of the figure-eight knot group under Riley's pair A = rows (1, 1), (0, 1) and B = rows (1, 0), (-w, 1),
  inside SL(2, O), O = Z[w].
  C0  The pair satisfies a relation of the knot group: three standard writings are tested exactly; at least one must
      hold, and which one is reported.
  C1  The images of G in SL(2, O/I) for I = (2), (4), (8), by closing the generators' images under products; their
      orders; whether -I lies in them; their indices in SL(2, O/I)/{+-1}.  |SL(2, O/2^k)| = 60 * 64^(k-1).
  C2  [PSL(2, O) : G] from volumes: the volume of the knot's complement over the volume of H^3/PSL(2, O), which is
      3^(3/2) zeta_K(2) / (4 pi^2), zeta_K(2) = zeta(2) L(2, chi_-3).
  C3  The level.  2 is inert in O (x^2 + x + 1 has no root modulo 2), so the ideals containing (8) are (1), (2), (4),
      (8).  Since SL(2, O) maps onto SL(2, O/I), G contains Gamma(I) exactly when the image's index equals [PSL(2,O):G].
      Then the largest such ideal among those containing (8) is the level; that the ideals I with Gamma(I) in G are closed
      under sums is the standard consequence of strong approximation for SL(2), cited and not computed.
  CONTROL  The same closure with -w replaced by -1 (that pair generates the modular group's image).  Its index modulo
      (2) must not be 6.

EXPECTATIONS (written before the run)
  X0  C0: at least one writing of the relation holds.
  X1  C1: the closure terminates, and the orders are 10, 320 and 20480.
  X2  C1: the indices in SL/{+-1} are 6 at (2), 12 at (4), 12 at (8).
  X3  C2: the ratio of volumes is 12 to 1e-8.
  X4  C3: so the level is (4): Gamma(4) lies in G and Gamma(2) does not.
  X5  CONTROL: with -1 for -w the image modulo (2) has order 6 and index 10.
"""
import sys
from collections import deque

import mpmath as mp


def omul(x, y, n):
    """(a + b w)(c + d w) in (Z/n)[w], w^2 = -1 - w"""
    a, b = x
    c, d = y
    # ac + (ad + bc) w + bd w^2 = (ac - bd) + (ad + bc - bd) w
    return ((a * c - b * d) % n, (a * d + b * c - b * d) % n)


def oadd(x, y, n):
    return ((x[0] + y[0]) % n, (x[1] + y[1]) % n)


def mmul(P, Q, n):
    (p11, p12), (p21, p22) = P
    (q11, q12), (q21, q22) = Q
    return ((oadd(omul(p11, q11, n), omul(p12, q21, n), n), oadd(omul(p11, q12, n), omul(p12, q22, n), n)),
            (oadd(omul(p21, q11, n), omul(p22, q21, n), n), oadd(omul(p21, q12, n), omul(p22, q22, n), n)))


def minv(P, n):
    """inverse of a determinant-one matrix: rows (d, -b), (-c, a)"""
    (a, b), (c, d) = P
    neg = lambda x: ((-x[0]) % n, (-x[1]) % n)
    return ((d, neg(b)), (neg(c), a))


def mred(P, n):
    return tuple(tuple(((e[0] % n, e[1] % n)) for e in row) for row in P)


def closure(gens, n, cap=10 ** 6):
    I = (((1, 0), (0, 0)), ((0, 0), (1, 0)))
    I = mred(I, n)
    gs = [mred(g, n) for g in gens] + [minv(mred(g, n), n) for g in gens]
    seen = {I}
    q = deque([I])
    while q:
        x = q.popleft()
        for g in gs:
            y = mmul(x, g, n)
            if y not in seen:
                seen.add(y)
                if len(seen) > cap:
                    raise SystemExit('closure exceeded the cap')
                q.append(y)
    return seen


def exact_mul(P, Q):
    # over Z[w] with no reduction: use a large modulus that never wraps for these small words
    return mmul(P, Q, 10 ** 12)


def exact_inv(P):
    return minv(P, 10 ** 12)


def norm_exact(P):
    """map entries back from residues mod 10**12 to signed integers"""
    f = lambda v: v - 10 ** 12 if v > 10 ** 11 else v
    return tuple(tuple((f(e[0]), f(e[1])) for e in row) for row in P)


def word(letters, A, B):
    Ai, Bi = exact_inv(A), exact_inv(B)
    m = {'a': A, 'A': Ai, 'b': B, 'B': Bi}
    out = (((1, 0), (0, 0)), ((0, 0), (1, 0)))
    for ch in letters:
        out = exact_mul(out, m[ch])
    return norm_exact(out)


def main():
    print('W-C1, E2: the congruence level of the figure-eight knot group, by the seat\'s own route')
    A = (((1, 0), (1, 0)), ((0, 0), (1, 0)))          # rows (1, 1), (0, 1)
    B = (((1, 0), (0, 0)), ((0, -1), (1, 0)))         # rows (1, 0), (-w, 1)
    A = norm_exact(mred(A, 10 ** 12))
    B = norm_exact(mred(B, 10 ** 12))
    # C0: three writings of the figure-eight relation, each as a word that should be the identity
    writings = {
        'a w = w b, w = b a^-1 b^-1 a': 'a' + 'bABa' + 'B' + 'AbaB',          # a w b^-1 w^-1 with w = bABa
        'a w = w b, w = b^-1 a b a^-1': 'a' + 'BabA' + 'B' + 'aBAb',
        'b w = w a, w = a^-1 b a b^-1': 'b' + 'AbaB' + 'A' + 'bABa',          # b w a^-1 w^-1
    }
    ident = (((1, 0), (0, 0)), ((0, 0), (1, 0)))
    held = []
    for name, wd in writings.items():
        r = word(wd, A, B)
        ok = r == ident or r == (((-1, 0), (0, 0)), ((0, 0), (-1, 0)))
        held.append(ok)
        print('    C0  %-34s  relator = %s   holds (up to sign): %s' % (name, r, ok))
    x0 = any(held)
    print('X0: %s' % ('HOLDS' if x0 else 'FAILS'))
    print()

    print('C1  images modulo 2^k')
    res = {}
    for k in (1, 2, 3):
        n = 2 ** k
        img = closure([A, B], n)
        order = len(img)
        minus = mred((((-1, 0), (0, 0)), ((0, 0), (-1, 0))), n)
        has_minus = minus in img
        full = 60 * 64 ** (k - 1)
        # index in SL/{+-1} = |SL| / |image.{+-1}|; modulo 2, -I = I
        ipm = order if (has_minus or k == 1) else 2 * order
        index = full // ipm
        res[k] = (order, has_minus, index)
        print('    I = (%d): |image| = %d;  -I in image: %s;  |SL(2, O/I)| = %d;  index in SL/{+-1} = %d'
              % (n, order, has_minus, full, index))
    x1 = [res[k][0] for k in (1, 2, 3)] == [10, 320, 20480]
    x2 = [res[k][2] for k in (1, 2, 3)] == [6, 12, 12]
    print('X1: %s' % ('HOLDS' if x1 else 'FAILS'))
    print('X2: %s' % ('HOLDS' if x2 else 'FAILS'))
    print()

    print('C2  the index from volumes')
    mp.mp.dps = 30
    try:
        import snappy
        vol = mp.mpf(str(snappy.ManifoldHP('m004').volume()))
        src = 'SnapPy ManifoldHP'
    except Exception as exc:  # reported
        vol = None
        src = 'failed: %s' % type(exc).__name__
    L = (mp.zeta(2, mp.mpf(1) / 3) - mp.zeta(2, mp.mpf(2) / 3)) / 9
    zK = mp.zeta(2) * L
    vb = mp.mpf(3) ** mp.mpf(1.5) * zK / (4 * mp.pi ** 2)
    print('    L(2, chi_-3) = %s;  vol(H^3/PSL(2,O)) = %s;  vol(m004) = %s (%s)' % (mp.nstr(L, 20), mp.nstr(vb, 20), mp.nstr(vol, 20) if vol else '-', src))
    ratio = vol / vb if vol else None
    print('    ratio = %s' % (mp.nstr(ratio, 20) if ratio else '-'))
    x3 = ratio is not None and abs(ratio - 12) < mp.mpf(10) ** -8
    print('X3: %s' % ('HOLDS' if x3 else 'FAILS'))
    print()

    print('C3  the level')
    inert = all((x * x + x + 1) % 2 != 0 for x in range(2))
    print('    2 inert in Z[w]: %s;  ideals containing (8): (1), (2), (4), (8)' % inert)
    in4 = res[2][2] == 12
    in2 = res[1][2] == 12
    print('    Gamma(4) in G: %s;  Gamma(2) in G: %s' % (in4, in2))
    x4 = inert and x3 and in4 and not in2
    print('    so the level is (4): %s' % x4)
    print('X4: %s' % ('HOLDS' if x4 else 'FAILS'))
    print()

    print('CONTROL  -1 in place of -w')
    Bc = norm_exact(mred((((1, 0), (0, 0)), ((-1, 0), (1, 0))), 10 ** 12))
    imgc = closure([A, Bc], 2)
    print('    modulo (2): |image| = %d;  index = %d' % (len(imgc), 60 // len(imgc)))
    x5 = len(imgc) == 6 and 60 // len(imgc) == 10
    print('X5: %s' % ('HOLDS' if x5 else 'FAILS'))
    print()
    flags = [x0, x1, x2, x3, x4, x5]
    print('EXPECTATIONS: %d of 6 hold' % sum(flags))
    return 0


if __name__ == '__main__':
    sys.exit(main())
