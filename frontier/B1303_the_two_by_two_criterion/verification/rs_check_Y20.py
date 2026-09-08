#!/usr/bin/env python3
"""Independent check of the 2x2 criterion where it was never validated: the 41-part of Y_20 (the first even level with a
splitting prime whose roots have exact order n).  Reidemeister-Schreier presentation (B1274), Smith form, the 41-torsion
characters (1680) and 11-torsion characters (120, control: pulled back from Y_5, expected h^1 = 1 on 20), h^1 by
B1278's Fox calculus on one representative per deck orbit."""
import sys, math, time, collections
import numpy as np, mpmath as mp
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parents[2] / 'B1301_the_towers_alphabet' / 'verification'))
import tower_alphabet as T
SF = T.SF; TW = T.TW
n = 20
gens, rels = TW.presentation(n, branched=True)
Rm = SF.relation_matrix(gens, rels)
D, U, V = SF.smith_with_transforms(Rm)
g = V.shape[0]
inv = [int(D[j, j]) if j < D.shape[0] and j < D.shape[1] else 0 for j in range(g)]
tors = [d for d in inv if d not in (0, 1)]
m = 1
for d in tors: m = m * d // math.gcd(m, d)
print(f"Y_20 (RS): H_1 = {tors}, exponent {m}", flush=True)
Vi = [[int(V[i, j]) for j in range(g)] for i in range(g)]
def chars_of_order_dividing(p):
    # characters a = V c with c_j in multiples of (d_j / gcd(d_j, p)) * (m / d_j) ... simpler: c_j ranges over the p-torsion of Z/d_j
    ranges = []
    for j in range(g):
        d = inv[j] if inv[j] != 0 else m
        gcd = math.gcd(d, m) if d != 0 else m
        step = m // gcd
        # elements c in {step * i} (i < gcd) with p * c = 0 mod m  <=>  i in multiples of gcd/gcd(gcd,p)
        t = math.gcd(gcd, p)
        ranges.append([step * (gcd // t) * i for i in range(t)])
    out = []
    import itertools
    for c in itertools.product(*ranges):
        a = tuple(sum(Vi[i][j] * c[j] for j in range(g)) % m for i in range(g))
        out.append(a)
    return out
mp.mp.dps = 40
for p in (11, 41):
    t0 = time.time()
    chars = [a for a in chars_of_order_dividing(p) if any(a)]
    seen = set(); reps = []
    for a in chars:
        if a in seen: continue
        orb = [a]; b = T.deck(a, n)
        while b != a:
            orb.append(b); b = T.deck(b, n)
        seen.update(orb); reps.append((a, len(orb)))
    res = collections.Counter()
    for a, size in reps:
        h, h0, lo, hi = SF.h1_numeric(gens, rels, a, m)
        res[h] += size
    print(f"  order-{p} characters: {len(chars)} in {len(reps)} deck orbits; h^1 distribution {dict(res)}  ({time.time() - t0:.0f} s)", flush=True)
