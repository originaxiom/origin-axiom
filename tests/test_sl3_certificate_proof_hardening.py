"""Tests for B49 SL(3) certificate-to-proof hardening."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = ROOT / "frontier" / "B49_sl3_certificate_proof_hardening" / "probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("b49_sl3_proof_hardening", PROBE_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_b49_all_checks_pass():
    probe = load_probe()
    results = probe.run_checks()
    assert all(ok for _, ok, _ in results)


def test_square_gap_seed_logic_rejects_bad_seed():
    probe = load_probe()
    assert probe.seed_is_propagating((1, 1, 1, 1, 1))
    assert not probe.seed_is_propagating((1, 1, 1, 2, 1))
    assert not probe.seed_is_propagating((0, 1, 1, 1, 1))
