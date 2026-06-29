"""B282 lock -- the figure-eight's E6 is ARITHMETIC, not geometric: the 2T surjection (sole McKay-E6 source) is
present only for the arithmetic cusped manifolds (4_1, m003) and absent for non-arithmetic hyperbolic knots, while
the character-variety E6 structure is generic to all (B281, R6). FIREWALLED; nothing to CLAIMS.md.
(Heavy SnapPy+GAP reproduced by sage-python e6_specificity_gap.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B282_e6_is_arithmetic_not_geometric" / "verdict.py"
_spec = importlib.util.spec_from_file_location("b282", _PATH)
b282 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b282)


def test_2T_is_arithmetic_specific():
    assert all(b282.SURJECTIONS_2T[k] > 0 for k in b282.ARITHMETIC)          # arithmetic -> 2T
    assert all(v == 0 for k, v in b282.SURJECTIONS_2T.items() if k not in b282.ARITHMETIC)  # non-arith -> none
    assert b282.verdict()


def test_only_arithmetic_content_is_object_specific():
    # the sole object-specific E6 facts trace to the arithmetic; the rest is generic
    assert any("2T" in s for s in b282.OBJECT_SPECIFIC)
    assert any("MFP" in s or "any G" in s for s in b282.GENERIC)
