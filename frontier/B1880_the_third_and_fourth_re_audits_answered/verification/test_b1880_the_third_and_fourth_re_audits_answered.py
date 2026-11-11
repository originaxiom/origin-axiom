"""B1880 lock -- the advisor seat's third and fourth re-audits, reproduced and answered.

What could fail here: the seat's counts not being main's; a planted case of the seat having no test of its own name in the
suite; the measured state of the lists of hashed files drifting from the frozen table the gate pins; a raw hash that the tracked
gzip does not decompress to; a changed file that is not equal to its sealed version after a path repair or a redaction."""
import ast
import fnmatch
import gzip
import hashlib
import importlib.util
import json
import os
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


G = _load("gates_b1880_lock", ROOT / "scripts" / "gates" / "gates.py")
DATA = json.loads((HERE / "all_hash_lists.json").read_text(encoding="utf-8"))


def _tests_in(rel):
    tree = ast.parse((ROOT / rel).read_text(encoding="utf-8"))
    return {n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}


def test_the_seats_counts_are_mains():
    n = DATA["named_lists"]
    assert (n["entries"], n["lists"], n["do_not_verify"], n["distinct_keys"]) == (1497, 189, 67, 63)
    assert n["first_found"] == {"beside the list": 1137, "from the root": 338}                 # re-audit 3: 338 of the 1,497
    assert n["files_found_only_from_the_root"] == 177                                          # re-audit 3: 177 files
    assert n["candidate_entries"] == 21 and n["candidate_entries_from_the_root"] == 19
    assert len(n["candidate_files_no_other_list_reads"]) == 8                                  # re-audit 3: eight of the candidate's 21
    assert any(f.endswith("exact_end_web_seat.py") for f in n["candidate_files_no_other_list_reads"])
    assert n["frozen_script_entries_that_do_not_verify"] == 23 and n["frozen_scripts_that_do_not_verify"] == 21


def test_every_planted_case_of_the_two_re_audits_has_its_test_in_the_suite():
    """the seat's acceptance rows HASH-a, HASH-b, HASH-c, STATE-b, ATTR-a, ARR-a, ARR-b, and its corrected PV14"""
    want = {
        "tests/test_artifact_hashes.py": ["test_t3_a_copy_does_not_stand_in_for_the_file_a_seal_hashed", "test_t4_a_frozen_entry_that_changes_again_is_refused",
                                          "test_t7_a_seal_list_under_another_name_is_read", "test_a_list_under_another_name_cannot_be_edited_deleted_or_moved",
                                          "test_what_is_a_list_and_what_only_prints_a_hash"],
        "tests/test_attribution_history.py": ["test_a_trailer_on_a_commit_that_arrives_by_a_merge_is_refused", "test_a_foreign_author_on_a_commit_that_arrives_by_a_merge_is_refused"],
        "tests/test_arrival_phrases.py": ["test_the_advisor_seats_six_planted_sentences", "test_the_gate_is_green_on_this_repository_and_its_old_lines_are_frozen_by_key"],
        "tests/test_gate_failing_paths.py": ["test_arc_data_fails_on_a_verdict_file_that_cannot_be_read"],
        "tests/test_harvest_debt_gate.py": ["test_the_gates_sentence_names_every_seat_past_its_pin"],
        "frontier/B1861_the_closure_programme/verification/test_b1861_the_closure_programme.py": ["test_the_refusals_about_the_seats_verdicts_can_fire"],
    }
    for rel, names in want.items():
        have = _tests_in(rel)
        for name in names:
            assert name in have, (rel, name)


def test_the_measured_state_is_the_gates_and_the_frozen_table_is_the_one_pinned():
    """The measurement is of 2026-11-11 and is a file; the tree goes on taking new seals.  So the measured counts are checked as
    recorded, and the live state is held to what cannot move without a fault: nothing that verified then is missing now, and
    what does not verify is exactly the frozen table.  (This lock first pinned the live counts; the next sealed card, a day
    later, added a list and failed it.)"""
    a = DATA["all_lists"]
    assert (a["lists"], a["under_another_name"], a["entries"]) == (269, 80, 2247)
    assert a["states"]["VERIFIES"] == 1826 and "AMBIGUOUS" not in a["states"]
    assert a["under_another_name_states"]["VERIFIES"] == 396 and a["under_another_name_states"]["MISMATCH"] == 144
    assert a["under_another_name_states"].get("ABSENT", 0) + a["under_another_name_states"].get("NOT TRACKED", 0) == 210       # a clone has no untracked files
    assert a["lowest_share_among_lists"] == 0.375 > G.HASH_LIST_MIN_SHARE > 0.06 >= a["highest_share_among_files_that_are_not_lists"]      # 6 lines of 16, against 1 of 17
    state = G.hash_list_state()
    lists = {e[1] for e in state}
    other = {l for l in lists if not fnmatch.fnmatch(os.path.basename(l), G.ARTIFACT_HASH_GLOB)}
    assert len(lists) >= 269 and len(other) >= 80 and len(state) >= 2247
    assert sum(1 for e in state if e[3] == "VERIFIES") >= 1826 and not [e for e in state if e[3] == "AMBIGUOUS"]
    table = G.hash_lists_frozen()
    assert table is not None and len(table) == DATA["frozen_table"]["keys"] == 417
    assert hashlib.sha256((ROOT / G.HASH_LISTS_FROZEN_FILE).read_bytes()).hexdigest() == DATA["frozen_table"]["sha256"] == G.HASH_LISTS_FROZEN_SHA256
    broken = {e[0]: e[4] for e in state if e[3] != "VERIFIES"}
    assert broken == table                                    # every entry that does not verify is in the table with its state, and nothing else is
    ok, why = G.gate_artifact_hashes()
    assert ok and "the table holds 417" in why and "of the lists are under another name" in why, why


def test_the_two_entries_declared_by_name_each_mean_the_file_beside_their_list():
    amb = [e for e in G.hash_list_state(_resolved={}) if e[3] == "AMBIGUOUS"]
    assert sorted(e[0] for e in amb) == sorted(G.HASH_LIST_RESOLVED) and len(amb) == 2
    for key, path in G.HASH_LIST_RESOLVED.items():
        lst = next(e[1] for e in amb if e[0] == key)
        assert os.path.dirname(path) == os.path.dirname(lst)                 # the arc's own copy, beside its list
    assert all(e[3] == "VERIFIES" for e in G.hash_list_state() if e[0] in G.HASH_LIST_RESOLVED)


def test_the_entries_under_other_names_that_do_not_verify_are_classed_and_nine_are_read():
    o = DATA["other_names_not_verifying"]
    assert o["classes"] == {"A": 7, "B": 2, "C": 135, "D": 22, "E": 188} or (
        o["classes"]["A"] == 7 and o["classes"]["B"] == 2 and o["classes"]["C"] == 135 and o["classes"].get("D", 0) + o["classes"].get("E", 0) == 210)
    assert sorted({r["file"].split("/")[1].split("_")[0] for r in o["class_A"]}) == ["B666", "B756"]
    assert sorted({r["file"].split("/")[1].split("_")[0] for r in o["class_B"]}) == ["B1298", "B879"]
    run = (HERE / "read_class_a_run.txt").read_text(encoding="utf-8")
    assert "files: 9; equal to their sealed version after the substitutions: 9" in run
    assert run.count("equal after the path and attribution substitutions: True") == 9 and "NOT ALL EQUAL" not in run
    # and it is recomputed here, not only read: the mechanical reading passes on today's files
    assert _load("read_class_a_b1880", HERE / "read_class_a.py").main() is True


def test_the_three_raw_hashes_are_the_tracked_gzips_decompressed():
    raw = DATA["raw_hashes_checked_against_the_tracked_gzip"]
    assert len(raw) == 3 and all(r["decompresses_to_the_recorded_hash"] for r in raw)
    assert sum("B1798_" in r["tracked_gzip"] for r in raw) == 2                 # two of them in an arc of the candidate's chain
    r = next(r for r in raw if "B1786_" in r["tracked_gzip"])                   # one recomputed here (the smallest)
    want = next(G._hash_list_entry(l.strip())[0] for l in (ROOT / r["list"]).read_text(encoding="utf-8").split("\n") if G._hash_list_entry(l.strip()))
    assert hashlib.sha256(gzip.open(ROOT / r["tracked_gzip"], "rb").read()).hexdigest() == want


def test_the_ceilings_gate_as_mended():
    sents = G.arrival_sentences()
    assert len(sents) == 3 and {k for k, *_ in sents} == set(G.ARRIVAL_FROZEN)
    pages = G._arrival_files(str(ROOT))
    assert len(pages) > 500 and any(p.endswith(".tex") for p in pages) and any(p.startswith("docs/progress/") for p in pages)
    assert not G._ARRIVAL_NEG_RE.search(" we claim that ") and G._ARRIVAL_NEG_RE.search(" our aim is that ")
    assert not G._ARRIVAL_NEG_RE.search(" a minor point: ") and not G._ARRIVAL_NEG_RE.search(" nonetheless ")
    assert len(G.ARRIVAL_PHRASES) == 16


def test_the_programme_holds_the_two_re_audits():
    prog = json.loads((ROOT / "frontier" / "B1861_the_closure_programme" / "PROGRAMME.json").read_text(encoding="utf-8"))
    assert prog["reaudits"] == {"REAUDIT_2_2026-11-10.md": ["b5034197b", "ab97082c0"], "REAUDIT_3_2026-11-11.md": ["6ab743907", "b28dceea8"], "REAUDIT_4_2026-11-11.md": ["58ae45c70", "015be0cc7"]}
    st = prog["stats"]
    assert st["fixed_and_not_yet_re_audited"] == [] and st["findings_with_a_re_audit_verdict"] == 15
    assert st["findings_main_changed_since_the_re_audit"] == ["E4", "E8", "G2", "G9", "X1"]
    f = prog["findings"]
    fixed = sorted(k for k, v in f.items() if v["state"] == "FIXED")
    assert fixed == sorted(["G1", "G2", "G3", "G4", "G9", "E3", "E6", "E10", "E13", "L5", "X1"])
    assert all(prog["accepted"][k].startswith("accepted") for k in fixed)
    assert f["G14"]["state"] == "PARTLY FIXED" and f["E3"]["state"] == "FIXED"


def test_the_record_carries_the_harvest_and_the_arc():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1880" and v["verdict"] == "PROVED" and v["claim_one_line"].endswith("0 of 19.")
    led = (ROOT / "docs" / "HARVEST_LEDGER.md").read_text(encoding="utf-8")
    assert "REAUDIT_3_2026-11-11.md" in led and "REAUDIT_4_2026-11-11.md" in led and "`58ae45c7`" in led
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("## Seen first", "## Disclosed", "## Reproduce", "0 of 19", "eight hours late"):
        assert s in f
