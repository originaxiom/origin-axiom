"""Exact characteristic-zero (Q) variant of the Phase A pinv-limit (S=I, the canonical
positive-definite metric).  Same construction as jacobian_closure.py but over exact
rationals -- the faithful analog of B66's real SVD-pinv, with no float conditioning and
no finite-field non-canonicity.

VALIDATED at n=3: reproduces char(M^-1).char(M^2).char(M^3).(t-1)(t+1) EXACTLY (~10s).
But IMPRACTICALLY SLOW at n>=4 via sympy+Fraction (rational blowup: n=4 did not finish
in minutes vs the F_p engine's ~3s) without python-flint.  It is also UNNECESSARY: the
exact F_p engine with S=I (jacobian_closure.py) is prime-stable, hence equals this Q
object mod p for the (non-singular) primes -- and gives the same n=5 verdict (a_2=1).
See FINDINGS.md: the n=5 char(M^2) shortfall is the pinv-limit CONSTRUCTION at the
degenerate even-k collision, not the field/metric, so this Q field-swap is not the fix."""
from __future__ import annotations
import sys, math
from fractions import Fraction as Fr
from pathlib import Path
import numpy as np, sympy as sp
sys.path.insert(0, str(Path(__file__).resolve().parent))
import jacobian_closure as J   # b66_select, basis_sln

t = sp.symbols("t")

def eye_q(L, n):
    A = np.empty((L + 1, n, n), dtype=object); A[:] = Fr(0)
    for i in range(n): A[0][i, i] = Fr(1)
    return A

def zero_q(L, n):
    A = np.empty((L + 1, n, n), dtype=object); A[:] = Fr(0); return A

def epmul_q(A, B):
    L = A.shape[0] - 1; n = A.shape[1]
    C = np.empty((L + 1, n, n), dtype=object); C[:] = Fr(0)
    for e in range(L + 1):
        acc = None
        for i in range(e + 1):
            term = A[i] @ B[e - i]
            acc = term if acc is None else acc + term
        C[e] = acc
    return C

def epinv_q(A):
    L = A.shape[0] - 1; n = A.shape[1]
    negN = -A.copy()
    for i in range(n): negN[0][i, i] = negN[0][i, i] + Fr(1)   # I - A; const part -> 0
    acc = eye_q(L, n); term = eye_q(L, n)
    for _ in range(L):
        term = epmul_q(term, negN); acc = acc + term
    return acc

def epexp_q(P, L):
    n = P.shape[0]; E = zero_q(L, n)
    Pk = np.eye(n, dtype=object)
    for k in range(L + 1):
        E[k] = Pk * Fr(1, math.factorial(k)); Pk = Pk @ P
    return E

def demul_q(A, B): return (epmul_q(A[0], B[0]), epmul_q(A[0], B[1]) + epmul_q(A[1], B[0]))
def deinv_q(A):
    a0i = epinv_q(A[0]); return (a0i, -epmul_q(epmul_q(a0i, A[1]), a0i))
def depow_q(A, k, L, n):
    R = (eye_q(L, n), zero_q(L, n))
    for _ in range(k): R = demul_q(R, A)
    return R

def grad_series_q(words, P, Q, basis, L, substitute):
    n = P.shape[0]; dim = len(basis)
    expP, expQ = epexp_q(P, L), epexp_q(Q, L)
    out = np.empty((L, len(words), 2 * dim), dtype=object); out[:] = Fr(0)
    for which in ("A", "B"):
        for jg, g in enumerate(basis):
            col = jg if which == "A" else dim + jg
            G = zero_q(L, n); G[0] = g.astype(object)
            if which == "A":
                A_d = (expP, epmul_q(G, expP)); B_d = (expQ, zero_q(L, n))
            else:
                A_d = (expP, zero_q(L, n)); B_d = (expQ, epmul_q(G, expQ))
            if substitute:
                A_eff = demul_q(depow_q(A_d, 1, L, n), B_d); B_eff = A_d   # m=1
            else:
                A_eff, B_eff = A_d, B_d
            mats = {"A": A_eff, "B": B_eff, "a": deinv_q(A_eff), "b": deinv_q(B_eff)}
            for r, w in enumerate(words):
                acc = (eye_q(L, n), zero_q(L, n))
                for c in w: acc = demul_q(acc, mats[c])
                h1 = acc[1]
                for l in range(1, L + 1):
                    out[l - 1, r, col] = sum(h1[l][ii, ii] for ii in range(n))
    return out

def run_q(n, maxlen, L, Pent=1):
    words = J.b66_select(n, maxlen, seed=20); dim = n * n - 1
    basis = J.basis_sln(n)
    rng = np.random.default_rng(7)
    def small_tl():
        Z = rng.integers(-Pent, Pent + 1, size=(n, n)).astype(object)
        Z[n - 1, n - 1] = -sum(Z[i, i] for i in range(n - 1)); return Z
    P, Q = small_tl(), small_tl()
    Dx = grad_series_q(words, P, Q, basis, L, False)
    DX = grad_series_q(words, P, Q, basis, L, True)
    mo = L + 1
    # G_l = sum Dx_i Dx_j^T, R_l = sum DX_i Dx_j^T  (S = I)
    G = [None] * (mo + 1); R = [None] * (mo + 1)
    for l in range(2, mo + 1):
        g = sp.zeros(dim); r = sp.zeros(dim)
        for i in range(1, L + 1):
            j = l - i
            if 1 <= j <= L:
                g += sp.Matrix(Dx[i - 1].tolist()) * sp.Matrix(Dx[j - 1].tolist()).T
                r += sp.Matrix(DX[i - 1].tolist()) * sp.Matrix(Dx[j - 1].tolist()).T
        G[l] = g; R[l] = r
    jmax = mo - 2; morders = list(range(2, mo + 1))
    Mrows = []
    for m in morders:
        for c in range(dim):
            row = [Fr(0)] * ((jmax + 1) * dim)
            for jj in range(jmax + 1):
                o = m - jj
                if 2 <= o <= mo:
                    for b in range(dim): row[jj * dim + b] = G[o][b, c]
            Mrows.append(row)
    M = sp.Matrix(Mrows)
    DT0 = sp.zeros(dim, dim)
    for a in range(dim):
        rhs = []
        for m in morders:
            for c in range(dim): rhs.append(R[m][a, c])
        sol = M.gauss_jordan_solve(sp.Matrix(rhs))[0]
        for b in range(dim): DT0[a, b] = sol[b]
    cp = DT0.charpoly(t).as_expr()
    return sp.factor(sp.expand(cp)), words

if __name__ == "__main__":
    import time
    # n=3 is the validated, tractable case; n>=4 is impractically slow (see module docstring)
    for n, ml, L in [(3, 4, 6)]:
        t0 = time.time()
        fac, words = run_q(n, ml, L)
        print(f"n={n} (exact Q, S=I, L={L}): {time.time()-t0:.1f}s")
        print("char(DT0) =", fac, "  [= char(M^-1).char(M^2).char(M^3).(t-1)(t+1)]")
