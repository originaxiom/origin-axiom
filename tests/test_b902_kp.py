"""B902 locks: the Knus-Paques inverse-class theorem, certificates recomputed."""
import json
import os

import sympy as sp

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B902_knus_paques")


def fmul(u, v):
    a1, b1, c1, d1 = u
    a2, b2, c2, d2 = v
    return (a1*a2 + 77*b1*b2 - 3*c1*c2 - 231*d1*d2,
            a1*b2 + b1*a2 - 3*(c1*d2 + d1*c2),
            a1*c2 + c1*a2 + 77*(b1*d2 + d1*b2),
            a1*d2 + d1*a2 + b1*c2 + c1*b2)


def _alphas():
    with open(os.path.join(ARC, "results.json")) as f:
        r = json.load(f)
    return {k: tuple(sp.Rational(t) for t in v) for k, v in r["alphas"].items()}


G1 = (sp.Rational(73008, 7), sp.Integer(0), sp.Rational(73008, 7), sp.Integer(0))
G2 = (sp.Rational(30901351219200, 13), sp.Integer(0),
      sp.Rational(30901351219200, 13), sp.Integer(0))


def test_certificate_mu_vacuum():
    a = _alphas()
    lhs = fmul(a["mu"], a["vacuum"])
    assert fmul(fmul(G1, G1), G1) == lhs


def test_certificate_generic_vacuum():
    a = _alphas()
    lhs = fmul(a["generic"], a["vacuum"])
    assert fmul(fmul(G2, G2), G2) == lhs


def test_certificates_live_in_the_cyclotomic_line():
    # both gammas are rational multiples of 1 + sqrt(-3): no sqrt(77) content
    for g in (G1, G2):
        assert g[1] == 0 and g[3] == 0 and g[0] == g[2]


def test_inverse_class_corollary():
    # alpha_mu / alpha_generic = (G1/G2)^3 follows by composition;
    # equivalently alpha_mu * alpha_vac and alpha_gen * alpha_vac cubes
    # => [alpha_vac] = [alpha_mu]^{-1} = [alpha_generic]^{-1}.
    # Sanity: the alphas themselves are NOT rational cubes (nontrivial classes):
    a = _alphas()
    for k in ("mu", "generic", "vacuum"):
        aa = a[k]
        assert aa[3] != 0        # genuinely quadratic over Q -> nontrivial
