"""W112: the skeleton's significance (stage 1 of THE_SKELETON_AND_THE_FLESH.md). The rule, W112_RULE.md, was committed
and pushed before this script (e49b89655). One run.

Does W69's menu of forced assignments (28 pairs of the seven parameter-free sections per sector, 28^3 assignments)
fit the data's hierarchy pattern at the skeleton level -- every fitted observable within a factor F -- better than it
fits random targets?

  K0  the control: W69's best point evaluated here gives W69's five observables to 1%
  K1  F*(data) <= 2 on the grid
  K2  p_B1 < 0.05 (synthetic targets log-uniform within a decade of the data)
  K3  p_B2 < 0.05 (within half a decade)
  K4  at most 50 distinct assignments within a factor 2
  K5  every point within a factor 2 lies within 0.12 of an elliptic point
  K6  at every point within a factor 2, some sector's m1/m3 is 0 or more than a factor 10 from the data

Run: python3 the_skeleton.py -> the_skeleton.json and the_skeleton_run.txt beside it.
"""
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_parameter_free_census as PF  # noqa: E402  (W66: the data, the grid, the domain map)
import the_weighted_census as WC  # noqa: E402  (W69: the seven sections, the 28 pairs, the observables)

OUT = HERE / "the_skeleton.json"
RUN = HERE / "the_skeleton_run.txt"
LINES = []
OMEGA = complex(-0.5, np.sqrt(3) / 2)
ELLIPTIC = [OMEGA, OMEGA + 1, 1j]
LN2, LN3 = np.log(2.0), np.log(3.0)
NP = len(WC.PAIRS)


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    LINES.append(s)


def in_fd(t):
    return abs(t.real) <= 0.5 + 1e-12 and abs(t) >= 1 - 1e-12 and t.imag > 0


def points():
    pts = list(PF.grid())
    for c in ELLIPTIC:
        for r in np.geomspace(1e-3, 0.12, 24):
            for th in np.linspace(0, 2 * np.pi, 36, endpoint=False):
                t = c + r * np.exp(1j * th)
                if in_fd(t):
                    pts.append(t)
    return np.array(pts)


def delta(t):
    return min(abs(t - c) for c in ELLIPTIC)


def pair_arrays(vals):
    R1, R2, U = [], [], []
    for a, b in WC.PAIRS:
        va, vb = vals[a], vals[b]
        Y = va[:, :, None] * vb[:, None, :] + vb[:, :, None] * va[:, None, :]
        Y -= np.einsum("ti,ti->t", va, vb)[:, None, None] * np.eye(3)[None]
        u, s, _ = np.linalg.svd(Y)
        s, u = s[:, ::-1], u[:, :, ::-1]
        R1.append(s[:, 0] / s[:, 2])
        R2.append(s[:, 1] / s[:, 2])
        U.append(u)
    return np.array(R1), np.array(R2), np.array(U)


def safelog(x):
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(x > 1e-12, np.log(np.maximum(x, 1e-300)), np.nan)


def ckm_tables(U):
    T = U.shape[1]
    V01, V12, V02, V20 = (np.empty((NP, NP, T)) for _ in range(4))
    for pu in range(NP):
        V = np.einsum("tji,qtjk->qtik", U[pu].conj(), U)
        V01[pu], V12[pu] = np.abs(V[:, :, 0, 1]), np.abs(V[:, :, 1, 2])
        V02[pu], V20[pu] = np.abs(V[:, :, 0, 2]), np.abs(V[:, :, 2, 0])
    return V01, V12, V02, V20


def dist(L, lx):
    d = np.abs(L - lx)
    return np.where(np.isnan(d), np.inf, d)


class Menu:
    def __init__(self, L2, LV01, LV12):
        self.L2, self.LV01, self.LV12 = L2, LV01, LV12

    def parts(self, lx):
        du, dd, de = dist(self.L2, lx[0]), dist(self.L2, lx[1]), dist(self.L2, lx[2])
        q = np.maximum(np.maximum(du[:, None, :], dd[None, :, :]),
                       np.maximum(dist(self.LV01, lx[3]), dist(self.LV12, lx[4])))   # (pu, pd, T)
        return q, de

    def D(self, lx):
        q, de = self.parts(lx)
        return float(np.min(np.maximum(q.min(axis=(0, 1)), de.min(axis=0))))


def data():
    hz = json.loads((HERE / "received" / "HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))
    ckm = json.loads((HERE / "received" / "B1612_data.json").read_text(encoding="utf-8"))["ckm_abs"]["value"]
    m = hz["masses_GeV"]["value"]
    first = {"m_u/m_t": m["u"] / m["t"], "m_d/m_b": m["d"] / m["b"], "m_e/m_tau": m["e"] / m["tau"]}
    return np.array(PF.LOGD), first, {"|V_ub|": ckm[0][2], "|V_td|": ckm[2][0]}


def refine(S, assign, t0, lx):
    def f(xy):
        t = PF.to_fd(complex(xy[0], xy[1]))
        if t.imag > 6:
            return 1e3
        obs = WC.observables(S, assign, t)[0]
        if np.any(obs < 1e-12):
            return 1e3
        return float(np.max(np.abs(np.log(obs) - lx)))
    r = minimize(f, [t0.real, t0.imag], method="Nelder-Mead", options={"xatol": 1e-9, "fatol": 1e-10, "maxiter": 3000})
    return float(np.exp(r.fun)), PF.to_fd(complex(*r.x))


def main():
    out = {"status": "one run", "rule": "W112_RULE.md (e49b89655)", "cells": {}}
    lx, first, ckm_first = data()
    sec, S = WC.solve_all()
    pts = points()
    w69 = json.loads((HERE / "the_weighted_census.json").read_text(encoding="utf-8"))
    best69 = w69["read-outs"]["the ten best at a = 0.10"][0]
    t69 = complex(*best69["tau_min"])
    pts = np.append(pts, t69)
    say("tau points:", len(pts), "(W66's grid, the three elliptic patches, and W69's best point last)")
    vals = WC.values_on(S, pts)
    R1, R2, U = pair_arrays(vals)
    V01, V12, V02, V20 = ckm_tables(U)
    L2, LV01, LV12 = safelog(R2), safelog(V01), safelog(V12)

    # K0: the control at W69's best point, by W69's own per-point path and by this instrument's tables
    idx69 = tuple(WC.PNAME.index(n) for n in best69["assignment (up / down / lepton)"].split(" / "))
    obs69 = WC.observables(S, idx69, t69)[0]
    rec69 = np.array([best69["observables"][k] for k in PF.LABELS])
    k = len(pts) - 1
    tab = np.array([R2[idx69[0], k], R2[idx69[1], k], R2[idx69[2], k], V01[idx69[0], idx69[1], k],
                    V12[idx69[0], idx69[1], k]])
    k0 = bool(np.max(np.abs(obs69 / rec69 - 1)) < 0.01 and np.max(np.abs(tab / rec69 - 1)) < 0.01)
    out["K0"] = {"W69's recorded observables": rec69.tolist(), "W69's path here": obs69.tolist(),
                 "this instrument's tables": tab.tolist(), "holds": k0}
    out["cells"]["K0"] = k0
    say("K0", "held" if k0 else "FAILED", out["K0"])
    pts, L2, LV01, LV12 = pts[:-1], L2[:, :-1], LV01[:, :, :-1], LV12[:, :, :-1]
    R1, V02, V20 = R1[:, :-1], V02[:, :, :-1], V20[:, :, :-1]
    menu = Menu(L2, LV01, LV12)

    # the real data
    q, de = menu.parts(lx)
    Dassign = np.empty((NP, NP, NP))
    for pe in range(NP):
        Dassign[:, :, pe] = np.min(np.maximum(q, de[pe][None, None, :]), axis=2)
    Dd = float(Dassign.min())
    Fstar = float(np.exp(Dd))
    within2 = [tuple(map(int, i)) for i in np.argwhere(Dassign <= LN2)]
    within3 = [tuple(map(int, i)) for i in np.argwhere(Dassign <= LN3)]
    out["cells"]["K1"] = bool(Fstar <= 2)
    out["K1"] = {"F*(data) on the grid": Fstar}
    say("K1", "held" if Fstar <= 2 else "FAILED", "F*(data) =", Fstar)
    out["cells"]["K4"] = bool(len(within2) <= 50)
    out["K4"] = {"assignments within a factor 2": len(within2), "within a factor 3": len(within3)}
    say("K4", "held" if len(within2) <= 50 else "FAILED", out["K4"])

    # K5, K6: every (assignment, point) within a factor 2
    near, firstgen, rows = True, True, []
    for (pu, pd, pe) in within2:
        tt = np.where(np.maximum(q[pu, pd], de[pe]) <= LN2)[0]
        for t in tt:
            dl = delta(pts[t])
            near = near and dl <= 0.12
            r1 = [float(R1[pu, t]), float(R1[pd, t]), float(R1[pe, t])]
            bad = [r < 1e-12 or abs(np.log(r / v)) > np.log(10) for r, v in zip(r1, first.values())]
            firstgen = firstgen and any(bad)
            if len(rows) < 60:
                rows.append({"assignment": WC.label((pu, pd, pe)), "tau": [pts[t].real, pts[t].imag], "delta": dl,
                             "factor": float(np.exp(max(q[pu, pd, t], de[pe, t]))), "m1/m3 (up, down, lepton)": r1,
                             "|V_ub|": float(V02[pu, pd, t]), "|V_td|": float(V20[pu, pd, t])})
    out["cells"]["K5"] = bool(near and len(within2) > 0)
    out["cells"]["K6"] = bool(firstgen and len(within2) > 0)
    out["points within a factor 2 (first 60)"] = rows
    out["K5 and K6 vacuous (no point within a factor 2)"] = len(within2) == 0
    say("K5", "held" if out["cells"]["K5"] else "FAILED", "; K6", "held" if out["cells"]["K6"] else "FAILED")

    # the null: target randomisation in two boxes
    rng = np.random.default_rng(112)
    nulls = {}
    for name, half in (("B1", np.log(10.0)), ("B2", 0.5 * np.log(10.0))):
        Ds = np.array([menu.D(lx + rng.uniform(-half, half, size=5)) for _ in range(4000)])
        p = float(np.mean(Ds <= Dd + 1e-12))
        nulls[name] = {"N": 4000, "p": p, "F* quantiles (5, 25, 50, 75, 95%)":
                       np.exp(np.percentile(Ds, [5, 25, 50, 75, 95])).tolist(),
                       "fraction of targets within a factor 2": float(np.mean(Ds <= LN2))}
        say(name, nulls[name])
    out["null"] = nulls
    out["cells"]["K2"] = bool(nulls["B1"]["p"] < 0.05)
    out["cells"]["K3"] = bool(nulls["B2"]["p"] < 0.05)

    # read-outs: the ten best assignments, refined
    order = np.argsort(Dassign, axis=None)[:10]
    best = []
    for flat in order:
        pu, pd, pe = np.unravel_index(flat, Dassign.shape)
        tt = int(np.argmin(np.maximum(q[pu, pd], de[pe])))
        Fr, tr = refine(S, (int(pu), int(pd), int(pe)), pts[tt], lx)
        obs, extra = WC.observables(S, (int(pu), int(pd), int(pe)), tr)
        best.append({"assignment": WC.label((pu, pd, pe)), "grid factor": float(np.exp(Dassign[pu, pd, pe])),
                     "refined factor": Fr, "tau": [tr.real, tr.imag], "delta": delta(tr),
                     "observables": dict(zip(PF.LABELS, map(float, obs))), "unfitted": extra})
    out["the ten best, refined"] = best
    out["data"] = {"fitted": dict(zip(PF.LABELS, np.exp(lx).tolist())), "first generation": first,
                   "unfitted CKM": ckm_first}
    say("the best, refined:", best[0])
    say("cells:", out["cells"])
    OUT.write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
    RUN.write_text("\n".join(LINES) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
