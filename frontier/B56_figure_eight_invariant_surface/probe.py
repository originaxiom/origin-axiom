"""B56 -- figure-eight invariant-surface negative control.

Standalone trace-map mathematics. This probe is a NEGATIVE control. It tests the
hoped-for bridge that the figure-eight knot would sit on the self-evidencing
invariant surface I = 1/4 (the m=1 value of I = m^2/4), via the diagonal
SL(2,C) representation locus x = y = z = w, and via the resemblance between the
c=1 symmetric-sector Eisenstein factor (B55) and the figure-eight ideal
tetrahedron shape.

Result: the bridge is DEAD.

  * The diagonal locus cubic w^3 - 2w^2 - 2w + 1 = (w+1)(w^2-3w+1) has roots
    w in {-1, phi^2, phi^-2}. On the Fricke-Vogt surface the diagonal invariant
    is I = 3w^2 - 2w^3 - 1, giving I in {4, -17/2 + 7*sqrt(5)/2, -17/2 - 7*sqrt(5)/2}.
    NONE equals 1/4.
  * The two irrational I-values multiply to the clean integer 11 -- ordinary
    algebra of Q(sqrt(5)), not a structural coincidence with 1/4.
  * The figure-eight ideal tetrahedron shape solves z^2 - z + 1 = 0 (root
    e^{i*pi/3}, discriminant -3, trace field Q(sqrt(-3))) -- a COMPLEX point,
    disjoint from the real diagonal locus above. The c=1 symmetric Eisenstein
    factor (B55) is the same polynomial only because Phi_6 = t^2 - t + 1 is the
    simplest discriminant -3 cyclotomic; the coincidence is cyclotomic, not an
    invariant-surface connection.

Scope guard: this does NOT touch the separate, real fact that the c=1 twins'
discriminant pair (-3, 5) matches the factors of the figure-eight gluing
equation z^2(z-1)^2 = (z^2-z+1)(z^2-z-1) (claim P12). That is a gluing-equation
echo, recorded as such; it is the holonomy-on-I=1/4 bridge that is dead.

No physics dictionary, no Origin-core claim. The self-evidencing / I=1/4 framing
is quarantined in paths/E21_self_evidencing_closure/.
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


def diagonal_cubic(w: sp.Symbol) -> sp.Expr:
    return w**3 - 2 * w**2 - 2 * w + 1


def diagonal_invariant(w: sp.Expr) -> sp.Expr:
    """Fricke-Vogt invariant I = x^2+y^2+z^2-2xyz-1 on the diagonal x=y=z=w."""
    return sp.simplify(3 * w**2 - 2 * w**3 - 1)


def check_diagonal_reps_miss_quarter() -> CheckResult:
    w = sp.symbols("w")
    roots = sp.roots(diagonal_cubic(w))
    invariants = [sp.radsimp(diagonal_invariant(r)) for r in roots]
    if any(sp.simplify(value - sp.Rational(1, 4)) == 0 for value in invariants):
        return result("DIAGONAL REPS MISS I=1/4", False, "some diagonal representation has I=1/4")
    detail = "roots w in {-1, phi^2, phi^-2}; I in {4, -17/2 +/- 7 sqrt5/2}; none = 1/4"
    return result("DIAGONAL REPS MISS I=1/4", True, detail)


def check_irrational_pair_product() -> CheckResult:
    w = sp.symbols("w")
    roots = list(sp.roots(diagonal_cubic(w)))
    irrational = [sp.radsimp(diagonal_invariant(r)) for r in roots if sp.simplify(sp.im(r)) == 0 and r != -1]
    product = sp.simplify(sp.prod(irrational))
    if sp.simplify(product - 11) != 0:
        return result("IRRATIONAL I-PAIR PRODUCT = 11", False, f"product = {product}")
    return result("IRRATIONAL I-PAIR PRODUCT = 11", True, "(-17/2)^2 - (7 sqrt5/2)^2 = 11 (plain Q(sqrt5) algebra)")


def check_eisenstein_coincidence() -> CheckResult:
    z = sp.symbols("z")
    shape = z**2 - z + 1  # figure-eight ideal tetrahedron shape
    disc = sp.discriminant(shape, z)
    shape_roots_complex = all(sp.simplify(sp.im(r)) != 0 for r in sp.roots(shape))
    # the diagonal locus is real; the geometric shape is complex -> disjoint
    if disc != -3 or not shape_roots_complex:
        return result("EISENSTEIN IS A CYCLOTOMIC COINCIDENCE", False, "shape not the disc -3 complex cyclotomic")
    return result(
        "EISENSTEIN IS A CYCLOTOMIC COINCIDENCE",
        True,
        "fig-8 shape z^2-z+1 is complex (disc -3, Q(sqrt-3)); c=1 Eisenstein is the same Phi_6 by coincidence",
    )


def run_checks() -> list[CheckResult]:
    return [
        check_diagonal_reps_miss_quarter(),
        check_irrational_pair_product(),
        check_eisenstein_coincidence(),
    ]


def main() -> int:
    print("B56 -- FIGURE-EIGHT INVARIANT-SURFACE NEGATIVE CONTROL")
    print("Status: negative control; the holonomy-on-I=1/4 bridge is DEAD; no claim")
    print()
    checks = run_checks()
    for item in checks:
        print_result(item)
    ok = all(item.ok for item in checks)
    print()
    print(f"B56 NEGATIVE CONTROL: {'OK' if ok else 'FAIL'}  (verdict: bridge DEAD)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
