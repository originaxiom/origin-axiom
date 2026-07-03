"""Locks for the B377 acceptance duel -- three registered predictions, 3/3 PASS."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B377_existence_law_derivation")
R = json.load(open(os.path.join(HERE, "acceptance_rungs.json")))


def test_all_three_rungs_pass_at_three_primes():
    for N in ("375", "405", "675"):
        assert R[N]["all_primes_pass"] is True
        assert R[N]["verdicts"] == [True, True, True]


def test_registered_predictions():
    assert (R["375"]["prediction_deg"], R["375"]["ord_pred"]) == (108, 500)
    assert (R["405"]["prediction_deg"], R["405"]["ord_pred"]) == (36, 540)
    assert (R["675"]["prediction_deg"], R["675"]["ord_pred"]) == (90, 900)
