"""Locks B885 -- the inter-breaking dictionary."""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B885_interbreaking"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def test_all_three_gradings_canonical():
    assert RES["coarse_dims"] == [[1, 10, 16]] * 3


def test_law1_vacuum_to_higgs_all_pairs():
    for pair in ("01", "02", "12"):
        row = RES["coarse"][pair][0]
        assert row[0] < 1e-18 and row[2] < 1e-18
        assert abs(row[1] - 1.0) < 1e-12


def test_law2_sixteen_vacuum_exclusion_all_pairs():
    for pair in ("01", "02", "12"):
        assert RES["coarse"][pair][2][0] < 1e-18


def test_the_ten_spreads_and_rows_normalize():
    for pair in ("01", "02", "12"):
        for i in range(3):
            assert abs(sum(RES["coarse"][pair][i]) - 1.0) < 1e-9
        assert all(x > 0.01 for x in RES["coarse"][pair][1])


def test_fine_pattern_recorded_as_convention():
    assert RES["fine"]["01"]["zeros"] == 13
    assert RES["fine"]["01"]["total"] == 121
    assert "no fine numbers are claimed" in _F


def test_honesty_and_the_flag():
    assert "nothing resembling a mixing matrix of values is computed or claimed" in _F
    assert "magnitudes are not" in _F
    assert "flagged for the joint queue" in _F
