#!/usr/bin/env python3
"""Geometric-component ID: census identity + shape minpoly (brute integer search,
deg<=4, |coeff|<=40) for the bundles R^m L^m, m=1,2,3."""
import numpy as np, itertools
import snappy

def minpoly_brute(s, maxdeg=4, maxc=40):
    powers = np.array([s**k for k in range(maxdeg+1)])
    best = None
    for deg in range(2, maxdeg+1):
        rng = np.arange(-maxc, maxc+1)
        # monic: c_deg = 1; search lower coeffs
        grids = np.meshgrid(*([rng]*deg), indexing='ij')
        coeffs = np.stack([g.ravel() for g in grids], axis=1)  # (n, deg): c_0..c_{deg-1}
        vals = coeffs @ powers[:deg] + powers[deg]
        idx = np.argmin(np.abs(vals))
        if abs(vals[idx]) < 1e-9:
            c = list(coeffs[idx]) + [1]
            return c, deg
        if deg >= 3 and maxc > 12: maxc = 12  # keep the grid tractable
    return None, None

for m in (1, 2, 3):
    name = 'b++' + 'R'*m + 'L'*m
    M = snappy.Manifold(name)
    ident = M.identify()
    vol = float(M.volume())
    s0 = complex(M.tetrahedra_shapes(part='rect')[0])
    c, deg = minpoly_brute(s0)
    print(f"m={m} {name}: identify={ident}, vol={vol:.8f}, shape minpoly coeffs (c0..cd)={c}", flush=True)
print("GEOM ID DONE", flush=True)
