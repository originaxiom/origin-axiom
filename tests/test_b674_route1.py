"""B674 route-1 locks."""
import json
import os

_B = os.path.join(os.path.dirname(__file__), "..", "frontier",
                  "B674_generation_leg", "cellES")


def test_trace_silence_and_golden_rotation():
    t = json.load(open(os.path.join(_B, "cellES_traces.json")))
    s = json.dumps(t)
    # [CORRECTED 2026-11-12 (Review 80, the web seat's finding 1): this assert ended in `or True`, which made it unable to fail; the constant is gone and the statement holds]
    assert "phi" in s.lower() or "golden" in s.lower()
    out = open(os.path.join(_B, "cellES_output.txt"),
               errors="ignore").read()
    assert "MISS" in out or "silent" in out.lower()


def test_mismatch_table_exists():
    m = json.load(open(os.path.join(_B, "cellES_mismatch_table.json")))
    assert m
