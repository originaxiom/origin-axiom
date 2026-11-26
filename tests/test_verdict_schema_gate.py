"""R81-3 (register rows P-810 and P-881; main's M48, 2026-11-24): the schema's test of the verdict files is a gate.

The gate `verdict-schema` runs the test's own checks on every verdict file. Each planted file below breaks one rule the
test holds, and stands with a twin that keeps it."""
import json, os, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts" / "gates"))
import gates

GOOD = {"id": "B99990", "verdict": "PROVED", "claim_one_line": "a planted line", "instrument": False, "creates_law": False,
        "identifications": [], "scope": {"frame": "none", "object": "a planted object", "reach": "single", "hypotheses": "none"}}


def _plant(tmp_path, name, d):
    folder = tmp_path / name
    folder.mkdir()
    p = folder / "arc_verdict.json"
    p.write_text(d if isinstance(d, str) else json.dumps(d), encoding="utf-8")
    return p


def test_a_verdict_file_that_breaks_the_schema_fails_the_gate_and_its_twin_passes(tmp_path):
    """the control: a verdict file whose scope carries a key the schema does not have, as P-810's eleven did"""
    good = _plant(tmp_path, "B99990_good", GOOD)
    assert gates.gate_verdict_schema(_files=[good])[0]
    bad = _plant(tmp_path, "B99991_bad", dict(GOOD, id="B99991", scope=dict(GOOD["scope"], domain="the eleven's extra key")))
    ok, msg = gates.gate_verdict_schema(_files=[good, bad])
    assert not ok and "B99991" in msg and "1 verdict file(s)" in msg


def test_each_rule_of_the_schema_reaches_the_gate(tmp_path):
    cases = {
        "B99992_noinstr": {k: v for k, v in dict(GOOD, id="B99992").items() if k != "instrument"},
        "B99993_enum": dict(GOOD, id="B99993", verdict="SETTLED"),
        "B99994_idmismatch": dict(GOOD, id="B99999"),
        "B99995_noscope": {k: v for k, v in dict(GOOD, id="B99995").items() if k != "scope"},
        "B99996_reach": dict(GOOD, id="B99996", scope=dict(GOOD["scope"], reach="the programme")),
        "B99997_nolaw": {k: v for k, v in dict(GOOD, id="B99997").items() if k != "creates_law"},
        "B99998_json": "{ not json",
    }
    for name, d in cases.items():
        p = _plant(tmp_path, name, d)
        ok, msg = gates.gate_verdict_schema(_files=[p])
        assert not ok, name


def test_on_the_record_the_gate_passes_and_reads_every_file():
    ok, msg = gates.gate_verdict_schema()
    assert ok, msg
    assert len(gates._verdict_schema_test().FILES) > 900
    reg = json.load(open(ROOT / "tests" / "GATE_CONTROLS.json", encoding="utf-8"))
    assert reg["verdict-schema"].endswith("::test_a_verdict_file_that_breaks_the_schema_fails_the_gate_and_its_twin_passes")
