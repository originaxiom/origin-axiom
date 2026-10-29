"""The second isotropic branch of the 7/2 class at i (not in the draft's table): a(i) on Rbar(i)'s line, i.e.
2 f0(i) + (5/144) E4(i) f2(i) = 0 with f2(i) != 0.  Then g = f1^2 - 2 f0 f2 - (5/144) E4 f2^2 vanishes at i (to order 2),
so m2/m3 ~ |tau - i|^2 (L = inf), while a.R(i) = -(1/4) f2(i) eta6(i) != 0, so m1(i) != 0 (lift slope 0).
Example at 31/2: f2 = E4^3, f0 = -(5/288) E4^4 + E4 E6^2, f1 random in M14 = <E4^2 E6>.  Large-L (ref_near_i.slopes) and
finite L (ref_finite_L.point)."""
import json, pathlib
import mpmath as mp
from ref_near_i import make_section, slopes
from ref_finite_L import point
base = make_section(8, 1)
fs = lambda e4, e6: [-(mp.mpf(5) / 288) * e4 ** 4 + e4 * e6 ** 2, base(e4, e6)[1], e4 ** 3]
out = {"large-L (Y(a,R)) slopes": slopes(fs)}
I = mp.mpc(0, 1); EPS = [mp.mpf("0.01"), mp.mpf("0.001"), mp.mpf("0.0001")]; Ls = [0.65, 2.5, 40.0, 2560.0]
pts = [point(fs, I + e * mp.exp(0.3j), Ls) for e in EPS]
sl = lambda v: [round(float(mp.log10(v[k] / v[k + 1])), 3) for k in range(len(v) - 1)]
for L in Ls:
    out["L=%g" % L] = {"m1 slopes": sl([p[L]["m1/m3"] for p in pts]), "m2 slopes": sl([p[L]["m2/m3"] for p in pts]),
                       "m2/m3 at 1e-4": mp.nstr(pts[-1][L]["m2/m3"], 4), "m1/m3 at 1e-4": mp.nstr(pts[-1][L]["m1/m3"], 4)}
pathlib.Path(__file__).resolve().parent.joinpath("ref_rbar_branch.json").write_text(json.dumps(out, indent=1)); print(json.dumps(out, indent=1))
