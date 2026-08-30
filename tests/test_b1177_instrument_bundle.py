"""B1177 lock -- the instrument bundle (R50-5)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1177_instrument_bundle"


def test_arc_verdict():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1177" and d["verdict"] == "OPEN" and d["instrument"] is True
    assert "21 TRUE no-runner-no-lock" in d["claim_one_line"]


def test_debt_list_committed():
    txt = (ARC / "reproducer_debt.md").read_text(encoding="utf-8")
    assert "21 true no-runner-no-lock" in txt and "B1067" in txt
    assert "no retro mass-authoring" in " ".join(txt.lower().split())


def test_law_map_rows():
    lm = (ROOT / "docs" / "LAW_MAP.md").read_text(encoding="utf-8")
    for name in ("THE TRIT MORPHISM", "SUPERLINEAR SEAM CREATION", "THE INVARIANT LINE ON THE 27", "THE ARITY VOID"):
        assert name in lm, name


def test_doc_currency_watches_toolbox_live():
    dc = (ROOT / "scripts" / "checks" / "doc_currency.py").read_text(encoding="utf-8")
    assert "docs/TOOLBOX_LIVE.md" in dc
    tl = (ROOT / "docs" / "TOOLBOX_LIVE.md").read_text(encoding="utf-8")
    assert "extraction seed" in tl


def test_measurements_honest():
    d = json.loads((ARC / "b1177_results.json").read_text(encoding="utf-8"))
    assert "addendum" in d["fences"].lower()
    assert "178.41" in d["l184_diagnosis"]
    assert "Gate 5 clean" in d["fences"]
