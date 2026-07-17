"""B669 locks — track H refuted (artifact-level)."""
import os

_B = os.path.join(os.path.dirname(__file__), "..", "frontier",
                  "B669_track_h_adjudication")


def test_h1_proper_control_and_verdicts():
    out = open(os.path.join(_B, "h1_proper_output.txt")).read()
    assert "C1 CONTROL — reproduces the banked fig-8 ladder "\
           "[1, 1, 1, 0, 1, 1, 2, 1]: True" in out
    assert out.count("BOUNDED (finite q-support => periodic => bounded)") == 4
    assert "REFUTED" in out


def test_m136_amphichiral_and_first_pass_preserved():
    out = open(os.path.join(_B, "h1_output.txt")).read()
    assert "|Isom(m136)| = 8; amphichiral: True" in out
    # the wrong-object first pass is preserved with its failing control
    assert "C1 fig-8 control reproduces banked [1, 1, 1, 0, 1, 1, 2, 1]: "\
           "False" in out
