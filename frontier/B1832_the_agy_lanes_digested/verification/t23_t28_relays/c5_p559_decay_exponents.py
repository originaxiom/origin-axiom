"""c5: P-559 -- the agy lane's replacement of B1788's hypothesis (a) (FULL_AUDIT relay s2.4; ELEVATION s4;
twisted_norms.channel_pair_decay_exponents), measured with MAIN's channel norms (b1656_funcs.cA via cm_zero_line):

  |c_1 - c_i| ~ exp(-4 pi E1 Im tau),  E1 = ||3 alpha|| / 2
  |c_j - c_k| ~ exp(-4 pi E2 Im tau),  E2 = 1/4 - ||3 alpha|| / 2
and the lane's own referee's exceptions (HOSTILE 3.4): c_1 - c_i == 0 identically for alpha = 1/3, b = 1/12; on Re tau = 1/2,
alpha = 2/5, b = -1/20; and at Re tau = 0.35, alpha = 2/5, b = -3/50 the exponent of c_1 - c_i jumps from 0.10 to 0.40.

Method: down sector (1, 2) (c_s is sector-blind, B1826); kappa = -slope of ln|Delta| against Im tau by least squares over
Im tau in {2.0, 2.5, 3.0, 3.5} at a generic Re tau; E_meas = kappa / (4 pi) (the lane's convention; kappa / (2 pi) printed too)."""
import math, pathlib, sys
from fractions import Fraction as F
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
import cm_zero_line as Z
B = Z.mods()["B"]
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

def cs(alpha, b, tau):
    w = B.line_w(alpha, b, tau); x, yy = B.sector_twists(w, tau, 1, 2)
    R = B.residues(x, yy, tau); return B.cA(x, yy, tau, R)

def dist(v): v = v % 1; return min(v, 1 - v)
ys = [2.0, 2.5, 3.0, 3.5]
def fit(vals):
    pts = [(y, math.log(abs(v))) for y, v in zip(ys, vals) if v is not None and abs(v) > 1e-300]
    if len(pts) < 3: return None
    Y = np.array([p[0] for p in pts]); Lg = np.array([p[1] for p in pts])
    k = -np.polyfit(Y, Lg, 1)[0]; return k

say("%-14s %-6s %8s %8s %8s | %8s %8s %8s | %s" % ("line", "Re t", "E1 pred", "E1 meas", "(k/2pi)", "E2 pred", "E2 meas", "(k/2pi)", "max |Delta| at Im 2"))
lines = [(F(2, 5), F(1, 10)), (F(2, 5), F(0)), (F(2, 5), F(3, 10)), (F(1, 7), F(3, 7)), (F(1, 7), F(0)), (F(4, 9), F(2, 9)),
         (F(1, 5), F(1, 10)), (F(2, 7), F(1, 7)), (F(3, 11), F(5, 11)), (F(1, 8), F(3, 8)), (F(1, 3), F(1, 7))]
for (al, b) in lines:
    for rx in (0.17, 0.41):
        d1, d2 = [], []
        for y in ys:
            c = cs(al, b, complex(rx, y))
            d1.append(None if None in (c["1"], c["i"]) else c["1"] - c["i"])
            d2.append(None if None in (c["j"], c["k"]) else c["j"] - c["k"])
        k1, k2 = fit(d1), fit(d2)
        e = dist(3 * al)
        say("%-14s %-6s %8.4f %8s %8s | %8.4f %8s %8s | %s" % (
            "(%s,%s)" % (al, b), rx, e / 2, "-" if k1 is None else "%.4f" % (k1 / (4 * math.pi)), "-" if k1 is None else "%.4f" % (k1 / (2 * math.pi)),
            0.25 - e / 2, "-" if k2 is None else "%.4f" % (k2 / (4 * math.pi)), "-" if k2 is None else "%.4f" % (k2 / (2 * math.pi)),
            ["%.1e" % abs(v) if v is not None else None for v in (d1[0], d2[0])]))

say("the lane's referee's exceptions (c_1 - c_i):")
for (al, b, rx, note) in ((F(1, 3), F(1, 12), 0.23, "alpha 1/3, b 1/12: claimed == 0 for all tau"),
                          (F(1, 3), F(1, 12), 0.71, "same, another Re tau"),
                          (F(2, 5), F(-1, 20), 0.5, "alpha 2/5, b -1/20, Re tau 1/2: claimed == 0"),
                          (F(2, 5), F(-3, 50), 0.35, "alpha 2/5, b -3/50, Re tau 0.35: claimed E 0.40 not 0.10"),
                          (F(2, 5), F(-3, 50), 0.20, "same line, Re tau 0.20 (control)")):
    d1 = []
    for y in ys:
        c = cs(al, b, complex(rx, y)); d1.append(None if None in (c["1"], c["i"]) else c["1"] - c["i"])
    k1 = fit(d1)
    say("  %-56s |c1-ci| at Im 2..3.5 = %s ; E_meas = %s" % (note, ["%.2e" % abs(v) if v is not None else None for v in d1],
                                                           "-" if k1 is None or max(abs(v) for v in d1 if v is not None) < 1e-9 else "%.4f" % (k1 / (4 * math.pi))))
pathlib.Path(__file__).with_name("c5_p559_decay_exponents_out.txt").write_text("\n".join(out) + "\n")
