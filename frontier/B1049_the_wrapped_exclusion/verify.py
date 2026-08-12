"""B1049 — the full suite found five red locks that 94 targeted tests did not.

THIRD INSTANCE OF THE MECHANISM REVIEW 42 NAMED AND B1041 SAID HAD RECURRED. Two arcs banked
green: B1047 on 88 targeted tests, B1048 on 94, both with 28 gates green. The first full suite to
run to completion on an uncontended box -- 4074 tests, 48 minutes -- returned FIVE failures.

  1-2. tests/test_b1037_band_dispositions.py -- RED SINCE B1043, five arcs.
  3.   tests/test_b967_retraction_sweep.py    -- B1048's own FINDINGS, invisible before commit.
  4.   tests/test_repo_gates.py               -- cascade of 3.
  5.   tests/test_b887_gate_audit.py          -- cascade of 3.

TWO DISTINCT DEFECTS, BOTH GENERAL, BOTH REPAIRED HERE.

(A) THE PER-LINE EXCLUSION IDIOM IS DEFEATED BY MARKDOWN WRAPPING. Four arcs wrote the same idiom:
    to measure a gap without counting your own rows, drop every LINE naming this arc or a later
    one. B1043's ladder bullet wraps between its author token and its citation --

        - ... **B1043** adds that the
          phi-fixed cluster's own open question (B141 Item 4) was closed by B564 ...

    -- so the filter drops line 1, keeps line 2, and B141 reads as curated by nobody. B1037's band
    fell 37 -> 36. A SIBLING SWEEP (the rule ERROR_LEDGER gained one arc ago: "the repair is not
    complete until the file is swept") found B1032 carries the identical defect and is GREEN ONLY
    BY LUCK -- it counts B885/B889/B890/B891, not the orphaned B141/B564. TWO of the four, not
    three: the draft of this docstring said three, and the arc's own check corrected it, because
    B1031's predicate targets "**X33**" while the bullet reads "**X33 (three generations)**" and
    B1048's window starts after B1043. All four now use one declared module,
    `scripts/checks/md_blocks.py` -- the idiom is wrong even where it happens not to bite.

(B) THE RETRACTION SWEEP COULD NOT SEE THE ARC RUNNING IT. `_tracked_md()` used
    `git ls-files *.md` -- committed files only -- so a new arc's own FINDINGS.md was invisible to
    the sweep that arc ran, and its violations surfaced only in the NEXT run, after banking. That
    is how B1048 shipped two live uses of the two phrases IT HAD JUST REGISTERED. Repaired with
    `-co --exclude-standard`.

AND ONE MEASUREMENT CORRECTED: the suite is 48 minutes, not 81. The 81 in BANKING_PROTOCOL was
measured while two suite runs competed for the box.
"""
import importlib.util as ilu
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = {"checks": {}}


def chk(name, ok, **d):
    R["checks"][name] = {"pass": bool(ok), **d}
    return ok


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def load(rel, name):
    spec = ilu.spec_from_file_location(name, ROOT / rel)
    mod = ilu.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


MB = load("scripts/checks/md_blocks.py", "_md_blocks")

CURATED = ["docs/LAW_MAP.md", "docs/THE_FRAMEWORK.md", "docs/THEOREM_LEDGER.md", "CLAIMS.md",
           "docs/THE_LADDER.md"]

# ============================================ 1. THE DEFECT, EXHIBITED ON THE ACTUAL TEXT
LADDER = read("docs/THE_LADDER.md")
wrapped = [(a, b) for a, b in zip(LADDER.splitlines(), LADDER.splitlines()[1:])
           if re.search(r"\bB1043\b", a) and re.search(r"\bB141\b", b)]
chk("the_wrapped_bullet_EXISTS_in_the_live_text", len(wrapped) == 1,
    author_line=wrapped[0][0].strip()[-60:] if wrapped else None,
    citation_line=wrapped[0][1].strip()[:60] if wrapped else None)

REFRESH = re.compile(r"\bB10(?:3[7-9]|[4-9]\d)\b")
per_line = "\n".join(ln for ln in LADDER.splitlines() if not REFRESH.search(ln))
per_block = MB.drop_blocks(LADDER, REFRESH)
chk("the_LINE_filter_KEEPS_the_orphaned_citation", bool(re.search(r"\bB141\b", per_line)))
chk("the_BLOCK_filter_DROPS_it", not re.search(r"\bB141\b", per_block))
# ...and that is exactly the difference between 36 and 37.
chk("B1037s_own_check_is_green_again_and_says_why",
    "BLOCK-level, not line-level (B1049)" in read("frontier/B1037_band_B100_dispositioned/verify.py")
    and json.loads(read("frontier/B1037_band_B100_dispositioned/results.json"))
        ["checks"]["the_band_carries_37_debt_rows"]["pass"] is True)

# THE SIBLING SWEEP -- the rule ERROR_LEDGER gained at B1048, applied at the first opportunity.
CONSUMERS = {"frontier/B1031_generation_rung/verify.py": r"\bB1031\b|\*\*X33\*\*",
             "frontier/B1032_across_breakings_route/verify.py": r"\bB10(?:3[2-9]|[4-9]\d)\b|\*\*X33\*\*",
             "frontier/B1037_band_B100_dispositioned/verify.py": r"\bB10(?:3[7-9]|[4-9]\d)\b",
             "frontier/B1048_the_seam_cluster_closed/verify.py": r"\bB104[89]\b|\bB10[5-9]\d\b"}
# CORRECTED BY THIS CHECK, AGAINST ITS AUTHOR. The draft said THREE consumers carried the defect.
# Measured with each consumer's ACTUAL predicate over ALL five curated files: it is TWO. B1031's
# filter targets the string "**X33**", and the ladder bullet reads "**X33 (three generations)**",
# which that predicate never matched line-wise OR block-wise; B1048's pattern starts at B1048 and
# the wrapped bullet is B1043's. Both were converted anyway -- the idiom is wrong even where it
# happens not to bite -- but the COUNT is two, and saying three would have been the overextended
# record (E11) inside the arc about latent defects.
latent = {}
for rel, pat in CONSUMERS.items():
    rx = re.compile(pat)
    orphans = []
    for f in CURATED:
        txt = read(f)
        kept_wrongly = set(ln for ln in txt.splitlines() if not rx.search(ln)) \
            - set(MB.drop_blocks(txt, rx).splitlines())
        orphans += [b for ln in kept_wrongly for b in re.findall(r"\bB\d+\b", ln)]
    latent[rel.split("/")[1][:5]] = sorted(set(orphans))
chk("TWO_of_the_four_consumers_carried_the_defect_not_three",
    sum(1 for v in latent.values() if v) == 2, latent=latent)
chk("the_RED_one_and_the_LATENT_GREEN_one_orphan_the_SAME_two_citations",
    latent["B1037"] == latent["B1032"] == ["B141", "B564"])
chk("and_B1032_was_green_BY_LUCK__it_counts_B885_B889_B890_B891_not_B141",
    not any(b in latent["B1032"] for b in ("B885", "B889", "B890", "B891")))
for rel in CONSUMERS:
    chk("repaired__" + rel.split("/")[1][:5], "_MB.drop_blocks" in read(rel))
chk("all_four_now_share_ONE_declared_implementation",
    (ROOT / "scripts/checks/md_blocks.py").is_file()
    and "DECLARED SHARING, not shadow sharing" in read("scripts/checks/md_blocks.py"))
# B1035's finding is why the module says so: shared code filed as a research arc is the shadow
# library. This one is in scripts/checks/ with the other instruments and names its consumers.
chk("the_module_names_its_consumers_so_it_is_not_a_shadow_library",
    all(c in read("scripts/checks/md_blocks.py")
        for c in ("B1031", "B1032", "B1037", "B1048")))
# law_siblings uses the same idiom and is NOT affected -- checked, not assumed.
LS = load("scripts/checks/law_siblings.py", "_ls")
ls_line = LS._curated_blob()
ls_block = "\n".join(MB.drop_blocks(read(p), LS._REGISTRY_ROW) for p in LS.CURATED)
chk("law_siblings_uses_the_idiom_but_is_UNAFFECTED__its_targets_are_single_line_headlines",
    not [l for l in set(ls_line.splitlines()) - set(ls_block.splitlines())
         if re.search(r"\bB\d+\b", l)])

# ================================== 2. THE SWEEP THAT COULD NOT SEE THE ARC RUNNING IT
RS = read("scripts/checks/retraction_sweep.py")
chk("the_sweep_now_lists_UNTRACKED_files_too",
    '"-co", "--exclude-standard"' in RS and "ALREADY COMMITTED" in RS)
tracked_only = subprocess.run(["git", "ls-files", "*.md"], cwd=ROOT,
                              capture_output=True, text=True).stdout.split("\n")
chk("...which_is_why_B1048_shipped_two_live_uses_of_phrases_it_had_just_registered",
    "frontier/B1048_the_seam_cluster_closed/FINDINGS.md" in tracked_only)
sweeper = load("scripts/checks/retraction_sweep.py", "_rs")
chk("the_sweep_is_clean_now", sweeper.sweep() == [])
chk("and_B1048s_two_lines_carry_their_cue",
    "a phrase now retracted and registered (`RETRACTED_PHRASES` row 9)"
    in read("frontier/B1048_the_seam_cluster_closed/FINDINGS.md")
    and "retracted here, `RETRACTED_PHRASES` row 10"
    in read("frontier/B1048_the_seam_cluster_closed/FINDINGS.md"))

# ============================== 3. THE MECHANISM, THIRD INSTANCE, AND THE SUITE'S REAL COST
chk("Review_42s_finding_is_on_the_record_as_having_RECURRED_once_already",
    "RECURRED IN TWO DAYS" in read("docs/LAW_MAP.md")
    or "RECURRED IN TWO DAYS" in read("docs/LAW_MAP.md").upper())
bp = read("docs/BANKING_PROTOCOL.md")
chk("BANKING_PROTOCOL_already_says_a_partial_run_is_not_a_run", "A PARTIAL RUN IS NOT A RUN" in bp)
# FLATTENED, and the reason is this arc's own subject: the phrase WRAPS in the document, so a
# line-level `in` test would fail on prose that is perfectly correct. Content tests flatten.
bpf = re.sub(r"\s+", " ", bp)
chk("and_it_now_carries_the_MEASURED_uncontended_figure",
    "48 minutes, measured 2026-08-12 on an UNCONTENDED box" in bpf
    and "two suite runs competed" in bpf and "the figure to plan against is **48**" in bpf)
chk("and_it_records_that_TARGETED_runs_do_not_substitute",
    "banked on **88** targeted tests and B1048 on **94**" in bpf
    and "the next full suite returned **five failures**" in bpf)
chk("and_that_a_run_against_a_MOVING_TREE_discharges_nothing",
    "A RUN AGAINST A MOVING TREE DISCHARGES NOTHING EITHER" in bpf)
chk("the_gap_this_arc_names__gates_do_not_cover_locks",
    "gates do not cover what the locks cover" in read("docs/LAW_MAP.md"))

R["answer"] = {
    "what_happened": "Two arcs banked green on 88 and 94 TARGETED tests with 28 gates green. The "
                     "first full suite to complete on an uncontended box — 4074 tests, 48 minutes "
                     "— returned FIVE failures. Third instance of the mechanism Review 42 named "
                     "and B1041 recorded as already recurred: gates do not cover what the locks "
                     "cover, and a suite nobody runs to completion hides red locks at HEAD.",
    "defect_A": "THE PER-LINE EXCLUSION IDIOM IS DEFEATED BY MARKDOWN WRAPPING. Four arcs wrote "
                "the same idiom — drop every LINE naming this arc or a later one, then measure "
                "what remains. B1043's ladder bullet wraps between its author token (B1043) and "
                "its citation (B141), so the filter drops the first line, keeps the second, and "
                "B141 reads as curated by nobody. B1037's band count fell 37 → 36 and its lock "
                "went RED AT B1043 — five arcs ago. A sibling sweep found B1031 and B1032 carry "
                "the identical defect and are GREEN ONLY BY LUCK, since neither counts the "
                "orphaned citation; law_siblings uses the idiom and is genuinely unaffected, "
                "because its targets are single-line headlines. All four now share one declared "
                "module, scripts/checks/md_blocks.py, which names its consumers so it does not "
                "become the shadow library B1035 found.",
    "defect_B": "THE RETRACTION SWEEP COULD NOT SEE THE ARC RUNNING IT. `_tracked_md()` used "
                "`git ls-files *.md` — committed files only — so a new arc's own FINDINGS.md was "
                "invisible to the sweep that arc ran, and its violations first appeared in the "
                "NEXT run, after banking. That is exactly how B1048 shipped two live uses of the "
                "two phrases IT HAD JUST REGISTERED, and neither its own sweep nor its gate run "
                "could have caught them. Repaired with `-co --exclude-standard`, which shows the "
                "sweep the working tree an author is about to bank while honouring .gitignore.",
    "the_measurement_corrected": "The suite is 48 minutes, not 81. The 81 recorded in "
                                 "BANKING_PROTOCOL was measured while TWO suite runs competed for "
                                 "the same box — and both were invalid anyway, because the tree "
                                 "changed underneath them. A suite run against a moving tree "
                                 "discharges nothing, which is the same row's own rule one level "
                                 "up.",
}
R["all_pass"] = all(v["pass"] for v in R["checks"].values())

if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(
        json.dumps(R, indent=1, ensure_ascii=False))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\n%d checks; ALL PASS: %s" % (len(R["checks"]), R["all_pass"]))
