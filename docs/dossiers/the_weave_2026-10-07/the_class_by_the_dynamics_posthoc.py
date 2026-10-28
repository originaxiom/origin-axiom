#!/usr/bin/env python3
"""W176, a labelled post hoc read-out (written after W176's output was read; not a cell). W176's K3 failed as computed:
at N = 2, 3, 5, 9, 12 and 25 the least tested "not CP-fixed". Every order's least sits on the line (0, 1/N) at the
domain's top edge Im tau = 4, at Re tau within 1e-5 of 0 or 1/2 except at N = 3 (0.400002), and each order's five
refined candidates agree in V to the fifth decimal across Re tau. This reads, with no cell and no target:

  P1  the X-profile of each order's least line at Im tau = 4 (201 points, Re tau in [-1/2, 1/2]): its amplitude, its
      evenness, its argmin, and the exact CP test at the least as stored (at the script's 1e-5 and the rule's 1e-6)
      and at the profile's argmin
  P2  the height: V on each least line at the profile's argmin for Im tau = 2, 3, 4, 6, 8, 16 (above 4 outside the
      rule's domain), V / (Im tau)^3, dV/dy at 4; the cusp coefficient A(psi1) (the kernel's n = 0 terms over y^s,
      summed over the content) on every line of each order, against the hand formula A(0) = (15/8) zeta(6) Sum_q w_q
  P3  the second-least distinct configuration at the top edge: per order, every line's least over W176's 21-point row
      at Im tau = 4; the least, the second, the gap, and the least line with a != 0
  P4  J off the mirror on a = 0 lines: own_point at (0, 1/3) and (0, 1/5), Re tau 0.1, 0.25, 0.4, Im tau 2 and 4

Disclosed: before this script was committed, a timing call evaluated V on (0, 1/3) at tau = 4i and 8i (-5003.50, as
stored, and -40042.17).

    python3 -B docs/dossiers/the_weave_2026-10-07/the_class_by_the_dynamics_posthoc.py
"""
import contextlib
import io
import json
import math
import sys
import time
import traceback
import warnings
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_class_by_the_dynamics as D76     # noqa: E402  (W176: the lines, the potential, the exact CP test)
W72, W66, T8 = D76.W72, D76.W66, D76.T8
OUT = HERE / "the_class_by_the_dynamics_posthoc.json"
SRC = HERE / "the_class_by_the_dynamics.json"
XS201 = [-0.5 + k / 200 for k in range(201)]
HEIGHTS = (2.0, 3.0, 4.0, 6.0, 8.0, 16.0)


def cp_at(tau, psi, tol):
    old = D76.LOCUS_TOL
    D76.LOCUS_TOL = tol
    try:
        return D76.cp_fixed(tau, psi)[0]
    finally:
        D76.LOCUS_TOL = old


def least_line(row):
    return (Fr(row["least"]["line"][0]), Fr(row["least"]["line"][1]))


def p1(per, wv):
    out = {}
    for N, row in per.items():
        psi = D76.psi_of(least_line(row))
        x0, y0 = row["least"]["tau"]
        prof = [D76.V_one(complex(x, 4.0), psi, wv) for x in XS201]
        xm = XS201[int(np.argmin(prof))]
        out[N] = {"line": row["least"]["line"], "least as stored": [x0, y0],
                  "distance of Re tau from the nearest of 0, +-1/2": min(abs(x0), abs(abs(x0) - 0.5)),
                  "CP-fixed as stored, tol 1e-5 (the script's)": cp_at(complex(x0, y0), psi, 1e-5),
                  "CP-fixed as stored, tol 1e-6 (the rule's)": cp_at(complex(x0, y0), psi, 1e-6),
                  "profile amplitude (max - min)": max(prof) - min(prof),
                  "profile amplitude over |V|": (max(prof) - min(prof)) / abs(min(prof)),
                  "profile evenness, worst |V(x) - V(-x)|": max(abs(prof[i] - prof[200 - i]) for i in range(201)),
                  "V(0) - V(1/2)": prof[100] - prof[0],
                  "profile argmin Re tau": xm,
                  "CP-fixed at the argmin (exact)": cp_at(complex(xm, 4.0), psi, 1e-12)}
    return out


def cusp_coefficient(psi1, wv):
    """A(psi1): the n = 0 terms of the content's kernel over y^s, so V -> A(psi1) y^s at the cusp"""
    K = W72.KernelS(complex(0.0, 1.0), D76.S)
    sel = K.n == 0
    return float(sum(wv[qi] * -(K.cw[sel] @ np.cos(2 * np.pi * K.m[sel] * q * psi1))
                     for qi, q in enumerate(W72.QS) if wv[qi] != 0))


def p2(per, prof, wv):
    out = {"Sum_q w_q": float(np.sum(wv)),
           "hand formula (15/8) zeta(6) Sum_q w_q": 15 / 8 * math.pi ** 6 / 945 * float(np.sum(wv)),
           "A(0) computed": cusp_coefficient(0.0, wv), "per order": {}}
    for N, row in per.items():
        psi = D76.psi_of(least_line(row))
        xm = prof[N]["profile argmin Re tau"]
        vals = {str(y): D76.V_one(complex(xm, y), psi, wv) for y in HEIGHTS}
        h = 1e-3
        dvdy = (D76.V_one(complex(xm, 4.0 + h), psi, wv) - D76.V_one(complex(xm, 4.0 - h), psi, wv)) / (2 * h)
        lines = D76.lines_of_order(int(N))
        A = sorted((cusp_coefficient(float(-ln[0]), wv), [str(v) for v in ln]) for ln in lines)
        out["per order"][N] = {"V on the least line at its argmin": vals,
                               "V / y^3": {str(y): vals[str(y)] / y ** 3 for y in HEIGHTS},
                               "dV/dy at Im tau 4": dvdy,
                               "A on the least line": cusp_coefficient(float(-least_line(row)[0]), wv),
                               "A least over the order's lines": A[0][0],
                               "lines attaining the least A": [ln for a, ln in A if abs(a - A[0][0]) < 1e-9],
                               "lines with A < 0 (run to the cusp)": sum(1 for a, _ in A if a < 0),
                               "lines with A > 0 (pushed from the cusp)": sum(1 for a, _ in A if a > 0),
                               "lines": len(A)}
    return out


def p3(wv):
    out = {}
    for N in D76.ORDERS:
        best = []
        for ln in D76.lines_of_order(N):
            psi = D76.psi_of(ln)
            vs = [D76.V_one(complex(x, 4.0), psi, wv) for x in D76.XS]
            j = int(np.argmin(vs))
            best.append((vs[j], [str(v) for v in ln], D76.XS[j]))
        best.sort(key=lambda b: b[0])
        a_nonzero = [b for b in best if b[1][0] != "0"]
        out[str(N)] = {"least": best[0], "second": best[1] if len(best) > 1 else None,
                       "gap": best[1][0] - best[0][0] if len(best) > 1 else None,
                       "least with a != 0": a_nonzero[0] if a_nonzero else None,
                       "a = 0 lines": sum(1 for b in best if b[1][0] == "0")}
    return out


def p4(root):
    with contextlib.redirect_stdout(io.StringIO()):
        col, _sha, W93, W89, _L = W66.frame(root)
    out = {}
    for line in ((Fr(0), Fr(1, 3)), (Fr(0), Fr(1, 5))):
        for y in (2.0, 4.0):
            for x in (0.1, 0.25, 0.4):
                o, _d = T8.own_point(W93, W89, col, line, x, y)
                out[f"({line[0]}, {line[1]}) at {x} + {y}i"] = float(o[D76.KEY][3])
    return out


def main():
    root = T8.repo_root()
    D76._ROOT["<repo>"] = str(root)
    D76._ROOT["<home>"] = str(Path.home())
    out = {"arc": "W176 post hoc", "status": "post hoc, labelled", "head": T8.resolve(root, "HEAD")}
    t0 = time.time()
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            per = json.loads(SRC.read_text(encoding="utf-8"))["per order"]
            wv = W72.weights(1.0)
            out["P1"] = p1(per, wv)
            out["P2"] = p2(per, out["P1"], wv)
            out["P3"] = p3(wv)
            out["P4"] = p4(root)
        except Exception:  # noqa: BLE001
            out["run_failed"] = D76.sanitize(traceback.format_exc()[-3000:])
    out["warnings"] = sorted({D76.sanitize(f"{w.category.__name__}: {w.message}") for w in caught})
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print("done" if "run_failed" not in out else "run failed")


if __name__ == "__main__":
    main()
