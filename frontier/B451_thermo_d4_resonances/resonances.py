#!/usr/bin/env python3
"""B451 (thermo D4 / Relation R5) — trace-map transfer-operator Ruelle resonances
via cycle expansion, per the committed prereg.

Conventions (B186, the gate's source): T(x,y,z) = (2xy − z, x, y); invariant
I = x² + y² + z² − 2xyz − 1; the λ-surface is I = (λ/2)²; κ = 2 + λ². The
horseshoe on the surface is DG-proven hyperbolic for λ > 0; B186's banked escape
rate at λ = 3 is γ = 0.51 (ground-truth-validated) — THE GATE: the cycle
expansion's leading zero must reproduce it before any resonance is read.

Machinery: period-n points found by constrained Newton (T^n − id in two
components + the surface equation; third component verified); grammar
completeness = count vs 2^n (full binary shift — the prereg's grammar-as-input,
checked, not assumed); multipliers = expanding eigenvalue of the orbit Jacobian
restricted to the surface tangent plane; 1/ζ(z) = ∏_p (1 − z^{n_p}/|Λ_p|)
expanded to order N; escape rate γ = ln z₀ from the leading (smallest positive
real) zero; subleading zeros = the resonances.
"""
import sys
from collections import defaultdict

import numpy as np
np.seterr(over="ignore", invalid="ignore")

rng = np.random.default_rng(451)


def T(p):
    x, y, z = p
    return np.array([2 * x * y - z, x, y])


def DT(p):
    x, y, z = p
    return np.array([[2 * y, 2 * x, -1.0], [1, 0, 0], [0, 1, 0]])


def Ival(p):
    x, y, z = p
    return x * x + y * y + z * z - 2 * x * y * z - 1


def gradI(p):
    x, y, z = p
    return np.array([2 * x - 2 * y * z, 2 * y - 2 * x * z, 2 * z - 2 * x * y])


def Tn(p, n):
    q = p.copy()
    for _ in range(n):
        q = T(q)
    return q


def newton_periodic(p0, n, c, iters=60):
    """solve (T^n − id)_{0,1} = 0, I − c = 0; verify the third component."""
    p = p0.copy()
    for _ in range(iters):
        q = p.copy()
        J = np.eye(3)
        for _ in range(n):
            J = DT(q) @ J
            q = T(q)
        F = np.array([q[0] - p[0], q[1] - p[1], Ival(p) - c])
        A = np.vstack([(J - np.eye(3))[0], (J - np.eye(3))[1], gradI(p)])
        if not np.all(np.isfinite(F)) or not np.all(np.isfinite(A)):
            return None
        try:
            dp = np.linalg.solve(A, -F)
        except np.linalg.LinAlgError:
            return None
        p = p + dp
        if np.linalg.norm(p) > 1e6:
            return None
        if np.linalg.norm(F) < 1e-12 and np.linalg.norm(dp) < 1e-12:
            break
    q = Tn(p, n)
    if (np.linalg.norm(q - p) < 1e-9 and abs(Ival(p) - c) < 1e-9):
        return p
    return None


def surface_seeds(c, ngrid, box):
    """seed points on I = c: z = xy ± sqrt((xy)² − x² − y² + 1 + c)."""
    seeds = []
    for x in np.linspace(-box, box, ngrid):
        for y in np.linspace(-box, box, ngrid):
            disc = (x * y) ** 2 - x * x - y * y + 1 + c
            if disc >= 0:
                r = np.sqrt(disc)
                seeds.append(np.array([x, y, x * y + r]))
                seeds.append(np.array([x, y, x * y - r]))
    return seeds


def find_period_n_points(n, c, ngrid=28, box=3.5):
    found = {}
    for s in surface_seeds(c, ngrid, box):
        p = newton_periodic(s, n, c)
        if p is None:
            continue
        key = tuple(np.round(p, 7))
        if key not in found:
            # dedupe against near-duplicates
            if any(np.linalg.norm(p - np.array(k)) < 1e-5 for k in found):
                continue
            found[key] = p
    return list(found.values())


def orbits_from_points(points, n):
    """group period-n points into orbits; keep primitive ones (min period == n)."""
    used = set()
    orbits = []
    pts = [np.array(p) for p in points]
    for i, p in enumerate(pts):
        if i in used:
            continue
        orbit = [p]
        q = T(p)
        minper = n
        for k in range(1, n):
            if np.linalg.norm(q - p) < 1e-7:
                minper = k
                break
            orbit.append(q)
            q = T(q)
        for j, r in enumerate(pts):
            if j != i and any(np.linalg.norm(r - o) < 1e-6 for o in orbit):
                used.add(j)
        used.add(i)
        if minper == n:
            orbits.append(orbit)
    return orbits


def expanding_multiplier(orbit):
    p = orbit[0]
    J = np.eye(3)
    q = p.copy()
    for _ in range(len(orbit)):
        J = DT(q) @ J
        q = T(q)
    g = gradI(p)
    g = g / np.linalg.norm(g)
    # orthonormal tangent basis
    a = np.array([1.0, 0, 0]) if abs(g[0]) < 0.9 else np.array([0, 1.0, 0])
    u = a - g * (a @ g)
    u /= np.linalg.norm(u)
    v = np.cross(g, u)
    B = np.column_stack([u, v])
    A2 = B.T @ J @ B
    ev = np.linalg.eigvals(A2)
    return ev[np.argmax(np.abs(ev))]


def cycle_expansion(prims, N):
    """expand prod_p (1 − z^{n_p}/|Λ_p|) to order N; return coefficient array."""
    coeffs = np.zeros(N + 1)
    coeffs[0] = 1.0
    for n_p, lam in prims:
        t = np.zeros(N + 1)
        t[0] = 1.0
        if n_p <= N:
            t[n_p] = -1.0 / abs(lam)
        out = np.zeros(N + 1)
        for i in range(N + 1):
            for j in range(0, N + 1 - i):
                out[i + j] += coeffs[i] * t[j]
        coeffs = out
    return coeffs


def run_surface(lam, N, label):
    c = (lam / 2.0) ** 2
    print(f"\n== {label}: lambda = {lam} (I = {c}, kappa = {2 + lam*lam}) ==")
    prims = []
    complete = True
    for n in range(1, N + 1):
        pts = find_period_n_points(n, c)
        expect = 2 ** n
        orbs = orbits_from_points(pts, n)
        status = "COMPLETE" if len(pts) == expect else f"{len(pts)}/{expect}"
        if len(pts) != expect:
            complete = False
        for o in orbs:
            lam_p = expanding_multiplier(o)
            prims.append((n, lam_p))
        print(f"  n={n:2d}: fixed points {len(pts):4d} (expect {expect:4d}) "
              f"[{status}]  primitive orbits {len(orbs)}")
    coeffs = cycle_expansion(prims, N)
    roots = np.roots(coeffs[::-1])
    roots = roots[np.abs(roots) > 1e-9]
    # leading zero: smallest |z| (within the convergence disc)
    order = np.argsort(np.abs(roots))
    z0 = roots[order[0]]
    gamma = float(np.log(np.abs(z0)))
    print(f"  leading zero z0 = {z0:.6f}  ->  escape rate gamma = {gamma:.4f}")
    print(f"  next zeros (resonances): "
          + ", ".join(f"{roots[i]:.4f} (rate {np.log(np.abs(roots[i])):.3f})"
                      for i in order[1:5]))
    return gamma, roots[order], complete


if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    # THE GATE: lambda = 3 must reproduce B186's banked gamma = 0.51
    gamma, zeros, complete = run_surface(3.0, N, "GATE surface (B186 ground truth)")
    gate = abs(gamma - 0.51) < 0.03
    print(f"\nGATE (gamma = 0.51 +- 0.03, B186): {'PASS' if gate else 'FAIL'} "
          f"(got {gamma:.4f}; grammar {'complete' if complete else 'INCOMPLETE'})")
    if not gate:
        print("NO RESONANCE IS READ — gate failed.")
        sys.exit(1)
    # the kappa-scan (prereg: kappa in {2.5, 3, 4} -> lambda = sqrt(kappa-2))
    for kappa in (2.5, 3.0, 4.0):
        run_surface(float(np.sqrt(kappa - 2)), N, f"kappa = {kappa}")
