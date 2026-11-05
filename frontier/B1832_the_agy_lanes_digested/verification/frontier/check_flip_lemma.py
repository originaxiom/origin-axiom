"""Universal form of the lepton-down relation behind agy's G2 (data-free; main's b1656_funcs): for ARBITRARY channel weights u,
is sv(coupling(S(h), M(u with u_i -> -u_i))) = sv(coupling(S(Ph), M(u))), P = diag(-1, 1, 1)?  And is the stronger
coupling(S(h), M(u^flip)) = U coupling(S(Ph), M(u)) V with fixed U, V?  Then on any line where R^lep = zeta (R_1, -R_i, R_j, R_k)^down
(and c_s is sector-blind, B1826), Y_lep(h) has the singular values of Y_down(Ph) for every Higgs h."""
import sys, pathlib, json
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _main_frame import B
Bf = B(); QS = [Bf.QI, Bf.QJ, Bf.QK]; P = np.diag([-1.0, 1, 1]); rng = np.random.default_rng(5); KEYS = list(Bf.UNITS)
worst, worst_plain = 0.0, np.inf
for _ in range(200):
    u = {s: complex(*rng.normal(size=2)) for s in KEYS}; uf = dict(u); uf["i"] = -u["i"]
    h = rng.normal(size=3) + 1j * rng.normal(size=3)
    S = lambda v: sum(v[k] * QS[k] for k in range(3))
    a = np.linalg.svd(Bf.coupling(S(h), Bf.weighted_M(uf)), compute_uv=False)
    b = np.linalg.svd(Bf.coupling(S(P @ h), Bf.weighted_M(u)), compute_uv=False)
    c = np.linalg.svd(Bf.coupling(S(h), Bf.weighted_M(u)), compute_uv=False)
    worst = max(worst, np.abs(a - b).max() / a.max()); worst_plain = min(worst_plain, np.abs(a - c).max() / a.max())
# fixed-unitary form: Y(h, u^flip) =? D1 Y(Ph, u) D2 with D = diag(+-1) acting on generations (try all sign patterns)
best = None
for s1 in range(8):
    for s2 in range(8):
        D1 = np.diag([(-1) ** ((s1 >> k) & 1) for k in range(3)]); D2 = np.diag([(-1) ** ((s2 >> k) & 1) for k in range(3)]); dev = 0
        for _ in range(20):
            u = {s: complex(*rng.normal(size=2)) for s in KEYS}; uf = dict(u); uf["i"] = -u["i"]; h = rng.normal(size=3) + 1j * rng.normal(size=3)
            dev = max(dev, np.abs(Bf.coupling(sum(h[k] * QS[k] for k in range(3)), Bf.weighted_M(uf)) - D1 @ Bf.coupling(sum((P @ h)[k] * QS[k] for k in range(3)), Bf.weighted_M(u)) @ D2).max())
        if best is None or dev < best[0]: best = (dev, np.diag(D1).tolist(), np.diag(D2).tolist())
print("sv(Y(h, u^flip)) vs sv(Y(Ph, u)), 200 random (u, h): max rel dev %.1e; control sv(Y(h, u^flip)) vs sv(Y(h, u)): min rel dev %.2e" % (worst, worst_plain))
print("best signed-permutation-free form Y(h,u^flip) = D1 Y(Ph,u) D2: dev %.1e with D1 = %s, D2 = %s" % best)
json.dump({"sv_flip_max_rel_dev": worst, "control_min": worst_plain, "D1D2": best}, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
print("exit 0")
