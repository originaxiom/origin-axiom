"""The agy lane's Theorem A, its last part (P-747, for P-318's B1228 item): the simply-laced simple Lie algebras of rank 1 to 8
at level 1, from their Cartan matrices alone, on main's own code. The lane's code is not run; its statement was read through
the mask.

For a simply-laced algebra at level 1: c = rank; the primaries are the classes of the weight lattice P modulo the root
lattice Q (|P/Q| = |det C|); a class's conformal weight is half its least norm; T = e^{2 pi i (h - c/24)} on each class, and
its order is the lcm of the denominators of h - c/24.
  A1  sigma = c/6 = 1 holds for A6, D6 and E6 (so 'sigma = 1 picks E6 uniquely', B1228, is false as stated; P-318 says so)
  A2  sigma = 1 with exactly three primaries holds for E6 alone among them
  A3  SL(2, Z/4) (order 48) has more than one element of order 2; the binary octahedral group has exactly one (-I): not isomorphic
Least norms are found by enumeration in a box and checked against the closed forms for A_n and D_n (a control).
No data.   python3 -B level_one_on_main.py"""
import json, math, itertools, pathlib
from fractions import Fraction as Fr
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
def run(lock=False):
    """the checks; returns OUT. `lock` asks for the lighter form a lock can run (see the code)"""
    OUT = {}; LOG = []
    def say(*a):
        s = " ".join(str(x) for x in a); LOG.append(s); print(s, flush=True)

    def cartan(kind, n):
        C = sp.zeros(n, n)
        for i in range(n): C[i, i] = 2
        if kind == "A":
            for i in range(n - 1): C[i, i + 1] = C[i + 1, i] = -1
        elif kind == "D":
            for i in range(n - 2): C[i, i + 1] = C[i + 1, i] = -1
            C[n - 3, n - 1] = C[n - 1, n - 3] = -1                 # the fork at node n-3
        elif kind == "E":
            # chain 0-1-2-...-(n-2), with node n-1 attached to node 2
            for i in range(n - 2): C[i, i + 1] = C[i + 1, i] = -1
            C[2, n - 1] = C[n - 1, 2] = -1
        return C

    ALG = [("A", n) for n in range(1, 9)] + [("D", n) for n in range(4, 9)] + [("E", n) for n in (6, 7, 8)]
    if lock: ALG = [("A", 3), ("D", 4), ("A", 6), ("D", 6), ("E", 6)]      # the lock's lighter form: the three of rank 6 and two controls
    def classes_least_norms(C, box):
        """P/Q classes in the basis of fundamental weights: lambda = sum m_i w_i, (lambda, lambda) = m^T C^-1 m;
        the class of m is m mod the rows of C (the simple roots in the w-basis). Least norm per class by enumeration."""
        n = C.shape[0]; Ci = C.inv()
        # class label: C^-1 m mod Z^n  (m in Q iff C^-1 m integral)
        best = {}
        for m in itertools.product(range(-box, box + 1), repeat=n):
            mv = sp.Matrix(m); lab = tuple(Fr(int(sp.numer(x)), int(sp.denom(x))) % 1 for x in (Ci * mv))
            nm = Fr(str((mv.T * Ci * mv)[0, 0]))
            if lab not in best or nm < best[lab]: best[lab] = nm
        return best

    rows = []
    for kind, n in ALG:
        C = cartan(kind, n); det = abs(int(C.det()))
        box = 1 if (n >= 7 or lock) else 2                 # box 1 holds a minuscule weight of every class; that all are found is asserted
        best = classes_least_norms(C, box)
        c = Fr(n); hs = sorted(v / 2 for v in best.values())
        torder = math.lcm(*[(h - c / 24).denominator for h in hs])
        rows.append({"algebra": "%s%d" % (kind, n), "c": str(c), "sigma": str(c / 6), "det_C": det, "classes_found": len(best),
                     "h": [str(h) for h in hs], "T_order": torder})
        say("%s%d  c=%s  sigma=%s  |det C|=%d  classes found %d  h=%s  T-order %d" % (kind, n, c, c / 6, det, len(best), [str(h) for h in hs], torder))
        assert len(best) == det, "the box is too small for %s%d" % (kind, n)
    OUT["level_one"] = rows
    # control: closed forms
    for r in rows:
        k, n = r["algebra"][0], int(r["algebra"][1:])
        if k == "A": want = sorted(Fr(j * (n + 1 - j), 2 * (n + 1)) for j in range(n + 1))
        elif k == "D": want = sorted([Fr(0), Fr(1, 2), Fr(n, 8), Fr(n, 8)])
        else: continue
        assert [Fr(h) for h in r["h"]] == want, r["algebra"]
    OUT["control_closed_forms_A_and_D"] = True
    sig1 = [r["algebra"] for r in rows if Fr(r["sigma"]) == 1]
    sig1_three = [r["algebra"] for r in rows if Fr(r["sigma"]) == 1 and r["det_C"] == 3]
    OUT["A1_sigma_one"] = sig1; OUT["A2_sigma_one_and_three_primaries"] = sig1_three
    say("A1 sigma = 1:", sig1, "| A2 sigma = 1 and three primaries:", sig1_three)
    assert sig1 == ["A6", "D6", "E6"] and sig1_three == ["E6"]

    # A3: SL(2, Z/4) against the binary octahedral group
    def mul(A, B, p):
        return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % p for j in range(2)) for i in range(2))
    SL24 = [((a, b), (c, d)) for a, b, c, d in itertools.product(range(4), repeat=4) if (a * d - b * c) % 4 == 1]
    I2 = ((1, 0), (0, 1))
    inv_sl = [A for A in SL24 if A != I2 and mul(A, A, 4) == I2]
    OUT["A3_SL2_Z4_order"] = len(SL24); OUT["A3_SL2_Z4_involutions"] = len(inv_sl)
    # the binary octahedral group as 48 unit quaternions: the 24 Hurwitz units and the 24 of the form (+-1 +-1 0 0)/sqrt2 permuted
    q = []
    for s in itertools.product((1, -1), repeat=1):
        for i in range(4):
            v = [0, 0, 0, 0]; v[i] = s[0]; q.append(tuple(Fr(x) for x in v))
    for s in itertools.product((1, -1), repeat=4): q.append(tuple(Fr(x, 2) for x in s))
    r2 = []
    for i, j in itertools.combinations(range(4), 2):
        for s in itertools.product((1, -1), repeat=2):
            v = [0, 0, 0, 0]; v[i] = s[0]; v[j] = s[1]; r2.append(tuple(v))       # times 1/sqrt2, kept symbolic
    OUT["A3_2O_order"] = len(q) + len(r2)
    # an element of order 2 in a group of unit quaternions squares to 1: real part -1 is the only solution besides 1
    def sq_real(v, scale2):            # the real part of v^2 for v = (a, b, c, d)/sqrt(scale2)
        a, b, c, d = v; return Fr(a * a - b * b - c * c - d * d, scale2)
    order2 = [v for v in q if sq_real(v, 1) == 1 and v != (1, 0, 0, 0) and v[0] != 1] + [v for v in r2 if sq_real(v, 2) == 1]
    OUT["A3_2O_elements_whose_square_is_1_other_than_1"] = len(order2)
    say("A3 SL(2, Z/4): order", len(SL24), "involutions", len(inv_sl), "| 2O: order", OUT["A3_2O_order"], "elements of order 2:", len(order2))
    assert len(SL24) == 48 and OUT["A3_2O_order"] == 48 and len(order2) == 1 and len(inv_sl) > 1
    return OUT, LOG

if __name__ == "__main__":
    OUT, LOG = run()
    json.dump(OUT, open(HERE / "level_one_on_main.json", "w"), indent=1, default=str)
    open(HERE / "level_one_on_main_run.txt", "w").write("\n".join(LOG) + "\n")
