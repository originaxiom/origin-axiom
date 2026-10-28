"""chat1, 2026-10-28: THE TWO W's, a second exact check after the read-only referee (post hoc, labelled; exact
arithmetic with Fractions, no data); committed before its one run.
The cover degree of a given line depends on how the frame's (a, b) is identified with the fibre's homology (any g in
GL(2, Z)); the set of possible degrees over all lines of an order does not. For N = 2, 5, 10, 25, 30: the set of least
k >= 1 with M^k v = v, and with M^k v = -v (charge conjugation), over every line v of exact order N, for M = LR; and M's
order on (Z/N)^2.
Run:  python3 -B bridge_check2.py"""
import math
from fractions import Fraction as Fr
from itertools import product
M = ((1, 1), (1, 2))


def act(v):
    a, b = v
    return ((M[0][0] * a + M[0][1] * b) % 1, (M[1][0] * a + M[1][1] * b) % 1)


def least(v, sign):
    target = v if sign > 0 else ((-v[0]) % 1, (-v[1]) % 1)
    w, k = act(v), 1
    while w != target:
        w, k = act(w), k + 1
        if k > 100000: return None
    return k


for N in (2, 5, 10, 25, 30):
    pts = [(Fr(i, N), Fr(j, N)) for i, j in product(range(N), repeat=2) if math.gcd(math.gcd(i, j), N) == 1]
    plus = sorted({least(v, 1) for v in pts}); minus = sorted({least(v, -1) for v in pts})
    order = math.lcm(*[least(v, 1) for v in pts])
    print("N = %2d: %4d lines of exact order N; least k with M^k v = v: %s; with M^k v = -v: %s; M's order on (Z/N)^2: %d"
          % (N, len(pts), plus, minus, order))
print("bridge_check2 exit 0")
