"""B1031 locks — the generation thread's grade, its bounding theorem, and the rung that was missing.

Every assertion re-reads a banked verdict or a curated surface at test time, so a later edit moves
the lock rather than only the prose (WORKING_RULES rule 7).
"""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location(
    "b1031", _ROOT / "frontier" / "B1031_generation_rung" / "verify.py")
v = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(v)


def test_every_check_in_the_audit_passes():
    failed = [k for k, c in v.R["checks"].items() if not c["pass"]]
    assert failed == [], failed


def test_the_grade_is_STRUCTURAL_and_that_word_means_a_named_debt():
    """The answer to 'do we derive three generations'. THE_CLAIM reserves DERIVED for the ℤ₆ form
    and hypercharge; generations get STRUCTURAL, which the same section defines as a named debt."""
    assert v.R["checks"]["the_claim_grades_the_generation_structure_STRUCTURAL"]["pass"]
    assert v.R["checks"]["the_claim_defines_STRUCTURAL_as_a_named_debt"]["pass"]
    assert v.R["checks"]["the_claim_reserves_DERIVED_for_z6_and_hypercharge"]["pass"]
    assert v.R["checks"]["the_spec_ledger_grades_it_structural_count_matches"]["pass"]


def test_the_positive_is_two_independent_computations_of_three():
    """B632's h¹ = 3 and B897's three 9-blocks. Neither is rhetoric; both are banked PROVED."""
    assert v.verdict("B632")[0] == "PROVED"
    assert v.verdict("B897")[0] == "PROVED"
    assert v.R["checks"]["b632_computes_h1_equals_three"]["pass"]


def test_the_three_sheets_are_exactly_degenerate_by_isometry():
    """B335 — the deck transformation is an isometry, so any mass is exactly degenerate and a
    hierarchy is its BREAKING. This is what makes 'structural' stronger than it sounds."""
    assert v.R["checks"]["b335_makes_the_three_sheets_exactly_degenerate"]["pass"]


def test_the_single_object_route_is_closed_by_theorem_not_by_failure():
    """B307 (= claim P54) plus B298's seven routes. The bound is a theorem with a named
    mechanism, which is why the rung is BOUNDED rather than a HOLE."""
    assert v.verdict("B307")[0] == "PROVED"
    assert v.verdict("B298")[0] == "NEGATIVE"
    assert v.R["checks"]["b307_closes_the_single_object_route"]["pass"]
    assert "P54" in (_ROOT / "CLAIMS.md").read_text(encoding="utf-8")


def test_registerability_presupposes_the_generation_structure():
    """The circularity that must travel with any 'the cascade lands on the SM' sentence."""
    assert v.R["checks"]["registerable_is_defined_as_the_generation_structure_surviving"]["pass"]
    assert v.R["checks"][
        "b994_states_registerability_IS_chirality_an_input_the_object_lacks"]["pass"]


def test_the_typing_wall_zeroes_the_identical_family_coupling():
    """Three slots exist; the Yukawa-type family tensor at that level does not."""
    assert v.R["checks"]["the_typing_wall_zeroes_the_coupling_for_identical_families"]["pass"]


def test_the_ladder_carries_the_generation_rung__the_repair():
    """THE FINDING, pinned. The word 'generation' appeared zero times in the file whose binding
    rule is 'if X is not on it, X has not been checked' — while 51 arcs speak to it."""
    assert v.R["checks"]["the_ladder_now_carries_a_generation_rung"]["pass"]
    assert v.R["checks"]["the_generation_rung_is_X33_in_the_BOUNDED_section"]["pass"]
    assert v.R["arcs_mentioning_generations"] > 40
    for token in ("B632", "B307", "B897", "B335", "B298"):
        assert v.R["checks"][f"the_rung_cites_{token}"]["pass"], token


def test_the_b302_check_is_scoped_so_the_repair_cannot_erase_its_own_finding():
    """The same measurement hazard as B1030 — and it fired TWICE inside this arc alone.

    'B302 is on no curated surface' passed before the repair; failed once the X33 rung cited B302;
    was scoped to exclude X33; then failed AGAIN once the LAW_MAP row cited B302 as well. The
    scope is now by AUTHORSHIP (drop the rows this arc wrote) rather than by location, which is
    the only version that survives adding a second row. Three instances in two arcs: a metric
    invalidated by its own output is the shape of the coverage error this refresh had to retract.
    """
    assert v.R["checks"]["b302_was_carried_by_no_curated_surface_before_this_arc"]["pass"]
    assert v.R["checks"]["b302_is_now_cited_by_this_arcs_rows"]["pass"]
