"""B1883 -- WHERE WE STAND: how far the record is from the final reading, as one generated page.

The owner asked, on 2026-11-11: "how far are we from ... 100% ready for the final reading? the dynamic scoreboard we talked?"
The advisor seat answered with a script that reads main's own generated files (its tools/where_we_stand.py @ 3dcc6319).  This is
main's own page for the same question: generated here, compared with this builder at every push by the gate closure-generated,
and quoted in every landing report to the owner.

NOTHING IS TYPED.  Every number is read from files that main's other builders write and that gates compare with those builders:
the closure programme's data (B1861), the closure map (B1858), the scoreboard's data file, and the point register.  The builder
refuses to write where two of its sources disagree.

    python3 build_where_we_stand.py            # build and print; write nothing
    python3 build_where_we_stand.py --write    # also write WHERE_WE_STAND.md and WHERE_WE_STAND.json beside this arc
"""
import collections
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
ARC = pathlib.Path(__file__).resolve().parents[1]
PROGRAMME = ROOT / "frontier" / "B1861_the_closure_programme" / "PROGRAMME.json"
NODES = ROOT / "frontier" / "B1858_the_closure_map" / "NODES.json"
SCOREBOARD = ROOT / "docs" / "total_inputs_scoreboard.json"
SCOREBOARD_PAGE = ROOT / "docs" / "TOTAL_INPUTS_SCOREBOARD.md"
REGISTER = ROOT / "docs" / "POINT_REGISTER.md"


def tally(ps):
    d = sum(p["status"].startswith("DONE") for p in ps)
    s = sum(p["status"].startswith("STARTED") for p in ps)
    return d, s, len(ps) - d - s


def register_counts(text):
    """open rows of the register by type, and the owner's open calls, by main's own parse of its rows"""
    rows = []
    for line in text.split("\n"):
        if re.match(r"^\| P-\d+ \|", line):
            c = line.split(" | ")
            if len(c) == 7:
                rows.append((c[0][2:], c[4], c[5], c[3]))
    open_rows = [r for r in rows if r[1] in ("QUEUED", "LEAD", "OWNER")]
    kinds = collections.Counter()
    for pid, disp, where, _ in open_rows:
        m = re.match(r"\[(DEBT|LEAD|PROCESS)\]", where)
        kinds["OWNER" if disp == "OWNER" else (m.group(1) if m else "UNTYPED")] += 1
    owner = [(pid, point) for pid, disp, _w, point in rows if disp == "OWNER"]
    return len(rows), len(open_rows), dict(kinds), owner


def build(_programme=None, _scoreboard=None, _page=None, _register=None, _nodes=None):
    fails = []
    P = _programme if _programme is not None else json.loads(PROGRAMME.read_text(encoding="utf-8"))
    sb = _scoreboard if _scoreboard is not None else json.loads(SCOREBOARD.read_text(encoding="utf-8"))
    page = _page if _page is not None else SCOREBOARD_PAGE.read_text(encoding="utf-8")
    reg = _register if _register is not None else REGISTER.read_text(encoding="utf-8")
    nodes = _nodes if _nodes is not None else json.loads(NODES.read_text(encoding="utf-8"))
    st, pk = P["stats"], P["packages"]
    by_id = {p["id"]: p for p in pk}

    # ---- refusals: two sources that must agree
    m = re.search(r"(\d+) of (\d+) earned", page)
    if not m:
        fails.append("the scoreboard's page has no line 'k of n earned'")
    elif int(m.group(1)) != sb["earned"]:
        fails.append("the scoreboard's page says %s earned and its data file says %d" % (m.group(1), sb["earned"]))
    recount = collections.Counter(p["status"].split()[0] if not p["status"].startswith("NOT STARTED") else "NOT STARTED" for p in pk)
    if dict(recount) != st["packages_by_status"]:
        fails.append("the programme's count of packages by status (%s) is not a recount of its packages (%s)" % (st["packages_by_status"], dict(recount)))
    waits = st["packages_the_sealed_card_must_wait_on_for_that"]
    for w in waits:
        if w not in by_id:
            fails.append("the sealed card waits on a package the programme does not hold: %s" % w)
    card = [p for p in pk if p["title"] == "The sealed card"]
    comp = [p for p in pk if p["title"] == "Calibration and comparison"]
    count_pkg = [p for p in pk if p["title"].startswith("The count as an output")]
    if len(card) != 1 or len(comp) != 1 or len(count_pkg) != 1:
        fails.append("the programme does not hold exactly one package each for the sealed card, the comparison and the count as an output")
    if len(nodes) != st["map_nodes"]:
        fails.append("the map has %d nodes and the programme read %d" % (len(nodes), st["map_nodes"]))
    if fails:
        return {"fails": fails, "stats": {"not_checked_in_this_clone": []}}

    card, comp, count_pkg = card[0], comp[0], count_pkg[0]
    by_ob = collections.defaultdict(list)
    for p in pk:
        by_ob[p["obligation"]].append(p)
    miles = []
    for mid, name, what, members in P["milestones"]:
        ps = [by_id[x] for x in members if x in by_id] + [p for ob in members if ob in by_ob for p in by_ob[ob]]
        d, s, n = tally(ps)
        miles.append({"id": mid, "name": name, "packages": len(ps), "done": d, "started": s, "not_started": n})
    wd, ws, wn = tally([by_id[w] for w in waits])
    total, n_open, kinds, owner = register_counts(reg)
    d, s, n = tally(pk)
    S = {
        "values_earned": sb["earned"], "values_in_all": int(m.group(2)), "rows_the_scoreboard_lists": len(sb["observables"]),
        "the_sealed_card": {"id": card["id"], "status": card["status"]},
        "calibration_and_comparison": {"id": comp["id"], "status": comp["status"]},
        "packages_the_card_waits_on": {"ids": waits, "done": wd, "started": ws, "not_started": wn,
                                       "each": [[w, by_id[w]["status"].split(" (")[0], by_id[w]["title"]] for w in waits]},
        "milestones": miles,
        "packages": {"all": len(pk), "done": d, "started": s, "not_started": n, "with_no_owner": st["unowned"],
                     "by_obligation": {ob: dict(zip(("done", "started", "not_started"), tally(by_ob[ob])), all=len(by_ob[ob])) for ob in sorted(by_ob)}},
        "obligations": {o[0]: o[1] for o in P["obligations"]},
        "map": {"nodes": st["map_nodes"], "nodes_that_need_a_path": st["nodes_needing_a_path"], "debts": st["debts"], "debts_joined_to_nothing": st["debts_on_the_map_joined_to_nothing"]},
        "put_in_by_hand": {"independent_choices": st["independent_choices"], "items": st["budget_items"], "by_kind": st["budget"], "supplied_by_the_lanes_model": st["lanes_supplied_inputs"],
                           "with_an_exit_on_the_table": st["inputs_with_an_exit_on_the_table"], "exits_by_kind": st["exits_by_kind"],
                           "conditional_headlines": st["open_choices_under_each_conditional_headline"], "conditional_results": st["conditional_results"]},
        "audit": {"findings": st["audit_findings"], "by_state": st["audit_findings_by_state"], "with_the_seats_verdict": st["findings_with_a_re_audit_verdict"],
                  "fixed_and_not_yet_re_audited": st["fixed_and_not_yet_re_audited"], "changed_by_main_since_its_re_audit": st["findings_main_changed_since_the_re_audit"]},
        "register": {"points": total, "open": n_open, "by_kind": kinds, "owner_calls_open": [o[0] for o in owner]},
        "the_count_as_an_output": {"id": count_pkg["id"], "status": count_pkg["status"]},
        "not_checked_in_this_clone": [],
    }
    S["ready_for_the_final_reading"] = bool(card["status"].startswith("DONE") and wn == 0 and ws == 0)
    return {"fails": [], "stats": S, "owner_rows": owner}


def generated(B):
    S = B["stats"]
    L = ["# WHERE WE STAND — how far the record is from the final reading", "",
         "*Generated by `frontier/B1883_where_we_stand/verification/build_where_we_stand.py --write`. Do not edit: the gate",
         "`closure-generated` compares this page with its builder at every push. Nothing here is typed. Every number is read",
         "from files that main's other builders write: the closure programme (B1861), the closure map (B1858), the scoreboard's",
         "data file and the point register.*", "",
         "## 1. In one line", "",
         "**Ready for the final reading: %s.** %d of %d values earned. The sealed card (%s) is %s; of the %d packages it must wait on, %d are done, %d started and %d not started." % (
             "YES" if S["ready_for_the_final_reading"] else "NO", S["values_earned"], S["values_in_all"], S["the_sealed_card"]["id"], S["the_sealed_card"]["status"].split(" (")[0],
             len(S["packages_the_card_waits_on"]["ids"]), S["packages_the_card_waits_on"]["done"], S["packages_the_card_waits_on"]["started"], S["packages_the_card_waits_on"]["not_started"]), "",
         "The final reading is a sealed set of predictions set beside measurement. It happens once, after everything below.", "",
         "## 2. The final reading", "",
         "| | state |", "|---|---|",
         "| values earned | %d of %d |" % (S["values_earned"], S["values_in_all"]),
         "| the sealed card (%s) | %s |" % (S["the_sealed_card"]["id"], S["the_sealed_card"]["status"].split(" (")[0]),
         "| calibration and comparison (%s) | %s |" % (S["calibration_and_comparison"]["id"], S["calibration_and_comparison"]["status"].split(" (")[0]), "",
         "**What the sealed card must wait on:**", "", "| package | what | state |", "|---|---|---|"]
    for w, status, title in S["packages_the_card_waits_on"]["each"]:
        L.append("| %s | %s | %s |" % (w, title, status))
    L += ["", "**The three milestones:**", "", "| milestone | packages | done | started | not started |", "|---|---|---|---|---|"]
    for m in S["milestones"]:
        L.append("| %s, %s | %d | %d | %d | %d |" % (m["id"], m["name"], m["packages"], m["done"], m["started"], m["not_started"]))
    p = S["packages"]
    L += ["", "## 3. The work order", "",
          "**%d packages: %d done, %d started, %d not started.** %d have no owner (%s)." % (p["all"], p["done"], p["started"], p["not_started"], len(p["with_no_owner"]), ", ".join(p["with_no_owner"]) or "none"), "",
          "| obligation | what | packages | done | started | not started |", "|---|---|---|---|---|---|"]
    for ob, t in p["by_obligation"].items():
        L.append("| %s | %s | %d | %d | %d | %d |" % (ob, S["obligations"].get(ob, ""), t["all"], t["done"], t["started"], t["not_started"]))
    mp = S["map"]
    L += ["", "- **The map:** %d nodes, of which %d still need a path to a result." % (mp["nodes"], mp["nodes_that_need_a_path"]),
          "- **Debts on the map:** %d, of which %d are joined to no node yet." % (mp["debts"], mp["debts_joined_to_nothing"]), "",
          "## 4. What is still put in by hand", ""]
    h = S["put_in_by_hand"]
    L += ["- **%d independent choices on main's spine,** which are %d items: %s." % (h["independent_choices"], h["items"], ", ".join("%d %s" % (v, k) for k, v in sorted(h["by_kind"].items()))),
          "- **%d more** are supplied by the lanes' model." % h["supplied_by_the_lanes_model"],
          "- **An exit is on the table for %d** of the choices: a way it could stop being a choice. None has been taken." % h["with_an_exit_on_the_table"],
          "- **%d results are conditional.** The headline ones, with the open choices under each: %s." % (h["conditional_results"], ", ".join("%s on %d" % kv for kv in sorted(h["conditional_headlines"].items()))), "",
          "| how a choice could leave | choices |", "|---|---|"]
    for k, v in sorted(h["exits_by_kind"].items(), key=lambda kv: -kv[1]):
        L.append("| %s | %d |" % (k, v))
    a = S["audit"]
    L += ["", "## 5. The audit of 2026-11-10", "",
          "- **%d findings:** %s." % (a["findings"], ", ".join("%s %d" % (k.lower(), v) for k, v in sorted(a["by_state"].items(), key=lambda kv: -kv[1]))),
          "- **%d carry the auditing seat's own verdict.** Fixed by main and not yet read by that seat: %s." % (a["with_the_seats_verdict"], ", ".join(a["fixed_and_not_yet_re_audited"]) or "none"),
          "- **Changed by main since the seat last read them:** %s." % (", ".join(a["changed_by_main_since_its_re_audit"]) or "none"), "",
          "## 6. The record's own list", ""]
    r = S["register"]
    L += ["- **%d points registered, %d open:** %s." % (r["points"], r["open"], ", ".join("%d %s" % (v, k.lower()) for k, v in sorted(r["by_kind"].items(), key=lambda kv: -kv[1]))),
          "- **Calls that are the owner's to make (%d):**" % len(B["owner_rows"])]
    for pid, point in B["owner_rows"]:
        L.append("  - %s: %s" % (pid, (point[:150] + "…") if len(point) > 150 else point))
    L += ["", "## 7. What this page does not know", "",
          "- **Which seats have work main has not read.** That depends on the clone; the gate `harvest-debt` prints it at every push.",
          "- **How many planted violations the gates catch.** The auditing seat runs that suite; its last count is on the register (P-757).",
          "- **The count itself is still printed from a typed data file,** and its denominator is a typed constant of the scoreboard's checker (the data file lists %d rows). It is not yet computed from each value's ancestry on the map: that is package %s, %s." % (
              S["rows_the_scoreboard_lists"],
              S["the_count_as_an_output"]["id"], S["the_count_as_an_output"]["status"].split(" (")[0]), ""]
    return {"WHERE_WE_STAND.md": "\n".join(L), "WHERE_WE_STAND.json": json.dumps(S, indent=1, sort_keys=True) + "\n"}


def one_line(S):
    """the line a landing report quotes"""
    w = S["packages_the_card_waits_on"]
    return "%d of %d earned; sealed card %s; it waits on %d packages (%d done, %d started, %d not started); %d packages in all, %d done; %d of %d map nodes still need a path; %d choices put in by hand" % (
        S["values_earned"], S["values_in_all"], S["the_sealed_card"]["status"].split(" (")[0], len(w["ids"]), w["done"], w["started"], w["not_started"],
        S["packages"]["all"], S["packages"]["done"], S["map"]["nodes_that_need_a_path"], S["map"]["nodes"], S["put_in_by_hand"]["independent_choices"])


if __name__ == "__main__":
    B = build()
    if B["fails"]:
        for f in B["fails"]:
            print("REFUSED: " + f)
        sys.exit(1)
    files = generated(B)
    if "--write" in sys.argv:
        for name, text in files.items():
            (ARC / name).write_text(text, encoding="utf-8")
    print(one_line(B["stats"]))
