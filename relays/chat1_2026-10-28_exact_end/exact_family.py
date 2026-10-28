"""chat1, 2026-10-28: THE EXACT END, THE FAMILY. Post hoc and labelled: written after the look (exact_end_look.py, its
output committed unread at 4aa66ca45, then read). Data-free: no measured value is read; the frame is compared with itself.
Committed before its one run, with its expectations.

The question. The six's fits at "L_max" (B1726, B1741, B1749, B1786, the horocycle test) weight each channel by the small-cut
form 2 pi L + c_s at L = L_max. The look found that the exact norms at the maximal horoball itself do not give the six. Are the
fits' weights the exact norms of ANY embedded horoball? The exact norm N_s(L) of K_s = P_s / R_s over B1667's Dirichlet cell
minus its horoball at height L exists for L >= L_max (the maximal embedded one) and tends to 2 pi L + c_s as L grows.

Per row (the look's rows A, (2/5, 23/30), and B, (2/5, 1/10), at their full-precision tau):
  F1  an L-scan at the row's tau: L = L_max + (L_2 - L_max) k / 12 for k = 0..12, then L = 3.0 and 3.5. At each L, the six
      of the seat reading (up S~, down S, lepton S; m2/m3 and m1/m3 per sector) with the exact norms N_s(L), and with the
      small-cut weights 2 pi L + c_s, against the lever: the small-cut six at L_max as compute() gives it at the row.
      Read: D(L), the largest |d ln| over the six, and the rms d ln.
  F2  one Nelder-Mead over (Re tau', Im tau', t) with L = L_max(tau') + t (L_2(tau') - L_max(tau')), t in [0, 1], minimising
      the rms d ln of the exact six at (tau', L) against the row's lever: from the row's tau and F1's best t; box Re +- 0.2,
      Im +- 0.5; at most 40 evaluations; fatol 1e-3; initial steps 0.05, 0.05 and 0.08.
  C   the exact norms per sector at L_max (up and lepton against down): the largest relative difference.
Expectations, stated before the run:
  F1  the exact family's down and lepton m2/m3 stay below the lever's by 0.3 or more in ln at every L >= L_max, so the least
      D(L) is above 0.2 at both rows; the small-cut family's D(L) grows from 0 at L_max.
  F2  the least rms is above 0.1 at both rows (the measure's 10% floor): no embedded horoball near the rows gives the fits'
      weights.
  C   the exact norms do not depend on the sector, to 1e-8 (c_s does not, to 3e-11).
Run:  python3 -B exact_family.py <main_checkout>        (main at 680d29e1c or later)"""
import sys, json, math, pathlib, importlib.util, time
from fractions import Fraction as Fr
from multiprocessing import Pool
import numpy as np
ROOT = pathlib.Path(sys.argv[1]).resolve(); HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("ee", HERE / "exact_end.py")
ee = importlib.util.module_from_spec(_spec); sys.argv = [sys.argv[0], str(ROOT)]; _spec.loader.exec_module(ee)
C, B, K = ee.C, ee.B, ee.K
A25 = Fr(2, 5)
LOOK = json.loads((HERE / "exact_end_look.json").read_text())
ROWS = {o["row"]: (complex(*o["tau"]), Fr(o["line"][1])) for o in LOOK["rows"] if o["row"] in ("A", "B")}
SEAT = (("up", "St"), ("down", "S"), ("lep", "S"))
NM_MAXFEV, NM_FATOL, DRE, DIM = 40, 1e-3, 0.2, 0.5


def reduce(tau, b):
    while tau.real > 0.5: tau, b = tau - 1, (b + A25) % 1
    while tau.real < -0.5: tau, b = tau + 1, (b - A25) % 1
    return tau, b


def lever(tau, b):
    """the fits' lever: the small-cut six at L_max, as compute() gives it"""
    r = K.compute(tau.real, tau.imag, A25, b)
    return np.log(np.array([q for s, rd in SEAT for q in r["%s|L_max|%s" % (s, rd)]], dtype=float))


class Frame:
    """the frame at tau with B1667's geometry; the accessory parameter continued from the nearest solved tau"""
    def __init__(self):
        self.solved = []

    def c_at(self, tau):
        if not self.solved:
            t0 = complex(0.25, 3.0); c = C.track(t0); c, _ = C.solve_accessory(t0, c); self.solved.append((t0, c))
        t0, c0 = min(self.solved, key=lambda p: abs(p[0] - tau))
        c, _ = C.newton_walk(t0, c0, tau); self.solved.append((tau, c)); return c

    def setup(self, tau, b):
        tau, b = reduce(tau, b); G = ee.geometry(tau, self.c_at(tau)); rd = ee.higgs(tau)
        w = float(A25) * tau + float(b); sec = {}
        for s, (lf, rf) in K.SECT.items():
            x, yy = B.sector_twists(w, tau, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, tau); cs = B.cA(x, yy, tau, R)
            sec[s] = (x, yy, R, cs)
        return tau, G, rd, sec

    @staticmethod
    def six(tau, G, rd, sec, L, exact=True):
        out, norms = [], {}
        for s, rdn in SEAT:
            x, yy, R, cs = sec[s]
            if exact:
                N, mg = ee.twisted_norms(tau, G["al"], G["be"], L, x, yy, R)
            else:
                N = {u: (2 * math.pi * L + cs[u] if cs[u] is not None else None) for u in B.UNITS}
            norms[s] = N; out += ee.ratios(rd, R, N)[rdn]
        return np.log(np.array(out, dtype=float)), norms


def row_task(name):
    from scipy.optimize import minimize
    tau0, b = ROWS[name]; F = Frame(); t0 = time.time(); lv = lever(tau0, b)
    tau, G, rd, sec = F.setup(tau0, b)
    Ls = [G["L_max"] + (G["L_2"] - G["L_max"]) * k / 12 for k in range(13)] + [3.0, 3.5]
    scan = []
    for L in Ls:
        ex, nx = Frame.six(tau, G, rd, sec, L, True); sc, _ = Frame.six(tau, G, rd, sec, L, False)
        de, ds = ex - lv, sc - lv
        scan.append({"L": L, "t": (L - G["L_max"]) / (G["L_2"] - G["L_max"]),
                     "exact": {"D": float(np.max(np.abs(de))), "rms": float(np.sqrt(np.mean(de ** 2))), "dln": de.tolist()},
                     "small_cut": {"D": float(np.max(np.abs(ds))), "rms": float(np.sqrt(np.mean(ds ** 2))), "dln": ds.tolist()},
                     "exact_norms_down": nx["down"]})
    # C: the exact norms per sector at L_max
    _, nx = Frame.six(tau, G, rd, sec, G["L_max"], True)
    cdev = max(abs(nx[s][u] / nx["down"][u] - 1) for s in ("up", "lep") for u in B.UNITS
               if nx[s][u] is not None and nx["down"][u] is not None and nx["down"][u] != 0)
    best = min((e for e in scan if e["t"] <= 1 + 1e-12), key=lambda e: e["rms"])
    evals = []

    def f(p):
        re_, im_, t = float(p[0]), float(p[1]), float(p[2])
        tq, Gq, rdq, secq = F.setup(complex(re_, im_), b)
        L = Gq["L_max"] + min(max(t, 0.0), 1.0) * (Gq["L_2"] - Gq["L_max"])
        ex, _ = Frame.six(tq, Gq, rdq, secq, L, True); d = ex - lv
        v = float(np.sqrt(np.mean(d ** 2))); evals.append([re_, im_, t, L, v, float(np.max(np.abs(d)))]); return v
    x0 = np.array([tau0.real, tau0.imag, best["t"]])
    lo = [tau0.real - DRE, tau0.imag - DIM, 0.0]; hi = [tau0.real + DRE, tau0.imag + DIM, 1.0]
    x0 = np.minimum(np.maximum(x0, lo), hi)
    simplex = np.array([x0, x0 + [0.05, 0, 0], x0 + [0, 0.05, 0], x0 + [0, 0, 0.08 if x0[2] <= 0.92 else -0.08]])
    minimize(f, x0, method="Nelder-Mead", bounds=list(zip(lo, hi)),
             options={"maxfev": NM_MAXFEV, "fatol": NM_FATOL, "xatol": np.inf, "initial_simplex": simplex})
    bestF2 = min(evals, key=lambda e: e[4])
    return {"row": name, "line": ["2/5", str(b)], "tau": [tau0.real, tau0.imag], "L_max": G["L_max"], "L_2": G["L_2"],
            "lever_six_ln": lv.tolist(), "F1_scan": scan, "C_sector_rel_dev_at_L_max": cdev,
            "F2": {"best": {"re": bestF2[0], "im": bestF2[1], "t": bestF2[2], "L": bestF2[3], "rms": bestF2[4], "D": bestF2[5]},
                   "evaluations": evals}, "seconds": time.time() - t0}


def main():
    t0 = time.time()
    with Pool(2) as P:
        out = P.map(row_task, sorted(ROWS), chunksize=1)
    (HERE / "exact_family.json").write_text(json.dumps({"rows": out}, indent=1, default=str))
    names = ("up m2/m3", "up m1/m3", "down m2/m3", "down m1/m3", "lep m2/m3", "lep m1/m3")
    for o in out:
        print("row %s %s at %.4f%+.4fi: L_max %.4f, L_2 %.4f" % (o["row"], o["line"], o["tau"][0], o["tau"][1], o["L_max"], o["L_2"]))
        print("  F1   L       t      exact D  rms     | small-cut D  rms   | exact d ln per ratio (%s)" % ", ".join(names))
        for e in o["F1_scan"]:
            print("      %.4f %6.3f  %6.3f %6.3f   | %6.3f %6.3f    | %s" % (e["L"], e["t"], e["exact"]["D"], e["exact"]["rms"],
                  e["small_cut"]["D"], e["small_cut"]["rms"], " ".join("%+.3f" % q for q in e["exact"]["dln"])))
        m = min(o["F1_scan"], key=lambda e: e["exact"]["D"])
        print("  F1 least exact D over the scan: %.3f at L %.4f (t %.3f)" % (m["exact"]["D"], m["L"], m["t"]))
        b2 = o["F2"]["best"]
        print("  F2 least rms %.3f (D %.3f) at tau %.4f%+.4fi, L %.4f (t %.3f), %d evaluations" % (
            b2["rms"], b2["D"], b2["re"], b2["im"], b2["L"], b2["t"], len(o["F2"]["evaluations"])))
        print("  C  exact norms, up and lepton against down at L_max: largest relative difference %.2e" % o["C_sector_rel_dev_at_L_max"])
    print("exact_family exit 0 (%.0f s)" % (time.time() - t0))


if __name__ == "__main__":
    main()
