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
