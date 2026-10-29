"""The weave-or-thread register for the W arcs (docs/workdesk/THE_LABELS_RULE_2026-10-29.md, committed first).

Main's field, unchanged, on every arc of NOTE's status table: copied where the record states it, assigned by the seat
under the rule where it does not. The register must rebuild exactly from the record, and a new W arc fails here until
its record step gives it an entry.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07" / "W_VERDICTS.json"
SCRIPT = ROOT / "docs" / "workdesk" / "w_labels.py"


def _reg():
    return json.loads(REG.read_text(encoding="utf-8"))


def test_the_register_rebuilds_exactly_from_the_record_with_no_arc_missing():
    r = subprocess.run([sys.executable, "-B", str(SCRIPT), "--check"], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr


def test_every_label_is_mains_convention():
    for e in _reg()["arcs"]:
        first = e["weave_or_thread"].split()[0]
        assert first in {"weave", "thread", "neither"}, e["id"]
        if first == "neither":
            assert "(" in e["weave_or_thread"], f"{e['id']}: neither carries its reason"
        assert e["source"] == "status row" or e["source"] == "assigned" or e["source"].split(":")[0] in (
            "NOTE.md", f"{e['id']}_RULE.md"), e["id"]


def test_the_first_record_of_the_register():
    reg = _reg()
    ids = [e["id"] for e in reg["arcs"]]
    assert len(ids) == len(set(ids)) >= 171
    assert reg["rule"] == "docs/workdesk/THE_LABELS_RULE_2026-10-29.md"
    assert [c["id"] for c in reg["conflicts"]][:1] == ["W125"]
    by = {e["id"]: e for e in reg["arcs"]}
    assert by["W125"]["weave_or_thread"] == "thread" and by["W125"]["source"] == "status row"
    assert by["W1"]["source"] == "assigned" and by["W1"]["weave_or_thread"].startswith("weave")
    assert by["W93"]["weave_or_thread"].startswith("neither (a fibre-frame result at one τ")
