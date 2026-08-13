"""B1047 — the seam / level-15 cluster, dispositioned FROM THE BODIES.

B1045 mapped B300–B499 from CLAIM LINES and said so: campaign step 1 forbids claim lines as a
basis for disposition. This arc reads the bodies of the largest candidate cluster — the seam /
level-15 (√−15) campaign, 14 rows — and dispositions it.

THE DOMINANT FINDING IS NOT A LAW. It is that this cluster's claim lines systematically overstate
their own bodies, in the one direction a consolidation pass cannot survive: three of them state as
a LAW what their own body tiers as an OBSERVED PATTERN, and a later arc refuted it.

  B359 claim line:  "the theta-lift seam form is pair-specific and parity-selective"
  B359 body:        "A parity selection rule (OBSERVED PATTERN, NOT CLAIMED AS LAW): 3 data points"
  B360, next arc:   both parity readings REFUTED in one exact run (verdict NEGATIVE)

  B361 claim line:  "Across 8 pairs with zero counterexamples ... carries √−15 exactly when it
                     contains a seed elliptic at both 3 and 5"
  B362 claim line:  "extending the doubly-elliptic-seed brightness law to 11 pairs"
  B367 body:        "the banked selection rule FAILS ON THE TWELFTH PAIR" — (3,4) is bright and
                     contains no doubly-elliptic seed; `arc_verdict` declares supersedes: B361

So: DECLINE — RETRACTION for B359 · B361 · B362. Restoring their headlines would restore refuted
claims — the B123 pattern, three more instances.

THE SURVIVOR IS NOT THE HEADLINE. What B410 independently re-derived as separating 4/4 is B393's
PRODUCT-FIELD STRATIFICATION LAW, which is restored here as its OWN LAW_MAP row.

FOUR RIDERS TRAVEL OR THE RESTORATION IS AN OVERCLAIM: the computed range; the per-side Π_H
erratum (with `k1_termwise.json` a NEGATIVE ARTIFACT); the named open residual; and the whole
cluster's theta-lift-sector / L57 / firewalled scope.
"""
import glob
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = {"checks": {}}


def chk(name, ok, **d):
    R["checks"][name] = {"pass": bool(ok), **d}
    return ok


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def body(bid):
    p = glob.glob(str(ROOT / "frontier" / f"{bid}_*" / "FINDINGS.md"))
    return pathlib.Path(p[0]).read_text(encoding="utf-8") if p else ""


def vd(bid):
    p = glob.glob(str(ROOT / "frontier" / f"{bid}_*" / "arc_verdict.json"))
    return json.loads(pathlib.Path(p[0]).read_text(encoding="utf-8")) if p else {}


def artifact(bid, name):
    p = glob.glob(str(ROOT / "frontier" / f"{bid}_*" / name))
    return json.loads(pathlib.Path(p[0]).read_text(encoding="utf-8")) if p else None


def flat(s):
    return re.sub(r"\s+", " ", s)


# =========================================================== 1. the claim-line/body gap, measured
c359 = vd("B359").get("claim_one_line", "")
b359 = body("B359")
chk("b359_CLAIM_LINE_says_parity_selective", "parity-selective" in c359, claim=c359[-70:])
chk("b359_BODY_tiers_it_OBSERVED_PATTERN_on_three_points",
    "OBSERVED PATTERN (not claimed as law)" in b359 and "3 data points" in b359)

b360 = body("B360")
chk("b360_REFUTED_both_parity_readings_the_very_next_arc",
    'the "contains an even seed" reading is REFUTED' in b360
    and 'the "opposite parity" reading is ALSO refuted' in b360
    and vd("B360").get("verdict") == "NEGATIVE")

c361 = vd("B361").get("claim_one_line", "")
c362 = vd("B362").get("claim_one_line", "")
chk("b361_CLAIM_LINE_states_a_law_on_8_pairs_zero_counterexamples",
    "zero counterexamples" in c361 and "elliptic at both 3 and 5" in c361)
chk("b362_CLAIM_LINE_extends_it_to_11_pairs", "11 pairs with zero counterexamples" in c362)
# B361's own body is honest at the site -- the tier is there, and the claim line drops it.
chk("b361_BODY_already_said_computed_range_not_proved",
    "stated as a law of the computed range,\nnot proved" in body("B361")
    or "stated as a law of the computed range, not proved" in flat(body("B361")))

b367 = body("B367")
chk("b367_BODY_refutes_the_law_at_pair_3_4",
    "the local law (B361) is REFUTED at pair (3,4)" in b367
    and "fails on the twelfth pair" in b367)
chk("b367_DECLARES_supersedes_B361", vd("B367").get("supersedes") == "B361")
# ...and the graph does not carry it -- B1046's defect A, this cluster being where it was found.
chk("but_B361_and_B362_still_carry_null_superseded_by",
    vd("B361").get("superseded_by") is None and vd("B362").get("superseded_by") is None)

# THE NUANCE THAT MUST TRAVEL WITH THE RETRACTION. B367 retracts the LAW, not the DATA -- and it
# says so in its own provenance line. A disposition that erased the 11 pairs would overshoot.
chk("b367_keeps_the_eleven_confirming_pairs_AS_DATA",
    "its 11 confirming pairs stand as data" in flat(b367))
# Same shape for B359: its exact tables were not refuted, they were SUPERSEDED BY A BETTER TABLE.
chk("b359s_tables_were_superseded_by_exactness_not_refuted",
    "B359/B360 (partial tables, superseded by this exact set)" in flat(b367))


# ============================== 2. the refutation's arithmetic, RE-VERIFIED HERE (campaign step 5)
# The seed A_m has char poly x^2 - (m^2+2)x + 1, disc = m^4 + 4m^2. Over F_p (p odd) the poly is
# irreducible -- the seed is ELLIPTIC at p -- exactly when disc is a quadratic NON-residue. Nothing
# is imported: this is the substrate of B360's mechanism, B361's law and B367's refutation, and it
# is integer arithmetic, so it is redone rather than cited.
def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def elliptic_at(m, p):
    return legendre(m ** 4 + 4 * m ** 2, p) == -1


doubly = [m for m in range(1, 9) if elliptic_at(m, 3) and elliptic_at(m, 5)]
chk("doubly_elliptic_seeds_up_to_8_are_exactly_2_7_and_8", doubly == [2, 7, 8], seeds=doubly)
# B361 scoped its list to m <= 7 and NAMED m=8 as its own next discriminator -- so the third
# qualifier is not an error in B361, and this arc does not report it as one.
chk("b361_scoped_to_m_le_7_and_named_the_next_qualifier_itself",
    "Qualifying seeds (m ≤ 7)" in body("B361")
    and "the first doubly-elliptic seed beyond 7" in flat(body("B361")))

chk("pair_3_4_contains_NO_doubly_elliptic_seed", not any(m in doubly for m in (3, 4)))
# ...yet the exact six-pair table makes it BRIGHT, with the second-largest aggregate.
s2 = artifact("B367", "step0_report.json")["S0_7_sum_s_squared"]
chk("yet_B367s_EXACT_table_makes_3_4_bright_at_1_over_192", s2["3,4"] == "1/192", table=s2)
chk("and_the_dark_pairs_are_exactly_zero_there", s2["1,3"] == "0" and s2["1,4"] == "0")

# The minimal repair -- "each prime covered by SOME seed of the pair" -- dies in the same table.
def covering(pair):
    return (any(elliptic_at(m, 3) for m in pair), any(elliptic_at(m, 5) for m in pair))


chk("the_minimal_repair_dies_too__(1,3)_and_(3,4)_cover_identically",
    covering((1, 3)) == covering((3, 4)) == (True, True))
chk("...and_(1,3)_is_exactly_dark_while_(3,4)_is_bright", s2["1,3"] == "0" and s2["3,4"] != "0")
# The ground B367 gives for "finer than spectra": W1 and W4 have the same level-15 order.
orders = artifact("B367", "step0_report.json")["orders"]
chk("W1_and_W4_share_an_order_which_is_B367s_finer_than_spectra_ground",
    orders["1"] == orders["4"] == 20, orders=orders)


# ================================================= 3. THE SURVIVOR — B393's stratification law
PF = artifact("B393", "product_fields.json")
STATUS = {"1,3": "dark", "1,4": "dark", "3,5": "dark", "3,4": "bright", "2,3": "bright"}
chk("product_fields_covers_five_pairs_three_dark_two_bright",
    {k: v["status"] for k, v in PF.items()} == STATUS)
# THE LAW: s-carrying is zero on exactly the dark pairs. This is the statement being restored.
chk("THE_LAW__s_carrying_is_zero_on_exactly_the_dark_pairs",
    all((PF[k]["s-carrying"] == 0) == (v == "dark") for k, v in STATUS.items()),
    s_carrying={k: PF[k]["s-carrying"] for k in PF})
# The stratification is finer than "zero vs nonzero": the dark class itself splits.
chk("the_dark_class_STRATIFIES__fully_real_vs_z_only",
    PF["1,4"]["real(x,y)"] == 39 and PF["1,4"]["z-only"] == 0
    and PF["3,5"]["real(x,y)"] == 15 and PF["3,5"]["z-only"] == 0
    and PF["1,3"]["real(x,y)"] == 15 and PF["1,3"]["z-only"] == 24)
chk("and_the_bright_controls_put_the_COMPLEMENTARY_stratum_into_s_carrying",
    PF["3,4"]["s-carrying"] == 24 and PF["2,3"]["s-carrying"] == 18)
# No product is zero anywhere -- so "termwise annihilation" is a statement about the FIELD each
# product lands in, not about products vanishing. This is what "no cancellation" means.
chk("NO_product_vanishes__annihilation_is_FIELD_MEMBERSHIP_not_a_zero",
    all(v["zero"] == 0 for v in PF.values()))

KF = artifact("B393", "k1_fullfield.json")
chk("k1_fullfield_agrees_termwise_with_the_strata",
    KF["1,3"]["nonzero_terms"] == 0 and KF["3,5"]["nonzero_terms"] == 0
    and KF["3,4"]["nonzero_terms"] == 24 and KF["2,3"]["nonzero_terms"] == 18)
chk("k1_14_completes_the_dark_class", artifact("B393", "k1_14.json")["nonzero_terms"] == 0)

# B410's criterion, on the SAME object, separating 4/4 -- the independent re-derivation.
FF = artifact("B410", "b2ii_fullfield.json")
chk("b410_criterion_separates_4_of_4_on_the_same_object",
    FF["separates"] is True
    and FF["fullfield_scounts"] == {"1,3": 0, "3,5": 0, "3,4": 24, "2,3": 18})
chk("b410_reduces_the_crowns_why_to_B393s_law",
    "the mechanism =\nM1's stratification law" in body("B410")
    or "the mechanism = M1's stratification law" in flat(body("B410")))
# B393's K2 was KILLED -- the Galois eigen-pattern does NOT discriminate. The law is what is left
# standing after its own first explanation died, which is why it is the thing worth restoring.
chk("b393s_own_first_explanation_K2_was_KILLED",
    "K2 (Galois eigen-pattern of X₃) KILLED" in body("B393")
    and "IDENTICAL\n  Galois structure" in body("B393"))


# ================================================================== 4. the four riders, each checked
# RIDER 1 — computed range, not proved.
chk("rider1_the_range_is_FIVE_pairs_plus_B410s_four", len(PF) == 5 and len(FF["fullfield_scounts"]) == 4)
chk("rider1_b393_scopes_itself_to_the_tested_set",
    "met on the tested set" in body("B393"))

# RIDER 2 — the per-side Π_H erratum, and the negative artifact.
chk("rider2_b393_records_the_broken_first_attempt",
    "per-side subfield coordinates\nsilently drop content" in body("B393")
    or "per-side subfield coordinates silently drop content" in flat(body("B393")))
chk("rider2_b410_calls_it_the_FOURTH_appearance",
    "The Π_H-per-side hazard, 4th appearance" in flat(body("B410")))
# THE ARTIFACT ITSELF IS THE PROOF OF THE ERRATUM, and this is the check that makes it unmissable:
# k1_termwise.json reports nonzero_terms = 0 for the BRIGHT controls too. A reader who took that
# file for a result would conclude every pair is dark. It must never be read as a result.
KT = artifact("B393", "k1_termwise.json")
chk("rider2_k1_termwise_is_a_NEGATIVE_ARTIFACT__it_reads_zero_on_the_BRIGHT_controls",
    KT["3,4"]["status"] == "bright" and KT["3,4"]["nonzero_terms"] == 0
    and KT["2,3"]["status"] == "bright" and KT["2,3"]["nonzero_terms"] == 0)
chk("rider2_and_the_full_field_run_reads_24_and_18_on_the_same_two_pairs",
    KF["3,4"]["nonzero_terms"] == 24 and KF["2,3"]["nonzero_terms"] == 18)
# The per-side run also carries the wrong spectrum SIZES -- 9 and 15 terms where the full field has
# 39. So the two files are not two readings of one computation; one of them is a different object.
chk("rider2_the_broken_run_even_has_different_TERM_COUNTS",
    KT["3,4"]["terms"] == 9 and KF["3,4"]["terms"] == 39)

# RIDER 3 — the named residual is OPEN.
chk("rider3_b393_names_the_residual_and_stages_it",
    "Residual (staged, named): why (1,3)'s 5-side withholds √5" in flat(body("B393")))
chk("rider3_b410_stages_the_same_residual_with_its_obstruction",
    "The deep residual (STAGED with the exact obstruction)" in flat(body("B410"))
    and "this is NOT a per-side statement" in flat(body("B410")))

# RIDER 4 — theta-lift sector, pending L57, firewalled, nothing to CLAIMS.md.
for b in ("B359", "B360", "B361", "B362", "B367"):
    chk(f"rider4_{b}_declares_firewalled_nothing_to_CLAIMS",
        "Firewalled" in body(b) and "CLAIMS.md" in body(b))
chk("rider4_the_arc_is_pending_L57",
    all("L57" in body(b) for b in ("B359", "B360", "B361", "B362")))
chk("rider4_b393_and_b410_declare_firewalled",
    "Firewalled" in body("B393") and "Firewalled" in body("B410"))
claims = read("CLAIMS.md")
chk("rider4_NONE_of_the_cluster_is_in_CLAIMS_md",
    not any(re.search(rf"\b{b}\b", claims)
            for b in ("B359", "B360", "B361", "B362", "B367", "B393", "B410")))


# ========================================================= 5. the provenance defect (registered L165)
chk("b410_NAMES_b2ii_fullfield_py_as_its_provenance",
    "b2ii_fullfield.py" in body("B410"))
chk("b2ii_fullfield_py_EXISTS_NOWHERE_IN_THE_REPO",
    not list(ROOT.glob("**/b2ii_fullfield.py")))
chk("yet_a_LOCK_asserts_the_json_it_would_have_produced",
    "b2ii_fullfield.json" in read("tests/test_b410_coupling.py"))


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


# CORRECTED IN THIS SCRIPT, AGAINST THIS ARC'S OWN PLAN. The plan asserted the numbers survive
# "only because they are byte-identical to B393's k1_fullfield.json". THEY ARE NOT: 188 bytes
# against 485, different hashes, different schema. b2ii_fullfield.json is a DERIVED SUMMARY whose
# four counts equal k1_fullfield's four `nonzero_terms`. The numbers ARE recoverable -- by
# re-deriving them from B393's artifact, not by finding a copy. Same conclusion, wrong reason, and
# the wrong reason is the kind that survives into a curated surface if unchecked.
f410 = glob.glob(str(ROOT / "frontier" / "B410_*" / "b2ii_fullfield.json"))[0]
f393 = glob.glob(str(ROOT / "frontier" / "B393_*" / "k1_fullfield.json"))[0]
chk("CORRECTION__the_two_jsons_are_NOT_byte_identical", sha(f410) != sha(f393))
chk("CORRECTION__b410s_json_is_a_DERIVED_SUMMARY_of_b393s",
    all(FF["fullfield_scounts"][k] == KF[k]["nonzero_terms"] for k in FF["fullfield_scounts"]))

# --- L165, measured corpus-wide, and the sentence the check refused to let me write -------------
HAVE = {p.name for p in ROOT.glob("**/*.py")}
ABSENT = {}
for f in sorted(ROOT.glob("frontier/B*/FINDINGS.md")):
    arc = f.parent.name.split("_")[0]
    for m in re.finditer(r"`([A-Za-z0-9_]+\.py)`", f.read_text(errors="ignore")):
        if m.group(1) not in HAVE:
            ABSENT.setdefault(m.group(1), set()).add(arc)
chk("L165_fourteen_BACKTICKED_reproducers_exist_nowhere", len(ABSENT) == 14,
    n=len(ABSENT), arcs=len({a for s in ABSENT.values() for a in s}))
# ...and the method that found 14 would have MISSED the one that started this: B410 names its
# generator WITHOUT backticks. That is why the figure is published as a lower bound, 15 across 12.
chk("L165_and_the_method_would_have_missed_B410s_own", "b2ii_fullfield.py" not in ABSENT)

# THE DRAFT SENTENCE WAS "none of the 15 sits under a CLAIMS.md promotion". FALSE, and false by
# the exact defect DEBT_LEDGER's Correction 2 records: CLAIMS.md cites its evidence BY PATH, so a
# bare-id grep misses it. Three of the eleven arcs are promoted -- and they are three DIFFERENT
# things, which is why the disposition is per-arc and not a count.
promoted = sorted({a for s in ABSENT.values() for a in s
                   if re.search(rf"frontier/{a}_", claims)}, key=lambda b: int(b[1:]))
chk("L165_THREE_of_the_absent_reproducer_arcs_ARE_promoted", promoted == ["B156", "B379", "B877"],
    promoted=promoted)
# B156: the absent script is one B156 itself REFUTED. Its absence is housekeeping, not a defect.
chk("L165_B156s_absent_script_is_one_B156_itself_calls_WRONG",
    "over-counts" in flat(body("B156")) and "L5=3120, L6=57792" in flat(body("B156"))
    and len(list(ROOT.glob("frontier/B156_*/*.py"))) >= 6)
# B877: already disclosed at the site, by the arc, under its own heading.
chk("L165_B877s_absence_is_ALREADY_DISCLOSED_by_B877",
    "Manifest gap" in body("B877") and "levi2.py` (core type, exact ℚ) — absent" in flat(body("B877")))
# B379: the real one. Named as THE reproducer; the arc directory holds no code at all; and
# CLAIMS.md P60 points a reader at that directory.
chk("L165_B379s_arc_directory_contains_NO_python_at_all",
    list(ROOT.glob("frontier/B379_*/*.py")) == [])
chk("L165_B379_names_it_as_THE_reproducer", "Reproducer: `reduction_verification.py`" in body("B379"))
chk("L165_and_CLAIMS_P60_cites_that_directory_as_its_evidence",
    "frontier/B379_selection_rule_reduction" in claims)
# STATED EXACTLY, because the temptation is to overclaim it: P60 is NOT unverified. Its lock
# recomputes the two traces from scratch through the B358/B367 engines. What is gone is the ARC's
# own computation -- a false impression of provenance, not a false claim.
b379lock = read("tests/test_b379_selection_rule.py")
chk("L165_but_P60s_LOCK_recomputes_the_traces_from_scratch",
    "the load-bearing lock" in b379lock and "step0_exact_matrices" in b379lock
    and "cyclo_engine" in b379lock)

# The re-verification route is real: pure Fractions, no external CAS -- but B393 is NOT
# self-contained. Four files in three other arcs are on its import path.
CHAIN = ["frontier/B358_seam_certification/cyclo_engine.py",
         "frontier/B358_seam_certification/seam_certification.py",
         "frontier/B367_value_map/step0_exact_matrices.py",
         "frontier/B386_crt_closed_form/tensor_gate.py"]
chk("the_dependency_chain_exists_and_is_named", all((ROOT / p).is_file() for p in CHAIN),
    chain=CHAIN)
gen = read("frontier/B393_cancellation_mechanism/product_fields.py")
chk("b393s_generator_imports_all_four_and_is_pure_Fraction",
    all(pathlib.Path(p).stem in gen for p in CHAIN)
    and "from fractions import Fraction" in gen and "float" not in gen)
# REGENERATED IN THIS SESSION: product_fields.py was re-run against the live tree and its output
# compared to the banked artifact. The hash below is the banked file's; the regeneration matched
# it, which is what "EXACT tier, regenerable end-to-end" is supposed to mean and is here checked
# rather than quoted. (Recorded as a hash so this check is cheap; the run itself is in FINDINGS.)
chk("the_banked_artifact_is_pinned_by_hash",
    sha(glob.glob(str(ROOT / "frontier" / "B393_*" / "product_fields.json"))[0])
    == "abeae76bda9a9814a03dc0aba79895320747376ddcb23820177a0d1bfadce92d")


# ============================================================ 6. what this arc wrote, checked back
lm = flat(read("docs/LAW_MAP.md"))
chk("LAW_MAP_carries_the_stratification_law_as_its_OWN_row",
    "THE SEAM'S DARKNESS IS TERMWISE" in lm)
# It must NOT be folded onto B1029's class-field row: tested read-only in the plan and re-tested
# here -- B393 and B410 mention class field / Hilbert / HCF / B334 exactly ZERO times, and B1029's
# row mentions neither theta nor darkness. They share the field √−15 as VOCABULARY, not statement.
seam_words = re.compile(r"class field|Hilbert|HCF|B334", re.I)
chk("B393_and_B410_are_not_class_field_statements",
    not seam_words.search(body("B393")) and not seam_words.search(body("B410")))
# ANCHORED ON THE ARC ID, NOT THE HEADLINE, AND THIS ARC IS WHY. The first draft matched rows
# containing "THE SEAM IS THE ENDS' CLASS FIELD" -- and then THIS arc's own row quoted that
# headline while explaining why it does not fold onto it, so the match returned TWO rows and the
# check went red. E37 in its cheapest form: writing the prose broke the measurement of the prose.
b1029_row = [ln for ln in read("docs/LAW_MAP.md").splitlines()
             if "(B1029, re-verifying B334)" in ln]
chk("B1029s_row_mentions_neither_theta_nor_darkness",
    len(b1029_row) == 1
    and not re.search(r"theta|darkness|s-channel", b1029_row[0], re.I))
# The restored row must carry the retraction, or a reader meets the dead law first.
row = [ln for ln in read("docs/LAW_MAP.md").splitlines()
       if "THE SEAM'S DARKNESS IS TERMWISE" in ln]
chk("the_restored_row_names_the_REFUTED_local_law_it_replaces",
    len(row) == 1 and "B361" in row[0] and "REFUTED" in row[0])
chk("the_restored_row_carries_all_four_riders",
    len(row) == 1 and all(t in row[0] for t in ("computed range", "Π_H", "L57", "k1_termwise")))

led = read("docs/consolidation/DEBT_LEDGER.md")
chk("the_debt_ledger_carries_the_dispositions",
    "DECLINE — RETRACTION, NOT RESTORATION: B359 · B361 · B362" in flat(led))

led = read("docs/consolidation/DEBT_LEDGER.md")
chk("the_ledger_states_the_debt_move_as_a_SET_not_a_subtraction",
    "**204 → 199**" in led and "set-differenced, not subtracted" in led
    and all(b in led for b in ("B359", "B361", "B362", "B393", "B410")))
# THE FINDING THAT THE SET-DIFFERENCE MADE VISIBLE. Two of the five retired rows were DECLINED,
# not restored -- and the sweep retires them all the same, because it asks "is it cited?" and not
# "is it endorsed?". Correct for campaign step 6, but it means the RAW NUMBER CANNOT TELL A
# RESTORATION FROM A RETRACTION.
chk("the_ledger_says_the_raw_number_cannot_tell_restoration_from_retraction",
    "cannot\n> tell a restoration from a retraction" in led
    or "cannot tell a restoration from a retraction" in flat(led))
# E38's second instance, and this time in a lock this refresh did not write.
chk("E38_second_instance_is_registered_with_the_lock_it_broke",
    "SECOND INSTANCE, B1047" in read("docs/ERROR_LEDGER.md")
    and "200 < sub < 280" in read("tests/test_consolidation_coverage.py"))
chk("...and_the_repaired_lock_bounds_a_SHARE",
    "share = sub / max(1, proved)" in read("tests/test_consolidation_coverage.py"))

# --- step 3: law-siblings extended to the row this cluster actually belongs to -------------------
import importlib.util as _il
_spec = _il.spec_from_file_location("_ls", ROOT / "scripts" / "checks" / "law_siblings.py")
_ls = _il.module_from_spec(_spec)
_spec.loader.exec_module(_ls)
chk("law_siblings_now_fingerprints_B1029s_row",
    "the seam is the ends' class field (B1029)" in _ls.FINGERPRINTS)
chk("...and_this_arcs_own_restored_law", "the seam's darkness is termwise (B1047)" in _ls.FINGERPRINTS)
_cands = {b for _, b, _ in _ls.candidates()}
# REPAIRED BY REVIEW 1 (B1054). The original asserted the three siblings are STILL SURFACING as
# untriaged candidates. B1048 restored/triaged them, so the sweep stopped returning them and this
# check inverted -- E38 again, a lock that fails because its finding was acted on. What does not
# move is that the fingerprint NAMES them: they are registered in LAW_SIBLINGS with a disposition.
_reg_now = read("docs/consolidation/LAW_SIBLINGS.md")
chk("the_new_fingerprint_surfaced_three_real_siblings_of_B1029s_row__all_now_DISPOSITIONED",
    all(b in _reg_now for b in ("B427", "B449", "B459")),
    still_untriaged=sorted(_cands),
    note="surfaced by this arc, dispositioned by B1048. The original form asserted they were still "
         "in the sweep's output, which could only hold until someone triaged them")
chk("and_the_gate_is_clean_because_all_four_are_triaged", _ls.sweep() == [])
_reg = read("docs/consolidation/LAW_SIBLINGS.md")
chk("B876_is_registered_as_a_WORD_match_not_a_statement_match",
    "DISTINCT — the fingerprint matched a word" in _reg and "Lie-algebra ANNIHILATOR" in _reg)
# REPAIRED BY REVIEW 1 (B1054). `"6 / 147"` pinned the LAW_MAP row count of the day; the corpus
# grew to 154 rows and the published figure moved with it, correctly. E38 -- the claim is that the
# coverage is PUBLISHED as a fraction, not that the denominator is frozen.
chk("the_coverage_number_is_PUBLISHED_not_implied",
    "Coverage, measured (B1047)" in _reg
    and re.search(r"\*\*\s*6 / \d+ = \d+ %\*\*", _reg) is not None
    and "(55 at B1047)" in _reg,
    published=(re.search(r"\*\*\s*(6 / \d+ = \d+ %)\*\*", _reg) or [None, None])[1],
    note="`**55**` was pinned as a literal and is now **62**, with `(55 at B1047)` annotated beside "
         "it -- the LEDGER recorded the movement correctly and only the check froze. Both figures "
         "here are asserted in the form the ledger publishes them: a live number with its "
         "measured-at-B1047 value beside it")

R["answer"] = {
    "the_disposition": "RESTORE B393's product-field stratification law (with B410's independent "
                       "4/4 criterion) as its OWN LAW_MAP row — NOT onto B1029's class-field row, "
                       "which shares only the field √−15 as vocabulary. DECLINE — RETRACTION for "
                       "B359 · B361 · B362, whose headlines were refuted by B360 and B367.",
    "the_dominant_finding": "This cluster's CLAIM LINES systematically overstate their own BODIES. "
                            "B359's body tiers the parity rule OBSERVED PATTERN, 3 data points; its "
                            "claim line says 'parity-selective' flat. B361's body says 'a law of "
                            "the computed range, not proved'; its claim line says '8 pairs, zero "
                            "counterexamples'. A claim-line ledger cannot see this band, which is "
                            "exactly what campaign step 1 says and what B1045 declared of its map.",
    "the_survivor": "s-darkness ⟺ the 5-side never donates √5 to an imaginary product. Every X₃·X₅ "
                    "product of a dark pair is individually s-free — termwise mutual annihilation, "
                    "NOT cancellation (no product is zero; the statement is about which field each "
                    "product lands in). The dark class itself stratifies: (1,4) and (3,5) fully "
                    "real, (1,3) √5-free in its imaginary part. Bright controls put exactly the "
                    "complementary stratum into s-carrying, 24 and 18.",
    "what_the_retraction_does_NOT_take": "B367 retracts the LAW, not the DATA — its own words: "
                                         "'its 11 confirming pairs stand as data'. B359's exact "
                                         "tables were SUPERSEDED BY A BETTER TABLE (B367's full "
                                         "identification), not refuted. The declined rows lose "
                                         "their headline, not their arithmetic.",
    "the_four_riders": "(1) COMPUTED RANGE: five pairs in B393, four in B410's criterion — not "
                       "proved. (2) THE Π_H ERRATUM: the criterion CANNOT be stated per-side; "
                       "k1_termwise.json is a NEGATIVE ARTIFACT that reads nonzero_terms = 0 on "
                       "the BRIGHT controls and even carries different term counts (9 vs 39), so "
                       "a reader taking it for a result would conclude every pair is dark. (3) THE "
                       "RESIDUAL IS OPEN: why the dark 5-side withholds √5 at exactly the "
                       "X₃-paired frequencies, staged with its exact obstruction. (4) SCOPE: "
                       "theta-lift sector, pending L57, firewalled, nothing to CLAIMS.md.",
    "the_provenance_defect": "B410's named generator b2ii_fullfield.py exists nowhere in the repo, "
                             "yet tests/test_b410_coupling.py locks the JSON it would have "
                             "produced. THE PLAN'S EXPLANATION WAS WRONG AND IS CORRECTED HERE: "
                             "the file is NOT a byte copy of B393's k1_fullfield.json (188 bytes "
                             "vs 485, different schema). It is a derived summary whose four counts "
                             "equal k1_fullfield's four nonzero_terms — so the numbers are "
                             "recoverable by re-derivation, not by finding a copy. Registered "
                             "L165 with the other 14 absent reproducers.",
    "the_arithmetic_reverified_here": "The doubly-elliptic classification is redone from integers: "
                                      "disc(A_m) = m⁴+4m², elliptic at p ⟺ disc a non-residue. "
                                      "Qualifiers below 9: m = 2, 7, 8 — and B361 scoped itself to "
                                      "m ≤ 7 AND named m=8 as its own next discriminator, so the "
                                      "third qualifier is not an error in B361. Pair (3,4) "
                                      "contains no qualifier yet B367's exact table gives it Σs² = "
                                      "1/192, the second-largest aggregate. The minimal repair "
                                      "dies in the same table: (1,3) has the IDENTICAL covering "
                                      "pattern (3 covered by m=1, 5 covered by m=3) and is exactly "
                                      "dark — and W₁, W₄ share the level-15 order 20, which is "
                                      "B367's ground for 'finer than spectra'.",
}
R["all_pass"] = all(v["pass"] for v in R["checks"].values())

if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(
        json.dumps(R, indent=1, ensure_ascii=False))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\n%d checks; ALL PASS: %s" % (len(R["checks"]), R["all_pass"]))
