#!/usr/bin/env python3
"""Independent read-only verification of the corrected B632 Cell 2 map.

The source repository is only read. All assertions and output live in the
external audit directory.
"""

from __future__ import annotations

import argparse
import subprocess
import time
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--repo",
        type=Path,
        default=Path("/Users/dri/origin-axiom"),
        help="read-only Origin Axiom checkout to inspect",
    )
    args = parser.parse_args()
    repo = args.repo.resolve()
    source = repo / "frontier/B632_cubic_route/cell2_texture.py"
    if not source.is_file():
        raise SystemExit(f"missing Cell 2 source: {source}")

    commit = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()
    print(f"AUDIT_SOURCE={source}", flush=True)
    print(f"AUDIT_COMMIT={commit}", flush=True)

    ns = {"__name__": "b632_cell2_audit", "__file__": str(source)}
    started = time.time()
    exec(compile(source.read_text(), str(source), "exec"), ns)
    print(f"AUDIT_PREFIX_SECONDS={time.time() - started:.1f}", flush=True)

    K = ns["K"]
    K0 = ns["K0"]
    A27 = ns["A27"]
    B27 = ns["B27"]
    A27i = ns["A27i"]
    B27i = ns["B27i"]
    La = ns["La"]
    Lb = ns["Lb"]
    Lad = ns["Lad"]
    Lbd = ns["Lbd"]
    Z = ns["Z"]
    phis = ns["phis"]
    REL = ns["REL"]
    PREFIX = ns["PREFIX"]
    apply = ns["apply"]
    C3 = ns["C3"]
    klass = ns["klass"]
    cup = ns["cup_covector"]
    nullspace = ns["nullspace"]

    def zero_scalar(x):
        return x.is_zero()

    def zero_vector(v):
        return all(zero_scalar(x) for x in v)

    def zero_class(c):
        return all(zero_scalar(x) for x in c)

    def matvec(M, v):
        return [
            sum(
                (M[i][j] * v[j] for j in range(len(v)) if not v[j].is_zero()),
                K0,
            )
            for i in range(len(M))
        ]

    def add(u, v):
        return [a + b for a, b in zip(u, v)]

    def scale_minus(v):
        return [K0 - x for x in v]

    def letter_value(z, ch):
        za, zb = z[:27], z[27:]
        if ch == "a":
            return za
        if ch == "b":
            return zb
        if ch == "A":
            return scale_minus(apply(A27i, za))
        return scale_minus(apply(B27i, zb))

    # Compare the implementation to the direct Fox-to-bar comparison chain:
    # positive x at p contributes [p|x], inverse x^-1 contributes -[px^-1|x].
    def cup_canonical(z, w):
        total = [K0] * 27
        u_prefix = [K0] * 27
        for i, ch in enumerate(REL):
            u_letter = apply(PREFIX[i], letter_value(z, ch))
            if ch in "ab":
                w_generator = w[:27] if ch == "a" else w[27:]
                w_value = apply(PREFIX[i], w_generator)
                term = C3(u_prefix, w_value)
            else:
                generator = ch.lower()
                u_next = add(u_prefix, u_letter)
                p_next = PREFIX[i + 1] if i + 1 < len(REL) else ns["meye"](27)
                w_generator = w[:27] if generator == "a" else w[27:]
                w_value = apply(p_next, w_generator)
                term = scale_minus(C3(u_next, w_value))
            total = add(total, term)
            u_prefix = add(u_prefix, u_letter)
        return total

    # The three stored representatives must actually be Fox cocycles.
    for T, z in Z.items():
        residual = add(matvec(La, z[:27]), matvec(Lb, z[27:]))
        assert zero_vector(residual), f"V({T}) representative is not a cocycle"
    print("GATE selected_representatives_are_cocycles PASS", flush=True)

    # The reported H^2 functionals must annihilate the full dual Fox image.
    for p, phi in enumerate(phis):
        for name, M in (("La*", Lad), ("Lb*", Lbd)):
            for j in range(27):
                val = sum((phi[i] * M[i][j] for i in range(27)), K0)
                assert val.is_zero(), f"phi[{p}] does not annihilate {name} column {j}"
    print("GATE h2_functionals_annihilate_dual_fox_image PASS", flush=True)

    # The revised implementation must equal the canonical comparison-chain formula.
    all_pairs = [(Ta, Tb) for Ta in (0, 8, 16) for Tb in (0, 8, 16)]
    for Ta, Tb in all_pairs:
        lhs = cup(Z[Ta], Z[Tb])
        rhs = cup_canonical(Z[Ta], Z[Tb])
        assert zero_vector([a - b for a, b in zip(lhs, rhs)]), (Ta, Tb)
    print("GATE canonical_bar_chain_agreement_9_of_9 PASS", flush=True)

    # Exhaustive descent on the chosen H^1 basis: every basis coboundary,
    # in each argument, against every selected cohomology representative.
    descent_checks = 0
    for j in range(27):
        v = [K(1) if i == j else K0 for i in range(27)]
        da = [x - v[i] for i, x in enumerate(apply(A27, v))]
        db = [x - v[i] for i, x in enumerate(apply(B27, v))]
        boundary = da + db
        for T in (0, 8, 16):
            assert zero_class(klass(cup(boundary, Z[T]))), ("left", j, T)
            assert zero_class(klass(cup(Z[T], boundary))), ("right", j, T)
            descent_checks += 2
    print(f"GATE exhaustive_coboundary_descent_{descent_checks}_of_{descent_checks} PASS", flush=True)

    # Alternating map checks, including the previously omitted trivial-block diagonal.
    for T in (0, 8, 16):
        assert zero_class(klass(cup(Z[T], Z[T]))), f"diagonal V({T})"
    pairs = ((0, 8), (0, 16), (8, 16))
    omega = []
    for Ta, Tb in pairs:
        ab = klass(cup(Z[Ta], Z[Tb]))
        ba = klass(cup(Z[Tb], Z[Ta]))
        assert zero_class(tuple(a + b for a, b in zip(ab, ba))), (Ta, Tb)
        omega.append(ab)
    print("GATE alternating_all_diagonals_and_pairs PASS", flush=True)

    # Rank of the 2x3 exact Omega table.
    omega_rows = [[omega[col][row] for col in range(3)] for row in range(2)]
    omega_rank = 3 - len(nullspace(omega_rows))
    assert omega_rank == 2, f"Omega rank {omega_rank}, expected 2"
    print("RESULT omega_rank=2 target_dimension=2 kernel_dimension=1", flush=True)
    print("AUDIT_VERDICT=CORRECTED_CELL2_MAP_PASSES_EXHAUSTIVE_DESCENT", flush=True)


if __name__ == "__main__":
    main()
