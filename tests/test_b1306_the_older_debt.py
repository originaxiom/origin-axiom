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


# ---------------- slice C ----------------
SC = ARC / "verification" / "sliceC"


def test_slice_c_design_is_sealed():
    h = hashlib.sha256((ARC / "DESIGN_C.md").read_bytes()).hexdigest()
    assert f"{h}  DESIGN_C.md" in (ARC / "DESIGN_C.sha256").read_text(encoding="utf-8")


def test_slice_c_own_rederivations_are_pinned():
    j = json.loads((SC / "c_su3_level2.json").read_text(encoding="utf-8")); assert j["ok"] and (j["order"], j["ordT"], j["classes"]) == (2880, 15, 63) and j["texp"] == [13, 2, 8, 2, 7, 8]
    j = json.loads((SC / "c_geodir_h1.json").read_text(encoding="utf-8")); assert j["ok"] and j["total"] == 6
    j = json.loads((SC / "c_positivity_bridge.json").read_text(encoding="utf-8")); assert j["ok"] and (j["words"], j["rotation_classes"], j["invariants"]) == (2026, 241, 241)
    j = json.loads((SC / "c_kac_classes.json").read_text(encoding="utf-8")); assert j["ok"] and j["labellings"] == 170 and j["dims"] == {"24": 80, "30": 90} and j["coldims"] == {"24": 40, "30": 45}
    j = json.loads((SC / "c_tits_lift.json").read_text(encoding="utf-8")); assert j["ok"] and j["order3"] and (j["mult_1"], j["mult_omega_pair"]) == (24, 54)
    j = json.loads((SC / "c_unit_dictionary.json").read_text(encoding="utf-8")); assert j["ok"] and j["n"] == 16
    # ADOPTED from the paper-verification seat (8dac820e), which reached this the other way:
    # it regenerates when the artifact is absent rather than shipping it.  Both halves are kept
    # deliberately -- the artifacts ARE committed here (with a .gitignore negation), so this takes
    # the fast path in this repository, and the fallback keeps the lock runnable in any clone that
    # does not have them, including one predating the negation.
    for script, needle in (("c_beat.py", "C10: PASS"), ("c_e8_types.py", "C5 (w_{A2} half): PASS")):
        shipped = SC / (script[:-3] + ".out")
        text = shipped.read_text(encoding="utf-8") if shipped.is_file() else subprocess.run(
            [sys.executable, str(SC / script)], capture_output=True, text=True, timeout=600, cwd=SC).stdout
        assert needle in text, (script, text[-1500:])


def test_slice_c_seventeen_reruns_green():
    recs = sorted(p.name for p in SC.glob("*_rerun.txt")); assert len(recs) == 17, recs
    for f in recs:
        assert (SC / f).read_text(encoding="utf-8", errors="replace").rstrip().endswith("RC=0"), f


def test_i29_registered_with_the_baseline_migrated():
    led = (ROOT / "docs" / "IDENTIFICATION_LEDGER.md").read_text(encoding="utf-8"); assert "| I-29 |" in led and "listener map" in led.split("| I-29 |")[1][:200]
    base = json.loads((ROOT / "docs" / "IDENTIFICATION_BASELINE.json").read_text(encoding="utf-8")); assert "I-29" in base["rows"] and base["unearned"] == len(base["rows"])
    assert any(r.get("row") == "I-29" for r in base.get("_baseline_raises", []))


# ---------------- slice D ----------------
def test_slice_d_every_index_id_has_a_row_and_scheduled_is_counted(tmp_path):
    out = tmp_path / "r.json"
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "checks" / "harvest_debt.py"), "--json", str(out), "--quiet"], capture_output=True, text=True, timeout=600)
    assert r.returncode in (0, 2), r.stdout[-1500:]
    rep = json.loads(out.read_text(encoding="utf-8"))
    for k, s in rep["seats"].items():
        if "skipped" in s: continue
        # an item the seat pushed after its pin is the gate's NEW debt, not slice D's: the backlog may only contain such items
        assert set(s["backlog"]) <= set(s["new_unrowed"]) and s["stale_rows"] == [], (k, s["backlog"][:5], s["stale_rows"][:5])
    # ADOPTED from the paper-verification seat (8dac820e): every seat is SKIPPED when its branch is
    # not fetched (a plain clone), and the gate then never emits a scheduled-row total, so the
    # counter is only meaningful where at least one seat was read.
    if all("skipped" in s for s in rep["seats"].values()):
        pytest.skip("no seat branch fetched in this clone; the SCHEDULED counter has nothing to count")
    assert rep["summary"]["scheduled_rows"] > 0 and "SCHEDULED rows" in r.stdout
    assert (ARC / "verification" / "sliceD" / "rows.md").is_file() and (ARC / "FINDINGS_D.md").is_file()
