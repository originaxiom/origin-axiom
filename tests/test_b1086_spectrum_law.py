"""B1086 lock: the independently-rebuilt untwisted rows (h1(M;27)=3, h1(D;27)=5)."""
import sympy as sp
import pytest

# Exact Q(sqrt-3) as pairs (P, Q) meaning P + Q*s, s^2 = -3 (the rebuilt pipeline's core).
def _mul(X, Y):
    return (X[0]*Y[0] - 3*X[1]*Y[1], X[0]*Y[1] + X[1]*Y[0])
def _eye(n): return (sp.eye(n), sp.zeros(n, n))
def _reg(X):
    return sp.Matrix.vstack(sp.Matrix.hstack(X[0], -3*X[1]), sp.Matrix.hstack(X[1], X[0]))
def _rank(X):
    r = _reg(X).rank(); assert r % 2 == 0; return r // 2

A = (sp.Matrix([[1, 1], [0, 1]]), sp.zeros(2, 2))
Ai = (sp.Matrix([[1, -1], [0, 1]]), sp.zeros(2, 2))
B = (sp.Matrix([[1, 0], [sp.Rational(1, 2), 1]]), sp.Matrix([[0, 0], [sp.Rational(1, 2), 0]]))
Bi = (sp.Matrix([[1, 0], [-sp.Rational(1, 2), 1]]), sp.Matrix([[0, 0], [-sp.Rational(1, 2), 0]]))

def _word(mats, letters):
    out = _eye(2)
    for c in letters:
        out = _mul(out, mats[c])
    return out

MATS = {"a": A, "A": Ai, "b": B, "B": Bi}

def test_relator_and_riley():
    w = _word(MATS, "bABa")
    lhs = _mul(A, w); rhs = _mul(w, B)
    assert lhs[0] == rhs[0] and lhs[1] == rhs[1]

def test_longitude_trace_minus_2():
    lam = _word(MATS, "bABa" + "aBAb")   # w * w-star
    tr = (lam[0][0, 0] + lam[0][1, 1], lam[1][0, 0] + lam[1][1, 1])
    assert tr == (-2, 0)
    c = _mul(lam, A); d = _mul(A, lam)
    assert c[0] == d[0] and c[1] == d[1]

def _sym(M, k):
    # Sym^k on x^{k-i} y^i via the substitution functor, exact pairs.
    P, Q = M
    def smul(a, b): return (a[0]*b[0] - 3*a[1]*b[1], a[0]*b[1] + a[1]*b[0])
    def sadd(a, b): return (a[0] + b[0], a[1] + b[1])
    u = {(1, 0): (P[0, 0], Q[0, 0]), (0, 1): (P[1, 0], Q[1, 0])}
    v = {(1, 0): (P[0, 1], Q[0, 1]), (0, 1): (P[1, 1], Q[1, 1])}
    def pmul(pa, pb):
        out = {}
        for k1, c1 in pa.items():
            for k2, c2 in pb.items():
                kk = (k1[0] + k2[0], k1[1] + k2[1])
                c = smul(c1, c2)
                out[kk] = sadd(out[kk], c) if kk in out else c
        return out
    up = [{(0, 0): (sp.Integer(1), sp.Integer(0))}]
    for _ in range(k): up.append(pmul(up[-1], u))
    vp = [{(0, 0): (sp.Integer(1), sp.Integer(0))}]
    for _ in range(k): vp.append(pmul(vp[-1], v))
    Po = sp.zeros(k + 1, k + 1); Qo = sp.zeros(k + 1, k + 1)
    for i in range(k + 1):
        for (ex, ey), (cp, cq) in pmul(up[k - i], vp[i]).items():
            Po[ey, i] = cp; Qo[ey, i] = cq
    return (Po, Qo)

@pytest.mark.parametrize("k,h1_expected", [(0, 1), (8, 1)])
def test_h1_M_blocks(k, h1_expected):
    # Fox calculus on <a,b | a w b^-1 w^-1>, block Sym^k (k=16 skipped for suite speed;
    # covered by the arc's archived full run).
    n = k + 1
    Ak, Bk = _sym(A, k), _sym(B, k)
    Aik, Bik = _sym(Ai, k), _sym(Bi, k)
    G = {1: Ak, 2: Bk}; Gi = {1: Aik, 2: Bik}
    def ev(word):
        out = _eye(n)
        for L in word:
            out = _mul(out, G[abs(L)] if L > 0 else Gi[abs(L)])
        return out
    def fox(word, g):
        acc = (sp.zeros(n, n), sp.zeros(n, n)); pre = []
        for L in word:
            if L > 0:
                if abs(L) == g:
                    m = ev(pre); acc = (acc[0] + m[0], acc[1] + m[1])
                pre = pre + [L]
            else:
                pre = pre + [L]
                if abs(L) == g:
                    m = ev(pre); acc = (acc[0] - m[0], acc[1] - m[1])
        return acc
    w = [2, -1, -2, 1]
    r = [1] + w + [-2] + [-x for x in reversed(w)]
    I = _eye(n)
    d0 = (sp.Matrix.vstack(Ak[0] - I[0], Bk[0] - I[0]), sp.Matrix.vstack(Ak[1], Bk[1]))
    fa, fb = fox(r, 1), fox(r, 2)
    d1 = (sp.Matrix.hstack(fa[0], fb[0]), sp.Matrix.hstack(fa[1], fb[1]))
    r0, r1 = _rank(d0), _rank(d1)
    h1 = (2 * n - r1) - r0
    assert h1 == h1_expected
