"""EXPLORATION (unsealed; excluded order N = 5 only): an out-of-sample test of the REFINED per-field cusp law, on the
line (0, 2) of L.R^25 and L.R^50 (the tower runs so far used only the line (0, 1)). Written, with its prediction,
before its run.

The first prediction (pf_towers.py, frozen before its run) took each unit's growth from its leading line only. It held
for the up quarks at N = 5 (C1 slopes -0.954, -1.903 against -1, -1.9) and failed for the down quarks (-0.828 against
-1). POST HOC, after seeing that run, the law was refined: a dressed unit's growth exponent is the largest over its
three components (lines e_i -> theta2, v+- -> theta4, theta3) of -(p + shift), floored at 0, with p the undressed
component exponent (F_i: -7/8, 7/8, 3/8; F+: 1/8, -1/8, 3/8; F-: 1/8, 7/8, -5/8 on e_i, v+, v-) and
shift = ||al + 1/2||^2 - 1/4 on theta2, ||al||^2 on theta4 and theta3, al = q lb / N. Post hoc it gives N = 5 line
(0, 1): up (1.00, 1.90), down (0.85, 1.95) against the observed C1 slopes (0.954, 1.903) and (0.828, 1.946).

PREDICTION for line (0, 2), N = 5 (al = 2q/5), C1 and the E4 cells (not ORTH, where the dressed f can grow):
  up (Q, u: a = 0.4, 0.4):  ln(m2/m3) slope -0.70,  ln(m1/m3) slope -2.00
  down (Q 0.4, d 0.2):      -0.85, -1.95
  leptons (L 0.2, e 0.4):   -0.85, -1.95
per 2 pi dy between L.R^25 and L.R^50; the line (0, 1) runs showed secant noise of about +-0.05 in C1.
"""
import sys, json, math, pickle, time
import mpmath as mp, flint
sys.path.insert(0, sys.argv[1]); import units_cells as UC
P = pickle.load(open(sys.argv[2], "rb"))
t0 = time.time(); flint.ctx.prec = 800
src = UC.PerFieldFactoredSource(P)
out = {}
for n in (25, 50):
    tr = n + 2; rho = math.sqrt(tr * tr - 4) / 2
    npts = int(2 * math.acosh(tr / 2) * (2 * math.pi * rho + 60)) // 4 * 4
    r = UC.run(src, n, (0, 2), 5, UC.SM, npts)
    out[f"L R^{n} N=5 line (0,2)"] = r
    print(f"L R^{n} line (0,2) rho={r['rho']:.3f} closure {r['closure']} t={time.time()-t0:.0f}s", flush=True)
k1, k2 = list(out)
d = 2 * math.pi * (out[k2]["rho"] - out[k1]["rho"])
for sec in ("up", "down", "lepton"):
    row = {}
    for c in out[k1]["sectors"][sec]:
        a, b = out[k1]["sectors"][sec][c], out[k2]["sectors"][sec][c]
        if a is None or b is None: continue
        row[c] = (round((b["ln R2"] - a["ln R2"]) / d, 3), round((b["ln R1"] - a["ln R1"]) / d, 3))
    print(sec, row, flush=True)
json.dump(out, open("pf_oos.json", "w"), indent=1, default=float)
print("seconds", round(time.time() - t0, 1))
