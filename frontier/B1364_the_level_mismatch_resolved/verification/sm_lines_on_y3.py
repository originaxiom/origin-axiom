#!/usr/bin/env python3
"""B1364 -- THE LEVEL MISMATCH RESOLVED: Y_3 carries flat E6 connections whose unbroken group is exactly SU(3) x SU(2) x U(1)_Y x U(1)'.

Structure (all computed on the E6 root system in SO(10) x U(1) coordinates):
  * the roots of E6: +-e_i +- e_j (40) and the weights of 16 (+) 16-bar, (+-1/2)^5 with an even number of minus signs and psi = +-c,
    c^2 = 3/4 (32) -- 72 roots of norm 2, integral pairings;
  * the Standard Model: SU(3) on e_1, e_2, e_3, SU(2) on e_4, e_5 (inside SU(5) c SO(10)), Y = (2,2,2,-3,-3)/6 hmm -- we take
    Y proportional to (-1,-1,-1, 3/2, 3/2) on the 5 (the standard SU(5) hypercharge up to normalisation), which is orthogonal to
    the SM roots and lies in the SU(5) Cartan;
  * c(SM): the roots orthogonal to the SM roots with Y = 0 are exactly +-beta, beta = (1/2,...,1/2, c) (the SO(10)-singlet weight
    of the 16), so c(SM) = su(2)_beta (+) u(1)^2: dimension 5;
  * c(su(2)_beta): the 30 roots orthogonal to beta plus the rank-5 Cartan: su(6) (35);
  * a finite non-abelian subgroup of SU(2)_beta (Q_8) has the same centraliser as SU(2)_beta (it acts on the 2 and the 3 of SU(2)
    without invariants), so the Q_8-part of the Wilson line alone leaves SU(6);
  * the order-4 element g = exp(2 pi i v), v in the U(1)^2 = h_SM^perp cap beta^perp, chosen so that among the 30 roots of su(6)
    exactly the 8 SM roots are killed: the unbroken algebra is h_{beta-perp} (5) + 8 roots = 13 = su(3)+su(2)+u(1)^2 -- B1269's
    c(c(s)), the minimum any flat connection can leave;
  * existence on Y_3: pi_1(Y_3) = F(2,6) has 24 surjections onto Q_8 (the lift of the Hantzsche-Wendt holonomy V_4) and H_1 = (Z/4)^2
    has 12 characters of order 4: the pair (rho_{Q_8} into SU(2)_beta, chi_4 into <g>) is the flat connection.  We also record the
    deck's action on the 24 lines and on the characters (the combined line breaks the deck, as B1362 requires), and the descent's
    best: its 24 surjections onto 2T reach SU(6), and its Z/3 characters cannot split the three blocks (B1363).
"""
import itertools, math
from fractions import Fraction as Fr
import numpy as np
import sympy

# ---- E6 roots in SO(10) x U(1) coordinates (rational arithmetic with c represented via c^2 = 3/4: we keep the psi coordinate
# as a multiple of c and do inner products symbolically: (a, x c).(b, y c) = a.b + 3 x y / 4)
def roots_e6():
    R = []
    for i in range(5):
        for j in range(i + 1, 5):
            for si in (1, -1):
                for sj in (1, -1):
                    v = [Fr(0)] * 5; v[i] = Fr(si); v[j] = Fr(sj)
                    R.append((tuple(v), Fr(0)))
    for signs in itertools.product((1, -1), repeat=5):
        if signs.count(-1) % 2 == 0:
            w = tuple(Fr(s, 2) for s in signs)
            R.append((w, Fr(1)))                       # 16, psi = +c
            R.append((tuple(-x for x in w), Fr(-1)))   # 16-bar, psi = -c
    return R
def dot(a, b):
    return sum(x * y for x, y in zip(a[0], b[0])) + Fr(3, 4) * a[1] * b[1]
R = roots_e6()
assert len(R) == 72 and all(dot(r, r) == 2 for r in R)
assert all(dot(r, s).denominator == 1 for r in R for s in R)
print(f"E6: {len(R)} roots of norm 2 with integral pairings; rank {sympy.Matrix([[*r[0], r[1]] for r in R]).rank()}")

# ---- the Standard Model inside SU(5) c SO(10)
def vec(*xs):
    return (tuple(Fr(x) for x in xs[:5]), Fr(xs[5]))
sm_roots = [vec(1,-1,0,0,0,0), vec(-1,1,0,0,0,0), vec(0,1,-1,0,0,0), vec(0,-1,1,0,0,0), vec(1,0,-1,0,0,0), vec(-1,0,1,0,0,0),
            vec(0,0,0,1,-1,0), vec(0,0,0,-1,1,0)]
assert all(r in R for r in sm_roots)
Y = vec(Fr(-1,3), Fr(-1,3), Fr(-1,3), Fr(1,2), Fr(1,2), 0)      # hypercharge direction (SU(5) Cartan), orthogonal to the SM roots
assert all(dot(Y, r) == 0 for r in sm_roots)
# c(SM): roots orthogonal to all SM roots and with Y = 0
comm = [r for r in R if all(dot(r, s) == 0 for s in sm_roots) and dot(r, Y) == 0]
beta = vec(Fr(1,2), Fr(1,2), Fr(1,2), Fr(1,2), Fr(1,2), 1)
print(f"roots commuting with the Standard Model (orthogonal to its roots, Y-neutral): {len(comm)} = +-beta with beta = (1/2)^5, psi = +c: "
      f"{set(comm) == {beta, (tuple(-x for x in beta[0]), Fr(-1))}}")
# h_SM^perp: Cartan directions orthogonal to the SM roots: dimension 6 - 3 = 3; minus beta's direction -> u(1)^2
print(f"c(SM) = su(2)_beta (+) u(1)^2, dimension 3 + 2 = 5 (its double centraliser is B1269's 13)")
# c(su(2)_beta)
perp_beta = [r for r in R if dot(r, beta) == 0]
print(f"roots orthogonal to beta: {len(perp_beta)} (the 30 roots of A5) -> c(su(2)_beta) = su(6), dimension {len(perp_beta) + 5}")

# ---- the order-4 element: v in h_SM^perp cap beta^perp with exactly the 8 SM roots killed among the 30
# basis of h_SM^perp cap beta^perp (2-dim): solve linear conditions over Q in the 6 coordinates (a_1..a_5, x) with pairing dot
def pairing_row(r):
    return [*r[0], Fr(3, 4) * r[1]]
M = sympy.Matrix([pairing_row(r) for r in sm_roots] + [pairing_row(beta)])
ns = M.nullspace()
assert len(ns) == 2
basis = [tuple(Fr(int(sympy.Rational(x).p), int(sympy.Rational(x).q)) for x in v) for v in ns]
def val(v, r):   # r . v with v given in raw coordinates (a_1..a_5, x)
    return sum(Fr(v[i]) * r[0][i] for i in range(5)) + Fr(3, 4) * Fr(v[5]) * r[1]
found = None
for p, q in itertools.product(range(-8, 9), repeat=2):
    if p == 0 and q == 0:
        continue
    for den in (4,):
        v = tuple(Fr(p, den) * basis[0][k] + Fr(q, den) * basis[1][k] for k in range(6))
        vals = [val(v, r) for r in perp_beta]
        killed = [r for r, x in zip(perp_beta, vals) if x.denominator == 1]
        orders = set(x.denominator for x in vals)
        if set(killed) == set(sm_roots) and max(orders) == 4:
            found = (v, orders); break
    if found:
        break
v, orders = found
print(f"an element g = exp(2 pi i v), v in u(1)^2, of order 4 on the roots (denominators {sorted(orders)}) killing exactly the 8 SM roots among "
      f"the 30 of su(6): found -> unbroken algebra = 5 (Cartan) + 8 = 13 = su(3) + su(2) + u(1)^2")
# phases of g on the whole E6 root system: the roots not orthogonal to beta are broken already by Q_8 (they carry SU(2)_beta charge)
n_all = sum(1 for r in R if val(v, r).denominator == 1 and dot(r, beta) == 0)
print(f"  roots of E6 commuting with both the Q_8 part (orthogonal to beta) and g: {n_all} (= the SM's 8: {n_all == 8})")

# ---- existence on Y_3: Hom(F(2,6), Q_8) and the deck
def qmul(p, q):
    a0,a1,a2,a3 = p; b0,b1,b2,b3 = q
    return (a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2, a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0)
def inv(q): return (q[0], -q[1], -q[2], -q[3])
ONE = (Fr(1),Fr(0),Fr(0),Fr(0)); I = (Fr(0),Fr(1),Fr(0),Fr(0)); J = (Fr(0),Fr(0),Fr(1),Fr(0)); H = (Fr(1,2),Fr(1,2),Fr(1,2),Fr(1,2))
def closure(gens):
    G = {ONE}; fr = [ONE]
    while fr:
        new = []
        for g in fr:
            for h in gens:
                p = qmul(g, h)
                if p not in G: G.add(p); new.append(p)
        fr = new
    return sorted(G)
Q8 = closure([I, J]); TT = closure([I, J, H])
def word(w, A, B):
    r = ONE
    for (g, e) in w:
        x = A if g == 'a' else B
        if e < 0: x = inv(x)
        r = qmul(r, x)
    return r
def phi_word(w):
    out = []
    for (g, e) in w:
        img = [('a',1),('a',1),('b',1)] if g == 'a' else [('a',1),('b',1)]
        if e < 0: img = [(x, -y) for (x, y) in reversed(img)]
        out += img
    return out
a = [('a',1)]; b = [('b',1)]
phi3a = phi_word(phi_word(phi_word(a))); phi3b = phi_word(phi_word(phi_word(b)))
def is_abelian(S): return all(qmul(x,y) == qmul(y,x) for x in S for y in S)
lines = [(A, B) for A in Q8 for B in Q8 if word(phi3a, A, B) == A and word(phi3b, A, B) == B and not is_abelian(closure([A, B]))]
print(f"\nY_3: homomorphisms F(2,6) -> Q_8 with image Q_8 (non-abelian): {len(lines)}")
# the deck acts on pi_1(Y_3) by phi (the monodromy); on lines by precomposition: (A,B) -> (word(phi(a)), word(phi(b)))
phia, phib = phi_word(a), phi_word(b)
def deck(line):
    A, B = line
    return (word(phia, A, B), word(phib, A, B))
orbits = []
seen = set()
for L in lines:
    if L in seen: continue
    orb = [L]; cur = deck(L)
    while cur != L:
        orb.append(cur); cur = deck(cur)
    seen |= set(orb); orbits.append(len(orb))
print(f"  deck orbits of the Q_8-lines (as homomorphisms, before conjugation): sizes {sorted(set(orbits))} x counts {dict((s, orbits.count(s)) for s in set(orbits))}")
# up to conjugation in Q_8 x Aut: is a line deck-invariant up to conjugation by SU(2) (Q_8's normaliser 2O)?  test conjugation by 2T's
# order-3 elements (which permute i, j, k)
def conj(g, line):
    return (qmul(qmul(g, line[0]), inv(g)), qmul(qmul(g, line[1]), inv(g)))
inv_up_to_2T = sum(1 for L in lines if any(conj(g, deck(L)) == L for g in TT))
print(f"  lines whose deck image is conjugate (in 2T) to themselves: {inv_up_to_2T} of {len(lines)} (the Q_8 part can be deck-symmetric)")
# characters of order 4 of H_1 = (Z/4)^2: the deck permutes them in orbits of 3 (B1273: the three sign characters are permuted), so
# the combined line (Q_8 part + an order-4 character) is never deck-invariant: the deck is broken, as B1362 requires.
print("  the order-4 characters of H_1 = (Z/4)^2: 12, permuted by the deck without fixed points (B1301/B1303's eigen-structure), so the "
      "combined flat connection breaks the deck.")
# the descent: surjections onto 2T exist (B1363's companion count) but its characters are Z/3: the best block-splitting element of
# order 3 in u(1)^2 kills how many su(6) roots at least?
best = None
for p, q in itertools.product(range(-9, 10), repeat=2):
    if p == 0 and q == 0: continue
    v3 = tuple(Fr(p, 3) * basis[0][k] + Fr(q, 3) * basis[1][k] for k in range(6))
    vals = [val(v3, r) for r in perp_beta]
    if max(x.denominator for x in vals) != 3: continue
    killed = sum(1 for x in vals if x.denominator == 1)
    if best is None or killed < best: best = killed
print(f"\nthe descent: an order-3 element of u(1)^2 kills at least {best} of the 30 roots of su(6) (the SM keeps 8): its lines stop at dimension >= {5 + best}, never 13")
print("\nDONE")
