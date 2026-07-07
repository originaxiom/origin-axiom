#!/usr/bin/env python3
"""B451 — enumeration v2: union-of-depth survivors + orbit-point bootstrapping.
Stability check = two independent grid densities must agree on all counts."""
import sys
import numpy as np
import resonances as R
from survivor_enum import Tinv, survivors


def enumerate_v2(lam, N, ngrid):
    c = (lam / 2.0) ** 2
    pool = []
    for depth in (5, 6, 7, 8):
        pool += survivors(c, ngrid, 4.0, depth, 40.0)
    print(f"  seed pool {len(pool)} (grid {ngrid}, depths 5-8)")
    all_orbits = {}
    seeds = [np.array(s) for s in pool]
    for n in range(1, N + 1):
        found = {}
        for s in seeds:
            p = R.newton_periodic(s, n, c)
            if p is None:
                continue
            orb = [p.copy()]
            q = R.T(p)
            minper = n
            for k in range(1, n):
                if np.linalg.norm(q - p) < 1e-7:
                    minper = k
                    break
                orb.append(q.copy())
                q = R.T(q)
            if minper != n:
                continue
            key = tuple(np.round(min((tuple(o) for o in orb)), 6))
            if key not in found and key not in all_orbits:
                found[key] = orb
        for key, orb in found.items():
            all_orbits[key] = (n, R.expanding_multiplier(orb), orb)
            seeds.extend(np.array(o) for o in orb)      # bootstrap
        cnt = sum(1 for (nn, _, _) in all_orbits.values() if nn == n)
        print(f"  n={n:2d}: primitive orbits {cnt}")
    return [(n, l) for (n, l, _) in all_orbits.values()]


if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    lam = float(sys.argv[2]) if len(sys.argv) > 2 else 3.0
    results = []
    for ngrid in (100, 150):
        print(f"== grid {ngrid} ==")
        prims = enumerate_v2(lam, N, ngrid)
        counts = {}
        for n, _ in prims:
            counts[n] = counts.get(n, 0) + 1
        coeffs = R.cycle_expansion(prims, N)
        roots = np.roots(coeffs[::-1])
        roots = roots[np.abs(roots) > 1e-9]
        order = np.argsort(np.abs(roots))
        z0 = roots[order[0]]
        gam = float(np.log(np.abs(z0)))
        results.append((counts, gam, [roots[i] for i in order[:5]]))
        print(f"  counts {counts}  gamma = {gam:.4f}")
    stable = results[0][0] == results[1][0]
    print(f"\ncount stability across grids: {'STABLE' if stable else 'UNSTABLE'}")
    print(f"gamma: {results[0][1]:.4f} vs {results[1][1]:.4f}  (banked gate 0.51)")
    if stable:
        print("resonances (grid-150): " + ", ".join(f"{z:.4f} (rate {np.log(abs(z)):.3f})"
                                                    for z in results[1][2]))
