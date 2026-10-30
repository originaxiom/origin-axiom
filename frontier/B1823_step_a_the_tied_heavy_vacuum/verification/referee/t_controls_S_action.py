"""A control the draft's invariance test lacks: the right couplings with the WRONG action on S_hat (L instead of L^-1 under
T; S untransformed under T or S).  If the test is sensitive to the action on S these must fail.  The draft's own MPModel."""
import sys, pathlib, json, random
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "rerun"))
import numpy as np, mpmath as mp
import step_a_v2 as S2
from search import Model, make_copies
from model import LINV, LMAT, PMAT, unit
mp.mp.dps = 34
rng = random.Random(5)
out = {}
for menu in ("Z", "H"):
    model = Model(make_copies(4, menu), 0.5, 0.005, 0.3)
    worst = {"right (L^-1, P)": 0.0, "T with L": 0.0, "T with S unchanged": 0.0, "S-move with S unchanged": 0.0}
    for _ in range(3):
        tau = mp.mpc(rng.uniform(-0.45, 0.45), rng.uniform(0.95, 1.7))
        S = unit(np.array([complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(3)]))
        for c in model.copies:
            mm = Model([c], 0.5, 0.005, 0.3)
            e = lambda t, s: S2.MPModel(mm, t, s).eigs([mp.mpf(0)] * 6)
            e0 = e(tau, S)
            dev = lambda e1: max(abs(a / b - 1) for a, b in zip(e1, e0))
            worst["right (L^-1, P)"] = max(worst["right (L^-1, P)"], dev(e(tau + 1, LINV @ S)), dev(e(-1 / tau, PMAT @ S)))
            worst["T with L"] = max(worst["T with L"], dev(e(tau + 1, LMAT @ S)))
            worst["T with S unchanged"] = max(worst["T with S unchanged"], dev(e(tau + 1, S)))
            worst["S-move with S unchanged"] = max(worst["S-move with S unchanged"], dev(e(-1 / tau, S)))
    out["menu_" + menu] = {k: float(v) for k, v in worst.items()}
    print(menu, out["menu_" + menu], flush=True)
(HERE / "t_controls_S_action.json").write_text(json.dumps(out, indent=1))
