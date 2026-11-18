"""B1957: every statement in every markdown file the seats added or changed in the window, as registered units.
A unit is a bullet or numbered item, a table row, or a paragraph, with its file, first line and text.  Mechanical, so that
none is skipped.  Run by hand (it needs the seats' remote branches); it writes UNITS.json.  Nothing of a seat's is run."""
import hashlib, json, pathlib, re, subprocess
HERE = pathlib.Path(__file__).resolve().parent
LANES = (  # (lane, the seat's name, branch, base before the window, head harvested to)
    ("agy-exp", "agy-exp", "origin/agy/self-consistent-loop-2026-11-11", "ef140a024", "d7bb27195"),
    ("agy-002-verify", "agy-002", "origin/agy-002/verify", "53ac6c7d", "55f72ee3f"),
    ("agy-002-endgame", "agy-002", "origin/agy-002/endgame", "613c4f417", "94e511f54"),
    ("agy-002-closure", "agy-002", "origin/agy-002/closure", "94e511f54", "358d61786"),
    ("agy-002-foundations", "agy-002", "origin/agy-002/foundations", "ff8e1ca57", "ef2ea365b"),   # added 2026-11-18: its gates 8 to 11, a synthesis, its harvest review for M43 to M45; the branch is cut from main at ff8e1ca57
    ("physical", "physical (codex)", "origin/audit/physical-bridge-2026-09-05", "1aa76251", "4e27d6d41"),
    ("web", "the web seat (chat1)", "origin/chat1/web-seat", "b1727da04", "9dccd2062"),
    ("agy-audit", "agy", "origin/agy/audit-2026-11-02", "da5c7125", "baadbad81"),
    ("sm", "the SM seat", "<remote>/standard-model-derivation-0qt6ao", "6ea836f5", "e7bf7bfca"),   # added 2026-11-18: its cards SM-C18 to SM-C21, delivered after its pin; the branch is written as the repository writes it (the label is not used to read: base and head are)
)
EXTRA = {  # files older than a lane's window that main's own record shows were never read in full or never given a verdict.
    # The web seat: its section 1d's eight notes (2026-11-17), then, at its section 7.3 (2026-11-18), every file named by one of its harvest rows whose
    # disposition opens RECEIVED, REGISTERED or UNREAD or says it was read only at its head, the six relays it names as read in full but outside the
    # register, its two review readings, and its cards; then, at its section 7.5 item 2, the four relays main's current arcs cite by label that were
    # read in their day (W-C5, W-C6 part 2, W-C8 parts 1 and 2a).  Rows whose disposition records a reading with main's verdict and that no current
    # arc cites are not reopened here (FINDINGS).
    # agy-exp (added 2026-11-18): the twenty files older than its window that its own HARVEST REVIEW FOR MAIN (its status page at c4c48f541,
    # section 1a) lists as owed, not read or deferred on main's record.
    "agy-exp": (
        "relays/AGY_TO_CC_AND_CHAT1_2026-11-11_P781_MASK_SAFE_THEOREMS.md",
        "relays/AGY_EXP_TO_CC_2026-11-11_W_C2_ANSWERS.md",
        "self_consistent_loop/reports/phase4_unification_cap_lepton_report.md",
        "relays/AGY_EXP_TO_CC_2026-11-11_X_C2_RESULTS.md",
        "relays/AGY_EXP_TO_CC_2026-11-11_X_C3_SPECIFICATION.md",
        "relays/AGY_EXP_TO_CC_2026-11-12_X_C1A_RESULTS.md",
        "relays/AGY_EXP_TO_CC_2026-11-12_X_C1B_RESULTS.md",
        "relays/AGY_EXP_TO_CC_2026-11-12_X_C1C_RESULTS.md",
        "relays/AGY_EXP_TO_CC_2026-11-12_X_C1D_RESULTS.md",
        "relays/REVIEW_79B_AGY-EXP.md",
        "relays/REVIEW_80_AGY-EXP.md",
        "relays/AGY_EXP_TO_CC_2026-11-14_X_C9_RESULTS.md",
        "relays/AGY_EXP_TO_CC_2026-11-14_X_NEVER_RESULTS.md",
        "relays/AGY_EXP_TO_CC_2026-11-14_X_OWN_RESULTS.md",
        "relays/AGY_EXP_TO_CC_2026-11-14_F3_CHARGE_SIGN_NOTE.md",
        "relays/AGY_EXP_TO_CC_2026-11-14_X_SURVIVAL_RESULTS.md",
        "relays/AGY_EXP_TO_CC_2026-11-14_X_CANON_AND_EXACT_W_RESULTS.md",
        "relays/AGY_EXP_TO_CC_2026-11-14_X_MEASURE_AND_AREA_RESULTS.md",
        "relays/AGY_EXP_TO_CC_2026-11-14_B1936_COLD_READ.md",
        "relays/AGY_EXP_TO_CC_2026-11-15_WHY_FRAME_C_WALLS_EVEN_IN_THE_CUSP.md",
    ),
    "web": (
        "docs/handoffs/chat1_i26_decision_table_2026-09-15/I26_DECISION_TABLE.md",
        "frontier/B1303_the_sm_closings_z_prime/CHAT1_TO_CC_2026-09-08_SESSION_RELAY.md",
        "relays/CHAT1_TO_CC_2026-10-06_FIRST_BACKGROUND.md",
        "relays/CHAT1_TO_CC_2026-11-07_R2S_BLOCK_A_PURE_NUMBER_ON_THE_RECORD.md",
        "relays/CHAT1_TO_CC_2026-11-07_THE_TUBES_TAU_FIRMED_UP.md",
        "relays/CHAT1_TO_CC_2026-11-10_THE_CONTENT_IN_WEAVE_FORM.md",
        "relays/CHAT1_TO_CC_2026-11-10_THE_WEAVES_OWN_ACTION_ON_TAU.md",
        "relays/CHAT1_TO_CC_2026-11-11_M3_RESULTS_IN_THE_WORDS_OF_SECTION_12.md",
        "relays/CHAT1_TO_CC_2026-11-11_P-783_THE_GOLDEN_STATE_IS_THE_LOWEST_AND_SIMPLE.md",
        "relays/CHAT1_TO_CC_2026-11-11_W-C1_REAUDIT_OF_E7_AND_E2.md",
        "relays/CHAT1_TO_CC_2026-11-11_W-C2_THE_AGY-EXP_SEATS_FOUR_THEOREMS.md",
        "relays/CHAT1_TO_CC_2026-11-11_W-C3_THE_SM_SEATS_ITEMS_UNDER_BANKED_ARCS.md",
        "relays/CHAT1_TO_CC_2026-11-12_W-C4_THE_AGY_LANES_THEOREMS_C_D_E.md",
        "relays/CHAT1_TO_CC_2026-11-13_W-C5_B1914_B1915_AND_THE_CUSP.md",
        "relays/CHAT1_TO_CC_2026-11-13_W-C6_PART_1_THE_PROGRAMME_IN_SHORT_READ_COLD.md",
        "relays/CHAT1_TO_CC_2026-11-13_W-C6_PART_2_B1919_AND_B1921.md",
        "relays/CHAT1_TO_CC_2026-11-13_W-C7_B1913_RECOMPUTED_AND_THE_REST_HELD.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-B1_FRAME_D_AND_B1936S_PREMISE.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-C8_PART_1_THE_TICK_PARITY_AND_THE_METALLIC_TICKS.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-C8_PART_2A_M000_IN_TWO_FRAMES_AND_TWISTED_DUALITY.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-C8_PART_3_THE_EVEN_TICK_CONDITION.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-C8_PART_4_THE_SYSTEMS_PAGE.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-C8_PART_5_THE_BRONZE_RIVAL.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F10_THE_FOUNDATIONS_LEDGER.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F11_FIVE_DISTINCTIONS_CARRY_THE_FRAMES_MATTER.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F12_THE_DOUBLETS_CLASS_INDEX_AT_ODD_LEVELS.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F13_P847_A_CRITERION_FOR_THE_HIGGS_READING.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F14_M25_THE_GLOBAL_BIT.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F15_THE_PRINCIPLE_DOING_ITS_JOB.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F16_THE_TWO_WAY_CHOICES_SETTLE_EACH_OTHER.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F17_SECOND_COMPUTATIONS_FOR_COMPUTED_NOWHERE.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F18_A_COLD_READ_OF_THE_BIG_RUNS_RULE.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F19_THE_ODD_LEVEL_CLASS_INDEX_PROVED.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F1_THE_DISTINCTION_LAYER_AND_THE_HAND.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F20_B1936S_PREMISE_IS_A_CHOICE_IN_FRAME_C.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F21_THE_RULES_VERSION_2_CLOSES_O1_TO_O10.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F22_B1922S_NEGATIVE_HALF_RECOMPUTED.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F23_THE_RULES_AMENDMENTS_A1_TO_A13.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F2_MIRRORS_OR_HALF_TURNS.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F3_THE_CONE_POINT_LOOPHOLE.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F4_THE_NON_ORIENTABLE_CLOSING.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F5_THE_CONE_POINT_IS_A_RELATION_AMONG_THE_DISTINCTIONS.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F6_THE_CHARACTER_GAP_LAW_AND_THE_NORMALISER.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F7_THE_MIXED_FACES.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F8_THREE_DISTINCTIONS_AGAINST_N.md",
        "relays/CHAT1_TO_CC_2026-11-14_W-F9_THE_ORDER_AT_THE_SCAR.md",
        "relays/CHAT1_TO_CC_2026-11-15_W-F24_WHERE_FRAME_CS_READ_OUT_LOSES_THE_HIERARCHY.md",
        "relays/CHAT1_TO_CC_2026-11-15_W-F25_FRAME_CS_CUSP_EXPONENTS.md",
        "relays/CHAT1_TO_CC_2026-11-15_W-F26_THE_CUSPS_MIXING_IN_EVERY_OPTION.md",
        "relays/REVIEW_79B_CHAT1.md",
        "relays/REVIEW_79_CHAT1.md",
        "relays/REVIEW_80_CHAT1.md",
        "relays/REVIEW_81_CHAT1.md",
        "relays/STATUS_CHAT1.md",
        "relays/cards/CHAT1_P-783_the_golden_state_lowest_and_simple.md",
        "relays/cards/CHAT1_W-A1_the_attack_on_selection_and_the_dictionary.md",
        "relays/cards/CHAT1_W-A2_deriving_postulate_d.md",
        "relays/cards/CHAT1_W-A3_the_cover_the_class_and_the_up_sector.md",
        "relays/cards/CHAT1_W-B1_frame_d_and_b1936s_premise.md",
        "relays/cards/CHAT1_W-B2_frame_d1s_coupling_as_a_triple_overlap.md",
        "relays/cards/CHAT1_W-C1_reaudit_of_E7_and_E2.md",
        "relays/cards/CHAT1_W-C2_the_agy_lanes_four_theorems.md",
        "relays/cards/CHAT1_W-C3_the_sm_seats_items_under_banked_arcs.md",
        "relays/cards/CHAT1_W-C4_the_agy_lanes_theorems_c_d_e.md",
        "relays/cards/CHAT1_W-C5_b1914_b1915_and_the_cusp.md",
        "relays/cards/CHAT1_W-C6_a_cold_reading_and_b1919_b1921.md",
        "relays/cards/CHAT1_W-C7_three_negatives_b1913_run_the_rest_held.md",
        "relays/cards/CHAT1_W-C8_the_one_tick_object_and_the_foundational_system.md",
        "relays/cards/CHAT1_W-F10_the_foundations_ledger.md",
        "relays/cards/CHAT1_W-F11_five_distinctions_and_the_frames_matter.md",
        "relays/cards/CHAT1_W-F12_the_doublets_class_index_at_odd_levels.md",
        "relays/cards/CHAT1_W-F13_p847_a_criterion_for_the_higgs_reading.md",
        "relays/cards/CHAT1_W-F14_m25_the_global_bit.md",
        "relays/cards/CHAT1_W-F15_the_principle_doing_its_job.md",
        "relays/cards/CHAT1_W-F16_the_two_way_choices_settle_each_other.md",
        "relays/cards/CHAT1_W-F17_second_computations_for_x_never.md",
        "relays/cards/CHAT1_W-F18_cold_read_of_the_big_runs_rule.md",
        "relays/cards/CHAT1_W-F19_a_proof_of_the_odd_level_class_index.md",
        "relays/cards/CHAT1_W-F1_the_distinction_layer_and_the_hand_at_the_common_point.md",
        "relays/cards/CHAT1_W-F20_cold_read_of_b1936s_parity_candidate.md",
        "relays/cards/CHAT1_W-F21_cold_read_of_the_rules_version_2.md",
        "relays/cards/CHAT1_W-F22_b1922s_negative_half.md",
        "relays/cards/CHAT1_W-F23_cold_read_of_the_rules_amendments.md",
        "relays/cards/CHAT1_W-F24_where_frame_cs_average_loses_the_hierarchy.md",
        "relays/cards/CHAT1_W-F25_frame_cs_cusp_exponents.md",
        "relays/cards/CHAT1_W-F26_the_cusps_mixing_in_every_option.md",
        "relays/cards/CHAT1_W-F2_mirrors_or_half_turns_and_what_the_record_holds.md",
        "relays/cards/CHAT1_W-F3_the_cone_point_loophole.md",
        "relays/cards/CHAT1_W-F4_the_non_orientable_closing.md",
        "relays/cards/CHAT1_W-F5_the_cone_point_is_a_relation_among_the_distinctions.md",
        "relays/cards/CHAT1_W-F6_the_character_gap_law_and_the_normaliser.md",
        "relays/cards/CHAT1_W-F7_the_mixed_faces.md",
        "relays/cards/CHAT1_W-F8_three_distinctions_against_n.md",
        "relays/cards/CHAT1_W-F9_the_order_at_the_scar.md",
        "relays/cards/CHAT1_W-L1_the_look_at_tau_i.md",
        "relays/cards/CHAT1_W-R79_review_79_seven_arcs.md",
        "relays/cards/CHAT1_W-R79b_main_answers_and_the_instruments.md",
        "relays/cards/CHAT1_W-R80_review_80.md",
        "relays/cards/CHAT1_W-R81_review_81.md",
        "relays/cards/CHAT1_W-V1_view_on_selection_and_dictionary.md",
        "relays/cards/CHAT1_cold_read_the_three_part_structure.md",
        "relays/CHAT1_TO_CC_2026-11-11_A_COLD_READ_OF_THE_THREE_PART_STRUCTURE.md",      # added 2026-11-18: named in main's own list and left out of this one; found by the seat (its section 8.2)
        "relays/chat1_2026-10-14_selection/FINDINGS_LAGRANGE_LAW.md",
        "relays/chat1_2026-10-14_selection/FINDINGS_THREAD_FRAME.md",
        "relays/chat1_2026-10-14_selection/PREREGISTRATION_LAGRANGE_LAW.md",
        "relays/chat1_2026-10-14_selection/PREREGISTRATION_THREAD_FRAME.md",
        "relays/chat1_2026-10-14_selection/THE_SELECTION_PRINCIPLE.md",
        "relays/chat1_2026-10-14_the_first_row/FINDINGS.md",
        "relays/chat1_2026-10-14_the_first_row/PREREGISTRATION.md",
        "relays/chat1_2026-10-14_the_scale/FINDINGS.md",
        "relays/chat1_2026-10-14_the_scale/PREREGISTRATION.md",
        "relays/chat1_2026-10-14_the_scale/THE_SCALE.md",
        "relays/chat1_2026-10-14_the_scale/T_ROOT_FINDINGS.md",
        "relays/chat1_2026-10-14_the_scale/T_ROOT_PREREGISTRATION.md",
        "relays/chat1_2026-10-14_the_scale/T_SIGN_FINDINGS.md",
        "relays/chat1_2026-10-14_the_scale/T_SIGN_PREREGISTRATION.md",
        "relays/chat1_2026-10-22_selection_map/THREADS_WITH_INGREDIENTS_RULE.md",
        "relays/chat1_2026-10-23_framing/THE_FRAMING_CHECK.md",
        "relays/chat1_2026-10-23_tick_line/DISCLOSURES_BEFORE_READING.md",
        "relays/chat1_2026-10-23_tick_line/PREDICTION_BEFORE_ZERO_FREE_HOLOMORPHIC.md",
        "relays/chat1_2026-10-23_tick_line/TICK_LINE_HIGGS_RESULT.md",
        "relays/chat1_2026-10-23_tick_line/TICK_LINE_HIGGS_RULE.md",
        "relays/chat1_2026-10-23_two_higgs/TWO_HIGGS_RESULT.md",
        "relays/chat1_2026-10-23_two_higgs/TWO_HIGGS_RULE.md",
        "relays/chat1_2026-10-23_zero_free_frame/ZERO_FREE_FRAME_EXPLORATION.md",
        "relays/chat1_2026-10-23_zero_free_frame/ZERO_FREE_HOLOMORPHIC_RESULT.md",
        "relays/chat1_2026-10-23_zero_free_frame/ZERO_FREE_HOLOMORPHIC_RULE.md",
    ),
}
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
BUL = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+\S"); TROW = re.compile(r"^\s*\|.*\|\s*$"); TSEP = re.compile(r"^\s*\|[\s:|-]+\|\s*$")
META = re.compile(r"^\W*(from|to|date|kind|seat|card|read|state|on|needs|next push)\W*[:*]", re.I)


def units_of(text):
    L = text.split("\n"); out = []; cur = None; section = ""; fence = False
    def close():
        nonlocal cur
        if cur: out.append(cur)
        cur = None
    for n, line in enumerate(L, 1):
        if line.strip().startswith("```"):
            fence = not fence
            if cur: cur["text"] += "\n" + line
            continue
        if fence:
            if cur: cur["text"] += "\n" + line
            continue
        if not line.strip(): close(); continue
        if line.lstrip().startswith("#"): close(); section = line.strip().lstrip("#").strip()[:160]; continue
        if TSEP.match(line): close(); continue
        if TROW.match(line):
            close(); head = n < len(L) and bool(TSEP.match(L[n]))       # a row followed by a separator is a table's header
            cur = {"line": n, "form": "head" if head else "row", "section": section, "text": line.strip()}; close(); continue
        if BUL.match(line): close(); cur = {"line": n, "form": "item", "section": section, "text": line.strip()}; continue
        if cur is None: cur = {"line": n, "form": "paragraph", "section": section, "text": line.strip()}
        else: cur["text"] += " " + line.strip()
    close(); return out


def tag(path):
    parts = path.split("/"); stem = re.sub(r"\.md$", "", parts[-1])
    if parts[0] == "relays" and len(parts) == 2: return stem
    return "/".join(parts[1:-1] + [stem]) if parts[0] in ("relays", "reports") else path[:-3]


if __name__ == "__main__":
    allu = []; files = []
    def resolve(ref):
        """a branch written the repository's way, `<remote>/<short name>`, is found by its last segments among the remote refs"""
        if not ref.startswith("<remote>/"): return ref
        short = ref.split("/", 1)[1]; c = [r for r in git("for-each-ref", "--format=%(refname:short)", "refs/remotes").split("\n") if r.endswith("/" + short)]
        c = [r for r in c if r.startswith("origin/")] or c          # the same branch on a mirror remote is not a second candidate
        assert len(c) == 1, (ref, c); return c[0]
    for lane, seat, ref, base, head in LANES:
        # CHANGED 2026-11-18: the register is cut AT THE HEAD NAMED, not at the branch's tip, so that a seat's later push cannot change a
        # cut already described; the head must lie on the branch, and a tip beyond it is said aloud (harvest_debt.py counts it as debt).
        tip = git("rev-parse", "--short=9", resolve(ref)).strip()
        assert subprocess.run(["git", "merge-base", "--is-ancestor", head, resolve(ref)], cwd=HERE).returncode == 0, (lane, head, "is not on", ref)
        if tip != head: print("%-18s the branch is at %s, beyond the head this register is cut at (%s)" % (lane, tip, head))
        names = [f for f in git("diff", "--name-only", "--diff-filter=AM", base, head, "--", "*.md").split("\n") if f]
        names = sorted(set(names) | set(EXTRA.get(lane, ())))
        for f in sorted(names):
            text = git("show", "%s:%s" % (head, f)); us = units_of(text); k = 0
            for u in us:
                t = re.sub(r"\s+", " ", u["text"])
                kind = "meta" if (u["form"] == "head" or len(t) < 25 or META.match(t) or t.strip("*` .") in ("0 of 19", "")) else "statement"
                allu.append({"id": "%s:%s:%d" % (lane, tag(f), u["line"]), "lane": lane, "seat": seat, "file": f, "line": u["line"], "form": u["form"],
                             "section": u["section"], "kind": kind, "sha": hashlib.sha1(t.encode()).hexdigest()[:10], "text": t[:700]}); k += 1
            files.append({"lane": lane, "seat": seat, "file": f, "head": head, "lines": text.count("\n") + 1, "units": k})
    assert len({u["id"] for u in allu}) == len(allu)
    lanes = [dict(zip(("lane", "seat", "branch", "base", "head"), l)) for l in LANES]
    # the committed register holds each unit's id, form, kind and a hash of its text; the text itself is read at the source
    compact = [[u["id"], u["form"][0], u["kind"][0], u["sha"]] for u in allu]
    (HERE / "UNITS.json").write_text(json.dumps({"lanes": lanes, "files": files, "units": compact}, separators=(",", ":"), ensure_ascii=False) + "\n")
    full = HERE.parents[2] / "audit" / "claims" / "UNITS_full.json"; full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(json.dumps({"lanes": lanes, "files": files, "units": allu}, ensure_ascii=False) + "\n")
    import collections
    c = collections.Counter(u["lane"] for u in allu); s = collections.Counter(u["lane"] for u in allu if u["kind"] == "statement"); fl = collections.Counter(x["lane"] for x in files)
    for lane, *_ in LANES: print("%-16s %4d files, %5d units, of which %5d statements" % (lane, fl[lane], c[lane], s[lane]))
    print("total: %d files, %d units, %d statements" % (len(files), len(allu), sum(s.values())))
