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
