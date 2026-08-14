"""Locks B884 -- the invariant cubic and the Yukawa-support table."""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B884_yukawa_support"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def test_the_cubic_exact():
    assert RES["n_weight_zero_triples"] == 45
    assert RES["cubic_support"] == 45
    assert RES["cubic_coeff_values"] == [1]
    assert RES["nullspace_dim"] == 1


def test_the_grading():
    assert RES["piece_dims"] == [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 6]


def test_the_support_eleven_cells():
    assert len(RES["coupled"]) == 11
    assert RES["zero_triples"] == 275
    dims = sorted(tuple(sorted(c["dims"])) for c in RES["coupled"])
    from collections import Counter
    cnt = Counter(dims)
    assert cnt[(2, 3, 6)] == 3
    assert cnt[(1, 2, 2)] == 3
    assert cnt[(1, 3, 3)] == 3
    assert cnt[(3, 3, 3)] == 1
    assert cnt[(3, 6, 6)] == 1


def test_charge_conservation_on_coupled_cells():
    assert all(c["charge_norm"] < 1e-20 for c in RES["coupled"])


def test_honesty():
    assert "only the zero/nonzero support is basis-invariant" in _F
    assert "magnitude hierarchy" in _F and "not\nclaimed" in _F.replace("not claimed", "not\nclaimed")
    assert "no values, no textures" in _F


def test_addendum_support_is_purely_charge_forced():
    """11/286 charge-conserving == the 11 coupled cells; no dynamical zeros."""
    assert "exactly 11 — and they are the 11 coupled cells" in _F
    assert "conservation-forced" in _F
