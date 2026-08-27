"""Lock: every paper names its verification script and states a count matching the live suite."""
import json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "frontier/B8151_verified_vs_used_sweep/results.json").read_text())
S = ROOT / "papers/series"

EXPECTED = {"paper1_characterization": ("check_locus", 15),
            "paper2_rung_spectrum":    ("check_forcing", 13),
            "paper3_one_loop":         ("check_n2_abscissa", 5),
            "paper4_what_cannot_be_supplied": ("check_family", 7)}

def test_every_paper_names_its_script_and_count():
    for pap, (script, n) in EXPECTED.items():
        tex = (S / pap / "main.tex").read_text()
        assert script.replace("_", r"\_") in tex, pap
        assert re.search(r"\b%d\b" % n, tex), (pap, n)

def test_no_paper_points_only_at_a_bare_directory():
    for pap in EXPECTED:
        tex = (S / pap / "main.tex").read_text()
        assert "reproduced by \\texttt{verify/}," not in tex, pap

def test_the_defect_is_checkability_not_correctness():
    assert "defect of CHECKABILITY" in json.loads(
        (ROOT / "frontier/B8151_verified_vs_used_sweep/arc_verdict.json").read_text())["creates_law"]

def test_papers_I_and_II_passed_the_quantifier_audit():
    u = R["universal_quantifier_audit"]
    assert u["paper_I"].startswith("PASS") and u["paper_II"].startswith("PASS")

def test_the_single_failure_mode_is_named():
    assert "wider than" in R["the_pattern_across_the_session"]
