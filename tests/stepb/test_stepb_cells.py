"""The continuous-tau cell index (main's rulings after the interpolant's diagnosis): the Bernstein enclosure contains the
interpolant's values on a fine sample of every tested cell (J signed and ln|J|); the per-row radius bounds the excursion; the
branch-and-bound's cell minimum equals a 201 x 201 brute force within its resolution and never lies above it; S's decision
equals an exhaustive scan of every cell (planted worlds inside cells, steep frame); the J sign change is followed."""
import pytest
pytestmark = pytest.mark.slow
import math, pathlib, sys
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'scripts' / 'stepb')); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import stepb_core as C
from assemble import Choices
from cells import CellIndex, ln_abs_range
from synth import steep_frame, PTS


def signed_frame(slope=8.0, seed=0, n_lines=1):
    """the steep frame with J given a sign that changes along a curve through the band (J = |J| * sin(phase))"""
    cen = steep_frame(slope=slope, seed=seed, n_lines=n_lines)
    x, y = cen.tau[cen.cfg, 0], cen.tau[cen.cfg, 1]
    cen.J = cen.J * np.sin(9.0 * x - 2.0 * y + 1.0 + 0.5 * cen.d)
    return cen


def build(cen, sig=0.10):
    F = C.features(cen); ch = Choices(cen, F, PTS)
    return F, CellIndex(F, cen.J, PTS, ch, np.full(10, sig))


def test_enclosure_contains_the_interpolant():
    cen = signed_frame(); F, ci = build(cen)
    rng = np.random.default_rng(1)
    rows = rng.choice(np.nonzero(ci.ok)[0], 150, replace=False)
    lo, hi = ci.enclosure(rows)
    for a, i in enumerate(rows):
        x0, x1, y0, y1 = ci.cellr[ci.node[i]]
        pts = [(x, y) for x in np.linspace(x0, x1, 31) for y in np.linspace(y0, y1, 31)]
        nd = ci.node[i]; Xs = ci.coords(ci.stencil_rows([i])[0])
        V = np.array([ci.gs.weights(nd, x, y) @ Xs for x, y in pts])
        assert (V >= lo[a] - 1e-9).all() and (V <= hi[a] + 1e-9).all()
        lj = np.log(np.abs(V[:, 9]))
        assert (lj >= ci.jlo[i] - 1e-4).all() and (lj <= ci.jhi[i] + 1e-4).all()


def test_radius_bounds_the_excursion():
    cen = signed_frame(); F, ci = build(cen)
    rng = np.random.default_rng(2)
    for i in rng.choice(np.nonzero(ci.ok)[0], 100, replace=False):
        x0, x1, y0, y1 = ci.cellr[ci.node[i]]
        f = ci.values_at(int(i), [(x, y) for x in np.linspace(x0, x1, 9) for y in np.linspace(y0, y1, 9)])
        d = np.linalg.norm((f[:, :9] - F[i, :9]) / ci.sig[:9], axis=1)
        assert (d <= ci.rad["nine"][i] + 1e-6).all()


def test_ln_abs_range():
    lo, hi = ln_abs_range(np.array([-2.0, 1.0, -3.0]), np.array([1.0, 4.0, -1.0]))
    assert lo[0] == -np.inf and abs(hi[0] - math.log(2)) < 1e-15
    assert abs(lo[1]) < 1e-15 and abs(hi[1] - math.log(4)) < 1e-15
    assert abs(lo[2]) < 1e-15 and abs(hi[2] - math.log(3)) < 1e-15


def test_cell_min_equals_brute_force():
    cen = signed_frame(); F, ci = build(cen)
    rng = np.random.default_rng(3); comps = tuple(range(10))
    for trial in range(25):
        i = int(rng.choice(np.nonzero(ci.ok)[0])); x0, x1, y0, y1 = ci.cellr[ci.node[i]]
        p = (rng.uniform(x0, x1), rng.uniform(y0, y1))
        t = ci.values_at(i, [p])[0] + rng.normal(0, 0.3 * (trial % 3), 10)
        st, v, bp, lb = ci.cell_min(i, t, comps)                     # relative tolerance 1e-4
        g = [(x, y) for x in np.linspace(x0, x1, 201) for y in np.linspace(y0, y1, 201)]
        brute = ci._x2(ci.values_at(i, g), t, comps).min()
        assert st == "min" and v <= brute + 1e-4 * max(1.0, v) + 1e-12, (v, brute)   # the guarantee: within 1e-4 max(1, chi2)
        assert lb <= brute + 1e-12, (lb, brute)                                     # the lower bound is a lower bound
        assert brute - v < 0.02 * max(1.0, brute), (v, brute)                      # the brute grid is coarser than the search


def test_support_equals_exhaustive_scan():
    cen = signed_frame(slope=16.0); F, ci = build(cen)
    rng = np.random.default_rng(4); comps = tuple(range(10)); n_in = n_out = 0
    for trial in range(30):
        i = int(rng.choice(np.nonzero(ci.ok)[0])); x0, x1, y0, y1 = ci.cellr[ci.node[i]]
        p = (rng.uniform(x0, x1), rng.uniform(y0, y1))
        t = ci.values_at(i, [p])[0] + C.c_shift(3.0) + rng.normal(0, [0.05, 0.5, 2.0][trial % 3], 10)
        fast = ci.support(t, C.C_OURS)
        tt = t - C.c_shift(3.0); exh = False
        for r in ci.rows:
            st, v, _, _ = ci.cell_min(int(r), tt, comps, T=C.SUPPORT_THRESHOLD)
            if st == "below":
                exh = True; break
        assert fast["in_support"] == exh, (trial, fast)
        assert fast["undecided"] == 0
        n_in += exh; n_out += not exh
    assert n_in >= 5 and n_out >= 5, (n_in, n_out)


def test_global_min_equals_scan():
    """the reference: every row whose rigorous lower bound (its stored enclosure, checked by the enclosure tests) lies
    below the claimed minimum, searched cell by cell -- a row the search missed would show a smaller minimum"""
    cen = signed_frame(slope=6.0, n_lines=2); F, ci = build(cen, 0.12)
    rng = np.random.default_rng(5); comps = tuple(range(10))
    for trial in range(6):
        i = int(rng.choice(np.nonzero(ci.ok)[0])); x0, x1, y0, y1 = ci.cellr[ci.node[i]]
        t = ci.values_at(i, [(rng.uniform(x0, x1), rng.uniform(y0, y1))])[0] + C.c_shift(3.0) + rng.normal(0, 1.0, 10)
        g = ci.global_min(t, C.C_OURS)
        tt = t - C.c_shift(3.0)
        lb = ci.chi2_lower(ci.rows, tt, comps)
        cand = ci.rows[lb < g["min_chi2"]]
        assert len(cand) >= 1
        scan = min(ci.cell_min(int(r), tt, comps, tol=1e-3)[1] for r in cand)
        assert scan >= g["min_chi2"] * (1 - 2e-3) - 2e-3, (g, scan)


def test_j_sign_change_is_followed():
    """a planted world on J's zero curve's neighbourhood: |J| small there; the signed interpolant reaches it, ln|J|'s would not"""
    cen = signed_frame(slope=4.0); F, ci = build(cen)
    crossing = [i for i in np.nonzero(ci.ok)[0][:3000] if ci.jlo[i] == -np.inf]
    assert len(crossing) > 20
    rng = np.random.default_rng(6); found = 0
    for i in rng.choice(crossing, 20, replace=False):
        x0, x1, y0, y1 = ci.cellr[ci.node[i]]
        g = [(x, y) for x in np.linspace(x0, x1, 41) for y in np.linspace(y0, y1, 41)]
        f = ci.values_at(int(i), g); k = int(np.argmin(f[:, 9]))       # the smallest |J| in the cell
        t = f[k] + C.c_shift(3.0)
        found += ci.support(t, C.C_OURS)["in_support"]
    assert found == 20


def test_interp_many_equals_values_at_and_prior_sampling():
    cen = signed_frame(); F, ci = build(cen)
    rng = np.random.default_rng(7)
    rows, xs, ys = ci.sample_prior(rng, 400)
    many = ci.interp_many(rows, xs, ys)
    one = np.array([ci.values_at(int(r), [(x, y)])[0] for r, x, y in zip(rows, xs, ys)])
    assert np.allclose(many, one, rtol=1e-12, atol=1e-12)
    x0, x1, y0, y1 = ci.cellr[ci.node[rows]].T
    assert ((xs >= x0) & (xs <= x1) & (ys >= y0) & (ys <= y1)).all()
    # the y law: within the band's lowest cells, 1/y uniform -- the sample mean of 1/y matches its expectation per cell
    r2, x2, y2 = ci.sample_prior(np.random.default_rng(8), 200000)
    lo = ci.cellr[ci.node[r2], 2]; hi = ci.cellr[ci.node[r2], 3]
    z = (1 / lo - 1 / y2) / (1 / lo - 1 / hi)                      # uniform on [0, 1] under the law
    assert abs(z.mean() - 0.5) < 0.005 and abs((z ** 2).mean() - 1 / 3) < 0.005


def test_support_batch_equals_support():
    cen = signed_frame(slope=10.0, n_lines=2); F, ci = build(cen)
    rng = np.random.default_rng(9); worlds = []
    for trial in range(60):
        i = int(rng.choice(np.nonzero(ci.ok)[0])); x0, x1, y0, y1 = ci.cellr[ci.node[i]]
        t = ci.values_at(i, [(rng.uniform(x0, x1), rng.uniform(y0, y1))])[0] + C.c_shift([1.0, 3.0][trial % 2]) + rng.normal(0, [0.05, 0.5, 1.5][trial % 3], 10)
        worlds.append(t)
    worlds = np.array(worlds)
    b = ci.support_batch(worlds, C.C_SCAN)["in_support"]
    one = np.array([ci.support(t, C.C_SCAN)["in_support"] for t in worlds])
    assert (b == one).all(), np.nonzero(b != one)
    assert 10 <= b.sum() <= 50


def test_stored_enclosures_are_outward():
    cen = signed_frame(); F, ci = build(cen)
    rows = np.nonzero(ci.ok)[0][:500]
    lo, hi = ci.enclosure(rows)
    assert (ci.lo[rows].astype(float) <= lo).all() and (ci.hi[rows].astype(float) >= hi).all()


def test_cell_find2_equals_brute_force():
    cen = signed_frame(slope=6.0); F, ci = build(cen)
    rng = np.random.default_rng(10); A = tuple(range(6)); B = (6, 7, 8, 9); agree = 0
    for trial in range(40):
        i = int(rng.choice(np.nonzero(ci.ok)[0])); x0, x1, y0, y1 = ci.cellr[ci.node[i]]
        t = ci.values_at(i, [(rng.uniform(x0, x1), rng.uniform(y0, y1))])[0] + rng.normal(0, [0.1, 0.6][trial % 2], 10)
        g = [(x, y) for x in np.linspace(x0, x1, 161) for y in np.linspace(y0, y1, 161)]
        f = ci.values_at(i, g); a = ci._x2(f, t, A); b = ci._x2(f, t, B)
        bound = float(a.min()) + 13.86
        st, bb, _ = ci.cell_find2(i, t, A, bound, B, 13.28)
        brute = bool(((a <= bound) & (b < 13.28)).any())
        if brute:
            assert st == "found", (trial, st, bb)
        agree += (st == "found") == brute
    assert agree >= 36


def test_structural_zeros_and_physical_choices():
    """a direction whose J is roundoff everywhere (a real CKM) is a structural zero: its choices are not physical, so the
    null's CKM marginal never draws them; the unconditional measure does"""
    cen = signed_frame()
    cen.J = np.where(cen.d == 1, 1e-30, cen.J)
    F, ci = build(cen)
    assert {int(cen.d[r]) for r in ci.rows[ci.phys[ci.rows]]} == {0}
    assert ci.zero4[:, 3].sum() >= 1 and not ci.zero4[:, :3].any()
    rows, _, _ = ci.sample_prior(np.random.default_rng(0), 3000)
    assert {int(cen.d[r]) for r in rows} == {0}
    rows2, _, _ = ci.sample_prior(np.random.default_rng(0), 3000, physical=False)
    assert {int(cen.d[r]) for r in rows2} == {0, 1}
