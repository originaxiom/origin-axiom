"""Regenerates y080_rise_validation.txt (provenance per prereg v3 D-5)."""
import sys
sys.path.insert(0, 'frontier/B792_maass_m004_eigenvalues')
from hejhal_m004 import Lattice, build_moves, find_cusp_lattice, reduce_pt, sample_points
tau, _, _, _ = find_cusp_lattice()
lat = Lattice(tau); moves = build_moves()
for Y in (0.75, 0.80):
    zs = sample_points(lat, 200, rng_seed=3)
    rise, tmin = 0, 9.9
    for z in zs:
        _, t, mv = reduce_pt(lat, moves, z, Y)
        if mv and t > Y*(1+1e-9): rise += 1
        tmin = min(tmin, t)
    print(f"Y = {Y}: raised {rise}/200, min t* = {tmin:.6f}, margin t*-Y = {tmin-Y:.6f}, assert >= 0.05: {tmin-Y >= 0.05}")
