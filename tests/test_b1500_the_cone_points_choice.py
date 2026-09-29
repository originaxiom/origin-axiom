"""B1500 lock -- THE CONE POINT'S CHOICE.

On the one-point compactification of a cusped hyperbolic 3-manifold every cusp point is not Witt (its link is the cusp torus). With
lower middle perversity (eps = -1), upper (+1) or a Lagrangian line (0) chosen at each point, the Euler characteristic of the
intersection homology is sum eps -- for every cuspidal Higgs twist.  Lower everywhere: IH = (1, b1, b1 - k, 1); upper: (1, b1 - k,
b1, 1).  A generic twist moves the groups (one mode per cusp point in a single degree) and never chi."""
import importlib.util
import json
import random
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1500_the_cone_points_choice" / "verification"


def _load():
    spec = importlib.util.spec_from_file_location("b1500_cone_point_ih", VER / "cone_point_ih.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _chi(g):
    return g[0] - g[1] + g[2] - g[3]


def test_m004_and_m003_with_both_subdivisions():
    C = _load()
    for name in ("m004", "m003"):
        r = C.run_manifold(name, name, second=True, rng=random.Random(7))      # asserts every prediction inside
        res = r["results"]
        assert r["H(Q^)"] == [1, 0, 1, 1] and r["cuspidal dimension (H^1(Q^))"] == 0
        assert res["lower"] == [1, 1, 0, 1] and res["upper"] == [1, 0, 1, 1]
        assert all(x["IH"] == [1, 0, 0, 1] and x["chi"] == 0 for x in res["lagrangian"])
        assert res["second subdivision"]["agrees"] and res["second subdivision"]["simplices"][3] == 1152


def test_a_census_cover_twisted_by_its_cuspidal_classes():
    C = _load()
    census = json.load(open(ROOT / "frontier" / "B1399_the_rank_two_higgs" / "verification" / "census.json"))["members"]
    (m,) = [m for m in census if m["label"].startswith("BvLQvvLvwMAQLQAQLPQcefdh")]       # the v2873 cover: 1 cusp, dim 2
    r = C.run_manifold(m["label"], "v2873 cover", rng=random.Random(11), twists=2)
    res = r["results"]
    assert (r["cusps"], r["b1"], r["cuspidal dimension (H^1(Q^))"]) == (1, 3, 2) == (m["cusps"], 3, m["dim"])
    assert res["lower"] == [1, 3, 2, 1] and res["upper"] == [1, 2, 3, 1]
    for t in res["twisted"]:
        assert t["IH_lower"] != res["lower"]                                   # the twist moves the groups ...
        assert (_chi(t["IH_lower"]), _chi(t["IH_upper"])) == (-1, 1)         # ... and not chi


def test_the_recorded_run_on_ten_members():
    reps = json.load(open(VER / "cone_point_ih.json"))
    assert len(reps) == 10
    for r in reps:
        res, k, b1 = r["results"], r["cusps"], r["b1"]
        assert res["lower"] == [1, b1, b1 - k, 1] and res["upper"] == [1, b1 - k, b1, 1]
        assert r["cuspidal dimension (H^1(Q^))"] == b1 - k
        assert all(x["chi"] == x["predicted"] for x in res["mixed"] + res["lagrangian"])
        for t in res["twisted"]:
            assert tuple(t["chi"]) == (k, -k, k)
    cube = [r for r in reps if r["label"].startswith("cube~3.24")][0]
    assert (cube["cusps"], cube["b1"], cube["cuspidal dimension (H^1(Q^))"]) == (4, 5, 1)
    assert all(t["IH_lower"] == [0, 4, 0, 0] for t in cube["results"]["twisted"])     # one mode per cusp point


def test_the_harvey_lawson_link_is_the_hexagonal_torus():
    """the metric of the link {(e^{i t1}, e^{i t2}, e^{-i(t1+t2)})/sqrt 3}: (1/3)[[2, 1], [1, 2]], i.e. shape e^{i pi/3}"""
    def point(t1, t2):
        return np.array([np.exp(1j * t1), np.exp(1j * t2), np.exp(-1j * (t1 + t2))]) / np.sqrt(3)
    t1, t2, h = 0.37, 1.91, 1e-6
    e1 = (point(t1 + h, t2) - point(t1 - h, t2)) / (2 * h)
    e2 = (point(t1, t2 + h) - point(t1, t2 - h)) / (2 * h)
    G = np.array([[np.vdot(u, v).real for v in (e1, e2)] for u in (e1, e2)])
    assert np.allclose(G, np.array([[2, 1], [1, 2]]) / 3, atol=1e-8)
    cos = G[0, 1] / np.sqrt(G[0, 0] * G[1, 1])
    assert abs(cos - 0.5) < 1e-8 and abs(G[0, 0] - G[1, 1]) < 1e-8          # equal periods at 60 degrees
