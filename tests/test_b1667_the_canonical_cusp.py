"""B1667 -- the canonical cusp. The sealed instrument unchanged; the stored cells; live through the sealed instrument:
at tau = e^{i pi/3} the canonical radii equal the eta^4 closed form and the lift vanishes; the bite -- a real but
non-uniformising root (0.4 + 2.2i, c = -1.956, found by the reviewing pass) fails the uniformisation check, while the
tracked root passes it."""
import hashlib, importlib.util, json, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1667_the_canonical_cusp"
INSTR = A / "verification" / "the_canonical_cusp.py"


def _load():
    spec = importlib.util.spec_from_file_location("b1667_lock", INSTR)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_sealed_and_stored():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at ca1c08efb")
    assert hashlib.sha256(open(INSTR, "rb").read()).hexdigest() == first.split()[4]
    assert hashlib.sha256(open(A / "PREREGISTRATION.md", "rb").read()).hexdigest().startswith("83689a5d")
    d = json.load(open(A / "verification" / "the_canonical_cusp.json"))
    assert not d["failures"] and len(d["points"]) == 54
    assert all(d["L0"].values())
    assert d["T1"]["holds"] and 0.6 < d["T1"]["L_max_range"][0] and d["T1"]["L_max_range"][1] < 0.7
    assert 2.2 < d["T1"]["L_2_range"][0] and d["T1"]["L_2_range"][1] < 2.8
    assert d["T2"]["holds"] and d["T2"]["rho_2_min"] > 0.03 and d["T2"]["rho_max_min"] > 0.2
    assert d["T3"]["holds"] and abs(d["T3"]["slope"] - 1) < 0.1
    assert d["T4"]["holds"] and -3.0 < d["T4"]["slope"] < -2.3
    assert d["verdict_by_rule"] == "PROVED"
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"


def test_live_eta_control_and_wrong_root_bite():
    m = _load()
    r = m.point(np.exp(1j * np.pi / 3), 0.0)
    assert abs(r["L_max"] - 0.69208004049) < 1e-6 and abs(r["L_2"] - 2.78647514288) < 1e-6
    assert abs(r["cusp_area"] - 6) < 1e-8 and r["rho_2"] < 1e-10
    tau = 0.4 + 2.2j
    good, _ = m.solve_accessory(tau, 0.556)
    bad, res = m.solve_accessory(tau, -1.956)
    assert np.max(np.abs(res)) < 1e-9 and abs(good - bad) > 1                    # two distinct real roots
    for c, sign in ((good, 1), (bad, -1)):
        lat, z0, Aa, Ab = m.monodromy(tau, c)
        P0 = m.mobius_of(m.puncture_loop(lat, c, z0, 0.05))
        g, *_ = m.normalise(Aa, Ab, P0)
        assert sign * m.uniformisation_check(tau, c, g, npts=4) > 0             # bite: the wrong root fails


def test_the_radii_between_the_grid_points_p542():
    """P-542 (2026-11-19): the committed midpoint run reproduces the committed column at the grid points, and each stated
    interpolation error is recomputed here from the run's midpoint radius and the committed column's two neighbours."""
    import re
    run = (A / "verification" / "radius_midpoints_run.txt").read_text(encoding="utf-8")
    rep = float(re.search(r"largest difference ([0-9.e+-]+)", run).group(1)); assert rep < 1e-10, rep
    col = {round(r[0], 6): (r[1], r[2]) for r in json.loads((A / "verification" / "the_canonical_cusp.json").read_text())["readout"]["column_025"]}
    rows = re.findall(r"^\s+(\d\.\d{3})\s+([0-9.]+)\s+([+-][0-9.e+-]+)\s+([0-9.]+)\s+([+-][0-9.e+-]+)$", run, re.M)
    assert len(rows) == 12
    em = e2 = 0.0
    for y, lm, dm, l2, d2 in rows:
        y = float(y); lo, hi = col[round(y - 0.125, 6)], col[round(y + 0.125, 6)]
        tol = lambda d: 1e-6 + 6e-3 * abs(float(d))                    # the run prints L to 6 decimals, errors to 3 figures
        assert abs(float(lm) - (lo[0] + hi[0]) / 2 - float(dm)) < tol(dm) and abs(float(l2) - (lo[1] + hi[1]) / 2 - float(d2)) < tol(d2)
        assert float(dm) < 0 and float(d2) < 0                       # convex: the chord lies above
        em, e2 = max(em, abs(float(dm))), max(e2, abs(float(d2)))
    assert 6.6e-4 < em < 6.8e-4 and 4.3e-3 < e2 < 4.5e-3, (em, e2)
    f = (A / "FINDINGS.md").read_text(encoding="utf-8")
    assert "at most 6.7 × 10⁻⁴ in L_max and 4.4 × 10⁻³ in L_2" in f
