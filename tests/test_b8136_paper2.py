"""Lock: Paper II's banked claims match the paper and its verification."""
import json, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "frontier/B8136_paper2_drafted/results.json").read_text())

def test_master_formula_and_finite_image():
    inh = R["inherited_from_B8078_rerun"]
    assert "flat-function of 30 hyperplanes in a 4-space" in inh["master_formula"]
    assert inh["image"]["n_flats"] == 109
    assert inh["image"]["spectrum"] == [12, 14, 16, 18, 20, 26, 28, 30, 36, 46, 78]
    assert inh["image"]["all_attained"] is True

def test_the_46_is_inaccessible_not_merely_rare():
    s = R["inherited_from_B8078_rerun"]["the_46"]
    assert "IRREDUCIBLE" in s and "INACCESSIBLE over Q" in s
    assert "DERIVED as the exponent" in s          # not recorded as 46-30

def test_C_is_forced_and_the_mckay_partner_is_load_bearing():
    n = R["new_in_paper2"]
    assert "{8,14,16,22}" in n["statement"]
    assert n["controls_that_make_it_nontrivial"]["2O"].startswith("D(2O) cap E = [8, 16]")
    assert n["controls_that_make_it_nontrivial"]["2I"].startswith("D(2I) cap E = []")

def test_the_octahedral_mislabel_is_recorded_not_quietly_fixed():
    e = R["my_own_error_caught_mid_draft"]
    assert "BINARY OCTAHEDRAL" in e["what"]
    assert "8, 12, 18" in e["why_wrong"]           # 2O's real degrees
    assert "STRONGER" in e["effect"]

def test_the_qbar_residue_is_registered_open():
    assert "REGISTERED AS OPEN" in R["scope"]["three_faithful_primes_only"]
    assert any("OA-C0006" in x for x in R["scope"]["not_claimed"])

def test_forcing_suite_runs_green():
    v = ROOT / "papers/series/paper2_rung_spectrum/verify/check_forcing.py"
    r = subprocess.run([sys.executable, str(v)], capture_output=True, text=True, cwd=v.parent)
    assert r.returncode == 0, r.stdout[-2000:]
    assert "13/13 checks passed" in r.stdout
