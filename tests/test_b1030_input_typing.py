"""B1030 locks — the counted input list's typing and its membership collision.

These re-run the audit rather than asserting its transcript (WORKING_RULES rule 7): every
assertion below reads a banked artifact or a curated surface at test time, so a later edit to
`THE_CLAIM`, B1000's census or B1015's declaration moves the lock, not just the prose.
"""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location(
    "b1030", _ROOT / "frontier" / "B1030_input_typing_audit" / "verify.py")
v = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(v)


def test_every_check_in_the_audit_passes():
    failed = [k for k, c in v.R["checks"].items() if not c["pass"]]
    assert failed == [], failed


def test_the_count_of_continuous_dimensionless_inputs_is_one_not_zero():
    """The owner's question, answered against B1015's sealed declaration.

    Four of the five counted inputs ARE dimensionless; all four are DISCRETE. The count that
    "parameter-free" is about — CONTINUOUS dimensionless inputs — is exactly one: A2 = c = 6*sigma,
    an anchor. L154 would take it to zero. Until then the stronger reading is not banked.
    """
    assert len(v.typing["dimensionless_CONTINUOUS"]) == 1
    assert len(v.typing["dimensionless_DISCRETE"]) == 4
    assert len(v.typing["dimensionful"]) == 1
    assert "the one continuous dimensionless input is A2" in v.flat(v.DECL)


def test_tier4_parameter_free_is_not_done_and_no_arc_may_claim_it():
    assert v.R["checks"]["tier4_parameter_free_is_graded_NOT_DONE"]["pass"]
    assert v.R["checks"]["no_arc_may_claim_parameter_free"]["pass"]


def test_b1000_grades_three_inputs_as_artifacts_not_closings():
    """The exact extent of 'every input anchors what the object cannot contain': four sectors,
    five closings — and three imports that are ours and reducible in principle."""
    assert v.B1000["artifacts"] == ["the 6d type", "the filling slope", "P5 menu completeness"]
    assert len(v.B1000["closings"]) == 5
    assert v.B1000["incompletenesses_closed"] == 4
    assert v.B1000["classification"]["the 6d type"][0] == "ARTIFACT"


def test_the_two_fives_have_the_same_size_and_different_membership():
    """THE FINDING. Not a counting error — a membership claim asserted as agreement."""
    assert "the 6d type" in v.B1000["artifacts"]          # THE_CLAIM lists it as a hypothesis
    assert "4d / the N=2->N=1 datum" in v.B1000["closings"]  # THE_CLAIM lists it nowhere
    assert v.in_claim["the 6d type"]
    assert v.R["checks"]["the_two_fives_are_different_fives"]["pass"]


def test_the_agreement_was_asserted_in_both_places():
    """B1017 wrote the list and closed 'B1000's five-closings census (confirmed)'; THE_CLAIM
    repeats 'B1000's census of five closings stands'. Both are membership claims."""
    assert "B1000's five-closings census (confirmed)" in v.flat(v.B1017)
    assert v.R["checks"]["the_claim_asserts_b1000s_five_closings_stand"]["pass"]
    assert v.R["checks"]["b1017s_resource_table_assigns_no_resource_to_space"]["pass"]


def test_the_claim_states_one_count_not_two():
    """The repaired drafting defect: 'four typed external data' in the quoted one-sentence claim
    against 'five' in §1, B1017's correction having reached only the paragraph."""
    assert "four typed external data" not in v.CLAIM
    assert "five typed external data" in v.CLAIM.split("The one-sentence claim")[-1]


def test_the_space_check_is_scoped_so_this_arc_cannot_erase_its_own_finding():
    """MB-shaped guard on the measurement itself.

    A whole-file search for the space closing passed before this arc and FAILED after it, because
    the arc wrote the finding into the file it was searching. The same shape as the coverage error
    this refresh already retracted: a metric invalidated by its own output. The check is scoped to
    the hypothesis list and to the body before the B1030 note, and both must hold.
    """
    assert v.R["checks"]["the_claim_hypothesis_list_names_no_space_closing"]["pass"]
    assert v.R["checks"]["the_claim_body_named_no_space_closing_before_this_arc"]["pass"]
    # and the note itself must be present — the finding is recorded on the surface it concerns
    assert "4d lift / N=2→N=1 datum" in v.CLAIM


def test_the_defined_term_for_the_widest_quantifier_is_where_the_findings_say():
    p = (_ROOT / "docs" / "COMPUTE_THE_PROGRAM.md").read_text(encoding="utf-8")
    assert "compute over the object as FULL RELATIONS, never as a single manifold" in p
    assert "quantifier instruction" in p
    for layer in ("the member", "the ends", "the class", "the sisters", "the rows",
                  "the child", "the faces", "the axioms", "the algebra", "the observer"):
        assert f"**{layer}**" in p, layer
