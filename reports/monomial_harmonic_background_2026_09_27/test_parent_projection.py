from verify_parent_projection import (
    actual_root_trace_control, direct_sum_gauge_control, projection_control,
)


def test_full_cartan_projection_and_actual_structure_weyl_normalizer():
    result = projection_control()
    assert result["projection_rank"] == 4 and result["root_count"] == 240
    assert result["non_normalizing_reflections"] > 0


def test_raw_trace_factor_from_every_root_not_only_branching():
    assert actual_root_trace_control() == 60


def test_other_parent_gauge_directions_do_not_remove_diagonal_class():
    assert direct_sum_gauge_control()
