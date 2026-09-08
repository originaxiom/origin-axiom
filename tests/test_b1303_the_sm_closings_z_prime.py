"""B1303 -- THE SM CLOSING'S Z': the DESIGN is sealed; Q0 (the two centralisers), Q1 (the Z' re-derivation), Q2 (the FCNC fork) and
Q3 (the lattice table + the Y_9 census) reproduce by RUNNING; Q4's arithmetic reproduces by running and its census is pinned from
its JSON; the seat receipts and the archived relay are present."""
import hashlib, json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1303_the_sm_closings_z_prime"; VER = ARC / "verification"


def _run(script, cwd, timeout=900):
    r = subprocess.run([sys.executable, str(VER / script)], capture_output=True, text=True, cwd=str(cwd), timeout=timeout)
    assert r.returncode == 0, r.stdout[-2500:] + r.stderr[-2500:]
    return r.stdout


def test_the_design_is_sealed():
    h = hashlib.sha256((ARC / "DESIGN.md").read_bytes()).hexdigest()
    assert f"{h}  DESIGN.md" in (ARC / "DESIGN.sha256").read_text(encoding="utf-8")


def test_q0_both_embeddings_reproduce_by_RUNNING(tmp_path):
    out = _run("b1303_centraliser.py", tmp_path)
    assert "CENTRALISER of the 14 inside the 64 (trivial summands): 0" in out and "CENTRALISER of the 14 inside the 64 (trivial summands): 2" in out
    assert out.count("of them colour singlets: 2") == 2 and out.rstrip().endswith("Q0: PASS")


def test_q1_the_z_prime_rederives_by_RUNNING(tmp_path):
    out = _run("b1303_zprime.py", tmp_path)
    assert "maximal F-flat coordinate subspaces: 85" in out and "every branch preserves the SM): 9" in out
    assert "[PASS] (d) the E6 part of the surviving U(1) is (5psi - 3chi)/2" in out and "three 27s: {'cubic': -20250" in out
    assert "27 * sum f^3 = -20250" in out and out.rstrip().endswith("Q1/Q1': PASS")


def test_q2_the_fcnc_fork_reproduces_by_RUNNING(tmp_path):
    out = _run("b1303_fcnc.py", tmp_path)
    assert "K_dmK 154, K_epsK_O1phase 1.72e+03" in out and "D_if_CKM_is_up_sector 48.7" in out
    assert "g = third family : |B_12| = 8.914e-05" in out and out.rstrip().endswith("Q2: PASS")
    j = json.loads((VER / "b1303_fcnc.json").read_text(encoding="utf-8"))
    assert j["norm"]["trQ2"] == 6210 and 1e-8 <= j["convention_control"]["fK156"] <= 3e-8 and j["caseII_third"]["Bs"] < 10 < j["caseI_first"]["K_dmK"]


def test_q3_the_lattice_table_and_the_y9_census_reproduce_by_RUNNING(tmp_path):
    import shutil; (tmp_path / "inputs").mkdir(); shutil.copy(VER / "inputs" / "e6_roots_qul.json", tmp_path / "inputs" / "e6_roots_qul.json")
    out = _run("b1303_dt.py", tmp_path)
    assert "'D': (-2, 0, 0)" in out and "determinant +-1" in out and "{'three_gen': 758593, 'su5_broken': 737568, 'sm_vacua': 706464, 'full': 568656}" in out
    assert out.rstrip().endswith("Q3: PASS")


def test_q4_is_pinned_from_its_run():
    j = json.loads((VER / "b1303_tower.json").read_text(encoding="utf-8"))
    assert j["fails"] == [] and {k: v["pred_odd"] for k, v in j["arith"].items()} == {"2": 0, "3": 0, "4": 0, "5": 20, "6": 0, "7": 56, "8": 0, "9": 36, "10": 20, "11": 396, "12": 0}
    assert j["Y12"]["census"] == {"three_gen": 190849, "su5_broken": 181440, "sm_vacua": 34752, "full": 3264} and j["Y12"]["Dtot"] == {"1": 31488, "3": 3264}
    assert j["Y9"]["census"]["sm_vacua"] == 706464 and j["Y12"]["orders"] == {"1": 1, "16": 96}
    sums = (VER / "inputs" / "SHA256SUMS").read_text()
    for f in ("support_Y12.json", "support_Y9.json", "e6_roots_qul.json"):
        assert hashlib.sha256((VER / "inputs" / f).read_bytes()).hexdigest() in sums


def test_the_receipts_and_the_archived_relay_are_present():
    for f in ("sm_b1283_sm_closing_vacuum_rerun.txt", "sm_b1300_dt_structure_rerun.txt", "sm_b1301_tower_alphabet_rerun.txt", "sm_b1301_lines_from_support_Y12_rerun.txt",
              "main_b1140_spacetime64_rerun.txt", "main_b1103_being_gate_rerun.txt", "chat1_check_relay_rerun.txt"):
        t = (VER / f).read_text(encoding="utf-8", errors="replace"); assert t.rstrip().endswith("RC=0"), f
    assert "SELFTEST: PASS" in (VER / "sm_b1283_sm_closing_vacuum_rerun.txt").read_text() and "ALL CHECKS PASSED" in (VER / "main_b1103_being_gate_rerun.txt").read_text()
    assert (ARC / "CHAT1_TO_CC_2026-09-08_SESSION_RELAY.md").exists()
    assert hashlib.sha256((VER / "chat1_check_relay.py").read_bytes()).hexdigest().startswith("f71c2fd7")
