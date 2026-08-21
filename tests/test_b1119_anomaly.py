"""B1119 lock -- the anomaly resolved + the classification-as-checksum method."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
F = " ".join((ROOT / "frontier/B1119_anomaly_resolved/FINDINGS.md")
             .read_text(encoding="utf-8").split())


def test_root_cause_and_method():
    assert "FAKE INVARIANT FORM" in F
    assert "ad-invariant" in F and "τ-invariant" in F
    assert "classification theorem as" in F and "checksum" in F


def test_corrected_verdicts_and_lorentz_unaffected():
    assert "E₆(2)" in F and "E₆(6)" in F
    assert "Neither lift gives compact color" in F
    assert "B1114's Lorentz algebra is UNAFFECTED" in F or "Lorentz algebra is UNAFFECTED" in F
