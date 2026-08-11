"""B1030 — the counted input list, audited mechanically against its own banked sources.

The question this answers, in the owner's words: *is "zero dimensionless inputs" proven, and are
all the inputs anchors for things the object provably cannot contain?*

Nothing here is mathematics. Every check reads a BANKED artifact (B1000's `results.json`, B1015's
sealed DECLARATION, B1017's FINDINGS) or a curated surface, and diffs them against each other.
That is the whole method: the three convention collisions this refresh has found were all found
by diffing two surfaces rather than by reading either one.
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = {"checks": {}}


def chk(name, ok, **detail):
    R["checks"][name] = {"pass": bool(ok), **detail}
    return ok


# ---------------------------------------------------------------- the sources
B1000 = json.loads((ROOT / "frontier/B1000_input_count/results.json").read_text())
CLAIM = (ROOT / "docs/THE_CLAIM.md").read_text()
DECL = (ROOT / "frontier/B1015_anchor_declaration/DECLARATION.md").read_text()
B1017 = (ROOT / "frontier/B1017_recount/FINDINGS.md").read_text()


def flat(s):
    """Markdown hard-wraps at 100 columns and prefixes blockquote lines with '> '. Every phrase
    checked below is a SENTENCE, not a line, so it must be matched against the unwrapped text —
    the first run of this script reported two false negatives for exactly this reason."""
    return re.sub(r"\s+", " ", s.replace("\n> ", "\n"))

# ------------------------------------------------------- 1. B1000's own census
closings = list(B1000["closings"])
artifacts = list(B1000["artifacts"])
chk("b1000_census_is_five_closings_three_artifacts",
    len(closings) == 5 and len(artifacts) == 3,
    closings=closings, artifacts=artifacts)

# The doctrine the owner's sentence states, and the exact extent to which B1000 confirms it:
# every closing is a deficit of the object; every ARTIFACT is not.
chk("b1000_grades_the_6d_type_an_artifact_not_a_closing",
    "the 6d type" in artifacts and "the 6d type" not in closings,
    grade=B1000["classification"]["the 6d type"])
chk("b1000_grades_the_4d_lift_a_closing_in_the_space_sector",
    "4d / the N=2->N=1 datum" in closings,
    grade=B1000["classification"]["4d / the N=2->N=1 datum"])
chk("b1000_closes_four_incompletenesses_with_five_closings",
    B1000["incompletenesses_closed"] == 4 and len(closings) == 5,
    by_incompleteness={k: v for k, v in B1000["by_incompleteness"].items()})

# ------------------------------------- 2. THE_CLAIM's hypothesis list, as written
hypo = re.search(r"plus \*\*five\*\* typed external data.*?(?=\n>\s*\n)", CLAIM, re.S)
hypo_text = hypo.group(0) if hypo else ""
chk("the_claim_hypothesis_list_is_five_typed_external_data", bool(hypo_text))

# Its members, by the words THE_CLAIM itself uses.
hf = flat(hypo_text)
in_claim = {
    "time's arrow": "time's arrow" in hf,
    "chirality": "chirality" in hf,
    "one scale": "one scale" in hf,
    "the 6d type": "the 6d type J" in hf,
    "the rank-closing VEV direction": "rank-closing VEV" in hf,
}
chk("the_claim_list_names_all_five_of_its_own_members", all(in_claim.values()), members=in_claim)
chk("the_claim_list_names_the_6d_type", in_claim["the 6d type"], hypothesis=hf.strip()[:400])
# and it asserts the same agreement B1017 asserted, inside the hypothesis paragraph itself
chk("the_claim_asserts_b1000s_five_closings_stand",
    "B1000's census of five closings stands" in hf)

# THE FINDING. B1000's census counts a space closing; THE_CLAIM's counted hypothesis list has no
# such member. Checked on the hypothesis paragraph AND on the body outside this arc's own note —
# the note added by B1030 names the 4d lift in order to flag its absence, so a whole-file search
# would now report the finding as absent because the finding was written down. (That is not a
# hypothetical: the first run of this check failed for exactly that reason.)
SPACE_WORDS = ("N=2", "4d lift", "4d / the", "the 4d", "filling", "space sector")
body = CLAIM.split("**four → five here, 2026-08-11, B1030.**")[0]
chk("the_claim_hypothesis_list_names_no_space_closing",
    [w for w in SPACE_WORDS if w in hf] == [], found=[w for w in SPACE_WORDS if w in hf])
chk("the_claim_body_named_no_space_closing_before_this_arc",
    [w for w in SPACE_WORDS if w in body] == [], found=[w for w in SPACE_WORDS if w in body])

# So the two fives are different fives: same cardinality, one member swapped.
swapped_in = "the 6d type"      # in THE_CLAIM's list; ARTIFACT per B1000
swapped_out = "4d / the N=2->N=1 datum"   # CLOSING per B1000; absent from THE_CLAIM
chk("the_two_fives_are_different_fives",
    swapped_in in artifacts and swapped_out in closings
    and in_claim["the 6d type"] and not [w for w in SPACE_WORDS if w in hf],
    claim_list_has=swapped_in, b1000_grade_of_it="ARTIFACT",
    b1000_closing_missing_from_claim=swapped_out)

# ------------------------------- 3. and B1017 asserted the two agree, in terms
chk("b1017_asserts_it_confirms_b1000s_census",
    "B1000's five-closings census (confirmed)" in flat(B1017))
chk("b1017s_own_resource_table_spends_the_lie_type_on_the_6d_type",
    re.search(r"\|\s*Lie type\s*\|.*?\|\s*the 6d type J\s*\|", B1017) is not None)
chk("b1017s_resource_table_assigns_no_resource_to_space",
    not re.search(r"\|[^|\n]*(space|4d|N=2)[^|\n]*\|", B1017))

# --------------------------------------- 4. the dimensionless typing, verbatim
chk("b1015_types_the_bits_and_lie_type_as_discrete",
    "𝔽₂ bits and the Lie type are discrete" in flat(DECL))
chk("b1015_names_exactly_ONE_continuous_dimensionless_input",
    "the one continuous dimensionless input is A2" in flat(DECL))
chk("b1015_A2_is_an_ANCHOR_not_a_derived_value",
    "A2 (dimensionless frame)" in flat(DECL) and "UNQUANTIZED" in DECL)
chk("b1017_types_the_vev_direction_as_not_a_continuous_parameter",
    "orbit-valued, not a continuous dimensionless parameter" in flat(B1017))

# The count the owner's sentence is really about, assembled from the above and nothing else.
typing = {
    "dimensionful": ["one scale (= A1)"],
    "dimensionless_DISCRETE": ["𝔽₂ bit A (time's arrow)", "𝔽₂ bit B (chirality)",
                               "the Lie type", "the rank-closing VEV direction (orbit-valued)"],
    "dimensionless_CONTINUOUS": ["A2 = c = 6σ (declared anchor, priced; L154 would derive it)"],
}
chk("dimensionless_inputs_is_FOUR_not_zero", len(typing["dimensionless_DISCRETE"]) == 4)
chk("continuous_dimensionless_inputs_is_ONE_not_zero",
    len(typing["dimensionless_CONTINUOUS"]) == 1)

# ------------------------------ 5. Tier 4 is the whole-programme grade, and it is NOT DONE
WWC = (ROOT / "docs/WHAT_WOULD_COUNT.md").read_text()
chk("tier4_parameter_free_is_graded_NOT_DONE",
    re.search(r"Tier 4 — parameter-free.*?STATUS:\s*\*?\*?NOT DONE", WWC, re.S) is not None)
chk("no_arc_may_claim_parameter_free",
    "No arc claims 'parameter-free'" in WWC or 'No arc claims "parameter-free"' in WWC)
chk("parameter_free_means_zero_FREE_dimensionless_parameters",
    "zero *free* dimensionless parameters" in CLAIM)

# ----------------------------------------- 6. the drafting inconsistency, and its repair
# Before this arc, §1 said "five" and the closing one-sentence claim said "four": B1017
# propagated 4 -> 5 into the hypothesis paragraph and not into the sentence that gets quoted.
chk("the_claim_no_longer_says_four_typed_external_data",
    "four typed external data" not in CLAIM)
chk("the_claim_says_five_in_the_one_sentence_claim",
    "five typed external data" in CLAIM.split("The one-sentence claim")[-1])

R["typing"] = typing
R["answer"] = {
    "zero_dimensionless_inputs": "NOT PROVEN — four of the five counted inputs are dimensionless "
                                 "(two 𝔽₂ bits, the Lie type, the VEV direction); all four are "
                                 "DISCRETE.",
    "zero_continuous_dimensionless_inputs": "NOT PROVEN — exactly one (A2 = c = 6σ), declared and "
                                            "priced as an anchor by B1015. L154 is the single open "
                                            "cell that would convert it to an output and take the "
                                            "count to zero.",
    "all_inputs_anchor_what_the_object_cannot_contain":
        "B1000 tests exactly this and it holds for FOUR SECTORS / FIVE CLOSINGS — with three "
        "named exceptions graded ARTIFACT ('ours, not the object's', reducible in principle): "
        "the 6d type, the filling slope, P5 menu completeness.",
    "the_defect_found": "THE_CLAIM's counted list carries one of those artifacts (the 6d type) as "
                        "a hypothesis and carries no space closing at all, while B1017 — the arc "
                        "that wrote that list — asserts it confirms B1000's census. Same "
                        "cardinality, different set.",
}
R["all_pass"] = all(v["pass"] for v in R["checks"].values())

if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(json.dumps(R, indent=1,
                                                                          ensure_ascii=False))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\nALL PASS:", R["all_pass"])
