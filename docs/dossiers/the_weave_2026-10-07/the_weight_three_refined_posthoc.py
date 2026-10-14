"""W78, POST HOC (labelled; written after W78's read-out). W78's grid route did not reach main's B1637 fits: (5, 7, 3)
at 190.7 against main's 1.86, (3, 7, 7) at 915.8 against 6.72. Both W78 and main's searches are local. This asks, at
main's own tau, whether this seat's model (W54's forms, data and residuals, unchanged) reaches main's numbers at all.
At a fixed tau the quark part and the lepton part separate, so each is fitted alone with many starts.

  PH1  (5, 7, 3) at tau = 0.36 + 6.79i: the quark pair (5, 7) and the leptons at weight 3, 200 starts each
  PH2  (3, 7, 7) at tau = -0.09 + 6.63i: the quark pair (3, 7) and the leptons at weight 7, 200 starts each
  PH3  each sector alone at weight 3 (main's F3: u at Im tau 6.66, d at 5.09, e at 5.85, each chi^2 ~ 0): the up, down
       and lepton masses alone at weight 3, with tau free in the window x in [-0.5, 0.5], y in [4, 8], 60 starts each

Run: python3 the_weight_three_refined_posthoc.py  ->  the_weight_three_refined_posthoc.json beside it.
"""
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_fit_at_the_geometrys_weight as FW  # noqa: E402
import the_rank_thirteen_structures as RT  # noqa: E402

OUT = HERE / "the_weight_three_refined_posthoc.json"
FR = "T (x) T"


def best_of(fun, n, args, starts, seed):
    rng = np.random.default_rng(seed)
    best = None
    for _ in range(starts):
        r = least_squares(fun, rng.normal(size=n), args=args, method="trf", xtol=1e-12, ftol=1e-12, gtol=1e-12,
                          max_nfev=2000)
        c = float(np.sum(r.fun ** 2))
        if best is None or c < best[0]:
            best = (c, r.fun)
    return best


def at_tau(tau, ku, kd, ke, seed):
    F = {k: RT.forms_at(FR, k, tau) for k in {ku, kd, ke}}
    q = best_of(RT.q_res, 2 * (F[ku].shape[0] + F[kd].shape[0]), (F[ku], F[kd]), 200, seed)
    e = best_of(RT.e_res, 2 * F[ke].shape[0], (F[ke],), 200, seed + 1)
    return {"tau": [tau.real, tau.imag], "quark part": q[0], "lepton part": e[0], "total": q[0] + e[0],
            "quark pulls": [float(v) for v in q[1]], "lepton pulls": [float(v) for v in e[1]]}


def sector_alone(s, seed):
    """the masses of one sector at weight 3, tau free in the window"""
    d = RT.DIMS[FR][3]
    def res(th):
        tau = FW.reduce(complex(th[0], th[1]))
        _, logs = RT.sector(RT.coupling(th[2:], RT.forms_at(FR, 3, tau)))
        return RT.mass_res(s, logs, FW.A_MAIN)
    rng = np.random.default_rng(seed)
    best = None
    for _ in range(60):
        x0 = np.concatenate([[rng.uniform(-0.5, 0.5), rng.uniform(4, 8)], rng.normal(size=2 * d)])
        r = least_squares(res, x0, bounds=([-0.5, 4] + [-np.inf] * 2 * d, [0.5, 8] + [np.inf] * 2 * d), method="trf",
                          xtol=1e-12, ftol=1e-12, gtol=1e-12, max_nfev=2000)
        c = float(np.sum(r.fun ** 2))
        if best is None or c < best[0]:
            best = (c, [float(r.x[0]), float(r.x[1])])
    return {"chi^2_min": best[0], "tau": best[1]}


def main():
    out = {"status": "W78 POST HOC (labelled): this seat's model at main's tau, and each sector alone at weight 3"}
    out["PH1 (5, 7, 3) at main's tau"] = at_tau(complex(0.36, 6.79), 5, 7, 3, 7810)
    out["PH2 (3, 7, 7) at main's tau"] = at_tau(complex(-0.09, 6.63), 3, 7, 7, 7820)
    out["PH3 each sector alone at weight 3"] = {s: sector_alone(s, 7830 + i) for i, s in enumerate(FW.SECTORS)}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main()
