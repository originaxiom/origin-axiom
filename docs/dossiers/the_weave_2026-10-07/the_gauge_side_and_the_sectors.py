"""W55 (the rule: W55_RULE.md, committed before this script). Does the gauge side on record tell the sectors apart?

  K1  the tie's bound: the minimum over two shared log ratios and the two scales of the chi^2 of the six down and lepton
      log masses with equal in-sector ratios (W53's data and tolerance), at a = 0.05, 0.10, 0.20; exact (linear least
      squares). Predicted: at least 50 at a = 0.10.
  K2  the Kronecker lemma: for 200 random complex symmetric lambda and random complex (v_d, n, s), the singular values
      of P (x) lambda and P^T (x) lambda (P = [[v_d, 0], [n, s]]) are the products sigma_a(P) sigma_i(lambda), to
      1e-10.
  K3  the Standard Model frame's tie k_d = k_e, read from W54's JSON and its post hoc: the fitting structures with it
      are exactly (5, 5, 5), (5, 7, 7), (7, 7, 7), each with P >= 23.
  K4  the allowance a* at which the tie's bound falls to 5.99 is above 0.25.

Run: python3 the_gauge_side_and_the_sectors.py  ->  the_gauge_side_and_the_sectors.json beside it.
"""
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_fit_at_the_geometrys_weight as FW  # noqa: E402  (W53: the data and the tolerance)

OUT = HERE / "the_gauge_side_and_the_sectors.json"


def tie_bound(a):
    """min over (rho1, rho2, c_d, c_e) of the chi^2 of the d and e log masses with in-sector ratios (rho1, rho2, 0)"""
    rows, rhs = [], []
    for si, s in enumerate(("d", "e")):
        sig = np.sqrt(FW.DELM[s] ** 2 + a ** 2)
        for i in range(3):
            r = np.zeros(4)
            if i < 2:
                r[i] = 1.0                       # rho_1 or rho_2
            r[2 + si] = 1.0                      # this sector's scale
            rows.append(r / sig[i])
            rhs.append(FW.LOGM[s][i] / sig[i])
    A, b = np.array(rows), np.array(rhs)
    x, *_ = np.linalg.lstsq(A, b, rcond=None)
    res = A @ x - b
    return float(res @ res), x


def a_star(target=FW.THRESH):
    lo, hi = 0.0, 3.0
    if tie_bound(hi)[0] > target:
        return None
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if tie_bound(mid)[0] > target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def K2(n=200, seed=5500):
    rng = np.random.default_rng(seed)
    worst = 0.0
    for _ in range(n):
        X = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        lam = X + X.T
        v, nn, s = rng.normal(size=3) + 1j * rng.normal(size=3)
        P = np.array([[v, 0], [nn, s]])
        sl = np.linalg.svd(lam, compute_uv=False)
        for Q in (P, P.T):
            sp = np.linalg.svd(Q, compute_uv=False)
            prod = np.sort(np.outer(sp, sl).ravel())
            got = np.sort(np.linalg.svd(np.kron(Q, lam), compute_uv=False))
            worst = max(worst, float(np.max(np.abs(got - prod) / prod)))
    return worst


def K3():
    w54 = json.loads((HERE / "the_rank_thirteen_structures.json").read_text(encoding="utf-8"))
    ph = json.loads((HERE / "the_rank_thirteen_structures_posthoc.json").read_text(encoding="utf-8"))
    s = w54["the structures (global minimum found)"]
    fitting = {k for k, v in s.items() if v["fits"]}
    if ph["read-outs (post hoc, no prior)"]["P1: (7, 7, 7) fits (Q + E_7 <= 5.99)"]:
        fitting.add("T (x) T: (7, 7, 7)")
    tied = sorted(k for k in fitting if s[k]["weights (u, d, e)"][1] == s[k]["weights (u, d, e)"][2])
    return {k: s[k]["P"] for k in tied}, sorted(fitting)


def main():
    bounds = {}
    for a in (0.05, 0.10, 0.20):
        chi, x = tie_bound(a)
        bounds[f"a = {a:.2f}"] = {"chi^2_min": chi, "shared ratios m1/m3, m2/m3 at the minimum":
                                  [float(np.exp(x[0])), float(np.exp(x[1]))]}
    ast = a_star()
    worst = K2()
    tied, fitting = K3()
    cells = {"K1: the tie's bound at a = 0.10 is at least 50": bounds["a = 0.10"]["chi^2_min"] >= 50,
             "K2: the Kronecker lemma holds on all 200 samples (1e-10)": worst < 1e-10,
             "K3: the fitting structures with k_d = k_e are exactly (5, 5, 5), (5, 7, 7), (7, 7, 7), each with P >= 23":
                 sorted(tied) == [f"T (x) T: {t}" for t in ((5, 5, 5), (5, 7, 7), (7, 7, 7))]
                 and all(P >= 23 for P in tied.values()),
             "K4: the allowance a* at which the bound falls to 5.99 is above 0.25": ast is not None and ast > 0.25}
    data = {s: {n: float(np.exp(FW.LOGM[s][i])) for i, n in enumerate(FW.NAMES[s])} for s in ("d", "e")}
    out = {"status": "W55: does the gauge side on record tell the sectors apart? (the rule first; one run)",
           "the data used (GeV)": data,
           "K1: the tie's bound": bounds, "K4: the allowance a* where the bound reaches 5.99": ast,
           "K2: the largest relative deviation over 400 Kronecker products": worst,
           "K3: the Standard Model frame's fitting structures (W54 with its post hoc)": fitting,
           "K3: those with k_d = k_e, and their P": tied,
           "cells (as worded)": {k: bool(v) for k, v in cells.items()},
           "priors": {"K1": 0.90, "K2": 0.97, "K3": 0.95, "K4": 0.80},
           "every cell holds": bool(all(cells.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells (as worded)"], indent=1))


if __name__ == "__main__":
    main()
