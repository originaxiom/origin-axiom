import verify as v


def test_all_exact_safeguards():
    rows = v.checks()
    assert len(rows) > 300 and all(rows.values())


def test_all_ranks_include_complex_frames_and_missing_circle_point():
    rows = v.checks()
    for rank in range(7):
        for basis in ('coordinate', 'complex_rotated'):
            for direction in ('rational_circle', 'omitted_circle_point'):
                assert rows[f'{direction}_{rank}_{basis}_forbidden_calderon_angle']


def test_green_and_total_grading_are_not_sufficient_for_ellipticity():
    rows = v.checks()
    assert rows['bad_plane_green_isotropic'] and rows['bad_plane_total_graded']
    assert rows['bad_plane_actual_zero_solution'] and rows['bad_plane_finite_positive_norm']
    assert rows['bad_plane_fails_angle']


def test_all_angular_formula_not_only_critical_trace():
    rows = v.checks()
    assert rows['normal_square_zeroth'] and rows['normal_square_first_derivative']
    assert rows['radial_integration_by_parts_plus'] and rows['radial_integration_by_parts_minus']
    assert rows['half_shift_control']


def test_actual_coefficient_and_spin_conventions():
    rows = v.checks()
    assert rows['same_clifford_as_full_metric']
    assert rows['actual_puncture_coefficient'] and rows['combined_angular_periodic']


def test_cutoff_argument_distinguishes_complete_and_incomplete_metrics():
    rows = v.checks()
    assert rows['full_metric_cusp_cutoff_bound'] and rows['complete_cusp_distance']
    assert rows['incomplete_metric_cutoff_control'] and rows['incomplete_control_distance']
