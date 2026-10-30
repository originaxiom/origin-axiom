import sys, pathlib, random
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "rerun"))
import numpy as np, mpmath as mp
import step_a_v2 as S2
from search import Model, make_copies
from model import LINV, PMAT, unit
mp.mp.dps = 34
rng = random.Random(5)
model = Model(make_copies(4, "H"), 0.5, 0.005, 0.3)
for _ in range(3):
    tau = mp.mpc(rng.uniform(-0.45, 0.45), rng.uniform(0.95, 1.7))
    S = unit(np.array([complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(3)]))
    print("tau", mp.nstr(tau, 8), "norms", np.linalg.norm(S) - 1, np.linalg.norm(LINV @ S) - 1, np.linalg.norm(PMAT @ S) - 1)
    for c in model.copies:
        mm = Model([c], 0.5, 0.005, 0.3)
        e = lambda t, s: S2.MPModel(mm, t, s).eigs([mp.mpf(0)] * 6)
        e0 = e(tau, S)
        dT = max(abs(a / b - 1) for a, b in zip(e(tau + 1, LINV @ S), e0)); dS = max(abs(a / b - 1) for a, b in zip(e(-1 / tau, PMAT @ S), e0))
        print("  ", c.name, mp.nstr(dT, 3), mp.nstr(dS, 3))
