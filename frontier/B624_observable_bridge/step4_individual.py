"""Step 4: individual (pm,wi) reflection-term values (wi in {1,2,5}) for
word RRL, at kappa=4,8,12,16,20,24 -- see the pairwise sqrt(3) cancellation
inside pm=+1 vs the constant pm=-1 (Cm-coset) contribution."""
import math
from fractions import Fraction
import numpy as np

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

def fit(x, root=3, den_max=48, tol=1e-7):
    s = math.sqrt(root)
    for db in range(1, den_max + 1):
        for nb in range(-6 * db, 6 * db + 1):
            b = nb / db
            a = x - b * s
            fa = Fraction(a).limit_denominator(den_max)
            if abs(float(fa) - a) < tol:
                return f"{fa}+{Fraction(nb,db)}*sqrt3"
    return "?"

print(f"{'kap':>4} {'wi':>3} {'tt(pm=+1,wi)':>28} {'fit':>18}   {'tt(pm=-1,wi)':>28} {'fit':>18}")
for kap in (4, 8, 12, 16, 20, 24):
    T, S, perms, n = weil_ops(kap)
    M = rho_weil("RRL", T, S)
    for wi in (1, 2, 5):
        vP = np.trace(M @ perms[(1, wi)][0])
        vM = np.trace(M @ perms[(-1, wi)][0])
        fP = f"{fit(vP.real)} + {fit(vP.imag)}i"
        fM = f"{fit(vM.real)} + {fit(vM.imag)}i"
        print(f"{kap:>4} {wi:>3} {vP: .6f}                 {fP:>18}   {vM: .6f}                 {fM:>18}")
    print()
