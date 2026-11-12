"""
REVIEW 80, M11's addendum, the web seat: a post hoc check, written after reading the six differences M11 added (B731,
B732, B733, B942, B1030, B1067 over 38d2a36dc..0dda7b472).  Their corrections of 2026-11-11 say that "12 at (8)" is the
reading "in the quotient by every central unit of square one (order 960 at (4))", and B942's says that the image order
it quotes at (8), 2560, is the image's order in that quotient.  The sealed run (retraction_rows_math.py, 0fc1197a5)
computed the image of the knot group in SL(2, O3/(n)) and in SL(2, O3/(n))/{+-1}; it did not compute the quotient by
every central unit of square one.  This file does, with the same generators and the same arithmetic, imported from the
sealed file unchanged.  Computed once; post hoc: the expectations below are main's statements, read before this file.

  EXPECTED (main's pages): at (4) the quotient has order 960; at (8) the image's order in the quotient is 2560.  Also
  printed: the number of central units of square one at (2), (4) and (8), and the index of the image in each quotient.

Usage: retraction_rows_math_posthoc_2.py
"""
import importlib.util
import os

spec = importlib.util.spec_from_file_location('sealed', os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                                     'retraction_rows_math.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def run(n):
    one, zero = (1 % n, 0), (0, 0)
    ring = [(a, b) for a in range(n) for b in range(n)]
    central = [u for u in ring if m.mul(u, u, n) == one]                  # scalars u with u^2 = 1 lie in SL(2)
    w = (0, 1 % n)
    x = ((one, one), (zero, one))
    y = ((one, zero), (m.neg(w, n), one))
    seen, frontier = {x, y}, [x, y]
    while frontier:
        nxt = []
        for A in frontier:
            for G in (x, y):
                B = m.mmul(A, G, n)
                if B not in seen:
                    seen.add(B)
                    nxt.append(B)
        frontier = nxt
    scal = lambda u: ((u, zero), (zero, u))
    in_image = sum(1 for u in central if scal(u) in seen)
    sl = m.order_sl(n) if n < 8 else 60 * 64 ** 2
    q_order = sl // len(central)
    img_q = len(seen) // in_image
    print('n = %d: central units of square one %d; |SL| %d; quotient %d; image in SL %d, meeting the centre in %d; '
          'image in the quotient %d; index %d' % (n, len(central), sl, q_order, len(seen), in_image, img_q, q_order // img_q))


for n in (2, 4, 8):
    run(n)
