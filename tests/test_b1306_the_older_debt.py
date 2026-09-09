"""B1306 slice A -- THE OLDER DEBT: the DESIGN_A is sealed; the criterion check is pinned from its run (and runs live under OA_SLOW); the alias
table's reserved ranges include the seat's; the receipts index and the inventories are present."""
import hashlib, json, os, subprocess, sys
from pathlib import Path
import pytest
ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1306_the_older_debt"; SM = ARC / "verification" / "sm_new"


def test_slice_a_design_is_sealed():
    h = hashlib.sha256((ARC / "DESIGN_A.md").read_bytes()).hexdigest()
    assert f"{h}  DESIGN_A.md" in (ARC / "DESIGN_A.sha256").read_text(encoding="utf-8")


def test_the_criterion_check_is_pinned_from_its_run():
    j = json.loads((SM / "b1306_tower_criterion.json").read_text(encoding="utf-8"))
    assert j["fails"] == []
    assert {int(k): v["support"] for k, v in j["levels"].items()} == {3: 3, 4: 0, 5: 20, 6: 27, 7: 56, 8: 0, 9: 147}
    assert all(v["bad_rank"] == 0 and v["bad_det"] == 0 and v["bad_chain"] == 0 for v in j["levels"].values())
    assert j["Y20"]["order41_support"] == 0 and j["Y20"]["order11_support"] == 20
    assert j["Y12_2adic"] == {"2": 3, "8": 24, "16": 96} and j["Y24_2adic"] == {"2": 3, "8": 24, "16": 96}


@pytest.mark.slow
def test_the_criterion_check_reproduces_by_RUNNING(tmp_path):
    if not os.environ.get("OA_SLOW"):
        pytest.skip("OA_SLOW=1 runs the full Fox calculus to Y_9 (several minutes)")
    r = subprocess.run([sys.executable, str(SM / "b1306_tower_criterion.py")], capture_output=True, text=True, cwd=str(tmp_path), timeout=3600)
    assert r.returncode == 0 and "support 147 by order {2: 3, 19: 36, 38: 108}" in r.stdout and r.stdout.rstrip().endswith("Q1-Q3: PASS")


def test_the_reserved_ranges_cover_the_seat_and_the_alias_table_names_the_collisions():
    src = (ROOT / "tests" / "test_b1277_alias_table.py").read_text(encoding="utf-8")
    assert "(1308, 1319)" in src and "(1350, 1399)" in src
    tab = (ROOT / "docs" / "SM_SEAT_ALIAS_TABLE.md").read_text(encoding="utf-8")
    assert "the_two_by_two_criterion" in tab and "the_two_adic_tower" in tab and "B1350–B1399" in tab and "B1320" in tab


def test_the_receipts_and_inventories_are_present():
    for f in ("sm_B1303_criterion_rerun.txt", "sm_B1304_two_lemmas_rerun.txt", "sm_B1304_two_adic_lines_rerun.txt"):
        assert (SM / f).read_text(encoding="utf-8", errors="replace").rstrip().endswith("RC=0"), f
    assert (SM / "RECEIPTS.md").exists() and (SM / "already_banked_at_seal.txt").exists()
    for f in ("sm_seat_inventory.md", "fc_codex_hostile_inventory.md"):
        assert (ARC / "inputs" / f).exists(), f


# ---------------- slice B ----------------
SB = ARC / "verification" / "sliceB"


def test_slice_b_design_is_sealed():
    h = hashlib.sha256((ARC / "DESIGN_B.md").read_bytes()).hexdigest()
    assert f"{h}  DESIGN_B.md" in (ARC / "DESIGN_B.sha256").read_text(encoding="utf-8")


def test_slice_b_positive_half_is_pinned_from_its_run():
    j = json.loads((SB / "b1306_positive_half.json").read_text(encoding="utf-8"))
    assert j["fails"] == [] and j["pairs_m_le_4000"] == 1037 and j["mismatches"] == []
    t = {int(k): v for k, v in j["table"].items()}
    assert [t[n]["classes"] for n in range(2, 14)] == [1, 0, 1, 2, 1, 2, 1, 2, 5, 2, 1, 2]
    assert all(t[n]["carry"] == t[n]["predicted"] and t[n]["both_even_carry"] == 0 for n in t)
    assert (t[10]["predicted"], t[10]["both_even"]) == (2, 3)


def test_slice_b_colored_jones_tail_is_pinned_from_its_run():
    j = json.loads((SB / "b1306_jones_52_N9.json").read_text(encoding="utf-8"))
    assert j["fails"] == [] and j["m52_orientation"] == "as-is"
    m = {int(k): v for k, v in j["m52"].items()}
    assert [(m[n]["lo"], m[n]["hi"]) for n in (6, 7, 8, 9)] == [(5, 80), (6, 111), (7, 147), (8, 188)]
    assert m[9]["stable_bottom"][:8] == [1, -1, 0, 1, 0, 0, -1, 0] and m[9]["stable_top"] == []
    assert abs(float(j["inv_phi_growth"]["3000"]) - 1.2880) < 0.002


def test_slice_b_park_eq32_defect_is_pinned():
    j = json.loads((SB / "b1306_park_eq32.json").read_text(encoding="utf-8"))
    assert j["fails"] == [] and j["x72"].startswith("-1q^12 +1q^13 -1q^15 +1q^18") and j["x72"] == j["target"]
    assert j["f3_diff"].startswith("+1q^3 -1q^4 +1q^5 +1q^6")


def test_slice_b_receipts_present_and_green():
    for f in ("sm_B1304_law_positive_half_rerun.txt", "sm_B1303_presentations_h1_all_characters_rerun.txt", "sm_B1350_obstruction_rerun.txt",
              "sm_B1350_obstruction_higher_rerun.txt", "cloud_memo183_park_large_color_rerun.txt", "cloud_memo183_park_ahat_erratum_rerun.txt", "cloud_memo184_tail_52_rerun.txt"):
        assert (SB / f).read_text(encoding="utf-8", errors="replace").rstrip().endswith("RC=0"), f
    assert "SELFTEST: PASS" in (SB / "sm_B1304_law_positive_half_rerun.txt").read_text(encoding="utf-8")
    assert "ALL CONTROLS PASSED" in (SB / "cloud_memo184_tail_52_rerun.txt").read_text(encoding="utf-8")


def test_slice_b_the_two_locks_read_tracked_records():
    for f in ("frontier/B1299_the_period_2_duality/verification/b1299_w1w2_main_run.txt", "frontier/B1302_the_sibling_m202/verification/b1302_signs_run.txt"):
        assert (ROOT / f).is_file(), f
        r = subprocess.run(["git", "-C", str(ROOT), "ls-files", "--error-unmatch", f], capture_output=True, text=True); assert r.returncode == 0, f
    src = (ROOT / "tests" / "test_b1299_the_period_2_duality.py").read_text(encoding="utf-8"); assert "b1299_w1w2_main_run.txt" in src and ".out" not in src
    src = (ROOT / "tests" / "test_b1302_the_sibling_m202.py").read_text(encoding="utf-8"); assert "b1302_signs_run.txt" in src and ".out" not in src


@pytest.mark.slow
def test_slice_b_positive_half_reproduces_by_RUNNING(tmp_path):
    r = subprocess.run([sys.executable, str(SB / "b1306_positive_half.py"), "9"], cwd=tmp_path, capture_output=True, text=True, timeout=1200)
    assert r.returncode == 0 and "Q1: PASS" in r.stdout, r.stdout[-1500:] + r.stderr[-1500:]
