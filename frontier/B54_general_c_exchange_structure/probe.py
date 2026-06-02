"""B54 -- general-c exchange structure of the metallic SL(3) trace-map Jacobian.

Standalone trace-map mathematics. This probe verifies, as exact symbolic
algebra, that the fixed-line Jacobian of the metallic SL(3) trace map commutes
with the record-exchange involution P for ALL c -- not only at the c=3
representation point established in B51 -- and records the resulting sector
structure:

  * [J(m,c), P] = 0 for symbolic c  (the whole fixed line block-diagonalizes)
  * at c=1 the symmetric sector carries the Eisenstein quadratic t^2-t+1 and the
    antisymmetric sector carries the golden quadratic t^2-t-1 -- the same
    discriminant pair (-3 and 5) recorded for the figure-eight gluing equation
    z^2(z-1)^2=1 = (z^2-z+1)(z^2-z-1) in tests/test_gluing_equation.py (P12).
  * for m=1 the symmetric quadratic t^2-c t+1 sweeps the cyclotomic polynomials
    Phi_3, Phi_4, Phi_6, the parabolic (t-1)^2, and char(A)=t^2-3t+1 as
    c = -1, 0, 1, 2, 3.
  * regression: at c=3 it reproduces the B51 sector factorization for all m.

No physics dictionary, no selector, and no Origin-core claim is promoted. The
[J,P]=0 fact is structural: the trace map is equivariant under the coordinate
exchange P, and the fixed line is P-invariant, so the Jacobian commutes with P
everywhere on it. The clean cyclotomic sweep is m=1-specific (for general m the
symmetric c=1 polynomial depends on m parity); the c=1 antisymmetric char(M)
and the c=3 factorization are the m-general facts.

Coordinate convention follows B48/B51:
x1=tr(A), x2=tr(B), x3=tr(AB), x4=tr(A^-1),
x5=tr(B^-1), x6=tr(A^-1 B), x7=tr(A B^-1), x8=tr(A^-1 B^-1).
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


def _unit(index: int) -> sp.Matrix:
    column = sp.zeros(8, 1)
    column[index] = 1
    return column


def exchange_involution() -> sp.Matrix:
    """Matrix for x1<->x4, x2<->x5, x3<->x8, x6<->x7."""
    pairs = {0: 3, 3: 0, 1: 4, 4: 1, 2: 7, 7: 2, 5: 6, 6: 5}
    matrix = sp.zeros(8)
    for source, target in pairs.items():
        matrix[target, source] = 1
    return matrix


def tau_derivative_rows(c: sp.Expr, max_k: int) -> dict[int, sp.Matrix]:
    """d tau_k / d x_j on the fixed line x_i = c, as column vectors.

    tau_k = x1 tau_{k-1} - x4 tau_{k-2} + tau_{k-3}; on the fixed line every
    trace equals c, so differentiating gives the linearized recurrence
    dtau_k = c dtau_{k-1} - c dtau_{k-2} + dtau_{k-3} + c (e_x1 - e_x4).
    Seeds: tau_{-1}=x6, tau_0=x2, tau_1=x3.
    """
    rows = {-1: _unit(5), 0: _unit(1), 1: _unit(2)}
    forcing = c * (_unit(0) - _unit(3))
    for k in range(2, max_k + 1):
        rows[k] = sp.expand(c * rows[k - 1] - c * rows[k - 2] + rows[k - 3] + forcing)
    return rows


def symbolic_jacobian(m_value: int, c: sp.Expr) -> sp.Matrix:
    """8x8 fixed-line Jacobian J(m, c); m a positive integer, c symbolic."""
    exchange = exchange_involution()
    tau = tau_derivative_rows(c, m_value + 1)
    sigma = {k: exchange * tau[k] for k in tau}
    rows = [
        tau[m_value],
        _unit(0),
        tau[m_value + 1],
        sigma[m_value],
        _unit(3),
        sigma[m_value - 1],
        tau[m_value - 1],
        sigma[m_value + 1],
    ]
    return sp.Matrix.hstack(*rows).T


def exchange_basis() -> sp.Matrix:
    """Columns: symmetric then antisymmetric exchange eigenvectors."""
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


def sectors(m_value: int, c_value: sp.Expr):
    """Return (symmetric 4x4, antisymmetric 4x4, off_upper, off_lower)."""
    jacobian = symbolic_jacobian(m_value, c_value)
    basis = exchange_basis()
    in_basis = sp.simplify(basis.inv() * jacobian * basis)
    return (
        in_basis[:4, :4],
        in_basis[4:, 4:],
        sp.simplify(in_basis[:4, 4:]),
        sp.simplify(in_basis[4:, :4]),
    )


def check_exchange_commutation_all_c() -> CheckResult:
    c = sp.symbols("c")
    exchange = exchange_involution()
    for m_value in (1, 2, 3):
        jacobian = symbolic_jacobian(m_value, c)
        if sp.simplify(jacobian * exchange - exchange * jacobian) != sp.zeros(8):
            return result("EXCHANGE COMMUTATION (ALL c)", False, f"[J,P]!=0 at m={m_value}")
        _, _, off_upper, off_lower = sectors(m_value, c)
        if off_upper != sp.zeros(4) or off_lower != sp.zeros(4):
            return result("EXCHANGE COMMUTATION (ALL c)", False, f"off-diagonal block nonzero at m={m_value}")
    return result(
        "EXCHANGE COMMUTATION (ALL c)",
        True,
        "symbolic-c block diagonalization, m=1,2,3 (generalizes B51's c=3 result)",
    )


def check_c1_twin_polynomials() -> CheckResult:
    t = sp.symbols("t")
    symmetric, antisymmetric, _, _ = sectors(1, sp.Integer(1))
    eisenstein = t**2 - t + 1  # discriminant -3, Phi_6
    golden = t**2 - t - 1  # discriminant 5, char(M) for m=1
    sym_rem = sp.rem(symmetric.charpoly(t).as_expr(), eisenstein, t)
    anti_rem = sp.rem(antisymmetric.charpoly(t).as_expr(), golden, t)
    if sym_rem != 0:
        return result("C1 TWIN POLYNOMIALS", False, "symmetric sector not divisible by t^2-t+1")
    if anti_rem != 0:
        return result("C1 TWIN POLYNOMIALS", False, "antisymmetric sector not divisible by t^2-t-1")
    return result(
        "C1 TWIN POLYNOMIALS",
        True,
        "sym=Eisenstein(disc -3), anti=golden(disc 5) -- same pair as P12 gluing equation",
    )


def check_cyclotomic_sweep() -> CheckResult:
    t, c = sp.symbols("t c")
    expected = {
        -1: t**2 + t + 1,  # Phi_3
        0: t**2 + 1,  # Phi_4
        1: t**2 - t + 1,  # Phi_6 (Eisenstein)
        2: t**2 - 2 * t + 1,  # (t-1)^2 parabolic
        3: t**2 - 3 * t + 1,  # char(A)
    }
    for c_value, quadratic in expected.items():
        symmetric, _, _, _ = sectors(1, sp.Integer(c_value))
        charpoly = symmetric.charpoly(t).as_expr()
        predicted = sp.expand((t - 1) * (t + 1) * quadratic)
        if sp.expand(charpoly - predicted) != 0:
            return result("CYCLOTOMIC SWEEP (m=1)", False, f"mismatch at c={c_value}")
    return result(
        "CYCLOTOMIC SWEEP (m=1)",
        True,
        "symmetric t^2-ct+1 = Phi_3,Phi_4,Phi_6,(t-1)^2,char(A) at c=-1,0,1,2,3",
    )


def check_c3_regression() -> CheckResult:
    t, m = sp.symbols("t m")
    for m_value in (1, 2, 3):
        symmetric, antisymmetric, _, _ = sectors(m_value, sp.Integer(3))
        sym_expected = sp.expand((t - 1) * (t + 1) * (t**2 - (m_value**2 + 2) * t + 1))
        anti_expected = sp.expand((t**2 + m_value * t - 1) * (t**2 - (m_value**3 + 3 * m_value) * t - 1))
        if sp.expand(symmetric.charpoly(t).as_expr() - sym_expected) != 0:
            return result("C3 REGRESSION (vs B51)", False, f"symmetric mismatch at m={m_value}")
        if sp.expand(antisymmetric.charpoly(t).as_expr() - anti_expected) != 0:
            return result("C3 REGRESSION (vs B51)", False, f"antisymmetric mismatch at m={m_value}")
    return result("C3 REGRESSION (vs B51)", True, "c=3 sectors match B51 for m=1,2,3")


def run_checks() -> list[CheckResult]:
    return [
        check_exchange_commutation_all_c(),
        check_c1_twin_polynomials(),
        check_cyclotomic_sweep(),
        check_c3_regression(),
    ]


def main() -> int:
    print("B54 -- GENERAL-c EXCHANGE STRUCTURE (metallic SL(3) trace map)")
    print("Status: standalone trace-map math; no claim promotion")
    print()
    checks = run_checks()
    for item in checks:
        print_result(item)
    ok = all(item.ok for item in checks)
    print()
    print(f"B54 GENERAL-c STRUCTURE: {'OK' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
