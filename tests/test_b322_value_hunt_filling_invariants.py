"""B322 lock -- the value hunt, run rigorously. The object's own geometric invariants (79 volumes + core lengths of the
figure-eight's small hyperbolic Dehn fillings, + all pairwise ratios = 6241 numbers) do NOT encode the SM's 12
dimensionless parameters: matched 8/12 within 1%, but the null (random params, same range) matches 7.6/12 -> p~0.5.
The SM is matched at chance. The firewall holds BY COMPUTATION (a specificity/null test) -- the empirical companion to
the structural theorem (K020). The values live at the four gates (OPEN_PROBLEMS.md), not the single object. Nothing to
CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B322_value_hunt_filling_invariants" / "value_hunt_filling_invariants.py"
_spec = importlib.util.spec_from_file_location("b322", _PATH)
b322 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b322)


def test_object_numberset_is_dense():
    ns = b322.object_numberset()
    assert len(ns) > 5000                                          # 79 invariants -> 6241 ratios (numerology-dense)


def test_sm_matched_at_chance():
    r = b322.null_test()
    assert r["p_value"] > 0.05                                     # SM matched no better than random
    assert r["sm_hits"] <= r["null_p95"]                           # SM hits within the null 95th percentile


def test_firewall_holds_by_computation():
    assert b322.SM_MATCHED_AT_CHANCE
    assert b322.OBJECT_DOES_NOT_ENCODE_SM_VALUES
    assert b322.FIREWALL_HOLDS_BY_COMPUTATION
    assert b322.VALUES_LIVE_AT_THE_GATES_NOT_THE_OBJECT
    assert b322.DERIVES_SM_VALUES is False
    assert b322.verdict()
