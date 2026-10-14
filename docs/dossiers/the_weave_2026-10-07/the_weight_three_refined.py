"""W78: main's B1637 ask. Every T (x) T structure with a sector at weight 3 (sixteen), searched over Im tau in [5, 10],
the region W54's box (Im tau <= 6) never reached, with W54's model, data, tolerance and residuals unchanged. The rule
(W78_RULE.md) was committed before this script.

  N0  the control: W54's ten shape observables for (5, 7, 3) unchanged under tau -> tau + 1 at three points far up
      the tau line, and under tau -> -1/tau at three points near the unit circle, to 1e-8 (the rule's corrected N0)
  N1  (5, 7, 3) fits by the grid route alone, at Im tau in [6.3, 7.3]
  N2  (5, 7, 3)'s minimum is at most 2.9 by the grid route alone
  N3  (3, 7, 7) does not fit in the window by the grid route alone
  N4  no structure with a quark sector at weight 3 fits in the window, other than (3, 7, 7) if N3 fails
  plus the read-outs: every structure's minimum, tau, P, pulls and grid best; window-edge flags; the refinements from
  main's tau (labelled: they use main's result)

Run: python3 the_weight_three_refined.py  ->  the_weight_three_refined.json beside it.
"""
import os

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools  # noqa: E402
import json  # noqa: E402
import sys  # noqa: E402
from multiprocessing import Pool  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
from scipy.optimize import least_squares  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_fit_at_the_geometrys_weight as FW  # noqa: E402  (W53: the data, reduce, the threshold)
import the_rank_thirteen_structures as RT  # noqa: E402  (W54: the model and residuals, unchanged)

OUT = HERE / "the_weight_three_refined.json"
FR = "T (x) T"
STRUCTS = [ks for ks in itertools.product((3, 5, 7), repeat=3) if 3 in ks and ks[:2] != (3, 3)]
QP = [(ku, kd) for ku in (3, 5, 7) for kd in (3, 5, 7) if (ku, kd) != (3, 3)]
EW = [3, 5, 7]
YLO, YHI = 5.0, 10.0
MAIN_TAU = {(5, 7, 3): complex(0.36, 6.79), (3, 7, 7): complex(-0.09, 6.63)}
NPROC = 4


def window():
    return [complex(float(x), float(y)) for y in np.geomspace(YLO, YHI, 16) for x in np.linspace(-0.5, 0.5, 11)]


WIN = window()


def stage1_point(g):
    tau = WIN[g]
    F = {k: RT.forms_at(FR, k, tau) for k in (3, 5, 7)}
    out = {"Q": [], "E": []}
    for qi, (ku, kd) in enumerate(QP):
        Fu, Fd = F[ku], F[kd]
        n = 2 * (Fu.shape[0] + Fd.shape[0])
        rng = np.random.default_rng([7800, qi, g])
        best = None
        for _ in range(16):
            r = least_squares(RT.q_res, rng.normal(size=n), args=(Fu, Fd), method="trf", xtol=1e-10, ftol=1e-10,
                              gtol=1e-10, max_nfev=400)
            c = float(np.sum(r.fun ** 2))
            if best is None or c < best[0]:
                best = (c, [float(v) for v in r.x])
        out["Q"].append(best)
    for ei, k in enumerate(EW):
        Fe = F[k]
        rng = np.random.default_rng([7800, 100 + ei, g])
        best = None
        for _ in range(8):
            r = least_squares(RT.e_res, rng.normal(size=2 * Fe.shape[0]), args=(Fe,), method="trf", xtol=1e-10,
                              ftol=1e-10, gtol=1e-10, max_nfev=400)
            c = float(np.sum(r.fun ** 2))
            if best is None or c < best[0]:
                best = (c, [float(v) for v in r.x])
        out["E"].append(best)
    return out


def grid_values(rows, ks):
    qi, ei = QP.index(ks[:2]), EW.index(ks[2])
    vals = []
    for g, row in enumerate(rows):
        (cq, pq), (ce, pe) = row["Q"][qi], row["E"][ei]
        vals.append((cq + ce, [WIN[g].real, WIN[g].imag] + pq + pe))
    vals.sort(key=lambda t: t[0])
    return vals


def refine(args):
    ks, starts = args
    n = len(starts[0])
    lb = [-0.5, YLO] + [-np.inf] * (n - 2)
    ub = [0.5, YHI] + [np.inf] * (n - 2)
    best = None
    for th in starts:
        x0 = np.array(th, dtype=float)
        x0[0] = min(max(x0[0], -0.5 + 1e-9), 0.5 - 1e-9)
        x0[1] = min(max(x0[1], YLO + 1e-9), YHI - 1e-9)
        r = least_squares(RT.full_res, x0, args=(FR, ks), bounds=(lb, ub), method="trf", xtol=1e-12, ftol=1e-12,
                          gtol=1e-12, max_nfev=1500)
        c = float(np.sum(r.fun ** 2))
        if best is None or c < best[0]:
            best = (c, [float(v) for v in r.x])
    return best


def describe(ks, best, grid_best):
    c, theta = best
    res = RT.full_res(np.array(theta), FR, ks)
    tau = FW.reduce(complex(theta[0], theta[1]))
    d, _ = RT.split(FR, ks)
    return {"weights (u, d, e)": list(ks), "P": 2 + sum(2 * x - 1 for x in d), "chi^2_min": float(np.sum(res ** 2)),
            "fits": bool(np.sum(res ** 2) <= FW.THRESH), "tau (raw)": [theta[0], theta[1]],
            "tau (reduced)": [tau.real, tau.imag],
            "on the window's edge": bool(abs(theta[1] - YLO) < 1e-6 or abs(theta[1] - YHI) < 1e-6
                                        or abs(abs(theta[0]) - 0.5) < 1e-6),
            "the grid's best": grid_best, "pulls": {lab: float(v) for lab, v in zip(FW.LABELS, res)}}


def control():
    rng = np.random.default_rng(7801)
    ks = (5, 7, 3)
    d, _ = RT.split(FR, ks)
    alphas = [rng.normal(size=2 * x) for x in d]
    def change(tau, t2):
        base = np.array(RT.shape10(tau, FR, ks, alphas))
        return float(np.max(np.abs(np.array(RT.shape10(t2, FR, ks, alphas)) - base)))
    far = max(change(t, t + 1) for t in (complex(0.2, 6.5), complex(-0.3, 8.0), complex(0.4, 9.5)))
    near_pts = [complex(rng.uniform(-0.25, 0.25), rng.uniform(1.0, 1.08)) for _ in range(3)]
    near = max(change(t, -1 / t) for t in near_pts)
    return {"T at the far points: largest change": far, "S near the unit circle: largest change": near,
            "holds": bool(far < 1e-8 and near < 1e-8)}


def main():
    out = {"status": "W78: every structure with a sector at weight 3, up to Im tau = 10 (the rule W78_RULE.md first;"
                     " one run)", "window": {"x": [-0.5, 0.5, 11], "y": [YLO, YHI, 16], "points": len(WIN)}}
    out["N0"] = control()
    with Pool(NPROC) as pool:
        rows = list(pool.imap(stage1_point, range(len(WIN))))
        jobs = [(ks, [th for _, th in grid_values(rows, ks)[:8]]) for ks in STRUCTS]
        bests = pool.map(refine, jobs)
    table = {}
    for ks, best in zip(STRUCTS, bests):
        gv = grid_values(rows, ks)
        if gv[0][0] < best[0]:                     # the grid's own point is better: keep it
            best = (gv[0][0], gv[0][1])
        table[str(ks)] = describe(ks, best, gv[0][0])
    out["the structures"] = table
    from_main = {}
    for ks, t0 in MAIN_TAU.items():
        gv = grid_values(rows, ks)
        g = min(range(len(WIN)), key=lambda i: abs(WIN[i] - t0))
        qi, ei = QP.index(ks[:2]), EW.index(ks[2])
        start = [t0.real, t0.imag] + rows[g]["Q"][qi][1] + rows[g]["E"][ei][1]
        from_main[str(ks)] = describe(ks, refine((ks, [start])), gv[0][0])
    out["read-out: refined from main's tau (uses main's result)"] = from_main
    t573, t377 = table["(5, 7, 3)"], table["(3, 7, 7)"]
    out["N1"] = {"chi^2_min": t573["chi^2_min"], "Im tau": t573["tau (reduced)"][1],
                 "holds": bool(t573["fits"] and 6.3 <= t573["tau (reduced)"][1] <= 7.3)}
    out["N2"] = {"chi^2_min": t573["chi^2_min"], "holds": bool(t573["chi^2_min"] <= 2.9)}
    out["N3"] = {"chi^2_min": t377["chi^2_min"], "holds": bool(not t377["fits"])}
    quark3 = {k: v for k, v in table.items() if 3 in v["weights (u, d, e)"][:2]}
    fitting = sorted(k for k, v in quark3.items() if v["fits"])
    allowed = [] if out["N3"]["holds"] else ["(3, 7, 7)"]
    out["N4"] = {"quark-at-3 structures that fit": fitting, "holds": bool(set(fitting) <= set(allowed))}
    out["cells"] = {k: out[k]["holds"] for k in ("N0", "N1", "N2", "N3", "N4")}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main()
