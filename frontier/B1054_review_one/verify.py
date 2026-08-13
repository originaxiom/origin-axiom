"""B1054 — the instrument behind Review 1, the consolidation seat's decadal review of its own window.

WHY THIS EXISTS. The owner commissioned this seat to review its OWN thirty arcs (qB1024-qB1053).
A seat grading itself is exactly the hazard this window named as E37, and the commission's answer
is STRUCTURAL, not a prohibition: main's digest re-grades the review one step later. That only
works if the digest can RE-RUN the review's numbers instead of re-reading its prose. So every
countable claim in `docs/progress/REVIEW_1_CONSOLIDATION_SEAT_2026-08-12.md` is produced here,
against the tree, with no arguments and no network required.

E37 DISCIPLINE, MECHANISED. Every denominator that measures this window EXCLUDES this window.
The corpus base rates below are computed over 931 arcs with the window's 30 removed; the check
names carry `_excl_window` wherever that is what happened.

E38 DISCIPLINE, TURNED ON THIS INSTRUMENT. A review that locks absolute counts inside a programme
whose purpose is to change them breaks the moment the work succeeds -- this window found two live
instances of exactly that and repaired both. So the structural claims are locked and the moving
figures are RECORDED with a band, never pinned to a single integer.

WHAT IT FOUND, and none of it is flattering. The first one outranks the rest:

  0. AT `5b26e51` -- THE ANCHOR, whose commit message is "Pin the known-green suite at be87a51,
     3996 passed, 0 failed" -- SIX OF THE THIRTY ARCS WERE RED, AND THE SUITE COULD NOT SEE IT.
     Proven on pristine worktrees of that commit: `pytest` over those six arcs' locks returned
     46 passed / 0 failed, while re-running their six `verify.py` scripts turned all six red.
     Every one shipped `results.json` recording `all_pass: true`. The mechanism is structural:
     a lock asserts over the instrument's committed OUTPUT, that output is a CACHE, and a
     consolidation window's whole job is to edit the files the instrument measures. Registered
     as E39 (cached verification) and fixed by `scripts/checks/instrument_freshness.py`.
     A related correction against this review's own first draft: it graded the window's
     reproducers RUN on the strength of their EXIT CODES, and 28 of 30 exit 0 no matter what.
  1. All 30 arcs carry `verdict: PROVED`. The corpus base rate excluding them is 65.5%; the
     probability of 30/30 under it is 3e-6. Eighteen of the thirty bodies carry retraction,
     refutation, decline or NON-FINDING language. This window discovered L166 -- "the verdict
     field does not describe the body" -- and then instanced it thirty times out of thirty.
  2. RETRACTED BY THIS REVIEW ITSELF. The first form claimed the consolidation-debt metric
     "counts 175 and cannot see 191 -- 48% of its own subject", as L166's defect in the window's
     own metric. WRONG: the scope is DECLARED (DEBT_LEDGER's own table, added by qB1033), the code
     agrees (representation_sweep.py:69), and the NEGATIVE complement is covered by a GATED
     register. What survives is a partition remainder an order of magnitude smaller -- OPEN and
     RETRACTED fall outside BOTH registers: 41 arcs corpus-wide, 20 of them uncited.
  3. The handoff's correction tally partitions 24 corrections as 12 + 6 + 4 + 1 = 23.
     B1052's instrument checked `>= 20`, so a bound gated an exact claim and the gap survived.
  4. 29 of 30 arcs are unsealed; 2 of those 29 declare it. Main's R43/R44 declare every one.
  5. `git branch -r --no-merged` -- template item 1b's instrument -- under-reports on this
     container: it answers from the refs that happen to be fetched, not from the remote.

All five are the same species this window has been naming all along: the instrument answers from
what it holds rather than from the ground, and nothing gates the difference.
"""
import glob
import json
import os
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = {"checks": {}, "measured": {}}

WINDOW = range(1024, 1054)          # qB1024-qB1053, the declared modulus
HANDOFF = "docs/handoffs/CONSOLIDATION_REFRESH_HANDOFF_2026-08-12.md"
REVIEWS = "docs/progress/REVIEWS.md"


def chk(name, ok, **d):
    R["checks"][name] = {"pass": bool(ok), **d}
    return ok


def rec(name, value):
    """A number the review QUOTES but does not lock -- E38: it is designed to move."""
    R["measured"][name] = value
    return value


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def flat(s):
    """Prose as a reader sees it -- blockquote markers stripped, then whitespace collapsed.

    Inherited from B1052. The fourth markdown-structure-versus-string bug this window hit; kept
    because Review 1 quotes prose out of a file that uses blockquotes heavily."""
    return re.sub(r"\s+", " ", re.sub(r"(?m)^\s*>\s?", "", s))


def arcs():
    """Every arc directory with a verdict, deduped by number. Yields (n, dirname, verdict_dict)."""
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
        yield n, os.path.basename(d), json.loads(pathlib.Path(vp).read_text(encoding="utf-8"))


ALL = list(arcs())
WIN = [(n, b, v) for n, b, v in ALL if n in WINDOW]
OUT = [(n, b, v) for n, b, v in ALL if n not in WINDOW]

# The six instruments that were RED at 5b26e51 while the suite ran green over their locks, each
# with the literal that froze it. See the E39 registration and section 6 of the review.
SILENT_RED = {1042: "HEAD:", 1043: "SELF", 1046: "RETRACTIONS", 1047: "6 / 147", 1049: "== 2",
              1052: "d48ab85"}

# ---------------------------------------------------------------------------
# ITEM 2 -- THE DECLARED MODULUS
# ---------------------------------------------------------------------------
chk("modulus_is_exactly_thirty_arcs", len(WIN) == 30, n=len(WIN))
chk("modulus_runs_B1024_to_B1053",
    min(n for n, _, _ in WIN) == 1024 and max(n for n, _, _ in WIN) == 1053)
chk("modulus_has_no_gaps", sorted(n for n, _, _ in WIN) == list(WINDOW))
chk("the_windows_opening_arc_B1024_is_the_shared_fork_seal_and_carries_a_prereg",
    (ROOT / "frontier/B1024_l153_bits/PREREGISTRATION.md").is_file())

# ---------------------------------------------------------------------------
# ITEM 1 -- THE LOOP. What Review 1 inherits, and why the answer is "nothing parseable".
# ---------------------------------------------------------------------------
RV = read(REVIEWS)
blocks = re.findall(r"^#{2,4} Action items \(Review (\d+)\)", RV, re.M)
heads = re.findall(r"^#{1,3} Review (\d+) —", RV, re.M)
rec("branch_reviews_present", [int(h) for h in heads][-6:])
rec("branch_action_item_blocks", [int(b) for b in blocks])

chk("BRANCH_last_parseable_action_items_block_is_Review_37",
    blocks and int(blocks[-1]) == 37, last=blocks[-1] if blocks else None)
chk("BRANCH_last_review_present_is_Review_42", heads and int(heads[-1]) == 42,
    last=heads[-1] if heads else None)
chk("BRANCH_reviews_38_to_42_carry_NO_action_items_block",
    not any(38 <= int(b) <= 42 for b in blocks))
# Review 42 is a SINGLE-hash heading where 38-41 are double. A `^## Review` sweep misses it --
# the same match-the-text-not-the-structure shape, met inside this review's own item 1.
chk("and_Review_42s_heading_is_single_hash_which_a_naive_sweep_misses",
    re.search(r"(?m)^# Review 42 —", RV) is not None
    and re.search(r"(?m)^## Review 42 —", RV) is None)

# The gap is BRANCH-LOCAL: main resumed the practice at R43, after this branch forked.
try:
    MAIN_RV = subprocess.run(["git", "show", "origin/main:" + REVIEWS], cwd=ROOT,
                             capture_output=True, text=True, timeout=60).stdout
except Exception:
    MAIN_RV = ""
if MAIN_RV:
    mblocks = [int(b) for b in re.findall(r"^#{2,4} Action items \(Review (\d+)\)", MAIN_RV, re.M)]
    chk("MAIN_resumed_action_items_at_R43_and_R44__so_the_gap_is_branch_local",
        43 in mblocks and 44 in mblocks, main_blocks=mblocks[-4:])
    chk("CORRECTION__the_commission_read_this_as_no_prior_review_existing__it_is_the_fork_instead",
        44 in mblocks and 44 not in [int(h) for h in heads])
else:
    chk("MAIN_comparison_NOT_REACHED__origin_main_not_present_in_this_clone", True,
        disposition="NOT-REACHED")

# R42 escalated TOOLBOX.md by name. E38: lock the RELATION, never the integer.
DC = subprocess.run(["python3", "scripts/checks/doc_currency.py"], cwd=ROOT,
                    capture_output=True, text=True, timeout=300).stdout
m = re.search(r"docs/TOOLBOX\.md: B(\d+) vs B(\d+) \(lag (\d+)\)", DC)
lag = int(m.group(3)) if m else -1
rec("toolbox_lag_at_this_anchor", lag)
chk("TOOLBOX_is_still_the_largest_declared_currency_debt",
    lag > 600 and lag == max(int(x) for x in re.findall(r"\(lag (\d+)\)", DC)), lag=lag)
chk("R42_escalated_TOOLBOX_by_name_as_TWO_reviews_old",
    "TOOLBOX" in RV[RV.rfind("# Review 42"):])

# ---------------------------------------------------------------------------
# ITEM 1b -- THE BRANCH INVENTORY, and the defect in its own instrument
# ---------------------------------------------------------------------------
def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True, timeout=120)


# Refs are RECORDED BY ROLE, never by literal name: the `attribution` gate forbids the seat token
# that this branch's name contains, and a results file is a tracked artifact like any other.
def _role(ref):
    if ref.endswith("main") or ref == "main":
        return "main (the trunk)"
    if "audit/" in ref:
        return "the relay audit seat"
    return "the consolidation-refresh seat (this branch)"


tracked = [_role(l.strip()) for l in git("branch", "-r").stdout.splitlines()
           if l.strip() and "->" not in l]
rec("remote_tracking_refs_in_this_clone", sorted(set(tracked)))
ls = git("ls-remote", "--heads", "origin")
if ls.returncode == 0 and ls.stdout.strip():
    heads_remote = [_role(h) for h in re.findall(r"refs/heads/(\S+)", ls.stdout)]
    rec("actual_remote_heads", sorted(set(heads_remote)))
    chk("FINDING__branch_-r_UNDER-REPORTS_against_the_actual_remote",
        len(heads_remote) > len([t for t in tracked if "->" not in t]),
        tracked=len(tracked), actual=len(heads_remote))
    chk("...and_the_ref_it_misses_is_the_relay_audit_branch",
        "the relay audit seat" in heads_remote and "the relay audit seat" not in tracked)
else:
    chk("remote_inventory_NOT_REACHED__no_network_at_run_time", True, disposition="NOT-REACHED")

# ---------------------------------------------------------------------------
# ITEM 3 -- ADVANCEMENT, by LAW_MAP strength class
# ---------------------------------------------------------------------------
LM = read("docs/LAW_MAP.md").splitlines()
secs = {}                                   # section letter -> (start, end)
bounds = [(i, l[3]) for i, l in enumerate(LM) if re.match(r"^## [A-F]\. ", l)]
for j, (i, letter) in enumerate(bounds):
    secs[letter] = (i, bounds[j + 1][0] if j + 1 < len(bounds) else len(LM))

WIN_RX = re.compile(r"B10(?:2[4-9]|3\d|4\d|5[0-3])\b")
per_sec = {}
for letter, (a, b) in secs.items():
    per_sec[letter] = sum(1 for l in LM[a:b] if l.startswith("| **") and WIN_RX.search(l))
rec("lawmap_window_rows_per_section", per_sec)
total_rows = sum(per_sec.values())
rec("lawmap_window_rows_total", total_rows)

chk("the_window_moved_the_LAW_MAP_substantially", total_rows >= 20, n=total_rows)
chk("FINDING__every_single_window_row_landed_in_section_A_the_solo_laws",
    per_sec.get("A", 0) == total_rows and all(v == 0 for k, v in per_sec.items() if k != "A"),
    per_section=per_sec)
# Section A is "the object's arithmetic". Several window rows state nothing about the object's
# arithmetic at all -- they are findings about the PROGRAMME. Recorded, not adjudicated: LAW_MAP
# has no section for methodology, so this is a structural gap and an owner's call, not a slip.
meta_rx = re.compile(r"NAMING (IS NOT|A MECHANISM)|THE BAND IS THE WRONG UNIT|"
                     r"THE DEBT NUMBER COUNTS ROWS|KNOWLEDGE ROOM|SHADOW LIBRARY|"
                     r"REPRESENTATION GATE", re.I)
a0, a1 = secs["A"]
meta_in_A = [l[:120] for l in LM[a0:a1] if l.startswith("| **") and WIN_RX.search(l)
             and meta_rx.search(l[:260])]
rec("methodology_rows_filed_in_the_arithmetic_section", len(meta_in_A))
chk("FINDING__methodology_rows_sit_in_the_object_arithmetic_section",
    len(meta_in_A) >= 5, n=len(meta_in_A))
chk("...and_LAW_MAP_has_no_methodology_section_to_put_them_in",
    set(secs) == set("ABCDEF")
    and "meta-laws" in LM[secs["D"][0]] and "arithmetic" in LM[secs["A"][0]])

# What KIND of advancement: a consolidation window's rows are mostly RESTORATIONS of results the
# curated tier had lost, not new mathematics. The review must not let the row count read as
# thirty arcs of discovery.
win_rows = [l for l in LM[a0:a1] if l.startswith("| **") and WIN_RX.search(l)]
restoring = [l for l in win_rows if re.search(r"restoring B", l[:260])]
recollect = [l for l in win_rows if re.search(r"re-verifying B|collecting", l[:260])]
fresh = [l for l in win_rows if l not in restoring and l not in recollect]
rec("lawmap_rows_that_RESTORE_a_lost_result", len(restoring))
rec("lawmap_rows_that_RE_VERIFY_or_COLLECT", len(recollect))
rec("lawmap_rows_stating_something_NEW", len(fresh))
chk("the_row_split_accounts_for_every_window_row",
    len(restoring) + len(recollect) + len(fresh) == total_rows)
chk("RESTORATIONS_are_the_largest_class__this_was_a_consolidation_not_a_discovery_window",
    len(restoring) >= len(fresh), restoring=len(restoring), new=len(fresh))

# ---------------------------------------------------------------------------
# ITEM 4 -- ERROR-CLASS RECURRENCE
# ---------------------------------------------------------------------------
EL = read("docs/ERROR_LEDGER.md")
chk("E37_self_measurement_is_registered_and_attributed_to_this_window",
    re.search(r"\|\s*E37\s*\|.*Self-measurement", EL) and "B1042" in EL)
chk("E38_progress_eroded_threshold_is_registered_and_attributed_to_this_window",
    re.search(r"\|\s*E38\s*\|.*Progress-eroded threshold", EL) and "B1042" in EL)
chk("E36_artifact_clobber_is_registered", re.search(r"\|\s*E36\s*\|.*Artifact-clobber", EL))
# Registered BY this review, for the §6 finding, and the distinction is the whole point:
# E38 is a lock that FAILS when it should not; E39 is a lock that PASSES when it should not.
chk("E39_cached_verification_is_registered_by_THIS_review",
    re.search(r"\|\s*E39\s*\|.*Cached verification", EL) and "B1054" in EL)
chk("...and_it_names_the_six_arcs_it_was_measured_on",
    all(f"B{n}" in EL.split("| E39 |")[-1] for n in SILENT_RED)
    if "| E39 |" in EL else False)
chk("...and_it_states_the_distinction_from_E38_rather_than_blurring_it",
    "E38 is a lock that fails when it should not" in EL)

H = read(HANDOFF)
nums = re.findall(r"(?m)^\|\s*(\d+)\s*\|", H)
n_corr = len(set(int(x) for x in nums))
rec("handoff_numbered_corrections", n_corr)
chk("the_handoff_enumerates_twenty_four_numbered_corrections", n_corr == 24, n=n_corr)

# THE DEFECT. The tally sentence partitions them 12 + 6 + 4 + 1 = 23, against 24 rows -- and
# section 2.2's eleven rows carry no catch-mechanism column at all, so the partition is not
# derivable from the tables it claims to summarise.
tally = re.search(r"\*\*Twelve were caught by a check, six by a re-run, four by a\s+"
                  r"measurement moving unexpectedly, and one was published wrong", flat(H))
chk("FINDING__the_handoffs_catch_mechanism_tally_sums_to_23_not_24",
    tally is not None and 12 + 6 + 4 + 1 == 23 != n_corr, tally=23, rows=n_corr)
B1052V = read("frontier/B1052_the_handoff/verify.py")
chk("FINDING__B1052_gated_that_exact_claim_with_a_LOWER_BOUND_of_twenty",
    "n_corr >= 20" in B1052V and "== 24" not in B1052V)

# ---------------------------------------------------------------------------
# ITEM 5 -- PROVENANCE. The window's own L166 defect, measured on itself.
# ---------------------------------------------------------------------------
from collections import Counter

win_v = Counter(v.get("verdict") for _, _, v in WIN)
out_v = Counter(v.get("verdict") for _, _, v in OUT)
rec("window_verdicts", dict(win_v))
rec("corpus_verdicts_excl_window", dict(out_v))

base = out_v["PROVED"] / sum(out_v.values())
rec("corpus_PROVED_base_rate_excl_window", round(base, 4))
rec("p_of_thirty_of_thirty_under_that_base_rate", base ** 30)

chk("EVERY_arc_in_this_window_says_PROVED", win_v["PROVED"] == 30 and len(win_v) == 1)
chk("FINDING__the_corpus_excl_window_is_far_from_uniform", 0.5 < base < 0.8, base=round(base, 4))
chk("FINDING__30_of_30_is_a_base_rate_outlier_not_a_coincidence", base ** 30 < 1e-4)

NEG_RX = re.compile(r"\b(NON-FINDING|non-finding|RETRACT\w*|retract\w*|REFUTED|refuted|"
                    r"DECLINED?|declined?)\b")
bodies = 0
for n, b, _ in WIN:
    f = ROOT / "frontier" / b / "FINDINGS.md"
    if f.is_file() and NEG_RX.search(f.read_text(encoding="utf-8", errors="replace")):
        bodies += 1
rec("window_bodies_carrying_negative_or_retraction_language", bodies)
chk("FINDING__the_bodies_disagree_with_the_uniform_verdict_field",
    bodies >= 15 and win_v["PROVED"] == 30, bodies=bodies, of=30)

# Two arcs declare an outright NON-FINDING in the body and PROVED in the metadata.
nonfind = [b for n, b, _ in WIN
           if (ROOT / "frontier" / b / "FINDINGS.md").is_file()
           and re.search(r"non-finding", (ROOT / "frontier" / b / "FINDINGS.md")
                         .read_text(encoding="utf-8", errors="replace"), re.I)]
rec("arcs_declaring_a_NON_FINDING_in_the_body", nonfind)
chk("FINDING__arcs_whose_body_declares_a_NON_FINDING_still_say_PROVED", len(nonfind) >= 2,
    arcs=nonfind)

# THE CONTROL that makes the verdict finding fair. The SAME thirty arcs carry an atlas `status`
# field, and THAT one discriminates four ways. So the seat did record the distinction -- just not
# in the field the negatives hunts select on. The defect is a routing failure between two
# metadata fields, not an absence of judgement.
AT = json.loads(read("scripts/atlas/atlas_data.json"))["probes"]
win_status = Counter(AT[f"B{n}"]["status"] for n, _, _ in WIN if f"B{n}" in AT)
rec("window_atlas_statuses", dict(win_status))
chk("CONTROL__the_atlas_status_field_DOES_discriminate_across_the_same_thirty_arcs",
    len(win_status) >= 3, statuses=dict(win_status))
chk("...so_the_judgement_exists__it_is_the_verdict_field_that_does_not_carry_it",
    len(win_status) >= 3 and len(win_v) == 1)

# ---------------------------------------------------------------------------
# THE FINDING THAT OUTRANKS THE REST: six red instruments behind a green suite at 5b26e51.
# Locked structurally -- the six are named, their repairs are asserted at the repair sites, and
# the systemic fix is asserted to exist and to be wired where it can actually run.
# ---------------------------------------------------------------------------
rec("instruments_silently_red_at_5b26e51", sorted(SILENT_RED))
for n in SILENT_RED:
    src = read(glob.glob(f"frontier/B{n}_*/verify.py")[0].replace(str(ROOT) + "/", ""))
    chk(f"B{n}_carries_its_repair_and_says_why", "REPAIRED BY REVIEW 1" in src)

IFRESH = "scripts/checks/instrument_freshness.py"
chk("the_systemic_fix_EXISTS__a_sweep_that_re_runs_every_instrument",
    (ROOT / IFRESH).is_file() and "STALE-GREEN" in read(IFRESH))
chk("...and_it_reads_all_three_live_verdict_spellings_not_just_this_windows",
    all(k in read(IFRESH) for k in ('"all_pass"', '"all_ok"', '"checks"')))
chk("...and_it_is_wired_as_a_SUITE_TEST_because_5m20s_is_too_slow_for_a_per_push_gate",
    (ROOT / "tests/test_instrument_freshness.py").is_file()
    and "instrument_freshness" not in read("scripts/gates/gates.py"))
chk("...and_the_per_push_version_is_REGISTERED_rather_than_pretended",
    "R1-12" in read("docs/progress/REVIEW_1_CONSOLIDATION_SEAT_2026-08-12.md")
    if (ROOT / "docs/progress/REVIEW_1_CONSOLIDATION_SEAT_2026-08-12.md").is_file() else True)

# THE CORRECTION AGAINST THIS REVIEW'S OWN FIRST DRAFT. It reported "29 reproducers re-executed,
# 29 pass, 0 fail" and graded them RUN -- measured by EXIT CODE, which almost none of them set.
propagating = [n for n, b, _ in WIN
               if glob.glob(str(ROOT / "frontier" / b / "verify.py"))
               and re.search(r"SystemExit|sys\.exit\(",
                             read(glob.glob(f"frontier/B{n}_*/verify.py")[0]
                                  .replace(str(ROOT) + "/", "")))]
rec("window_instruments_that_propagate_failure_to_the_exit_code", sorted(propagating))
chk("CORRECTION__almost_no_arc_instrument_exits_non_zero_when_it_fails",
    len(propagating) <= 3, propagating=sorted(propagating),
    of=len([1 for n, b, _ in WIN if glob.glob(str(ROOT / "frontier" / b / "verify.py"))]))

repro = [b for n, b, _ in WIN if not glob.glob(str(ROOT / "frontier" / b / "*.py"))]
rec("window_arcs_with_no_reproducer", repro)
chk("twenty_nine_of_thirty_carry_a_reproducer", len(repro) == 1, missing=repro)

# ---------------------------------------------------------------------------
# ITEM 6 -- THE §5.1 PROMOTION SWEEP
# ---------------------------------------------------------------------------
CL = read("CLAIMS.md")
cites = re.findall(r"B10(?:2[4-9]|3\d|4\d|5[0-3])\b", CL)
rec("window_citations_in_CLAIMS_md", len(cites))
chk("nothing_from_this_window_was_promoted_to_CLAIMS_md__the_firewall_held",
    len(cites) <= 3)
chk("...and_the_citations_that_ARE_there_are_correction_banners_not_promotions",
    all(k in CL for k in ("re-labelled 2026-08-11 by B1036", "NAME COLLISION, declared 2026-08-11 (B1034)")))

# ---------------------------------------------------------------------------
# ITEM 7 -- PROTOCOL INTEGRITY
# ---------------------------------------------------------------------------
SL = read("docs/SEAL_LEDGER.md")
sealed = sorted(set(int(x) for x in re.findall(r"\bB(10(?:2[4-9]|3\d|4\d|5[0-3]))\b", SL)))
rec("window_arcs_with_a_seal", sealed)
chk("exactly_one_arc_in_the_window_is_sealed__B1024", sealed == [1024], sealed=sealed)

DECL_RX = re.compile(r"unsealed|no seal|not sealed|without a seal|no prereg", re.I)
declared = [b for n, b, _ in WIN
            if (ROOT / "frontier" / b / "FINDINGS.md").is_file()
            and DECL_RX.search((ROOT / "frontier" / b / "FINDINGS.md")
                               .read_text(encoding="utf-8", errors="replace"))]
rec("unsealed_arcs_that_DECLARE_being_unsealed", declared)
chk("FINDING__twenty_nine_arcs_are_unsealed_and_almost_none_declares_it",
    len(sealed) == 1 and len(declared) <= 4, unsealed=29, declaring=len(declared))
# Main's R43/R44 declare every unsealed arc in its header. That is the standard this window missed.
if MAIN_RV:
    chk("...against_mains_standard_which_declares_each_unsealed_arc_in_its_header",
        "openly unsealed" in MAIN_RV)

# ---------------------------------------------------------------------------
# THE HEADLINE FINDING -- the window's own metric triages on the verdict field
# ---------------------------------------------------------------------------
CUR = ["docs/LAW_MAP.md", "docs/THE_FRAMEWORK.md", "docs/THEOREM_LEDGER.md", "CLAIMS.md",
       "docs/THE_LADDER.md"]
blob = "\n".join(read(p) for p in CUR)


def cited(n):
    return bool(re.search(rf"\bB{n}\b", blob) or re.search(rf"B{n}_", blob))


counted, invisible = 0, Counter()
for n, b, v in ALL:
    if v.get("instrument") or cited(n):
        continue
    if v.get("verdict") == "PROVED":
        counted += 1
    else:
        invisible[v.get("verdict")] += 1
inv = sum(invisible.values())
rec("debt_as_the_metric_counts_it", counted)
rec("uncited_arcs_invisible_to_the_metric_by_verdict_field", dict(invisible))
rec("share_of_the_uncited_population_the_metric_shows", round(counted / (counted + inv), 4))

# RETRACTED AND REPLACED. The three checks that stood here locked the review's ORIGINAL headline:
# "the metric counts 175 and is blind to 191 -- 48% of its own subject", framed as L166's defect.
# THAT FRAMING WAS WRONG and the checks would have certified it, because the arithmetic is right
# and the SENTENCE was not -- which is why a lock over a number never certifies the claim built on
# it. What the re-read found:
#
#   * DEBT_LEDGER DECLARES its scope, in a table added by qB1033 -- an arc of this same window:
#     REPRESENTATION_TRIAGE = PROVED u NEGATIVE, this ledger = PROVED, "each right for its own
#     question";
#   * representation_sweep.py backs that in CODE, not prose: it rejects any verdict outside
#     (PROVED, NEGATIVE);
#   * and that register is GATED -- `representation-sweep` fails the build on an untriaged arc.
#     So the 191 "invisible" arcs are covered by a STRONGER mechanism than the ungated ledger.
#
# What survives is a PARTITION REMAINDER, an order of magnitude smaller: the two registers divide
# the corpus by verdict and neither takes OPEN or RETRACTED.
chk("the_debt_metric_does_select_on_the_verdict_field__the_factual_part",
    'verdict") == "PROVED"' in B1052V or "verdict'] == 'PROVED'" in B1052V)
DL = read("docs/consolidation/DEBT_LEDGER.md")
RS = read("scripts/checks/representation_sweep.py")
chk("CORRECTION__the_scope_is_DECLARED_in_the_ledger_itself_by_this_windows_own_qB1033",
    "| verdicts | PROVED ∪ NEGATIVE | PROVED |" in DL and "B1033" in DL)
chk("CORRECTION__and_the_CODE_agrees_so_it_is_not_merely_prose",
    'not in ("PROVED", "NEGATIVE")' in RS)
_gates = read("scripts/gates/gates.py")
chk("CORRECTION__the_NEGATIVE_complement_is_covered_by_a_GATED_register",
    '"representation-sweep"' in _gates and "def gate_representation_sweep" in _gates
    and "An untriaged" in read("docs/REPRESENTATION_TRIAGE.md"))

remainder = {k: v for k, v in invisible.items() if k not in ("PROVED", "NEGATIVE")}
outside_both = Counter(v.get("verdict") for _, _, v in ALL
                       if v.get("verdict") not in ("PROVED", "NEGATIVE"))
rec("verdicts_outside_BOTH_registers_corpus_wide", dict(outside_both))
rec("uncited_non_instrument_arcs_outside_both_registers", dict(remainder))
chk("WHAT_SURVIVES__OPEN_and_RETRACTED_fall_outside_BOTH_registers",
    set(outside_both) <= {"OPEN", "RETRACTED"} and sum(outside_both.values()) > 0,
    outside=dict(outside_both))
chk("...and_the_real_gap_is_an_order_of_magnitude_SMALLER_than_the_retracted_claim",
    0 < sum(remainder.values()) < inv / 5, gap=sum(remainder.values()), retracted_claim=inv)
_art_rel = "docs/progress/REVIEW_1_CONSOLIDATION_SEAT_2026-08-12.md"
chk("...and_the_review_RETRACTS_the_original_in_place_rather_than_softening_it",
    ("RETRACTED AND REPLACED" in read(_art_rel)
     and "That framing does not survive" in flat(read(_art_rel)))
    if (ROOT / _art_rel).is_file() else True)
# The window's own L166 is the rule this violates, and it is registered as a lead, not a fix.
chk("L166_is_registered_as_an_OPEN_LEAD_awaiting_the_owner",
    re.search(r"## L166 —.*PROVED", read("docs/OPEN_LEADS.md")) is not None)
chk("and_twelve_leads_L155_to_L166_were_registered_by_this_window",
    len(set(re.findall(r"(?m)^## (L1(?:5[5-9]|6[0-6])) —", read("docs/OPEN_LEADS.md")))) == 12)

# ---------------------------------------------------------------------------
# THE ARTIFACT ITSELF -- the review must carry what the commission required
# ---------------------------------------------------------------------------
ART = "docs/progress/REVIEW_1_CONSOLIDATION_SEAT_2026-08-12.md"
if (ROOT / ART).is_file():
    A = flat(read(ART))
    chk("ARTIFACT_declares_its_modulus_with_edges", "qB1024–qB1053" in A or "qB1024-qB1053" in A)
    chk("ARTIFACT_carries_a_parseable_action_items_block",
        re.search(r"(?m)^#{2,4} Action items \(Review 1", read(ART)) is not None)
    chk("ARTIFACT_asks_the_7d_certification_standard_of_itself",
        "without being misled" in A)
    chk("ARTIFACT_uses_REBUILT_and_RUN_labels", "REBUILT" in A and "RUN" in A)
    chk("ARTIFACT_marks_NOT_REACHED_as_a_first_class_disposition", "NOT-REACHED" in A)
    chk("ARTIFACT_scopes_its_measurements_by_authorship", "excluded" in A.lower())
    chk("ARTIFACT_credits_cc3s_independent_reproduction_rather_than_re_adjudicating",
        "cc3" in A and "28 candidates" in A)
    chk("ARTIFACT_states_it_never_merges", "never merges" in A)
    chk("ARTIFACT_carries_an_anchor_commit", "anchor-commit:" in read(ART))
else:
    chk("ARTIFACT_not_written_yet", True, disposition="NOT-REACHED")

# ---------------------------------------------------------------------------
# THE REVIEW'S QUOTED CHECK COUNT, CHECKED AGAINST ITSELF. The artifact said "64/64" while this
# instrument had grown to 67 -- a stale number inside a review about stale numbers, and it would
# have shipped. Compared against the live length rather than a literal, so it cannot drift again.
_art = ROOT / "docs/progress/REVIEW_1_CONSOLIDATION_SEAT_2026-08-12.md"
if _art.is_file():
    _q = re.search(r"(\d+)/(\d+) checks pass at this anchor", _art.read_text(encoding="utf-8"))
    _n = len(R["checks"]) + 1                      # +1: this check is not in the dict yet
    chk("ARTIFACT_quotes_this_instruments_ACTUAL_check_count",
        _q is not None and int(_q.group(1)) == int(_q.group(2)) == _n,
        quoted=_q.group(0) if _q else None, actual=_n)

bad = [k for k, v in R["checks"].items() if not v["pass"]]
R["all_pass"] = not bad
out = pathlib.Path(__file__).with_name("results.json")
out.write_text(json.dumps(R, indent=1, sort_keys=True, default=str), encoding="utf-8")
print(f"B1054: {len(R['checks']) - len(bad)}/{len(R['checks'])} checks pass")
for k in bad:
    print("  FAIL", k, R["checks"][k])
raise SystemExit(1 if bad else 0)
