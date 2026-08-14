"""Locks B882 -- the magic-square naming and novelty scoping."""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B882_magic_square_naming"
FINDINGS = json.loads((_D / "priorart_findings.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def test_ten_angle_results_preserved():
    assert len(FINDINGS) == 10
    assert all("claims" in a and a["claims"] for a in FINDINGS)


def test_the_identification_is_source_confirmed():
    txt = json.dumps(FINDINGS).lower()
    assert "landsberg" in txt and "elduque" in txt and "barton" in txt
    assert "exactly the user's decomposition" in txt


def test_the_cyclic_law_prototype_is_quoted():
    txt = json.dumps(FINDINGS)
    assert "indices modulo 3" in txt or "indices taken modulo 3" in txt


def test_the_generations_lineage_is_recorded():
    txt = json.dumps(FINDINGS).lower()
    assert "ramond" in txt and "boyle" in txt and "furey" in txt
    assert "dubois-violette" in txt


def test_the_trialitarian_setting_is_found():
    txt = json.dumps(FINDINGS, ensure_ascii=False).lower()
    assert "cubic étale" in txt or "cubic etale" in txt
    assert "trialitarian" in txt


def test_novelty_scoping_is_honest():
    assert "classical — cite, never claim" in _F
    assert "prior art postulates the triality frame" in _F
    assert "none derives the frame" in _F
    assert "bibliography, not endorsement" in _F
