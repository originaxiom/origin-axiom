"""Tests for B62: opposition involution and the 2 unresolved SL(5) modes."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = ROOT / "frontier" / "B62_opposition_involution" / "probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("b62_opposition_involution", PROBE_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_b62_checks_pass():
    probe = load_probe()
    assert all(item.ok for item in probe.run_checks())


def test_opposition_is_an_involution_preserving_height():
    probe = load_probe()
    for n in (3, 4, 5, 6):
        for h in range(1, n):
            for r in probe.roots_of_height(n, h):
                tr = probe.opposition(n, r)
                assert probe.opposition(n, tr) == r          # involution
                assert abs(tr[0] - tr[1]) == h               # preserves height


def test_height2_split_reproduces_sl3_sl4_and_predicts_sl5():
    probe = load_probe()
    assert probe.height2_sectors(3) == (1, 0)   # char(M^2) only      -> SL(3) tower
    assert probe.height2_sectors(4) == (1, 1)   # char(M^2).char(-M^2) -> SL(4) tower
    assert probe.height2_sectors(5) == (2, 1)   # char(M^2)^2.char(-M^2) -> 2 unresolved = char(M^2)


def test_char_M2_roots_are_golden():
    probe = load_probe()
    mp.mp.dps = 30
    phi = (1 + mp.sqrt(5)) / 2
    roots = probe.char_Mk_roots(2, +1)          # char(M^2) = t^2 - 3t + 1
    assert abs(roots[1] - phi ** 2) < mp.mpf("1e-25")
    assert abs(roots[0] - 1 / phi ** 2) < mp.mpf("1e-25")


def test_height2_dimension_is_2_times_n_minus_2():
    probe = load_probe()
    for n in (3, 4, 5, 6, 7):
        plus, minus = probe.theta_split(n, 2)
        assert plus + minus == 2 * (n - 2)
