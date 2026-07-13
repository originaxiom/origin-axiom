"""Locks for Frontier Cell 1: universal Z/11 charge transport."""

from cell1_charge_transport import run_all


def test_all_12_nodes_have_unique_z11_torsion():
    result = run_all()
    assert len(result["node_records"]) == 12
    for record in result["node_records"]:
        assert record["det_I_minus_A"] == -11
        assert record["smith_diagonal"][-1] == 11
        assert all(value == 1 for value in record["smith_diagonal"][:-1])
        assert record["charge_dimension_mod_11"] == 1


def test_all_flow_edges_transport_charge():
    result = run_all()
    assert len(result["edge_records"]) == 12
    assert all(
        record["intertwining_verified"]
        for record in result["edge_records"]
    )
    assert all(
        record["edge_scalar_mod_11"] in range(1, 11)
        for record in result["edge_records"]
    )


def test_base_charge():
    result = run_all()
    assert result["base_charge_abAB"] == [1, 3, 6, 7]


def test_two_cycle_holonomy_is_trivial():
    result = run_all()
    assert sorted(result["two_cycle_scalars"]) == [7, 8]
    assert result["two_cycle_holonomy_mod_11"] == 1
    assert (
        result["classification"]["nontrivial_clock_charge_holonomy"]
        == "REFUTED"
    )
