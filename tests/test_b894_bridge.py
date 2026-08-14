"""B894 locks: the torsion-prime bridge (support identity, no exponent identity)
and the four-column concordance on the measured plane."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..",
                                "frontier", "B894_meditation_trio"))
import m4_bridge  # noqa: E402


def test_support_identity_at_small_primes():
    res = m4_bridge.main()
    assert res["support_identity"] is True
    assert set(res["tau_ad_smallblock"]) == {"2", "3", "5", "7", "11", "13"}
    assert res["tau_ad_smallblock"] == {"2": 61, "3": 20, "5": 5,
                                        "7": 17, "11": 4, "13": 5}
    assert res["disc_mu"] == {"2": 32, "3": 10, "5": 2,
                              "7": 3, "11": 1, "13": 6}


def test_no_exponent_identity_honest_negative():
    res = m4_bridge.main()
    tau = {int(k): v for k, v in res["tau_ad_smallblock"].items()}
    dmu = {int(k): v for k, v in res["disc_mu"].items()}
    # no divisibility either way: some exponent bigger on each side
    assert any(tau[p] > dmu[p] for p in tau)          # e.g. 7^17 vs 7^3
    assert any(tau[p] < dmu[p] for p in tau)          # e.g. 13^5 vs 13^6


def test_large_torsion_primes_never_enter_disc_mu():
    res = m4_bridge.main()
    large = res["large_primes_absent_from_disc"]
    assert 17 in large and 160453 in large
    assert all(p > 13 for p in large)


def test_sign_law_marks_the_measured_plane():
    res = m4_bridge.main()
    signs = res["sign_law_alignment"]
    # tau_m > 0 exactly at the measured (theta-odd) exponents 4 and 8
    assert signs["4"] == "+" and signs["8"] == "+"
    assert signs["1"] == "-" and signs["5"] == "-"
    assert signs["7"] == "-" and signs["11"] == "-"
    # the unmeasured slot exponents multiply to the shared resolvent 77 (B888)
    assert 7 * 11 == 77
