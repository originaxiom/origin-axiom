"""Extra checks.
 (a) the 3/2 class with f2 = 0 (dR) at finite L: m1/m3 / |tau - i| scales like 1/L^2 (B1691's S164 correction's law, at i);
 (b) 7/2 class with nu_i(f2) = 4 (55/2, f2 = E6^4): large-L exponent 4 (the draft's nu), finite-L exponent?;
 (c) the parity flip when a(i) = 0: 27/2 with f1 = E6^2 (then E6 divides a: a = E6 b, b of weight 15/2), large-L lift
     exponent and m2/m3 at i; and 31/2 with f0 = E4 E6^2, f2 = E6^2 (a = E6 b, b of weight 19/2).
    python3 ref_extra.py -> ref_extra.json
"""
import json, pathlib
import mpmath as mp
from ref_near_i import make_section, mono, slopes
from ref_finite_L import point

HERE = pathlib.Path(__file__).resolve().parent
I = mp.mpc(0, 1); out = {}
# (a)
fs = make_section(1, 1)
rows = {}
for L in (2.5, 10.0, 40.0, 160.0, 640.0):
    p = point(fs, I + mp.mpf("0.001") * mp.exp(0.3j), [L])
    rows[str(L)] = {"m1/m3": mp.nstr(p[L]["m1/m3"], 6), "L^2 m1/m3 / eps": mp.nstr(p[L]["m1/m3"] * L ** 2 / mp.mpf("0.001"), 6)}
out["(a) dR at eps=1e-3: m1/m3 vs L"] = rows
# (b)
fs = make_section(14, 1, mono(0, 4))
EPS = [mp.mpf("0.01"), mp.mpf("0.001"), mp.mpf("0.0001")]
Ls = [0.65, 2.5, 40.0, 2560.0]
pts = [point(fs, I + e * mp.exp(0.3j), Ls) for e in EPS]
sl = lambda v: [round(float(mp.log10(v[k] / v[k + 1])), 3) for k in range(len(v) - 1)]
out["(b) 55/2 f2 = E6^4"] = {"large-L L*m1/m3 slopes": sl([p["L*m1/m3 large-L formula"] for p in pts]),
                             "L=inf m2/m3 slopes": sl([p["m2/m3 at L=inf"] for p in pts])}
for L in Ls:
    out["(b) 55/2 f2 = E6^4"]["L=%g m1 slopes" % L] = sl([p[L]["m1/m3"] for p in pts])
    out["(b) 55/2 f2 = E6^4"]["L=%g m2 slopes" % L] = sl([p[L]["m2/m3"] for p in pts])
# (c)
out["(c) 27/2 f1 = E6^2 (a(i) = 0; a = E6 * b, b in weight 15/2)"] = slopes(make_section(7, 1, None, None) if False else
    (lambda base: (lambda e4, e6: [base(e4, e6)[0], e6 ** 2, base(e4, e6)[2]]))(make_section(7, 1)))
out["(c') 31/2 f0 = E4 E6^2, f2 = E6^2 (a(i) = 0; a = E6 * b, b in weight 19/2)"] = slopes(make_section(8, 1, mono(0, 2), mono(1, 2)))
(HERE / "ref_extra.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
