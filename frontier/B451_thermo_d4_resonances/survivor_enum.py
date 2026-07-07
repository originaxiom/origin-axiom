#!/usr/bin/env python3
"""B451 — survivor-seeded orbit enumeration (the horseshoe approximates itself).

Seeds for period-n Newton = surface points whose forward AND backward orbits stay
bounded for `depth` steps (the nonwandering set's finite-depth approximation).
Counts validated across two survivor depths (the exploratory-numerics rule).
"""
import sys
import numpy as np
import resonances as R


def Tinv(p):
    x, y, z = p
    return np.array([y, z, 2 * y * z - x])


def survivors(c, ngrid, box, depth, bound):
    pts = []
    for s in R.surface_seeds(c, ngrid, box):
        p = s.copy(); ok = True
        for _ in range(depth):
            p = R.T(p)
            if np.linalg.norm(p) > bound: ok = False; break
        if not ok: continue
        p = s.copy()
        for _ in range(depth):
            p = Tinv(p)
            if np.linalg.norm(p) > bound: ok = False; break
        if ok: pts.append(s)
    return pts


def enumerate_orbits(lam, N, ngrid=120, depth=7, bound=40.0):
    c = (lam / 2.0) ** 2
    seeds = survivors(c, ngrid, 4.0, depth, bound)
    print(f"lambda={lam}: {len(seeds)} survivor seeds (grid {ngrid}, depth {depth})")
    all_orbits = {}          # key: rounded orbit-min point -> (period, multiplier)
    for n in range(1, N + 1):
        found = {}
        for s in seeds:
            p = R.newton_periodic(np.array(s), n, c)
            if p is None: continue
            # canonical key: lexicographically smallest point on the orbit
            orb = [p.copy()]
            q = R.T(p)
            minper = n
            for k in range(1, n):
                if np.linalg.norm(q - p) < 1e-7: minper = k; break
                orb.append(q.copy()); q = R.T(q)
            if minper != n: continue           # not primitive at this n
            key = tuple(np.round(min((tuple(o) for o in orb)), 6))
            if key not in found:
                found[key] = orb
        for key, orb in found.items():
            if key not in all_orbits:
                lam_p = R.expanding_multiplier(orb)
                all_orbits[key] = (n, lam_p)
        cnt = sum(1 for (nn, _) in all_orbits.values() if nn == n)
        print(f"  n={n:2d}: primitive orbits = {cnt:3d}  (points {cnt*n})")
    return list(all_orbits.values())


def zeta(prims, N):
    coeffs = R.cycle_expansion(prims, N)
    roots = np.roots(coeffs[::-1])
    roots = roots[np.abs(roots) > 1e-9]
    order = np.argsort(np.abs(roots))
    return roots[order]


if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    lam = float(sys.argv[2]) if len(sys.argv) > 2 else 3.0
    for depth in (6, 8):                      # two-depth stability check
        prims = enumerate_orbits(lam, N, depth=depth)
        zs = zeta(prims, N)
        gam = float(np.log(np.abs(zs[0])))
        print(f"depth {depth}: leading zero {zs[0]:.6f} -> gamma = {gam:.4f}; "
              f"next: " + ", ".join(f"{z:.4f}" for z in zs[1:4]))
