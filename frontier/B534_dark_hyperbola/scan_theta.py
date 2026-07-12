#!/usr/bin/env python3
"""B534 step 1: theta-lift convention scan (float, then exact follows)."""
import numpy as np
from itertools import product

def ops(p):
    z = np.exp(2j*np.pi/p)
    W1 = np.diag([z**((n*(n-1)//2) % p) for n in range(p)])
    F = np.array([[z**((a*b) % p) for b in range(p)] for a in range(p)])/np.sqrt(p)
    W2 = F @ np.conj(W1) @ np.conj(F).T
    Par = np.zeros((p, p))
    for n in range(p):
        Par[n, (-n) % p] = 1
    return W1, W2, Par

for p in (3, 5, 7, 11, 13, 17, 19, 23):
    W1, W2, Par = ops(p)
    dark = []
    W1s = [np.linalg.matrix_power(W1, j) for j in range(p)]
    W2s = [np.linalg.matrix_power(W2, l) for l in range(p)]
    for j, l in product(range(p), range(p)):
        t = np.trace(Par @ W1s[j] @ W2s[l])
        if abs(t) < 1e-8:
            dark.append((j, l))
    claim = sorted((j, l) for j in range(p) for l in range(p)
                   if (j*l) % p == (-4) % p and not (j == 2 and l == (p-2) % p))
    match = sorted(dark) == claim
    print(f"p={p:2d}: #dark={len(dark):3d} claim p-2={p-2:3d}  "
          f"dark==hyperbola\\{{(2,p-2)}}: {match}")
    if not match and len(dark) < 30:
        print(f"   dark:  {sorted(dark)}")
        print(f"   claim: {claim}")
