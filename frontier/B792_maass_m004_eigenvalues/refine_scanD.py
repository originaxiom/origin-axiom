r"""Refine the scanD window (r in 7.3-10): two-system stability,
multiplicities, S-invariance old/new split. Writes scanD_refined.json.

Gate 5-Q.
"""
import json
import sys

import numpy as np

sys.path.insert(0, 'frontier/B792_maass_m004_eigenvalues')
from eigenvalues_final import S_BIANCHI, eval_f  # noqa: E402
from hejhal_m004 import (K_table, Lattice, System, apply_m, build_moves,
                        find_cusp_lattice, golden_min, reduce_pt)  # noqa: E402

OUTDIR = 'frontier/B792_maass_m004_eigenvalues'

with open(f"{OUTDIR}/scanD_dips.json") as f:
    dips = json.load(f)['dips']

tau, _, _, _ = find_cusp_lattice()
lat = Lattice(tau)
moves = build_moves()

print("Building systems (rmax 10.1) ...")
S1 = System(lat, moves, 0.75, 10.1)
S2 = System(lat, moves, 0.62, 10.1, seed=23)
print(f"  S1: {len(S1.mus)} modes / {len(S1.zs)} pts; "
      f"S2: {len(S2.mus)} modes / {len(S2.zs)} pts", flush=True)


def analyze(S, r):
    KT = K_table(S.args, S.ts, S.wts, [r], [])
    KT = KT.reshape(len(S.norms), len(S.heights))
    V = ((S.Y * KT[S.nrm_idx, 0])[None, :] * S.P0
         - (S.tstar[:, None] * KT[S.nrm_idx, 1:].T) * S.P1)
    cn = np.linalg.norm(V, axis=0)
    cn[cn == 0] = 1
    _, sv, Vh = np.linalg.svd(V / cn[None, :])
    a = Vh[-1].conj() / cn
    rng = np.random.default_rng(5)
    num = den = 0.0
    for _ in range(24):
        z = complex(rng.uniform(-0.5, 0.5), rng.uniform(-1.7, 1.7))
        t = rng.uniform(0.8, 1.1)
        z1, t1, _ = reduce_pt(lat, moves, z, t)
        zs_, ts_ = apply_m(S_BIANCHI, z, t)
        z2, t2, _ = reduce_pt(lat, moves, zs_, ts_)
        if min(t1, t2) < 0.7:
            continue
        f1 = eval_f(S, a, r, z1, t1)
        f2 = eval_f(S, a, r, z2, t2)
        num += abs(f1 - f2) ** 2
        den += abs(f1) ** 2 + abs(f2) ** 2
    return sv[-4:], np.sqrt(num / den) if den else np.nan


results = []
for d in dips:
    r0 = d['r']
    r1, s1 = golden_min(S1.sigma_min, r0 - 0.006, r0 + 0.006, tol=2e-8)
    r2, s2 = golden_min(S2.sigma_min, r1 - 0.004, r1 + 0.004, tol=2e-8)
    tail, inv_dev = analyze(S1, r1)
    mult = int(np.sum(tail < 1e-5))
    stable = abs(r1 - r2) < 5e-4 and s1 < 1e-6 and s2 < 1e-6
    typ = 'OLD' if inv_dev < 1e-3 else 'NEW'
    results.append({'r': r1, 'lambda': 1 + r1 ** 2, 'r_Y2': r2,
                    'dr': abs(r1 - r2), 'sigma_Y1': s1, 'sigma_Y2': s2,
                    'sv_tail': [float(x) for x in tail],
                    'multiplicity': max(mult, 1),
                    'S_invariance_dev': float(inv_dev),
                    'stable': bool(stable), 'type': typ})
    print(f"  {r0:.4f} -> r = {r1:.8f}  lam = {1 + r1**2:.6f}  "
          f"|dr| = {abs(r1 - r2):.1e}  sig = {s1:.1e}/{s2:.1e}  "
          f"mult = {max(mult, 1)}  Sdev = {inv_dev:.1e}  {typ}"
          f"{'  STABLE' if stable else '  ?'}", flush=True)

stable_list = [x for x in results if x['stable']]
with open(f"{OUTDIR}/scanD_refined.json", 'w') as f:
    json.dump({'window': [7.3, 10.0], 'eigenvalues': stable_list,
               'all_candidates': results}, f, indent=1)
print()
print(f"{len(stable_list)}/{len(results)} stable; "
      f"{sum(x['multiplicity'] for x in stable_list)} with multiplicity; "
      f"old forms: {[round(x['r'], 6) for x in stable_list if x['type'] == 'OLD']}")
print("Saved scanD_refined.json")
