#!/usr/bin/env python3
"""POST HOC to V-LISTEN (written after its run showed three largest orbits of 648 points at mod 81; not blind):
P1  the three 648-point orbits over the common point on the cusp's leaf mod 81 have the same characteristic polynomial
    of W+ = P_L + P_R (so "the largest orbit" in B1996/B1997 is not a choice among different spectra);
P2  which of the seat's maps (the three sign actions, the swap (x,y,z) -> (y,x,z), the cycle (x,y,z) -> (y,z,x)) carry
    one 648-orbit onto another.
    python3 -B v_listen_posthoc.py
"""
import itertools, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from flint import fmpz_mat

m = 81
L = lambda q: (q[0], q[2], (q[0] * q[2] - q[1]) % m)
R = lambda q: (q[2], q[1], (q[1] * q[2] - q[0]) % m)
over = [q for q in itertools.product(range(0, m, 3), repeat=3) if (q[0] ** 2 + q[1] ** 2 + q[2] ** 2 - q[0] * q[1] * q[2]) % m == 0]
seen, orbs = set(), []
for s in over:
    if s in seen:
        continue
    comp, st = {s}, [s]
    while st:
        q = st.pop()
        for nb in (L(q), R(q)):
            if nb not in comp:
                comp.add(nb); st.append(nb)
    seen |= comp; orbs.append(frozenset(comp))
big = [o for o in orbs if len(o) == 648]
cps = []
for o in big:
    pts = sorted(o); idx = {q: i for i, q in enumerate(pts)}; n = len(pts)
    W = [[0] * n for _ in range(n)]
    for q in pts:
        W[idx[q]][idx[L(q)]] += 1; W[idx[q]][idx[R(q)]] += 1
    cps.append(fmpz_mat(W).charpoly())
print("P1 three 648-orbits; characteristic polynomials equal: %s" % (cps[0] == cps[1] == cps[2]))
maps = {"sign(-,-,+)": lambda q: ((-q[0]) % m, (-q[1]) % m, q[2]), "sign(-,+,-)": lambda q: ((-q[0]) % m, q[1], (-q[2]) % m),
        "sign(+,-,-)": lambda q: (q[0], (-q[1]) % m, (-q[2]) % m), "swap": lambda q: (q[1], q[0], q[2]),
        "cycle": lambda q: (q[1], q[2], q[0])}
for name, f in maps.items():
    img = [next(j for j, o in enumerate(big) if f(next(iter(b))) in o) if any(f(next(iter(b))) in o for o in big) else None for b in big]
    whole = [all(f(q) in big[img[i]] for q in b) if img[i] is not None else False for i, b in enumerate(big)]
    print("P2 %-12s sends orbit i to %s (whole orbit: %s)" % (name, img, whole))
