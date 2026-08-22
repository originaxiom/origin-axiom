"""B1133 lock -- C4 recognized = (278392949/1813985280) pi^4 C0; single-end (5 at exp 1,
no growth, no sqrt5); re-derived here and matched vs B1124's computed C4."""
import json
from pathlib import Path
import mpmath as mp, sympy as sp
ARC = Path(__file__).resolve().parents[1] / "frontier" / "B1133_c4_single_end"
B1124 = Path(__file__).resolve().parents[1] / "frontier" / "B1124_allorders_arithmetic"


def test_c4_closed_form_matches_computed():
    mp.mp.dps = 45
    C0 = mp.power(3, mp.mpf(-1) / 4)
    C4 = mp.mpf(278392949) / 1813985280 * mp.pi**4 * C0
    r = json.loads((B1124 / "b1124_results.json").read_text(encoding="utf-8"))
    c4v = mp.mpf(str(r["stability_analysis"]["C4"]["POOLED"]["best_value"]))
    assert abs(C4 - c4v) < mp.mpf('1e-20')           # matches the independently-computed C4


def test_single_end_the_5_does_not_grow():
    fac = sp.factorint(1813985280)
    assert fac == {2: 11, 3: 11, 5: 1}               # 5 at exponent 1, same as C3 -> no growth
    assert sp.isprime(278392949)                     # numerator prime


def test_findings_single_end_and_five_orders():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "SINGLE-END" in f and "does NOT grow" in f
    assert "no √5 appears" in f or "no √5" in f
    assert "five consecutive orders" in f.lower() or "FIVE consecutive orders" in f
