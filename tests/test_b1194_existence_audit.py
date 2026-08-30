"""B1194 lock -- the existence audit."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_arc():
    d = json.loads((ROOT / "frontier" / "B1194_existence_audit" / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["verdict"] == "PROVED"
    assert "EIGHT items" in d["claim_one_line"] and "THE COSMOLOGY LEDGER" in d["claim_one_line"]


def test_cells():
    d = json.loads((ROOT / "frontier" / "B1194_existence_audit" / "verification" / "audit_cells.json").read_text(encoding="utf-8"))
    assert len(d) == 6 and all(k.startswith("EX-") for k in d)   # one agent renamed its key
