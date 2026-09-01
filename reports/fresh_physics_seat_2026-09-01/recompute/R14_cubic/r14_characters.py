#!/usr/bin/env python3
"""R14 blind recomputation, part 1 (shape-free / character-theoretic).

Own construction, no arc code consulted:
  - E6 Cartan matrix (Bourbaki), weight system of the 27 = V(omega_1).
  - Count of unordered zero-sum weight triples (candidate cubic support).
  - Exact decomposition of Sym^3(27) by greedy highest-weight stripping with
    Freudenthal's multiplicity formula over exact rationals.
    => multiplicity of the trivial rep = dim Inv(Sym^3 27).
All arithmetic exact (Fraction).
"""
from fractions import Fraction
from itertools import combinations_with_replacement
import numpy as np

# ---------- E6 Cartan matrix, Bourbaki labeling (node 2 attached to node 4) ----
A = [
    [ 2, 0,-1, 0, 0, 0],
    [ 0, 2, 0,-1, 0, 0],
    [-1, 0, 2,-1, 0, 0],
    [ 0,-1,-1, 2,-1, 0],
    [ 0, 0, 0,-1, 2,-1],
    [ 0, 0, 0, 0,-1, 2],
]
n = 6
# exact inverse of A
Amat = [[Fraction(A[i][j]) for j in range(n)] for i in range(n)]
def mat_inv(M):
    m = len(M)
    aug = [row[:] + [Fraction(int(i == j)) for j in range(m)] for i, row in enumerate(M)]
    for c in range(m):
        p = next(r for r in range(c, m) if aug[r][c] != 0)
        aug[c], aug[p] = aug[p], aug[c]
        pv = aug[c][c]
        aug[c] = [x / pv for x in aug[c]]
        for r in range(m):
            if r != c and aug[r][c] != 0:
                f = aug[r][c]
                aug[r] = [x - f * y for x, y in zip(aug[r], aug[c])]
    return [row[m:] for row in aug]
Ainv = mat_inv(Amat)

def ip(m1, m2):
    """(w1,w2) for weights in Dynkin-label coords: m1^T A^{-1} m2 (simply laced, (a,a)=2)."""
    return sum(Fraction(m1[i]) * Ainv[i][j] * m2[j] for i in range(n) for j in range(n))

def sub_alpha(w, i, k=1):
    """w - k*alpha_i in Dynkin coords (alpha_i has Dynkin labels = row i of A)."""
    return tuple(w[j] - k * A[i][j] for j in range(n))

def weight_system(Lam):
    """All weights of V(Lam) (saturated set, no multiplicities)."""
    seen = {tuple(Lam)}
    frontier = [tuple(Lam)]
    while frontier:
        new = []
        for w in frontier:
            for i in range(n):
                if w[i] > 0:
                    for k in range(1, w[i] + 1):
                        ww = sub_alpha(w, i, k)
                        if ww not in seen:
                            seen.add(ww)
                            new.append(ww)
        frontier = new
    return seen

# ---------- roots ----------
# adjoint = V(omega_2) for E6 (Bourbaki): highest root = omega_2's rep
adj_w = weight_system((0, 1, 0, 0, 0, 0))
roots = [w for w in adj_w if any(x != 0 for x in w)]
assert len(roots) == 72, len(roots)
def root_coords(m):
    """coordinates in simple-root basis: c = A^{-1} m"""
    return [sum(Ainv[i][j] * m[j] for j in range(n)) for i in range(n)]
pos_roots = [r for r in roots if sum(root_coords(r)) > 0]
assert len(pos_roots) == 36, len(pos_roots)
for r in pos_roots:
    assert ip(r, r) == 2

rho = (1, 1, 1, 1, 1, 1)
def addw(a, b):
    return tuple(x + y for x, y in zip(a, b))

def weyl_dim(Lam):
    num = Fraction(1)
    lr = addw(Lam, rho)
    for a in pos_roots:
        num *= ip(lr, a) / ip(rho, a)
    return num

def freudenthal(Lam):
    """weight -> multiplicity for V(Lam), exact."""
    ws = weight_system(Lam)
    # sort by height descending (height = sum of root coords of Lam - w)
    def height(w):
        c = root_coords(tuple(l - x for l, x in zip(Lam, w)))
        s = sum(c)
        assert s.denominator == 1
        return int(s)
    order = sorted(ws, key=height)
    mult = {}
    c2 = ip(addw(Lam, rho), addw(Lam, rho))
    for w in order:
        if w == tuple(Lam):
            mult[w] = Fraction(1)
            continue
        s = Fraction(0)
        for a in pos_roots:
            k = 1
            while True:
                wk = addw(w, tuple(k * x for x in a))
                if wk not in ws:
                    break
                s += mult[wk] * ip(wk, a)
                k += 1
        denom = c2 - ip(addw(w, rho), addw(w, rho))
        mult[w] = 2 * s / denom
        assert mult[w].denominator == 1
    return {w: int(m) for w, m in mult.items()}

# ---------- the 27 ----------
w27 = weight_system((1, 0, 0, 0, 0, 0))
assert len(w27) == 27, len(w27)
m27 = freudenthal((1, 0, 0, 0, 0, 0))
assert all(v == 1 for v in m27.values()), "27 not multiplicity-free?"
print("[27] built: 27 weights, all multiplicity 1; dim check (Weyl):", weyl_dim((1, 0, 0, 0, 0, 0)))

W = sorted(w27)
# zero-sum unordered triples (with repetition allowed)
zero_triples = []
for t in combinations_with_replacement(range(27), 3):
    s = tuple(W[t[0]][i] + W[t[1]][i] + W[t[2]][i] for i in range(n))
    if all(x == 0 for x in s):
        zero_triples.append(t)
print("[27] unordered zero-sum weight triples:", len(zero_triples))
print("[27] any triple with a repeated index?",
      any(len(set(t)) < 3 for t in zero_triples))
# ordered count for reference
ordered = 0
Wset = {w: i for i, w in enumerate(W)}
for i in range(27):
    for j in range(27):
        s = tuple(-W[i][k] - W[j][k] for k in range(n))
        if s in Wset:
            ordered += 1
print("[27] ordered zero-sum triples:", ordered)

# ---------- Sym^3(27) decomposition ----------
sym_mult = {}
for t in combinations_with_replacement(range(27), 3):
    s = tuple(W[t[0]][i] + W[t[1]][i] + W[t[2]][i] for i in range(n))
    sym_mult[s] = sym_mult.get(s, 0) + 1
total = sum(sym_mult.values())
assert total == 27 * 28 * 29 // 6 == 3654
print("[Sym^3] total dim:", total)

decomp = []
work = dict(sym_mult)
while any(v for v in work.values()):
    dom = [w for w, v in work.items() if v > 0 and all(x >= 0 for x in w)]
    assert dom, "no dominant weight left but multiplicities remain — bug"
    # pick dominant weight of maximal height above 0 (maximal in dominance order among candidates)
    def ht(w):
        s = sum(root_coords(w))
        assert s.denominator == 1
        return int(s)
    lam = max(dom, key=ht)
    mlam = work[lam]
    fm = freudenthal(lam)
    for w, mv in fm.items():
        work[w] = work.get(w, 0) - mlam * mv
    assert all(v >= 0 for v in work.values()), "negative multiplicity — bug"
    decomp.append((lam, mlam, int(weyl_dim(lam))))

print("[Sym^3] decomposition (highest weight, multiplicity, dim):")
tot = 0
for lam, m, d in decomp:
    print("   ", lam, "x", m, " dim", d)
    tot += m * d
assert tot == 3654
triv = sum(m for lam, m, d in decomp if all(x == 0 for x in lam))
print("[Sym^3] multiplicity of trivial rep  =  dim Inv(Sym^3 27) =", triv)

# controls: Sym^2 and 27x27bar
sym2 = {}
for t in combinations_with_replacement(range(27), 2):
    s = tuple(W[t[0]][i] + W[t[1]][i] for i in range(n))
    sym2[s] = sym2.get(s, 0) + 1
triv2 = 0  # count via stripping quickly: trivial can only appear if 0 weight present; do full strip
work = dict(sym2)
dec2 = []
while any(v for v in work.values()):
    dom = [w for w, v in work.items() if v > 0 and all(x >= 0 for x in w)]
    lam = max(dom, key=lambda w: int(sum(root_coords(w))))
    mlam = work[lam]
    for w, mv in freudenthal(lam).items():
        work[w] = work.get(w, 0) - mlam * mv
    dec2.append((lam, mlam))
print("[control] Sym^2(27) decomposition:", dec2,
      " -> trivial mult:", sum(m for l, m in dec2 if all(x == 0 for x in l)))

# planted-positive control (character side): Sym^3 of 27 + 27bar must contain MORE
# than one invariant (at least: the cubic on 27, the conjugate cubic, and 27.27bar pairings
# times nothing... compute honestly)
w27b = weight_system((0, 0, 0, 0, 0, 1))
assert len(w27b) == 27
V54 = sorted(w27) + sorted(w27b)
sym3b = {}
for t in combinations_with_replacement(range(54), 3):
    s = tuple(V54[t[0]][i] + V54[t[1]][i] + V54[t[2]][i] for i in range(n))
    sym3b[s] = sym3b.get(s, 0) + 1
work = dict(sym3b)
trivb = 0
while any(v for v in work.values()):
    dom = [w for w, v in work.items() if v > 0 and all(x >= 0 for x in w)]
    lam = max(dom, key=lambda w: int(sum(root_coords(w))))
    mlam = work[lam]
    for w, mv in freudenthal(lam).items():
        work[w] = work.get(w, 0) - mlam * mv
    if all(x == 0 for x in lam):
        trivb += mlam
print("[planted control] dim Inv(Sym^3(27+27bar)) =", trivb, "(must be > 1 for the method to be able to fail)")
