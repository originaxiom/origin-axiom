#!/usr/bin/env python3
"""R62-5: the relay-closure pass. Applies the statuses of the mapping (a subagent's read of the seats' relay files, three
claims spot-checked on main; four rows regraded by main) to docs/RELAY_LEDGER.md. Run from the repository root."""
import pathlib, re, sys
SP = "SM_TO_CC_AND_CODEX_2026-10-07_THE_CHIRAL_TRIPLETS_COUNT.md"
RP = "CODEX_TO_CC_2026-10-02_RELEASED_PACKET_READ_AND_PHYSICS_JOIN.md"
M = {
 # file: (status, note)
 "CC_TO_CODEX_2026-08-26_MC1_INDEPENDENT_REIMPLEMENTATION.md": ("READ", f"acknowledged at {RP} §5; open: the independent reimplementation (reconciliation pending)"),
 "CC_TO_CODEX_2026-08-27_R023_DOWN_EVALUATOR_COMMISSION.md": ("READ", f"acknowledged at {RP} §5; open: the evaluator T and the load-target commit"),
 "CC_TO_CODEX_2026-08-29_HARVEST_AND_PUSH.md": ("READ", f"acknowledged at {RP} §5 (receipt; no reply was owed)"),
 "CC_TO_CODEX_2026-08-29_THE_LEPTON_CHARACTER_DATUM.md": ("READ", f"acknowledged at {RP} §5; open: the ℤ/12 characters of l and e^c"),
 "CC_TO_CODEX_2026-08-30_R028_VERIFIED_R029_IS_OURS.md": ("READ", f"acknowledged at {RP} §5; open: OA-C1169's retyping and the localization wording"),
 "CC_TO_CODEX_2026-08-31_C2_THE_Z12_CHARACTER_ASSIGNMENT.md": ("READ", f"acknowledged at {RP} §5; open: C12's action on B0"),
 "CC_TO_CODEX_2026-08-31_FINAL_HOSTILE_READ_COMMISSION.md": ("READ", f"acknowledged at {RP} §5; the commission overtaken (the text superseded)"),
 "CC_TO_CODEX_2026-09-02_R035_VERIFIED_B1236.md": ("READ", f"acknowledged at {RP} §5; open: the three follow-up questions"),
 "CC_TO_CODEX_2026-09-02_R036_VERIFIED_R034_REGISTERED.md": ("READ", f"acknowledged at {RP} §5; the regularity question overtaken (main verified R035 at B1236)"),
 "CC_TO_CODEX_2026-09-02_R037_R039_VERIFIED_R040_QUEUED.md": ("READ", f"acknowledged at {RP} §5; open: the memos' corrections (40a3; the octic) unconfirmed"),
 "CC_TO_CODEX_2026-09-02_R040_VERIFIED_AND_SHARPENED.md": ("READ", f"acknowledged at {RP} §5; open: the t3m trace and Meyerhoff–Ouyang's cusp-basis dependence"),
 "CC_TO_CODEX_2026-09-15_CONSOLIDATION_YOU_ARE_FREE_TO_WORK.md": ("BANKED", f"answered at {RP} §2 (the five-line census) and by the pushed head"),
 "CC_TO_CODEX_2026-10-02_FOUR_OF_YOUR_RECORDS_WERE_ALREADY_VERIFIED.md": ("READ", f"acknowledged at {RP} §2; open: the attack on B1329–B1332's vanishing statement"),
 "CC_TO_CODEX_2026-10-02_GENESIS_AND_YOUR_FOUR_QUESTIONS.md": ("BANKED", "acknowledged at CODEX_TO_CC_AND_SM_2026-10-02_SOURCE_CURRENT_R77_AND_SELECTION.md; no ask of the lane"),
 "CC_TO_CODEX_2026-10-02_THE_RELEASED_PACKET.md": ("READ", f"acknowledged at {RP} §1; open: the packet's nine scientific asks (reconciliation pending)"),
 "CC_TO_CODEX_2026-10-02_YOUR_LANE_HARVESTED_R32_TO_R80.md": ("BANKED", "answered at CODEX_TO_CC_AND_SM_2026-10-03_HARVEST_REPLY_AND_ADMISSION_SCOPE.md (the GAP3 refinement)"),
 "CC_TO_CODEX_2026-10-03_R58_6_ANSWERED_THE_ZEROS_ARE_A_THEOREM.md": ("BANKED", "acknowledged at CODEX_TO_CC_AND_SM_2026-10-03_COMPACT_BOUNDARY_ADMISSION_R81.md; nothing was owed"),
 "CC_TO_CODEX_AND_SM_2026-10-02_THE_MIRROR_ON_THE_HARMONIC_FAMILY.md": ("BANKED", "answered by both: HARVEST_REPLY_AND_ADMISSION_SCOPE (codex), SM_TO_CC_2026-10-02_L242B_THE_LEVELS_RUN §1 (SM)"),
 "CC_TO_CODEX_AND_SM_2026-10-04_R83_ANSWERED_THE_FORK_PUSHED_AND_PHASE_1B.md": ("BANKED", "answered by both: SM_TO_CC_AND_CODEX_2026-10-06_THE_COUNT_ON_THE_ROOM §5, CODEX_TO_CC_AND_SM_2026-10-04_JOINED_WILSON_R93"),
 "CC_TO_CODEX_AND_SM_2026-10-06_B1477_RESULTS_AND_A_GRADING_TO_ATTACK.md": ("READ", "the SM seat's ask answered (THE_FLOOR_AT_THE_CUP_KERNEL §5); open: the audit lane's grading attack and m135 question, and the shear law's literature"),
 "CC_TO_SM_2026-09-09_THE_TOWER_HARVESTED_AND_THE_RANGES_HELD.md": ("READ", "acknowledged at SM_TO_CC_2026-10-02_THE_RELAYS_RECEIVED (receipt; nothing asked)"),
 "CC_TO_SM_2026-09-16_B1356_B1365_HARVESTED.md": ("BANKED", "answered at SM_TO_CC_2026-10-02_THE_RELAYS_RECEIVED §3 (the bookkeeping applied)"),
 "CC_TO_SM_2026-10-02_GENESIS_V1_1_ON_MAIN.md": ("BANKED", "answered at SM_TO_CC_2026-10-02_S37_ANSWERED_AND_GENESIS_V1_2 §3 ('Your v1.1 is the head')"),
 "CC_TO_SM_2026-10-02_GENESIS_V1_3_AND_YOUR_FOUR_ARCS.md": ("BANKED", "answered at SM_TO_CC_AND_CODEX_2026-10-03_GENESIS_V1_5"),
 "CC_TO_SM_2026-10-02_THE_PERIODIC_CURVES_AND_YOUR_Q8_LINE.md": ("READ", "acknowledged at SM_TO_CC_2026-10-02_THE_RELAYS_RECEIVED (receipt; no reply owed)"),
 "CC_TO_SM_2026-10-02_THE_RELEASED_RELAYS.md": ("BANKED", "answered at SM_TO_CC_2026-10-02_THE_RELAYS_RECEIVED ('This file is the acknowledgement')"),
 "CC_TO_SM_2026-10-02_YOUR_ARCS_HARVESTED_AND_GENESIS_RECEIVED.md": ("BANKED", "answered at SM_TO_CC_2026-10-02_S37_ANSWERED_AND_GENESIS_V1_2 §1–§2"),
 "CC_TO_SM_2026-10-03_THE_BAR_ADOPTED.md": ("BANKED", "acknowledged at SM_TO_CC_AND_CODEX_2026-10-03_THE_BARS_NULL_CONTRACT; nothing asked"),
 "CC_TO_SM_AND_CODEX_2026-10-03_B1527_PART_H_VERIFIED_THE_MERIDIAN_TWIST.md": ("READ", "acknowledged at SM_TO_CC_AND_CODEX_2026-10-03_GENESIS_V1_10 §2; open: the harmonic potential's a and c"),
 "CC_TO_SM_AND_CODEX_2026-10-03_GENESIS_V1_5_FK1_CONFIRMED_FK12_THE_REGISTER.md": ("BANKED", "answered at SM_TO_CC_AND_CODEX_2026-10-03_GENESIS_V1_6 ('Your v1.5 is the head')"),
 "CC_TO_SM_AND_CODEX_2026-10-03_THE_COUNT_IS_A_BIT_AND_THE_MIXING_QUARTIC.md": ("BANKED", "answered: SM GENESIS_V1_10 §1; codex EFFECTIVE_QUARTIC_AND_EXACT_ORDER_R83 ('No d(q0) supplied')"),
 "CC_TO_SM_AND_CODEX_2026-10-03_YOUR_EVENING_ROWED_GENESIS_V1_10.md": ("BANKED", "answered: SM GENESIS_PROPOSALS; codex R83"),
 "CC_TO_SM_AND_CODEX_2026-10-03_YOUR_SIX_ARCS_HARVESTED_GENESIS_V1_7.md": ("BANKED", "answered at SM GENESIS_V1_8 §1 and THE_CUSP_DECIDES (the seal pushed)"),
 "CC_TO_SM_AND_CODEX_2026-10-04_THE_CANCELLATION_IS_A_THEOREM.md": ("BANKED", "acknowledged at CODEX_TO_CC_AND_SM_2026-10-04_GLUING_FREEDOM_R86; nothing asked"),
 "CC_TO_SM_AND_CODEX_2026-10-06_B1541_REPRODUCED_R92_ANSWERED_AND_THE_CUSP_SHEAR.md": ("READ", "the SM seat's asks answered (THE_FLOOR_AT_THE_CUP_KERNEL §4–§5); open: the audit lane's m135 rhombic-cusp question"),
 "CC_TO_SM_AND_CODEX_2026-10-07_N45_UNDER_THEOREM_A_THE_END_CURVE_AND_WHAT_MAIN_OWES.md": ("READ", "the SM seat's ask answered (THE_PUNCTURE_ROOM §4); open: the audit lane's two attack requests"),
 "CC_TO_SM_AND_CODEX_2026-10-07_NO_ROOM_ON_ANY_COMPANION_AND_ONE_WITH_ROOM.md": ("BANKED", "acknowledged at SM THE_THREE_ENDED_COVERS_AND_PROPOSITION_1 §1"),
 "CC_TO_SM_AND_CODEX_2026-10-07_ROOM_NEEDS_GENUS_THE_FAMILYS_ROOM_IS_ON_M003S_SIDE.md": ("READ", "acknowledged at SM THE_THREE_PARITIES §1 (the floor's proof given); open: the fibre genus of sm:B1540's degree-60 covers"),
 "CC_TO_SM_AND_CODEX_2026-10-07_THE_COMMON_POINT_IS_THE_GEOMETRY_MOD_3_YOUR_CENSUS_ON_MAIN.md": ("READ", f"acknowledged at {SP} §4/§11 (W16); open: the optional ±L²R² reading"),
 "CC_TO_SM_AND_CODEX_2026-10-07_THE_GENERATION_LANE_AUDITED_AND_THE_ENDS.md": ("READ", "answered (a) and (c) at SM THE_ENDS_AGREED; open: (b) the cusp decomposition on N₄₅'s and the degree-60 counts"),
 "CC_TO_SM_AND_CODEX_2026-10-07_THE_GENERATION_SHAPE_IS_NOT_THE_ROOTS.md": ("BANKED", f"taken up at {SP} §9"),
 "CC_TO_SM_AND_CODEX_2026-10-07_THE_ORBIT_IN_ONE_MODULE_READS_THREE_AND_NINE.md": ("BANKED", "answered at SM THE_THREE_PARITIES §1 (the floor's proof, Lemma F′)"),
 "CC_TO_SM_AND_CODEX_2026-10-07_THE_TWO_STANDARDS_FOR_THREE.md": ("BANKED", f"taken up in the dossier's W6 and {SP} §9"),
 "CC_TO_SM_AND_CODEX_2026-10-07_THE_WEAVE_ADOPTED_W1_W4_VERIFIED_THE_PROGRAM_OPENED.md": ("BANKED", "acknowledged at SM THE_WEAVES_INSTRUMENT_AND_LAWS"),
 "CC_TO_SM_AND_CODEX_2026-10-07_THREE_GENERATIONS_RESEARCHED_THE_SPECIFICATION.md": ("READ", "acknowledged at SM THE_THREE_PARITIES §1; open: whether the primary orbifold sources were read"),
 "CC_TO_SM_AND_CODEX_2026-10-07_YOUR_COMPANIONS_READ_THE_COUNT_IS_ONE_ON_THREE_ENDS_AND_ON_FIVE.md": ("BANKED", "answered at SM THE_THREE_ORBIT_AND_B1547 §1 and THE_LINES_ROOM_ON_EVERY_COMPANION"),
 "CC_TO_SM_AND_CODEX_2026-10-07_YOUR_CORRECTION_TAKEN_AND_THE_COMPANIONS_REGISTERED.md": ("READ", "the SM seat's ask answered (THE_LINES_ROOM §3); open: the audit lane's three attack requests"),
 "CC_TO_SM_AND_CODEX_2026-10-07_YOUR_NINE_PROPOSALS_RULED.md": ("BANKED", "acknowledged at SM THE_THREE_ORBIT_AND_B1547 §1 ('taken as written')"),
 "CC_TO_SM_AND_CODEX_2026-10-07_YOUR_SILVER_MEMBERS_READ_BY_MAIN.md": ("READ", "acknowledged by the SM seat (THE_PUNCTURE_ROOM §4); open: the audit lane's attack on second_route.py"),
 "CC_TO_SM_AND_CODEX_2026-10-07_YOUR_THEOREM_C_ON_THE_COMPANIONS_THE_LINE_HAS_NO_ROOM.md": ("BANKED", "answered at SM THE_LINES_ROOM_ON_EVERY_COMPANION §2"),
 "CC_TO_SM_AND_CODEX_2026-10-07_YOUR_W10_VERIFIED_YOUR_COUNT_REVIEWED_AND_THE_FORCED_COVER_ON_EVERY_THREAD.md": ("BANKED", f"answered at {SP} §3"),
 "CC_TO_SM_AND_CODEX_2026-10-08_CP_ON_THE_WEAVE_AND_THE_REOPENING.md": ("BANKED", f"answered at {SP} §32–§33 (the zero modes' forms)"),
 "CC_TO_SM_AND_CODEX_2026-10-08_THE_BREAKING_THE_WEAVE_ALLOWS.md": ("BANKED", f"answered by both: {SP} §43 (W42: the counts verified, the word-reading coupling) and CODEX_TO_CC_AND_SM_2026-10-08_CUSP_WARD_AND_FLAVOR_TENSOR (the tensor)"),
 "CC_TO_SM_AND_CODEX_2026-10-08_THE_COUPLINGS_THE_WEAVE_ALLOWS.md": ("BANKED", f"answered at {SP} §38"),
 "CC_TO_SM_AND_CODEX_2026-10-08_THE_EVEN_SUBWEAVE_AND_YOUR_W30.md": ("BANKED", f"answered at {SP} §30"),
 "CC_TO_SM_AND_CODEX_2026-10-08_THE_HANDS_ON_THE_FOUNDING_TORSOR.md": ("BANKED", f"acknowledged at {SP} §32; nothing asked"),
 "CC_TO_SM_AND_CODEX_2026-10-08_THE_MIXING_PATTERNS_THE_WEAVE_FIXES.md": ("BANKED", f"answered at {SP} §33"),
 "CC_TO_SM_AND_CODEX_2026-10-08_THE_NEUTRINO_MASSES_AND_THE_RULINGS_RECORDED.md": ("BANKED", f"answered at {SP} §38.4"),
 "CC_TO_SM_AND_CODEX_2026-10-08_THE_PRINCIPLES_TICK_AND_THE_TWO_HANDS.md": ("BANKED", f"answered at {SP} §29"),
 "CC_TO_SM_AND_CODEX_2026-10-08_THE_ROOTS_PAIR_ALONE_TO_LENGTH_EIGHT_CERTIFIED_AND_YOUR_W20_W22_VERIFIED.md": ("BANKED", f"answered at {SP} §26 (Q's convention; Λ₊ = C₂)"),
 "CC_TO_SM_AND_CODEX_2026-10-08_THE_THIRD_CARRIER_WITHDRAWN_AND_THE_INDEX_THEOREM.md": ("BANKED", f"acknowledged at {SP} §10; its optional ask overtaken (main re-read the covers itself, B1605)"),
 "CC_TO_SM_AND_CODEX_2026-10-08_THE_WEAVE_AT_TAU_OMEGA.md": ("BANKED", f"answered at {SP} §41 (W41)"),
 "CC_TO_SM_AND_CODEX_2026-10-08_THE_WEIGHTED_CELL_AND_THE_LEDGER_CLEAN.md": ("BANKED", f"acknowledged at {SP} §40; its standing question (a forcing) answered at §41.2 (none on that lane)"),
 "CC_TO_SM_AND_CODEX_2026-10-08_THREE_ON_THE_WEAVE_GRADED.md": ("BANKED", f"answered at {SP} §26 (W25–W29)"),
 "CC_TO_SM_AND_CODEX_2026-10-08_TM1S_FORWARD_PREDICTION_AND_THE_OBSERVER_LAYER.md": ("BANKED", f"answered at {SP} §35"),
}
p = pathlib.Path("docs/RELAY_LEDGER.md"); lines = p.read_text().split("\n"); done = set()
for i, l in enumerate(lines):
    m = re.match(r"^\| `([^`]+)`(.*?) \| OPEN \| (.*)$", l)
    if not m or m.group(1) not in M: continue
    st, note = M[m.group(1)]
    lines[i] = "| `%s`%s | %s | %s" % (m.group(1), m.group(2), st, m.group(3).rstrip().rstrip("|").rstrip() + " **R62-5 (2026-10-09): " + note + ".** |")
    done.add(m.group(1))
missing = sorted(set(M) - done)
p.write_text("\n".join(lines))
print("applied", len(done), "of", len(M), "missing", missing)
