"""EXPLORATION (P-168/P-175/P-177; data SEEN, a scoreboard). A search one can trust: per (variant, line) N local fits
(trust-region least squares in log space, 5% floor) from mixed starts — half near-null Higgs S = u v^T + 0.05 X (the
hierarchy's basin), half generic — in parallel (multiprocessing). Variants: 'same' (one S for all), 'tilde' (up sees
eps conj(S) eps^T), 'bar' (up sees conj(S)). Reports per line the best chi2, how many starts reach within 1% of it
(the basin's hit rate: a low rate means the minimum may still be missed), and the best point's ratios."""
import json, math, os, pathlib, sys
import numpy as np
from multiprocessing import Pool
from scipy.optimize import least_squares
HERE = pathlib.Path(__file__).resolve().parent
def load():
    src = (HERE / "joint_census2.py").read_text(encoding="utf-8"); sys.argv = ["x", "5", "1"]
    NS = {"__file__": str(HERE / "joint_census2.py"), "__name__": "jc2"}
    exec(compile(src.split("out = []")[0], "jc2", "exec"), NS); return NS
NS = load(); Yof, Ms, DATA, TGT = NS["Yof"], NS["Ms"], NS["DATA"], NS["TGT"]
CMIN = {ln: min(float(min(NS["PARTS"][ln][s][0])) for s in ("up", "down", "lep")) for ln in DATA}
EP = np.array([[0, 1], [-1, 0]], dtype=complex)
CONJ = {"same": lambda S: S, "tilde": lambda S: EP @ S.conj() @ EP.T, "bar": lambda S: S.conj()}
def svs(var, S, ln, L):
    return {s: np.linalg.svd(Yof(CONJ[var](S) if s == "up" else S, Ms(ln, s, L)), compute_uv=False) for s in ("up", "down", "lep")}
def unpack(p): return (p[0:4] + 1j*p[4:8]).reshape(2, 2), math.exp(p[8])
def resid(p, var, ln):
    S, L = unpack(p)
    if 2*np.pi*L + CMIN[ln] <= 0.5: return np.full(5, 1e3)
    q = svs(var, S, ln, L)
    return np.array([(math.log(max(q[s][k]/q[s][0], 1e-300)) - mu)/sg for s, k, (mu, sg) in TGT])
def one(job):
    var, ln, seed = job; rng = np.random.default_rng(seed)
    if seed % 2:
        u, v = rng.normal(size=2) + 1j*rng.normal(size=2), rng.normal(size=2) + 1j*rng.normal(size=2)
        S = np.outer(u, v) + 0.05*(rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)))
    else:
        S = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
    p0 = np.concatenate([S.real.ravel(), S.imag.ravel(), [math.log(10**rng.uniform(0.4, 3.0))]])
    try:
        r = least_squares(resid, p0, args=(var, ln), method="trf", max_nfev=600, xtol=1e-12, ftol=1e-12, gtol=1e-12)
        from scipy.optimize import minimize                  # the polish inside the worker (Nelder-Mead found minima trf missed)
        f = lambda p: float(np.sum(resid(p, var, ln)**2))
        m = minimize(f, r.x, method="Nelder-Mead", options={"maxiter": 6000, "xatol": 1e-10, "fatol": 1e-12})
        return var, ln, float(m.fun), m.x.tolist()
    except Exception:
        return var, ln, float("inf"), None
if __name__ == "__main__":
    NST = int(os.environ.get("NST", "300")); VARS = os.environ.get("VARS", "same,tilde,bar").split(",")
    lines = sorted(DATA)[::int(os.environ.get("STRIDE", "1"))]
    jobs = [(v, ln, 1000*i + k) for v in VARS for i, ln in enumerate(lines) for k in range(NST)]
    with Pool(14) as pool: res = pool.map(one, jobs, chunksize=8)
    out = {}
    for v in VARS:
        for ln in lines:
            rs = sorted([r for r in res if r[0] == v and r[1] == ln], key=lambda r: r[2]); best = rs[0]
            hit = sum(1 for r in rs if r[2] <= best[2]*1.01 + 1e-9)
            S, L = unpack(np.array(best[3])); q = svs(v, S, ln, L)
            out.setdefault(v, []).append({"line": list(ln), "chi2": best[2], "hits": hit, "n": len(rs), "L": L, "x": best[3],
                                          "ratios": {s: [q[s][1]/q[s][0], q[s][2]/q[s][0]] for s in q}})
            print(f"[{v}] {ln[0]:.3f},{ln[1]:.3f} best chi2 {best[2]:8.2f} (hits {hit}/{len(rs)}) L {L:7.2f} "
                  + "  ".join(f"{s}:{q[s][1]/q[s][0]:.3e}/{q[s][2]/q[s][0]:.2e}" for s in q), flush=True)
    json.dump(out, open(HERE / "joint_multistart.json", "w"), indent=1, default=float)
    print("targets:", [(s, k, round(math.exp(mu), 7)) for s, k, (mu, sg) in TGT])
