"""B1087 lock: the charge complementarity — spectra exact, O3 non-commutation real.

Recomputes the hv16 JM triple from the arc's own stored solve path is too heavy for the
suite; this lock pins the banked facts from b1087_results.json and re-verifies the
1+8+9+8+1 balance and the halving relation between slots.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def _load():
    return json.load(open(ROOT / "frontier/B1087_charge_grading/b1087_results.json"))

def test_both_slots_obstructed_O3():
    r = _load()
    assert r["hv8"][0] == "OBSTRUCTED-O3"
    assert r["hv16"][0] == "OBSTRUCTED-O3"

def test_spectra_1_8_9_8_1_balanced():
    r = _load()
    for slot in ("hv8", "hv16"):
        spec = {int(q): int(m) for q, m in r[slot][1]}
        assert sum(spec.values()) == 27
        assert sorted(spec.values(), reverse=True) == [9, 8, 8, 1, 1]
        assert spec[0] == 9
        assert sum(q * m for q, m in spec.items()) == 0     # trace zero
        assert all(spec.get(-q, 0) == m for q, m in spec.items())  # +-q balanced

def test_slot_halving():
    r = _load()
    s8 = {int(q): int(m) for q, m in r["hv8"][1]}
    s16 = {int(q): int(m) for q, m in r["hv16"][1]}
    assert {q: m for q, m in s8.items()} == {2 * q: m for q, m in s16.items()}
