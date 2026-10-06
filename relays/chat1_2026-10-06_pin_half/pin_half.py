"""Which half of the 2T door is Pin⁺ — in sm:B1382's presentation, deck and convention (PREREG f985053d)."""
import itertools, sympy as sp

# ---------- Q2 (control, part 1): Riley's holonomy satisfies B1382's relator exactly ----------
om = sp.Symbol('om')
def red(e): return sp.expand(sp.rem(sp.expand(e), om**2 + om + 1, om))
A = sp.Matrix([[1, 1], [0, 1]]); B = sp.Matrix([[1, 0], [-om, 1]])
SYM = {'a': A, 'A': A.adjugate(), 'b': B, 'B': B.adjugate()}
REL = 'abABaBAbaB'
def evs(word):
    M = sp.eye(2)
    for c in word: M = (M * SYM[c]).applyfunc(red)
    return M
print(f"Q2  relator {REL} exact over Z[omega] for Riley: {evs(REL) == sp.eye(2)}")
W = sp.Matrix([[1, -om], [0, 1]])
Wbar = W.subs(om, -1 - om).applyfunc(red)
print(f"    B1382's W = [[1,-w],[0,1]]: W*conj(W) = +A : {(W*Wbar).applyfunc(red) == A}")

# ---------- SL(2,3) ----------
p = 3
def mul(g, h):
    a, b, c, d = g; e, f, x, y = h
    return ((a*e+b*x) % p, (a*f+b*y) % p, (c*e+d*x) % p, (c*f+d*y) % p)
def det(g): return (g[0]*g[3]-g[1]*g[2]) % p
def inv(g):
    a, b, c, d = g; di = pow(det(g), -1, p)
    return ((d*di) % p, (-b*di) % p, (-c*di) % p, (a*di) % p)
I = (1, 0, 0, 1); NEG = (2, 0, 0, 2)
SL = [g for g in itertools.product(range(p), repeat=4) if det(g) == 1]
GLm = [g for g in itertools.product(range(p), repeat=4) if det(g) == 2]
def gsize(gs):
    S = {I}; fr = [I]
    while fr:
        x = fr.pop()
        for g in gs:
            y = mul(x, g)
            if y not in S: S.add(y); fr.append(y)
    return len(S)
def ev(word, val):
    r = I
    for c in word: r = mul(r, val[c.lower()] if c.islower() else inv(val[c.lower()]))
    return r
BEAT = {'a': 'a', 'b': 'BabAb'}          # b -> b^-1 a b a^-1 b

# ---------- Q1: all surjections, the deck, and the two halves ----------
S = []
for va, vb in itertools.product(SL, repeat=2):
    val = {'a': va, 'b': vb}
    if ev(REL, val) == I and gsize([va, vb]) == 24: S.append(val)
def deck(psi): return {g: ev(BEAT[g], psi) for g in 'ab'}
def classify(psi):
    d = deck(psi)
    As = [X for X in SL if all(mul(mul(X, psi[g]), inv(X)) == d[g] for g in 'ab')]
    if As:
        sq = {mul(X, X) for X in As}
        if psi['a'] in sq: return 'Pin+', As
        if mul(NEG, psi['a']) in sq: return 'Pin-', As
        return 'neither-sign', As
    if any(all(mul(mul(Y, psi[g]), inv(Y)) == d[g] for g in 'ab') for Y in GLm): return 'outer', []
    return 'none', []
from collections import Counter
cls = [classify(psi)[0] for psi in S]
print(f"\nQ1  surjections onto 2T: {len(S)}   halves: {dict(Counter(cls))}")
chi = {'a': NEG, 'b': NEG}                # m004's Z/2 character: a, b both meridians
sw = sum(classify({g: mul(chi[g], psi[g]) for g in 'ab'})[0] != c for psi, c in zip(S, cls))
print(f"    psi -> psi (x) chi changes the half in {sw} of {len(S)}")

# ---------- Q2 (control, part 2) and Q3: the geometric reductions ----------
psi1 = {'a': (1, 1, 0, 1), 'b': (1, 0, 2, 1)}      # rho1 mod sqrt(-3): omega -> 1, -omega -> -1 = 2
psi2 = {g: mul(NEG, psi1[g]) for g in 'ab'}         # rho2 = (-A, -B)
W3 = (1, 2, 0, 1)                                   # [[1,-omega],[0,1]] mod sqrt(-3)
print(f"\nQ2  psi1 is a surjection: {any(all(s[g] == psi1[g] for g in 'ab') for s in S)}")
print(f"    W3 intertwines psi1 with psi1 o beat: {all(mul(mul(W3, psi1[g]), inv(W3)) == deck(psi1)[g] for g in 'ab')}")
c1, As1 = classify(psi1); c2, _ = classify(psi2)
print(f"\nQ3  psi1 (reduction of the Pin⁺ lift rho1, tr mu = +2): {c1}    W3^2 = +psi1(a): {mul(W3, W3) == psi1['a']}")
print(f"    psi2 (reduction of rho2 = (-A,-B), tr mu = -2)    : {c2}")
print(f"    Q3: {'PASS' if (c1, c2) == ('Pin+', 'Pin-') and mul(W3, W3) == psi1['a'] else 'KILL'}")
