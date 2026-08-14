"""B895 locks: the 27-suite (exact color, Z6 kernel readout, belt confirms B884,
the solo-suite verdict tuples)."""
import json
import os
from fractions import Fraction

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B895_27_suite")


def _res():
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_z6c_exact_color_gates():
    z = _res()["z6c_exact_color"]
    assert z["color_dim_Q"] == 8 and z["color_cartan_dim_Q"] == 2
    assert z["singlet_space_dim"] == 9 and z["triplet_space_dim"] == 18
    # Casimir spectrum {0 x9, 4/9 x18}; tr(h^3)=0 => color is vector-like 3+3bar
    eigs = {Fraction(v): m for v, m in z["casimir_eigenvalues"]}
    assert eigs == {Fraction(0): 9, Fraction(4, 9): 18}
    assert z["tr_h3_on_T18"] == 0
    assert z["all_solo_gates"] is True


def test_z6d_kernel_coverage():
    z = _res()["z6d_kernel_readout"]
    assert z["singlets_covered"] == [9, 9]
    assert z["triplets_covered"] == [18, 18]
    assert z["triplet_cells"] == 6
    assert z["all_triplets_carry_hcp_fit"] is True


def test_belt_confirms_b884_after_projection():
    b = _res()["belt639"]
    # the refinement story: 15 fine cells from the four-operator combo,
    # exactly 11 coarse (X1,Y) classes = B884's cells
    assert b["fine_cells"] == 15 and b["coarse_X1Y_classes"] == 11
    # the 17-vs-11 anomaly dissolves under projection, at both seeds
    assert b["coarse_allowed_seed7"] == 11
    assert b["coarse_allowed_seed11"] == 11
    assert b["b884_confirmed"] is True
    # hypercharge direction at a second prime: exactly the conjugation pair
    assert b["y_solve_passing"] == 2 and b["y_solve_is_conjugation_pair"] is True


def test_solo_suite_verdict_tuples():
    s = _res()["solo_suite_verdicts"]
    assert (s["hypercharge"]["conjugation_pair_rank"],
            s["hypercharge"]["mixed_rank"]) == (3, 4)
    assert (s["g20"]["dim"], s["g20"]["derived"], s["g20"]["center"]) == (20, 19, 1)
    assert s["z2_obstruction"]["product_c"] == -1
    assert s["z2_obstruction"]["all_commuting_config_exists"] is False
    assert s["texture"]["allowed_cells"] == s["texture"]["b884_cells"] == 11
