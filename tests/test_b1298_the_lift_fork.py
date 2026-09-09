"""B1298 -- THE LIFT FORK: the DESIGN is sealed, the twelve signs and the inner lift reproduce by RUNNING, the seat re-run receipts are present."""
import hashlib, json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1298_the_lift_fork"; VER = ARC / "verification"


def _run(script, cwd):
    r = subprocess.run([sys.executable, str(VER / script)], capture_output=True, text=True, cwd=str(cwd))
    assert r.returncode == 0, r.stdout[-2500:] + r.stderr[-2500:]
    return r.stdout


def test_the_design_is_sealed_and_names_its_predictions():
    h = hashlib.sha256((ARC / "DESIGN.md").read_bytes()).hexdigest()
    assert f"{h}  DESIGN.md" in (ARC / "DESIGN.sha256").read_text(encoding="utf-8")
    d = (ARC / "DESIGN.md").read_text(encoding="utf-8")
    assert "P1 (the germ's lift)" in d and "P2 (fc's inner lift)" in d and "FAIL" in d


def test_the_twelve_signs_reproduce_by_RUNNING(tmp_path):
    out = _run("b1298_signs.py", tmp_path)
    assert out.rstrip().endswith("B1298 SIGNS: PASS"), out[-800:]
    j = json.loads((tmp_path / "b1298_signs.json").read_text(encoding="utf-8"))
    assert j["S"]["det"] == "(-1)" and j["P"]["det"] == "(1)"
    assert [j["S"]["eps"][str(k)] for k in range(0, 23, 2)] == ["(-1)", "(1)"] * 6
    assert all(j["P"]["eps"][str(k)] == "(1)" for k in range(0, 23, 2))
    assert "the six deformation classes: {'V2 (f4)': '(1)', 'V8 (26)': '(-1)', 'V10 (f4)': '(1)', 'V14 (f4)': '(1)', 'V16 (26)': '(-1)', 'V22 (f4)': '(1)'}" in out


def test_the_inner_lift_reproduces_on_main_s_E6(tmp_path):
    out = _run("b1298_inner_lift.py", tmp_path)
    assert out.rstrip().endswith("P2: PASS"), out[-600:]
    j = json.loads((tmp_path / "b1298_inner_lift.json").read_text(encoding="utf-8"))
    assert j["inner2"] == {"fixed": 32, "type": ["A1", "A5"]} and j["inner3"] == {"fixed": 18, "type": ["A2", "A2", "A2"]} and j["outer"]["fixed"] == 24


def test_the_seat_scripts_were_rerun_here_and_passed():
    for name in ("fc_r72_inner_lift_rerun.txt", "sm_b1280_theta_odd_pairing_rerun.txt", "fc_r71_seats_on_the_cusp_rerun.txt",
                 "fc_r71_theta_even_pairing_rerun.txt", "fc_r72c_d2_is_the_so10_axis_rerun.txt"):
        t = (VER / name).read_text(encoding="utf-8")
        assert "SELFTEST: PASS" in t and t.rstrip().endswith("RC=0"), name
    hl = (ROOT / "docs" / "HARVEST_LEDGER.md").read_text(encoding="utf-8")
    assert hl.count("| B1298 |") >= 6 and hl.count("| B1302 |") >= 1 and "sm:B1280 Theorem 2" in hl and "R72 §1" in hl


def test_I28_is_registered_unearned_and_joins_I27_s_source():
    b = json.loads((ROOT / "docs" / "IDENTIFICATION_BASELINE.json").read_text(encoding="utf-8"))
    # replay the audit trail instead of pinning a snapshot: the last raise with a "to" plus one per later raise without one
    raises = b["_baseline_raises"]; last_to = max(r["to"] for r in raises if "to" in r); later = sum(1 for r in raises if "to" not in r)
    assert b["unearned"] == last_to + later and "I-28" in b["rows"]
    raise_ = next(r for r in b["_baseline_raises"] if r.get("row") == "I-28")
    assert raise_["from"] == 11 and raise_["to"] == 12 and raise_["arc"] == "B1298"
    led = (ROOT / "docs" / "IDENTIFICATION_LEDGER.md").read_text(encoding="utf-8")
    row = next(l for l in led.splitlines() if l.startswith("| I-28 |"))
    assert "**UNEARNED**" in row and "paying I-27 pays this" in row
