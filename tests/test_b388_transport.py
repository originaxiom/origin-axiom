"""Locks for B388 -- the m=2 transport kill + coarsening structure."""
import json
import os
from fractions import Fraction as Fr

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B388_m2_relabel_law")
S45 = json.load(open(os.path.join(HERE, "..", "B372_level45_sweeper",
                                  "sweep45.json")))["singles2"]


def test_kill_no_registered_law():
    R = json.load(open(os.path.join(HERE, "transport_law.json")))
    assert R["C0"] is False and R["C1"] == [] and R["C3"] == []


def test_c1_block_identically_zero():
    for a in range(12):
        assert all(Fr(x) == 0 for x in S45[str(a)][4:8])


def test_bare_two_values_by_mod3():
    for a in range(12):
        bare = tuple(Fr(x) for x in S45[str(a)][:4])
        if a % 3 == 1:
            assert bare == (Fr(1, 24), Fr(-1, 24), 0, 0)
        else:
            assert bare == (Fr(5, 48), Fr(1, 48), 0, 0)


def test_c2_odd_half_period_even_support():
    for a in range(12):
        c2 = tuple(Fr(x) for x in S45[str(a)][8:12])
        if a % 2:
            assert all(x == 0 for x in c2)
    for a in range(6):
        c2a = tuple(Fr(x) for x in S45[str(a)][8:12])
        c2b = tuple(Fr(x) for x in S45[str(a + 6)][8:12])
        assert c2b == tuple(-x for x in c2a)
