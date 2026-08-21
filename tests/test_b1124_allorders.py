"""B1124 lock -- V-1 all-orders: the parity law extends to C3, C3 = (724351/12597120)
sqrt3 pi^3 C0 (odd k -> sqrt3), recognized to ~36 digits; the {2,3}-smoothness anomaly
(factor of 5) disclosed. This bench re-derives the closed form from the banked pooled fit.

NB: mp.mp.dps is set INSIDE each test (not module-level) -- mpmath's precision is a
global the pytest session shares, so a module-level setting is silently overwritten by
another test module's import (the precision-context bug L180 itself caught)."""
import json
from fractions import Fraction
from pathlib import Path
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1124_allorders_arithmetic"


def _pooled(r, k):
    return mp.mpf(str(r["stability_analysis"][k]["POOLED"]["best_value"]))


def test_C3_closed_form_and_parity():
    mp.mp.dps = 60
    r = json.loads((ARC / "b1124_results.json").read_text(encoding="utf-8"))
    C0 = mp.power(3, mp.mpf(-1) / 4)
    C3 = _pooled(r, "C3")
    q3 = Fraction(724351, 12597120)
    closed = mp.mpf(q3.numerator) / q3.denominator * mp.sqrt(3) * mp.pi**3 * C0
    # the recognition matches the computed pooled C3 to deep precision (odd k -> sqrt3)
    assert abs(C3 - closed) < mp.mpf('1e-25'), abs(C3 - closed)
    # pipeline sanity: C1, C2 reproduce the banked closed forms (ground-truth validation)
    C1, C2 = _pooled(r, "C1"), _pooled(r, "C2")
    assert abs(C1 / C0 - mp.mpf(11) / 108 * mp.sqrt(3) * mp.pi) < mp.mpf('1e-20')
    assert abs(C2 / C0 - mp.mpf(697) / 7776 * mp.pi**2) < mp.mpf('1e-20')


def test_smoothness_anomaly_disclosed():
    # the factor of 5 is real and the FINDINGS disclose it (not {2,3}-smooth)
    assert 12597120 == 2**7 * 3**9 * 5
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "2⁷·3⁹·5" in f or "2^7*3^9*5" in f or "2⁷·3⁹·**5**" in f
    assert "detection, not derivation" in f.lower()
    assert "C₄" in f and "PRECISION-FLOOR" in f
