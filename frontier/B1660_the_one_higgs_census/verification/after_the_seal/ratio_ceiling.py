"""POST-SEAL EXPLORATION (B1660's read-out; labelled, not a cell; kept in the arc at Review 64, first run from the draft room). The census's misses are the two middle ratios: the
data need (m_mu/m_tau)/(m_s/m_b) ~ 3.15 and the best fits give 0.6-1.75. That quantity reads only the down and lepton
sectors, so it is the same in all three readings. How large can it be on each line, over every Higgs S and L (with the
census's domain), with no other target? Multistart (40 starts per line, two seeds' worth), Nelder-Mead on -log R."""
import importlib.util, json, math, pathlib, sys
import numpy as np
from scipy.optimize import minimize
ROOT = next(d for d in pathlib.Path(__file__).resolve().parents if (d / "frontier").is_dir())
p = ROOT / "frontier/B1660_the_one_higgs_census/verification/the_one_higgs_census.py"
spec = importlib.util.spec_from_file_location("b1660", p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
hz = m.v_; data = (hz["mu"]/hz["tau"])/(hz["s"]/hz["b"])
picks = [0, 1, 5, 2]          # the 'same' classes 85.4, 87.3, 291.1, and the line of the 'bar' best (34.4)
full = m.LINES18; m.LINES18 = [full[i] for i in picks]; m.build(); m.LINES18 = full
def negR(p, ln):
    S, L = m.unpack(p)
    if 2*np.pi*L + m.CMIN[ln] <= 0.5 or L > 1e4: return 50.0
    q = m.svs("same", S, ln, L)
    return -(math.log(q["lep"][1]/q["lep"][0]) - math.log(q["down"][1]/q["down"][0]))
print(f"data (m_mu/m_tau)/(m_s/m_b) = {data:.3f}")
for i in picks:
    ln = full[i]; best = 0
    for seed in (11, 12):
        rng = np.random.default_rng(seed)
        for k in range(20):
            p0 = np.r_[rng.normal(size=8)*(0.05 if k % 2 else 1.0), math.log(10**rng.uniform(0.4, 3))]
            if k % 2: p0[[0, 4]] += 1.0
            r = minimize(negR, p0, args=(ln,), method="Nelder-Mead", options={"maxiter": 4000, "xatol": 1e-9, "fatol": 1e-12})
            best = max(best, math.exp(-r.fun))
    print(f"line {i:2d} {tuple(round(9*v) for v in ln)}/9: max over S, L of (mu/tau)/(s/b) found = {best:.3f}")
