"""B1622 -- Review 62's block is on the page with its anchor, its core lines and its carries with their ancestors; the E85 and
E58 instances filed; the window's terms glossed."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[3]


def test_review_62_block_has_anchor_core_lines_and_carries_with_ancestors():
    t = ROOT.joinpath("docs", "progress", "REVIEWS.md").read_text(encoding="utf-8")
    i = t.index("# Review 62 (2026-10-09)"); blk = t[i:]
    assert "**anchor-commit: `d85301ad5`**" in blk
    assert "fresh-clone: PASS @ d85301ad" in blk and "sample seed: b7ce48c5c" in blk and "gate controls: 44 registered" in blk
    acts = blk.split("### Action items (Review 62)")[1]
    for key in ("R61-2", "R60-5", "R58-5", "R61-3", "R61-4", "R61-5"):
        assert key in acts, key
    assert all(("R62-%d:" % n) in acts for n in range(1, 8))
    r61 = t[t.index("# Review 61 (2026-10-08)"):i]
    assert not re.search(r"^- \[ \]", r61.split("### Action items (Review 61)")[1], re.M)


def test_the_two_instances_and_the_terms_are_filed():
    e = ROOT.joinpath("docs", "ERROR_LEDGER.md").read_text(encoding="utf-8")
    assert "**E85 instance (this bench, B1620's post-seal checks, 2026-10-08)" in e
    assert "**E58 instance (this bench, B1619, found by the audit lane's relay of 2026-10-08)" in e
    g = ROOT.joinpath("TERMINOLOGY.md").read_text(encoding="utf-8")
    assert "## Added at Review 62 (2026-10-09)" in g
    for term in ("the parity grading", "the clock", "the tick", "the mass tensor", "the family dimension"):
        assert "**%s**" % term in g, term
