"""B1296's rational E6 in R^8 (Bourbaki), copied verbatim from e6_theta_spectra.py lines 7-58 for reuse."""
from fractions import Fraction as Fr

H = Fr(1, 2)
def e(i): v = [Fr(0)] * 8; v[i] = Fr(1); return v
def add(a, b): return [x + y for x, y in zip(a, b)]
def sub(a, b): return [x - y for x, y in zip(a, b)]
def scale(c, a): return [c * x for x in a]
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def key(v): return tuple(v)

# Bourbaki simple roots of E6 (Planche V)
a1 = add(scale(H, add(e(0), e(7))), scale(-H, [sum(x) for x in zip(e(1), e(2), e(3), e(4), e(5), e(6))]))
a2 = add(e(0), e(1)); a3 = sub(e(1), e(0)); a4 = sub(e(2), e(1)); a5 = sub(e(3), e(2)); a6 = sub(e(4), e(3))
S = [a1, a2, a3, a4, a5, a6]
C = [[dot(a, b) for b in S] for a in S]                   # Cartan matrix (simply laced, norm^2 2)
E6_CARTAN = [[2,0,-1,0,0,0],[0,2,0,-1,0,0],[-1,0,2,-1,0,0],[0,-1,-1,2,-1,0],[0,0,0,-1,2,-1],[0,0,0,0,-1,2]]
assert C == [[Fr(x) for x in row] for row in E6_CARTAN], C

def refl(v, a): return sub(v, scale(dot(v, a), a))       # norm^2(a) = 2
def orbit(start):
    seen = {key(start): start}; frontier = [start]
    while frontier:
        nxt = []
        for v in frontier:
            for a in S:
                w = refl(v, a)
                if key(w) not in seen: seen[key(w)] = w; nxt.append(w)
        frontier = nxt
    return list(seen.values())

roots = orbit(a1); assert len(roots) == 72
# inverse Cartan matrix, exact
def inv(M):
    n = len(M); A = [[Fr(x) for x in row] + [Fr(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
    for i in range(n):
        p = next(r for r in range(i, n) if A[r][i] != 0); A[i], A[p] = A[p], A[i]
        A[i] = [x / A[i][i] for x in A[i]]
        for r in range(n):
            if r != i and A[r][i] != 0: A[r] = [x - A[r][i] * y for x, y in zip(A[r], A[i])]
    return [row[n:] for row in A]
Cinv = inv(E6_CARTAN)
omega = [[sum((Cinv[k][j] * S[j][i] for j in range(6)), Fr(0)) for i in range(8)] for k in range(6)]
for k in range(6): assert [dot(omega[k], a) for a in S] == [Fr(int(j == k)) for j in range(6)]
W27 = orbit(omega[0]); assert len(W27) == 27
W27bar = orbit(omega[5]); assert len(W27bar) == 27
# simple-root coordinates of a root
def coords(r): return tuple(dot(r, omega[k]) for k in range(6))
FLIP = {0: 5, 5: 0, 2: 4, 4: 2, 1: 1, 3: 3}
def theta(v):  # diagram automorphism on the span of the simple roots: permute simple-root coordinates
    c = [dot(v, omega[k]) for k in range(6)]; ct = [c[FLIP[k]] for k in range(6)]
    return [sum((ct[k] * S[k][i] for k in range(6)), Fr(0)) for i in range(8)]
rk = {key(r) for r in roots}
