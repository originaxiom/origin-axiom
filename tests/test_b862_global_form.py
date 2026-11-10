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


def test_the_kernel_is_computed_from_the_map():
    """B1862 (the advisor seat's audit, E6): exact, from the diagonal phases of g(A, B, a); complete on the grid of
    sixths; cyclic. A different map gives a different kernel, so the computation can tell."""
    from fractions import Fraction as Fr
    ker = b2.kernel_exact(6)
    assert len(ker) == len(b2.kernel_exact(12)) == len(b2.kernel_exact(72)) == 6
    assert max(b2._order(g) for g in ker) == 6 and sorted(b2._order(g) for g in ker) == [1, 2, 3, 3, 6, 6]
    assert (Fr(1, 3), Fr(1, 2), Fr(1, 6)) in ker                  # the generator: A = e^{2 pi i/3}, B = -1, a = 2 pi/6
    # the same enumeration for another map, diag(A e^{-ia}, B e^{ia}), finds the identity alone
    other = [(al, be, Fr(n, 6)) for al in (Fr(0), Fr(1, 3), Fr(2, 3)) for be in (Fr(0), Fr(1, 2)) for n in range(6)
             if (al - Fr(n, 6)) % 1 == 0 and (be + Fr(n, 6)) % 1 == 0]
    assert len(other) == 1 and len(other) != len(ker)


def test_the_ambiguity_and_the_source_are_named():
    assert "1705.01853" in _F
    assert "ℤ₆" in (_D / "FINDINGS.md").read_text(encoding="utf-8")


def test_conditionality_is_stated():
    assert "Conditional on the cascade" in _F
    assert "P5" in _F


def test_the_wall_layer_is_not_claimed():
    assert "remain open" in _F and "B715" in _F
