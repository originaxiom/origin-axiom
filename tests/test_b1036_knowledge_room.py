"""B1036 locks — the knowledge room: the firewall breaches, the gate holes, and the clean sweep."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location(
    "b1036", _ROOT / "frontier" / "B1036_knowledge_room" / "verify.py")
v = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(v)
N = v.R["numbers"]


def test_every_check_passes():
    failed = [k for k, c in v.R["checks"].items() if not c["pass"]]
    assert failed == [], failed


def test_the_contradiction_hunt_is_clean__the_positive_result():
    """No registered retracted phrase appears anywhere in the room. Banked as loudly as any
    defect, because it is the outcome the sweep was built to falsify."""
    c = v.R["checks"]["NO_retracted_phrase_appears_anywhere_in_the_room"]
    assert c["pass"] and c["hits"] == [] and c["n_phrases_checked"] >= 5


def test_the_rooms_no_premise_rule_has_no_gate_behind_it():
    """firewall-oneway tests exactly speculations/, philosophy/, story/. knowledge/ is not one."""
    assert v.R["checks"]["the_room_forbids_being_used_as_a_premise"]["pass"]
    assert v.R["checks"]["but_the_firewall_gate_does_not_cover_this_room"]["pass"]


def test_an_explainer_carries_a_THEOREM_grade_on_the_law_register():
    """LAW_MAP:149 — K020 names the row, authorises the grade, and precedes the arc B642."""
    c = v.R["checks"]["BREACH_1_an_explainer_carries_a_THEOREM_grade_on_the_law_register"]
    assert c["pass"] and c["grade"] == "**THEOREM** (K020)"


def test_a_sealed_preregistration_cites_an_explainer_as_its_authority():
    """SEAL_LEDGER:461 — the sharpest, because a sealed document cannot be amended."""
    assert v.R["checks"][
        "BREACH_2_a_SEALED_preregistration_cites_an_explainer_as_its_authority"]["pass"]


def test_the_gate_counts_a_mention_not_a_row_and_cannot_see_the_ungated_docs():
    assert v.R["checks"]["HOLE_1_the_gate_counts_a_mention_not_a_row"]["pass"]
    assert v.R["checks"]["HOLE_2_unnumbered_room_documents_are_invisible_to_the_gate"]["pass"]
    assert len(N["unnumbered_docs"]) == 2


def test_the_factor_of_two_between_the_two_ungated_documents():
    """A fifth E1, recomputed rather than quoted: A has eigenvalue phi^2, so h_top = 2 log phi,
    and the other document's 4 log phi is exactly twice it. A convention gap (positive Lyapunov
    exponents vs the sum of absolute values), declared by neither. Shape of B62 = 2 x P33."""
    c = v.R["checks"]["and_the_arithmetic_is_exact__4logphi_is_twice_log_of_A_s_eigenvalue"]
    assert c["pass"] and abs(c["quoted"] - 2 * c["h_top_of_A"]) < 1e-12


def test_K021s_generation_grade_is_corrected_against_its_own_open_gate():
    assert v.R["checks"]["K021_says_the_object_FORCES_three_generations"]["pass"]
    assert v.R["checks"]["while_its_own_section_8_lists_that_step_as_an_OPEN_gate"]["pass"]
    k021 = next(p for p in (_ROOT / "knowledge").glob("K021_*.md"))
    assert "STRUCTURAL, not forced" in k021.read_text(encoding="utf-8")


def test_standard_background_does_not_decay_but_the_rest_does():
    """The split that governs any currency reading of this room; reporting one number without it
    would repeat the error B1030 filed against THE_CLAIM vs B1000."""
    assert v.R["checks"]["standard_entries_old_anchors_are_NOT_evidence_of_decay"]["pass"]
    assert N["own_or_mixed"] == 19 and N["median_own_newest_anchor"] < 300


def test_the_size_statements_and_the_currency_pointer_are_repaired():
    assert v.R["checks"]["all_three_size_statements_now_match_the_room"]["pass"]
    assert v.R["checks"]["the_current_headline_label_is_gone_from_the_proven_register"]["pass"]
    assert v.R["checks"]["the_index_is_now_one_contiguous_table_with_no_orphan_rows"]["pass"]


def test_freshness_is_measured_with_this_arcs_own_lines_removed():
    """Ninth instance of one hazard, and the sharpest: repairing the index moved the very
    number that motivated the repair (the new K026 row carries B917 against an old max of B483)."""
    assert v.R["checks"]["knowledge_INDEX_is_the_oldest_of_the_nine_sweep_surfaces"]["pass"]
    assert N["sweep_surface_freshness"]["knowledge/INDEX.md"] < 600
