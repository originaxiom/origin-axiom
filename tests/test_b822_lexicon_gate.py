"""B822 — locks the size floor and the removal of the gate's unsupported verdict.

B823 later replaced B822's CEILING with a triage registry, so these locks assert the properties
B822 established that SURVIVE that change -- not the wording of the implementation it shipped.
Re-anchoring a lock on a superseded literal would make it a test of the past, not of the invariant.
"""
import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location("gates", ROOT / "scripts" / "gates" / "gates.py")
g = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(g)


def _gate_src():
    src = (ROOT / "scripts" / "gates" / "gates.py").read_text(encoding="utf-8")
    return src[src.index("def gate_atlas_lexicon_current"):src.index("GATES = {")]


def test_the_metric_is_still_size_floored():
    """B822's surviving contribution: thin stubs cannot match any lexicon and are not counted."""
    assert g.LEXICON_MIN_BYTES == 2000
    assert "LEXICON_MIN_BYTES" in _gate_src()


def test_the_gate_reports_what_it_excluded():
    ok, msg = g.gate_atlas_lexicon_current()
    assert ok, msg
    assert "thin arcs excluded" in msg, "the gate must report what it excluded, not hide it"


def test_the_gate_no_longer_asserts_ROTTING():
    """B821 showed count-plus-rate cannot support that inference. It must never come back."""
    assert "ROTTING" not in _gate_src()


def test_instrument_arcs_are_still_counted_not_filtered_out():
    """B822 refused to exclude by TOPIC, because that lets the number be tuned by relabelling.

    B823 kept that: instrument arcs are still counted as blind, and are DISPOSITIONED in the
    registry rather than silently dropped from the metric.
    """
    reg = (ROOT / "docs" / "atlas" / "BLIND_ARCS.md").read_text(encoding="utf-8")
    rows = re.findall(r"^\| `(B\d+)` \| \*?\*?(GAP|INSTRUMENT)", reg, re.M)
    assert any(d == "INSTRUMENT" for _, d in rows), (
        "instrument arcs must appear IN the registry -- counted and judged, not filtered away")
    src = _gate_src()
    assert "INSTRUMENT" in src and "GAP" in src, "the gate must ask for the disposition explicitly"
