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
     marked confirmed that is not among the relayed ones, or without a date and main's plain words on what the owner answered, or without main's opinion
     (which the owner asked for with the confirmation); an opinion is written for a ruling that is not confirmed;
 14. a row of the record's own checklist for a theory of everything has no package, or a quoted word of the record is gone.
 16. a finding names nothing it bears on, or names something that is not there;
 17. the sealed card does not wait on a package that holds a finding about the repository as a whole, or a debt the map joins
     to nothing: what no value's own list can show must be clean before any seal;
 18. a package is marked started while a package it cannot be worked before has not started;
 19. a finding is marked FIXED and the advisor seat's re-audit did not accept it, or says the correction was not carried.
 20. main records a change made after the re-audit for a finding the re-audit gave no verdict on, or names an arc that is not
     on main; and a finding so changed is never shown as re-audited at its new state.
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
    confirmed = list(S.CONFIRMED) + list(S.CONFIRMED_LATER)             # the first eleven by one answer; the later ones each by its own
    for name, (date_, asked_, answer_) in S.CONFIRMED_LATER.items():
        if not (date_ and asked_ and answer_):
            fails.append("a later confirmation has no date, question or answer of the owner: %s" % name)
        if name in S.CONFIRMED:
            fails.append("a ruling is confirmed twice: %s" % name)
    for name, asked_, answer_, date_, ps, means_ in S.DIRECT_RULINGS:
        if not (date_ and asked_ and answer_ and means_):
            fails.append("a ruling given to main directly has no date, question, answer or meaning: %s" % name)
        if not ps or any(x not in wp for x in ps):
            fails.append("a ruling given to main directly has no package: %s" % name)
        if name in names_r:
            fails.append("a ruling given to main directly bears a relayed ruling's name: %s" % name)
    for name in confirmed:
        if name not in names_r:
            fails.append("a ruling is marked confirmed and is not among the relayed rulings: %s" % name)
        if name not in S.OPINION or not S.OPINION[name]:
            fails.append("the owner asked for main's opinion on every confirmed ruling; none is written for: %s" % name)
    for name in S.OPINION:
        if name not in confirmed:
            fails.append("an opinion is written for a ruling that is not confirmed: %s" % name)
    if S.CONFIRMED and not (S.CONFIRMATION[0] and S.CONFIRMATION[1]):
        # REWORDED 2026-11-12 (Review 80; the SM seat's finding 28).  It read "rulings are marked confirmed with no date or no
        # words of the owner": the builder asked for his words, and the page printed them.  What it asks for now is main's
        # account of what he answered, in plain words.
        fails.append("rulings are marked confirmed with no date, or with nothing in plain words on what the owner answered")
    for name, words in S.NOT_CONFIRMED.items():
        if name not in names_r:
            fails.append("a ruling is marked not confirmed and is not among the relayed rulings: %s" % name)
        if name in confirmed:
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

    # ---- 16 to 19: the joins the seal's rule needs (the advisor seat's read of this page as a non-author; B1873)
    CARD = "WP-5.3"
    tracked = None
    def exists(tok):
        if tok == S.REPO or tok in by:
            return True
        if re.fullmatch(r"B\d+", tok):
            return any((ROOT / "frontier").glob(tok + "_*"))
        return (ROOT / tok).exists()
    for fid, f in S.FINDINGS.items():
        bo = S.BEARS_ON.get(fid)
        if not bo:
            fails.append("finding %s names nothing it bears on (an arc, a node of the map, a tracked path, or the repository as a whole)" % fid)
            continue
        for tok in bo:
            if not exists(tok):
                fails.append("finding %s bears on something that is not there: %s" % (fid, tok))
    for fid in S.BEARS_ON:
        if fid not in S.FINDINGS:
            fails.append("a bears-on line is written for a finding the programme does not hold: %s" % fid)
    touched = {e["src"] for e in edges} | {e["dst"] for e in edges}
    unjoined = sorted(n["id"] for n in nodes if n["kind"] == "debt" and n["id"] not in touched)
    row_of_debt = {n["id"]: (n["rows"][0] if n.get("rows") else n["id"].split(":")[-1]) for n in nodes if n["kind"] == "debt"}
    must = {}
    for fid, f in S.FINDINGS.items():
        if S.REPO in S.BEARS_ON.get(fid, []):
            must.setdefault(f["wp"], []).append(fid)
    for nid in unjoined:
        w_ = debt_of.get(row_of_debt[nid])
        if w_:
            must.setdefault(w_, []).append(row_of_debt[nid])
    if CARD in wp:
        for w_, why in sorted(must.items()):
            if w_ != CARD and w_ not in anc_needs[CARD]:
                fails.append("the sealed card does not wait on %s, which holds what no value's own list can show (%s%s)" % (
                    w_, ", ".join(why[:4]), ", ..." if len(why) > 4 else ""))
    for w in wps:
        if not w["status"].startswith("NOT STARTED"):
            for d in w["needs"]:
                for x in expand([d]):
                    if x in wp and x != w["id"] and wp[x]["status"].startswith("NOT STARTED"):
                        fails.append("%s is marked %s while %s, which it cannot be worked before, has not started (use GIVEN for work done first and conditional)" % (
                            w["id"], w["status"].split()[0], x))
    for fid, verdict in S.ACCEPTED.items():
        if fid not in S.FINDINGS:
            fails.append("a re-audit verdict is written for a finding the programme does not hold: %s" % fid)
        elif S.FINDINGS[fid]["state"] == "FIXED" and not verdict.startswith("accepted") :
            fails.append("finding %s is marked FIXED and the re-audit did not accept it: %s" % (fid, verdict))
        elif S.FINDINGS[fid]["state"] == "FIXED" and "not carried" in verdict:
            fails.append("finding %s is marked FIXED and the re-audit says the correction was not carried everywhere" % fid)
    # ---- 21 (B1880; the advisor seat's third re-audit, its case j4): a verdict is the seat's, so it is read in the seat's file.
    # Each verdict has a row of the re-audit that gave it, verbatim; the first row names the finding and its bold words are the
    # verdict in force, with which the programme's own wording must begin.
    reaudit_text = {}
    for fname, (srev, mrev) in S.REAUDITS.items():
        reaudit_text[fname] = seat_file(srev, S.ADVISOR[1] + "/" + fname)
        if reaudit_text[fname] is None and "the advisor seat's re-audits" not in unchecked:
            unchecked.append("the advisor seat's re-audits")
    verdicts_checked = 0
    for fid, verdict in S.ACCEPTED.items():
        rows_ = S.VERDICT_ROWS.get(fid)
        if not rows_:
            fails.append("the re-audit's verdict on %s has no row of the seat's file behind it" % fid)
            continue
        for k, (fname, row) in enumerate(rows_):
            if fname not in S.REAUDITS:
                fails.append("a verdict row for %s names a re-audit the programme does not hold: %s" % (fid, fname))
                continue
            if reaudit_text[fname] is not None:
                if norm(row) not in reaudit_text[fname]:
                    fails.append("the seat's %s does not hold the row quoted for %s: %r" % (fname, fid, row))
                else:
                    verdicts_checked += 1
            if k == 0:
                if not re.search(r"(?<![A-Za-z0-9])%s(?![0-9])" % re.escape(fid), row):
                    fails.append("the row that carries the verdict in force on %s does not name that finding: %r" % (fid, row))
                said = re.findall(r"\*\*([^*]+)\*\*", row)
                if not said or not norm(verdict).lower().startswith(norm(said[-1]).lower()):
                    fails.append("the programme's verdict on %s does not begin with the seat's own words in its row (%r): %r" % (fid, said[-1] if said else "", verdict))
    for fid in S.VERDICT_ROWS:
        if fid not in S.ACCEPTED:
            fails.append("a row of a re-audit is quoted for %s, which has no verdict here" % fid)
    fixed_unread = sorted(fid for fid, f in S.FINDINGS.items() if f["state"] == "FIXED" and fid not in S.ACCEPTED)
    for fid, (arc_, what_) in S.SINCE_REAUDIT.items():
        if fid not in S.ACCEPTED:
            fails.append("a change since the re-audit is recorded for %s, on which the re-audit gave no verdict" % fid)
        if not re.fullmatch(r"B\d+", arc_) or not list((ROOT / "frontier").glob(arc_ + "_*")):
            fails.append("a change since the re-audit names an arc that is not on main: %s (%s)" % (arc_, fid))
        if not what_:
            fails.append("a change since the re-audit says nothing of what changed: %s" % fid)

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
    # THE COMPARISON RESTS ON EVERYTHING (2026-11-11; the advisor seat's row ORD-a; P-782).  Until this date nothing waited on
    # WP-0.8, the errors in the mathematics, or on WP-0.10: the card could be sealed with them open.  A package that nothing
    # needs is an end of the order.  With one end, and no circle among the needs, every package lies under that end.  With two,
    # the reading could be taken with one of them unfinished, so the order is refused.
    ends = sorted(w["id"] for w in wps if not any(w["id"] in x["needs_all"] for x in wps))
    if len(ends) != 1:
        fails.append("the work order has %d packages that nothing needs (%s); it must have one, the last step, or the reading could be taken with the others unfinished"
                     % (len(ends), ", ".join(ends)))
    # The advisor seat's residual on that rule (its run of ORD-a at 818d17f46, cases o2 and o3): with WP-0.8 moved from the
    # upstream audit to the comparison, or to the independent challenge, the order still has one end, and the CARD no longer
    # rests on the errors in the mathematics: it could be sealed with them open and only the comparison would wait.  The row
    # itself, stated: the sealed card rests on every package of the first obligation, the clean record.
    if CARD in wp:
        lacking = sorted(w["id"] for w in wps if w["obligation"] == "C0" and w["id"] not in rests[CARD])
        if lacking:
            fails.append("the sealed card does not rest on %s, of the clean record: it could be sealed with %s open"
                         % (", ".join(lacking), "it" if len(lacking) == 1 else "them"))
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
        forcing_arguments_one_clause_short=exits.get("ONE CLAUSE SHORT", 0),
        findings_that_bear_on_the_repository_as_a_whole=sum(1 for fid in S.FINDINGS if S.REPO in S.BEARS_ON.get(fid, [])),
        findings_that_name_arcs_nodes_or_pages_only=sum(1 for fid in S.FINDINGS if S.BEARS_ON.get(fid) and S.REPO not in S.BEARS_ON[fid]),
        debts_on_the_map_joined_to_nothing=len(unjoined), packages_the_sealed_card_must_wait_on_for_that=sorted(must),
        findings_with_a_re_audit_verdict=len(S.ACCEPTED), fixed_and_not_yet_re_audited=fixed_unread, verdict_rows_read_in_the_seats_files=verdicts_checked,
        findings_main_changed_since_the_re_audit=sorted(S.SINCE_REAUDIT),
        audit_findings=len(S.FINDINGS), audit_findings_by_state={s: fstate.get(s, 0) for s in S.FINDING_STATES}, relayed_rulings=len(S.RULINGS),
        rulings_confirmed_by_the_owner_to_main=len(confirmed), rulings_not_confirmed=len(S.NOT_CONFIRMED), rulings_asked=len(S.RULINGS) - len(confirmed) - len(S.NOT_CONFIRMED),
        rulings_given_to_main_directly=len(S.DIRECT_RULINGS),
        headline_results_that_are_conditional_results=cond_heads,
        headline_results_not_yet_results_on_main=[h for h in S.HEADLINES if h not in waits],
        open_choices_under_each_conditional_headline={h: len(waits[h]["premises"]) for h in cond_heads},
        conditional_headlines_released_by_closing_one_choice=len([h for h in cond_heads if any(h in v for v in released.values())]),
        work_order_quotes_checked=wo_checked, audit_findings_checked_at_the_seats_revision=audit_checked, not_checked_in_this_clone=unchecked)
    return dict(packages=wps, waits=waits, closure=closure, debt_of=debt_of, by_layer=by_layer, stats=stats, fails=fails, notes=notes,
                nodes=by, pkg_of=pkg_of, released=dict(released), proj={"%s -> %s" % k: v for k, v in proj.items()})


def cell(s):
    return str(s).replace("|", "∣").replace("\n", " ")


def short(s, n=110):
    """A sentence cut for a table cell, at a word's end, and marked as cut.  CORRECTED 2026-11-12 (Review 79; found by a reading
    of this builder's page): the cell was the first n characters and no more, so a sentence could end in the middle of a word
    with nothing to say that it went on, and a condition stated after the cut was dropped unseen."""
    s = str(s).strip()
    if len(s) <= n:
        return s
    # CORRECTED 2026-11-12 (Review 79's second round; found by a reading on another family of model): where the cut fell just
    # after a whole word, that word was dropped; and a sentence that opened with a space came back as the mark alone.
    head = s[:n + 1]                                   # one character more: a space there means the last word is whole
    cut = head.rfind(" ")
    head = head[:cut] if cut > 0 else s[:n]
    # CORRECTED 2026-11-12 (Review 80; a reader's finding F10, its second part).  The last line was
    #     return head.rstrip(" ,;:") + " […]"
    # A text that opens with punctuation and a space, and then holds a word longer than the cut, was cut at that first space:
    # what was kept held no word, and came back as the mark alone, or as one dash and the mark.  Where the cut keeps no letter
    # and no digit, the text is cut at n characters, as a single long word is.
    kept = head.rstrip(" ,;:")
    # CORRECTED 2026-11-12 (Review 80; the third gap of the cold read of the mend above, not checked by main, made again by
    # the builder).  The last three lines were
    #     if not any(c.isalnum() for c in kept):
    #         kept = s[:n].rstrip(" ,;:") or s[:n]
    #     return kept + " […]"
    # Three texts still came back with nothing of the sentence in them: one that opens with a bracket or a dash and then holds
    # only spaces and commas up to the cut (the mark alone); one that opens with a comma and spaces (the comma and the spaces);
    # and a short label in brackets before a long word (the label alone).  So: where the cut at a word's end keeps less than
    # half of what a cell may hold, the text is cut at n characters, inside the long word; and where the first n characters
    # hold no letter and no digit at all, the text is kept up to the end of its first word (to three times n at most).
    if len(kept) < n // 2 or not any(c.isalnum() for c in kept):
        kept = s[:n].rstrip(" ,;:")
    if not any(c.isalnum() for c in kept):
        first = re.search(r"\w+", s)
        kept = s[:min(first.end(), 3 * n)] if first else s[:n]
    return kept + " […]"


def render(B):
    st, wps, by = B["stats"], B["packages"], B["nodes"]
    L = ["# The closure programme", "",
         "*Generated by `verification/build_programme.py` from the closure map (B1858), the register, the scoreboard's data",
         "file and `programme_source.py`. Do not edit by hand. The builder refuses to write this page if a node of the map",
         "that still needs a path is in no package, or if the order of work ignores a dependency the map records.*", ""]
    # (B1886) What a clone could not check is no longer written into this page.  It made the page differ from one clone to the
    # next, and the gate that compares the page with this builder then skipped the comparison where a seat's branch was
    # absent: a count changed by hand on the page passed in a fresh clone (the advisor seat's fifth re-audit, its case g1).
    # The page is the same in every clone; what was not checked is said by the gate's line and by this builder's last line.
    L += ["## 1. The state, in numbers", "",
          "- **%d nodes of the map still need a path:** inputs, open questions, lanes' results not verified on main, and duties. **All %d are in a package.**"
          % (st["nodes_needing_a_path"], st["nodes_assigned"]),
          "  The map's other nodes are proved, refuted or facts about the record; or they are the %d conditional results (§ 6), the %d debts (C0) and the map's own eleven groupings."
          % (st["conditional_results"], st["debts"]),
          "- **%d packages** in %d waves: %s." % (st["packages"], st["waves"], ", ".join("%s %d" % (k.lower(), v) for k, v in st["packages_by_status"].items())),
          "- **%d packages have no owner:** %s." % (len(st["unowned"]), ", ".join(st["unowned"]) or "none"),
          "- **Main's spine presently holds %d inputs as the record lists them** (§ 3). Counted by kind they are %d items, since one input can hold more than one choice: %s. The lanes' model adds %d supplied inputs of its own, not typed here."
          % (st["independent_choices"], st["budget_items"], ", ".join("%d %s" % (v, PLURAL[k]) for k, v in st["budget"].items()), st["lanes_supplied_inputs"]),
          "- **%d findings of the advisor seat's audit** are each in a package (§ 8): %s." % (st["audit_findings"], ", ".join("%s %d" % (k.lower(), v) for k, v in st["audit_findings_by_state"].items())),
          "- **%d rulings of the owner, as that seat relayed them,** are each mapped to a package. The owner has confirmed %d of them to main (%d on %s, %d on %s) and did not confirm %d; %d are asked. **%d more rulings were given to main directly** (§ 9)." % (
              st["relayed_rulings"], st["rulings_confirmed_by_the_owner_to_main"], len(S.CONFIRMED), S.CONFIRMATION[0], len(S.CONFIRMED_LATER),
              sorted({v[0] for v in S.CONFIRMED_LATER.values()})[-1] if S.CONFIRMED_LATER else "no later date", st["rulings_not_confirmed"], st["rulings_asked"], st["rulings_given_to_main_directly"]),
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
          "**The budget is a union over frames and readings.** The fitted modulus and the choices of the rule that is meant to replace",
          "the fit are counted side by side; several inputs stand under two frames' names. It over-counts, which is the safe direction,",
          "and it is not the price of any one value: a value's price is its own certificate's list.", "",
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
    L += ["", "**An exit is on the table for %d of the %d inputs** (a forcing argument with no objection on this page, rigidity, or a named back-edge); %d more forcing arguments are one clause short. None is proved or built." % (
              st["inputs_with_an_exit_on_the_table"], st["independent_choices"], st["forcing_arguments_one_clause_short"]), "",
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
          "choices are what must close. The counts are lower bounds: they follow the map's `requires` and `applies-under` edges only.",
          "A sentence that is cut to fit ends in […]; the whole sentence, with every condition it states, is the map's (`frontier/B1858_the_closure_map/MAP.md`).", "",
          "| result | what it says | open choices | packages | the foundation's axioms it uses | debts that bear on it |", "|---|---|---|---|---|---|"]
    for nid, w in B["waits"].items():
        L.append("| %s | %s | %s | %s | %s | %s |" % (nid, cell(short(by[nid]["text"])),
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
          "Two more columns, added at the advisor seat's read of this page as a non-author. *Bears on* names what the finding touches:",
          "arcs, nodes of the map, pages, or REPOSITORY for a property of the repository as a whole that a seal depends on. *The",
          "re-audit* is that seat's verdict on main's fix, kept apart from main's own word. Each verdict is of main at the commit its",
          "re-audit read (%s), and each is read in the row of the seat's own file." % "; ".join(
              "%s read main at `%s`" % (f.split("_20")[0].replace("REAUDIT_", "re-audit "), m) for f, (srev, m) in sorted(S.REAUDITS.items())), "",
          "| finding | what it says | package | bears on | on main | the re-audit | what main did or checked |", "|---|---|---|---|---|---|---|"]
    for fid in sorted(S.FINDINGS, key=fkey):
        f = S.FINDINGS[fid]
        L.append("| %s | %s | %s | %s | %s | %s | %s |" % (fid, cell(f["short"]), f["wp"], cell(", ".join(S.BEARS_ON.get(fid, []))), f["state"],
                                                   cell(S.ACCEPTED.get(fid, "") + (" **Main has changed this since (%s); the seat has not read the change.**" % S.SINCE_REAUDIT[fid][0] if fid in S.SINCE_REAUDIT else "")) or "—",
                                                   cell(f["note"] + (" Since the re-audit (%s): %s" % S.SINCE_REAUDIT[fid] if fid in S.SINCE_REAUDIT else "")) or "—"))
    L += ["", "## 9. The owner's rulings of 2026-11-10: relayed by the advisor seat, and confirmed to main", "",
          "The advisor seat recorded them and wrote that main confirms each with the owner before acting on it. That is also",
          "main's standing rule for a relayed ruling. Main asked about the %d then relayed. The owner answered main on %s. What he" % (len(S.CONFIRMED), S.CONFIRMATION[0]),
          # CHANGED 2026-11-12 (Review 80; the SM seat's finding 28).  The next line was a block quotation of the owner's answer.
          # It is main's account of the answer, in plain words; nothing he said is quoted on this page (register row P-796).
          "answered is given here in plain words, and nothing he said is quoted (register row P-796): %s." % S.CONFIRMATION[1], "",
          "So %d are confirmed, and main's opinion on each, which the owner asked for, is in the table. %d were relayed after main had" % (len(S.CONFIRMED), len(S.NOT_CONFIRMED)),
          "asked. Asked about those, the owner did not confirm them (what he answered is in the table, in plain words): main treats them as no ruling and",
          "acts on neither. %d more sentences, recorded by the seat later and marked by it as relayed, were asked of the owner once; the" % len(S.CONFIRMED_LATER),
          "owner answered each in a dialog with main, and the question and the chosen answer are in the table. %d are still asked." % (len(S.RULINGS) - len(S.CONFIRMED) - len(S.CONFIRMED_LATER) - len(S.NOT_CONFIRMED)),
          "A confirmed ruling is carried out in its packages, in landings of its own; this page changes no governing document.", "",
          "| ruling | in the seat's words | state | packages | main's opinion |", "|---|---|---|---|---|"]
    for name, q, ps in S.RULINGS:
        L.append("| %s | \"%s\" | %s | %s | %s |" % (name, cell(q), "CONFIRMED" if name in S.CONFIRMED else "CONFIRMED %s: asked \"%s\", the owner chose main's option: %s" % S.CONFIRMED_LATER[name] if name in S.CONFIRMED_LATER else "NOT CONFIRMED: %s" % S.NOT_CONFIRMED[name] if name in S.NOT_CONFIRMED else "ASKED",
                                                 ", ".join(ps), cell(S.OPINION.get(name, "")) or "—"))
    L += ["", "**Rulings given to main directly** (no seat relayed them; each is the owner's choice among options main put to him. The",
          "question and the option's label are main's words; where main recommended an option its label says so. Nothing the owner",
          "said is quoted: register row P-796):", "",
          "| ruling | the question, as main put it | the option the owner chose, in main's label | date | packages | what it means on main |", "|---|---|---|---|---|---|"]
    for name, asked_, answer_, date_, ps, means_ in S.DIRECT_RULINGS:
        L.append("| %s | \"%s\" | %s | %s | %s | %s |" % (name, cell(asked_), cell(answer_), date_, ", ".join(ps), cell(means_)))
    L.append("")
    return "\n".join(L) + "\n"


def live_line(st):
    """one line of the live counts, for the findings: the arc's lock compares it with the page, so the hand-written prose
    cannot carry a stale count silently (Review 78: its reader found four that had gone stale within a day)"""
    return ("LIVE: %d inputs as the record lists them, %d items by kind (%s); exits: %s; an exit on the table for %d; rulings: %d relayed, %d confirmed, "
            "%d not confirmed, %d asked, and %d given to main directly; findings: %s; %d packages in %d waves." % (
                st["independent_choices"], st["budget_items"], ", ".join("%d %s" % (v, PLURAL[k]) for k, v in st["budget"].items()),
                ", ".join("%s %d" % (k, v) for k, v in st["exits_by_kind"].items()), st["inputs_with_an_exit_on_the_table"],
                st["relayed_rulings"], st["rulings_confirmed_by_the_owner_to_main"], st["rulings_not_confirmed"], st["rulings_asked"], st["rulings_given_to_main_directly"],
                ", ".join("%s %d" % (k, v) for k, v in st["audit_findings_by_state"].items()), st["packages"], st["waves"]))


CLONE_DEPENDENT = ("verdict_rows_read_in_the_seats_files", "work_order_quotes_checked", "audit_findings_checked_at_the_seats_revision", "not_checked_in_this_clone")


def generated(B):
    """the two generated files as text, by name: what --write writes, and what the gate compares the committed files with"""
    out = dict(stats={k: v for k, v in B["stats"].items() if k not in CLONE_DEPENDENT}, packages=B["packages"], waits=B["waits"], closure=B["closure"], debt_of=B["debt_of"],
               inputs=S.INPUTS, rules=S.RULES, tallies=S.TALLIES, certificate=S.CERTIFICATE, value_status=S.VALUE_STATUS,
               seal_rule=S.SEAL_RULE, findings=S.FINDINGS, rulings=S.RULINGS, confirmed=S.CONFIRMED, confirmation=list(S.CONFIRMATION), opinion=S.OPINION, not_confirmed=S.NOT_CONFIRMED, confirmed_later={k: list(v) for k, v in S.CONFIRMED_LATER.items()}, direct_rulings=[list(r) for r in S.DIRECT_RULINGS],
               bears_on=S.BEARS_ON, milestones=[list(m) for m in S.MILESTONES], obligations=[list(o) for o in S.OBLIGATIONS], accepted=S.ACCEPTED, accepted_at=list(S.ACCEPTED_AT), reaudits={k: list(v) for k, v in S.REAUDITS.items()}, verdict_rows={k: [list(r) for r in v] for k, v in S.VERDICT_ROWS.items()}, since_reaudit={k: list(v) for k, v in S.SINCE_REAUDIT.items()}, released=B["released"], map_dependencies=B["proj"],
               given=S.GIVEN, also=S.ALSO, exits={k: list(v) for k, v in S.EXITS.items()}, exit_kinds=S.EXIT_KINDS)
    return {"PROGRAMME.md": render(B), "PROGRAMME.json": json.dumps(out, indent=1, ensure_ascii=False, sort_keys=True) + "\n"}


def main():
    B = build()
    if "--write" in sys.argv and not B["fails"]:
        for name, text in generated(B).items():
            (ARC / name).write_text(text, encoding="utf-8")
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
