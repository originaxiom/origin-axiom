"""B1806 -- the third fixed point, and a proxy corrected (P-406's L2 at tau = i).  The committed runs: rho(S) of order 8;
the exact s2/s1 = 1 at i where B1691's proxy reads 1/2; the f2 = 0 sections' slope 2; the closed form at weight 7/2."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1806_the_third_fixed_point_and_a_proxy_corrected" / "verification" / "referee"


def test_the_residual_symmetry_and_the_degenerate_pair():
    r = json.loads((V / "referee_check.json").read_text(encoding="utf-8"))
    assert r["1_rho_S_order"] == 8
    f = json.loads((V / "f2zero_with_b1691_code.json").read_text(encoding="utf-8"))
    for k in ("3/2 seed1 at i", "11/2 seed1 at i", "19/2 seed1 at i"):
        assert f[k]["proxy"] == "0.5" and f[k]["exact s2/s1"] == "1.0"


def test_the_sections_without_d2r_and_the_closed_form():
    f = json.loads((V / "f2zero_with_b1691_code.json").read_text(encoding="utf-8"))
    for k in ("15/2, f2 = 0", "23/2, f2 = 0"):
        assert f[k]["slope_in_eps"] == [2.0, 2.0, 2.0]
    c = json.loads((V / "closed_form_7half.json").read_text(encoding="utf-8"))
    assert abs(float(c["c - 1/192"])) < 1e-40
