"""W3 support pre-test STOP lock — the tau-vs-sigma fact + c_eff=2/5."""
import mpmath as mp


def test_tau_keeps_pairs_invariant():
    # tau: q->1/q sends class a/5 -> (5-a)/5; each pair {2,3},{1,4} stays
    for a, b in [(2, 3), (1, 4)]:
        assert (5 - a) % 5 == b and (5 - b) % 5 == a


def test_ceff_two_fifths():
    mp.mp.dps = 30
    phi = (1 + mp.sqrt(5)) / 2
    X = 1/phi
    L = mp.polylog(2, X) + mp.mpf('0.5')*mp.log(X)*mp.log(1 - X)
    assert abs(L - mp.pi**2/10) < mp.mpf(10)**-20
    assert abs((1 - (6/mp.pi**2)*L) - mp.mpf(2)/5) < mp.mpf(10)**-20
