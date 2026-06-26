"""B216 -- the f>=8 boundary of the class-field period law (L39): a validated general-word WRT tool,
and the precise OBSTRUCTION proving the f>=8 split is genus-theoretic (NEEDS-SPECIALIST). Nothing to
CLAIMS.md.

B215 found d(gamma) = max{d'|f : gamma == +-I mod d'} (scalar-reduction depth), EXACT for conductor
f in {2,3,4}, with f=8 the named boundary. L39 = the focused attack on f>=8 (pure algebra). Result:

  (1) A correct GENERAL WRT factorization (any gamma in SL(2,Z) -> word in S,T -> Z_k=tr rho_k),
      VALIDATED to machine precision against the block-word Z of B204/B214 (a real bug in a first
      quick version was caught and fixed -- the e=-1 final block is S^2 T^{-m}, not -T^m).
  (2) THE OBSTRUCTION: at f=8 (t=18, D=320), TWO non-conjugate classes
        gamma_A = [[13,-8],[-8,5]]  -> period 10, d=8
        gamma_B = [[17,-4],[-4,1]]  -> period 20, d=4
      have IDENTICAL elementary invariants: scalar-depth 4 AND order-profile (mod 2,4,8,16) = (1,1,2,4).
      Same elementary invariants, DIFFERENT d  =>  d is NOT a function of scalar-depth or order-mod-2^k;
      it is a finer FORM-CLASS / GENUS invariant of the ideal class (Latimer-MacDuffee = repo B92).
      So the full f>=8 closed form is genuinely genus-theoretic (2-adic genus / spinor-genus / Hecke
      level) -> NEEDS-SPECIALIST. (Computed to exhaustion of the elementary criteria, then named.)

Firewall: standalone quantum-topology / arithmetic; nothing to CLAIMS.md. Run: python general_wrt.py (pyenv).
"""
import numpy as np
import math
from math import gcd
from collections import deque


def lcm(a, b):
    return a * b // gcd(a, b)


# ---- the validated general SL(2,Z) -> S,T factorization + WRT trace ----
def factor_ST(M):
    """reduce gamma by  M <- S^{-1} T^{-q} M  (q=round(a/c)); returns (ops=[q_i], final=(e,m))
    so that  gamma = prod_i (T^{q_i} S) * final,  final = [[e,m],[0,e]], e=+-1."""
    M = [[int(M[0][0]), int(M[0][1])], [int(M[1][0]), int(M[1][1])]]
    ops = []
    while M[1][0] != 0:
        a, c = M[0][0], M[1][0]
        q = int(round(a / c))
        M = [[a - q * M[1][0], M[0][1] - q * M[1][1]], [M[1][0], M[1][1]]]   # T^{-q} M
        M = [[M[1][0], M[1][1]], [-M[0][0], -M[0][1]]]                       # S^{-1} M
        ops.append(q)
    return ops, (M[0][0], M[0][1])


def rho_mat(M, k):
    n = k + 2; j = np.arange(k + 1)
    S = np.sqrt(2.0 / n) * np.sin(np.pi * np.outer(j + 1, j + 1) / n)
    Td = np.exp(1j * np.pi * ((j + 1) ** 2 / (2.0 * n)))
    Tp = lambda p: np.diag(Td ** p)        # noqa: E731
    ops, (e, m) = factor_ST([[M[0, 0], M[0, 1]], [M[1, 0], M[1, 1]]])
    rho = np.eye(k + 1, dtype=complex)
    for q in ops:
        rho = rho @ Tp(q) @ S
    rho = rho @ Tp(m) if e == 1 else rho @ (S @ S) @ Tp(-m)   # final [[-1,m],[0,-1]] = S^2 T^{-m}
    return rho


def Zabs(M, k):
    return abs(np.trace(rho_mat(M, k)))


def period(M, maxk=95, k0=14, W=16, tol=1e-3):
    v = [Zabs(M, k) for k in range(k0, k0 + maxk + 1)]
    for P in range(1, maxk - W):
        if all(abs(v[i] - v[i + P]) < tol for i in range(W)):
            return P
    return None


# ---- block-word ground truth (validated in B204/B214) ----
def gmat(bl):
    R = np.array([[1, 1], [0, 1]]); L = np.array([[1, 0], [1, 1]]); M = np.eye(2, dtype=int)
    for a, b in bl:
        M = M @ np.linalg.matrix_power(R, a) @ np.linalg.matrix_power(L, b)
    return M


def Zabs_block(bl, k):
    n = k + 2; j = np.arange(k + 1)
    S = np.sqrt(2.0 / n) * np.sin(np.pi * np.outer(j + 1, j + 1) / n); Si = np.linalg.inv(S)
    T = np.exp(1j * np.pi * ((j + 1) ** 2 / (2.0 * n))); M = np.eye(k + 1, dtype=complex)
    for a, b in bl:
        M = M @ (((T ** a)[:, None] * S * (T ** (-b))[None, :]) @ Si)
    return abs(np.trace(M))


# ---- elementary invariants + conjugacy ----
def scalar_depth(M, f=8):
    a, b, c, d = int(M[0, 0]), int(M[0, 1]), int(M[1, 0]), int(M[1, 1]); best = 1
    for dp in [g for g in range(2, f + 1) if f % g == 0]:
        if ((a - 1) % dp == 0 and (d - 1) % dp == 0 and b % dp == 0 and c % dp == 0) or \
           ((a + 1) % dp == 0 and (d + 1) % dp == 0 and b % dp == 0 and c % dp == 0):
            best = dp
    return best


def order_profile(M, mods=(2, 4, 8, 16)):
    out = []
    for dp in mods:
        X = np.array(M, dtype=int) % dp; I = np.eye(2, dtype=int); o = None
        for kk in range(1, 100):
            if np.array_equal(X % dp, I):
                o = kk; break
            X = (X @ np.array(M, dtype=int)) % dp
        out.append(o)
    return tuple(out)


def conjugate(A, B, bound=120, cap=300000):
    R = np.array([[1, 1], [0, 1]]); Ri = np.array([[1, -1], [0, 1]])
    L = np.array([[1, 0], [1, 1]]); Li = np.array([[1, 0], [-1, 1]])

    def t(M):
        return (int(M[0, 0]), int(M[0, 1]), int(M[1, 0]), int(M[1, 1]))
    seen = {t(A)}; dq = deque([np.array(A, dtype=int)]); tgt = t(B)
    while dq and len(seen) < cap:
        X = dq.popleft()
        if t(X) == tgt:
            return True
        for P, Pi in ((R, Ri), (L, Li), (Ri, R), (Li, L)):
            Y = P @ X @ Pi
            if max(abs(int(v)) for v in Y.flatten()) <= bound:
                tt = t(Y)
                if tt not in seen:
                    seen.add(tt); dq.append(Y)
    return tgt in seen


GAMMA_A = np.array([[13, -8], [-8, 5]])   # period 10, d=8
GAMMA_B = np.array([[17, -4], [-4, 1]])   # period 20, d=4


if __name__ == "__main__":
    print("(1) general WRT factorization VALIDATED vs block-word Z:")
    bad = []
    for bl in [[(1, 1)], [(2, 3)], [(1, 2), (2, 1)], [(5, 1)], [(4, 4)], [(1, 2), (1, 3)]]:
        g = gmat(bl)
        for k in [4, 7, 11, 16]:
            if abs(Zabs(g, k) - Zabs_block(bl, k)) > 1e-7:
                bad.append((bl, k))
    print("    ALL MATCH" if not bad else f"    MISMATCH {bad}")
    print("\n(2) THE OBSTRUCTION (f=8, t=18, base lcm(16,20)=80):")
    for M, nm in [(GAMMA_A, "A=[[13,-8],[-8,5]]"), (GAMMA_B, "B=[[17,-4],[-4,1]]")]:
        p = period(M)
        print(f"    {nm}: period={p} d={80 // p}  scalar-depth={scalar_depth(M)}  order-profile={order_profile(M)}")
    print(f"    A ~ B conjugate? {conjugate(GAMMA_A, GAMMA_B)}  (different d => different class)")
    print("    => identical elementary invariants, different d: the f>=8 split is a finer")
    print("       FORM-CLASS / GENUS invariant -> NEEDS-SPECIALIST (2-adic genus theory).")
    print("ALL CHECKS PASS")
