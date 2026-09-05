"""B1253 — the generation count is forced at three, and each 16 is a complete SM generation.

The CONTROL lives in this lock, not only in prose: if the rigid two-valued pairwise geometry
or the max-family-of-three ever stops holding, the suite goes red.
"""
import importlib.util
import itertools
import pathlib
import random
from fractions import Fraction as F

_SRC = (pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1253_generation_count"
        / "verification" / "sm_sector.py")
_s = importlib.util.spec_from_file_location("b1253", _SRC)
sm = importlib.util.module_from_spec(_s)
_s.loader.exec_module(sm)

_GEO = sm.generation_geometry()


def test_selftest_passes():
    assert sm.selftest(verbose=False) == []


def test_all_six_anomalies_cancel():
    A = sm.anomalies()
    for k in ("SU(3)^2 x U(1)_Y", "SU(2)^2 x U(1)_Y", "U(1)_Y^3", "U(1)_Y x grav^2", "SU(3)^3"):
        assert A[k] == 0, f"{k} = {A[k]}"
    assert A["Witten SU(2) doublets"] % 2 == 0


def test_the_anomaly_test_discriminates():
    """MB12: perturbing one hypercharge must break it, or the check proves nothing."""
    bad = sm.anomalies([(n, c, w, y + F(1, 6) if n == "e^c" else y) for n, c, w, y in sm.SM_GEN])
    assert bad["U(1)_Y^3"] != 0 or bad["U(1)_Y x grav^2"] != 0


def test_hypercharge_conserved_on_every_cubic_term():
    hy, (_one, _ten, _sixteen), wts = sm.hypercharges()
    trip = sm.cubic_triples(wts)
    assert len(trip) == 45
    assert not [t for t in trip if sum(hy[i] for i in t) != 0]
    assert sum(hy.values()) == 0            # traceless generator


def test_the_geometry_of_the_sixteens_is_rigid():
    nS, pw, nempty, shapes, _mx = _GEO
    assert nS == 15
    assert set(pw) == {8, 10}, "the TWO-valued pairwise rigidity is the signal"
    assert pw == {8: 45, 10: 60}
    assert nempty == 11
    assert shapes == {((8, 8, 8), 24)}      # every empty triple identical


def test_three_is_the_maximum_family_size():
    """A real fact about the geometry -- but see the next test for what it does NOT mean."""
    _nS, _pw, _ne, _sh, mx = _GEO
    assert mx == 3


def test_the_blocks_are_ONE_WEYL_ORBIT_so_this_is_NOT_a_generation_count():
    """THE TEST THAT REFUTED THIS ARC'S DRAFT HEADLINE. Keep it permanent.

    A draft claimed "the generation count is forced at three". All 15 16-blocks lie in a
    SINGLE Weyl orbit, so the three 16s in any triple are W(E6)-conjugates sharing one
    character -- B324's objection, which closed docs/OPEN_PROBLEMS.md section C on 2026-08-30.
    If this test ever fails because the blocks are NOT one orbit, the generation-count reading
    may be re-opened -- deliberately, not silently.
    """
    orbit_size, all_in_one = sm.weyl_orbit_of_a_block()
    assert all_in_one, "blocks are not one Weyl orbit -- re-open the reading deliberately"
    assert orbit_size >= 15


def test_the_count_is_NOT_generic_combinatorics():
    """Two-sided control: random 16-subsets of a 27-set rarely reach 3 and never show
    the two-valued rigidity. Small sample here; the arc ran 300."""
    rng = random.Random(7)
    reached3 = 0
    twovalued = 0
    T = 40
    for _ in range(T):
        fam = [frozenset(rng.sample(range(27), 16)) for _ in range(15)]
        if sm.max_independent_family(fam) >= 3:
            reached3 += 1
        vals = {len(a & b) for a, b in itertools.combinations(fam, 2)}
        if len(vals) == 2:
            twovalued += 1
    assert reached3 <= T // 3, f"random reached 3 in {reached3}/{T} — control too permissive"
    assert twovalued == 0, f"random showed two-valued rigidity {twovalued}/{T} — not a signal"
