"""EXPLORATION (P-168; data SEEN — a scoreboard). Is the one-Higgs census's search reliable at the data's hierarchy?
(1) fit the data on 3 representative lines (multistart: trf + Nelder-Mead polish per worker, mixed near-null/generic
starts); (2) PLANT a world at each best point (the model's own ratios there: as hierarchical as the data); (3) rerun the
same search from fresh starts against the planted ratios: recovery (chi2 -> 0) shows the search can find data-like
minima. 8 workers, single-threaded BLAS (the owner's machine is shared)."""
import json, math, os, pathlib, sys
import numpy as np
from multiprocessing import Pool
HERE = pathlib.Path(__file__).resolve().parent
sys.argv = ["x"]
src = (HERE / "joint_multistart.py").read_text(encoding="utf-8").split('if __name__ == "__main__":')[0]
NS = {"__file__": str(HERE / "joint_multistart.py"), "__name__": "jm"}; exec(compile(src, "jm", "exec"), NS)
svs, unpack, DATA, TGT, CMIN, least_squares = NS["svs"], NS["unpack"], NS["DATA"], NS["TGT"], NS["CMIN"], NS["least_squares"]
from scipy.optimize import minimize
VAR = os.environ.get("VARIANT", "same")
KEYS = [(s, k) for s, k, _ in TGT]; SIG = {(s, k): sg for s, k, (mu, sg) in TGT}
def resid(p, ln, mus):
    S, L = unpack(p)
    if 2*np.pi*L + CMIN[ln] <= 0.5: return np.full(5, 1e3)
    q = svs(VAR, S, ln, L)
    return np.array([(math.log(max(q[s][k]/q[s][0], 1e-300)) - mus[(s, k)])/SIG[(s, k)] for s, k in KEYS])
def fit(job):
    ln, mus, seed = job; rng = np.random.default_rng(seed)
    if seed % 2:
        u, v = rng.normal(size=2) + 1j*rng.normal(size=2), rng.normal(size=2) + 1j*rng.normal(size=2)
        S = np.outer(u, v) + 0.05*(rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)))
    else:
        S = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
    p0 = np.concatenate([S.real.ravel(), S.imag.ravel(), [math.log(10**rng.uniform(0.4, 3.0))]])
    try:
        r = least_squares(resid, p0, args=(ln, mus), method="trf", max_nfev=600)
        m = minimize(lambda p: float(np.sum(resid(p, ln, mus)**2)), r.x, method="Nelder-Mead", options={"maxiter": 6000, "xatol": 1e-10, "fatol": 1e-12})
        return float(m.fun), m.x.tolist()
    except Exception:
        return float("inf"), None
def search(pool, ln, mus, n, base):
    res = pool.map(fit, [(ln, mus, base + k) for k in range(n)], chunksize=4)
    res = sorted([r for r in res if r[1] is not None]); best = res[0][0]
    return best, sum(1 for r in res if r[0] <= best*1.05 + 1e-6), len(res), res[0][1]
if __name__ == "__main__":
    N = int(os.environ.get("NST", "120")); lines = sorted(DATA)[::6]
    DMU = {(s, k): mu for s, k, (mu, sg) in TGT}; out = []
    with Pool(8) as pool:
        for i, ln in enumerate(lines):
            b, hit, n, x = search(pool, ln, DMU, N, 100000*i)
            S, L = unpack(np.array(x)); q = svs(VAR, S, ln, L)
            planted = {(s, k): math.log(q[s][k]/q[s][0]) for s, k in KEYS}
            pb, phit, pn, _ = search(pool, ln, planted, N, 100000*i + 50000)
            rec = {"line": list(ln), "data_chi2": b, "data_hits": f"{hit}/{n}", "planted_ratios": {f"{s}{k}": math.exp(v) for (s, k), v in planted.items()},
                   "planted_best_chi2": pb, "planted_hits": f"{phit}/{pn}"}
            out.append(rec)
            print(f"{ln[0]:.3f},{ln[1]:.3f}: data chi2 {b:.2f} (within 5%: {hit}/{n}); planted at that point -> recovered chi2 {pb:.2e} (within 5%: {phit}/{pn}); planted ratios "
                  + ", ".join(f"{s}{k} {math.exp(v):.2e}" for (s, k), v in planted.items()), flush=True)
    json.dump(out, open(HERE / f"joint_reliable_{VAR}.json", "w"), indent=1, default=float)
