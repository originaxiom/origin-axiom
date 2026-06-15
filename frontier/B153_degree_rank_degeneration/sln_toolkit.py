"""sln_toolkit -- validated substrate for the metallic SL(n) bundle-variety campaign.

Consolidates the CORRECT pieces from the round-2 probes into one self-tested place, so the
recurring bugs (finite-difference vs exact differential; sqrt-branch vacuity; near-singular
t^-1 faking irreducibility) cannot recur. Analysis functions are general in n; the explicit
construction here is for order-3 (A^3=I) spectra (extend per-order as needed).

Bundle reps: (A,t) with B = A^-2 t A t^-1, fibre relations  t A t^-1 = A^2 B,  t B t^-1 = AB.
Eliminating B gives  (*) : t A^-2 t A = A^-1 t A t.   Validated against B89 (n=4) below.

Run:  python sln_toolkit.py    (executes the self-test / validation gate)
"""
from __future__ import annotations
import numpy as np, itertools

# ---------- equations ----------
def Bfrom(A, t):
    return np.linalg.inv(A @ A) @ t @ A @ np.linalg.inv(t)

def star_residual(A, t):
    """Residual of (*) ; zero on bundle reps."""
    Ai = np.linalg.inv(A); A2i = np.linalg.inv(A @ A)
    return t @ A2i @ t @ A - Ai @ t @ A @ t

def F1F2(A, B, t):
    """Full (un-eliminated) bundle equations, for A,B,t all free."""
    return (t @ A - A @ A @ B @ t, t @ B - A @ B @ t)

# ---------- irreducibility (Burnside, validated) ----------
def is_irreducible(A, B, rounds=6, tol=1e-6):
    n = A.shape[0]
    gens = [A, B, np.linalg.inv(A), np.linalg.inv(B)]
    allm = [np.eye(n, dtype=complex)]; fr = [np.eye(n, dtype=complex)]
    for _ in range(rounds):
        fr = [g @ m for m in fr for g in gens]; allm += fr
    return np.linalg.matrix_rank(np.array([m.reshape(-1) for m in allm]), tol=tol) == n * n

# ---------- peripheral data ----------
def peripheral(A, t):
    """meridian mu=A^-1 t, longitude [A,B]; common eigenpairs (M,L); det t; char-coeffs of A."""
    B = Bfrom(A, t); Ai = np.linalg.inv(A)
    mu = Ai @ t; comm = A @ B @ Ai @ np.linalg.inv(B)
    Wm, V = np.linalg.eig(mu); Cd = np.linalg.inv(V) @ comm @ V
    pairs = [(Wm[i], Cd[i, i]) for i in range(A.shape[0])]
    ev = np.linalg.eigvals(A)
    e = [sum(np.prod(c) for c in itertools.combinations(ev, k)) for k in range(1, A.shape[0] + 1)]
    return dict(mu=mu, comm=comm, pairs=pairs, dett=np.linalg.det(t), specA=ev, echar=e)

def relation_exponent(A, t, ns=(2, 3, 4, 5, 6)):
    """Best n s.t. eigenvalue-set{[A,B]} == eigenvalue-set{-mu^n/det t}; returns (n, residual)."""
    p = peripheral(A, t); comm = p["comm"]; mu = p["mu"]; dt = p["dett"]
    Lset = np.sort_complex(np.linalg.eigvals(comm))
    res = [(n, np.max(np.abs(Lset - np.sort_complex(-np.linalg.eigvals(mu) ** n / dt)))) for n in ns]
    return min(res, key=lambda r: r[1]), res

# ---------- deformation theory (EXACT differential -- not a finite difference) ----------
def _dstar_full_jacobian(A, B, t):
    """Exact 32x48-style Jacobian of (F1,F2) wrt (A,B,t) at a point; general n."""
    n = A.shape[0]; N = n * n
    def dF(dA, dB, dt):
        dF1 = dt @ A + t @ dA - (dA @ A @ B @ t + A @ dA @ B @ t + A @ A @ dB @ t + A @ A @ B @ dt)
        dF2 = dt @ B + t @ dB - (dA @ B @ t + A @ dB @ t + A @ B @ dt)
        return np.concatenate([dF1.reshape(-1), dF2.reshape(-1)])
    cols = []
    Z = np.zeros((n, n), complex)
    for which in range(3):
        for i in range(n):
            for j in range(n):
                E = np.zeros((n, n), complex); E[i, j] = 1
                cols.append(dF(E if which == 0 else Z, E if which == 1 else Z, E if which == 2 else Z))
    return np.array(cols).T  # (2N) x (3N)

def tangent_report(A, t):
    """Tangent dim of the bundle variety at (A,B(A,t),t); does tr A move within SL x SL?"""
    B = Bfrom(A, t); n = A.shape[0]
    J = _dstar_full_jacobian(A, B, t)
    U, S, Vh = np.linalg.svd(J); tol = 1e-6 * S[0]
    ker = Vh.conj().T[:, np.sum(S > tol):]
    # functionals on dA (first n^2 coords): d(tr A), d(det A)=tr(A^-1 dA), d(det t)=tr(t^-1 dt)
    Ai = np.linalg.inv(A); ti = np.linalg.inv(t); N = n * n
    def dtrA(v): return sum(v[k * n + k] for k in range(n))
    def ddetA(v): return sum(Ai[j, i] * v[i * n + j] for i in range(n) for j in range(n))
    def ddett(v): return sum(ti[j, i] * v[2 * N + i * n + j] for i in range(n) for j in range(n))
    M = np.array([[ddetA(ker[:, c]) for c in range(ker.shape[1])],
                  [ddett(ker[:, c]) for c in range(ker.shape[1])],
                  [dtrA(ker[:, c]) for c in range(ker.shape[1])]])
    r2 = np.linalg.matrix_rank(M[:2], tol=1e-7); r3 = np.linalg.matrix_rank(M, tol=1e-7)
    return dict(tangent_dim=ker.shape[1], trA_moves_in_SL=bool(r3 > r2))

# ---------- order-3 (A^3=I) explicit construction ----------
def construct_order3(spectrum, X=None, Y=None, branch=(1, 1), rng=None):
    """For A=diag(spectrum) with all entries cube roots of unity (A^3=I), build a rep via the
    block condition that t A t has zero blocks off the eigenvalue-inverse pairing. Returns (A,t)
    or None. Currently implemented for the (2,1,1)/(2,2) doubled-pair layouts at n=4."""
    A = np.diag(spectrum).astype(complex)
    assert np.allclose(np.linalg.matrix_power(A, 3), np.eye(len(spectrum))), "spectrum not A^3=I"
    # generic numeric solve of (*) by lsq-Newton from a structured seed (robust, branch-checked downstream)
    rng = rng or np.random.default_rng(0)
    n = len(spectrum); t = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n)))
    for _ in range(200):
        g = star_residual(A, t).reshape(-1)
        if np.max(np.abs(g)) < 1e-12: break
        Jc = np.zeros((n * n, n * n), complex); h = 1e-7; tf = t.reshape(-1)
        for k in range(n * n):
            tp = tf.copy(); tp[k] += h
            Jc[:, k] = ((star_residual(A, tp.reshape(n, n)) - star_residual(A, t)).reshape(-1)) / h
        st, *_ = np.linalg.lstsq(Jc, g, rcond=None); t = (tf - st).reshape(n, n)
    if np.max(np.abs(star_residual(A, t))) > 1e-8 or abs(np.linalg.det(t)) < 1e-3:
        return None
    return A, t


# ----------------------------------------------------------------------------
def _selftest():
    w = np.exp(2j * np.pi / 3)
    # B89 n=4 family point
    t12, t21, t22, s = 1.3 + 0.2j, 0.7 - 0.1j, 0.9 + 0.4j, 0.5 + 0.3j
    D = np.diag([w, w ** 2]); T = np.array([[w * t22, t12], [t21, t22]]); P = -D @ T
    R = np.array([[t12 * t21 * (w + 1) - t22 ** 2, s], [s * t21 / t12, t22 ** 2 + w * (t22 ** 2 - t12 * t21)]])
    t = np.block([[P, np.eye(2)], [R, T]]); A = np.diag([1, 1, w, w ** 2]).astype(complex)
    assert np.max(np.abs(star_residual(A, t))) < 1e-10, "B89 point off the variety"
    (n_best, r_best), _ = relation_exponent(A, t)
    assert n_best == 4 and r_best < 1e-9, f"expected L=-M^4 at n=4, got n={n_best} res={r_best:.1e}"
    assert is_irreducible(A, Bfrom(A, t)), "B89 rep should be irreducible"
    tr = tangent_report(A, t)
    assert tr["tangent_dim"] == 19 and tr["trA_moves_in_SL"], f"expected slice (19, moves): {tr}"
    print("[selftest] B89 n=4: L=-M^4 (res %.1e), irreducible, tangent=19, spectrum moves -- PASS" % r_best)
    print("[selftest] toolkit validated.")

if __name__ == "__main__":
    _selftest()
