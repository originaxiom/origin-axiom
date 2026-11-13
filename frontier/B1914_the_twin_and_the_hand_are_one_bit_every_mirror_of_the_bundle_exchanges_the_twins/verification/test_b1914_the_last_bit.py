"""B1914's lock. It runs the census again (it writes nothing), checks each claim, plants three faults that must be caught,
and holds the page to the kept run."""
import sys, json, pathlib, itertools
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_last_bit as W
PAGE = " ".join((HERE.parent / "FINDINGS.md").read_text(encoding="utf-8").split())
R = W.run()
SL = [((a, b), (c, d)) for a, b, c, d in itertools.product(range(5), repeat=4) if (a * d - b * c) % 5 == 1]


def separating(p, q):
    return sum(1 for X in SL if W.fixed(X, 5).get(p) != W.fixed(X, 5).get(q))


def test_the_ground_fixes_only_the_pair_at_order_5():
    assert R["a_orders_with_a_fixed_line"] == [5]
    assert R["a_at_5"] == {"1,2": -1, "2,4": -1}


def test_no_history_separates_the_two_points_and_the_check_can_fail():
    assert R["b_elements_separating_the_two_points"] == 0 and R["b_SL2_F5_size"] == 120
    assert R["b_words_agreeing"] == R["b_words_up_to_14"] == 32766
    assert separating((1, 2), (2, 4)) == 0
    assert separating((1, 2), (1, 3)) > 0                       # planted: two points not on one line ARE separated
    assert R["b_LaR_fixing"] == [1, 6, 11, 16, 21, 26] and R["b_run6_periods_signs"] == [1, -1, 1]
    assert R["plant_swapped_run6_fixes_v1"] is False            # planted: the swapped convention loses the line


def test_the_mirror_and_only_the_mirror_exchanges_them():
    assert R["c_full_search_equals_families_within_12"] and R["c_every_symmetry_keeps_the_eigenline"]
    assert R["c_all_found_are_pm_Jn_or_pm_JnK"]
    assert R["c_preserving_scalars"] == [1, 4] and R["c_reversing_scalars"] == [2, 3]
    assert R["c_classes_modulo_A"] == 8 and R["c_classes_reversing"] == 4
    snap = R["c_snappy_4_1"]
    assert "skipped" in snap or (snap["order"] == 8 and snap["amphicheiral"])
    # planted: orientation read from det X alone (forgetting whether X inverts A) mixes the two scalar sets
    A = W.word("LR"); Ainv = W.inv(A)
    by_det = {}
    for a in range(-20, 21):
        for b in range(-20, 21):
            for X in (((a, b), (b, a - b)), ((a, b), (-a - b, -a))):
                if W.det(X) in (1, -1) and (W.mul(X, A) == W.mul(A, X) or W.mul(X, A) == W.mul(Ainv, X)):
                    by_det.setdefault(W.det(X), set()).add(W.scalar_on(X, (1, 2), 5))
    assert by_det[1] & {2, 3} and by_det[1] & {1, 4}


def test_two_classes_of_placements():
    orb = sorted(sorted(o) for o in R["d_orbits"])
    assert orb == [["+ hand, 2v", "- hand, v"], ["+ hand, v", "- hand, 2v"]]


def test_the_page_is_the_kept_run():
    k = json.loads((HERE / "the_last_bit.json").read_text(encoding="utf-8"))
    for key in ("a_orders_with_a_fixed_line", "b_elements_separating_the_two_points", "b_words_fixing_the_pair",
                "c_symmetries_found", "c_classes_modulo_A", "c_classes_reversing"):
        assert k[key] == R[key], key
    for s in ("32,766", "2,687", "of the 120 elements modulo 5, 10 keep the pair", "104", "eight classes, four of them reversing",
              "L⁶R", "+, −, +", "two classes"):
        assert s in PAGE, s
