"""B1727 -- the flavour-blind bound (P-299), PROVED. Live: with S = 1 B1656's coupling is c 1 + [a]_x (linear in the
channel weights; the unit images); the equality case (3, 1, 1); the proof's three steps on 2 000 random (c, a). Stored:
the minimum by 400 starts is 1/3 and no step was violated on 200 000 draws."""
import json, pathlib, importlib.util
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1727_the_flavour_blind_bound"


def _m():
    spec = importlib.util.spec_from_file_location("b1727_bound", A / "verification" / "the_flavour_blind_bound.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_the_structure_live():
    a = _m().part_a()
    assert a["linearity_max"] < 1e-12 and a["symmetric_part_minus_c1_max"] < 1e-12 and a["ijk_images_antisymmetry_max"] == 0.0
    assert a["unit_images"]["1"] == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert a["unit_images_imag_max"] == 0.0


def test_the_equality_case_live():
    s = _m().part_d()["singular_values"]
    assert abs(s[0] - 3) < 1e-12 and abs(s[1] - 1) < 1e-12 and abs(s[2] - 1) < 1e-12


def test_the_steps_live():
    c = _m().part_c(n=2000, seed=1727)
    assert c["step_i_max_(|c|-s2)/s1"] <= 1e-12 and c["step_ii_max_rel_(s1A-s2A)"] < 1e-12
    assert c["step_iii_max_(s1-3s2)/s1"] <= 1e-12 and c["min_ratio_random"] >= 1 / 3 - 1e-12


def test_the_stored_output():
    d = json.loads((A / "verification" / "the_flavour_blind_bound.json").read_text(encoding="utf-8"))
    assert abs(d["B"]["min_ratio"] - 1 / 3) < 1e-9 and d["B"]["starts"] == 400
    assert d["C"]["draws"] == 200000 and d["C"]["step_iii_max_(s1-3s2)/s1"] < 0 and d["C"]["step_i_max_(|c|-s2)/s1"] <= 0
    assert d["C"]["min_ratio_random"] >= 1 / 3


def test_the_claim_line_matches():
    v = json.loads((A / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["verdict"] == "PROVED" and "m2/m3 >= 1/3" in v["claim_one_line"] and "0.333333333333" in v["claim_one_line"]
