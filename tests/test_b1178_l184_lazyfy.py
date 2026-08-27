"""B1178 lock -- L184 executed: the collection lazy-fy. Pins the two offenders' lazy shape
(no module-level heavy compute) + the recorded 12x win."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_offenders_are_lazy():
    for f in ("test_b371_two_state_sector.py", "test_cc2_r5_adopted.py"):
        txt = (ROOT / "tests" / f).read_text(encoding="utf-8")
        assert "functools.lru_cache" in txt, f
    # the b371 shape specifically: no module-level REPORT = run()
    b371 = (ROOT / "tests" / "test_b371_two_state_sector.py").read_text(encoding="utf-8")
    assert "\nREPORT = run()" not in b371


def test_arc_and_addendum():
    d = json.loads((ROOT / "frontier" / "B1178_l184_lazyfy" / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1178" and "12x" in d["claim_one_line"] and "OUTCOMES PRESERVED" in d["claim_one_line"]
    add = (ROOT / "frontier" / "B1177_instrument_bundle" / "ADDENDUM_measurements.md").read_text(encoding="utf-8")
    assert "156.95" in add and "launched, not yet complete" in add
    assert (ROOT / "frontier" / "B1177_instrument_bundle" / "collect_per_file.txt").exists()
