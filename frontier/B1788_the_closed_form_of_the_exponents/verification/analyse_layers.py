"""Closed-form check: read layers_<tag>.json; per (line, sector) the measured exponents of the M entries, det M, the c_s
differences, and the singular-value ratios; test (i) M_ij ~ E_ij, (ii) e(m2/m3) = min(1/2, E(det M) - 2 mu_min) with the
MEASURED det M, (iii) E(det M) against E00 + E11 and against the c-difference terms."""
import sys, json, math
from fractions import Fraction as Fr
import numpy as np
import tropical as T
H = (4.0, 5.0, 6.0); X = np.array([2 * math.pi * y for y in H])


def fit(v):
    Y = np.log(np.maximum(np.abs(np.asarray(v, dtype=complex)), 1e-300)); A = np.vstack([X, np.ones(3)]).T
    (s, c), *_ = np.linalg.lstsq(A, Y, rcond=None); return float(-s)


def cx(z): return complex(z[0], z[1])


rows = json.load(open(sys.argv[1]))
print("%-6s %-6s %-4s | %-23s | %-23s | %6s %6s | %6s %6s %6s | %s" % ("alpha", "b", "sec", "M exps (00 01 10 11)", "E_ij closed", "detM", "E00+11", "dcjk", "dc1i", "m2/m3", "obs S/St ; pred(meas detM) ; closed"))
for r in rows:
    a = Fr(r["alpha"]); lf, rf = T.SECTORS[r["sec"]]; E = [float(e) for e in T.E(T.SIXY[lf] * a, T.SIXY[rf] * a)]
    hs = [r["h"][str(y)] for y in H]
    M = [[[cx(h["M"][i][j]) for h in hs] for j in range(2)] for i in range(2)]
    mexp = [fit(M[0][0]), fit(M[0][1]), fit(M[1][0]), fit(M[1][1])]
    det = [M[0][0][k] * M[1][1][k] - M[0][1][k] * M[1][0][k] for k in range(3)]
    ed = fit(det)
    def cdiff(s1, s2):
        v = [(h["c"][s1] - h["c"][s2]) if (h["c"][s1] is not None and h["c"][s2] is not None) else float("nan") for h in hs]
        return float("nan") if any(np.isnan(v)) else fit(v)
    obsS = fit([h["S"][0] for h in hs]); obsT = fit([h["St"][0] for h in hs])
    pred_meas = min(0.5, ed - 2 * min(mexp))
    closed = 0.5 - (T.nd(2 * T.SIXY[lf] * a) + T.nd(2 * T.SIXY[rf] * a)) / 2
    cs = " ".join("%s:%s" % (s, ("%.2f" % hs[-1]["c"][s]) if hs[-1]["c"][s] is not None else "None") for s in ("1", "i", "j", "k"))
    print("%-6s %-6s %-4s | %s | %s | %6.3f %6.3f | %6.3f %6.3f | %5.3f/%5.3f ; %5.3f ; %5.3f | c@6 %s" % (
        r["alpha"], r["b"], r["sec"], " ".join("%5.3f" % e for e in mexp), " ".join("%5.3f" % e for e in E), ed, E[0] + E[3],
        cdiff("j", "k"), cdiff("1", "i"), obsS, obsT, pred_meas, float(closed), cs))
