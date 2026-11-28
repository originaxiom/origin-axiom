#!/usr/bin/env python3
"""Banking seat V1 (fam1-v1-unset-04), Q0002: an own recomputation, sharing nothing with the producer's code.
For each of the six orbits: the points by breadth-first search under L, R and their inverses; T4, sigma (S) and C as maps
on points, the pointwise identity T4 = S(C + C^2) + (C + C^2)S checked on every point; A = 3 P(1 + S)P on the C-orbit
sums; R, d1 to d4 from A and sigma's fixed points; the factorisation of T4's characteristic polynomial checked exactly over
Z with python-flint on the five smaller orbits and modulo three primes on the mod-135 orbit.
    python3 relays/claims/banking/q0002_own.py                    the decisive run
    python3 relays/claims/banking/q0002_own.py --plant-shift-one   the failing control (R(x + 3) R(x + 2) in place of
                                                                   R(x + 4) R(x + 2), which must not match)
Exit 0 when every orbit's values come out as the card states; 1 otherwise."""
import sys
from collections import Counter, deque
import flint

PLANT = sys.argv[1:] == ["--plant-shift-one"]
if sys.argv[1:] not in ([], ["--plant-shift-one"]):
    print("usage: no argument, or --plant-shift-one"); sys.exit(2)

def moves(n):
    L = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % n)
    R = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % n)
    Li = lambda v: (v[0], (v[0] * v[1] - v[2]) % n, v[1])
    Ri = lambda v: ((v[0] * v[1] - v[2]) % n, v[1], v[0])
    return L, R, Li, Ri
def Cm(v): return (v[1], v[2], v[0])
def Sg(v, n): return (v[1], v[0], (v[0] * v[1] - v[2]) % n)

def orbit_of(start, n):
    seen, q = {start}, deque([start])
    while q:
        v = q.popleft()
        for m in moves(n):
            u = m(v)
            if u not in seen:
                seen.add(u); q.append(u)
    return seen

def largest_on_leaf(n, k):
    pts = {(x, y, z) for x in range(n) for y in range(n) for z in range(n) if (x * x + y * y + z * z - x * y * z) % n == k}
    best, left = set(), set(pts)
    while left:
        o = orbit_of(min(left), n)
        left -= o
        if len(o) > len(best):
            best = o
    return best

def check(O, n, primes=None):
    pts = sorted(O); idx = {v: i for i, v in enumerate(pts)}
    L, R, Li, Ri = moves(n)
    pointwise = all(Counter([L(v), R(v), Li(v), Ri(v)]) ==
                    Counter([Sg(Cm(v), n), Sg(Cm(Cm(v)), n), Cm(Sg(v, n)), Cm(Cm(Sg(v, n)))]) for v in pts)
    corb, rep = [], {}
    for v in pts:
        if v in rep: continue
        o = sorted({v, Cm(v), Cm(Cm(v))})
        for u in o: rep[u] = len(corb)
        corb.append(o)
    m = len(corb)
    A = [[0] * m for _ in range(m)]
    for i, o in enumerate(corb):
        A[i][i] += 3
        for u in o:
            t = rep[Sg(u, n)]
            A[t][i] += 3 // len(corb[t])
    fS = sum(Sg(v, n) == v for v in pts)
    chA = flint.fmpz_mat(A).charpoly()
    x = flint.fmpz_poly([0, 1])
    d1 = d2 = 0
    Rp = chA
    while Rp(6) == 0:
        Rp = Rp // (x - 6); d1 += 1
    while Rp(0) == 0:
        Rp = Rp // x; d2 += 1
    deg = Rp.degree()
    nn = len(pts)
    d3, d4 = (nn + fS) // 2 - d1 - deg, (nn - fS) // 2 - d2 - deg
    shift = 3 if PLANT else 4
    target = Rp(x + shift) * Rp(x + 2) * (x - 4) ** d1 * (x + 4) ** d2 * (x + 2) ** d3 * (x - 2) ** d4
    rows = [[0] * nn for _ in range(nn)]
    for v in pts:
        for mv in (L, R, Li, Ri):
            rows[idx[mv(v)]][idx[v]] += 1
    if primes is None:
        same = flint.fmpz_mat(rows).charpoly() == target
    else:
        same = [flint.nmod_mat(rows, p).charpoly() == flint.nmod_poly([int(c) % p for c in target.coeffs()], p)
                for p in primes]
    return (nn, m, fS, pointwise, (d1, d2, d3, d4), deg, same)

ok = True
def show(label, got, want):
    global ok
    print("DECISIVE: %s %s" % (label, got))
    if got != want:
        ok = False
cases = [("leaf k = 5 mod 7, largest orbit", largest_on_leaf(7, 5), 7, (64, 22, 0, True, (1, 0, 10, 11), 21, True)),
         ("leaf k = 6 mod 11, largest orbit", largest_on_leaf(11, 6), 11, (60, 20, 2, True, (1, 0, 11, 10), 19, True)),
         ("leaf k = 9 mod 13, largest orbit", largest_on_leaf(13, 9), 13, (112, 38, 0, True, (1, 0, 18, 19), 37, True)),
         ("orbit of (3,3,3) mod 27", orbit_of((3, 3, 3), 27), 27, (72, 26, 0, True, (1, 1, 11, 11), 24, True)),
         ("orbit of (3,3,3) mod 81", orbit_of((3, 3, 3), 81), 81, (648, 218, 0, True, (1, 1, 107, 107), 216, True))]
for label, O, n, want in cases:
    show(label + ": points, C-orbits, sigma's fixed points, pointwise identity, d1..d4, deg R, factorisation over Z",
         check(O, n), want)
primes = [p for p in range(2 ** 61 - 1, 2 ** 61 - 4000, -2) if flint.fmpz(p).is_prime()][:3]
show("orbit of (3,3,3) mod 135: points, C-orbits, sigma's fixed points, pointwise identity, d1..d4, deg R, "
     "factorisation modulo three primes near 2^61", check(orbit_of((3, 3, 3), 135), 135, primes),
     (2880, 962, 0, True, (1, 1, 479, 479), 960, [True, True, True]))
sys.exit(0 if ok else 1)
