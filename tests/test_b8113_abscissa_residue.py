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


def test_the_flat_claim_is_retracted_not_quietly_dropped():
    """First pass stopped at 5.0 and called the increments flat. The 5.5 point retracts that."""
    assert "RETRACTED" in R["flat_claim_retracted"]
    assert "TWO-POINT ARTIFACT" in R["flat_claim_retracted"]
    assert R["S2_increments_relative_change"] > 0.05


def test_s2_decays_like_one_over_L_and_s3_geometrically():
    """The replacement reading, and it is stronger than the one it replaces."""
    assert abs(R["S2_increment_ratio"] - R["log_divergence_predicted_ratio"]) < 0.15
    assert R["S3_increment_ratio"] > 1.3 * R["S2_increment_ratio"]
    assert R["S2_last_two_increments"][1] > 100 * R["S3_last_two_increments"][1]


def test_pfaff_is_not_required_for_the_assembly():
    """The correction cutting the other way: the geodesic product comes from the spectrum."""
    assert R["pfaff_is_required_for_the_assembly"] is False


def test_no_divergence_is_claimed():
    assert "does NOT prove divergence" in R["scope"]
    assert "conditionally" in R["verdict"].lower()
    assert "OPEN STEP" in R["verdict"]
