import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "rerun"))
import numpy as np
from search import Model, make_copies, local_min
from model import eigs_from
m = Model(make_copies(5, "Z", "N", "sup"), 0.3, 0.003, 1.0)
rng = np.random.default_rng(1)
best = None
for k in range(40):
    S = rng.normal(size=3) + 1j * rng.normal(size=3)
    tau, Sf, v, r = local_min(m, complex(0.0065, 11.38), S)
    if best is None or v < best[0]:
        best = (v, tau, Sf)
v, tau, S = best
print("best V", v, "tau", tau, "S", np.round(S, 6))
A, D, W = m.pieces(tau)
for i in range(5):
    b2 = abs(W[i] @ S) ** 2
    print(" copy", i + 1, m.copies[i].name, "a2 %.3e d2 %.3e b2 %.3e |W| %.3e" % (A[i], D[i], b2, np.linalg.norm(W[i])), "eigs", np.round(eigs_from(A[i], D[i], b2), 6))
