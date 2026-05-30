"""B18 -- trace-lift functoriality for the half-step F."""

from __future__ import annotations

import sympy as sp


def assert_zero(expr: sp.Expr, label: str) -> None:
    value = sp.factor(sp.simplify(expr))
    if value != 0:
        raise AssertionError(f"{label}: expected 0, got {value}")


def main() -> None:
    print("=" * 72)
    print("B18 -- Trace-lift functoriality")
    print("SPECULATIVE: observations only, not claims (GOVERNANCE.md section 5)")
    print("=" * 72)

    X, Y, Z, x, y, z, t = sp.symbols("X Y Z x y z t")

    print("\n[1] Full-trace half-step")
    full_T = sp.Matrix([Z, X, X * Z - Y])
    print(f"    T_full(X,Y,Z) = {tuple(full_T)}")

    print("\n[2] Half-trace convention")
    half_from_full = [sp.simplify(component.subs({X: 2 * x, Y: 2 * y, Z: 2 * z}) / 2) for component in full_T]
    half_T = sp.Matrix([z, x, 2 * x * z - y])
    assert sp.Matrix(half_from_full) == half_T
    print(f"    T_half(x,y,z) = {tuple(half_T)}")

    print("\n[3] Invariant preservation")
    full_I = X**2 + Y**2 + Z**2 - X * Y * Z - 4
    full_next = full_I.subs({X: full_T[0], Y: full_T[1], Z: full_T[2]}, simultaneous=True)
    assert_zero(full_next - full_I, "full Fricke invariant")
    half_I = x**2 + y**2 + z**2 - 2 * x * y * z - 1
    half_next = half_I.subs({x: half_T[0], y: half_T[1], z: half_T[2]}, simultaneous=True)
    assert_zero(half_next - half_I, "half Fricke invariant")
    assert_zero(full_I.subs({X: 2 * x, Y: 2 * y, Z: 2 * z}) - 4 * half_I, "full/half invariant scale")
    print("    full and half Fricke-Vogt invariants are preserved")

    print("\n[4] A-level map is T_F squared")
    T2 = sp.Matrix([component.subs({x: half_T[0], y: half_T[1], z: half_T[2]}, simultaneous=True) for component in half_T])
    expected_T2 = sp.Matrix([2 * x * z - y, z, z * (2 * x * z - y) * 2 - x])
    # Simplify expected third component: T(T(x,y,z)) = (2xz-y, z, 2z(2xz-y)-x)
    assert sp.simplify(T2 - expected_T2) == sp.zeros(3, 1)
    print(f"    T_F^2 = {tuple(sp.factor(v) for v in T2)}")

    print("\n[5] Jacobian spectra")
    J = half_T.jacobian([x, y, z])
    J0 = J.subs({x: 1, y: 1, z: 1})
    assert_zero(J0.charpoly(t).as_expr() - (t + 1) * (t**2 - 3 * t + 1), "F-level charpoly")
    J2 = J0**2
    assert_zero(J2.charpoly(t).as_expr() - (t - 1) * (t**2 - 7 * t + 1), "A-level charpoly")
    print(f"    char(J_F) = {sp.factor(J0.charpoly(t).as_expr())}")
    print(f"    char(J_F^2) = {sp.factor(J2.charpoly(t).as_expr())}")
    print("    parity -1 resolves to +1 at the A-level")

    print("\nVerdict: STALLED")
    print("Canonical trace-lift gate passes; physics/semantic dictionary remains open.")


if __name__ == "__main__":
    main()
