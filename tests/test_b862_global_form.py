"""Locks B862 -- the Z6 global form."""
import importlib.util
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B862_global_form"
_S = importlib.util.spec_from_file_location("b862", _D / "global_form.py")
b2 = importlib.util.module_from_spec(_S)
_S.loader.exec_module(b2)
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split())


def test_the_kernel_is_exactly_Z6():
    assert b2.kernel_elements() == [0, 1, 2, 3, 4, 5]
    assert RES["kernel_order"] == 6


def test_the_ambiguity_and_the_source_are_named():
    assert "1705.01853" in _F
    assert "ℤ₆" in (_D / "FINDINGS.md").read_text(encoding="utf-8")


def test_conditionality_is_stated():
    assert "Conditional on the cascade" in _F
    assert "P5" in _F


def test_the_wall_layer_is_not_claimed():
    assert "remain open" in _F and "B715" in _F
