"""POST-SEAL EXPLORATION (B1660's read-out, P-175; labelled, not a cell). Drop the up quarks (as a separate Higgs for
them would): can one S and L fit the three down/lepton targets (s/b, d/b, mu/tau) on W59's lines? Same search as the
census (trust region + Nelder-Mead polish, half the starts near-null), 40 starts per line, four lines."""
import importlib.util, math, pathlib
import numpy as np
from scipy.optimize import least_squares, minimize
ROOT = next(d for d in pathlib.Path(__file__).resolve().parents if (d / "frontier").is_dir())
p = ROOT / "frontier/B1660_the_one_higgs_census/verification/the_one_higgs_census.py"
spec = importlib.util.spec_from_file_location("b1660", p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
picks = [0, 1, 5, 2]; full = m.LINES18; m.LINES18 = [full[i] for i in picks]; m.build(); m.LINES18 = full
KEYS3 = [k for k in m.KEYS if k[0] != "up"]
def res3(p, ln):
    S, L = m.unpack(p)
    if 2*np.pi*L + m.CMIN[ln] <= 0.5: return np.full(3, 1e3)
    q = m.svs("same", S, ln, L)
    return np.array([(math.log(max(q[s][k]/q[s][0], 1e-300)) - m.DMU[(s, k)])/m.SIG[(s, k)] for s, k in KEYS3])
for i in picks:
    ln = full[i]; best = (1e9, None); rng = np.random.default_rng(31 + i)
    for k in range(40):
        if k % 2:
            u, v = rng.normal(size=2) + 1j*rng.normal(size=2), rng.normal(size=2) + 1j*rng.normal(size=2)
            S0 = np.outer(u, v) + 0.05*(rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)))
        else:
            S0 = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
        p0 = np.r_[S0.real.ravel(), S0.imag.ravel(), math.log(10**rng.uniform(0.4, 3))]
        try:
            r = least_squares(res3, p0, args=(ln,), method="trf", max_nfev=600)
            mm = minimize(lambda q: float(np.sum(res3(q, ln)**2)), r.x, method="Nelder-Mead", options={"maxiter": 4000})
            c = float(mm.fun)
        except Exception:
            continue
        if c < best[0]: best = (c, mm.x)
    S, L = m.unpack(best[1]); q = m.svs("same", S, ln, L)
    print(f"line {i:2d} {tuple(round(9*v) for v in ln)}/9: down+lep chi2_min = {best[0]:.4g}  L {L:.3f}  "
          f"s/b {q['down'][1]/q['down'][0]:.4f} d/b {q['down'][2]/q['down'][0]:.2e} mu/tau {q['lep'][1]/q['lep'][0]:.4f}")
