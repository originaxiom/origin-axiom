"""B1848 -- Review 76's block is on the page with its core lines; Review 75's items are all closed or carried by lineage;
the review's additions (B1846's two LAW_MAP rows, Review 76's practices) are in place."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[3]


def _reviews():
    return ROOT.joinpath("docs", "progress", "REVIEWS.md").read_text(encoding="utf-8")


def test_review_76_block_core_lines():
    t = _reviews()
    blk = t[t.index("# Review 76 (2026-11-06)"):]
    assert "sample seed: 264fa6d98" in blk and "read in full: B1845, B1846, B1847" in blk
    assert "fresh-clone: PASS @ d10b05652" in blk and "fresh-clone suite:" in blk and "gate controls: 48 registered" in blk
    acts = blk.split("### Action items (Review 76)")[1]
    assert all(("R76-%d:" % n) in acts for n in range(1, 9))
    for key in ("R75-4", "R75-5", "R75-8"):
        assert key in acts, key


def test_review_75_items_all_closed():
    t = _reviews()
    r75 = t[t.index("# Review 75 (2026-11-06)"):t.index("# Review 76 (2026-11-06)")]
    acts = r75.split("### Action items (Review 75)")[1]
    assert not re.search(r"^- \[ \]", acts, re.M)
    assert acts.count("carried to Review 76 as R76-") == 4
    assert acts.count("declined from the review loop at its third carry") == 3


def test_the_reviews_additions():
    lm = ROOT.joinpath("docs", "LAW_MAP.md").read_text(encoding="utf-8")
    assert "HARMONIC TIME SPREADS THE ENERGY EVENLY (B1846" in lm and "THE VOLUME WEIGHT HAS NO ATOM" in lm
    pr = ROOT.joinpath("docs", "PRACTICES.md").read_text(encoding="utf-8")
    assert "## Review 76's practices" in pr
