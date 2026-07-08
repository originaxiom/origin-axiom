#!/usr/bin/env python3
"""B461 rung 1 — the incoming-claims table + the SL(2)/Q(i) gate, for L6a4 + controls."""
import numpy as np
import sympy as sp
import snappy

VOCT = 3.663862376708876

def survey(name):
    M = snappy.ManifoldHP(name)
    vol = float(M.volume())
    print(f"== {name}: vol={vol:.12f}  cusps={M.num_cusps()}  H1={M.homology()}  tets={M.num_tetrahedra()}")
    return M, vol

print("---- incoming-claims verification ----")
M, vol = survey('L6a4')
print(f"   vol/v_oct = {vol/VOCT:.10f}   (claim: exactly 2)")
# trace field via shape minpolys (the Q(i) gate)
shapes = M.tetrahedra_shapes('rect')
t = sp.Symbol('t')
fields = set()
for z in shapes:
    zc = complex(z)
    # recognize the minimal polynomial via PSLQ-style integer fit on 1, z, z^2
    best = None
    for a2 in range(0, 5):
        for a1 in range(-8, 9):
            for a0 in range(-8, 9):
                if a2 == 0 and a1 == 0:
                    continue
                if abs(a2*zc*zc + a1*zc + a0) < 1e-9:
                    best = (a2, a1, a0)
                    break
            if best:
                break
        if best:
            break
    fields.add(best)
print(f"   shape minpolys: {fields}   (gate: all in Q(i))")
print()
print("---- controls ----")
for nm in ['m129', 's776', 'o9_39906']:   # m129 = Whitehead link exterior
    try:
        survey(nm)
    except Exception as e:
        print(f"== {nm}: FAILED {e}")
print()
print("---- SL(2) exact (obstruction classes; Groebner - small) ----")
for nm in ['L6a4']:
    M2 = snappy.Manifold(nm)
    try:
        V = M2.ptolemy_variety(2, 'all')
        n_obs = len(V)
        print(f"{nm}: SL(2) obstruction classes = {n_obs}")
        for i, Vi in enumerate(V):
            vars_ = [str(v) for v in Vi.variables]
            print(f"   class {i}: {len(vars_)} vars, {len(Vi.equations)} eqs")
    except Exception as e:
        print(f"{nm}: ptolemy failed {e}")
