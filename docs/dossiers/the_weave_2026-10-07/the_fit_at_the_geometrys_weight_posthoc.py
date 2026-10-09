"""W53, POST HOC (P1 to P3 written during W53's one run, after its progress line showed M0 failing; P4 added after W53's
read-out, for F1's failure; nothing in W53's JSON is changed). W53's rule claimed that T (x) T at (3, 3, 3) is the only
structure on record that could both fit and predict, and M0(e) checked that against W52's recorded scan. W52's own scan
(and its test) has two more at rank 11: T (x) T at (3, 3, 5) and (3, 3, 7). Their quark sector is (3, 3, 3)'s, and the
two relations are in the quark sector, so the lepton weight does not matter to them. This script settles those two as
well.

  P1  W52's recorded ranks: the assignments without an O+-alone sector below rank 13 are exactly T (x) T (3, 3, k_e),
      k_e = 3, 5, 7, each with rank 11.
  P2  the quark-only fit: the six quark log masses (two scales profiled) and the four log |V|, against tau, rho_u and
      rho_d (eight parameters with the scales; two degrees of freedom), at a = 0.10 (and 0.05, 0.20). Every structure
      (3, 3, k_e) has chi^2 >= its quark part, so a quark-only chi^2_min above 5.99 excludes all three.
  P3  the quark masses alone (six log masses, eight parameters) at a = 0.10.
  P4  W53's F1 failed for the up sector alone, its best point against the box edge x = -1/2. The same refinement
      with x free (tau -> tau + 1 is a symmetry, M0(c)): is the up sector alone reachable to 1e-6?
  Consistency with W53's JSON: the quark-only minimum does not exceed W53's 13-observable minimum at each a.

  The search is W53's, restricted to the quarks: the same tau grid and per-sector minima, the best of the nine
  combinations at each grid tau, then bounded least squares from the 60 best grid points and 200 random starts
  (seed 5310).

Run: python3 the_fit_at_the_geometrys_weight_posthoc.py  ->  the_fit_at_the_geometrys_weight_posthoc.json beside it.
"""
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_fit_at_the_geometrys_weight as FW  # noqa: E402  (W53: the model, the data, the grid, the sector minima)

OUT = HERE / "the_fit_at_the_geometrys_weight_posthoc.json"
QS = ("u", "d")
LB6 = [-0.5, FW.H0, -12, -50, -12, -50]
UB6 = [0.5, FW.YMAX, 12, 50, 12, 50]
QLABELS = FW.LABELS[:6] + FW.LABELS[9:]


def P1():
    w52 = json.loads((HERE / "the_free_numbers_counted.json").read_text(encoding="utf-8"))
    alone = {"T (x) T": {1}, "Sym^2 T": {1, 3}}
    below = {}
    for key, v in w52["C2: the scan"].items():
        frame, ks = key.split(": ")
        ks = tuple(int(x) for x in ks.strip("()").split(", "))
        if not any(k in alone[frame] for k in ks) and v["ranks at three points"] != [13] * 3:
            below[key] = v["ranks at three points"]
    want = {f"T (x) T: (3, 3, {k})": [11, 11, 11] for k in (3, 5, 7)}
    return below, below == want


def q_residuals_from(lu, ld, vlog, a, masses_only=False):
    res = []
    for s, l in (("u", lu), ("d", ld)):
        sig = np.sqrt(FW.DELM[s] ** 2 + a ** 2)
        w = 1 / sig ** 2
        c = np.sum(w * (FW.LOGM[s] - l)) / np.sum(w)
        res += list((l + c - FW.LOGM[s]) / sig)
    if not masses_only:
        res += list((vlog - FW.LOGV) / np.sqrt(FW.DELV ** 2 + a ** 2))
    return np.array(res)


def q_parts(theta):
    tau = FW.reduce(complex(theta[0], theta[1]))
    fp, fm = FW.forms_at(tau)
    Uu, su = FW.sector(fp, fm, np.exp(theta[2] + 1j * theta[3]))
    Ud, sd = FW.sector(fp, fm, np.exp(theta[4] + 1j * theta[5]))
    V = Uu.conj().T @ Ud
    vlog = np.log(np.maximum([abs(V[i, j]) for _, i, j in FW.CKM_KEYS], 1e-300))
    return tau, np.log(np.maximum(su, 1e-300)), np.log(np.maximum(sd, 1e-300)), vlog


def q_residuals(theta, a, masses_only=False):
    _, lu, ld, vlog = q_parts(theta)
    return q_residuals_from(lu, ld, vlog, a, masses_only)


def stage1(pts):
    rows = []
    for n, tau in enumerate(pts):
        fp, fm = FW.forms_at(tau)
        per, row = {}, {"tau": tau}
        for s in QS:
            mins = FW.sector_minima(fp, fm, FW.TARGET[s])
            per[s] = [(FW.sector(fp, fm, np.exp(u + 1j * v)), (u, v)) for _, u, v in mins]
            row[f"{s} residual"], row[f"{s} best"] = mins[0][0], mins[0][1:]
        mo = 0.0
        for s in QS:
            best = None
            for (_, sv), _ in per[s]:
                sig = np.sqrt(FW.DELM[s] ** 2 + FW.A_MAIN ** 2)
                w = 1 / sig ** 2
                ls = np.log(np.maximum(sv, 1e-300))
                c = np.sum(w * (FW.LOGM[s] - ls)) / np.sum(w)
                chi = float(np.sum(((ls + c - FW.LOGM[s]) / sig) ** 2))
                best = chi if best is None or chi < best else best
            mo += best
        row["quark masses only"] = (mo, [tau.real, tau.imag] + list(per["u"][0][1]) + list(per["d"][0][1]))
        for a in (FW.A_MAIN,) + FW.A_EXTRA:
            best = (np.inf, None)
            for (Uu, su), pu in per["u"]:
                for (Ud, sd), pd in per["d"]:
                    V = Uu.conj().T @ Ud
                    vlog = np.log(np.maximum([abs(V[i, j]) for _, i, j in FW.CKM_KEYS], 1e-300))
                    chi = float(np.sum(q_residuals_from(np.log(np.maximum(su, 1e-300)),
                                                        np.log(np.maximum(sd, 1e-300)), vlog, a) ** 2))
                    if chi < best[0]:
                        best = (chi, [tau.real, tau.imag, pu[0], pu[1], pd[0], pd[1]])
            row[a] = best
        rows.append(row)
        if n % 100 == 0:
            FW.log(f"post hoc stage 1: {n + 1} of {len(pts)}")
    return rows


def P4(rows):
    lb, ub = [-np.inf, FW.H0, -12, -50], [np.inf, FW.YMAX, 12, 50]
    lo, hi = np.array([-np.inf, FW.H0 + 1e-9, -12 + 1e-9, -50 + 1e-9]), np.array([np.inf, FW.YMAX - 1e-9, 12 - 1e-9,
                                                                                  50 - 1e-9])

    def fun(p):
        tau = FW.reduce(complex(p[0], p[1]))
        fp, fm = FW.forms_at(tau)
        return FW.ratio_res(p[2:], fp, fm, FW.TARGET["u"])

    sols = []
    for r in sorted(rows, key=lambda r: r["u residual"])[:30]:
        x0 = np.clip(np.array([r["tau"].real, r["tau"].imag] + list(r["u best"]), dtype=float), lo, hi)
        q = least_squares(fun, x0, bounds=(lb, ub), method="trf", xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=2000)
        tau = FW.reduce(complex(q.x[0], q.x[1]))
        sols.append((float(np.linalg.norm(q.fun)), [tau.real, tau.imag]))
    sols.sort(key=lambda t: t[0])
    exact = [t for c, t in sols if c < 1e-6]
    return {"the smallest residual": sols[0][0], "its tau": sols[0][1], "exact solutions found": len(exact),
            "their tau (rounded)": sorted([round(t[0], 4), round(t[1], 4)] for t in exact)}


def random_starts(n=200, seed=5310):
    rng = np.random.default_rng(seed)
    st = []
    for _ in range(n):
        th = [rng.uniform(-0.5, 0.5), float(np.exp(rng.uniform(np.log(0.87), np.log(FW.YMAX))))]
        for _ in QS:
            th += [rng.uniform(np.log(0.01), np.log(100)), rng.uniform(0, 2 * np.pi)]
        st.append(th)
    return st


def refine(fun, starts):
    out = []
    lb, ub = np.array(LB6), np.array(UB6)
    for th in starts:
        x0 = np.clip(np.array(th, dtype=float), lb + 1e-9, ub - 1e-9)
        r = least_squares(fun, x0, bounds=(LB6, UB6), method="trf", xtol=1e-12, ftol=1e-12, gtol=1e-12,
                          max_nfev=1500)
        out.append((float(np.sum(r.fun ** 2)), [float(x) for x in r.x]))
    out.sort(key=lambda t: t[0])
    return out


def describe(theta, a, masses_only=False):
    tau, lu, ld, vlog = q_parts(theta)
    res = q_residuals_from(lu, ld, vlog, a, masses_only)
    labels = QLABELS if not masses_only else QLABELS[:6]
    model = {"m_u/m_t": float(np.exp(lu[0] - lu[2])), "m_c/m_t": float(np.exp(lu[1] - lu[2])),
             "m_d/m_b": float(np.exp(ld[0] - ld[2])), "m_s/m_b": float(np.exp(ld[1] - ld[2]))}
    for (k, _, _), v in zip(FW.CKM_KEYS, vlog):
        model[f"|{k}|"] = float(np.exp(v))
    rhos = [np.exp(theta[2] + 1j * theta[3]), np.exp(theta[4] + 1j * theta[5])]
    return {"chi^2": float(np.sum(res ** 2)), "tau (reduced)": [tau.real, tau.imag],
            "distance from i": abs(tau - 1j), "distance from omega": min(abs(tau - w) for w in FW.OMEGAS),
            "rho_u, rho_d (modulus, phase)": [[float(abs(r)), float(np.angle(r))] for r in rhos],
            "pulls": {l: float(x) for l, x in zip(labels, res)}, "the model's ratios and |V|": model}


def main():
    below, p1 = P1()
    pts = FW.grid()
    rows = stage1(pts)
    p4 = P4(rows)
    FW.log(f"post hoc P4: the up sector's smallest residual with x free = {p4['the smallest residual']:.3g}")
    rnd = random_starts()
    fits = {}
    for name, key, a, mo in (("quark masses only, a = 0.10", "quark masses only", FW.A_MAIN, True),
                             ("quarks (ten observables), a = 0.10", FW.A_MAIN, FW.A_MAIN, False),
                             ("quarks (ten observables), a = 0.05", 0.05, 0.05, False),
                             ("quarks (ten observables), a = 0.20", 0.20, 0.20, False)):
        ranked = sorted(rows, key=lambda r: r[key][0])
        starts = [r[key][1] for r in ranked[:60]] + rnd
        res = refine(lambda th, a=a, mo=mo: q_residuals(th, a, mo), starts)
        d = describe(res[0][1], a, mo)
        d["starts reaching it (within 0.1)"] = sum(1 for c, _ in res if c < res[0][0] + 0.1)
        d["starts"] = len(res)
        d["the grid's best (stage 1)"] = ranked[0][key][0]
        fits[name] = d
        FW.log(f"post hoc {name}: chi^2_min = {d['chi^2']:.6g}")
    w53 = json.loads((HERE / "the_fit_at_the_geometrys_weight.json").read_text(encoding="utf-8"))
    full = w53["the fits (global minimum found)"]
    consistent = {a: bool(fits[f"quarks (ten observables), a = {a}"]["chi^2"]
                          <= full[f"13 observables, a = {a}"]["chi^2"] + 1e-6) for a in ("0.10", "0.05", "0.20")}
    q = fits["quarks (ten observables), a = 0.10"]["chi^2"]
    out = {"status": "W53 post hoc: the structures (3, 3, 5) and (3, 3, 7), through the quark sector alone "
                     "(labelled post hoc; W53's JSON unchanged)",
           "P1: W52's assignments without an O+-alone sector below rank 13": below,
           "P2, P3: the quark fits (global minimum found)": fits,
           "P4: the up sector alone with x free": p4,
           "consistency: the quark-only minimum does not exceed W53's 13-observable minimum": consistent,
           "read-outs (post hoc, no prior)": {
               "P1: exactly T (x) T (3, 3, k_e), k_e = 3, 5, 7, at rank 11": bool(p1),
               "P2: the quark-only chi^2_min at a = 0.10 exceeds 5.99 (then (3, 3, 5) and (3, 3, 7) fail too)": bool(
                   q > FW.THRESH),
               "P3: the quark-masses-only chi^2_min at a = 0.10 exceeds 5.99": bool(
                   fits["quark masses only, a = 0.10"]["chi^2"] > FW.THRESH),
               "P4: with x free the up sector alone is reachable to 1e-6": bool(p4["the smallest residual"] < 1e-6)}}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["read-outs (post hoc, no prior)"], indent=1))
    print("consistency:", consistent)


if __name__ == "__main__":
    main()
