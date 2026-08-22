"""B1132 lock -- instrument null on the full sphere + the golden meridian law.
The phi-law's y-component is re-derived symbolically here (the load-bearing sub-identity)."""
import json
from pathlib import Path
import sympy as sp
ARC = Path(__file__).resolve().parents[1] / "frontier" / "B1132_meridian_null_phi_law"


def test_verdict_null_full_sphere():
    r = json.loads((ARC / "b1132_results.json").read_text(encoding="utf-8"))
    assert "INSTRUMENT-NULL-FULL-SPHERE" in json.dumps(r)


def test_phi_law_y_component_symbolic():
    # axis(R^2L^2) = -phi*[axis(RL) + yhat]; check the y-component with wy(RL)=-phi/2
    phi = (1 + sp.sqrt(5)) / 2
    wy_RL = -phi / 2
    wy_RRLL = (1 - phi) / 2
    assert sp.simplify(wy_RRLL - (-phi * (wy_RL + 1))) == 0


def test_findings_carry_law_and_domain():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "INSTRUMENT-NULL-FULL-SPHERE" in f
    assert "h(R²L², u) = −φ·h(RL, u) − iφ·n_y(u)" in f
    assert "n_y(u)=0" in f and "real great circle" in f      # the domain
    assert "NOT a cc3-flaggable positive" in f or "not a cc3-flaggable positive" in f.lower()
