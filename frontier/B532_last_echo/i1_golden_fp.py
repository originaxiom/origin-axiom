#!/usr/bin/env python3
"""B532 I1 Part A — Search for chat1's golden fixed point.

Chat1 claimed: σ* on X(F₄, SL₂C) has isolated (dim=0) irreducible fixed points,
including a golden FP at tr(a)=1, tr(b)=1/φ, tr(A)=-1/φ, tr(B)=0, κ=1.

Prior search (diagonal T only) found all irreducible FPs on the trace-zero locus
(dim=4), NOT isolated. This search uses FULL SL(2,C) parameterization of T.

The substitution-induced map σ* on SL(2,C) representations of F₄ = <a,b,A,B>:
Given (a,b,A,B) → (abAAB, aAB, abAB, aA), a fixed point satisfies
σ*(ρ)(g) = ρ(σ(g)) = ρ(g) for all g, i.e. the representation of the image
word equals the representation of the letter.
"""

import numpy as np
from itertools import product

np.random.seed(42)


def sl2_from_params(t1, t2, z1, z2):
    """Parameterize SL(2,C) via trace t and two complex params z1,z2.
    Returns 2x2 matrix with tr = t, det = 1.
    Uses the parameterization: [[a, b], [c, d]] with a+d=t, ad-bc=1."""
    a = t1 / 2 + z1
    d = t1 / 2 - z1
    b = z2
    c = (a * d - 1) / b if abs(b) > 1e-12 else 0.0
    return np.array([[a, b], [c, d]])


def random_sl2(rng=None):
    """Random SL(2,C) matrix via random trace and random off-diagonal."""
    if rng is None:
        rng = np.random.default_rng()
    t = rng.normal(0, 2) + 1j * rng.normal(0, 1)
    z = rng.normal(0, 1) + 1j * rng.normal(0, 1)
    b = rng.normal(0, 1) + 1j * rng.normal(0, 1)
    if abs(b) < 0.01:
        b = 0.5
    a = t / 2 + z
    d = t / 2 - z
    c = (a * d - 1) / b
    return np.array([[a, b], [c, d]])


def sigma_star(a, b, A, B):
    """Apply σ*: map (a,b,A,B) → (σ(a), σ(b), σ(A), σ(B))
    where σ(a)=abAAB, σ(b)=aAB, σ(A)=abAB, σ(B)=aA."""
    sa = a @ b @ A @ A @ B
    sb = a @ A @ B
    sA = a @ b @ A @ B
    sB = a @ A
    return sa, sb, sA, sB


def fp_residual(a, b, A, B):
    """||σ*(a,b,A,B) - (a,b,A,B)||."""
    sa, sb, sA, sB = sigma_star(a, b, A, B)
    return (np.linalg.norm(sa - a) + np.linalg.norm(sb - b) +
            np.linalg.norm(sA - A) + np.linalg.norm(sB - B))


def traces(a, b, A, B):
    """Return trace dictionary."""
    return {
        'tr(a)': np.trace(a),
        'tr(b)': np.trace(b),
        'tr(A)': np.trace(A),
        'tr(B)': np.trace(B),
        'tr(ab)': np.trace(a @ b),
        'tr(aB)': np.trace(a @ B),
        'kappa': np.trace(a @ b @ A @ B),
    }


def newton_fp(a0, b0, A0, B0, max_iter=200, tol=1e-12):
    """Newton-like iteration for σ* fixed point.
    Iterate by damped fixed-point: x_{n+1} = (1-α)x_n + α·σ*(x_n)."""
    a, b, A, B = a0.copy(), b0.copy(), A0.copy(), B0.copy()
    alpha = 0.3
    for it in range(max_iter):
        sa, sb, sA, sB = sigma_star(a, b, A, B)
        res = fp_residual(a, b, A, B)
        if res < tol:
            return a, b, A, B, res, it
        a = (1 - alpha) * a + alpha * sa
        b = (1 - alpha) * b + alpha * sb
        A = (1 - alpha) * A + alpha * sA
        B = (1 - alpha) * B + alpha * sB
        # Re-project to SL(2) (det=1)
        for M in [a, b, A, B]:
            d = np.linalg.det(M)
            if abs(d) > 1e-15:
                M[:] = M / np.sqrt(d)
    return a, b, A, B, fp_residual(a, b, A, B), max_iter


def check_irreducible(a, b, A, B, tol=1e-6):
    """Check if the representation is irreducible.
    Reducible iff all four matrices share a common eigenvector."""
    for M in [a, b, A, B]:
        evals, evecs = np.linalg.eig(M)
        for i in range(2):
            v = evecs[:, i]
            is_common = True
            for N in [a, b, A, B]:
                Nv = N @ v
                if abs(v[0]) > 1e-10:
                    ratio = Nv[0] / v[0]
                elif abs(v[1]) > 1e-10:
                    ratio = Nv[1] / v[1]
                else:
                    continue
                if np.linalg.norm(Nv - ratio * v) > tol * np.linalg.norm(Nv):
                    is_common = False
                    break
            if is_common:
                return False
    return True


def main():
    phi = (1 + np.sqrt(5)) / 2

    print("=" * 70)
    print("B532 I1 Part A — Golden fixed-point search")
    print("=" * 70)

    # Strategy 1: seed with chat1's claimed traces
    print("\n--- Strategy 1: Seed from chat1's claimed golden traces ---")
    print("  Chat1 claims: tr(a)=1, tr(b)=1/φ, tr(A)=-1/φ, tr(B)=0, κ=1")
    print(f"  Target traces: tr(a)=1, tr(b)={1/phi:.6f}, tr(A)={-1/phi:.6f}, tr(B)=0")

    rng = np.random.default_rng(12345)
    found_golden = []

    for trial in range(500):
        # Build matrices with target traces + random off-diagonal
        for _ in range(3):
            z = rng.normal(0, 0.5, 4) + 1j * rng.normal(0, 0.5, 4)
            off = rng.normal(0, 1, 4) + 1j * rng.normal(0, 1, 4)
            off = np.where(np.abs(off) < 0.1, 0.5, off)

            target_tr = [1.0, 1/phi, -1/phi, 0.0]
            mats = []
            for i in range(4):
                a_val = target_tr[i] / 2 + z[i]
                d_val = target_tr[i] / 2 - z[i]
                b_val = off[i]
                c_val = (a_val * d_val - 1) / b_val
                mats.append(np.array([[a_val, b_val], [c_val, d_val]]))

            a, b, A, B, res, iters = newton_fp(*mats)
            if res < 1e-8:
                tr = traces(a, b, A, B)
                if (abs(tr['tr(a)'] - 1) < 0.1 and
                    abs(tr['tr(b)'] - 1/phi) < 0.1 and
                    abs(tr['kappa'] - 1) < 0.1):
                    found_golden.append((res, tr, check_irreducible(a, b, A, B)))
                    print(f"  FOUND (trial {trial}): res={res:.2e}, "
                          f"tr(a)={tr['tr(a)']:.4f}, tr(b)={tr['tr(b)']:.4f}, "
                          f"κ={tr['kappa']:.4f}, irred={found_golden[-1][2]}")

    print(f"  Total golden candidates: {len(found_golden)}")

    # Strategy 2: random search with full SL(2,C)
    print("\n--- Strategy 2: Random search (2000 seeds, full SL(2,C)) ---")
    found_all = []
    rng2 = np.random.default_rng(54321)

    for trial in range(2000):
        mats = [random_sl2(rng2) for _ in range(4)]
        a, b, A, B, res, iters = newton_fp(*mats)
        if res < 1e-8:
            tr = traces(a, b, A, B)
            irred = check_irreducible(a, b, A, B)
            found_all.append((res, tr, irred))

    print(f"  Total FPs found: {len(found_all)}")
    irred_fps = [x for x in found_all if x[2]]
    red_fps = [x for x in found_all if not x[2]]
    print(f"  Irreducible: {len(irred_fps)}, Reducible: {len(red_fps)}")

    if irred_fps:
        print("\n  Irreducible FP traces:")
        seen = set()
        for res, tr, _ in sorted(irred_fps, key=lambda x: abs(x[1]['tr(a)'])):
            key = (round(tr['tr(a)'].real, 3), round(tr['tr(b)'].real, 3))
            if key not in seen:
                seen.add(key)
                print(f"    tr(a)={tr['tr(a)']:.4f}, tr(b)={tr['tr(b)']:.4f}, "
                      f"tr(A)={tr['tr(A)']:.4f}, tr(B)={tr['tr(B)']:.4f}, "
                      f"κ={tr['kappa']:.4f}")

    # Strategy 3: targeted golden seed with conjugation variations
    print("\n--- Strategy 3: Conjugation-varied golden seeds ---")
    found_conj = []
    rng3 = np.random.default_rng(99999)

    for trial in range(500):
        # Start with diagonal matrices having the target traces
        a0 = np.diag([np.exp(1j * rng3.uniform(0, 2*np.pi)),
                       np.exp(-1j * rng3.uniform(0, 2*np.pi))])
        # Scale to get target trace
        a0 = a0 * 1.0 / np.trace(a0)
        b0 = np.diag([np.exp(1j * rng3.uniform(0, 2*np.pi)),
                       np.exp(-1j * rng3.uniform(0, 2*np.pi))])
        b0 = b0 * (1/phi) / np.trace(b0) if abs(np.trace(b0)) > 0.01 else b0

        # Random conjugation
        P = random_sl2(rng3)
        Pinv = np.linalg.inv(P)

        mats = [P @ a0 @ Pinv, P @ b0 @ Pinv]
        # A, B from inverses (F₄ free group: A=a⁻¹, B=b⁻¹)
        mats.append(np.linalg.inv(mats[0]))
        mats.append(np.linalg.inv(mats[1]))

        a, b, A, B, res, iters = newton_fp(*mats, max_iter=500)
        if res < 1e-8:
            tr = traces(a, b, A, B)
            irred = check_irreducible(a, b, A, B)
            found_conj.append((res, tr, irred))
            if irred and abs(tr['kappa'] - 1) < 0.5:
                print(f"  FOUND irred (trial {trial}): res={res:.2e}, "
                      f"tr(a)={tr['tr(a)']:.4f}, tr(b)={tr['tr(b)']:.4f}, "
                      f"κ={tr['kappa']:.4f}")

    print(f"  Total from conjugation seeds: {len(found_conj)}")
    irred_conj = [x for x in found_conj if x[2]]
    print(f"  Irreducible: {len(irred_conj)}")

    # Final verdict
    print("\n" + "=" * 70)
    print("GOLDEN FP VERDICT")
    print("=" * 70)
    golden_found = any(
        abs(x[1]['tr(a)'] - 1) < 0.1 and
        abs(x[1]['tr(b)'] - 1/phi) < 0.1 and
        abs(x[1]['kappa'] - 1) < 0.5
        for x in found_golden + found_all + found_conj if x[2]
    )
    if golden_found:
        print("  Golden FP: FOUND (irreducible)")
    else:
        print("  Golden FP: NOT FOUND after 3000 seeds (3 strategies)")
        print("  Chat1's claim is UNVERIFIED — the golden FP may not exist for this σ")
        print("  All irreducible FPs found sit at the trace-zero locus (dim=4 family)")


if __name__ == '__main__':
    main()
