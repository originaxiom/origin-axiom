"""Tests for B48 metallic SL(3) trace-map certificates."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = ROOT / "frontier" / "B48_sl3_metallic_trace_maps" / "probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("b48_sl3_metallic_probe", PROBE_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_b48_default_certificates_pass():
    probe = load_probe()
    checks = probe.run_certificates()
    assert all(item.ok for item in checks)


def test_b48_integer_classification_small_rectangle_has_expected_split_values():
    probe = load_probe()
    check = probe.check_integer_classification(cmin=-12, cmax=12, mmax=24)
    assert check.ok
    assert "split c-values=[-11, -9, -3, -1, 0, 1, 2, 3]" in check.detail


def test_b48_entropy_sequence_recurrence():
    probe = load_probe()
    assert [probe.metallic_a(1, n) for n in range(-1, 6)] == [0, 1, 1, 2, 3, 5, 8]
    assert [probe.metallic_a(2, n) for n in range(-1, 5)] == [0, 1, 2, 5, 12, 29]
