#!/usr/bin/env python3
"""W119 -- beyond tree level: does a Kahler correction or a loop move theta-bar's structural zero, or carry the first
generation's forced coefficients into the data's windows?  The rule is W119_RULE.md, committed and pushed before this
script.  One run; its output (the_beyond_tree_level.json, the_beyond_tree_level_run.txt) is committed before it is
read.

The order: the rule was committed (403bf62b7) before this script was begun; its push waited on the pre-push suite and
came before this script's commit.

Pre-run disclosure: while this script was written, its parts were run in scratch only on code paths that touch no
cell: the Hermitian-metric sampler and the canonical normalization on random complex matrices (not W113's
couplings), and the RG integrator on a toy system with a known solution (dy/dt = y^3, whose blow-up time is exact).
No W113 coupling was evaluated, no physical running was integrated, and no cell was computed.
- What the dev test changed: on random matrices the float64 change in arg det was up to 2.2e-13, within a factor of 5
  of B1's threshold, from rounding alone; on random hierarchical matrices (columns scaled by 1, 1e-3, 1e-6) it was up
  to 8e-3, against 5e-38 at 50 digits. So B1 is decided at 50 digits (mpmath): each K^(-1/2) is made exactly
  Hermitian in float64, and the products and determinants are taken at 50 digits. The float64 change is reported
  beside it as a read-out. A non-Hermitian control, diag(1, 1, e^0.3i) on Q in both sectors (a change of 0.6 by
  construction), is also reported, to show the check can fail.

Inputs fixed here, within the rule:
- the gauge couplings at M_Z from alpha_em^-1(M_Z) = 127.95, sin^2 theta_W(M_Z) = 0.23122 and alpha_s(M_Z) = 0.1179
  (PDG-era values recalled by this seat, MS-bar); g1 in GUT normalization, g1 = sqrt(5/3) g';
- the third-generation masses at M_Z from W66's file (HZ2021, received/HZ2021_running_masses_MZ.json), with
  y = sqrt(2) m / v and v = 246 GeV, HZ2021's own convention;
- W113's forced assignment from the_strong_angle.py: every quark field in Tbar, Tbar(x)Tbar at weight 3 in both
  sectors, real coefficients drawn from seed 1191; three tau: 0.13 + 1.21i, -0.31 + 1.07i, 0.05 + 1.6i; the metrics
  K = A A^dagger + 0.1 (with A complex normal, seed 1192), 100 per field and tau;
- the integration: scipy's solve_ivp (DOP853, rtol 1e-10, atol 1e-12) in t = ln(mu / GeV); a point is dropped if any
  Yukawa exceeds sqrt(4 pi) on the way.
"""
import json
import math
import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_strong_angle as SA  # noqa: E402  (W113's spaces and evaluation)
import the_shared_tau as ST  # noqa: E402  (W115's lepton data)

T0 = time.time()
OUT = HERE / "the_beyond_tree_level.json"
MZ = 91.1876
V = 246.0
PI16 = 16 * math.pi ** 2
B_GAUGE = {"SM": (41 / 10, -19 / 6, -7.0), "MSSM": (33 / 5, 1.0, -3.0)}
TANB = (2, 5, 10, 20, 30, 40, 50)
LAMBDAS = (1e12, 1e14, 1e16)
YMAX = math.sqrt(4 * math.pi)
FORCED = {"W68 E with X": Fraction(15), "W68 EE, X with X": Fraction(1), "W118 P2 with E": Fraction(735, 121),
          "W118 P2 with X": Fraction(77, 4), "W118 P3 with E": Fraction(3, 5), "W118 P3 with X": Fraction(5, 4),
          "W118 P2 with P3": Fraction(385, 529)}


def log(*a):
    print(f"[{time.time() - T0:9.1f}s]", *a, flush=True)


# ------------------------------------------------------------------------------------------- part K
def herm_pos(rng):
    A = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    return A @ A.conj().T + 0.1 * np.eye(3)


def inv_sqrt(K):
    w, U = np.linalg.eigh(K)
    S = U @ np.diag(w ** -0.5) @ U.conj().T
    return (S + S.conj().T) / 2  # exactly Hermitian as a float64 matrix


def arg_det(M):
    return float(np.angle(np.linalg.det(M)))


def wrap(x):
    return (x + math.pi) % (2 * math.pi) - math.pi


def mpm(A):
    return mp.matrix([[mp.mpc(complex(x)) for x in row] for row in A])


def arg_det_mp(*Ms):
    P = mp.eye(3)
    for M in Ms:
        P = P * mpm(M)
    return mp.arg(mp.det(P))


def wrap_mp(x):
    return float(abs((x + mp.pi) % (2 * mp.pi) - mp.pi))


def part_k():
    mp.mp.dps = 50
    basis, d = SA.space(-1, -1, 3)
    _, rb = SA.real_basis(basis, d)
    sec = SA.Sector(rb, SA.M_ETA[(-1, -1)], "Tbar(x)Tbar k=3")
    rc = np.random.default_rng(1191)
    cu, cd = rc.normal(size=sec.dim), rc.normal(size=sec.dim)
    rk = np.random.default_rng(1192)
    rows, worst, worst64 = {}, 0.0, 0.0
    for tau in (complex(0.13, 1.21), complex(-0.31, 1.07), complex(0.05, 1.6)):
        U, E = SA.u_eta_np(np.array([SA.to_fd(tau)]))
        Yu, Yd = sec.Y(U, E, cu)[0], sec.Y(U, E, cd)[0]
        a0, a064 = arg_det_mp(Yu, Yd), arg_det(Yu @ Yd)
        dev, dev64 = 0.0, 0.0
        for _ in range(100):
            SQ, Su, Sd = (inv_sqrt(herm_pos(rk)) for _ in range(3))
            dev = max(dev, wrap_mp(arg_det_mp(SQ, Yu, Su, SQ, Yd, Sd) - a0))
            dev64 = max(dev64, abs(wrap(arg_det(SQ @ Yu @ Su @ SQ @ Yd @ Sd) - a064)))
        ctrl = np.diag([1, 1, np.exp(0.3j)])
        rows[f"{tau}"] = {"arg det(Yu Yd)": float(a0), "worst change over 100 metrics, 50 digits": dev,
                          "worst change over 100 metrics, float64 (read-out)": dev64,
                          "non-Hermitian control, change": wrap_mp(arg_det_mp(ctrl, Yu, ctrl, Yd) - a0),
                          "|det(Yu Yd)|": float(abs(np.linalg.det(Yu @ Yd)))}
        worst, worst64 = max(worst, dev), max(worst64, dev64)
    return {"per tau": rows, "worst change": worst, "worst change float64 (read-out)": worst64,
            "holds": bool(worst <= 1e-12)}


# ------------------------------------------------------------------------------------------- part L
def gauge_at_mz():
    e = math.sqrt(4 * math.pi / 127.95)
    s = math.sqrt(0.23122)
    c = math.sqrt(1 - 0.23122)
    g2, gp = e / s, e / c
    return math.sqrt(5 / 3) * gp, g2, math.sqrt(4 * math.pi * 0.1179)


def rhs(model):
    b = B_GAUGE[model]

    def f(t, z):
        g1, g2, g3, yt, yb, ytau = z[:6]
        g = (g1, g2, g3)
        dg = [b[i] * g[i] ** 3 / PI16 for i in range(3)]
        if model == "SM":
            T = 3 * yt ** 2 + 3 * yb ** 2 + ytau ** 2
            dyt = yt * (1.5 * (yt ** 2 - yb ** 2) + T - (17 / 20 * g1 ** 2 + 9 / 4 * g2 ** 2 + 8 * g3 ** 2)) / PI16
            dyb = yb * (1.5 * (yb ** 2 - yt ** 2) + T - (1 / 4 * g1 ** 2 + 9 / 4 * g2 ** 2 + 8 * g3 ** 2)) / PI16
            dyta = ytau * (1.5 * ytau ** 2 + T - (9 / 4 * g1 ** 2 + 9 / 4 * g2 ** 2)) / PI16
            c_up, c_dn, c_lp = 1.5 * (yt ** 2 - yb ** 2), 1.5 * (yb ** 2 - yt ** 2), 1.5 * ytau ** 2
        else:
            dyt = yt * (6 * yt ** 2 + yb ** 2 - (13 / 15 * g1 ** 2 + 3 * g2 ** 2 + 16 / 3 * g3 ** 2)) / PI16
            dyb = yb * (yt ** 2 + 6 * yb ** 2 + ytau ** 2 - (7 / 15 * g1 ** 2 + 3 * g2 ** 2 + 16 / 3 * g3 ** 2)) / PI16
            dyta = ytau * (3 * yb ** 2 + 4 * ytau ** 2 - (9 / 5 * g1 ** 2 + 3 * g2 ** 2)) / PI16
            c_up, c_dn, c_lp = 3 * yt ** 2 + yb ** 2, 3 * yb ** 2 + yt ** 2, 3 * ytau ** 2
        return dg + [dyt, dyb, dyta, c_up / PI16, c_dn / PI16, c_lp / PI16]
    return f


def run(model, tanb, lam, masses):
    g1, g2, g3 = gauge_at_mz()
    mt, mb, mta = masses
    if model == "SM":
        y0 = [math.sqrt(2) * m / V for m in (mt, mb, mta)]
    else:
        sb, cb = math.sin(math.atan(tanb)), math.cos(math.atan(tanb))
        y0 = [math.sqrt(2) * mt / (V * sb), math.sqrt(2) * mb / (V * cb), math.sqrt(2) * mta / (V * cb)]

    def blow(t, z):
        return YMAX - max(z[3:6])
    blow.terminal = True
    sol = solve_ivp(rhs(model), (math.log(MZ), math.log(lam)), [g1, g2, g3] + y0 + [0.0, 0.0, 0.0], method="DOP853",
                    rtol=1e-10, atol=1e-12, events=blow)
    z = sol.y[:, -1]
    kept = bool(sol.status == 0 and max(np.max(sol.y[3:6], axis=1)) < YMAX)
    F = {"up": math.exp(-z[6]), "down": math.exp(-z[7]), "leptons": math.exp(-z[8])}
    return {"kept": kept, "y at M_Z": y0, "y at Lambda": [float(x) for x in z[3:6]],
            "g at Lambda": [float(x) for x in z[:3]], "F": F}


def windows():
    out = {}
    for name, (i, j), logd, rel in (("up", (0, 1), SA.LOGD, SA.REL), ("down", (2, 3), SA.LOGD, SA.REL),
                                    ("leptons", (0, 1), ST.LLOG, ST.LREL)):
        dr = math.exp(logd[i] - logd[j])
        sig = math.sqrt(math.hypot(rel[i], 0.10) ** 2 + math.hypot(rel[j], 0.10) ** 2)
        out[name] = [dr * math.exp(-1.96 * sig), dr * math.exp(1.96 * sig)]
    return out


def control_b0():
    out = {}
    for model in ("SM", "MSSM"):
        g1, g2, g3 = gauge_at_mz()
        b = B_GAUGE[model]
        L = math.log(2e16 / MZ)
        gs = [1 / math.sqrt(1 / g ** 2 - 2 * bi * L / PI16) for g, bi in zip((g1, g2, g3), b)]
        out[model] = {"g at 2e16 GeV": gs, "spread": (max(gs) - min(gs)) / (sum(gs) / 3)}
    out["holds"] = bool(out["MSSM"]["spread"] < 0.02 and out["SM"]["spread"] > 0.05)
    return out


def main():
    out = {"rule": "W119_RULE.md", "script": "the_beyond_tree_level.py", "status": "one run"}
    out["B0"] = control_b0()
    log("B0", out["B0"]["holds"], {m: round(out["B0"][m]["spread"], 4) for m in ("SM", "MSSM")})
    out["B1"] = part_k()
    log("B1", out["B1"]["holds"], out["B1"]["worst change"])

    hz = json.loads((HERE / "received" / "HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))
    mv = hz["masses_GeV"]["value"]
    masses = (mv["t"], mv["b"], mv["tau"])
    wins = windows()
    out["windows"] = wins
    points = []
    for model in ("SM", "MSSM"):
        for tanb in ((None,) if model == "SM" else TANB):
            for lam in LAMBDAS:
                r = run(model, tanb, lam, masses)
                r.update({"model": model, "tan beta": tanb, "Lambda": lam})
                reach = {}
                for s in ("up", "down", "leptons"):
                    reach[s] = [k for k, v in FORCED.items() if wins[s][0] <= float(v) * r["F"][s] <= wins[s][1]]
                r["reaches"] = reach
                r["coherent"] = bool(r["kept"] and all(reach[s] for s in reach))
                points.append(r)
                log(model, tanb, f"{lam:.0e}", "kept", r["kept"], {s: round(v, 4) for s, v in r["F"].items()},
                    {s: len(v) for s, v in reach.items()})
    kept = [p for p in points if p["kept"]]
    band = {s: [min(p["F"][s] for p in kept), max(p["F"][s] for p in kept)] for s in ("up", "down", "leptons")}
    out["points"] = points
    out["B2"] = {"band of F over the kept points": band, "kept": len(kept), "of": len(points),
                 "holds": bool(all(0.4 <= lo and hi <= 2.5 for lo, hi in band.values()))}
    coherent = [(p["model"], p["tan beta"], p["Lambda"]) for p in kept if p["coherent"]]
    lepton_reach = [(p["model"], p["tan beta"], p["Lambda"]) for p in kept if p["reaches"]["leptons"]]
    out["B3"] = {"coherent points": coherent, "points where some forced coefficient reaches the leptons' window":
                 lepton_reach, "holds": bool(not coherent and not lepton_reach)}
    out["B4"] = {s: sorted({k for p in kept for k in p["reaches"][s]}) for s in ("up", "down", "leptons")}
    out["cells"] = {c: out[c]["holds"] for c in ("B0", "B1", "B2", "B3")}
    out["seconds"] = time.time() - T0
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    log("B2", out["B2"]["holds"], band)
    log("B3", out["B3"]["holds"], "coherent", coherent, "lepton reach", lepton_reach)
    log("cells", out["cells"])
    log("written the_beyond_tree_level.json")


if __name__ == "__main__":
    main()
