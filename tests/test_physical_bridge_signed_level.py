"""R78 exact algebra and opposite controls; not a physics spectrum test."""
import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "r78_signed_level", ROOT / "reports/physical_bridge_2026_09_05/signed_level.py")
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def test_sign_after_even_power_is_not_cover_of_negative_seed():
    a = M.word("LR")
    assert M.sign(M.power(a, 2), -1) == ((-5, -3), (-3, -2))
    assert M.old_reconstruction(-1, "LRLR") == ((5, 3), (3, 2))
    assert M.trace(M.sign(M.power(a, 2), -1)) != M.trace(M.old_reconstruction(-1, "LRLR"))


@pytest.mark.parametrize("eps,w", [(1, "LRLR"), (-1, "LRLRLR"), (-1, "LLR")])
def test_old_reconstruction_valid_opposite_controls(eps, w):
    assert M.old_reconstruction(eps, w) == M.sign(M.word(w), eps)


def test_exact_homology_distinguishes_equal_unsigned_trace():
    u = M.sign(M.word("LRLR"), -1)
    assert M.fibre_smith(u) == (3, 3)
    assert M.fibre_smith(M.word("LRLR")) == (5,)
    assert M.trace(M.word("LLLLLR")) == M.trace(M.word("LRLR")) == 7
    assert M.fibre_smith(M.sign(M.word("LLLLLR"), -1)) == (9,)


def test_fixed_characters_are_the_full_C3_square_not_only_order_nine():
    u = M.sign(M.word("LRLR"), -1)
    chars = M.fixed_characters(u, 3)
    assert set(chars) == {(x, y) for x in range(3) for y in range(3)}
    assert M.fixed_characters(M.word("LRLR"), 3) == [(0, 0)]
    assert M.fixed_characters(M.sign(M.word("LLLLLR"), -1), 3) != chars


def test_complete_trace_seven_window_and_cover_law():
    r = M.exact_report()
    assert set(r["trace7_complete_candidates"]) == {"LLLLLR", "LRLR"}
    assert r["corrected_cover_checks"] > 0
    assert r["common_double_cover_matrix"] == M.power(M.word("LR"), 4)


def test_even_power_root_reason_requires_hyperbolic_target():
    elliptic = ((0, -1), (1, 0))
    assert M.power(elliptic, 2) == M.sign(M.I, -1)
    assert abs(M.trace(M.power(elliptic, 2))) == 2
    assert abs(M.trace(M.power(M.sign(M.word("LR"), -1), 3))) == 18


def test_foreign_check_passes_while_the_reconstruction_predicate_fails():
    r = M.foreign_reconstruction_audit()
    assert r["foreign_census"]["total"] == 758 and r["foreign_census"]["passed"]
    assert r["foreign_C9"]["passed"]
    failures = r["additional_reconstruction_failures"]
    assert failures
    u = M.sign(M.word("LRLR"), -1)
    assert any(x["matrix"] == u for x in failures)
    assert all(x["eps"] == -1 and x["level"] % 2 == 0 for x in failures)


@pytest.mark.parametrize("callback", [lambda: M.word("X"), lambda: M.sign(M.I, 0),
                                    lambda: M.power(M.L, -1), lambda: M.fibre_smith(M.I),
                                    lambda: M.covered("LR", 1, 1, 0)])
def test_invalid_inputs_do_not_silently_pass(callback):
    with pytest.raises(ValueError):
        callback()
