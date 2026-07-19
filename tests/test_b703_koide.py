"""B703 lock — the corrected Koide sigma-distance (chat1 Q3)."""
import importlib.util, os, mpmath as mp
_c = os.path.join(os.path.dirname(__file__), "..", "frontier", "B703_koide_sigma_distance", "koide_q3.py")
_s = importlib.util.spec_from_file_location("koide_q3", _c); k = importlib.util.module_from_spec(_s); _s.loader.exec_module(k)

def test_koide_theta0_is_sub_sigma_from_2_9():
    mp.mp.dps = 30
    th = k.theta0(k.ME, k.MMU, k.MTAU); sig = k.sigma_theta()
    d = abs(th - mp.mpf(2)/9) / sig
    assert d < 1.5, f"theta_0 sigma-distance {d} (expected sub-sigma ~0.89)"
    assert d > 0.5, "and it is NOT exact/zero (a coincidence, not an identity)"
    # chat1's ~7 sigma is refuted
    assert d < 7, "chat1's ~7 sigma estimate is corrected (it is sub-sigma)"

def test_koide_Q_is_two_thirds_tautology():
    # Q ~ 2/3 (the parametrization tautology, B686) -- close but the CONTENT is the fit
    Q = k.koide_Q(k.ME, k.MMU, k.MTAU)
    assert abs(Q - mp.mpf(2)/3) < 1e-4
