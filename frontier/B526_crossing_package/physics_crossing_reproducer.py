#!/usr/bin/env python3
"""Exact structural calculations for the Origin Axiom physics-crossing program.

This script establishes:

1. the canonical frequency-weighted tetrahedral metric on the three-dimensional
   quotient of the four-letter Perron space;
2. the exact incompatibility between that local-isotropy metric and a positive
   one-step Stein driver for the substitution matrix;
3. the correct renormalization interpretation of the stable eigenmodes;
4. exact correction-to-scaling exponents and log-periodic frequency.

No physical claim is made by the script itself.
"""

from __future__ import annotations

import math
import sympy as sp


# ---------------------------------------------------------------------------
# Forced four-letter object
# ---------------------------------------------------------------------------

M = sp.Matrix([
    [1, 1, 1, 1],
    [1, 0, 1, 0],
    [2, 1, 1, 1],
    [1, 1, 1, 0],
])

phi = (1 + sp.sqrt(5)) / 2
sqrt_phi = sp.sqrt(phi)

beta = sp.simplify(phi * (1 + sqrt_phi))
heartbeat = sp.simplify(phi * (1 - sqrt_phi))
gamma = sp.simplify(-1 / phi + sp.I * sp.sqrt(sp.sqrt(5) - 2))
gamma_modulus = sp.simplify(1 / sp.sqrt(phi))

# Right Perron vector already banked in B517.
r = sp.Matrix([phi, 1, phi * sqrt_phi, sqrt_phi])

# Left Perron vector, normalized by ell^T r = 1.
ell_symbols = sp.symbols("ell0:4")
ell_unknown = sp.Matrix(ell_symbols)
ell_solution = sp.solve(
    list((M.T - beta * sp.eye(4)) * ell_unknown)
    + [sp.expand((ell_unknown.T * r)[0] - 1)],
    ell_symbols,
    dict=True,
)[0]
ell = sp.Matrix([sp.simplify(ell_solution[symbol]) for symbol in ell_symbols])


# ---------------------------------------------------------------------------
# Canonical tetrahedral quotient metric
# ---------------------------------------------------------------------------

D = sp.diag(*r)

# Gram matrix of four centered regular-tetrahedron vertices:
# diagonal 3/4, off-diagonal -1/4, kernel span{(1,1,1,1)}.
C_TETRA = sp.eye(4) - sp.ones(4) / 4

# Pullback form on R^4.  It has kernel span{r}.  The weighted quotient vectors
# d_i = r_i [e_i] have Gram matrix C_TETRA exactly.
S_TETRA = sp.simplify(D.inv() * C_TETRA * D.inv())


def weighted_direction(index: int) -> sp.Matrix:
    basis = sp.eye(4)[:, index]
    return sp.simplify(r[index] * basis)


def weighted_gram() -> sp.Matrix:
    directions = [weighted_direction(index) for index in range(4)]
    return sp.Matrix([
        [sp.simplify((left.T * S_TETRA * right)[0]) for right in directions]
        for left in directions
    ])


# ---------------------------------------------------------------------------
# Canonical invariant-splitting Lorentzian extension
# ---------------------------------------------------------------------------

# The stable space is ker(ell^T); r is the canonical time line.
# This is the unique extension with:
#   - spatial quotient metric S_TETRA,
#   - r orthogonal to ker(ell^T),
#   - G(r,r) = -1.
G_ISO = sp.simplify(S_TETRA - ell * ell.T)

# If substitution iteration were microscopic time with a strict positive
# Stein driver, this matrix would need to be positive definite:
W_ISO = sp.simplify(G_ISO - M.T * G_ISO * M)


def leading_principal_minors(matrix: sp.Matrix) -> list[sp.Expr]:
    return [
        sp.factor(matrix[:size, :size].det())
        for size in range(1, matrix.rows + 1)
    ]


def signs(expressions: list[sp.Expr]) -> list[int]:
    output: list[int] = []
    for expression in expressions:
        if expression.is_positive:
            output.append(1)
        elif expression.is_negative:
            output.append(-1)
        elif expression.is_zero:
            output.append(0)
        else:
            raise ValueError(f"Could not determine exact sign: {expression}")
    return output


# An exact basis of the stable hyperplane ker(ell^T).
STABLE_BASIS = sp.Matrix.hstack(*[
    ell[index] * sp.eye(4)[:, 0] - ell[0] * sp.eye(4)[:, index]
    for index in (1, 2, 3)
])

W_STABLE = sp.simplify(
    STABLE_BASIS.T
    * (S_TETRA - M.T * S_TETRA * M)
    * STABLE_BASIS
)


# ---------------------------------------------------------------------------
# Renormalization modes
# ---------------------------------------------------------------------------

omega_heartbeat = sp.simplify(-sp.log(sp.Abs(heartbeat)) / sp.log(beta))
omega_breath = sp.simplify(-sp.log(gamma_modulus) / sp.log(beta))
theta_breath = sp.arg(gamma)
log_angular_frequency = sp.simplify(theta_breath / sp.log(beta))
log_period = sp.simplify(2 * sp.pi / log_angular_frequency)
scale_ratio_per_breath_cycle = sp.simplify(sp.exp(log_period))


def normalized_breath_minpoly() -> sp.Expr:
    z = sp.symbols("z")
    normalized = sp.simplify(gamma / gamma_modulus)
    return sp.factor(sp.minimal_polynomial(normalized, z))


def is_breath_cyclotomic() -> bool:
    polynomial = normalized_breath_minpoly()
    z = next(iter(polynomial.free_symbols))
    # Euler phi(n)=8 exactly for these n.
    return any(
        sp.expand(polynomial - sp.cyclotomic_poly(index, z)) == 0
        for index in (15, 16, 20, 24, 30)
    )


def conformal_scalar_for_tetra_metric() -> sp.Expr | None:
    scalar = sp.symbols("c")
    equations = list(M.T * S_TETRA * M - scalar * S_TETRA)
    solution = sp.solve(equations, [scalar], dict=True)
    if not solution:
        return None
    return sp.simplify(solution[0][scalar])


def main() -> None:
    x = sp.symbols("x")

    print("=== Forced four-letter object ===")
    print("charpoly:", sp.factor(M.charpoly(x).as_expr()))
    print("det:", M.det())
    print("M r = beta r:", sp.simplify(M * r - beta * r) == sp.zeros(4, 1))
    print("ell^T M = beta ell^T:", sp.simplify(ell.T * M - beta * ell.T) == sp.zeros(1, 4))
    print("ell^T r:", sp.simplify((ell.T * r)[0]))

    print("\n=== Canonical tetrahedral quotient metric ===")
    print("rank(S_tetra):", S_TETRA.rank())
    print("S_tetra r = 0:", sp.simplify(S_TETRA * r) == sp.zeros(4, 1))
    print("weighted Gram equals regular tetrahedron:", weighted_gram() == C_TETRA)
    print("M conformal for tetrahedral metric:", conformal_scalar_for_tetra_metric())

    print("\n=== Isotropy / Stein incompatibility ===")
    print("G_iso leading-minor signs:", signs(leading_principal_minors(G_ISO)))
    print("W_iso leading-minor signs:", signs(leading_principal_minors(W_ISO)))
    print("stable W leading-minor signs:", signs(leading_principal_minors(W_STABLE)))
    print("det(W_stable) < 0:", W_STABLE.det().is_negative)
    print("Conclusion: no positive Stein driver for the isotropic metric.")

    print("\n=== Exact renormalization modes ===")
    print("beta =", beta, "≈", sp.N(beta, 16))
    print("heartbeat eigenvalue =", heartbeat, "≈", sp.N(heartbeat, 16))
    print("gamma =", gamma, "≈", sp.N(gamma, 16))
    print("|gamma| =", gamma_modulus, "≈", sp.N(gamma_modulus, 16))
    print("omega_h =", sp.N(omega_heartbeat, 16))
    print("omega_gamma =", sp.N(omega_breath, 16))
    print("theta/pi =", sp.N(theta_breath / sp.pi, 16))
    print("log angular frequency =", sp.N(log_angular_frequency, 16))
    print("log period =", sp.N(log_period, 16))
    print("scale ratio per complex cycle =", sp.N(scale_ratio_per_breath_cycle, 16))
    print("breath phase minpoly =", normalized_breath_minpoly())
    print("breath phase cyclotomic:", is_breath_cyclotomic())


if __name__ == "__main__":
    main()
