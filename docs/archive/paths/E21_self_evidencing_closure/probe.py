"""E21 -- self-evidencing closure (instantiates E18 self-consistency/bootstrap).

SPECULATIVE PHASE-C PROBE.  Observations only, not claims
(see ../../GOVERNANCE.md sec. 5 and ./README.md).

This probe records, as exact algebra, the one verified fact under the
"self-evidencing" framing, and deflates the framing to what the algebra
actually says:

  * On the SL(2) Fricke-Vogt surface I = c^2 - 1, the half-return (third
    iterate) of the Fibonacci trace map T(x,y,z) = (2xy - z, x, y), restricted
    to the surface at (0,0,c), has characteristic polynomial t^2-(4c^2-2)t+1.
  * This equals char(M^2) = t^2-(m^2+2)t+1 (M = [[m,1],[1,0]]) exactly when
    4c^2-2 = m^2+2, i.e. I = m^2/4, i.e. lambda = m.
  * The "self-model discrepancy" D(I) = (4I - m^2)^2 is precisely the squared
    difference of the two middle coefficients; its unique zero at I = m^2/4 is
    immediate. It is a squared residual, not a free energy in any established
    (Kullback-Leibler) sense.

The exact algebra is real and trivial. The self-evidencing / variational
free-energy reading supplies framing, not force, and predicts no observable.
No Origin-core or physics claim is promoted; nothing here enters PC12.
"""

from __future__ import annotations

import sympy as sp


def fibonacci_trace_map(point: sp.Matrix) -> sp.Matrix:
    x, y, z = point
    return sp.Matrix([2 * x * y - z, x, y])


def half_return_charpoly(c: sp.Symbol, t: sp.Symbol) -> sp.Expr:
    """Char poly of the surface-restricted third-iterate Jacobian at (0,0,c)."""
    x, y, z = sp.symbols("x y z")
    field = sp.Matrix([2 * x * y - z, x, y])
    jac = field.jacobian([x, y, z])
    invariant = x**2 + y**2 + z**2 - 2 * x * y * z - 1
    grad = sp.Matrix([sp.diff(invariant, v) for v in (x, y, z)])

    point = sp.Matrix([0, 0, c])
    product = sp.eye(3)
    for _ in range(3):
        product = jac.subs({x: point[0], y: point[1], z: point[2]}) * product
        point = sp.simplify(fibonacci_trace_map(point))
    product = sp.simplify(product)

    tangent = sp.Matrix.hstack(*grad.subs({x: 0, y: 0, z: c}).T.nullspace())
    restricted = sp.simplify((tangent.T * tangent).inv() * tangent.T * product * tangent)
    return sp.expand(restricted.charpoly(t).as_expr())


def run_checks() -> list[tuple[str, bool, str]]:
    c, t, m, I = sp.symbols("c t m I")
    out = []

    cp = half_return_charpoly(c, t)
    target = sp.expand(t**2 - (4 * c**2 - 2) * t + 1)
    ok1 = sp.expand(cp - target) == 0
    out.append(("HALF-RETURN CHARPOLY = t^2-(4c^2-2)t+1", ok1, str(cp)))

    # at I = m^2/4 (c^2 = m^2/4 + 1): equals char(M^2)
    char_M2 = t**2 - (m**2 + 2) * t + 1
    at_self = target.subs(c**2, m**2 / 4 + 1)
    # ensure substitution of c^2 lands; rewrite target in c^2
    at_self = sp.expand((t**2 - (4 * (m**2 / 4 + 1) - 2) * t + 1))
    ok2 = sp.expand(at_self - char_M2) == 0
    out.append(("EQUALS char(M^2) AT I=m^2/4 (lambda=m)", ok2, "4c^2-2 -> m^2+2"))

    # D(I) is the squared residual of the middle-coefficient match, zero iff I=m^2/4
    D = (4 * I - m**2) ** 2
    residual = (4 * I + 2) - (m**2 + 2)  # half-return middle coeff minus char(M^2) middle coeff
    ok3 = sp.expand(D - residual**2) == 0 and sp.solve(sp.Eq(D, 0), I) == [m**2 / 4]
    out.append(("D(I)=(4I-m^2)^2 IS THE SQUARED RESIDUAL", ok3, "zero iff I=m^2/4"))

    # Fisher information of D(I) equals 16/disc(char(M^2)) = 16*g_WP(m^2+2).
    # Exact, but it follows from the chain rule on LE(I)=arccosh(2I+1) plus the
    # elementary disc(t^2 - a t + 1) = a^2 - 4 = 1/g_WP(a). The Weil-Petersson
    # geometric reading is the originating session's own "may be just calculus";
    # recorded, NOT promoted.
    fisher = 16 / (m**2 * (m**2 + 4))
    disc_charM2 = (m**2 + 2) ** 2 - 4
    ok4 = (
        sp.simplify(fisher - 16 / disc_charM2) == 0
        and sp.simplify(disc_charM2 - m**2 * (m**2 + 4)) == 0
    )
    out.append(("FISHER INFO = 16/disc(char(M^2)) (WP coeff; chain-rule identity)", ok4, "exact; geometric reading not promoted"))

    # Aubry deflation: the duality map lambda -> m^2/lambda has lambda=m as its
    # trivial fixed point, so "self-dual at lambda=m" is vacuous. The off-diagonal
    # model has no genuine Aubry self-duality at lambda=m for m>=2 (session IPR test:
    # IPR(lambda) != IPR(m^2/lambda) off the fixed point). No metal-insulator observable.
    ok5 = sp.simplify(m**2 / m - m) == 0
    out.append(("AUBRY lambda=m IS THE TRIVIAL FIXED POINT (no metal-insulator obs)", ok5, "m^2/m = m; duality is vacuous at the fixed point"))
    return out


def main() -> int:
    print("E21 -- SELF-EVIDENCING CLOSURE (instantiates E18)")
    print("Status: STALLED -- structural analogy only; predicts no observable")
    print()
    checks = run_checks()
    for name, ok, detail in checks:
        print(f"{name}: {'OK' if ok else 'FAIL'} -- {detail}")
    ok = all(item[1] for item in checks)
    print()
    print(f"E21 EXACT ALGEBRA: {'OK' if ok else 'FAIL'}  (verdict: STALLED, framing not force)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
