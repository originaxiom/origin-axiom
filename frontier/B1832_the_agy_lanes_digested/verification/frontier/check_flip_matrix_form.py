"""Matrix form of the flip lemma (main's b1656_funcs): find constant U, V with Y(h; u^flip) = U Y(Ph; u) V for all (h, u)
(u^flip: u_i -> -u_i; P = diag(-1, 1, 1)), or with a transpose.  U solves U A_k = A'_k U for A_k = Y_k Y_1^{-1} (Sylvester nullspace)."""
import sys, pathlib, json
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _main_frame import B
Bf = B(); QS = [Bf.QI, Bf.QJ, Bf.QK]; P = np.diag([-1.0, 1, 1]); KEYS = list(Bf.UNITS); rng = np.random.default_rng(23)
def Y(h, u): return Bf.coupling(sum(h[k] * QS[k] for k in range(3)), Bf.weighted_M(u))
def sample():
    u = {s: complex(*rng.normal(size=2)) for s in KEYS}; uf = dict(u); uf["i"] = -u["i"]; h = rng.normal(size=3) + 1j * rng.normal(size=3)
    return Y(h, uf), Y(P @ h, u)
res = {}
for transpose in (False, True):
    S = [sample() for _ in range(5)]
    tgt = [a for a, b in S]; src = [(b.T if transpose else b) for a, b in S]
    rows = []
    for k in range(1, 5):
        A = src[k] @ np.linalg.inv(src[0]); Ap = tgt[k] @ np.linalg.inv(tgt[0])
        rows.append(np.kron(np.eye(3), A.T) - np.kron(Ap, np.eye(3)))     # vec_row(U A - A' U) = 0
    Mtx = np.vstack(rows); _, sv, Vh = np.linalg.svd(Mtx); U = Vh[-1].conj().reshape(3, 3)
    V = np.linalg.inv(U @ src[0]) @ tgt[0]
    dev = 0.0
    for _ in range(50):
        a, b = sample(); bb = b.T if transpose else b
        dev = max(dev, np.abs(a - U @ bb @ V).max() / np.abs(a).max())
    Un = U / np.abs(U).max(); Vn = V / np.abs(V).max()
    res["transpose" if transpose else "plain"] = {"smallest_sv": sv[-1], "second_sv": sv[-2], "dev_50_samples": dev, "U": np.round(Un, 6).tolist(), "V": np.round(Vn, 6).tolist()}
    print("%s: nullspace sv %.1e (next %.1e); Y(h;u^flip) = U Y(Ph;u)%s V on 50 fresh samples: max rel dev %.1e" % ("transpose" if transpose else "plain", sv[-1], sv[-2], "^T" if transpose else "", dev))
    print("   U ~", np.round(Un, 3).tolist()); print("   V ~", np.round(Vn, 3).tolist())
json.dump(res, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1, default=str); print("exit 0")
