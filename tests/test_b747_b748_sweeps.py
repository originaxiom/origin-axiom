"""Locks for B747 (sqrt5 mirror sweep) + B748 (V4 completion) -- artifact locks
(the sweeps run in the Sage env; the canonical pyenv suite locks the committed
outputs, the sealed input's integrity, and the parity bookkeeping)."""
import hashlib
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
B747 = os.path.join(ROOT, "frontier", "B747_mirror_sweep")
B748 = os.path.join(ROOT, "frontier", "B748_v4_completion")
SEALED_SHA = "77818016ab051c4a43eaa832ac626e7ed582d2af5618525d4d3f030d88010bee"


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def test_sealed_input_integrity_and_parity_split():
    for arc in (B747, B748):
        p = os.path.join(arc, "door1_final_sealed_input.json")
        assert hashlib.sha256(open(p, "rb").read()).hexdigest() == SEALED_SHA
    rows = json.load(open(os.path.join(B747, "door1_final_sealed_input.json")))
    assert len(rows) == 78
    odd = [r for r in rows if r["degree"] % 2 == 1]
    even = [r for r in rows if r["degree"] % 2 == 0]
    assert (len(odd), len(even)) == (54, 24)
    assert all(not r["contains_sqrt_m3"] for r in rows)      # the B740/B288 census fact


def test_b747_verdict_mirror_silent():
    out = _read(os.path.join(B747, "b747_out.txt"))
    assert "TALLY: 54 excluded by parity + 23 exact-negative + 0 HITS" in out
    assert out.count("contains sqrt5 = False") == 23
    assert "contains sqrt5 = True" not in out.split("STAGE 2")[1]
    closure = _read(os.path.join(B747, "b747_closure_out.txt"))
    assert "isometry 4_1(3,8) ~ 4_1(-3,8) VERIFIED: True" in closure
    assert "deg 30, contains sqrt5 = False" in closure


def test_b748_verdict_v4_silent_and_b740_consistency():
    out = _read(os.path.join(B748, "b748_out.txt"))
    assert "TALLY: 54 parity + 24 exact-negative + 0 HITS + 0 unresolved" in out
    assert "consistency failures: []" in out
    assert "VERDICT: V4-SILENT" in out
    assert out.count("== sealed False: True") == 24


def test_controls_present_in_both_runs():
    o747 = _read(os.path.join(B747, "b747_out.txt"))
    assert "[ctrl] Q(sqrt5) contains sqrt5: True" in o747
    assert "[ctrl] m004 pipeline: contains sqrt-3 True (True), sqrt5 False (False)" in o747
    o748 = _read(os.path.join(B748, "b748_out.txt"))
    assert "[ctrl] Q(sqrt-15) contains sqrt-15: True" in o748
    assert "[ctrl] m004: sqrt-3 True (True), sqrt-15 False (False)" in o748
