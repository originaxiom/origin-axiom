"""B198 -- gauge-fixed Newton for the metallic exponent k in [A,B]=s*mu^k, mu=A^-m t.

Resolves the B157 "SL(4)/SL(5) Newton wall": that wall was gauge-induced Jacobian
rank-deficiency (the diagonal torus commuting with A=diag gives a whole orbit of solutions,
not a point). FIXING the gauge (pin the superdiagonal t[i,i+1]=1) removes the null space and
Newton converges -- including SL(5) o=5, previously unreachable.

m=1 reduces to a SINGLE unknown t (B = A^-2 t A t^-1), single relation
    R(t) = t A^-2 t A - A^-1 t A t = 0      (25 vars at SL5, vs 50 for the (B,t) system).
General m uses the (B,t) system  F1: t B^m = A^-1 t A ,  F2: t B = A^m B t.

Standalone character-variety / low-dimensional-topology computation. No physics; nothing to
CLAIMS.md. pyenv (numpy).
"""
import numpy as np
from collections import Counter


def make_A(o, exps):
    z = np.exp(2j * np.pi / o)
    d = np.array([z**e for e in exps], complex)
    return np.diag(d), np.diag(d**-1), np.diag(d**-2)


# ---------- m=1 single-t engine ----------
def resid_t(t, A, Ai, Ai2, gfix):
    R = t @ Ai2 @ t @ A - Ai @ t @ A @ t
    extra = [np.linalg.det(t) - 1] + [t[i, i + 1] - 1 for i in gfix]
    return np.concatenate([R.reshape(-1), np.array(extra, complex)])


def newton_t(A, Ai, Ai2, n, gfix, rng, iters=300):
    x = rng.standard_normal(n * n) + 1j * rng.standard_normal(n * n)
    for _ in range(iters):
        t = x.reshape(n, n)
        g = resid_t(t, A, Ai, Ai2, gfix)
        mx = np.max(np.abs(g))
        if mx < 1e-12:
            break
        if mx > 1e9 or not np.isfinite(mx):
            return None, 9.0
        h = 1e-7
        J = np.zeros((g.size, n * n), complex)
        for k in range(n * n):
            xp = x.copy(); xp[k] += h
            J[:, k] = (resid_t(xp.reshape(n, n), A, Ai, Ai2, gfix) - g) / h
        try:
            st, *_ = np.linalg.lstsq(J, g, rcond=None)
        except np.linalg.LinAlgError:
            return None, 9.0
        x = x - st
    t = x.reshape(n, n)
    return t, np.max(np.abs(resid_t(t, A, Ai, Ai2, gfix)))


# ---------- general-m (B,t) engine ----------
def resid_bt(x, A, Am, Ai, m, n, gfix):
    B = x[:n * n].reshape(n, n); t = x[n * n:].reshape(n, n)
    F1 = t @ np.linalg.matrix_power(B, m) - Ai @ t @ A
    F2 = t @ B - Am @ B @ t
    extra = [np.linalg.det(B) - 1, np.linalg.det(t) - 1] + [t[i, i + 1] - 1 for i in gfix]
    return np.concatenate([F1.reshape(-1), F2.reshape(-1), np.array(extra, complex)])


def newton_bt(A, m, n, gfix, rng, iters=400):
    Ai = np.linalg.inv(A); Am = np.linalg.matrix_power(A, m)
    x = rng.standard_normal(2 * n * n) + 1j * rng.standard_normal(2 * n * n)
    for _ in range(iters):
        g = resid_bt(x, A, Am, Ai, m, n, gfix); mx = np.max(np.abs(g))
        if mx < 1e-12:
            break
        if mx > 1e9 or not np.isfinite(mx):
            return None, 9.0
        h = 1e-7; J = np.zeros((g.size, 2 * n * n), complex)
        for k in range(2 * n * n):
            xp = x.copy(); xp[k] += h
            J[:, k] = (resid_bt(xp, A, Am, Ai, m, n, gfix) - g) / h
        try:
            st, *_ = np.linalg.lstsq(J, g, rcond=None)
        except np.linalg.LinAlgError:
            return None, 9.0
        x = x - st
    return x, np.max(np.abs(resid_bt(x, A, Am, Ai, m, n, gfix)))


# ---------- shared: irreducibility + exponent reading ----------
def irred(A, B, n, rounds=6, tol=1e-7):
    gens = [A, B, np.linalg.inv(A), np.linalg.inv(B)]
    allm = [np.eye(n, dtype=complex)]; fr = [np.eye(n, dtype=complex)]
    for _ in range(rounds):
        fr = [g @ mm for mm in fr for g in gens]; allm += fr
    return np.linalg.matrix_rank(np.array([mm.reshape(-1) for mm in allm]), tol=tol)


def exponent(A, B, t, m=1, kmax=16):
    Ai = np.linalg.inv(A)
    comm = A @ B @ Ai @ np.linalg.inv(B)
    mu = np.linalg.matrix_power(Ai, m) @ t
    best = (None, None, 9e9)
    for k in range(0, kmax + 1):
        muk = np.linalg.matrix_power(mu, k)
        for s in (1, -1):
            err = np.max(np.abs(comm - s * muk))
            if err < best[2]:
                best = (s, k, err)
    return best


def confirm(m, o, n, exps, label, seeds=400, rng_seeds=(0, 1, 7)):
    """Returns Counter{(s,k):count} over irreducible, non-degenerate reps."""
    A = make_A(o, exps)[0]; Ai = np.linalg.inv(A); gfix = list(range(n - 1))
    allk = Counter(); nrep = 0; samp = None
    for rs in rng_seeds:
        rng = np.random.default_rng(rs)
        for s in range(seeds):
            if m == 1:
                Aa, Aii, Ai2 = make_A(o, exps)
                t, r = newton_t(Aa, Aii, Ai2, n, gfix, rng)
                B = None if t is None else Ai2 @ t @ Aa @ np.linalg.inv(t)
            else:
                x, r = newton_bt(A, m, n, gfix, rng)
                if x is None:
                    t = None; B = None
                else:
                    B = x[:n * n].reshape(n, n); t = x[n * n:].reshape(n, n)
            if t is None or r > 1e-10 or abs(np.linalg.det(t)) < 1e-3 or np.linalg.cond(t) > 1e6:
                continue
            mu = np.linalg.matrix_power(Ai, m) @ t
            if np.max(np.abs(mu - t)) < 1e-6:   # exclude A^m=I degenerate (mu=t)
                continue
            bd = irred(A, B, n); sgn, k, err = exponent(A, B, t, m)
            if err < 1e-6 and bd == n * n:
                allk[(sgn, k)] += 1; nrep += 1
                if samp is None:
                    samp = (np.max(np.abs(mu - t)), np.linalg.cond(t))
    print("m=%d %-26s irred reps=%d  {(s,k):count}=%s %s" %
          (m, label, nrep, dict(allk), ("  ||mu-t||=%.2g cond=%.2g" % samp if samp else "")))
    return allk


if __name__ == "__main__":
    print("=== validation: reproduce known k (B71/B89/B157) ===")
    confirm(1, 3, 3, [0, 1, 2], "SL3 o3 {1,w,w2} ->4")
    confirm(1, 4, 3, [0, 1, 3], "SL3 o4 {1,i,-i} ->3")
    confirm(2, 4, 3, [0, 1, 3], "SL3 o4 m=2     ->2")
    confirm(2, 3, 3, [0, 1, 2], "SL3 o3 m=2     ->4")
    print("=== NEW (B157 wall, now reached) ===")
    confirm(1, 5, 5, [0, 1, 2, 3, 4], "SL5 o5 m=1 ->2 (=7-o)")
    confirm(2, 5, 5, [0, 1, 2, 3, 4], "SL5 o5 m=2 ->none (formula k=0)")
    print("=== grid sparsity (no irreducible reps) ===")
    confirm(1, 5, 3, [0, 1, 4], "SL3 o5 -> empty")
    confirm(1, 6, 3, [0, 1, 5], "SL3 o6 -> empty")
