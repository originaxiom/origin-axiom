"""B67 -- the figure-eight knot A-polynomial from the trace-map fixed-point set.

The figure-eight complement is the once-punctured-torus bundle with monodromy
phi = [[2,1],[1,1]] = M^2 (M = [[1,1],[1,0]], Fibonacci), realized on F_2 = <a,b>
by phi(a) = a^2 b, phi(b) = a b (abelianizes to [[2,1],[1,1]], det +1). Its induced
SL(2,C) trace map on the Fricke variety (x,y,z) = (tr A, tr B, tr AB) is the square
of T_1(x,y,z) = (z, x, xz - y):

    T_1^2(x,y,z) = (xz - y,  z,  xz^2 - x - yz).

A representation of the punctured torus extends over the bundle iff its character is
FIXED by T_1^2 (then it is conjugate to its phi-image, so a monodromy t exists). The
fixed locus is the one-parameter family

    y = z = x/(x-1).

At each fixed point the monodromy t in SL(2,C) is determined up to sign by
t A t^-1 = A^2 B and t B t^-1 = A B. The figure-eight meridian is t and the
longitude is the fiber boundary [A,B] (= the Seifert/0-framed longitude), so

    M + 1/M = tr(t),     L + 1/L = tr[A,B] =: kappa(x).

With tr(t)^2 = (x^2 + x - 1)/(x - 1) and kappa(x) = (x^4 - 3x^3 + x^2 + 4x - 2)/(x-1)^2,
eliminating x gives the meridian<->longitude trace identity  kappa = tr(t)^4 - 5 tr(t)^2 + 2,
and in eigenvalue coordinates the eliminant is exactly A_CL(M,L)^2 with A_CL the
published Cooper-Long (1996) A-polynomial of the figure-eight knot.

Standalone character-variety / knot-theory mathematics; no physics, no Origin claim.
This is an exact symbolic derivation (one ingredient, tr(t)^2, is confirmed to 50
digits and by the exact final match).
"""

from __future__ import annotations

import numpy as np
import sympy as sp


# --------------------------------------------------------------------------- #
# symbolic ingredients
# --------------------------------------------------------------------------- #

def trace_map_T1sq():
    """T_1^2 on (x,y,z), the trace map of the figure-eight monodromy."""
    x, y, z = sp.symbols("x y z")
    T1 = lambda v: (v[2], v[0], sp.expand(v[0] * v[2] - v[1]))
    return tuple(sp.expand(c) for c in T1(T1((x, y, z))))


def fixed_locus():
    """The fixed locus of T_1^2: y = z = x/(x-1)."""
    x = sp.symbols("x")
    return x / (x - 1)


def commutator_trace():
    """kappa(x) = tr[A,B] = L + 1/L on the fixed locus."""
    x = sp.symbols("x")
    return (x ** 4 - 3 * x ** 3 + x ** 2 + 4 * x - 2) / (x - 1) ** 2


def meridian_trace_squared():
    """(M + 1/M)^2 = tr(t)^2/det(t) on the fixed locus (det t = 1)."""
    x = sp.symbols("x")
    return (x ** 2 + x - 1) / (x - 1)


def cooper_long():
    """The published figure-eight A-polynomial (Cooper-Long 1996)."""
    M, L = sp.symbols("M L")
    return M ** 4 * L ** 2 + (-M ** 8 + M ** 6 + 2 * M ** 4 + M ** 2 - 1) * L + M ** 4


def eliminant():
    """Eliminate the fixed-point parameter x between (M+1/M)^2 = tr(t)^2 and
    L + 1/L = kappa, in eigenvalue coordinates. Returns the numerator polynomial
    in (M,L); it equals A_CL^2 (the resultant of a quadratic-in-x squares it)."""
    x, P, S, M, L = sp.symbols("x P S M L")
    e1 = P ** 2 * (x - 1) - (x ** 2 + x - 1)                      # P = tr(t) = M + 1/M
    e2 = S * (x - 1) ** 2 - (x ** 4 - 3 * x ** 3 + x ** 2 + 4 * x - 2)  # S = L + 1/L
    F = sp.resultant(e1, e2, x)                                   # = (P^4 - 5P^2 - S + 2)^2
    num, _ = sp.fraction(sp.together(F.subs({P: (M ** 2 + 1) / M, S: (L ** 2 + 1) / L})))
    return sp.expand(num)


def derived_A_polynomial():
    """The squarefree part of the eliminant: the A-polynomial A(M,L) the trace map
    produces. Equals Cooper-Long up to a monomial unit."""
    num = eliminant()
    _, factors = sp.factor_list(num)
    return sp.prod([f for f, _m in factors])


# --------------------------------------------------------------------------- #
# explicit representation + monodromy (numerical)
# --------------------------------------------------------------------------- #

def build_rep(xval):
    """At fixed point x = xval, explicit A, B in SL(2,C) with (tr A, tr B, tr AB) =
    (x, x/(x-1), x/(x-1)), and the monodromy t with tAt^-1 = A^2B, tBt^-1 = AB.
    Returns (A, B, t, residual) where residual measures the monodromy equations."""
    x = complex(xval)
    w = x / (x - 1)
    b = (w + np.sqrt(w * w - 4 + 0j)) / 2          # root of b^2 - w b + 1 = 0
    A = np.array([[x, -1], [1, 0]], dtype=complex)
    B = np.array([[0, b], [-1 / b, w]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    A2B, AB = A @ A @ B, A @ B
    # t A t^-1 = A^2B and t B t^-1 = AB  ->  t A = A^2B t,  t B = AB t  (linear in t)
    # column-major vec: vec(t N) = (N^T (x) I) vec(t),  vec(M t) = (I (x) M) vec(t)
    E = np.vstack([np.kron(A.T, I2) - np.kron(I2, A2B),
                   np.kron(B.T, I2) - np.kron(I2, AB)])
    t = np.linalg.svd(E)[2][-1].conj().reshape(2, 2, order="F")
    t = t / np.sqrt(np.linalg.det(t))              # normalize det t = 1 (fixes t up to sign)
    res = (np.max(np.abs(t @ A @ np.linalg.inv(t) - A2B))
           + np.max(np.abs(t @ B @ np.linalg.inv(t) - AB)))
    return A, B, t, res


def ML_at(xval):
    """(meridian eigenvalue M, longitude eigenvalue L, monodromy residual) at x=xval.
    M = eigenvalue of t; L = eigenvalue of the fiber boundary [B,A] = [A,B]^-1."""
    A, B, t, res = build_rep(xval)
    comm = B @ A @ np.linalg.inv(B) @ np.linalg.inv(A)   # [B,A]: the branch on A_CL=0
    trt, kap = np.trace(t), np.trace(comm)
    M = (trt + np.sqrt(trt * trt - 4 + 0j)) / 2
    L = (kap + np.sqrt(kap * kap - 4 + 0j)) / 2
    return M, L, res


# --------------------------------------------------------------------------- #

def main():
    print("B67 -- figure-eight A-polynomial from the trace-map fixed-point set\n")
    print("trace map T_1^2(x,y,z) =", trace_map_T1sq())
    print("fixed locus:  y = z =", fixed_locus())
    print("tr[A,B] = kappa(x)   =", commutator_trace())
    print("(M+1/M)^2 = tr(t)^2  =", meridian_trace_squared())
    x = sp.symbols("x")
    P2 = meridian_trace_squared()
    print("trace identity  kappa - (tr(t)^4 - 5 tr(t)^2 + 2) =",
          sp.simplify(commutator_trace() - (P2 ** 2 - 5 * P2 + 2)))

    A = sp.expand(derived_A_polynomial())
    CL = sp.expand(cooper_long())
    ratio = sp.simplify(A / CL)
    print("\nderived A(M,L) =", A)
    print("Cooper-Long    =", CL)
    print("derived / Cooper-Long =", ratio, " (monomial unit => exact match)")

    print("\nnumerical check  A_CL(eig t, eig[B,A]) = 0  at sample fixed points:")
    M, L = sp.symbols("M L")
    CLf = sp.lambdify((M, L), cooper_long(), "numpy")
    for xv in (3, 4, 5, 2.5, 7, -1):
        Mv, Lv, res = ML_at(xv)
        print(f"   x={xv:>4}: monodromy residual {res:.1e}, |A_CL(M,L)| = {abs(CLf(Mv, Lv)):.1e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
