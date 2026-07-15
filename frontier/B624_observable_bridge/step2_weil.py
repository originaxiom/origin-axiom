"""Step 2: build the B620/B621 Weil-coset term table for word RRL and try
to match TrW, Tr(Cm W) (b238 model) against combinations of the twelve
signed-Weyl terms tt[(pm,wi)]."""
import importlib.util
import os
import numpy as np

HERE = "/Users/dri/origin-axiom/frontier/B238_su32_levelrank"
spec = importlib.util.spec_from_file_location("b238", os.path.join(HERE, "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)

# ---- copy B620/B621 Weil machinery verbatim ----
S1 = np.array([[-1, 0], [1, 1]])
S2m = np.array([[1, 1], [0, -1]])
WEYL = []
for word in ((), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)):
    M = np.eye(2, dtype=int)
    for g in word:
        M = (S1 if g == 0 else S2m) @ M
    WEYL.append((M, (-1) ** len(word)))

def ip_weight(u, v):
    return (2.0 * (u[..., 0] * v[..., 0] + u[..., 1] * v[..., 1])
            + (u[..., 0] * v[..., 1] + u[..., 1] * v[..., 0])) / 3.0

def build_G(kap):
    U = np.array([[0, -1], [1, 2]])
    Uinv = np.array([[2, 1], [-1, 0]])
    reps, index = [], {}
    for c1 in range(kap):
        for c2 in range(3 * kap):
            mu = Uinv @ np.array([c1, c2])
            index[(c1, c2)] = len(reps)
            reps.append(mu)
    reps = np.array(reps)
    def canon(mu):
        c = U @ mu
        return (int(c[0]) % kap, int(c[1]) % (3 * kap))
    return reps, index, canon

def weil_ops(kap):
    reps, index, canon = build_G(kap)
    n = len(reps)
    q = ip_weight(reps, reps)
    T = np.exp(1j * np.pi * q / kap)
    pair = ip_weight(reps[:, None, :], reps[None, :, :])
    S = np.exp(-2j * np.pi * pair / kap) / np.sqrt(n)
    assert np.allclose(S @ S.conj().T, np.eye(n), atol=1e-6)
    perms = {}
    for pm in (1, -1):
        for wi, (Wm, sg) in enumerate(WEYL):
            P = np.zeros((n, n))
            for i, mu in enumerate(reps):
                P[index[canon(pm * (Wm @ mu))], i] = 1.0
            perms[(pm, wi)] = (P, sg)
    Pm1 = perms[(-1, 0)][0]
    assert np.allclose(S @ S, Pm1, atol=1e-5), f"S^2 != parity at kap={kap}"
    return T, S, perms, n

def rho_weil(word, T, S):
    n = S.shape[0]
    Sinv = S.conj().T
    Rop = np.diag(T)
    Lop = Sinv @ np.diag(T).conj() @ S
    M = np.eye(n, dtype=complex)
    for ch in word:
        M = M @ (Rop if ch == 'R' else Lop)
    return M

def term_table(word, kap):
    T, S, perms, n = weil_ops(kap)
    M = rho_weil(word, T, S)
    out = {}
    for key, (P, sg) in perms.items():
        out[key] = np.trace(M @ P)
    return out


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
    prs = sorted({(min(a, b), max(a, b)) for (a, b) in w if a != b})
    U = np.zeros((n, len(prs)))
    for j, (a, b) in enumerate(prs):
        U[w.index((a, b)), j] = 1 / np.sqrt(2)
        U[w.index((b, a)), j] = -1 / np.sqrt(2)
    Bodd = -(U.T @ W @ U)
    return np.trace(Bodd), np.trace(W), np.trace(Cm @ W)


for kap in (4, 5, 6, 8, 12, 16, 20, 24):
    k = kap - 3
    tr_odd, TrW, TrCmW = odd_form_and_full(k, "RRL")
    tt = term_table("RRL", kap)
    # (1/6) sum over pm=+1 branch, signed by wi
    sum_p1 = sum(sg * tt[(1, wi)] for wi, (Wm, sg) in enumerate(WEYL)) / 6.0
    sum_m1 = sum(sg * tt[(-1, wi)] for wi, (Wm, sg) in enumerate(WEYL)) / 6.0
    print(f"kappa={kap:>3}  TrW(b238)={TrW: .6f}   (1/6)Σ_{{+1}} sign*tt = {sum_p1: .6f}  "
          f"ratio={ (TrW/sum_p1) if abs(sum_p1)>1e-9 else float('nan') }")
    print(f"           TrCmW(b238)={TrCmW: .6f}   (1/6)Σ_{{-1}} sign*tt = {sum_m1: .6f}  "
          f"ratio={ (TrCmW/sum_m1) if abs(sum_m1)>1e-9 else float('nan') }")
