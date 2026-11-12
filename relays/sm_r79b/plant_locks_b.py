#!/usr/bin/env python3
"""SM-R79b: the planted errors of SM-R79 run again against the five locks main mended, and new ones against the tripwire's
widened reading and its entries for E5 and for the level of a ground (B1884) (M5 on main's docs/seats/sm.md). Run against
a scratch clone of main checked out at 896cae025, never main itself.

Every plant carries its expectation (CAUGHT or MISSED), written and committed before the run, and its origin: "as before"
(SM-R79's plant unchanged), "re-aimed" (SM-R79's plant, its target text moved by the mend, the same error aimed at the
new text) or "new". The expectations are in plant_expectations.json, written by this script with --expectations only.

Usage: plant_locks_b.py CLONE OUT.json | plant_locks_b.py --expectations OUT.json

For each lock: the lock is first run unaltered and must pass, or its plants are not counted. Then each plant is applied to
the clone, the lock's own tests are run, and the clone is reset (git reset --hard; git clean -fdq; checked clean) before the next plant.
A plant is CAUGHT when the lock's run fails, MISSED when it passes. Each plant names the rule it breaks and its shape.
A plant whose edit could not be applied (its target text absent) is reported NOT APPLIED and not counted."""
import json
import os
import pathlib
import re
import subprocess
import sys

EXPECT_ONLY = sys.argv[1] == "--expectations"
CLONE = None if EXPECT_ONLY else pathlib.Path(sys.argv[1]).resolve()
OUT = pathlib.Path(sys.argv[2])
B1862 = "frontier/B1862_the_audits_first_corrections/verification/test_b1862_the_audits_first_corrections.py"
B1877 = "frontier/B1877_review_78_the_decadal_review/verification/test_b1877_review_78.py"
TRIP = f"{B1862}::test_no_place_still_carries_an_old_form_unmarked"
LOCKS = {   # the tripwire now holds E13's and E5's old forms (main, 2026-11-12), so it is part of those two locks
    "E13": [f"{B1862}::test_e13_twenty_distinct_eigenvalues_at_level_165", TRIP],
    "E6": [f"{B1862}::test_e6_the_kernel_is_computed_from_the_map"],
    "E10": [f"{B1862}::test_e10_the_arc_lookup_reads_its_argument"],
    "E3": [f"{B1862}::test_e3_the_charge_premise_splits", f"{B1862}::test_no_place_still_carries_an_old_form_unmarked",
           f"{B1877}::test_the_readers_corrections_stand_where_the_corrected_lines_stand"],
    "E5": ["tests/test_b892_walls_on_the_line.py", TRIP],
    "B1884": [TRIP],
}


class NotApplied(Exception):
    pass


def sh(*a, env=None):
    return subprocess.run(list(a), cwd=CLONE, capture_output=True, text=True, env=env)


def reset():
    sh("git", "reset", "-q", "--hard")   # also drops intent-to-add entries, which checkout keeps
    sh("git", "clean", "-fdq")
    left = sh("git", "status", "--porcelain").stdout.strip()
    if left:
        raise SystemExit("clone not clean after reset: " + left[:200])


def rd(rel):
    return (CLONE / rel).read_text(encoding="utf-8")


def wr(rel, text, add=False):
    p = CLONE / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    if add:
        r = sh("git", "add", "-N", rel)     # intent-to-add: tracked for `git ls-files`, nothing committed
        if r.returncode:
            raise NotApplied(r.stderr)


def sub(rel, old, new, count=1):
    t = rd(rel)
    if old not in t:
        raise NotApplied(f"{rel}: target text not found: {old[:60]!r}")
    wr(rel, t.replace(old, new, count))


def run_lock(lock, slow=False, nodes=None):
    env = dict(os.environ)
    env.pop("OA_SLOW", None)
    if slow:
        env["OA_SLOW"] = "1"
    r = sh(sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", *(nodes or LOCKS[lock]), env=env)
    tail = [ln for ln in r.stdout.strip().splitlines() if ln.strip()][-1:] if r.stdout.strip() else []
    return r.returncode, (tail[0] if tail else r.stderr.strip()[-200:])


G567 = "frontier/B567_hamiltonian_handoff/FINDINGS.md"
T567 = "tests/test_b567_hamiltonian.py"
GF = "frontier/B862_global_form/global_form.py"
QY = "scripts/atlas/query.py"
B892F = "frontier/B892_second_measurement/FINDINGS.md"
WJ = "frontier/B892_second_measurement/verification/walls_on_the_line.json"
WPY = "frontier/B892_second_measurement/verification/walls_on_the_line.py"
B1856F = "frontier/B1856_charge_or_symmetry_at_five_verified/FINDINGS.md"
B1856V = "frontier/B1856_charge_or_symmetry_at_five_verified/arc_verdict.json"
PS = "frontier/B1856_charge_or_symmetry_at_five_verified/verification/parity_split.py"


def json_edit(rel, fn):
    d = json.loads(rd(rel))
    fn(d)
    wr(rel, json.dumps(d, indent=1) + "\n")


PLANTS = [
    # ---- E13: twenty distinct eigenvalues at level 165, bounded by the order 20 ----
    ("E13", "findings_count_reverted", "the corrected count stands in B567's findings", "the old value restored in place",
     lambda: sub(G567, "**20 distinct eigenvalues** [corrected", "**21 distinct eigenvalues** [corrected")),
    ("E13", "dated_bracket_removed", "the correction is dated and attributed", "the dated bracket's opening deleted",
     lambda: sub(G567, "[corrected 2026-11-10 (B1862;", "[(B1862;")),
    ("E13", "old_count_not_kept", "the old count is kept as history beside the correction", "the quoted old count reworded",
     lambda: sub(G567, 'this read "21 distinct', "this read twenty-one distinct")),
    ("E13", "count_split_at_branch_cut", "count on the lattice of the order's roots, not by angle", "the original mistake re-made in code",
     lambda: sub(T567, "    return len(mult), order, mult",
                 "    n_by_angle = len(np.unique(np.round(np.angle(ev), 6)))\n    return n_by_angle, order, mult")),
    ("E13", "wrong_half_in_the_weil_matrix", "the Weil matrix uses the inverse of 2 mod N", "s = N // 2 instead of (N + 1) // 2",
     lambda: sub(T567, "    s = (N + 1) // 2", "    s = N // 2")),
    ("E13", "multiplicity_list_wrong_in_findings", "the findings' multiplicity list equals the computation",
     "two entries changed, sum kept at 165", lambda: sub(G567, "7, 7, 7, 6, 6, 5, 5", "8, 7, 7, 6, 5, 5, 5")),
    ("E13", "bound_misstated_in_findings", "with order 20 there are at most 20", "the stated bound changed to 21",
     lambda: sub(G567, "so there are at most 20", "so there are at most 21")),
    ("E13", "old_count_in_verdict_line", "the corrected count travels to the verdict line", "21 added to B567's claim line",
     lambda: json_edit("frontier/B567_hamiltonian_handoff/arc_verdict.json",
                       lambda d: d.__setitem__("claim_one_line", d["claim_one_line"] + " Level 165 has 21 distinct eigenvalues."))),
    ("E13", "old_count_on_another_page", "the corrected count travels to every page", "a new tracked page states 21",
     lambda: wr("docs/PLANT_E13.md", "B567 found 21 distinct eigenvalues at level 165.\n", add=True)),
    # ---- E6: the kernel computed from the map ----
    ("E6", "hand_condition_back_respelt", "the kernel is computed from the map, not a hand-derived condition",
     "the old exp(6ia) = 1 test restored, spelt exp(1j * 6 * a)",
     lambda: sub(GF, "    assert grid % 6 == 0\n",
                 "    assert grid % 6 == 0\n    import numpy as np\n    return [((2 * Fr(n, grid)) % 1, (-3 * Fr(n, grid)) % 1, Fr(n, grid))"
                 " for n in range(grid) if abs(np.exp(1j * 6 * (2 * np.pi * n / grid)) - 1) < 1e-9]\n")),
    ("E6", "kernel_hard_coded", "the kernel is computed from the map", "the six triples returned without building the map",
     lambda: sub(GF, "    assert grid % 6 == 0\n",
                 "    assert grid % 6 == 0\n    return [((2 * Fr(k, 6)) % 1, (-3 * Fr(k, 6)) % 1, Fr(k, 6)) for k in range(6)]\n")),
    ("E6", "exponents_swapped", "the map is diag(A e^{-2ia}, B e^{3ia})", "the two exponents exchanged",
     lambda: sub(GF, "[(al + charges[0] * q) % 1] * 3 + [(be + charges[1] * q) % 1] * 2",
                 "[(al + charges[1] * q) % 1] * 3 + [(be + charges[0] * q) % 1] * 2")),
    ("E6", "grid_half_scanned", "the grid of sixths is scanned completely", "only half the grid scanned",
     lambda: sub(GF, "            for n in range(grid):", "            for n in range(grid // 2):")),
    ("E6", "dated_note_removed", "the correction is dated in the findings", "the dated note's marker deleted",
     lambda: sub("frontier/B862_global_form/FINDINGS.md", "Dated note, 2026-11-10 (B1862", "Note (B1862")),
    ("E6", "results_file_stale", "the committed results equal the computation", "results.json's kernel changed to Z3",
     lambda: json_edit("frontier/B862_global_form/results.json",
                       lambda d: (d.__setitem__("kernel_sixth_root_indices", [0, 2, 4]), d.__setitem__("kernel_order", 3)))),
    # ---- E10: the arc lookup reads its argument ----
    ("E10", "argument_ignored_again", "card <arc> prints that arc", "the corpus card printed whatever the id",
     lambda: sub(QY, '        print(arc_card(argv[1], g)["text"])', '        print(context_card(g)["text"])')),
    ("E10", "verdict_field_wrong", "the verdict line shows the verdict", "the status field printed as the verdict",
     lambda: sub(QY, "verdict: {v.get('verdict')}", "verdict: {v.get('status')}")),
    ("E10", "verdict_file_of_another_arc", "the verdict and claim are the named arc's", "B1812's verdict file read for every arc",
     lambda: sub(QY, '"frontier", arc_id + "_*", "arc_verdict.json"', '"frontier", "B1812" + "_*", "arc_verdict.json"')),
    ("E10", "claim_line_dropped", "the card prints the claim line", "the claim line not printed",
     lambda: sub(QY, '        text.append("  claim: " + str(v.get("claim_one_line", "")))\n', "")),
    ("E10", "status_hard_coded", "the card prints the arc's status", "every arc shown as [banked]",
     lambda: sub(QY, 'head = (v or {}).get("verdict") or "no verdict"', 'head = "PROVED"')),
    ("E10", "verdict_hard_coded", "the verdict line shows the arc's verdict", "every arc shown as NEGATIVE",
     lambda: sub(QY, "verdict: {v.get('verdict')}", "verdict: NEGATIVE")),
    ("E10", "unknown_arc_prints_corpus", "an unknown arc is reported as unknown", "the corpus card printed for an unknown id",
     lambda: sub(QY, 'return dict(probe=arc_id, error="unknown arc", text=f"unknown arc \'{arc_id}\'")',
                 "return context_card(g)")),
    # ---- E5: the walls are purely imaginary; the scan's sentence carries its correction ----
    ("E5", "wall_gets_a_real_part", "no wall has a real part", "the committed ratio set to 0.3",
     lambda: json_edit(WJ, lambda d: d["numbers"].__setitem__("largest_real_part_over_modulus", 0.3))),
    ("E5", "one_wall_shifted", "the walls come in conjugate pairs at the computed values", "one wall moved by 1e-6",
     lambda: json_edit(WJ, lambda d: d["numbers"]["walls"][0].__setitem__(0, d["numbers"]["walls"][0][0] + 1e-6))),
    ("E5", "a_check_false_run_text_unchanged", "every committed check holds", "one boolean check set false",
     lambda: json_edit(WJ, lambda d: d.__setitem__(next(k for k, v in d.items() if isinstance(v, bool)), False))),
    ("E5", "class_pattern_changed", "the seven classes are as computed", "one class 6 -> 8",
     lambda: json_edit(WJ, lambda d: d["numbers"].__setitem__("classes", [2, 2, 6, 6, 6, 6, 8]))),
    ("E5", "findings_correction_removed", "the scan's sentence carries its correction", "the CORRECTED marker reworded",
     lambda: sub(B892F, "CORRECTED 2026-11-11 (the audit's finding E5", "Revised (the audit's finding E5")),
    ("E5", "b874_note_removed", "the correction travels to B874", "B874's dated note reworded",
     lambda: sub("frontier/B874_measurement_ladder/FINDINGS.md", "Dated note 2026-11-11 (the audit's finding E5", "Note (E5")),
    ("E5", "skeleton_narrowed", "the paper's sentence covers all three roots", "'all three' narrowed to one root",
     lambda: sub("papers/structure_paper/SKELETON.md", "**all three** Galois roots", "**the first** Galois root")),
    ("E5", "faulty_script_silently_fixed", "the old fault is kept in the script as it was run", "the 'if not found:' guard removed",
     lambda: sub("frontier/B892_second_measurement/wall_search.py", "if not found:", "if True:")),
    ("E5", "old_sentence_on_another_page", "the correction travels to every page", "a new tracked page repeats the old exclusion",
     lambda: wr("docs/PLANT_E5.md", "B892's 120-point real-line scan excludes a real point of nullity 14 on the line.\n", add=True)),
    ("E5", "instrument_broken_fast_lane", "the committed numbers come from the instrument as it stands",
     "the instrument's nullity made a rank; outputs not rerun (fast lane)",
     lambda: sub(WPY, "def nullity_direct(", "def _nullity_direct_true(")
     or sub(WPY, "\ndef joint_weights(", "\ndef nullity_direct(*a, **k):\n    n, *rest = _nullity_direct_true(*a, **k)\n"
            "    return (a[2] - n, *rest)\n\n\ndef joint_weights(")),
    # ---- E3: the charge premise splits; no old form stands without its correction ----
    ("E3", "old_form_on_a_new_page", "no old form stands without the correction beside it", "the exact old form, uncorrected",
     lambda: wr("docs/PLANT_E3.md", "The premise holds by (invisibility to every state) at the ramified prime.\n", add=True)),
    ("E3", "old_form_paraphrased", "no old form stands without the correction beside it", "'invisible to every state', uncorrected",
     lambda: wr("docs/PLANT_E3.md", "B1856 shows the charge premise is invisible to every state.\n", add=True)),
    ("E3", "old_form_broken_across_a_line", "no old form stands without the correction beside it", "the exact form split by a newline",
     lambda: wr("docs/PLANT_E3.md", "The premise holds by (invisibility to every\nstate) at the ramified prime.\n", add=True)),
    ("E3", "spoof_marker_beside_it", "the correction stands beside the old form", "an unrelated 'E = +I' within 900 characters",
     lambda: wr("docs/PLANT_E3.md", "The premise holds by (invisibility to every state). Elsewhere, E = +I is a unit test name.\n",
                add=True)),
    ("E3", "old_form_in_a_text_file", "no old form stands anywhere in the record", "the exact old form in a .txt file",
     lambda: wr("docs/PLANT_E3.txt", "The premise holds by (invisibility to every state) at the ramified prime.\n", add=True)),
    ("E3", "old_form_in_an_excluded_folder", "no old form stands anywhere in the record", "the exact old form under docs/views/",
     lambda: wr("docs/views/PLANT_E3.md", "The premise holds by (invisibility to every state).\n", add=True)),
    ("E3", "correction_too_far_away", "the correction stands beside the old form", "the marker 1000 characters after it",
     lambda: wr("docs/PLANT_E3.md", "The premise holds by (invisibility to every state)." + " filler" * 150 + " E = +I only.\n",
                add=True)),
    ("E3", "parity_split_miscounts", "338 have E = +I and 305 have E = -I", "one class of E = -I counted as +I",
     lambda: sub(PS, "        elif e == mod(MINUS, P):\n            minus.append(r)",
                 "        elif e == mod(MINUS, P):\n            (plus if len(minus) == 0 else minus).append(r)")),
    ("E3", "findings_counts_removed", "the findings carry the split", "the count sentence reworded",
     lambda: sub(B1856F, "338 have E ≡ +I and 305 have E ≡ −I", "most have E ≡ +I")),
    ("E3", "verdict_line_unmarked", "the verdict line carries the correction", "the CORRECTED marker removed from the claim line",
     lambda: json_edit(B1856V, lambda d: d.__setitem__("claim_one_line", d["claim_one_line"].replace("CORRECTED 2026-11-10 (B1862", "(B1862")))),
    ("E3", "tau_page_note_removed", "the correction travels to the read-out rule's page", "the carried-here marker reworded",
     lambda: sub("docs/THE_TAU_READOUT_RULE.md", "carried here by Review 78", "noted at Review 78")),
    ("E3", "b1855_note_removed", "the correction travels to B1855", "the carried-here marker reworded in B1855",
     lambda: sub("frontier/B1855_the_charge_law_settled/FINDINGS.md", "carried here by Review 78", "noted at Review 78")),
    # ================= new plants (SM-R79b) =================
    # ---- E13: the tripwire's entry for the old count ----
    ("E13", "old_count_in_words", "the corrected count travels to every page", "'twenty-one distinct eigenvalues' on a new page",
     lambda: wr("docs/PLANT_E13.md", "B567 found twenty-one distinct eigenvalues at level 165.\n", add=True)),
    ("E13", "old_count_beside_an_unrelated_bound", "the correction stands beside the old count",
     "21 asserted, with 'at most 20' about another matter in the next sentence",
     lambda: wr("docs/PLANT_E13.md", "B567 found 21 distinct eigenvalues at level 165. A different lattice has at most 20 roots.\n",
                add=True)),
    ("E13", "old_count_in_a_paper", "the corrected count travels to every page", "the old count in papers/",
     lambda: wr("papers/PLANT_E13.md", "B567 found 21 distinct eigenvalues at level 165.\n", add=True)),
    # ---- E6: the kernel's statement on the arc's pages ----
    ("E6", "findings_kernel_misstated", "the page states the kernel the map gives", "the findings' 'exactly ℤ₆' changed to 'exactly ℤ₃'",
     lambda: sub("frontier/B862_global_form/FINDINGS.md", "**exactly ℤ₆**", "**exactly ℤ₃**")),
    ("E6", "verdict_line_kernel_misstated", "the verdict line states the kernel the map gives", "the claim line's '/Z6' changed to '/Z3'",
     lambda: json_edit("frontier/B862_global_form/arc_verdict.json",
                       lambda d: d.__setitem__("claim_one_line", d["claim_one_line"].replace("]/Z6 -- kernel", "]/Z3 -- kernel")))),
    # ---- E10: the claim line printed whole ----
    ("E10", "claim_line_truncated", "the card prints the claim line", "the claim cut to its first 100 characters",
     lambda: sub(QY, 'text.append("  claim: " + str(v.get("claim_one_line", "")))',
                 'text.append("  claim: " + str(v.get("claim_one_line", ""))[:100])')),
    # ---- E5: the tripwire's entry for the scan's old sentence ----
    ("E5", "old_sentence_exact_on_a_new_page", "the correction travels to every page", "the exact old sentence, uncorrected",
     lambda: wr("docs/PLANT_E5.md", "The real-line scan shows that no real nullity-14 point exists there.\n", add=True)),
    ("E5", "old_sentence_exact_across_a_line", "the correction travels to every page", "the exact old sentence split by a newline",
     lambda: wr("docs/PLANT_E5.md", "The real-line scan shows that no real nullity-14\npoint exists there.\n", add=True)),
    ("E5", "old_sentence_reworded", "the correction travels to every page", "'there is no real point of nullity 14 there'",
     lambda: wr("docs/PLANT_E5.md", "The real-line scan shows there is no real point of nullity 14 there.\n", add=True)),
    ("E5", "old_sentence_citing_the_instrument", "the correction stands beside the old sentence",
     "the old sentence with the instrument's file name cited after it",
     lambda: wr("docs/PLANT_E5.md", "The real-line scan shows that no real nullity-14 point exists there (see walls_on_the_line.json).\n",
                add=True)),
    ("E5", "old_sentence_in_a_paper", "the correction travels to every page", "the exact old sentence in papers/",
     lambda: wr("papers/PLANT_E5.md", "The real-line scan shows that no real nullity-14 point exists there.\n", add=True)),
    # ---- B1884: the tripwire's entry for the level of a ground ----
    ("B1884", "old_form_exact", "the scoped statement travels to every page", "the exact old form on a new page",
     lambda: wr("docs/PLANT_B1884.md", "LR fixes a point of P¹(ℤ/N) only at N = 5.\n", add=True)),
    ("B1884", "old_form_ascii", "the scoped statement travels to every page", "the old form spelt P^1(Z/N)",
     lambda: wr("docs/PLANT_B1884.md", "LR fixes a point of P^1(Z/N) only at N = 5.\n", add=True)),
    ("B1884", "old_form_short", "the scoped statement travels to every page", "the short form the finding quoted, 'fixes a point only at N = 5'",
     lambda: wr("docs/PLANT_B1884.md", "LR fixes a point only at N = 5.\n", add=True)),
    ("B1884", "old_form_reordered", "the scoped statement travels to every page", "'only at N = 5 does LR fix a point of P¹(ℤ/N)'",
     lambda: wr("docs/PLANT_B1884.md", "Only at N = 5 does LR fix a point of P¹(ℤ/N).\n", add=True)),
    ("B1884", "old_form_z_mod_nz", "the scoped statement travels to every page", "the old form spelt P¹(ℤ/Nℤ)",
     lambda: wr("docs/PLANT_B1884.md", "LR fixes a point of P¹(ℤ/Nℤ) only at N = 5.\n", add=True)),
    ("B1884", "old_form_with_the_marker_phrase", "the scoped statement replaces the old one",
     "the old form kept, with 'exactly one point at N = 5' added after it",
     lambda: wr("docs/PLANT_B1884.md", "LR fixes a point of P¹(ℤ/N) only at N = 5, and it has exactly one point at N = 5.\n", add=True)),
    ("B1884", "old_form_in_a_paper", "the scoped statement travels to every page", "the exact old form in papers/",
     lambda: wr("papers/PLANT_B1884.md", "LR fixes a point of P¹(ℤ/N) only at N = 5.\n", add=True)),
    # ---- E3: the widened tripwire ----
    ("E3", "spoof_with_a_split_word", "the correction must name the split", "an unrelated 'E = +I only' within 500 characters",
     lambda: wr("docs/PLANT_E3.md", "The premise holds by (invisibility to every state). Elsewhere, E = +I only names a unit test.\n",
                add=True)),
    ("E3", "old_form_other_words", "no old form stands without the correction beside it", "'invisible to all states', uncorrected",
     lambda: wr("docs/PLANT_E3.md", "B1856 shows the charge premise is invisible to all states.\n", add=True)),
    ("E3", "old_form_in_a_script_header", "no old form stands anywhere in the record", "the exact old form in a .py docstring under frontier/",
     lambda: wr("frontier/B1856_charge_or_symmetry_at_five_verified/verification/plant_e3.py",
                '"""The premise holds by (invisibility to every state) at the ramified prime."""\n', add=True)),
    ("E3", "old_form_in_a_paper", "no old form stands anywhere in the record", "the exact old form in papers/",
     lambda: wr("papers/PLANT_E3.md", "The premise holds by (invisibility to every state) at the ramified prime.\n", add=True)),
    ("E3", "old_form_in_the_progress_log", "no old form stands without the correction beside it",
     "the exact old form appended to PROGRESS_LOG.md (main: append-only, not read)",
     lambda: wr("PROGRESS_LOG.md", rd("PROGRESS_LOG.md") + "\nThe premise holds by (invisibility to every state).\n")),
]

EXPECT = {
    ('E13', 'findings_count_reverted'): ('as before', 'CAUGHT'),
    ('E13', 'dated_bracket_removed'): ('as before', 'CAUGHT'),
    ('E13', 'old_count_not_kept'): ('as before', 'CAUGHT'),
    ('E13', 'count_split_at_branch_cut'): ('as before', 'CAUGHT'),
    ('E13', 'wrong_half_in_the_weil_matrix'): ('as before', 'CAUGHT'),
    ('E13', 'multiplicity_list_wrong_in_findings'): ('as before', 'CAUGHT'),
    ('E13', 'bound_misstated_in_findings'): ('as before', 'CAUGHT'),
    ('E13', 'old_count_in_verdict_line'): ('as before', 'CAUGHT'),
    ('E13', 'old_count_on_another_page'): ('as before', 'CAUGHT'),
    ('E6', 'hand_condition_back_respelt'): ('as before', 'CAUGHT'),
    ('E6', 'kernel_hard_coded'): ('as before', 'CAUGHT'),
    ('E6', 'exponents_swapped'): ('re-aimed', 'CAUGHT'),
    ('E6', 'grid_half_scanned'): ('as before', 'CAUGHT'),
    ('E6', 'dated_note_removed'): ('as before', 'CAUGHT'),
    ('E6', 'results_file_stale'): ('as before', 'CAUGHT'),
    ('E10', 'argument_ignored_again'): ('as before', 'CAUGHT'),
    ('E10', 'verdict_field_wrong'): ('as before', 'CAUGHT'),
    ('E10', 'verdict_file_of_another_arc'): ('as before', 'CAUGHT'),
    ('E10', 'claim_line_dropped'): ('as before', 'CAUGHT'),
    ('E10', 'status_hard_coded'): ('re-aimed', 'CAUGHT'),
    ('E10', 'verdict_hard_coded'): ('as before', 'CAUGHT'),
    ('E10', 'unknown_arc_prints_corpus'): ('as before', 'CAUGHT'),
    ('E5', 'wall_gets_a_real_part'): ('as before', 'CAUGHT'),
    ('E5', 'one_wall_shifted'): ('as before', 'CAUGHT'),
    ('E5', 'a_check_false_run_text_unchanged'): ('as before', 'CAUGHT'),
    ('E5', 'class_pattern_changed'): ('as before', 'CAUGHT'),
    ('E5', 'findings_correction_removed'): ('as before', 'CAUGHT'),
    ('E5', 'b874_note_removed'): ('as before', 'CAUGHT'),
    ('E5', 'skeleton_narrowed'): ('as before', 'CAUGHT'),
    ('E5', 'faulty_script_silently_fixed'): ('as before', 'CAUGHT'),
    ('E5', 'old_sentence_on_another_page'): ('as before', 'MISSED'),
    ('E5', 'instrument_broken_fast_lane'): ('as before', 'MISSED'),
    ('E3', 'old_form_on_a_new_page'): ('as before', 'CAUGHT'),
    ('E3', 'old_form_paraphrased'): ('as before', 'CAUGHT'),
    ('E3', 'old_form_broken_across_a_line'): ('as before', 'CAUGHT'),
    ('E3', 'spoof_marker_beside_it'): ('as before', 'CAUGHT'),
    ('E3', 'old_form_in_a_text_file'): ('as before', 'CAUGHT'),
    ('E3', 'old_form_in_an_excluded_folder'): ('as before', 'MISSED'),
    ('E3', 'correction_too_far_away'): ('as before', 'CAUGHT'),
    ('E3', 'parity_split_miscounts'): ('as before', 'CAUGHT'),
    ('E3', 'findings_counts_removed'): ('as before', 'CAUGHT'),
    ('E3', 'verdict_line_unmarked'): ('as before', 'CAUGHT'),
    ('E3', 'tau_page_note_removed'): ('as before', 'CAUGHT'),
    ('E3', 'b1855_note_removed'): ('as before', 'CAUGHT'),
    ('E13', 'old_count_in_words'): ('new', 'MISSED'),
    ('E13', 'old_count_beside_an_unrelated_bound'): ('new', 'MISSED'),
    ('E13', 'old_count_in_a_paper'): ('new', 'MISSED'),
    ('E6', 'findings_kernel_misstated'): ('new', 'MISSED'),
    ('E6', 'verdict_line_kernel_misstated'): ('new', 'MISSED'),
    ('E10', 'claim_line_truncated'): ('new', 'CAUGHT'),
    ('E5', 'old_sentence_exact_on_a_new_page'): ('new', 'CAUGHT'),
    ('E5', 'old_sentence_exact_across_a_line'): ('new', 'CAUGHT'),
    ('E5', 'old_sentence_reworded'): ('new', 'MISSED'),
    ('E5', 'old_sentence_citing_the_instrument'): ('new', 'MISSED'),
    ('E5', 'old_sentence_in_a_paper'): ('new', 'MISSED'),
    ('B1884', 'old_form_exact'): ('new', 'CAUGHT'),
    ('B1884', 'old_form_ascii'): ('new', 'CAUGHT'),
    ('B1884', 'old_form_short'): ('new', 'MISSED'),
    ('B1884', 'old_form_reordered'): ('new', 'MISSED'),
    ('B1884', 'old_form_z_mod_nz'): ('new', 'MISSED'),
    ('B1884', 'old_form_with_the_marker_phrase'): ('new', 'MISSED'),
    ('B1884', 'old_form_in_a_paper'): ('new', 'MISSED'),
    ('E3', 'spoof_with_a_split_word'): ('new', 'MISSED'),
    ('E3', 'old_form_other_words'): ('new', 'MISSED'),
    ('E3', 'old_form_in_a_script_header'): ('new', 'MISSED'),
    ('E3', 'old_form_in_a_paper'): ('new', 'MISSED'),
    ('E3', 'old_form_in_the_progress_log'): ('new', 'MISSED'),
}


def expectations():
    rows = [{"lock": l, "plant": n, "rule_broken": r, "shape": s, "origin": EXPECT[(l, n)][0], "expected": EXPECT[(l, n)][1]}
            for l, n, r, s, _ in PLANTS]
    assert len(rows) == len(EXPECT) == len({(r["lock"], r["plant"]) for r in rows})
    OUT.write_text(json.dumps({"written_before_any_run": True, "main": "896cae025", "plants": rows}, indent=1,
                              ensure_ascii=False) + "\n", encoding="utf-8")
    print(len(rows), "expectations written")


def main():
    if EXPECT_ONLY:
        return expectations()
    res = {"clone_head": sh("git", "rev-parse", "HEAD").stdout.strip(), "baseline": {}, "plants": []}
    reset()
    for lock in LOCKS:
        rc, tail = run_lock(lock)
        res["baseline"][lock] = {"passes_unaltered": rc == 0, "tail": tail}
    for lock, name, rule, shape, apply in PLANTS:
        reset()
        row = {"lock": lock, "plant": name, "rule_broken": rule, "shape": shape, "origin": EXPECT[(lock, name)][0],
               "expected": EXPECT[(lock, name)][1]}
        if not res["baseline"][lock]["passes_unaltered"]:
            row["result"] = "NOT COUNTED (lock fails unaltered)"
        else:
            try:
                apply()
                rc, tail = run_lock(lock)
                row["result"] = "CAUGHT" if rc != 0 else "MISSED"
                row["tail"] = tail
                if name == "instrument_broken_fast_lane":
                    rc2, tail2 = run_lock(lock, slow=True, nodes=["tests/test_b892_walls_on_the_line.py::test_the_joint_weights_recomputed"])
                    row["slow_lane"] = "CAUGHT" if rc2 != 0 else "MISSED"
                    row["slow_tail"] = tail2
            except NotApplied as e:
                row["result"] = "NOT APPLIED"
                row["why"] = str(e)
        res["plants"].append(row)
        print(f"{lock:5} {name:38} {row['result']:8} expected {row['expected']}" + (f"  (slow lane: {row['slow_lane']})" if "slow_lane" in row else ""),
              flush=True)
    reset()
    summary = {}
    for lock in LOCKS:
        rows = [r for r in res["plants"] if r["lock"] == lock and r["result"] in ("CAUGHT", "MISSED")]
        summary[lock] = {"planted": len(rows), "caught": sum(r["result"] == "CAUGHT" for r in rows),
                         "missed": [r["plant"] for r in rows if r["result"] == "MISSED"],
                         "as_before_planted": sum(r["origin"] != "new" for r in rows),
                         "as_before_caught": sum(r["origin"] != "new" and r["result"] == "CAUGHT" for r in rows),
                         "not_as_expected": [r["plant"] for r in rows if r["result"] != r["expected"]]}
    res["not_applied"] = [(r["lock"], r["plant"]) for r in res["plants"] if r["result"] == "NOT APPLIED"]
    res["summary"] = summary
    OUT.write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
