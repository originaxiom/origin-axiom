"""Frame C's cusp exponents, point by point (main, 2026-11-15; data-free, nothing is set beside a measured number).
At each of the 24 points of order 5, each sector and each Higgs reading, the ratios sigma2/sigma3 and sigma1/sigma3 are
computed with B1940's extended-precision frame at three heights of one column; the decay rate in |q| = exp(-2 pi y),
k = -d ln(ratio) / d(2 pi y), is printed with the nearest multiple of 1/200 (the characteristics are tenths, so the
theta exponents ||alpha||^2 / 2 are two-hundredths). The mixing moduli at the top height are printed too."""
import sys, json, math, pathlib
from fractions import Fraction as Fr
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1940_*")) / "verification"))
import frame_mp as FM
X = "0.13"; YS = [24, 32, 40]
ALL = list(FM.POINTS); out = {}
for p in ALL:
    FM.POINTS = [p]
    vals = {y: FM.fbar(X, y) for y in YS}
    rec = {}
    for k in FM.KEYS:
        if k.startswith("ckm"):
            rec[k] = [float(v) for v in vals[YS[-1]][k]]; continue
        ks = []
        for j in range(2):
            r = [float(FM.mp.log(vals[y][k][j])) for y in YS]
            ks.append([-(r[i + 1] - r[i]) / (2 * math.pi * (YS[i + 1] - YS[i])) for i in range(2)])
        rec[k] = ks
    out["%s,%s" % p] = rec
    line = "(%s, %s)" % p
    for k in FM.KEYS[:4]:
        line += "  %s: %s" % (k.replace("|L_2|", " "), " ".join("%.4f~%s" % (s[-1], Fr(round(s[-1] * 200), 200)) for s in rec[k]))
    print(line, flush=True)
FM.POINTS = ALL
json.dump(out, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
print("written", pathlib.Path(__file__).with_suffix(".json").name)
