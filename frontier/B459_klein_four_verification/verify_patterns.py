#!/usr/bin/env python3
"""B459 — verify the 'Klein-four selection rule' addendum (2026-07-07), exactly.

Claim: FT-ing each of the four genus-channel coordinates (1, sqrt5, sqrt-3, sqrt-15) of the
pair seam to the dual torus (Z/20 x Z/12), only FIVE of 16 vanishing patterns occur:
{} : 120, {r,s} : 20, {q,s} : 20, {q,r,s} : 10, {p,q,r,s} : 70  (p=rat, q=sqrt5, r=sqrt-3, s=sqrt-15).
Laws: no single vanishing; s dies in every nontrivial pattern; the patterns = the SUBFIELD
LATTICE of Q(sqrt5, sqrt-3) (the honest mechanism — Galois equivariance, not a group miracle).
"""
import sys, os
from fractions import Fraction as Fr
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
from step0_exact_matrices import build_theta_W, matrix_order, pair_smatrix
import cyclo_engine as E

W1 = build_theta_W(1); W2 = build_theta_W(2)
_, p1 = matrix_order(W1); _, p2 = matrix_order(W2)
sm = pair_smatrix(p1, p2)

# four channel tables on the (a,b) grid
chan = {i: {(a, b): v[i] for (a, b), v in sm.items() if v[i] != 0} for i in range(4)}
print("channel support sizes (cells):", {i: len(c) for i, c in chan.items()}, flush=True)

def ft(table):
    grid = {}
    for x in range(20):
        for y in range(12):
            t = E.ZERO
            for (a, b), val in table.items():
                t = E.add(t, E.scal(Fr(val), E.zeta((3*a*x + 5*b*y) % 60)))
            grid[(x, y)] = t
    return grid

grids = {i: ft(chan[i]) for i in range(4)}
names = ['p(rat)', 'q(sqrt5)', 'r(sqrt-3)', 's(sqrt-15)']
pat = Counter()
per_point = {}
for x in range(20):
    for y in range(12):
        z = tuple(1 if grids[i][(x, y)] == E.ZERO else 0 for i in range(4))
        pat[z] += 1
        per_point[(x, y)] = z

print("\nvanishing patterns (1 = channel is ZERO at the point) and counts:")
for z, n in sorted(pat.items(), key=lambda kv: -kv[1]):
    label = "{" + ",".join(names[i] for i in range(4) if z[i]) + "}"
    print(f"  {z}  {label:32s} : {n}")
print(f"\ntotal patterns occurring: {len(pat)} of 16")
# the three laws
single = [z for z in pat if sum(z) == 1]
print(f"Law 1 (no single vanishing): {'PASS' if not single else 'FAIL ' + str(single)}")
nontriv = [z for z in pat if 0 < sum(z)]
law2 = all(z[3] == 1 for z in nontriv)
print(f"Law 2 (s=sqrt-15 dies in every nontrivial pattern): {'PASS' if law2 else 'FAIL'}")
# subfield-lattice check: the occurring patterns should be exactly
# {} (full field), {r,s} (value in Q(sqrt5)), {q,s} (in Q(sqrt-3)), {q,r,s} (in Q), all (0)
expected = {(0,0,0,0), (0,0,1,1), (0,1,0,1), (0,1,1,1), (1,1,1,1)}
print(f"patterns == the subfield lattice of Q(sqrt5,sqrt-3): {set(pat) == expected}")
print(f"the Q(sqrt-15)-valued pattern (q,r dead, s alive) occurs: {(0,1,1,0) in pat}")
# claimed counts
claim = {(0,0,0,0):120, (0,0,1,1):20, (0,1,0,1):20, (0,1,1,1):10, (1,1,1,1):70}
print(f"counts match the addendum (120/20/20/10/70): {all(pat.get(k,0)==v for k,v in claim.items())}")
