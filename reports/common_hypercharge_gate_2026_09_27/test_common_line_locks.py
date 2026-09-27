from verify_common_line import (
    candidate_point, certificate, character_reduction, inputs, ml,
    modules, specialization,
)
from verify_global_seed import blockdiag, eye, kron, zeta5


def test_all_eight_families_zero_index_with_complete_minor_coverage():
    count = 0
    for number in range(2):
        for e in character_reduction()["quadratic_characters"]:
            eta = tuple(e)
            result = certificate(number, eta)
            assert all(c["interior_upper_bound_off_candidate_roots"] == 0
                       for c in result["coefficients"].values())
            for coefficients in result["candidate_factors"]:
                assert len(coefficients)-1 <= inputs()["max_factor_degree"]
                point = candidate_point(number, eta, tuple(coefficients))
                assert point["indexed"]["I"] == 0
            count += 1
    assert count == 8


def test_nontrivial_quadratic_paired_locus_and_spurious_nonunitary_roots():
    for number in range(2):
        for e in character_reduction()["quadratic_characters"]:
            if not any(e):
                continue
            eta = tuple(e)
            paired = candidate_point(number, eta, ("1", "0", "1"))
            assert paired["E_relative"]["interior"] == paired["dual_relative"]["interior"] == 1
            spurious = candidate_point(number, eta, ("1", "-4", "1"))
            assert spurious["E_relative"]["interior"] == spurious["dual_relative"]["interior"] == 0
            assert spurious["indexed"]["V"][0] == spurious["indexed"]["dual"][0] == 0


def test_absorption_by_direct_cyclotomic_matrices_all_fifth_powers():
    z = zeta5()
    for number in range(2):
        gens = modules(ml.ex.inputs()["seeds"][number])["E"]
        spec = inputs()["absorption"][number]
        base = specialization(gens, 2*eye(4))
        d = blockdiag(*(z**s for s in spec["diagonal_exponents"]))
        for r in range(5):
            actual = specialization(gens, 2*(z**r))
            conjugator = d**r
            for g, a, c in zip(base.mats, actual.mats, inputs()["M2_chi5_exponents"]):
                twist = kron(eye(5), z**(r*spec["k"]*c))
                assert a == conjugator*twist*g*conjugator.inv()
        twisted_b = kron(eye(5), z**spec["k"])*base.mats[1]
        correct_b = specialization(gens, 2*z).mats[1]
        assert correct_b != d.inv()*twisted_b*d
