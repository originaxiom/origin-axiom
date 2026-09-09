"""B1231 — the identification discipline.

These locks assert FACTS about the register and the ratchet, and they PIN the two live UNEARNED
rows: if a later seat quietly upgrades I-6 or I-7 to EARNED without exhibiting a map, the suite
reds. That is the whole point — the failure mode this arc exists for is a seat deciding two things
are the same because their labels match.
"""
import importlib.util
import io
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs" / "IDENTIFICATION_LEDGER.md"
BASELINE = ROOT / "docs" / "IDENTIFICATION_BASELINE.json"
TOOL = ROOT / "scripts" / "checks" / "identification_audit.py"


def _rows():
    out = {}
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(I-\d+)\s*\|(.*)", line)
        if not m:
            continue
        cells = [c.strip().replace("*", "") for c in m.group(2).split("|")]
        out[m.group(1)] = next((c for c in cells
                                if c in ("EARNED", "REFUTED", "UNEARNED")), "?")
    return out


def _gates():
    spec = importlib.util.spec_from_file_location("b1231_gates", ROOT / "scripts" / "gates" / "gates.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_register_is_seeded_and_parses():
    r = _rows()
    assert len(r) >= 7, r
    assert sum(1 for v in r.values() if v == "EARNED") >= 3
    assert sum(1 for v in r.values() if v == "REFUTED") >= 2


def test_the_two_live_unearned_stay_unearned():
    """I-6 (B1228's nomination) and I-7 (B1230/C-5b's Z/3 cut). Upgrading either without a map is
    exactly the error this arc names. If you have earned one, say so in the ledger AND here."""
    r = _rows()
    assert r.get("I-6") == "UNEARNED", r.get("I-6")
    assert r.get("I-7") == "UNEARNED", r.get("I-7")


def test_the_ratchet_bites():
    """A NEW unearned identification must red the gate — that is when it would have been caught."""
    g = _gates()
    ok_before, _ = g.gate_identification_register()
    assert ok_before, "register must be green before the bite test"
    orig = LEDGER.read_text(encoding="utf-8")
    try:
        LEDGER.write_text(orig.replace(
            "| I-7 |",
            "| I-99 | synthetic | A | B | ✘ | ✘ | **UNEARNED** | test | test |\n| I-7 |", 1),
            encoding="utf-8")
        g2 = _gates()                      # re-import: the gate reads the file at call time
        ok_after, detail = g2.gate_identification_register()
        assert not ok_after, "the ratchet did NOT bite on a new UNEARNED row"
        assert any("UNEARNED increased" in str(d) for d in detail), detail
    finally:
        LEDGER.write_text(orig, encoding="utf-8")
    assert _gates().gate_identification_register()[0], "register must be restored"


def test_baseline_matches_the_register():
    base = json.loads(BASELINE.read_text(encoding="utf-8"))
    live = sum(1 for v in _rows().values() if v == "UNEARNED")
    assert base["unearned"] == live, (base["unearned"], live)


def test_instrument_selftest_passes_including_the_blind_spot():
    """The tool's own controls, INCLUDING the control that asserts its recall limit. The detector
    misses the bare 'X IS Y' form — which is how C-5b's error was actually phrased — and that must
    stay asserted so nobody mistakes --extract for coverage."""
    r = subprocess.run([sys.executable, str(TOOL), "--selftest"],
                       capture_output=True, text=True, cwd=str(ROOT))
    assert r.returncode == 0, r.stdout + r.stderr
    assert "CONTROLS PASS" in r.stdout
    assert "KNOWN BLIND SPOT" in r.stdout
    assert "RECALL IS PARTIAL BY DESIGN" in r.stdout


def test_the_rule_is_binding_and_names_its_template():
    w = (ROOT / "WORKING_RULES.md").read_text(encoding="utf-8")
    assert "THE IDENTIFICATION RULE" in w
    assert "Direct is not semidirect" in w        # B1223, the template
    assert "B1225" in w                            # why it is an INPUT, not a slip


def test_this_arc_declares_its_identifications():
    d = json.loads((ROOT / "frontier" / "B1231_identification_discipline" /
                    "arc_verdict.json").read_text(encoding="utf-8"))
    assert "identifications" in d
    assert {i["row"] for i in d["identifications"]} == {"I-6", "I-7"}
