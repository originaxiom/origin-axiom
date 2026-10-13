"""W54, POST HOC (written after W54's one run and its read-out; labelled; W54's JSON is unchanged). Two checks on the
two cells that failed as worded.

  P1  H3 failed only through (7, 7, 7), at chi^2_min = 6.38, just above 5.99, while (7, 7, 5) fits at 0.88 with the
      same quark pair, and the leptons at weight 7 reach their two ratios exactly on the grid. Is (7, 7, 7)'s value
      the search's? From (7, 7, 5)'s tau, refine the quark part Q_(7,7) over tau and alpha_u, alpha_d (48 starts, seed
      5410); at the tau found, fit the leptons at weights 5 and 7 (32 starts each). Then chi^2(7, 7, 7) <= Q + E_7.
  P2  H1 failed only at weight 5: the weight-5 span holds rank-one couplings at a generic tau, against the rule's count
      (5 conditions on 4). At H1's three tau: the rank-one couplings found from 40 starts (seed 5411), how many distinct
      ones (projectively), and which pieces they use (|alpha| on D, O+, O+, O-), with the same read at weight 7.

Run: python3 the_rank_thirteen_structures_posthoc.py  ->  the_rank_thirteen_structures_posthoc.json beside it.
"""
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_rank_thirteen_structures as RT  # noqa: E402  (W54: the model, the residuals, the rank-one test)

FW = RT.FW
OUT = HERE / "the_rank_thirteen_structures_posthoc.json"


def P1():
    w54 = json.loads((HERE / "the_rank_thirteen_structures.json").read_text(encoding="utf-8"))
    s = w54["the structures (global minimum found)"]
    tau0 = complex(*s["T (x) T: (7, 7, 5)"]["tau (reduced)"])
    d = RT.DIMS["T (x) T"][7]

    def q(th):
        tau = FW.reduce(complex(th[0], th[1]))
        F = RT.forms_at("T (x) T", 7, tau)
        return RT.q_res(np.asarray(th[2:]), F, F)

    rng = np.random.default_rng(5410)
    lb, ub = [-0.5, FW.H0] + [-np.inf] * (4 * d), [0.5, FW.YMAX] + [np.inf] * (4 * d)
    best = None
    for _ in range(48):
        x0 = np.array([tau0.real, tau0.imag] + list(rng.normal(size=4 * d)))
        x0[0] = min(max(x0[0], -0.5 + 1e-9), 0.5 - 1e-9)
        r = least_squares(q, x0, bounds=(lb, ub), method="trf", xtol=1e-12, ftol=1e-12, gtol=1e-12, max_nfev=1500)
        c = float(np.sum(r.fun ** 2))
        if best is None or c < best[0]:
            best = (c, r.x)
    tau = FW.reduce(complex(best[1][0], best[1][1]))
    e = {}
    for k in (5, 7):
        F = RT.forms_at("T (x) T", k, tau)
        r2 = np.random.default_rng([5410, k])
        e[k] = min(float(np.sum(least_squares(RT.e_res, r2.normal(size=2 * F.shape[0]), args=(F,), method="trf",
                                              xtol=1e-12, ftol=1e-12, gtol=1e-12, max_nfev=1500).fun ** 2))
                   for _ in range(32))
    return {"(7, 7, 5)'s tau": [tau0.real, tau0.imag], "the quark part Q_(7,7), refined": best[0],
            "at tau": [tau.real, tau.imag], "E_5 there": e[5], "E_7 there": e[7],
            "so chi^2(7, 7, 5) <=": best[0] + e[5], "so chi^2(7, 7, 7) <=": best[0] + e[7],
            "W54's recorded chi^2_min, (7, 7, 5) and (7, 7, 7)": [s["T (x) T: (7, 7, 5)"]["chi^2_min"],
                                                                   s["T (x) T: (7, 7, 7)"]["chi^2_min"]]}


def P2():
    w54 = json.loads((HERE / "the_rank_thirteen_structures.json").read_text(encoding="utf-8"))
    taus = [complex(*r["tau"]) for r in w54["H1: the span's closest approach to rank one"]["k = 5"]]
    out = {}
    for k in (5, 7):
        rows = []
        for i, tau in enumerate(taus):
            F = RT.forms_at("T (x) T", k, tau)
            rng = np.random.default_rng([5411, k, i])
            found = []
            for _ in range(40):
                q = least_squares(RT.minors, rng.normal(size=2 * F.shape[0]), args=(F,), method="trf", xtol=1e-15,
                                  ftol=1e-15, gtol=1e-15, max_nfev=2000)
                if np.linalg.norm(q.fun) > 1e-10:
                    continue
                a = q.x[:F.shape[0]] + 1j * q.x[F.shape[0]:]
                a = a / np.linalg.norm(a)
                a = a * np.exp(-1j * np.angle(a[np.argmax(np.abs(a))]))
                if all(min(np.linalg.norm(a - b), np.linalg.norm(a + b)) > 1e-6 for b in found):
                    found.append(a)
            pieces = [[round(float(x), 6) for x in np.abs(a)] for a in found]
            rows.append({"tau": [tau.real, tau.imag], "distinct rank-one couplings found (of 40 starts)": len(found),
                         "|alpha| on the basis (D, O+, O+, O-[, O-]) for each": pieces})
        out[f"k = {k}"] = rows
    return out


def main():
    p1 = P1()
    p2 = P2()
    out = {"status": "W54 post hoc: the two cells that failed as worded (labelled post hoc; W54's JSON unchanged)",
           "P1: (7, 7, 7) from (7, 7, 5)'s tau": p1, "P2: the rank-one couplings at weights 5 and 7": p2,
           "read-outs (post hoc, no prior)": {
               "P1: (7, 7, 7) fits (Q + E_7 <= 5.99)": bool(p1["so chi^2(7, 7, 7) <="] <= FW.THRESH),
               "P2: at weight 5 every one of H1's tau has a rank-one coupling": bool(
                   all(r["distinct rank-one couplings found (of 40 starts)"] > 0 for r in p2["k = 5"]))}}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["read-outs (post hoc, no prior)"], indent=1))
    print(json.dumps(p1, indent=1))


if __name__ == "__main__":
    main()
