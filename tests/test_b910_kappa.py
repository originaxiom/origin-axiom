"""B910 locks: kappa's identity, the split certificate, the One-Class theorem."""
import json
import os

import sympy as sp

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B910_kappa_class")


def _res():
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_kappa_identity_and_split():
    s, rho = sp.symbols("s rho")
    kappa = 2771822592000*s**3 + 3033676800*s**2 - 56402640*s - 6859
    assert sp.Poly(kappa, s).all_coeffs()[-1] == -19**3
    d = sp.discriminant(kappa, s)
    sf = sp.Integer(1)
    for p, e in sp.factorint(d).items():
        if e % 2: sf *= p
    assert sf == 77
    mu = 500716339200*rho**3 - 2075673600*rho**2 - 4769856*rho + 2197
    sstar = sp.Rational(-4997, 1257360) - sp.Rational(198911, 68107)*rho \
        + sp.Rational(560387520, 885391)*rho**2
    rem = sp.rem(sp.expand(kappa.subs(s, sstar)), mu, rho)
    assert sp.expand(rem) == 0


def fmul(u, v):
    a1, b1, c1, d1 = u
    a2, b2, c2, d2 = v
    return (a1*a2 + 77*b1*b2 - 3*c1*c2 - 231*d1*d2,
            a1*b2 + b1*a2 - 3*(c1*d2 + d1*c2),
            a1*c2 + c1*a2 + 77*(b1*d2 + d1*b2),
            a1*d2 + d1*a2 + b1*c2 + c1*b2)


def test_headline_certificate_gamma3():
    R = sp.Rational
    alpha_mu = (R(4826809, 25443808051200), 0, 0, R(4826809, 299873452032000))
    alpha_kappa = (19**6*R(-1, 690594465792000), 0, 0,
                   19**6*R(1, 1470297894912000))
    gamma3 = (R(5239, 48013), 0, R(5239, 48013), 0)
    g2 = (R(-5239, 192052)*3, 0, 0, 0)
    # gamma3 = (1+sqrt(-3))*(5239/48013 - (5239/192052)sqrt(-231)) in 4-vector:
    a, b = R(5239, 48013), R(-5239, 192052)
    g = (a, 0, a, 0)
    h = (0, 0, 0, b)
    hh = fmul((1, 0, 1, 0), (0, 0, 0, b))
    gamma3 = tuple(x + y for x, y in zip(g, hh))
    cube = fmul(fmul(gamma3, gamma3), gamma3)
    lhs = fmul(cube, alpha_kappa)
    assert lhs == alpha_mu


def test_class_table_banked():
    r = _res()
    assert "classes" in r and "pairs" in r and "singles" in r
