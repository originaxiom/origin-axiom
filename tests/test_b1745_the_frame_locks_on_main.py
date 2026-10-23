"""B1745 -- the web seat's frame locks on main (P-358), PROVED.  Live: K1 the canonical matrix (sympy); K3 at four grid
points (|V_cb| against |kappa_u - kappa_d| with w = +u1 within 3%, with w = -u1 far off: the control).  Stored: the run."""
import importlib.util, json, pathlib
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1745_the_frame_locks_on_main"


def _m():
    spec = importlib.util.spec_from_file_location("b1745_fl", A / "verification" / "frame_locks.py"); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); return m


def test_k1_live():
    assert _m().k1()["F^dagger Y F - seat's matrix (simplified, max entry)"] == "Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])"


def test_k3_live_with_control():
    m = _m(); rows = [r for task in ((1, 0.5625, 2.6), (6, 0.4375, 3.1)) for r in m.point(task)]
    assert max(r["rel_err_sign+1"] for r in rows) < 0.03 and min(r["rel_err_sign-1"] for r in rows) > 1.0


def test_stored():
    d = json.loads((A / "verification" / "frame_locks.json").read_text(encoding="utf-8"))
    assert d["K3 sign +1"]["median rel err"] < 0.01 and d["K3 sign +1"]["max"] < 0.03 and d["K3 sign -1"]["median rel err"] > 1
    assert d["K4"]["order 5 max |u1|/|u|"] == 0.0 and d["K4"]["order 10 max |a2|/|u|"] == 0.0 and d["K4"]["order 5 min |a2|/|u|"] > 0.01
    k7 = d["K7"]; assert abs(k7["R at 0.3 + 4.0i"][0] - 2 * np.sqrt(2)) < 1e-6 and abs(k7["DR at 0.3 + 4.0i"][1] - 20) < 1e-4
