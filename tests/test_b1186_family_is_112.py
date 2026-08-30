"""B1186 lock -- the family is 112; criteria nested; t06829 the certified corrective member."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1186_family_is_112"


def test_arc_verdict():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1186" and d["verdict"] == "PROVED"
    c = d["claim_one_line"]
    assert "|F| = 112" in c and "t06829" in c and "STRICTLY NESTED" in c
    assert "den bound 256" in c or "denominator bound" in c   # the bound is part of the claim


def test_census_artifact():
    d = json.loads((ARC / "verification" / "family_census.json").read_text(encoding="utf-8"))
    assert d["census_size"] == 212641
    assert d["B_shape_field_in_Qsqrt3"] == 112 == len(d["members_B"])
    assert d["A_all_regular"] == 77 == len(d["members_A"])
    assert "t06829" in d["members_B"] and "t06829" not in d["members_A"]
    assert d["amphichirality_failures"] == [] and d["quine_collisions"] == []
    assert set(d["carriers_2sqrt3i_excl_m004"]) == {
        "t12840", "o9_41001", "o9_41009", "o10_150684", "o10_150685", "o10_150693"}
    assert all(d["known_member_control"].values())


def test_results_and_fences():
    d = json.loads((ARC / "b1186_results.json").read_text(encoding="utf-8"))
    assert d["counts"] == {"census": 212641, "A_all_regular": 77,
                           "B_shape_field_Qsqrt3": 112, "B_not_A": 35, "cc3_reported": 111}
    assert d["corrective_member"]["max_shape_denominator"] == 98
    assert "double-cast" in d["self_caught_bug"]
    t = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "applies to B8152's own count" in t          # the recursion of the lesson
    assert "NOT a claim about all hyperbolic 3-manifolds" in t
