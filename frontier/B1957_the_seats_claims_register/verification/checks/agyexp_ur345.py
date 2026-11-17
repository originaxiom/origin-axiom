"""B1957: agy-exp's UR-3, UR-4, UR-5 (X-RELATIONS-2), the exact part: the cusp exponents of its overlap's entries and the
'gap ratios' it derives from them, recomputed by main from the entry rule as its note and script text state it:
  c_L = (2i + 1)/6 + q_L a / 3,  c_R = (2j + 1)/6 - q_R a / 3;  over integer shifts d_L = c_L - l1, d_R = c_R - l2,
  the entry's exponent is the least of 3 |d_L^2 - d_R^2| when d_L d_R > 0 and 3 (d_L^2 + d_R^2) otherwise;
  the three singular values' exponents are the tropical ones (least entry, least 2 x 2 minor, the determinant).
This checks the arithmetic the seat reports for its own rule.  It does not check that the rule is the object's: the rule
belongs to the seat's overlap, a supplied ansatz with a cut-off (its own page of premises says so).  Data-free."""
import itertools, math
from fractions import Fraction as Fr


def entry(i, j, a, ql, qr):
    cl = Fr(2 * i + 1, 6) + Fr(ql, 3) * a; cr = Fr(2 * j + 1, 6) - Fr(qr, 3) * a; best = None
    for l1 in range(math.floor(cl) - 3, math.floor(cl) + 4):
        for l2 in range(math.floor(cr) - 3, math.floor(cr) + 4):
            dl, dr = cl - l1, cr - l2; e = 3 * abs(dl * dl - dr * dr) if dl * dr > 0 else 3 * (dl * dl + dr * dr)
            best = e if best is None or e < best else best
    return best


def exps(a, ql, qr):
    E = [[entry(i, j, a, ql, qr) for j in range(3)] for i in range(3)]; w1 = min(min(r) for r in E)
    w2 = min(min(E[r1][c1] + E[r2][c2], E[r1][c2] + E[r2][c1]) for r1, r2 in itertools.combinations(range(3), 2) for c1, c2 in itertools.combinations(range(3), 2))
    w3 = min(sum(E[k][p[k]] for k in range(3)) for p in itertools.permutations(range(3)))
    return w3 - w2, w2 - w1, w1


def gap(a, ql, qr):
    e1, e2, e3 = exps(a, ql, qr); return None if e2 == e3 else (e1 - e3) / (e2 - e3)


prim = lambda N: sorted({Fr(p, N) for p in range(N) for q in range(N) if math.lcm(Fr(p, N).denominator, Fr(q, N).denominator) == N})
SECT = {"up (1, -4)": (1, -4), "down (1, 2)": (1, 2), "lepton (-3, 6)": (-3, 6)}

if __name__ == "__main__":
    for N in (5, 10, 15):
        for lab, (ql, qr) in SECT.items():
            gs = sorted({g for a in prim(N) if (g := gap(a, ql, qr)) is not None}); und = sum(1 for a in prim(N) if gap(a, ql, qr) is None)
            print("order %2d, %-15s gap ratios (e1 - e3)/(e2 - e3) over the points: %s%s" % (N, lab + ":", [str(g) for g in gs], "" if not und else " (%d values of a with e2 = e3)" % und))
    same5 = all(exps(a, 1, 2) == exps(a, -3, 6) for a in prim(5)); six = all(exps(a, -3, 6) == exps((6 * a) % 1, 1, 2) for a in prim(15)); three = all(exps(a, -3, 6) == exps((3 * a) % 1, 1, 2) for a in prim(15))
    ten = [c for c in range(10) if all(exps(a, -3, 6) == exps((c * a) % 1, 1, 2) for a in prim(10))]
    print("the lepton's exponents equal the down quark's at the same point at order 5: %s; at order 15 they equal the down quark's at 6w: %s (at 3w: %s); at order 10 the multipliers c with lepton(w) = down(c w) for all points: %s" % (same5, six, three, ten))
