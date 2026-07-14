"""B597 — D1's T1/T2: the label non-degeneracy (locks).

See frontier/B597_d1_dictionary/FINDINGS.md.
"""
import json
import os
from fractions import Fraction

_ROOT = os.path.join(os.path.dirname(__file__), "..")


def _taus():
    d = json.load(open(os.path.join(_ROOT, "frontier", "B581_six_torsions",
                                    "six_torsions_results.json")))
    out = {}
    for m in d:
        q = d[m]["quotient"]
        coeffs = [Fraction(c[0]) for c in q]
        lead = coeffs[-1]
        out[int(m)] = sum(k * (c / lead) for k, c in enumerate(coeffs))
    return out


def test_theta_odd_widths_distinct():
    t = _taus()
    assert abs(t[4]) == 260736
    assert abs(t[8]) == 100636318520821923840
    assert abs(t[4]) != abs(t[8])


def test_theta_even_torsions_pairwise_distinct():
    t = _taus()
    vals = [abs(t[m]) for m in (1, 5, 7, 11)]
    assert len(set(vals)) == 4
