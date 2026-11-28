#!/usr/bin/env python3
"""Banking seat V1 (fam1-v1-unset-04), Q0001: an own recomputation, sharing nothing with the producer's code.
The orbit of (3, 3, 3) mod 135 under L, R and their inverses by breadth-first search; the neutral sector (W on the C-orbit
sums) and the charged sector q = 1 (W on the w-twisted sums), both built from the six moves' action; their characteristic
polynomials, the gcd and the quotient computed modulo several primes p = 1 mod 3, w a cube root of unity in F_p.  A
multi-prime check, not an exact computation over Z.
    python3 relays/claims/banking/q0001_own.py                 the decisive run
    python3 relays/claims/banking/q0001_own.py --plant-w-one   the failing control (w = 1: the neutral sector passed off as
                                                                the charged one, which must not leave the named ten)
Exit 0 when every value comes out as the card states; 1 otherwise."""
import sys
from collections import deque
import flint

PLANT = sys.argv[1:] == ["--plant-w-one"]
if sys.argv[1:] not in ([], ["--plant-w-one"]):
    print("usage: no argument, or --plant-w-one"); sys.exit(2)
N = 135
PRIMES = [p for p in range(2 ** 61 - 1, 2 ** 61 - 40000, -2) if p % 3 == 1 and flint.fmpz(p).is_prime()][:6]

def L(v, n): x, y, z = v; return (x, z, (x * z - y) % n)
def R(v, n): x, y, z = v; return (z, y, (y * z - x) % n)
def Li(v, n): x, y, z = v; return (x, (x * y - z) % n, y)          # L^-1: (x, y, z) -> (x, xy - z, y)
def Ri(v, n): x, y, z = v; return ((x * y - z) % n, y, x)          # R^-1: (x, y, z) -> (xy - z, y, x)
def Cm(v): x, y, z = v; return (y, z, x)
def Xm(v, n): x, y, z = v; return (y, (y * z - x) % n, z)
def Xi(v, n): x, y, z = v; return ((x * z - y) % n, x, z)          # X^-1
for v in [(1, 2, 3), (4, 7, 11)]:
    assert Li(L(v, 97), 97) == v and Ri(R(v, 97), 97) == v and Xi(Xm(v, 97), 97) == v

def orbit(n):
    start = (3 % n, 3 % n, 3 % n)
    seen, q = {start}, deque([start])
    while q:
        v = q.popleft()
        for m in (L, R, Li, Ri):
            u = m(v, n)
            if u not in seen:
                seen.add(u); q.append(u)
    return seen

O = orbit(N)
six = (L, R, Li, Ri, Xm, Xi)
assert all(m(v, N) in O for v in O for m in six)                  # the six moves keep the orbit
fixed = [v for v in O if Cm(v) == v]
corb, rep = [], {}
for v in sorted(O):
    if v in rep: continue
    o = [v, Cm(v), Cm(Cm(v))] if Cm(v) != v else [v]
    for k, u in enumerate(o):
        rep[u] = (len(corb), k)
    corb.append(o)
three = [i for i, o in enumerate(corb) if len(o) == 3]
ok = True
def show(label, got, want):
    global ok
    print("DECISIVE: %s %s" % (label, got))
    if got != want:
        ok = False
show("mod 135: orbit points, C's fixed points, neutral dimension, charged dimension",
     (len(O), len(fixed), len(corb), len(three)), (2880, 3, 962, 959))

def sectors(p):
    w = next(pow(g, (p - 1) // 3, p) for g in range(2, 50) if pow(g, (p - 1) // 3, p) != 1)
    if PLANT:
        w = 1
    winv = pow(w, p - 2, p)
    nidx = {i: k for k, i in enumerate(range(len(corb)))}
    cidx = {i: k for k, i in enumerate(three)}
    Nm = [[0] * len(corb) for _ in corb]
    Cmx = [[0] * len(three) for _ in three]
    inv = {1: 1, 3: pow(3, p - 2, p)}
    for i, o in enumerate(corb):                     # W c_o = sum over u in o, m: e_m(u) -> c_o' / |o'|
        for u in o:
            for m in six:
                t, _ = rep[m(u, N)]
                Nm[nidx[t]][nidx[i]] = (Nm[nidx[t]][nidx[i]] + inv[len(corb[t])]) % p
    third = pow(3, p - 2, p)
    for i in three:                                  # W b_o = sum_j w^-j sum_m e_m(C^j v) -> (1/3) w^k b_o'
        o = corb[i]
        for j, u in enumerate(o):
            for m in six:
                t, k = rep[m(u, N)]
                if len(corb[t]) != 3:
                    continue
                c = pow(winv, j, p) * pow(w, k, p) % p * third % p
                Cmx[cidx[t]][cidx[i]] = (Cmx[cidx[t]][cidx[i]] + c) % p
    return flint.nmod_mat(Nm, p).charpoly(), flint.nmod_mat(Cmx, p).charpoly()

named = flint.fmpz_poly([-2, -2, 1]) * flint.fmpz_poly([-2, 2, 1]) * flint.fmpz_poly([-1, -3, 0, 1]) * \
    flint.fmpz_poly([1, -3, 0, 1])
degs, quot_ok = [], []
for p in PRIMES[:4]:
    pn, S = sectors(p)
    d = pn.degree()
    two, half = 2 % p, pow(2, p - 2, p)
    co = [int(c) for c in pn.coeffs()]
    scaled = flint.nmod_poly([co[i] * pow(2, i, p) * pow(half, d, p) % p for i in range(d + 1)], p)
    g = scaled.gcd(S)
    q, r = divmod(S, g)
    degs.append(g.degree())
    quot_ok.append(int(r.degree()) < 0 or r == 0)
    quot_ok[-1] = quot_ok[-1] and q == flint.nmod_poly([int(c) % p for c in named.coeffs()], p)
show("degree of gcd(p_neutral(2x)/2^d, S) at four primes p = 1 mod 3 near 2^61", degs, [949] * 4)
show("the charged unpaired part equals (x^2 - 2x - 2)(x^2 + 2x - 2)(x^3 - 3x - 1)(x^3 - 3x + 1) at each prime", quot_ok,
     [True] * 4)
O27 = orbit(27)
show("reduction mod 27 maps the mod-135 orbit onto the mod-27 orbit",
     ({tuple(c % 27 for c in v) for v in O} == O27, len(O27)), (True, len(O27)))
sys.exit(0 if ok else 1)
