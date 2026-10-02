"""B1453 lock -- the SM seat's arcs sm:B1367-B1515, harvested.

Live: the seat's join on the projective vacuum with main's own index code (I = -1 at q = 17 + 12 sqrt 2 with the
twist -1, nothing at a control); the trap met on the way (the stable letter is not the meridian: main's code would
read 0, so the wrapper refuses it); and the family is not the class (a non-integral trace on two members, none on a
third).  Recorded: the three own-code runs, the thirteen members, and the table of 47 arcs.
"""
import json
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1453_the_sm_seats_join_arcs_harvested"
V = ARC / "verification"
sys.path.insert(0, str(V))


@pytest.fixture(autouse=True)
def sixty_digits():
    import mpmath
    old = mpmath.mp.dps; mpmath.mp.dps = 60
    yield
    mpmath.mp.dps = old


def test_the_join_carries_the_index_live():
    import join_own as jo
    from mpmath import mpf, mpc, sqrt, matrix
    g = jo.ballas(17 + 12 * sqrt(mpf(2)), mpc(-1)); reps, z, rb = jo.cocycles(g)
    assert (z, rb, len(reps)) == (5, 4, 1)
    c = {"m": matrix([reps[0][i] for i in range(4)]), "n": matrix([reps[0][4 + i] for i in range(4)])}
    h, T = jo.fibred(jo.ext(g, c)); I, a, b = jo.ix.index(jo.PHI, h, T)
    assert I == -1 and (a["h1"], a["interior"], b["h1"], b["interior"]) == (1, 0, 2, 1)
    assert a["gaps"][1][0] > mpf("0.01") and a["gaps"][1][1] < mpf("1e-40"), "every rank has a gap"
    assert len(jo.cocycles(jo.ballas(mpf(3), mpc(-1)))[0]) == 0, "and a generic member of the family has no class to extend by"


def test_the_stable_letter_is_not_the_meridian_live():
    """phi sends the fibre's boundary to its conjugate by u1 u0^-1; with m itself as the meridian main's index reads 0"""
    import join_own as jo
    from mpmath import mpf, mpc, sqrt, matrix, inverse
    g = jo.ballas(17 + 12 * sqrt(mpf(2)), mpc(-1)); reps, _, _ = jo.cocycles(g)
    c = {"m": matrix([reps[0][i] for i in range(4)]), "n": matrix([reps[0][4 + i] for i in range(4)])}
    W = jo.ext(g, c); u0 = W["n"] * inverse(W["m"]); u1 = W["m"] * u0 * inverse(W["m"])
    lam = u0 * u1 * inverse(u0) * inverse(u1); d = W["m"] * lam - lam * W["m"]
    assert max(abs(d[i, j]) for i in range(5) for j in range(5)) > mpf("0.1"), "m does not commute with [u0, u1]"
    I, a, b = jo.ix.index({1: [2], 2: [2, -1, 2, 2]}, {1: u0, 2: u1}, W["m"])
    assert I == 0, "the wrong peripheral pair passes the module check and reads zero"


def test_the_family_is_not_the_class_live():
    snappy = pytest.importorskip("snappy")
    import family_integrality as fi
    assert fi.witness("t11365") is not None and fi.witness("o10_143602") is not None
    assert fi.witness("s958") is None and fi.witness("m004") is None


def test_the_recorded_runs_and_the_thirteen():
    j = open(V / "join_own_run.txt").read(); t = open(V / "tower_own_run.txt").read(); l = open(V / "tower_line_run.txt").read(); h = open(V / "hyperbolic_own_run.txt").read()
    assert j.count("index -1") == 4 and "generic control" in j
    assert t.count("index -1") == 16 and t.count("h1(A) = 0") == 4
    assert l.count("index +1") == 32 and l.count("h1(A/L) = 0") == 2
    assert h.count("interior 1/1") == 4 and h.count("interior 0/0") == 4
    d = json.load(open(V / "family_integrality.json"))
    assert d["members"] == 112 and d["regular"] == 77 and len(d["non_integral"]) == 13
    assert {"t11365", "o10_143602", "v2875", "t06828", "t06829"} <= set(d["non_integral"])


def test_the_table_of_the_harvest():
    d = json.load(open(V / "harvest_table.json")); rows = d["rows"]
    assert len(rows) == 47 and len({r["n"] for r in rows}) == 47
    import collections
    c = collections.Counter(r["disp"] for r in rows)
    assert c == {"REGISTERED": 37, "ALREADY ON MAIN": 4, "VERIFIED": 3, "VERIFIED-DIFFERS": 2, "PARTLY VERIFIED": 1}
    led = open(ROOT / "docs" / "HARVEST_LEDGER.md").read()
    for r in rows: assert ("| sm:B%d |" % r["n"]) in led, r["n"]
    assert len(list((V / "readers").glob("s*.md"))) == 6
