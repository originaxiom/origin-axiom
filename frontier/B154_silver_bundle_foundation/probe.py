"""B154 -- silver bundle (m=2, R^2 L^2) foundation: SL(2) character variety + monodromy solver.

Phase C of the B153 campaign: does the rank-stratified degeneration of degree=rank generalize from the
figure-eight (m=1, RL) to the silver bundle (m=2, R^2 L^2), or is it figure-eight-specific?

This module banks the VERIFIED foundation (the rest -- the silver principal spectrum and the SL(n)
degeneration -- is open):

  - the silver monodromy on F_2=<A,B>:  phi_silver = sigma_R^2 o sigma_L^2 :  A -> A^3 B A^2 B,  B -> A^2 B
    (sigma_R: A->A,B->AB ; sigma_L: A->AB,B->B ; abelianizations M1^2=[[2,1],[1,1]] (fig), M2^2=[[5,2],[2,1]]);
  - the trace-map fixed locus (the bundle SL(2) character variety): characters transform CONTRAVARIANTLY,
    so the trace map of phi=sigma_R o sigma_L is t(sigma_L) o t(sigma_R) (REVERSED) -- a bug-class caught
    by the figure-eight control (which must reproduce B67's y=z=x/(x-1));
  - the silver geometric component carries  kappa = tr[A,B] = 1/2 z^2 + 8/z^2 - 2  (z = tr AB), distinct
    from the figure-eight's  kappa = x^2 + z^2 - x - z - 2  (B67);
  - the conjugating monodromy t (tA=phi(A)t, tB=phi(B)t) solved convention-free over the E_ij basis.

Exact fixed-locus derivation: silver_tracemap.sage (Sage/Groebner). This probe verifies numerically.
Run:  python frontier/B154_silver_bundle_foundation/probe.py
"""
from __future__ import annotations
import numpy as np

# ---- monodromy words on F_2 (matrix functions) ----
def phi_fig(A, B):
    return A @ A @ B, A @ B
def phi_silver(A, B):
    return A @ A @ A @ B @ A @ A @ B, A @ A @ B

# ---- SL(2,C) pair with prescribed (tr A, tr B, tr AB) ----
def AB_from_traces(x, y, z):
    A = np.array([[x, -1], [1, 0]], dtype=complex)          # tr A = x, det 1
    p = np.roots([1, (x - y), (2 - z)])[0]                  # p^2+(x-y)p+(2-z)=0  => tr AB = z
    r = p * (y - p) - 1
    B = np.array([[p, 1], [r, y - p]], dtype=complex)       # tr B = y, det 1
    return A, B

def kappa(A, B):
    return np.trace(A @ B @ np.linalg.inv(A) @ np.linalg.inv(B))

def solve_monodromy(A, B, phi, n=2):
    """t with tA=phi(A)t, tB=phi(B)t; null space of t->(tA-A't, tB-B't) over E_ij (convention-free)."""
    Ap, Bp = phi(A, B)
    cols = []
    for i in range(n):
        for j in range(n):
            E = np.zeros((n, n), complex); E[i, j] = 1
            cols.append(np.concatenate([(E @ A - Ap @ E).reshape(-1), (E @ B - Bp @ E).reshape(-1)]))
    M = np.array(cols).T
    _, s, vh = np.linalg.svd(M)
    null = vh[np.sum(s > 1e-9 * s[0]):].conj().T
    if null.shape[1] == 0:
        return None
    t = null[:, 0].reshape(n, n); d = np.linalg.det(t)
    if abs(d) < 1e-12:
        return None
    return t / (d ** (1.0 / n))

def check():
    ok = True
    # figure-eight geometric component (B67): y=z, x=z/(z-1); kappa = x^2+z^2-x-z-2
    for z in [2.1 + 0.3j, 1.6 - 0.7j]:
        y = z; x = z / (z - 1); A, B = AB_from_traces(x, y, z)
        k = kappa(A, B); f = x**2 + z**2 - x - z - 2
        t = solve_monodromy(A, B, phi_fig)
        res = np.max(np.abs(t @ A - phi_fig(A, B)[0] @ t)) if t is not None else 9
        good = abs(k - f) < 1e-9 and res < 1e-9
        ok &= good
        print(f"[fig]    z={z}: kappa matches x^2+z^2-x-z-2: {abs(k-f)<1e-9}; t-res={res:.1e}")
    # silver geometric component: y=xz/2, x^2=2+8/z^2; kappa = 1/2 z^2 + 8/z^2 - 2
    for z in [2.1 + 0.3j, 1.6 - 0.7j, 3 + 1j]:
        x = np.sqrt(2 + 8 / z**2); y = x * z / 2; A, B = AB_from_traces(x, y, z)
        k = kappa(A, B); f = 0.5 * z**2 + 8 / z**2 - 2
        t = solve_monodromy(A, B, phi_silver)
        res = np.max(np.abs(t @ A - phi_silver(A, B)[0] @ t)) if t is not None else 9
        good = abs(k - f) < 1e-9 and res < 1e-9
        ok &= good
        print(f"[silver] z={z}: kappa matches 1/2 z^2+8/z^2-2: {abs(k-f)<1e-9}; t-res={res:.1e}")
    print("\nB154 foundation:", "PASS" if ok else "FAIL")
    print("Open (Phase C continues): the silver principal spectrum + the SL(n) degeneration (component? slice? absent?).")
    return ok

if __name__ == "__main__":
    check()
