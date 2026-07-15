"""Independent verification of seat cc2's level-ladder headline:
Z_k = Tr rho_k(A1) at E6 levels 1..4 — my own pipeline (the c3 vectorized
Kac-Peterson builder generalized to any level); gates: N(k) = 3, 9, 20, 42;
Z_1..3 = +1 (banked); the claim: Z_4 = 0 and Tr(Theta rho_4) = 0."""
import importlib.util
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "c3", os.path.join(HERE, "..", "B570_allowed_plays", "c3_e6_level2_monodromy.py"))
c3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c3)

# comarks in c3's node ordering (chain 0-2-3-4-5, branch 1 on 3): (1,2,2,3,2,1)
COMARK = [1, 2, 2, 3, 2, 1]
HV = 12

W, eps = c3.weyl_group()
rho_w = c3.root_coords([1] * 6)

def level_weights(k):
    out = []
    def rec(prefix, rem):
        i = len(prefix)
        if i == 6:
            out.append(tuple(prefix))
            return
        for v in range(rem // COMARK[i] + 1):
            rec(prefix + [v], rem - COMARK[i] * v)
    rec([], k)
    return out

for k in (1, 2, 3, 4):
    prim = level_weights(k)
    N = len(prim)
    KH = k + HV
    shifted = [c3.root_coords(p) + rho_w for p in prim]
    S = np.zeros((N, N), dtype=complex)
    Wl = np.einsum('wij,lj->wli', W.astype(float), np.array(shifted))
    for a in range(N):
        for b in range(a, N):
            ips = Wl[:, a, :] @ (c3.C @ shifted[b])
            S[a, b] = S[b, a] = np.sum(eps * np.exp(-2j * np.pi * ips / KH))
    S /= np.sqrt((S @ S.conj().T)[0, 0].real)
    if S[0, 0].real < 0:
        S = -S
    ipf = lambda x, y: float(x @ (c3.C @ y))
    cc = k * 78 / KH
    hs = [ipf(c3.root_coords(p), c3.root_coords(p) + 2 * rho_w) / (2 * KH)
          for p in prim]
    T = np.diag([np.exp(2j * np.pi * (h - cc / 24)) for h in hs])
    # gate: two words agree
    r1 = T @ T @ S @ T
    r2 = T @ S @ np.linalg.inv(T) @ np.linalg.inv(S)
    agree = np.linalg.norm(r1 - r2)
    Z = np.trace(r1)
    theta_perm = np.zeros((N, N))
    for i, p in enumerate(prim):
        theta_perm[prim.index(c3.theta(p)), i] = 1.0
    ZT = np.trace(theta_perm @ r1)
    n_odd = sum(1 for p in prim if c3.theta(p) != p) // 2 * 1
    print(f"k={k}: N={N:3d}  words-agree={agree:.1e}  Z={Z:+.10f}  "
          f"Tr(Theta rho)={ZT:+.10f}  odd-pairs={n_odd}")
print("expected: N = 3, 9, 20, 42; Z = +1, +1, +1, 0; Tr(Theta rho_4) = 0")
