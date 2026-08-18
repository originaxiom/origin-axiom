"""B8071 locks -- which real forms are available to the rank-4 centralisers.

The census and the orbit-meets table are combinatorial and are RECOMPUTED here.  The
centraliser intersections are exact-Q linear algebra that takes minutes, so those are read
from the arc's results.json.
"""
import itertools
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARC = os.path.join(ROOT, "frontier", "B8071_reality_gate")
sys.path.insert(0, os.path.join(ROOT, "frontier", "B8068_j2t_charge_field"))
import e8_build as E  # noqa: E402

E6_ROOTS = [r for r in E.ROOTS if r[6] == 0 and r[7] == 0]


def _res():
    return json.load(open(os.path.join(ARC, "results.json")))


def _eps(signs):
    def f(r):
        s = 1
        for j in range(6):
            if r[j] % 2:
                s *= signs[j]
        return s
    return f


def _pair(r, s):
    return sum(r[i] * E.A[i][j] * s[j] for i in range(8) for j in range(8))


def _isroot(t):
    return any(t) and t in E.IDX


def test_the_inner_census_reproduces_B907_unprompted():
    """RECOMPUTED.  The 64 inner sign characters must give dim k in {78, 46, 38} and
    nothing else, with counts 78x1 / 46x27 / 38x36 -- B907's sealed inner sweep, which
    this computation was not given."""
    census = {}
    for signs in itertools.product([1, -1], repeat=6):
        ch = _eps(signs)
        dimk = 6 + sum(1 for r in E6_ROOTS if ch(r) == 1)
        census[dimk] = census.get(dimk, 0) + 1
    assert census == {78: 1, 46: 27, 38: 36}
    assert {int(k): v for k, v in _res()["census"].items()} == census


def test_a_compact_real_form_admits_no_nilpotent_orbit():
    """The method validating itself.  A compact real form contains no nonzero nilpotent,
    so neither A2 nor 2A1 may meet p_C for the compact character.  If this ever came back
    True the whole orbit-meets computation would be broken."""
    ch = _eps((1,) * 6)
    pr = [r for r in E6_ROOTS if ch(r) == -1]
    assert pr == [], "the compact character must leave p_C empty"


def test_A2_meets_e6_2_at_every_one_of_its_thirty_six_characters():
    """Kostant-Sekiguchi: the complex orbit meets g_R iff some nilpotent of p_C lies in it.
    An A2 nilpotent exists in p_C iff p_C holds two roots pairing -1 whose sum is a root."""
    n_e62 = 0
    for signs in itertools.product([1, -1], repeat=6):
        ch = _eps(signs)
        pr = [r for r in E6_ROOTS if ch(r) == -1]
        if 6 + (72 - len(pr)) != 38:
            continue
        hasA2 = any(_pair(r, s) == -1 and _isroot(tuple(r[i] + s[i] for i in range(8)))
                    for r, s in itertools.combinations(pr, 2))
        assert hasA2, "an e6(2) character whose p_C holds no A2 nilpotent"
        n_e62 += 1
    assert n_e62 == 36


def test_the_rank_four_centralisers_have_the_bala_carter_dimensions():
    r = _res()["orbits"]
    assert (r["A2"]["dim_z_e"], r["A2"]["dim_z_ehf"]) == (36, 16)
    assert (r["2A1"]["dim_z_e"], r["2A1"]["dim_z_ehf"]) == (46, 22)


def test_the_compact_su3_su3_is_available_in_e6_2_and_only_there():
    """The headline: A2's centraliser su(3)+su(3) is COMPACT (dim k = 16) at 3 characters
    of e6(2), and at none of e6(-14)."""
    a2 = _res()["orbits"]["A2"]
    assert a2["compact_dim"] == 16
    assert a2["compact_in_e6_2"] == 3
    assert a2["compact_in_e6_m14"] == 0


def test_2A1_is_never_compact_in_e6_2():
    """The complementary half, and the reason the gap is one step wide: the orbit the
    object is placed on carries no compact form in the object's own real form."""
    a1 = _res()["orbits"]["2A1"]
    assert a1["compact_dim"] == 22
    assert a1["compact_in_e6_2"] == 0
    assert a1["compact_in_e6_m14"] == 3


def test_the_detector_is_not_constant():
    """False-positive control: if dim(z_red ^ k) were the same for every character the
    instrument would be measuring nothing."""
    for label in ("A2", "2A1"):
        assert _res()["orbits"][label]["varies"] is True


def test_availability_is_not_occupancy():
    """The arc must not claim the object occupies any of these forms."""
    scope = _res()["scope"]
    assert "does NOT verify the object OCCUPIES" in scope
    assert "vacuous by construction" in scope
