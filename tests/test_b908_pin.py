"""B908 locks: the pin's legs as banked."""
import json
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B908_exactness_pin")


def test_leg2_seven_primes():
    with open(os.path.join(ARC, "leg2_results.json")) as f:
        r = json.load(f)
    assert r["leg2_multiprime"]["primes"] == [40123, 40639, 40693, 40897,
                                              40903, 40927, 40939]


def test_leg3_mechanism_banked():
    with open(os.path.join(ARC, "leg3_results.json")) as f:
        r = json.load(f)
    for p in ("40123", "40639"):
        assert r["primes"][p]["I_is_minus1"] is True
        assert r["primes"][p]["v_is_0"] is True
        assert r[f"mechanism_{p}"]["stabilizer_dim"] == 16
        assert r[f"mechanism_{p}"]["control_random"]["dim"] == 4
    assert all(r["verification_all_primes"][p]["support_recomputed_equals_stored"]
               for p in r["verification_all_primes"])


def test_leg3_exact_closure():
    with open(os.path.join(ARC, "leg3_exact_results.json")) as f:
        r = json.load(f)
    assert int(r["I"]) == -1
    assert r["v_is_0"] is True
    assert int(r["P_R"]) == -int(r["P_C"])
    assert r["c_S_equals_minus_disc_mu13"] is True
    assert r["checks"]["four_ops_commute_exactly_over_Q"] is True
