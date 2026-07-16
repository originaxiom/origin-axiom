"""kappa-gating scan: reuse B620/B238 machinery, scan RL/RRL/RRRL over kappa=4..30
(capped where runtime too large), detect sqrt(base) content in the six
reflection Gauss-sum terms, print a bearing/silent table per word.
"""
import importlib.util
import os
import sys
import time
import math
from fractions import Fraction

import numpy as np

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "..", "B620_conductor_mechanism")
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(HERE, "..", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)

# --- copy the weil machinery (avoid re-running conductor_mechanism.py's prints) ---
S1 = np.array([[-1, 0], [1, 1]])
S2m = np.array([[1, 1], [0, -1]])
WEYL = []
for word in ((), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)):
    M = np.eye(2, dtype=int)
    for g in word:
        M = (S1 if g == 0 else S2m) @ M
    WEYL.append((M, (-1) ** len(word)))

R2 = np.array([[1, 1], [0, 1]])
L2 = np.array([[1, 0], [1, 1]])
def mono(word):
    M = np.eye(2, dtype=int)
    for ch in word:
        M = M @ (R2 if ch == 'R' else L2)
    return M

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

REFL = {1, 2, 5}

def term_table(word, T, S, perms):
    M = rho_weil(word, T, S)
    out = {}
    for key, (P, sg) in perms.items():
        out[key] = np.trace(M @ P)
    return out

def fit_sqrt(x, root, den_max=24, tol=1e-8):
    s = math.sqrt(root)
    for db in range(1, den_max + 1):
        for nb in range(-6 * db, 6 * db + 1):
            if nb == 0:
                continue
            b = nb / db
            a = x - b * s
            fa = Fraction(a).limit_denominator(den_max)
            if abs(float(fa) - a) < tol:
                return (fa, Fraction(nb, db))
    return None

WORDS = {"RL": 3, "RRL": 4, "RRRL": 5}

if __name__ == "__main__":
    kmax = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    results = {}
    for kap in range(4, kmax + 1):
        t0 = time.time()
        T, S, perms, n = weil_ops(kap)
        for word, tr_ in WORDS.items():
            base = tr_ ** 2 - 4
            tt = term_table(word, T, S, perms)
            refl_bearing = False
            for (pm, wi), v in tt.items():
                if wi not in REFL:
                    continue
                for part in (v.real, v.imag):
                    if abs(part) < 1e-8:
                        continue
                    f = fit_sqrt(part, base)
                    if f and f[1] != 0:
                        refl_bearing = True
            results[(word, kap)] = refl_bearing
        dt = time.time() - t0
        print(f"kap={kap:2d} n={n:5d}  " +
              "  ".join(f"{w}:{'BEAR' if results[(w,kap)] else 'sil '}" for w in WORDS) +
              f"   [{dt:.2f}s]", flush=True)

    print("\n--- summary ---")
    for word, tr_ in WORDS.items():
        base = tr_ ** 2 - 4
        bearing_kaps = [k for k in range(4, kmax + 1) if results[(word, k)]]
        print(f"{word} (t={tr_}, base={base}): bearing at kappa = {bearing_kaps}")
