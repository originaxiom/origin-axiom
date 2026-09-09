"""B1227 -- one theorem, two regimes. The lock asserts the FACTS, not the sentences."""
import json, pathlib, pytest
ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1227_one_theorem_two_regimes"

def _cs(M):
    v = float(M.chern_simons()) % 0.5
    return 0.0 if min(v, 0.5 - v) < 1e-9 else round(v, 9)

def test_regime_torsion_is_two_torsion_and_not_vacuous():
    """A = R/(1/2)Z: amphichiral forces {0,1/4}. Non-vacuous only if some sibling is OFF zero --
    otherwise 'CS is 2-torsion' would be indistinguishable from 'CS is zero' (MB12)."""
    snappy = pytest.importorskip("snappy")
    vals = {n: _cs(snappy.Manifold(n)) for n in ['m004','m003','m136','m135','m206','m207']}
    for n in vals:
        assert snappy.Manifold(n).symmetry_group().is_amphicheiral(), n
        assert vals[n] in (0.0, 0.25), (n, vals[n])
    assert 0.25 in vals.values(), "vacuous: nothing sits off zero"
    assert 0.0 in vals.values(), "vacuous: nothing sits at zero"

def test_the_weakened_hypothesis_is_recorded():
    r = json.load(open(ARC / "results.json"))
    assert "OBJECT-CANONICAL" in r["b1225_hypothesis_before"]
    assert "REAL" in r["b1225_hypothesis_after"]
    assert r["regime_torsion"]["arc"] == "B1224"

def test_novelty_is_claimed_as_consolidation_not_discovery():
    """If this arc ever gets upgraded to a discovery claim, that is a regression."""
    r = json.load(open(ARC / "results.json"))
    assert "CONSOLIDATION" in r["novelty"]
    assert r["still_owed"]
