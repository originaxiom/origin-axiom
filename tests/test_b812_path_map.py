"""B812 — locks the path map and the axis-distribution finding."""
import json
from pathlib import Path

ARC = Path(__file__).resolve().parents[1] / "frontier" / "B812_physics_path_map"


def _m():
    return json.loads((ARC / "map.json").read_text())


def test_no_target_clears_all_four_axes():
    """A genuine path is (S,V,C,M) = (no,no,no,yes). None exists."""
    genuine = [t for t in _m()
               if t["S"] == "no" and t["V"] == "no" and t["C"] == "no" and t["M"] == "yes"]
    assert genuine == [], f"a path cleared -- the map's verdict must be re-derived: {genuine}"


def test_the_dominant_blocker_is_M_not_a_proved_wall():
    """The finding: M (no computed mechanism) is an ABSENCE, and it blocks the most targets."""
    from collections import Counter
    c = Counter(t["killed_by"] for t in _m())
    assert c["M"] >= c["S"] + c["V"], (
        "if the proved walls (S, V) ever outnumber M, the map's central reading -- that the "
        "blocker is a missing derivation rather than an impossibility -- has changed")
    assert c["M"] == 5 and c["C"] == 3


def test_theta_qcd_is_the_most_advanced_entry_and_fails_only_M():
    t = [x for x in _m() if "theta_QCD" in x["target"]][0]
    assert (t["S"], t["V"], t["C"]) == ("no", "no", "no")
    assert t["M"] == "NO" and t["killed_by"] == "M"


def test_quasicrystal_is_killed_by_class_level_not_by_scale():
    """m004 is at kappa = -2; the Fibonacci Hamiltonian at kappa > 2. Different points."""
    t = [x for x in _m() if "quasicrystal" in x["target"]][0]
    assert t["S"] == "no", "the MATERIAL supplies the scale -- S must not be the blocker"
    assert t["killed_by"] == "C"
    assert "kappa = -2" in t["reason"] and "2+lambda^2" in t["reason"]
