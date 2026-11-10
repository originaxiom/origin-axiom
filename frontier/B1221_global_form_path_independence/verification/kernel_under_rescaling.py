"""B1221, the correction of 2026-11-10 (P-604; data-free; exact rationals): the kernel when every abelian charge is
rescaled by k.

- **The group.** Z(SU(3)) x Z(SU(2)) x U(1): elements (a mod 3, b mod 2, c mod 1), acting on a field of triality t,
  duality s and integer charge k*y by the phase exp(2 pi i (a t/3 + b s/2 + k y c)).
- **The exact kernel.** e^c (t = s = 0, y = 6) forces 6 k c to be an integer, so c = m/(6k) with m mod 6k. Every
  kernel element is therefore on the grid of 6k points, and the enumeration over that grid is complete, not a sample.
- **The result.** The kernel is cyclic of order 6k for every k >= 1. It has order 6 only at k = 1.
- **The addendum's table** (2026-08-31) is the count on a fixed grid of 72 points, c = n/72. On that grid the count
  is 6 gcd(k, 12): the grid's answer, not the group's. Every row of the table is reproduced here from that grid.
  (`kernel_27.py`'s own default grid, n/12, gives a third count, 6 gcd(k, 2).)
- **Found by** the physics seat (its R05; SCHEDULED row 181), carried as P-604; the agy lane's relay of 2026-11-07
  states the same order. This file is main's own check; neither seat's code is run."""
from fractions import Fraction as F
from itertools import product
from math import gcd

G16 = [(1, 1, 1), (2, 0, -4), (2, 0, 2), (0, 1, -3), (0, 0, 6), (0, 0, 0)]     # Q u^c d^c L e^c nu^c
G10 = [(0, 1, 3), (0, 1, -3), (1, 0, -2), (2, 0, 2)]                           # H_u H_d D D^c
C27 = G16 + G10 + [(0, 0, 0)]


def kernel(comps, k, N):
    """The kernel elements with c on the grid n/N, charges rescaled by k."""
    return [(a, b, F(n, N)) for a, b in product(range(3), range(2)) for n in range(N)
            if all(((F(a * t, 3) + F(b * s, 2) + k * y * F(n, N)) % 1) == 0 for t, s, y in comps)]


def order(g):
    add = lambda x, y: ((x[0] + y[0]) % 3, (x[1] + y[1]) % 2, (x[2] + y[2]) % 1)
    o, e = 1, g
    while e != (0, 0, F(0)):
        e = add(e, g); o += 1
    return o


rows = []
for k in range(1, 25):
    exact = kernel(C27, k, 6 * k)                     # the complete grid for this k
    finer = kernel(C27, k, 72 * k)                    # a 12-fold finer grid finds nothing more
    grid72 = kernel(C27, k, 72)                       # the fixed grid that reproduces the addendum's table
    grid12 = kernel(C27, k, 12)                       # kernel_27.py's default grid
    assert len(exact) == len(finer) == 6 * k
    assert max(order(g) for g in exact) == 6 * k      # cyclic
    assert len(grid72) == 6 * gcd(k, 12) and len(grid12) == 6 * gcd(k, 2)
    rows.append("k = %2d   exact kernel order %3d (cyclic)   on the fixed grid n/72: %2d = 6 gcd(k, 12)" % (k, len(exact), len(grid72)))
print("\n".join(rows))
assert [k for k in range(1, 25) if len(kernel(C27, k, 6 * k)) == 6] == [1]
print("=> the kernel is Z_(6k); its order is 6 only at k = 1 (among k = 1..24; by the argument above, for every k)")
TABLE = {1: 6, 5: 6, 7: 6, 11: 6, 2: 12, 10: 12, 3: 18, 9: 18, 4: 24, 6: 36, 12: 72}      # the addendum's table, verbatim
assert all(len(kernel(C27, k, 72)) == v for k, v in TABLE.items())
print("=> the addendum's table is the 72-point grid's count, row for row")
print("=> 'kernel = 6 exactly when gcd(k, 6) = 1' holds on that grid only: at k = 5, 7, 11 the true orders are 30, 42, 66")
