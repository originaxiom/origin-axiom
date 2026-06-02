"""Tests for B57 general-m Diophantine splitting classification."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = ROOT / "frontier" / "B57_general_m_splitting" / "probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("b57_general_m_splitting", PROBE_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_b57_all_checks_pass():
    probe = load_probe()
    assert all(item.ok for item in probe.run_checks())


def test_classification_matches_expected():
    probe = load_probe()
    for m_value, expected in probe.EXPECTED.items():
        assert probe.splitting_points(m_value) == expected


def test_c1_and_c3_universal():
    probe = load_probe()
    for m_value in range(1, 7):
        points = probe.splitting_points(m_value)
        assert 1 in points and 3 in points
