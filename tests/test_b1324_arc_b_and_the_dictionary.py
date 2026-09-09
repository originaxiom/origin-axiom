"""B1324 -- Arc B + the dictionary: the DESIGN is sealed; the cover census is pinned (66 chiral of 87, methods agree, six live one-cusped covers);
the index on the chiral covers has no live nonzero sector and 136 zero control sectors; the dictionary identity holds on m004, the census and the
covers; the four-record probe fails as pre-registered; Parts C and D re-run live under OA_SLOW."""
import hashlib, json, os, subprocess, sys
from pathlib import Path
import pytest
ROOT = Path(__file__).resolve().parents[1]; ARC = ROOT / "frontier" / "B1324_arc_b_and_the_dictionary"; V = ARC / "verification"


def _j(name):
    return json.loads((V / name).read_text(encoding="utf-8"))


def test_design_is_sealed():
    h = hashlib.sha256((ARC / "DESIGN.md").read_bytes()).hexdigest()
    assert f"{h}  DESIGN.md" in (ARC / "DESIGN.sha256").read_text(encoding="utf-8")


def test_part_a_census_pinned():
    a = _j("a_arc_b_census.json")
    assert a["covers"] == 87 and a["per_degree"] == {str(d): n for d, n in zip(range(2, 11), [1, 1, 2, 4, 11, 9, 10, 11, 38])} and a["b1295_mismatches"] == []
    assert a["chiral_total"] == 66 and a["amphichiral_total"] == 21 and a["methods_disagree"] == []
    assert a["by_type_total_and_chiral"] == {"cyclic": [9, 0], "irregular": [77, 66], "regular": [1, 0]}
    assert a["A1_covers_inherit_amphichirality"] is False and a["A2_chiral_one_cusped_3_divisible"] is True and a["A3_identity_holds_on_all_one_cusped"] is True
    assert sorted(tuple(x[:2]) for x in a["one_cusped_chiral_with_3_divisible_torsion"]) == [(6, 4), (6, 9), (8, 0), (8, 2), (9, 6), (9, 10)]
    assert a["one_cusped"] == 23
    full = [[-1, -1, 1], [-1, 1, -1], [1, -1, -1], [1, 1, 1]]
    for k, v in a["triple_sets_one_cusped"].items():
        if "cyclic" in k: assert sorted(map(list, v)) == full, k


def test_part_b_index_pinned():
    b = _j("b_index_on_chiral_covers.json")
    assert b["live_nonzero"] == [] and b["protected_nonzero"] == [] and b["PASS_B"] is False
    assert b["live_sectors"] == 2 and b["protected_sectors"] == 4 and b["control_sectors"] == 136
    live = [(c["degree"], c["index"], s["order"], s["I"]) for c in b["covers"] if "sectors" in c and not c["amphichiral"] for s in c["sectors"] if not s["galois_protected"]]
    assert sorted(live) == [(8, 0, 3, 0), (8, 2, 3, 0)]
    assert b["identity_failures"] <= 1


def test_part_c_dictionary_pinned():
    c = _j("c_dictionary.json"); assert c["PASS"]
    c1 = c["C1"]; assert c1["identity det = s_m*s_l on all"] and c1["four patterns twice each"] and c1["kernel of D4 -> (Z/2)^2 has order"] == 2
    c2 = c["C2"]; assert c2["one-cusped H1=Z census manifolds to 7 tets"] == 2804 and c2["identity holds on every census isometry"]
    assert sorted(c2["fully symmetric (all four patterns)"]) == ["m004", "s726", "s912"]
    counts = c2["pattern sets -> count"]; assert sorted(counts.values()) == [3, 7, 2794]


def test_part_d_four_records_fails_as_preregistered():
    d = _j("d_four_records.json")
    assert d["records"] == 4 and d["min_trace"] == 4 and d["PASS"] is False
    assert d["charpolys_of_minimal"] == ["t**4 - 4*t**3 + 6*t**2 - 5*t + 1"]
    assert abs(d["theta4"] - 1.3802775690976) < 1e-9 and abs(d["dilatation"] - 2.220744) < 1e-5


@pytest.mark.skipif(not os.environ.get("OA_SLOW"), reason="live re-run of Parts C and D (about two minutes)")
def test_live_reruns_c_d():
    for script in ("c_dictionary.py", "d_four_records.py"):
        r = subprocess.run([sys.executable, str(V / script)], capture_output=True, text=True, cwd=str(V), timeout=1800)
        assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]

def test_part_b_tolerance_robustness():
    """nonzero indices occur only where the four identities fail; the two live sectors are zero with the identities intact at 1e-9, 1e-7 and 1e-5."""
    for name in ("b_index_tol1e-9.json", "b_index_on_chiral_covers.json", "b_index_tol1e-5.json"):
        b = _j(name)
        secs = [(c, s) for c in b["covers"] if "sectors" in c for s in c["sectors"]]
        assert len(secs) == 142
        assert [1 for c, s in secs if s["I"] != 0 and s["identities"]] == [], name
        live = sorted((c["degree"], c["index"], s["order"], s["I"], s["identities"]) for c, s in secs if not c["amphichiral"] and not s["galois_protected"])
        assert live == [(8, 0, 3, 0, True), (8, 2, 3, 0, True)], (name, live)
