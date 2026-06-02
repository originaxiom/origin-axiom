"""Tests for B60 SL(n) tower: cross-n structure map (n=3,4) + SL(5) barrier."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = ROOT / "frontier" / "B60_sln_tower" / "probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("b60_sln_tower", PROBE_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_b60_checks_pass():
    probe = load_probe()
    assert all(item.ok for item in probe.run_checks())


def test_sl5_conditioning_is_a_barrier():
    # documents that double precision cannot resolve SL(5)
    probe = load_probe()
    item = probe.check_sl5_conditioning_barrier()
    assert item.ok  # cond(Dx) > 1e8
