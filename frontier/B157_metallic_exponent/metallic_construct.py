"""General metallic-m SL(n) bundle construction + exponent k in [A,B]=+-mu^k, mu=A^-m t.

Derived clean system (verified by free-group word reduction, see derivation):
   phi(B) = A^m B,   phi(A) = A*(A^m B)^m = A * t B^m t^-1
   relations  tBt^-1 = phi(B),  tAt^-1 = phi(A)
   =>  F1:  B^m = t^-1 A^-1 t A      (equivalently t B^m = A^-1 t A)
       F2:  t B t^-1 = A^m B         (equivalently t B = A^m B t)
   {F1,F2} <=> the two bundle relations.  m=1 reduces to figure-eight, m=2 to silver (B154).

Meridian mu = A^-m t (cusp meridian; commutes with [A,B] via phi([A,B])=A^m[A,B]A^-m).
"""
from __future__ import annotations
import numpy as np
from collections import Counter


def resid(A, B, t, m):
    Ai = np.linalg.inv(A)
    F1 = t @ np.linalg.matrix_power(B, m) - Ai @ t @ A          # t B^m = A^-1 t A
    F2 = t @ B - np.linalg.matrix_power(A, m) @ B @ t           # t B = A^m B t
    return np.concatenate([F1.reshape(-1), F2.reshape(-1)])


def newton(A, m, rng, iters=200):
    n = A.shape[0]
    x = rng.standard_normal(2 * n * n) + 1j * rng.standard_normal(2 * n * n)
    split = lambda x: (x[:n * n].reshape(n, n), x[n * n:].reshape(n, n))
    for _ in range(iters):
        B, t = split(x)
        g = np.concatenate([resid(A, B, t, m), [np.linalg.det(B) - 1, np.linalg.det(t) - 1]])
        mx = np.max(np.abs(g))
        if mx < 1e-12:
            break
        if mx > 1e7:
            return None, None, 9.0
        h = 1e-7
        J = np.zeros((g.size, 2 * n * n), complex)
        for k in range(2 * n * n):
            xp = x.copy(); xp[k] += h
            Bp, tp = split(xp)
            gp = np.concatenate([resid(A, Bp, tp, m), [np.linalg.det(Bp) - 1, np.linalg.det(tp) - 1]])
            J[:, k] = (gp - g) / h
        try:
            st, *_ = np.linalg.lstsq(J, g, rcond=None)
        except np.linalg.LinAlgError:
            return None, None, 9.0
        x = x - st
    B, t = split(x)
    return B, t, np.max(np.abs(resid(A, B, t, m)))


def irred(A, B, rounds=5, tol=1e-7):
    n = A.shape[0]
    gens = [A, B, np.linalg.inv(A), np.linalg.inv(B)]
    allm = [np.eye(n, dtype=complex)]; fr = [np.eye(n, dtype=complex)]
    for _ in range(rounds):
        fr = [g @ mm for mm in fr for g in gens]; allm += fr
    return np.linalg.matrix_rank(np.array([mm.reshape(-1) for mm in allm]), tol=tol) == n * n


def exponent(A, B, t, m, kmax=14):
    """[A,B] = s * mu^k as a MATRIX identity; mu = A^-m t. Returns (s,k,err) or None."""
    Ai = np.linalg.inv(A)
    comm = A @ B @ Ai @ np.linalg.inv(B)
    mu = np.linalg.matrix_power(Ai, m) @ t
    best = (None, None, 9e9)
    for k in range(1, kmax + 1):
        muk = np.linalg.matrix_power(mu, k)
        for s in (1, -1):
            err = np.max(np.abs(comm - s * muk))
            if err < best[2]:
                best = (s, k, err)
    return best


def scan(m, n, spectrum, seeds=200, want=4, cond_cap=1e4):
    sp = np.array(spectrum, complex)
    sp = sp / (np.prod(sp)) ** (1.0 / n)
    A = np.diag(sp)
    rng = np.random.default_rng(0)
    found = []
    for s in range(seeds):
        B, t, r = newton(A, m, rng)
        if B is None or r > 1e-9 or abs(np.linalg.det(t)) < 1e-3 or np.linalg.cond(t) > cond_cap:
            continue
        if not irred(A, B):
            continue
        s_, k_, err = exponent(A, B, t, m)
        if err < 1e-6:
            found.append((s_, k_, err, np.linalg.cond(t)))
        if len(found) >= want:
            break
    return found


if __name__ == "__main__":
    w = np.exp(2j * np.pi / 3); i_ = 1j; z5 = np.exp(2j * np.pi / 5)
    print("=== validation: m=1,2 reproduce figure-eight/silver baseline ===")
    cases = [
        (1, 3, "o3 {1,w,w2}", [1, w, w ** 2]),
        (2, 3, "o3 {1,w,w2}", [1, w, w ** 2]),
        (2, 3, "o4 {1,i,-i}", [1, i_, -i_]),
    ]
    for m, n, name, spec in cases:
        f = scan(m, n, spec)
        c = Counter((s, k) for s, k, e, cc in f)
        print(f"  m={m} n={n} {name:14s}: {dict(c)}  (reps {len(f)})")
