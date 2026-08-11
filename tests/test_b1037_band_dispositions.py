"""B1037 locks — the first band dispositioned, and the body-read payoff."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location(
    "b1037", _ROOT / "frontier" / "B1037_band_B100_dispositioned" / "verify.py")
v = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(v)
N = v.R["numbers"]


def test_every_check_passes():
    failed = [k for k, c in v.R["checks"].items() if not c["pass"]]
    assert failed == [], failed


def test_the_debt_number_counts_rows_but_the_debt_is_laws():
    """THE FINDING: 37 rows are 27 arcs in 7 clusters plus 10 standalone = 17 statements owed.
    If the ratio holds corpus-wide, the row count is not a work estimate."""
    assert N["band_rows"] == 37
    assert N["clustered_rows"] == 27 and len(N["clusters"]) == 7
    assert N["statements_owed"] == 17


def test_the_clusters_are_the_arcs_own_claim_not_an_editorial_grouping():
    assert v.R["checks"]["B122_says_it_and_B121_are_one_object"]["pass"]
    assert v.R["checks"]["B117_says_it_supersedes_B111_and_B113"]["pass"]


def test_B123_is_a_retraction_not_a_restoration():
    """The one outcome a consolidation pass must never produce. A claim-line sweep would have
    marked this PROVED, uncited arc for restoration; the body says B125 refuted it."""
    assert v.R["checks"]["B123_is_in_the_debt_set"]["pass"]
    assert v.R["checks"]["but_B125_retracts_B123s_sub_claim"]["pass"]
    assert v.R["checks"]["and_it_records_B123_as_a_RETRACTION_not_a_restoration"]["pass"]


def test_the_entropy_misattribution_is_sharper_than_a_convention_gap():
    """B1036 diagnosed a factor of two as an undeclared convention. B109's body shows the number
    is the TRACE MAP's rate at the void, while the room document calls it the CAT MAP's metric
    entropy — and h_top(A) is 2 log phi, recomputed here."""
    assert abs(N["h_top_A"] - N["four_log_phi"] / 2) < 1e-12
    for k in ("the_cat_maps_entropy_is_2_log_phi",
              "B109_computes_4_log_phi_for_the_TRACE_MAP_at_the_void",
              "the_room_doc_attaches_that_number_to_the_CAT_MAP_and_calls_it_its_metric_entropy",
              "and_the_same_row_names_the_void_as_the_linearisation__which_is_B109s_object"):
        assert v.R["checks"][k]["pass"], k


def test_the_campaigns_step_six_is_actually_executed():
    """The ledger no longer says 'None applied' for this band."""
    assert v.R["checks"]["the_ledger_no_longer_says_no_dispositions_applied"]["pass"]
    assert v.R["checks"]["the_band_section_exists_with_the_three_dispositions"]["pass"]
