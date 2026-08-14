"""Locks B864 -- the anomaly ledger."""
import importlib.util
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B864_anomaly_ledger"
_S = importlib.util.spec_from_file_location("b864", _D / "anomaly_ledger.py")
b4 = importlib.util.module_from_spec(_S)
_S.loader.exec_module(b4)
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split())


def test_parent_level_is_anomaly_free():
    assert RES["parent_all_free"] is True
    psi27, chi16 = b4.parent_level()
    assert all(v == 0 for v in psi27.values())
    assert all(v == 0 for v in chi16.values())


def test_dials_become_anomalous_over_the_chiral_matter():
    assert RES["dials_anomalous_over_chiral_matter"] is True
    psi16, chi_gen = b4.truncated_level()
    assert psi16 == {"tr": 16, "tr3": 16, "so10sq": 2}
    assert chi_gen == {"tr": 5, "tr3": 125}


def test_hypercharge_is_the_UNIQUE_gaugeable_direction():
    u = b4.uniqueness()
    assert u["b_c_zero"] is True
    assert u["miracle"] is True


def test_the_sm_generation_is_fully_Y_anomaly_free():
    y = b4.sm_hypercharge_free()
    assert y["all_zero"] is True


def test_the_L5_correction_is_recorded():
    """'automatic for complete SU(5) multiplets' was wrong; the cross-cancellation is the truth."""
    assert "wrong as stated" in _F
    assert "A(10)+A(5̄) = 0" in (_D / "FINDINGS.md").read_text(encoding="utf-8")


def test_the_scope_note_on_stripping_more_than_forced():
    assert "more" in _F and "not forced" in _F


def test_g2_is_not_claimed():
    assert "does not derive the re-anchoring" in _F
