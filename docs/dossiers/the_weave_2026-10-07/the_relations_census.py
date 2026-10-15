"""W88: the relations census (step 1 of the route in docs/THE_MAP_TO_REALITY_2026-10-15.md). Each relation the record's
frames make among the nineteen numbers with no free size, against the data once under W66's predicate. The rule
(W88_RULE.md) was committed before this script; the relations, predictions and priors are there.

  Q1  point couplings (B1653): m1 = 0 in every sector, V's first row and column trivial
  Q2  one coupling for every sector (B1649, W73): m_c/m_t = m_s/m_b = m_mu/m_tau, V = 1
  Q3  the surface frame (W74): J = 0
  Q4  a hypercharge line of order dividing 6 (relay §115): up = down
  Q5  a hypercharge line of order dividing 4 (relay §115): down = leptons
  Q6  the thread frame's deep-cusp texture with one coupling (W84): ln(m1/m3)/ln(m2/m3) = 3/2 in each sector
  Q7  the inverse map on line orders N <= 12, given Q4 and Q5 refuted

Data: HZ2021's running masses at M_Z (W53's received file) and B1612's CKM moduli (received/B1612_data.json). J from
the moduli by the unitarity identity; its sigma from 10^5 Gaussian draws (seed 88).

Run: python3 the_relations_census.py  ->  the_relations_census.json beside it.
"""
import json
import math
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_relations_census.json"
A = 0.10
CHI95 = {1: 3.841, 2: 5.991, 3: 7.815}
ZSIG = 5.0
SECTORS = {"up": ("u", "c", "t"), "down": ("d", "s", "b"), "leptons": ("e", "mu", "tau")}


def load():
    hz = json.loads((HERE / "received" / "HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))
    ckm = json.loads((HERE / "received" / "B1612_data.json").read_text(encoding="utf-8"))["ckm_abs"]
    return hz["masses_GeV"]["value"], hz["masses_GeV"]["sigma"], np.array(ckm["value"]), np.array(ckm["sigma"])


MV, MS, VV, VS = load()


def ratio(a, b):
    """value and relative error of m_a / m_b"""
    return MV[a] / MV[b], math.hypot(MS[a] / MV[a], MS[b] / MV[b])


def z_eq(x, y):
    (vx, rx), (vy, ry) = x, y
    return (math.log(vx) - math.log(vy)) / math.sqrt(rx * rx + ry * ry + A * A)


def sigmas_from_zero(value, rel):
    return value / (value * rel)


def j_of(a, b, c, d):
    j2 = (a * b * c * d) ** 2 - 0.25 * (1 - a * a - b * b - c * c - d * d + a * a * d * d + b * b * c * c) ** 2
    return np.sqrt(np.maximum(j2, 0.0))


def jarlskog():
    idx = [(0, 0), (0, 1), (1, 0), (1, 1)]
    central = float(j_of(*[VV[i] for i in idx]))
    rng = np.random.default_rng(88)
    draws = [rng.normal(VV[i], VS[i], 100000) for i in idx]
    js = j_of(*draws)
    return central, float(np.std(js)), float(np.mean(js == 0.0))


def equalities(pairs):
    zs = {f"{p} = {q}": z_eq(ratio(*p.split("/")), ratio(*q.split("/"))) for p, q in pairs}
    return zs, float(sum(z * z for z in zs.values()))


def main():
    out = {"status": "W88: the relations census (script committed before its one run)", "a": A,
           "data": {"masses (GeV, M_Z)": MV, "CKM moduli": VV.tolist()}}
    vus = (float(VV[0, 1]), float(VV[0, 1] / VS[0, 1]))
    out["|V_us| and its sigmas from 0"] = list(vus)

    # Q1: point couplings
    firsts = {s: ratio(f[0], f[2]) for s, f in SECTORS.items()}
    sig1 = {s: sigmas_from_zero(*v) for s, v in firsts.items()}
    off = {"|V_us|": vus[1], "|V_ub|": float(VV[0, 2] / VS[0, 2]), "|V_cd|": float(VV[1, 0] / VS[1, 0]),
           "|V_td|": float(VV[2, 0] / VS[2, 0])}
    q1 = all(v > ZSIG for v in sig1.values()) and vus[1] > ZSIG
    out["Q1"] = {"m1/m3 per sector": {s: v[0] for s, v in firsts.items()},
                 "sigmas from 0": sig1, "the first row and column, sigmas from 0": off, "refuted": bool(q1)}

    # Q2: one coupling
    zs, chi = equalities([("c/t", "s/b"), ("s/b", "mu/tau")])
    q2 = chi > CHI95[2] and vus[1] > ZSIG
    out["Q2"] = {"z": zs, "sum z^2": chi, "threshold": CHI95[2], "refuted": bool(q2)}

    # Q3: J = 0
    J, sJ, frac0 = jarlskog()
    q3 = J / sJ > ZSIG
    out["Q3"] = {"J from the moduli": J, "sigma_J": sJ, "sigmas from 0": J / sJ, "draws with J^2 < 0": frac0,
                 "refuted": bool(q3)}

    # Q4: order dividing 6, up = down
    zs, chi = equalities([("c/t", "s/b"), ("u/t", "d/b")])
    q4 = chi > CHI95[2] and vus[1] > ZSIG
    out["Q4"] = {"z": zs, "sum z^2": chi, "threshold": CHI95[2], "refuted": bool(q4)}

    # Q5: order dividing 4, down = leptons
    zs, chi = equalities([("s/b", "mu/tau"), ("d/b", "e/tau")])
    q5 = chi > CHI95[2]
    out["Q5"] = {"z": zs, "sum z^2": chi, "threshold": CHI95[2], "refuted": bool(q5)}

    # Q6: W84's deep-cusp ratio 3/2
    rows, chi = {}, 0.0
    for s, (f1, f2, f3) in SECTORS.items():
        (x1, r1), (x2, r2) = ratio(f1, f3), ratio(f2, f3)
        l1, l2 = math.log(x1), math.log(x2)
        rho = l1 / l2
        r_rho = math.hypot(r1 / l1, r2 / l2)
        z = math.log(rho / 1.5) / math.sqrt(r_rho * r_rho + A * A)
        chi += z * z
        rows[s] = {"ln(m1/m3)": l1, "ln(m2/m3)": l2, "rho": rho, "relative error of rho": r_rho, "z": z}
    q6 = chi > CHI95[3]
    out["Q6"] = {"per sector": rows, "sum z^2": chi, "threshold": CHI95[3], "refuted": bool(q6)}

    # Q7: the inverse map on line orders
    left = [n for n in range(1, 13) if 4 % n != 0 and 6 % n != 0]
    out["Q7"] = {"orders N <= 12 dividing neither 4 nor 6": left, "as predicted": left == [5, 7, 8, 9, 10, 11, 12]}

    pred = {"Q1": q1, "Q2": q2, "Q3": q3, "Q4": q4, "Q5": q5, "Q6": q6, "Q7": out["Q7"]["as predicted"]}
    out["cells as predicted"] = {k: bool(v) for k, v in pred.items()}
    out["every cell as predicted"] = all(pred.values())
    out["relations holding"] = [k for k in ("Q1", "Q2", "Q3", "Q4", "Q5", "Q6") if not pred[k]]
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print("written", OUT.name)
    print(json.dumps(out["cells as predicted"], indent=1))


if __name__ == "__main__":
    main()
