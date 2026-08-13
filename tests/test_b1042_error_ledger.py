"""B1042 locks — the error ledger's currency and the two minted classes.

Independently re-checks the register's shape; reads results.json only for what needs git.
"""
import json
import pathlib
import re

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_R = json.loads((_ROOT / "frontier" / "B1042_the_error_ledger" / "results.json")
                .read_text(encoding="utf-8"))
_EL = (_ROOT / "docs" / "ERROR_LEDGER.md").read_text(encoding="utf-8")


def test_every_check_passes():
    failed = [k for k, c in _R["checks"].items() if not c["pass"]]
    assert failed == [], failed


def test_the_two_classes_exist_with_their_standing_rules():
    assert "| E37 |" in _EL and "Self-measurement" in _EL
    assert "| E38 |" in _EL and "Progress-eroded threshold" in _EL
    # REPAIRED BY REVIEW 1 (B1054). `== 38` is E38 inside the arc that REGISTERED E38: an absolute
    # count over a register whose whole purpose is to grow. Review 1 added E39 (cached
    # verification) and this inverted. The claim is that both classes exist and the register is at
    # least as large as when they were added.
    assert len(re.findall(r"^\| E\d+ \|", _EL, re.M)) >= 38
    # E37's rule is B1033's, and must say so
    e37 = [l for l in _EL.splitlines() if l.startswith("| E37 |")][0]
    assert "EXCLUSION SET" in e37 and "AUTHORSHIP" in e37
    assert "X31" in e37 and "Review 42" in e37       # credited, not claimed
    # E38's rule is a share, not a count
    e38 = [l for l in _EL.splitlines() if l.startswith("| E38 |")][0]
    assert "SHARE" in e38 and "never as a raw count" in e38
    assert "B870" in e38 and "92" in e38             # the finding that did NOT move


def test_E1_now_carries_the_refreshs_five_collisions():
    e1 = [l for l in _EL.splitlines() if l.startswith("| E1 |")][0]
    for b in ("B1024", "B1026", "B1034", "B1036"):
        assert b in e1, b
    assert "2026-07-16" in e1                        # the original three are not dropped


def test_the_one_offs_are_instances_not_classes():
    """The header forbids per-incident entries; B1039 and B1041 are filed under E31 and E36."""
    assert "One entry per ERROR CLASS, not per incident" in _EL
    e31 = _EL.split("| E32 |")[0].split("| E31 |")[-1]
    e36 = _EL.split("| E37 |")[0].split("| E36 |")[-1]
    assert "B1039" in e31 and "ANTI-homomorphism" in e31
    assert "B1041" in e36
    # REPAIRED BY REVIEW 1 (B1054). The original asserted `"| E39 |" not in _EL` to mean "neither
    # one-off was promoted to a class" -- but it said so by claiming the NEXT SLOT stays empty
    # forever, which any later finding falsifies without touching the claim. E39 now exists, for
    # cached verification, which is neither of these two. The claim is restated as what it is:
    # these two incidents live inside E31 and E36 and nowhere else.
    for row in re.findall(r"^\| E\d+ \|.*$", _EL, re.M):
        if row.startswith("| E31 |") or row.startswith("| E36 |"):
            continue
        assert "ANTI-homomorphism" not in row, row[:80]


def test_the_hazard_that_earned_E37_is_still_named_at_its_origin():
    """E37 credits THE_LADDER X31 and Review 42. If either text moves, the credit must move."""
    assert "Registering a gap creates hits for the gap" in \
        (_ROOT / "docs" / "THE_LADDER.md").read_text(encoding="utf-8")
    assert "self-inflates" in (_ROOT / "docs" / "progress" / "REVIEWS.md").read_text(encoding="utf-8")


def test_the_gate_change_is_registered_not_made():
    """L163 is an owner decision; the drafting seat must not have edited LIVING."""
    dc = (_ROOT / "scripts" / "checks" / "doc_currency.py").read_text(encoding="utf-8")
    living = re.search(r"LIVING = \{(.*?)\n\}", dc, re.S).group(1)
    for f in ("ERROR_LEDGER.md", "RETRACTIONS.md", "REPRESENTATION_TRIAGE.md"):
        assert f not in living, f
    assert "L163" in (_ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8")
