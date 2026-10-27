"""Main's independent check of the SM seat's W160 (data-free), on main's own instrument (b1656_funcs' contour residues):
 (a) the zero law: R_i^up = 0 exactly iff 5w = 1/2 or 3w = 1/2 (mod Z + Z tau), and R_i^down = 0 iff 3w = 1/2 or w = 1/2,
     over B1785's 662 lines at tau = 0.3145 + 3.0345i (W160's probe);
 (b) the identity I = |R_j^2 + R_k^2| / (|R_j|^2 + |R_k|^2) = 2 eps / (1 + eps^2) with eps = |r11 / r00| (algebraic, from
     R_j = -(r00 + r11), R_k = i (r00 - r11)), on every line;
 (c) W160's exponent law on the ten lines (1/5, odd/10), (2/5, odd/10): eps = exp(-pi (1 - 2||3a||) Im tau) up to O(e^{-pi Im tau}),
     at the probe, 0.85 + 3.45i and 0.5 + 6i -- and main's general form: eps's exponent |E00 - E11| = | ||q_L a|| + ||q_R a|| - 1/2 |."""
import math, json, pathlib
from fractions import Fraction as Fr
import numpy as np
import blocks as K
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
B = K.B
HERE = pathlib.Path(__file__).resolve().parent


def nd(x): x = x % 1; return min(x, 1 - x)


def half_torsion(k, a, b):        # k w = 1/2 mod Z + Z tau  <=>  k a in Z and k b = 1/2 mod 1
    return (k * a).denominator == 1 and ((k * b) - Fr(1, 2)).denominator == 1


def R_of(a, b, sec, t):
    lf, rf = B.SECTORS[sec]; w = float(a) * t + float(b)
    x, y = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); return B.residues(x, y, t)


if __name__ == "__main__":
    lines = [(Fr(r["alpha"]), Fr(r["b"])) for r in json.load(open(ROOT / "frontier/B1785_the_slope_sets_the_exponents/verification/exponents.json"))]
    probe = complex(0.3145, 3.0345); out = {}
    # (a) the zero law
    mism = {"up": 0, "down": 0}; zeros = {"up": [], "down": []}; minnz = {"up": 1.0, "down": 1.0}
    rule = {"up": (5, 3), "down": (3, 1)}
    for a, b in lines:
        for sec in ("up", "down"):
            R = R_of(a, b, sec, probe); nrm = math.sqrt(sum(abs(R[s]) ** 2 for s in R)); z = abs(R["i"]) / nrm
            pred = any(half_torsion(k, a, b) for k in rule[sec]); isz = z < 1e-12
            if isz: zeros[sec].append((str(a), str(b)))
            else: minnz[sec] = min(minnz[sec], z)
            mism[sec] += (pred != isz)
    out["zero_law"] = {"mismatches": mism, "zero_lines": zeros, "smallest_nonzero_relative": minnz}
    print("(a) zero law mismatches:", mism, " zeros up:", len(zeros["up"]), "down:", len(zeros["down"]), " smallest nonzero |R_i|/|R|:", minnz)
    print("    up zero lines:", zeros["up"])
    # (b) the identity, every line, every sector, at the probe
    worst = 0.0
    for a, b in lines:
        for sec in ("up", "down", "lep"):
            lf, rf = B.SECTORS[sec]; bl, _ = K.blocks(a, b, B.SIXY[lf], B.SIXY[rf], probe)
            t = probe; h = 1e-6; th1pt = complex((B.th1(t + h, t) - B.th1(t - h, t)) / (2 * h))
            (ax, bx), (ay, by) = B.sector_twists(float(a) * t + float(b), t, B.SIXY[lf], B.SIXY[rf])
            r11 = np.exp(1j * np.pi * (bx + by)) * bl["X1"] * bl["Y1"] / th1pt; r00 = bl["r00"]
            R = R_of(a, b, sec, probe)
            I = abs(R["j"] ** 2 + R["k"] ** 2) / (abs(R["j"]) ** 2 + abs(R["k"]) ** 2)
            pr = abs(r00 * r11); e2 = 2 * pr / (abs(r00) ** 2 + abs(r11) ** 2); worst = max(worst, abs(I - e2))
    out["identity_worst_rel"] = worst; print("(b) I = 2 eps/(1+eps^2), eps = |r11/r00| (= 2|r00 r11|/(|r00|^2+|r11|^2)): worst ABSOLUTE deviation over 662 x 3:", "%.1e" % worst)
    # (c) the exponent law on the ten lines
    ten = [(a, b) for a, b in lines if a in (Fr(1, 5), Fr(2, 5)) and (2 * b * 5).denominator == 1 and (10 * b) % 2 == 1]
    rows = []
    for t in (probe, complex(0.85, 3.45), complex(0.5, 6.0)):
        for a, b in ten:
            R = R_of(a, b, "up", t); I = abs(R["j"] ** 2 + R["k"] ** 2) / (abs(R["j"]) ** 2 + abs(R["k"]) ** 2)
            eps = math.exp(-math.pi * (1 - 2 * float(nd(3 * a))) * t.imag); pred = 2 * eps / (1 + eps * eps)
            rows.append((str(t), str(a), str(b), I, pred, abs(I / pred - 1)))
    out["ten_lines"] = rows
    print("(c) ten lines:", len(ten), "; worst |I/pred - 1| at Im tau 3.03, 3.45, 6:", ["%.3f" % max(r[5] for r in rows if r[0] == str(t)) for t in (probe, complex(0.85, 3.45), complex(0.5, 6.0))])
    print("    2/5 lines I at the probe:", sorted(set("%.5f" % r[3] for r in rows if r[0] == str(probe) and r[1] == "2/5")), " 1/5:", sorted(set("%.4f" % r[3] for r in rows if r[0] == str(probe) and r[1] == "1/5")))
    # main's general form: E00 - E11 = ||ax|| + ||ay|| - 1/2 on every line; equals -(1/2 - ||3a||) for up when 5a in Z
    ok = all(abs(nd(a) + nd(-4 * a) - Fr(1, 2)) == Fr(1, 2) - nd(3 * a) for a in (Fr(k, 5) for k in range(5)))
    out["general_form_reduces_to_W160_on_5a_in_Z"] = ok; print("(c') |E00 - E11| = 1/2 - ||3a|| for up on every a with 5a in Z:", ok)
    json.dump(out, open(HERE / "w160_check.json", "w"), indent=1, default=str)
    print("w160_check exit 0")
