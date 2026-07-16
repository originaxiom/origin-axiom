"""Step 1: verify trace(B_odd) = -(1/2)[Tr(W) - Tr(Cm W)] as an exact
identity in the b238 (Kac-Peterson weight-simplex) model, for word RRL."""
import importlib.util
import os
import numpy as np

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "..", "B238_su32_levelrank")
spec = importlib.util.spec_from_file_location("b238", os.path.join(HERE, "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)


def odd_form_and_full(level, word):
    w, S, T, cc = b238.su3_data(level)
    n = len(w)
    Cm = np.zeros((n, n))
    for i, wt in enumerate(w):
        Cm[w.index((wt[1], wt[0])), i] = 1.0
    R = T
    L = np.linalg.inv(S) @ np.linalg.inv(T) @ S
    W = np.eye(n, dtype=complex)
    for ch in word:
        W = W @ (R if ch == "R" else L)
    assert np.allclose(Cm @ W, W @ Cm, atol=1e-9)
    prs = sorted({(min(a, b), max(a, b)) for (a, b) in w if a != b})
    U = np.zeros((n, len(prs)))
    for j, (a, b) in enumerate(prs):
        U[w.index((a, b)), j] = 1 / np.sqrt(2)
        U[w.index((b, a)), j] = -1 / np.sqrt(2)
    Bodd = -(U.T @ W @ U)
    return Bodd, W, Cm


for kap in (4, 5, 6, 8, 12, 16, 20, 24):
    k = kap - 3
    Bodd, W, Cm = odd_form_and_full(k, "RRL")
    tr_odd = np.trace(Bodd)
    TrW = np.trace(W)
    TrCmW = np.trace(Cm @ W)
    pred = -0.5 * (TrW - TrCmW)
    ok = abs(tr_odd - pred) < 1e-8
    print(f"kappa={kap:>3}  tr_odd={tr_odd: .6f}  -(1/2)(TrW-TrCmW)={pred: .6f}  match={ok}")
