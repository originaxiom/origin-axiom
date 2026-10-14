"""B1647 -- Review 63's block is on the page with its anchor and core lines; Review 62's open item carried; the ledger
corrections, the relay rows, B1600's addendum, the E82 instance, the terms and the register rows are filed."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[3]


def _t(*p):
    return ROOT.joinpath(*p).read_text(encoding="utf-8")


def test_review_63_block_anchor_core_lines_and_loop():
    t = _t("docs", "progress", "REVIEWS.md")
    i = t.index("# Review 63 (2026-10-14)"); blk = t[i:]
    assert "**anchor-commit: `0bbbb6cab`**" in blk
    assert "fresh-clone: PASS @ 0bbbb6ca" in blk and "sample seed: d85301ad5" in blk and "gate controls: 45 registered" in blk
    acts = blk.split("### Action items (Review 63)")[1]
    assert "R62-1" in acts and all(("R63-%d:" % n) in acts for n in range(1, 8))
    r62 = t[t.index("# Review 62 (2026-10-09)"):i]
    assert not re.search(r"^- \[ \]", r62.split("### Action items (Review 62)")[1], re.M)


def test_the_corrections_are_filed():
    h = _t("docs", "HARVEST_LEDGER.md")
    for s in ("NOT RE-RUN TO COMPLETION; ITS OWN CHECK DIFFERS", "**CONSISTENT** (read in full; nothing recomputed)",
              "**VERIFIED** (B1470: 6 435 of 6 435 agree", "B1600 addendum (`verification/w21_check.py`)",
              "no arc recomputes W51", "B1637 (its preregistration, the input re-fetch)", "marker added at Review 63"):
        assert s in h, s
    assert "## 4b. Addenda: main's checks of the seat's later items" in _t("frontier", "B1600_the_weave_verified", "FINDINGS.md")
    r = _t("docs", "RELAY_LEDGER.md")
    for n in ("SURFACE_PARENT_DICTIONARY", "GLOBAL_SPIN_AND_RAW_RESIDUE", "BASED_PREREQUISITE_AND_HIGGS_FIBRE"):
        assert "PHYSICAL_TO_GENESIS_MAIN_SM_2026-10-13_%s.md" % n in r, n
    assert "A SEALED CELL THAT COULD NOT FAIL" in _t("docs", "ERROR_LEDGER.md")
    g = _t("TERMINOLOGY.md"); assert "## Added at Review 63 (2026-10-14)" in g
    for term in ("the ruled branch", "the golden coupling", "the theta triplet R", "the isotropic cone", "the point register"):
        assert "**%s**" % term in g, term
    p = _t("docs", "POINT_REGISTER.md")
    assert all(("| P-%d |" % n) in p for n in range(119, 128))
    assert re.search(r"^\| P-086 .*\| DONE \| B1647", p, re.M)
