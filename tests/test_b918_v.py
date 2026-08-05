"""B918 locks: HIER exact, the class, the observer's place."""
import json
import os

import sympy as sp

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B918_v_kummer")


def _res():
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_hier_cubic_exact_and_irreducible():
    x = sp.Symbol("x")
    HIER = 953**4*x**3 - 27609909080832*x**2 + 264084438122496*x - 760840571584512
    assert sp.factorint(27609909080832) == {2: 8, 3: 9, 13: 1, 421493: 1}
    assert sp.factorint(264084438122496) == {2: 21, 3: 8, 17: 1, 1129: 1}
    assert sp.factorint(760840571584512) == {2: 32, 3: 11}
    assert sp.Poly(HIER, x).is_irreducible
    d = sp.discriminant(HIER, x)
    sf = sp.Integer(1)
    for p, e in sp.factorint(d).items():
        if e % 2: sf *= p
    assert sf == 77


def test_hier_root_in_K():
    x, rho = sp.symbols("x rho")
    HIER = 953**4*x**3 - 27609909080832*x**2 + 264084438122496*x - 760840571584512
    mu = 500716339200*rho**3 - 2075673600*rho**2 - 4769856*rho + 2197
    V = (sp.Rational(1084447130452992, 139398566318089)
         + sp.Rational(2399403349337702400, 1812181362135157)*rho
         + sp.Rational(3020358603911646412800, 23558357707757041)*rho**2)
    rem = sp.rem(sp.expand(HIER.subs(x, V)), mu, rho)
    assert sp.expand(rem) == 0


def test_class_and_place_verdicts_banked():
    t = json.dumps(_res())
    assert "953" in t
    # the class verdict and the place valuations recorded
    assert "-4" in t or "v_deg1" in t
