"""B1234 -- the walls trace to A6. Locks the forcing AND its control: if the control ever comes
back high, the test says nothing and must fail loudly rather than pass quietly."""
import json, pathlib
import pytest
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1234_a6_built_the_walls"


def test_orientation_covers_are_amphichiral_and_the_base_rate_is_low():
    """Both halves, or the finding is vacuous: 100% forcing AND a low base rate."""
    snappy = pytest.importorskip("snappy")
    cov = tot = 0
    for M in snappy.NonorientableCuspedCensus[:12]:
        try:
            tot += 1
            cov += bool(M.orientation_cover().symmetry_group().is_amphicheiral())
        except Exception:
            pass
    assert tot >= 8 and cov == tot, (cov, tot)          # the forcing
    base = bt = 0
    for M in snappy.OrientableCuspedCensus(cusps=1)[:60]:
        try:
            bt += 1
            base += bool(M.symmetry_group().is_amphicheiral())
        except Exception:
            pass
    assert base / bt < 0.15, (base, bt)                 # the control -- or the test is vacuous


def test_m004_is_the_orientation_cover_of_gieseking():
    snappy = pytest.importorskip("snappy")
    G = snappy.Manifold('m000')
    assert not G.is_orientable()
    assert G.orientation_cover().is_isometric_to(snappy.Manifold('m004'))


def test_the_finding_is_not_overclaimed():
    """The arc must keep saying that dropping A6 may BREAK THE TOOLS, not open a door."""
    c = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]
    assert "WHAT THIS DOES NOT ESTABLISH" in c
    assert "BREAK THE TOOLS" in c
    r = json.load(open(ARC / "results.json"))
    assert r["cell1"]["cover_rate"] == 1.0 and r["cell1"]["base_rate"] < 0.15
    assert r["cell3"]["gieseking_surjections_onto_2T"] == r["cell3"]["m004_surjections_onto_2T"]
