"""B1689 -- W23, W24 and W44's c-gauge frame verified on main (P-229): live, W23's census (E6 {0,1}, SO(10) {0,1,2}, SU(5)
{(0,0),(1,3),(2,2)}) and W24's D2-D3 (the 248 on Q8 = (248, 24, 28) by two branchings; 55, 27, 56); the bite: an index
rule counting characters too changes W23's table. Stored: W24's K1-K2 (chi_orb 96, 32, 28 for V4, A4 and the rotation
group O; T_d gives 40) and F_c's block test (98 subgroups, 4096 pairs, none passing; the planted pattern passes)."""
import importlib.util, io, contextlib, json, pathlib
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1689_w23_w24_w44_verified" / "verification"


def _load(name):
    spec = importlib.util.spec_from_file_location(name + "_lock", A / (name + ".py"))
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    return m


def test_w23_live_and_the_bite():
    m = _load("main_w23")
    assert m.res["holds_as_recorded"] and m.res["max_complete_generations"] == 2
    wrong = lambda ch: sum(m.decompose(ch).values())                       # the bite: every block counted
    assert sorted({wrong(m.char_of(b)) for b in m.bundles(3)}) != m.res["E6_27xV_n3"]


def test_w24_gauge_side_and_stored_census():
    d = json.loads((A / "main_w24.json").read_text(encoding="utf-8"))
    assert d["D2"]["via_SU2xSU3xSU6"] == d["D2"]["via_G2xF4"] == {"1": 248.0, "-1": 24.0, "i": 28.0}
    assert (d["D3"]["trivial"], d["D3"]["each_character"], d["D3"]["rho"]) == (55.0, 27.0, 56.0) and all(d["D1"].values())
    k2 = {k: (v["chi_orb"], v["net_generations_standard_embedding"]) for k, v in d["K2"].items()}
    assert k2["V4"] == ("96", "48") and k2["A4"] == ("32", "16") and k2["O"] == ("28", "14") and k2["T_d (control, not Calabi-Yau)"][0] == "40"
    assert d["K1b"]["chi_generic"] == 6 and d["K1b"]["chi_at_-2"] == 5 and d["K1b"]["chi_at_2"] == 2 and d["K1b"]["fibration_check_chi_C3"] == 1


def test_w44_fc_block_test_stored():
    d = json.loads((A / "main_w44_fc.json").read_text(encoding="utf-8"))
    assert d["subgroups_of_O_h"] == 98 and d["pairs_tested"] == 4096 and d["pairs_passing_the_block_test"] == 0 and d["control_pattern_passes"]
