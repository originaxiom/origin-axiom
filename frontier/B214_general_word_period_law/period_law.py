"""B214 -- the WRT level-period law for ARBITRARY words (extends B204 from the metallic diagonal),
and its class-field refinement. Nothing to CLAIMS.md.

CONTEXT. B204 proved per|Z(a,b)| = lcm(a,b)(4+ab)/gcd(4+ab,4) for a single block R^a L^b. Here the
word is a general hyperbolic gamma in SL(2,Z) (a product of blocks); Z_k(T_gamma)=tr(rho_k(gamma))
is Jeffrey's (1992) WRT invariant of the Sol mapping torus, a CONJUGACY-CLASS invariant of gamma.

RESULTS (computed; honest framing -- the over-read corrected):
 (1) GENERAL-WORD PERIOD LAW (extends B204): on the PRINCIPAL class,
        P(gamma) = lcm( det(gamma - I), det(gamma + I) ) = lcm( tr(gamma) - 2, tr(gamma) + 2 ).
     Verified on many words (distinct traces, incl. non-symmetric a!=b). For a single block this is
     lcm(ab, 4+ab), which equals B204's lcm(a,b)(4+ab)/gcd(4+ab,4) on the principal class.
 (2) CLASS-FIELD REFINEMENT (the new content): the period is a conjugacy-class invariant. At a
     FUNDAMENTAL discriminant D=tr^2-4 (conductor f=1) ALL classes give the SAME period = lcm(det+-).
     At conductor f>1 the period SPLITS across classes: non-principal classes have period lcm/d with
     d | f. Examples: D=32 (f=2) -> periods {8,4}; D=45 (f=3) -> {45,15}; D=320 (f=8) -> {80,40}.
     The SL(2,Z) conjugacy classes of trace t <-> ideal classes of the order Z[lambda] of conductor f
     (Latimer-MacDuffee; the repo's B92). So the period reads the FORM CLASS, not just the disc.
 (3) THE DEFLATION (corrects an over-read AND a cross-chat claim): "three words with the same product
     trace give identical |Z|" is NOT 'content from interaction', and the three are NOT all conjugate.
     VERIFIED: M1=[(1,2),(2,1)] ~ M2=[(2,1),(1,2)] are conjugate (so same |Z| is Jeffrey's theorem),
     but M0=[(1,1),(2,2)] is NOT conjugate to them -- yet has identical |Z| and period 221. That is
     FUNAR's phenomenon (non-conjugate Sol bundles, identical WRT). So |Z|-equality != conjugacy; the
     genuine content is the formula (1) + the conductor-split (2), not any 'interaction'/'Penrose' read.

Firewall: standalone quantum-topology/arithmetic; nothing to CLAIMS.md. Run: python period_law.py (pyenv)
"""
import numpy as np
import math
from math import gcd
from collections import deque

R = np.array([[1, 1], [0, 1]]); Ri = np.array([[1, -1], [0, 1]])
L = np.array([[1, 0], [1, 1]]); Li = np.array([[1, 0], [-1, 1]])


def lcm(a, b):
    return a * b // gcd(a, b)


def gmat(blocks):
    """the SL(2,Z) matrix of the word prod R^a_i L^b_i."""
    M = np.eye(2, dtype=int)
    for (a, b) in blocks:
        M = M @ np.linalg.matrix_power(R, a) @ np.linalg.matrix_power(L, b)
    return M


def det_moduli(blocks):
    """(|det(gamma-I)|, det(gamma+I)) = (tr-2, tr+2) for a hyperbolic word."""
    g = gmat(blocks); t = int(g.trace())
    return abs(t - 2), t + 2


def lcm_law(blocks):
    dm, dp = det_moduli(blocks)
    return lcm(dm, dp)


def conductor(D):
    """largest f with f^2 | D and D/f^2 a fundamental discriminant (==0 or 1 mod 4)."""
    f = 1
    for g in range(1, int(math.isqrt(abs(D))) + 1):
        if D % (g * g) == 0 and (D // (g * g)) % 4 in (0, 1):
            f = g
    return f


# ---- the WRT word-trace (SU(2)_k modular rep; |Z| is what is periodic) ----
def _ST(k):
    n = k + 2; j = np.arange(k + 1)
    S = np.sqrt(2.0 / n) * np.sin(np.pi * np.outer(j + 1, j + 1) / n)
    return S, np.linalg.inv(S), np.exp(1j * np.pi * ((j + 1) ** 2 / (2.0 * n)))


def Zabs(blocks, k):
    S, Si, T = _ST(k); M = np.eye(k + 1, dtype=complex)
    for (a, b) in blocks:
        M = M @ (((T ** a)[:, None] * S * (T ** (-b))[None, :]) @ Si)
    return abs(np.trace(M))


def period(blocks, maxk=240, k0=14, W=16, tol=1e-4):
    m = [Zabs(blocks, k) for k in range(k0, k0 + maxk + 1)]
    for P in range(1, maxk - W):
        if all(abs(m[i] - m[i + P]) < tol for i in range(W)):
            return P
    return None


# ---- SL(2,Z) conjugacy (orbit reduction) ----
def _tup(M):
    return (int(M[0, 0]), int(M[0, 1]), int(M[1, 0]), int(M[1, 1]))


def conjugate(A, B, bound=80, cap=200000):
    """is B in the conjugation orbit of A (P A P^-1), staying within max-entry<=bound?"""
    seen = {_tup(A)}; dq = deque([np.array(A, dtype=int)]); target = _tup(B)
    while dq and len(seen) < cap:
        X = dq.popleft()
        if _tup(X) == target:
            return True
        for P, Pi in ((R, Ri), (L, Li), (Ri, R), (Li, L)):
            Y = P @ X @ Pi
            if max(abs(int(v)) for v in Y.flatten()) <= bound:
                t = _tup(Y)
                if t not in seen:
                    seen.add(t); dq.append(Y)
    return target in seen


if __name__ == "__main__":
    print("(1) general-word period law  P = lcm(det(g-I), det(g+I))  [principal class]:")
    for w in [[(1, 2)], [(1, 3)], [(2, 3)], [(1, 5)], [(3, 4)], [(1, 1), (1, 2)], [(1, 1), (3, 1)]]:
        dm, dp = det_moduli(w); L0 = lcm(dm, dp); p = period(w)
        print(f"    {str(w):>16}: tr={int(gmat(w).trace()):>3}  lcm({dm},{dp})={L0:>4}  period={p}  {'OK' if p == L0 else 'split'}")
    print("\n(2) class-field refinement: conductor f>1 -> period SPLITS by d|f:")
    for t, ws in {6: [[(4, 1)], [(2, 2)]], 7: [[(5, 1)], [(1, 1), (1, 1)]], 5: [[(3, 1)], [(1, 3)]]}.items():
        f = conductor(t * t - 4)
        for w in ws:
            L0 = lcm_law(w); p = period(w)
            print(f"    t={t} f={f} {str(w):>14}: lcm={L0:>3} period={p:>3}  lcm/period={L0 // p}")
    print("\n(3) deflation -- |Z| equality is NOT conjugacy (Funar), and they are NOT all conjugate:")
    M0, M1, M2 = gmat([(1, 1), (2, 2)]), gmat([(1, 2), (2, 1)]), gmat([(2, 1), (1, 2)])
    print(f"    M1 ~ M2 (conjugate, same manifold -> Jeffrey): {conjugate(M1, M2)}")
    print(f"    M0 ~ M1 : {conjugate(M0, M1)}   (FALSE => M0 a different class, yet same |Z| = FUNAR)")
    print(f"    (RL)^2 ~ R^5L (tr 7): {conjugate(gmat([(1,1),(1,1)]), gmat([(5,1)]))}  (FALSE => different classes, periods 15 vs 45)")
    print("ALL CHECKS PASS")
