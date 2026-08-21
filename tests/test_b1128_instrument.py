"""B1128 lock -- P-INSTRUMENT: INSTRUMENT-NULL; the coupling predicts |Ue1|/|Ue2|=phi
which misses; the degeneracy h(RRLL)=-phi h(RL) is exact (the honest boundary)."""
import json
from pathlib import Path
ARC = Path(__file__).resolve().parents[1] / "frontier" / "B1128_instrument_null"


def test_verdict_and_degeneracy():
    r = json.loads((ARC / "b1128_results.json").read_text(encoding="utf-8"))
    assert r["verdict"] == "INSTRUMENT-NULL"
    # the degeneracy that collapsed the test, verified to deep precision
    d = r["degeneracy_diagnosis"]
    assert float(d["verified_on_curve_worst_residual"]) < 1e-30


def test_findings_carry_the_fences():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "INSTRUMENT-NULL" in f
    assert "|U_e1|/|U_e2| = φ" in f and "MISS" in f
    assert "Not numerology" in f and "absorbed ZERO effective dof" in f
    assert "different meridian" in f.lower()   # the named soft spot
    assert "h(R²L², θ) = −φ·h(RL, θ)" in f      # the side-finding flagged
