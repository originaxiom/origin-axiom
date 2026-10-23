"""B1743 -- the nine's target and the principled pencils (P-352), POST HOC exploration, NEGATIVE for its question.
Live: the idealised up channel's identity (m1 = 0, m2 m3 = |a3|^2 |h.h|, m2/m3 >= |h.h|/4) on random Higgs directions,
with a planted failure (a non-null channel breaks m1 = 0).  Stored: the target's best row reproduced (17.257, nearly
null) and no pencil below the bar."""
import json, math, pathlib, re
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1743_the_principled_pencils_and_the_nines_target"
N0 = np.array([0, 1, 1j]) / math.sqrt(2)


def _Y(u, h):
    return np.outer(u, h) + np.outer(h, u) - (u @ h) * np.eye(3)


def test_idealised_up_channel_live():
    rng = np.random.default_rng(1743)
    for _ in range(200):
        h = rng.normal(size=3) + 1j * rng.normal(size=3); h /= np.linalg.norm(h); a3 = complex(rng.normal(), rng.normal())
        s = np.linalg.svd(_Y(a3 * N0, h), compute_uv=False)
        assert s[2] / s[0] < 1e-12 and abs(s[0] * s[1] - abs(a3) ** 2 * abs(h @ h)) < 1e-10 * abs(a3) ** 2
        assert (s[1] / s[0]) >= abs(h @ h) / 4 * (1 - 1e-9)
    u = np.array([0.3, 1, 1j]); h = np.array([0.2, 1, -0.5j]); assert np.linalg.svd(_Y(u, h), compute_uv=False)[2] > 1e-3   # planted: u not null


def test_stored():
    d = json.loads((A / "verification" / "target.json").read_text(encoding="utf-8"))
    best = d["optima"][0]; assert abs(best["chi2_nine"] - 17.257) < 1e-2 and 0.015 < best["|h.h|/|h|^2"] < 0.02
    assert all(0.014 < o["|h.h|/|h|^2"] < 0.02 for o in d["optima"])
    run = (A / "verification" / "pencils_run.txt").read_text(encoding="utf-8")
    mins = [float(m) for m in re.findall(r"min chi2_nine\s+([0-9.]+)", run)]
    assert len(mins) == 10 and min(mins) > 21.67 and "rows below 21.67: 0" in run and all(l.endswith("rows below 21.67: 0") for l in run.strip().splitlines() if "min chi2_nine" in l)
