"""The fifth pre-seal review's regressions (generator_review_5/MAIN_RULINGS.md), each able to fail:
- B1: global_min on a frame with undefined mixings (node-only argmins) and with targets AT nodes and within chi2 1e-3 of
  them equals a dense lattice's minimum (never above it beyond the tolerance), and the returned point's chi2 equals it;
- ckm_clause against a lattice, with True and False cases;
- the Gauss weights sum to the cell's measure;
- sample_prior's laws (rows by cell measure, x uniform, 1/y uniform within the cell);
- windowed's doubling: a tiny first window gives the same totals as the default;
- the mirror pair: L_six from first principles (each choice's own rows and its partner line's rows) equals K_ten's;
- candidates at the ball's edge; K's convergence flag."""
import pytest
pytestmark = pytest.mark.slow
import math, pathlib, sys
import numpy as np
import pytest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'scripts' / 'stepb')); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import stepb_core as C
import compression as K
import grid as G
import kten
from assemble import Choices
from cells import CellIndex
from census_io import line_key
from synth import PTS
from test_stepb_cells import signed_frame, build
from test_stepb_kten import boxed_target


def holey(seed=2, hole=0.10, slope=10.0):
    cen = signed_frame(slope=slope, seed=seed)
    rng = np.random.default_rng(100 + seed)
    cen.vdef = cen.vdef.copy(); cen.vdef[rng.random(len(cen.cfg)) < hole] = False
    F = C.features(cen); ch = Choices(cen, F, PTS)
    return cen, F, CellIndex(F, cen.J, PTS, ch, np.full(10, 0.10))


def lattice(ci, rows, n=31):
    u = np.linspace(0, 1, n); out = np.empty((len(rows), n * n, 10))
    for a in range(0, len(rows), 300):
        r = rows[a:a + 300]; x0, x1, y0, y1 = ci.cellr[ci.node[r]].T
        xs = (x0[:, None, None] + (x1 - x0)[:, None, None] * u[None, :, None]) + 0 * u[None, None, :]
        ys = (y0[:, None, None] + (y1 - y0)[:, None, None] * u[None, None, :]) + 0 * u[None, :, None]
        out[a:a + 300] = ci.interp_many(np.repeat(r, n * n), xs.reshape(-1), ys.reshape(-1)).reshape(len(r), n * n, 10)
    return out


def lat_min(Lt, tt, sig, comps=tuple(range(10))):
    z = (Lt[..., list(comps)] - tt[list(comps)]) / sig[list(comps)]
    with np.errstate(invalid="ignore"):
        d = np.einsum("nkf,nkf->nk", z, z)
    return float(np.where(np.isfinite(d), d, np.inf).min())


def test_global_min_seeded_holes_and_node_targets():
    cen, F, ci = holey()
    rows = ci.rows; Lt = lattice(ci, rows)
    nodeonly = np.array([i for i in rows if not ci.ok[i] and np.isfinite(F[i]).all()]); okr = np.array([i for i in rows if ci.ok[i]])
    assert len(nodeonly) > 20
    rng = np.random.default_rng(5); n_node_argmin = 0
    for trial in range(30):
        src = int(rng.choice(nodeonly if trial % 2 == 0 else okr))
        base = ci.feat(ci.coords([src]))[0]
        noise = [0.0, 1e-3, 0.5][trial % 3] * ci.sig * rng.normal(size=10) / (1.0 if trial % 3 != 1 else math.sqrt(10))
        t = base + noise + C.c_shift(3.0); tt = t - C.c_shift(3.0)
        g = ci.global_min(t, C.C_OURS); lat = lat_min(Lt, tt, ci.sig)
        assert math.isfinite(g["min_chi2"]) and g["row"] is not None, trial
        assert g["min_chi2"] <= lat * (1 + 1e-3) + 1e-3, (trial, g["min_chi2"], lat)
        at = float(ci._x2(ci.values_at(g["row"], [g["point"]])[0], tt, tuple(range(10))))
        assert abs(at - g["min_chi2"]) <= 1e-9 * max(1.0, at), (trial, at, g["min_chi2"])
        n_node_argmin += not ci.ok[g["row"]]
    assert n_node_argmin >= 5


def test_ckm_clause_against_a_lattice():
    cen = signed_frame(slope=6.0, seed=3); F, ci = build(cen, 0.10)
    rows = ci.rows; Lt = lattice(ci, rows, 25)
    rng = np.random.default_rng(6); trues = falses = 0
    for trial in range(24):
        i = int(rng.choice(np.nonzero(ci.ok)[0])); x0, x1, y0, y1 = ci.cellr[ci.node[i]]
        tt = ci.values_at(i, [(rng.uniform(x0, x1), rng.uniform(y0, y1))])[0]
        tt[6:10] += rng.normal(0, [0.2, 2.0, 6.0][trial % 3], 4) * ci.sig[6:10]
        z6 = (Lt[..., :6] - tt[:6]) / ci.sig[:6]; z4 = (Lt[..., 6:10] - tt[6:10]) / ci.sig[6:10]
        with np.errstate(invalid="ignore"):
            d6 = np.einsum("nkf,nkf->nk", z6, z6); d4 = np.einsum("nkf,nkf->nk", z4, z4)
        d6 = np.where(np.isfinite(d6), d6, np.inf); d4 = np.where(np.isfinite(d4), d4, np.inf)
        bound = d6.min() + kten.CLAUSE_DCHI2
        lat = bool(((d6 <= bound) & (d4 < C.CKM_LEG_THRESHOLD)).any())
        cl = kten.ckm_clause(ci, tt)
        if lat:
            assert cl["clause"], trial                               # the clause is exhaustive on the interpolant
        trues += cl["clause"]; falses += not cl["clause"]
        if not cl["clause"]:                                         # and a False is real: no lattice point meets both
            assert not lat
    assert trues >= 4 and falses >= 4, (trues, falses)


def test_gauss_weights_sum_to_the_cell_measure():
    cen = signed_frame(); F, ci = build(cen)
    for n in (4, 16):
        Wt, LW = ci.gauss_table(n)
        for nd in range(0, len(ci.gs.pts), 37):
            x0, x1, y0, y1 = ci.cellr[nd]
            assert abs(np.exp2(LW[nd]).sum() - (x1 - x0) * (1 / y0 - 1 / y1) / (2 * G.band_area())) < 1e-13
            assert np.allclose(Wt[nd].sum(axis=1), 1.0, atol=1e-12)
            gx, gw = np.polynomial.legendre.leggauss(n)
            xs = (x1 - x0) / 2 * gx + (x1 + x0) / 2; ys = (y1 - y0) / 2 * gx + (y1 + y0) / 2
            k = int(n * n // 3); xi, yi = xs[k // n], ys[k % n]
            assert np.allclose(Wt[nd][k], ci.gs.weights(nd, xi, yi), atol=1e-12)


def test_sample_prior_laws():
    from scipy.stats import chisquare, kstest
    cen = signed_frame(); F, ci = build(cen)
    rows, xs, ys = ci.sample_prior(np.random.default_rng(9), 300000)
    pool = ci.rows[ci.phys[ci.rows]]
    m = np.exp2(ci.log2_cell_measure(pool)); p = m / m.sum()
    # rows grouped by their node's Im band (enough counts per group): observed against the measure's expectation
    bands = np.digitize(np.array([ci.gs.pts[ci.node[r]][1] for r in pool]), [1.25, 1.5, 2.0, 2.5, 3.0, 3.5])
    obs = np.bincount(np.digitize(np.array([ci.gs.pts[ci.node[r]][1] for r in rows]), [1.25, 1.5, 2.0, 2.5, 3.0, 3.5]), minlength=7)
    exp = np.bincount(bands, weights=p, minlength=7) * len(rows)
    assert chisquare(obs, exp).pvalue > 1e-3
    x0, x1, y0, y1 = ci.cellr[ci.node[rows]].T
    assert kstest((xs - x0) / (x1 - x0), "uniform").pvalue > 1e-3
    assert kstest((1 / y0 - 1 / ys) / (1 / y0 - 1 / y1), "uniform").pvalue > 1e-3


def test_windowed_doubling_equals_the_default(monkeypatch):
    cen = signed_frame(slope=6.0, seed=1); F, ci = build(cen, 0.12)
    t = boxed_target(ci, np.random.default_rng(3), 0.3); tt = t - C.c_shift(3.0)
    g = kten.Integrand(ci, tt, six=True)
    r1, I1, rep1 = kten.windowed(ci, tt, g, "six", kten.SIX, K.MISFIT_CONST6)
    monkeypatch.setattr(kten, "D0", 0.5)
    r2, I2, rep2 = kten.windowed(ci, tt, g, "six", kten.SIX, K.MISFIT_CONST6)
    assert rep2["D"] > 0.5 and rep2["drop_bits_rel"] <= -30                      # it doubled until the bound held
    assert abs(kten.lse2(I1) - kten.lse2(I2)) < 1e-6


def test_mirror_pair_first_principles():
    """two lines that are each other's mirror partners: each choice's mixture is its own rows' cells plus its partner
    line's rows' cells; L_six from that, at 32 x 32, equals K_ten's"""
    rng = np.random.default_rng(4)
    l1, l2 = line_key("2/5", "1/10"), line_key("2/5", "9/10")
    from census_io import mirror_partner
    assert mirror_partner(l1) == l2 and mirror_partner(l2) == l1
    cen = signed_frame(slope=4.0, seed=8, n_lines=1)
    # a second line: the same rows' outputs shifted, so the two lines differ
    import copy
    c2 = copy.deepcopy(cen); n = len(cen.cfg); nc = len(cen.lines)
    c2.m = cen.m * np.exp(0.3); c2.v = cen.v * 0.9
    cen = C.Census(cfg=np.concatenate([cen.cfg, c2.cfg + nc]), d=np.concatenate([cen.d, c2.d]), r=np.concatenate([cen.r, c2.r]),
                   k=np.concatenate([cen.k, c2.k]), m=np.concatenate([cen.m, np.minimum(c2.m, 0.9)]), v=np.concatenate([cen.v, c2.v]),
                   J=np.concatenate([cen.J, c2.J]), vdef=np.concatenate([cen.vdef, c2.vdef]),
                   lines=[l1] * nc + [l2] * nc, tau=np.concatenate([cen.tau, c2.tau]))
    F = C.features(cen); ch = Choices(cen, F, PTS); ci = CellIndex(F, cen.J, PTS, ch, np.full(10, 0.12))
    t = boxed_target(ci, rng, 0.2); tt = t - C.c_shift(3.0)
    I = kten.integrals(ci, ci.rows, kten.Integrand(ci, tt, six=True), 32)
    Irow = dict(zip(ci.rows.tolist(), I))
    best = math.inf
    for j, q in enumerate(ch.keys):
        own = [int(x) for x in ch.R[j] if x >= 0]
        qp = (mirror_partner(q[0]),) + tuple(q[1:]); jp = ch.keys.index(qp)
        part = [int(x) for x in ch.R[jp] if x >= 0]
        best = min(best, -kten.lse2([Irow[i] for i in own + part]))
    L_fp = K.A_DISCRETE + best
    r = kten.K_ten(ci, t, C.C_OURS)
    assert r["grade"] == "JUDGED" and abs(r["L_six"] - L_fp) < 0.02, (r["L_six"], L_fp)


def test_candidates_at_the_ball_edge():
    cen = signed_frame(slope=8.0); F, ci = build(cen)
    rng = np.random.default_rng(10); T = C.SUPPORT_THRESHOLD
    rows = rng.choice(ci.rows[(ci.rad["nine"][ci.rows] > 0.5) & np.isfinite(ci.rad["nine"][ci.rows])], 40, replace=False)
    for i in rows:
        u = rng.normal(size=9); u /= np.linalg.norm(u)
        y = F[i, :9].astype(float) / ci.sig[:9] + u * (math.sqrt(T) + float(ci.rad["nine"][i]) - 1e-4)
        t = np.zeros(10); t[:9] = y * ci.sig[:9]; t[9] = F[i, 9]
        assert int(i) in set(ci.candidates("nine", t, T).tolist())


def test_convergence_flag():
    cen = signed_frame(slope=6.0, seed=1); F, ci = build(cen, 0.12)
    r = kten.K_ten(ci, boxed_target(ci, np.random.default_rng(3), 0.1), C.C_OURS)
    assert r["grade"] == "JUDGED" and r["converged"] is True
    assert kten.converged({"rows": 3, "delta32": 0.002}) is True
    assert kten.converged({"rows": 3, "delta32": 0.5}) is False
    assert kten.converged({"rows": 3, "delta32": 0.5, "used32": True, "delta64": 0.001}) is True
    assert kten.converged({"rows": 3}) is False
