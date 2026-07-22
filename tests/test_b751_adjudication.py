"""Locks for B751 -- the iterated-hearing adjudication (artifact + arithmetic locks)."""
import math
import os

import sympy as sp

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "frontier", "B751_iterated_hearing_adjudication", "output.txt")
phi = (1 + sp.sqrt(5)) / 2


def test_cell1_identity_exact():
    assert sp.simplify((1 / phi**2) * (1 / (2 * phi)) - 1 / (2 * phi**3)) == 0
    assert sp.simplify(phi**3 - 2 - sp.sqrt(5)) == 0


def test_cell2_banked_amplitude_is_complex_word_level():
    amp = 1 / (2 * phi) + sp.I * sp.sin(2 * sp.pi / 5) / sp.sqrt(5)
    assert float(sp.Abs(sp.im(amp))) > 0.42          # the dropped part is not small
    assert abs(float(sp.Abs(amp)) - 0.5257311) < 1e-6


def test_cell3_alpha_s_runs_by_factor_two_over_the_dial():
    aMZ, MZ, b0 = 0.1180, 91.1876, (33 - 10) / (12 * math.pi)
    a10 = aMZ / (1 + b0 * aMZ * math.log(10.0**2 / MZ**2))
    a1k = aMZ / (1 + b0 * aMZ * math.log(1000.0**2 / MZ**2))
    assert a10 > 0.17 and a1k < 0.09


def test_verdict_lines_in_banked_output():
    text = open(OUT, encoding="utf-8").read()
    assert "CELL 2 VERDICT: CONSTRUCTED" in text
    assert "CELL 3 VERDICT: KNOB-DEPENDENT" in text
    assert "HITS = 2:" in text and "Poisson P(>= 2 hits" in text
    assert "pairs tested = 192 (distinct candidate values only)" in text


def test_addendum_born_weight_identity():
    amp = 1 / (2 * phi) + sp.I * sp.sin(2 * sp.pi / 5) / sp.sqrt(5)
    m2 = sp.simplify(sp.Abs(amp) ** 2)
    assert sp.simplify(m2 - (5 - sp.sqrt(5)) / 10) == 0
    assert sp.simplify(m2 - 1 / (phi * sp.sqrt(5))) == 0
