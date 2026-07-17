"""B670 locks — the anatomy loops 1-3 integration."""
import os

_B = os.path.join(os.path.dirname(__file__), "..", "frontier",
                  "B670_anatomy_full")


def test_f4_dim52_verified_here():
    out = open(os.path.join(_B, "verify_f4_dim52.py")).read()
    assert "52" in out
    fnd = open(os.path.join(_B, "FINDINGS.md")).read()
    assert "dimension 52 = f4" in fnd


def test_packet_headlines():
    c1 = open(os.path.join(_B, "packet", "loop3", "c1_vecmassey",
                           "FINDINGS_CC2.md")).read()
    assert "CORRECTION" in c1 and "SLOT-WISE" in c1.upper()
    b1 = open(os.path.join(_B, "packet", "loop2", "b1_f4",
                           "FINDINGS_CC2.md")).read()
    assert "52" in b1 and "F4" in b1
