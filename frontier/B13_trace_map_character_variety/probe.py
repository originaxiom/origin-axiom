"""Frontier probe B13 -- trace map character variety.

This probe verifies exact algebra for the punctured-torus trace map. It does
not promote any claim and does not interpret trace coordinates as physical
spacetime coordinates.
"""

from __future__ import annotations

import sympy as sp


def assert_zero(expr: sp.Expr, label: str) -> None:
    simplified = sp.factor(sp.simplify(expr))
    if simplified != 0:
        raise AssertionError(f"{label}: expected 0, got {simplified}")


def symmetric_square_matrix(matrix: sp.Matrix) -> sp.Matrix:
    """Symmetric-square action in the basis u^2, uv, v^2."""

    a, b, c, d = matrix[0, 0], matrix[0, 1], matrix[1, 0], matrix[1, 1]
    return sp.Matrix(
        [
            [a * a, a * c, c * c],
            [2 * a * b, a * d + b * c, 2 * c * d],
            [b * b, b * d, d * d],
        ]
    )


def symmetric_square_charpoly(matrix: sp.Matrix, variable: sp.Symbol) -> sp.Expr:
    """Expected characteristic polynomial of the symmetric-square lift."""

    trace = matrix.trace()
    determinant = matrix.det()
    return sp.factor(
        (variable - determinant)
        * (variable**2 - (trace**2 - 2 * determinant) * variable + determinant**2)
    )


def main() -> None:
    x, y, z, t, eps = sp.symbols("x y z t eps")
    sqrt5 = sp.sqrt(5)
    phi = (1 + sqrt5) / 2

    A = sp.Matrix([[2, 1], [1, 1]])
    trace_map = sp.Matrix([z, x, 2 * x * z - y])
    invariant = x**2 + y**2 + z**2 - 2 * x * y * z - 1

    print("=" * 72)
    print("B13 -- Trace map character variety")
    print("SPECULATIVE: observations only, not claims (GOVERNANCE.md section 5)")
    print("=" * 72)

    print("\n[1] Jacobian at the Cayley singular point")
    J = trace_map.jacobian([x, y, z])
    J0 = sp.Matrix(J.subs({x: 1, y: 1, z: 1}))
    expected_J0 = sp.Matrix([[0, 0, 1], [1, 0, 0], [2, -1, 2]])
    assert J0 == expected_J0
    charpoly = sp.factor(J0.charpoly(t).as_expr())
    expected_charpoly = (t + 1) * (t**2 - 3 * t + 1)
    assert sp.expand(charpoly - expected_charpoly) == 0
    print(f"    J = {J0.tolist()}")
    print(f"    charpoly(J) = {charpoly}")
    print("    eigenvalue sectors: parity (-1) plus golden quadratic")

    print("\n[2] The A-sector as an invariant lattice restriction")
    b1 = sp.Matrix([0, 1, -1])
    b2 = sp.Matrix([1, 0, 3])
    B = sp.Matrix.hstack(b1, b2)
    restriction_cols = [B.gauss_jordan_solve((J0 * B)[:, i])[0] for i in range(2)]
    M = sp.Matrix.hstack(*restriction_cols)
    expected_M = sp.Matrix([[0, 1], [-1, 3]])
    assert M == expected_M
    P = sp.Matrix([[-5, 8], [-2, 3]])
    assert P.det() == 1
    assert P.inv() * M * P == A
    parity_vector = sp.Matrix([1, -1, -1])
    block_basis = sp.Matrix.hstack(parity_vector, B)
    block_form = block_basis.inv() * J0 * block_basis
    expected_block = sp.Matrix([[-1, 0, 0], [0, 0, 1], [0, -1, 3]])
    assert block_form == expected_block
    assert block_basis.det() == 5
    print(f"    restriction M = {M.tolist()}")
    print("    P^-1 M P = A with det(P)=1")
    print(f"    full block basis determinant = {block_basis.det()}")
    print(f"    block form = {block_form.tolist()}")

    print("\n[3] Fricke-Vogt invariant")
    x1, y1, z1 = trace_map
    invariant_next = x1**2 + y1**2 + z1**2 - 2 * x1 * y1 * z1 - 1
    assert_zero(invariant_next - invariant, "trace-map invariant")
    print(f"    I(x,y,z) = {invariant}")
    print("    I(T(x,y,z)) - I(x,y,z) = 0")

    print("\n[4] Cayley cubic singular tetrahedron")
    gradient = [sp.diff(invariant, var) for var in (x, y, z)]
    singular_points = [
        (1, 1, 1),
        (1, -1, -1),
        (-1, 1, -1),
        (-1, -1, 1),
    ]
    for point in singular_points:
        subs = dict(zip((x, y, z), point))
        assert invariant.subs(subs) == 0
        assert all(component.subs(subs) == 0 for component in gradient)
    squared_distances = set()
    for i, p in enumerate(singular_points):
        for q in singular_points[i + 1 :]:
            squared_distances.add(sum((p[k] - q[k]) ** 2 for k in range(3)))
    assert squared_distances == {8}
    print(f"    singular points = {singular_points}")
    print("    all six edge lengths = 2*sqrt(2)")

    print("\n[5] Hessian at (1,1,1)")
    H = sp.hessian(invariant, (x, y, z)).subs({x: 1, y: 1, z: 1})
    eigenvals = H.eigenvals()
    assert eigenvals == {-2: 1, 4: 2}
    assert H * sp.Matrix([1, 1, 1]) == -2 * sp.Matrix([1, 1, 1])
    print(f"    H = {H.tolist()}")
    print("    eigenvalues = {-2: 1, 4: 2}")
    print("    diagonal direction (1,1,1) has eigenvalue -2")

    print("\n[6] Local parity-protected splitting family")
    J_eps = sp.Matrix(J.subs({x: 1 + eps, z: 1 + eps}))
    char_eps = sp.factor(J_eps.charpoly(t).as_expr())
    expected_char_eps = (t + 1) * (t**2 - (3 + 2 * eps) * t + 1)
    assert sp.expand(char_eps - expected_char_eps) == 0
    char = char_eps
    char_0 = char.subs(eps, 0)
    char_1 = sp.diff(char, eps).subs(eps, 0)
    dchar_0 = sp.diff(char_0, t)
    d_parity = sp.simplify(-char_1.subs(t, -1) / dchar_0.subs(t, -1))
    d_expand = sp.simplify(-char_1.subs(t, phi**2) / dchar_0.subs(t, phi**2))
    d_contract = sp.simplify(-char_1.subs(t, phi ** -2) / dchar_0.subs(t, phi ** -2))
    assert d_parity == 0
    assert sp.simplify(d_expand - (1 + 3 * sqrt5 / 5)) == 0
    assert sp.simplify(d_contract - (1 - 3 * sqrt5 / 5)) == 0
    print(f"    charpoly(J_eps) = {char_eps}")
    print(f"    delta(lambda_phi2) = {d_expand}")
    print(f"    delta(lambda_phi-2) = {d_contract}")
    print("    delta(lambda_parity) = 0")

    print("\n[7] Control: the deformation is not a fixed-point family")
    fixed_equations = [
        sp.Eq(trace_map[0], x),
        sp.Eq(trace_map[1], y),
        sp.Eq(trace_map[2], z),
    ]
    fixed_points = sp.solve(fixed_equations, (x, y, z), dict=True)
    assert fixed_points == [{x: 0, y: 0, z: 0}, {x: 1, y: 1, z: 1}]
    print(f"    fixed points of T = {fixed_points}")
    print("    so x=z=1+eps is a local Jacobian family, not a fixed-point branch")

    print("\n[8] Iterate spectrum and continuum proxy")
    for n in range(1, 9):
        Jn = J0**n
        spectral_value = phi ** (2 * n)
        assert (Jn - spectral_value * sp.eye(3)).det().simplify() == 0
    print("    for N=1..8, phi^(2N) is an eigenvalue of J^N")
    print("    log spectral radius = 2N*log(phi) (spectral arithmetic only)")

    G = J0 - sp.eye(3)
    G_char = sp.factor(G.charpoly(t).as_expr())
    expected_G_char = (t - phi) * (t + 1 / phi) * (t + 2)
    assert_zero(G_char - expected_G_char, "continuum-proxy characteristic polynomial")
    print(f"    charpoly(J-I) = {G_char}")
    print("    eigenvalues(J-I) = phi, -1/phi, -2")

    print("\n[9] Volume/shear control")
    assert J0.det() == -1
    assert (J0**2).det() == 1
    abs_product = phi**2 * 1 * phi ** -2
    assert sp.simplify(abs_product - 1) == 0
    print("    det(J) = -1")
    print("    det(J^2) = +1")
    print("    product of absolute eigenvalues = 1")

    print("\n[10] Genericity control: symmetric-square lift")
    F = sp.Matrix([[1, 1], [1, 0]])
    A_direct = sp.Matrix([[2, 1], [1, 1]])
    controls = [
        ("F half-step", F, (t + 1) * (t**2 - 3 * t + 1)),
        ("A=F^2 direct monodromy", A_direct, (t - 1) * (t**2 - 7 * t + 1)),
        (
            "orientation-reversing trace-2 control",
            sp.Matrix([[2, 1], [1, 0]]),
            (t + 1) * (t**2 - 6 * t + 1),
        ),
        (
            "orientation-reversing trace-3 control",
            sp.Matrix([[3, 1], [1, 0]]),
            (t + 1) * (t**2 - 11 * t + 1),
        ),
    ]
    for label, matrix, expected in controls:
        sym2 = symmetric_square_matrix(matrix)
        actual = sp.factor(sym2.charpoly(t).as_expr())
        formula = symmetric_square_charpoly(matrix, t)
        assert_zero(actual - formula, f"{label} symmetric-square formula")
        assert_zero(actual - expected, f"{label} expected polynomial")
        print(
            f"    {label}: tr={matrix.trace()}, det={matrix.det()}, "
            f"disc={matrix.trace()**2 - 4 * matrix.det()}, char={actual}"
        )

    coefficient = t**2 - 3 * t + 1
    # The A quadratic appears in a symmetric-square lift iff
    # trace(M)^2 - 2 det(M) = 3 and det(M)^2 = 1.
    # Over GL(2,Z), det=+1 would require trace^2=5, impossible; det=-1
    # requires trace^2=1. Thus the A-sector is the minimal
    # orientation-reversing hyperbolic case, exemplified by F.
    possible = []
    for determinant in (-1, 1):
        for trace_value in range(-8, 9):
            if trace_value**2 - 2 * determinant == 3:
                possible.append((determinant, trace_value))
    assert possible == [(-1, -1), (-1, 1)]
    assert coefficient == t**2 - 3 * t + 1
    print("    A-sector criterion: det=-1 and trace=+/-1 only")
    print("    direct A gives an A^2-sector, not an A-sector")

    print("\nVerdict: STALLED")
    print("Exact trace-map algebra is real; the physics/awareness dictionary is not derived.")


if __name__ == "__main__":
    main()
