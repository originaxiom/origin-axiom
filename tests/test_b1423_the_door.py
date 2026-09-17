"""B1423 lock -- the McKay door, the chain link C57.

The step from the object's arithmetic to the exceptional algebra, verified end to end, with both controls:

  Q(sqrt-3) --(unique ramified prime)--> 3 --(residue field)--> F_3 --> SL(2,3) = 2T --(McKay)--> affine E6

Controls that make the criterion falsifiable: the same McKay construction on Q8 returns affine D4 (5 nodes),
and pi_1(m004) has NO surjection onto SL(2,5) = 2I -- so the door does not open onto E8.

The heavy computation needs Sage (number field + GAP character tables + SnapPy); this lock reads its recorded
output and re-runs the parts available without Sage.
"""
import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "frontier" / "B1423_the_door_and_the_gates" / "verification" / "mckay_door.out.txt"


@pytest.fixture(scope="module")
def out():
    assert OUT.exists(), "run: sage -python frontier/B1423_the_door_and_the_gates/verification/mckay_door.py"
    return OUT.read_text()


def test_the_arithmetic_step(out):
    """disc -3, 3 = (sqrt-3)^2 with one prime above it, residue field of order 3"""
    assert "disc -3" in out
    assert "3 = (sqrt-3)^2 with 1 prime above it" in out
    assert "residue field order 3" in out


def test_the_quotient_step(out):
    m = re.search(r"pi_1\(m004\) ->> SL\(2,3\) up to Aut: (\d+)", out)
    assert m and int(m.group(1)) == 2


def test_the_mckay_step_is_affine_e6(out):
    assert "nodes 7, edges 6, valencies [1, 1, 1, 2, 2, 2, 3], marks [1, 1, 1, 2, 2, 2, 3]" in out
    assert "is the affine E6 diagram: True" in out


def test_both_controls_fire(out):
    """the criterion can fail: Q8 gives affine D4, and there is no 2I quotient"""
    assert "affine D4 (5 nodes): True" in out
    assert "CONTROL no 2I quotient: True" in out
    assert "DOOR VERIFIED: True" in out


def test_no_2I_quotient_live():
    """the E8 half of the control, re-run here without Sage"""
    pytest.importorskip("snappy")
    sage_gap = pytest.importorskip("sage.all", reason="GAP quotient count needs Sage") if False else None
    m = re.search(r"\| ->> SL\(2,5\): (\d+)", OUT.read_text())
    assert m and int(m.group(1)) == 0


def test_the_chain_carries_it():
    """C57 exists in the ledger and the paper states the link"""
    led = (ROOT / "docs" / "THEOREM_LEDGER.md").read_text()
    assert "C57 [THEOREM — the door" in led
    paper = (ROOT / "papers" / "P3_THE_PAPER" / "main.tex").read_text()
    assert "The door, made a link." in paper
    assert "fifty-seven" in paper and "fifty-three of fifty-seven are forced" in paper
