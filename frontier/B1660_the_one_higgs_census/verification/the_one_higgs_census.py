#!/usr/bin/env python3
"""B1660 -- THE ONE-HIGGS CENSUS UNDER THE CANONICAL END CONDITION (a scoreboard: the data were seen). In B1656's twisted
frame at tau = omega on W59's 18 lines, under P4 (u_s = sqrt(2 pi L + c_s) R_s, B1654/B1656), with B1659's joint law: can
ONE Higgs S in M2(C) (scale-free) and the end radius L reproduce the five non-electron mass ratios of HZ2021 at M_Z (up
m2/m3, m1/m3; down m2/m3, m1/m3; leptons m2/m3), in log space with a 5% floor (the frame is leading order)? Three
readings of the up sector: the same S ('same'), eps conj(S) eps^T ('tilde'), conj(S) ('bar'). The electron is massless on
these lines for every S and L (B1656) and is not a target.
  C0  plumbing: B1659's identities on the sector matter; the fast coupling equals B1656's
  C1  the search's reliability IN THE DATA'S REGIME, per reading: worlds planted at the census's own best point on lines
      0, 9 and 12 (0 and 12 of two classes, 9 the known multi-basin line), and two random data-like worlds (near-null S,
      up m1/m3 < 1e-4) on lines 0 and 9, are each recovered by the same search to chi2 < 0.1
  C2  the census: per line and reading, chi2_min over NST starts (trust region + Nelder-Mead polish, half the starts
      near-null). The statistic is chi2_min minimised over 7 effective parameters against 5 targets: NOT chi2_5-distributed;
      if the frame were true with Gaussian log-errors, chi2_min <= chi2 at the true point ~ chi2_5, so chi2_min > 11.07 is
      a conservative one-sided bound ('no fit below 11.07 found'); a cell whose best is reached by <= 2 starts is flagged
      unreliable rather than excluded
  C3  read-outs (no test): the best point's ratios, |det S|/||S||^2, L, the residual pattern
Multiprocessing with 8 workers (half of 16 cores: the owner's 50/50 rule; the machine is shared), single-threaded BLAS.
Fits are restricted to 2 pi L + c_s > 0.5 for every channel (real radicands). If interrupted, a rerun resumes from the
JSON, keeping completed cells (logged). Writes the_one_higgs_census.json and the_one_higgs_census_run.txt."""
import os
for k in ("OMP_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"): os.environ[k] = "1"
import json, math, pathlib, sys, time
import numpy as np
from multiprocessing import Pool
from scipy.optimize import least_squares, minimize
HERE = pathlib.Path(__file__).resolve().parent; ROOT = next(d for d in HERE.parents if (d / "frontier").is_dir())
OUT = HERE / "the_one_higgs_census.json"; RUN = HERE / "the_one_higgs_census_run.txt"
NST = 160; WORKERS = 8; FLOOR = 0.05; THRESH = 11.07; PLANT_LINES = (0, 9, 12); RANDOM_PLANT_LINES = (0, 9); MAXFAIL = 0.05
src = (ROOT / "frontier/B1656_the_electrons_zero/verification/the_electrons_zero.py").read_text(encoding="utf-8")
assert src.count("T0 = time.time()") == 1
NS = {"__file__": str(HERE / "b1656_head_namespace.py"), "__name__": "b1656_head"}
exec(compile(src.split("T0 = time.time()")[0], "b1656_head", "exec"), NS)
OM, line_w, sector_twists, residues, weighted_M, coupling, SIXY, SECTORS, cA, UNITS, EDUAL, BLOCKS, EPS = (NS[k] for k in (
    "OM", "line_w", "sector_twists", "residues", "weighted_M", "coupling", "SIXY", "SECTORS", "cA", "UNITS", "EDUAL", "BLOCKS", "EPS"))
LINES18 = [(b + i/3, b + j/3) for b in (1/9, 2/9) for i in range(3) for j in range(3)]
T = np.einsum('aki,bjl->abijkl', np.array([C.T @ EPS for C in BLOCKS]), np.array(BLOCKS)); KM = T.reshape(9, 16)
EP = np.array([[0, 1], [-1, 0]], dtype=complex)
CONJ = {"same": lambda S: S, "tilde": lambda S: EP @ S.conj() @ EP.T, "bar": lambda S: S.conj()}
hz = json.load(open(ROOT / "frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json"))["masses_GeV"]
v_, s_ = hz["value"], hz["sigma"]
def rr(a, b): r = v_[a]/v_[b]; return math.log(r), max(math.hypot(s_[a]/v_[a], s_[b]/v_[b]), FLOOR)
TGT = [("up", 1, rr("c", "t")), ("up", 2, rr("u", "t")), ("down", 1, rr("s", "b")), ("down", 2, rr("d", "b")), ("lep", 1, rr("mu", "tau"))]
KEYS = [(s, k) for s, k, _ in TGT]; SIG = {(s, k): sg for s, k, (mu, sg) in TGT}; DMU = {(s, k): mu for s, k, (mu, sg) in TGT}
PARTS = None; CMIN = None
def build():
    global PARTS, CMIN
    PARTS, CMIN = {}, {}
    for ln in LINES18:
        w = line_w(*ln, OM); PARTS[ln] = {}
        for sec, (fl, fr) in SECTORS.items():
            x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM); c = cA(x, y, OM, R, nth=64, ns=48)
            ks = [k for k in UNITS if c[k] is not None]
            PARTS[ln][sec] = (np.array([c[k] for k in ks], dtype=float), np.array([R[k]*EDUAL[k] for k in ks]))
        CMIN[ln] = min(float(PARTS[ln][s][0].min()) for s in PARTS[ln])
def init(parts, cmin):
    global PARTS, CMIN
    PARTS, CMIN = parts, cmin
def Ms(ln, sec, L): cs, E = PARTS[ln][sec]; return np.tensordot(np.sqrt(2*np.pi*L + cs), E, 1)
def Yof(S, M): return (KM @ np.kron(S.ravel(), M.ravel())).reshape(3, 3)
def svs(var, S, ln, L): return {s: np.linalg.svd(Yof(CONJ[var](S) if s == "up" else S, Ms(ln, s, L)), compute_uv=False) for s in ("up", "down", "lep")}
def unpack(p): return (np.asarray(p[0:4]) + 1j*np.asarray(p[4:8])).reshape(2, 2), math.exp(p[8])
def resid(p, var, ln, mus):
    S, L = unpack(p)
    if 2*np.pi*L + CMIN[ln] <= 0.5: return np.full(5, 1e3)
    q = svs(var, S, ln, L)
    return np.array([(math.log(max(q[s][k]/q[s][0], 1e-300)) - mus[(s, k)])/SIG[(s, k)] for s, k in KEYS])
def fit(job):
    try:
        return _fit(job)
    except Exception:
        return float("inf"), None
def _fit(job):
    var, li, mus, seed = job; ln = LINES18[li]; rng = np.random.default_rng(seed)
    if seed % 2:
        u, v = rng.normal(size=2) + 1j*rng.normal(size=2), rng.normal(size=2) + 1j*rng.normal(size=2)
        S = np.outer(u, v) + 0.05*(rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)))
    else:
        S = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
    p0 = np.concatenate([S.real.ravel(), S.imag.ravel(), [math.log(10**rng.uniform(0.4, 3.0))]])
    r = least_squares(resid, p0, args=(var, ln, mus), method="trf", max_nfev=600)
    m = minimize(lambda p: float(np.sum(resid(p, var, ln, mus)**2)), r.x, method="Nelder-Mead",
                 options={"maxiter": 6000, "xatol": 1e-10, "fatol": 1e-12})
    if not np.isfinite(m.fun): raise FloatingPointError((var, li, seed))
    return float(m.fun), m.x.tolist()
def say(*a):
    line = " ".join(str(x) for x in a); print(line, flush=True)
    with open(RUN, "a", encoding="utf-8") as fh: fh.write(line + "\n")
if __name__ == "__main__":
    T0 = time.time()
    RES = json.load(open(OUT)) if OUT.exists() else {"NST": NST, "floor": FLOOR, "threshold": THRESH}
    if not OUT.exists(): RUN.write_text("", encoding="utf-8")
    else: say(f"RESUMED from the JSON (completed cells kept): {sorted(RES.keys())}")
    def save(): RES["seconds"] = round(time.time() - T0, 1); json.dump(RES, open(OUT, "w"), indent=1, default=float)
    build()
    # C0
    rng = np.random.default_rng(1660); c0 = 0.0; EPSn = np.array([[0, 1], [-1, 0]], dtype=complex)
    for li in (0, 9):
        for sec in ("up", "down", "lep"):
            M = Ms(LINES18[li], sec, 30.0); S = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)); Y = Yof(S, M)
            c0 = max(c0, np.abs(Y - coupling(S, M)).max()/np.abs(Y).max(),
                     abs(np.linalg.det(Y) - 4*np.linalg.det(S)*np.linalg.det(M)*np.trace(EPSn @ S @ M.T))/np.linalg.norm(Y)**3)
    RES["C0"] = {"fast_vs_B1656_and_joint_law_max": c0, "holds": bool(c0 < 1e-12)}; say("C0", RES["C0"], f"[{time.time()-T0:.0f}s]"); save()
    assert RES["C0"]["holds"], "C0 failed: the run stops (a gate)"
    with Pool(WORKERS, initializer=init, initargs=(PARTS, CMIN)) as pool:
        census = RES.get("C2_partial", {})
        for var in ("same", "tilde", "bar"):
            census.setdefault(var, [])
            for li, ln in enumerate(LINES18):
                if li < len(census[var]): continue                                           # resume: completed cell
                res = pool.map(fit, [(var, li, DMU, 10**6*li + 1000*["same", "tilde", "bar"].index(var) + k) for k in range(NST)], chunksize=4)
                ok = sorted([r for r in res if r[1] is not None], key=lambda r: r[0]); nfail = NST - len(ok)
                assert nfail <= MAXFAIL*NST, f"too many failed fits ({nfail}) at {var} line {li}"
                best = ok[0]; S, L = unpack(best[1]); q = svs(var, S, ln, L)
                hits = sum(1 for r in ok if r[0] <= best[0]*1.05 + 1e-9)
                rec = {"line": list(ln), "chi2_min": best[0], "within_5pct": hits, "n_failed": nfail,
                       "reliable": bool(hits > 2), "no_fit_below_threshold": bool(best[0] > THRESH),
                       "excluded": bool(best[0] > THRESH and hits > 2), "x": best[1], "L": L,
                       "boundary_margin": 2*np.pi*L + CMIN[ln], "dS_rel": abs(np.linalg.det(S))/np.linalg.norm(S)**2,
                       "ratios": {s: [q[s][1]/q[s][0], q[s][2]/q[s][0]] for s in q},
                       "residuals": resid(best[1], var, ln, DMU).round(3).tolist()}
                census[var].append(rec)
                say(f"C2 [{var}] line {li:2d} ({ln[0]:.3f},{ln[1]:.3f}) chi2_min {best[0]:.3f} (within 5%: {hits}/{NST}; failed {nfail}) no fit below {THRESH}: {rec['no_fit_below_threshold']} reliable {rec['reliable']} [{time.time()-T0:.0f}s]")
                RES["C2_partial"] = census; save()
        c1 = RES.get("C1_partial", {})
        def plant(var, li, S, L, tag, base):
            ln = LINES18[li]; q = svs(var, S, ln, L); mus = {(s, k): math.log(q[s][k]/q[s][0]) for s, k in KEYS}
            res = pool.map(fit, [(var, li, mus, base + k) for k in range(NST)], chunksize=4)
            ok = [r for r in res if r[1] is not None]; best = min(r[0] for r in ok); n_rec = sum(1 for r in ok if r[0] < 0.1)
            say(f"C1 [{var}] line {li} {tag} plant -> best {best:.2e}, starts below 0.1: {n_rec}/{NST} [{time.time()-T0:.0f}s]")
            return {"line": li, "kind": tag, "planted_ratios": {f"{s}{k}": math.exp(v) for (s, k), v in mus.items()},
                    "recovered_chi2": best, "starts_below_0.1": n_rec, "n_failed": NST - len(ok)}
        for vi, var in enumerate(("same", "tilde", "bar")):
            c1.setdefault(var, [])
            jobs = [("census-best", li) for li in PLANT_LINES] + [("random data-like", li) for li in RANDOM_PLANT_LINES]
            for j, (tag, li) in enumerate(jobs):
                if j < len(c1[var]): continue                                                    # resume
                if tag == "census-best":
                    S, L = unpack(census[var][li]["x"])
                else:
                    prng = np.random.default_rng(9*10**8 + 10**5*vi + 1000*li)
                    for tries in range(100000):                                                  # a random near-null world as hierarchical as the data
                        u, v = prng.normal(size=2) + 1j*prng.normal(size=2), prng.normal(size=2) + 1j*prng.normal(size=2)
                        S = np.outer(u, v) + 10**prng.uniform(-3, -1)*(prng.normal(size=(2, 2)) + 1j*prng.normal(size=(2, 2)))
                        L = 10**prng.uniform(0.5, 2.5); q = svs(var, S, LINES18[li], L)
                        if q["up"][2]/q["up"][0] < 1e-4: break
                    else:
                        raise RuntimeError(f"no data-like random world found for {var} line {li}")
                c1[var].append(plant(var, li, S, L, tag, 10**8 + 10**7*vi + 10**5*li + 10**4*j))
                RES["C1_partial"] = c1; save()
    RES["C1"] = {"plants": c1, "holds_by_reading": {v: all(p["recovered_chi2"] < 0.1 for p in c1[v]) for v in c1}}
    RES["C1"]["holds"] = all(RES["C1"]["holds_by_reading"].values()); RES.pop("C1_partial", None)
    RES["C2"] = {"census": census, "excluded_lines": {v: sum(r["excluded"] for r in census[v]) for v in census},
                 "unreliable_cells": {v: [i for i, r in enumerate(census[v]) if not r["reliable"]] for v in census},
                 "no_fit_below_threshold_lines": {v: sum(r["no_fit_below_threshold"] for r in census[v]) for v in census},
                 "chi2_min_range": {v: [min(r["chi2_min"] for r in census[v]), max(r["chi2_min"] for r in census[v])] for v in census}}
    RES.pop("C2_partial", None)
    RES["C2"]["all_excluded"] = all(r["excluded"] for v in census.values() for r in v)
    say("C1", {"holds": RES["C1"]["holds"]}, "C2", {k: RES["C2"][k] for k in ("excluded_lines", "chi2_min_range", "all_excluded")}); save()
