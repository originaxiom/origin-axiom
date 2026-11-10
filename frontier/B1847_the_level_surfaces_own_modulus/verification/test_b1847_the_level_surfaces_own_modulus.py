"""B1847 -- the level surface's own modulus (P-727; data-free). The conformal modulus of a harmonic level surface from its
3D shape and its fibre group alone: a Fuchsian control of known tau (live, coarse; Richardson to < 2e-4 from the committed
runs; a 3D-inverted curved copy agrees), then m004's loop, whose symmetric levels are forced (Re tau = 1/2 at s = 0, 1/2;
tau = i at s = 1/4, 3/4) and which closes (s = 1 on s = 0)."""
import math, pathlib, re, sys
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def _runs(name):
    out = {}
    for line in (HERE / name).read_text(encoding="utf-8").splitlines():
        m = re.search(r"(?:\[s=([0-9.]+)\])?.*res \((\d+),(\d+)\): tau ([+-][0-9.]+)([+-][0-9.]+)i\s+reduced ([+-][0-9.]+)([+-][0-9.]+)i\s+detE-1 ([+-][0-9.e+-]+)\s+bad cycles (\d+)", line)
        if m:
            s = float(m.group(1)) if m.group(1) else None
            out[(s, int(m.group(2)))] = dict(tau=complex(float(m.group(4)), float(m.group(5))),
                                              red=complex(float(m.group(6)), float(m.group(7))),
                                              detE1=float(m.group(8)), bad=int(m.group(9)))
    return out


def test_the_fuchsian_control_live_coarse():
    import stage_a_control as A
    tau0 = complex(0.23, 1.41)
    x, y, z, im = A.traces_cached(tau0)
    Am, Bm = A.jorgensen(x, y, z)
    K = Am @ Bm @ np.linalg.inv(Am) @ np.linalg.inv(Bm); Kt = complex(A.mob(K, 0.0))
    assert abs(Kt - 2) < 1e-9                                        # Jorgensen: [A, B] is z -> z + 2
    faces, allc, floor, T = A.solve_modulus(Am, Bm, Kt, T=6 * abs(Kt), verbose=False)
    tau, info = A.build_and_solve_cols(faces, allc, floor, T, abs(Kt), lambda u, t: np.c_[u, np.zeros_like(u), t], n_arc=60, nlev=40)
    assert info["inconsistent_cycles"] == 0 and abs(tau - tau0) < 0.02 and abs(info["detE"] - 1) < 0.02


def test_the_control_converges_at_second_order_to_the_known_tau():
    rows = [l for l in (HERE / "stage_a_control_run.txt").read_text().splitlines()]
    for tau0 in (complex(0.23, 1.41), complex(-0.31, 1.07)):
        for kind in ("flat", "curved"):
            vals = {}
            for l in rows:
                if l.startswith(f"tau0 {tau0}") and f" {kind} " in l:
                    a = int(re.search(r"arc\s+(\d+)", l).group(1))
                    m = re.search(r"tau ([+-][0-9.]+)([+-][0-9.]+)i", l)
                    vals[a] = complex(float(m.group(1)), float(m.group(2)))
            r = vals[240] + (vals[240] - vals[120]) / 3                  # Richardson, error ~ h^2
            assert abs(r - tau0) < 2e-4, (tau0, kind, r)
            assert abs(vals[120] - tau0) / abs(vals[240] - tau0) > 3   # second order


def test_m004_loop_symmetric_levels_and_closure():
    R = _runs("stage_b_m004_run.txt")
    for k, v in R.items():
        assert v["bad"] == 0
    rich = lambda s: R[(s, 240)]["red"] + (R[(s, 240)]["red"] - R[(s, 120)]["red"]) / 3
    t0, th, tq, t3 = rich(0.0), rich(0.5), rich(0.25), rich(0.75)
    assert abs(abs(t0.real) - 0.5) < 1e-3 and abs(abs(th.real) - 0.5) < 1e-3     # sigma-fixed levels: Re tau = 1/2
    assert abs(tq - 1j) < 1e-3 and abs(t3 - 1j) < 1e-3                          # tau = i (two symmetries)
    assert abs(t0.imag - th.imag) < 1e-4                                         # the half-shift
    assert abs(R[(1.0, 120)]["red"].imag - R[(0.0, 120)]["red"].imag) < 1e-3      # the loop closes
    assert R[(0.0, 240)]["detE1"] < 5e-4
    assert abs(t0.imag - math.sqrt(5) / 2) > 5e-3                                # NOT the Teichmuller apex 1.11803


def _gen(name):
    t = (HERE / name).read_text(encoding="utf-8")
    m = re.search(r"tau ([+-][0-9.]+)([+-][0-9.]+)i\s+reduced ([+-][0-9.]+)([+-][0-9.]+)i\s+detE-1 ([+-][0-9.e+-]+)", t)
    return complex(float(m.group(3)), float(m.group(4))), float(m.group(5))


def _graph(name):
    out = {}
    for l in (HERE / name).read_text(encoding="utf-8").splitlines():
        m = re.search(r"res \((\d+),(\d+)\): tau .*reduced ([+-][0-9.]+)([+-][0-9.]+)i\s+detE-1 ([+-][0-9.e+-]+)", l)
        if m:
            out[int(m.group(1))] = (complex(float(m.group(3)), float(m.group(4))), float(m.group(5)))
    return out


def test_the_general_method_reproduces_m004_and_the_graph_method():
    t120, d120 = _gen("gen_m004_120_run.txt")
    assert abs(t120 - complex(-0.5, 1.12438)) < 6e-4 and abs(d120) < 5e-4
    g = _graph("exc_s0.25_exact_run.txt")
    rich = g[240][0] + (g[240][0] - g[120][0]) / 3
    t25, d25 = _gen("gen_exc_s025_80_run.txt")
    assert abs(t25 - rich) < 3e-4 and abs(d25) < 1e-3                 # two independent meshings agree at s = 1/4


def test_the_excursion_anti_apex_and_the_teichmuller_gap():
    g = _graph("exc_s0.5_exact_run.txt")
    t = g[240][0]
    assert abs(abs(t.real) - 0.5) < 1e-4 and g[240][1] < 5e-4          # the sigma-fixed level: Re tau = 1/2
    im = g[240][0].imag + (g[240][0].imag - g[120][0].imag) / 3
    assert abs(im - 1.5904) < 5e-4
    tr = (HERE / "teichmuller_readings_run.txt").read_text()
    assert "max Im 3.651484" in tr and "1.369306" in tr and "max Im 1.118034" in tr
    assert im / 1.369306 > 1.15                                         # the metric's anti-apex reading is 16 % above Teichmuller's


def test_the_fold_and_the_disclosed_failure():
    f0 = (HERE / "fold_s0.0_recentred_run.txt").read_text(); f25 = (HERE / "fold_s0.25_run.txt").read_text()
    assert "t = 0.45: crossings per period over 24 lines of u: min 1 max 5" in f0
    assert all("max 1 " in l for l in f25.splitlines() if l.strip().startswith("t ="))
    bad = _graph("exc_s0_240_160_run.txt")
    assert bad[240][1] > 0.1                                            # the graph method's tube run failed its own check: not used


def test_the_single_block_at_level_five_is_not_the_leading_exponential():
    import kashaev_block as KB
    import mpmath as mp
    ex = KB.kashaev(5)
    assert abs(ex - (46 + 2 * mp.sqrt(5))) < 1e-20
    lead = mp.e ** (5 * KB.VOL / (2 * mp.pi))
    assert ex / lead > 9                                                     # R2's form drops a factor ~10 at N = 5
    full = lambda N: 3 ** mp.mpf(-0.25) * N ** 1.5 * mp.e ** (N * KB.VOL / (2 * mp.pi))
    assert abs(KB.kashaev(80) / full(80) - 1) < 0.01                         # the asymptotic holds at large N


def _rises(toward):
    """rows ordered by falling s: at least eight of them, Im tau strictly rising from each to the next"""
    return len(toward) >= 8 and all(a[3] < b[3] for a, b in zip(toward, toward[1:]))


def test_the_rise_check_can_fail():
    """MB12 (B1862): the check that replaced a list compared with its own sort refuses a table with one value out of order."""
    good = [(0.02 - 0.002 * k, 120, 0.0, 3.7 + 0.3 * k, 0.0) for k in range(9)]
    assert _rises(good)
    bad = list(good)
    bad[4], bad[5] = (bad[4][0], 120, 0.0, bad[5][3], 0.0), (bad[5][0], 120, 0.0, bad[4][3], 0.0)
    assert not _rises(bad) and not _rises(good[:5])


def test_the_tube_by_the_full_groups_ford_domain():
    rows = []
    for l in (HERE / "gamma_tube_table.txt").read_text().splitlines()[1:]:
        f = l.split()
        rows.append((float(f[0]), int(f[1]), float(f[2]), float(f[3]), float(f[4])))
    get = lambda s, g: [r for r in rows if abs(r[0] - s) < 1e-9 and r[1] == g][0]
    c25 = get(0.25, 80); c50 = get(0.5, 80)
    assert abs(complex(c25[2], c25[3]) - complex(-0.37218, 1.00851)) < 1e-3 and abs(c25[4]) < 1e-3      # the controls
    assert abs(abs(c50[2]) - 0.5) < 3e-3 and abs(c50[3] - 1.5904) < 2e-3
    near = [r for r in rows if 0 < abs(r[0]) <= 0.002 or r[0] == 0.0]
    assert all(6.0 < r[3] < 6.3 for r in near)                                    # the limit cluster: 6.15 +- 0.15
    # Im tau rises toward the tube: strictly, as s falls to 0 on the 120 grid. [Corrected 2026-11-10 (B1862; the advisor
    # seat's audit, L5, reproduced on main): this compared a sorted list with its own sort and could not fail.]
    toward = sorted((r for r in rows if 0 < r[0] <= 0.02 and r[1] == 120), key=lambda r: -r[0])
    assert _rises(toward)
    assert abs(get(0.005, 80)[3] - get(0.005, 120)[3]) < 2e-3                    # two grids agree (1.7e-3)
    g = (HERE / "core_gradient_run.txt").read_text()
    assert "min 4.19" in g                                                        # the tube level is regular
    # far from every record reading: the cluster's own least value against each. [Corrected 2026-11-10 (B1862, L5): this
    # subtracted three literals from the literal 6.0.]
    least = min(r[3] for r in near)
    for x in (3.65, 2.87, 2.58):
        assert least - x > 2.0
