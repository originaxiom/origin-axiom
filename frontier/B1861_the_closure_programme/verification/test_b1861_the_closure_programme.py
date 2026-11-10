"""B1861 -- the closure programme is what its builder generates, it covers the map, its order does not ignore the map,
and each of its refusals can fire.

The builder reads the closure map as generated (B1858), the register, the scoreboard's data file, the record's own pages
and, where this clone holds them, the work order's and the advisor seat's revisions. In a clone without those revisions
the tests that need them are SKIPPED, visibly; nothing is counted as passed."""
import contextlib
import importlib.util
import json
import pathlib

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
    assert j["stats"] == json.loads(json.dumps(B["stats"]))
    assert [w["id"] for w in j["packages"]] == [w["id"] for w in B["packages"]]


def test_the_order_does_not_ignore_the_map():
    """every dependency edge of the map between two packages is recorded as needs or as given"""
    nodes = json.loads((bp.MAP / "NODES.json").read_text(encoding="utf-8"))
    edges = json.loads((bp.MAP / "EDGES.json").read_text(encoding="utf-8"))
    pk = {n: w["id"] for w in S.WP for n in w["nodes"]}
    wp = {w["id"]: w for w in B["packages"]}
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
            assert pk[b] in wp[pk[a]]["rests_on"], (a, b, pk[a], pk[b])
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
    assert st["relayed_rulings"] == len(S.RULINGS) == 11
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
    assert "when all seven hold" in g and "**Version 1.64" in g and "7. *Worth spending.*" in g
