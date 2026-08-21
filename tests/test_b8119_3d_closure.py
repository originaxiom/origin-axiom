"""B8119 -- locks the closure audit: every row disposed, novelty disclaimed, residues named."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = json.load(open(os.path.join(ROOT, "frontier", "B8119_3d_closure", "results.json")))


def test_all_eleven_rows_are_disposed():
    assert len(R["rows"]) == 11
    assert R["rows_still_open"] == []
    assert not any(r["now"] in ("PARTIAL", "AMBIGUOUS", "MISSING") for r in R["rows"])


def test_the_state_integral_row_moved_because_b787_was_never_searched():
    row = next(r for r in R["rows"] if r["row"] == "state integral")
    assert row["b8099"] == "PARTIAL" and row["now"] == "PRESENT"
    assert R["b8099_mentions_b787"] == 0
    assert R["b787_phi_validated"] is True
    assert float(R["b787_saddle_check"]) < 1e-30


def test_the_saddle_is_the_volume_and_the_volume_is_an_L_value():
    v = float(R["saddle_volume"])
    assert abs(v - 2.029883212819307) < 1e-13
    assert abs(v - float(R["snappy_volume"])) < 1e-13
    assert abs(v - float(R["vol_as_L_value"])) < 1e-9


def test_the_one_loop_is_NOT_assembled_and_its_residues_are_named():
    assert R["one_loop_assembled"] is False
    assert len(R["one_loop_residues"]) == 3
    joined = " ".join(R["one_loop_residues"]).lower()
    for key in ("continuous spectrum", "graviton determinant", "abscissa"):
        # matched case-insensitively: the prose capitalises for emphasis, the lock tracks content
        assert key in joined


def test_novelty_is_disclaimed():
    assert R["novelty_claimed"] is False
    assert "does NOT re-derive" in R["scope"] or "Claims no novelty" in R["scope"]


def test_definition_complete_but_that_is_a_scoped_claim():
    assert R["definition_complete"] is True and R["parameter_free"] is True
    # the claim must not be stated without the quantum caveat riding with it
    assert "NOT assembled" in R["verdict"]


def test_the_precision_truncation_hazard_is_recorded():
    h = R["snappy_str_truncation_caught"]
    assert "FALSE FAIL" in h and "manufactures a negative" in h
