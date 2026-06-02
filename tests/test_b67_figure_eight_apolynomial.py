"""Tests for B67: the figure-eight A-polynomial from the trace-map fixed-point set.

Locks the exact symbolic derivation -- the eliminant of the fixed-point parameter
between (M+1/M)^2 = tr(t)^2 and L+1/L = tr[A,B] equals the Cooper-Long (1996)
figure-eight A-polynomial -- plus a numerical check that the explicit monodromy t
satisfies tAt^-1 = A^2B, tBt^-1 = AB and that A_CL(eig t, eig[B,A]) = 0.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = ROOT / "frontier" / "B67_figure_eight_apolynomial" / "probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("b67_figure_eight_apolynomial", PROBE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_trace_map_and_fixed_locus():
    probe = load_probe()
    x, y, z = sp.symbols("x y z")
    assert probe.trace_map_T1sq() == (x * z - y, z, sp.expand(x * z ** 2 - x - y * z))
    # the fixed locus y=z=x/(x-1) is genuinely fixed by T_1^2
    w = probe.fixed_locus()
    img = [c.subs({y: w, z: w}) for c in probe.trace_map_T1sq()]
    assert [sp.simplify(a - b) for a, b in zip(img, (x, w, w))] == [0, 0, 0]


def test_meridian_longitude_trace_identity():
    """kappa = tr(t)^4 - 5 tr(t)^2 + 2 on the fixed locus."""
    probe = load_probe()
    P2 = probe.meridian_trace_squared()
    assert sp.simplify(probe.commutator_trace() - (P2 ** 2 - 5 * P2 + 2)) == 0


def test_derived_A_polynomial_equals_cooper_long():
    """The exact polynomial equality: the trace-map eliminant is the Cooper-Long
    figure-eight A-polynomial."""
    probe = load_probe()
    assert sp.expand(probe.derived_A_polynomial() - probe.cooper_long()) == 0
    # the raw eliminant is A_CL^2 (the resultant of a quadratic-in-x squares it)
    ratio = sp.simplify(probe.eliminant() / probe.cooper_long() ** 2)
    assert ratio.is_constant() and ratio != 0


def test_monodromy_and_apolynomial_vanish_numerically():
    probe = load_probe()
    M, L = sp.symbols("M L")
    CLf = sp.lambdify((M, L), probe.cooper_long(), "numpy")
    for xv in (3, 4, 5, 2.5, 7, -1):
        Mv, Lv, res = probe.ML_at(xv)
        assert res < 1e-9                         # t solves the monodromy equations
        assert abs(CLf(Mv, Lv)) < 1e-9            # (M, L) lies on A_CL = 0


def test_cooper_long_is_the_published_invariant():
    """Guard the reference polynomial against accidental edits."""
    probe = load_probe()
    M, L = sp.symbols("M L")
    expected = M ** 4 * L ** 2 + (-M ** 8 + M ** 6 + 2 * M ** 4 + M ** 2 - 1) * L + M ** 4
    assert sp.expand(probe.cooper_long() - expected) == 0
