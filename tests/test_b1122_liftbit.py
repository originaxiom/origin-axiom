"""B1122 lock -- L179 the lift-bit meter: PAIR-INVISIBLE (the negative + the mechanism)."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]


def test_verdict_pair_invisible():
    r = json.loads((ROOT / "frontier/B1122_liftbit_meter/b1122_results.json")
                   .read_text(encoding="utf-8"))
    blob = json.dumps(r)
    assert "PAIR-INVISIBLE" in blob or r.get("verdict") == "PAIR-INVISIBLE"


def test_findings_carry_the_mechanism():
    f = " ".join((ROOT / "frontier/B1122_liftbit_meter/FINDINGS.md")
                 .read_text(encoding="utf-8").split())
    assert "central" in f.lower() and "sign operator" in f.lower()
    assert "STRONGER no-go than B1087" in f
    assert "do NOT happen" in f or "does NOT happen" in f  # the fusion fails
