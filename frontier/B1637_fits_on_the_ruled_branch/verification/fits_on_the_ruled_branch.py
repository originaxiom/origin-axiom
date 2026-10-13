#!/usr/bin/env python3
"""B1637 -- DOES ANY MODULAR STRUCTURE ON THE RULED BRANCH FIT THE CHARGED FERMIONS WITH ONE tau?  Main's own check of the SM
seat's W53 (the (3, 3, 3) structure fails: chi2_min 1887 on the 13, 163 on the 9 masses) and of its open question (does
any weight assignment fit at all?).  Main's own forms (B1635's polynomials in theta squares, eta^18 cleared, the cusp
condition; general T (x) T at each weight), main's own fast theta series, main's own optimizer (scipy least squares, multi-
start over the fundamental domain); the seat's conventions for the observables (they are what is checked):
  Y_s(tau) = sum_j c_sj Fhat_j(tau), Fhat = F / ||F||_Frobenius at tau, c_s1 = 1, the other c_sj complex; masses = the
  singular values (ascending), mixing V = U_u^H U_d from the left singular vectors (ascending): V_us = V12, V_cb = V23,
  V_ub = V13, V_td = V31; z_i = (log O_i - log O_i^data) / sqrt(delta_i^2 + a^2), a = 0.10 (0.05, 0.20 reported); each
  sector's scale profiled (its weighted mean); chi2 = sum z^2.  The observables are invariant under the weave (the forms
  transform by one unitary on both sectors and a scalar), so tau is searched in the fundamental domain, y <= 10.
 F2  (3, 3, 3): chi2_min on the 9 masses and on all 13.
 F3  (3, 3, 3), each sector alone (its 3 masses, its own tau): the best Im tau of each.
 F4  every assignment (k_u, k_d, k_e) in {3, 5, 7}^3 (general T (x) T, dims 2, 4, 5): P = 2 + sum (2 d - 1) and chi2_min on
     the 9 masses and on all 13.
 F5  the smallest P among assignments with chi2_min(13) <= 13.
Data: received/HZ2021_running_masses_MZ.json (checked against the source PDF before the seal, sha256 baeddc97...), and B1612's
PDG 2025 CKM (|V_us|, |V_cb|, |V_ub|, |V_td|).  Writes fits_on_the_ruled_branch.json."""
import json, pathlib, os, sys, importlib.util, itertools, math
sys.dont_write_bytecode = True
import numpy as np
from scipy.optimize import least_squares
from multiprocessing import Pool
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = pathlib.Path(os.environ.get("OA_FRONTIER", HERE.parents[1]))
spec = importlib.util.spec_from_file_location("c35", FRONTIER / "B1635_couplings_on_the_ruled_branch" / "verification" / "couplings_on_the_ruled_branch.py")
c35 = importlib.util.module_from_spec(spec); spec.loader.exec_module(c35)
inv = np.linalg.inv
MASS = json.load(open(HERE.parent / "received" / "HZ2021_running_masses_MZ.json"))["masses_GeV"]
CKM = json.load(open(FRONTIER / "B1612_the_mixing_patterns_the_weave_fixes" / "verification" / "data.json"))["ckm_abs"]
SECT = {"u": ("u", "c", "t"), "d": ("d", "s", "b"), "e": ("e", "mu", "tau")}
LOGM = {s: np.log([MASS["value"][f] for f in SECT[s]]) for s in SECT}
DLM = {s: np.array([MASS["sigma"][f] / MASS["value"][f] for f in SECT[s]]) for s in SECT}
CK_IDX = [(0, 1), (1, 2), (0, 2), (2, 0)]                       # V_us, V_cb, V_ub, V_td
LOGV = np.log([CKM["value"][i][j] for i, j in CK_IDX])
DLV = np.array([CKM["sigma"][i][j] / CKM["value"][i][j] for i, j in CK_IDX])
NSTART = int(os.environ.get("B1637_STARTS", "60"))


def forms(k):
    full, mons, _ = c35.equivariant_space(k + 9, lambda A: inv(A).T, lambda A: inv(A))
    hol = c35.cusp_condition(full, mons, 6)
    return hol, mons


FORMS = {}


def theta_eta(t, N=40):
    q = np.exp(1j * np.pi * t)
    n = np.arange(N)
    th2 = 2 * np.sum(q ** ((n + 0.5) ** 2))
    th3 = 1 + 2 * np.sum(q ** ((n[1:]) ** 2))
    th4 = 1 + 2 * np.sum(((-1.0) ** n[1:]) * q ** ((n[1:]) ** 2))
    eta = np.exp(1j * np.pi * t / 12) * np.prod(1 - q ** (2 * np.arange(1, 4 * N)))
    return np.array([th2 ** 2, th3 ** 2, th4 ** 2]), eta


def basis_at(k, t):
    hol, mons = FORMS[k]
    u, eta = theta_eta(t)
    vals = np.array([u[0] ** m[0] * u[1] ** m[1] * u[2] ** m[2] for m in mons])
    Ys = [(b @ vals) / eta ** 18 for b in hol]
    return [Y / np.linalg.norm(Y) for Y in Ys]


def sector_matrix(k, t, coeffs):
    B = basis_at(k, t)
    Y = B[0].copy()
    for cj, Bj in zip(coeffs, B[1:]): Y = Y + cj * Bj
    return Y


def unpack(p, ks):
    t = complex(p[0], p[1]); out = {}; i = 2
    for s, k in zip("ude", ks):
        d = len(FORMS[k][0]); n = d - 1
        out[s] = p[i:i + n] + 1j * p[i + n:i + 2 * n]; i += 2 * n
    return t, out


def residual(p, ks, a, use_ckm, sectors="ude"):
    t, co = unpack(p, ks)
    res = []; U = {}
    for s, k in zip("ude", ks):
        if s not in sectors: continue
        Y = sector_matrix(k, t, co[s])
        Us, sv, _ = np.linalg.svd(Y)
        order = np.argsort(sv); sv = sv[order]; U[s] = Us[:, order]
        lm = np.log(np.maximum(sv, 1e-300))
        sig = np.sqrt(DLM[s] ** 2 + a ** 2)
        w = 1 / sig ** 2; shift = np.sum(w * (LOGM[s] - lm)) / np.sum(w)     # the profiled scale
        res.extend(((lm + shift) - LOGM[s]) / sig)
    if use_ckm:
        V = U["u"].conj().T @ U["d"]
        lv = np.log(np.maximum([abs(V[i, j]) for i, j in CK_IDX], 1e-300))
        res.extend((lv - LOGV) / np.sqrt(DLV ** 2 + a ** 2))
    return np.array(res)


def nparams(ks):
    """the fitted parameters (tau and the coefficient shapes); the three sector scales are profiled on top"""
    return 2 + sum(2 * (len(FORMS[k][0]) - 1) for k in ks)


def P_total(ks):
    """the structure's real parameters, 2 + sum (2 d - 1): the fitted ones plus the three profiled scales"""
    return nparams(ks) + 3


def fit(ks, a=0.10, use_ckm=True, sectors="ude", seed=0):
    rng = np.random.default_rng(seed)
    n = nparams(ks); best = (np.inf, None)
    xs = [-0.4, -0.2, 0.0, 0.2, 0.4]; ys = [1.0, 1.6, 2.5, 3.5, 5.0, 7.0]
    starts = [(x, y) for x in xs for y in ys]
    lo = np.full(n, -np.inf); hi = np.full(n, np.inf); lo[0], hi[0], lo[1], hi[1] = -0.5, 0.5, 0.5, 10.0
    for st in range(NSTART):
        x, y = starts[st % len(starts)]
        p0 = np.concatenate([[x, max(y, 0.5) if y > 0.5 else 0.6], rng.normal(scale=1.5, size=n - 2)])
        if abs(p0[0]) ** 2 + p0[1] ** 2 < 1: p0[1] = math.sqrt(1 - p0[0] ** 2) + 0.05
        try:
            r = least_squares(residual, p0, bounds=(lo, hi), args=(ks, a, use_ckm, sectors), max_nfev=400 * n, x_scale="jac")
        except Exception:
            continue
        chi2 = float(np.sum(r.fun ** 2))
        if chi2 < best[0]: best = (chi2, r.x.tolist())
    return best


def task(args):
    ks, a, use_ckm, sectors, seed = args
    chi2, p = fit(ks, a, use_ckm, sectors, seed)
    t = (p[0], p[1]) if p else None
    return {"ks": list(ks), "a": a, "ckm": use_ckm, "sectors": sectors, "P": P_total(ks), "chi2_min": chi2, "tau": t}


def init():
    for k in (3, 5, 7): FORMS[k] = forms(k)


def main():
    init()
    out = {"dims": {str(k): len(FORMS[k][0]) for k in FORMS}, "nstart": NSTART}
    jobs = []
    for a in (0.05, 0.10, 0.20):
        jobs += [((3, 3, 3), a, False, "ude", 1), ((3, 3, 3), a, True, "ude", 2)]
    for s in "ude": jobs.append(((3, 3, 3), 0.10, False, s, 3))
    for ks in itertools.product((3, 5, 7), repeat=3):
        jobs += [(ks, 0.10, False, "ude", 4), (ks, 0.10, True, "ude", 5)]
    with Pool(int(os.environ.get("B1637_PROCS", "10")), initializer=init) as pool:
        res = pool.map(task, jobs)
    out["F2"] = [r for r in res if r["ks"] == [3, 3, 3] and r["sectors"] == "ude"]
    out["F3_each_sector_alone"] = [r for r in res if r["ks"] == [3, 3, 3] and r["sectors"] != "ude"]
    scan = [r for r in res if r["a"] == 0.10 and r["sectors"] == "ude" and not (r["ks"] == [3, 3, 3] and r in out["F2"] and False)]
    out["F4_scan_a0.10"] = sorted([r for r in scan if r["a"] == 0.10], key=lambda r: (r["ckm"], r["P"], r["chi2_min"]))
    fits13 = [r for r in scan if r["ckm"] and r["chi2_min"] <= 13]
    out["F5"] = {"assignments_fitting_all_13": [(r["ks"], r["P"], round(r["chi2_min"], 3)) for r in fits13],
                 "smallest_P_that_fits": min((r["P"] for r in fits13), default=None)}
    json.dump(out, open(HERE / "fits_on_the_ruled_branch.json", "w"), indent=1, default=str)
    print(json.dumps({"F2": out["F2"], "F3": out["F3_each_sector_alone"], "F5": out["F5"]}, indent=1, default=str))


if __name__ == "__main__":
    main()
