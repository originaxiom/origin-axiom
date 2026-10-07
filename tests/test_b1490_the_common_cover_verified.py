"""B1490 -- LP01 verified: the level, the covers, the subgroup abelianisations, and the one failed prediction."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1490_the_common_cover_verified" / "verification"


def test_the_figure_eight_group_is_congruence_at_level_4_not_only_8():
    d = json.load(open(HERE / "level_recount.json"))
    assert d["2"]["PSL_index"] == 6 and d["4"]["PSL_index"] == 12 and d["8"]["PSL_index"] == 12 and d["level_4_index_12"]
    assert d["4"]["PSL_group"] == 1920 and d["4"]["PSL_image"] == 160
    c = json.load(open(HERE / "congruence_level.json")); assert c["level_4_given_index_12"] and not c["level_2"]
    k = json.load(open(HERE / "controls.json")); assert k["index_12_both"] and k["K_seat_conjugate_to_K_riley_mod4"]


def test_the_two_covers_match_the_seats_table_and_the_subgroups_abelianisations():
    o = json.load(open(HERE / "cover_o10_150726.json")); m = json.load(open(HERE / "cover_m202.json")); s = json.load(open(HERE / "subgroup_h1.json"))
    assert o["orbit_size"] == 4 and abs(o["cover"]["volume_over_m004"] - 20) < 1e-9 and o["cover"]["cusps"] == 6 and o["cover"]["H1"] == "Z/4 + Z + Z + Z + Z + Z + Z"
    assert o["isometries"]["total"] == 16 and o["isometries"]["chiral"] and not o["isometries"]["three"] and set(o["isometries"]["cusp_fixing_det_values"]) == {"0", "4"}
    assert m["orbit_size"] == 12 and abs(m["cover"]["volume_over_m004"] - 24) < 1e-9 and m["cover"]["cusps"] == 6 and m["cover"]["H1"] == "Z + Z + Z + Z + Z + Z + Z + Z"
    assert m["isometries"]["total"] == 12 and m["isometries"]["chiral"] and not m["isometries"]["three"]
    assert s["o10_150726"]["left_action_stabiliser"] == {"rank": 6, "torsion": [4]} and s["m202"]["left_action_stabiliser"] == {"rank": 8, "torsion": []}
    assert s["o10_150726"]["right_action_stabiliser"] == {"rank": 6, "torsion": [2]}       # the other stabiliser, which the sealed run built


def test_c4_failed_the_hexagonal_cusps_survive_on_one_cover():
    o = json.load(open(HERE / "cover_o10_150726.json"))
    hexagonal = [sh for sh in o["cusp_shapes"] if abs(float(sh.split("+")[0].replace(" ", "")) - 0.5) < 1e-6]
    assert len(hexagonal) == 4 and o["cover"]["cusps"] == 6
