import numpy as np, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("weighted_M","UNITS","np","EDUAL"): globals()[k] = ns[k]
rng = np.random.default_rng(2)
worst = 0
for _ in range(1000):
    u = {s: complex(*rng.normal(size=2)) for s in UNITS}
    M = weighted_M(u); worst = max(worst, abs(np.linalg.det(M) - sum(v*v for v in u.values())/4)/abs(sum(v*v for v in u.values())/4))
print("det M' = (1/4) sum u_s^2: worst rel err %.2e (1000 random u)" % worst)
