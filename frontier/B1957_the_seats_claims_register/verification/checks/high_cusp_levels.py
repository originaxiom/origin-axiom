"""B1957: the cusp exponents of frame C at points of orders 5, 10 and 15, by main's own extended-precision frame (B1940's
frame_mp), against the exact exponents of B1788's tropical rule: the six cases agy-002's gate 2 quotes.  Data-free."""
import sys, math, pathlib
from fractions import Fraction as Fr
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1940_*")) / "verification")); import frame_mp as FM
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1788_*")) / "verification")); import tropical as T
P = T.polys("S"); X = "0.13"; YS = (24, 32, 40)
CASES = (("N5 down a = 2/5", (Fr(2, 5), Fr(1, 5)), "down"), ("N10 down a = 1/10", (Fr(1, 10), Fr(3, 10)), "down"), ("N10 lepton a = 1/10", (Fr(1, 10), Fr(3, 10)), "lep"),
         ("N15 down a = 2/15", (Fr(2, 15), Fr(4, 15)), "down"), ("N15 down a = 4/15", (Fr(4, 15), Fr(2, 15)), "down"), ("N15 lepton a = 4/15", (Fr(4, 15), Fr(2, 15)), "lep"))
SEC0 = dict(FM.B.SECTORS); worst = 0.0
for lab, p, sec in CASES:
    FM.POINTS = [p]; FM.B.SECTORS["down"] = SEC0[sec]                          # the frame's 'down' slot carries the sector asked for
    vals = {y: FM.fbar(X, y)["down|L_2|S"] for y in YS}; ql, qr = (FM.B.SIXY[c] for c in SEC0[sec])
    ex = T.predict(P, T.E(ql * p[0], qr * p[0])); got = []
    for j in range(2):
        r = [float(FM.mp.log(vals[y][j])) for y in YS]; s1, s2 = (-(r[i + 1] - r[i]) / (2 * math.pi * (YS[i + 1] - YS[i])) for i in range(2))
        L1, L2 = math.log(YS[1] / YS[0]), math.log(YS[2] / YS[1]); h = 2 * math.pi * (YS[1] - YS[0]); pw = (s1 - s2) * h / (L2 - L1); got.append(s1 + pw * L1 / h)
    worst = max(worst, max(abs(g - float(e)) for g, e in zip(got, ex)))
    print("%-20s exact (%s, %s); main's frame at heights 24, 32, 40: (%.6f, %.6f)" % (lab, ex[0], ex[1], got[0], got[1]), flush=True)
FM.B.SECTORS["down"] = SEC0["down"]
print("worst difference %.1e (the seat's bar 2e-3; its own worst 4.2e-5)" % worst)
