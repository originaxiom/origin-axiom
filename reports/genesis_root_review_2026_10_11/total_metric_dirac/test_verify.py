import verify as v


def test_all_exact_metric_and_operator_identities():
    assert len(v.checks()) > 300
    assert all(v.checks().values())


def test_clifford_compatibility_has_independent_coordinate_connection():
    g, co, E, gi, G, C, GK, GC, cs, omega, wc, M, K = v.geometry()
    assert GK == GC
    assert any(not v.zero(GK[i][j][k]) for i in range(4) for j in range(4) for k in range(4))


def test_mixed_term_cannot_be_dropped_from_geometric_operator():
    rows = v.checks()
    assert rows['omitted_mixed_rejected'] and rows['reversed_mixed_rejected']
    assert rows['full_spin_term']


def test_density_and_flat_controls_are_not_universal_nonzero_detector():
    rows = v.checks()
    assert rows['missing_density_rejected']
    assert rows['flat_control_connection'] and rows['flat_control_curvature']


def test_curved_line_keeps_full_lichnerowicz_coupling():
    rows = v.checks()
    names = [key for key in rows if key.startswith('twisted_lichnerowicz_')]
    assert len(names) == 15 and all(rows[key] for key in names)


def test_deck_and_unitary_radial_map():
    rows = v.checks()
    assert rows['cusp_deck_coframe'] and rows['unitary_radial_term'] and rows['radial_density']
