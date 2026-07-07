#!/usr/bin/env python3
"""B459 addendum — the within-level control: the tier breakdown across SEED PAIRS.
If the 120/70/20/20/10 breakdown is construction-generic, every pair shows it;
if it varies by pair, the breakdown is pair-arithmetic (address/seed data), not
'the figure-eight's selection rule'. Exact Q(zeta60), same engine as the verification."""
import sys, os
from fractions import Fraction as Fr
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
from step0_exact_matrices import build_theta_W, matrix_order, pair_smatrix
import cyclo_engine as E

def tiers(m1, m2):
    W1 = build_theta_W(m1); W2 = build_theta_W(m2)
    _, p1 = matrix_order(W1); _, p2 = matrix_order(W2)
    sm = pair_smatrix(p1, p2)
    chan = {i: {(a, b): v[i] for (a, b), v in sm.items() if v[i] != 0} for i in range(4)}
    grids = {}
    for i in range(4):
        g = {}
        for x in range(20):
            for y in range(12):
                t = E.ZERO
                for (a, b), val in chan[i].items():
                    t = E.add(t, E.scal(Fr(val), E.zeta((3*a*x + 5*b*y) % 60)))
                g[(x, y)] = t
        grids[i] = g
    pat = Counter()
    for x in range(20):
        for y in range(12):
            z = tuple(1 if grids[i][(x, y)] == E.ZERO else 0 for i in range(4))
            pat[z] += 1
    return pat

LATTICE = {(0,0,0,0):'generic', (0,0,1,1):'in Q(sqrt5)', (0,1,0,1):'in Q(sqrt-3)',
           (0,1,1,1):'in Q', (1,1,1,1):'zero', (0,1,1,0):'in Q(sqrt-15) [absent for (1,2)]'}
for pair in [(1,2), (1,3), (2,3), (2,4), (3,4)]:
    pat = tiers(*pair)
    lattice_ok = set(pat) <= set(LATTICE)
    desc = ", ".join(f"{LATTICE.get(z, 'NON-LATTICE '+str(z))}:{n}" for z, n in sorted(pat.items(), key=lambda kv: -kv[1]))
    print(f"pair {pair}:  subfield-lattice-only={lattice_ok}   {desc}", flush=True)
