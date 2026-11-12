"""B1877 -- Review 78's block is on the page with its core lines; Review 77's items are each resolved or carried; the
review's additions (the practices, the glosses, the ledger's instances, the new gate) are in place; the readers'
corrections stand where the corrected lines stand; the owner's rulings at the review are recorded in the owner's words."""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[3]
F = ROOT / "frontier"


def _reviews():
    return ROOT.joinpath("docs", "progress", "REVIEWS.md").read_text(encoding="utf-8")


def _read(*parts):
    return ROOT.joinpath(*parts).read_text(encoding="utf-8")


def _arc(prefix, name="FINDINGS.md"):
    hits = sorted(F.glob(prefix + "_*"))
    assert len(hits) == 1, (prefix, hits)
    return (hits[0] / name).read_text(encoding="utf-8")


def test_review_78_block_core_lines():
    t = _reviews()
    blk = t[t.index("# Review 78 (2026-11-11)"):]
    assert "sample seed: 10641a1b2" in blk and "read in full: B1861, B1862, B1863, B1865, B1872" in blk
    assert "fresh-clone suite: FAIL @ b28dceea8 (2 failed, 8266 passed, 70 skipped" in blk and "fresh-clone:" in blk
    assert "gate controls: 52 registered failing-path tests; unregistered: none" in blk
    acts = blk.split("### Action items (Review 78)")[1]
    assert all(("R78-%d:" % n) in acts for n in range(1, 12)) and "R78-12:" not in acts
    for carried in ("carried from R77-3", "carried from R77-4", "carried from R77-5", "carried from R77-6", "carried from R77-8"):
        assert carried in acts, carried


def test_review_77_items_each_resolved_or_carried():
    t = _reviews()
    r77 = t[t.index("# Review 77 (2026-11-10)"):t.index("# Review 78 (2026-11-11)")]
    acts = r77.split("### Action items (Review 77)")[1]
    assert not re.search(r"^- \[ \]", acts, re.M)
    assert len(re.findall(r"^- \[x\] R77-", acts, re.M)) == 3 and len(re.findall(r"^- \[>\] R77-", acts, re.M)) == 5
    for n, to in ((3, 6), (4, 7), (5, 8), (6, 9), (8, 10)):
        assert re.search(r"^- \[>\] R77-%d: .*carried to Review 78 as R78-%d" % (n, to), acts, re.M), n


def test_the_reviews_additions():
    assert "E53 instances #39–#41 (found at Review 78" in _read("docs", "ERROR_LEDGER.md")
    assert "## Review 78's practices" in _read("docs", "PRACTICES.md") and "`closure-generated`" in _read("docs", "PRACTICES.md")
    assert "## Added at Review 78 (2026-11-11)" in _read("TERMINOLOGY.md")
    gates = _read("scripts", "gates", "gates.py")
    assert "def gate_closure_generated(" in gates and '"closure-generated": gate_closure_generated' in gates
    controls = json.loads(_read("tests", "GATE_CONTROLS.json"))
    assert "closure-generated" in controls and "artifact-hashes" in controls
    rep = _arc("B1877", "verification/readers/reader_READ_IN_FULL.md")
    assert "Ten must-fix findings." in rep and "## Reader A's report" in rep and "## Reader B's report" in rep and ("/" + "Users" + "/") not in rep        # spelt in pieces: the suite's guard reads every .py file for the literal


def test_the_readers_corrections_stand_where_the_corrected_lines_stand():
    assert "[COMMUTING -- corrected 2026-11-10 (B1862" in _arc("B952", "arc_verdict.json") and "[COMMUTING -- corrected 2026-11-10 (B1862" in _arc("B952", "results.json")
    assert "the elements must COMMUTE" in _read("docs", "GUT_REQUIREMENTS_LEDGER.md")
    assert "carried to this block 2026-11-11 by Review 78" in _arc("B854")
    assert "[FOR E = +I ONLY: corrected 2026-11-10 (B1862)" in _arc("B1856", "arc_verdict.json")
    for arc in ("B1853", "B1855", "B1857"):
        assert "carried here by Review 78" in _arc(arc), arc
    assert "carried here by Review 78" in _read("docs", "THE_TAU_READOUT_RULE.md")
    assert "## Dated correction, 2026-11-11 (Review 78" in _arc("B1862") and "## Dated correction, 2026-11-11 (Review 78" in _arc("B1872")
    assert "Which twin is a convention. One twin or both is not." in _arc("B1872")
    assert "## Live counts, checked by the lock (added at Review 78, 2026-11-11)" in _arc("B1861")
    assert "**Six are caught.**" in _arc("B1865")


def test_the_owners_rulings_at_the_review_are_recorded_in_the_owners_words():
    reg = _read("docs", "POINT_REGISTER.md")
    rows = {m.group(1): m.group(0) for m in re.finditer(r"^\| (P-\d+) \|.*$", reg, re.M)}
    assert "| DONE |" in rows["P-771"] and "'Yes, admit it (Recommended)'" in rows["P-771"] and "'Yes, all three (Recommended)'" in rows["P-771"]
    assert "| DONE |" in rows["P-774"] and "'The act itself (Recommended)'" in rows["P-774"] and "'Whole agrees (Recommended)'" in rows["P-774"]
    assert "| DONE |" in rows["P-697"] and "WAS NOT SENT" in rows["P-697"]
    # [CHANGED 2026-11-12.  This test held the three rows to the disposition OWNER, which is where they stood at the review.
    #  The owner's later word (register row P-825) moved all three, and a lock of a review holds what the review recorded,
    #  not where a live row stands today.  What is held now: the confirmation of 2026-11-11 stays in each row, and the row
    #  that moved says that it moved and when.]
    for n in ("P-081", "P-082", "P-253"):
        assert "2026-11-11, the owner confirmed in a dialog" in rows[n], n
        assert "| OWNER |" in rows[n] or ("row P-825" in rows[n] and "UNTIL 2026-11-12 THE ROW READ, as a call of the owner's" in rows[n]), n
    assert (ROOT / "docs" / "handoffs" / "CC_TO_AGY_2026-11-11_YOUR_THREE_COMPLIANCE_POINTS_ARE_MENDED.md").is_file()
    prog = json.loads(_arc("B1861", "PROGRAMME.json"))
    assert sorted(prog["confirmed_later"]) == ["no rule picks a next thing", "the ledger, cancelling, interaction", "the tick is an act", "what exists is what survives"]
    # the first three are the review's; a fourth was given after it, with the computation in hand (B1879), and the
    # programme lists the rulings in the order they were given, so the review's three stay the first three
    assert [r[0] for r in prog["direct_rulings"]][:3] == ["what a ground is", "what 'the ledger must close' means",
                                                           "how 'the tick is an act' stands with 'even ticks observed'"]
    assert prog["direct_rulings"][2][2] == "After the computation" and "'After the computation'" in rows["P-771"]
    assert [r[0] for r in prog["direct_rulings"]][3:] == ["'even ticks observed', after the computation"]
    assert prog["direct_rulings"][3][2] == "A condition to derive (Recommended)"
    assert "A condition to derive (Recommended)" in rows["P-771"]
    # the over-reading is corrected where it stood: no page says the ruling on the tick settles the mark
    blk = _reviews(); blk = blk[blk.index("# Review 78 (2026-11-11)"):]
    assert "*Corrected the same day,\n    before the push.*" in blk and "so the allowed subweave at level 5\n    is the stabiliser of the eigenline" not in blk
    assert prog["stats"]["rulings_asked"] == 0 and prog["stats"]["rulings_confirmed_by_the_owner_to_main"] == 15
    # nothing was carried into the foundation by the review: that is P-767
    assert "| QUEUED |" in rows["P-767"] and "EXTENDED BY THE OWNER'S ANSWERS TO MAIN" in rows["P-767"]
