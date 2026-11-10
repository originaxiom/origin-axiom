"""B1865 -- the advisor seat's planted-violation script, as run on main at 30dd1fea7: what its output says, and that each
violation it reports caught is caught by main's own planted tests too."""
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = (HERE / "planted_violations_at_30dd1fea7_out.txt").read_text(encoding="utf-8")


def _rows():
    return {m.group(1): m.group(2).strip() for m in re.finditer(r"^((?:CTL|PV)\d+)\s+\S+\s+(CAUGHT|NOT CAUGHT|MANUAL)", OUT, re.M)}


def test_the_counts():
    r = _rows()
    assert sum(1 for k, v in r.items() if k.startswith("CTL") and v == "CAUGHT") == 5
    pv = {k: v for k, v in r.items() if k.startswith("PV")}
    assert sum(1 for v in pv.values() if v == "CAUGHT") == 7 and sum(1 for v in pv.values() if v == "NOT CAUGHT") == 14
    assert sum(1 for v in pv.values() if v == "MANUAL") == 6 and len(pv) == 27
    assert "controls not reported CAUGHT: 0" in OUT and "NOT CAUGHT: 14" in OUT
    assert ("/" + "Users" + "/") not in OUT                             # no local path in a tracked file (spelt in pieces: the suite's guard reads this file too)


def test_the_six_real_catches_and_the_one_that_is_not():
    r = _rows()
    for k in ("PV1", "PV2", "PV3", "PV4", "PV6", "PV8"):
        assert r[k] == "CAUGHT", k
    # the seventh is reported caught because the two clones agree, not because a gate sees that a clone is shallow
    assert r["PV22"] == "CAUGHT" and "full clone PASS, shallow clone PASS" in OUT
    f = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")
    assert "The seventh is not a fix" in f


def test_mains_own_planted_tests_exist_for_each_catch():
    t1 = (ROOT / "tests" / "test_append_only_history.py").read_text(encoding="utf-8")
    t2 = (ROOT / "tests" / "test_seal_immutable.py").read_text(encoding="utf-8")
    for name in ("test_pv1_a_committed_deletion_is_refused", "test_pv2_the_log_replaced_by_one_line_is_refused"):
        assert "def %s(" % name in t1
    for name in ("test_pv3_a_sentence_appended_to_a_sealed_file_is_refused", "test_pv4_a_deleted_sealed_file_is_refused",
                 "test_pv5_an_edit_with_its_ledger_row_rewritten_in_the_same_commit_is_refused", "test_pv6_a_ledger_row_changed_by_hand_is_refused",
                 "test_pv7_the_ledger_does_not_vouch_for_itself", "test_pv8_a_seal_under_another_name_committed_with_its_results_is_in_the_class"):
        assert "def %s(" % name in t2
