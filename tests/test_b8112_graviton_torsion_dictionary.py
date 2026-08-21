"""B8112 -- locks the dictionary entry's mathematics, read from results.json."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = json.load(open(os.path.join(ROOT, "frontier", "B8112_graviton_torsion_dictionary", "results.json")))


def test_the_graviton_one_loop_is_not_a_single_rho_m():
    assert R["is_a_single_rho_m"] is False
    assert R["graviton_one_loop_is"] == "prod_{n>=2} |R(n,sigma_n)|^{-2}"


def test_the_two_orderings_agree_and_reproduce_b8100():
    assert R["orderings_agree"] is True
    assert abs(R["logZ_via_R"] - R["logZ_via_gamma"]) < 1e-12
    assert R["b8100_reproduced"] is True
    assert abs(R["logZ_via_gamma"] - (-0.2729771708384004)) < 1e-9


def test_the_n2_term_carries_the_cutoff_instability():
    """The abscissa-of-convergence finding: Re(s) > 2, and the product starts AT 2."""
    assert R["n2_last_delta"] > 100 * R["n3plus_last_delta"]
    assert R["n2_oscillates"] is True


def test_c_ratio_recomputation_matches_b8104s_unscripted_values():
    for m in ("3", "4", "5"):
        assert abs(R["c_ratio_recomputed"][m] - R["c_ratio_b8104"][m]) < 1e-8
    assert R["c_ratio_agrees"] is True


def test_torsion_ratios_are_computed_and_decrease():
    t = {int(k): v for k, v in R["torsion_ratio"].items()}
    assert abs(t[3] - 1.429269e-02) < 1e-8
    assert all(t[m] > t[m + 1] for m in (3, 4, 5))
    assert R["torsion_ratio_relative_uncertainty"] < 1e-5


def test_b8100s_conjugate_control_ran_on_a_different_dataset():
    """The E2 frame-not-instance instance: control at cutoff 2.0, headline at 5.5."""
    assert R["b8100_conjugate_control_ran_at_cutoff"] < R["b8100_headline_used_cutoff"]
    assert R["self_conjugate_theta_pi_classes"] == 4


def test_kappa_and_volume_are_the_objects_own():
    assert R["kappa"] == 1
    assert abs(R["volume"] - 2.029883212819307) < 1e-15
