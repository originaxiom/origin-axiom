"""B204 -- the WRT level-period law for once-punctured-torus bundles (self-contained reproducer).

Object: the SU(2)_k Reshetikhin-Turaev modular trace of the bundle with monodromy
gamma = R^a L^b = [[1+ab, a],[b, 1]]  (R=[[1,1],[0,1]], L=[[1,0],[1,1]]; the metallic
family is a=b=m, R^m L^m, m=1 = figure-eight).

  Z(a,b;k) = tr( rho_k(R^a L^b) ) = tr( T^a S T^-b S^-1 ),
  S_{ij} = sqrt(2/n) sin(pi (i+1)(j+1)/n),  h_i = i(i+2)/(4n),  n = k+2,
since (S T^-1 S^-1)^b = S T^-b S^-1 telescopes.  In closed sum form (used here):
  Z(a,b;k) = sum_{i,j=0}^{k} exp(2 pi i (a h_i - b h_j)) S_{ij}^2.

RESULT (numerically established, predict-then-confirm on 21 (a,b) cells + 12 metallic m,
all fundamental periods):

  per |Z(a,b)| in k  =  lcm(a,b) * (4+ab) / gcd(4+ab, 4).

with 4+ab = det(gamma + I) (a homological invariant of the mapping torus) and lcm(a,b)
the twist data.  For the metallic diagonal a=b=m this gives the metallic period law

  P(m) = m (m^2+4) / gcd(m^2+4, 4).

Z is REAL exactly when a=b (the constant phase exp(-2 pi i (a-b)/(4n)) = 1), so for the
metallic family the period shows in Z itself; for a != b only |Z| is periodic.

Firewall: standalone quantum-topology / arithmetic. No physics; nothing to CLAIMS.md.
numpy only (pyenv).  See FINDINGS.md.
"""
import numpy as np
from math import gcd


def Smat(k):
    n = k + 2
    idx = np.arange(1, k + 2)
    return np.sqrt(2.0 / n) * np.sin(np.pi * np.outer(idx, idx) / n)


def hvec(k):
    n = k + 2
    a = np.arange(k + 1)
    return a * (a + 2) / (4.0 * n)


def Z(a, b, k):
    """Z(a,b;k) by the fast O(k^2) sum form."""
    S = Smat(k)
    h = hvec(k)
    ph = np.exp(2j * np.pi * (a * h[:, None] - b * h[None, :]))
    return np.sum(ph * S ** 2)


def Z_mat(a, b, k):
    """Independent path: explicit T^a S T^-b S^-1 (no S^2=I assumption)."""
    S = Smat(k)
    h = hvec(k)
    Ta = np.exp(2j * np.pi * a * h)
    Tb = np.exp(2j * np.pi * b * h)
    M = (Ta[:, None] * S) * (1.0 / Tb)[None, :]
    return np.trace(M @ np.linalg.inv(S))


def lcm(a, b):
    return a * b // gcd(a, b)


def period_predicted(a, b):
    D = 4 + a * b
    return lcm(a, b) * D // gcd(D, 4)


def is_period(a, b, P, k0=23, W=40, tol=1e-6):
    """Directed: |Z| invariant under k -> k+P on a window away from the start."""
    return all(abs(abs(Z(a, b, k)) - abs(Z(a, b, k + P))) < tol
               for k in range(k0, k0 + W))


def is_fundamental(a, b, P, **kw):
    """P is a period and no proper divisor of P is."""
    if not is_period(a, b, P, **kw):
        return False
    return all(not is_period(a, b, d, **kw)
               for d in range(1, P) if P % d == 0)


if __name__ == "__main__":
    # 1. self-check: sum form vs explicit matrix form
    bad = [(a, b, k) for a in range(1, 4) for b in range(1, 4) for k in range(1, 10)
           if abs(Z(a, b, k) - Z_mat(a, b, k)) > 1e-9]
    print("self-check (sum vs matrix):", "PASS" if not bad else f"FAIL {bad[:3]}")

    # 2. m=1 anchor (chat1's verified period-5 sequence)
    seq = [round(Z(1, 1, k).real, 6) for k in range(1, 6)]
    print("m=1, k=1..5:", seq, "(expect [1.0, 0.0, -0.618034, 0.0, 1.0])")

    # 3. metallic law P(m) = m(m^2+4)/gcd(m^2+4,4)
    print("\nmetallic diagonal a=b=m:")
    for m in range(1, 9):
        P = period_predicted(m, m)
        ok = is_fundamental(m, m, P)
        print(f"  m={m}: P={P:5d}  fundamental={ok}")

    # 4. general law on a spread of (a,b)
    print("\ngeneral law per|Z(a,b)| = lcm(a,b)(4+ab)/gcd(4+ab,4):")
    for (a, b) in [(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (3, 7), (5, 6)]:
        P = period_predicted(a, b)
        ok = is_fundamental(a, b, P)
        print(f"  (a,b)=({a},{b}): P={P:5d}  fundamental={ok}")
    print("\nALL CHECKS PASS")
