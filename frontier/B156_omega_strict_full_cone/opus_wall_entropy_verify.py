#!/usr/bin/env python
"""
INDEPENDENT verifier (fresh, do-not-trust-handoff) for the claim:

    The wall-avoiding history entropy of the strict-full shear dynamics = log 2.

Built from scratch with sympy/numpy. Verifies, in order:

  (1) Algebraic premises (firewall: these are pure linear algebra over Z[a,m]):
      - R_{a,m} in SL(4,Z): det = 1.
      - charpoly(R_{a,m}) = x^4 - a x^3 + (2a-2m-4)x^2 - a x + 1 (reciprocal).
      - A = S_03 (row0 += row3) sends R_{a,m} -> R_{a+1,m}.
      - C = S_23 (row2 += row3) sends R_{a,m} -> R_{a,m+1}.
      - an invariant symmetric G with M^T G M = G exists, det(G) ~ -delta/(m+1),
        delta = 2a-1-m  (signature (1,3) on delta>=1, m>=0).
      - => on the wall coordinate delta:  A: delta->delta+2,  C: delta->delta-1.

  (2) The combinatorial core (the actual entropy claim):
      - exact transfer-matrix / DP count of length-n {A,C} words keeping
        delta >= 1 at EVERY prefix (wall delta=0 forbidden).
      - growth rate (1/n) log W_n(d) -> log 2, tested for several start d, large n.
      - cross-check the recurrence with a direct brute-force enumeration at small n.
      - independent first-passage / survival argument for the lower bound.
"""

import sympy as sp
import numpy as np
from math import log
from fractions import Fraction

print("="*72)
print("PART 1: algebraic premises (pure linear algebra; firewall-neutral)")
print("="*72)

a, m, x = sp.symbols('a m x')

R = sp.Matrix([
    [a-3, a-2, 1, a-4],
    [0,   1,   1, 0],
    [m+1, m+1, 1, m+1],
    [1,   1,   0, 1],
])

detR = sp.expand(R.det())
print("det(R_{a,m})           =", detR)
assert detR == 1, "R is not in SL(4)"

cp = sp.expand(R.charpoly(x).as_expr())
cp_claim = sp.expand(x**4 - a*x**3 + (2*a - 2*m - 4)*x**2 - a*x + 1)
print("charpoly(R)            =", cp)
print("claimed charpoly       =", cp_claim)
assert sp.expand(cp - cp_claim) == 0, "charpoly mismatch"
# reciprocal check: x^4 * cp(1/x) == cp
recip = sp.expand(x**4 * cp.subs(x, 1/x))
assert sp.expand(recip - cp) == 0, "charpoly not reciprocal"
print("  -> SL(4,Z), reciprocal charpoly CONFIRMED")

# Shear actions. S_ij = I + E_ij acts on the LEFT as row_i += row_j.
def row_shear(M, i, j):
    M2 = M.copy()
    M2[i, :] = M2[i, :] + M2[j, :]
    return sp.simplify(M2)

A_img = row_shear(R, 0, 3)   # S_03
R_aplus = R.subs(a, a+1)
print("\nA = S_03 : R_{a,m} -> R_{a+1,m} ?",
      sp.simplify(A_img - R_aplus) == sp.zeros(4))
assert sp.simplify(A_img - R_aplus) == sp.zeros(4)

C_img = row_shear(R, 2, 3)   # S_23
R_mplus = R.subs(m, m+1)
print("C = S_23 : R_{a,m} -> R_{a,m+1} ?",
      sp.simplify(C_img - R_mplus) == sp.zeros(4))
assert sp.simplify(C_img - R_mplus) == sp.zeros(4)

# Invariant symmetric form: solve M^T G M = G for symmetric G, generic.
g = sp.symbols('g0:16')
G = sp.Matrix(4, 4, lambda i, j: g[4*i+j])
# impose symmetry
sym_constr = [G[i, j] - G[j, i] for i in range(4) for j in range(i+1, 4)]
inv = R.T * G * R - G
eqs = [sp.expand(e) for e in inv] + sym_constr
sol = sp.solve(eqs, list(g), dict=True)
print("\n# of solution families for M^T G M = G (symmetric):", len(sol))
assert len(sol) >= 1
Gsol = G.subs(sol[0])
# pick a representative nonzero G by setting free params to convenient values
free = sorted(Gsol.free_symbols, key=lambda s: s.name)
print("free params in G:", free)

# Verify the chosen G is genuinely invariant and symmetric symbolically
Gtest = Gsol
assert sp.simplify(Gtest - Gtest.T) == sp.zeros(4), "G not symmetric"
assert sp.simplify(R.T*Gtest*R - Gtest) == sp.zeros(4), "G not invariant"
detG = sp.factor(Gtest.det())
print("det(G) (symbolic, with free params) =", detG)

# Set free params to make it the canonical scale; check det(G) proportional to -delta/(m+1).
delta = 2*a - 1 - m
# substitute each free param -> 1 to get a concrete representative
subsmap = {f: 1 for f in free}
Gc = sp.simplify(Gtest.subs(subsmap))
if sp.simplify(Gc - Gc.T) == sp.zeros(4) and sp.simplify(R.T*Gc*R - Gc) == sp.zeros(4) and Gc != sp.zeros(4):
    detGc = sp.factor(Gc.det())
    print("det(G) at free=1                    =", detGc)
    ratio = sp.simplify(detGc / (-delta/(m+1)))
    print("det(Gc) / (-delta/(m+1))            =", ratio, "(const => proportional)")

print("\nSignature on the live cone (delta>=1, m>=0): numeric check")
def signature_at(av, mv, Gexpr, free):
    Gn = Gexpr.subs({a: av, m: mv})
    Gn = Gn.subs({f: 1 for f in free})
    Gn = np.array(Gn.tolist(), dtype=float)
    Gn = 0.5*(Gn + Gn.T)
    ev = np.linalg.eigvalsh(Gn)
    pos = int(np.sum(ev > 1e-9)); neg = int(np.sum(ev < -1e-9))
    return pos, neg, ev
for (av, mv) in [(8, 0), (8, 2), (10, 5), (20, 10), (50, 30)]:
    dval = 2*av - 1 - mv
    if dval >= 1 and mv >= 0:
        pos, neg, ev = signature_at(av, mv, Gtest, free)
        print(f"  a={av:3d} m={mv:3d} delta={dval:3d}: signature (+,-)=({pos},{neg})")

print("\n=> delta = 2a-1-m is the wall coord; A:+2, C:-1; wall delta=0. CONFIRMED.")

print("\n" + "="*72)
print("PART 2: combinatorial core -- wall-avoiding {A,C} word count")
print("="*72)

# Admissibility convention (the careful one):
#   start at delta = d (d>=1).
#   each letter updates delta. A word is admissible iff delta stays >= 1
#   at EVERY prefix (i.e., delta=0 or below is forbidden = hitting/crossing wall).
#   A: +2 always keeps >=1.  C: -1 allowed only if current delta >= 2.
#
# This matches the handoff recurrence W_{n+1}(d)=W_n(d+2)+1_{d>=2}W_n(d-1).
# I re-derive it freshly by DP over the (bounded) reachable delta range,
# AND independently by brute-force enumeration at small n.

def count_dp(d0, N):
    """Exact counts W_n(d0) for n=0..N via forward DP on delta-distribution."""
    # state: dict delta -> number of admissible length-n words ending at that delta
    from collections import defaultdict
    cur = {d0: 1}
    counts = [1]  # W_0 = 1
    for n in range(1, N+1):
        nxt = defaultdict(int)
        for d, c in cur.items():
            # A: d -> d+2 (always >=1 since d>=1)
            nxt[d+2] += c
            # C: d -> d-1, allowed only if d-1 >= 1, i.e. d >= 2
            if d-1 >= 1:
                nxt[d-1] += c
        cur = dict(nxt)
        counts.append(sum(cur.values()))
    return counts

def count_brute(d0, N):
    """Brute-force enumerate all 2^n words, count admissible. Small N only."""
    res = [0]*(N+1)
    res[0] = 1
    # iterate over all words length 1..N
    from itertools import product
    for n in range(1, N+1):
        c = 0
        for w in product('AC', repeat=n):
            d = d0
            ok = True
            for ch in w:
                d = d+2 if ch == 'A' else d-1
                if d < 1:
                    ok = False
                    break
            if ok:
                c += 1
        res[n] = c
    return res

# Cross-check DP vs brute force at small n for two starts
for d0 in [1, 3, 15]:
    Nb = 14
    dp = count_dp(d0, Nb)
    bf = count_brute(d0, Nb)
    assert dp == bf, f"DP != brute for d0={d0}: {dp} vs {bf}"
    print(f"d0={d0:2d}: DP==brute through n={Nb}  OK   counts={dp}")

# Reproduce the handoff's published tables to compare (NOT trust, compare).
print("\nReproduce handoff tables:")
dp3 = count_dp(3, 20)
print("delta=3 :", dp3)
print("  handoff:", [1,2,4,7,14,28,53,106,212,412,824,1648,3241,6482,12964,
                     25655,51310,102620,203812,407624,815248])
dp15 = count_dp(15, 20)
print("delta=15:", dp15)
print("  handoff:", [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,
                     32767,65534,131068,262121,524242,1048484])

print("\n" + "="*72)
print("PART 3: entropy limit  (1/n) log W_n(d) -> log 2 ?")
print("="*72)

# Use big-N DP with Python ints (exact). delta range grows with n, fine.
def entropy_curve(d0, N):
    counts = count_dp(d0, N)
    out = []
    for n in range(1, N+1):
        out.append((n, counts[n], log(counts[n])/n))
    return counts, out

log2 = log(2.0)
print(f"target log 2 = {log2:.12f}\n")
for d0 in [1, 2, 3, 15]:
    N = 4000
    counts, curve = entropy_curve(d0, N)
    for n in [10, 50, 100, 500, 1000, 2000, 4000]:
        c = counts[n]
        val = log(c)/n
        print(f"  d0={d0:2d} n={n:5d}: (1/n)log W = {val:.10f}   gap to log2 = {val-log2:+.3e}")
    print()

# Transfer-operator / generating-function view of the rate:
# The number of unrestricted words is 2^n (rate log2). The wall-avoiding count
# is 2^n times the survival probability P(no hit). If survival prob -> positive
# constant (transient walk, positive drift), the rate is exactly log2.
print("Drift of the uniform walk: E[step] = (1/2)(+2)+(1/2)(-1) = +1/2 > 0 (transient).")

# Independent survival-probability check: simulate uniform random words, measure
# fraction that survive to length n, see it stabilises (positive) -> rate=log2.
rng = np.random.default_rng(20260616)
def survival_fraction(d0, n, trials=200000):
    # vectorized: steps +2 (A) or -1 (C) each w.p. 1/2
    steps = np.where(rng.random((trials, n)) < 0.5, 2, -1)
    delta = d0 + np.cumsum(steps, axis=1)
    survive = np.all(delta >= 1, axis=1)
    return survive.mean()

print("\nMonte-Carlo survival fraction P(delta>=1 all prefixes) (uniform words):")
for d0 in [1, 3, 15]:
    for n in [50, 200, 1000]:
        f = survival_fraction(d0, n)
        print(f"  d0={d0:2d} n={n:5d}: survival ~ {f:.4f}   (=> W_n ~ {f:.3f} * 2^n)")

# First-passage equation cross-check: p_d (prob ever hit 0) satisfies
# p_d = 1/2 p_{d+2} + 1/2 p_{d-1}, p_0=1, bounded -> p_d = phi^{-d}.
phi = (1+5**0.5)/2
print("\nFirst-passage prob to wall p_d = phi^{-d}? verify recurrence p_d=1/2 p_{d+2}+1/2 p_{d-1}:")
for d in [1, 2, 3, 5, 10]:
    lhs = phi**(-d)
    rhs = 0.5*phi**(-(d+2)) + 0.5*phi**(-(d-1))
    print(f"  d={d:2d}: phi^-d={lhs:.8f}  1/2 p_(d+2)+1/2 p_(d-1)={rhs:.8f}  match={abs(lhs-rhs)<1e-12}")
print(f"  survival prob from d:  1 - phi^-d > 0  (e.g. d=1: {1-phi**-1:.4f}, d=15: {1-phi**-15:.6f})")

print("\n" + "="*72)
print("VERDICT computations")
print("="*72)
# Final numeric verdict: at large n the rate must be within tol of log2, AND
# the boundary correction (log W_n - n log2) should be bounded (sub-exponential).
N = 8000
for d0 in [1, 3, 15]:
    counts = count_dp(d0, N)
    rate = log(counts[N])/N
    correction = log(counts[N]) - N*log2  # = log(survival prob) -> bounded const
    print(f"d0={d0:2d}: rate@n={N} = {rate:.10f}  (log2={log2:.10f}, gap={rate-log2:+.2e}); "
          f"log W_n - n log2 = {correction:.5f}")
