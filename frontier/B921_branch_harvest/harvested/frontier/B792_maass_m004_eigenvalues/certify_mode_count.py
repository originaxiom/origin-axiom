r"""Mode-count certification (cc gate item 2, hold relay).

Two-height stability certifies collocation convergence but not
truncation. Here every banked eigenvalue is re-refined at a SECOND
mode count (margin 21 -> 27, i.e. Bessel-tail cut pushed from ~1e-9
to ~1e-11 relative) at fixed Y = 0.75. Reports per-eigenvalue |dr|
between mode counts and the max — which sets the floor on any
tolerance tau usable in value-comparison tests.

Gate 5-Q.
"""
import json
import sys

import numpy as np

sys.path.insert(0, 'frontier/B792_maass_m004_eigenvalues')
from hejhal_m004 import (Lattice, System, build_moves, find_cusp_lattice,
                        golden_min)  # noqa: E402

OUTDIR = 'frontier/B792_maass_m004_eigenvalues'

banked = []
with open(f"{OUTDIR}/eigenvalues_final.json") as f:
    banked += [(e['r'], e['multiplicity']) for e in
               json.load(f)['eigenvalues']]
with open(f"{OUTDIR}/scanD_refined.json") as f:
    banked += [(e['r'], e['multiplicity']) for e in
               json.load(f)['eigenvalues']]
banked.sort()

tau, _, _, _ = find_cusp_lattice()
lat = Lattice(tau)
moves = build_moves()

print("Building second-mode-count system (margin 27, Y = 0.75) ...")
S_hi = System(lat, moves, 0.75, 10.1, margin=27.0)
S_lo = System(lat, moves, 0.75, 10.1, margin=21.0)
print(f"  margin 21: {len(S_lo.mus)} modes / {len(S_lo.zs)} pts")
print(f"  margin 27: {len(S_hi.mus)} modes / {len(S_hi.zs)} pts", flush=True)
print()

print(f"{'r (banked)':>14} {'r (margin 27)':>15} {'|dr|':>9} "
      f"{'sigma':>9}")
rows = []
worst = 0.0
for r0, mult in banked:
    r1, s1 = golden_min(S_hi.sigma_min, r0 - 0.001, r0 + 0.001, tol=3e-9)
    dr = abs(r1 - r0)
    worst = max(worst, dr)
    rows.append({'r_banked': r0, 'r_margin27': r1, 'dr': dr,
                 'sigma': s1, 'multiplicity': mult})
    print(f"{r0:>14.8f} {r1:>15.8f} {dr:>9.1e} {s1:>9.1e}", flush=True)

print()
print(f"MAX |dr| between mode counts: {worst:.2e}")
print(f"=> honest tolerance floor for any value test: tau >= {worst:.1e}")
print(f"   (relative, on r ~ 4-10: {worst / 4:.1e} .. {worst / 10:.1e})")

with open(f"{OUTDIR}/mode_count_certification.json", 'w') as f:
    json.dump({'margins': [21.0, 27.0], 'Y': 0.75,
               'modes': [len(S_lo.mus), len(S_hi.mus)],
               'rows': rows, 'max_dr': worst}, f, indent=1)
print("Saved mode_count_certification.json")
