"""Exact controls, not a replacement for the sealed full replay."""
import importlib.util
from fractions import Fraction
from pathlib import Path

BASE = Path(__file__).resolve().parents[1] / "reports/physical_bridge_2026_09_05/cusp_negative_audit_2026_10_09"


def load(name):
    spec = importlib.util.spec_from_file_location("cusp_audit_" + name, BASE / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_exact_finite_counterexample():
    p = load("probe")
    assert p.tail(10, 2) == Fraction(124, 165)
    assert p.tail(10, 2) != Fraction(3, 4)


def test_independent_small_population():
    p, r = load("probe"), load("reference")
    for n in range(2, 9):
        count, row, _ = r.rows(n)
        assert count == p.population(n)
        assert row == {str(k): str(p.tail(n, k)) for k in range(1, n + 1)}


def test_primitive_detector_opposing_cases():
    r = load("reference")
    assert r.primitive("LLLR") and r.primitive("LLRR")
    assert not r.primitive("LLLL") and not r.primitive("LRLR")


def test_run_wrap_control():
    r = load("reference")
    assert r.marked_run("LLRLL") == 4
    assert r.marked_run("RLLLR") == 2
    assert r.marked_run("LLLL") == 4


def test_exact_height_controls():
    r = load("reference")
    assert r.height_squared("LR") == Fraction(5, 4)
    assert r.height_squared("LLRR") == 2
    assert r.height_squared("LLLR") == Fraction(21, 4)
    assert r.height_squared("LLLR") == r.height_squared("RLLL")


def test_conditioning_error_bound():
    p = load("probe")
    for n in range(2, 16):
        q = Fraction(2 ** n - p.population(n), 2 ** n)
        assert 0 <= q < 1
        for k in range(1, n):
            assert abs(p.tail(n, k) - Fraction(k + 1, 2 ** k)) <= q


def test_full_length_and_invalid_domain():
    import pytest
    p = load("probe")
    assert all(p.tail(n, n) == 0 for n in range(2, 19))
    with pytest.raises(ValueError):
        p.tail(1, 1)
