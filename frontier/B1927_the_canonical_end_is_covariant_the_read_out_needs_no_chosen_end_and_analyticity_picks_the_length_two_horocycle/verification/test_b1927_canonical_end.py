"""The lock of B1927. Each test recomputes, with a planted case that must fail.

1. The canonical end at a stored grid point is recomputed by B1667's instrument (a stored value moved by 1e-6 is caught).
2. The covariance L(-1/tau) = L(tau) + log|tau| is recomputed at one point; planted: without the log|tau| shift it fails.
3. Periodicity on the golden thread at the mark with the canonical end (outputs at tau and gamma tau); planted: at a line
   the thread does not keep, the outputs differ.
4. The two conventions differ: recomputed from the stored per-word rows (paired), median |z| above 5."""
import json, math, pathlib, sys
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import grid as GR                    # B1667's instrument functions
import canon_readout as CR


def test_grid_point_recomputed():
    G = json.loads((HERE / "grid.json").read_text())["grid"]
    p = next(q for q in G if abs(q["tau"][0] - 0.25) < 1e-9 and abs(q["tau"][1] - 1.5) < 1e-9)
    lm, l2 = GR.ends(complex(*p["tau"]), complex(*p["c"]))
    assert abs(lm - p["L_max"]) < 1e-9 and abs(l2 - p["L_2"]) < 1e-9
    assert abs(lm - (p["L_max"] + 1e-6)) > 1e-7


def test_covariance():
    t = complex(0.25, 1.5)
    G = json.loads((HERE / "grid.json").read_text())["grid"]
    p = next(q for q in G if abs(q["tau"][0] - 0.25) < 1e-9 and abs(q["tau"][1] - 1.5) < 1e-9)
    cs, res = GR.CC.newton_walk(t, complex(*p["c"]), -1 / t, step=0.02)
    lm_s, l2_s = GR.ends(-1 / t, cs)
    assert abs(lm_s - (p["L_max"] + math.log(abs(t)))) < 1e-8
    assert abs(lm_s - p["L_max"]) > 1e-3                      # planted: no shift
    # Review 82 (agy-002's R82-04, 2026-11-14): the selected end, L_2, was computed and never asserted
    assert abs(l2_s - (p["L_2"] + math.log(abs(t)))) < 1e-8
    assert abs(l2_s - p["L_2"]) > 1e-3                      # planted: no shift


def test_periodicity_at_the_own_line():
    T = CR.T
    beta, betap, ell, g = T.geodesic("LR")
    z = complex((beta * 1j * math.exp(0.1) + betap) / (1j * math.exp(0.1) + 1))
    T.MARK = (0.4, 0.8)
    o1, o2 = CR.outputs(z), CR.outputs(g(z))
    dev = max(float(np.max(np.abs(np.log(np.array(o1[k]) / np.array(o2[k]))))) for k in o1 if min(o1[k]) > 1e-12 and min(o2[k]) > 1e-12)
    assert dev < 1e-8
    T.MARK = (0.2, 0.6)                                        # planted: a line the golden thread does not keep
    o1, o2 = CR.outputs(z), CR.outputs(g(z))
    dev2 = max(float(np.max(np.abs(np.log(np.array(o1[k]) / np.array(o2[k]))))) for k in o1 if min(o1[k]) > 1e-12 and min(o2[k]) > 1e-12)
    T.MARK = (0.4, 0.8)
    assert dev2 > 1e-3


def test_conventions_differ():
    D = json.loads((HERE / "canon_readout.json").read_text())
    rows = D["16 mark"]["rows"]; w = np.array([r["length"] for r in rows]); zs = []
    for k in rows[0]["A"]:
        if "L_max" not in k:
            continue
        d = np.array([np.array(r["A"][k]) - np.array(r["A"][k.replace("L_max", "L_2")]) for r in rows])
        mean = (w[:, None] * d).sum(0) / w.sum()
        jk = np.array([(np.delete(w, i)[:, None] * np.delete(d, i, 0)).sum(0) / np.delete(w, i).sum() for i in range(len(w))])
        se = np.sqrt((len(w) - 1) * np.mean((jk - mean) ** 2, 0)); zs += list(np.abs(mean) / se)
    assert np.median(zs) > 5


def test_the_corner_rules_out_the_maximal_horoball():
    """Recomputes the arc test at 80 degrees: L_max's ratio near 2 (a corner), L_2's near 4 (smooth). Takes about a minute."""
    import smoothness as SM
    C = 0.5772156649015329 + math.log(math.pi)
    G = json.loads((HERE / "grid.json").read_text())["grid"]
    th = math.radians(80.0)
    pts = {dr: complex((1 + dr) * math.cos(th), (1 + dr) * math.sin(th)) for dr in (0.02, 0.01, 0.0)}
    seed = min((p for p in G if "c" in p), key=lambda p: abs(complex(*p["tau"]) - pts[0.02]))
    tau, c = complex(*seed["tau"]), complex(*seed["c"]); vals = {}
    for dr in (0.02, 0.01, 0.0):
        c, res = SM.CC.newton_walk(tau, c, pts[dr]); tau = pts[dr]
        lm, l2, gap = SM.ends_and_gap(tau, c)
        vals[dr] = (lm + 0.5 * math.log(tau.imag) - C, l2 + 0.5 * math.log(tau.imag) - C)
    rmax = (vals[0.02][0] - vals[0.0][0]) / (vals[0.01][0] - vals[0.0][0])
    r2 = (vals[0.02][1] - vals[0.0][1]) / (vals[0.01][1] - vals[0.0][1])
    assert abs(rmax - 2) < 0.2 and abs(r2 - 4) < 0.3
