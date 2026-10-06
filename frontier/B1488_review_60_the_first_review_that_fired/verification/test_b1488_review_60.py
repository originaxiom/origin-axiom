"""B1488 -- Review 60's block is on the page with its anchor, its core lines and its carry continuity."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[3]


def test_review_60_block_has_anchor_core_lines_and_closes_the_carried_items():
    t = ROOT.joinpath("docs", "progress", "REVIEWS.md").read_text()
    i = t.index("# Review 60 (2026-10-07)"); blk = t[i:]
    assert "**anchor-commit: `aab434644`**" in blk
    assert "fresh-clone: PASS @" in blk and "sample seed: 7b20d258" in blk and "gate controls: 43 registered" in blk
    for key in ("R58-4", "R58-5", "R55-1", "R55-7", "R55-12", "R56-1", "R56-3"):
        assert re.search(r"- \[[x>]\] %s" % re.escape(key), blk), key
    assert all(("R60-%d:" % n) in blk for n in range(1, 8))
