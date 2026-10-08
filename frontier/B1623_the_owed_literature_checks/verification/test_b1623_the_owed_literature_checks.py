"""B1623 -- the owed literature checks recorded: the four theorems' lit-status carries the search; Lemma F's step (2) verified;
R62-2 and R62-6 marked paid; the three new theorem rows present."""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]


def test_registry_and_review_carry_the_checks():
    reg = ROOT.joinpath("docs", "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    assert reg.count("Searched 2026-10-09 (B1623)") == 4
    for row in ("| T-WEAVE-REDUCES-NONE |", "| T-TAU-ONLY-PERMUTATION |", "| T-CLOCK-IN-GRADING |"):
        assert row in reg, row
    rev = ROOT.joinpath("docs", "progress", "REVIEWS.md").read_text(encoding="utf-8")
    blk = rev[rev.index("### Action items (Review 62)"):]
    assert "- [x] R62-2: **resolved at S101 (B1623)" in blk and "- [x] R62-6: **paid at S101" in blk
    f = ROOT.joinpath("frontier", "B1623_the_owed_literature_checks", "FINDINGS.md").read_text(encoding="utf-8")
    assert "**Step (2) stands**" in f and "Tillmann–Yao" in f and "Declined." in f
