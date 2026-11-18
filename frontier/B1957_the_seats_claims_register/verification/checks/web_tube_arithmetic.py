"""B1957: the web seat's note 'the tube's own tau, firmed up' (2026-11-07): its extrapolation arithmetic redone on main
from the members it prints.  ARITHMETIC ONLY: the members themselves (the harmonic level surfaces of L^6 R (LR)^k at
k = 6, 7, 8 and the fifth subdivision) are the seat's and are not recomputed here; main's own instrument stops at
k = 2 (B1854; register row P-739).  Data-free.
 A1  the k-steps D6 = v7 - v6, D7 = v8 - v7 and their ratio, from the printed v6, v7, v8; D6/D5 from the printed steps
 A2  Aitken's limit on k = 6, 7, 8
 A3  the fifth subdivision at k = 1 and k = 8: the step ratio, Richardson's value at n <= 5 and at n <= 4, the shift
 A4  the firmed value = Aitken's limit + k = 8's shift; the k part of its error"""
v6, v7, v8 = 6.0652941, 6.0652696, 6.0652645                     # Im tau at the tube, n <= 4, as printed (seven decimals)
D5p, D6p, D7p = -1.1729e-4, -2.4475e-5, -5.1086e-6               # the steps as printed (five figures, from the unrounded members)
k1 = (6.1414324, 6.1472244, 6.1487034); k8 = (6.0575280, 6.0633304, 6.0648123)       # Im tau at n = 3, 4, 5
if __name__ == "__main__":
    D6, D7 = v7 - v6, v8 - v7
    print("A1: from the printed members: D6 = %.3e, D7 = %.3e (the note's -2.4475e-05 and -5.1086e-06, to the members' seven decimals); the ratios from the printed steps: D6/D5 = %.5f, D7/D6 = %.5f (the note's 0.20867 and 0.20872)" % (D6, D7, D6p / D5p, D7p / D6p))
    ait = v8 - D7p ** 2 / (D7p - D6p)
    print("A2: Aitken on k = 6, 7, 8 (printed steps): %.7f (the note's 6.065263178; the sealed estimate's centre 6.065263777 is %.1e above)" % (ait, 6.065263777 - ait))
    out = {}
    for name, (a, b, c) in (("k = 1", k1), ("k = 8", k8)):
        rho = (b - a) / (c - b); r5 = c + (c - b) / 3; r4 = b + (b - a) / 3; out[name] = (rho, r5, r4, r5 - r4)
        print("A3: %s: step ratio %.4f; Richardson at n <= 5: %.7f; at n <= 4: %.7f; the shift %+.3e" % (name, rho, r5, r4, r5 - r4))
    print("A3: the note's 3.916 and 6.1491965 with +4.14e-05 at k = 1; 3.915 and 6.0653063 with +4.18e-05 at k = 8; the two shifts differ by %.1e (its 3.5e-07, from unrounded members)" % abs(out["k = 8"][3] - out["k = 1"][3]))
    firm = 6.065263178 + 4.175e-5
    print("A4: the firmed value: 6.065263178 + 4.175e-05 = %.7f (the note's 6.0653049); the k part of its error, |limit - v8| = %.2e (its 1.35e-06); against main's B1854: k = 1 by this note 6.14920, main's calibration 6.1491" % (firm, abs(6.065263178 - v8)))
