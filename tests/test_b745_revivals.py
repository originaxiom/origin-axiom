"""Locks for B745 -- the B742 revivals (B58, B225) cross-verified CONFIRMED x2.

Each lock re-runs one of the arc's independent checks exactly
(frontier/B745_revivals_crossverify/crossverify.py); deterministic, sympy-only.
"""
import json
import os
import random

import sympy as sp

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
t, m, x, z = sp.symbols("t m x z")


def test_c1_b65_exact_j1_charpoly_is_fibonacci_seven_factor_product():
    data = json.load(open(os.path.join(
        ROOT, "frontier/B65_sl4_symbolic_jacobian/jacobian_m.json")))
    J1 = sp.Matrix(15, 15, lambda i, j: sp.sympify(data["J"][i][j])).subs(m, 1)
    A = sp.Matrix([[1, 1], [1, 0]])

    def char_ak(k):
        Ak = A**k if k >= 0 else A.inv() ** (-k)
        return sp.expand(t**2 - sp.trace(Ak) * t + Ak.det())

    A2 = A**2
    target = (char_ak(-1) * char_ak(1) * char_ak(2) * char_ak(3) * char_ak(4)
              * sp.expand(t**2 + sp.trace(A2) * t + A2.det()) * (t - 1) ** 2 * (t + 1))
    assert sp.expand(J1.charpoly(t).as_expr() - sp.expand(target)) == 0


def test_c3_sl3_fixed_line_jacobian_anchor_from_b48_conventions():
    xs = sp.symbols("x1:9")
    x1, x2, x3, x4, x5, x6, x7, x8 = xs
    F = (x3, x1, sp.expand(x1 * x3 - x4 * x2 + x6), x8, x4, x5, x2,
         sp.expand(x4 * x8 - x1 * x5 + x7))
    J = sp.Matrix(8, 8, lambda i, j: sp.diff(F[i], xs[j])).subs({v: 3 for v in xs})
    target = sp.expand((t - 1) * (t + 1) * (t**2 - 3 * t + 1)
                       * (t**2 + t - 1) * (t**2 - 4 * t - 1))
    assert sp.expand(J.charpoly(t).as_expr() - target) == 0


def test_c4_disc_mod_2_always_square_vacuity():
    rng = random.Random(42)
    tested = 0
    for _ in range(30):
        dz = rng.randint(2, 5)
        f = z**dz + sum(rng.randint(-9, 9) * x ** rng.randint(0, 4) * z**k
                        for k in range(dz))
        D = sp.discriminant(sp.Poly(f, z), z)
        if D == 0 or sp.Poly(D, x).degree() <= 0:
            continue
        tested += 1
        fac = sp.factor_list(sp.Poly(D, x, modulus=2).as_expr(), modulus=2)
        assert all(mult % 2 == 0 for _, mult in fac[1])
    assert tested >= 20


def test_c5_11a3_false_positive_at_two():
    delta = -(-4) ** 2 * (-1) - 8 * 0**3 - 27 * (1 + 0) ** 2 + 0
    # recompute Delta honestly from the b-invariants (a1,a2,a3,a4,a6 = 0,-1,1,0,0)
    b2, b4, b6 = -4, 0, 1
    b8 = -1  # a2*a3^2 with a2=-1
    delta = -b2**2 * b8 - 8 * b4**3 - 27 * b6**2 + 9 * b2 * b4 * b6
    assert delta == -11 and delta % 2 != 0            # good reduction at 2
    D = sp.expand(sp.discriminant(sp.Poly(z**2 + z - x**3 + x**2, z), z))
    assert D == 4 * x**3 - 4 * x**2 + 1
    assert sp.LC(sp.Poly(D, x)) % 2 == 0              # the extraction fires at 2 anyway
