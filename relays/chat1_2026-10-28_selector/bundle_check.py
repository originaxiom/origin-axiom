"""chat1, 2026-10-28: the selector's (iv), the flat lines that extend over the mapping torus. Post hoc, labelled; exact
arithmetic, no data; committed before its one run.
A flat line (a, b) on the fibre extends over the mapping torus of the monodromy M as a flat bundle when M fixes it,
M (a, b) = (a, b) mod 1; with the fibre's elliptic involution allowed, when -M fixes it. The figure-eight's monodromy is
LR = [[1, 1], [1, 2]] (or RL = [[2, 1], [1, 1]], its conjugate by the swap). Lines to order 60; their orders; whether
5a and 5b are integers (the holonomies central in SU(5), so SU(5) unbroken).
Run:  python3 -B bundle_check.py"""
import math
from fractions import Fraction as Fr
lines = sorted({(Fr(i, n), Fr(j, n)) for n in range(1, 61) for i in range(n) for j in range(n)})
for name, M in (("LR", ((1, 1), (1, 2))), ("RL", ((2, 1), (1, 1)))):
    for sgn, tag in ((1, "M"), (-1, "-M (with the involution)")):
        fx = [(a, b) for a, b in lines
              if (sgn * (M[0][0] * a + M[0][1] * b) - a) % 1 == 0 and (sgn * (M[1][0] * a + M[1][1] * b) - b) % 1 == 0]
        print("%s, fixed by %s: %d lines %s; orders %s; SU(5)-preserving (5a, 5b integers): %s"
              % (name, tag, len(fx), [(str(a), str(b)) for a, b in fx], sorted({math.lcm(a.denominator, b.denominator) for a, b in fx}),
                 all((5 * a).denominator == 1 and (5 * b).denominator == 1 for a, b in fx)))
print("bundle_check exit 0")
