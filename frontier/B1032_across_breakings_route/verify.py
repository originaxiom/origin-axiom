"""B1032 — the across-breakings generation route, and the correction of B1031's own rung.

The B800-B1024 claim-line sweep (this arc's occasion) surfaced a four-arc cluster — B885, B889,
B890, B891 — carried by NO curated consolidation under any of six names. It is a SECOND route to
generation multiplicity, untouched by B307's theorem, with TWO SEALED CELLS already run on it.

That contradicts a sentence B1031 wrote one arc earlier: *"the relational route via B302's
commensurator ℤ/3 is the only one B307 leaves open, and no arc runs it end to end."* The first
clause is false. Corrected here, in the same file that carries the rung.
"""
import glob
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = {"checks": {}}


def chk(name, ok, **d):
    R["checks"][name] = {"pass": bool(ok), **d}
    return ok


def verdict(bid):
    p = glob.glob(str(ROOT / "frontier" / f"{bid}_*" / "arc_verdict.json"))
    if not p:
        return None, ""
    d = json.loads(pathlib.Path(p[0]).read_text())
    return d.get("verdict"), d.get("claim_one_line") or ""


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


CURATED = ["docs/LAW_MAP.md", "docs/THE_FRAMEWORK.md", "docs/THEOREM_LEDGER.md", "CLAIMS.md",
           "docs/THE_LADDER.md", "docs/THE_SM_VERDICT.md"]
GENERATED = ["docs/views/VERDICT_LEDGER.md", "docs/OPEN_LEADS.md", "docs/CAMPAIGN_STATUS.md",
             "docs/progress/REVIEWS.md"]
CLUSTER = ("B885", "B889", "B890", "B891")

# ---------------------------------------------------------- 1. the cluster exists and is PROVED
for b in CLUSTER:
    v, c = verdict(b)
    chk(f"{b}_is_PROVED", v == "PROVED", claim=c[:160])

_, c890 = verdict("B890")
_, c891 = verdict("B891")
chk("b890_is_a_sealed_cell_returning_DISTINCT",
    "SEALED" in c890.upper() and "DISTINCT IN ALL THREE FRAMES" in c890.upper())
chk("b891_is_a_sealed_cell_returning_DISTINCT",
    "SEALED" in c891.upper() and "DISTINCT IN ALL THREE FRAMES" in c891.upper())

# B890 banked AGAINST its disclosed prior — the programme's strongest evidence shape.
f890 = read("frontier/B890_foreign_pair/FINDINGS.md")
chk("b890_banked_against_its_disclosed_prior",
    "The disclosed prior was WRONG" in f890 and "prereg disclosed the expectation EQUAL" in f890)
chk("b890_states_the_operational_point",
    "does NOT\ntranslate into operational indistinguishability" in f890
    or "does NOT translate into operational indistinguishability" in re.sub(r"\s+", " ", f890))

f891 = read("frontier/B891_matter_extension/FINDINGS.md")
chk("b891_extends_the_result_to_matter",
    "three\npairwise-distinguishable matter sectors" in f891
    or "three pairwise-distinguishable matter sectors" in re.sub(r"\s+", " ", f891))

# Both cells keep the SAME declared fence. The route is a candidate, not a mechanism.
for b, f in (("B890", f890), ("B891", f891)):
    chk(f"{b}_keeps_the_solo_seats_fence", "fence" in f and "STANDS" in f.upper())

# --------------------- 2. the cluster is carried by NO curated surface, under SIX distinct names
def without_this_arc(rel):
    """Drop the rows this arc wrote (the corrected X33 rung, and anything citing B1032).

    FOURTH instance of one hazard in three arcs: a consolidation arc that both MEASURES a gap and
    FILLS it invalidates its own metric unless the measurement is scoped by AUTHORSHIP. B1030 hit
    it once, B1031 twice. It is now the default shape here rather than a repair.

    WIDENED 2026-08-11 (B1042). The original exclusion dropped only rows naming B1032 itself --
    which scopes the arc out of its own measurement but NOT the arcs that come after it. B1042's
    currency read on THE_SM_VERDICT cited this very cluster (B885 -> B889 -> B890 -> B891) as a
    live second route, and this check went red: the gap had been FILLED, correctly, by a later
    arc. That is the eleventh instance of the same hazard and the first caught by a LOCK rather
    than by the author. The exclusion is now "this arc AND EVERY LATER ONE" -- B1037's pattern --
    so the published figure means "as at B1032", which is what it always claimed.
    """
    AFTER = re.compile(r"\bB10(?:3[2-9]|[4-9]\d)\b")   # this arc AND EVERY LATER ONE
    return "\n".join(ln for ln in read(rel).splitlines()
                     if not AFTER.search(ln) and "**X33**" not in ln)


blob = "\n".join(without_this_arc(p) for p in CURATED)
absent = [b for b in CLUSTER
          if not (re.search(rf"\b{b}\b", blob) or re.search(rf"{b}_", blob))]
# CORRECTED BEFORE PUBLICATION, by this script, against this script's author. The first draft
# asserted all FOUR were curated-absent. B885 -- the cluster's FOUNDATION -- is cited by LAW_MAP
# ("THE INTER-BREAKING LAWS") and THEOREM_LEDGER. The true shape is sharper: the foundation is
# distilled and everything BUILT ON IT is not. Consolidation stops exactly where the sealed
# results begin.
chk("the_foundation_B885_IS_curated", "B885" not in absent)
chk("the_three_arcs_built_on_it_were_curated_absent_before_this_arc",
    sorted(absent) == ["B889", "B890", "B891"], absent=absent)

# Topic names for the part built ON B885 -- deliberately excluding "inter-breaking", which is
# B885's own curated row.
NAMES = ("across-breakings", "generations-as-sectors", "three frames", "foreign vacu",
         "foreign 16", "registerably distinct")
found = [n for n in NAMES if re.search(re.escape(n), blob, re.I)]
chk("nor_under_any_of_six_topic_names", found == [], found=found)
chk("and_this_arc_is_what_puts_it_on_a_curated_surface",
    all(b in read("docs/THE_LADDER.md") for b in CLUSTER))

# ...but it IS carried by the generated tier. Reachable, not distilled — the two-tier distinction
# this refresh already had to retract a headline over.
gblob = "\n".join(read(p) for p in GENERATED)
carried = [b for b in CLUSTER if re.search(rf"\b{b}\b", gblob)]
chk("but_the_generated_tier_carries_it", sorted(carried) == sorted(CLUSTER), carried=carried)

# ------------------------- 3. THE CORRECTION: B307 does not touch this route, so it is not "the only one"
_, c307 = verdict("B307")
chk("b307_scopes_itself_to_the_trace_field_of_a_single_knot",
    "trace field" in c307 and "single-knot route" in c307, claim=c307[:200])
# nothing in the cluster is a trace-field statement — B307's hypothesis simply does not apply
cluster_claims = " ".join(verdict(b)[1] for b in CLUSTER)
chk("the_cluster_makes_no_trace_field_claim",
    not re.search(r"trace field", cluster_claims, re.I))

ladder = read("docs/THE_LADDER.md")
chk("the_withdrawn_only_one_sentence_is_gone",
    "is the only one\nB307 leaves open" not in ladder
    and "is the only one B307 leaves open" not in re.sub(r"\s+", " ", ladder))
flat_ladder = re.sub(r"\s+", " ", ladder)
chk("x33_now_names_two_routes",
    "TWO routes B307 leaves open" in flat_ladder)
chk("x33_now_cites_the_cluster",
    all(b in flat_ladder for b in ("B889", "B890", "B891")))
chk("x33_keeps_the_fence_that_both_sealed_cells_declared",
    "registerable distinctness is not mechanism-hood" in flat_ladder)

R["answer"] = {
    "the_cluster": "B885 (the inter-breaking dictionary: two structural laws, zeros at 1e-21) → "
                   "B889 (the canonical across-breakings dictionary; the vacuum→frame "
                   "identification is a COMPUTED BIJECTION — the S₃ torsor of frames realized as "
                   "three labeled lines in the 27) → B890 (SEALED: the foreign VACUA are DISTINCT "
                   "in all three frames, decisively above the sealed 1e-6 band, AGAINST the "
                   "disclosed prior EQUAL) → B891 (SEALED: the foreign 16s are DISTINCT too — one "
                   "observer registers three pairwise-distinguishable MATTER sectors on one 27).",
    "why_it_matters": "B307 closes the single-knot TRACE-FIELD route to three generations. This "
                      "route is not a trace-field statement at all, so B307's hypothesis does not "
                      "apply to it. It is a second live route to multiplicity, and unlike the "
                      "commensurator route it has TWO SEALED CELLS already run on it.",
    "the_fence_both_cells_declared": "Registerable distinctness is NOT mechanism-hood. The three "
                                     "16s OVERLAP on one 27 — they are not direct summands — and "
                                     "replication with identical gauge behaviour is what "
                                     "'generations' means. Both cells state this and neither "
                                     "claims more.",
    "the_correction": "B1031's rung X33 wrote 'the relational route via B302's commensurator ℤ/3 "
                      "is the only one B307 leaves open, and no arc runs it end to end.' The first "
                      "clause is FALSE and is withdrawn: there are two, and the second has two "
                      "sealed cells on it. The second clause survives for BOTH routes — neither "
                      "runs to mechanism-hood — and is restated per route.",
    "the_consolidation_finding": "The cluster's FOUNDATION is curated — B885's inter-breaking laws "
                                 "have a LAW_MAP row and a THEOREM_LEDGER entry. Everything BUILT "
                                 "ON IT is not: B889's computed bijection and the two SEALED cells "
                                 "B890/B891 — one of them banking against its own disclosed prior "
                                 "— appear on NO curated surface under any of six topic names, "
                                 "while the generated tier carries all three. Consolidation stops "
                                 "exactly where the sealed results begin. (This row is itself a "
                                 "correction: the first draft said all four were absent, and this "
                                 "script's own check refuted it before publication.)",
}
R["all_pass"] = all(v["pass"] for v in R["checks"].values())

if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(
        json.dumps(R, indent=1, ensure_ascii=False))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\nALL PASS:", R["all_pass"])
