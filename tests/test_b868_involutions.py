"""Locks B868 -- the three involutions separated."""
import importlib.util
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B868_three_involutions"
_S = importlib.util.spec_from_file_location("b868", _D / "three_involutions.py")
b8 = importlib.util.module_from_spec(_S)
_S.loader.exec_module(b8)
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def test_A4_label_map_is_dynkin_reversal():
    assert b8.minus_w0_A4((1, 0, 0, 0)) == (0, 0, 0, 1)   # 5 -> 5bar
    assert b8.minus_w0_A4((0, 1, 0, 0)) == (0, 0, 1, 0)   # 10 -> 10bar


def test_D5_label_map_is_spinor_swap():
    assert b8.minus_w0_D5((0, 0, 0, 0, 1)) == (0, 0, 0, 1, 0)   # 16 -> 16bar


def test_so10_fixed_core_is_so9():
    tot, fx = b8.so10_fixed_core_dim()
    assert (tot, fx) == (45, 36)


def test_the_gate_is_linear_no_c_anywhere():
    assert RES["gate_is_linear"] is True
    assert RES["ok"] is True


def test_the_d_type_subtlety_is_recorded():
    """On so(n) in the vector realization X -> -X^T is the IDENTITY; a naive matrix check
    would silently verify nothing. The weight-lattice statement is the uniform one."""
    assert "identity" in _F and "det = −1".lower().replace("*","") in _F or "det = -1" in _F


def test_c_is_placed_at_layer_8_only():
    assert "layer 8" in _F
    assert "cannot recur" in _F
