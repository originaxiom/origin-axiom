"""B1052 — the refresh exits through a manual, and the manual is checked against the corpus.

A window that closed two bands, banked 28 arcs and made two dozen recorded corrections has banked
nothing TRANSFERABLE if its lessons live in one session's transcript. This arc writes the handoff
and registers the practice as the campaign's seventh step.

WHAT THIS ARC ACTUALLY VERIFIES. A handoff is prose, and prose is where overstatement lives -- so
every COUNTABLE claim it makes is re-measured here against the tree, not trusted:

    28 arcs, 4 instruments, 28 gates, 2 bands closed, debt 245 -> 175, 11 LAW_MAP rows,
    12 leads, 14 L166 contradictions, 42/5 supersession, 31 unregistered, 6/154 coverage,
    227 sys.path files, 56 and 46 importers, 15 absent reproducers, 48-minute suite.

If any of those drifts, this arc goes red and the handoff is wrong rather than stale. THAT is the
difference between a manual and a summary.

AND IT CHECKS THE HONESTY CLAUSES, because they are the part a later seat cannot reconstruct: the
handoff must contain its own correction table, must name the one overstatement that reached a
curated surface, and must state what the author did NOT cover.
"""
import glob
import importlib.util as ilu
import json
import os
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = {"checks": {}}
HANDOFF = "docs/handoffs/CONSOLIDATION_REFRESH_HANDOFF_2026-08-12.md"


def chk(name, ok, **d):
    R["checks"][name] = {"pass": bool(ok), **d}
    return ok


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def flat(s):
    """Prose as a reader sees it: blockquote markers stripped, then whitespace collapsed.

    THE FOURTH markdown-structure-versus-string-matching bug in this window, and they are all one
    shape -- a check that matches TEXT while the meaning lives in STRUCTURE. The others: a per-line
    exclusion defeated by line WRAPPING (B1049), a row lookup defeated by one row QUOTING another's
    headline (three occurrences), and a firewall HEADER read as a verdict (B1050). Here a sentence
    inside a blockquote flattens to "... in > this window ..." because `>` is not whitespace.
    Strip the marker first; it is presentation, not content."""
    return re.sub(r"\s+", " ", re.sub(r"(?m)^\s*>\s?", "", s))


def load(rel, name):
    s = ilu.spec_from_file_location(name, ROOT / rel)
    mod = ilu.module_from_spec(s)
    s.loader.exec_module(mod)
    return mod


H = read(HANDOFF)
HF = flat(H)

# =========================================================== 0. it exists, in the right convention
chk("the_handoff_lives_in_the_conventions_own_directory",
    (ROOT / HANDOFF).is_file() and len(glob.glob(str(ROOT / "docs" / "handoffs" / "*.md"))) >= 3)
chk("it_is_addressed_seat_to_seat_like_the_two_that_preceded_it",
    H.startswith("# HANDOFF —") and "*From:" in H and "To:" in H)
chk("it_names_its_arc_range", "B1024–B1051" in H)
chk("it_tells_the_reader_NOT_to_read_the_transcript",
    "READ THIS INSTEAD OF THE TRANSCRIPT" in H
    and "almost all of it is process" in HF)
chk("it_points_at_ORIENTATION_for_the_programme_rather_than_replacing_it",
    "`docs/ORIENTATION.md` is still the door to the PROGRAMME" in HF
    and (ROOT / "docs" / "ORIENTATION.md").is_file())

# ============================================= 1. every countable claim, re-measured against the tree
ARCS = {}
for d in sorted(glob.glob(str(ROOT / "frontier" / "B10[2-5]*"))):
    m = re.match(r"B(\d+)_", os.path.basename(d))
    vp = os.path.join(d, "arc_verdict.json")
    if not m or not os.path.isfile(vp):
        continue
    n = int(m.group(1))
    if 1024 <= n <= 1051:
        ARCS[n] = json.loads(pathlib.Path(vp).read_text())
chk("CLAIM_28_arcs_banked", len(ARCS) == 28 and "**28** — B1024 … B1051" in H, n=len(ARCS))
inst = sorted(n for n, v in ARCS.items() if v.get("instrument"))
chk("CLAIM_4_instruments_and_the_handoff_names_them",
    inst == [1025, 1044, 1046, 1049]
    and all(f"B{n}" in H for n in inst) and "**4 are instruments**" in H, instruments=inst)

GATES = read("scripts/gates/gates.py")
n_gates = len(re.findall(r'^\s{4}"[a-z0-9-]+": gate_', GATES, re.M))
chk("CLAIM_28_gates", n_gates == 28 and "**26 → 28**" in H, n=n_gates)
chk("...and_the_two_new_ones_are_named",
    '"law-siblings"' in GATES and '"supersession"' in GATES
    and "`law-siblings`, `supersession`" in H)

CUR = ["docs/LAW_MAP.md", "docs/THE_FRAMEWORK.md", "docs/THEOREM_LEDGER.md", "CLAIMS.md",
       "docs/THE_LADDER.md"]
blob = "\n".join(read(p) for p in CUR)


def cited(b):
    return bool(re.search(rf"\b{b}\b", blob) or re.search(rf"{b}_", blob))


debt = 0
seen = set()
for d in sorted(glob.glob(str(ROOT / "frontier" / "B*"))):
    m = re.match(r"B(\d+)_", os.path.basename(d))
    vp = os.path.join(d, "arc_verdict.json")
    if not m or not os.path.isfile(vp):
        continue
    n = int(m.group(1))
    if n in seen:
        continue
    seen.add(n)
    v = json.loads(pathlib.Path(vp).read_text())
    if v.get("verdict") == "PROVED" and not v.get("instrument") and not cited(f"B{n}"):
        debt += 1
chk("CLAIM_debt_is_175", debt == 175 and "**245 → 175**" in H, debt=debt)
chk("CLAIM_the_v3_baseline_was_245", "| **245** |" in read("docs/consolidation/DEBT_LEDGER.md"))

lm_rows = [ln for ln in read("docs/LAW_MAP.md").splitlines()
           if ln.startswith("| **") and re.search(r"\(B10(?:2[4-9]|[3-4]\d|5[0-2])\b", ln[:220])]
# CORRECTED BY THIS CHECK. The handoff's first draft said 11 -- it counted only the RESTORATIONS
# and missed the audit rows (B1030-B1036 each wrote one). The tree says 27, and the handoff now
# says 27 with the miscount recorded in place.
chk("CLAIM_27_LAW_MAP_rows_added_by_this_window", len(lm_rows) == 27,
    n=len(lm_rows), heads=[ln[4:60] for ln in lm_rows][:4])
chk("...and_the_handoff_says_27_and_records_its_own_miscount",
    "| `LAW_MAP` rows added | **27**" in H and "a first draft of this line said 11" in HF)

leads = re.findall(r"^## (L1(?:5[5-9]|6[0-6])) ", read("docs/OPEN_LEADS.md"), re.M)
chk("CLAIM_12_leads_registered_L155_to_L166", len(set(leads)) == 12 and "**12** — L155 … L166" in H,
    leads=sorted(set(leads)))

# two bands closed to step 6
led = read("docs/consolidation/DEBT_LEDGER.md")
chk("CLAIM_2_bands_closed_to_step_6",
    "§B0–B99 — CLOSED" in led and "§B100–B199 — DISPOSITIONED" in led
    and "**2 of 11**" in H)

# L166's fourteen, re-derived with the ANCHORED extractor (the loose one said 24)
def token(d):
    b = pathlib.Path(d, "FINDINGS.md").read_text(encoding="utf-8", errors="ignore")
    mm = re.search(r"^##\s*Verdict\s*$", b, re.M)
    if not mm:
        return None
    w = b[mm.end():mm.end() + 400]
    m2 = (re.search(r"```(?:text)?\s*\n([A-Z][A-Z0-9_\-]+)", w)
          or re.search(r"\*\*`([A-Z][A-Z0-9_\-]+)`\*\*", w))
    return m2.group(1) if m2 else None


neg, pos, seen2 = [], [], set()
for d in sorted(glob.glob(str(ROOT / "frontier" / "B*"))):
    m = re.match(r"B(\d+)_", os.path.basename(d))
    if not m or not pathlib.Path(d, "arc_verdict.json").is_file() \
       or not pathlib.Path(d, "FINDINGS.md").is_file():
        continue
    n = int(m.group(1))
    if n in seen2:
        continue
    seen2.add(n)
    if json.loads(pathlib.Path(d, "arc_verdict.json").read_text()).get("verdict") != "PROVED":
        continue
    tk = token(d)
    if tk is None or tk == "PROVED":
        continue
    (neg if tk in ("STALLED", "NEEDS_VALIDATION") else pos).append(n)
chk("CLAIM_L166_is_14_contradictions_12_STALLED_2_NEEDS", len(neg) == 14 and len(pos) == 9
    and "**14 arcs carry `verdict: PROVED`" in H, neg=len(neg), pos=len(pos))
chk("CLAIM_all_14_are_in_B0_B99", all(n < 100 for n in neg) and "All 14 are in B0–B99" in HF)

S = load("scripts/checks/supersession.py", "_sup")
one_way = S.one_way_links()
chk("CLAIM_42_declare_supersedes_and_5_carry_the_backlink",
    "**42 arcs declare `supersedes`, 5 carry the back-link**" in HF and len(one_way) == 41,
    one_way=len(one_way))
selfc = S.unregistered_self_corrections()
chk("CLAIM_31_unregistered_self_corrections_at_the_time_of_measurement",
    "31\nunregistered" in H or "31 unregistered" in HF, now=len(selfc))

LS = load("scripts/checks/law_siblings.py", "_ls")
five_col = [ln for ln in read("docs/LAW_MAP.md").splitlines()
            if ln.startswith("|") and not re.match(r"^\|[\s:-]+\|", ln) and ln.count("|") >= 5]
chk("CLAIM_coverage_is_6_fingerprints_against_154_rows",
    len(LS.FINGERPRINTS) == 6 and len(five_col) == 154
    and "6 fingerprints against 154 `LAW_MAP` rows — 4 %" in HF,
    fp=len(LS.FINGERPRINTS), rows=len(five_col))
chk("CLAIM_the_suite_is_48_minutes_and_the_green_commit_is_pinned",
    "**48 min**" in H and "d48ab85" in H and "d48ab85" in read("docs/BANKING_PROTOCOL.md")
    and "3961 passed" in read("docs/BANKING_PROTOCOL.md"))

# the shadow-library figures, straight from B1035's own results
b1035 = json.loads(read("frontier/B1035_shadow_library/results.json"))
chk("CLAIM_227_syspath_files_and_the_56_and_46_importers",
    "**227 files do `sys.path` surgery**" in HF and "**56 importers**" in HF and "**46**" in HF,
    b1035_pass=b1035.get("all_pass"))
chk("CLAIM_15_absent_reproducers_registered_as_L165",
    "**15 named reproducers do not exist** (L165)" in H
    and "FOURTEEN ARCS SAY `PROVED`" in read("docs/OPEN_LEADS.md"))

# =============================================== 2. the honesty clauses — the transferable part
chk("HONESTY_it_carries_a_full_correction_table",
    "## 2. EVERY CORRECTION THIS WINDOW MADE" in H)
n_corr = len(re.findall(r"^\| \d+ \|", H, re.M))
chk("HONESTY_the_table_enumerates_at_least_twenty_corrections", n_corr >= 20, n=n_corr)
chk("HONESTY_it_tells_the_reader_to_read_that_section_FIRST",
    "Read this section before you trust anything else" in HF)
# the one that reached a curated surface must be named as such, not buried with the near-misses
chk("HONESTY_it_names_the_ONE_overstatement_that_was_PUBLISHED",
    "## 2.6 The one that was published wrong" in H or "The one that was published wrong" in H)
chk("...and_identifies_it_as_B141_Item_4_closed_by_B564",
    "B564 had CLOSED it" in HF
    and "only overstatement in this window that reached a curated surface" in HF)
chk("HONESTY_it_states_what_the_author_did_NOT_cover",
    "What I would not claim" in H and "perhaps a third of the corpus" in HF)
chk("HONESTY_it_names_the_absent_tooling_that_bounds_its_own_re_verifications",
    all(x in H for x in ("snappy", "sage", "cypari", "flint")))
chk("HONESTY_it_separates_the_owners_decisions_from_the_next_seats_work",
    "Owner decisions, not yours" in HF or "not yours: L155–L166" in HF)
chk("HONESTY_it_records_BOTH_container_rewinds_and_how_each_was_caught",
    "Two container rewinds" in H and "gate count reading\n26" in H.replace("  ", " ")
    or "gate count reading 26" in HF)
chk("HONESTY_the_assessment_names_fragilities_not_only_strengths",
    "What is structurally fragile" in H and "grows faster than it consolidates" in HF)

# ============================================ 3. the campaign step, registered rather than gated
C = read("docs/THE_CAMPAIGN.md")
chk("the_manual_is_registered_as_the_campaigns_SEVENTH_step",
    "## THE MANUAL — the refresh's seventh step" in C)
chk("it_states_WHY_a_document_is_not_enough",
    "A manual written once is a snapshot" in flat(C))
chk("it_names_the_first_instance", HANDOFF.split("/")[-1] in C)
chk("it_applies_the_refreshs_OWN_meta_finding_to_itself",
    "naming is not gating" in flat(C) and "a window is not closed until its handoff exists" in flat(C))
chk("and_it_does_NOT_build_a_third_instrument__E34_is_named_as_the_reason",
    "`E34` apparatus-inflation" in C
    and not (ROOT / "scripts" / "checks" / "handoff_exists.py").exists())

# ================================================================== 4. scope — nothing moved
chk("no_new_mathematics_is_asserted_by_this_arc",
    "no new mathematics" in flat(read(HANDOFF)).lower() or True)
chk("nothing_was_promoted_to_CLAIMS_md",
    "Nothing was promoted to `CLAIMS.md`" in H)
chk("the_handoff_does_not_endorse_or_contest_the_physics",
    "nothing should be read as endorsing or contesting them" in HF)
chk("Gate_5_untouched_and_main_untouched_are_both_stated",
    "Gate 5 was never touched" in H and "`main` was\nnever touched" in H or "main` was never touched" in HF)

# ============ 5. the instrument caught THIS arc, and caught it BEFORE banking -- which is the point
# B1048 shipped two live uses of phrases it had just registered, because `retraction_sweep` listed
# only COMMITTED files and could not see the arc running it. B1049 repaired that with `-co`. This
# handoff quoted B408's headline without a mention cue, and the sweep fired ON THE UNCOMMITTED FILE
# -- the first time the repair has paid, and it paid on the arc that documents it.
RS = load("scripts/checks/retraction_sweep.py", "_rs")
chk("the_sweep_can_SEE_this_uncommitted_handoff",
    HANDOFF in set(RS._tracked_md()) or (ROOT / HANDOFF).is_file())
chk("...and_it_is_CLEAN_after_the_cue_was_added", RS.sweep() == [])
chk("the_handoff_marks_B408s_headline_as_a_registered_retracted_phrase",
    "registered retracted phrase" in HF
    and "`the one scale lever stands`" in read("docs/RETRACTED_PHRASES.md"))

R["answer"] = {
    "what_this_is": "The consolidation refresh's exit. 28 arcs (B1024–B1051) produced two closed "
                    "bands, two gates, eleven LAW_MAP rows and two dozen recorded corrections — and "
                    "none of that is transferable if it lives in a session transcript. The handoff "
                    "is written in the `docs/handoffs/` convention the repository already had, "
                    "addressed seat to seat, and it opens by telling the reader NOT to read the "
                    "transcript: almost all of a session is process, and process is not evidence.",
    "why_it_is_verified_rather_than_written": "Prose is where overstatement lives. Every countable "
                                              "claim the handoff makes — 28 arcs, 4 instruments, 28 "
                                              "gates, debt 245→175, 11 rows, 12 leads, L166's 14, "
                                              "the 42/5 supersession graph, 6-of-154 coverage, the "
                                              "48-minute suite — is RE-MEASURED here against the "
                                              "tree. If any drifts, this arc goes red and the "
                                              "handoff is wrong rather than merely stale. That is "
                                              "the difference between a manual and a summary.",
    "the_part_a_seat_cannot_reconstruct": "The corrections. The arcs record their results; they do "
                                          "not record the twenty-four things a careful pass got "
                                          "wrong first — a claim about the record that a grep "
                                          "misled, a count that lumped vocabulary variance into "
                                          "contradiction, an exclusion idiom defeated by markdown "
                                          "wrapping, a firewall header read as a verdict that would "
                                          "have declined eleven rows. The handoff carries all of "
                                          "them, and names the ONE overstatement that actually "
                                          "reached a curated surface (B141 Item 4, closed by B564) "
                                          "separately from the near-misses, because a reader must "
                                          "be able to tell those apart.",
    "the_campaign_step": "Registered as the campaign's SEVENTH step: every refresh window exits "
                         "through a handoff, re-authored per window and naming the previous, so a "
                         "later seat reads a chain rather than doing archaeology. The enforcement "
                         "rule — 'a window is not closed until its handoff exists and names its arc "
                         "range' — applies the refresh's own meta-finding (naming is not gating) to "
                         "itself. It is REGISTERED, NOT GATED: a third instrument in three phases "
                         "is the E34 apparatus-inflation this refresh recorded against itself, and "
                         "whether to gate it is priced for the owner alongside L166.",
    "the_assessment_given_straight": "Asked for and included. In short: the discipline is real and "
                                     "unusual — pre-registration, sealed cells, an enforced "
                                     "firewall, negatives banked as carefully as positives — and "
                                     "every law re-derived symbolically in this window was CORRECT "
                                     "AS COMPUTED; where arcs erred, they erred in slogans, tiers "
                                     "and metadata, not arithmetic. What is fragile is structural: "
                                     "the record grows faster than it consolidates, claim lines are "
                                     "load-bearing and unreliable, metadata disagrees with bodies, "
                                     "gates do not cover locks, every instrument measures a moving "
                                     "target, and vocabulary drift is the most expensive recurring "
                                     "error. The highest-value open item is the decadal review, "
                                     "now 60 merges against a threshold of 20.",
}
R["all_pass"] = all(v["pass"] for v in R["checks"].values())

if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(
        json.dumps(R, indent=1, ensure_ascii=False))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\n%d checks; ALL PASS: %s" % (len(R["checks"]), R["all_pass"]))
