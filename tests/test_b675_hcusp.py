"""B675 locks — H-CUSP predicts (artifact-level)."""
import os

_B = os.path.join(os.path.dirname(__file__), "..", "frontier",
                  "B675_hcusp_sweep")


def test_silver_tau_and_assignment():
    out = open(os.path.join(_B, "cell_output.txt"),
               errors="ignore").read()
    assert "-2i" in out or "-2*I" in out or "2i" in out
    assert "A3" in out


def test_addendum_presealed():
    t = open(os.path.join(_B, "PREREG_ADDENDUM_OUTCOMES.md")).read()
    assert "ENTANGLEMENT-CONFOUNDED" in t
