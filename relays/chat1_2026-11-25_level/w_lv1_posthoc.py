#!/usr/bin/env python3
"""POST HOC (written after the referee read of W-LV1, which computed most of what follows on its own code; so nothing
here is blind): four checks on frame C's coupling that the corrected relay leans on. Data-free.

    python3 -B w_lv1_posthoc.py <a checkout of main at be8c83d4f>      # prints; no file written

Same coupling and settings as w_lv1_level.py (determinant_law.parts, column 0.13, height 6, reading S). For matrices,
prop(A, B) is the relative residual of the best fit A = c B over complex c: |A - c B| / |A| (Frobenius).

Q1  near misses: at (0, 1/4) of order 4 and (0, 1/8) of order 8, the three cross pairs at the same point; the largest
    normalised singular-value difference of each pair the unit rule does not tie.
Q2  swapped ties are transposes: for (down, lep) at N = 5 (k = 1), (up, lep) at N = 7 (k = 6), (up, down) at N = 9
    (k = 2) and up against itself at N = 15 (k = 11), prop(Y_t(w), Y_s(k w)^T) and prop(Y_t(w), Y_s(k w)); for the
    direct ties (up, down) at N = 6 and (down, lep) at N = 4 (k = 1), prop(Y_t(w), Y_s(w)).
Q3  the leptons and the point 3w: at (11/30, 2/5) and (8/15, 9/10) of order 30 on the act's line, prop(Y_lep(w),
    Y_lep(11 w)); and at those points and at (7/10, 2/5) and (1/5, 9/10) of order 10 on the act's line,
    prop(Y_lep(w), Y_dn(3 w)), where dn is the down sector with its doublet's charge negated, (6Y) = (-1, 2), added in
    memory only (B1949's relation).
Q4  the point negated: normalised singular values of every sector at w and -w, at the two order-30 points.

Reading: Q2, Q3 and Q4 hold if every stated residual or difference is below 1e-30 (the working precision is about
1e-40), and Q2's other column (transposed against untransposed) is above 1e-3. Q1 reports its values; a pair the rule
does not tie that agrees below 1e-30 would be a tie not of the unit form, which W-LV1 names as its failure.
"""
import sys, pathlib
from fractions import Fraction as Fr
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import w_lv1_level as W


def main():
    DL = W.load(sys.argv[1])
    mp, B = DL.mp, DL.B
    B.SIXY["Qn"] = -1
    B.SECTORS["dn"] = ("Qn", "d")

    def Y(a, b, sec):
        return DL.parts("0.13", 6.0, a % 1, b % 1, sec)[2]["S"]

    def prop(A, Bm):
        num = sum(mp.conj(Bm[i, j]) * A[i, j] for i in range(3) for j in range(3))
        den = sum(abs(Bm[i, j]) ** 2 for i in range(3) for j in range(3))
        c = num / den if den != 0 else mp.mpf(0)
        return mp.mnorm(A - c * Bm, "F") / mp.mnorm(A, "F")

    def svn(A):
        sv = sorted(abs(x) for x in mp.svd_c(A, compute_uv=False))
        return [x / sv[-1] for x in sv] if sv[-1] != 0 else sv

    def d(A, Bm):
        return max(abs(x - y) for x, y in zip(svn(A), svn(Bm)))

    worst = mp.mpf(0)
    print("Q1 near misses (largest normalised singular-value difference at the same point):")
    for (a, b, N) in ((Fr(0), Fr(1, 4), 4), (Fr(0), Fr(1, 8), 8)):
        for s, t in (("up", "down"), ("up", "lep"), ("down", "lep")):
            ties = W.tied(N, (B.SIXY[B.SECTORS[s][0]], B.SIXY[B.SECTORS[s][1]]),
                          (B.SIXY[B.SECTORS[t][0]], B.SIXY[B.SECTORS[t][1]]), False, ks=(1,))
            print("  N = %d (%s, %s), %s~%s: tied by k = 1: %s; difference %.1e" % (
                N, a, b, s, t, bool(ties), float(d(Y(a, b, s), Y(a, b, t)))), flush=True)
    print("Q2 swapped ties are transposes; direct ties equalities:")
    for (N, s, t, k, pts) in ((5, "down", "lep", 1, [(Fr(1, 5), Fr(2, 5)), (Fr(2, 5), Fr(4, 5))]),
                              (7, "up", "lep", 6, [(Fr(1, 7), Fr(2, 7)), (Fr(3, 7), Fr(1, 7))]),
                              (9, "up", "down", 2, [(Fr(1, 9), Fr(2, 9)), (Fr(4, 9), Fr(1, 3))]),
                              (15, "up", "up", 11, [(Fr(1, 15), Fr(2, 15)), (Fr(2, 5), Fr(1, 3))])):
        for (a, b) in pts:
            At, As = Y(a, b, t), Y(k * a, k * b, s)
            rT, r0 = prop(At, As.T), prop(At, As)
            worst = max(worst, rT)
            print("  N = %2d %s(w) against %s(%d w)^T at (%s, %s): %.1e; untransposed %.1e" % (
                N, t, s, k, a, b, float(rT), float(r0)), flush=True)
    for (N, s, t, pts) in ((6, "up", "down", [(Fr(1, 6), Fr(1, 3)), (Fr(1, 2), Fr(1, 3))]),
                           (4, "down", "lep", [(Fr(1, 4), Fr(1, 2)), (Fr(3, 4), Fr(1, 4))])):
        for (a, b) in pts:
            r = prop(Y(a, b, t), Y(a, b, s))
            worst = max(worst, r)
            print("  N = %2d %s(w) against %s(w) at (%s, %s): %.1e" % (N, t, s, a, b, float(r)), flush=True)
    print("Q3 the leptons and the point 3w:")
    for (a, b) in ((Fr(11, 30), Fr(2, 5)), (Fr(8, 15), Fr(9, 10))):
        r = prop(Y(a, b, "lep"), Y(11 * a, 11 * b, "lep"))
        worst = max(worst, r)
        print("  order 30 (%s, %s): lep(w) against lep(11 w): %.1e" % (a, b, float(r)), flush=True)
    for (a, b, n) in ((Fr(11, 30), Fr(2, 5), 30), (Fr(8, 15), Fr(9, 10), 30), (Fr(7, 10), Fr(2, 5), 10),
                      (Fr(1, 5), Fr(9, 10), 10)):
        r = prop(Y(a, b, "lep"), Y(3 * a, 3 * b, "dn"))
        worst = max(worst, r)
        print("  order %d (%s, %s): lep(w) against dn(3 w): %.1e; lep(w) against down(w), singular values %.1e" % (
            n, a, b, float(r), float(d(Y(a, b, "lep"), Y(a, b, "down")))), flush=True)
    print("Q4 the point negated (normalised singular values, every sector):")
    for (a, b) in ((Fr(11, 30), Fr(2, 5)), (Fr(8, 15), Fr(9, 10))):
        for s in ("up", "down", "lep"):
            r = d(Y(a, b, s), Y(-a, -b, s))
            worst = max(worst, r)
            print("  (%s, %s) %s: %.1e" % (a, b, s, float(r)), flush=True)
    print("READING: the largest residual or difference in Q2 to Q4 is %.1e -> %s" % (
        float(worst), "holds" if worst < 1e-30 else "FAILS"))


if __name__ == "__main__":
    main()
