"""B1957, check 1: the web seat's W-A1, Part 3 (frame C at tau = i), row by row on main's frame code.  Data-free.
I1 mark against twin at i; I2, I3 no forced zero or one, no large hierarchy; I4 the equality is special to i (the axis
near i); the plant; H1, H3 S-tilde = S at i; H2 controls; H4 the end moved by -0.3 and +0.3; G1 the second crossing;
the printed outputs at (i, mark).  G2 (the reading S*) is not in main's code and is not checked here."""
import json, math, pathlib, sys
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "B1945_the_frames_cusp_exponents" / "verification"))
import determinant_law as DL, cusp_mixing as CM
mp = DL.mp; CR = DL.FM.CR
MARK, TWIN = (Fr(2, 5), Fr(4, 5)), (Fr(1, 5), Fr(2, 5))
qn = lambda M: np.array([[complex(M[i, j]) for j in range(M.cols)] for i in range(M.rows)])


def out(tx, ty, w, end=None):
    """ratios (s2/s1, s3/s1) for up and down in both readings, and |V| for the four reading pairs"""
    table = CR.canon
    if end is not None: CR.canon = lambda z, e=end: {"L_2": e}
    try:
        Yu = DL.parts(tx, ty, w[0], w[1], "up")[2]; Yd = DL.parts(tx, ty, w[0], w[1], "down")[2]
    finally:
        CR.canon = table
    r = {}
    for sec, Y in (("up", Yu), ("down", Yd)):
        for rd in ("S", "St"):
            s = sorted((abs(v) for v in mp.svd_c(Y[rd], compute_uv=False)), reverse=True); r[(sec, rd)] = (float(s[1] / s[0]), float(s[2] / s[0]))
    V = {}
    for ru in ("S", "St"):
        for rdn in ("S", "St"):
            Vm = CM.U_of(Yu[ru]).H * CM.U_of(Yd[rdn]); V[(ru, rdn)] = np.abs(qn(Vm))
    return r, V


def rdiff(a, b):
    return max(abs(a[k][i] / b[k][i] - 1) for k in a for i in (0, 1))


def vdiff(a, b, same_pair=True):
    return max(float(np.abs(a[k] - b[k]).max()) for k in a)


if __name__ == "__main__":
    R = {}
    rm, Vm = out("0", 1.0, MARK); rt, Vt = out("0", 1.0, TWIN)
    R["I1"] = (rdiff(rm, rt), vdiff(Vm, Vt)); print("I1: at tau = i, mark against twin: ratios differ by %.1e, |V| by %.1e" % R["I1"])
    allr = [x for k in rm for x in rm[k]]; R["I2"] = (min(allr), max(allr)); print("I2: every ratio at (i, mark) lies between %.6f and %.6f: none forced to 0 or 1" % R["I2"])
    s3 = [rm[k][1] for k in rm]; R["I3"] = min(s3); print("I3: the smallest sigma_3/sigma_1 is %.6f: above 1e-3, no large hierarchy" % R["I3"])
    s0 = math.atanh(-1 / math.sqrt(5)); ds = []
    for d in (-0.1, -0.05, 0.05, 0.1):
        s = s0 + d; x = 0.5 + (math.sqrt(5) / 2) * math.tanh(s); y = (math.sqrt(5) / 2) / math.cosh(s)
        a, _ = out(repr(x), y, MARK); b, _ = out(repr(x), y, TWIN); ds.append(rdiff(a, b))
    z0 = complex(0.5 + (math.sqrt(5) / 2) * math.tanh(s0), (math.sqrt(5) / 2) / math.cosh(s0))
    R["I4"] = (min(ds), max(ds)); print("I4: the axis point at s0 is %.12f + %.12fi; at arclength -0.1, -0.05, 0.05, 0.1 from it mark and twin differ by %s in the ratios" % (z0.real, z0.imag, ", ".join("%.3f" % d for d in ds)))
    rp, Vp = out("0", 1.0, (Fr(0), Fr(3, 5))); R["plant"] = (rdiff(rm, rp), vdiff(Vm, Vp)); print("plant: (i, mark) against (i, (0, 3/5)): ratios differ by %.2f, |V| by %.2f" % R["plant"])
    h1 = max(abs(rm[(sec, "S")][i] / rm[(sec, "St")][i] - 1) for sec in ("up", "down") for i in (0, 1)); h1v = max(float(np.abs(Vm[k] - Vm[("S", "S")]).max()) for k in Vm)
    R["H1"] = (h1, h1v); print("H1: at (i, mark) the reading S-tilde gives S's ratios to %.1e, and the four reading pairs the same |V| to %.1e" % R["H1"])
    h2 = []
    for tx, ty in (("0", 1.3), ("0.05", 0.9)):
        r, V = out(tx, ty, MARK); h2.append(max(abs(r[(sec, "S")][i] / r[(sec, "St")][i] - 1) for sec in ("up", "down") for i in (0, 1)))
    R["H2"] = h2; print("H2: controls at 1.3i and 0.05 + 0.9i: S-tilde against S differ by %.2f and %.2f in the ratios" % tuple(h2))
    PTS = [(Fr(i, 5), Fr(j, 5)) for i in range(5) for j in range(5) if (i, j) != (0, 0)]; h3 = 0.0
    for w in PTS:
        for sec in ("up", "down"):
            Ys = DL.parts("0", 1.0, w[0], w[1], sec)[2]; h3 = max(h3, float(max(abs(x) for x in (Ys["S"] - Ys["St"])) / max(abs(x) for x in Ys["S"])))
    R["H3"] = h3; print("H3: at tau = i the two readings' couplings agree at all 24 points, both sectors: %.1e" % h3)
    L = CR.canon(complex(0, 1))["L_2"]; h4 = []
    for dL in (-0.3, 0.3):
        r, V = out("0", 1.0, MARK, end=L + dL); h4.append((rdiff(r, rm), vdiff(V, Vm)))
    R["H4"] = (L, h4); print("H4: the end at i is %.4f; moved by -0.3 and +0.3 the ratios move by %.1f %% and %.1f %%, |V| by %.4f and %.4f" % (L, 100 * h4[0][0], 100 * h4[1][0], h4[0][1], h4[1][1]))
    rg, Vg = out("0", 1.0, (Fr(2, 5), Fr(1, 5))); R["G1"] = (rdiff(rg, rm), vdiff(Vg, Vm)); print("G1: (i, (2/5, 1/5)) against (i, mark): ratios %.1e, |V| %.1e" % R["G1"])
    print("outputs at (i, mark): up %.6f, %.7f; down %.6f, %.7f; |V| rows: %s" % (rm[("up", "S")][0], rm[("up", "S")][1], rm[("down", "S")][0], rm[("down", "S")][1], " | ".join(" ".join("%.4f" % x for x in row) for row in Vm[("S", "S")])))
    (HERE / "web_wa1_part3.json").write_text(json.dumps({k: (list(v) if isinstance(v, tuple) else v) for k, v in R.items()}, indent=1, default=str) + "\n")
