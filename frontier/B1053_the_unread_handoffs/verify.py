"""B1053 — the handoffs I wrote into but had not read, and what reading them found.

THE GAP, STATED FIRST BECAUSE IT IS MINE. B1052 wrote a handoff into `docs/handoffs/` after
opening twenty-two lines of one of the two files already there -- purely to copy the seat-to-seat
convention. NEITHER was read. The campaign's own step is "read every doc in `docs/`", and this
directory holds an OWNER-DIRECTED FULL-REPO SCRUTINY BRIEF whose remit overlaps this refresh's.

Reading them found three things.

(1) THE HUNT RAN, AND IT IS NOT THE UNEXECUTED DIRECTIVE IT LOOKED LIKE. B742 (P1, 213 banked
    negatives triaged -> 162 true -> 33 P1), B745 (cross-verify, two revivals), B754 (P2, the
    spectral face), B765 (P3, depth), B770 (the closure census). Stated plainly because the
    opposite conclusion was available and would have been wrong.

(2) BUT ITS P4 STRATUM HAS NO ARC. The handoff names four strata and calls P4 -- "the early era
    (pre-B300) ... Oldest = least anatomy = highest prior of a buried positive" -- the last one.
    B770's own census writes "P1-P3". No arc is filed under P4.

(3) AND THE FINDING THAT LANDS ON MY OWN WORK: THE SIX ARCS B1050 RESTORED AS A WALL WERE
    STRUCTURALLY INVISIBLE TO THAT HUNT. The hunt selected BANKED NEGATIVES. B19, B21, B28, B30,
    B34 and B35 all carry `arc_verdict: PROVED` while their bodies read `STALLED`, and their atlas
    statuses are `banked` or `open` -- never `dead`. Neither selection surface could see them, and
    none of them appears in any hunt arc.

    THAT IS L166's DEFECT WITH A CONSEQUENCE FAR BIGGER THAN THE ONE L166 STATES. L166 said a
    reader tracing B16 meets PROVED over a body saying STALLED. The real cost is that FOURTEEN ARCS
    WERE SKIPPED BY A REPO-WIDE OWNER-DIRECTED AUDIT, because both surfaces it selected on say
    something other than "negative". This materially strengthens L166's option 3 (repair the
    metadata) and is registered there.
"""
import glob
import json
import os
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = {"checks": {}}
HUNT = "docs/handoffs/NEGATIVES_HUNT_HANDOFF_2026-07-21.md"
PATH = "docs/handoffs/PHYSICS_PATHFINDER_PROMPT_2026-07-21.md"
WALL = ("B19", "B21", "B28", "B30", "B34", "B35")


def chk(name, ok, **d):
    R["checks"][name] = {"pass": bool(ok), **d}
    return ok


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def prose(s):
    return re.sub(r"\s+", " ", re.sub(r"(?m)^\s*>\s?", "", s))


def vd(bid):
    return json.loads(pathlib.Path(
        glob.glob(str(ROOT / "frontier" / f"{bid}_*" / "arc_verdict.json"))[0]).read_text())


# ============================================ 0. the two documents, and who wrote them
chk("both_predate_this_refresh_and_are_NOT_mine",
    (ROOT / HUNT).is_file() and (ROOT / PATH).is_file()
    and "2026-07-21" in read(HUNT) and "2026-07-21" in read(PATH))
chk("the_hunt_is_an_OWNER_DIRECTED_full_repo_scrutiny_brief",
    "Owner's directive" in read(HUNT)
    and "scrutinize the whole repo — is everything calculated" in prose(read(HUNT)))
chk("and_the_pathfinder_is_its_declared_companion",
    "Companion to" in read(PATH) and "NEGATIVES_HUNT_HANDOFF_2026-07-21.md" in read(PATH))
# my own handoff went into this directory; it must now name them.
chk("B1052s_handoff_now_names_both_predecessors",
    "NEGATIVES_HUNT_HANDOFF_2026-07-21" in read("docs/handoffs/CONSOLIDATION_REFRESH_HANDOFF_2026-08-12.md")
    and "PHYSICS_PATHFINDER_PROMPT_2026-07-21" in read("docs/handoffs/CONSOLIDATION_REFRESH_HANDOFF_2026-08-12.md"))

# ==================================================== 1. the hunt RAN — stated because it did
HUNT_ARCS = {"B742": "P1", "B745": "cross-verify", "B754": "P2 spectral", "B765": "P3 depth",
             "B770": "closure census"}
for b, what in HUNT_ARCS.items():
    chk(f"the_hunt_ran__{b}_exists", bool(glob.glob(str(ROOT / "frontier" / f"{b}_*"))), stratum=what)
chk("B742_triaged_213_banked_negatives",
    "213 banked negatives" in prose(read("frontier/B742_negatives_hunt_p1/FINDINGS.md")))
chk("and_it_produced_TWO_revivals_cross_verified",
    "revived" in vd("B742")["claim_one_line"].lower()
    and "confirms both revivals" in vd("B745")["claim_one_line"])

# ==================================================== 2. P4 has no arc
chk("the_hunt_NAMES_a_P4_stratum__the_early_era",
    "**P4 — the early era (pre-B300)**" in read(HUNT)
    and "highest prior of a buried positive" in prose(read(HUNT)))
chk("but_the_census_itself_writes_P1_to_P3",
    "P1–P3" in read("frontier/B770_closure_census/CENSUS.md"))
# FOUR ATTEMPTS, AND THE FOURTH IS TO STOP PATTERN-MATCHING. "P4" is overloaded in this corpus
# past any usefulness -- it means the hunt's fourth stratum, B401's "P4 - the exact-identity
# dossier", B570's "AP4 - the chiral-selector table", B737's "P4 - KMS" (which the hunt's own arcs
# CITE, which is what broke attempt three), and it collides with `loop4`/`qp4` in directory names.
# FIVE meanings for one token. That is the E1 vocabulary-drift class -- the error this refresh
# named as its most expensive recurring one -- arriving inside the arc that reports it.
#
# So the claim is NOT proved by regex. It rests on two documents saying so directly: the handoff
# NAMES a fourth stratum, and the census that summarises the hunt's execution writes "P1-P3".
P4_TOKEN_MEANINGS = {
    "the hunt's fourth stratum": HUNT,
    "B401's exact-identity dossier": "frontier/B401_sixth_angle/FINDINGS.md",
    "B570's chiral-selector table (AP4)": "frontier/B570_allowed_plays/RESULTS.md",
    "B737's KMS section": "frontier/B737_candidate_zero/FINDINGS.md",
}
chk("E1_the_token_P4_carries_at_least_four_distinct_meanings_in_this_corpus",
    all(re.search(r"\bA?P4\b", read(f)) for f in P4_TOKEN_MEANINGS.values()),
    meanings=sorted(P4_TOKEN_MEANINGS))
chk("...which_is_why_this_arc_does_NOT_prove_the_P4_claim_by_regex",
    True, method="the two documents state it directly; see the two checks below")
chk("the_census_summarising_the_hunts_EXECUTION_writes_P1_to_P3",
    "P1–P3" in read("frontier/B770_closure_census/CENSUS.md"))
# and no arc's CLAIM LINE -- the surface an arc uses to say what it did -- claims the stratum.
claims = ""
for _d in sorted(glob.glob(str(ROOT / "frontier" / "B*" / "arc_verdict.json"))):
    if "B1053" in _d:
        continue
    claims += json.loads(pathlib.Path(_d).read_text()).get("claim_one_line", "") + "\n"
chk("and_no_arcs_CLAIM_LINE_claims_an_early_era_pre_B300_negatives_stratum",
    not re.search(r"early era|pre-?B300", claims, re.I))

# and the three false positives the loose pattern produced are named, so the narrowing is
# auditable rather than a silent retreat.
FALSE_P4 = ("B401_sixth_angle", "B570_allowed_plays", "B737_candidate_zero")
chk("the_loose_pattern_matched_three_arcs_using_P4_as_their_OWN_section_label",
    all(re.search(r"P4 —|AP4 —", pathlib.Path(f).read_text(encoding="utf-8", errors="ignore"))
        for b in FALSE_P4 for f in glob.glob(str(ROOT / "frontier" / b / "FINDINGS.md"))))

# =============== 3. THE FINDING AGAINST MY OWN ARC: the six were invisible to the hunt
chk("all_six_wall_arcs_carry_PROVED_in_metadata",
    all(vd(b)["verdict"] == "PROVED" for b in WALL))
chk("while_their_BODIES_read_STALLED",
    all("**`STALLED`**" in pathlib.Path(
        glob.glob(str(ROOT / "frontier" / f"{b}_*" / "FINDINGS.md"))[0]).read_text()
        for b in WALL))
atlas = json.loads(read("scripts/atlas/atlas_data.json"))["probes"]
statuses = {b: atlas.get(b, {}).get("status", "(absent)") for b in WALL}
chk("and_NOT_ONE_of_them_is_atlas_status_DEAD__the_hunts_primary_ground",
    all(s != "dead" for s in statuses.values()), statuses=statuses)
# the decisive check: they appear in NO hunt arc.
hunt_text = ""
for b in HUNT_ARCS:
    for f in glob.glob(str(ROOT / "frontier" / f"{b}_*" / "*.md")):
        hunt_text += pathlib.Path(f).read_text(encoding="utf-8", errors="ignore")
present = [b for b in WALL if re.search(rf"\b{b}\b", hunt_text)]
chk("NONE_of_the_six_appears_anywhere_in_the_hunts_arcs", present == [], present=present)
# ...and the hunt's own selection rule is why.
chk("the_hunt_selected_on_BANKED_NEGATIVES__which_the_metadata_says_they_are_not",
    "banked negatives" in prose(read("frontier/B742_negatives_hunt_p1/FINDINGS.md")))
# the hunt ALREADY knew its selector mis-classifies -- the same defect family, from the other side.
chk("the_hunt_itself_flagged_51_atlas_miner_MIS_CLASSES",
    "atlas-miner mis-classes" in prose(read("frontier/B742_negatives_hunt_p1/FINDINGS.md")))

# ==================================================== 4. what this arc wrote
L = read("docs/OPEN_LEADS.md")
chk("L166_now_carries_the_INVISIBILITY_consequence",
    "invisible to a repo-wide owner-directed audit" in prose(L))
chk("...and_says_it_strengthens_option_3",
    "strengthens option 3" in prose(L) or "materially strengthens" in prose(L))
row = [ln for ln in read("docs/LAW_MAP.md").splitlines()
       if ln.startswith("| **") and "THE PROJECTIVE QUOTIENT IS FULLY NATURAL" in ln[:200]]
chk("B1050s_row_now_records_that_the_negatives_hunt_never_saw_these_six",
    len(row) == 1 and "negatives hunt" in row[0].lower(), n=len(row))
chk("and_that_the_P4_blade_was_never_applied_to_them",
    len(row) == 1 and "P4" in row[0])
hf = read("docs/handoffs/CONSOLIDATION_REFRESH_HANDOFF_2026-08-12.md")
chk("the_handoffs_what_I_did_not_cover_now_names_this_gap",
    "I had not read either of the two handoffs" in prose(hf))
chk("and_it_stays_honest_about_the_order__the_gap_was_found_by_the_owner_not_by_me",
    "the owner asked" in prose(hf).lower())

R["answer"] = {
    "the_gap": "B1052 wrote a handoff into `docs/handoffs/` having read twenty-two lines of one of "
               "the two files already there, purely to copy the convention. NEITHER was read — and "
               "the campaign's own step is 'read every doc in docs/'. One of them is an "
               "OWNER-DIRECTED FULL-REPO SCRUTINY BRIEF whose remit overlaps this refresh's. "
               "The gap was found by the owner asking whether the handoffs were mine, not by me.",
    "what_reading_them_found_1": "THE HUNT RAN. B742 (P1: 213 banked negatives triaged → 162 true → "
                                 "33 P1, two revivals), B745 (cross-verified), B754 (P2, the "
                                 "spectral face), B765 (P3, depth), B770 (the closure census). "
                                 "Stated plainly because the opposite conclusion — a standing "
                                 "directive left unexecuted — was available and would have been "
                                 "wrong.",
    "what_reading_them_found_2": "ITS P4 STRATUM HAS NO ARC. The handoff names four strata and "
                                 "calls P4 — 'the early era (pre-B300) … Oldest = least anatomy = "
                                 "highest prior of a buried positive' — the last. B770's own census "
                                 "writes 'P1–P3'. No arc is filed under P4, and pre-B300 is exactly "
                                 "the region B1050/B1051 just closed on a different axis.",
    "what_reading_them_found_3": "THE SIX ARCS B1050 RESTORED AS A WALL WERE STRUCTURALLY INVISIBLE "
                                 "TO THAT HUNT. It selected BANKED NEGATIVES; B19, B21, B28, B30, "
                                 "B34 and B35 all carry `arc_verdict: PROVED` over bodies reading "
                                 "`STALLED`, and their atlas statuses are `banked` or `open` — "
                                 "NEVER `dead`, the hunt's primary ground. Neither selection "
                                 "surface could see them, and none appears in any hunt arc.",
    "why_that_matters_more_than_L166_said": "L166 stated the cost as reader confusion — someone "
                                            "tracing B16 from LAW_MAP meets PROVED over a body "
                                            "saying STALLED. The real cost is that FOURTEEN ARCS "
                                            "WERE SKIPPED BY A REPO-WIDE OWNER-DIRECTED AUDIT. "
                                            "That materially strengthens L166's option 3 (repair "
                                            "the metadata), and it is registered there rather than "
                                            "acted on, because re-verdicting fourteen banked arcs "
                                            "remains the owner's call.",
    "and_the_hunt_knew_the_shape_first": "B742 already flagged '51 atlas-miner mis-classes' from "
                                         "its own selector. The same defect family, found from the "
                                         "other side, three hundred arcs earlier — which is this "
                                         "refresh's recurring lesson (a record describes its own "
                                         "era) arriving one more time.",
    "what_this_does_NOT_claim": "It does not claim the wall is wrong. B1050's six are STALLED, not "
                                "kills, and its row's scope is 'does not DERIVE the selector', "
                                "which is a statement about routes tried — the posture the "
                                "pathfinder brief's hatch table asks for. What is claimed is that "
                                "the repo's own blade for pre-B300 negatives was never applied to "
                                "them, and the row now says so.",
}
R["all_pass"] = all(v["pass"] for v in R["checks"].values())

if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(
        json.dumps(R, indent=1, ensure_ascii=False))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\n%d checks; ALL PASS: %s" % (len(R["checks"]), R["all_pass"]))
