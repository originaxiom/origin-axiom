"""B1723 -- the golden valley (P-069, L254), sealed 23f8a7621, NEGATIVE as sealed. Live: the best worst factor and the
mixing's best re-derived from the stored rows and the pinned data; the valley's geometry (F = 8 at its points, the arcs'
heights and length). Stored: the cells and the control. Seal: the hashes."""
import hashlib, json, math, pathlib
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1723_the_golden_valley"
ROOT = A.parents[1]


def _stored():
    return json.loads((A / "verification" / "comparison.json").read_text(encoding="utf-8"))


def test_the_cells_stored():
    c = _stored()
    assert not c["T1_six_within_factor_3"] and not c["T2_specific_p_below_0.01"] and not c["T3_chi2_below_16.75"]
    assert c["K1_three_within_factor_3"] and not c["K2_specific_p_below_0.01"] and not c["K3_nine_within_factor_3"] and not c["K4_specific_p_below_0.01"]
    assert c["C1_holds"] and c["rows"] == 77910 and c["points"] == 49 and c["lines"] == 265
    assert abs(c["masses"]["worst_factor"] - 147.391) < 0.01 and abs(c["calibration_masses"]["fraction_fit_as_well"] - 0.26625) < 1e-9
    assert abs(c["mixing"]["worst_factor"] - 1.5120) < 0.001 and abs(c["calibration_mixing"]["fraction_fit_as_well"] - 0.30225) < 1e-9


def test_the_best_rows_live():
    G = json.loads((A / "verification" / "the_golden_valley.json").read_text(encoding="utf-8"))
    v = json.loads((ROOT / "frontier" / "B1637_fits_on_the_ruled_branch" / "received" / "HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))["masses_GeV"]["value"]
    C = json.loads((ROOT / "frontier" / "B1612_the_mixing_patterns_the_weave_fixes" / "verification" / "data.json").read_text(encoding="utf-8"))["ckm_abs"]["value"]
    t6 = np.log([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]])
    t3 = np.log([C[0][1], C[1][2], C[0][2]])
    A6, K3 = [], []
    for p in G["rows"]:
        for h in ("L_max", "L_2"):
            for rd in ("S", "St", "conjS"):
                A6.append(np.log(np.maximum(p["up|%s|%s" % (h, rd)] + p["down|%s|S" % h] + p["lep|%s|S" % h], 1e-300)))
                K3.append(np.log(np.maximum(p["ckm|%s|%s" % (h, rd)][:3], 1e-300)))
    w6 = math.exp(np.min(np.max(np.abs(np.array(A6) - t6), axis=1)))
    w3 = math.exp(np.min(np.max(np.abs(np.array(K3) - t3), axis=1)))
    c = _stored()
    assert abs(w6 - c["masses"]["worst_factor"]) < 1e-6 and abs(w3 - c["mixing"]["worst_factor"]) < 1e-9


def test_the_valley_geometry():
    G = json.loads((A / "verification" / "the_golden_valley.json").read_text(encoding="utf-8"))
    pts = [complex(*p["tau"]) for p in G["points"]]
    assert len(pts) == 49 and min(abs(abs(z - 0.5 * (1 if z.real >= 0 else -1)) - math.sqrt(5) / 2) for z in pts) < 1e-12
    assert all(1 - 1e-12 <= z.imag <= math.sqrt(5) / 2 + 1e-12 for z in pts)
    assert abs(max(p["s"] for p in G["points"]) - math.log((1 + math.sqrt(5)) / 2)) < 1e-12
    import mpmath as mp
    def F(t):
        q = mp.exp(mp.pi * 1j * t)
        th2, th3, th4 = mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
        eta = mp.exp(mp.pi * 1j * t / 12) * mp.qp(mp.exp(2 * mp.pi * 1j * t))
        return sum(abs(th / eta) ** 4 for th in (th2, th3, th4))
    for z in (pts[0], pts[12], pts[24], pts[40]):
        assert abs(F(mp.mpc(z.real, z.imag)) - 8) < 1e-9


def test_the_seal():
    for name in ("the_golden_valley.py", "compare.py", "b1656_funcs.py"):
        h = hashlib.sha256((A / "verification" / name).read_bytes()).hexdigest()
        assert h in (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    assert hashlib.sha256((A / "PREREGISTRATION.md").read_bytes()).hexdigest().startswith("3850a2f9")
