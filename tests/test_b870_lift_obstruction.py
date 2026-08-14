"""Locks B870 -- G7: the lift obstruction on the object and the sister."""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B870_lift_obstruction"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def test_presentations_and_exponent_sums():
    assert RES["m004"]["relator"] == "aaabABBAb"
    assert RES["m004"]["exponent_sums"] == [1, 0] and RES["m004"]["gcd"] == 1
    assert RES["m003"]["relator"] == "abAAbabbb"
    assert RES["m003"]["exponent_sums"] == [0, 5] and RES["m003"]["gcd"] == 5


def test_asphericity_hypothesis_certified():
    """Lyndon needs relator-not-a-proper-power; both certified by direct period check."""
    assert RES["m004"]["not_proper_power"] is True
    assert RES["m003"]["not_proper_power"] is True


def test_h1_cross_checked_against_snappy():
    assert RES["m004"]["snappy_homology"] == "Z" and RES["m004"]["h1_matches"]
    assert RES["m003"]["snappy_homology"] == "Z/5 + Z" and RES["m003"]["h1_matches"]


def test_object_unobstructed_at_every_prime():
    assert RES["verdicts"]["object_unobstructed_all_primes"] is True
    assert all(v == 1 for v in RES["m004"]["H2"].values())


def test_e6_center_and_sm_z6_lift_on_the_object():
    assert RES["verdicts"]["object_E6_center_Z3"] == {"H2": 1, "lifts_torsor": 3}
    assert RES["verdicts"]["object_SM_Z6"] == {"H2": 1, "lifts_torsor": 6}


def test_the_object_sister_split_at_5():
    """Both vanish at the atom prime 3; at 5 the sister alone turns on: Z/5."""
    assert RES["verdicts"]["sister_at_atom_prime_3"] == 1
    assert RES["verdicts"]["sister_at_5"] == 5
    assert RES["verdicts"]["split"] is True


def test_findings_state_the_scope_honestly():
    assert "a nonzero obstruction group means obstructed bundles are possible, not that any given flat bundle is obstructed" in _F
    assert "not established here" in _F
    assert "culler" in _F
    assert "h²(m, ∂m) is not computed by this arc" in _F
