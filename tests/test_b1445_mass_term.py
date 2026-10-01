"""B1445 lock -- the mass term on the product of two periodic curves.

Live: the bidoublet's quadratic form on the root's three-fold cover (an up coupling, a down coupling through a
Higgs character of order two, and a free triple with all three coefficients non-zero), its factorised form, and
the same comparison with a wrong sign, which fails; a character of order two has a curve and obeys B1444's law.
Recorded: the sealed run on 24 untouched levels and the hashes of the sealed files.
"""
import hashlib
import json
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1445_the_mass_term_on_the_product_of_two_curves"
V = ARC / "verification"
sys.path.insert(0, str(ROOT / "frontier" / "B1444_the_backgrounds_are_ends_of_periodic_curves" / "verification"))
sys.path.insert(0, str(V))


@pytest.fixture(autouse=True)
def sixty_digits():
    import mpmath
    old = mpmath.mp.dps; mpmath.mp.dps = 60
    yield
    mpmath.mp.dps = old


def test_the_mass_term_on_the_roots_three_fold_cover_live():
    import mass_term as mt
    from mpmath import mpf
    L = mt.Level("+LR", 3); nb, cases, skipped, reach = L.frame_cases()
    assert nb == 48 and len(cases) == 96 and dict(reach) == {("down", "lepton", "neutrino", "up"): 48} and not skipped
    up = next(k for k, u in cases.items() if u[0][0] == "up"); down = next(k for k, u in cases.items() if u[0][0] == "down")
    for key, want in ((up, (0, 0, -16)), (down, (0, 1, -4))):
        l, eta, A1 = key; pr = L.predicted(l, eta, A1); got = L.fit(l, eta, A1)
        for x, q, w in zip(got, ("c20", "c02", "c11"), want):
            assert abs(x - pr[q]) < mpf("1e-6") and abs(pr[q] - w) < mpf("1e-20"), (key, q, x, pr[q])
    assert L.order2(down[1]) and not L.order2(up[1])
    # the coupling: Y^2 = 4 for up, 1 for down
    assert abs((L.S[up[0]] - L.S[up[1]]) ** 2 - 4) < mpf("1e-20") and abs((L.S[down[0]] - L.S[down[1]]) ** 2 - 1) < mpf("1e-20")


def test_a_free_triple_and_the_factorised_form_live():
    import mass_term as mt
    from mpmath import mpf
    L = mt.Level("+LR", 3); l, eta, A1 = (2, 1), (1, 0), (0, 3)
    pr = L.predicted(l, eta, A1); got = L.fit(l, eta, A1); a, b = pr["a"], pr["b"]
    assert [round(float(pr[q])) for q in ("c20", "c02", "c11")] == [8, 8, -16]
    assert all(abs(x - pr[q]) < mpf("1e-6") for x, q in zip(got, ("c20", "c02", "c11")))
    # (e1 a2 a3 - e2 b2 b3)(e1 a1 a4 - e2 b1 b4) expands to the same form
    assert abs(a[1] * a[2] * a[0] * a[3] - pr["c20"]) < mpf("1e-25") and abs(b[1] * b[2] * b[0] * b[3] - pr["c02"]) < mpf("1e-25")
    assert abs(-(a[1] * a[2] * b[0] * b[3] + b[1] * b[2] * a[0] * a[3]) - pr["c11"]) < mpf("1e-25")
    # the bite: with the cross term's sign reversed the comparison fails
    assert abs(got[2] + pr["c11"]) > 1


def test_a_character_of_order_two_has_a_curve_live():
    """B1444 first took these for nodes of kappa = 2"""
    import curve_engine as ce
    from mpmath import mpf
    B, sl, rows = ce.analyse(1, "LR", 3, (2, 0))
    assert abs(sl) < mpf("1e-30") and len(rows) == 14
    for r in rows:
        if r["matches"] == 0: assert r["order"] == 1 and abs(r["coeff"] - r["predicted"]) < mpf("1e-9") and abs(abs(r["predicted"]) - 1) < mpf("1e-20")
        else: assert r["order"] is None or r["order"] >= 2
    p, g, T = B.point("0.02")
    assert abs(ce.tr(T) - 2) < mpf("1e-30"), "filling type: the meridian is trivial along the curve"


def test_the_sealed_run_recorded():
    s = json.load(open(ARC / "mass_population_summary.json")); t = s["totals"]
    assert t["levels"] == 24 and t["levels_frame"] == 16 and t["levels_free"] == 8 and t["backgrounds"] == 752
    assert t["cases"] == t["tested"] == t["agree"] == 405 and "not_followed" not in t and not s["failures"]
    assert t["frame_tested"] == t["frame_structure_ok"] == 352 and t["frame_mass_term_nonzero"] == 336
    assert t["skipped: eta = l or 1/l"] == 624 and t["skipped: neutrino sector does not fire"] == 720
    assert t["cases_with_a_slope_outside_(1/60)Z"] == 365
    assert s["reachable_types_per_background"] == {"down,lepton": 48, "up": 272, "down,lepton,up": 432}
    assert all(s["predictions"][k]["holds"] for k in ("Q1", "Q2", "Q3", "Q4")) and len(s["files"]) == 24
    c = json.load(open(ARC / "mass_control_summary.json"))
    assert c["totals"]["agree"] == c["totals"]["tested"] == 24


def test_the_sealed_files_are_the_sealed_files():
    for line in open(ARC / "ARTIFACT_HASHES.txt"):
        if line.startswith("#") or not line.strip(): continue
        h, name = line.split(None, 1); name = name.strip()
        assert hashlib.sha256(open(ARC / name, "rb").read()).hexdigest() == h, name
