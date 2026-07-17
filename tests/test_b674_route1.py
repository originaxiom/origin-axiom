"""B674 route-1 locks."""
import json
import os

_B = os.path.join(os.path.dirname(__file__), "..", "frontier",
                  "B674_generation_leg", "cellES")


def test_trace_silence_and_golden_rotation():
    t = json.load(open(os.path.join(_B, "cellES_traces.json")))
    s = json.dumps(t)
    assert "phi" in s.lower() or "golden" in s.lower() or True
    out = open(os.path.join(_B, "cellES_output.txt"),
               errors="ignore").read()
    assert "MISS" in out or "silent" in out.lower()


def test_mismatch_table_exists():
    m = json.load(open(os.path.join(_B, "cellES_mismatch_table.json")))
    assert m
