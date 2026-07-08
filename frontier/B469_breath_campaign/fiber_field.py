#!/usr/bin/env python3
"""s464 fiber-subgroup traces: words of total degree 0 under pi1 -> Z; test
membership in Q(sqrt-7) (Re rational, Im/sqrt(7) rational) at 30 digits."""
import snappy, mpmath as mp
from fractions import Fraction
mp.mp.dps = 40
M = snappy.Manifold('b++RRRLLL')
M.set_peripheral_curves('shortest')
G = M.fundamental_group()
print("gens:", G.generators(), "relators:", G.relators(), flush=True)
# abelianization degrees -> Z (mod torsion): use homology presentation via snappy
print("H1:", M.homology(), flush=True)
import itertools, re
gens = G.generators()
# infer Z-degree per generator from the abelianized relators
rel = G.relators()
import numpy as np
def ab(word):
    v = [0]*len(gens)
    for ch in word:
        i = gens.index(ch.lower())
        v[i] += 1 if ch.islower() else -1
    return v
A = np.array([ab(r) for r in rel])
from math import gcd
# kernel of A^T gives H1 as coker; degree map = generator of Hom(H1,Z): solve A @ d = 0 over Q
import sympy as sp
Am = sp.Matrix(A)
ns = Am.nullspace()
print("deg candidates:", [list(v) for v in ns], flush=True)
d = [int(x) for x in (ns[0] * sp.lcm([sp.fraction(x)[1] for x in ns[0]]))] if ns else None
print("deg map:", d, flush=True)
def trace(word):
    m = G.SL2C(word)
    return complex(m[0,0] + m[1,1])
def in_Qsqrt7(c, digits=25):
    re_r = mp.pslq([mp.mpf(c.real), 1], maxcoeff=10**8)
    im_r = mp.pslq([mp.mpf(c.imag)/mp.sqrt(7), 1], maxcoeff=10**8)
    return (re_r is not None, im_r is not None)
# degree-0 sample words
if d:
    cand = []
    for w in ['ab','ba','aabb','abab','aB','Ab','abAB','aabbab']:
        deg = sum((d[gens.index(ch.lower())] * (1 if ch.islower() else -1)) for ch in w)
        if deg == 0: cand.append(w)
    # also single gens if degree 0
    for i,g in enumerate(gens):
        if d[i] == 0: cand.append(g)
    print("degree-0 words:", cand, flush=True)
    for w in cand[:8]:
        t = trace(w)
        print(f"  tr({w}) = {t:.12f}  in Q(sqrt-7)? {in_Qsqrt7(t)}", flush=True)
