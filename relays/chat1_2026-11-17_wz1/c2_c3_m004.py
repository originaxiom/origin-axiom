"""C2: m004's volume against Humbert's formula for PSL(2, Z[w]).  C3: is Riley's group a congruence subgroup?"""
import sys
from collections import deque
from mpmath import mp, mpf, pi, clsin, zeta, dirichlet, sqrt

mp.dps = 40
lob = lambda th: clsin(2, 2 * th) / 2  # Lobachevsky function
vol_m004 = 6 * lob(pi / 3)
zK2 = zeta(2) * dirichlet(2, [0, 1, -1])
humbert = mpf(3) ** mpf(1.5) * zK2 / (4 * pi ** 2)
print('C2: vol(m004) = 6 Lob(pi/3) =', mp.nstr(vol_m004, 30))
print('    12 * Humbert vol(PSL(2,Z[w])\\H^3) =', mp.nstr(12 * humbert, 30), ' diff', mp.nstr(vol_m004 - 12 * humbert, 3))

# C3. elements of O/N: (a, b) = a + b w, w^2 = -1 - w
def mul(x, y, N):
    a, b = x; c, d = y
    # (a + b w)(c + d w) = ac + (ad + bc) w + bd w^2 = (ac - bd) + (ad + bc - bd) w
    return ((a * c - b * d) % N, (a * d + b * c - b * d) % N)

def add(x, y, N):
    return ((x[0] + y[0]) % N, (x[1] + y[1]) % N)

def mmul(A, B, N):
    return (add(mul(A[0], B[0], N), mul(A[1], B[2], N), N), add(mul(A[0], B[1], N), mul(A[1], B[3], N), N),
            add(mul(A[2], B[0], N), mul(A[3], B[2], N), N), add(mul(A[2], B[1], N), mul(A[3], B[3], N), N))

def red(M, N):
    return tuple(((e[0] % N, e[1] % N)) for e in M)

def neg(M, N):
    return tuple(((-e[0]) % N, (-e[1]) % N) for e in M)

def canon(M, N):
    return min(M, neg(M, N))  # PSL: identify M and -M

def closure(gens, N):
    gens = [red(g, N) for g in gens]
    I = red(((1, 0), (0, 0), (0, 0), (1, 0)), N)
    seen = {canon(I, N)}
    q = deque([I])
    while q:
        M = q.popleft()
        for g in gens:
            P = mmul(M, g, N)
            c = canon(P, N)
            if c not in seen:
                seen.add(c)
                q.append(P)
    return len(seen)

one, zero = (1, 0), (0, 0)
w = (0, 1)
A = (one, one, zero, one)            # [[1,1],[0,1]]
B = (one, zero, (0, -1), one)        # [[1,0],[-w,1]]
T = (one, one, zero, one)
Tw = (one, w, zero, one)
S = (zero, (-1, 0), one, zero)
for N in [int(a) for a in sys.argv[1:]] or [2, 3, 4, 6, 7, 8, 12]:
    G = closure([T, Tw, S], N)
    H = closure([A, B], N)
    print(f'C3: N = {N:2d}: |PSL(2,O/N)| = {G:8d}, |image of Riley group| = {H:8d}, index = {G / H:g}', flush=True)
