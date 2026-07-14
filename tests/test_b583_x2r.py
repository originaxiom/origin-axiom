"""B583-X2R — the corrected X2: phase dichotomy + the quadrature theorem.

See frontier/B583_chiral_content/FINDINGS.md (X2R section).
"""
import cmath
import json
import math
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
        coeffs = [c / lead for c in coeffs]
        out[int(m)] = sum(k * coeffs[k] for k in range(len(coeffs)))
    return out


def test_phase_dichotomy():
    for m, tau in _taus().items():
        assert (tau > 0) == (m % 2 == 0)              # the sign law
        f = 1 / cmath.sqrt(complex(float(tau)))
        if m in (4, 8):
            assert abs(f.imag) < 1e-15 and f.real > 0     # chiral: real
        else:
            assert abs(f.real) < 1e-15                    # gauge: imaginary


def test_quadrature_theorem():
    taus = _taus()
    one_loop = {m: 1 / cmath.sqrt(complex(float(t))) for m, t in taus.items()}
    for kap in (5, 14, 50):
        c = {m: math.exp(-kap * 2.029883212819307 / (2 * math.pi)) * (1 + 0.1 * m)
             for m in taus}
        total = abs(sum(c[m] * one_loop[m] for m in taus)) ** 2
        chir = abs(sum(c[m] * one_loop[m] for m in (4, 8))) ** 2
        gaug = abs(sum(c[m] * one_loop[m] for m in (1, 5, 7, 11))) ** 2
        assert abs(total - (chir + gaug)) < 1e-12 * max(total, chir + gaug)
