"""B1451 lock -- the complete points on other levels.

Live: on the sister's three-fold cover the charged sectors at a background's complete point are 2 +- 2 sqrt 5 and
the down-type coupling is their product, -16; a wrong value fails; on a curve of filling type a matched doublet
vanishes away from the complete point too.  Recorded: the sealed run on sixteen levels and the hashes.
"""
import hashlib
import json
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1451_the_complete_points_on_other_levels"
V = ARC / "verification"
sys.path.insert(0, str(V))


@pytest.fixture(autouse=True)
def sixty_digits():
    import mpmath
    old = mpmath.mp.dps; mpmath.mp.dps = 60
    yield
    mpmath.mp.dps = old


def test_the_sisters_three_fold_cover_live():
    """the Higgs character's point here is a double root of kappa = -2 along its curve, so the sealed instrument has
    it to about 1e-15 and the repair to 1e-33; the lock checks both"""
    import complete_points as cp
    import refine_degenerate as rd
    from mpmath import mp, mpf, sqrt, exp, pi
    L = cp.mt.Level("-LR", 3); P = cp.Points(L)
    pe = P.cusp((6, 2)); assert pe[4]["kind"] == "parabolic"
    t1, t2 = P.sector(pe, (4, 3)), P.sector(pe, (3, 1))
    want = sorted([2 - 2 * sqrt(mpf(5)), 2 + 2 * sqrt(mpf(5))]); got = sorted([t1.real, t2.real])
    assert all(abs(g - w) < mpf("1e-10") for g, w in zip(got, want)) and abs(t1 * t2 + 16) < mpf("1e-10")
    assert abs(t1 * t2 - 16) > 1, "the sign is not a convention of the check"
    assert max(abs(g - w) for g, w in zip(got, want)) > mpf("1e-25"), "and the sealed point is not exact: the double root"
    mp.dps = rd.DPS                                              # the repair's precision; the fixture restores sixty
    B = pe[0]; p, info = rd.polish(B, pe[1]); assert info["degenerate"]
    g = cp.ce.rep(p); T = cp.ce.intertwiner(B.Phi, g, B.sig); z = exp(2j * pi / L.N)
    t = cp.ce.sector_torsion(B.Phi, g, T, B.v[0] * z ** 4, B.v[1] * z ** 3)[0]
    assert min(abs(t - w) for w in want) < mpf("1e-28")


def test_a_zero_is_along_the_whole_curve_of_filling_type_live():
    import complete_points as cp
    from mpmath import mpf, exp, pi
    L = cp.mt.Level("-LLRLR", 1); C = L.curve((6, 10)); B = C.B; z = exp(2j * pi / L.N)
    p, g, T = C.point(mpf("0.3"))
    assert abs(cp.ce.tr(T) - 2) < mpf("1e-40"), "the meridian is trivial along the curve"
    assert abs(cp.ce.sector_torsion(B.Phi, g, T, B.v[0] * z ** 6, B.v[1] * z ** 10)[0]) < mpf("1e-40")
    C2 = L.curve((9, 9)); p, g, T = C2.point(mpf("0.3")); B2 = C2.B
    assert abs(cp.ce.sector_torsion(B2.Phi, g, T, B2.v[0] * z ** 3, B2.v[1] * z ** 11)[0]) > mpf("0.1"), "and on a curve of open type it does not vanish"


def records():
    return [json.load(open(f)) for f in sorted((V / "run").glob("complete_*.json"))]


def test_the_sealed_run_recorded():
    R = records(); assert len(R) == 16
    cc = [c["cusp_cusp"] for d in R for c in d["couplings"]
          if c.get("higgs_point") == "parabolic" and c.get("extension_point") == "parabolic" and "cusp_cusp" in c]
    assert len(cc) == 188 and {c["index"] for c in cc} == {0}
    clean = [c for c in cc if float(c["smallest_kept"]) > 0.1 and float(c["largest_dropped"]) < 1e-50]
    assert len(clean) == 148, "at the other forty the sealed ranks are not resolved: a singular value near 1e-21 is kept"
    assert all(c["h1"] == [0, 0] and float(c["smallest_kept"]) < 1e-15 for c in cc if c not in clean)
    kinds = [p.get("kind", "not reached") for d in R for p in d["points"].values()]
    assert kinds.count("parabolic") == 209 and kinds.count("elliptic") == 3 and len(kinds) == 212
    zeros = [(d["state"], d["k"]) for d in R for c in d["couplings"] if c.get("higgs_point") == "parabolic" and float(c.get("abs_end_cusp", 1)) < 1e-9]
    assert len(zeros) == 6 and set(zeros) == {("-LLRLR", 1)}
    checks = [float(c["rank_four_check"]) for d in R for c in d["couplings"] if "rank_four_check" in c]
    assert len(checks) == 16 and max(checks) < 1e-10
    text = open(V / "run_read.txt").read()
    assert "all zero" in text and "11 of 16" in text and "parabolic point 209, elliptic 3, not reached 0" in text


def test_the_repair_resolves_the_forty():
    recs = [json.load(open(f)) for f in sorted((V / "refine").glob("refined_*.json"))]
    assert len(recs) == 5
    rows = [c for d in recs for c in d["couplings"]]
    assert len(rows) == 60 and all(c["index"] == 0 and c["interior"] == [0, 0] for c in rows)
    assert all(float(c["smallest_kept"]) > 0.1 and float(c["largest_dropped"]) < 1e-30 for c in rows), "every rank has a gap"
    was = [c for c in rows if c["sealed_h1"] == [0, 0]]
    assert len(was) == 40 and all(c["h1"] == [2, 2] for c in was), "the sealed h1 was wrong there, the index was not"
    assert sum(1 for c in was if any(c["degenerate"])) == 12, "twelve at an exact double root; the rest at points the continuation left 1e-20 off"
    assert all(c["h1"] == c["sealed_h1"] for c in rows if c not in was)


def test_the_ten_and_the_five_bar_differ():
    d = next(r for r in records() if (r["state"], r["k"]) == ("+LLR", 3))
    ab = lambda s: abs(complex(s.replace(" ", "")))
    rows = [r for r in d["sectors"] if r["kind"] == "parabolic"]
    assert rows and all(abs(ab(r["torsion"]["Q"]) - ab(r["torsion"]["dc"])) > 0.5 for r in rows)
    assert all(r["alpha"]["Q"] == r["alpha"]["uc"] == r["alpha"]["ec"] for r in rows), "the ten's equality is forced here"


def test_the_sealed_files_are_the_sealed_files():
    for line in open(ARC / "ARTIFACT_HASHES.txt"):
        if line.startswith("#") or not line.strip(): continue
        h, name = line.split(None, 1); name = name.strip()
        assert hashlib.sha256(open(ARC / name, "rb").read()).hexdigest() == h, name
