"""B1708 -- W120 and W121 on main. Stored: the cone's Ricci tensor vanishes exactly at kappa = -1; the least volume is
+-LR; Z/12; the q = 2p invariance and the exponent 1/6; the lifts scalar exactly at k = 3, 6, 9, 12 with -1 at 6 and 1 at
12. Live: the abelianization's Smith form; the exponent at |z| = 1e-7."""
import json, pathlib
import sympy as sp, mpmath as mp
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1708_w120_w121_on_main" / "verification"


def test_stored():
    d = json.loads((A / "w120_w121_on_main.json").read_text(encoding="utf-8"))
    assert d["1_cone"]["all_vanish_at_kappa_-1"] and d["1_cone"]["Ric_tt"] == "0"
    assert d["2_volumes"]["least"][0][1][1:] == "LR" and abs(d["2_volumes"]["least_value"] - 2.0298832128) < 1e-9
    assert d["3_abelianization"]["smith"] == [1, 12]
    inv = d["4_invariance_and_exponent"]["max_rel_dev"]
    assert inv["p=1 q=2"] < 1e-20 and inv["p=2 q=4"] < 1e-20 and min(inv["p=1 q=1"], inv["p=1 q=3"], inv["p=2 q=3"]) > 1e-2
    l = d["5_lifts"]
    assert l["scalar_exactly_at"] == [3, 6, 9, 12] and l["products"]["6"]["lambda"] == [-1.0, 0.0] and l["products"]["12"]["lambda"] == [1.0, -0.0]


def test_live():
    from sympy.matrices.normalforms import smith_normal_form
    assert [int(v) for v in smith_normal_form(sp.Matrix([[4, 0], [1, 3]]), domain=sp.ZZ).diagonal()] == [1, 12]
    mp.mp.dps = 30
    zz = mp.mpf("1e-7"); tau = mp.log(zz) / (2j * mp.pi)
    eta = mp.exp(2j * mp.pi * tau / 24) * mp.qp(mp.exp(2j * mp.pi * tau))
    f = mp.im(tau) * abs(eta) ** 4
    assert abs(float(mp.log(f / (-mp.log(zz) / (2 * mp.pi))) / mp.log(zz)) - 1 / 6) < 1e-5
