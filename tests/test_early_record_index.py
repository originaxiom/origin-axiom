"""The early record's subject index (Foundation Lock, Stage 1): every arc from B1 to B500 sits under a subject, every
listed arc exists, the page is current -- and the check can fail."""
import importlib.util, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("early_record_index", os.path.join(ROOT, "scripts", "checks", "early_record_index.py"))
eri = importlib.util.module_from_spec(spec); spec.loader.exec_module(eri)


def test_every_early_arc_is_under_a_subject_and_the_page_is_current():
    text, unassigned, missing = eri.build()
    assert unassigned == [] and missing == []
    assert open(eri.PAGE).read() == text, "run scripts/checks/early_record_index.py"
    assert len(eri.early()) >= 480 and len(eri.SUBJECTS) >= 15


def test_the_check_can_fail_both_ways():
    rows = eri.early() + [dict(id="B499", dir="B499_planted", verdict="OPEN", claim="planted", title="")]
    rows.append(dict(id="B12", dir="B12_planted_unassigned", verdict="OPEN", claim="planted", title=""))
    _, unassigned, _ = eri.build(rows)
    assert unassigned == [12], "an arc in no subject is named"
    _, _, missing = eri.build([r for r in eri.early() if eri.number(r["id"]) != 14])
    assert ("genesis", 14) in missing, "a listed arc that is not in the record is named"


def test_the_text_is_the_arcs_own_line_not_retyped():
    import json
    v = json.load(open(os.path.join(ROOT, "frontier", "B14_half_step_square_root_selector", "arc_verdict.json")))
    assert v["claim_one_line"][:120].replace("|", "/") in open(eri.PAGE).read()


def test_the_subjects_a_keyword_sweep_misses_are_there():
    keys = {k for k, *_ in eri.SUBJECTS}
    assert {"genesis", "multi-state", "dynamics", "scale", "seed-selection"} <= keys
    multi = next(nums for k, _, _, nums in eri.SUBJECTS if k == "multi-state")
    assert {131, 172, 174, 191, 471} <= set(multi), "the early gluing and weaving arcs are under 'more than one object'"
