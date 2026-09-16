"""B1419 lock -- the arithmetic filling census of m004, corrected (closed criterion).

Six of the 78 closed hyperbolic fillings in the |p|,q <= 8 grid are arithmetic: m004(+-5,1) (Meyerhoff, x^4-x-1,
disc -283), m004(+-6,1) (disc -59), m004(+-8,1) (disc -31); the other 72 are not.  B288's 'zero' applied the cusped
criterion (imaginary quadratic invariant trace field) to closed manifolds (E82).  The heavy computation is Sage; this
lock reads its artefacts and re-runs the cheap live checks with SnapPy."""
import json, pathlib, pytest

D = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1419_the_arithmetic_fillings_corrected" / "verification"
ARITH = {(-8, 1), (-6, 1), (-5, 1), (5, 1), (6, 1), (8, 1)}
DEEP = [(1, 7), (1, 8), (3, 7), (3, 8), (5, 7), (5, 8), (7, 8)]
MIRROR_ONLY = [(1, 6), (5, 6), (7, 6)]      # resolved at degree 23 on the positive slope; the mirror inherits the field


def rows():
    return [json.loads(l) for l in (D / "arithmetic_census_closed.jsonl").read_text().splitlines() if l.strip()]


def test_grid_and_count():
    r = rows()
    assert len(r) == 87 and sum(1 for x in r if x["hyperbolic"]) == 78


def test_exactly_six_arithmetic():
    got = {tuple(x["slope"]) for x in rows() if x.get("arithmetic") is True}
    assert got == ARITH


def test_meyerhoff_field():
    for s in ((5, 1), (-5, 1)):
        x = next(r for r in rows() if tuple(r["slope"]) == s)
        assert x["field"] == "x^4 - x - 1" and x["disc"] == -283 and x["signature"] == [2, 1]
        assert x["traces_integral"] and x["ramified_at_real_places"] == [True, True]


def test_every_filling_decided():
    """rows undetermined at the degree-24 pass are decided by the recheck, the deep pass, or the mirror isometry"""
    und = {tuple(x["slope"]) for x in rows() if x["hyperbolic"] and x["arithmetic"] == "undetermined"}
    rec = {tuple(x["slope"]): x for x in json.loads((D / "stragglers_recheck.json").read_text())}
    deep = {tuple(x["slope"]): x for x in json.loads((D / "deep_stragglers.json").read_text())}
    for s in und:
        p, q = s
        if s in rec:
            assert rec[s]["signature"][1] > 1
        elif s in deep:
            assert deep[s]["signature"][1] > 1
        else:                                  # a negative slope: its mirror is decided
            m = (-p, q)
            if m in deep:
                assert deep[m]["signature"][1] > 1
            else:
                mm = next(r for r in rows() if tuple(r["slope"]) == m)
                assert mm["arithmetic"] is False and mm["signature"][1] > 1
            assert m in DEEP or m in MIRROR_ONLY


def test_live_snappy_checks():
    snappy = pytest.importorskip("snappy")
    M = snappy.Manifold("m004(5,1)")
    assert abs(float(M.volume()) - 0.98136882889) < 1e-8 and str(M.homology()) == "Z/5"
    for p, q in DEEP + MIRROR_ONLY:
        assert snappy.Manifold("m004(%d,%d)" % (p, q)).is_isometric_to(snappy.Manifold("m004(%d,%d)" % (-p, q)))
