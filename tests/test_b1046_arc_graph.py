"""B1046 locks — the arc graph's two defects, the instrument, and what it refuses to do."""
import json
import pathlib
import re
import sys

_ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "scripts" / "checks"))
import supersession as sp  # noqa: E402

_R = json.loads((_ROOT / "frontier" / "B1046_the_arc_graph" / "results.json")
                .read_text(encoding="utf-8"))


def test_every_check_passes():
    failed = [k for k, c in _R["checks"].items() if not c["pass"]]
    assert failed == [], failed


def test_the_graph_is_one_way_and_targets_are_live():
    arcs = sp._arcs()
    says = [b for b, d in arcs.items() if sp._refs(d.get("supersedes"))]
    back = [b for b, d in arcs.items() if sp._refs(d.get("superseded_by"))]
    assert len(says) > 40 and len(back) < 10, (len(says), len(back))
    cited = [c for c in sp.one_way_links() if "IS CITED" in c[2]]
    assert len(cited) >= 10
    assert any(c[1] == "B123" for c in cited)   # the arc B1037 declined to restore


def test_B408_headline_contradicts_its_own_verdict():
    f = list(_ROOT.glob("frontier/B408_*/FINDINGS.md"))[0].read_text(encoding="utf-8")
    v = json.loads(list(_ROOT.glob("frontier/B408_*/arc_verdict.json"))[0]
                   .read_text(encoding="utf-8"))
    head = f.split("\n", 1)[0]
    assert "THE SEAM DOES NOT CONTRACT" in head and "scale lever stands" in head
    assert v["verdict"] == "NEGATIVE"
    flat = re.sub(r"\s+", " ", f)
    assert "the seam CONTRACTS" in flat and "NO scale lever in any tested channel" in flat


def test_the_gate_is_wired_registered_and_fails_closed():
    g = (_ROOT / "scripts" / "gates" / "gates.py").read_text(encoding="utf-8")
    assert '"supersession": gate_supersession' in g
    assert '"law-siblings": gate_law_siblings' in g      # gate 27 survived the rewind
    assert "FAIL-CLOSED" in g.split("def gate_supersession")[1][:900]
    assert "supersession" in (_ROOT / "docs" / "PRACTICES.md").read_text(encoding="utf-8")


def test_nothing_is_untriaged_and_the_backlog_is_published():
    assert sp.sweep() == [], sp.sweep()
    assert len(sp.candidates()) > len(sp.load_bearing())
    reg = (_ROOT / "docs" / "consolidation" / "SUPERSESSIONS.md").read_text(encoding="utf-8")
    assert "backlog, measured and not hidden" in reg.lower() or "backlog" in reg


def test_the_back_links_are_not_written_and_B141_stays_live():
    """The instrument's central refusal: B142 supersedes B141, B1039 restored BOTH."""
    src = (_ROOT / "scripts" / "checks" / "supersession.py").read_text(encoding="utf-8")
    assert "DELIBERATELY NOT AUTOMATED" in src
    arcs = sp._arcs()
    assert sp._refs(arcs["B141"].get("superseded_by")) == []
    reg = (_ROOT / "docs" / "consolidation" / "SUPERSESSIONS.md").read_text(encoding="utf-8")
    assert "EXTENDS" in reg and "REPLACES" in reg and "SELF-LABELLED" in reg
