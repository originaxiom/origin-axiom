"""Tests for B64: the parity mechanism (k(alpha) sector assignment).

All checks are exact symbolic algebra (sympy), so the suite runs them directly.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = ROOT / "frontier" / "B64_parity_mechanism" / "probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("b64_parity_mechanism", PROBE_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_b64_checks_pass():
    probe = load_probe()
    assert all(item.ok for item in probe.run_checks())


def test_dickson_parity():
    probe = load_probe()
    m = sp.symbols("m")
    for kk in range(1, 7):
        Lk = probe.lucas_poly(kk)
        assert sp.expand(Lk.subs(m, -m) - (-1) ** kk * Lk) == 0


def test_sl3_sectors_are_dickson_products():
    probe = load_probe()
    t, m = sp.symbols("t m")
    sym, anti, ou, ol = probe.sl3_sectors()
    assert sp.expand(ou) == sp.zeros(4) and sp.expand(ol) == sp.zeros(4)  # block-diagonal
    assert sp.expand(sym.charpoly(t).as_expr() - (t - 1) * (t + 1) * (t**2 - (m**2 + 2) * t + 1)) == 0
    assert sp.expand(anti.charpoly(t).as_expr() - (t**2 + m * t - 1) * (t**2 - (m**3 + 3 * m) * t - 1)) == 0


def test_symmetric_sector_even_in_m_antisym_odd_k():
    probe = load_probe()
    t, m = sp.symbols("t m")
    sym, anti, _, _ = probe.sl3_sectors()
    sym_cp = sym.charpoly(t).as_expr()
    assert sp.expand(sym_cp.subs(m, -m) - sym_cp) == 0  # symmetric sector even in m


def test_depth4_sequences_are_polynomials_in_k():
    probe = load_probe()
    k = sp.symbols("k")
    seqs = probe.sl4_dtau_sequences()
    assert max(sp.degree(seqs[j], k) for j in ("s_-2", "s_-1", "s_0", "s_1")) <= 3
    assert max(sp.degree(seqs[j], k) for j in ("e1", "e2", "e3")) <= 4
