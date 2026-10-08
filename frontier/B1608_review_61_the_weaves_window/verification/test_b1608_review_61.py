"""B1608 -- Review 61's block is on the page with its anchor, its core lines and its carry continuity; E85 and E86 filed."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[3]


def test_review_61_block_has_anchor_core_lines_and_carries_with_ancestors():
    t = ROOT.joinpath("docs", "progress", "REVIEWS.md").read_text(encoding="utf-8")
    i = t.index("# Review 61 (2026-10-08)"); blk = t[i:]
    assert "**anchor-commit: `b7ce48c5c`**" in blk
    assert "fresh-clone: PASS @" in blk and "sample seed: aab434644" in blk and "gate controls: 44 registered" in blk
    for key in ("R60-2", "R60-5", "R58-4", "R59-3", "R58-5"):
        assert key in blk.split("### Action items (Review 61)")[1], key
    assert all(("R61-%d:" % n) in blk for n in range(1, 7))
    r60 = t[t.index("# Review 60 (2026-10-07)"):i]
    assert not re.search(r"^- \[ \]", r60.split("### Action items (Review 60)")[1], re.M)


def test_the_two_error_classes_are_filed():
    e = ROOT.joinpath("docs", "ERROR_LEDGER.md").read_text(encoding="utf-8")
    assert "**E85 the UNCONTROLLED-PRECISION READING class**" in e and "**E86 the MOVING-TARGET PIN class**" in e
