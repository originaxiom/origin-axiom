"""B57 -- general-m Diophantine splitting classification.

Standalone trace-map mathematics. This probe classifies the integer values of the
fixed-line parameter c at which the antisymmetric-sector quartic of the metallic
SL(3) trace-map Jacobian splits into two integer quadratics, for m = 1..6. It
generalizes B51's c=3 Diophantine observation (the lone APPARENTLY_NEW block of
the PC12 literature screen) to the metallic family.

The antisymmetric quartic has the form
    chi(t) = t^4 - A(m,c) t^3 + C(m,c) t^2 + A(m,c) t + 1,
and splits over Z as (t^2 - alpha t - 1)(t^2 - beta t - 1) with alpha, beta in Z
iff D = A^2 - 4(C+2) is a perfect square and A + sqrt(D) is even (so that
alpha, beta = (A +/- sqrt(D))/2 are integers).

Results (scan c in -120..120):
    m=1: c in {-11, -9, 1, 3}
    m=2: c in {-3, -1, 1, 3}
    m=3: c in {-3, 0, 1, 3}
    m=4: c in {-1, 1, 3}
    m=5: c in {1, 3}
    m=6: c in {-1, 0, 1, 2, 3}
c = 1 and c = 3 are universal splitting points; the extra points are
m-dependent and the count varies (2..5), with no class-number law (see FINDINGS:
the Hilbert-class-field coincidence for m=1 is killed).

No physics dictionary, no Origin-core claim. Coordinate convention follows
B48/B51/B54/B55.
"""

from __future__ import annotations

import math
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


def _exchange() -> sp.Matrix:
    pairs = {0: 3, 3: 0, 1: 4, 4: 1, 2: 7, 7: 2, 5: 6, 6: 5}
    matrix = sp.zeros(8)
    for source, target in pairs.items():
        matrix[target, source] = 1
    return matrix


def _tau_rows(c: sp.Expr, max_k: int) -> dict[int, sp.Matrix]:
    rows = {-1: _unit(5), 0: _unit(1), 1: _unit(2)}
    forcing = c * (_unit(0) - _unit(3))
    for k in range(2, max_k + 1):
        rows[k] = sp.expand(c * rows[k - 1] - c * rows[k - 2] + rows[k - 3] + forcing)
    return rows


def _jacobian(m_value: int, c: sp.Expr) -> sp.Matrix:
    exchange = _exchange()
    tau = _tau_rows(c, m_value + 1)
    sigma = {k: exchange * tau[k] for k in tau}
    rows = [
        tau[m_value], _unit(0), tau[m_value + 1], sigma[m_value],
        _unit(3), sigma[m_value - 1], tau[m_value - 1], sigma[m_value + 1],
    ]
    return sp.Matrix.hstack(*rows).T


def _antisymmetric_sector(m_value: int, c: sp.Expr) -> sp.Matrix:
    jacobian = _jacobian(m_value, c)
    pairs = [(0, 3), (1, 4), (2, 7), (5, 6)]
    columns = []
    for left, right in pairs:
        v = sp.zeros(8, 1); v[left] = 1; v[right] = 1; columns.append(v)
    for left, right in pairs:
        v = sp.zeros(8, 1); v[left] = 1; v[right] = -1; columns.append(v)
    basis = sp.Matrix.hstack(*columns)
    return sp.simplify((basis.inv() * jacobian * basis)[4:, 4:])


def antisymmetric_quartic_coeffs(m_value: int):
    """Return (A(c), C(c)) and a form-check flag for chi = t^4 - A t^3 + C t^2 + A t + 1."""
    c, t = sp.symbols("c t")
    quartic = sp.expand(_antisymmetric_sector(m_value, c).charpoly(t).as_expr())
    poly = sp.Poly(quartic, t)
    lead, a3, a2, a1, a0 = (poly.coeff_monomial(t**i) for i in range(4, -1, -1))
    A = sp.simplify(-a3)
    C = sp.simplify(a2)
    form_ok = lead == 1 and a0 == 1 and sp.simplify(a1 - A) == 0
    return A, C, form_ok


def splitting_points(m_value: int, lo: int = -120, hi: int = 120) -> list[int]:
    c = sp.symbols("c")
    A, C, _ = antisymmetric_quartic_coeffs(m_value)
    discriminant = sp.expand(A**2 - 4 * (C + 2))
    points = []
    for c_value in range(lo, hi + 1):
        d_value = int(discriminant.subs(c, c_value))
        a_value = int(A.subs(c, c_value))
        if d_value < 0:
            continue
        root = math.isqrt(d_value)
        if root * root == d_value and (a_value + root) % 2 == 0:
            points.append(c_value)
    return points


EXPECTED = {
    1: [-11, -9, 1, 3],
    2: [-3, -1, 1, 3],
    3: [-3, 0, 1, 3],
    4: [-1, 1, 3],
    5: [1, 3],
    6: [-1, 0, 1, 2, 3],
}


def check_quartic_form() -> CheckResult:
    for m_value in range(1, 7):
        _, _, form_ok = antisymmetric_quartic_coeffs(m_value)
        if not form_ok:
            return result("ANTISYM QUARTIC FORM", False, f"not palindromic at m={m_value}")
    return result("ANTISYM QUARTIC FORM", True, "t^4 - A t^3 + C t^2 + A t + 1 for m=1..6")


def check_universal_splitting() -> CheckResult:
    for m_value in range(1, 7):
        points = splitting_points(m_value)
        if 1 not in points or 3 not in points:
            return result("UNIVERSAL SPLITTING c=1,c=3", False, f"missing at m={m_value}")
    return result("UNIVERSAL SPLITTING c=1,c=3", True, "c=1 and c=3 split for every m=1..6")


def check_classification() -> CheckResult:
    for m_value in range(1, 7):
        points = splitting_points(m_value)
        if points != EXPECTED[m_value]:
            return result("SPLITTING CLASSIFICATION", False, f"m={m_value}: {points} != {EXPECTED[m_value]}")
    return result("SPLITTING CLASSIFICATION", True, "integer splitting sets match for m=1..6 (scan -120..120)")


def check_counts_vary_no_class_number_law() -> CheckResult:
    counts = {m_value: len(splitting_points(m_value)) for m_value in range(1, 7)}
    if len(set(counts.values())) == 1:
        return result("COUNTS VARY (no class-number law)", False, "counts constant")
    return result(
        "COUNTS VARY (no class-number law)",
        True,
        f"|splitting set| = {[counts[m] for m in range(1,7)]} (varies; Hilbert-class-field coincidence killed)",
    )


def run_checks() -> list[CheckResult]:
    return [
        check_quartic_form(),
        check_universal_splitting(),
        check_classification(),
        check_counts_vary_no_class_number_law(),
    ]


def main() -> int:
    print("B57 -- GENERAL-m DIOPHANTINE SPLITTING CLASSIFICATION")
    print("Status: standalone trace-map math; no claim promotion")
    print()
    checks = run_checks()
    for item in checks:
        print_result(item)
    ok = all(item.ok for item in checks)
    print()
    print(f"B57 SPLITTING CLASSIFICATION: {'OK' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
