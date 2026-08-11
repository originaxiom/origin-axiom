"""B1044 locks — the law-siblings instrument, its gate, and its triage.

Exercises the sweeper directly (it is cheap) rather than only reading results.json.
"""
import json
import pathlib
import sys

_ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "scripts" / "checks"))
import law_siblings as ls  # noqa: E402

_R = json.loads((_ROOT / "frontier" / "B1044_law_siblings_gated" / "results.json")
                .read_text(encoding="utf-8"))


def test_every_check_passes():
    failed = [k for k, c in _R["checks"].items() if not c["pass"]]
    assert failed == [], failed


def test_the_gate_is_wired_and_registered():
    g = (_ROOT / "scripts" / "gates" / "gates.py").read_text(encoding="utf-8")
    assert '"law-siblings": gate_law_siblings' in g
    assert "FAIL-CLOSED" in g.split("def gate_law_siblings")[1][:900]
    assert "law-siblings" in (_ROOT / "docs" / "PRACTICES.md").read_text(encoding="utf-8")


def test_no_candidate_is_untriaged():
    assert ls.sweep() == [], ls.sweep()


def test_the_registry_disposes_both_ways():
    """A registry that only ever consolidates is a rubber stamp."""
    reg = (_ROOT / "docs" / "consolidation" / "LAW_SIBLINGS.md").read_text(encoding="utf-8")
    assert "SAME-LAW" in reg and "RELATED" in reg
    assert len(ls.triaged()) >= 8
    # and the RELATED one is genuinely still in debt, not quietly consolidated
    assert any(b == "B257" for _, b, _ in ls.candidates())


def test_the_sweeper_reaches_B564_by_topic():
    """The defect that motivated the instrument must be mechanically reachable."""
    import re
    pat = ls.FINGERPRINTS["phi-fixed reducibility (B1039)"]
    hits = [p for p in _ROOT.glob("frontier/B564_*/arc_verdict.json")
            if re.search(pat, json.loads(p.read_text(encoding="utf-8"))["claim_one_line"], re.I)]
    assert hits, "B564 no longer matches the phi-fixed fingerprint"


def test_the_registry_exclusion_is_by_purpose_not_by_mention():
    """Excluding every line that names the registrar also drops that row's real citations —
    a LAW_MAP row is one line. That bug made B117/B122/B121/B118 read as uncited."""
    src = (_ROOT / "scripts" / "checks" / "law_siblings.py").read_text(encoding="utf-8")
    assert "Excluded by PURPOSE, not by mention" in src
    blob = ls._curated_blob()
    for b in ("B117", "B122", "B121", "B118"):
        assert b in blob, b        # the tower row's citations must survive the exclusion
