"""B650 locks — the type system's battery is reproducible."""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
B650 = os.path.join(HERE, "..", "frontier", "B650_typed_functor")


def test_checker_reproduces_battery():
    out = subprocess.run([sys.executable,
                          os.path.join(B650, "types_checker.py")],
                         capture_output=True, text=True).stdout
    assert "B584 antiphase-listener coefficient: ('T_coup(listener)', ('W(RL)', 'core', 'dimless'))" in out
    assert "B613 closure predicate: ('T_spec'" in out
    assert "B632/B637 chord cubic Y: ('T_coup(partner-object)'" in out
    assert "ILL-TYPED" not in out  # post-revision: everything types


def test_frozen_hash_recorded():
    hh = open(os.path.join(B650, "ARTIFACT_HASHES.txt")).read()
    assert "306d6cde" in hh and "FROZEN before the held-out check" in hh
    fnd = open(os.path.join(B650, "FINDINGS.md")).read()
    assert "one disclosed revision cycle used" in fnd.lower()
    assert "K1 does not fire" in fnd
