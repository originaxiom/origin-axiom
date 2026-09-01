#!/usr/bin/env python3
"""R12: exact re-run of the full selection argument using the beat REPRESENTATIVE
derived independently from snappy's m000 holonomy (beat_derivation.py):
    beat'(a) = a,  beat'(b) = b a b^-1,   sigma'^2 = a
(the transported odd element was W' = -[[1, -conj(omega)],[0,1]], with
 W' conj(W') = A numerically). If the selection verdict (untwisted extends,
twisted killed by |lambda|^2 = -1) agrees with the banked-beat verdict, the
claim is representative-independent — the Gieseking side genuinely pays for
exactly one spin structure.
"""
import sympy as sp
from sympy import I, Rational, sqrt, conjugate, Matrix, eye, zeros

w = Rational(-1, 2) + sqrt(3) * I / 2
A = Matrix([[1, 1], [0, 1]])
B = Matrix([[1, 0], [-w, 1]])

def S(M):
    return M.applyfunc(lambda e: sp.simplify(sp.expand(e)))

def conjM(M):
    return M.applyfunc(lambda e: sp.simplify(conjugate(sp.expand(e))))

def wtm(word, Ma, Mb):
    d = {'a': Ma, 'b': Mb, 'A': Ma.inv(), 'B': Mb.inv()}
    M = eye(2)
    for ch in word:
        M = S(M * d[ch])
    return M

BEAT2 = {'a': 'a', 'b': 'baB'}
def beat_word(word):
    inv = {'a': 'A', 'b': 'B', 'A': 'a', 'B': 'b'}
    out = []
    for ch in word:
        if ch in 'ab':
            out.append(BEAT2[ch])
        else:
            img = BEAT2[inv[ch]]
            out.append(''.join(inv[c] for c in reversed(img)))
    return ''.join(out)

RELATOR = "abABaBAbaB"
print("beat' respects relator:", wtm(beat_word(RELATOR), A, B) == eye(2))

t_a = wtm(BEAT2['a'], A, B)
t_b = wtm(BEAT2['b'], A, B)

w11, w12, w21, w22 = sp.symbols('w11 w12 w21 w22')
W = Matrix([[w11, w12], [w21, w22]])

def decide(eps):
    """eps in {+1,-1}: the lift with chi(a)=chi(b)=eps. Returns verdict string."""
    La, Lb = eps * A, eps * B
    ta = wtm(BEAT2['a'], La, Lb)
    tb = wtm(BEAT2['b'], La, Lb)
    es = []
    for Mg, tg in ((La, ta), (Lb, tb)):
        E = S(W * conjM(Mg) - tg * W)
        es += [E[i, j] for i in range(2) for j in range(2)]
    Mx, _ = sp.linear_eq_to_matrix(es, [w11, w12, w21, w22])
    Mx = S(Mx)
    rk = Mx.rank(); ns = Mx.nullspace()
    if len(ns) != 1:
        return f"rank {rk}, nullspace {len(ns)} (not a line)"
    v = ns[0]
    Wx = S(Matrix([[v[0], v[1]], [v[2], v[3]]]))
    dd = sp.simplify(Wx.det())
    Wx = S(Wx / sp.sqrt(dd))
    sq = S(Wx * conjM(Wx))
    # sigma'^2 = a, so the square must equal rho_eps(a) = eps*A for some lambda:
    # (lam Wx) conj(lam Wx) = |lam|^2 sq ; need |lam|^2 * s = eps where sq = s * (eps-independent A)
    s = sp.simplify(sq[0, 0] / A[0, 0])
    assert S(sq - s * A) == zeros(2), "square not proportional to A"
    need = sp.simplify(sp.Integer(eps) / s)
    tag = "EXTENDS" if need == 1 else f"KILLED (|lambda|^2 = {need})"
    return f"rank {rk}, nullspace 1, W0 = {Wx.tolist()}, W0 conj(W0) = {s}*A -> {tag}"

for eps in (1, -1):
    print(f"lift chi(a)=chi(b)={eps:+d}:", decide(eps))
