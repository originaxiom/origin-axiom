"""A waiver of the review's block covers only the window it was granted in (main's M23, a finding on the gate
`review-fires`): a date does not tell two windows of one day apart, so the gate reads the anchor the waiver was granted
under, named on its line or read from git's history, and the waiver stops covering when a later anchor is written."""
import importlib.util
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _gates():
    sys.dont_write_bytecode, was = True, sys.dont_write_bytecode
    try:
        spec = importlib.util.spec_from_file_location("gates_for_the_waiver", ROOT / "scripts" / "gates" / "gates.py")
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
    finally:
        sys.dont_write_bytecode = was
    return m


g = _gates()
LINE = "- waived 2026-11-13 by the owner through 60 merges: a planted waiver"
NAMED = "- waived 2026-11-13 by the owner through 60 merges, in the window after anchor `aaaaaaa11`: a planted waiver"


def test_two_windows_of_one_day_are_told_apart():
    under_a = {LINE: "aaaaaaa11"}.get
    # the same day, the next window: the date rule alone lets the waiver cover; the anchor does not
    assert g.review_waiver_covers(45, LINE, since="2026-11-13") is True
    assert g.review_waiver_covers(45, LINE, since="2026-11-13", anchor="bbbbbbb22", granted=under_a) is False
    # the twin: the window it was granted in
    assert g.review_waiver_covers(45, LINE, since="2026-11-13", anchor="aaaaaaa11", granted=under_a) is True
    assert g.review_waiver_covers(60, LINE, since="2026-11-13", anchor="aaaaaaa11", granted=under_a) is False


def test_a_line_may_name_its_anchor():
    assert g.review_waiver_covers(45, NAMED, anchor="aaaaaaa11") is True
    assert g.review_waiver_covers(45, NAMED, anchor="aaaaaaa11fffffff") is True       # a longer form of the same commit
    assert g.review_waiver_covers(45, NAMED, anchor="bbbbbbb22") is False


def test_where_no_anchor_is_known_the_date_rule_is_read():
    nothing = lambda line: None
    assert g.review_waiver_covers(45, LINE, since="2026-11-13", anchor="bbbbbbb22", granted=nothing) is True
    assert g.review_waiver_covers(45, LINE, since="2026-11-14", anchor="bbbbbbb22", granted=nothing) is False


def test_each_waiver_on_record_is_read_with_the_anchor_it_was_granted_under():
    text = (ROOT / g.REVIEW_WAIVER).read_text(encoding="utf-8")
    lines = re.findall(r"^- waived .*$", text, re.M)
    assert lines
    anchors = [g.waiver_granted_under(l) for l in lines]
    if all(a is None for a in anchors):            # a clone without the history: the date rule stands, and is said
        return
    reviews = (ROOT / g.REVIEWS).read_text(encoding="utf-8")
    written = re.findall(r"anchor-commit: `?([0-9a-f]{7,40})`?", reviews)
    assert all(a in written for a in anchors if a), anchors
    assert g.review_anchor() == written[-1]
