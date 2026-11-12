"""B1897 lock -- B1881's lock tested by a session that did not write it.

What could fail: one of the six plants that passed passing again, or the control failing, in the committed result; the four tests
that hold the six leaving B1881's lock; a quotation of the reader not found at the commit it tested; the page giving another
count than the files; the page claiming that the open shape is closed."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
ROOT = HERE.parents[2]
PAGE = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
RES = json.loads((HERE / "planted_a_second_time.json").read_text(encoding="utf-8"))
LOCK = (ROOT / "frontier" / "B1881_the_whole_and_the_value_verified" / "verification" / "test_b1881_the_whole_and_the_value_verified.py").read_text(encoding="utf-8")
NEW = ("test_the_committed_run_is_what_the_script_gives_today", "test_the_conditions_of_the_mended_checks_are_the_ones_that_were_mended",
       "test_the_script_computes_what_it_says_it_computes", "test_the_withdrawn_word_stands_only_where_it_is_taken_back")


def test_the_six_that_passed_are_caught_now_and_the_control_passes():
    plants = RES["plants"]
    assert RES["control passes"] is True and plants[0]["tests failing"] == [] and plants[0]["plant"].startswith("control")
    six, eighteen = plants[1:7], plants[7:]
    assert len(six) == 6 and all(p["plant"].startswith("of the six that passed: ") for p in six)
    assert len(eighteen) == 18 and all(p["plant"].startswith("of B1895's eighteen: ") for p in eighteen)
    assert all(p["tests failing"] for p in six), [p["plant"] for p in six if not p["tests failing"]]
    assert all(p["tests failing"] for p in eighteen), [p["plant"] for p in eighteen if not p["tests failing"]]
    assert RES["of the six that passed, caught now"] == 6 and RES["of B1895's eighteen, caught"] == 18 and RES["caught"] == RES["of"] == 24
    # each of the six is caught by a test that this arc added, and each of the four added tests catches at least one of them
    by_new = [set(p["tests failing"]) & set(NEW) for p in six]
    assert all(by_new), [p["plant"] for p, s in zip(six, by_new) if not s]
    assert set().union(*by_new) == set(NEW)
    assert "the lock now catches 24 of 24, the control passing" in PAGE


def test_the_four_tests_are_in_the_lock_and_the_lock_says_why():
    for t in NEW:
        assert "\ndef %s(" % t in LOCK, t
    assert LOCK.count("\ndef test_") >= 14
    assert "ADDED 2026-11-12, a second time" in LOCK and "WHAT THIS CANNOT HOLD: the claim restated without the word" in LOCK
    # the first of the four runs the script: the lock holds the run file to what the script gives, not to three of its lines
    assert "_run_the_script_in_a_copy(tmp_path, seed)" in LOCK and "for seed in (1, 2):" in LOCK
    # bytes under the versions that made the run, less under others, and the weaker comparison is itself tested
    assert "_held_under_another_version(run, data, run0, data0, seed)" in LOCK and "\ndef test_what_is_held_under_another_version_can_fail_and_lets_a_last_digit_be(" in LOCK
    made = json.loads((ROOT / "frontier" / "B1881_the_whole_and_the_value_verified" / "verification" / "whole_and_value_on_main_made_with.json").read_text(encoding="utf-8"))
    assert set(made) == {"python", "mpmath", "sympy"} and "**So the script now writes which versions made its run,**" in PAGE


def test_the_readers_count_and_its_quotations():
    q = json.loads((HERE / "quote_check.json").read_text(encoding="utf-8"))
    assert q["quotations"] == q["found"] == 6 and q["the commit of main read"] == "3c5ab6bef" and q["control: the first quotation altered by one character is reported missing"] is True
    assert "6 of 6 found at `3c5ab6bef`" in PAGE
    for s in ("**The reader's count: 17 of 23.**", "twelve are caught and six pass", "**Main's own count for the same lock had been 18 of 18.**"):
        assert s in PAGE, s
    led = (ROOT / "docs" / "HARVEST_LEDGER.md").read_text(encoding="utf-8")
    row = [l for l in led.split("\n") if l.startswith("| 1733 |")]
    assert len(row) == 1 and "03794ed0" in row[0] and "B1897" in row[0] and "17 of 23" in row[0]


def test_the_arc_says_what_it_is_and_what_it_is_not():
    for s in ("## Seen first", "## Disclosed", "## Reproduce", "0 of 19", "**One of the six cannot be closed in general,**", "The six plants here are main's reconstructions",
              "**The reader's own 23 against the new lock.** It is asked to run them.", "**A sentence restated in new words is not found by any list.**"):
        assert s in PAGE, s
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1897" and v["verdict"] == "PROVED" and v["instrument"] is True and v["claim_one_line"].endswith("0 of 19.")
    assert set(v["scope"]) == {"frame", "object", "reach", "hypotheses"} and v["scope"]["reach"] in ("single", "class", "general")
    assert "17 OF 23 PLANTED ERRORS CAUGHT" in v["claim_one_line"] and "the lock catches 24 of 24, the control passing" in v["claim_one_line"]
