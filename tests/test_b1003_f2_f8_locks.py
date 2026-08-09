"""B1003 — the two missing axiom-price locks: F2 (A2's price) and F8 (A4/A5's price).

B998 found THEOREM_LEDGER citing `test_b749_genesis_forks.py` as the lock for C1–C4 while that
file tests only F4–F7 — no F2, no F8. **B998 was right about the LOCKS and wrong to imply the
COMPUTATIONS were missing**: B749 computed all seven forks, with `compute.py`, `output.txt` and a
verdict in `RESULTS.json` for each. What was absent was any test asserting those verdicts, so a
regression in `RESULTS.json` would have been silent.

These are the locks. They assert the two prices that are the programme's OWN computations rather
than classical results — the ones B998 correctly identified as the load-bearing gap.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
RESULTS = ROOT / "frontier" / "B749_genesis_forks" / "RESULTS.json"


def _verdicts():
    return json.loads(RESULTS.read_text(encoding="utf-8"))["verdicts"]


def test_all_seven_forks_carry_a_verdict():
    """B998's premise checked from the other side: the computations exist for every fork."""
    v = _verdicts()
    assert set(v) == {"F2", "F3", "F4", "F5", "F6", "F7", "F8"}, sorted(v)


def test_f2_prices_A2_and_is_robust():
    """A2 (inexhaustibility). Allowing periodicity must LOSE the hyperbolic carrier."""
    f2 = _verdicts()["F2"]
    assert f2["verdict"] == "ROBUST"
    facts = f2["computed_facts"]
    # the load-bearing measurement: the whole sibling family has NO pseudo-Anosov
    assert "pA count 0" in facts, "F2's content is that the periodic siblings admit no pA"
    assert "max|eigenvalue|=1" in facts
    # and it was falsifiable -- MB12, checked in the arc itself
    assert "FRAGILE would have been triggered" in f2.get("vacuity_note", "")


def test_f8_prices_the_carrier_and_geometry_is_necessary():
    """A5 (the geometric carrier). The combinatorial carrier must NOT reach Q(sqrt(-3))."""
    f8 = _verdicts()["F8"]
    assert f8["verdict"] == "GEOMETRY-NECESSARY"
    facts = f8["computed_facts"]
    # the four pre-registered redundancy witnesses all fail
    assert "All four pre-registered redundancy witnesses FAIL" in facts
    # the sharpest single fact: x^2+3 stays irreducible over the hearing field
    assert "x^2+3 irreducible over Q(sqrt5)" in facts
    # the ordered K0 is the golden order -- the carrier sees hearing only
    assert "Z[phi]" in facts
    # and the criterion could have fired -- the arc proves it, not just claims it
    assert "squares to -3I" in f8.get("vacuity_note", ""), "W3 must be shown satisfiable"


def test_the_two_fragile_forks_are_orientation_and_the_puncture():
    """The chain's real price: five cheap axioms, TWO load-bearing ones."""
    v = _verdicts()
    fragile = sorted(k for k, r in v.items() if r["verdict"] == "FRAGILE")
    assert fragile == ["F5", "F6"], f"expected orientation + puncture, got {fragile}"


def test_f5_records_that_the_monodromy_is_the_golden_matrix_squared():
    """A6's sibling is Gieseking, and the identity behind it is A = F^2 (B14)."""
    assert "M^2 = RL" in _verdicts()["F5"]["computed_facts"]
