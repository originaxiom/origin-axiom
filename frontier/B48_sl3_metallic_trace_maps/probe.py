"""B48 -- Metallic SL(3) trace-map certificates.

This is a governed intake of the SL(3) metallic trace-map side work.  It checks
the reproducible algebra only:

* the trace-map recurrence for phi_m(a)=a^m b, phi_m(b)=a;
* direct exact SL(3,Z) matrix sanity checks;
* degree-growth / entropy recurrences;
* fixed-line Jacobian block factorizations;
* integer splitting classification over an audit rectangle;
* compact SU(3) diagonal-slice representatives.

No physical dictionary, selector theorem, or Origin-core claim is promoted.
"""

from __future__ import annotations

import argparse
import math
import time
from collections import defaultdict
from dataclasses import dataclass

import numpy as np
import sympy as sp


@dataclass(frozen=True)
class CheckResult:
    name: str
    ok: bool
    detail: str


def result(name: str, ok: bool, detail: str = "") -> CheckResult:
    return CheckResult(name=name, ok=ok, detail=detail)


def print_result(item: CheckResult) -> None:
    status = "OK" if item.ok else "FAIL"
    suffix = f" -- {item.detail}" if item.detail else ""
    print(f"{item.name}: {status}{suffix}")


def metallic_a(m: int, n: int) -> int:
    """Metallic sequence A_{n+1}=m A_n + A_{n-1}, A_-1=0, A_0=1."""
    if n == -1:
        return 0
    if n == 0:
        return 1
    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, m * current + previous
    return current


def trace_map_coords_from_recurrence(coords: tuple[sp.Expr, ...], m: int) -> tuple[sp.Expr, ...]:
    """Return the eight trace coordinates after a -> a^m b, b -> a.

    Coordinate convention:
    x1=tr(A), x2=tr(B), x3=tr(AB), x4=tr(A^-1),
    x5=tr(B^-1), x6=tr(A^-1 B), x7=tr(A B^-1), x8=tr(A^-1 B^-1).
    """
    x1, x2, x3, x4, x5, x6, x7, x8 = coords
    tau = {-1: x6, 0: x2, 1: x3}
    sigma = {-1: x7, 0: x5, 1: x8}

    for k in range(2, m + 2):
        tau[k] = sp.expand(x1 * tau[k - 1] - x4 * tau[k - 2] + tau[k - 3])
        sigma[k] = sp.expand(x4 * sigma[k - 1] - x1 * sigma[k - 2] + sigma[k - 3])

    return (
        tau[m],
        x1,
        tau[m + 1],
        sigma[m],
        x4,
        sigma[m - 1],
        tau[m - 1],
        sigma[m + 1],
    )


def check_trace_map_formula() -> CheckResult:
    x1, x2, x3, x4, x5, x6, x7, x8 = sp.symbols("x1 x2 x3 x4 x5 x6 x7 x8")
    observed = trace_map_coords_from_recurrence((x1, x2, x3, x4, x5, x6, x7, x8), 1)
    expected = (
        x3,
        x1,
        x1 * x3 - x4 * x2 + x6,
        x8,
        x4,
        x5,
        x2,
        x4 * x8 - x1 * x5 + x7,
    )
    ok = all(sp.expand(a - b) == 0 for a, b in zip(observed, expected))
    return result("TRACE MAP FORMULA", ok, "m=1 formula and Cayley-Hamilton recurrences")


def coords_from_matrices(a: sp.Matrix, b: sp.Matrix) -> tuple[sp.Expr, ...]:
    a_inv, b_inv = a.inv(), b.inv()
    tr = sp.trace
    return (
        tr(a),
        tr(b),
        tr(a * b),
        tr(a_inv),
        tr(b_inv),
        tr(a_inv * b),
        tr(a * b_inv),
        tr(a_inv * b_inv),
    )


def check_direct_matrix_trace(max_m: int = 4) -> CheckResult:
    examples = [
        (
            sp.Matrix([[1, 1, 0], [0, 1, 1], [0, 0, 1]]),
            sp.Matrix([[1, 0, 0], [1, 1, 0], [0, 1, 1]]),
        ),
        (
            sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]]),
            sp.Matrix([[1, 1, 0], [0, 1, 0], [0, 0, 1]]),
        ),
        (
            sp.Matrix([[1, 2, 1], [0, 1, 1], [0, 0, 1]]),
            sp.Matrix([[1, 0, 0], [1, 1, 0], [1, 1, 1]]),
        ),
    ]

    for index, (a, b) in enumerate(examples, start=1):
        if a.det() != 1 or b.det() != 1:
            return result("DIRECT MATRIX TRACE", False, f"example {index} determinant is not 1")
        coords = coords_from_matrices(a, b)
        for m in range(1, max_m + 1):
            predicted = trace_map_coords_from_recurrence(coords, m)
            direct = coords_from_matrices((a**m) * b, a)
            if any(sp.simplify(p - d) != 0 for p, d in zip(predicted, direct)):
                return result("DIRECT MATRIX TRACE", False, f"example {index}, m={m}")

    return result("DIRECT MATRIX TRACE", True, f"{len(examples)} SL(3,Z) examples, m<= {max_m}")


def check_entropy(max_m: int = 25, max_n: int = 30) -> CheckResult:
    """Check the exact degree recurrence behind h_alg(T_m)=log(lambda_m)."""
    for m in range(1, max_m + 1):
        for n in range(2, max_n + 1):
            a = metallic_a(m, n)
            b = metallic_a(m, n - 1)
            next_a = metallic_a(m, n + 1)

            if m * a + b != next_a:
                return result("ENTROPY DEGREE", False, f"next recurrence mismatch m={m}, n={n}")
            if (m + 1) * a + b != next_a + a:
                return result("ENTROPY DEGREE", False, f"tau m+1 mismatch m={m}, n={n}")

            tau_m_minus_1 = (m - 1) * a + b if m >= 2 else b
            if tau_m_minus_1 != next_a - a:
                return result("ENTROPY DEGREE", False, f"tau m-1 mismatch m={m}, n={n}")

            for k in range(2, max(3, m + 2)):
                first = a + ((k - 1) * a + b)
                second = a + (((k - 2) * a + b) if k - 2 >= 1 else b)
                third = ((k - 3) * a + b) if k - 3 >= 1 else (a - b if k == 2 else b)
                if not (first > second and first > third):
                    return result("ENTROPY DEGREE", False, f"dominance fail m={m}, n={n}, k={k}")

    return result("ENTROPY DEGREE", True, f"m<= {max_m}, n<= {max_n}")


def check_c3_jacobian(max_m: int = 50) -> CheckResult:
    t = sp.symbols("t")
    for m in range(1, max_m + 1):
        sym_block = sp.Matrix(
            [
                [0, 1 - m * m, (m * m + m) // 2, (m * m - m) // 2],
                [1, 0, 0, 0],
                [0, -m * m - 2 * m, (m * m + 3 * m) // 2 + 1, (m * m + m) // 2],
                [0, -m * m + 2 * m, (m * m - m) // 2, (m * m - 3 * m) // 2 + 1],
            ]
        )
        anti_block = sp.Matrix(
            [
                [m**3 - m, 1 - m * m, (m * m + m) // 2, (m * m - m) // 2],
                [1, 0, 0, 0],
                [m**3 + 3 * m * m + 2 * m, -m * m - 2 * m, (m * m + 3 * m) // 2 + 1, (m * m + m) // 2],
                [-m**3 + 3 * m * m - 2 * m, m * m - 2 * m, -(m * m - m) // 2, -(m * m - 3 * m) // 2 - 1],
            ]
        )
        expected_sym = sp.factor((t - 1) * (t + 1) * (t**2 - (m * m + 2) * t + 1))
        expected_anti = sp.factor((t**2 + m * t - 1) * (t**2 - (m**3 + 3 * m) * t - 1))
        if sp.expand(sym_block.charpoly(t).as_expr() - expected_sym) != 0:
            return result("C3 JACOBIAN BLOCKS", False, f"symmetric block mismatch m={m}")
        if sp.expand(anti_block.charpoly(t).as_expr() - expected_anti) != 0:
            return result("C3 JACOBIAN BLOCKS", False, f"antisymmetric block mismatch m={m}")

    return result("C3 JACOBIAN BLOCKS", True, f"checked m<= {max_m}")


def check_c1_jacobian(max_r: int = 20) -> CheckResult:
    t = sp.symbols("t")
    for r in range(max_r + 1):
        blocks = [
            (4 * r, sp.Matrix([[4 * r, 1, 0, 0], [1, 0, 0, 0], [4 * r, 0, 1, 0], [-4 * r, 0, 0, -1]])),
            (4 * r + 1, sp.Matrix([[4 * r, 0, 1, 0], [1, 0, 0, 0], [4 * r + 2, -1, 1, 1], [-4 * r, -1, 0, 0]])),
            (4 * r + 2, sp.Matrix([[4 * r + 2, -1, 1, 1], [1, 0, 0, 0], [4 * r + 4, 0, 0, 1], [-4 * r, 0, -1, 0]])),
            (4 * r + 3, sp.Matrix([[4 * r + 4, 0, 0, 1], [1, 0, 0, 0], [4 * r + 4, 1, 0, 0], [-4 * r - 2, 1, -1, -1]])),
        ]
        for m, block in blocks:
            if m < 1:
                continue
            expected = sp.factor((t - 1) * (t + 1) * (t**2 - m * t - 1))
            if sp.expand(block.charpoly(t).as_expr() - expected) != 0:
                return result("C1 JACOBIAN BLOCKS", False, f"m={m}")

    return result("C1 JACOBIAN BLOCKS", True, f"checked residue blocks r<= {max_r}")


def q_vectors(c: int, mmax: int) -> dict[int, tuple[int, int, int, int]]:
    q = {-1: (0, 0, 0, 1), 0: (0, 1, 0, 0), 1: (0, 0, 1, 0)}
    force = (2 * c, 0, 0, 0)
    for k in range(2, mmax + 2):
        a, b, d = q[k - 1], q[k - 2], q[k - 3]
        q[k] = tuple(c * a[i] - c * b[i] + d[i] + force[i] for i in range(4))
    return q


def matmul4(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def trace4(a: list[list[int]]) -> int:
    return sum(a[i][i] for i in range(4))


def discriminant_data(c: int, m: int) -> tuple[int, int, int]:
    q = q_vectors(c, m + 1)
    block = [list(q[m]), [1, 0, 0, 0], list(q[m + 1]), [-x for x in q[m - 1]]]
    trace = trace4(block)
    block2 = matmul4(block, block)
    second_coeff = (trace * trace - trace4(block2)) // 2
    discriminant = trace * trace - 4 * (second_coeff + 2)
    return trace, second_coeff, discriminant


def actual_splits(c: int, m: int) -> bool:
    trace, _, discriminant = discriminant_data(c, m)
    if discriminant < 0:
        return False
    root = math.isqrt(discriminant)
    return root * root == discriminant and (trace + root) % 2 == 0


def theorem_splits(c: int, m: int) -> bool:
    return (
        c in (1, 3)
        or (c == 0 and m % 3 == 0)
        or (c == 2 and m % 6 == 0)
        or (c == -1 and m % 2 == 0)
        or (c == -3 and m in (2, 3))
        or (c in (-9, -11) and m == 1)
    )


def check_integer_classification(cmin: int = -120, cmax: int = 120, mmax: int = 120) -> CheckResult:
    failures = []
    split_counts: dict[int, int] = defaultdict(int)
    checked = 0

    for c in range(cmin, cmax + 1):
        for m in range(1, mmax + 1):
            checked += 1
            observed = actual_splits(c, m)
            expected = theorem_splits(c, m)
            if observed:
                split_counts[c] += 1
            if observed != expected:
                failures.append((c, m, observed, expected, discriminant_data(c, m)))
                if len(failures) >= 5:
                    break
        if failures:
            break

    detail = (
        f"{cmin}<=c<={cmax}, 1<=m<={mmax}, checked={checked}, "
        f"split c-values={sorted(split_counts)}"
    )
    if failures:
        detail += f", failures={failures[:3]}"
    return result("INTEGER CLASSIFICATION", len(failures) == 0, detail)


def check_su3_slice(tolerance: float = 1e-9) -> CheckResult:
    omega = np.exp(2j * np.pi / 3)
    representatives = {
        3: (np.eye(3, dtype=complex), np.eye(3, dtype=complex)),
        -1: (
            np.diag([1, -1, -1]).astype(complex),
            np.diag([-1, 1, -1]).astype(complex),
        ),
        0: (
            np.diag([1, omega, omega**2]),
            np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex),
        ),
        1: (
            np.array([[1j, 0, 0], [0, -1j, 0], [0, 0, 1]], dtype=complex),
            np.array([[0, 1j, 0], [1j, 0, 0], [0, 0, 1]], dtype=complex),
        ),
    }

    def coords(a: np.ndarray, b: np.ndarray) -> list[complex]:
        a_inv = np.linalg.inv(a)
        b_inv = np.linalg.inv(b)
        return [
            np.trace(a),
            np.trace(b),
            np.trace(a @ b),
            np.trace(a_inv),
            np.trace(b_inv),
            np.trace(a_inv @ b),
            np.trace(a @ b_inv),
            np.trace(a_inv @ b_inv),
        ]

    for c, (a, b) in representatives.items():
        if np.linalg.norm(a.conj().T @ a - np.eye(3)) > 1e-8:
            return result("SU3 SLICE", False, f"A not unitary c={c}")
        if np.linalg.norm(b.conj().T @ b - np.eye(3)) > 1e-8:
            return result("SU3 SLICE", False, f"B not unitary c={c}")
        if abs(np.linalg.det(a) - 1) > 1e-8:
            return result("SU3 SLICE", False, f"det A mismatch c={c}")
        if abs(np.linalg.det(b) - 1) > 1e-8:
            return result("SU3 SLICE", False, f"det B mismatch c={c}")
        for value in coords(a, b):
            if abs(value - c) > tolerance:
                return result("SU3 SLICE", False, f"coordinate {value} != {c}")

    return result("SU3 SLICE", True, "explicit representatives for c=-1,0,1,3")


def run_certificates(*, deep: bool = False, cmin: int | None = None, cmax: int | None = None, mmax: int | None = None) -> list[CheckResult]:
    if deep:
        cmin, cmax, mmax = -300, 120, 260
    else:
        cmin = -120 if cmin is None else cmin
        cmax = 120 if cmax is None else cmax
        mmax = 120 if mmax is None else mmax

    return [
        check_trace_map_formula(),
        check_direct_matrix_trace(),
        check_entropy(),
        check_c3_jacobian(),
        check_c1_jacobian(),
        check_integer_classification(cmin, cmax, mmax),
        check_su3_slice(),
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run B48 SL(3) metallic trace-map certificates.")
    parser.add_argument("--cmin", type=int, default=None)
    parser.add_argument("--cmax", type=int, default=None)
    parser.add_argument("--mmax", type=int, default=None)
    parser.add_argument("--deep", action="store_true", help="use the larger integer-classification audit rectangle")
    args = parser.parse_args(argv)

    if args.deep:
        rectangle = "-300 <= c <= 120, 1 <= m <= 260"
    else:
        cmin = -120 if args.cmin is None else args.cmin
        cmax = 120 if args.cmax is None else args.cmax
        mmax = 120 if args.mmax is None else args.mmax
        rectangle = f"{cmin} <= c <= {cmax}, 1 <= m <= {mmax}"

    print("B48 -- SL(3) METALLIC TRACE-MAP CERTIFICATES")
    print("Status: frontier evidence only; no Origin-core claim promotion")
    print(f"timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"integer audit rectangle: {rectangle}")
    print()

    checks = run_certificates(deep=args.deep, cmin=args.cmin, cmax=args.cmax, mmax=args.mmax)
    for item in checks:
        print_result(item)

    all_ok = all(item.ok for item in checks)
    print()
    print(f"ALL CERTIFICATES: {'OK' if all_ok else 'FAIL'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
