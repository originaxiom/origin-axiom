"""B686 — the Koide firewall: Q=2/3 is a 120-deg parametrization tautology."""
import mpmath as mp


def test_koide_Q_is_tautological():
    mp.mp.dps = 25
    for theta in [mp.mpf('0.2222'), mp.mpf('1.0'), mp.mpf('2.7')]:
        s = [1 + mp.sqrt(2)*mp.cos(theta + 2*mp.pi*k/3) for k in range(3)]
        Q = sum(x*x for x in s)/sum(s)**2
        assert abs(Q - mp.mpf(2)/3) < mp.mpf(10)**-18   # 2/3 for EVERY theta


def test_empirical_koide_is_close_but_not_ours():
    mp.mp.dps = 25
    me, mmu, mtau = mp.mpf('0.51099895'), mp.mpf('105.6583755'), mp.mpf('1776.86')
    Q = (me+mmu+mtau)/(mp.sqrt(me)+mp.sqrt(mmu)+mp.sqrt(mtau))**2
    assert abs(Q - mp.mpf(2)/3) < 1e-4          # the famous coincidence, not derived
