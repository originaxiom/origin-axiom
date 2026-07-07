#!/usr/bin/env python3
"""B469 BR-N — the norm identity (the owner's sentence, 2026-07-08, as three exact
statements):

  "the smallest residue that can't cancel is the norm of the scale, frozen at -1
   across the entire family, living on the golden axis alone."

(a) THE RESIDUE IS THE NORM OF THE SCALE: the metallic mean lambda_m satisfies
    x^2 - m x - 1, so N(lambda_m) = -1 = det(X_m) — the half-monodromy X_m =
    [[m,1],[1,0]] is the COMPANION MATRIX of the scale's minimal polynomial; the
    orientation bit (BR2) and the field norm of the scaling unit are the same -1.
(b) FROZEN ACROSS THE FAMILY: for all m symbolically; and it survives the
    same-field degeneracy — the Q(sqrt5) members m = 1, 4, 11, 29 are exactly
    phi^{1,3,5,7} (ODD powers of the fundamental unit; banked L16 Pell sub-lead),
    so N = (-1)^odd = -1 even where lambda_m is a proper power. The full
    monodromy A_m = X_m^2 has det = N(lambda_m^2) = +1: the orientable cover
    carries norm +1; the residue lives on the HALF (the Gieseking floor).
(c) ON THE GOLDEN (REAL/SCALE) AXIS ALONE: in an imaginary quadratic field the
    norm form a^2 + d b^2 is positive definite — a unit of norm -1 is
    IMPOSSIBLE. The residue's norm-realization structurally cannot live on the
    geometry end (sqrt-3, sqrt-7, sqrt-15); only the scale end can carry it.

Adjudication: all three are classical algebra (companion determinant; odd Pell
indices; positive definiteness) — LAUNDERS, banked as the exact exhibit. The
identity ties BR2's topology (the double cover) to unit arithmetic: norm -1 of
the scale <=> det -1 of the half-monodromy <=> the non-orientable quotient exists.
"""
import sys

import sympy as sp


def main():
    ok = True
    m = sp.Symbol('m', positive=True, integer=True)
    x = sp.Symbol('x')
    lam = (m + sp.sqrt(m * m + 4)) / 2
    ok &= sp.simplify(lam**2 - m * lam - 1) == 0
    X = sp.Matrix([[m, 1], [1, 0]])
    ok &= sp.expand(X.charpoly(x).as_expr() - (x**2 - m * x - 1)) == 0
    ok &= X.det() == -1
    print("(a) N(lambda_m) = -1 = det(X_m), X_m = companion(scale):", ok)
    A = X * X
    ok2 = A.det() == 1
    ok &= ok2
    print("(b1) the cover A_m = X_m^2 has det = N(lambda_m^2) = +1:", ok2)
    phi = (1 + sp.sqrt(5)) / 2
    for mm, k in [(1, 1), (4, 3), (11, 5), (29, 7)]:
        lm = (mm + sp.sqrt(mm * mm + 4)) / 2
        hit = sp.simplify(lm - phi**k) == 0 and (-1)**k == -1
        ok &= hit
        print(f"(b2) m={mm}: lambda = phi^{k} (odd) -> N = -1 through the degeneracy: {hit}")
    a, b, d = sp.symbols('a b d', positive=True)
    # imaginary norm form: positive definite (definitional; exhibited)
    ok3 = sp.ask(sp.Q.positive(a**2 + d * b**2)) is True
    ok &= ok3
    print("(c) imaginary quadratic norm form positive definite -> norm -1 impossible:", ok3)
    print("ALL CHECKS PASS" if ok else "CHECK FAILURE")
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
