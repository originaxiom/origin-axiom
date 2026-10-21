#!/usr/bin/env python3
"""W115 -- the leptons at the shared tau: does the modulus the quarks pin predict the charged leptons?  The rule is
W115_RULE.md, committed and pushed before this script.  One run; its output (the_shared_tau.json,
the_shared_tau_run.txt) is committed before it is read.

Pre-run disclosure: while this script was written, its parts were run in scratch only on code paths that touch no
cell: the lepton spaces' construction (their dimensions are on record, B1635), the curve evaluation and the pinned
routine at one random tau that is not a quark solution (0.21 + 1.17i, T(x)T at 3; it printed that no angle there fits
m_mu/m_tau exactly, and no chi-squared value), and the null's vectorised minimum on random curves.  No quark solution
was searched for, no lepton fit was run at any quark solution's tau, and W114's best points were not reproduced.

It reuses W113's and W114's code (the_strong_angle.py and the_tuned_fit.py, imported).  W114's best points are
reproduced exactly by replaying W114's sector construction (seed 114, in its order) and its searches (seeds 1150 + n).
"""
import itertools
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, minimize, minimize_scalar

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_strong_angle as SA  # noqa: E402
import the_tuned_fit as TF  # noqa: E402

T0 = time.time()
ASSIGNED = (11, 13, 14)
THRESH = {11: 1e-6, 13: 1e-6, 14: 3.84}
PASS = 3.84
NGRID = 40000
PHI = np.linspace(0.0, math.pi, NGRID, endpoint=False)


def log(*a):
    print(f"[{time.time() - T0:8.1f}s]", *a, flush=True)


def lepton_data():
    hz = json.loads((HERE / "received" / "HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))
    mv, ms = hz["masses_GeV"]["value"], hz["masses_GeV"]["sigma"]
    obs, rel = [], []
    for one, two in (("e", "mu"), ("mu", "tau")):
        obs.append(mv[one] / mv[two])
        rel.append(float(np.hypot(ms[one] / mv[one], ms[two] / mv[two])))
    return np.log(obs), np.array(rel)


LLOG, LREL = lepton_data()
LSIG = np.hypot(LREL, 0.10)


def lepton_ratios(sec, tau, phis):
    U, E = SA.u_eta_np(np.full(len(phis), tau))
    C = np.stack([np.cos(phis), np.sin(phis)], 1)
    _, s = SA.svd_sorted(sec.Y(U, E, C))
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.stack([s[:, 0] / s[:, 1], s[:, 1] / s[:, 2]], 1)


def chi2_lep(r, llog=LLOG):
    with np.errstate(divide="ignore", invalid="ignore"):
        z = (np.log(np.where(r > 0, r, 1e-300)) - llog) / LSIG
    c = np.sum(z * z, axis=-1)
    bad = np.any(~np.isfinite(r) | (r < SA.ZERO_OBS), axis=-1)
    return np.where(bad, np.inf, c)


def pinned(sec, tau, llog=LLOG):
    r = lepton_ratios(sec, tau, PHI)
    c = chi2_lep(r, llog)
    i = int(np.argmin(c))

    def f(phi):
        return float(chi2_lep(lepton_ratios(sec, tau, np.array([phi])), llog)[0])

    step = math.pi / NGRID
    res = minimize_scalar(f, bounds=(PHI[i] - step, PHI[i] + step), method="bounded",
                          options={"xatol": 1e-14})
    best = (float(res.fun), float(res.x)) if res.fun < c[i] else (float(c[i]), float(PHI[i]))
    # every angle where m_mu/m_tau equals the data exactly, and the m_e/m_mu predicted there
    target = math.exp(llog[1])
    g = r[:, 1] - target
    preds = []
    for j in range(NGRID):
        a, b = g[j], g[(j + 1) % NGRID]
        if np.isfinite(a) and np.isfinite(b) and a * b < 0:
            lo, hi = PHI[j], PHI[j] + step

            def h(phi):
                return float(lepton_ratios(sec, tau, np.array([phi]))[0, 1] - target)

            try:
                root = brentq(h, lo, hi, xtol=1e-15)
                preds.append({"phi": root, "m_e/m_mu predicted": float(lepton_ratios(sec, tau,
                                                                                      np.array([root]))[0, 0])})
            except ValueError:
                pass
    return {"chi2_min": best[0], "phi": best[1], "ratios at the minimum": lepton_ratios(sec, tau,
                                                                                       np.array([best[1]]))[0].tolist(),
            "exact m_mu/m_tau fits": preds}, r


def main():
    out = {"rule": "W115_RULE.md", "script": "the_shared_tau.py", "status": "one run",
           "lepton data": {"m_e/m_mu": float(math.exp(LLOG[0])), "m_mu/m_tau": float(math.exp(LLOG[1])),
                           "relative errors": LREL.tolist(), "allowance": 0.10}}

    # ---------------- W114's sectors, replayed exactly (seed 114, W114's order)
    rng114 = np.random.default_rng(114)
    secs = {}
    for _, _, up, dn in TF.ASSIGN:
        for typ, k in (up, dn):
            if (typ, k) not in secs:
                secs[(typ, k)] = TF.SectorParam(typ, k, rng114)
    models = {}
    for num, hand, up, dn in TF.ASSIGN:
        if num in ASSIGNED:
            models[num] = TF.Model(secs[up], secs[dn])
    w114 = json.loads((HERE / "the_tuned_fit.json").read_text(encoding="utf-8"))["assignments"]

    # ---------------- V1: the lepton census
    lep = {}
    dims = {}
    for typ in SA.TYPES:
        for k in SA.WEIGHTS[typ]:
            basis, d = SA.space(typ[0], typ[1], k)
            dims[f"{SA.NAME[typ]} k={k}"] = len(basis)
            if len(basis) in (1, 2):
                _, rb = SA.real_basis(basis, d)
                lep[(typ, k)] = SA.Sector(rb, SA.M_ETA[typ], f"{SA.NAME[typ]} k={k}")
    small = sorted(k for k, v in dims.items() if v <= 2)
    expected = sorted(["T(x)T k=1", "T(x)T k=3", "Tbar(x)Tbar k=1", "mixed (Q in T) k=0", "mixed (Q in T) k=2",
                       "mixed (Q in Tbar) k=0", "mixed (Q in Tbar) k=2"])
    out["V1"] = {"dimensions": dims, "the couplings with d <= 2": small, "as stated": small == expected}
    PRED = {"T(x)T k=3": lep[((1, 1), 3)], "mixed k=2": lep[((1, -1), 2)]}

    # ---------------- V2: the quark solutions
    sols = {}
    v2 = {}
    for num in ASSIGNED:
        t = time.time()
        model = models[num]
        (p114, v114), _, _, _ = TF.search(model, SA.LOGD, np.random.default_rng(1150 + num))
        tf114 = SA.to_fd(complex(p114[0], p114[1]))
        rec_tau = w114[str(num)]["best point"]["tau_in_F"]
        reproduced = abs(tf114 - complex(*rec_tau)) < 1e-6 and abs(v114 - w114[str(num)]["chi2_min (a = 0.10)"]) < 1e-6

        def f(p, model=model):
            return model.chi2(p, SA.LOGD, 0.10)

        rng = np.random.default_rng(115 + num)
        P1 = TF.random_starts(model, rng, 60000)
        v1 = TF.stage1(model, P1, SA.LOGD, 0.10)
        order = np.argsort(v1)
        ends = [TF.nm(f, P1[i], 8000) for i in order[:120]]
        ends.append(TF.nm(f, p114, 8000))
        found = []
        for p, v in sorted(ends, key=lambda e: e[1]):
            if v > THRESH[num]:
                continue
            tfp = SA.to_fd(complex(p[0], p[1]))
            if all(abs(tfp - q[2]) > 1e-3 for q in found):
                found.append((p, v, tfp))
        sols[num] = found
        v2[str(num)] = {"W114's best point reproduced": bool(reproduced), "W114's chi2": v114,
                        "W114's tau": [tf114.real, tf114.imag],
                        "W114's point among the solutions": bool(any(abs(tf114 - q[2]) <= 1e-3 for q in found)),
                        "solutions": [{"tau": [q[2].real, q[2].imag], "chi2_q": q[1]} for q in found],
                        "endpoints below the threshold": int(sum(1 for _, v in ends if v <= THRESH[num])),
                        "seconds": time.time() - t}
        log(f"assignment {num}: W114 reproduced {reproduced}; {len(found)} distinct solutions",
            [(round(q[2].real, 4), round(q[2].imag, 4), f"{q[1]:.1e}") for q in found])
    out["V2"] = v2
    out["V2 holds"] = bool(all(v2[str(n)]["W114's point among the solutions"] for n in (11, 13)))

    # V1's qualitative failures at every solution's tau
    fails = {}
    for num in ASSIGNED:
        for p, v, tfp in sols[num]:
            U, E = SA.u_eta_np(np.array([tfp]))
            row = {}
            for (typ, k), sec in lep.items():
                if sec.dim != 1:
                    continue
                _, s = SA.svd_sorted(sec.Y(U, E, np.array([1.0])))
                s = s[0]
                row[sec.label] = {"m2/m1": float(s[1] / s[2]), "m_min/m_max": float(s[0] / s[2]),
                                  "spread": float((s[2] - s[0]) / s[2])}
            fails[f"{num} at {tfp.real:.4f}+{tfp.imag:.4f}i"] = row
    ok_fail = all(r["T(x)T k=1"]["m2/m1"] >= 0.5 - 1e-12 and r["Tbar(x)Tbar k=1"]["m_min/m_max"] < 1e-12
                  and r["mixed (Q in T) k=0"]["spread"] < 1e-9 and r["mixed (Q in Tbar) k=0"]["spread"] < 1e-9
                  for r in fails.values())
    # the two mixed orders give the same masses
    trow = complex(0.21, 1.17)
    a = lepton_ratios(lep[((1, -1), 2)], trow, PHI[::4000])
    b = lepton_ratios(lep[((-1, 1), 2)], trow, PHI[::4000])
    out["V1"].update({"the d = 1 couplings at the solutions": fails, "they fail as stated": bool(ok_fail),
                      "the mixed orders' ratios agree (max difference over 10 angles; bases may differ)":
                          float(np.max(np.abs(np.sort(a, 1) - np.sort(b, 1))))})
    out["V1"]["holds"] = bool(out["V1"]["as stated"] and ok_fail)

    # ---------------- T1, pinned; V0's first half
    combos = []
    t1 = {}
    curves = {}
    for num in ASSIGNED:
        for si, (p, v, tfp) in enumerate(sols[num]):
            for lname, sec in PRED.items():
                key = f"{num}/{si}/{lname}"
                res, r = pinned(sec, tfp)
                t1[key] = dict(res, tau=[tfp.real, tfp.imag], chi2_q=v)
                curves[key] = r
                combos.append((key, num, si, lname))
                log("T1", key, f"chi2_min {res['chi2_min']:.4g}", "exact fits", len(res["exact m_mu/m_tau fits"]))
    out["T1"] = t1
    out["combinations"] = len(combos)
    best_t1 = min((t1[k]["chi2_min"] for k, *_ in combos), default=float("inf"))

    # V0, the control
    rc = np.random.default_rng(1151)
    v0 = {}
    if sols[13]:
        p13, v13, tf13 = sols[13][0]
        phistar = float(rc.uniform(0, math.pi))
        rstar = lepton_ratios(PRED["mixed k=2"], tf13, np.array([phistar]))[0]
        res, _ = pinned(PRED["mixed k=2"], tf13, np.log(rstar))
        model = models[13]

        def fj(q):
            r = model.evaluate(q[:-1])
            if r is None:
                return 1e30
            cq = SA.chi2_many(r[3][0][0], SA.LOGD, 0.10)
            cl = chi2_lep(lepton_ratios(PRED["mixed k=2"], r[0], np.array([q[-1]])), np.log(rstar))[0]
            tot = float(cq + cl)
            return tot if np.isfinite(tot) else 1e30

        qx, qv = TF.nm(fj, np.concatenate([p13, [res["phi"] + 0.05]]), 12000)
        v0 = {"phi*": phistar, "synthetic ratios": rstar.tolist(), "T1 chi2": res["chi2_min"], "T2 chi2": qv,
              "holds": bool(res["chi2_min"] <= 1e-6 and qv <= 0.01)}
    else:
        v0 = {"holds": False, "note": "no solution for 13"}
    out["V0"] = v0
    log("V0", v0.get("T1 chi2"), v0.get("T2 chi2"), v0.get("holds"))

    # ---------------- T2, joint
    t2 = {}
    for num in ASSIGNED:
        model = models[num]
        for lname, sec in PRED.items():
            best = (None, float("inf"))
            for si, (p, v, tfp) in enumerate(sols[num]):
                phi0 = t1[f"{num}/{si}/{lname}"]["phi"]

                def fj(q, model=model, sec=sec):
                    r = model.evaluate(q[:-1])
                    if r is None:
                        return 1e30
                    cq = SA.chi2_many(r[3][0][0], SA.LOGD, 0.10)
                    cl = chi2_lep(lepton_ratios(sec, r[0], np.array([q[-1]])))[0]
                    tot = float(cq + cl)
                    return tot if np.isfinite(tot) else 1e30

                qx, qv = TF.nm(fj, np.concatenate([p, [phi0]]), 12000)
                if qv < best[1]:
                    best = (qx, qv)
            rec = {"chi2_min": best[1]}
            if best[0] is not None and best[1] < 1e29:
                r = model.evaluate(best[0][:-1])
                rec.update({"tau": [r[0].real, r[0].imag],
                            "chi2_q": float(SA.chi2_many(r[3][0][0], SA.LOGD, 0.10)),
                            "lepton ratios": lepton_ratios(sec, r[0], np.array([best[0][-1]]))[0].tolist(),
                            "quark observables": dict(zip(SA.LABELS, r[3][0][0].tolist())), "J": float(r[3][1][0])})
            t2[f"{num}/{lname}"] = rec
            log("T2", num, lname, f"chi2_min {best[1]:.4g}")
    out["T2"] = t2
    best_t2 = min(v["chi2_min"] for v in t2.values())

    # ---------------- T3, the null (pinned; the family's best over every combination)
    rn = np.random.default_rng(1150)
    NT = 4000
    targets = LLOG[None, :] + rn.uniform(-math.log(10), math.log(10), size=(NT, 2))
    fam = np.full(NT, np.inf)
    per = {}
    data_grid = {}
    for key, *_ in combos:
        r = curves[key]
        lr = np.log(np.where(r > 0, r, 1e-300))
        badc = np.any(~np.isfinite(r) | (r < SA.ZERO_OBS), axis=1)
        mins = np.empty(NT)
        for s in range(0, NT, 50):
            tt = targets[s:s + 50]
            z = (lr[None, :, :] - tt[:, None, :]) / LSIG
            c = np.sum(z * z, axis=2)
            c[:, badc] = np.inf
            mins[s:s + 50] = c.min(axis=1)
        dg = float(chi2_lep(r)[np.isfinite(chi2_lep(r))].min()) if np.any(np.isfinite(chi2_lep(r))) else np.inf
        data_grid[key] = dg
        per[key] = {"data's grid chi2_min": dg, "p (this combination alone)": float(np.mean(mins <= dg))}
        fam = np.minimum(fam, mins)
    data_fam = min(data_grid.values()) if data_grid else float("inf")
    p_fam = float(np.mean(fam <= data_fam)) if combos else 1.0
    out["T3"] = {"targets": NT, "combinations": len(combos), "the data's family-best (grid)": data_fam,
                 "p (family)": p_fam, "per combination": per,
                 "the targets' family-best quantiles (5, 25, 50, 75, 95%)":
                     [float(x) for x in np.quantile(fam, [0.05, 0.25, 0.5, 0.75, 0.95])]}
    log("T3 p (family)", p_fam, "data's family-best", data_fam)

    out["cells"] = {"V0": bool(out["V0"].get("holds", False)), "V1": out["V1"]["holds"], "V2": out["V2 holds"],
                    "V3": bool(best_t1 > PASS), "V4": bool(best_t2 > PASS), "V5": bool(p_fam >= 0.05)}
    out["best pinned chi2"] = best_t1
    out["best joint chi2"] = best_t2
    out["seconds"] = time.time() - T0
    (HERE / "the_shared_tau.json").write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    log("cells", out["cells"])
    log("written the_shared_tau.json")


if __name__ == "__main__":
    main()
