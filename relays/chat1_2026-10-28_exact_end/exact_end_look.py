"""chat1, 2026-10-28: THE EXACT END, THE LOOK, the instrument for EXACT_END_LOOK_RULE.md (sealed at 5215f337a). It is
committed after the rule and before its one run.
Per row: E0 the control (small-cut, compute() as is), E2 the six with exact norms at the row, E1 one Nelder-Mead refit over
tau with exact norms, E3 the read-outs.
Run:  python3 -B exact_end_look.py <main_checkout>"""
import sys, json, math, pathlib, importlib.util, hashlib, time, os
from fractions import Fraction as Fr
from multiprocessing import Pool
import numpy as np
ROOT = pathlib.Path(sys.argv[1]).resolve(); HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("ee", HERE / "exact_end.py")
ee = importlib.util.module_from_spec(_spec); sys.argv = [sys.argv[0], str(ROOT)]; _spec.loader.exec_module(ee)
CMP = ROOT / "frontier" / "B1741_tau_from_the_thread_rule_the_line_free" / "verification" / "compare.py"
assert hashlib.sha256(CMP.read_bytes()).hexdigest() == "6308ed93e53ab99522cf654a85250f1299e9fa334ce13f92a74334cd7812f3bd"
_s2 = importlib.util.spec_from_file_location("b1741_compare", CMP); Cm = importlib.util.module_from_spec(_s2)
sys.modules["b1741_compare"] = Cm; _s2.loader.exec_module(Cm)
C, B, K = ee.C, ee.B, ee.K
A25 = Fr(2, 5)
ROW_LINES = {"A": Fr(23, 30), "B": Fr(1, 10), "C": Fr(23, 25), "D": Fr(11, 25)}


def horocycle_lines():
    """the horocycle test's 40 lines, in its order (horocycle.py's lines())"""
    out = [(A25, Fr(k, 10)) for k in range(10)]
    out += [(A25, Fr(k, 25)) for k in range(1, 25) if k % 5 != 0]
    out += [(A25, Fr(k, 30)) for k in range(1, 30) if math.gcd(k, 6) == 1]
    return out


def rows():
    """each row's tau and small-cut chi2_six at full precision, from the horocycle test's Nelder-Mead read-out (L_max)"""
    cells = json.loads((HERE.parent / "chat1_2026-10-28_horocycle" / "horocycle_cells.json").read_text())
    L = horocycle_lines(); out = {}
    for name, b in ROW_LINES.items():
        li = L.index((A25, b)); e = [r for r in cells["readout_nelder_mead"] if r["line"] == li and r["horocycle"] == "L_max"][0]
        out[name] = (complex(e["x"][0], e["x"][1]), b, float(e["chi2"]))
    return out


ROWS = rows()
NM_MAXFEV, NM_FATOL, NM_STEP, DRE, DIM = 40, 1e-3, 0.05, 0.2, 0.5


def targets():
    v = json.loads(Cm.DATA.read_text(encoding="utf-8"))["masses_GeV"]["value"]
    T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
    return T6, Cm.sigmas()[0]


def chi2_seat(rat, T, s):
    """B1741's seat measure (as in the horocycle test's chi2_seat), rat[sector][reading S=0, S~=1][m2/m3, m1/m3]"""
    best = float("inf"); lg = np.log(np.array(rat, dtype=float))
    for (a, b, l) in Cm.SEAT:
        U, Dn, E = lg[0, a], lg[1, b], lg[2, l]
        for k in (0.0, Cm.LC3):
            x = np.array([U[0], U[1], Dn[0], Dn[1], E[0] + k, E[1] - k])
            v = float(np.sum(((x - T) / s) ** 2))
            if np.isfinite(v) and v < best: best = v
    return best


def reduce(tau, b):
    while tau.real > 0.5: tau, b = tau - 1, (b + A25) % 1
    while tau.real < -0.5: tau, b = tau + 1, (b - A25) % 1
    return tau, b


class Exact:
    """the frame with exact norms at the maximal horoball; the accessory parameter continued from the nearest solved tau"""
    def __init__(self):
        self.solved = []                         # (tau, c)

    def c_at(self, tau):
        if not self.solved:
            c = C.track(complex(0.25, 3.0)); c, _ = C.solve_accessory(complex(0.25, 3.0), c); self.solved.append((complex(0.25, 3.0), c))
        t0, c0 = min(self.solved, key=lambda p: abs(p[0] - tau))
        c, _ = C.newton_walk(t0, c0, tau); self.solved.append((tau, c)); return c

    def ratios(self, tau, b):
        tau, b = reduce(tau, b); c = self.c_at(tau); G = ee.geometry(tau, c); rd = ee.higgs(tau)
        w = float(A25) * tau + float(b); out = []
        for sec, (lf, rf) in K.SECT.items():
            x, yy = B.sector_twists(w, tau, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, tau)
            N, mg = ee.twisted_norms(tau, G["al"], G["be"], G["L_max"], x, yy, R)
            r = ee.ratios(rd, R, N); out.append([r["S"], r["St"]])
        return out, G["L_max"]


def small_cut(tau, b):
    tau, b = reduce(tau, b); r = K.compute(tau.real, tau.imag, A25, b)
    return [[r["%s|L_max|S" % s], r["%s|L_max|St" % s]] for s in ("up", "down", "lep")]


def row_task(name):
    from scipy.optimize import minimize
    tau0, b, ref = ROWS[name]; T, s = targets(); X = Exact(); t0 = time.time(); evals = []
    ctl = chi2_seat(small_cut(tau0, b), T, s)
    rat0, L0 = X.ratios(tau0, b); at_row = chi2_seat(rat0, T, s)
    lo = [tau0.real - DRE, tau0.imag - DIM]; hi = [tau0.real + DRE, tau0.imag + DIM]

    def f(x):
        rat, L = X.ratios(complex(float(x[0]), float(x[1])), b); v = chi2_seat(rat, T, s)
        evals.append([float(x[0]), float(x[1]), v]); return v
    x0 = np.array([tau0.real, tau0.imag])
    res = minimize(f, x0, method="Nelder-Mead", bounds=list(zip(lo, hi)),
                   options={"maxfev": NM_MAXFEV, "fatol": NM_FATOL, "xatol": np.inf,
                            "initial_simplex": np.array([x0, x0 + [NM_STEP, 0], x0 + [0, NM_STEP]])})
    best = min(evals, key=lambda e: e[2]) if evals else [tau0.real, tau0.imag, at_row]
    if at_row < best[2]: best = [tau0.real, tau0.imag, at_row]
    ratb, _ = X.ratios(complex(best[0], best[1]), b)
    on_bound = any(abs(best[i] - lo[i]) < 1e-6 or abs(best[i] - hi[i]) < 1e-6 for i in range(2))
    return {"row": name, "line": ["2/5", str(b)], "tau": [tau0.real, tau0.imag], "reference_small_cut": ref,
            "E0_small_cut_chi2": ctl, "E2_exact_chi2_at_row": at_row, "L_max_exact_at_row": L0,
            "E1_refit": {"chi2": best[2], "tau": best[:2], "evaluations": len(evals), "on_a_box_bound": on_bound},
            "ratios_small_cut_at_row": small_cut(tau0, b), "ratios_exact_at_row": rat0, "ratios_exact_at_refit": ratb,
            "evals": evals, "seconds": time.time() - t0}


def main():
    t0 = time.time()
    with Pool(2) as P:
        out = P.map(row_task, list(ROWS), chunksize=1)
    T, s = targets()
    e0 = all(abs(o["E0_small_cut_chi2"] / o["reference_small_cut"] - 1) < 1e-6 for o in out)
    e1 = min(o["E1_refit"]["chi2"] for o in out) > 16.75
    e2 = all(o["E2_exact_chi2_at_row"] > 16.75 for o in out)
    res = {"rows": out, "cells": {"E0_control_to_1e-6": e0, "E1_least_refit_above_16.75": e1,
                                  "E2_every_row_above_16.75": e2}, "targets_ln": T.tolist(), "sigmas": s.tolist()}
    (HERE / "exact_end_look.json").write_text(json.dumps(res, indent=1, default=str))
    for o in out:
        print("row %s %s at %s: E0 small-cut chi2 %.4f (table %.3f) | E2 exact at row %.3f (L_max %.4f) | E1 refit %.3f at %s (%d evaluations%s)" % (
            o["row"], o["line"], o["tau"], o["E0_small_cut_chi2"], o["reference_small_cut"], o["E2_exact_chi2_at_row"], o["L_max_exact_at_row"],
            o["E1_refit"]["chi2"], ["%.4f" % q for q in o["E1_refit"]["tau"]], o["E1_refit"]["evaluations"], ", ON A BOX BOUND" if o["E1_refit"]["on_a_box_bound"] else ""))
        names = ("m_c/m_t", "m_u/m_t", "m_s/m_b", "m_d/m_b", "m_mu/m_tau", "m_e/m_tau")
        for tag in ("ratios_small_cut_at_row", "ratios_exact_at_row", "ratios_exact_at_refit"):
            r = o[tag]; print("    %-24s up S~ %s | down S %s, S~ %s | lep S %s, S~ %s" % (tag, ["%.3g" % q for q in r[0][1]], ["%.3g" % q for q in r[1][0]],
                  ["%.3g" % q for q in r[1][1]], ["%.3g" % q for q in r[2][0]], ["%.3g" % q for q in r[2][1]]))
    print("cells: E0 %s | E1 (decisive) %s | E2 %s" % ("HOLDS" if e0 else "FAILS", "HOLDS" if e1 else "FAILS", "HOLDS" if e2 else "FAILS"))
    print("exact_end_look exit 0 (%.0f s)" % (time.time() - t0))


if __name__ == "__main__":
    main()
