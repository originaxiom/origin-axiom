"""Tests for B65: the symbolic SL(4) Jacobian J(m) and its factorization.

Loads the committed reconstructed J(m) (jacobian_m.json) and verifies, as exact
symbolic algebra, that char(J(m)) factors over Z[m] as the Dickson product
char(M^-1)char(M)char(M^2)char(M^3)char(M^4)char(-M^2)(t-1)^2(t+1).
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = ROOT / "frontier" / "B65_sl4_symbolic_jacobian" / "probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("b65_sl4_symbolic_jacobian", PROBE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_jacobian_is_15x15_degree4_in_m():
    probe = load_probe()
    m = sp.symbols("m")
    J = probe.symbolic_jacobian()
    assert J.shape == (15, 15)
    assert max(sp.degree(J[i, j], m) if J[i, j].has(m) else 0
               for i in range(15) for j in range(15)) == 4


def test_charpoly_factors_over_Zm_as_dickson_product():
    """The full symbolic identity char(J(m)) == the Dickson factorization."""
    probe = load_probe()
    t = sp.symbols("t")
    cp = sp.expand(probe.symbolic_jacobian().charpoly(t).as_expr())
    assert sp.expand(cp - probe.target_factorization()) == 0


def test_factors_are_char_Mk_with_lucas_coefficients():
    probe = load_probe()
    m = sp.symbols("m")
    assert sp.expand(probe.Lk(2) - (m**2 + 2)) == 0
    assert sp.expand(probe.Lk(3) - (m**3 + 3 * m)) == 0
    assert sp.expand(probe.Lk(4) - (m**4 + 4 * m**2 + 2)) == 0
    assert sp.expand(probe.Lk(-1) + m) == 0  # tr(M^-1) = -m


def test_m1_matches_b59_factorization():
    probe = load_probe()
    t, m = sp.symbols("t m")
    cp1 = sp.expand(probe.symbolic_jacobian().charpoly(t).as_expr().subs(m, 1))
    b59 = sp.expand(
        (t**2 + t - 1) * (t**2 - t - 1) * (t**2 - 3 * t + 1) * (t**2 - 4 * t - 1)
        * (t**2 - 7 * t + 1) * (t**2 + 3 * t + 1) * (t - 1) ** 2 * (t + 1)
    )
    assert sp.expand(cp1 - b59) == 0
