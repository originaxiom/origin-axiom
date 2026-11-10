"""B1860 -- Review 77's block is on the page with its core lines; Review 76's items are all closed; the review's
additions (the new error class, Review 77's practices, the reader's corrections where the corrected lines stand) are
in place."""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[3]


def _reviews():
    return ROOT.joinpath("docs", "progress", "REVIEWS.md").read_text(encoding="utf-8")


def test_review_77_block_core_lines():
    t = _reviews()
    blk = t[t.index("# Review 77 (2026-11-10)"):]
    assert "sample seed: 1eb535ecd" in blk and "read in full: B1849, B1852, B1853, B1854, B1858" in blk
    assert "fresh-clone suite:" in blk and "fresh-clone:" in blk and "gate controls: 49 registered" in blk
    acts = blk.split("### Action items (Review 77)")[1]
    assert all(("R77-%d:" % n) in acts for n in range(1, 9))
    assert "fresh-clone suite: FAIL @ cf0c56079 (8125 passed, 7 failed, 70 skipped" in blk


def test_review_76_items_all_closed():
    t = _reviews()
    r76 = t[t.index("# Review 76 (2026-11-06)"):t.index("# Review 77 (2026-11-10)")]
    acts = r76.split("### Action items (Review 76)")[1]
    assert not re.search(r"^- \[ \]", acts, re.M) and not re.search(r"^- \[>\]", acts, re.M)
    assert acts.count("RESOLVED") == 8


def test_the_reviews_additions():
    el = ROOT.joinpath("docs", "ERROR_LEDGER.md").read_text(encoding="utf-8")
    assert "| E96 | **A thread taken for the weave**" in el
    pr = ROOT.joinpath("docs", "PRACTICES.md").read_text(encoding="utf-8")
    assert "## Review 77's practices" in pr
    # E94's third instance, found by the review's fresh-clone suite, and the gate widened for it
    assert "**B1854's three driver logs** (Review 77's fresh-clone run" in el
    gates = ROOT.joinpath("scripts", "gates", "gates.py").read_text(encoding="utf-8")
    assert "def _file_relative_refs(rel, txt):" in gates and (ROOT / "tests" / "test_tracked_deps_locks.py").is_file()
    assert (ROOT / "frontier" / "B1860_review_77_the_decadal_review" / "verification" / "readers" / "reader_READ_IN_FULL.md").is_file()


def test_the_readers_corrections_stand_where_the_corrected_lines_stand():
    f = ROOT / "frontier"
    b1854 = (f / "B1854_the_tubes_tau_beyond_k1_on_main" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "with an error of about 0.02" in b1854 and "one of the two unlabelled ones" in b1854
    b1853 = (f / "B1853_the_departures_depth_premises_verified" / "FINDINGS.md").read_text(encoding="utf-8")
    assert b1853.count("marked here at Review 77") == 2
    for arc in ("B1853_the_departures_depth_premises_verified", "B1854_the_tubes_tau_beyond_k1_on_main", "B1858_the_closure_map"):
        v = json.loads((f / arc / "arc_verdict.json").read_text(encoding="utf-8"))
        assert "Review 77" in v["claim_one_line"], arc
    nodes = {n["id"]: n for n in json.loads((f / "B1858_the_closure_map" / "NODES.json").read_text(encoding="utf-8"))}
    assert nodes["T:RE"]["grade"] == "CONDITIONAL"
