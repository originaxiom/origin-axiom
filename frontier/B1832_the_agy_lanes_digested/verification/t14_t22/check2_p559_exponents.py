"""CHECK 2 (P-559; agy Theorem 15 Part A, Theorem 22 Part B.3).  Data-free.  MAIN's code only.

Claim: E(c_1 - c_i) = ||3 alpha|| and E(c_j - c_k) = ||3 alpha + 1/2|| = 1/2 - ||3 alpha|| in B1788's convention (a modulus
~ exp(-E 2 pi Im tau)); i.e. ||3a||/2 and 1/4 - ||3a||/2 in the 4 pi convention -- sector-independent.
Method: main's cA (down sector; c_s is sector-blind, check 1) at Re tau = 0.13, Im tau = 2.0 ... 4.5, two offsets p2 per
slope; local exponents E(y1, y2) = -ln|D(y2)/D(y1)| / (2 pi (y2 - y1)).  Then B1788's hypothesis (a) in exact arithmetic:
as worded (both differences at least at rate |E00 - E11|) and term by term (c_j - c_k against |E00 - E11|, c_1 - c_i
against |E01 - E10|), E_ij = ||q_L a + i/2||^2 + ||q_R a + j/2||^2 - 1/8 (B1788 section 1).
"""
import json, math, pathlib
from fractions import Fraction as Fr
import numpy as np
import mainB

B = mainB.B()
HERE = pathlib.Path(__file__).resolve().parent


def nz(x):
    x = Fr(x); f = x - math.floor(x); return min(f, 1 - f)


SLOPES = [Fr(1, 7), Fr(1, 5), Fr(2, 5), Fr(4, 9), Fr(3, 8), Fr(1, 10), Fr(3, 10), Fr(2, 7), Fr(1, 9), Fr(5, 12), Fr(3, 7)]
P2S = [0.13, 0.29]
YS = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
rows = []
for a in SLOPES:
    pred_1i, pred_jk = float(nz(3 * a)), float(nz(3 * a + Fr(1, 2)))
    for p2 in P2S:
        d1i, djk = [], []
        for y in YS:
            t = complex(0.13, y); w = B.line_w(float(a), p2, t); x, yy = B.sector_twists(w, t, 1, 2)
            R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
            d1i.append(c["1"] - c["i"]); djk.append(c["j"] - c["k"])
        loc = lambda d: [(-math.log(abs(d[k + 1] / d[k])) / (2 * math.pi * (YS[k + 1] - YS[k]))) for k in range(len(d) - 1)]
        rows.append({"alpha": str(a), "p2": p2, "pred_1i": pred_1i, "pred_jk": pred_jk,
                     "local_E_1i": loc(d1i), "local_E_jk": loc(djk),
                     "diff_1i": d1i, "diff_jk": djk})
        r = rows[-1]
        print(f"alpha={a} p2={p2}: E(c1-ci) pred {pred_1i:.4f} local {[round(v, 4) for v in r['local_E_1i']]} | "
              f"E(cj-ck) pred {pred_jk:.4f} local {[round(v, 4) for v in r['local_E_jk']]}", flush=True)

# exact counts of B1788's hypothesis (a)
SECT = [(1, -4), (1, 2), (-3, 6)]
def counts(nmax):
    n = worded_fail = tbt_fail = 0; ties_jk = ties_1i = 0; fails = []
    for N in range(2, nmax + 1):
        for p in range(1, N):
            a = Fr(p, N)
            if math.gcd(p, N) != 1 or a >= Fr(1, 2) or (6 * a).denominator == 1:
                continue
            e1i, ejk = nz(3 * a), nz(3 * a + Fr(1, 2))
            for ql, qr in SECT:
                n += 1
                dx, dy = nz(ql * a) - Fr(1, 4), nz(qr * a) - Fr(1, 4)
                b0011, b0110 = abs(dx + dy), abs(dx - dy)
                if min(e1i, ejk) < b0011:
                    worded_fail += 1; fails.append((str(a), (ql, qr)))
                if ejk < b0011 or e1i < b0110:
                    tbt_fail += 1
                ties_jk += ejk == b0011; ties_1i += e1i == b0110
    return {"cases": n, "as_worded_fail": worded_fail, "term_by_term_fail": tbt_fail,
            "ties_jk": ties_jk, "ties_1i": ties_1i, "as_worded_fail_list": fails}
cnt = {"N<=12": counts(12), "N<=20": counts(20)}
# B1788's three named down lines against |E00 - E11| and |E01 - E10|
named = {}
for a in (Fr(2, 5), Fr(1, 7), Fr(4, 9)):
    dx, dy = nz(a) - Fr(1, 4), nz(2 * a) - Fr(1, 4)
    named[str(a)] = {"E_jk": str(nz(3 * a + Fr(1, 2))), "E_1i": str(nz(3 * a)), "|E00-E11|": str(abs(dx + dy)),
                     "|E01-E10|": str(abs(dx - dy))}
for k, v in cnt.items():
    print(k, {kk: vv for kk, vv in v.items() if kk != "as_worded_fail_list"})
print("named", named)
(HERE / "check2_p559_exponents_out.json").write_text(json.dumps({"rows": rows, "counts": cnt, "named_down_lines": named}, indent=1))
