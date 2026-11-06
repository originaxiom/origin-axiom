"""B1844 -- Review 75's block is on the page with its core lines, Review 74's items are all closed or carried by lineage,
the review's rulings reached the register and the scoreboard, THE COUNT is adopted, and the Stage 16-18 ranges are sealed."""
import json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[3]


def _reviews():
    return ROOT.joinpath("docs", "progress", "REVIEWS.md").read_text(encoding="utf-8")


def test_review_75_block_core_lines():
    t = _reviews()
    blk = t[t.index("# Review 75 (2026-11-06)"):]
    assert "sample seed: 41420ae14" in blk and "read in full: B1834, B1836, B1838, B1839, B1841" in blk
    assert "fresh-clone suite:" in blk and "gate controls: 48 registered" in blk
    acts = blk.split("### Action items (Review 75)")[1]
    assert all(("R75-%d:" % n) in acts for n in range(1, 10))
    for key in ("R74-3", "R74-4", "R74-5", "R74-8", "R74-9"):
        assert key in acts, key


def test_review_74_items_all_closed():
    t = _reviews()
    r74 = t[t.index("# Review 74 (2026-11-04)"):t.index("# Review 75 (2026-11-06)")]
    acts = r74.split("### Action items (Review 74)")[1]
    assert not re.search(r"^- \[ \]", acts, re.M)
    assert acts.count("carried to Review 75 as R75-") == 5
    assert "declined from the review loop at its third carry" in acts


def test_rulings_reached_the_register_and_the_scoreboard():
    reg = ROOT.joinpath("docs", "POINT_REGISTER.md").read_text(encoding="utf-8")
    for pid in ("P-707", "P-708", "P-611"):
        row = [l for l in reg.splitlines() if l.startswith("| %s |" % pid)][0]
        assert "| DONE |" in row and "Review 75" in row, pid
    sb = json.loads(ROOT.joinpath("docs", "total_inputs_scoreboard.json").read_text(encoding="utf-8"))
    ids = [j["id"] for j in sb["frames"]["A"]["joints"]]
    assert "A06" not in ids and "A07" in ids and len(ids) == 11
    assert sb["frames"]["A"]["claims"] == [1, 2, 3, 4, 5, 6]


def test_the_count_adopted_and_the_ranges_sealed():
    c = ROOT.joinpath("docs", "THE_COUNT_2026-11-06.md").read_text(encoding="utf-8")
    assert "adopted at Review 75" in c and "borrows 13 joints" in c and "0 of 19" in c
    ex = json.loads((ROOT / "frontier" / "B1832_the_agy_lanes_digested" / "verification" / "SEALED_EXHIBITS.json").read_text(encoding="utf-8"))
    assert len(ex) >= 160
    assert sum(1 for x in ex if x["rev"] == "08e98b516") == 15
