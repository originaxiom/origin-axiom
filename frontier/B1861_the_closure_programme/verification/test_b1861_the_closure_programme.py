"""B1861 -- the closure programme is what its builder generates, it covers the map, its order does not ignore the map,
and each of its refusals can fire.

The builder reads the closure map as generated (B1858), the register, the scoreboard's data file, the record's own pages
and, where this clone holds them, the work order's and the advisor seat's revisions. In a clone without those revisions
the tests that need them are SKIPPED, visibly; nothing is counted as passed."""
import contextlib
import copy
import importlib.util
import json
import pathlib
import re

import pytest

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
spec = importlib.util.spec_from_file_location("b1861_build_programme", HERE / "build_programme.py")
bp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bp)
S = bp.S
B = bp.build()
SEATS = not B["stats"]["not_checked_in_this_clone"]


def _refusals():
    return bp.build()["fails"]


def _wp(i):
    return next(x for x in S.WP if x["id"] == i)


@contextlib.contextmanager
def planted(apply, undo):
    apply()
    try:
        yield _refusals()
    finally:
        undo()


def test_the_programme_covers_the_map():
    assert B["fails"] == [], B["fails"][:5]
    st = B["stats"]
    assert st["nodes_needing_a_path"] == st["nodes_assigned"] >= 131
    # computed from the map, not typed here: every node that is an input, an open question, a lane's result or a duty
    nodes = json.loads((bp.MAP / "NODES.json").read_text(encoding="utf-8"))
    need = {n["id"] for n in nodes if n["grade"] not in bp.TERMINAL + bp.CONDITIONAL + bp.OTHER}
    assigned = [n for w in S.WP for n in w["nodes"]]
    assert set(assigned) == need and len(assigned) == len(set(assigned))
    debts = {n["rows"][0] for n in nodes if n["grade"] == "DEBT"}
    assert set(B["debt_of"]) == debts
    assert set(st["packages_by_obligation"]) == {"C0", "C1", "C2", "C3", "C4", "C5", "C6"}


def test_the_committed_files_are_the_builders_output():
    assert (ARC / "PROGRAMME.md").read_text(encoding="utf-8") == bp.render(B)
    j = json.loads((ARC / "PROGRAMME.json").read_text(encoding="utf-8"))
    # what a clone could or could not check of other seats' words is not written to the files (B1886): the page is the same in
    # every clone, so the gate can compare it everywhere
    assert j["stats"] == {k: v for k, v in json.loads(json.dumps(B["stats"])).items() if k not in bp.CLONE_DEPENDENT}
    assert not set(bp.CLONE_DEPENDENT) & set(j["stats"]) and "NOT CHECKED" not in (ARC / "PROGRAMME.md").read_text(encoding="utf-8")
    for name, text in bp.generated(B).items():
        assert (ARC / name).read_text(encoding="utf-8") == text, name
    assert [w["id"] for w in j["packages"]] == [w["id"] for w in B["packages"]]


def test_the_order_does_not_ignore_the_map():
    """every dependency edge of the map between two packages is recorded as needs or as given"""
    nodes = json.loads((bp.MAP / "NODES.json").read_text(encoding="utf-8"))
    edges = json.loads((bp.MAP / "EDGES.json").read_text(encoding="utf-8"))
    pk = {n: w["id"] for w in S.WP for n in w["nodes"]}
    wp = {w["id"]: w for w in B["packages"]}
    def before(i, seen=None):
        """the packages that must be worked before package i: the closure of its needs (rule 6 asks for this, or a direct given)"""
        seen = set() if seen is None else seen
        for x in wp[i]["needs_all"]:
            if x in wp and x not in seen:
                seen.add(x)
                before(x, seen)
        return seen
    cross = 0
    for e in edges:
        if e["kind"] in ("requires", "applies-under"):
            a, b = e["src"], e["dst"]
        elif e["kind"] == "blocks":
            a, b = e["dst"], e["src"]
        else:
            continue
        if a in pk and b in pk and pk[a] != pk[b]:
            cross += 1
            # Review 78's reader: this asked only for the transitive "rests on", which is weaker than the rule it names
            assert pk[b] in before(pk[a]) or pk[b] in wp[pk[a]]["given"], (a, b, pk[a], pk[b])
    assert cross >= 20
    # the lanes' results rest on the parent and on the modulus, and the parent has no owner
    for i in ("WP-2.1", "WP-2.3", "WP-3.1", "WP-3.3"):
        assert {"WP-1.8", "WP-4.1"} <= set(wp[i]["rests_on"]), i
    assert wp["WP-1.8"]["owner"] == "unowned" and wp["WP-1.8"]["sits_under"] >= 10
    # the action, the dynamics and the modulus close together
    assert ["WP-2.1", "WP-2.5", "WP-4.1"] in B["stats"]["packages_that_close_together"]
    # planted: drop what WP-2.1 is given, and the builder refuses
    saved = S.GIVEN.pop("WP-2.1")
    try:
        f = _refusals()
    finally:
        S.GIVEN["WP-2.1"] = saved
    assert any("the order ignores the map: WP-2.1 rests on WP-1.8" in x for x in f)


def test_the_input_budget_agrees_with_the_record():
    # every present input of the spine is typed once: a choice, a rule of the comparison, or a tally
    nodes = json.loads((bp.MAP / "NODES.json").read_text(encoding="utf-8"))
    inputs = {n["id"] for n in nodes if n["grade"] in bp.INPUT_GRADES}
    typed = [m for i in S.INPUTS for m in i["members"]] + S.RULES + S.TALLIES
    assert len(typed) == len(set(typed)) and set(typed) == inputs
    # the candidate frame, read from the scoreboard's own data file: 13 borrowed joints, 10 chosen, 2 fitted, 1 ansatz
    sb = json.loads((bp.ROOT / "docs" / "total_inputs_scoreboard.json").read_text(encoding="utf-8"))
    joints = [("S:" + j["id"], j["type"]) for j in sb["shared_block"]] + [("A:" + j["id"], j["type"]) for j in sb["frames"]["A"]["joints"]]
    borrowed = {m: t for m, t in joints if t not in ("FORCED-BY-MAIN", "VERIFIED-BY-MAIN")}
    entry = {m: i for i in S.INPUTS for m in i["members"]}
    assert set(m for m in entry if m.startswith(("A:", "S:"))) == set(borrowed) and len(borrowed) == 13
    assert sorted(m for m, t in borrowed.items() if t == "FITTED") == sorted(m for m in borrowed if "real" in entry[m]["kinds"])
    assert sorted(m for m, t in borrowed.items() if t == "ANSATZ") == sorted(m for m in borrowed if "ansatz" in entry[m]["kinds"])
    # the record grades theta-bar an input: it is a real number in the budget, not a rule of the comparison
    assert "FL:16" in entry and "real" in entry["FL:16"]["kinds"] and "FL:16" not in S.RULES
    # the lanes' supplied inputs are named as outside the budget
    assert sorted(S.LANE_INPUT_NOTE) == sorted(n["id"] for n in nodes if n["grade"] == "LANE-INPUT")
    assert B["stats"]["budget_items"] == sum(sum(i["kinds"].values()) for i in S.INPUTS)


def test_the_premises_are_in_series():
    st, w = B["stats"], B["waits"]
    heads = st["headline_results_that_are_conditional_results"]
    assert sorted(heads) == ["G:ROOT", "MC:Z6", "V:SIX", "W:INDEX3"]
    assert sorted(st["headline_results_not_yet_results_on_main"]) == ["E:L10", "T:IM"]
    # for each conditional headline: more than one open choice, the foundation's axioms and the tallies not counted
    axioms = {m for i in S.INPUTS if set(i["kinds"]) == {"axiom"} for m in i["members"]}
    for h in heads:
        assert len(w[h]["premises"]) >= 2 and not set(w[h]["premises"]) & (axioms | set(S.TALLIES) | set(S.RULES)), h
        assert not any(h in rs for rs in B["released"].values())
    assert w["G:ROOT"]["premises"] == ["G:SE1", "G:SE2"] and set(w["G:ROOT"]["axioms"]) == {"G:GM3", "G:GM4"}
    assert "MC:PRICE" in w["MC:Z6"]["not_counted"]


def test_the_audit_is_carried_finding_by_finding():
    st = B["stats"]
    assert st["audit_findings"] == 73 and sum(st["audit_findings_by_state"].values()) == 73
    for fid, f in S.FINDINGS.items():
        assert f["state"] in S.FINDING_STATES and f["wp"] in {w["id"] for w in S.WP}
        if f["state"] != "OPEN":
            assert f["note"], fid
    assert S.FINDINGS["G1"]["wp"] == S.FINDINGS["G2"]["wp"] == "WP-0.7"
    assert st["relayed_rulings"] == len(S.RULINGS) == 17
    # the owner's confirmation to main (2026-11-10) covers the eleven main asked about; the two relayed afterwards are asked
    # eleven by the owner's answer of 2026-11-10; the four asked later (P-771) each by the owner's own answer of 2026-11-11; none is left asked
    assert len(S.CONFIRMED) == 11 and len(S.CONFIRMED_LATER) == 4 and st["rulings_confirmed_by_the_owner_to_main"] == 15
    assert st["rulings_not_confirmed"] == len(S.NOT_CONFIRMED) == 2 and st["rulings_asked"] == 0
    # the ground is the act; 'close' means the whole agrees (P-774); and how the tick's ruling stands with 'even ticks observed': after the computation
    assert st["rulings_given_to_main_directly"] == len(S.DIRECT_RULINGS) == 4 and S.DIRECT_RULINGS[2][2] == "After the computation"
    assert S.DIRECT_RULINGS[3][2] == "A condition to derive (Recommended)" and S.EXITS["the orientation"][0] == "BACK-EDGE NAMED"      # ruled with B1879 in hand
    assert not set(S.NOT_CONFIRMED) & set(S.CONFIRMED) and all(S.NOT_CONFIRMED.values())
    assert [n for n, q, ps in S.RULINGS][:11] == S.CONFIRMED and sorted(S.OPINION) == sorted(list(S.CONFIRMED) + list(S.CONFIRMED_LATER))
    assert sorted(S.CONFIRMED_LATER) == sorted(n for n, q, ps in S.RULINGS[13:])           # the four relayed last, each answered by the owner on 2026-11-11
    keep = list(S.CONFIRMED)
    def restore():
        S.CONFIRMED[:] = keep
    with planted(lambda: S.CONFIRMED.append("stress-test the principle"), restore) as f:
        assert any("none is written for: stress-test the principle" in x for x in f)
        assert any("marked both confirmed and not confirmed: stress-test the principle" in x for x in f)
    with planted(lambda: S.CONFIRMED.append("a ruling nobody relayed"), restore) as f:
        assert any("is not among the relayed rulings: a ruling nobody relayed" in x for x in f)
    with planted(lambda: S.CONFIRMED.remove("the goal"), restore) as f:
        assert any("an opinion is written for a ruling that is not confirmed: the goal" in x for x in f)
    if not SEATS:
        pytest.skip("this clone does not hold the advisor seat's revision: its finding ids and quotes are not checked")
    assert st["audit_findings_checked_at_the_seats_revision"] == 73 and st["work_order_quotes_checked"] == len(S.WORK_ORDER_QUOTES)


def test_the_refusals_about_the_map_can_fire():
    """MB12: each refusal is planted once and must be reported; the source is restored whatever happens."""
    w16, w41, w21 = _wp("WP-1.6"), _wp("WP-4.1"), _wp("WP-2.1")
    with planted(lambda: w16["nodes"].remove("W:CLOCK"), lambda: w16["nodes"].append("W:CLOCK")) as f:
        assert any("a map node has no package: W:CLOCK" in x for x in f)
    with planted(lambda: w41["nodes"].append("W:CLOCK"), lambda: w41["nodes"].remove("W:CLOCK")) as f:
        assert any("a node is in two packages: W:CLOCK" in x for x in f)
    with planted(lambda: w16["nodes"].append("W:Q8"), lambda: w16["nodes"].remove("W:Q8")) as f:
        assert any("needs no closure path: W:Q8" in x for x in f)
    with planted(lambda: w16["nodes"].append("NO:SUCH"), lambda: w16["nodes"].remove("NO:SUCH")) as f:
        assert any("names a node that is not in the map: NO:SUCH" in x for x in f)
    with planted(lambda: w21["needs"].append("WP-3.1"), lambda: w21["needs"].remove("WP-3.1")) as f:
        assert any("hold a cycle" in x for x in f)
    with planted(lambda: w21["needs"].append("WP-9.9"), lambda: w21["needs"].remove("WP-9.9")) as f:
        assert any("WP-2.1 needs an unknown package: WP-9.9" in x for x in f)
    with planted(lambda: S.ALSO.__setitem__("W:CLOCK", ["WP-1.6"]), lambda: S.ALSO.pop("W:CLOCK")) as f:
        assert any("ALSO repeats W:CLOCK's own package" in x for x in f)
    with planted(lambda: w16["rows"].append("P-99999"), lambda: w16["rows"].remove("P-99999")) as f:
        assert any("cites a row that is not in the register: P-99999" in x for x in f)
    saved = S.DEBT_TO_WP.pop("P-757")
    try:
        f = _refusals()
    finally:
        S.DEBT_TO_WP["P-757"] = saved
    assert any("a ranked debt has no package: P-757" in x for x in f)
    assert _refusals() == []


def test_the_refusals_about_the_packages_and_the_budget_can_fire():
    w11, w16 = _wp("WP-1.1"), _wp("WP-1.6")
    # a package marked done that holds an open question
    old = w16["status"]
    with planted(lambda: w16.__setitem__("status", "DONE (by wording)"), lambda: w16.__setitem__("status", old)) as f:
        assert any("WP-1.6 is marked DONE and is not a declaration" in x for x in f)
    old_i = w16["intent"]
    with planted(lambda: w16.__setitem__("intent", "ASSERT"), lambda: w16.__setitem__("intent", old_i)) as f:
        assert any("WP-1.6: intent 'ASSERT'" in x for x in f)
    old_q = w11["question"]
    with planted(lambda: w11.__setitem__("question", "The principle is declared."), lambda: w11.__setitem__("question", old_q)) as f:
        assert any("WP-1.1: its question is not a question" in x for x in f)
    # the budget: typed twice; not typed; a fitted number called discrete; an axiom the record does not grade so
    with planted(lambda: S.INPUTS[0]["members"].append("G:PF2"), lambda: S.INPUTS[0]["members"].remove("G:PF2")) as f:
        assert any("types a node twice: G:PF2" in x for x in f)
    tau = next(i for i in S.INPUTS if "A:A01" in i["members"])
    with planted(lambda: tau["members"].remove("FL:04"), lambda: tau["members"].append("FL:04")) as f:
        assert any("a present input is not in the budget: FL:04" in x for x in f)
    kinds = dict(tau["kinds"])
    with planted(lambda: tau.__setitem__("kinds", {"discrete": 2}), lambda: tau.__setitem__("kinds", kinds)) as f:
        assert any("a FITTED node is not typed as a real number: A:A01" in x for x in f)
        assert any("disagrees with the scoreboard's type FITTED" in x for x in f)
    clock = next(i for i in S.INPUTS if i["members"] == ["W:CLOCK"])
    ck = dict(clock["kinds"])
    with planted(lambda: clock.__setitem__("kinds", {"axiom": 1}), lambda: clock.__setitem__("kinds", ck)) as f:
        assert any("the budget calls W:CLOCK an axiom; the record grades it CHOSEN" in x for x in f)
    note = S.LANE_INPUT_NOTE.pop("E:L02")
    try:
        f = _refusals()
    finally:
        S.LANE_INPUT_NOTE["E:L02"] = note
    assert any("the lanes' supplied inputs are not the ones listed" in x for x in f)
    with planted(lambda: S.MAIN_QUOTES.append(("GENESIS.md", "this sentence is not in the foundation document")), lambda: S.MAIN_QUOTES.pop()) as f:
        assert any("GENESIS.md does not say" in x for x in f)
    with planted(lambda: S.TOE_LEDGER.append(("A ninth row", ["WP-1.1"])), lambda: S.TOE_LEDGER.pop()) as f:
        assert any("the record's checklist has no row 9 'A ninth row'" in x for x in f)
    assert _refusals() == []


def test_the_refusals_about_the_audit_can_fire():
    orig = dict(S.FINDINGS["G2"])                                  # never mutated: each plant works on a fresh copy
    restore = lambda: S.FINDINGS.__setitem__("G2", dict(orig))
    with planted(lambda: S.FINDINGS.__setitem__("G2", dict(orig, state="FIXED", note="")), restore) as f:
        assert any("G2 is marked FIXED with no note" in x for x in f)
    with planted(lambda: S.FINDINGS.__setitem__("G2", dict(orig, state="CLOSED")), restore) as f:
        assert any("G2 has a state outside the list" in x for x in f)
    assert S.FINDINGS["G2"] == orig
    with planted(lambda: S.RULINGS.append(("an eighth", "a sentence the seat did not write", [])), lambda: S.RULINGS.pop()) as f:
        assert any("the relayed ruling 'an eighth' has no package" in x for x in f)
    if not SEATS:
        pytest.skip("this clone does not hold the seats' revisions: the planted checks that read them are not run")
    saved = S.FINDINGS.pop("G1")
    S.FINDINGS["G99"] = dict(saved)
    try:
        f = _refusals()
    finally:
        S.FINDINGS.pop("G99")
        S.FINDINGS["G1"] = saved
    assert any("a finding of the audit has no package: G1" in x for x in f)
    assert any("names a finding the audit does not hold: G99" in x for x in f)
    with planted(lambda: S.RULINGS.append(("an eighth", "a sentence the seat did not write", ["WP-0.7"])), lambda: S.RULINGS.pop()) as f:
        assert any("the relayed ruling 'an eighth' is not in the seat's file as quoted" in x for x in f)
    with planted(lambda: S.WORK_ORDER_QUOTES.__setitem__("C9", "An obligation the work order does not have"), lambda: S.WORK_ORDER_QUOTES.pop("C9")) as f:
        assert any("the work order does not say" in x for x in f)
    assert _refusals() == []


def test_the_foundations_count_is_corrected():
    g = (ARC.parents[1] / "GENESIS.md").read_text(encoding="utf-8")
    assert "when all seven hold" in g and "- **v1.64 · 2026-11-10 · main B1861.**" in g and "7. *Worth spending.*" in g       # the correction's own log entry; the page has moved on


def test_every_input_says_how_it_could_leave_and_the_refusal_can_fire():
    """rule 15 (added with B1867): one line per input, of a listed kind; the tallies are the builder's, not typed"""
    st = B["stats"]
    names = [i["name"] for i in S.INPUTS]
    assert sorted(S.EXITS) == sorted(names) and sum(st["exits_by_kind"].values()) == len(names)
    assert st["inputs_with_an_exit_on_the_table"] == sum(1 for n in names if S.EXITS[n][0] in ("FORCING ARGUED", "RIGID", "BACK-EDGE NAMED"))
    # nothing is typed as leaving: no kind says derived, proved or closed
    assert not any(w in " ".join(S.EXIT_KINDS).upper() for w in ("DERIVED", "PROVED", "CLOSED"))
    # every identification is a dictionary entry or is pressed; every kept entry is one of the principle's three faces
    for i in S.INPUTS:
        k = S.EXITS[i["name"]][0]
        if set(i["kinds"]) == {"identification"}:
            assert k in ("DICTIONARY", "PRESSED"), i["name"]
        if k == "KEPT":
            assert i["members"][0].startswith("G:PF"), i["name"]
    page = (ARC / "PROGRAMME.md").read_text(encoding="utf-8")
    assert "### How each input could leave the budget" in page
    assert "**An exit is on the table for %d of the %d inputs**" % (st["inputs_with_an_exit_on_the_table"], len(names)) in page
    keep = dict(S.EXITS)
    def restore():
        S.EXITS.clear()
        S.EXITS.update(keep)
    with planted(lambda: S.EXITS.pop("the clock"), restore) as f:
        assert any("has no line saying how it could leave: the clock" in x for x in f)
    with planted(lambda: S.EXITS.__setitem__("the clock", ("DERIVED", "x")), restore) as f:
        assert any("exit of an unknown kind: DERIVED" in x for x in f)
    with planted(lambda: S.EXITS.__setitem__("the clock", ("BACK-EDGE NAMED", "")), restore) as f:
        assert any("names a route and does not say what it is" in x for x in f)
    with planted(lambda: S.EXITS.__setitem__("the clock", ("DICTIONARY", "")), restore) as f:
        assert any("typed a dictionary entry and is not an identification" in x for x in f)
    with planted(lambda: S.EXITS.__setitem__("the modulus τ", ("KEPT", "x")), restore) as f:
        assert any("typed kept and is not an axiom" in x for x in f)
    with planted(lambda: S.EXITS.__setitem__("a number nobody typed", ("UNTOUCHED", "")), restore) as f:
        assert any("not an input of the budget: a number nobody typed" in x for x in f)
    assert not _refusals()


def test_the_joins_the_seals_rule_needs_and_each_refusal_can_fire():
    """rules 16 to 19 (added with B1873, the advisor seat's read of this page as a non-author)"""
    st = B["stats"]
    assert sorted(S.BEARS_ON) == sorted(S.FINDINGS) and all(S.BEARS_ON[f] for f in S.FINDINGS)
    assert st["findings_that_bear_on_the_repository_as_a_whole"] + st["findings_that_name_arcs_nodes_or_pages_only"] == 73
    card = _wp("WP-5.3")
    built = {w["id"]: w for w in B["packages"]}
    def upstream(i, seen=None):
        seen = set() if seen is None else seen
        for x in built[i]["needs_all"]:
            if x not in seen:
                seen.add(x)
                upstream(x, seen)
        return seen
    up = upstream("WP-5.3")
    for w in st["packages_the_sealed_card_must_wait_on_for_that"]:
        assert w in up, w
    # the comparison now waits on the suite and on the comparison's own instruments
    assert {"WP-0.2", "WP-0.5"} <= set(card["needs"])
    # 16: a finding that names nothing, and one that names something that is not there
    keep = dict(S.BEARS_ON)
    def restore():
        S.BEARS_ON.clear()
        S.BEARS_ON.update(keep)
    with planted(lambda: S.BEARS_ON.pop("E7"), restore) as f:
        assert any("finding E7 names nothing it bears on" in x for x in f)
    with planted(lambda: S.BEARS_ON.__setitem__("E7", ["B99999"]), restore) as f:
        assert any("finding E7 bears on something that is not there: B99999" in x for x in f)
    # 17: the sealed card set free of the suite, and of a package that holds debts the map joins to nothing
    needs = list(card["needs"])
    def restore_needs():
        card["needs"][:] = needs
    with planted(lambda: card["needs"].remove("WP-0.5"), restore_needs) as f:
        assert any("the sealed card does not wait on WP-0.5" in x for x in f)
    with planted(lambda: card["needs"].remove("WP-0.4"), restore_needs) as f:
        assert any("the sealed card does not wait on WP-0.4" in x for x in f)
    # 18: a package marked started under a need that has not started
    w42, w43 = _wp("WP-4.2"), _wp("WP-4.3")
    assert w42["status"].startswith("NOT STARTED") and w43["status"].startswith("STARTED")
    n43 = list(w43["needs"])
    def restore43():
        w43["needs"][:] = n43
    with planted(lambda: w43["needs"].append("WP-4.2"), restore43) as f:
        assert any("WP-4.3 is marked STARTED while WP-4.2" in x for x in f)
    # 19: fixed is main's word; the re-audit's verdict is kept apart, and a finding it did not accept cannot be marked fixed
    # fixed by main and not read by that seat: listed, never shown as accepted.  B1878's two (G9, X1) stood here until the seat's
    # fourth re-audit read them; with it every finding main marks fixed has the seat's verdict (B1880)
    assert st["findings_with_a_re_audit_verdict"] == len(S.ACCEPTED) and st["fixed_and_not_yet_re_audited"] == []
    # E3 was PARTLY FIXED until the fourth re-audit accepted it; E4's verdict is still "partly", and marking it fixed is refused
    assert S.FINDINGS["E3"]["state"] == "FIXED" and "PARTLY FIXED" in [t[0] for t in S.FINDINGS["E3"]["trail"]] and S.ACCEPTED["E3"].startswith("accepted")
    assert S.FINDINGS["E4"]["state"] == "PARTLY FIXED" and S.ACCEPTED["E4"].startswith("partly")
    e4 = dict(S.FINDINGS["E4"])
    def restore_e4():
        S.FINDINGS["E4"].clear()
        S.FINDINGS["E4"].update(e4)
    with planted(lambda: S.FINDINGS["E4"].__setitem__("state", "FIXED"), restore_e4) as f:
        assert any("finding E4 is marked FIXED and the re-audit" in x for x in f)
    # 20: what main changed after the re-audit is shown as not re-read; an entry for a finding with no verdict, or an arc not on main, is refused
    assert st["findings_main_changed_since_the_re_audit"] == sorted(S.SINCE_REAUDIT) and set(S.SINCE_REAUDIT) <= set(S.ACCEPTED)
    page = (ARC / "PROGRAMME.md").read_text(encoding="utf-8")
    for fid, (arc_, _) in S.SINCE_REAUDIT.items():
        row = next(l for l in page.splitlines() if l.startswith("| %s |" % fid))
        assert "the seat has not read the change" in row and arc_ in row, fid
    keep_since = dict(S.SINCE_REAUDIT)
    def restore_since():
        S.SINCE_REAUDIT.clear()
        S.SINCE_REAUDIT.update(keep_since)
    with planted(lambda: S.SINCE_REAUDIT.__setitem__("W1", ("B1874", "x")), restore_since) as f:
        assert any("a change since the re-audit is recorded for W1, on which the re-audit gave no verdict" in x for x in f)
    with planted(lambda: S.SINCE_REAUDIT.__setitem__("G2", ("B99999", "x")), restore_since) as f:
        assert any("names an arc that is not on main: B99999" in x for x in f)
    # the exits: three forcing arguments are one clause short and are not counted as exits
    assert st["exits_by_kind"]["ONE CLAUSE SHORT"] == 3 and st["inputs_with_an_exit_on_the_table"] == 9      # 8 until the owner named the orientation's condition (2026-11-11)
    assert st["budget"]["bit"] == 9 and st["budget_items"] == 47          # the charge premise is two choices under one name (B1869); 46 until the ground was entered as an axiom (GENESIS v1.65, B1886)
    assert st["budget"]["axiom"] == 9 and st["independent_choices"] == 39
    assert not _refusals()


# Review 78 (2026-11-11): its reader listed the refusals of the builder that no planted control could make fire.  Each gets one
# here, and a last test reads the builder's source and fails if a refusal is added without a control that names it.
def test_the_refusals_review_78s_reader_found_unplanted_can_fire():
    import copy
    keep = copy.deepcopy((S.WP, S.ALSO, S.GIVEN, S.INPUTS, S.CONFIRMATION, S.CONFIRMED, S.NOT_CONFIRMED, S.HEADLINES))
    def restore():
        S.WP[:] = copy.deepcopy(keep[0])
        S.ALSO.clear(); S.ALSO.update(copy.deepcopy(keep[1]))
        S.GIVEN.clear(); S.GIVEN.update(copy.deepcopy(keep[2]))
        S.INPUTS[:] = copy.deepcopy(keep[3])
        S.CONFIRMATION = keep[4]
        S.CONFIRMED[:] = list(keep[5])
        S.NOT_CONFIRMED.clear(); S.NOT_CONFIRMED.update(copy.deepcopy(keep[6]))
        S.HEADLINES[:] = list(keep[7])
    w = lambda: _wp("WP-1.2")
    a_node = next(iter(S.ALSO))
    with_A = lambda: next(i for i in S.INPUTS if any(m.startswith("A:") for m in i["members"]))
    ansatz = lambda: next(i for i in S.INPUTS if "ansatz" in i["kinds"])
    confirmed0, relayed_unconfirmed = S.CONFIRMED[0], next(n for n, _, _ in S.RULINGS if n not in S.CONFIRMED and n not in S.NOT_CONFIRMED)
    groups = [
        # rule 10: a package is whole; rule 5: the order of work
        [(lambda: w().__setitem__("owner", " "), "WP-1.2 has no owner"),
         (lambda: w().__setitem__("first", ""), "WP-1.2 has no first"),
         (lambda: w().__setitem__("accept", ""), "WP-1.2 has no accept"),
         (lambda: w().__setitem__("status", "PERHAPS"), "WP-1.2: status 'PERHAPS'"),
         (lambda: w().__setitem__("obligation", "C9"), "WP-1.2: obligation 'C9'"),
         (lambda: w()["needs"].append("@Z9"), "WP-1.2 needs an unknown obligation: @Z9"),
         (lambda: w()["needs"].append("WP-9.9"), "WP-1.2 needs an unknown package: WP-9.9")],
        # rule 10 again, and rule 2: a second package for a node; rule 5: GIVEN
        [(lambda: S.WP.append(dict(S.WP[0])), "a package id repeats"),
         (lambda: S.ALSO.__setitem__("ZZ:NOPE", ["WP-1.2"]), "ALSO names a node that is in no package: ZZ:NOPE"),
         (lambda: S.ALSO[a_node].append("WP-9.9"), "ALSO sends %s to an unknown package: WP-9.9" % a_node),
         (lambda: S.GIVEN.__setitem__("WP-9.9", ["WP-1.2"]), "GIVEN names an unknown package: WP-9.9"),
         (lambda: S.GIVEN.setdefault("WP-1.2", []).append("WP-9.8"), "GIVEN names an unknown package under WP-1.2: WP-9.8")],
        # rule 8: the budget's kinds; rule 9: the candidate frame's joints against the scoreboard
        [(lambda: S.INPUTS[0]["kinds"].__setitem__("guess", 1), "has an unknown kind: guess"),
         (lambda: ansatz().__setitem__("kinds", {"discrete": 1}), "an ANSATZ node is not typed as an ansatz"),
         (lambda: S.INPUTS[1]["members"].append(S.INPUTS[0]["members"][0]), "the budget types a node twice: %s" % S.INPUTS[0]["members"][0]),
         (lambda: S.INPUTS[0]["members"].append("ZZ:NOPE"), "the budget names a node that is not in the map: ZZ:NOPE"),
         (lambda: with_A()["members"].remove(next(m for m in with_A()["members"] if m.startswith("A:"))), "are not the scoreboard's borrowed joints")],
        # rule 13: the owner's confirmations; rule 14: the headline results are nodes of the map
        # CHANGED 2026-11-12 (Review 80; the SM seat's finding 28).  The refusal read "rulings are marked confirmed with no date or
        # no words of the owner".  The builder no longer asks for his words: it asks for main's account of what he answered.
        [(lambda: setattr(S, "CONFIRMATION", ("", "")), "rulings are marked confirmed with no date, or with nothing in plain words on what the owner answered"),
         (lambda: S.CONFIRMED.append("a ruling nobody relayed"), "a ruling is marked confirmed and is not among the relayed rulings: a ruling nobody relayed"),
         (lambda: S.NOT_CONFIRMED.__setitem__("another nobody relayed", "words"), "a ruling is marked not confirmed and is not among the relayed rulings: another nobody relayed"),
         (lambda: S.NOT_CONFIRMED.__setitem__(confirmed0, "words"), "a ruling is marked both confirmed and not confirmed: %s" % confirmed0),
         (lambda: S.NOT_CONFIRMED.__setitem__(relayed_unconfirmed, ""), "a ruling is marked not confirmed without the owner's words: %s" % relayed_unconfirmed),
         (lambda: S.HEADLINES.append("ZZ:NOPE"), "a headline result is not in the map: ZZ:NOPE")],
    ]
    assert not _refusals()
    for group in groups:                                     # the plants of a group touch different things, so one build shows them all
        def apply_all(group=group):
            for apply, _ in group:
                apply()
        with planted(apply_all, restore) as f:
            for _, want in group:
                assert any(want in x for x in f), (want, f[:4])
    assert not _refusals()
    # rule 13, the later confirmations and the rulings given to main directly
    keep_later, keep_direct = dict(S.CONFIRMED_LATER), list(S.DIRECT_RULINGS)
    def restore_later():
        S.CONFIRMED_LATER.clear(); S.CONFIRMED_LATER.update(keep_later)
        S.DIRECT_RULINGS[:] = keep_direct
    def later():
        S.CONFIRMED_LATER["the tick is an act"] = ("2026-11-11", "Is the tick an act?", "")
        S.CONFIRMED_LATER[S.CONFIRMED[0]] = ("2026-11-11", "q", "a")
        S.DIRECT_RULINGS.append(("a ruling with no answer", "q", "", "2026-11-11", ["WP-1.6"], "m"))
        S.DIRECT_RULINGS.append(("a ruling with no package", "q", "a", "2026-11-11", ["WP-9.9"], "m"))
        S.DIRECT_RULINGS.append((S.RULINGS[0][0], "q", "a", "2026-11-11", ["WP-1.6"], "m"))
    with planted(later, restore_later) as f:
        for want in ("a later confirmation has no date, question or answer of the owner: the tick is an act", "a ruling is confirmed twice: %s" % S.CONFIRMED[0],
                     "a ruling given to main directly has no date, question, answer or meaning: a ruling with no answer",
                     "a ruling given to main directly has no package: a ruling with no package",
                     "a ruling given to main directly bears a relayed ruling's name: %s" % S.RULINGS[0][0]):
            assert any(want in x for x in f), (want, f[:4])
    # the six that the recorded run of every planting test still found silent (Review 78): rules 8, 12, 13, 14, 19, 20
    nodes0 = json.loads((bp.MAP / "NODES.json").read_text(encoding="utf-8"))
    not_an_input = next(n["id"] for n in nodes0 if n["grade"] not in bp.INPUT_GRADES and n["id"] not in {m for i in S.INPUTS for m in i["members"]})
    keep6 = copy.deepcopy((S.FINDINGS, S.ADVISOR_QUOTES, S.TOE_LEDGER, S.ACCEPTED, S.SINCE_REAUDIT))
    def restore6():
        restore()
        S.FINDINGS.clear(); S.FINDINGS.update(copy.deepcopy(keep6[0]))
        S.ADVISOR_QUOTES[:] = list(keep6[1])
        S.TOE_LEDGER[:] = list(keep6[2])
        S.ACCEPTED.clear(); S.ACCEPTED.update(keep6[3])
        S.SINCE_REAUDIT.clear(); S.SINCE_REAUDIT.update(keep6[4])
    fixed_and_accepted = next(fid for fid, f in S.FINDINGS.items() if f["state"] == "FIXED" and fid in S.ACCEPTED)
    def six():
        S.INPUTS[0]["members"].append(not_an_input)
        S.FINDINGS["E7"]["wp"] = "WP-9.9"
        S.ADVISOR_QUOTES.append((S.ADVISOR_QUOTES[0][0], "a sentence that seat never wrote"))
        S.TOE_LEDGER[0] = (S.TOE_LEDGER[0][0], [])
        S.ACCEPTED[fixed_and_accepted] = "refused"
        S.SINCE_REAUDIT["G2"] = ("B1874", "")
    with planted(six, restore6) as f:
        wants = ["the budget names a node that is not a present input: %s" % not_an_input, "finding E7 is assigned to an unknown package: WP-9.9",
                 "the checklist row %r has no package" % S.TOE_LEDGER[0][0], "finding %s is marked FIXED and the re-audit did not accept it: refused" % fixed_and_accepted,
                 "a change since the re-audit says nothing of what changed: G2"]
        if SEATS:
            wants.append("does not say: 'a sentence that seat never wrote'")
        for want in wants:
            assert any(want in x for x in f), (want, f[:6])
    assert not _refusals()
    # rule 5: two packages that need each other
    def cycle():
        _wp("WP-1.2")["needs"].append("WP-1.3")
        _wp("WP-1.3")["needs"].append("WP-1.2")
    with planted(cycle, restore) as f:
        assert any("the packages' needs hold a cycle" in x for x in f), f[:4]
    # rule 11: a quote of the work order with a digit in it (read only where this clone holds the work order's revision)
    if SEATS:
        keep_q = dict(S.WORK_ORDER_QUOTES)
        def restore_q():
            S.WORK_ORDER_QUOTES.clear()
            S.WORK_ORDER_QUOTES.update(keep_q)
        with planted(lambda: S.WORK_ORDER_QUOTES.__setitem__("planted", "milestone 3 of the plan"), restore_q) as f:
            assert any("a work-order quote carries a digit: planted" in x for x in f), f[:4]
    # rule 4, on the map itself: a conditional result with every edge to a premise removed
    nodes = json.loads((bp.MAP / "NODES.json").read_text(encoding="utf-8"))
    edges = json.loads((bp.MAP / "EDGES.json").read_text(encoding="utf-8"))
    cond = next(n["id"] for n in nodes if n["grade"] in bp.CONDITIONAL and any(e["src"] == n["id"] and e["kind"] in ("requires", "applies-under") for e in edges))
    cut = [e for e in edges if not (e["src"] == cond and e["kind"] in ("requires", "applies-under"))]
    assert any("a conditional result names no premise: %s" % cond in x for x in bp.build(nodes=nodes, edges=cut)["fails"])


def _refusal_patterns():
    """every refusal in the builder's source, as a regular expression that its message matches in full"""
    import re
    src = (HERE / "build_programme.py").read_text(encoding="utf-8")
    templates = re.findall(r'fails\.append\(\s*"((?:[^"\\]|\\.)*)"', src)
    assert len(templates) >= 70
    out = []
    for tpl in templates:
        parts = re.split(r"%[sdr]", tpl.replace("%%", "%"))
        out.append((tpl, re.compile(".*?".join(re.escape(p) for p in parts), re.S)))
    return out


def fired_by(test_functions, monkeypatch):
    """run the given planting tests with the builder recorded, and return every refusal message it issued"""
    fired = []
    real = bp.build
    def recording(*a, **k):
        out = real(*a, **k)
        fired.extend(out["fails"])
        return out
    monkeypatch.setattr(bp, "build", recording)
    for fn in test_functions:
        fn()
    monkeypatch.setattr(bp, "build", real)
    return fired


def test_the_refusals_about_the_seats_verdicts_can_fire():
    """B1880, rule 21 (the advisor seat's third re-audit, its case j4): a finding the re-audit did not accept, marked FIXED with the
    re-audit's verdict RETYPED as "accepted" in main's own file, built.  A verdict is now read in the seat's own file."""
    st = B["stats"]
    assert st["verdict_rows_read_in_the_seats_files"] == (sum(len(v) for v in S.VERDICT_ROWS.values()) if SEATS else 0)
    assert set(S.VERDICT_ROWS) == set(S.ACCEPTED)
    # 2026-11-11: this line pinned the number of re-audits at four, and the seat's sixth made it five.  What it holds now is the
    # rule: every re-audit a verdict row names is registered with its two commits, and none is registered that no row names.
    assert {f for rows in S.VERDICT_ROWS.values() for f, _ in rows} == set(S.REAUDITS) and len(S.REAUDITS) >= 4
    keep = copy.deepcopy((S.FINDINGS, S.ACCEPTED, S.VERDICT_ROWS, S.SINCE_REAUDIT))
    def restore():
        S.FINDINGS.clear(); S.FINDINGS.update(copy.deepcopy(keep[0]))
        S.ACCEPTED.clear(); S.ACCEPTED.update(keep[1])
        S.VERDICT_ROWS.clear(); S.VERDICT_ROWS.update(copy.deepcopy(keep[2]))
        S.SINCE_REAUDIT.clear(); S.SINCE_REAUDIT.update(keep[3])
    # j4 itself: E4's verdict is "partly"; mark it FIXED and retype the verdict
    def j4():
        S.FINDINGS["E4"]["state"] = "FIXED"
        S.ACCEPTED["E4"] = "accepted"
    with planted(j4, restore) as f:
        assert any("the programme's verdict on E4 does not begin with the seat's own words in its row ('partly')" in x for x in f), f[:4]
    # ... and with the seat's row retyped to match: the row is not in the seat's file
    def j4_row():
        j4()
        S.VERDICT_ROWS["E4"] = [("REAUDIT_2_2026-11-10.md", "| **E4** B952's lemma | **accepted** |")]
    with planted(j4_row, restore) as f:
        if SEATS:
            assert any("the seat's REAUDIT_2_2026-11-10.md does not hold the row quoted for E4" in x for x in f), f[:4]
    # ... and with another finding's row borrowed: the row does not name the finding
    def j4_borrowed():
        j4()
        S.VERDICT_ROWS["E4"] = [S.VERDICT_ROWS["E6"][0]]
    with planted(j4_borrowed, restore) as f:
        assert any("the row that carries the verdict in force on E4 does not name that finding" in x for x in f), f[:4]
    def others():
        S.ACCEPTED["E12"] = "accepted"                                  # a verdict with no row (E12: until 2026-11-11 this plant used E7, which has had a row since the seat's seventh re-audit)
        S.VERDICT_ROWS["E6"] = [("REAUDIT_9_2099-01-01.md", S.VERDICT_ROWS["E6"][0][1])]
        S.VERDICT_ROWS["E9"] = [("REAUDIT_2_2026-11-10.md", "| **E9** a row |")]      # a row for a finding with no verdict
    with planted(others, restore) as f:
        for want in ("the re-audit's verdict on E12 has no row of the seat's file behind it",
                     "a verdict row for E6 names a re-audit the programme does not hold: REAUDIT_9_2099-01-01.md",
                     "a row of a re-audit is quoted for E9, which has no verdict here"):
            assert any(want in x for x in f), (want, f[:4])
    # a verdict that begins with the seat's "accepted" and goes on to say the correction was not carried: still not fixed
    with planted(lambda: S.ACCEPTED.__setitem__("E6", "accepted in the arc; not carried to two places that state the old form"), restore) as f:
        assert any("finding E6 is marked FIXED and the re-audit says the correction was not carried everywhere" in x for x in f), f[:4]
    assert not _refusals()
    # the page says which re-audit read which commit of main, and the three widened entries of "bears on" are there
    page = (ARC / "PROGRAMME.md").read_text(encoding="utf-8")
    assert "re-audit 2 read main at `ab97082c0`; re-audit 3 read main at `b28dceea8`; re-audit 4 read main at `015be0cc7`; re-audit 5 read main at `16b82acda`" in page
    assert "B734" in S.BEARS_ON["E2"] and "B1850" in S.BEARS_ON["L6"] and "B1841" in S.BEARS_ON["V4"]


def test_the_last_step_rests_on_every_package_and_the_refusals_can_fire():
    """2026-11-11, the advisor seat's row ORD-a (its relay on the scoreboard page; P-782).  Until this date nothing waited on
    WP-0.8, the audit's thirteen errors in the mathematics or its code, or on WP-0.10: by the order as it stood the card could
    be sealed with nine of the thirteen not marked fixed.  The order now ends in one package, and that package rests on every
    other one.  What could fail: the old order, planted again, building."""
    wp = {w["id"]: w for w in B["packages"]}
    last = [i for i in wp if not any(i in x["needs_all"] for x in wp.values())]
    assert last == ["WP-6.1"] and set(wp["WP-6.1"]["rests_on"]) == set(wp) - {"WP-6.1"} and len(wp) == 43
    assert "WP-0.8" in _wp("WP-5.2")["needs"] and "WP-0.10" in _wp("WP-5.3")["needs"]
    assert wp["WP-0.8"]["blocks"] == ["WP-5.2"] and wp["WP-0.10"]["blocks"] == ["WP-5.3"]
    # the old order, planted: the upstream audit no longer needs the errors in the mathematics, then the card the governing document;
    # and an order with two ends of another kind: the comparison no longer needs the independent challenge
    for holder, dropped in (("WP-5.2", "WP-0.8"), ("WP-5.3", "WP-0.10"), ("WP-6.1", "WP-5.4")):
        w = _wp(holder); old = list(w["needs"])
        with planted(lambda: w["needs"].remove(dropped), lambda: w.__setitem__("needs", old)) as f:
            assert any(x.startswith("the work order has 2 packages that nothing needs (%s, WP-6.1); it must have one" % dropped) for x in f), f
    # the advisor seat's cases o2 and o3 (its run of ORD-a at 818d17f46): the errors in the mathematics moved from the upstream
    # audit to a step AFTER the card.  The order still has one end; the card would no longer rest on them.
    c0 = sorted(i for i, w in wp.items() if w["obligation"] == "C0")
    assert len(c0) == 12 and set(c0) <= set(wp["WP-5.3"]["rests_on"])
    for later in ("WP-6.1", "WP-5.4"):
        a, b = _wp("WP-5.2"), _wp(later); olda, oldb = list(a["needs"]), list(b["needs"])
        def move():
            a["needs"].remove("WP-0.8"); b["needs"].append("WP-0.8")
        def back():
            a["needs"] = olda; b["needs"] = oldb
        with planted(move, back) as f:
            assert any(x == "the sealed card does not rest on WP-0.8, of the clean record: it could be sealed with it open" for x in f), f
            assert not any(x.startswith("the work order has 2 packages") for x in f)
    assert not _refusals()
    # who builds and who verifies (P-785): the five packages name the seat that builds and say that main verifies and lands
    for i in ("WP-0.7", "WP-0.9", "WP-0.11", "WP-0.12", "WP-5.1"):
        o = _wp(i)["owner"]
        assert "cld-advisor) builds" in o and ("main verifies" in o or "verifies and lands" in o) and "lands" in o, i
    for i in ("WP-0.8", "WP-0.2", "WP-0.4", "WP-0.5"):
        assert "cld-advisor" not in _wp(i)["owner"], i


PLANTING_TESTS = ("test_the_last_step_rests_on_every_package_and_the_refusals_can_fire", "test_the_refusals_about_the_seats_verdicts_can_fire", "test_the_refusals_about_the_map_can_fire", "test_the_refusals_about_the_packages_and_the_budget_can_fire",
                  "test_the_refusals_about_the_audit_can_fire", "test_the_order_does_not_ignore_the_map", "test_the_audit_is_carried_finding_by_finding",
                  "test_every_input_says_how_it_could_leave_and_the_refusal_can_fire", "test_the_joins_the_seals_rule_needs_and_each_refusal_can_fire",
                  "test_the_refusals_review_78s_reader_found_unplanted_can_fire")


def test_every_refusal_of_the_builder_fires_in_this_lock(monkeypatch):
    """Review 78: a refusal that no planted control can make fire is not known to work.  This test runs every planting test of
    this file once more with the builder recorded, and asks that each refusal in the builder's source was issued at least
    once.  A refusal added to the builder without a control fails here.  (Two refusals read a seat's pinned revision and can
    fire only where this clone holds it; they are excused, by name, in a clone that does not.)"""
    g = globals()
    assert all(name in g for name in PLANTING_TESTS)
    fired = fired_by([g[name] for name in PLANTING_TESTS], monkeypatch)
    never = [tpl for tpl, rx in _refusal_patterns() if not any(rx.fullmatch(m) for m in fired)]
    if not SEATS:
        never = [t for t in never if not t.startswith(("a work-order quote", "the work order does not say", "the relayed ruling", "the advisor seat's", "the seat's %s does not hold"))]
    assert not never, never


def test_the_findings_live_counts_are_the_builders():
    """Review 78: the one line of live counts in the findings is the builder's own, so the prose cannot carry a stale count silently"""
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "> " + bp.live_line(B["stats"]) + "\n" in f
    assert f.count("LIVE: ") == 1


def test_a_sentence_cut_for_a_cell_ends_at_a_word_and_says_that_it_is_cut():
    """Added 2026-11-12 (Review 79's second round).  The cut had no lock.  What could fail: a whole word dropped where the cut
    falls just after it; a sentence returned as the mark alone; a cut in the middle of a word; a short sentence changed."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("bp_short", HERE / "build_programme.py"); bp = importlib.util.module_from_spec(spec); spec.loader.exec_module(bp)
    assert bp.short("a short sentence") == "a short sentence"
    s = "x" * 100 + " exactword" + " trailing words that go on"
    assert bp.short(s, 110) == "x" * 100 + " exactword […]"                     # the word that ends at the cut is kept
    assert bp.short(" " + "y" * 200, 110) == "y" * 110 + " […]"                  # a leading space does not empty it
    assert bp.short("one two three four five six", 12) == "one two […]"         # never in the middle of a word
    for text in ("Given the unit, the chiral three is an index on the weave's own surface; the three lines carry a vector of units",) * 1:
        out = bp.short(text, 60)
        assert out.endswith(" […]") and text.startswith(out[:-4]) and text[len(out) - 4] == " "
    # MOVED 2026-11-12 (Review 80; the SM seat's finding 29).  Two lines stood here:
    #     page = (ARC / "PROGRAMME.md").read_text(encoding="utf-8")
    #     assert "the option the owner chose, in main's label" in page and "NOT CONFIRMED: the owner, \"" not in page
    # They looked for one phrase and forbade one spelling, and passed while the page held a block quotation of the owner.
    # What is asked of the page is now `what_the_plans_page_quotes`, below, with its own test.


# Review 80 (2026-11-12; the SM seat's finding 29).  The page gives what the owner answered in plain words and quotes nothing he
# said (register row P-796).  The lock asked for less: one phrase present, one spelling absent.  This reads the page by shape.
_OPENS = "\"“‘«'"
_AN_OPENING_MARK = re.compile(r"(?:(?<=[\s:,;(\[])|^)[%s](?=\S)" % re.escape(_OPENS))
_A_WORD_FOR_THE_OWNER = re.compile(r"\b(?:[Oo]wner|[Hh]e|[Hh]is|[Hh]im)\b")
_A_BLOCK = re.compile(r"^\s*(?:[-*+]\s+|\d+\.\s+)?>|<\s*(?:blockquote|q)\b", re.I)
WITHIN = 120
# What this reader found on the page the day it was written, 2026-11-12, and did not mend: a ruling of 2026-10-08 that the
# page names by three words in single marks, in two places (the package WP-1.4 and its row in section 9).  Whether a ruling's
# name in marks is a quotation of the owner is main's to say; it went back to main with this patch.  The list shortens
# freely.  It grows only with a line here that says who entered the name and why.
HELD_BY_NAME = {"even ticks observed": 2}


def the_owners_answers_in_plain_words():
    """what the source keeps of each answer of the owner: main's account, or the label of the option he chose"""
    return ([S.CONFIRMATION[1]] + list(S.NOT_CONFIRMED.values()) + [v[2] for v in S.CONFIRMED_LATER.values()]
            + [r[2] for r in S.DIRECT_RULINGS])


def what_the_plans_page_quotes(page, accounts=None, held=None):
    """Every place where the plan's page could be quoting the owner, as (line number, what it is).  Three shapes:
      1. a block quotation.  The page has none of its own, so a line that opens with '>' is one, and so is the HTML for one;
      2. a quotation mark that OPENS with a word for the owner in the 120 characters before it, in the same cell.  A mark
         that closes a quotation of another's words (a sentence of a seat that names the owner) is not one: it follows a
         letter.  A phrase of HELD_BY_NAME is not reported, up to the number of places the table gives it;
      3. an account that the source keeps in plain words, printed inside quotation marks, which would present it as his.
    What it cannot see: his words given with no mark at all, or set in italics.  A reader sees those; this does not."""
    accounts = the_owners_answers_in_plain_words() if accounts is None else accounts
    left = dict(HELD_BY_NAME if held is None else held)
    out = []
    for n, line in enumerate(page.split("\n"), 1):
        if _A_BLOCK.search(line):
            out.append((n, "a block quotation"))
        for cell in line.split("|"):
            for m in _AN_OPENING_MARK.finditer(cell):
                if not _A_WORD_FOR_THE_OWNER.search(cell[max(0, m.start() - WITHIN):m.start()]):
                    continue
                name = next((k for k in left if cell[m.end():].startswith(k)), None)
                if name and left[name] > 0:
                    left[name] -= 1
                    continue
                out.append((n, "a quotation opens after a word for the owner"))
        for a in accounts:
            if a and any(o + a in line for o in _OPENS):
                out.append((n, "an account kept in plain words is printed in quotation marks"))
    return out


def _as_the_lock_asked_before(page):
    return "the option the owner chose, in main's label" in page and "NOT CONFIRMED: the owner, \"" not in page


def test_the_plans_page_quotes_nothing_of_the_owner():
    """The planted pages below each pass what the lock asked before 2026-11-12, and each is reported now.  The first is the
    page as it stood until that day: the builder printed the owner's answer as a block quotation, and the lock passed."""
    page = (ARC / "PROGRAMME.md").read_text(encoding="utf-8")
    assert what_the_plans_page_quotes(page) == []
    # the two places held by name are there to be held: with the table empty they are reported, and a third is reported
    assert [w for _, w in what_the_plans_page_quotes(page, held={})] == ["a quotation opens after a word for the owner"] * 2
    assert len(what_the_plans_page_quotes(page + "\nThe owner's ruling ('even ticks observed') once more.\n")) == 1
    assert "the option the owner chose, in main's label" in page                # the column that says whose words a label is
    at = "The owner answered main on %s." % S.CONFIRMATION[0]
    assert page.count(at) == 1
    words = "planted words that stand for an answer"
    plants = {
        "a block quotation, as the builder printed it": page.replace(at, at + "\n\n> \"%s\"\n" % words),
        "a block quotation with no mark in it": page.replace(at, at + "\n\n> %s\n" % words),
        "a block quotation inside a list": page.replace(at, at + "\n\n- > %s\n" % words),
        "the HTML for one": page.replace(at, at + "\n\n<blockquote>%s</blockquote>\n" % words),
        "another spelling than the one forbidden": page.replace("NOT CONFIRMED: asked, the owner", "NOT CONFIRMED: the owner: \"%s\"; asked, the owner" % words, 1),
        "typographic marks": page.replace(at, at + " The owner said “%s”." % words),
        "single marks": page.replace(at, at + " He answered: '%s'." % words),
        "an account in plain words, printed as his": page.replace(S.CONFIRMATION[1], "\"%s\"" % S.CONFIRMATION[1], 1),
    }
    for what, planted_page in plants.items():
        assert planted_page != page, what
        assert _as_the_lock_asked_before(planted_page), what                     # the lock as it was passes every one
        assert what_the_plans_page_quotes(planted_page), what
    # twins that must stay quiet: a seat's sentence that names the owner, quoted in its cell; a possessive; a question of main's
    for quiet in ("| the weave discipline | \"the owner agreed to the five proposals\" | CONFIRMED |",
                  "the owner's rulings, and main's opinion on each",
                  "CONFIRMED 2026-11-11: asked \"Is the tick an act?\", the owner chose main's option: Yes, admit it (Recommended)"):
        assert what_the_plans_page_quotes(quiet) == [], quiet

