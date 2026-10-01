"""B1446 lock -- the parabolic points and the branch points on the root's three-fold cover.

Live: the complete-cusp point of one curve and the generation sector's torsion -sqrt5 +- sqrt(-3) there; the
bidoublet's class index (zero) at a doubly-parabolic point, with the index instrument shown able to return a
non-zero count of boundary classes; the sextic's roots as zeros of the doubly matched sector's torsion, and a
non-root where it does not vanish.  Recorded: all twelve curves, all 96 couplings, the exact derivation.
"""
import glob
import json
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1446_the_parabolic_points_and_the_branch_points"
V = ARC / "verification"
for d in ("B1444_the_backgrounds_are_ends_of_periodic_curves", "B1445_the_mass_term_on_the_product_of_two_curves"):
    sys.path.insert(0, str(ROOT / "frontier" / d / "verification"))
sys.path.insert(0, str(V))


@pytest.fixture(autouse=True)
def sixty_digits():
    import mpmath
    old = mpmath.mp.dps; mpmath.mp.dps = 60
    yield
    mpmath.mp.dps = old


def test_the_generation_sector_at_the_complete_cusp_live():
    import curve_engine as ce
    import parabolic as pb
    from mpmath import mpf, sqrt, mpc
    B, p, g, T = pb.point((2, 1), "cusp+")
    assert abs(ce.kappa(p) + 2) < mpf("1e-40") and abs(ce.tr(T) - 2) < mpf("1e-30")
    X = p[0]; assert abs(X ** 4 + 3 * X ** 3 + 5 * X ** 2 + 6 * X + 4) < mpf("1e-40")
    tors = {}
    for be in ((3, 2), (3, 3), (0, 1)):
        ax, ay = B.v[0] * pb.z ** be[0], B.v[1] * pb.z ** be[1]; tors[be] = ce.sector_torsion(B.Phi, g, T, ax, ay)[0]
    r5, r3 = sqrt(mpf(5)), sqrt(mpc(-3))
    for be in ((3, 2), (3, 3)):
        assert min(abs(tors[be] - (-r5 + s * r3)) for s in (1, -1)) < mpf("1e-40"), tors[be]
    assert min(abs(tors[(0, 1)] - (r5 + s * r3)) for s in (1, -1)) < mpf("1e-40")


def test_the_index_at_a_doubly_parabolic_point_is_zero_live():
    import mass_term as mt
    import index_num as ix
    import parabolic as pb
    from mpmath import mpf
    L = pb.L; nb, cases, skipped, reach = L.frame_cases()
    l, eta, A1 = next(k for k, u in cases.items() if u[0][0] == "up")
    Bl, pl, gl, Tl = pb.point(l, "cusp+"); Be, pe, ge, Te = pb.point(eta, "cusp-")
    ax = pb.z ** A1[0] / (Bl.v[0] * Be.v[0]); ay = pb.z ** A1[1] / (Bl.v[1] * Be.v[1])
    h = {1: ax * mt.kron(gl[1], ge[1]), 2: ay * mt.kron(gl[2], ge[2])}; T = mt.kron(Tl, Te)
    I, a, b = ix.index(L.Phi, h, T)
    assert I == 0 and a["t0"] == 1 and a["h1"] == 1 and a["interior"] == 0 and b["t0"] == 1 and b["h1"] == 1 and b["interior"] == 0
    assert a["gaps"][1][0] > mpf("1e-3") and a["gaps"][1][1] < mpf("1e-40")
    assert abs(mt.torsion_n(L.Phi, h, T)) < mpf("1e-40")
    # the instrument is not blind: off the parabolic points the same module has no boundary invariants and no cohomology
    Bl, pl, gl, Tl = pb.point(l, "end")
    ax = pb.z ** A1[0] / (Bl.v[0] * Be.v[0]); ay = pb.z ** A1[1] / (Bl.v[1] * Be.v[1])
    h = {1: ax * mt.kron(gl[1], ge[1]), 2: ay * mt.kron(gl[2], ge[2])}; T = mt.kron(Tl, Te)
    I, a, b = ix.index(L.Phi, h, T)
    assert a["t0"] == 0 and a["h1"] == 0
    assert abs(abs(mt.torsion_n(L.Phi, h, T)) - 8) < mpf("1e-10")


def test_the_branch_points_live():
    import curve_engine as ce
    from mpmath import mpf, mpc, sqrt, polyroots, exp, pi
    Phi = ce.monodromy(1, "LR", 3); sig = (1, -1, -1); z8 = exp(2j * pi / 8)
    def taus(u):
        Z = sqrt(1 + 1 / u ** 2); p = (u - 1, -Z, Z); q = ce.tracemap(Phi, p)
        assert all(abs(q[i] - sig[i] * p[i]) < mpf("1e-40") for i in range(3))
        g = ce.rep(p); T = ce.intertwiner(Phi, g, sig)
        return [abs(ce.sector_torsion(Phi, g, ts * T, z8 ** 4, z8 ** j)[0]) for j in (3, 5) for ts in (1, -1)], [abs(ce.sector_torsion(Phi, g, ts * T, z8 ** 4, z8 ** j)[0]) for j in (1, 7) for ts in (1, -1)]
    roots = polyroots([1, 0, -8, 12, 0, 0, 4], maxsteps=300, extraprec=300)
    assert sum(1 for r in roots if abs(r.imag) < mpf("1e-40")) == 2
    for u in roots:
        a, b = taus(u); assert min(a + b) < mpf("1e-30"), u
    real = min((r for r in roots if abs(r.imag) < mpf("1e-40")), key=lambda r: abs(r)); w = real - 1 / real
    assert abs(real.real + mpf("0.62070466408")) < mpf("1e-10") and abs(w.real - mpf("0.99036748966")) < mpf("1e-10")
    # the bite: at a point of the curve that is not a root, no sign and no sector of the family vanishes
    a, b = taus(mpf("-0.7")); assert min(a + b) > mpf("1e-3")


def test_the_records():
    s = json.load(open(V / "parabolic_sectors.json"))
    assert s["curves"] == 12 and len(s["points"]) == 24 and sum(t["count"] for t in s["table"]) == 24 * 14
    gen = [t for t in s["table"] if t["kind"].startswith("1 matches, order 2, coefficient 0.5")]
    assert sum(t["count"] for t in gen) == 96 and all(t["exact"].startswith("0 + -1*sqrt(5) + ") and t["exact"].endswith("*sqrt(-3) + 0*sqrt(-15)") for t in gen)
    assert all(p["tr_meridian"].startswith("(2.0 ") for p in s["points"])
    n = dbl = up = dn = 0
    for f in sorted(glob.glob(str(V / "parabolic_bidoublet_*.json"))):
        for r in json.load(open(f))["records"]:
            n += 1
            for p in r["points"]:
                assert p["index"] == 0 and float(p["smallest_kept"]) > 1e-3 and float(p["largest_dropped"]) < 1e-40
                both = "cusp" in p["extension"] and "cusp" in p["higgs"]
                if both:
                    dbl += 1; t0 = 1 if r["eta_order"] == 4 else 2
                    assert p["V"] == dict(h0=0, t0=t0, h1=t0, interior=0) and p["Vdual"] == p["V"] and p["exact"] == "0"
                elif p["extension"] == "end":
                    want = 8 if r["eta_order"] == 4 else 16
                    assert abs(float(p["abs"]) - want) < 1e-9
                    up += r["eta_order"] == 4; dn += r["eta_order"] == 2
                else: assert abs(float(p["abs"]) - 8) < 1e-9
    assert n == 96 and dbl == 288 and up == 96 and dn == 48
    b = json.load(open(V / "branch_points.json"))
    assert b["exact"]["factorisation"] == "16*(u - 1)**4*(u + 1)**2*(u**6 - 8*u**4 + 12*u**3 + 4)"
    assert b["numeric"]["product_trivial"] and b["numeric"]["slopes_equal"]
    assert b["numeric"]["doubly_matched_beta"] == [[1, 0], [1, 3]] and b["numeric"]["orbit_of_the_character"] == [[2, 1], [1, 3], [1, 0]]
    assert all(len(p["zero_sectors"]) == 2 for p in b["numeric"]["points"])
