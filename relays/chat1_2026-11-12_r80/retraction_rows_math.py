"""
REVIEW 80, the web seat: the statements of mathematics in the last section of main's docs/RETRACTIONS.md (at c40446392)
that can be recomputed with nothing behind the firewall, recomputed here with this seat's own code.  Nothing of main's is
imported or run.  The rule and the expected outcomes are written below before any run; this file is committed and pushed,
and its sha256 recorded, before it is run.

THE ROWS AND WHAT IS EXPECTED (each expectation is the row's own statement):

  M28 the figure-eight knot group, as the subgroup of PSL(2, O3) (O3 = Z[w], w a primitive cube root of unity) generated
      by x = [[1, 1], [0, 1]] and y = [[1, 0], [-w, 1]] (Riley's generators).  The row: "in SL(2, O3/(4))/{+-1} the image
      of the knot group already has the geometric index 12, and 6 at (2)".
        EXPECTED: index of the image in SL(2, O3/(2))/{+-1} is 6; in SL(2, O3/(4))/{+-1} it is 12.
        Also computed, with no expectation from the row: the index in SL(2, O3/(8))/{+-1}.  If the level is (4), it is 12.
      The orders of SL(2, O3/(n)) are counted by brute force over all matrices at (2) and (4).  At (8) the count would
      take 16.7 million determinants, so the formula |SL(2, F4)| * 4^(3(k-1)) is used there, and the counts at (2) and
      (4) are printed beside the formula's values as its check.
      What would count as not holding: any index other than the expected one.
  M24 in sl(2, Q), h = diag(1, -1) and s = [[0, 1], [1, 0]].  The row: "diag(1, -1) and the swap have zero common
      centralizer".  EXPECTED: the centralizer of h alone has dimension 1, of s alone 1, of both 0.
  M25 "none in real radicals; it is expressible by complex radicals".  What is computed are the premises of the standard
      theorem (casus irreducibilis), not the theorem: the minimal polynomial of cos(2 pi/7) over Q has degree 3 and a
      positive discriminant (three real roots); cos(2 pi/7) = 1 - 2 sin(pi/7)^2, so a real-radical form of sin(pi/7) would
      give one of cos(2 pi/7); and sin(pi/7) lies in the cyclotomic field Q(zeta_28), which is abelian over Q.
        EXPECTED: degree 3, discriminant > 0, the identity holds exactly, the minimal polynomial of sin(pi/7) has degree 6.
  M23 the row's counts: 338 with +I and 305 with -I of 643.  EXPECTED: 338 + 305 = 643.
  M32 the row's "209 = 11 x 19".  EXPECTED: true.

Usage: retraction_rows_math.py
"""
import itertools

import sympy as sp


# --- M28: O3/(n) as pairs (a, b) = a + b w, with w^2 = -1 - w --------------------------------------------------------
def mul(p, q, n):
    a, b = p
    c, d = q
    # (a + b w)(c + d w) = ac + (ad + bc) w + bd w^2 = (ac - bd) + (ad + bc - bd) w
    return ((a * c - b * d) % n, (a * d + b * c - b * d) % n)


def add(p, q, n):
    return ((p[0] + q[0]) % n, (p[1] + q[1]) % n)


def mmul(A, B, n):
    (a, b), (c, d) = A
    (e, f), (g, h) = B
    return ((add(mul(a, e, n), mul(b, g, n), n), add(mul(a, f, n), mul(b, h, n), n)),
            (add(mul(c, e, n), mul(d, g, n), n), add(mul(c, f, n), mul(d, h, n), n)))


def neg(p, n):
    return ((-p[0]) % n, (-p[1]) % n)


def det(A, n):
    (a, b), (c, d) = A
    return add(mul(a, d, n), neg(mul(b, c, n), n), n)


def order_sl(n):
    ring = [(a, b) for a in range(n) for b in range(n)]
    return sum(1 for a, b, c, d in itertools.product(ring, repeat=4) if det(((a, b), (c, d)), n) == (1 % n, 0))


def image(n):
    one, zero = (1 % n, 0), (0, 0)
    w = (0, 1 % n)
    x = ((one, one), (zero, one))
    y = ((one, zero), (neg(w, n), one))
    seen = {x, y}
    frontier = [x, y]
    while frontier:
        nxt = []
        for A in frontier:
            for G in (x, y):
                B = mmul(A, G, n)
                if B not in seen:
                    seen.add(B)
                    nxt.append(B)
        frontier = nxt
    minus = lambda A: tuple(tuple(neg(e, n) for e in row) for row in A)
    with_sign = seen | {minus(A) for A in seen}
    central = 2 if (neg((1 % n, 0), n) != (1 % n, 0)) else 1
    return len(seen), len(with_sign) // central, central


def m28():
    for n in (2, 4, 8):
        if n == 8:
            sl = 60 * 64 ** 2          # |SL(2, R)| = |SL(2, F4)| * 4^(3(k-1)) for R = O3/(2^k); checked against the count at n = 2, 4
        else:
            sl = order_sl(n)
        img, img_psl, central = image(n)
        psl = sl // central
        print('M28 n = %d: |SL(2, O3/(n))| = %d%s; image in SL %d; in SL/{+-1} %d of %d; index %s'
              % (n, sl, ' (formula)' if n == 8 else ' (counted)', img, img_psl, psl, sp.Rational(psl, img_psl)))
    print('M28 the formula at n = 2 and 4: %d and %d' % (60, 60 * 64))


def m24():
    a, b, c = sp.symbols('a b c')
    X = sp.Matrix([[a, b], [c, -a]])
    h = sp.diag(1, -1)
    s = sp.Matrix([[0, 1], [1, 0]])

    def dim(*els):
        eqs = [e for E in els for e in (X * E - E * X)]
        sol = sp.linsolve(eqs, [a, b, c])
        (v,) = sol
        return len({sym for comp in v for sym in sp.Matrix([comp]).free_symbols})
    print('M24 dim of the centralizer in sl(2, Q): of h %d; of s %d; of both %d' % (dim(h), dim(s), dim(h, s)))


def m25():
    x = sp.symbols('x')
    c = sp.cos(2 * sp.pi / 7)
    pc = sp.minimal_polynomial(c, x)
    ps = sp.minimal_polynomial(sp.sin(sp.pi / 7), x)
    print('M25 minimal polynomial of cos(2pi/7): %s; degree %d; irreducible over Q: %s; discriminant %s (> 0: %s)'
          % (pc, sp.degree(pc, x), sp.Poly(pc, x).is_irreducible, sp.discriminant(pc, x), sp.discriminant(pc, x) > 0))
    print('M25 cos(2pi/7) - (1 - 2 sin(pi/7)^2) = %s; minimal polynomial of sin(pi/7) has degree %d'
          % (sp.simplify(c - (1 - 2 * sp.sin(sp.pi / 7) ** 2)), sp.degree(ps, x)))
    z = sp.exp(2 * sp.pi * sp.I / 28)
    print('M25 sin(pi/7) = (z^2 - z^-2)/(2i) with z = exp(2 pi i/28): %s' % sp.simplify(sp.sin(sp.pi / 7) - (z ** 2 - z ** -2) / (2 * sp.I)).equals(0))


if __name__ == '__main__':
    m28()
    m24()
    m25()
    print('M23 338 + 305 == 643: %s' % (338 + 305 == 643))
    print('M32 11 * 19 == 209: %s' % (11 * 19 == 209))
