"""B813 — locks the type audit's three mismatches and B812's updated entry."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B813_cs_theta_type_audit"


def test_the_three_mismatches_are_recorded():
    t = (ARC / "FINDINGS.md").read_text()
    for term in ("PSL(2,ℂ)", "SU(3)", "free coupling", "coefficient", "functional"):
        assert term in t, f"the type audit must name {term}"
    assert "F1 FIRES" in t


def test_the_refutation_is_scoped_not_overread():
    """It refutes the DIRECT identification, not every possible construction."""
    t = (ARC / "FINDINGS.md").read_text()
    assert "does" in t and "not** prove that no construction" in t.replace("\n", " ")


def test_b812_theta_entry_remains_the_most_advanced_and_M_blocked():
    """B813 supplies the reason for M; the axis assignment itself must not have moved."""
    m = json.loads((ROOT / "frontier" / "B812_physics_path_map" / "map.json").read_text())
    t = [x for x in m if "theta_QCD" in x["target"]][0]
    assert (t["S"], t["V"], t["C"], t["M"]) == ("no", "no", "no", "NO")
