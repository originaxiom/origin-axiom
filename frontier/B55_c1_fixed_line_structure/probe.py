"""B55 -- c=1 fixed-line structure of the metallic SL(3) trace-map Jacobian.

Standalone trace-map mathematics. This probe characterizes both exchange sectors
of the fixed-line Jacobian at c=1 for GENERAL m, completing the c=1 row that B54
established only for m=1. The results are proved per residue class mod 4 with m
symbolic, then cross-checked numerically for m=1..12.

Results:
  * symmetric sector (mod 4):
        m = 1, 3 (mod 4) : (t-1)(t+1)(t^2 - t + 1)   [Phi_6, Eisenstein]
        m = 2     (mod 4): (t-1)(t+1)(t^2 + 1)        [Phi_4, Gaussian]
        m = 0     (mod 4): (t-1)^3 (t+1)              [degenerate, parabolic]
  * antisymmetric sector (all m):
        (t-1)(t+1)(t^2 - m t - 1)                     [char(M) universal]

Mechanism: at c=1 the fixed-line derivative recurrence
    dtau_k = dtau_{k-1} - dtau_{k-2} + dtau_{k-3} + (e_x1 - e_x4)
has characteristic equation (r-1)(r^2+1) = 0, roots {1, i, -i}. The constant
forcing resonates with the root r=1, producing a single linear-in-k term
(slope L = (1/2,0,0,-1/2,0,0,0,0), living only in the x1, x4 coordinates) on top
of a period-4 part. Hence dtau_k = k*L + Q(k mod 4) with Q periodic, so
dtau(k+4) = dtau(k) + 4L. The period-4 part gives the mod-4 cyclotomic symmetric
sector; the linear term (in x1, x4) gives the m-dependent char(M) = t^2 - m t - 1
in the antisymmetric sector.

No physics dictionary, no selector, no Origin-core claim. The c=1 Eisenstein
factor's resemblance to the figure-eight tetrahedron shape is a cyclotomic
coincidence -- see frontier/B56 for the negative control on the I=1/4 bridge.

Coordinate convention follows B48/B51/B54:
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
    pairs = {0: 3, 3: 0, 1: 4, 4: 1, 2: 7, 7: 2, 5: 6, 6: 5}
    matrix = sp.zeros(8)
    for source, target in pairs.items():
        matrix[target, source] = 1
    return matrix


_FORCING = _unit(0) - _unit(3)
_SLOPE = sp.Matrix([sp.Rational(1, 2), 0, 0, sp.Rational(-1, 2), 0, 0, 0, 0])


def c1_tau_rows(max_k: int) -> dict[int, sp.Matrix]:
    """Integer-index derivative rows on the c=1 fixed line, by the recurrence."""
    rows = {-1: _unit(5), 0: _unit(1), 1: _unit(2)}
    for k in range(2, max_k + 1):
        rows[k] = sp.expand(rows[k - 1] - rows[k - 2] + rows[k - 3] + _FORCING)
    return rows


def _periodic_offsets() -> dict[int, sp.Matrix]:
    """Q(r) = dtau(r) - r*L for r = 0,1,2,3 (the period-4 part)."""
    rows = c1_tau_rows(4)
    return {r: sp.expand(rows[r] - r * _SLOPE) for r in range(4)}


_OFFSET = _periodic_offsets()


def tau_row_symbolic(residue: int, index_expr: sp.Expr) -> sp.Matrix:
    """dtau at a symbolic index with the given residue mod 4: index*L + Q(residue)."""
    return sp.expand(index_expr * _SLOPE + _OFFSET[residue % 4])


def exchange_basis() -> sp.Matrix:
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


def _assemble(tau_mm1, tau_m, tau_mp1) -> sp.Matrix:
    exchange = exchange_involution()
    sigma = lambda row: exchange * row
    rows = [tau_m, _unit(0), tau_mp1, sigma(tau_m), _unit(3), sigma(tau_mm1), tau_mm1, sigma(tau_mp1)]
    return sp.Matrix.hstack(*rows).T


def _sectors(jacobian: sp.Matrix):
    basis = exchange_basis()
    in_basis = sp.simplify(basis.inv() * jacobian * basis)
    return in_basis[:4, :4], in_basis[4:, 4:]


def jacobian_integer(m_value: int) -> sp.Matrix:
    """Direct c=1 Jacobian at integer m (independent of the L+Q decomposition)."""
    rows = c1_tau_rows(m_value + 1)
    return _assemble(rows[m_value - 1], rows[m_value], rows[m_value + 1])


def jacobian_symbolic_class(residue: int, m: sp.Symbol) -> sp.Matrix:
    """c=1 Jacobian for symbolic m in residue class `residue` mod 4."""
    tau_m = tau_row_symbolic(residue, m)
    tau_mm1 = tau_row_symbolic((residue - 1) % 4, m - 1)
    tau_mp1 = tau_row_symbolic((residue + 1) % 4, m + 1)
    return _assemble(tau_mm1, tau_m, tau_mp1)


def expected_symmetric(residue: int, t: sp.Symbol) -> sp.Expr:
    if residue % 4 in (1, 3):
        return sp.expand((t - 1) * (t + 1) * (t**2 - t + 1))  # Phi_6
    if residue % 4 == 2:
        return sp.expand((t - 1) * (t + 1) * (t**2 + 1))  # Phi_4
    return sp.expand((t - 1) ** 3 * (t + 1))  # degenerate


def check_period_structure() -> CheckResult:
    rows = c1_tau_rows(6)
    for k in range(-1, 3):
        if sp.expand(rows[k + 4] - rows[k] - 4 * _SLOPE) != sp.zeros(8, 1):
            return result("PERIOD-4 + LINEAR STRUCTURE", False, f"dtau(k+4)-dtau(k)!=4L at k={k}")
    return result("PERIOD-4 + LINEAR STRUCTURE", True, "dtau(k)=k*L+Q(k mod 4); roots {1,i,-i} + resonance")


def check_symmetric_mod4() -> CheckResult:
    m, t = sp.symbols("m t")
    for residue in range(4):
        sym, _ = _sectors(jacobian_symbolic_class(residue, m))
        if sp.expand(sym.charpoly(t).as_expr() - expected_symmetric(residue, t)) != 0:
            return result("SYMMETRIC SECTOR (mod 4)", False, f"mismatch at m=={residue} (mod 4)")
    return result("SYMMETRIC SECTOR (mod 4)", True, "m=1,3->Phi6; m=2->Phi4; m=0->(t-1)^2 (symbolic m per class)")


def check_antisymmetric_charM() -> CheckResult:
    m, t = sp.symbols("m t")
    expected = sp.expand((t - 1) * (t + 1) * (t**2 - m * t - 1))
    for residue in range(4):
        _, anti = _sectors(jacobian_symbolic_class(residue, m))
        if sp.expand(anti.charpoly(t).as_expr() - expected) != 0:
            return result("ANTISYMMETRIC SECTOR (char(M), all m)", False, f"mismatch at m=={residue} (mod 4)")
    return result("ANTISYMMETRIC SECTOR (char(M), all m)", True, "(t-1)(t+1)(t^2-mt-1) for every residue class")


def check_numerical_cross_check(max_m: int = 12) -> CheckResult:
    t = sp.symbols("t")
    for m_value in range(1, max_m + 1):
        sym, anti = _sectors(jacobian_integer(m_value))
        if sp.expand(sym.charpoly(t).as_expr() - expected_symmetric(m_value, t)) != 0:
            return result("NUMERICAL CROSS-CHECK m=1..12", False, f"symmetric mismatch at m={m_value}")
        anti_expected = sp.expand((t - 1) * (t + 1) * (t**2 - m_value * t - 1))
        if sp.expand(anti.charpoly(t).as_expr() - anti_expected) != 0:
            return result("NUMERICAL CROSS-CHECK m=1..12", False, f"antisymmetric mismatch at m={m_value}")
    return result("NUMERICAL CROSS-CHECK m=1..12", True, "direct integer-m Jacobian matches the symbolic proof")


def check_b54_c1_regression() -> CheckResult:
    t = sp.symbols("t")
    sym, anti = _sectors(jacobian_integer(1))
    eisenstein_ok = sp.rem(sym.charpoly(t).as_expr(), t**2 - t + 1, t) == 0
    golden_ok = sp.rem(anti.charpoly(t).as_expr(), t**2 - t - 1, t) == 0
    if not (eisenstein_ok and golden_ok):
        return result("B54 c=1 REGRESSION", False, "m=1 twins not reproduced")
    return result("B54 c=1 REGRESSION", True, "m=1 reproduces B54's Eisenstein/golden twins")


def run_checks() -> list[CheckResult]:
    return [
        check_period_structure(),
        check_symmetric_mod4(),
        check_antisymmetric_charM(),
        check_numerical_cross_check(),
        check_b54_c1_regression(),
    ]


def main() -> int:
    print("B55 -- c=1 FIXED-LINE STRUCTURE (metallic SL(3) trace map, general m)")
    print("Status: standalone trace-map math; no claim promotion")
    print()
    checks = run_checks()
    for item in checks:
        print_result(item)
    ok = all(item.ok for item in checks)
    print()
    print(f"B55 c=1 STRUCTURE: {'OK' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
