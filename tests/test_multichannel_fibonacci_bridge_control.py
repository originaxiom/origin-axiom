"""Tests for B52 multichannel Fibonacci bridge control."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = ROOT / "frontier" / "B52_multichannel_fibonacci_bridge_control" / "probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("b52_multichannel_fibonacci_bridge_control", PROBE_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_b52_all_checks_pass():
    probe = load_probe()
    checks = probe.run_checks()
    assert all(item.ok for item in checks)


def test_naive_bridge_has_wrong_trace_recursion_order():
    probe = load_probe()
    energy, onsite_a, onsite_b, coupling = probe.deterministic_model()
    transfer_a = probe.transfer_matrix(energy, onsite_a, coupling)
    transfer_b = probe.transfer_matrix(energy, onsite_b, coupling)
    assert max(abs(value) for value in probe.pc12_third_order_residuals(transfer_a, transfer_b)) > 1e-3
    assert max(abs(value) for value in probe.order_six_residuals(transfer_a, transfer_b)) < 1e-8
