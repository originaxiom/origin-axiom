"""Synthetic frames for the generator's tests (data-free): the refined grid's points, and a steep smooth frame with every
row's outputs moving several sigma per cell."""
import pathlib, sys
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import stepb_core as C
from census_io import line_key

MAIN = [(round(0.05 * i, 4), round(1.0 + 0.05 * k, 4)) for i in range(11) for k in range(61)]
SUB = sorted({(round(0.025 * i, 4), round(1.0 + 0.025 * k, 4)) for i in range(21) for k in range(21)} - set(MAIN))
PTS = MAIN + SUB



def steep_frame(slope=16.0, seed=0, n_lines=1):
    rng = np.random.default_rng(seed); lines = [line_key("2/5", "1/10"), line_key("1/3", "0")][:n_lines]
    cfg, d, r, k, m, v, J, vd, L, tau = [], [], [], [], [], [], [], [], [], []
    a = rng.normal(0, 1, (2, 10)); b = rng.normal(0, 1, (2, 10)); c = rng.normal(0, 1, (2, 10))
    for ln in lines:
        for (x, y) in PTS:
            ci = len(L); L.append(ln); tau.append((x, y))
            for dd in (0, 1):
                logs = -4.0 + 0.3 * a[dd] + slope * 0.1 * b[dd] * np.sin(3 * y) + 2.0 * c[dd] * x
                vals = np.exp(np.clip(logs, -14, -0.05))
                mm = np.sort(vals[:6].reshape(3, 2), axis=1)
                cfg.append(ci); d.append(dd); r.append(0); k.append(0); m.append(mm); v.append(vals[6:9]); J.append(vals[9]); vd.append(True)
    return C.Census(cfg=np.array(cfg), d=np.array(d), r=np.array(r), k=np.array(k), m=np.array(m), v=np.array(v), J=np.array(J),
                    vdef=np.array(vd), lines=L, tau=np.array(tau))
