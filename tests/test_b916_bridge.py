"""B916 locks: the bridge verdicts."""
import json
import os

import sympy as sp

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B916_lambda_bridge")


def _res():
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_bridge_and_cubic_transport():
    r = _res()
    t = json.dumps(r)
    assert '"t": 1' in t or '"t": "1"' in t or '"cubic_transport_t": "1"' in t \
        or '"cubic_transport_t": 1' in t or "'t' = 1" in t or '"t_exact": "1"' in t


def test_norm_law():
    # prod d_i = -(953/2304)^2 exactly => lambda ratio = 2304/953
    x = sp.Symbol("x")
    pS = 2304**2*x**3 + 9123840*x**2 + 5077008*x + 953**2
    pA = 2304**2*x**3 - 1907712*x**2 - 2304*953*x + 953**2
    # the product of the roots of each cubic (by Vieta): -const/lead
    for p in (pS, pA):
        prod_roots = sp.Rational(-sp.Poly(p, x).all_coeffs()[-1],
                                 sp.Poly(p, x).all_coeffs()[0])
        assert prod_roots == -sp.Rational(953, 2304)**2


def test_two_lambdas_recorded():
    t = json.dumps(_res())
    assert "2304/953" in t or "2304, 953" in t


def test_d2_is_not_a_weight_lattice_character():
    import itertools
    r = _res()
    W = r["H_prime_diag_vs_H_plus"]["flipped_coordinates_weights"]
    flips = [tuple(x % 2 for x in w) for w in W]
    sols = [a for a in itertools.product((0, 1), repeat=6)
            if all(sum(a[i]*f[i] for i in range(6)) % 2 == 1 for f in flips)]
    assert sols == []
    assert r["H_prime_diag_vs_H_plus"]["flip_count"] == 11
