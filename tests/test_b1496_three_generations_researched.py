"""B1496 -- THREE GENERATIONS, RESEARCHED FIRST: main's own arithmetic checks, the archived report's shape, and the page's rows."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]; HERE = ROOT / "frontier" / "B1496_three_generations_researched" / "verification"


def test_the_shape_identity_and_the_orbifold_arithmetic_hold_on_main():
    c = json.load(open(HERE / "checks.json"))
    assert all(c[f"rank {n}: ch3(L2V) - (n-4) ch3(V)"] == "0" for n in range(2, 9))          # ch3(Lambda^2 V) = (n - 4) ch3(V), c1 = 0
    assert c["omega^3 = I"] is True and c["|det(omega - I)|"] == 3 and c["chi_orb(T^6/Z3) = (1/3)(chi(T^6) + 8*27)"] == "72"


def test_the_archived_report_and_its_verification_counts():
    r = json.load(open(HERE / "research_report.json"))
    assert r["stats"]["confirmed"] == 22 and r["stats"]["killed"] == 3 and r["stats"]["unverified"] == 0 and r["agentCount"] == 105
    assert len(r["findings"]) == 10 and len(r["refuted"]) == 3
    assert "/private/tmp" not in json.dumps(r) and ("/Us" + "ers/") not in json.dumps(r)      # no temporary or home paths in the archived report
    kinds = {f["claim"][:3] for f in r["findings"]}; assert any(f["confidence"] == "low" for f in r["findings"])      # the orbifold row is marked unverified


def test_the_page_carries_the_specification_and_its_statuses():
    p = (ROOT / "docs" / "THREE_GENERATIONS_RESEARCHED.md").read_text(encoding="utf-8")
    for row in ("(1) the count is an index", "(4) the shape: as many 5̄'s as 10's", "(6) nobody derives three", "(8) the orbifold mechanism", "(9) the E₈ family triplet"):
        assert row in p
    assert "UNVERIFIED in this run" in p and "UNADDRESSED" in p and "N_ν = 2.9963 ± 0.0074" in p and "one** rank-5 bundle" in p
