#!/usr/bin/env python3
"""B532 I1 Part A — Fixed-point dimension analysis.

Compute the dimension of the σ*-fixed-point variety at known irreducible FPs
by analyzing the Jacobian rank of the fixed-point equations.

The fixed-point system: T·ρ(g)·T⁻¹ = ρ(σ(g)) for g ∈ {a,b,A,B},
with det(ρ(g))=1. This is 4×4 matrix equations (16 real conditions per
generator) + 4 det conditions + 3 gauge conditions (conjugation by T),
in 4×4+2 = 18 real parameters (4 SL(2,C) matrices + 1 T diagonal param).

Expected generic dimension: 18 params - 16 FP conditions - 4 det - 3 gauge
= 18 - 16 - 4 + 3 = 1? No: the FP conditions are NOT all independent because
σ is an automorphism of F₄ — the induced map on the 9-dim character variety
is a 9→9 map, so FP conditions give codim ≤ 9, and dim ≥ 9 - 9 = 0 generically.

But the actual dimension depends on the rank of the Jacobian at the FP.
"""

import numpy as np
from scipy.optimize import least_squares
from scipy.linalg import expm

PHI = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
GENS = ['a', 'b', 'A', 'B']

_E = [np.array([[0, 1], [0, 0]], complex),
      np.array([[0, 0], [1, 0]], complex),
      np.array([[1, 0], [0, -1]], complex)]


def _mat(v):
    return np.array([[v[0], v[1]], [v[2], v[3]]], complex)


def _unpack(x):
    z = x[:len(x) // 2] + 1j * x[len(x) // 2:]
    return np.diag([z[0], 1 / z[0]]), {g: _mat(z[1 + 4 * i:5 + 4 * i]) for i, g in enumerate(GENS)}


def _wm(w, Ms, inv):
    P = np.eye(2, dtype=complex)
    for ch in w:
        P = P @ (Ms[ch] if ch in Ms else inv[ch.lower()])
    return P


def _resid(x):
    T, Ms = _unpack(x)
    Ti = np.linalg.inv(T)
    inv = {g: np.linalg.inv(Ms[g]) for g in GENS}
    r = [T @ Ms[g] @ Ti - _wm(PHI[g], Ms, inv) for g in GENS]
    d = np.array([np.linalg.det(Ms[g]) - 1 for g in GENS])
    flat = np.concatenate([m.ravel() for m in r] + [d])
    return np.concatenate([flat.real, flat.imag])


def find_fp(seed, n_tries=500, irred_only=True):
    """Find a fixed point using random restarts."""
    np.random.seed(seed)
    for _ in range(n_tries):
        s = least_squares(_resid, np.random.randn(34) * 0.9, method='lm', max_nfev=1500)
        if s.cost < 1e-18:
            T, Ms = _unpack(s.x)
            if irred_only:
                C = Ms['a'] @ Ms['b'] @ np.linalg.inv(Ms['a']) @ np.linalg.inv(Ms['b'])
                if abs(np.trace(C) - 2) > 0.3:
                    return s.x, T, Ms
            else:
                return s.x, T, Ms
    return None


def jacobian_rank(x0, eps=1e-7):
    """Compute numerical Jacobian rank of the FP residual at x0."""
    r0 = _resid(x0)
    n = len(x0)
    m = len(r0)
    J = np.zeros((m, n))
    for j in range(n):
        xp = x0.copy()
        xp[j] += eps
        J[:, j] = (_resid(xp) - r0) / eps
    sv = np.linalg.svd(J, compute_uv=False)
    rank = int(np.sum(sv > 1e-6))
    kernel_dim = n - rank
    return rank, kernel_dim, sv


def trace_coords(Ms):
    """Compute trace coordinates at a representation."""
    inv = {g: np.linalg.inv(Ms[g]) for g in GENS}
    coords = {}
    for g in GENS:
        coords[f'tr({g})'] = np.trace(Ms[g])
    coords['tr(ab)'] = np.trace(Ms['a'] @ Ms['b'])
    coords['tr(aB)'] = np.trace(Ms['a'] @ Ms['B'])
    coords['tr(Ab)'] = np.trace(Ms['A'] @ Ms['b'])
    coords['tr(AB)'] = np.trace(Ms['A'] @ Ms['B'])
    C = Ms['a'] @ Ms['b'] @ inv['a'] @ inv['b']
    coords['kappa'] = np.trace(C)
    return coords


def main():
    print("=" * 70)
    print("B532 I1 — Fixed-point dimension analysis")
    print("=" * 70)

    results = []
    for seed in [2, 7, 11, 19, 31, 37, 41, 53, 67, 83]:
        r = find_fp(seed)
        if r is None:
            continue
        x0, T, Ms = r
        rank, kernel_dim, sv = jacobian_rank(x0)
        tc = trace_coords(Ms)

        print(f"\n  Seed {seed}: irreducible FP found")
        print(f"    tr(a)={tc['tr(a)']:.4f}, tr(b)={tc['tr(b)']:.4f}, "
              f"tr(A)={tc['tr(A)']:.4f}, tr(B)={tc['tr(B)']:.4f}")
        print(f"    κ={tc['kappa']:.4f}")
        print(f"    Jacobian: {len(_resid(x0))} equations × {len(x0)} unknowns")
        print(f"    Rank = {rank}, Kernel dim = {kernel_dim}")
        print(f"    Top singular values: {sv[:5]}")
        print(f"    Bottom singular values: {sv[-8:]}")

        # The "geometric" dimension = kernel_dim - gauge_dim
        # Gauge is conjugation by SL(2,C) = 3 complex = 6 real params
        # But T already eats 2 real (1 complex) of gauge, leaving 4 real
        gauge_dim = 4
        geom_dim = max(0, kernel_dim - gauge_dim)
        print(f"    Geometric dimension (kernel - remaining gauge) = {kernel_dim} - {gauge_dim} = {geom_dim}")
        results.append({
            'seed': seed,
            'traces': tc,
            'rank': rank,
            'kernel_dim': kernel_dim,
            'geom_dim': geom_dim,
        })

    # Also search for the golden FP with explicit trace seeding
    print("\n" + "=" * 70)
    print("Golden FP search with trace-seeded initial conditions")
    print("=" * 70)
    phi = (1 + np.sqrt(5)) / 2
    target_traces = {'a': 1.0, 'b': 1/phi, 'A': -1/phi, 'B': 0.0}

    found_golden = False
    for seed in range(100):
        np.random.seed(seed + 1000)
        x0 = np.random.randn(34) * 0.5
        # Set the diagonal entries to approximate target traces
        for i, g in enumerate(GENS):
            half_tr = target_traces[g] / 2
            x0[1 + 4*i] = half_tr + 0.5  # a11 real part
            x0[17 + 1 + 4*i] = 0  # a11 imag part
            x0[4 + 4*i] = half_tr - 0.5  # a22 real part
            x0[17 + 4 + 4*i] = 0  # a22 imag part

        s = least_squares(_resid, x0, method='lm', max_nfev=3000)
        if s.cost < 1e-16:
            T, Ms = _unpack(s.x)
            tc = trace_coords(Ms)
            C = Ms['a'] @ Ms['b'] @ np.linalg.inv(Ms['a']) @ np.linalg.inv(Ms['b'])
            if abs(np.trace(C) - 2) > 0.3:
                if (abs(tc['tr(a)'] - 1) < 0.3 and
                    abs(tc['tr(b)'] - 1/phi) < 0.3):
                    found_golden = True
                    rank, kernel_dim, sv = jacobian_rank(s.x)
                    print(f"\n  GOLDEN FP CANDIDATE (seed {seed}):")
                    print(f"    tr(a)={tc['tr(a)']:.6f}, tr(b)={tc['tr(b)']:.6f}, κ={tc['kappa']:.6f}")
                    print(f"    Rank = {rank}, Kernel dim = {kernel_dim}")

    if not found_golden:
        print("\n  Golden FP NOT FOUND in 100 trace-seeded trials")

    # Verdict
    print("\n" + "=" * 70)
    print("DIMENSION VERDICT")
    print("=" * 70)
    if results:
        geom_dims = [r['geom_dim'] for r in results]
        print(f"  Geometric dimensions at irreducible FPs: {geom_dims}")
        if all(d == geom_dims[0] for d in geom_dims):
            print(f"  UNIFORM dimension = {geom_dims[0]}")
            if geom_dims[0] == 0:
                print("  → ISOLATED (dim=0) — consistent with chat1")
            else:
                print(f"  → {geom_dims[0]}-dimensional family — INCONSISTENT with chat1's dim=0 claim")
        else:
            print(f"  → NON-UNIFORM dimensions — the FP variety has multiple components")
    print(f"  Golden FP: {'FOUND' if found_golden else 'NOT FOUND'}")


if __name__ == '__main__':
    main()
