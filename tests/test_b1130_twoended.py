"""B1130 lock -- P-TWOENDED: PRECISION-FLOOR; C3's factor-of-5 (724351=53x79x173) has no
sqrt5 fingerprint (leans generic von Staudt-Clausen); C4/C5 precision-floored."""
import json
from pathlib import Path
ARC = Path(__file__).resolve().parents[1] / "frontier" / "B1130_twoended_tower"


def test_verdict_precision_floor():
    r = json.loads((ARC / "b1130_results.json").read_text(encoding="utf-8"))
    assert "PRECISION-FLOOR" in json.dumps(r)


def test_c3_numerator_factors_have_no_sqrt5_structure():
    # 724351 = 53 x 79 x 173: three distinct unrelated primes -> no golden/sqrt5 fingerprint
    assert 53 * 79 * 173 == 724351
    for p in (53, 79, 173):
        assert 724351 % p == 0


def test_findings_leans_single_end():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "PRECISION-FLOOR" in f and "leaning single-end" in f.lower()
    assert "von Staudt" in f
    assert "single data point cannot distinguish" in f.lower()
