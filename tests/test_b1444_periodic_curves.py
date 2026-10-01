"""B1444 lock -- the backgrounds are the reducible ends of the trace map's periodic curves.

Live: the exact statements about the root's three-fold curve, checked numerically at 60 digits; the torsion law on
two levels (first-order coefficient = product of slope differences); the same check with the wrong slope, which
fails; the filling criterion on one background of each kind.  Recorded: the sealed run on 27 untouched levels, the
sealed files' hashes, the per-sector tables of the frame's backgrounds.
"""
import hashlib
import json
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1444_the_backgrounds_are_ends_of_periodic_curves"
V = ARC / "verification"
sys.path.insert(0, str(V))


@pytest.fixture(autouse=True)
def sixty_digits():
    """the engine works at 60 digits and sets them at import; the suite resets mpmath's precision between tests"""
    import mpmath
    old = mpmath.mp.dps; mpmath.mp.dps = 60
    yield
    mpmath.mp.dps = old


def test_the_roots_three_fold_curve_live():
    """X = u - 1, Y = -Z, Z^2 = 1 + 1/u^2 is a curve of twisted period-3 points; kappa - 2 = w(w - 1) and
    m + 1/m - 2 = -w(w^2 - w + 4), w = u - 1/u; the complete cusp is at w^2 - w + 4 = 0"""
    import curve_engine as ce
    from mpmath import mpf, mpc, sqrt
    Phi = ce.monodromy(1, "LR", 3); tol = mpf(10) ** (-40)
    w0 = (1 + sqrt(mpc(-15))) / 2; u_cusp = (w0 + sqrt(w0)) / 2
    for u in (mpf("1.3"), mpc("0.7", "0.4"), u_cusp):
        Z = sqrt(1 + 1 / u ** 2); p = (u - 1, -Z, Z); w = u - 1 / u
        q = ce.tracemap(Phi, p); sig = (1, -1, -1)
        assert all(abs(q[i] - sig[i] * p[i]) < tol for i in range(3))
        assert abs(ce.kappa(p) - 2 - w * (w - 1)) < tol
        if u is u_cusp:
            assert abs(ce.kappa(p) + 2) < tol and abs(w * w - w + 4) < tol
            continue                                             # the meridian is parabolic there: the intertwiner is not normalisable by its trace sign
        T = ce.intertwiner(Phi, ce.rep(p), sig)
        assert abs(ce.tr(T) ** 2 - 4 + w * (w * w - w + 4)) < mpf(10) ** (-30)


def test_the_torsion_law_live():
    import curve_engine as ce
    from mpmath import mpf
    B, sl, rows = ce.analyse(1, "LR", 2, (1, 2))
    first = [r for r in rows if r["matches"] == 0]; matched = [r for r in rows if r["matches"]]
    assert len(first) == 1 and abs(first[0]["coeff"] - mpf(4) / 5) < mpf("1e-9") and abs(first[0]["predicted"] - mpf(4) / 5) < mpf("1e-20")
    assert len(matched) == 2 and all(r["order"] == 2 and abs(r["coeff"] + mpf(1) / 125) < mpf("1e-9") for r in matched)
    B, sl, rows = ce.analyse(1, "LR", 3, (2, 1))
    assert abs(sl - 1) < mpf("1e-30") and len(rows) == 14
    for r in rows:
        if r["matches"] == 0: assert r["order"] == 1 and abs(r["coeff"] - r["predicted"]) < mpf("1e-9")
        else: assert r["order"] >= 2
    seen = sorted(set((r["matches"], r["order"], round(float(r["coeff"].real), 6)) for r in rows))
    assert seen == [(0, 1, 2.0), (0, 1, 4.0), (1, 2, 0.5), (1, 2, 0.75), (2, 3, 0.5625)], seen
    # the bite: the same comparison with the slope of l negated fails
    S = B.slopes(); N = B.N; add = lambda a, b: ((a[0] + b[0]) % N, (a[1] + b[1]) % N)
    wrong = [r for r in rows if r["matches"] == 0 and abs(r["coeff"] - (S[r["alpha"]] + sl) * (S[r["beta"]] + sl)) > mpf("1e-6")]
    assert wrong, "the check cannot fail"


def test_the_two_kinds_of_background_live():
    """+LLR level 2, l = (1, 2): the meridian is +-(longitude)^+-1 along the curve and the matched sectors' torsion is
    identically zero; on the root's three-fold cover neither"""
    import curve_engine as ce
    from mpmath import mpf, inverse
    def kind(eps, word, k, ell):
        B, sl, rows = ce.analyse(eps, word, k, ell)
        p, g, T = B.point("0.02"); lam = g[1] * g[2] * inverse(g[1]) * inverse(g[2])
        d = min(max(abs((T - sg * Q)[i, j]) for i in range(2) for j in range(2)) for sg in (1, -1) for Q in (lam, inverse(lam)))
        return any(r["order"] is None for r in rows), d < mpf("1e-25"), sl
    z, f, sl = kind(1, "LLR", 2, (1, 2)); assert z and f and abs(abs(sl) - 1) < mpf("1e-30")
    z, f, sl = kind(1, "LR", 3, (2, 1)); assert not z and not f and abs(abs(sl) - 1) < mpf("1e-30")


def test_the_sealed_run_recorded():
    s = json.load(open(ARC / "law_population_summary.json")); t = s["totals"]
    assert t["levels"] == 27 and t["backgrounds"] == 146 and t["sectors"] == 1734
    assert t["unmatched"] == t["unmatched_first_order_ok"] == 1223
    assert t["matched"] == 511 and t["matched_identically_zero"] == 131 and t["matched_order_ge_2"] == 380
    assert t["slope_limit_ok"] == t["slope_limit_tested"] == 146
    assert t["zero_type"] == t["filling_type"] == 27 and t["zero_iff_filling_ok"] == t["filling_tested"] == 146
    assert "backgrounds_not_followed" not in t and not s["failures"]
    assert all(s["predictions"][k]["holds"] for k in ("P1", "P2", "P3", "P4", "P5"))
    assert len(s["files"]) == 27


def test_the_sealed_files_are_the_sealed_files():
    for line in open(ARC / "ARTIFACT_HASHES.txt"):
        if line.startswith("#") or not line.strip(): continue
        h, name = line.split(None, 1); name = name.strip()
        assert hashlib.sha256(open(ARC / name, "rb").read()).hexdigest() == h, name


def test_the_frames_backgrounds_sector_by_sector_recorded():
    def pats(name):
        d = json.load(open(V / ("frame_sectors_%s.json" % name)))
        return d["backgrounds"], sorted((p["count"], tuple((t[0], t[1], t[2]) for t in p["pattern"])) for p in d["patterns"])
    n, p = pats("+LR_3"); assert n == 48 and p == [(48, tuple((s, 2, "1/2") for s in ("Q", "uc", "ec", "dc", "L", "nuc")))]
    n, p = pats("+LLR_3"); assert n == 48 and len(p) == 2
    for c, pat in p:
        d = dict((t[0], t[1:]) for t in pat)
        assert c == 24 and d["Q"] == d["uc"] == d["ec"] == (2, "1/2") and d["dc"] == d["L"] and d["dc"][1] in ("3/4+1/4*sqrt(5)", "3/4-1/4*sqrt(5)")
    n, p = pats("+LLRLRRLR_1"); assert n == 16 and p == [(16, tuple((s, None, None) for s in ("Q", "uc", "ec", "dc", "L", "nuc")))]
    n, p = pats("+LR_4"); assert n == 256 and sum(c for c, _ in p) == 256 and {pat[0][2] for _, pat in p} == {"69/4+15/2*sqrt(5)", "69/4-15/2*sqrt(5)"}
    n, p = pats("-LR_3"); assert n == 96 and all(pat[0][2] == "3/4" for _, pat in p)


def test_the_exact_records():
    for k, comps in ((1, 1), (2, 3)):
        d = json.load(open(V / ("periodic_curves_LR_%d.json" % k)))
        assert all(len(d[s]) == comps and all(c["dim"] == 1 and c["genus"] == 0 for c in d[s]) for s in d)
    d = json.load(open(V / "periodic_curves_LR_3.json"))
    assert len(d["+++"]) == 7 and all(len(d[s]) == 3 and sorted(c["degree"] for c in d[s]) == [1, 4, 4] for s in d if s != "+++")
    for s in d:
        if s == "+++": continue
        for c in d[s]:
            if c["degree"] == 4: assert c["genus"] == 0 and c["at_kappa_2"]["points"] == 8 and c["at_kappa_m2"]["points"] == 8
    c = json.load(open(V / "cusp_point.json"))
    assert all(r["kappa"] == "-2" and r["m_plus_inv_minus_2"] == "0" and r["u_minpoly"] == "x^4 - x^3 + 2*x^2 + x + 1" and r["E_squared_is_square_in_K"] for r in c)


def test_no_bulk_product_of_an_orbits_higgs_classes_recorded():
    d = json.load(open(V / "no_bulk_cubic.json"))
    assert [(r["state"], r["k"]) for r in d] == [("+LR", 3), ("-LLLR", 3), ("+LR", 5)]
    for r in d:
        assert r["trivial_module"]["h2"] == 0 and all("all zero" in k for k in r["orbits"])
    assert d[0]["orbits"] == {"down: pairwise products all zero": 16, "up: pairwise products all zero": 16}


def test_the_curve_commutes_with_the_standard_model_live():
    """su(2)_beta is the one root pair of E6 commuting with su(3) + su(2)_L + u(1)_Y, and it commutes with all of su(5)"""
    import subprocess
    out = subprocess.run([sys.executable, str(V / "e6_centraliser.py")], capture_output=True, text=True, check=True).stdout
    assert "centraliser of su(3) + su(2)_L + u(1)_Y: 2 " in out
    assert "(the centraliser of su(2)_beta): 30 " in out
    assert "su(5) roots: 20 all orthogonal to beta: True" in out
    assert out == open(V / "e6_centraliser_run.txt").read()
