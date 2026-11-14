#!/usr/bin/env python3
"""SM-C13b's scope (M35, B1939 section 1): orbit lengths of fibre lines under the tick sigma = [[1, 1], [1, 0]] and under
m004's monodromy sigma^2, mod 2, 5 and 10; and the mark's order-10 halves.  Structure only."""
import json
import pathlib

import numpy as np

S = np.array([[1, 1], [1, 0]])


def orb(P, M, N):
    p = np.array(P) % N
    q = p.copy()
    k = 0
    while True:
        q = (M @ q) % N
        k += 1
        if (q == p).all():
            return k


out = {}
for N in (2, 5, 10):
    pts = [(i, j) for i in range(N) for j in range(N) if (i, j) != (0, 0)]
    out[f"mod {N}"] = {"tick": sorted(set(orb(P, S, N) for P in pts)), "m004": sorted(set(orb(P, S @ S, N) for P in pts))}
halves = {"(7/10, 2/5)": (7, 4), "(1/5, 9/10)": (2, 9), "(7/10, 9/10)": (7, 9)}
out["the mark's order-10 halves"] = {k: {"tick": orb(v, S, 10), "m004": orb(v, S @ S, 10)} for k, v in halves.items()}
out["the mark (2/5, 4/5)"] = {"tick": orb((4, 8), S, 10), "m004": orb((4, 8), S @ S, 10)}
print(json.dumps(out, indent=1))
pathlib.Path(__file__).with_name("scope_orbits.json").write_text(json.dumps(out, indent=1))
