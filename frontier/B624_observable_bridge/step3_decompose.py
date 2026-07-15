"""Step 3: verify the bridge formula
   trace(B_odd) = -(phi/12) * sum_{pm,wi} sign(wi) tt(pm,wi)
with phi = omega^{-(nR-nL)} = omega^2 for RRL (nR-nL=1),
and decompose into REFL (wi in {1,2,5}, both pm) vs OTHER (wi in {0,3,4}),
looking at the sqrt(3) content of each half and the cancellation pattern
at kappa = 4,8,12,16,20,24 (4 | kappa in all these; 3 | kappa only at 12,24).
"""
import importlib.util
import os
import math
from fractions import Fraction
import numpy as np

HERE = "/Users/dri/origin-axiom/frontier/B238_su32_levelrank"
spec = importlib.util.spec_from_file_location("b238", os.path.join(HERE, "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)

S1 = np.array([[-1, 0], [1, 1]])
S2m = np.array([[1, 1], [0, -1]])
WEYL = []
for word in ((), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)):
    M = np.eye(2, dtype=int)
    for g in word:
        M = (S1 if g == 0 else S2m) @ M
    WEYL.append((M, (-1) ** len(word)))
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

def term_table(word, kap):
    T, S, perms, n = weil_ops(kap)
    M = rho_weil(word, T, S)
    return {key: np.trace(M @ P) for key, (P, sg) in perms.items()}

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

def fit(x, root=3, den_max=48, tol=1e-7):
    """fit x (real) = a + b*sqrt(root), a,b rational, small denominators."""
    s = math.sqrt(root)
    for db in range(1, den_max + 1):
        for nb in range(-6 * db, 6 * db + 1):
            b = nb / db
            a = x - b * s
            fa = Fraction(a).limit_denominator(den_max)
            if abs(float(fa) - a) < tol:
                return (fa, Fraction(nb, db))
    return None

omega = complex(math.cos(2 * math.pi / 3), math.sin(2 * math.pi / 3))
phi_word = omega ** (-1)   # RRL: nR-nL = 2-1 = 1

print("word = RRL   phi = omega^(-1) =", phi_word)
print(f"{'kap':>4} {'3|kap':>6} {'trace(B_odd)':>24} {'pred (-phi/12)ΣsignTt':>26} {'match':>6}   "
      f"{'REFL-sum (both pm)':>22} {'OTHER-sum (both pm)':>22}")
for kap in (4, 8, 12, 16, 20, 24):
    k = kap - 3
    tro = odd_trace(k, "RRL")
    tt = term_table("RRL", kap)
    full = sum(sg * tt[(pm, wi)] for pm in (1, -1) for wi, (Wm, sg) in enumerate(WEYL))
    pred = -(phi_word / 12) * full
    refl_sum = sum(tt[(pm, wi)] for pm in (1, -1) for wi in (1, 2, 5))   # sign=-1 each, folded into pred formula
    other_sum = sum(tt[(pm, wi)] for pm in (1, -1) for wi in (0, 3, 4))
    ok = abs(tro - pred) < 1e-7
    print(f"{kap:>4} {str(kap % 3 == 0):>6} {tro: .9f}      {pred: .9f}   {str(ok):>6}   "
          f"{refl_sum: .6f}      {other_sum: .6f}")
    # field part of trace(B_odd) = +(phi/12)*refl_sum  (since sign=-1 folds the minus away)
    field_part = (phi_word / 12) * refl_sum
    print(f"      field part = (phi/12)*REFL-sum = {field_part: .9f}   "
          f"|field part| = {abs(field_part):.6f}")
    # per-pm reflection sums
    r_p1 = sum(tt[(1, wi)] for wi in (1, 2, 5))
    r_m1 = sum(tt[(-1, wi)] for wi in (1, 2, 5))
    print(f"      REFL(pm=+1) sum = {r_p1: .6f}   REFL(pm=-1) sum = {r_m1: .6f}   "
          f"sum(+1)+conj? diff={abs(r_p1-np.conj(r_m1)):.4f} sameornot(r_p1==r_m1)={np.allclose(r_p1,r_m1,atol=1e-6)}")
