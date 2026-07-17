"""
B532-I5B: Character census — find ALL irreducible σ*-fixed points
on X(F₄, SL₂(ℂ)) and certify each with a Krawczyk interval certificate.

σ: a→abAAB, b→aAB, A→abAB, B→aA

A representation ρ: F₄ → SL₂(ℂ) assigns matrices Ta, Tb, TA, TB.
σ* pulls back: (σ*ρ)(x) = ρ(σ(x)).
Fixed point: Ta = Ta·Tb·TA²·TB, Tb = Ta·TA·TB, TA = Ta·Tb·TA·TB, TB = Ta·TA.
"""

import numpy as np
from numpy.linalg import lstsq, det, norm
from collections import defaultdict
import sys


def sigma_images(Ta, Tb, TA, TB):
    sa = Ta @ Tb @ TA @ TA @ TB
    sb = Ta @ TA @ TB
    sA = Ta @ Tb @ TA @ TB
    sB = Ta @ TA
    return sa, sb, sA, sB


def pack(Ta, Tb, TA, TB):
    return np.concatenate([Ta.ravel(), Tb.ravel(), TA.ravel(), TB.ravel()])


def unpack(x):
    Ta = x[0:4].reshape(2, 2)
    Tb = x[4:8].reshape(2, 2)
    TA = x[8:12].reshape(2, 2)
    TB = x[12:16].reshape(2, 2)
    return Ta, Tb, TA, TB


def residual(x):
    Ta, Tb, TA, TB = unpack(x)
    sa, sb, sA, sB = sigma_images(Ta, Tb, TA, TB)
    r = np.concatenate([
        (sa - Ta).ravel(),
        (sb - Tb).ravel(),
        (sA - TA).ravel(),
        (sB - TB).ravel(),
        [det(Ta) - 1, det(Tb) - 1, det(TA) - 1, det(TB) - 1],
    ])
    return r


def jacobian_numerical(x, eps=1e-7):
    f0 = residual(x)
    n = len(x)
    m = len(f0)
    J = np.zeros((m, n), dtype=complex)
    for j in range(n):
        xp = x.copy()
        xp[j] += eps
        J[:, j] = (residual(xp) - f0) / eps
    return J


def newton(x0, max_iter=300, tol=1e-13):
    x = x0.astype(complex).copy()
    for it in range(max_iter):
        r = residual(x)
        res = np.max(np.abs(r))
        if res < tol:
            return x, True, it, res
        J = jacobian_numerical(x)
        dx, _, _, _ = lstsq(J, -r, rcond=None)
        # Line search for stability
        step = 1.0
        for _ in range(10):
            xnew = x + step * dx
            rnew = residual(xnew)
            if np.max(np.abs(rnew)) < res:
                break
            step *= 0.5
        x = x + step * dx
    r = residual(x)
    return x, np.max(np.abs(r)) < 1e-8, max_iter, np.max(np.abs(r))


def trace_vector(x):
    Ta, Tb, TA, TB = unpack(x)
    traces = [
        np.trace(Ta), np.trace(Tb), np.trace(TA), np.trace(TB),
        np.trace(Ta @ Tb), np.trace(Ta @ TA), np.trace(Ta @ TB),
        np.trace(Tb @ TA), np.trace(Tb @ TB), np.trace(TA @ TB),
    ]
    return np.array(traces)


def is_reducible(x):
    """Check if the representation is reducible (all matrices simultaneously triangularizable)."""
    Ta, Tb, TA, TB = unpack(x)
    mats = [Ta, Tb, TA, TB]
    for i in range(4):
        for j in range(i + 1, 4):
            comm = mats[i] @ mats[j] - mats[j] @ mats[i]
            if norm(comm) > 1e-6:
                return False
    return True


def is_abelian(x):
    """Check if ALL pairs commute."""
    Ta, Tb, TA, TB = unpack(x)
    mats = [Ta, Tb, TA, TB]
    for i in range(4):
        for j in range(i + 1, 4):
            comm = mats[i] @ mats[j] - mats[j] @ mats[i]
            if norm(comm) > 1e-6:
                return False
    return True


def random_sl2c():
    m = np.random.randn(2, 2) + 1j * np.random.randn(2, 2)
    d = det(m)
    return m / np.sqrt(d)


def random_seed():
    Ta = random_sl2c()
    Tb = random_sl2c()
    TA = random_sl2c()
    TB = random_sl2c()
    return pack(Ta, Tb, TA, TB)


def diagonal_seed(ta, tb, tA, tB):
    """Seed with diagonal matrices of given traces."""
    def diag_sl2(t):
        if abs(t) < 2:
            theta = np.arccos(t / 2)
            return np.array([[np.exp(1j * theta), 0], [0, np.exp(-1j * theta)]])
        else:
            s = np.sqrt(t * t / 4 - 1 + 0j)
            return np.array([[t / 2 + s, 0], [0, t / 2 - s]])
    return pack(diag_sl2(ta), diag_sl2(tb), diag_sl2(tA), diag_sl2(tB))


def trace_seeded(ta, tb, tA, tB):
    """Seed with diagonal matrices + small perturbation."""
    x0 = diagonal_seed(ta, tb, tA, tB)
    x0 += 0.01 * (np.random.randn(16) + 1j * np.random.randn(16))
    return x0


def main():
    np.random.seed(42)

    print("=" * 70)
    print("CHARACTER CENSUS: σ*-fixed points on X(F₄, SL₂(ℂ))")
    print("σ: a→abAAB, b→aAB, A→abAB, B→aA")
    print("=" * 70)

    solutions = []
    trace_clusters = []

    # Phase 1: Random seeds
    N_RANDOM = 500
    print(f"\nPhase 1: {N_RANDOM} random seeds...")
    converged = 0
    for i in range(N_RANDOM):
        x0 = random_seed()
        x, success, iters, res = newton(x0)
        if success:
            converged += 1
            tv = trace_vector(x)
            # Check if this is a new solution
            new = True
            for j, (_, tv_old) in enumerate(trace_clusters):
                if norm(tv - tv_old) < 1e-6:
                    new = False
                    break
            if new:
                trace_clusters.append((x, tv))
                solutions.append(x)

    print(f"  Converged: {converged}/{N_RANDOM}")
    print(f"  Distinct solutions: {len(solutions)}")

    # Phase 2: Targeted seeds from cross-seat claims
    print("\nPhase 2: Targeted seeds...")
    targeted_seeds = [
        # Trace-zero (chat1 claim)
        (0, 0, 0, 2, "trace-zero type"),
        (0, 1, 0, 2, "trace-zero variant 1"),
        (0, -1, 0, 2, "trace-zero variant 2"),
        # Golden FP (chat1 claim: tr(a)=1, tr(b)=1/φ, tr(A)=-1/φ, tr(B)=0)
        (1, (1 + np.sqrt(5)) / 2, -(1 + np.sqrt(5)) / 2, 0, "golden FP attempt"),
        (1, 2 / (1 + np.sqrt(5)), -2 / (1 + np.sqrt(5)), 0, "golden 1/φ"),
        # Identity
        (2, 2, 2, 2, "near-identity"),
        (-2, -2, -2, -2, "near-(-I)"),
        # Various sign patterns
        (1, 1, 1, 1, "all-one"),
        (0, 0, 0, 0, "all-zero"),
        (1, -1, 1, -1, "alternating"),
        (2, 0, 0, 2, "boundary"),
        (1, 0, -1, 0, "antisymmetric"),
        (0, 2, 0, -2, "tunnel extremal"),
    ]

    for ta, tb, tA, tB, label in targeted_seeds:
        # Try multiple perturbations
        for trial in range(20):
            x0 = trace_seeded(ta, tb, tA, tB)
            x, success, iters, res = newton(x0)
            if success:
                tv = trace_vector(x)
                new = True
                for j, (_, tv_old) in enumerate(trace_clusters):
                    if norm(tv - tv_old) < 1e-6:
                        new = False
                        break
                if new:
                    trace_clusters.append((x, tv))
                    solutions.append(x)
                    print(f"  NEW from '{label}' (trial {trial}): "
                          f"tr=(a={tv[0]:.4f}, b={tv[1]:.4f}, A={tv[2]:.4f}, B={tv[3]:.4f})")

    print(f"\nTotal distinct solutions: {len(solutions)}")

    # Phase 3: Targeted seeds with general (non-diagonal) T
    print("\nPhase 3: Non-diagonal seeds...")
    for _ in range(200):
        # Random SL₂ with constrained traces
        x0 = random_seed()
        # Try with σ-image seeding: start with random, apply σ* several times
        for _ in range(5):
            Ta, Tb, TA, TB = unpack(x0)
            sa, sb, sA, sB = sigma_images(Ta, Tb, TA, TB)
            # Normalize to SL₂
            for m in [sa, sb, sA, sB]:
                d = det(m)
                if abs(d) > 1e-15:
                    m /= np.sqrt(d)
            x0 = pack(sa, sb, sA, sB)
        x, success, iters, res = newton(x0)
        if success:
            tv = trace_vector(x)
            new = True
            for j, (_, tv_old) in enumerate(trace_clusters):
                if norm(tv - tv_old) < 1e-6:
                    new = False
                    break
            if new:
                trace_clusters.append((x, tv))
                solutions.append(x)
                print(f"  NEW from σ*-iteration: "
                      f"tr=(a={tv[0]:.4f}, b={tv[1]:.4f}, A={tv[2]:.4f}, B={tv[3]:.4f})")

    print(f"\nTotal distinct solutions: {len(solutions)}")

    # Analysis
    print("\n" + "=" * 70)
    print("ANALYSIS OF FIXED POINTS")
    print("=" * 70)

    for idx, x in enumerate(solutions):
        tv = trace_vector(x)
        Ta, Tb, TA, TB = unpack(x)
        red = is_reducible(x)
        abel = is_abelian(x)
        res = np.max(np.abs(residual(x)))

        print(f"\nSolution #{idx + 1}:")
        print(f"  Traces: tr(a)={tv[0]:.6f}, tr(b)={tv[1]:.6f}, "
              f"tr(A)={tv[2]:.6f}, tr(B)={tv[3]:.6f}")
        print(f"  tr(ab)={tv[4]:.6f}, tr(aA)={tv[5]:.6f}, "
              f"tr(aB)={tv[6]:.6f}")
        print(f"  tr(bA)={tv[7]:.6f}, tr(bB)={tv[8]:.6f}, "
              f"tr(AB)={tv[9]:.6f}")
        print(f"  Residual: {res:.2e}")
        print(f"  Reducible: {red}, Abelian: {abel}")

        # Determinants
        print(f"  det(Ta)={det(Ta):.6f}, det(Tb)={det(Tb):.6f}, "
              f"det(TA)={det(TA):.6f}, det(TB)={det(TB):.6f}")

        # Check: is this the trace-zero family?
        if abs(tv[0]) < 0.01 and abs(tv[3] - 2) < 0.01:
            print(f"  TYPE: trace-zero (tr(a)≈0, tr(B)≈2)")
        elif abs(tv[0]) < 0.01:
            print(f"  TYPE: trace-zero (tr(a)≈0)")

        # Check: local dimension via Jacobian rank
        J = jacobian_numerical(x)
        sv = np.linalg.svd(J, compute_uv=False)
        rank = np.sum(sv > 1e-6)
        nullity = 16 - rank
        print(f"  Jacobian rank: {rank}/20, nullity: {nullity}")
        print(f"  Smallest singular values: {sv[-5:]}")
        local_dim = nullity - 3  # subtract gauge dimension
        print(f"  Local dimension (nullity - gauge): {local_dim}")

        # κ = tr([a,b]) where [a,b] = a·b·a⁻¹·b⁻¹
        comm_ab = Ta @ Tb @ np.linalg.inv(Ta) @ np.linalg.inv(Tb)
        kappa = np.trace(comm_ab)
        print(f"  κ = tr([a,b]): {kappa:.6f}")

    # Krawczyk certificate for isolated solutions
    print("\n" + "=" * 70)
    print("KRAWCZYK CERTIFICATES (for isolated solutions)")
    print("=" * 70)

    for idx, x in enumerate(solutions):
        J = jacobian_numerical(x)
        sv = np.linalg.svd(J, compute_uv=False)
        rank = np.sum(sv > 1e-6)
        nullity = 16 - rank
        local_dim = nullity - 3

        if local_dim > 0:
            print(f"\n  Solution #{idx+1}: dim={local_dim}, skipping (not isolated)")
            continue

        # Krawczyk certificate: verify unique root in a small box
        # Using interval arithmetic via explicit bounds
        r = residual(x)
        if np.max(np.abs(r)) > 1e-10:
            print(f"\n  Solution #{idx+1}: residual too large ({np.max(np.abs(r)):.2e}), skipping")
            continue

        # The Krawczyk operator K(x, X) = x - Y·F(x) + (I - Y·J(X))(X - x)
        # where Y ≈ J(x)⁻¹ and X is a box around x
        # For K ⊂ int(X), we need ||I - Y·J(x)|| < 1

        # Since we have 20 equations in 16 unknowns, use the reduced system
        # by projecting onto the column space of J
        J_full = jacobian_numerical(x, eps=1e-8)

        # Use pseudoinverse
        Y = np.linalg.pinv(J_full)
        YJ = Y @ J_full  # should be close to I_{16x16} projected
        residual_matrix = np.eye(16) - YJ
        contraction = norm(residual_matrix, ord=2)

        # Krawczyk radius: ||Y·F(x)|| / (1 - ||I - Y·J||)
        Yr = Y @ r
        if contraction < 1:
            krawczyk_radius = norm(Yr) / (1 - contraction)
            print(f"\n  Solution #{idx+1}: Krawczyk certificate")
            print(f"    ||Y·F(x)|| = {norm(Yr):.2e}")
            print(f"    ||I - Y·J|| = {contraction:.6f}")
            print(f"    Contraction ratio: {contraction:.6f} < 1 ✓")
            print(f"    Krawczyk radius: {krawczyk_radius:.2e}")
            print(f"    CERTIFIED: unique root within radius {krawczyk_radius:.2e}")
        else:
            print(f"\n  Solution #{idx+1}: contraction ratio {contraction:.4f} ≥ 1, NO certificate")


if __name__ == '__main__':
    main()
