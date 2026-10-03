#!/usr/bin/env python3
"""B1527: the step of Part A that the PREREGISTRATION states in one line, checked exactly (written after the run, while drafting
FINDINGS; it computes no manifold).

Part A says: "A non-zero tangent with c = 0 would have a pure so(3,1) tangent. That makes the cusp loxodromic at first order,
outside S."  The step rests on one fact about the slice, which this script proves in exact arithmetic (sympy):
  at a = b = 0 the slice's a- and b-directions take values in v, the complement of so(3,1):
  D_a(g) = d/da [ |det|^(-1/4) exp(X N_a + Y N_b) ] at a = b = 0, right-translated, equals
           X (E22 - I/4) + (X^2/2) (E12 - E24) - (X^3/3) E14,
  and it is Q-symmetric (Q D^T Q = D) for the form Q = E14 + E41 - E22 - E33 (2 x1 x4 - x2^2 - x3^2), whose so(Q) contains
  N_a and N_b at a = b = 0. Likewise D_b with (2, 3) and (X, Y) exchanged.
So the slice's so(3,1)-directions at a = b = 0 are the translations alone (parabolic), and the projective directions are D_a and
D_b. A tangent class whose v-part vanishes on the cusp restricts there to a parabolic so(3,1) class; the complete structure has
no non-zero first-order deformation with parabolic cusp (Garland, Weil; the meridian's complex length is a local coordinate,
Thurston), so the class is zero. Hence a non-zero tangent has a non-zero v-part, and (rigid rel cusp, l a rigid slope)
0 != c(l) = a' D_a(l) + b' D_b(l). On a type-one path (b = 0), a' != 0 and D_a(l) != 0, and D_a(l) = 0 exactly when X_l = 0.

Prints the checks; exits non-zero if one fails."""
import sys

import sympy as sp

X, Y, a, b = sp.symbols("X Y a b", real=True)


def E(i, j):
    m = sp.zeros(4, 4)
    m[i - 1, j - 1] = 1
    return m


I4 = sp.eye(4)
Q = E(1, 4) + E(4, 1) - E(2, 2) - E(3, 3)
Na = E(1, 2) + a * E(2, 2) + E(2, 4)
Nb = E(1, 3) + b * E(3, 3) + E(3, 4)


def dexp_at(M, K, order=6):
    """d/ds exp(M + s K) at s = 0, by the series sum_n 1/n! sum_j M^j K M^(n-1-j) (M nilpotent: it terminates)"""
    out = sp.zeros(4, 4)
    for n in range(1, order + 1):
        acc = sp.zeros(4, 4)
        for j in range(n):
            acc += M ** j * K * M ** (n - 1 - j)
        out += acc / sp.factorial(n)
    return out


def main():
    ok = True
    M0 = (X * Na + Y * Nb).subs({a: 0, b: 0})
    checks = {}
    checks["M0^3 = 0 (the cusp at a = b = 0 is unipotent)"] = sp.simplify(M0 ** 3) == sp.zeros(4, 4)
    for name, N in (("N_a", Na), ("N_b", Nb)):
        N0 = N.subs({a: 0, b: 0})
        checks[f"{name} at a = b = 0 lies in so(Q)"] = sp.simplify(Q * N0 + N0.T * Q) == sp.zeros(4, 4)
    exp0 = I4 + M0 + M0 ** 2 / 2
    exp0_inv = I4 - M0 + M0 ** 2 / 2
    # D_a: d/da of exp(X N_a + Y N_b) e^{-(aX + bY)/4} at a = b = 0, right-translated
    Da = sp.expand((dexp_at(M0, X * E(2, 2)) - X / 4 * exp0) * exp0_inv)
    Db = sp.expand((dexp_at(M0, Y * E(3, 3)) - Y / 4 * exp0) * exp0_inv)
    closed = X * (E(2, 2) - I4 / 4) + X ** 2 / 2 * (E(1, 2) - E(2, 4)) - X ** 3 / 3 * E(1, 4)
    closed_b = Y * (E(3, 3) - I4 / 4) + Y ** 2 / 2 * (E(1, 3) - E(3, 4)) - Y ** 3 / 3 * E(1, 4)
    checks["D_a equals its closed form"] = sp.simplify(Da - closed) == sp.zeros(4, 4)
    checks["D_b equals its closed form"] = sp.simplify(Db - closed_b) == sp.zeros(4, 4)
    checks["D_a is traceless"] = sp.simplify(Da.trace()) == 0
    checks["D_a lies in v (Q D_a^T Q = D_a)"] = sp.simplify(Q * Da.T * Q - Da) == sp.zeros(4, 4)
    checks["D_b lies in v (Q D_b^T Q = D_b)"] = sp.simplify(Q * Db.T * Q - Db) == sp.zeros(4, 4)
    sol = sp.solve([e for e in Da if e != 0], X, dict=True)
    checks["D_a(g) = 0 exactly when X_g = 0"] = sol == [{X: 0}]
    # a numeric cross-check of the derivative against a finite difference of the exact matrix exponential
    import mpmath as mp
    mp.mp.dps = 40
    xv, yv, h = mp.mpf("0.7"), mp.mpf("-1.3"), mp.mpf(10) ** -15

    def sl(av):
        Mn = mp.matrix([[0, xv, yv, 0], [0, av * xv, 0, xv], [0, 0, 0, yv], [0, 0, 0, 0]])
        return mp.expm(Mn) * mp.exp(-av * xv / 4)
    fd = (sl(h) - sl(-h)) / (2 * h) * mp.inverse(sl(0))
    Dn = mp.matrix([[float(0)] * 4] * 4)
    for i in range(4):
        for j in range(4):
            Dn[i, j] = mp.mpf(str(sp.N(closed[i, j].subs({X: sp.Rational(7, 10)}), 40)))
    checks["D_a against a central difference of mpmath's expm (< 1e-25)"] = float(mp.norm(fd - Dn)) < 1e-25
    for k, v in checks.items():
        print(("PASS " if v else "FAIL ") + k)
        ok = ok and bool(v)
    print("D_a =", closed)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
