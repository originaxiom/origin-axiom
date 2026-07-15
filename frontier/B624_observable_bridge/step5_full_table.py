"""Step 5: the full twelve-term table (identity, rotation x2, reflection x3,
each at pm=+1 and pm=-1) for word RRL at kappa=4,8,12,16,20,24, plus the
final assembled trace(B_odd) via the bridge formula, printed as a clean
verification table."""
import math
from fractions import Fraction
import numpy as np

S1 = np.array([[-1, 0], [1, 1]])
S2m = np.array([[1, 1], [0, -1]])
WEYL = []
NAMES = {}
for word in ((), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)):
    M = np.eye(2, dtype=int)
    for g in word:
        M = (S1 if g == 0 else S2m) @ M
    WEYL.append((M, (-1) ** len(word)))
WNAME = {0: "identity", 1: "refl(s1)", 2: "refl(s2)", 3: "rot(s2s1)", 4: "rot(s1s2)", 5: "refl(s1s2s1)=Cm-elt"}
REFL = {1, 2, 5}

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
    perms = {}
    for pm in (1, -1):
        for wi, (Wm, sg) in enumerate(WEYL):
            P = np.zeros((n, n))
            for i, mu in enumerate(reps):
                P[index[canon(pm * (Wm @ mu))], i] = 1.0
            perms[(pm, wi)] = (P, sg)
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

omega = complex(math.cos(2*math.pi/3), math.sin(2*math.pi/3))
phi_word = omega ** -1

import importlib.util, os
HERE = "/Users/dri/origin-axiom/frontier/B238_su32_levelrank"
spec = importlib.util.spec_from_file_location("b238", os.path.join(HERE, "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)

def odd_trace(level, word):
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
    return np.trace(Bodd)

for kap in (4, 8, 12, 16, 20, 24):
    T, S, perms, n = weil_ops(kap)
    M = rho_weil("RRL", T, S)
    print(f"=== kappa={kap}  (3|kappa: {kap%3==0}) ===")
    total = 0j
    for pm in (1, -1):
        for wi, (Wm, sg) in enumerate(WEYL):
            v = np.trace(M @ perms[(pm, wi)][0])
            tag = "REFL" if wi in REFL else "id/rot"
            total += sg * v
            print(f"   pm={pm:+d} wi={wi} [{WNAME[wi]:>15}] sign={sg:+d} ({tag:>6})  v = {v: .6f}")
    bridge_pred = -(phi_word / 12) * total
    direct = odd_trace(kap - 3, "RRL")
    print(f"   -> sum sign(wi)*v = {total: .6f};  bridge pred trace(B_odd) = {bridge_pred: .6f}")
    print(f"   -> direct trace(B_odd) (b238 model)               = {direct: .6f}   match={abs(bridge_pred-direct)<1e-7}")
    print()
