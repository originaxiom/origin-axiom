"""B952 locks — the GUT requirements ledger and the rank obstruction.

The load-bearing lock is that measurement CANNOT reduce rank: a centralizer of
semisimple elements contains a maximal torus. If a future arc claims the cascade
reaches the SM, this must fail.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B952_gut_ledger_rank"
LEDGER = ROOT / "docs" / "GUT_REQUIREMENTS_LEDGER.md"


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def _n(p):
    return " ".join(p.read_text(encoding="utf-8").split())


def test_the_rank_arithmetic():
    r = _res()
    assert r["rank_E6"] == 6
    assert r["rank_SMT"]["total"] == 6
    assert r["rank_SM"]["total"] == 4
    assert r["rank_deficit"] == 2
    assert r["dim_SMT"] == 14 and r["dim_SM_gauge"] == 12


def test_the_cascade_preserves_rank_and_therefore_cannot_reach_the_SM():
    r = _res()
    assert r["SMT_preserves_rank_of_E6"] is True
    assert r["SM_rank_is_lower"] is True
    assert r["measurement_can_reduce_rank"] is False
    assert "maximal torus" in r["theorem"]


def test_rank_reduction_needs_a_named_mechanism():
    r = _res()
    for m in ("Higgs VEV", "Wilson line / Hosotani flux", "orbifold projection"):
        assert m in r["rank_reduction_requires"]


def test_the_ledger_carries_the_hard_experimental_bounds():
    t = _n(LEDGER)
    assert "2.4×10³⁴ yr" in t
    assert "Minimal SU(5) is EXCLUDED" in t
    assert "27 = 16 + 10 + 1" in t
    assert "twelve" in t.lower() or "12 states" in t


def test_the_finding_does_not_overreach():
    """It must not be read as refuting the cascade or as excusing the crossings."""
    t = _n(CELL / "FINDINGS.md")
    assert "does **not** refute the measurement cascade" in t
    assert "not a retrofit excuse" in t
    assert "those verdicts stand exactly as banked" in t
    assert "L133" in t and "L134" in t
