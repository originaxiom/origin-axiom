"""Post-result regression locks; separately sealed, not advance predictions."""
from verify_matter_locus import candidate_point, certificate


def test_complete_candidate_set_no_unanalysed_remainder():
    expected = {("1", "-1"), ("1", "1"), ("1", "0", "1")}
    for seed in range(2):
        assert {tuple(c) for c in certificate(seed)["candidate_factors"]} == expected


def test_paired_interior_dimensions_not_erased_by_zero_index():
    for seed in range(2):
        for factor, dimension in [(("1", "-1"), 1), (("1", "1"), 2), (("1", "0", "1"), 2)]:
            result = candidate_point(seed, factor)
            assert result["indexed"]["I"] == 0
            assert result["E_relative"]["interior"] == dimension
            assert result["dual_relative"]["interior"] == dimension
