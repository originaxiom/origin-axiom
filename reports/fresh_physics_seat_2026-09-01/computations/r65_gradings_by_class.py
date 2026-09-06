"""R65 -- B1264's 170 trinification labellings classified by E6 conjugacy class (centralizer dimension). Exact."""
import itertools, collections
from fractions import Fraction as Fr
C = [[ 2, 0,-1, 0, 0, 0],[ 0, 2, 0,-1, 0, 0],[-1, 0, 2,-1, 0, 0],[ 0,-1,-1, 2,-1, 0],[ 0, 0, 0,-1, 2,-1],[ 0, 0, 0, 0,-1, 2]]
# roots in simple-root coordinates (string algorithm), 27 weights in fundamental coordinates (Weyl orbit of omega_1)
simple = [tuple(int(i == j) for j in range(6)) for i in range(6)]
pos, fr = set(simple), list(simple)
def pairing(beta, i): return sum(beta[j]*C[j][i] for j in range(6))
while fr:
    beta = fr.pop()
    for i in range(6):
        p, b = 0, list(beta); b[i] -= 1
        while tuple(b) in pos: p += 1; b[i] -= 1
        if p - pairing(beta, i) > 0:
            nb = list(beta); nb[i] += 1; nb = tuple(nb)
            if nb not in pos: pos.add(nb); fr.append(nb)
roots = list(pos) + [tuple(-c for c in r) for r in pos]; assert len(roots) == 72
def reflect(wt, i): return tuple(wt[j] - wt[i]*C[i][j] for j in range(6))
w0 = tuple(int(j == 0) for j in range(6)); W27, fr = {w0}, [w0]
while fr:
    v = fr.pop()
    for i in range(6):
        u = reflect(v, i)
        if u not in W27: W27.add(u); fr.append(u)
W27 = sorted(W27); assert len(W27) == 27
# exact inverse Cartan
import sympy as sp
Cinv = sp.Matrix(C).inv()
CinvF = [[Fr(int(Cinv[i,j].p), int(Cinv[i,j].q)) for j in range(6)] for i in range(6)]
def pair_weight(lam, c):   # <lambda, h_c> = lambda . C^-1 . c   (B1264's formula)
    coef = [sum(CinvF[j][i]*c[i] for i in range(6)) for j in range(6)]
    return sum(Fr(lam[j])*coef[j] for j in range(6))
def pair_root(alpha, c):   # <alpha, h_c> = sum c_i * (alpha_i-coefficient)
    return sum(c[i]*alpha[i] for i in range(6))
rows = []
for c in itertools.product(range(3), repeat=6):
    if not any(c): continue
    vals = [pair_weight(l, c) for l in W27]
    if any(v.denominator != 1 for v in vals): continue
    res = tuple(int(v) % 3 for v in vals)
    if sorted(collections.Counter(res).values()) != [9, 9, 9]: continue
    cdim = 6 + sum(1 for a in roots if pair_root(a, c) % 3 == 0)
    colouring = min(tuple(p[x] for x in res) for p in itertools.permutations(range(3)))
    rows.append((c, cdim, colouring))
print(f"labellings splitting the 27 as 9+9+9: {len(rows)} (B1264: 170); distinct colourings: {len({r[2] for r in rows})} (B1264: 85)")
bydim = collections.Counter(r[1] for r in rows)
print("centralizer dimension of the grading operator (6 + #roots with <alpha,h> = 0 mod 3):", dict(sorted(bydim.items())))
col_by_dim = collections.defaultdict(set)
for c, d, col in rows: col_by_dim[d].add(col)
print("distinct colourings per class:", {d: len(s) for d, s in sorted(col_by_dim.items())})
# consistency: a colouring should not appear in two classes
allcols = collections.defaultdict(set)
for c, d, col in rows: allcols[col].add(d)
print("colourings appearing in more than one class:", sum(1 for s in allcols.values() if len(s) > 1))
# the classes by Kac: dim 24 = A2^3 (the trinification element, = w_3's class), dim 30 = D4 x T^2, dim 28 = A5 x A1? / A4 x A1 x T
print("w_3's lift (R64): 24 three-cycles on the 72 roots, no fixed Cartan vector -> Ad-fixed dim 24 -> the A2^3 class.")
