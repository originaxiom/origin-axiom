"""B8113 -- locks the abscissa residue, read from results.json."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = json.load(open(os.path.join(ROOT, "frontier", "B8113_abscissa_residue", "results.json")))


def test_item5_has_three_residues_not_one():
    assert len(R["item5_residues"]) == 3


def test_the_graviton_product_starts_at_the_abscissa():
    assert R["graviton_product_starts_at_n"] == R["abscissa_of_absolute_convergence"] == 2


def test_positive_control_the_instrument_can_see_convergence():
    """s = 3 is strictly inside the half-plane; its increments MUST decay."""
    assert R["S3_increments_decay_monotonically"] is True
    a, b = R["S3_last_two_increments"]
    assert a / b > 1.4


def test_s2_increments_are_flat_where_s3_decays():
    assert R["S2_increments_flat_within"] < 0.01
    assert R["S2_last_two_increments"][1] > 100 * R["S3_last_two_increments"][1]


def test_pfaff_is_not_required_for_the_assembly():
    """The correction cutting the other way: the geodesic product comes from the spectrum."""
    assert R["pfaff_is_required_for_the_assembly"] is False


def test_no_divergence_is_claimed():
    assert "does NOT prove divergence" in R["scope"]
    assert "conditionally" in R["verdict"].lower()
    assert "OPEN STEP" in R["verdict"]
