"""B1635 and B1636 -- the sealed instruments unchanged; the coupling dimensions (two routes) and the seat's mixing distance;
the lowest symmetric coupling golden at i and along the tick's geodesic, not on the controls; the mechanism (the coupling is
the theta constants off-diagonal; the spectrum a function of F = sum |theta_p/eta|^4; golden at F = 8).  Live checks: the
zero-diagonal sum rule on random matrices (bite: a diagonal entry breaks it); the golden matrix's spectrum; F(i) = 8 and
F(omega) != 8 from the series."""
import hashlib, json, math, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
A35 = ROOT / "frontier" / "B1635_couplings_on_the_ruled_branch"
A36 = ROOT / "frontier" / "B1636_the_golden_spectrum_on_the_ticks_geodesic"
PHI = (1 + 5 ** 0.5) / 2


def _sealed(arc, name, sha):
    first = open(arc / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith(f"# sealed at {sha}")
    assert hashlib.sha256(open(arc / "verification" / name, "rb").read()).hexdigest() == first.split()[4]


def test_b1635_sealed_and_graded():
    _sealed(A35, "couplings_on_the_ruled_branch.py", "cf5f8dd08")
    d = json.load(open(A35 / "verification" / "couplings_on_the_ruled_branch.json"))
    k1 = d["K1_TT_dims"]
    assert [k1[str(k)]["algebraic_full"] for k in range(1, 12, 2)] == [1, 2, 4, 5, 7, 8]
    assert all(k1[str(k)]["algebraic_full"] == round(k1[str(k)]["formula_full"]) for k in range(1, 12, 2))
    assert [k1[str(k)]["algebraic_O+"] for k in range(1, 12, 2)] == [1, 1, 2, 2, 3, 3]
    assert min(k1["1"]["control_random_W_law_errors"]) > 1e-2 > 1e-10 > max(k1["1"]["law_check_relative_errors"])
    assert d["K2_TbarT_dims"]["k0_is_identity"]
    assert abs(d["K4"]["(a) O+ k=3 vs D k=5"]["distance"] - 0.670933) < 1e-6 and d["K4"]["(c) D k=5 vs D k=7"]["distance"] < 1e-8
    assert "TT O+ k=1 #0" in d["K5_nondegenerate_at_i"] and not d["K5_nondegenerate_at_omega"] == []
    assert all(not n.startswith("TT") for n in d["K5_nondegenerate_at_omega"])
    assert d["K6_count"]["two sectors at the lowest symmetric weights (k = 1, 3)"] == 4
    assert json.load(open(A35 / "arc_verdict.json"))["verdict"] == "NEGATIVE"


def test_b1636_sealed_and_the_mechanism():
    _sealed(A36, "golden_on_the_ticks_geodesic.py", "6d3c2ee30")
    d = json.load(open(A36 / "verification" / "golden_on_the_ticks_geodesic.json"))
    assert d["G1"]["max_deviation_from_golden"] < 1e-10 and d["G2_sum_rule_worst_relative"] < 1e-12
    assert all(v["spread"] > 1e-3 for k, v in d["G4_controls_spread_of_O+k1"].items() if not k.startswith("tick"))
    assert d["G4_controls_spread_of_O+k1"]["tick LR (reference)"]["spread"] < 1e-10
    assert all(v["spread"] > 1e-3 for v in d["G5_other_couplings_on_the_tick"].values())
    p = json.load(open(A36 / "verification" / "post_seal_golden.json"))
    assert p["M1"]["max_relative_spread_over_points"] < 1e-10 and p["M1"]["diagonal_max"] == 0.0
    lo, hi = p["M2"]["F_on_the_tick_min_max"]
    assert abs(lo - 8) < 1e-10 and abs(hi - 8) < 1e-10 and p["M2"]["spectrum_vs_cubic_max_deviation"] < 1e-10
    assert p["M3"]["fraction_within_1e-9_of_disc5"] > 0.9 and p["M3"]["control_disc8_fraction_within_1e-9"] == 0.0
    assert json.load(open(A36 / "arc_verdict.json"))["verdict"] == "PROVED"


def test_the_sum_rule_and_its_bite():
    rng = np.random.default_rng(5)
    for _ in range(50):
        a, b, c = rng.normal(size=3) + 1j * rng.normal(size=3)
        Y = np.array([[0, a, b], [a, 0, c], [b, c, 0]])
        s = np.linalg.svd(Y, compute_uv=False)
        assert abs(s[0] - s[1] - s[2]) < 1e-12 * s[0]
    Y[0, 0] = 1.3                                                       # a diagonal entry breaks it
    s = np.linalg.svd(Y, compute_uv=False)
    assert abs(s[0] - s[1] - s[2]) > 1e-6


def test_the_golden_matrix_and_F_from_the_series():
    r = 1 / math.sqrt(2)
    s = np.linalg.svd(np.array([[0, r, 1], [r, 0, r], [1, r, 0]]), compute_uv=False)
    assert np.allclose(s / s[0], [1, 1 / PHI, 1 / PHI ** 2], atol=1e-14)
    import mpmath as mp
    mp.mp.dps = 25
    def F(t):
        e = lambda x: mp.exp(1j * mp.pi * t * x)
        th = (mp.fsum(e((n + mp.mpf(1) / 2) ** 2) for n in range(-30, 30)), mp.fsum(e(n * n) for n in range(-30, 31)),
              mp.fsum((-1) ** abs(n) * e(n * n) for n in range(-30, 31)))
        eta = mp.exp(1j * mp.pi * t / 12) * mp.fprod(1 - mp.exp(2j * mp.pi * t * n) for n in range(1, 120))
        return float(sum(abs(x) ** 4 for x in th) / abs(eta) ** 4)
    assert abs(F(mp.mpc(0, 1)) - 8) < 1e-15
    assert abs(F(mp.mpc(0.5, 5 ** 0.5 / 2)) - 8) < 1e-15                # the top of the tick's geodesic
    assert abs(F(mp.mpc(-0.5, 3 ** 0.5 / 2)) - 8) > 0.4                 # omega: 3 * 4^(2/3)
