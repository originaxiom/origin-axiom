"""W53 (the rule: W53_RULE.md, committed with its data before this script). The fit at the geometry's weight: W52's
structure T (x) T at k = 3 in every sector, Y_s = e^{c_s} (F+^ (tau) + rho_s F-^ (tau)), against the 13 flavour
numbers. The masses are at M_Z (Huang and Zhou 2021, received/HZ2021_running_masses_MZ.json), the CKM is PDG 2025
(received/B1612_data.json). Observables in logs, sigma_i = sqrt(delta_i^2 + a^2), the three scales profiled.

  M0  the controls: (a) one form in O+ and one in O- at k = 3, symmetric and antisymmetric with zero diagonal;
      (b) rho_T(S) and rho_T(T) unitary in the basis t_p; (c) the ten shape observables unchanged under tau -> tau + 1
      and tau -> -1/tau at five random points, to 1e-8; (d) the 13 x 11 Jacobian's rank 11 at three random points;
      (e) in W52's recorded scan, every assignment without an O+-alone sector has rank 13, except T (x) T (3, 3, 3): 11.
  F1  each sector alone reachable: its two log mass ratios reproduced to 1e-6 by some tau in the domain and rho_s.
  F2  the masses-only chi^2_min (nine log masses, eleven parameters, a = 0.10) exceeds 5.99.
  F3  the fit: chi^2_min <= 5.99 at a = 0.10 (13 observables, 11 parameters).
  F4  at tau = 5i, every grid rho with m2/m3 in [0.005, 0.05] has m1/m3 in [0.95, 1.20] x 1e-3 (at least 20 points).

  The search (fixed in the rule): a tau grid over the fundamental domain (y <= 6); at each grid tau each sector's rho
  fitted to its two ratios from 72 starts, the best three minima kept, the best of the 27 combinations; a joint bounded
  least-squares refinement from the 60 best grid points and 200 random starts (seed 5300), for the 13-observable
  objective at a = 0.10, 0.05 and 0.20 and for the masses-only objective; F1's refinements from each sector's 30 best
  grid points. A trial tau with |tau| < 1 is mapped into the fundamental domain before evaluation.

Run: python3 the_fit_at_the_geometrys_weight.py  ->  the_fit_at_the_geometrys_weight.json beside it.
"""
import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_free_numbers_counted as FC  # noqa: E402  (W52: the forms by frame and weight, and its scan)

PG = FC.PG                                   # W50: rho_T in the basis t_p
GM, H = PG.GM, PG.H
OUT = HERE / "the_fit_at_the_geometrys_weight.json"
SECTORS = ("u", "d", "e")
NAMES = {"u": ("u", "c", "t"), "d": ("d", "s", "b"), "e": ("e", "mu", "tau")}
CKM_KEYS = (("V_us", 0, 1), ("V_cb", 1, 2), ("V_ub", 0, 2), ("V_td", 2, 0))
LABELS = [f"log m_{n}" for s in SECTORS for n in NAMES[s]] + [f"log |{k}|" for k, _, _ in CKM_KEYS]
A_MAIN, A_EXTRA = 0.10, (0.05, 0.20)
THRESH = 5.99
YMAX = 6.0
H0 = np.sqrt(3) / 2
OMEGAS = (complex(-0.5, H0), complex(0.5, H0))
T0 = time.time()


def log(msg):
    print(f"[{time.time() - T0:7.1f} s] {msg}", flush=True)


# ------------------------------------------------------------------------------------------------------------- data
def load_data():
    hz = json.loads((HERE / "received" / "HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))
    b1612 = json.loads((HERE / "received" / "B1612_data.json").read_text(encoding="utf-8"))
    mv, ms = hz["masses_GeV"]["value"], hz["masses_GeV"]["sigma"]
    logm = {s: np.log([mv[n] for n in NAMES[s]]) for s in SECTORS}
    delm = {s: np.array([ms[n] / mv[n] for n in NAMES[s]]) for s in SECTORS}
    cv, cs = b1612["ckm_abs"]["value"], b1612["ckm_abs"]["sigma"]
    logv = np.log([cv[i][j] for _, i, j in CKM_KEYS])
    delv = np.array([cs[i][j] / cv[i][j] for _, i, j in CKM_KEYS])
    used = {"masses (GeV)": {n: [mv[n], ms[n]] for s in SECTORS for n in NAMES[s]},
            "CKM": {k: [cv[i][j], cs[i][j]] for k, i, j in CKM_KEYS}}
    return logm, delm, logv, delv, used


LOGM, DELM, LOGV, DELV, USED = load_data()
TARGET = {s: LOGM[s][:2] - LOGM[s][2] for s in SECTORS}            # log(m1/m3), log(m2/m3)


# ------------------------------------------------------------------------------------------------------------ forms
FORMS, BY_PIECE = FC.basis_functions()
FP_RAW, FM_RAW = FORMS["T (x) T"][3]


def reduce(tau):
    """into the fundamental domain |x| <= 1/2, |tau| >= 1 (the observables are invariant, M0(c))"""
    for _ in range(60):
        tau = complex(tau.real - round(tau.real), tau.imag)
        if abs(tau) < 1 - 1e-15:
            tau = -1 / tau
        else:
            break
    return tau


def forms_at(tau):
    fp, fm = FP_RAW(tau), FM_RAW(tau)
    return fp / np.linalg.norm(fp), fm / np.linalg.norm(fm)


def sector(fp, fm, rho):
    U, sv, _ = np.linalg.svd(fp + rho * fm)
    idx = np.argsort(sv)
    return U[:, idx], sv[idx]


def raw_observables(fp, fm, rhos):
    """the nine log singular values (by sector, ascending) and the four log |V|"""
    logs, Us = [], {}
    for s, rho in zip(SECTORS, rhos):
        U, sv = sector(fp, fm, rho)
        Us[s] = U
        logs.append(np.log(np.maximum(sv, 1e-300)))
    V = Us["u"].conj().T @ Us["d"]
    vlog = np.log(np.maximum([abs(V[i, j]) for _, i, j in CKM_KEYS], 1e-300))
    return logs, vlog


def rhos_of(theta):
    return [np.exp(theta[2 + 2 * i] + 1j * theta[3 + 2 * i]) for i in range(3)]


def residuals_from(logs, vlog, a, masses_only=False):
    res = []
    for i, s in enumerate(SECTORS):
        sig = np.sqrt(DELM[s] ** 2 + a ** 2)
        w = 1 / sig ** 2
        c = np.sum(w * (LOGM[s] - logs[i])) / np.sum(w)            # the scale, profiled
        res += list((logs[i] + c - LOGM[s]) / sig)
    if not masses_only:
        res += list((vlog - LOGV) / np.sqrt(DELV ** 2 + a ** 2))
    return np.array(res)


def residuals(theta, a, masses_only=False):
    tau = reduce(complex(theta[0], theta[1]))
    fp, fm = forms_at(tau)
    logs, vlog = raw_observables(fp, fm, rhos_of(theta))
    return residuals_from(logs, vlog, a, masses_only)


def shape10(tau, rhos):
    fp, fm = forms_at(tau)
    logs, vlog = raw_observables(fp, fm, rhos)
    return np.concatenate([l[:2] - l[2] for l in logs] + [vlog])


# ------------------------------------------------------------------------------------------------------------- M0
def M0():
    out = {}
    fp, fm = FP_RAW(0.13 + 1.21j), FM_RAW(0.13 + 1.21j)
    a_ok = (len(FORMS["T (x) T"][3]) == 2 and BY_PIECE["O+ at k = 3"] == 1 and BY_PIECE["O- at k = 3"] == 1
            and BY_PIECE["D at k = 3"] == 0
            and np.linalg.norm(fp - fp.T) < 1e-10 * np.linalg.norm(fp)
            and np.linalg.norm(fm + fm.T) < 1e-10 * np.linalg.norm(fm)
            and np.max(np.abs(np.diag(fp))) < 1e-10 * np.max(np.abs(fp))
            and np.max(np.abs(np.diag(fm))) < 1e-10 * np.max(np.abs(fm)))
    out["(a) one O+ form and one O- form at k = 3, symmetric / antisymmetric, zero diagonal"] = bool(a_ok)

    names, U = GM.units()
    named, _ = H.triplets()
    C = named["T"]
    _, _, xs, ell, lhat, _, _ = GM.M1(C, U)
    Ct = GM.t_basis(C, xs, ell, lhat)
    A, Tm = PG.rho_T(Ct)
    dev = max(float(np.linalg.norm(A @ A.conj().T - np.eye(3))), float(np.linalg.norm(Tm @ Tm.conj().T - np.eye(3))))
    out["(b) rho_T(S), rho_T(T) unitary: the largest |X X^H - 1|"] = dev

    rng = np.random.default_rng(5301)
    worst = 0.0
    for _ in range(5):
        tau = complex(rng.uniform(-0.25, 0.25), rng.uniform(1.0, 1.08))
        rhos = [np.exp(rng.uniform(np.log(0.1), np.log(10)) + 1j * rng.uniform(0, 2 * np.pi)) for _ in range(3)]
        base = shape10(tau, rhos)
        for t2 in (tau + 1, -1 / tau):
            worst = max(worst, float(np.max(np.abs(shape10(t2, rhos) - base))))
    out["(c) the shape observables at tau + 1 and -1/tau: the largest difference"] = worst

    def obs13(p):
        tau = complex(p[0], p[1])
        fp_, fm_ = forms_at(tau)
        rhos = [p[5] + 1j * p[6], p[7] + 1j * p[8], p[9] + 1j * p[10]]
        logs, vlog = raw_observables(fp_, fm_, rhos)
        return np.concatenate([logs[i] + p[2 + i] for i in range(3)] + [vlog])

    ranks, gaps = [], []
    for _ in range(3):
        p0 = np.array([rng.uniform(-0.4, 0.4), rng.uniform(1.05, 1.6)] + list(rng.normal(size=3) * 0.3)
                      + list(rng.normal(size=6)))
        J = np.zeros((13, 11))
        for i in range(11):
            e = np.zeros(11)
            e[i] = 1e-6
            J[:, i] = (obs13(p0 + e) - obs13(p0 - e)) / 2e-6
        s = np.linalg.svd(J, compute_uv=False)
        r = int(sum(s > 1e-6 * s[0]))
        ranks.append(r)
        gaps.append([float(s[r - 1] / s[0]), float(s[r] / s[0]) if r < len(s) else None])
    out["(d) the 13 x 11 Jacobian's rank at three random points"] = ranks
    out["(d) its smallest kept and largest dropped singular values over the largest"] = gaps

    w52 = json.loads((HERE / "the_free_numbers_counted.json").read_text(encoding="utf-8"))
    alone = {"T (x) T": {1}, "Sym^2 T": {1, 3}}
    rows, e_ok = {}, True
    for key, v in w52["C2: the scan"].items():
        frame, ks = key.split(": ")
        ks = tuple(int(x) for x in ks.strip("()").split(", "))
        if any(k in alone[frame] for k in ks):
            continue
        want = 11 if key == "T (x) T: (3, 3, 3)" else 13
        rows[key] = v["ranks at three points"]
        e_ok &= v["ranks at three points"] == [want] * 3
    out["(e) W52's assignments without an O+-alone sector: their recorded ranks"] = rows
    out["(e) holds"] = bool(e_ok)
    ok = (a_ok and dev < 1e-10 and worst < 1e-8 and ranks == [11, 11, 11] and e_ok)
    return out, bool(ok)


# ----------------------------------------------------------------------------------------------- stage 1: the grid
def grid():
    pts = []
    for y in np.geomspace(0.87, YMAX, 28):
        for x in np.linspace(-0.5, 0.5, 21):
            if abs(complex(x, y)) >= 1 - 1e-12:
                pts.append(complex(float(x), float(y)))
    return pts


R_STARTS = [(np.log(m), ph) for m in np.logspace(-2, 2, 9) for ph in 2 * np.pi * np.arange(8) / 8]


def ratio_res(p, fp, fm, target):
    u = float(np.clip(p[0], -30, 30))                              # |rho| kept finite on the unbounded LM path
    sv = np.sort(np.linalg.svd(fp + np.exp(u + 1j * p[1]) * fm, compute_uv=False))
    return np.log(np.maximum(sv[:2], 1e-300)) - np.log(sv[2]) - target


def sector_minima(fp, fm, target, keep=3):
    found = []
    for p0 in R_STARTS:
        r = least_squares(ratio_res, np.array(p0), args=(fp, fm, target), method="lm", xtol=1e-14, ftol=1e-14,
                          gtol=1e-14, max_nfev=400)
        found.append((float(np.linalg.norm(r.fun)), float(np.clip(r.x[0], -30, 30)), float(np.mod(r.x[1], 2 * np.pi))))
    found.sort()
    kept = []
    for f in found:
        rho = np.exp(f[1] + 1j * f[2])
        if all(abs(rho - np.exp(k[1] + 1j * k[2])) > 1e-4 * (1 + abs(rho)) for k in kept):
            kept.append(f)
        if len(kept) == keep:
            break
    return kept


def stage1(pts):
    rows = []
    for n, tau in enumerate(pts):
        fp, fm = forms_at(tau)
        mins = {s: sector_minima(fp, fm, TARGET[s]) for s in SECTORS}
        per = {s: [(sector(fp, fm, np.exp(u + 1j * v)), (u, v)) for _, u, v in mins[s]] for s in SECTORS}
        row = {"tau": tau, "sector residual": {s: mins[s][0][0] for s in SECTORS},
               "sector best": {s: mins[s][0][1:] for s in SECTORS}}
        # masses only: the sectors decouple at a fixed tau
        mo = 0.0
        for s in SECTORS:
            best = None
            for (U, sv), _ in per[s]:
                sig = np.sqrt(DELM[s] ** 2 + A_MAIN ** 2)
                w = 1 / sig ** 2
                ls = np.log(np.maximum(sv, 1e-300))
                c = np.sum(w * (LOGM[s] - ls)) / np.sum(w)
                chi = float(np.sum(((ls + c - LOGM[s]) / sig) ** 2))
                best = chi if best is None or chi < best else best
            mo += best
        row["masses only"] = mo
        for a in (A_MAIN,) + A_EXTRA:
            best = (np.inf, None)
            for iu in range(len(per["u"])):
                for idd in range(len(per["d"])):
                    for ie in range(len(per["e"])):
                        (Uu, su), pu = per["u"][iu]
                        (Ud, sd), pd = per["d"][idd]
                        (_, se), pe = per["e"][ie]
                        V = Uu.conj().T @ Ud
                        vlog = np.log(np.maximum([abs(V[i, j]) for _, i, j in CKM_KEYS], 1e-300))
                        logs = [np.log(np.maximum(x, 1e-300)) for x in (su, sd, se)]
                        chi = float(np.sum(residuals_from(logs, vlog, a) ** 2))
                        if chi < best[0]:
                            best = (chi, [tau.real, tau.imag, pu[0], pu[1], pd[0], pd[1], pe[0], pe[1]])
            row[a] = best
        rows.append(row)
        if n % 50 == 0:
            log(f"stage 1: {n + 1} of {len(pts)} grid points")
    return rows


# --------------------------------------------------------------------------------------------- stage 2: refinement
LB = [-0.5, H0, -12, -50, -12, -50, -12, -50]
UB = [0.5, YMAX, 12, 50, 12, 50, 12, 50]


def clip_start(th):
    th = np.array(th, dtype=float)
    return np.clip(th, np.array(LB) + 1e-9, np.array(UB) - 1e-9)


def refine(fun, starts):
    out = []
    for th in starts:
        r = least_squares(fun, clip_start(th), bounds=(LB, UB), method="trf", xtol=1e-12, ftol=1e-12, gtol=1e-12,
                          max_nfev=1500)
        out.append((float(np.sum(r.fun ** 2)), [float(x) for x in r.x]))
    out.sort(key=lambda t: t[0])
    return out


def random_starts(n=200, seed=5300):
    rng = np.random.default_rng(seed)
    st = []
    for _ in range(n):
        th = [rng.uniform(-0.5, 0.5), float(np.exp(rng.uniform(np.log(0.87), np.log(YMAX))))]
        for _ in SECTORS:
            th += [rng.uniform(np.log(0.01), np.log(100)), rng.uniform(0, 2 * np.pi)]
        st.append(th)
    return st


def describe(theta, a, masses_only=False):
    tau = reduce(complex(theta[0], theta[1]))
    fp, fm = forms_at(tau)
    rhos = rhos_of(theta)
    logs, vlog = raw_observables(fp, fm, rhos)
    res = residuals_from(logs, vlog, a, masses_only)
    labels = LABELS if not masses_only else LABELS[:9]
    model = {}
    for i, s in enumerate(SECTORS):
        model[f"m_{NAMES[s][0]}/m_{NAMES[s][2]}"] = float(np.exp(logs[i][0] - logs[i][2]))
        model[f"m_{NAMES[s][1]}/m_{NAMES[s][2]}"] = float(np.exp(logs[i][1] - logs[i][2]))
    for (k, _, _), v in zip(CKM_KEYS, vlog):
        model[f"|{k}|"] = float(np.exp(v))
    return {"chi^2": float(np.sum(res ** 2)), "tau (reduced)": [tau.real, tau.imag],
            "distance from i": abs(tau - 1j), "distance from omega": min(abs(tau - w) for w in OMEGAS),
            "rho (modulus, phase)": [[float(abs(r)), float(np.angle(r))] for r in rhos],
            "pulls": {l: float(x) for l, x in zip(labels, res)}, "the model's ratios and |V|": model}


def objective(a, masses_only):
    return lambda th: residuals(th, a, masses_only)


def run_objective(rows, key, a, masses_only, rnd):
    ranked = sorted(rows, key=lambda r: r[key][0] if isinstance(r[key], tuple) else r[key])
    grid_starts = []
    for r in ranked[:60]:
        if masses_only:
            th = [r["tau"].real, r["tau"].imag]
            for s in SECTORS:
                th += list(r["sector best"][s])
        else:
            th = r[key][1]
        grid_starts.append(th)
    res = refine(objective(a, masses_only), grid_starts + rnd)
    best = res[0]
    reach = sum(1 for c, _ in res if c < best[0] + 0.1)
    d = describe(best[1], a, masses_only)
    d["starts reaching it (within 0.1)"] = reach
    d["starts"] = len(res)
    return d, best


def F1(rows):
    out, ok = {}, True
    for s in SECTORS:
        ranked = sorted(rows, key=lambda r: r["sector residual"][s])[:30]
        sols = []
        for r in ranked:
            th = [r["tau"].real, r["tau"].imag] + list(r["sector best"][s])

            def fun(p, s=s):
                tau = reduce(complex(p[0], p[1]))
                fp, fm = forms_at(tau)
                return ratio_res(p[2:], fp, fm, TARGET[s])

            lb, ub = [-0.5, H0, -12, -50], [0.5, YMAX, 12, 50]
            x0 = np.clip(np.array(th, dtype=float), np.array(lb) + 1e-9, np.array(ub) - 1e-9)
            q = least_squares(fun, x0, bounds=(lb, ub), method="trf", xtol=1e-15, ftol=1e-15, gtol=1e-15,
                              max_nfev=2000)
            tau = reduce(complex(q.x[0], q.x[1]))
            sols.append((float(np.linalg.norm(q.fun)), [tau.real, tau.imag]))
        sols.sort(key=lambda t: t[0])
        exact = [t for c, t in sols if c < 1e-6]
        out[s] = {"the smallest residual": sols[0][0], "its tau": sols[0][1], "exact solutions found": len(exact),
                  "their y (sorted)": sorted(round(t[1], 4) for t in exact)}
        ok &= sols[0][0] < 1e-6
    return out, bool(ok)


def F4():
    tau = 5j
    fp, fm = forms_at(tau)
    mods = np.logspace(-3, 3, 601)
    phases = 2 * np.pi * np.arange(1440) / 1440
    ph = np.exp(1j * phases)
    in_win, best = [], (np.inf, None)
    for m in mods:
        rho = m * ph
        Y = fp[None, :, :] + rho[:, None, None] * fm[None, :, :]
        sv = np.sort(np.linalg.svd(Y, compute_uv=False), axis=1)
        r1, r2 = sv[:, 0] / sv[:, 2], sv[:, 1] / sv[:, 2]
        sel = (r2 >= 0.005) & (r2 <= 0.05)
        in_win += list(r1[sel])
        j = int(np.argmin(r2))
        if r2[j] < best[0]:
            best = (float(r2[j]), [float(m), float(phases[j])])
    in_win = np.array(in_win)
    q4 = float(np.exp(-2 * np.pi * 5 / 4))
    out = {"points in the window": int(len(in_win)),
           "m1/m3 over the window: min, max": [float(in_win.min()), float(in_win.max())] if len(in_win) else None,
           "q^(1/4) at 5i": q4, "kappa q^(1/4) from the rule (2.755 q^(1/4))": 2.755 * q4,
           "the grid's smallest m2/m3 and its rho (modulus, phase)": [best[0], best[1]]}
    ok = len(in_win) >= 20 and in_win.min() >= 0.95e-3 and in_win.max() <= 1.20e-3
    return out, bool(ok)


def bands(rows):
    edges = [(0.87, 1.5), (1.5, 2.5), (2.5, 3.5), (3.5, 4.5), (4.5, YMAX + 1e-9)]
    out = {}
    for lo, hi in edges:
        sel = [r for r in rows if lo <= r["tau"].imag < hi]
        if sel:
            b = min(sel, key=lambda r: r[A_MAIN][0])
            out[f"y in [{lo}, {min(hi, YMAX)}]"] = {"best chi^2 (a = 0.10)": b[A_MAIN][0],
                                                    "at tau": [b["tau"].real, b["tau"].imag],
                                                    "best masses-only chi^2": min(r["masses only"] for r in sel)}
    return out


def main():
    m0, ok0 = M0()
    log(f"M0 done: {ok0}")
    f4, ok4 = F4()
    log(f"F4 done: {ok4}")
    pts = grid()
    log(f"stage 1 over {len(pts)} grid points")
    rows = stage1(pts)
    f1, ok1 = F1(rows)
    log(f"F1 done: {ok1}")
    rnd = random_starts()
    fits = {}
    for name, key, a, mo in (("masses only, a = 0.10", "masses only", A_MAIN, True),
                             ("13 observables, a = 0.10", A_MAIN, A_MAIN, False),
                             ("13 observables, a = 0.05", 0.05, 0.05, False),
                             ("13 observables, a = 0.20", 0.20, 0.20, False)):
        fits[name], _ = run_objective(rows, key, a, mo, rnd)
        log(f"{name}: chi^2_min = {fits[name]['chi^2']:.6g}")
    chi_main = fits["13 observables, a = 0.10"]["chi^2"]
    chi_mass = fits["masses only, a = 0.10"]["chi^2"]
    cells = {
        "M0: the controls": ok0,
        "F1: each sector alone is reachable (its two ratios to 1e-6)": ok1,
        "F2: the masses-only chi^2_min at a = 0.10 exceeds 5.99": chi_mass > THRESH,
        "F3: the fit, chi^2_min <= 5.99 at a = 0.10": chi_main <= THRESH,
        "F4: at tau = 5i, m1/m3 in [0.95, 1.20] x 1e-3 over the window (at least 20 points)": ok4,
    }
    priors = {"M0": 0.97, "F1": 0.85, "F2": 0.70, "F3": 0.10, "F4": 0.75}
    leaned = {k: bool(v) == (priors[k.split(":")[0]] > 0.5) for k, v in cells.items()}
    out = {"status": "W53: the fit at the geometry's weight (the rule and its data first; one run)",
           "data used": USED,
           "the running allowance a: the verdict's, and the extras": [A_MAIN, list(A_EXTRA)],
           "M0": m0, "F1": f1, "F4": f4,
           "the fits (global minimum found)": fits,
           "consistency: the 13-observable minimum is not below the masses-only minimum (a = 0.10)": bool(
               chi_main >= chi_mass - 1e-6),
           "extra: the grid's best by band of y": bands(rows),
           "extra: the grid's best chi^2 (a = 0.10) and masses-only chi^2": [
               min(r[A_MAIN][0] for r in rows), min(r["masses only"] for r in rows)],
           "cells (as worded)": {k: bool(v) for k, v in cells.items()},
           "priors": priors,
           "each cell went the way its prior leaned": leaned,
           "every cell went the way its prior leaned": bool(all(leaned.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells (as worded)"], indent=1))
    print("every cell went the way its prior leaned:", out["every cell went the way its prior leaned"])


if __name__ == "__main__":
    main()
