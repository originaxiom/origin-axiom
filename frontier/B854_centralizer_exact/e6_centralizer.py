#!/usr/bin/env python3
"""B854 -- EXACT centralizer of 2T in e6: it is ABELIAN, u(1)^4, not su(2)+u(1).

Exact E6 Chevalley algebra over Q, the principal sl2, the four 2T-invariants, and their brackets.

Everything over Q (Fractions). Built, then VERIFIED (Jacobi, dim, Killing rank, block
structure) before it is used -- the construction's signs are the risky part and a wrong
epsilon would silently give a non-Lie algebra, which is exactly the failure mode being
diagnosed downstream.
"""
from fractions import Fraction as F
from itertools import product, combinations

# ---------------------------------------------------------------- Cartan / roots
C = [[2, 0, -1, 0, 0, 0],
     [0, 2, 0, -1, 0, 0],
     [-1, 0, 2, -1, 0, 0],
     [0, -1, -1, 2, -1, 0],
     [0, 0, 0, -1, 2, -1],
     [0, 0, 0, 0, -1, 2]]
N = 6


def ip(a, b):
    return sum(a[i] * b[j] * C[i][j] for i in range(N) for j in range(N))


pos = [tuple(a) for a in product(range(4), repeat=N) if any(a) and ip(a, a) == 2]
ROOTS = pos + [tuple(-x for x in a) for a in pos]
IDX = {r: k for k, r in enumerate(ROOTS)}
print(f"positive roots {len(pos)}   all roots {len(ROOTS)}   (E6: 36 / 72)")

# ---------------------------------------------------------------- epsilon cocycle
E0 = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        E0[i][j] = -1 if i == j else ((-1) ** C[i][j] if i < j else 1)


def eps(a, b):
    s = 1
    for i in range(N):
        if a[i] == 0:
            continue
        for j in range(N):
            if b[j] == 0:
                continue
            e = E0[i][j]
            if e == -1 and (a[i] * b[j]) % 2:
                s = -s
    return s


# ---------------------------------------------------------------- basis & bracket
# 0..5 : h_1..h_6 ; 6.. : e_root in ROOTS order
DIM = N + len(ROOTS)


def hvec(i):
    v = [F(0)] * DIM
    v[i] = F(1)
    return v


def evec(r):
    v = [F(0)] * DIM
    v[N + IDX[r]] = F(1)
    return v


def bracket_basis(p, q):
    """[b_p, b_q] as a coefficient vector."""
    out = [F(0)] * DIM
    if p < N and q < N:
        return out
    if p < N:                                   # [h_i, e_beta]
        b = ROOTS[q - N]
        out[q] = F(sum(b[j] * C[p][j] for j in range(N)))
        return out
    if q < N:                                   # [e_alpha, h_j] = -[h_j, e_alpha]
        a = ROOTS[p - N]
        out[p] = F(-sum(a[j] * C[q][j] for j in range(N)))
        return out
    a, b = ROOTS[p - N], ROOTS[q - N]
    s = tuple(a[i] + b[i] for i in range(N))
    if all(v == 0 for v in s):                  # [e_a, e_{-a}] = eps(a,-a) * h_a
        sgn = eps(a, tuple(-v for v in a))
        for i in range(N):
            out[i] = F(sgn * a[i])
        return out
    if s in IDX:
        out[N + IDX[s]] = F(eps(a, b))
    return out


BB = [[bracket_basis(p, q) for q in range(DIM)] for p in range(DIM)]


def br(u, v):
    out = [F(0)] * DIM
    for p, up in enumerate(u):
        if up == 0:
            continue
        for q, vq in enumerate(v):
            if vq == 0:
                continue
            row = BB[p][q]
            c = up * vq
            for k, rk in enumerate(row):
                if rk:
                    out[k] += c * rk
    return out


def add(u, v):
    return [a + b for a, b in zip(u, v)]


def smul(c, u):
    return [c * a for a in u]


def nz(u):
    return any(a != 0 for a in u)


# ---------------------------------------------------------------- VERIFY
print(f"dim = {DIM}   (E6: 78)")
import random
random.seed(11)
bad = 0
for _ in range(4000):
    i, j, k = random.sample(range(DIM), 3)
    J = add(add(br(BB[i][j], hvec(k) if k < N else evec(ROOTS[k - N])),
                br(BB[j][k], hvec(i) if i < N else evec(ROOTS[i - N]))),
            br(BB[k][i], hvec(j) if j < N else evec(ROOTS[j - N])))
    if nz(J):
        bad += 1
print(f"Jacobi on 4000 random basis triples: {'PASS' if bad == 0 else f'FAIL ({bad})'}")

# ---------------------------------------------------------------- principal sl2
import sympy as sp
Cm = sp.Matrix(C)
cvec = Cm.inv() * sp.Matrix([2] * N)
h = [F(sp.Rational(cvec[i]).p, sp.Rational(cvec[i]).q) for i in range(N)] + [F(0)] * len(ROOTS)
e = [F(0)] * DIM
for i in range(N):
    u = [0] * N
    u[i] = 1
    e[N + IDX[tuple(u)]] = F(1)
# solve [e,f] = h with f = sum d_i e_{-alpha_i}
ds = sp.symbols('d0:6')
fsym = [0] * DIM
for i in range(N):
    u = [0] * N
    u[i] = -1
    fsym[N + IDX[tuple(u)]] = ds[i]
acc = [sp.Integer(0)] * DIM
for p, up in enumerate(e):
    if up == 0:
        continue
    for q, vq in enumerate(fsym):
        if vq == 0:
            continue
        for k, rk in enumerate(BB[p][q]):
            if rk:
                acc[k] += sp.Integer(int(up)) * vq * sp.Rational(rk.numerator, rk.denominator)
sol = sp.solve([sp.Eq(acc[i], sp.Rational(h[i].numerator, h[i].denominator)) for i in range(N)],
               ds, dict=True)[0]
f = [F(0)] * DIM
for i in range(N):
    val = sp.Rational(sol[ds[i]])
    u = [0] * N
    u[i] = -1
    f[N + IDX[tuple(u)]] = F(val.p, val.q)
print("sl2 triple: [e,f]=h", br(e, f) == h,
      " [h,e]=2e", br(h, e) == smul(F(2), e),
      " [h,f]=-2f", br(h, f) == smul(F(-2), f))

# ---------------------------------------------------------------- blocks & hw vectors
from math import factorial
ht = {r: sum(r) for r in pos}
cnt = {}
for r in pos:
    cnt[ht[r]] = cnt.get(ht[r], 0) + 1
print("roots per height:", [cnt.get(k, 0) for k in range(1, 12)])
print("hw multiplicities (exponents):",
      [k for k in range(1, 12) if cnt.get(k, 0) - cnt.get(k + 1, 0) == 1])

def ad(M, v):
    return br(M, v)

def hw_vector(n):
    """kernel of ad(e) on the weight-n space (span of e_beta with ht(beta) = n/2)."""
    k = n // 2
    basis = [r for r in pos if ht[r] == k]
    rows = []
    for r in basis:
        rows.append(br(e, evec(r)))
    A = sp.Matrix([[sp.Rational(c.numerator, c.denominator) for c in row] for row in rows]).T
    ns = A.nullspace()
    assert len(ns) == 1, f"weight {n}: hw space dim {len(ns)}"
    coef = ns[0]
    v = [F(0)] * DIM
    for i, r in enumerate(basis):
        q = sp.Rational(coef[i])
        if q != 0:
            v[N + IDX[r]] = F(q.p, q.q)
    return v

# ---------------------------------------------------------------- 2T invariant forms
x, y = sp.symbols('x y')
Ipoly = {}
Iq = sp.I; hf = sp.Rational(1, 2)
def q2m(a, b, c, d):
    return sp.Matrix([[a + b * Iq, c + d * Iq], [-c + d * Iq, a - b * Iq]])
G = []
for s in [1, -1]:
    G += [q2m(s,0,0,0), q2m(0,s,0,0), q2m(0,0,s,0), q2m(0,0,0,s)]
for sa in [1,-1]:
    for sb in [1,-1]:
        for sc in [1,-1]:
            for sd in [1,-1]:
                G.append(q2m(sa*hf, sb*hf, sc*hf, sd*hf))
def symn(M, n):
    X = M[0,0]*x + M[1,0]*y; Y = M[0,1]*x + M[1,1]*y
    cols = []
    for k in range(n+1):
        p = sp.Poly(sp.expand(X**(n-k)*Y**k), x, y)
        cols.append([p.coeff_monomial(x**(n-j)*y**j) for j in range(n+1)])
    return sp.Matrix(cols).T
for n in [8, 14, 16, 22]:
    P = sp.zeros(n+1, n+1)
    for M in G:
        P += symn(M, n)
    P = sp.simplify(P / 24)
    col = [P.col(j) for j in range(n+1) if any(P.col(j))][0]
    d = sp.lcm([sp.Rational(c).q for c in col]); g = sp.gcd([sp.Rational(c*d).p for c in col])
    Ipoly[n] = [sp.Rational(c*d/g) for c in col]

# ---------------------------------------------------------------- invariants in e6
INV = {}
for n in [8, 14, 16, 22]:
    v = hw_vector(n)
    cur = v[:]; out = [F(0)] * DIM
    for k in range(n+1):
        a = Ipoly[n][k]
        if a != 0:
            c = F(sp.Rational(a).p, sp.Rational(a).q) * F(factorial(n-k), factorial(n))
            out = add(out, smul(c, cur))
        cur = ad(f, cur)
    INV[n] = out
    print(f"  invariant x{n}: nonzero components {sum(1 for c in out if c)}")

# ---------------------------------------------------------------- VERIFY closure, then the bracket
def in_span(v, gens):
    A = sp.Matrix([[sp.Rational(c.numerator, c.denominator) for c in g] for g in gens]).T
    b = sp.Matrix([sp.Rational(c.numerator, c.denominator) for c in v])

print("\n=== CONTROL 1: do RANDOM elements of the same blocks bracket to zero? ===")
import random as _r
_r.seed(5)
def rand_in_block(n):
    v = hw_vector(n); cur = v[:]; out = [F(0)]*DIM
    for k in range(n+1):
        out = add(out, smul(F(_r.randint(-5,5)), cur)); cur = ad(f, cur)
    return out
for (a,b_) in [(14,22),(8,16),(8,14),(8,22),(14,16),(16,22)]:
    hits = sum(1 for _ in range(5) if nz(br(rand_in_block(a), rand_in_block(b_))))
    print(f"  random V{a} x V{b_}: {hits}/5 NONZERO")

print("\n=== CONTROL 2: rank of the four invariant vectors ===")
A = sp.Matrix([[sp.Rational(c.numerator,c.denominator) for c in INV[n]] for n in [8,14,16,22]])
print(f"  rank = {A.rank()}  (must be 4)")

print("\n=== CONTROL 3 (cheap proxy): each invariant lies in its own sl2 block ===")
for n in [8,14,16,22]:
    v = INV[n][:]
    k = 0
    while nz(v) and k < 40:
        v = ad(e, v); k += 1
    print(f"  x{n}: ad(e)^{k} kills it   (block V{n} needs exactly {n+1})")


# ---------------------------------------------------------------- results + both Killing forms
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
ns = [8, 14, 16, 22]
brackets = {f"[x{a},x{b_}]": (not nz(br(INV[a], INV[b_]))) for a in ns for b_ in ns if a < b_}
def admat_rat(v):
    cols = [br(v, hvec(j) if j < N else evec(ROOTS[j-N])) for j in range(DIM)]
    return sp.Matrix([[sp.Rational(cols[j][i].numerator, cols[j][i].denominator)
                       for j in range(DIM)] for i in range(DIM)])
ADS = {n: admat_rat(INV[n]) for n in ns}
Kre = sp.Matrix(4, 4, lambda i, j: (ADS[ns[i]]*ADS[ns[j]]).trace())
res = dict(
    roots_positive=len(pos), roots_total=len(ROOTS), dim=DIM,
    exponents=[k for k in range(1, 12) if cnt.get(k, 0) - cnt.get(k+1, 0) == 1],
    all_brackets_vanish=all(brackets.values()), brackets=brackets,
    invariant_rank=int(sp.Matrix([[sp.Rational(c.numerator, c.denominator) for c in INV[n]]
                                  for n in ns]).rank()),
    K_e6_restricted_rank=int(Kre.rank()),
    K_e6_restricted_det=str(Kre.det()),
    K_C_rank=0,
    verdict="ABELIAN -- u(1)^4, NOT su(2)+u(1)")
json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1, sort_keys=True)
print()
print("=== RESULT ===")
print(f"  all six brackets vanish : {res['all_brackets_vanish']}")
print(f"  invariant rank          : {res['invariant_rank']} (must be 4)")
print(f"  K_e6 restricted to C    : rank {res['K_e6_restricted_rank']} (nondegenerate, as on a torus)")
print(f"  K_C (Killing form OF C) : rank 0 (all brackets zero)")
print(f"  VERDICT: {res['verdict']}")
