"""Is the fibre group's sphere list complete near the tube? Penetration of the tube's axis points by F-spheres from two
word searches (depth 8, radius > 0.08 vs depth 10, radius > 0.03); also the axis points' own heights."""
import sys, os, math, pickle, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "B1846_the_metrics_read_out", "verification"))
from stage_b_surface import fibre_generators, setup
G, H, info, _wf = setup("b++LLLLLLRLR", 12, 0.33, 9604, 7)          # rebuilds and caches if no cache is present
from step4_tube import shortest_loxodromic, axis_points
lat = G.lat; wf = lat.w1 if lat.c1 == 0 else lat.w2
x, y, Kt = fibre_generators(G, wf)
X, Lx, cx = shortest_loxodromic(G, depth=6)
pts, ends = axis_points(X, n=64)
print(f"tube element: length {Lx.real:.6f}; axis endpoints {ends[0]:.4f}, {ends[1]:.4f}; axis heights {min(p[1] for p in pts):.4f}..{max(p[1] for p in pts):.4f}")
import importlib
for depth, rmin in ((8, 0.08), (10, 0.03)):
    os.environ["OA_FDEPTH"] = str(depth); os.environ["OA_FRMIN"] = str(rmin)
    import stage_b_modulus as SB; importlib.reload(SB)
    els = SB.fibre_spheres(G, x, y, depth=depth)
    c = np.array([M[1, 0] for _, M, _ in els]); d = np.array([M[1, 1] for _, M, _ in els])
    pens = []
    for z, t in pts:
        # all lattice translates along wf near the point: shift the point instead (period 0 translation)
        best = -1e9
        for n in (-1, 0, 1):
            zz = z + n * wf
            p = 1 - (np.abs(c * zz + d) ** 2 + np.abs(c) ** 2 * t * t)
            best = max(best, p.max())
        pens.append(best)
    pens = np.array(pens)
    print(f"   depth {depth}, radius > {rmin}: {len(els)} spheres; axis points inside some sphere: {np.sum(pens > 0)}/64; max pen {pens.max():+.3e}")
