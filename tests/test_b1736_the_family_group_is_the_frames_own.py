"""B1736 -- the family group is the frame's own (P-302), PROVED.  Live: Gamma' at k = 21 is the cube's 24 rotations with
no Sym^3 invariant and one Lambda^3 invariant; B1656's coupling equals the vector closed form on random complex input;
the object's g = -R L^-1 mod 5 has order 3 in 2I.  Stored: E8's Cartan determinant and frames, the class permutation,
the channel weights' transformation under T and S."""
import importlib.util, json, pathlib
import numpy as np
V = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1736_the_family_group_is_the_frames_own" / "verification"


def _m():
    spec = importlib.util.spec_from_file_location("b1736_fg", V / "the_family_group.py"); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_gamma_prime_live():
    c = _m().part_c()
    assert [c[k]["order"] for k in ("5", "13", "21")] == [72, 72, 24] and c["21"]["real"]
    assert all(abs(c[k]["dim_Sym3_inv"]) < 1e-9 and abs(c[k]["dim_Lambda3_inv"] - 1) < 1e-9 for k in c)
    assert abs(c["21"]["Sym3 x rho'"] - 2) < 1e-9 and abs(c["21"]["Sym3 x sign"] - 1) < 1e-9


def test_the_closed_form_live():
    d = _m().part_d()
    assert d["closed_form_vs_coupling_rel"] < 1e-12 and d["B1659_det_law_rel"] < 1e-12


def test_the_stored_parts():
    r = json.loads((V / "the_family_group.json").read_text(encoding="utf-8"))
    a, b = r["A"], r["B"]
    assert a["roots"] == 240 and a["is_E8_diagram"] and a["order3"] == 20 and a["subgroups"] == 10
    assert a["frames_72_and_6x27_with_A2_roots"] and a["conjugation_transitive_on_frames"]
    assert b["order_g_q"] == 3 and b["left_mult_isometry"] and b["left_mult_cycles_on_classes"] == [3, 3]
    assert b["left_mult_and_weyl_same_class_permutation"] and b["weyl_sab_fixes_E6_pointwise"] and not b["left_mult_fixes_E6_pointwise"]
    for e in r["E"]:
        if e["move"] == "T":
            assert e["triplet_resid_R_-90"] < 1e-12 and abs(e["triplet_ratio_abs"] - 1) < 1e-9
            assert abs((e["triplet_phase/(2pi)"] - e["u1_phase/(2pi)"] + 0.5) % 1 - 0.5) < 1e-9
        else:
            assert e["triplet_resid_P"] < 1e-12 and abs(e["triplet_ratio"][0] - e["u1_ratio"][0]) < 1e-9
            assert abs((e["triplet_ratio"][1] - e["u1_ratio"][1]) % 1 - 0.5) < 1e-9      # u by -P: the scalar of u1 times -1
