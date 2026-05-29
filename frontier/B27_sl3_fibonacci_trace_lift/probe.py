"""B27 -- SL(3) Fibonacci trace lift.

Computes the Fibonacci substitution on the eight standard trace coordinates of
the SL(3) character variety of F_2. This is exact algebra and numerical
verification only; no physical dictionary is claimed.
"""

from __future__ import annotations

import numpy as np
import sympy as sp


PHI = (1.0 + np.sqrt(5.0)) / 2.0


def sl3_trace_map_symbolic() -> tuple[tuple[sp.Symbol, ...], sp.Matrix]:
    x = sp.symbols("x1:9")
    x1, x2, x3, x4, x5, x6, x7, x8 = x
    image = sp.Matrix(
        [
            x5,
            x6,
            x1,
            x2,
            x1 * x5 - x2 * x3 + x8,
            x2 * x6 - x1 * x4 + x7,
            x3,
            x4,
        ]
    )
    return x, image


def sl3_trace_map_numeric(state: np.ndarray) -> np.ndarray:
    x1, x2, x3, x4, x5, x6, x7, x8 = state
    return np.array(
        [
            x5,
            x6,
            x1,
            x2,
            x1 * x5 - x2 * x3 + x8,
            x2 * x6 - x1 * x4 + x7,
            x3,
            x4,
        ],
        dtype=float,
    )


def random_sl3(seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    matrix = rng.normal(size=(3, 3))
    determinant = np.linalg.det(matrix)
    scale = np.sign(determinant) / (abs(determinant) ** (1.0 / 3.0))
    out = scale * matrix
    assert abs(np.linalg.det(out) - 1.0) < 1e-10
    return out


def trace_state(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    a_inv = np.linalg.inv(a)
    b_inv = np.linalg.inv(b)
    ab = a @ b
    return np.array(
        [
            np.trace(a),
            np.trace(a_inv),
            np.trace(b),
            np.trace(b_inv),
            np.trace(ab),
            np.trace(np.linalg.inv(ab)),
            np.trace(a @ b_inv),
            np.trace(a_inv @ b),
        ],
        dtype=float,
    )


def commutator(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b @ np.linalg.inv(a) @ np.linalg.inv(b)


def main() -> None:
    print("=" * 72)
    print("B27 -- SL(3) Fibonacci trace lift")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    t = sp.symbols("t")
    x, image = sl3_trace_map_symbolic()
    jacobian = image.jacobian(sp.Matrix(x))
    fixed_point = {var: 3 for var in x}
    jacobian_fp = jacobian.subs(fixed_point)

    print("\n[1] exact polynomial map")
    for index, component in enumerate(image, start=1):
        print(f"    x{index}' = {component}")

    print("\n[2] random SL(3) matrix verification")
    for seed in range(5):
        a = random_sl3(1000 + seed)
        b = random_sl3(2000 + seed)
        before = trace_state(a, b)
        expected = trace_state(a @ b, a)
        observed = sl3_trace_map_numeric(before)
        error = float(np.max(np.abs(expected - observed)))
        print(f"    seed={seed}: max trace-map error = {error:.2e}")
        assert error < 1e-8

    print("\n[3] fixed-point Jacobian")
    charpoly = sp.factor(jacobian_fp.charpoly(t).as_expr())
    expected_charpoly = sp.factor(
        (t - 1) * (t + 1) * (t**2 - 4 * t - 1) * (t**2 - 3 * t + 1) * (t**2 + t - 1)
    )
    print(f"    char(DT) = {charpoly}")
    assert sp.expand(charpoly - expected_charpoly) == 0

    eigenvalues = sorted([complex(value.evalf()) for value in jacobian_fp.eigenvals()], key=lambda z: -abs(z))
    expected_abs_powers = [PHI**3, PHI**2, PHI, 1.0, 1.0, PHI**-1, PHI**-2, PHI**-3]
    for value, expected_abs in zip(eigenvalues, expected_abs_powers):
        print(f"    eigenvalue {value.real: .6f}; |value|/expected = {abs(value.real) / expected_abs:.6f}")
        assert abs(abs(value.real) - expected_abs) < 1e-9

    print("\n[4] symmetric / antisymmetric inverse-trace decomposition")
    columns = []
    for i, j in [(0, 1), (2, 3), (4, 5), (6, 7)]:
        column = [0] * 8
        column[i] = 1
        column[j] = 1
        columns.append(column)
    for i, j in [(0, 1), (2, 3), (4, 5), (6, 7)]:
        column = [0] * 8
        column[i] = 1
        column[j] = -1
        columns.append(column)
    basis = sp.Matrix.hstack(*[sp.Matrix(column) for column in columns])
    transformed = sp.simplify(basis.inv() * jacobian_fp * basis)
    sym_block = transformed[:4, :4]
    anti_block = transformed[4:8, 4:8]
    assert transformed[:4, 4:8] == sp.zeros(4, 4)
    assert transformed[4:8, :4] == sp.zeros(4, 4)
    sym_char = sp.factor(sym_block.charpoly(t).as_expr())
    anti_char = sp.factor(anti_block.charpoly(t).as_expr())
    print(f"    symmetric char = {sym_char}")
    print(f"    antisymmetric char = {anti_char}")
    assert sp.expand(sym_char - (t - 1) * (t + 1) * (t**2 - 3 * t + 1)) == 0
    assert sp.expand(anti_char - (t**2 - 4 * t - 1) * (t**2 + t - 1)) == 0

    print("\n[5] commutator trace swap")
    for seed in range(5):
        a = random_sl3(3000 + seed)
        b = random_sl3(4000 + seed)
        comm = commutator(a, b)
        new_comm = commutator(a @ b, a)
        tr_comm = float(np.trace(comm))
        tr_comm_inv = float(np.trace(np.linalg.inv(comm)))
        tr_new = float(np.trace(new_comm))
        tr_new_inv = float(np.trace(np.linalg.inv(new_comm)))
        print(
            f"    seed={seed}: tr -> {tr_comm:.6f},{tr_new:.6f}; "
            f"tr_inv -> {tr_comm_inv:.6f},{tr_new_inv:.6f}"
        )
        assert abs(tr_new - tr_comm_inv) < 1e-8
        assert abs(tr_new_inv - tr_comm) < 1e-8

    print("\nVerdict: STALLED")
    print("The SL(3) lift preserves and enriches the golden trace-lift structure,")
    print("but no physical dictionary is derived.")


if __name__ == "__main__":
    main()
