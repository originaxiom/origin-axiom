"""B51 -- symbolic-m SL(3) fixed-line factorization.

This probe integrates the symbolic proof module for PC12's c=3 fixed-line
Jacobian. It keeps m formal, derives the derivative rows from the triple-root
Cayley-Hamilton recurrence, and verifies the symmetric/antisymmetric block
factorizations symbolically.

No physics dictionary or Origin-core claim is promoted.
"""

from __future__ import annotations

from dataclasses import dataclass

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


def tau_derivative_row(k: sp.Expr) -> sp.Matrix:
    """Closed-form derivatives of tau_k at the c=3 fixed line.

    Coordinate convention follows B48:
    x1=tr(A), x2=tr(B), x3=tr(AB), x4=tr(A^-1),
    x5=tr(B^-1), x6=tr(A^-1 B), x7=tr(A B^-1), x8=tr(A^-1 B^-1).
    """
    return sp.Matrix(
        [
            k * (k**2 - 1) / 2,
            1 - k**2,
            k * (k + 1) / 2,
            -k * (k**2 - 1) / 2,
            0,
            k * (k - 1) / 2,
            0,
            0,
        ]
    ).T


def sigma_derivative_row(k: sp.Expr) -> sp.Matrix:
    """Closed-form derivatives of sigma_k by record exchange."""
    tau = tau_derivative_row(k)
    # Exchange x1<->x4, x2<->x5, x3<->x8, x6<->x7.
    return sp.Matrix([[tau[0, 3], 0, 0, tau[0, 0], tau[0, 1], 0, tau[0, 5], tau[0, 2]]])


def recurrence_derivative_step(
    previous_1: sp.Matrix,
    previous_2: sp.Matrix,
    previous_3: sp.Matrix,
    *,
    tau_value: int = 3,
) -> sp.Matrix:
    """Derivative recurrence for tau_k at the c=3 fixed line."""
    forcing = sp.Matrix([[tau_value, 0, 0, -tau_value, 0, 0, 0, 0]])
    return 3 * previous_1 - 3 * previous_2 + previous_3 + forcing


def check_derivative_sequences(max_k: int = 12) -> CheckResult:
    rows = {
        -1: sp.Matrix([[0, 0, 0, 0, 0, 1, 0, 0]]),
        0: sp.Matrix([[0, 1, 0, 0, 0, 0, 0, 0]]),
        1: sp.Matrix([[0, 0, 1, 0, 0, 0, 0, 0]]),
    }

    for k in range(2, max_k + 1):
        rows[k] = recurrence_derivative_step(rows[k - 1], rows[k - 2], rows[k - 3])

    for k in range(-1, max_k + 1):
        if any(sp.simplify(value) != 0 for value in rows[k] - tau_derivative_row(sp.Integer(k))):
            return result("DERIVATIVE SEQUENCES", False, f"tau derivative mismatch at k={k}")

    return result("DERIVATIVE SEQUENCES", True, f"closed forms checked through k={max_k}")


def symbolic_jacobian() -> sp.Matrix:
    m = sp.symbols("m")
    return sp.Matrix.vstack(
        tau_derivative_row(m),
        sp.Matrix([[1, 0, 0, 0, 0, 0, 0, 0]]),
        tau_derivative_row(m + 1),
        sigma_derivative_row(m),
        sp.Matrix([[0, 0, 0, 1, 0, 0, 0, 0]]),
        sigma_derivative_row(m - 1),
        tau_derivative_row(m - 1),
        sigma_derivative_row(m + 1),
    )


def exchange_involution() -> sp.Matrix:
    """Matrix for x1<->x4, x2<->x5, x3<->x8, x6<->x7."""
    pairs = {0: 3, 3: 0, 1: 4, 4: 1, 2: 7, 7: 2, 5: 6, 6: 5}
    matrix = sp.zeros(8)
    for source, target in pairs.items():
        matrix[target, source] = 1
    return matrix


def exchange_basis() -> sp.Matrix:
    """Columns are symmetric then antisymmetric exchange eigenvectors."""
    pairs = [(0, 3), (1, 4), (2, 7), (5, 6)]
    columns = []
    for left, right in pairs:
        vector = sp.zeros(8, 1)
        vector[left] = 1
        vector[right] = 1
        columns.append(vector)
    for left, right in pairs:
        vector = sp.zeros(8, 1)
        vector[left] = 1
        vector[right] = -1
        columns.append(vector)
    return sp.Matrix.hstack(*columns)


def block_data() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    jacobian = symbolic_jacobian()
    basis = exchange_basis()
    in_exchange_basis = sp.simplify(basis.inv() * jacobian * basis)
    symmetric = sp.simplify(in_exchange_basis[:4, :4])
    antisymmetric = sp.simplify(in_exchange_basis[4:, 4:])
    return in_exchange_basis, symmetric, antisymmetric


def check_exchange_block_diagonalization() -> CheckResult:
    jacobian = symbolic_jacobian()
    exchange = exchange_involution()
    if sp.simplify(exchange * jacobian - jacobian * exchange) != sp.zeros(8):
        return result("EXCHANGE COMMUTATION", False, "P J(m) != J(m) P")

    block_matrix, _, _ = block_data()
    if sp.simplify(block_matrix[:4, 4:]) != sp.zeros(4):
        return result("EXCHANGE COMMUTATION", False, "symmetric-to-antisymmetric block nonzero")
    if sp.simplify(block_matrix[4:, :4]) != sp.zeros(4):
        return result("EXCHANGE COMMUTATION", False, "antisymmetric-to-symmetric block nonzero")

    return result("EXCHANGE COMMUTATION", True, "symbolic J(m) block diagonalizes by exchange")


def check_symbolic_charpolys() -> CheckResult:
    m, t = sp.symbols("m t")
    _, symmetric, antisymmetric = block_data()

    symmetric_expected = sp.factor((t - 1) * (t + 1) * (t**2 - (m**2 + 2) * t + 1))
    antisymmetric_expected = sp.factor((t**2 + m * t - 1) * (t**2 - (m**3 + 3 * m) * t - 1))

    symmetric_difference = sp.expand(symmetric.charpoly(t).as_expr() - symmetric_expected)
    antisymmetric_difference = sp.expand(antisymmetric.charpoly(t).as_expr() - antisymmetric_expected)
    if symmetric_difference != 0:
        return result("SYMBOLIC CHARPOLYS", False, f"symmetric difference {symmetric_difference}")
    if antisymmetric_difference != 0:
        return result("SYMBOLIC CHARPOLYS", False, f"antisymmetric difference {antisymmetric_difference}")

    return result("SYMBOLIC CHARPOLYS", True, "both block identities expand to zero")


def run_checks() -> list[CheckResult]:
    return [
        check_derivative_sequences(),
        check_exchange_block_diagonalization(),
        check_symbolic_charpolys(),
    ]


def main() -> int:
    print("B51 -- SL(3) SYMBOLIC-m FACTORIZATION")
    print("Status: proof module only; PC12 remains NEEDS_VALIDATION")
    print()
    checks = run_checks()
    for item in checks:
        print_result(item)
    ok = all(item.ok for item in checks)
    print()
    print(f"B51 SYMBOLIC PROOF MODULE: {'OK' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
