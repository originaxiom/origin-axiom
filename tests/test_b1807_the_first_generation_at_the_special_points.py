"""B1807 -- the first generation at the special points, and what the end radius changes (P-431).  The committed runs: the
identity a.R = -f2 eta^6/4 at every weight; the large-L exponents as predicted; at finite L near i the k = 3/2 class's exponent 1;
B1697's a0 at i, m2/m3 = 2/3."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1807_the_first_generation_at_the_special_points" / "verification"


def test_the_identity_and_the_large_L_exponents():
    r = json.loads((V / "first_generation_near_i.json").read_text(encoding="utf-8"))
    assert all(r["identity a.R + f2 eta^6/4 = 0"].values()) and len(r["identity a.R + f2 eta^6/4 = 0"]) == 12
    assert r["dR.dR / eta^6"]["value"] == ["1/4", "0"]
    assert r["all_hold"] is True
    assert r["slopes"]["43/2, f2 = E6^3"]["seed1"]["slope_lift_in_eps"] == [3.0, 3.0, 3.0]


def test_the_end_radius_and_the_parameter_free_sections():
    f = json.loads((V / "referee" / "ref_finite_L.json").read_text(encoding="utf-8"))
    for name, row in f["i"].items():
        if name.startswith("i 3/2"):
            for phi in row.values():
                for L in ("L=0.65", "L=2.5"):
                    assert abs(phi[L]["m1 slopes"][-1] - 1.0) < 0.01
    a = json.loads((V / "referee_p406" / "r6_a0_at_i.json").read_text(encoding="utf-8"))
    assert a["a0 = D2R - E4 R/48 (k=7/2) @ i"]["m2/m3 = s2/s1"] == "0.666666666666667"
