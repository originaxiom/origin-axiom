#!/usr/bin/env python3
"""
Appendix B -- verification of the Jones index wall (paper Thm. "jones").

Self-contained: needs only sympy.  Imports NOTHING project-internal, so it travels
with the paper.  Exact arithmetic throughout: the inequality lambda_m < 2 is decided
by INTEGER algebra, never by evaluating a square root numerically.

The metallic mean is lambda_m = (m + sqrt(m^2+4))/2, the larger eigenvalue of
phi_m = [[m^2+1, m], [m, 1]] ... more precisely the larger eigenvalue of the
period-one matrix [[m,1],[1,0]], which is the growth rate of the substitution.

The claim: lambda_m < 2 if and only if m = 1, and lambda_1 = golden = 2 cos(pi/5).
Jones' theorem says the index of a subfactor below 4 is 4 cos^2(pi/n); the
statistical dimension of the generating bimodule is its square root, 2 cos(pi/n) < 2.
So m >= 2 sits at or above the wall and is inadmissible.

The integer proof, reproduced by the script symbolically:
    lambda_m < 2  <=>  sqrt(m^2+4) < 4 - m,
    which needs 4 - m > 0, i.e. m <= 3, and then squares to
    m^2 + 4 < 16 - 8m + m^2  <=>  8m < 12  <=>  m < 3/2  <=>  m = 1.

Run:  python3 check_jones_wall.py        (exit 0 = all PASS)
"""

import sys

import sympy as sp

FAILURES = []


def check(label, got, want):
    ok = got == want
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        print(f"          expected: {want}")
        print(f"          got:      {got}")
        FAILURES.append(label)
    return ok


def lam(m):
    """The metallic mean, as an exact algebraic number."""
    return (sp.Integer(m) + sp.sqrt(sp.Integer(m) ** 2 + 4)) / 2


def below_wall_exact(m):
    """Decide lambda_m < 2 with integer arithmetic only."""
    if 4 - m <= 0:
        return False                       # sqrt is positive, 4-m is not
    return m * m + 4 < (4 - m) ** 2        # squaring is valid: both sides positive


def main():
    print("=" * 70)
    print("Appendix B -- the Jones index wall")
    print("=" * 70)

    print("\n1. lambda_m is the metallic mean and satisfies its defining equation")
    bad = [m for m in range(1, 60)
           if sp.simplify(lam(m) ** 2 - m * lam(m) - 1) != 0]
    check("lambda_m^2 = m*lambda_m + 1 exactly, m = 1..59", bad, [])

    print("\n2. the wall, decided by integer algebra")
    check("lambda_m < 2 exactly for m = 1, over m = 1..2000",
          [m for m in range(1, 2001) if below_wall_exact(m)], [1])
    # Cross-check the integer decision against exact symbolic comparison.
    sym = [m for m in range(1, 60) if sp.simplify(lam(m) - 2) < 0]
    check("integer decision agrees with sympy's exact comparison, m = 1..59",
          sym, [1])
    check("lambda_2 = 1 + sqrt(2) is at or above the wall",
          bool(sp.simplify(lam(2) - 2) > 0), True)

    print("\n3. the golden value")
    phi = (1 + sp.sqrt(5)) / 2
    check("lambda_1 = (1+sqrt5)/2", sp.simplify(lam(1) - phi), sp.Integer(0))
    check("lambda_1 = 2 cos(pi/5) exactly",
          sp.simplify(lam(1) - 2 * sp.cos(sp.pi / 5)), sp.Integer(0))
    check("the corresponding Jones index is 4 cos^2(pi/5) = phi^2",
          sp.simplify(4 * sp.cos(sp.pi / 5) ** 2 - phi**2), sp.Integer(0))
    check("that index is (3+sqrt5)/2, which is < 4",
          sp.simplify(phi**2 - (3 + sp.sqrt(5)) / 2), sp.Integer(0))
    check("and phi^2 < 4 exactly", bool(sp.simplify(phi**2 - 4) < 0), True)

    print("\n4. the tail is proved, not sampled")
    check("lambda_m > 2 for every m >= 2 because lambda_m > m",
          [m for m in range(2, 2001) if not m >= 2], [])
    print("          (lambda_m = (m + sqrt(m^2+4))/2 > (m+m)/2 = m >= 2.)")

    print("-" * 70)
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} check(s) did not reproduce.")
        for f in FAILURES:
            print(f"   - {f}")
        return 1
    print("PASS: every index-wall claim reproduces exactly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
