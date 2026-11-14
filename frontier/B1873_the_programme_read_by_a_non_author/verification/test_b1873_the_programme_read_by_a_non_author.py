"""B1873 -- the recount is what the script prints, and the four repairs are in force in the programme as built.
The refusals themselves are planted and fired in B1861's own lock (test_the_joins_the_seals_rule_needs_and_each_refusal_can_fire)."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
P = json.loads((ROOT / "frontier/B1861_the_closure_programme/PROGRAMME.json").read_text(encoding="utf-8"))
PK = {w["id"]: w for w in P["packages"]}


def _up(i, seen=None):
    seen = set() if seen is None else seen
    for x in PK[i]["needs_all"]:
        if x not in seen:
            seen.add(x)
            _up(x, seen)
    return seen


def test_the_recount_runs_and_says_what_the_findings_quote():
    out = subprocess.run([sys.executable, "-B", str(HERE / "read_checks.py")], capture_output=True, text=True, check=True, timeout=300).stdout
    for s in ("every one is in a package upstream of the sealed card: True", "the sealed card now waits on the suite and on the comparison's own instruments: True",
              "packages marked started while a need has not started: 0", "every finding names what it bears on: True",
              "the script the foundation cites for the live price exits 1"):
        assert s in out, s
    # CORRECTED 2026-11-13 (Review 81, the SM seat's finding 08): the exit code alone passed while item 6 had lost its failure
    # line; the line itself is now asked for, in the run and in the kept output
    assert "exits 1: - VERDICT: the live figure" in out and "(no failure line)" not in out
    sealed = (HERE / "read_checks_run.txt").read_text(encoding="utf-8")
    assert "(no failure line)" not in sealed and "exits 1: - VERDICT: the live figure" in sealed      # Review 81, the SM seat's 08
    # 8 at the read; 9 since the owner named the orientation's condition on 2026-11-11 (B1879), which the run now prints
    # The count of debts joined to nothing was typed here (64 at the read, then 65, 66, 67): a pin on a live value, edited each time
    # a debt was registered.  What it stood for is asserted instead: the run's three counts agree
    import re as _re
    m = _re.search(r"debts on the map: (\d+); joined to a node by an edge: (\d+); joined to nothing: (\d+)", sealed)
    assert m and int(m.group(3)) == int(m.group(1)) - int(m.group(2))
    assert "an exit with no objection on the page: 9" in sealed
    # 2026-11-12 (R80b, part 6; a reader's supplement on the arcs main changed at Review 80, its finding 13; not checked by
    # main).  The two counts above are read from the kept run and were never read from the run made now.  They are read
    # from both, and the lines of the kept run that state a count are compared with the live ones.
    assert _what_the_live_run_does_not_say(out) == [], _what_the_live_run_does_not_say(out)
    assert _the_lines_that_differ(out, sealed) == [], _the_lines_that_differ(out, sealed)


def _what_the_live_run_does_not_say(run):
    import re as _re
    bad = []
    m = _re.search(r"debts on the map: (\d+); joined to a node by an edge: (\d+); joined to nothing: (\d+)", run)
    if not m:
        bad.append("the run does not print the three counts of debts")
    elif int(m.group(3)) != int(m.group(1)) - int(m.group(2)):
        bad.append("the three counts of debts do not agree: %s, %s, %s" % m.groups())
    if "an exit with no objection on the page: 9" not in run:
        bad.append("the run does not print nine exits with no objection on the page")
    return bad


THE_LINE_THAT_ENDS_IN_ANOTHER_SCRIPTS_WORDS = "6. the script the foundation cites for the live price exits 1:"


def _the_lines_that_differ(live, kept, but=THE_LINE_THAT_ENDS_IN_ANOTHER_SCRIPTS_WORDS):
    """The numbers of the lines, counted from one, on which the kept run is not the live run.  A line that begins with
    `but` is compared no further than that: it ends in what another script printed when it failed, which is not a count
    and differs between the kept run and this machine's."""
    a, b = live.rstrip("\n").split("\n"), kept.rstrip("\n").split("\n")
    cut = lambda l: but if l is not None and but and l.startswith(but) else l
    return [i + 1 for i in range(max(len(a), len(b)))
            if cut(a[i] if i < len(a) else None) != cut(b[i] if i < len(b) else None)]


def test_a_live_run_that_differs_from_the_kept_one_is_reported():
    kept = (HERE / "read_checks_run.txt").read_text(encoding="utf-8")
    import re as _re
    assert _what_the_live_run_does_not_say(kept) == [] and _the_lines_that_differ(kept, kept) == []
    m = _re.search(r"debts on the map: (\d+); joined to a node by an edge: (\d+); joined to nothing: (\d+)", kept)
    # a live run in which one debt more is joined to nothing: the counts no longer agree, and the line differs from the kept one
    one_more = kept.replace("joined to nothing: %s" % m.group(3), "joined to nothing: %d" % (int(m.group(3)) + 1), 1)
    assert len(_what_the_live_run_does_not_say(one_more)) == 1 and len(_the_lines_that_differ(one_more, kept)) == 1
    # a live run with a tenth exit
    ten = kept.replace("an exit with no objection on the page: 9", "an exit with no objection on the page: 10", 1)
    assert len(_what_the_live_run_does_not_say(ten)) == 1 and len(_the_lines_that_differ(ten, kept)) == 1
    # a live run in which a debt was registered and joined to nothing: its counts agree, and it is still not the kept run
    moved = kept.replace("debts on the map: %s;" % m.group(1), "debts on the map: %d;" % (int(m.group(1)) + 1), 1)
    moved = moved.replace("joined to nothing: %s" % m.group(3), "joined to nothing: %d" % (int(m.group(3)) + 1), 1)
    assert _what_the_live_run_does_not_say(moved) == [] and len(_the_lines_that_differ(moved, kept)) == 1
    # the twin: the line that ends in another script's words is the same line with another ending, and not with another beginning
    six = [l for l in kept.split("\n") if l.startswith(THE_LINE_THAT_ENDS_IN_ANOTHER_SCRIPTS_WORDS)]
    assert len(six) == 1
    n = kept.split("\n").index(six[0]) + 1
    assert _the_lines_that_differ(kept.replace(six[0], THE_LINE_THAT_ENDS_IN_ANOTHER_SCRIPTS_WORDS + " other words", 1), kept) == []
    assert _the_lines_that_differ(kept.replace(six[0], "7" + six[0][1:], 1), kept) == [n]


def test_the_four_repairs_are_in_force():
    F = P["findings"]
    assert sorted(P["bears_on"]) == sorted(F) and all(P["bears_on"][k] for k in F)
    repo = [k for k, b in P["bears_on"].items() if "REPOSITORY" in b]
    up = _up("WP-5.3")
    assert repo and all(F[k]["wp"] in up for k in repo)
    assert {"WP-0.2", "WP-0.5"} <= set(PK["WP-5.3"]["needs"])
    assert not [(w, x) for w in PK for x in PK[w]["needs_all"] if not PK[w]["status"].startswith("NOT STARTED") and PK[x]["status"].startswith("NOT STARTED")]
    fixed = [k for k, f in F.items() if f["state"] == "FIXED"]
    # "fixed" is main's word and the re-audit's verdict is a field apart: a fixed finding either carries that seat's acceptance,
    # or is listed as fixed and not yet re-audited.  (When this lock was written all eight fixed ones were accepted; main has
    # fixed more since, and those are shown as not yet read by that seat, never as accepted.)
    unread = P["stats"]["fixed_and_not_yet_re_audited"]
    assert fixed and sorted(k for k in fixed if k not in P["accepted"]) == sorted(unread)
    assert all(P["accepted"][k].startswith("accepted") for k in fixed if k in P["accepted"])
    # eight when this lock was written; eleven after the seat's fourth re-audit read B1878's two and accepted E3 (B1880)
    # 2026-11-11: the line pinned eleven, and the seat's sixth re-audit accepted a twelfth (E5).  What it holds now is the rule:
    # every finding marked fixed has a re-audit's acceptance, and none is fixed and unread.
    # 2026-11-12 (R80b, part 6; the same supplement, finding 13; not checked by main).  The line below this note read
    #     assert len([k for k in fixed if k in P["accepted"]]) == len(fixed) >= 11 and unread == []
    # It contradicts the allowance written above it: by that allowance a finding that main has fixed and the seat has not
    # read again is listed as such, and by this line there may be none.  The builder's reading, which is main's to change:
    # the allowance is the rule, and "none is unread" was the state of that day.  The rule is held by one function, so that
    # it can be planted against; the state of the day is held as a floor, since an acceptance given is not taken back.
    assert _what_the_fixed_findings_do_not_satisfy(P) == [], _what_the_fixed_findings_do_not_satisfy(P)
    assert F["E3"]["state"] == "FIXED" and F["X3"]["wp"] == "WP-0.12" and F["X4"]["wp"] == "WP-0.11"
    # the control: a finding about the repository filed in a package the card does not wait on would be seen here
    outside = [w for w in PK if w not in up and w != "WP-5.3" and not w.startswith(("WP-5.4", "WP-6"))]
    assert not any(F[k]["wp"] in outside for k in repo)


ACCEPTED_ON_2026_11_12 = ("E10", "E13", "E3", "E5", "E6", "E7", "G1", "G2", "G3", "G4", "G9", "L5", "X1")   # read from the programme on that day


def _what_the_fixed_findings_do_not_satisfy(prog):
    F, acc, unread = prog["findings"], prog["accepted"], prog["stats"]["fixed_and_not_yet_re_audited"]
    fixed = [k for k, f in F.items() if f["state"] == "FIXED"]
    bad = []
    if not fixed:
        bad.append("no finding is marked fixed")
    for k in sorted(fixed):
        if k in acc and k in unread:
            bad.append("%s is accepted and is listed as not read again" % k)
        elif k in acc and not acc[k].startswith("accepted"):
            bad.append("%s is fixed and what the re-audit says of it does not begin with its acceptance" % k)
        elif k not in acc and k not in unread:
            bad.append("%s is fixed, has no acceptance, and is not listed as not read again" % k)
    bad += ["%s is listed as not read again and is not marked fixed" % k for k in sorted(unread) if k not in fixed]
    bad += ["%s was accepted on 2026-11-12 and is not now" % k for k in ACCEPTED_ON_2026_11_12
            if not (k in acc and acc[k].startswith("accepted") and F.get(k, {}).get("state") == "FIXED")]
    return bad


def test_a_finding_fixed_and_not_read_again_is_allowed_and_one_that_is_neither_is_not():
    import copy
    assert _what_the_fixed_findings_do_not_satisfy(P) == []
    assert sorted(k for k, f in P["findings"].items() if f["state"] == "FIXED" and k in P["accepted"]) >= sorted(ACCEPTED_ON_2026_11_12)
    other = sorted(k for k, f in P["findings"].items() if f["state"] != "FIXED")[0]
    # what the allowance allows, and the line as it stood refused: main fixes one more, and it is listed as not read again
    q = copy.deepcopy(P)
    q["findings"][other]["state"] = "FIXED"
    q["stats"]["fixed_and_not_yet_re_audited"] = [other]
    q["accepted"].pop(other, None)
    assert _what_the_fixed_findings_do_not_satisfy(q) == []
    fixed = [k for k, f in q["findings"].items() if f["state"] == "FIXED"]
    assert not (len([k for k in fixed if k in q["accepted"]]) == len(fixed) >= 11 and q["stats"]["fixed_and_not_yet_re_audited"] == [])   # the line as it stood
    # fixed, and neither accepted nor listed
    q = copy.deepcopy(P)
    q["findings"][other]["state"] = "FIXED"
    q["accepted"].pop(other, None)
    assert len(_what_the_fixed_findings_do_not_satisfy(q)) == 1
    # listed as not read again, and not fixed
    q = copy.deepcopy(P)
    q["stats"]["fixed_and_not_yet_re_audited"] = [other]
    assert len(_what_the_fixed_findings_do_not_satisfy(q)) == 1
    # an acceptance taken back; one reworded so that it no longer begins with the word; one moved to the list of the unread
    q = copy.deepcopy(P)
    del q["accepted"]["E3"]
    assert len(_what_the_fixed_findings_do_not_satisfy(q)) == 2          # it is fixed and nowhere, and it was accepted on the day
    q = copy.deepcopy(P)
    q["accepted"]["E3"] = "not " + q["accepted"]["E3"]
    assert len(_what_the_fixed_findings_do_not_satisfy(q)) == 2
    q = copy.deepcopy(P)
    q["stats"]["fixed_and_not_yet_re_audited"] = ["E3"]
    assert len(_what_the_fixed_findings_do_not_satisfy(q)) == 1
    # a finding accepted on the day and no longer marked fixed
    q = copy.deepcopy(P)
    q["findings"]["E3"]["state"] = "REPRODUCED"
    assert len(_what_the_fixed_findings_do_not_satisfy(q)) == 1


def test_what_is_owed_is_said_and_registered():
    f = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("The repo sweep:", "**owed**: 64 of 81 are joined to nothing", "Both halves of the", "Nothing here is a result about the mathematics"):
        assert s in f, s
    reg = (ROOT / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8")
    assert "| P-773 |" in reg
