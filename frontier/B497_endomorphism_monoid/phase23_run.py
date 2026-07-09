#!/usr/bin/env python3
"""B497 Phases 2-3 reproducer: singular-verb geometry + the six-lens interaction program.

Phase 2: Q3 BS(1,2) < G_dec (exact, Britton); Q2 bounded atoroidality search for phi_TM.
Phase 3: L1 sandwich laws (exact); L2 Kronecker spectrum (exact); L5 coupled Schrodinger
         (bounded numerics, control lattice).

  python3 phase23_run.py
"""
import itertools as it
import numpy as np
import sympy as sp
from sympy import Matrix, symbols, simplify, fibonacci, sqrt

# ---------------- Phase 2 / Q2: bounded atoroidality search ----------------
def _reduce(w):
    out = []
    for t in w:
        if out and out[-1][0] == t[0] and out[-1][1] == -t[1]:
            out.pop()
        else:
            out.append(t)
    return out

def _cyc_reduce(w):
    w = _reduce(w)
    while len(w) >= 2 and w[0][0] == w[-1][0] and w[0][1] == -w[-1][1]:
        w = _reduce(w[1:-1])
    return w

def _phi_tm(word):
    out = []
    for (g, e) in word:
        img = [('A', 1), ('B', 1)] if g == 'A' else [('B', 1), ('A', 1)]
        if e == -1:
            img = [(x, -y) for (x, y) in reversed(img)]
        out += img
    return _reduce(out)

def _cyc_perms(w):
    return [tuple(w[i:] + w[:i]) for i in range(len(w))] if w else [tuple()]

def _is_conj_cyc(w1, w2):
    w1, w2 = _cyc_reduce(list(w1)), _cyc_reduce(list(w2))
    return len(w1) == len(w2) and tuple(w1) in set(_cyc_perms(w2))

def atoroidality_search(L=6, K=6, MMAX=4):
    """returns the list of (w,k,m) with phi^k(w) ~ w^m; empty = bounded atoroidal evidence."""
    gens = [('A', 1), ('A', -1), ('B', 1), ('B', -1)]
    seen, found = set(), []
    for l in range(1, L + 1):
        for tup in it.product(gens, repeat=l):
            w = _cyc_reduce(list(tup))
            if len(w) != l:
                continue
            key = min(min(_cyc_perms(w)),
                      min(_cyc_perms([(g, -e) for (g, e) in reversed(w)])))
            if key in seen:
                continue
            seen.add(key)
            cur = list(w)
            for k in range(1, K + 1):
                cur = _phi_tm(cur)
                cr = _cyc_reduce(cur)
                if w and len(cr) % len(w) == 0:
                    m = len(cr) // len(w)
                    if 1 <= m <= MMAX and _is_conj_cyc(cr, _reduce(list(w) * m)):
                        found.append((tuple(w), k, m))
    return found

# ---------------- Phase 3 / L1: the sandwich laws ----------------
def sandwich_scalar_law():
    """M X M = (e^T X e) M for all X (M = e e^T)."""
    M = Matrix([[1, 1], [1, 1]])
    e = Matrix([1, 1])
    X = Matrix(2, 2, symbols('x0:4'))
    return simplify(M*X*M - (e.T*X*e)[0]*M) == sp.zeros(2, 2)

def sandwich_fibonacci(kmax=8):
    """M F^k M = F_{k+3} M for the golden unit."""
    F = Matrix([[1, 1], [1, 0]]); M = Matrix([[1, 1], [1, 1]]); e = Matrix([1, 1])
    return all((e.T*F**k*e)[0] == fibonacci(k + 3) for k in range(1, kmax + 1))

def sandwich_metallic(m, kmax=6):
    """the sandwich sequence obeys the metallic recursion s' = m s + s_prev."""
    Fm = Matrix([[m, 1], [1, 0]]); e = Matrix([1, 1])
    s = [(e.T*Fm**k*e)[0] for k in range(1, kmax + 1)]
    return all(s[i+1] == m*s[i] + s[i-1] for i in range(1, kmax - 1))

def fusion_shape():
    """M^2 = 2M (the dim^2=2 idempotent shape)."""
    M = Matrix([[1, 1], [1, 1]])
    return M*M == 2*M

def kronecker_spectrum():
    """Fib (x) TM eigenvalues {1+sqrt5, 1-sqrt5, 0, 0} (non-Pisot)."""
    F = Matrix([[1, 1], [1, 0]]); M = Matrix([[1, 1], [1, 1]])
    K = sp.Matrix(sp.kronecker_product(F, M))
    ev = K.eigenvals()
    return set(ev.keys()) == {1 + sqrt(5), 1 - sqrt(5), 0}

# ---------------- Phase 3 / L5: coupled Schrodinger (bounded) ----------------
def _word(kind, N, m=2, rng=None):
    if kind == 'fib':
        w = 'a'
        while len(w) < N: w = ''.join('ab' if c == 'a' else 'a' for c in w)
    elif kind == 'tm':
        w = 'a'
        while len(w) < N: w = ''.join('ab' if c == 'a' else 'ba' for c in w)
    elif kind == 'pd':
        w = 'a'
        while len(w) < N: w = ''.join('ab' if c == 'a' else 'aa' for c in w)
    elif kind == 'silver':
        w = 'a'
        while len(w) < N: w = ''.join('a'*m + 'b' if c == 'a' else 'a' for c in w)
    else:
        w = ''.join(rng.choice(['a', 'b'], N))
    return w[:N]

def l5_gap_counts(N=2048, thresh=0.02, seed=7):
    from scipy.linalg import eigh_tridiagonal
    rng = np.random.default_rng(seed)
    V = lambda w, lam: np.array([lam if c == 'a' else -lam for c in w])
    fw, tw = _word('fib', N), _word('tm', N)
    pw, sw = _word('pd', N), _word('silver', N)
    rw = _word('rnd', N, rng=rng)
    out = {}
    for name, v in {
        'fib': V(fw, 1.0), 'tm': V(tw, 1.0),
        'coupled': V(fw, 1.0) + V(tw, 0.8),
        'ctrl_fib_pd': V(fw, 1.0) + V(pw, 0.8),
        'ctrl_silver_tm': V(sw, 1.0) + V(tw, 0.8),
        'ctrl_fib_rnd': V(fw, 1.0) + V(rw, 0.8),
    }.items():
        w = eigh_tridiagonal(v, np.ones(N - 1), eigvals_only=True)
        gaps = np.diff(w)
        out[name] = int(np.sum(gaps > thresh))
    return out

if __name__ == "__main__":
    print("Q2 atoroidality (L=6,K=6): witnesses =", atoroidality_search() or "NONE (bounded atoroidal)")
    print("L1 sandwich scalar law:", sandwich_scalar_law())
    print("L1 Fibonacci readout M F^k M = F_{k+3} M:", sandwich_fibonacci())
    print("L1 metallic m-scan (m=2..5):", all(sandwich_metallic(m) for m in range(2, 6)))
    print("L1 fusion shape M^2=2M:", fusion_shape())
    print("L2 Kronecker spectrum {1±sqrt5,0,0}:", kronecker_spectrum())
    print("L5 gap counts (N=2048):", l5_gap_counts())
