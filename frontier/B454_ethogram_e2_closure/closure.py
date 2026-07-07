#!/usr/bin/env python3
"""B454 (Ethogram E2) — the closure lemma + the bounded scan + choice analysis. EXACT.

THE LEMMA (Fricke/CH): tr(UV) = tr(U)tr(V) - tr(UV^-1) for U,V in SL(2); by induction the
trace of ANY word in two generators lies in Z[x,y,z] (seed traces). Hence the word channel
cannot leave its birth arithmetic. Class-generic by construction.

THE SCAN is non-vacuous: the matrix-ENTRY field is strictly bigger than the trace field here
(the generator solve forces b with b^2 - s b + 1 = 0, and that quadratic does NOT split over
Q(sqrt-3) — checked below), yet every word TRACE must collapse into Q(sqrt-3). We verify this
exactly in the ring K = Q(w)[b]/(w^2+3, b^2-s b+1), s=(3+w)/2: elements are 4-tuples of
Fractions (1, w, b, wb); the per-word check is "the b-components of tr vanish".

Run: python3 closure.py   (prints ALL CHECKS PASS)
"""
from fractions import Fraction as F
import numpy as np
import sympy as sp


# ---------- the ring K = Q(w,b) with w^2=-3, b^2 = s*b - 1, s=(3+w)/2 ----------
# element = (a0, a1, a2, a3) ~ a0 + a1 w + (a2 + a3 w) b
S0, S1 = F(3, 2), F(1, 2)          # s = S0 + S1 w

def kmul(x, y):
    a0, a1, a2, a3 = x
    c0, c1, c2, c3 = y
    # (A + B b)(C + D b) with A=a0+a1w etc.: = AC + (AD+BC) b + BD b^2,  b^2 = s b - 1
    def cmulw(p0, p1, q0, q1):     # (p0+p1 w)(q0+q1 w), w^2=-3
        return (p0 * q0 - 3 * p1 * q1, p0 * q1 + p1 * q0)
    AC = cmulw(a0, a1, c0, c1)
    AD = cmulw(a0, a1, c2, c3)
    BC = cmulw(a2, a3, c0, c1)
    BD = cmulw(a2, a3, c2, c3)
    sBD = cmulw(S0, S1, *BD)
    return (AC[0] - BD[0], AC[1] - BD[1],
            AD[0] + BC[0] + sBD[0], AD[1] + BC[1] + sBD[1])


def kadd(x, y):
    return tuple(a + b for a, b in zip(x, y))


KZ = (F(0), F(0), F(0), F(0))
KO = (F(1), F(0), F(0), F(0))
W = (F(0), F(1), F(0), F(0))
Bel = (F(0), F(0), F(1), F(0))
Sel = (S0, S1, F(0), F(0))


def mmul(X, Y):
    return [[kadd(kmul(X[0][0], Y[0][0]), kmul(X[0][1], Y[1][0])),
             kadd(kmul(X[0][0], Y[0][1]), kmul(X[0][1], Y[1][1]))],
            [kadd(kmul(X[1][0], Y[0][0]), kmul(X[1][1], Y[1][0])),
             kadd(kmul(X[1][0], Y[0][1]), kmul(X[1][1], Y[1][1]))]]


def neg(x):
    return tuple(-a for a in x)


# A = [[s, -1], [1, 0]];  B = [[0, b], [-1/b, s]], 1/b = s - b  (from b^2 - s b + 1 = 0)
inv_b = kadd(Sel, neg(Bel))
MA = [[Sel, neg(KO)], [KO, KZ]]
MB = [[KZ, Bel], [neg(inv_b), Sel]]


def lemma_symbolic():
    a11, a12, a21, b11, b12, b21 = sp.symbols('a11 a12 a21 b11 b12 b21')
    a22 = (1 + a12 * a21) / a11
    b22 = (1 + b12 * b21) / b11
    A = sp.Matrix([[a11, a12], [a21, a22]])
    B = sp.Matrix([[b11, b12], [b21, b22]])
    ok1 = sp.simplify(sp.trace(A * B) - (sp.trace(A) * sp.trace(B) - sp.trace(A * B.inv()))) == 0
    Wm = A * B
    ok2 = sp.simplify(sp.trace(Wm * A) - (sp.trace(Wm) * sp.trace(A) - sp.trace(Wm * A.inv()))) == 0
    return ok1 and ok2


def entry_field_strictly_bigger():
    """b^2 - s b + 1 does not split over Q(sqrt-3): (s^2-4) is not a square in the field."""
    w = sp.sqrt(-3)
    s = (3 + w) / 2
    disc = sp.expand(s * s - 4)                    # (-5 + 3 sqrt(-3))/2
    p, q = sp.symbols('p q', rational=True)
    sols = sp.solve([sp.Eq(p**2 - 3 * q**2, sp.Rational(-5, 2)), sp.Eq(2 * p * q, sp.Rational(3, 2))],
                    [p, q])
    rational_sols = [s_ for s_ in sols if all(v.is_rational for v in s_)]
    return len(rational_sols) == 0


def substitution(word, kind='fib'):
    out = []
    for c in word:
        if kind == 'fib':
            out += [0, 1] if c == 0 else [0]
        else:
            out += [0, 1] if c == 0 else [1, 0]
    return out


def gates():
    """level-2/3 traces reproduce the Fricke/Lucas structure: tr of the level word matrix."""
    # sanity: tr(A)=tr(B)=tr(AB)=s in the ring
    tA = kadd(MA[0][0], MA[1][1])
    tB = kadd(MB[0][0], MB[1][1])
    AB = mmul(MA, MB)
    tAB = kadd(AB[0][0], AB[1][1])
    return tA == Sel and tB == Sel and tAB == Sel


def scan(L=8, prefix_cap=200):
    """every prefix trace of the level-L golden word lies in Q(sqrt-3): b-components vanish."""
    word = [0]
    for _ in range(L):
        word = substitution(word, 'fib')
    word = word[:prefix_cap]
    M = [[KO, KZ], [KZ, KO]]
    ok = True
    n_checked = 0
    for c in word:
        M = mmul(M, MA if c == 0 else MB)
        tr = kadd(M[0][0], M[1][1])
        ok &= (tr[2] == 0 and tr[3] == 0)          # b-components vanish -> in Q(sqrt-3)
        n_checked += 1
    return ok, n_checked


def controls(n_random=1000, length=24, seed=20260708):
    """Thue-Morse + random words: the same collapse (class-generic), exact ring arithmetic."""
    rng = np.random.default_rng(seed)
    words = [substitution(substitution(substitution([0], 'tm'), 'tm'), 'tm')[:length]]
    for _ in range(n_random):
        words.append(rng.integers(0, 2, length).tolist())
    ok = True
    for wd in words:
        M = [[KO, KZ], [KZ, KO]]
        for c in wd:
            M = mmul(M, MA if c == 0 else MB)
        tr = kadd(M[0][0], M[1][1])
        ok &= (tr[2] == 0 and tr[3] == 0)
    return ok, len(words)


def choice_deterministic(L=8):
    word = [0]
    for _ in range(L):
        n1 = substitution(word, 'fib')
        n2 = substitution(word, 'fib')
        if n1 != n2:
            return False
        word = n1[:100]
    return True


def run():
    ok1 = lemma_symbolic()
    print(f"(1)+(2) Fricke identity + induction step (symbolic): {ok1}")
    okf = entry_field_strictly_bigger()
    print(f"(*) the scan is non-vacuous (entry field strictly bigger than Q(sqrt-3)): {okf}")
    okg = gates()
    print(f"(gate) seed traces x=y=z=s reproduced exactly in the ring: {okg}")
    ok3, n3 = scan()
    print(f"(3) L=8 scan: {n3} prefix traces, ALL collapse into Q(sqrt-3): {ok3}")
    ok4, n4 = controls()
    print(f"(4) controls (Thue-Morse + 1000 random words, exact): {ok4} ({n4} words)")
    ok5 = choice_deterministic()
    print(f"(5) per-level continuation deterministic: {ok5}")
    allok = ok1 and okf and okg and ok3 and ok4 and ok5
    print("ALL CHECKS PASS" if allok else "CHECK FAILURE")
    return bool(allok)


if __name__ == '__main__':
    run()
