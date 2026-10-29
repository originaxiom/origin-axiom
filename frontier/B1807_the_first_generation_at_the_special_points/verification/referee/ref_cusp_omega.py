"""Cusp bookkeeping and D's zero at omega, own route (ref_cr, refkit).
 * |D|/|R|^2 at tau = 2.5i, 3i, 3.5i: the exponent in |q| = e^{-2 pi Im tau} (B1654's law is in the nome e^{i pi tau});
 * |a.R|/s1 for a 19/2 section at the same heights (the draft omits this factor at the cusp: s1 and |R|^2 blow up there);
 * |D|/|R|^2 near omega along three directions: slope 1 (a linear zero).
    python3 ref_cusp_omega.py -> ref_cusp_omega.json
"""
import json, pathlib, math
import numpy as np
import mpmath as mp
from ref_cr import c_vec, R_vec
from ref_near_i import make_section, evalsec, masses

HERE = pathlib.Path(__file__).resolve().parent
out = {}
ys = [2.5, 3.0, 3.5]
DR = []; LF = []
fs = make_section(5, 1)
for y in ys:
    c = c_vec(1j * y); R = R_vec(1j * y); DR.append(abs(np.sum(c * R ** 2)) / np.sum(abs(R) ** 2))
    a, Rm = evalsec(fs, mp.mpc(0, y)); lf, m23, s = masses(a, Rm)
    LF.append(float(abs(sum(x * z for x, z in zip(a, Rm))) / s[0]))
lq = [-2 * math.pi * y for y in ys]
def sl(v, corr=None):
    return [round((math.log(v[k + 1]) - math.log(v[k]) - (math.log(corr[k + 1] / corr[k]) if corr else 0)) / (lq[k + 1] - lq[k]), 4) for k in range(len(v) - 1)]
out["|D|/|R|^2 exponent in |q| (raw)"] = sl(DR)
out["|D|/|R|^2 exponent in |q| after dividing out Im tau"] = sl(DR, ys)
out["|a.R|/s1 exponent in |q| (19/2)"] = sl(LF)
out["sum (should be B1691's 1, with Im tau)"] = [round(a + b, 4) for a, b in zip(sl(DR, ys), sl(LF))]
W = complex(np.exp(2j * np.pi / 3)); om = {}
for phi in (0.3, 1.9, 4.1):
    v = []
    for e in (1e-2, 1e-3, 1e-4):
        t = W + e * np.exp(1j * phi); c = c_vec(t); R = R_vec(t); v.append(abs(np.sum(c * R ** 2)) / np.sum(abs(R) ** 2))
    om["phi=%g" % phi] = {"|D|/|R|^2": [float("%.4e" % x) for x in v], "slopes": [round(math.log10(v[k] / v[k + 1]), 4) for k in range(2)]}
out["D near omega"] = om
(HERE / "ref_cusp_omega.json").write_text(json.dumps(out, indent=1)); print(json.dumps(out, indent=1))
