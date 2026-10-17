"""B1669 -- Review 65's block is on the page with its anchor and core lines; Review 64's open items resolved or carried;
the window's scope notes, B616's pin, E90 and its check are in place."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[3]


def _t(*p):
    return ROOT.joinpath(*p).read_text(encoding="utf-8")


def test_review_65_block_anchor_core_lines_and_loop():
    t = _t("docs", "progress", "REVIEWS.md")
    i = t.index("# Review 65 (2026-10-17)"); blk = t[i:]
    assert "**anchor-commit: `c370ff37c`**" in blk
    assert "fresh-clone: PASS @ c370ff37c" in blk and "sample seed: bf44d9032" in blk and "gate controls: 45 registered" in blk
    assert "@@SUITE@@" not in blk
    acts = blk.split("### Action items (Review 65)")[1]
    assert all(("R65-%d:" % n) in acts for n in range(1, 13))
    for carried in ("R64-1", "R64-4", "R64-5", "R64-6", "R64-7", "R64-8", "R64-10"):
        assert carried in acts, carried
    r64 = t[t.index("# Review 64 (2026-10-16)"):i]
    assert not re.search(r"^- \[ \]", r64.split("### Action items (Review 64)")[1], re.M)


def test_scope_notes_pin_and_e90():
    for arc in ("B1649_the_kernel_at_the_puncture", "B1651_where_a_higgs_can_couple", "B1658_the_twisted_half_bound",
                "B1662_the_pull_back_acts_on_the_records", "B1663_the_pull_backs_strength", "B1666_the_layers_robust"):
        assert "Review 65" in _t("frontier", arc, "FINDINGS.md"), arc
    assert "verification/szego_check.py" in _t("frontier", "B1651_where_a_higgs_can_couple", "ARTIFACT_HASHES.txt")
    assert "observed 2 coarse-tier matches of 384 pairs" in _t("tests", "test_b616_heldout.py")
    assert "E90 the BUILT-PAGE-NOT-READ class" in _t("docs", "ERROR_LEDGER.md")
    assert "source_hygiene.py" in _t("papers", "P9_what_a_grammar_fixes", "build.sh")
