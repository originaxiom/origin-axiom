"""Locks for B399 e3 — cell D4-e3 (B571 item B1). Fast, deterministic, no repo writes made
by the computing session; this file is a proposed addition to tests/test_b399_wall.py.

e3 = c1/1728, c1 = zeta9 + zeta9^{-1} = 2cos(2*pi/9), root of x^3-3x+1=0.
Verified against all available singles_1215*.json primes (>=20 at time of writing).
"""
import glob
import json
import os
import sys

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B399_wall_scale")
sys.path.insert(0, os.path.join(HERE, "..", "B391_existence_general"))
from census_big import primitive_root  # noqa: E402


def _load_triple_data():
    DATA = {}
    for f in glob.glob(os.path.join(HERE, "singles_1215*.json")):
        d = json.load(open(f))
        for p, cells in d.items():
            if all(str(c) in cells for c in (121, 256, 391)):
                DATA[p] = cells
    return DATA


def _vs(DATA, p):
    return [int(DATA[str(p)][str(c)]) for c in (121, 256, 391)]


def _c1(p):
    g = primitive_root(p)
    z9 = pow(g, (p - 1) // 9, p)
    return (z9 + pow(z9, 8, p)) % p


def test_e3_equals_c1_over_1728_all_primes():
    DATA = _load_triple_data()
    primes = sorted(map(int, DATA))
    assert len(primes) >= 20, "expected >=20 primes with full (121,256,391) cell data"
    for p in primes:
        v = _vs(DATA, p)
        e1 = sum(v) % p
        e2 = (v[0] * v[1] + v[0] * v[2] + v[1] * v[2]) % p
        e3 = (v[0] * v[1] * v[2]) % p
        e3_pred = (_c1(p) * pow(1728, p - 2, p)) % p
        assert e1 == 0
        assert e2 == (-pow(48, p - 2, p)) % p
        assert e3 == e3_pred
        # the census triple values are exactly the roots of t^3 - t/48 - e3
        inv48 = pow(48, p - 2, p)
        for vi in v:
            assert (pow(vi, 3, p) - vi * inv48 - e3_pred) % p == 0


def test_e3_minimal_polynomial_matches_sympy():
    import sympy as sp

    x = sp.symbols("x")
    mp = sp.minimal_polynomial(2 * sp.cos(2 * sp.pi / 9), x)
    assert sp.expand(mp - (x**3 - 3 * x + 1)) == 0
    disc = sp.discriminant(mp, x)
    assert disc == 81
    assert 1728 == 2**6 * 3**3


def test_sentinel_adjudication_negative():
    # 31-collision + supersingular {31,79,167}: none appear in e3's arithmetic content
    # (denominator 1728, minimal-poly discriminant 81) -- both fire negative.
    sentinel_primes = (17, 19, 31, 79, 167)
    for q in sentinel_primes:
        assert 1728 % q != 0
        assert 81 % q != 0
