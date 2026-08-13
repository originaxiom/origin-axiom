"""B1054 locks — Review 1's load-bearing findings, and the review's own required form.

These lock the STRUCTURAL claims, never the moving integers. A review that pins an absolute count
inside a programme whose purpose is to move it is E38, and this window found two live instances of
exactly that; the counts live in `results.json` where they are recorded rather than asserted.
"""
import glob
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARTIFACT = "docs/progress/REVIEW_1_CONSOLIDATION_SEAT_2026-08-12.md"
WINDOW = range(1024, 1054)


def _read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def _prose(s):
    return re.sub(r"\s+", " ", re.sub(r"(?m)^\s*>\s?", "", s))


def _results():
    return json.loads(_read("frontier/B1054_review_one/results.json"))


def test_all_checks_pass():
    R = _results()
    bad = [k for k, v in R["checks"].items() if not v["pass"]]
    assert bad == [] and R["all_pass"] is True, bad
    assert len(R["checks"]) >= 50


def test_the_window_verdict_field_carries_no_information():
    """The load-bearing finding: 30 arcs, one verdict value, against a discriminating corpus."""
    vals = set()
    for n in WINDOW:
        d = glob.glob(str(ROOT / "frontier" / f"B{n}_*" / "arc_verdict.json"))
        assert d, f"B{n} missing"
        vals.add(json.loads(pathlib.Path(d[0]).read_text())["verdict"])
    assert vals == {"PROVED"}, vals
    base = _results()["measured"]["corpus_PROVED_base_rate_excl_window"]
    assert 0.5 < base < 0.8, base            # the corpus is NOT uniform -- the window is


def test_the_atlas_status_field_does_discriminate_over_the_same_arcs():
    """The control. The judgement exists; the verdict field does not carry it."""
    atlas = json.loads(_read("scripts/atlas/atlas_data.json"))["probes"]
    seen = {atlas[f"B{n}"]["status"] for n in WINDOW if f"B{n}" in atlas}
    assert len(seen) >= 3, seen


def test_the_debt_metric_selects_on_the_verdict_field_and_is_blind_to_more_than_it_counts():
    m = _results()["measured"]
    assert m["debt_as_the_metric_counts_it"] < sum(
        m["uncited_arcs_invisible_to_the_metric_by_verdict_field"].values())
    assert m["share_of_the_uncited_population_the_metric_shows"] < 0.6


def test_this_arc_declares_its_own_verdict_convention():
    """The fix practised, not merely registered -- the first arc in the window to declare."""
    v = json.loads(_read("frontier/B1054_review_one/arc_verdict.json"))
    assert v["verdict_convention_declared"].strip()
    assert "OWNER" in v["verdict_convention_declared"]


def test_the_review_carries_every_form_the_commission_required():
    raw = _read(ARTIFACT)
    a = _prose(raw)
    assert re.search(r"(?m)^#{2,4} Action items \(Review 1\)", raw)
    assert "without being misled" in a          # the 7d certification standard, asked of itself
    assert "REBUILT" in a and "RUN" in a        # cc3's grading labels
    assert "NOT-REACHED" in a                   # a first-class, countable disposition
    assert "never merges" in a
    assert "anchor-commit:" in raw
    assert "cc3" in a and "28 candidates" in a  # the convergence cited, not re-adjudicated


def test_every_action_item_names_an_owner():
    block = _read(ARTIFACT).split("### Action items (Review 1)")[1]
    items = [l for l in block.splitlines() if l.startswith("- [ ]") or l.startswith("- [x]")]
    assert len(items) >= 10
    for l in items:
        assert "owner:" in l, l
        assert re.search(r"owner: (OWNER|SEAT|MAIN)", l), l


def test_the_review_registers_the_leads_and_decides_none_of_them():
    """The commission's boundary: qL155-qL166 stay the owner's calls."""
    a = _prose(_read(ARTIFACT))
    assert "qL155–qL166" in a or "qL155-qL166" in a
    assert "registered and did not decide" in a or "does not decide" in a
