#!/usr/bin/env python3
"""B1861 -- build and check the closure programme (the work order of 2026-11-10, sharpened).

Reads the closure map as generated (B1858's NODES.json and EDGES.json), the register, the scoreboard's data file, the
record's own pages, and this arc's programme_source.py. It REFUSES to build when
  1. a map node that needs a path (an input, an open question, a lane's result or a duty) is in no package, or in two;
  2. a package names a node that is not in the map or one that needs no path; an ALSO entry names an unknown node or
     package, or a node's own primary package;
  3. a ranked debt of the register has no package;
  4. a conditional result names no premise;
  5. `needs` holds an unknown id or a cycle, or GIVEN holds an unknown id;
  6. THE ORDER IGNORES THE MAP: a `requires`, `applies-under` or `blocks` edge of the map joins nodes of two packages,
     and neither `needs` (followed to its end) nor GIVEN records that the one package rests on the other;
  7. a register row that a package cites is not in the register;
  8. a present input of main's spine is not typed exactly once (a choice, a rule of the comparison, or a tally); a kind
     disagrees with the record's grade (a FITTED node outside a `real` entry, an ANSATZ node outside an `ansatz` entry,
     an `axiom` entry with a member that GENESIS does not grade POSTULATED); a lane's supplied input is not listed;
  9. the budget's joints of the candidate frame are not the scoreboard data file's borrowed joints, or a kind disagrees
     with the scoreboard's type for that joint;
 10. a package lacks a question, a first step, a closing condition or an owner, carries an intent or status outside the
     lists, or is marked DONE while it holds anything but declared postulates and choices;
 11. an obligation's phrase is not in the work order at its pinned revision;
 12. a finding of the advisor seat's audit has no package or no state, a state other than OPEN has no note, or the
     programme names a finding the audit does not hold;
 13. a relayed ruling or a quoted sentence of that seat is not in its file as quoted, or a ruling has no package; a ruling is
     marked confirmed that is not among the relayed ones, or without the owner's words and date, or without main's opinion
     (which the owner asked for with the confirmation); an opinion is written for a ruling that is not confirmed;
 14. a row of the record's own checklist for a theory of everything has no package, or a quoted word of the record is gone.
 15. an input of the budget has no line saying how it could leave the budget (or that no route is named), the line's kind is
     outside the list, a route is named and not described, a dictionary entry is not an identification, a kept entry is
     not an axiom, or a line is written for something that is not an input.
Rules 11 to 13 read other seats' branches. Where this clone does not hold a revision, the rule is NOT CHECKED, the
statistics say so, and the last line printed says so.

    python3 -B build_programme.py            check and print the statistics
    python3 -B build_programme.py --write    also write PROGRAMME.md and PROGRAMME.json beside the arc
"""
import collections
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
ROOT = ARC.parents[1]
MAP = ROOT / "frontier" / "B1858_the_closure_map"
sys.path.insert(0, str(HERE))
import programme_source as S  # noqa: E402

TERMINAL = ("DERIVED", "NEGATIVE", "RECORD", "CONFIRMED")          # proved, refuted, or a fact about the record
CONDITIONAL = ("CONDITIONAL", "READING")                           # proved given premises: closes when its premises close
OTHER = ("DEBT", "CLOSURE")                                        # the register's debts; the map's own groupings
INPUT_GRADES = ("POSTULATED", "CHOSEN", "TAGGED", "FITTED", "ANSATZ", "UNSTATED")
INTENTS = ("DERIVE", "DECIDE", "VERIFY", "DECLARE", "OWNER")
STATUSES = ("NOT STARTED", "STARTED", "DONE")
KINDS = ("axiom", "bit", "discrete", "real", "ansatz", "identification")
PLURAL = {"axiom": "axioms", "bit": "bits", "discrete": "discrete choices", "real": "real numbers", "ansatz": "ansatz",
          "identification": "identifications"}
FINDING_ORDER = ["G", "L", "E", "M", "P", "V", "X", "R", "W"]


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def register_rows():
    rows = {}
    for line in (ROOT / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8").split("\n"):
        if re.match(r"^\| P-\d+ \|", line):
            c = line.split(" | ")
            rows[c[0][2:]] = c[4] if len(c) == 7 else "?"
    return rows


def seat_file(rev, path, raw=False):
    """a file at a seat's pinned revision: None if this clone does not hold the revision, '' if the file is not there"""
    if subprocess.run(["git", "-C", str(ROOT), "cat-file", "-e", rev + "^{commit}"], capture_output=True).returncode != 0:
        return None
    r = subprocess.run(["git", "-C", str(ROOT), "show", "%s:%s" % (rev, path)], capture_output=True)
    if r.returncode != 0:
        return ""
    s = r.stdout.decode("utf-8", "replace")
    return s if raw else norm(s)


def fkey(fid):
    pre = re.match(r"[A-Z]+", fid).group(0)
    return (FINDING_ORDER.index(pre) if pre in FINDING_ORDER else 99, int(re.search(r"\d+", fid).group(0)))


def build(nodes=None, edges=None):
    fails, notes = [], []
    nodes = json.loads((MAP / "NODES.json").read_text(encoding="utf-8")) if nodes is None else nodes
    edges = json.loads((MAP / "EDGES.json").read_text(encoding="utf-8")) if edges is None else edges
    by = {n["id"]: n for n in nodes}
    wps = [dict(w) for w in S.WP]
    wp = {w["id"]: w for w in wps}
    obl = [o[0] for o in S.OBLIGATIONS]
    rows = register_rows()

    # ---- 10: each package is whole
    if len(wp) != len(wps):
        fails.append("a package id repeats")
    for w in wps:
        for k in ("title", "question", "first", "accept", "owner"):
            if not str(w.get(k, "")).strip():
                fails.append("%s has no %s" % (w["id"], k))
        if w["intent"] not in INTENTS:
            fails.append("%s: intent %r is not one of %s" % (w["id"], w["intent"], INTENTS))
        if not w["status"].startswith(STATUSES):
            fails.append("%s: status %r" % (w["id"], w["status"]))
        if w["obligation"] not in obl:
            fails.append("%s: obligation %r" % (w["id"], w["obligation"]))
        if not w["question"].rstrip().endswith("?"):
            fails.append("%s: its question is not a question" % w["id"])
        if w["status"].startswith("DONE"):
            bad = [n for n in w["nodes"] if n in by and by[n]["grade"] not in ("POSTULATED", "CHOSEN")]
            if w["intent"] != "DECLARE" or bad:
                fails.append("%s is marked DONE and is not a declaration of postulates and choices only: %s" % (w["id"], ", ".join(bad) or w["intent"]))

    # ---- 1, 2: the map's nodes that need a path, each in exactly one package
    need = [n["id"] for n in nodes if n["grade"] not in TERMINAL + CONDITIONAL + OTHER]
    pkg_of = {}
    for w in wps:
        for nid in w["nodes"]:
            if nid not in by:
                fails.append("%s names a node that is not in the map: %s" % (w["id"], nid))
            elif nid not in need:
                fails.append("%s names a node that needs no closure path: %s (%s)" % (w["id"], nid, by[nid]["grade"]))
            if nid in pkg_of:
                fails.append("a node is in two packages: %s in %s and %s" % (nid, pkg_of[nid], w["id"]))
            pkg_of[nid] = w["id"]
    for nid in need:
        if nid not in pkg_of:
            fails.append("a map node has no package: %s (%s) %s" % (nid, by[nid]["grade"], by[nid]["text"][:70]))
    for nid, ps in S.ALSO.items():
        if nid not in pkg_of:
            fails.append("ALSO names a node that is in no package: %s" % nid)
        for x in ps:
            if x not in wp:
                fails.append("ALSO sends %s to an unknown package: %s" % (nid, x))
            elif pkg_of.get(nid) == x:
                fails.append("ALSO repeats %s's own package: %s" % (nid, x))

    # ---- 3: the debts
    debt_of = {}
    for n in nodes:
        if n["grade"] != "DEBT":
            continue
        row = n["rows"][0]
        w = S.DEBT_TO_WP.get(row) or S.DEBT_CLASS_TO_WP.get(n.get("debt_class"))
        if not w or w not in wp:
            fails.append("a ranked debt has no package: %s (class %r)" % (row, n.get("debt_class")))
        else:
            debt_of[row] = w
    for row in S.DEBT_TO_WP:
        if "P:" + row[2:] not in by or by["P:" + row[2:]]["grade"] != "DEBT":
            notes.append("%s is assigned one by one and is no longer a ranked debt" % row)

    # ---- the map's own groupings, with the packages under each (a table, not a check: rule 1 already assigns every member)
    closure = {}
    for n in nodes:
        if n["grade"] == "CLOSURE":
            closure[n["id"]] = sorted({pkg_of[m] for m in n.get("members", []) if m in pkg_of})

    # ---- 5: the order of work, and what rests on what
    def expand(ns):
        out = []
        for x in ns:
            if x.startswith("@"):
                out += [w["id"] for w in wps if w["obligation"] == x[1:]]
            else:
                out.append(x)
        return out
    for w in wps:
        w["needs_all"] = [d for d in expand(w["needs"]) if d != w["id"]]
        w["given"] = list(S.GIVEN.get(w["id"], []))
        for d in w["needs"]:
            if d.startswith("@") and d[1:] not in obl:
                fails.append("%s needs an unknown obligation: %s" % (w["id"], d))
        for d in w["needs_all"]:
            if d not in wp:
                fails.append("%s needs an unknown package: %s" % (w["id"], d))
        for d in w["given"]:
            if d not in wp:
                fails.append("GIVEN names an unknown package under %s: %s" % (w["id"], d))
    for k in S.GIVEN:
        if k not in wp:
            fails.append("GIVEN names an unknown package: %s" % k)
    wave, state = {}, {}

    def level(i, path=()):
        if i in wave:
            return wave[i]
        if state.get(i) == "open":
            fails.append("the packages' needs hold a cycle: %s" % " -> ".join(path + (i,)))
            return 0
        state[i] = "open"
        wave[i] = 1 + max([level(d, path + (i,)) for d in wp[i]["needs_all"] if d in wp] or [-1])
        state[i] = "done"
        return wave[i]
    for w in wps:
        level(w["id"])

    def closure_of(i, rel):
        seen, stack = set(), [i]
        while stack:
            for d in rel(stack.pop()):
                if d in wp and d not in seen:
                    seen.add(d)
                    stack.append(d)
        return seen
    anc_needs = {w["id"]: closure_of(w["id"], lambda j: wp[j]["needs_all"]) - {w["id"]} for w in wps}
    rests = {w["id"]: closure_of(w["id"], lambda j: wp[j]["needs_all"] + wp[j]["given"]) for w in wps}

    # ---- 6: the order may not ignore the map
    proj = collections.defaultdict(list)
    for e in edges:
        if e["kind"] in ("requires", "applies-under"):
            a, b = e["src"], e["dst"]
        elif e["kind"] == "blocks":
            a, b = e["dst"], e["src"]                 # the blocked node rests on the one that blocks it
        else:
            continue
        if a in pkg_of and b in pkg_of and pkg_of[a] != pkg_of[b]:
            proj[(pkg_of[a], pkg_of[b])].append("%s rests on %s" % (a, b))
    for (x, y), why in sorted(proj.items()):
        if y not in anc_needs.get(x, ()) and y not in wp.get(x, {}).get("given", ()):
            fails.append("the order ignores the map: %s rests on %s (%s)" % (x, y, "; ".join(why[:3])))

    # ---- 4: what each conditional result waits on
    out = collections.defaultdict(list)
    for e in edges:
        if e["kind"] in ("requires", "applies-under"):
            out[e["src"]].append(e["dst"])
    bears = collections.defaultdict(list)
    for e in edges:
        if e["kind"] == "bears-on" and by.get(e["src"], {}).get("grade") == "DEBT":
            bears[e["dst"]].append(by[e["src"]]["rows"][0])

    def upstream(nid):
        seen, stack = set(), [nid]
        while stack:
            for d in out.get(stack.pop(), []):
                if d not in seen:
                    seen.add(d)
                    stack.append(d)
        return seen
    axioms = {m for i in S.INPUTS if set(i["kinds"]) == {"axiom"} for m in i["members"]}
    not_premises = set(S.TALLIES) | set(S.RULES)
    waits = {}
    for n in nodes:
        if n["grade"] in CONDITIONAL:
            if not out.get(n["id"]):
                fails.append("a conditional result names no premise: %s" % n["id"])
            up = upstream(n["id"])
            open_up = sorted(u for u in up if u in need)
            choices = [u for u in open_up if u not in axioms and u not in not_premises]
            waits[n["id"]] = dict(premises=choices, axioms=[u for u in open_up if u in axioms],
                                  not_counted=[u for u in open_up if u in not_premises],
                                  packages=sorted({pkg_of[u] for u in choices if u in pkg_of}),
                                  conditional=sorted(u for u in up if by[u]["grade"] in CONDITIONAL),
                                  debts=sorted({r for u in ({n["id"]} | up) for r in bears.get(u, [])}))
            if not open_up and not waits[n["id"]]["conditional"]:
                notes.append("%s is graded %s and every premise it names is proved: is its grade current?" % (n["id"], n["grade"]))
    released = collections.defaultdict(list)
    for nid, w in waits.items():
        if len(w["premises"]) == 1 and not w["conditional"]:
            released[w["premises"][0]].append(nid)

    # ---- 7: register rows
    for w in wps:
        for r in w["rows"]:
            if r not in rows:
                fails.append("%s cites a row that is not in the register: %s" % (w["id"], r))

    # ---- 8: the input budget
    inputs_now = [n["id"] for n in nodes if n["grade"] in INPUT_GRADES]
    typed = collections.Counter()
    entry_of = {}
    for i in S.INPUTS:
        for m in i["members"]:
            typed[m] += 1
            entry_of[m] = i
        for k in i["kinds"]:
            if k not in KINDS:
                fails.append("the budget's %r has an unknown kind: %s" % (i["name"], k))
        if set(i["kinds"]) == {"axiom"}:
            for m in i["members"]:
                if m in by and by[m]["grade"] != "POSTULATED":
                    fails.append("the budget calls %s an axiom; the record grades it %s" % (m, by[m]["grade"]))
    for m in S.RULES + S.TALLIES:
        typed[m] += 1
    for m, c in typed.items():
        if m not in by:
            fails.append("the budget names a node that is not in the map: %s" % m)
        elif by[m]["grade"] not in INPUT_GRADES:
            fails.append("the budget names a node that is not a present input: %s (%s)" % (m, by[m]["grade"]))
        if c > 1:
            fails.append("the budget types a node twice: %s" % m)
    for m in inputs_now:
        if m not in typed:
            fails.append("a present input is not in the budget: %s (%s)" % (m, by[m]["grade"]))
        elif by[m]["grade"] == "FITTED" and "real" not in entry_of.get(m, {}).get("kinds", {}):
            fails.append("a FITTED node is not typed as a real number: %s" % m)
        elif by[m]["grade"] == "ANSATZ" and "ansatz" not in entry_of.get(m, {}).get("kinds", {}):
            fails.append("an ANSATZ node is not typed as an ansatz: %s" % m)
    # ---- 15: every input says how it could leave the budget, or that no route is named
    names = [i["name"] for i in S.INPUTS]
    for n_ in names:
        if n_ not in S.EXITS:
            fails.append("an input of the budget has no line saying how it could leave: %s" % n_)
        elif S.EXITS[n_][0] not in S.EXIT_KINDS:
            fails.append("the budget's %r has an exit of an unknown kind: %s" % (n_, S.EXITS[n_][0]))
        elif S.EXITS[n_][0] == "DICTIONARY" and set(next(i for i in S.INPUTS if i["name"] == n_)["kinds"]) != {"identification"}:
            fails.append("the budget's %r is typed a dictionary entry and is not an identification" % n_)
        elif S.EXITS[n_][0] == "KEPT" and set(next(i for i in S.INPUTS if i["name"] == n_)["kinds"]) != {"axiom"}:
            fails.append("the budget's %r is typed kept and is not an axiom" % n_)
        elif S.EXITS[n_][0] not in ("DICTIONARY", "UNTOUCHED") and not S.EXITS[n_][1]:
            fails.append("the budget's %r names a route and does not say what it is" % n_)
    for n_ in S.EXITS:
        if n_ not in names:
            fails.append("an exit is written for something that is not an input of the budget: %s" % n_)
    exits = collections.Counter(S.EXITS[n_][0] for n_ in names if n_ in S.EXITS)
    lane_inputs = sorted(n["id"] for n in nodes if n["grade"] == "LANE-INPUT")
    if lane_inputs != sorted(S.LANE_INPUT_NOTE):
        fails.append("the lanes' supplied inputs are not the ones listed: map %s, listed %s" % (lane_inputs, sorted(S.LANE_INPUT_NOTE)))
    budget = collections.Counter()
    for i in S.INPUTS:
        for k, v in i["kinds"].items():
            budget[k] += v
        i["packages"] = sorted({pkg_of[m] for m in i["members"] if m in pkg_of})
        i["grades"] = sorted({by[m]["grade"] for m in i["members"] if m in by})
        i["weave_or_thread"] = sorted({by[m].get("weave_or_thread", "n/a") for m in i["members"] if m in by} - {"n/a"})

    # ---- 9: the candidate frame's joints, against the scoreboard's data file
    sb = json.loads((ROOT / "docs" / "total_inputs_scoreboard.json").read_text(encoding="utf-8"))
    earned = ("FORCED-BY-MAIN", "VERIFIED-BY-MAIN")
    sb_joints = {"S:" + j["id"]: j["type"] for j in sb["shared_block"] if j["type"] not in earned}
    sb_joints.update({"A:" + j["id"]: j["type"] for j in sb["frames"]["A"]["joints"] if j["type"] not in earned})
    mine = sorted(m for m in entry_of if m.startswith(("A:", "S:")))
    if mine != sorted(sb_joints):
        fails.append("the budget's joints of the candidate frame are not the scoreboard's borrowed joints: %s against %s" % (mine, sorted(sb_joints)))
    for m, typ in sb_joints.items():
        k = set(entry_of.get(m, {}).get("kinds", {}))
        if (typ == "FITTED") != ("real" in k) or (typ == "ANSATZ") != ("ansatz" in k):
            fails.append("the budget's kind for %s (%s) disagrees with the scoreboard's type %s" % (m, sorted(k), typ))

    # ---- 11: the work order's own words
    wo = seat_file(*S.WORK_ORDER)
    wo_checked = 0
    unchecked = []
    if wo is None:
        unchecked.append("the work order")
    else:
        for k, q in S.WORK_ORDER_QUOTES.items():
            if re.search(r"\d", q):
                fails.append("a work-order quote carries a digit: %s" % k)
            if norm(q) not in wo:
                fails.append("the work order does not say: %r (%s)" % (q, k))
            else:
                wo_checked += 1

    # ---- 12, 13: the advisor seat's audit, finding by finding; its relayed rulings; its own words
    arev, adir = S.ADVISOR
    for fid, f in S.FINDINGS.items():
        if f["wp"] not in wp:
            fails.append("finding %s is assigned to an unknown package: %s" % (fid, f["wp"]))
        if f["state"] not in S.FINDING_STATES:
            fails.append("finding %s has a state outside the list: %r" % (fid, f["state"]))
        elif f["state"] != "OPEN" and not f["note"]:
            fails.append("finding %s is marked %s with no note saying what main did or checked" % (fid, f["state"]))
    raw = seat_file(arev, adir + "/ADVISOR_TO_CC_2026-11-10_AUDIT_FINDINGS.md", raw=True)
    audit_checked = 0
    if raw is None:
        unchecked.append("the advisor seat's audit")
    else:
        ids = set(re.findall(r"^\| ([GLEMPVXRW]\d+) \|", raw, re.M))     # the audit's nine classes of finding
        for fid in sorted(ids - set(S.FINDINGS)):
            fails.append("a finding of the audit has no package: %s" % fid)
        for fid in sorted(set(S.FINDINGS) - ids):
            fails.append("the programme names a finding the audit does not hold: %s" % fid)
        audit_checked = len(ids & set(S.FINDINGS))
        rul = seat_file(arev, adir + "/OWNER_RULINGS_2026-11-10.md")
        for name, q, ps in S.RULINGS:
            if norm(q) not in (rul or ""):
                fails.append("the relayed ruling %r is not in the seat's file as quoted" % name)
        for path, q in S.ADVISOR_QUOTES:
            if norm(q) not in (seat_file(arev, adir + "/" + path) or ""):
                fails.append("the advisor seat's %s does not say: %r" % (path, q))
    for name, q, ps in S.RULINGS:
        if not ps or any(x not in wp for x in ps):
            fails.append("the relayed ruling %r has no package" % name)
    names_r = [name for name, q, ps in S.RULINGS]
    for name in S.CONFIRMED:
        if name not in names_r:
            fails.append("a ruling is marked confirmed and is not among the relayed rulings: %s" % name)
        if name not in S.OPINION or not S.OPINION[name]:
            fails.append("the owner asked for main's opinion on every confirmed ruling; none is written for: %s" % name)
    for name in S.OPINION:
        if name not in S.CONFIRMED:
            fails.append("an opinion is written for a ruling that is not confirmed: %s" % name)
    if S.CONFIRMED and not (S.CONFIRMATION[0] and S.CONFIRMATION[1]):
        fails.append("rulings are marked confirmed with no date or no words of the owner")
    for name, words in S.NOT_CONFIRMED.items():
        if name not in names_r:
            fails.append("a ruling is marked not confirmed and is not among the relayed rulings: %s" % name)
        if name in S.CONFIRMED:
            fails.append("a ruling is marked both confirmed and not confirmed: %s" % name)
        if not words:
            fails.append("a ruling is marked not confirmed without the owner's words: %s" % name)

    # ---- 14: the record's own checklist and words
    toe = norm((ROOT / "docs" / "TOE_REQUIREMENTS_LEDGER.md").read_text(encoding="utf-8"))
    for k, (title, ps) in enumerate(S.TOE_LEDGER):
        if norm("| %d | **%s** |" % (k + 1, title)) not in toe:
            fails.append("the record's checklist has no row %d %r" % (k + 1, title))
        if not ps or any(x not in wp for x in ps):
            fails.append("the checklist row %r has no package" % title)
    for path, q in S.MAIN_QUOTES:
        f = ROOT / path
        if not f.is_file() or norm(q) not in norm(f.read_text(encoding="utf-8")):
            fails.append("%s does not say: %r" % (path, q))
    for hid in S.HEADLINES:
        if hid not in by:
            fails.append("a headline result is not in the map: %s" % hid)

    # ---- derived tables
    fstate = collections.Counter(f["state"] for f in S.FINDINGS.values())
    under = collections.Counter()
    for i, r in rests.items():
        for d in r:
            if d != i:
                under[d] += 1
    # packages that can only close together: each rests on the other
    together, seen = [], set()
    for w in wps:
        i = w["id"]
        if i in seen:
            continue
        grp = sorted(j for j in (rests[i] | {i}) if i in (rests[j] | {j}))
        if len(grp) > 1:
            together.append(grp)
            seen |= set(grp)
    for w in wps:
        i = w["id"]
        w["wave"] = wave.get(i, 0)
        w["node_grades"] = dict(collections.Counter(by[n]["grade"] for n in w["nodes"] if n in by))
        w["node_labels"] = dict(collections.Counter(by[n].get("weave_or_thread", "n/a") for n in w["nodes"] if n in by))
        w["rows_live"] = {r: rows.get(r, "?") for r in w["rows"]}
        w["debts"] = sorted(r for r, x in debt_of.items() if x == i)
        w["blocks"] = sorted(x["id"] for x in wps if i in x["needs"])          # those that name it one by one
        w["closure_nodes"] = sorted(c for c, ps in closure.items() if i in ps)
        w["findings"] = sorted((fid for fid, f in S.FINDINGS.items() if f["wp"] == i), key=fkey)
        w["rulings"] = [name for name, q, ps in S.RULINGS if i in ps]
        w["rests_on"] = sorted(rests[i] - {i})
        w["sits_under"] = under.get(i, 0)
        w["also_nodes"] = sorted(n for n, ps in S.ALSO.items() if i in ps)
    by_layer = collections.OrderedDict()
    for n in nodes:
        if n["id"] in need:
            by_layer.setdefault(n["layer"], collections.Counter())[pkg_of.get(n["id"], "NONE")] += 1
    cond_heads = [h for h in S.HEADLINES if h in waits]
    stats = collections.OrderedDict(
        map_nodes=len(nodes), nodes_needing_a_path=len(need), nodes_assigned=len([n for n in need if n in pkg_of]),
        conditional_results=len(waits), debts=len(debt_of), packages=len(wps),
        packages_by_obligation={o: len([w for w in wps if w["obligation"] == o]) for o in obl},
        packages_by_status={s: len([w for w in wps if w["status"].startswith(s)]) for s in STATUSES},
        packages_by_intent={i: len([w for w in wps if w["intent"] == i]) for i in INTENTS},
        unowned=sorted(w["id"] for w in wps if w["owner"] == "unowned"),
        waves=1 + max(wave.values()) if wave else 0,
        map_dependencies_between_packages=len(proj), packages_that_close_together=together,
        independent_choices=len(S.INPUTS), budget=dict((k, budget.get(k, 0)) for k in KINDS), budget_items=sum(budget.values()),
        rules_of_the_comparison=len(S.RULES), lanes_supplied_inputs=len(lane_inputs), present_inputs=len(inputs_now),
        candidate_frame_joints=len(sb_joints),
        exits_by_kind={k: exits.get(k, 0) for k in S.EXIT_KINDS},
        inputs_with_an_exit_on_the_table=sum(exits.get(k, 0) for k in ("FORCING ARGUED", "RIGID", "BACK-EDGE NAMED")),
        audit_findings=len(S.FINDINGS), audit_findings_by_state={s: fstate.get(s, 0) for s in S.FINDING_STATES}, relayed_rulings=len(S.RULINGS),
        rulings_confirmed_by_the_owner_to_main=len(S.CONFIRMED), rulings_not_confirmed=len(S.NOT_CONFIRMED), rulings_asked=len(S.RULINGS) - len(S.CONFIRMED) - len(S.NOT_CONFIRMED),
        headline_results_that_are_conditional_results=cond_heads,
        headline_results_not_yet_results_on_main=[h for h in S.HEADLINES if h not in waits],
        open_choices_under_each_conditional_headline={h: len(waits[h]["premises"]) for h in cond_heads},
        conditional_headlines_released_by_closing_one_choice=len([h for h in cond_heads if any(h in v for v in released.values())]),
        work_order_quotes_checked=wo_checked, audit_findings_checked_at_the_seats_revision=audit_checked, not_checked_in_this_clone=unchecked)
    return dict(packages=wps, waits=waits, closure=closure, debt_of=debt_of, by_layer=by_layer, stats=stats, fails=fails, notes=notes,
                nodes=by, pkg_of=pkg_of, released=dict(released), proj={"%s -> %s" % k: v for k, v in proj.items()})


def cell(s):
    return str(s).replace("|", "∣").replace("\n", " ")


def render(B):
    st, wps, by = B["stats"], B["packages"], B["nodes"]
    L = ["# The closure programme", "",
         "*Generated by `verification/build_programme.py` from the closure map (B1858), the register, the scoreboard's data",
         "file and `programme_source.py`. Do not edit by hand. The builder refuses to write this page if a node of the map",
         "that still needs a path is in no package, or if the order of work ignores a dependency the map records.*", ""]
    if st["not_checked_in_this_clone"]:
        L += ["**NOT CHECKED in the clone that built this page:** %s (their revisions are not in it)." % ", ".join(st["not_checked_in_this_clone"]), ""]
    L += ["## 1. The state, in numbers", "",
          "- **%d nodes of the map still need a path:** inputs, open questions, lanes' results not verified on main, and duties. **All %d are in a package.**"
          % (st["nodes_needing_a_path"], st["nodes_assigned"]),
          "  The map's other nodes are proved, refuted or facts about the record; or they are the %d conditional results (§ 6), the %d debts (C0) and the map's own eleven groupings."
          % (st["conditional_results"], st["debts"]),
          "- **%d packages** in %d waves: %s." % (st["packages"], st["waves"], ", ".join("%s %d" % (k.lower(), v) for k, v in st["packages_by_status"].items())),
          "- **%d packages have no owner:** %s." % (len(st["unowned"]), ", ".join(st["unowned"]) or "none"),
          "- **Main's spine presently holds %d inputs as the record lists them** (§ 3): %s. The lanes' model adds %d supplied inputs of its own, not typed here."
          % (st["independent_choices"], ", ".join("%d %s" % (v, PLURAL[k]) for k, v in st["budget"].items()), st["lanes_supplied_inputs"]),
          "- **%d findings of the advisor seat's audit** are each in a package (§ 8): %s." % (st["audit_findings"], ", ".join("%s %d" % (k.lower(), v) for k, v in st["audit_findings_by_state"].items())),
          "- **%d rulings of the owner, as that seat relayed them,** are each mapped to a package. The owner confirmed %d of them to main on %s and did not confirm %d; %d more are asked (§ 9)." % (
              st["relayed_rulings"], st["rulings_confirmed_by_the_owner_to_main"], S.CONFIRMATION[0], st["rulings_not_confirmed"], st["rulings_asked"]),
          ""]
    # ---- milestones
    L += ["## 2. The three milestones", "",
          "The work order keeps three statuses apart. Each is read here from the packages' statuses, which main types in the source.", "",
          "| | milestone | what it needs | packages | done |", "|---|---|---|---|---|"]
    met = []
    for mid, name, needs, scope in S.MILESTONES:
        ps = [w for w in wps if w["id"] in scope or w["obligation"] in scope]
        done = [w for w in ps if w["status"].startswith("DONE")]
        L.append("| %s | **%s** | %s | %d | %d |" % (mid, name, cell(needs), len(ps), len(done)))
        if len(done) == len(ps):
            met.append(mid)
    L += ["", "**Met at this build: %s.**" % (", ".join(met) if met else "none"),
          "The coverage check of M1 passes at this build (%d of %d). M1 stays open while the map is rebuilt by hand and while the lanes'" % (st["nodes_assigned"], st["nodes_needing_a_path"]),
          "proofs stand in it at headline level only (WP-0.6).", ""]
    # ---- budget
    L += ["## 3. The input budget", "",
          "Every node of the map that is presently an input of main's spine, grouped by the choice it names. The same choice",
          "stands under several names across the record. The kinds follow the record's own grades where it has them; the",
          "builder checks them against GENESIS's grades and the scoreboard's types. Their independence is the record's listing.", "",
          "| kind | now | what a parameter-free theory may keep |", "|---|---|---|"]
    for k in KINDS:
        L.append("| %s | %d | %s |" % (k, st["budget"][k], cell(S.TARGET[k])))
    L += ["", "| the choice | kind | names in the map | stated about | settled by |", "|---|---|---|---|---|"]
    for i in S.INPUTS:
        kinds = ", ".join(("%d × %s" % (v, k)) if v > 1 else k for k, v in i["kinds"].items()) + (" (a functional form from a menu)" if i.get("form") else "")
        L.append("| %s%s | %s | %s | %s | %s |" % (cell(i["name"]), (" — " + cell(i["note"])) if i["note"] else "", kinds, ", ".join(i["members"]),
                                              ", ".join(i["weave_or_thread"]) or "—", ", ".join(i["packages"])))
    L += ["", "### How each input could leave the budget", "",
          "Read from three notes of the advisor seat (its forcing ledger, its statement of the closed loop, its design of the first",
          "back-edge; pinned at `%s`), each read in full and checked by main in B1867. This is a harvest of those notes onto the" % S.ADVISOR[0],
          "budget. It is not a sweep of the record, and it changes no grade: an argument is not a proof, and a named back-edge is not",
          "a built one.", "",
          "| kind | inputs | what it means |", "|---|---|---|"]
    for k, v in S.EXIT_KINDS.items():
        L.append("| %s | %d | %s |" % (k, st["exits_by_kind"][k], cell(v)))
    L += ["", "**An exit is on the table for %d of the %d inputs** (a forcing argument, rigidity, or a named back-edge). None is proved or built." % (
              st["inputs_with_an_exit_on_the_table"], st["independent_choices"]), "",
          "| the choice | kind | route | what the notes say, and what main checked |", "|---|---|---|---|"]
    for i in S.INPUTS:
        kinds = ", ".join(("%d × %s" % (v, k)) if v > 1 else k for k, v in i["kinds"].items())
        ek, et = S.EXITS[i["name"]]
        L.append("| %s | %s | %s | %s |" % (cell(i["name"]), kinds, ek, cell(et) or "—"))
    L += ["", "**Not inputs of the theory:** %d rules of the comparison (%s), which say how a prediction is graded; and one tally (%s)."
          % (len(S.RULES), ", ".join(S.RULES), ", ".join(S.TALLIES)), "",
          "**Outside this budget:** the lanes' conditional model has %d supplied inputs of its own. Main has not typed them, because main has not verified the model:" % len(S.LANE_INPUT_NOTE), ""]
    L += ["- %s: %s (%s)." % (k, v, B["pkg_of"].get(k, "?")) for k, v in sorted(S.LANE_INPUT_NOTE.items())]
    L += ["", "The agy lane's frame has borrowed joints of its own, counted on the scoreboard and held in WP-4.7.", ""]
    # ---- order
    L += ["## 4. The order of work", "",
          "Two relations are kept apart.",
          "- **Needs:** a package cannot be worked before these close. The waves are computed from it.",
          "- **Given:** a package can be worked first, and its result is then conditional on these. A lane's result verified on main is still conditional on that lane's supplied inputs.",
          "",
          "The builder projects every dependency edge of the map onto the packages (%d between different packages) and refuses" % st["map_dependencies_between_packages"],
          "an order that leaves one out.", "",
          "### What sits under the most", "",
          "For each package, how many others rest on it, by needs and given together. This, and not the wave, says what unblocks the most.", "",
          "| package | others resting on it | owner | status |", "|---|---|---|---|"]
    for w in sorted(wps, key=lambda w: (-w["sits_under"], w["id"]))[:12]:
        L.append("| %s %s | %d | %s | %s |" % (w["id"], cell(w["title"]), w["sits_under"], cell(w["owner"]), cell(w["status"])))
    if st["packages_that_close_together"]:
        L += ["", "### Packages that can only close together", "",
              "Each group rests on itself: no member becomes unconditional before the others.", ""] + ["- %s." % ", ".join(g) for g in st["packages_that_close_together"]]
    L += ["", "### The waves", ""]
    head = ["| package | question | owner | status | given |", "|---|---|---|---|---|"]

    def row(w):
        return "| %s %s | %s | %s | %s | %s |" % (w["id"], cell(w["title"]), cell(w["question"]), cell(w["owner"]), cell(w["status"]), ", ".join(w["given"]) or "—")
    for k in range(st["waves"]):
        ws = sorted([w for w in wps if w["wave"] == k], key=lambda w: (-w["sits_under"], w["id"]))
        if ws:
            L += ["**Wave %d**" % (k + 1), ""] + head + [row(w) for w in ws] + [""]
    # ---- packages
    L += ["## 5. The packages", ""]
    for oid, oname, osrc in S.OBLIGATIONS:
        L += ["### %s. %s" % (oid, oname), "", "*%s.*" % osrc, ""]
        for w in [w for w in wps if w["obligation"] == oid]:
            L += ["**%s — %s** (%s; %s; owner: %s)" % (w["id"], w["title"], w["intent"], w["status"], w["owner"]), "",
                  "- **The question:** %s" % w["question"],
                  "- **The first step:** %s." % w["first"].rstrip("."),
                  "- **Closed when:** %s." % w["accept"].rstrip(".")]
            if w["needs"]:
                L.append("- **Needs:** %s." % ", ".join(("every package of " + x[1:]) if x.startswith("@") else x for x in w["needs"]))
            if w["given"]:
                L.append("- **Given (its result is conditional on):** %s." % ", ".join(w["given"]))
            if w["nodes"]:
                L.append("- **Nodes (%d):** %s." % (len(w["nodes"]), ", ".join(w["nodes"])))
                lab = {k: v for k, v in w["node_labels"].items() if k != "n/a"}
                if lab:
                    L.append("- **Stated about:** %s." % ", ".join("%s %d" % (k, v) for k, v in sorted(lab.items())))
            if w["also_nodes"]:
                L.append("- **Also bears on nodes held elsewhere:** %s." % ", ".join(w["also_nodes"]))
            if w["closure_nodes"]:
                L.append("- **Missing dependencies it works on:** %s." % ", ".join(w["closure_nodes"]))
            if w["rows_live"]:
                L.append("- **Register:** %s." % ", ".join("%s (%s)" % (r, d) for r, d in w["rows_live"].items()))
            if w["debts"]:
                L.append("- **Debts (%d):** %s." % (len(w["debts"]), ", ".join(w["debts"])))
            if w["findings"]:
                L.append("- **The audit's findings (%d):** %s." % (len(w["findings"]), ", ".join(w["findings"])))
            if w["rulings"]:
                L.append("- **Relayed rulings:** %s." % "; ".join(w["rulings"]))
            L.append("")
    # ---- coverage
    L += ["## 6. Coverage", "", "### By layer of the map", "", "| layer | nodes needing a path | packages |", "|---|---|---|"]
    for layer, c in sorted(B["by_layer"].items(), key=lambda kv: int(kv[0].split()[0])):
        L.append("| %s | %d | %s |" % (layer, sum(c.values()), ", ".join("%s (%d)" % (k, v) for k, v in sorted(c.items()))))
    L += ["", "### The map's missing dependencies", "", "| missing dependency | packages working on it |", "|---|---|"]
    for c, ps in sorted(B["closure"].items()):
        L.append("| %s | %s |" % (c, ", ".join(ps)))
    L += ["", "### What each conditional result waits on", "",
          "A conditional result is proved given its premises. The axioms of the foundation are premises that are kept; the open",
          "choices are what must close. The counts are lower bounds: they follow the map's `requires` and `applies-under` edges only.", "",
          "| result | what it says | open choices | packages | the foundation's axioms it uses | debts that bear on it |", "|---|---|---|---|---|---|"]
    for nid, w in B["waits"].items():
        L.append("| %s | %s | %s | %s | %s | %s |" % (nid, cell(by[nid]["text"][:110]),
                                               ", ".join(w["premises"]) or ("none of its own: it rests on %s" % ", ".join(w["conditional"]) if w["conditional"] else "none"),
                                               ", ".join(w["packages"]) or "—", ", ".join(w["axioms"]) or "—", ", ".join(w["debts"]) or "—"))
    L += ["", "### The premises are in series", "",
          "What would become a theorem if one open choice alone were closed:", "",
          "| choice closed alone | results released |", "|---|---|"]
    for prem, rs in sorted(B["released"].items()):
        L.append("| %s | %s |" % (prem, ", ".join(sorted(rs))))
    hl = st["headline_results_that_are_conditional_results"]
    L += ["", "No headline result is among them. Of the map's six headline results, %d are conditional results: %s."
          % (len(hl), "; ".join("%s waits on %d open choices" % (h, st["open_choices_under_each_conditional_headline"][h]) for h in hl)),
          "The other %d are not yet results on main at all: %s." % (len(st["headline_results_not_yet_results_on_main"]),
                                                                   "; ".join("%s (%s)" % (h, by[h]["grade"]) for h in st["headline_results_not_yet_results_on_main"])),
          "Closing one choice releases a lemma. The advisor seat's dry run found the same on the candidate frame, where every joint",
          "feeds every row.", ""]
    L += ["### The record's own checklist for a theory of everything", "", "| row | packages |", "|---|---|"]
    for k, (title, ps) in enumerate(S.TOE_LEDGER):
        L.append("| %d %s | %s |" % (k + 1, title, ", ".join(ps)))
    L += ["", "### The debts, by package", "", "| package | debts |", "|---|---|"]
    for w in wps:
        if w["debts"]:
            L.append("| %s %s | %d: %s |" % (w["id"], cell(w["title"]), len(w["debts"]), ", ".join(w["debts"])))
    # ---- certificate
    L += ["", "## 7. The certificate", "",
          "What every arc that a value uses must carry before the value may be sealed. The standard is the advisor seat's;",
          "main adds two parts.", "",
          "| part | what it means | whose |", "|---|---|---|"]
    for name, what, whose in S.CERTIFICATE:
        L.append("| %s | %s | %s |" % (name, cell(what), cell(whose)))
    L += ["", "**The status of a value, computed from everything it uses by the weakest link:**", "", "| status | when |", "|---|---|"]
    for name, when in S.VALUE_STATUS:
        L.append("| %s | %s |" % (name, cell(when)))
    L += ["", "**The seal's rule:**", ""] + ["%d. %s" % (k + 1, s) for k, s in enumerate(S.SEAL_RULE)] + [""]
    # ---- the audit
    L += ["## 8. The advisor seat's audit, finding by finding", "",
          "The audit read main as it stood on 2026-11-07. Its own rule is that a finding is reproduced on main before anything",
          "is banked. OPEN: not yet reproduced on main. READER: main's reader reproduced it and main has not repeated the check.",
          "REPRODUCED: main's own check. PARTLY FIXED: part of the acceptance row is met, and the note says what is left.",
          "FIXED: main meets the whole row as main reads it; that seat's re-audit decides.", "",
          "| finding | what it says | package | on main | what main did or checked |", "|---|---|---|---|---|"]
    for fid in sorted(S.FINDINGS, key=fkey):
        f = S.FINDINGS[fid]
        L.append("| %s | %s | %s | %s | %s |" % (fid, cell(f["short"]), f["wp"], f["state"], cell(f["note"]) or "—"))
    L += ["", "## 9. The owner's rulings of 2026-11-10: relayed by the advisor seat, and confirmed to main", "",
          "The advisor seat recorded them and wrote that main confirms each with the owner before acting on it. That is also",
          "main's standing rule for a relayed ruling. Main asked about the %d then relayed. The owner answered main on %s:" % (len(S.CONFIRMED), S.CONFIRMATION[0]),
          "", "> \"%s\"" % S.CONFIRMATION[1], "",
          "So %d are confirmed, and main's opinion on each, which the owner asked for, is in the table. %d were relayed after main had" % (len(S.CONFIRMED), len(S.NOT_CONFIRMED)),
          "asked. Asked about those, the owner did not confirm them (the words are in the table): main treats them as no ruling and",
          "acts on neither. %d more sentences, recorded by the seat later and marked by it as relayed, are asked of the owner and not" % (len(S.RULINGS) - len(S.CONFIRMED) - len(S.NOT_CONFIRMED)),
          "acted on. A confirmed ruling is carried out in its packages, in landings of its own; this page changes no governing",
          "document.", "",
          "| ruling | in the seat's words | state | packages | main's opinion |", "|---|---|---|---|---|"]
    for name, q, ps in S.RULINGS:
        L.append("| %s | \"%s\" | %s | %s | %s |" % (name, cell(q), "CONFIRMED" if name in S.CONFIRMED else "NOT CONFIRMED: the owner, \"%s\"" % S.NOT_CONFIRMED[name] if name in S.NOT_CONFIRMED else "ASKED",
                                                 ", ".join(ps), cell(S.OPINION.get(name, "")) or "—"))
    L.append("")
    return "\n".join(L) + "\n"


def main():
    B = build()
    if "--write" in sys.argv and not B["fails"]:
        (ARC / "PROGRAMME.md").write_text(render(B), encoding="utf-8")
        out = dict(stats=B["stats"], packages=B["packages"], waits=B["waits"], closure=B["closure"], debt_of=B["debt_of"],
                   inputs=S.INPUTS, rules=S.RULES, tallies=S.TALLIES, certificate=S.CERTIFICATE, value_status=S.VALUE_STATUS,
                   seal_rule=S.SEAL_RULE, findings=S.FINDINGS, rulings=S.RULINGS, confirmed=S.CONFIRMED, confirmation=list(S.CONFIRMATION), opinion=S.OPINION, not_confirmed=S.NOT_CONFIRMED, released=B["released"], map_dependencies=B["proj"],
                   given=S.GIVEN, also=S.ALSO, exits={k: list(v) for k, v in S.EXITS.items()}, exit_kinds=S.EXIT_KINDS)
        (ARC / "PROGRAMME.json").write_text(json.dumps(out, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
        print("written: PROGRAMME.md, PROGRAMME.json")
    print(json.dumps(B["stats"], indent=1, ensure_ascii=False))
    for n in B["notes"]:
        print("NOTE:", n)
    for f in B["fails"]:
        print("REFUSED:", f)
    if B["fails"]:
        print("%d REFUSALS" % len(B["fails"]))
    else:
        nc = B["stats"]["not_checked_in_this_clone"]
        print("THE PROGRAMME COVERS THE MAP" + ("; NOT CHECKED IN THIS CLONE: " + ", ".join(nc) if nc else ""))
    return 1 if B["fails"] else 0


if __name__ == "__main__":
    sys.exit(main())
