#!/usr/bin/env python3
"""R09 control: the exclusion Hom(G, R+) = 0 must be a property of the
TARGET (R+ torsion-free), not an artifact of the instrument.  Plant the
excluded thing where it can exist and confirm the same machinery finds it.

Control 1: G = SL(2,3) has G^ab = Z/3, so a nontrivial hom EXISTS into a
  target with 3-torsion (mu_3 in C*).  Build it explicitly from the coset
  map G -> G/[G,G] and verify multiplicativity exactly (sympy roots of
  unity), and verify it is nontrivial.
Control 2: G = Z (not finite) has nontrivial Hom(Z, R+): n -> 2^n.
  Verify hom property exactly with Fractions; so finiteness is load-bearing.
Control 3: the decisive criterion x^e = 1 => x = 1 in R+ FAILS in C*
  (solve exactly: x^3 = 1 has 3 solutions in C, 1 in R+), so the
  instrument distinguishes the two targets rather than always saying 0.
"""
import itertools, sys
from fractions import Fraction
import sympy as sp

def log(*a): print(*a); sys.stdout.flush()

def mat_mul_mod(n):
    def mul(A, B):
        (a, b, c, d), (e, f, g, h) = A, B
        return ((a*e + b*g) % n, (a*f + b*h) % n,
                (c*e + d*g) % n, (c*f + d*h) % n)
    return mul

n = 3
mul = mat_mul_mod(n)
inv = lambda A: ((A[3]) % n, (-A[1]) % n, (-A[2]) % n, (A[0]) % n)  # det=1
G = {A for A in itertools.product(range(n), repeat=2) for _ in [0]}
G = set()
for a, b, c, d in itertools.product(range(n), repeat=4):
    if (a*d - b*c) % n == 1:
        G.add((a, b, c, d))
assert len(G) == 24

# derived subgroup by full commutator closure
def closure(gens, mul):
    el = set(gens); fr = list(gens); gl = list(gens)
    while fr:
        new = []
        for x in fr:
            for g in gl:
                p = mul(x, g)
                if p not in el:
                    el.add(p); new.append(p)
        fr = new
    return el
comms = {mul(mul(a, b), mul(inv(a), inv(b))) for a in G for b in G}
D = closure(comms, mul)
assert len(D) == 8 and len(G) // len(D) == 3

# coset map G -> G/D (a Z/3): label cosets, verify it is a hom, exhibit
# the induced character chi: G -> mu_3 in C* and check chi nontrivial.
cosets = []
for g in sorted(G):
    C = frozenset(mul(g, d) for d in D)
    if C not in cosets:
        cosets.append(C)
assert len(cosets) == 3
def cls(g):
    for i, C in enumerate(cosets):
        if g in C: return i
    raise AssertionError
# coset multiplication table => must be Z/3
identity_coset = cls((1, 0, 0, 1))
omega = sp.exp(2*sp.pi*sp.I/3)
# fix an isomorphism cosets -> Z/3 consistently: pick generator coset
table = {}
for i, C in enumerate(cosets):
    gi = next(iter(C))
    table[i] = gi
# find labeling as powers of a generating coset
gen_i = next(i for i in range(3) if i != identity_coset)
g0 = table[gen_i]
lab = {identity_coset: 0, cls(g0): 1, cls(mul(g0, g0)): 2}
assert sorted(lab.values()) == [0, 1, 2]
chi = {g: omega**lab[cls(g)] for g in G}
# exact multiplicativity check over all 24^2 pairs
for a in G:
    for b in G:
        assert sp.simplify(chi[mul(a, b)] - chi[a]*chi[b]) == 0
nontriv = sum(1 for g in G if sp.simplify(chi[g] - 1) != 0)
assert nontriv == 16  # two nonidentity cosets x 8 elements
log("Control 1 PASS: explicit nontrivial chi: SL(2,3) -> mu_3 in C*, "
    "multiplicative on all 576 pairs; nontrivial on 16/24 elements.")

# Control 2: Hom(Z, R+) nontrivial: phi(n) = 2^n, exact Fractions
phi = lambda k: Fraction(2)**k
for a in range(-6, 7):
    for b in range(-6, 7):
        assert phi(a + b) == phi(a) * phi(b)
assert phi(1) != 1
log("Control 2 PASS: phi(n)=2^n is a nontrivial hom Z -> R+ (exact); "
    "finiteness of G is load-bearing.")

# Control 3: the decisive criterion distinguishes targets
x = sp.symbols("x")
sols_C = sp.solve(sp.Eq(x**3, 1), x)
sols_Rp = [s for s in sols_C if s.is_real and s.is_positive]
assert len(sols_C) == 3 and sols_Rp == [1]
log("Control 3 PASS: x^3=1 has 3 solutions in C but only x=1 in R+; "
    "the vanishing is carried by torsion-freeness of R+, not by the instrument.")
log("ALL CONTROLS PASS")
