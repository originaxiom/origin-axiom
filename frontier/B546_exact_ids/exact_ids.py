#!/usr/bin/env python3
"""B546 (F-P1a): exact-grade IDS for the species chain via Sturm counts.

Removes B543's 1/N eigen-solver floor: IDS(E) = (# eigenvalues < E)/N by the
tridiagonal Sturm/LDL recurrence at N = 10^6. Evaluated at the gap-center
energies found at N = 3000; labels compared to the dictionary at 1e-6 scale.
"""
import numpy as np
from scipy.linalg import eigh_tridiagonal

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
PHI = (1 + np.sqrt(5)) / 2
TAU = np.sqrt(PHI)
S = PHI + 1 + PHI*TAU + TAU
F = {'a': PHI/S, 'b': 1/S, 'A': PHI*TAU/S, 'B': TAU/S}
DICT = {'f_b': F['b'], 'f_B': F['B'], 'f_a': F['a'], 'f_A': F['A'],
        'f_a+f_b': F['a'] + F['b']}

def word(N):
    w = 'a'
    while len(w) < N:
        w = ''.join(SUB[c] for c in w)
    return w[:N]

def sturm_ids(hop, E):
    """(# eigenvalues < E) / N for the zero-diagonal tridiagonal chain."""
    d = -E
    count = 1 if d < 0 else 0
    for t in hop:
        d = -E - t*t/d
        if d < 0:
            count += 1
    return count / (len(hop) + 1)

COUP = {'a': 1.0, 'b': 0.8, 'A': 0.6, 'B': 0.4}

# gap centers from the N=3000 spectrum
w3 = word(3000)
hop3 = np.array([COUP[c] for c in w3[:-1]])
ev = eigh_tridiagonal(np.zeros(3000), hop3, eigvals_only=True)
gaps = np.diff(ev)
top = sorted(np.argsort(gaps)[::-1][:12])
centers = [(ev[i] + ev[i+1])/2 for i in top]

N = 1_000_000
wN = word(N)
hopN = np.array([COUP[c] for c in wN[:-1]])
print(f"N = {N}: exact-grade IDS at the 12 gap centers (resolution 1e-6):")
for E in centers:
    ids = sturm_ids(hopN, E)
    x = min(ids, 1 - ids)
    name, val = min(DICT.items(), key=lambda kv: abs(kv[1] - x))
    d = abs(val - x)
    tag = f"= {name} ({d:.1e})" if d < 5e-6 else f"nearest {name} ({d:.1e})"
    print(f"  E = {E:+.4f}: IDS(folded) = {x:.7f}  {tag}")
