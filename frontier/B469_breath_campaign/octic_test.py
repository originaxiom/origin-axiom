#!/usr/bin/env python3
"""Decisive: evaluate the octic at s464's fiber-subgroup traces; also get the
fiber trace triple (tr a, tr c, tr ac) and test against BOTH components."""
import snappy, mpmath as mp
mp.mp.dps = 40
M = snappy.Manifold('b++RRRLLL')
G = M.fundamental_group()
def tr(w):
    m = G.SL2C(w)
    return mp.mpc(m[0,0]) + mp.mpc(m[1,1])
oct_c = [3, -3, 7, 15, 21, -5, 6, -1, 1]  # c0..c8
def octic(v):
    return sum(c * v**k for k, c in enumerate(oct_c))
def quad(v):  # z^2 - z + 2
    return v*v - v + 2
cands = {'a': tr('a'), 'c': tr('c'), 'ac': tr('ac'), 'aC': tr('aC'), 'abAB': tr('abAB'), 'cbCB': tr('cbCB')}
for nm, v in cands.items():
    print(f"tr({nm}) = {complex(v):.10f}  |octic| = {float(abs(octic(v))):.3e}  |quad| = {float(abs(quad(v))):.3e}", flush=True)
# the fiber triple's kappa: tr[a,c] should be -2 if (a,c) is a fiber basis
x, y, z = tr('a'), tr('c'), tr('ac')
kappa = x*x + y*y + z*z - x*y*z - 2
print(f"kappa(a,c) = {complex(kappa):.8f}  (fiber basis iff -2)", flush=True)
