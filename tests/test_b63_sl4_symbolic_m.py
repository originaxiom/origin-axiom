"""Tests for B63: SL(4) fixed-line factorization over Z[m] (computer-assisted).

Fast checks only: the symbolic factorization structure (pure sympy) and the m=1
numerical regression against B59.  The full multi-m verification + L_k
interpolation (~minutes) runs in the probe's __main__.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = ROOT / "frontier" / "B63_sl4_symbolic_m" / "probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("b63_sl4_symbolic_m", PROBE_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_b63_fast_checks_pass():
    probe = load_probe()
    assert all(item.ok for item in probe.run_checks())


def test_Lk_polynomials_are_lucas():
    probe = load_probe()
    m = sp.symbols("m")
    assert sp.expand(probe.Lk_poly(2) - (m**2 + 2)) == 0
    assert sp.expand(probe.Lk_poly(3) - (m**3 + 3 * m)) == 0
    assert sp.expand(probe.Lk_poly(4) - (m**4 + 4 * m**2 + 2)) == 0
    assert sp.expand(probe.Lk_poly_neg(-1) - (-m)) == 0


def test_symbolic_factorization_matches_b59_at_m1():
    probe = load_probe()
    t, m = sp.symbols("t m")
    expr = probe.symbolic_factorization().subs(m, 1)
    # B59: char(M^-1) char(M) char(M^2) char(M^3) char(M^4) char(-M^2) (t-1)^2 (t+1)
    b59 = sp.expand(
        (t**2 + t - 1) * (t**2 - t - 1) * (t**2 - 3 * t + 1) * (t**2 - 4 * t - 1)
        * (t**2 - 7 * t + 1) * (t**2 + 3 * t + 1) * (t - 1) ** 2 * (t + 1)
    )
    assert sp.expand(expr - b59) == 0


def test_factorization_is_degree_15_for_symbolic_m():
    probe = load_probe()
    t = sp.symbols("t")
    assert sp.degree(probe.symbolic_factorization(), t) == 15
    # the m=1 numerical regression against B59 is exercised by run_checks
    # (test_b63_fast_checks_pass); the full multi-m verification is in __main__.
