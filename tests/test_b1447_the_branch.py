"""B1447 lock -- the branch off one member's Higgs curve.

Live: the linearised relators at a generic point of the curve (no new class) and at the real branch point (one class in
each off-diagonal block, the second-order term in the image); the recorded parabolic point re-verified from its
matrices (a representation, irreducible, longitude a regular unipotent, meridian a scalar times one, a triplet
with spectrum 1, e, 1/e); the block representation is reducible (the test can tell).  Recorded: the search.
"""
import glob
import json
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1447_the_branch_off_one_members_higgs_curve"
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


def _real_branch_point():
    from mpmath import polyroots, mpf
    roots = polyroots([1, 0, -8, 12, 0, 0, 4], maxsteps=300, extraprec=300)
    return sorted(r.real for r in roots if abs(r.imag) < mpf(10) ** (-40))[1]


def test_the_obstruction_vanishes_at_the_branch_point_live():
    import branch_obstruction as bo
    from mpmath import mpf
    g = bo.analyse(mpf("-0.7"), (4, 3), quiet=True)
    assert (g["h1"], g["h2"], g["classes_upper"], g["classes_lower"]) == (3, 1, 0, 0) and "both" not in g
    b = bo.analyse(_real_branch_point(), (4, 3), quiet=True)
    assert (b["rank_dG"], b["kernel"], b["coboundaries"], b["h1"], b["h2"], b["classes_upper"], b["classes_lower"]) == (15, 12, 7, 5, 3, 1, 1)
    assert float(b["both"]["norm_of_second_order_term"]) > 5 and float(b["both"]["distance_from_image"]) < 1e-10
    assert float(b["upper alone"]["norm_of_second_order_term"]) < 1e-20


def test_the_parabolic_point_is_what_the_record_says_live():
    import branch_obstruction as bo
    import branch_follow as bf
    import branch_parabolic as bp
    import triplet_spectrum as ts
    from mpmath import mpf, mpc, matrix, zeros, eye, inverse, svd_c, norm
    d = json.load(open(V / "parabolic_point.json"))["matrices"]
    R = {g: matrix([[mpc(mpf(e[0]), mpf(e[1])) for e in row] for row in d[name]]) for g, name in ((1, "x"), (2, "y"), (3, "t"))}
    assert norm(bo.G(R, {g: zeros(3) for g in (1, 2, 3)})) < mpf("1e-50"), "a representation of the level"
    assert bf.burnside(R) == 9, "irreducible"
    lam = R[1] * R[2] * inverse(R[1]) * inverse(R[2])
    rank = lambda m: sum(1 for sv in svd_c(m, compute_uv=False) if abs(sv) > mpf("1e-12"))
    assert abs(lam[0, 0] + lam[1, 1] + lam[2, 2] - 3) < mpf("1e-40") and rank(lam - eye(3)) == 2
    c1, c2, c3 = bp.coeffs(R[3]); t0 = c1 / 3
    assert all(abs(c) < mpf("1e-40") for c in bp.f(R)) and rank(R[3] - t0 * eye(3)) == 2
    E, tau = ts.monodromy_on_H1({1: R[1], 2: R[2]}, R[3] / t0)
    assert min(abs(e - 1) for e in E) < mpf("1e-40") and abs(tau) < mpf("1e-40")
    big = max(E, key=lambda e: abs(e - 1)); assert abs(big + 1 / big - mpf("1.7310540547305267")) < mpf("1e-14")
    # the bite: the block representation at the branch point is reducible and the same test says so
    R0 = bo.block_rep(_real_branch_point(), (4, 3)); assert bf.burnside(R0) == 5


def test_three_distinct_eigenvalues_on_the_branch_live():
    import triplet_spectrum as ts
    from mpmath import mpf, log
    R, R0 = ts.branch_rep(mpf("0.05"))
    E, tau = ts.monodromy_on_H1({1: R[1], 2: R[2]}, R[3]); L = sorted(abs(log(e)) for e in E)
    assert abs(L[0] - mpf("0.0091884")) < mpf("1e-5") and abs(L[1] - mpf("1.4164")) < mpf("1e-3") and abs(L[2] - mpf("1.4250")) < mpf("1e-3")
    E0, tau0 = ts.monodromy_on_H1({1: R0[1], 2: R0[2]}, R0[3]); L0 = sorted(abs(log(e)) for e in E0)
    assert L0[0] < mpf("1e-40") and abs(L0[1] - L0[2]) < mpf("1e-40") and abs(L0[1] - mpf("1.4234")) < mpf("1e-3")


def test_the_search_recorded():
    recs = [r for f in sorted(glob.glob(str(V / "parabolic_search_*.json"))) for r in json.load(open(f))]
    found = [r for r in recs if r["found"]]
    assert len(recs) == 32 and len(found) == 22
    assert len({r["invariants"]["tr_x"][:25] for r in found}) == 1 and found[0]["invariants"]["tr_x"].startswith("(2.809155674623863480597948")
    for r in found:
        i = r["invariants"]
        assert i["algebra_dimension"] == 9 and i["rank_longitude_minus_1"] == 2 and i["rank_meridian_minus_scalar"] == 2
        assert len(r["spectra"]) == 16 and all(float(v["nearest_to_one"]) < 1e-40 for v in r["spectra"].values())
    run = open(V / "family_link_run.txt").read()
    assert "-LLLR level 3: torsion 112, backgrounds 48, orbit sizes {3: 16}" in run
    assert "16 orbits: down | distinct eta 3 | eta product trivial True | l product trivial True | thirds that are sector characters of members 1, 2: 4 of 4 | pool covers 12 of 111 characters" in run


def test_the_index_of_the_triplets_at_the_parabolic_point_live_and_recorded():
    """not self-dual, boundary invariants 1, h^1 = 1, no interior class: index 0"""
    sys.path.insert(0, str(ROOT / "frontier" / "B1446_the_parabolic_points_and_the_branch_points" / "verification"))
    import index_num as ix
    import branch_obstruction as bo
    import branch_parabolic as bp
    from mpmath import mpf, mpc, matrix
    d = json.load(open(V / "parabolic_point.json"))["matrices"]
    R = {g: matrix([[mpc(mpf(e[0]), mpf(e[1])) for e in row] for row in d[name]]) for g, name in ((1, "x"), (2, "y"), (3, "t"))}
    c1, c2, c3 = bp.coeffs(R[3]); Tn = R[3] / (c1 / 3)
    I, a, b = ix.index(bo.Phi, {1: R[1], 2: R[2]}, Tn)
    assert I == 0 and (a["t0"], a["h1"], a["interior"]) == (1, 1, 0) and (b["t0"], b["h1"], b["interior"]) == (1, 1, 0)
    assert a["gaps"][1][0] > mpf("1e-3") and a["gaps"][1][1] < mpf("1e-40")
    rec = json.load(open(V / "triplet_index.json"))
    assert len(rec) == 16 and all(r["index"] == 0 and not r["isomorphic_to_its_dual"] and r["V"] == dict(h0=0, t0=1, h1=1, interior=0) and r["Vdual"] == r["V"] for r in rec)
    allb = json.load(open(V / "all_branch_points.json"))
    assert len(allb) == 12 and all(r["h1"] == 5 and r["h2"] == 3 and r["classes"] == [1, 1] and float(r["distance_from_image"]) < 1e-10 and float(r["second_order_norm"]) > 5 for r in allb)
