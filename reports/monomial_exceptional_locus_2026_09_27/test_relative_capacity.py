from verify_relative_capacity import check_points


def test_all_fifth_root_cone_dimensions_in_both_families():
    rows = check_points()
    assert len(rows) == 4
    for row in rows:
        for side in ("E", "dual"):
            assert row[side]["relative_H1"] == 3
            assert row[side]["ordinary"][2] == 3


def test_combined_bounds_and_scope():
    bounds = [min(b, 3-b) for b in range(4)]
    assert bounds == [0, 1, 1, 0]
    assert max(bounds) == 1
    # This arithmetic uses a0=a0*=0 and fixed-meridian M6 holonomy I.
    # It is not asserted for the old unbalanced nonsplit witnesses.


def test_global_invariant_correction_is_not_dropped_at_finite_control():
    for row in check_points():
        if row["polynomial"] == ["1", "-1"]:
            for side in ("E", "dual"):
                entry = row[side]
                assert entry["ordinary"][0] == 1
                assert entry["interior"] == 1
                assert entry["relative_H1"]-entry["ordinary"][2] == 0
