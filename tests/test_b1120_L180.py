"""B1120 lock -- L180 the make-or-break: the tower coefficients are trace-field
arithmetic at TWO orders (EULER-STRUCTURE-CONFIRMED). This bench re-derives both
closed forms from the banked pooled fits."""
import json
from pathlib import Path
import mpmath as mp
mp.mp.dps = 50
ROOT = Path(__file__).resolve().parents[1]


def _pooled(r, k):
    return mp.mpf(str(r["stability_analysis"][k]["POOLED"]["best_value"]))


def test_C1_and_C2_are_trace_field_arithmetic():
    r = json.loads((ROOT / "frontier/B1120_L180_makeorbreak/b1120_results.json")
                   .read_text(encoding="utf-8"))
    C0 = mp.power(3, mp.mpf(-1) / 4)
    C1, C2 = _pooled(r, "C1"), _pooled(r, "C2")
    # C1 = (11/108) sqrt3 pi C0   (odd k -> rational x sqrt3)
    assert abs(C1 / C0 - mp.mpf(11) / 108 * mp.sqrt(3) * mp.pi) < mp.mpf('1e-15')
    # C2 = (697/7776) pi^2 C0     (even k -> plain rational)
    assert abs(C2 / C0 - mp.mpf(697) / 7776 * mp.pi**2) < mp.mpf('1e-15')
    # the reality-parity signature: C1/C0 divided by (sqrt3 pi) is rational 11/108;
    # C2/C0 divided by pi^2 is rational 697/7776 -- both in lowest terms
    from math import gcd
    assert gcd(11, 108) == 1 and gcd(697, 7776) == 1
    # verdict recorded EULER-STRUCTURE-CONFIRMED with both k precision-sufficient
    assert r["verdict"] == "EULER-STRUCTURE-CONFIRMED"
    assert r["precision_sufficient_by_k"]["C1"] and r["precision_sufficient_by_k"]["C2"]


def test_findings_state_two_order_positive_and_fence():
    f = " ".join((ROOT / "frontier/B1120_L180_makeorbreak/FINDINGS.md")
                 .read_text(encoding="utf-8").split())
    assert "EULER-STRUCTURE-CONFIRMED" in f
    assert "C₂ = (697/7776)·π²·C₀" in f
    assert "C₁ = (11/108)·√3·π·C₀" in f
    assert "OPEN, not negative" in f  # C3 honest fence
    assert "No SM value" in f or "does NOT deliver an SM value" in f
