"""Exact topology controls of the actual boundary objects, not a fitted chiral spectrum."""
import pytest

from reports.physical_bridge_2026_09_05 import boundary_index as b


@pytest.fixture(scope="module")
def result():
    return b.run()


def test_cells_and_rational_homology_agree(result):
    for row in result["torus"]["examples"].values():
        assert row["chi"] == sum((-1)**k*n for k, n in enumerate(row["betti"]))
        assert row["chi"]+row["complement_chi"]-row["intersection_chi"] == 0
    assert result["torus"]["examples"]["torus"]["betti"] == [1, 2, 1]


def test_invalid_complexes_rejected():
    grid = b.Cubes((12, 12))
    face = grid.cell((0, 0), 3)
    cells = grid.closure([face])
    assert grid.cohomology(cells)["betti"] == [1, 0, 0]
    with pytest.raises(ValueError, match="not closed"):
        grid.cohomology({face})
    with pytest.raises(ValueError, match="not a subcomplex"):
        grid.cohomology(cells, {face})


def test_annular_zero_and_three_disk_control(result):
    rows = result["torus"]["examples"]
    assert rows["two_annuli"]["betti"] == [2, 2, 0]
    assert rows["two_annuli"]["relative_chi_if_core_chi_zero"] == 0
    assert rows["three_disks"]["betti"] == [3, 0, 0]
    assert rows["torus_minus_three_disks"]["betti"] == [1, 4, 0]
    assert rows["three_disks"]["relative_chi_if_core_chi_zero"] == -3
    assert rows["torus_minus_three_disks"]["relative_chi_if_core_chi_zero"] == 3


def test_theta_even_does_not_mean_annular_or_all_symmetries(result):
    rows = result["torus"]["examples"]
    assert rows["three_disks"]["theta_preserves"]
    assert not rows["three_disks"]["theta_exchanges_sides"]
    assert not any(rows["three_disks"]["half_translation_preserves"].values())
    assert rows["two_annuli"]["theta_exchanges_sides"]


def test_null_circle_iff_fails_for_actual_nested_partition(result):
    row = result["torus"]["examples"]["nested_null_circles"]
    assert row["betti"] == [2, 2, 0] and row["chi"] == 0
    assert len(row["boundary_loops"]) == 2
    assert all(c["winding"] == [0, 0] for c in row["boundary_loops"])
    annular = result["torus"]["examples"]["two_annuli"]
    assert len(annular["boundary_loops"]) == 4
    assert all(c["winding"] != [0, 0] for c in annular["boundary_loops"])


def test_proper_arc_excision_changes_the_underlying_manifold(result):
    for row in result["excision"]:
        k = row["arcs"]
        assert row["Q"]["betti"] == [1, 1, 0, 0]
        assert row["C"]["betti"] == [1, k+1, 0, 0]
        assert row["N"]["chi"] == k and row["T"]["chi"] == 0
        assert row["endpoint_caps"]["chi"] == 2*k
        assert row["E"]["chi"] == -2*k
        assert row["boundary_C"]["chi"] == -2*k


def test_signs_alone_do_not_change_tube_only_relative_index(result):
    row = result["excision"][2]
    cases = row["positive_tubes_only_cusp_empty"]
    assert [c["relative"]["chi"] for c in cases] == [-2, -2, -2]
    assert [c["sign_only_claim"] for c in cases] == [-2, 2, 0]
    assert cases[1]["relative"]["betti"][0] == 1
    assert row["all_positive_tubes"]["betti"] == [0, 2, 0, 0]
    assert row["complementary_boundary"]["betti"] == [0, 0, 2, 0]


def test_singular_affine_linear_part_is_not_a_fixed_point_count(result):
    rows = result["affine"]
    assert rows["identity"]["grid_counts"] == [16, 64]
    assert rows["half_translation"]["grid_counts"] == [0, 0]
    assert rows["reflection"]["grid_counts"] == [8, 16]
    assert rows["free_glide"]["grid_counts"] == [0, 0]
    for name in ("inversion", "shifted_inversion"):
        assert rows[name]["grid_counts"] == [4, 4]
    assert rows["order_three"]["grid_counts"] == [3, 3]


def test_cusp_swap_is_not_a_self_map_but_rotation_on_same_cusp_is():
    A = [[0, -1], [1, -1]]
    assert b.cusp_interpretation(A, 0, 0)["count"] == 3
    assert b.cusp_interpretation(A, 0, 1)["count"] is None
    assert b.cusp_interpretation([[1, 0], [0, 1]], 0, 0)["count"] is None


def test_actual_snappy_witnesses_preserve_cusp_targets(result):
    manifolds = result["snappy"]["manifolds"]
    M = manifolds["m004"]
    assert M["orientable"] and M["cusps"] == 1 and M["symmetry_order"] == 8
    assert len(M["generators"]) == 2 and len(M["relators"]) == 1
    for manifold in manifolds.values():
        for iso in manifold["isometries"]:
            for row in iso["peripheral"]:
                if row["source"] != row["target"]:
                    assert row["interpretation"]["count"] is None
                elif row["raw_abs_det_minus_I"]:
                    assert row["interpretation"]["count"] == row["raw_abs_det_minus_I"]


def test_provenance_is_explicit_and_distinct(result):
    assert len(result["source_receipts"]) == 6
    assert len({r["commit"] for r in result["source_receipts"]}) == 3
    assert all(len(r["sha256"]) == 64 for r in result["source_receipts"])
