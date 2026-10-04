"""B1475 -- the spin swap, phase 1b: the stored census re-read (no mirror-invariant spin structure on any swap member;
D_{s0} in sqrt3.Q, zero on the controls; the symmetry step on every spin structure) and one member re-run live."""
import json, os, sys
from fractions import Fraction
from math import sqrt
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "frontier", "B1475_the_spin_swap_phase_1b_does_the_swap_carry_a_quantity", "verification")
SWAP = ["m003", "m207", "s955", "s957", "s960", "t12838", "o10_150695"]; FIX = ["m004", "s961", "t12839"]
EXPECT = {"m003": 1, "m207": -4, "s955": Fraction(1, 8), "s957": 8, "s960": -1, "t12838": 56, "o10_150695": -836}


def test_census_stored():
    d = json.load(open(os.path.join(V, "spin_quantity.json")))
    assert set(d) == set(SWAP + FIX)
    for nm in SWAP:
        r = d[nm]; assert r["mirror_invariant_any_tau"] == [] and not r["has_mirror_invariant_spin_structure"]
        q = float(r["D_s0_at_2"]) / sqrt(3); assert abs(q - float(EXPECT[nm])) < 1e-8, (nm, q)
    for nm in FIX:
        r = d[nm]; assert r["has_mirror_invariant_spin_structure"] and abs(float(r["D_s0_at_2"])) < 1e-30
    assert d["m004"]["mirror_invariant_any_tau"] == [[1, -1], [1, 1]] or len(d["m004"]["mirror_invariant_any_tau"]) == 2
    assert len(d["s961"]["mirror_invariant_any_tau"]) == 4 and len(d["t12839"]["mirror_invariant_any_tau"]) == 2
    assert sum(r["checks"]["symmetry_all_s"] for r in d.values()) == 432 and all(r["checks"]["symmetry_fail"] == 0 and r["checks"]["D_odd_fail"] == 0 for r in d.values())


def test_m003_live():
    sys.path.insert(0, V); sys.path.insert(0, os.path.join(ROOT, "frontier", "B1471_the_cancellation_is_a_theorem_of_amphichirality", "verification"))
    import spin_quantity as SQ
    sw = json.load(open(os.path.join(ROOT, "frontier", "B1474_the_spin_swap_phase_1a_fix_or_swap_by_the_matrix_route", "verification", "spin_swap.json")))
    r = SQ.run("m003", sw["m003"]["solutions"][:2])
    assert r["n_spin"] == 2 and r["mirror_invariant_any_tau"] == [] and r["checks"]["symmetry_fail"] == 0
    assert abs(float(r["D_s0_at_2"]) / sqrt(3) - 1) < 1e-8
