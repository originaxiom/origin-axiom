"""Locks for Cell 2 observer protocol classification."""

from cell2_observer_protocols import run_all


def test_one_letter_protocol_exact_closure():
    result = run_all()
    summary = result["protocols"]["1"]["summary"]
    assert summary["node_count"] == 12
    assert summary["fixed_point_count"] == 3
    assert summary["nontrivial_cycle_lengths"] == [2]
    assert summary["nontrivial_cycle_q_types"] == [[2, 2]]
    assert all(
        proof["exact_step_certified"]
        for proof in result["protocols"]["1"]["proofs"].values()
    )


def test_two_letter_protocol_refutes_intrinsic_graph():
    result = run_all()
    summary = result["protocols"]["2"]["summary"]
    assert summary["node_count"] == 12
    assert summary["fixed_point_count"] == 2
    assert summary["nontrivial_cycle_lengths"] == [2, 2]
    assert result["protocols"]["2"]["sigma_orbit"]["cycle_length"] == 2


def test_protocol_rows():
    result = run_all()
    expected = {
        1: (12, 3, [2], 1),
        2: (12, 2, [2, 2], 2),
        3: (11, 3, [2, 2], 2),
        4: (10, 4, [2], 1),
        5: (12, 3, [3], 1),
        6: (10, 4, [], 1),
        7: (12, 3, [4], 1),
        8: (11, 1, [2, 2, 3], 2),
        9: (12, 1, [2, 2, 3], 2),
        10: (12, 1, [2, 2, 3], 2),
        11: (12, 2, [2, 3], 2),
        12: (11, 1, [2, 2, 2], 2),
    }
    for row in result["protocol_summary_rows"]:
        assert (
            row["node_count"],
            row["fixed_point_count"],
            row["nontrivial_cycle_lengths"],
            row["sigma_cycle_length"],
        ) == expected[row["prefix_length"]]
        assert row["all_steps_exactly_certified"]


def test_integral_conjugacy_collision():
    result = run_all()
    collision = result["invariant_packet_collision"]
    assert collision["conjugator_determinant"] == -1
    assert collision["first_target"] != collision["second_target"]
    assert result["classification"][
        "incidence_arithmetic_packet_predicts_target"
    ].startswith("REFUTED")
