"""B1957: agy-exp's card X-L5 and its answers to M37 and M38 (its branch at d7bb27195), the exact statements recomputed on main
(data-free; nothing of the seat's run).  Main's own side of the level-5 law is checks/agyexp_x_foundation.py, F5.
 L1  E = q_L^2 + q_R^2 + c q_H^2 mod 5 for the three sectors at c = 0, +-1, +-2, 5, 7, and the determinant exponents 3E.
 L2  the magnetized overlap's E_mag = q_L^2 - q_R^2 mod 5 and its determinant exponents.
 L3  |1 - zeta| = 2 sin(pi/5) (the spread from the reference point) and |zeta - zeta^4| = 2 sin(2 pi/5) (the diameter).
 L4  the permutation [4, 3, 5, 0, 1, 2, 6, 7]: its cycles, order 4, and that it fixes the coordinates 6 and 7, so every root
     +-e6 +- e7 of the weak so(4); so(6) on the coordinates {0, 1, 2} has 12 roots."""
import math, cmath, itertools
sec = {"sec_1 (1, -4)": (1, -4), "sec_2 (1, 2)": (1, 2), "sec_3 (-3, 6)": (-3, 6)}
rows = {c: tuple((qL ** 2 + qR ** 2 + c * (qL + qR) ** 2) % 5 for qL, qR in sec.values()) for c in (0, 1, -1, 2, -2, 5, 7)}
print("L1: E mod 5 by c: %s; the seat's (2, 0, 0) at 0 and 5, (1, 4, 4) at 1, (3, 1, 1) at -1, (0, 3, 3) at 2 and 7, (4, 2, 2) at -2: %s; residues c mod 5 at which sec_1 closes, and sec_2 and sec_3 both: %s; determinant exponents 3E at c = 2: %s"
      % (rows, rows == {0: (2, 0, 0), 5: (2, 0, 0), 1: (1, 4, 4), -1: (3, 1, 1), 2: (0, 3, 3), 7: (0, 3, 3), -2: (4, 2, 2)}, ([c for c in range(5) if (17 + 9 * c) % 5 == 0], [c for c in range(5) if (5 + 9 * c) % 5 == 0 and (45 + 9 * c) % 5 == 0]), tuple(3 * e % 5 for e in rows[2])))
Em = tuple((qL ** 2 - qR ** 2) % 5 for qL, qR in sec.values())
print("L2: E_mag = q_L^2 - q_R^2 mod 5: %s (the seat: (0, 2, 3)); its determinant exponents 3 E_mag: %s (the seat: (0, 1, 4)); frame D1 at c = 2: %s" % (Em, tuple(3 * e % 5 for e in Em), tuple(3 * e % 5 for e in rows[2])))
z = cmath.exp(2j * math.pi / 5)
print("L3: |1 - zeta| - 2 sin(pi/5) = %.1e; |zeta - zeta^4| - 2 sin(2 pi/5) = %.1e" % (abs(1 - z) - 2 * math.sin(math.pi / 5), abs(z - z ** 4) - 2 * math.sin(2 * math.pi / 5)))
perm = [4, 3, 5, 0, 1, 2, 6, 7]; seen, cyc = set(), []
for i in range(8):
    if i not in seen:
        c, j = [], i
        while j not in seen: seen.add(j); c.append(j); j = perm[j]
        if len(c) > 1: cyc.append(tuple(c))
order = math.lcm(*[len(c) for c in cyc])
so6 = [r for r in itertools.product((-1, 0, 1), repeat=3) if sorted(map(abs, r)) == [0, 1, 1]]
print("L4: cycles %s, order %d; fixes 6 and 7: %s; so(6) on {0, 1, 2}: %d roots" % (cyc, order, perm[6] == 6 and perm[7] == 7, len(so6)))
