"""B1042 — the corpus names its lessons where it finds them; the register that generalises them
has not moved in 122 arcs.

B1041 found Review 42's governing finding recurring within two days because its prescribed action
was a prose checklist row. This is the same shape one level up, and it is the reason:

  * `docs/ERROR_LEDGER.md` — 36 classes, whose own header says "One entry per ERROR CLASS, not per
    incident. Reviews check the window's disclosed errors against this taxonomy" — has NOT BEEN
    UPDATED SINCE B920. The corpus is at B1042.
  * It is NOT in `doc_currency.py`'s LIVING set, so its staleness is invisible BY CONSTRUCTION.
    Neither is `RETRACTIONS.md`, nor `REPRESENTATION_TRIAGE.md`.
  * `E1`'s instance list still reads THREE, all from 2026-07-16 — while GOVERNANCE §13 calls E1
    "the program's single most recurrent error class".

Nothing here is a new error. Every instance cited is already banked, locked and disclosed in its
own arc. This arc makes the register reflect the arcs.
"""
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


EL_NOW = read("docs/ERROR_LEDGER.md")

# The PRE-REPAIR state is read from git, not from memory: this arc edits the register in the same
# commit that measures it, which is E37 itself. The exclusion is the commit boundary.
#
# REPAIRED BY REVIEW 1 (B1054). The boundary was written as `HEAD:docs/ERROR_LEDGER.md`, which was
# correct for exactly one moment -- while this arc was uncommitted and HEAD was its parent. Fifteen
# banks later `HEAD` is the POST-repair register, so all three checks below inverted and this
# instrument has been RED AT THE BRANCH TIP ever since, invisibly: `tests/test_b1042*.py` asserts
# over the committed `results.json`, which still records the green run from banking day.
#
# THE LESSON, and it is this arc's own subject one level up: an E37 exclusion anchored to a MOVING
# reference is not an exclusion. The boundary is now derived from the commit that INTRODUCED this
# arc, so it names the same bytes forever, and falls back to the recorded parent if the arc is not
# yet committed (the state the original was written in).
BOUNDARY_PARENT = "64388fd"          # the commit before B1042's bank; recorded, not assumed


def _pre_repair(rel):
    intro = subprocess.run(["git", "log", "--diff-filter=A", "--format=%H", "-1", "--",
                            "frontier/B1042_the_error_ledger/FINDINGS.md"],
                           capture_output=True, text=True, cwd=ROOT).stdout.strip()
    for ref in ([intro + "^"] if intro else []) + [BOUNDARY_PARENT]:
        out = subprocess.run(["git", "show", f"{ref}:{rel}"], capture_output=True, text=True,
                             cwd=ROOT).stdout
        if out:
            return out
    return ""


EL = _pre_repair("docs/ERROR_LEDGER.md")
assert EL, "could not read the pre-repair register from git"
CORPUS = max(int(m.group(1)) for d in (ROOT / "frontier").iterdir()
             if d.is_dir() and (m := re.match(r"B(\d+)_", d.name)))

# ------------------------------------------------- 1. the register stopped, and nothing says so
highest = max(int(x) for x in re.findall(r"\bB(\d{2,4})\b", EL))
chk("the_error_ledger_has_not_moved_in_over_a_hundred_arcs",
    highest <= 925 and CORPUS - highest > 100,
    highest_arc_cited="B%d" % highest, corpus_at="B%d" % CORPUS, lag=CORPUS - highest,
    latest_date=sorted(set(re.findall(r"20\d\d-\d\d-\d\d", EL)))[-1],
    note="its own header: 'Reviews check the window's disclosed errors against this taxonomy: a "
         "recurrence strengthens the class's standing rule; a new class gets a new entry'")

DC = read("scripts/checks/doc_currency.py")
LIVING = re.search(r"LIVING = \{(.*?)\n\}", DC, re.S).group(1)
unwatched = [f for f in ("ERROR_LEDGER.md", "RETRACTIONS.md", "REPRESENTATION_TRIAGE.md")
             if f not in LIVING]
chk("and_the_currency_gate_cannot_see_it_BY_CONSTRUCTION",
    len(unwatched) == 3,
    unwatched_governed_registers=unwatched, living_count=LIVING.count(":"),
    note="doc-currency watches 15 documents and none of the three GOVERNED REGISTERS whose entire "
         "job is currency. Same gate hole B1036 found for knowledge/INDEX.md")

# ------------------------------------------------- 2. E1: the count the register carries is stale
e1 = [l for l in EL.splitlines() if l.startswith("| E1 |")][0]
e1_instances = e1.split("|")[-2]
COLLISIONS = {
    "theta naming three distinct objects": "B1026",
    "B62 = 2 x P33, one identity in two conventions": "B1026",
    "B939's transposed shadow-map prose": "B1024",
    "kappa naming two quantities, one exported by the certified core": "B1034",
    "the entropy factor of two (4 log phi vs 2 log phi)": "B1036",
}
chk("E1_still_lists_three_instances_all_from_one_day_in_July",
    e1_instances.count(";") + 1 == 3 and "2026-07-16" in e1_instances
    and not any(b in e1_instances for b in ("B1024", "B1026", "B1034", "B1036")),
    registered=3, found_this_refresh=len(COLLISIONS),
    note="GOVERNANCE §13 calls E1 'the program's single most recurrent error class'. That claim is "
         "now far better supported than when it was written, and the register cannot show it")
b1034 = read("frontier/B1034_two_kappas/FINDINGS.md")
b1036 = read("frontier/B1036_knowledge_room/FINDINGS.md")
_flat = re.sub(r"\s+", " ", b1036)      # B1036's sentence spans a line break
chk("and_the_five_new_collisions_are_each_banked_and_SELF_COUNTED",
    "four undeclared-convention collisions" in b1034
    and "fifth undeclared-convention collision this refresh has found" in _flat,
    collisions=COLLISIONS,
    note="the arcs count themselves: B1034 says 'four', B1036 adds 'the fifth'. Nothing new is "
         "asserted here -- the count is read off the arcs")

# ------------------------------------------------- 3. the pass's OWN most recurrent failure
SELF_MEASURE = {"B1032": 4, "B1033": 6, "B1035": 8, "B1036": 9, "B1037": 10}
LADDER = read("docs/THE_LADDER.md")
REVIEWS = read("docs/progress/REVIEWS.md")
chk("the_hazard_IS_named_twice__and_in_NEITHER_case_as_a_class",
    "Registering a gap creates hits for the gap" in LADDER
    and "self-inflates" in REVIEWS
    and "self-inflat" not in EL and "self-measur" not in EL
    and "self-inflat" not in read("docs/PRACTICES.md"),
    named_in=["docs/THE_LADDER.md X31 (a parenthetical about ONE row)",
              "docs/progress/REVIEWS.md Review 42 (an annotation of that row)"],
    absent_from=["docs/ERROR_LEDGER.md (36 classes)", "docs/PRACTICES.md"],
    note="THE POINT, and it is B1041's shape one level up: the corpus NAMES its lessons where it "
         "finds them. Both notes are attached to the Markov-blanket row they were found on. "
         "Neither generalises to the taxonomy, so the next arc meets it fresh")
chk("meanwhile_the_refresh_hit_it_ten_times_across_nine_arcs",
    max(SELF_MEASURE.values()) == 10 and len(SELF_MEASURE) == 5,
    self_counted_by_the_arcs=SELF_MEASURE,
    note="read from the arcs' own self-correction lines: B1033 'SIX instances across five arcs', "
         "B1035 'eighth ... in seven arcs', B1036 'ninth ... in eight arcs', B1037 'Tenth'. By a "
         "wide margin the most frequent failure of this pass, and a reader of the error ledger "
         "would never learn it exists")

# ------------------------------------------------- 4. what is NOT minted, and why
chk("one_offs_are_recorded_as_INSTANCES_of_existing_classes_not_new_entries",
    "One entry per ERROR CLASS, not per incident" in EL,
    filed_under_existing={
        "B1039's anti-homomorphic sym_power": "E31 (instrument-precondition unchecked) -- ONE "
            "instance; the instrument was algebraically wrong and only its control knew",
        "B1041's d3_measure clobber (mine)": "E36 (artifact-clobber) -- the class already exists "
            "and already names the mechanism; this is an instance, not a discovery",
    },
    note="the ledger's own header forbids per-incident entries. Two of this pass's errors get "
         "INSTANCE rows under existing classes rather than classes of their own")

# ------------------------------------------------- 5. the repair landed, and the gate change did not
EL2 = EL_NOW
chk("the_register_now_carries_the_five_collisions",
    all(b in EL2.split("| E2 |")[0] for b in ("B1024", "B1026", "B1034", "B1036")),
    note="E1's instance list extended in place, each collision cited to its banked arc")
chk("and_the_two_missing_classes_exist",
    "| E37 |" in EL2 and "| E38 |" in EL2
    and "Self-measurement" in EL2 and "Progress-eroded threshold" in EL2
    # REPAIRED BY REVIEW 1 (B1054), AND THE SWEEP THAT FOUND IT WAS THIS ARC'S OWN LESSON.
    # `== 38` is E38 inside the arc that REGISTERED E38 -- an absolute count over a register whose
    # purpose is to grow. Review 1 repaired the identical lock in `tests/test_b1042_error_ledger.py`
    # first and MISSED this one, which is precisely the "the repair is not complete until the FILE
    # is swept" rule failing at one level up: the file was swept, the ARC was not. It was caught by
    # `scripts/checks/instrument_freshness.py` on its first real use.
    and len(re.findall(r"^\| E\d+ \|", EL2, re.M)) >= 38,
    classes=len(re.findall(r"^\| E\d+ \|", EL2, re.M)),
    note="E37 credits THE_LADDER X31 and Review 42 as having named it first; E38 credits B1033's "
         "own prose as having written the correct form before the check failed to implement it")
chk("and_the_two_one_offs_are_INSTANCES_not_classes",
    "B1039" in EL2.split("| E32 |")[0].split("| E31 |")[-1] and "B1041" in EL2.split("| E37 |")[0].split("| E36 |")[-1],
    note="E31 gains B1039's anti-homomorphic instrument; E36 gains B1041's clobber. The header "
         "forbids per-incident entries and it is honoured")
chk("the_GATE_change_is_registered_and_NOT_made",
    "ERROR_LEDGER.md" not in re.search(r"LIVING = \{(.*?)\n\}", read("scripts/checks/doc_currency.py"), re.S).group(1)
    and "L163" in read("docs/OPEN_LEADS.md"),
    note="adding the three governed registers to doc_currency's LIVING is a one-line gate change "
         "and an owner decision -- the L159/L160/L161 pattern. Registered as L163, not made")

R["proposed"] = {
    "E37 self-measurement": {
        "class": "an arc that both MEASURES a gap and FILLS it invalidates its own metric",
        "standing_rule": "a measurement published by the same commit that changes what it "
                         "measures must name its own exclusion set, in the artifact, next to the "
                         "number (B1033's rule, stated after it cost re-runs)",
        "instances": "ten across nine arcs this refresh; first named at THE_LADDER X31",
    },
    "E38 progress-eroded threshold": {
        "class": "a lock encoding a structural claim as an ABSOLUTE COUNT, inside a programme "
                 "whose purpose is to change that count",
        "standing_rule": "a lock on a quantity the programme intends to move states it as a SHARE "
                         "or a structural invariant, never as a raw count",
        "instances": "B1033's `> 200 rows dropped`, broken by B1038+B1039+B1040 at 198/216 with "
                     "the finding completely intact (lowest above-bar row still B870, share 92 %)",
    },
}

R["all_pass"] = all(v["pass"] for v in R["checks"].values())
if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(
        json.dumps(R, indent=1, ensure_ascii=False, default=str))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\nALL PASS:", R["all_pass"], " checks:", len(R["checks"]))
