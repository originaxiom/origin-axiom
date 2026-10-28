"""chat1, 2026-10-28: the selector's (iv) with (ii)'s relaxation, after the relay's read-only referee. Post hoc, labelled;
exact arithmetic, no data; committed before its one run.
(ii) admits a line whose holonomies return to themselves up to SU(5)'s centre. The same relaxation in (iv): the monodromy
M (or -M, with the fibre's involution) maps (a, b) to itself up to a central shift, (M (a, b) - (a, b)) in (1/5)Z^2 mod 1.
Every such line, to order 60 (the relaxed fixed lines have order dividing 25); how many break SU(5) (5a or 5b not an
integer); and whether any lies on slope 2/5 (a = 2/5, or a = 3/5, its image under the sign flip).
Run:  python3 -B bundle_check_centre.py"""
import math
from fractions import Fraction as Fr
lines = sorted({(Fr(i, n), Fr(j, n)) for n in range(1, 61) for i in range(n) for j in range(n)})
central = lambda x: (5 * x).denominator == 1
for name, M in (("LR", ((1, 1), (1, 2))), ("RL", ((2, 1), (1, 1)))):
    for sgn, tag in ((1, "M"), (-1, "-M (with the involution)")):
        for relax, rtag in ((False, "strictly"), (True, "up to SU(5)'s centre")):
            ok = (central if relax else (lambda x: x.denominator == 1))
            fx = [(a, b) for a, b in lines if ok(sgn * (M[0][0] * a + M[0][1] * b) - a) and ok(sgn * (M[1][0] * a + M[1][1] * b) - b)]
            brk = [(a, b) for a, b in fx if not (central(a) and central(b))]
            on25 = [(a, b) for a, b in brk if a in (Fr(2, 5), Fr(3, 5))]
            print("%s, %-26s %-21s: %3d lines, orders %s; breaking SU(5): %3d (orders %s; e.g. %s); breaking on slope 2/5: %d"
                  % (name, tag + ",", rtag, len(fx), sorted({math.lcm(a.denominator, b.denominator) for a, b in fx}), len(brk),
                     sorted({math.lcm(a.denominator, b.denominator) for a, b in brk}), [(str(a), str(b)) for a, b in brk[:2]], len(on25)))
print("bundle_check_centre exit 0")
