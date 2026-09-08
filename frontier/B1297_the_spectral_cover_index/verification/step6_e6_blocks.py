"""PREREG §5(a): exhibit the trinification block structure of the 27 and the order-3 element of W(E6) permuting the blocks.
E6 in the SL(3)^3 frame: roots = A2^3 roots (18) + weights of (3,3,3) (27) + weights of (3b,3b,3b) (27) = 72;
27 = (3,3b,1) + (1,3,3b) + (3b,1,3).  sigma: (x,y,z) -> (z,x,y).  Exact rational arithmetic."""
from fractions import Fraction as Fr
import itertools
def eps(i):                       # weights of the 3 of SL(3) in the traceless hyperplane of Q^3
    v = [Fr(0)] * 3; v[i] = Fr(1); return [x - Fr(1, 3) for x in v]
Z3 = [Fr(0)] * 3
def cat(*parts): return tuple(x for p in parts for x in p)
def dot(u, v): return sum(a * b for a, b in zip(u, v))
def add(u, v): return tuple(a + b for a, b in zip(u, v))
def sub(u, v): return tuple(a - b for a, b in zip(u, v))
def neg(u): return tuple(-a for a in u)
def scale(u, c): return tuple(a * c for a in u)
A2 = [sub(tuple(eps(i)), tuple(eps(j))) for i in range(3) for j in range(3) if i != j]
roots = set()
for f in range(3):
    for r in A2:
        parts = [Z3, Z3, Z3]; parts[f] = list(r); roots.add(cat(*parts))
for i, j, k in itertools.product(range(3), repeat=3):
    w = cat(eps(i), eps(j), eps(k)); roots.add(w); roots.add(neg(w))
roots = sorted(roots)
print("number of roots:", len(roots), " all norm^2 = 2:", all(dot(r, r) == 2 for r in roots))
def refl(a, b): return sub(b, scale(a, dot(a, b)))          # norm^2 2  =>  <b, a^vee> = a.b
closed = all(refl(a, b) in set(roots) for a in roots for b in roots)
print("closed under reflections:", closed)
# rank and Cartan type: simple roots from a generic functional
gen = tuple(Fr(p) for p in (97, 89, 83, 79, 73, 71, 67, 61, 59))
pos = [r for r in roots if dot(gen, r) > 0]
possum = set(add(a, b) for a in pos for b in pos)
simple = [r for r in pos if r not in possum]
print("positive roots:", len(pos), " simple roots:", len(simple))
C = [[dot(a, b) for b in simple] for a in simple]
degs = sorted(sum(1 for j in range(6) if i != j and C[i][j] != 0) for i in range(6))
import sympy
detC = sympy.Matrix(C).det()
print("Cartan matrix node degrees:", degs, " det:", detC, "  (E6: degrees [1,1,1,2,2,3], det 3)")
assert len(roots) == 72 and closed and len(simple) == 6 and degs == [1, 1, 1, 2, 2, 3] and detC == 3
# the 27 in blocks
B1 = [cat(eps(i), neg(tuple(eps(j))), Z3) for i in range(3) for j in range(3)]      # (3, 3b, 1)
B2 = [cat(Z3, eps(j), neg(tuple(eps(k)))) for j in range(3) for k in range(3)]      # (1, 3, 3b)
B3 = [cat(neg(tuple(eps(i))), Z3, eps(k)) for i in range(3) for k in range(3)]      # (3b, 1, 3)
W27 = B1 + B2 + B3
print("27 weights:", len(set(W27)), " norm^2:", set(dot(w, w) for w in W27), " minuscule (<w,a> in {-1,0,1}):", all(dot(w, a) in (-1, 0, 1) for w in W27 for a in roots))
# single Weyl orbit
orbit = {W27[0]}; frontier = [W27[0]]
while frontier:
    new = []
    for w in frontier:
        for a in simple:
            v = refl(a, w)
            if v not in orbit: orbit.add(v); new.append(v)
    frontier = new
print("W-orbit of one weight has size", len(orbit), " and equals the 27:", orbit == set(W27))
# sigma: cyclic permutation of the three SL(3) factors
def sigma(v): return cat(v[6:9], v[0:3], v[3:6])
print("sigma preserves the roots:", set(map(sigma, roots)) == set(roots))
print("sigma maps 27 -> 27 (not 27bar):", set(map(sigma, W27)) == set(W27), "; 27 -> 27bar?", set(map(sigma, W27)) == set(map(neg, W27)))
print("sigma on blocks: B1->B2", set(map(sigma, B1)) == set(B2), " B2->B3", set(map(sigma, B2)) == set(B3), " B3->B1", set(map(sigma, B3)) == set(B1))
print("sigma^3 = id:", all(sigma(sigma(sigma(v))) == v for v in roots), " order 3 (sigma != id):", any(sigma(v) != v for v in roots))
# exhibit sigma as a Weyl word: walk sigma(v_generic) back into the dominant chamber
def proj(u):                     # project onto the root span: remove the trace part of each factor
    out = []
    for f in range(3):
        blk = u[3*f:3*f+3]; m = sum(blk) / 3; out += [x - m for x in blk]
    return tuple(out)
v = proj(gen); wv = proj(sigma(v)); word = []
while True:
    i = next((i for i, a in enumerate(simple) if dot(wv, a) < 0), None)
    if i is None: break
    wv = refl(simple[i], wv); word.append(i)
print("sigma in W(E6):", wv == v, " reduced word length (as product of simple reflections):", len(word), " word:", word)
assert wv == v
# and it acts: the three A2 factors are permuted (root subsystems), the diagonal fixed space has dim 2
fixed_dim = 9 - sympy.Matrix([[ (1 if i == j else 0) - (1 if sigma(tuple(Fr(int(k == i)) for k in range(9)))[j] else 0) for j in range(9)] for i in range(9)]).rank()
print("dim of sigma's fixed subspace in Q^9:", fixed_dim, " (within the E6 Cartan: 2)")
print("E6 BLOCKS: PASS")
