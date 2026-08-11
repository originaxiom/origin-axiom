"""B1032 locks — the across-breakings route, and the withdrawal of B1031's "only one" clause."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location(
    "b1032", _ROOT / "frontier" / "B1032_across_breakings_route" / "verify.py")
v = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(v)


def test_every_check_in_the_audit_passes():
    failed = [k for k, c in v.R["checks"].items() if not c["pass"]]
    assert failed == [], failed


def test_the_route_rests_on_two_sealed_cells():
    assert v.R["checks"]["b890_is_a_sealed_cell_returning_DISTINCT"]["pass"]
    assert v.R["checks"]["b891_is_a_sealed_cell_returning_DISTINCT"]["pass"]
    for b in v.CLUSTER:
        assert v.verdict(b)[0] == "PROVED", b


def test_b890_banked_against_its_own_disclosed_prior():
    """The programme's strongest evidence shape: prereg said EQUAL, the computation said DISTINCT,
    and the arc says so in its own heading."""
    assert v.R["checks"]["b890_banked_against_its_disclosed_prior"]["pass"]
    assert v.R["checks"]["b890_states_the_operational_point"]["pass"]


def test_both_sealed_cells_keep_the_same_fence():
    """Registerable distinctness is not mechanism-hood. Neither cell claims more, and the rung
    must not either."""
    assert v.R["checks"]["B890_keeps_the_solo_seats_fence"]["pass"]
    assert v.R["checks"]["B891_keeps_the_solo_seats_fence"]["pass"]
    assert v.R["checks"]["x33_keeps_the_fence_that_both_sealed_cells_declared"]["pass"]


def test_b307_does_not_reach_this_route():
    """B307 forbids a TRACE-FIELD route in a single knot. Nothing in the cluster is a trace-field
    statement, so its hypothesis does not apply — which is why 'the only one' was false."""
    assert v.R["checks"]["b307_scopes_itself_to_the_trace_field_of_a_single_knot"]["pass"]
    assert v.R["checks"]["the_cluster_makes_no_trace_field_claim"]["pass"]


def test_the_only_one_clause_is_withdrawn_and_two_routes_are_named():
    """THE CORRECTION, pinned: B1031 wrote 'the only one B307 leaves open' one arc earlier."""
    assert v.R["checks"]["the_withdrawn_only_one_sentence_is_gone"]["pass"]
    assert v.R["checks"]["x33_now_names_two_routes"]["pass"]
    assert v.R["checks"]["x33_now_cites_the_cluster"]["pass"]


def test_the_foundation_is_curated_but_what_is_built_on_it_is_not():
    """The sharper shape, and itself a correction: the first draft said all four were absent.
    B885 holds a LAW_MAP row and a THEOREM_LEDGER entry; B889/B890/B891 held nothing."""
    assert v.R["checks"]["the_foundation_B885_IS_curated"]["pass"]
    assert v.R["checks"][
        "the_three_arcs_built_on_it_were_curated_absent_before_this_arc"]["pass"]
    assert v.R["checks"]["nor_under_any_of_six_topic_names"]["pass"]
    assert v.R["checks"]["but_the_generated_tier_carries_it"]["pass"]


def test_the_measurement_is_scoped_by_authorship():
    """Fourth instance of one hazard in three arcs: recording a gap creates the citation that
    makes the gap look closed. THE_LADDER's own X31 row already knew it."""
    assert v.R["checks"]["and_this_arc_is_what_puts_it_on_a_curated_surface"]["pass"]
    ladder = (_ROOT / "docs" / "THE_LADDER.md").read_text(encoding="utf-8")
    assert "Registering a gap creates hits for the gap" in ladder.replace("\n", " ")
