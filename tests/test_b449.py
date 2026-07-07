"""Lock for B449 — the forcing-boundary adjudication + the conductor law."""
import os
import sys

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B449_forcing_boundary")
sys.path.insert(0, HERE)


def test_conductor_law_and_adjudication():
    import conductor_law as C
    assert C.run()
