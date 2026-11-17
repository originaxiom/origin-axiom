"""B1953's lock: the stored output of weyl_operator.py, the exact facts live, and one covariance test live on the frame."""
import json, pathlib, sys
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
D = json.loads((HERE / "weyl_operator.json").read_text())
BASES = ("0.13+1.7i", "0.31+1.2i")


def test_the_exact_facts_on_the_weil_space():
    import exact_facts as EF
    f = EF.facts()
    assert f["twist_is_the_degree"] is True and f["even_combinations_commuting_with_the_parity"] == 12
    assert max(f["basis_of_sl5"], f["parity_reverses_the_label"], f["trace_against_the_parity"], f["hypercharge_is_the_sum"], f["weil_T_no_phases"], f["weil_S_no_phases"]) < 1e-12


def test_the_down_sector_is_one_covariant_operator():
    for b in BASES:
        for rd in ("S", "St"):
            r = D["%s down %s" % (b, rd)]
            assert r["mixing_of_3_and_2"] < 1e-12 and r["parseval"] < 1e-12, (b, rd)
            assert max(abs(x - y) for x, y in zip(r["gramian_3"], r["gramian_2"])) > 0.05          # the two blocks differ
            for gen in ("T", "S"):
                g = r[gen]
                assert g["law_residual"] < 1e-10 and g["unitary_null"] < 1e-10 < 1e-3 < g["unitary_next"], (b, rd, gen)
                assert g["phase_order"] == 5 and g["phase_form_deviation"] < 1e-10
                assert g["O_law_with_the_weil_representation"] < 1e-10 and g["O_singular_values"] < 1e-9
                assert max(g["gramian_3"], g["gramian_2"], g["phased_sum"]) < 1e-9
                assert g["O_without_table"] > 0.1 and g["plain_sum"] > 0.05                             # the controls move
                assert abs(g["modulus"][1] - (1.0 if gen == "T" else r["abs_tau"])) < 1e-6 and g["modulus"][1] - g["modulus"][0] < 1e-9


def test_the_up_sector_is_obstructed_at_level_five():
    for b in BASES:
        for rd in ("S", "St"):
            r = D["%s up %s" % (b, rd)]
            assert r["mixing_of_3_and_2"] > 0.1
            for gen in ("T", "S"):
                assert r[gen]["law_residual"] < 1e-10 and r[gen]["phase_order"] == 25                    # the law holds; its phases are 25th roots
                assert r[gen]["O_singular_values"] > 0.1 and r[gen]["O_law_with_the_weil_representation"] > 0.1


def test_one_case_live_on_the_frame():
    import weyl_operator as W
    Y0 = W.frame("0.13", 1.7, "down")["S"]; Y1 = W.frame("1.13", 1.7, "down")["S"]
    assert np.abs(W.svn(W.O(Y1)) / W.svn(W.O(Y0)) - 1).max() < 1e-9
    assert np.abs(W.svn(W.O(Y1, False)) / W.svn(W.O(Y0, False)) - 1).max() > 0.1
    lw = W.law(Y0, Y1, "T")
    assert lw["residual"] < 1e-10 and W.phase_form(lw["phi"], "T") < 1e-10
