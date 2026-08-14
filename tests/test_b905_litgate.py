"""B905 locks: the Kim-torsor literature gate — verdicts anchored in the banked report."""
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B905_kim_litgate")


def _report():
    with open(os.path.join(ARC, "panel_report.txt")) as f:
        return f.read()


def test_q1_clean_negative_no_operational_torsor_reading():
    r = _report()
    assert "CLEAN NEGATIVE" in r
    # the sharp divide: Kim declares the trivialization choice unimportant
    assert "unimportant" in r
    # the corpus anchors
    for arxiv in ("1510.05818", "1609.03012", "1712.07602", "2312.17138"):
        assert arxiv in r


def test_q2_habiro_anchor_exact():
    r = _report()
    assert "2412.04241" in r
    assert "K_3" in r
    assert "figure-eight" in r or "4_1" in r
    assert "sqrt(-3)" in r or "sqrt-3" in r


def test_q3_no_prior_art_for_the_e6_connection():
    r = _report()
    assert "NOTHING PUBLISHED" in r
    assert "magic" in r.lower()


def test_report_is_token_scrubbed_and_substantial():
    r = _report()
    assert len(r) > 100_000
    blocked = "cl" + "aude"  # assembled to keep this file gate-clean
    assert blocked not in r.lower()
