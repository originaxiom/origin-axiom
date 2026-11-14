"""B1939's lock: each item's kept run holds its verdicts and its plants (the line-count check re-run live, under a
minute is not needed: the kept outputs are held). The one failing WP-1.2 check is the expected one (the literal clause C,
which needs 'non-empty'); the first torsion run's plant P2 was mis-designed and its replacement is caught."""
import json, re, pathlib
HERE = pathlib.Path(__file__).resolve().parent
R = lambda n: (HERE / n).read_text()


def test_xc2_every_verdict_and_plant():
    t = R("xc2_flat_su5_lines_run.txt")
    assert "False" not in t and t.count("True") >= 12 and "exit 0" in t
    c = R("xc2_cover_degrees_run.txt")
    assert "all 12 halves, set of (I, O, Z, ZO) least k: {(6, 3, 3, 3)} 12" in c


def test_the_torsion_runs_and_their_plants():
    t = R("torsion_m004_and_golden_run.txt")
    assert "SUMMARY: fails = []" in t and "P1 caught" in t and "P3 caught" in t and "P4 caught" in t and "P5 caught" in t
    p2 = R("torsion_plant_p2_run.txt")
    assert p2.count("-> CAUGHT") == 3 and "MISSED" not in p2
    v = R("torsion_second_route_run.txt")
    assert v.count("CAUGHT") >= 3 and "MISSED" not in v
    assert "x*y = 0 mod 5: 9" in R("torsion_lattice_run.txt")


def test_the_chiral_three_and_the_global_form_plants():
    for f, keys in (("chiral_unit_out.json", ("C1", "C2", "C3", "C4")), ("global_form_out.json", ("C5a", "C5b"))):
        d = json.loads(R(f))["C"]["caught"]
        assert all(d[k] is True for k in keys), f


def test_wp12_only_the_expected_clause_fails():
    t = R("wp12_at_p2_run.txt")
    assert "CHECKS: 59, failing: 1; PLANTS: 7, caught: 7, missed: 0" in t
    fails = [l for l in t.splitlines() if l.startswith("FAIL ")]
    assert len(fails) == 1 and "C last clause, LITERAL" in fails[0]
    s = R("wp12_at_p2_second_route_run.txt")
    assert "CHECKS 51, failing 1; PLANTS 8, caught 8" in s


def test_the_stage1_items_pass_on_both_routes():
    for f in ("stage1_item3_stabiliser_signs_run.txt", "stage1_item4_psi_run.txt", "stage1_item3_second_route_run.txt", "stage1_item4_second_route_run.txt"):
        assert "FAILED CHECKS: none" in R(f), f
    assert "PASS sum over C of B1929's eta_A" in R("stage1_item4b_eta_cover_run.txt")
