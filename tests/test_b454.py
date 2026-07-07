"""Lock for B454 — Ethogram E2: the closure lemma + exact scan."""
import os
import sys

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B454_ethogram_e2_closure")
sys.path.insert(0, HERE)


def test_closure_lemma_and_scan():
    import closure
    assert closure.run()
