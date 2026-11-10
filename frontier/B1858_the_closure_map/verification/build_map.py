"""B1858 -- build and check the closure map (documentary; reads the record, runs no science, reads no held-out value).

What it does
- loads the curated nodes and edges (`map_source.py`);
- adds, mechanically: the scoreboard's joints (docs/total_inputs_scoreboard.json), the register's open debts with the
  ranked list's own one-line reason, and each cited register row's live disposition;
- CHECKS, and fails on any miss:
  1. every pin on main: the quote occurs, up to whitespace, in the file;
  2. every pin on a seat branch: the quote occurs in the file at the pinned revision (skipped, and counted, when this
     clone does not hold that revision);
  3. every GENESIS item's curated grade agrees with the status cell parsed from GENESIS.md;
  4. every scoreboard joint's type is the scoreboard's own, and its row is printed in the scoreboard page;
  5. every cited register row exists; every edge's two ends exist; no node id repeats;
- writes NODES.json, EDGES.json, MAP.md and CLOSURE_QUEUE.md beside the findings (with --write), and prints a summary.

The map is a statement about the record at one commit. It derives nothing.

IT IS A LIVING FILE. A landing that changes the register, the scoreboard, GENESIS.md, the framing ledger or any page a
pin quotes must run this with --write, or the arc's test fails: the map cannot go stale silently (P-754)."""
import collections
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
ROOT = ARC.parents[1]
sys.path.insert(0, str(HERE))
import map_source as S  # noqa: E402


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


_main_cache, _seat_cache = {}, {}


def main_text(path):
    if path not in _main_cache:
        p = ROOT / path
        _main_cache[path] = norm(p.read_text(encoding="utf-8")) if p.is_file() else None
    return _main_cache[path]


def seat_text(rev, path):
    key = (rev, path)
    if key not in _seat_cache:
        ok = subprocess.run(["git", "-C", str(ROOT), "cat-file", "-e", rev + "^{commit}"], capture_output=True).returncode == 0
        if not ok:
            _seat_cache[key] = "UNAVAILABLE"
        else:
            r = subprocess.run(["git", "-C", str(ROOT), "show", "%s:%s" % (rev, path)], capture_output=True)
            _seat_cache[key] = norm(r.stdout.decode("utf-8", "replace")) if r.returncode == 0 else None
    return _seat_cache[key]


def genesis_cells():
    out = {}
    for line in (ROOT / "GENESIS.md").read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^\| (PF\d|GM\d[a-d]?|SE\d|T-ROOT|FK\d+)(?: \*\*\[v[\d.]+\]\*\*)? \| ", line)
        if m:
            c = line.split(" | ")
            out[m.group(1)] = c[3] if m.group(1).startswith("PF") else c[2]
    return out


GRADE_WORDS = {"POSTULATED": ("POSTULATED",), "CHOSEN": ("CHOSEN", "ADOPTED", "RULED"), "OPEN": ("OPEN", "UNEARNED"),
               "DERIVED": ("DERIVED",)}
# the framing ledger's status cells, read by their first keyword
FL_WORDS = (("UNEARNED", "OPEN"), ("OPEN", "OPEN"), ("inconsistent", "OPEN"), ("working state", "OPEN"), ("CHOSEN", "CHOSEN"),
            ("FORCED", "CONDITIONAL"), ("UNSTATED", "UNSTATED"), ("partly stated", "UNSTATED"))


def register():
    rows, text = {}, (ROOT / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8")
    for line in text.split("\n"):
        if re.match(r"^\| P-\d+ \|", line):
            c = line.split(" | ")
            rows[c[0][2:]] = c[4] if len(c) == 7 else "?"
    debts, cls = [], None
    a = text.index("## The debts, by load")
    b = text.index("\n## ", a + 10)
    for line in text[a:b].split("\n"):
        if line.startswith("*") and line.rstrip().endswith("*"):
            cls = line.strip("* :").rstrip(":")
        m = re.match(r"^(\d+)\. (P-\d+) — (.*)$", line)
        if m:
            debts.append((int(m.group(1)), m.group(2), cls, m.group(3)))
    return rows, debts


def build():
    fails, notes = [], []
    nodes = [dict(n) for n in S.NODES]
    edges = [dict(e) for e in S.EDGES]
    # ---- the scoreboard's joints
    sb = json.loads((ROOT / "docs" / "total_inputs_scoreboard.json").read_text(encoding="utf-8"))
    page = main_text("docs/TOTAL_INPUTS_SCOREBOARD.md")
    obs = sb["observables"]

    claims_a = set(sb["frames"]["A"]["claims"])

    def joint(prefix, j, layer, frame):
        typ = j["type"]
        grade = "CONDITIONAL" if typ == "FORCED-BY-MAIN" else typ
        row = norm("| %s | %s | %s |" % (j["id"], j["name"], typ))
        if row not in page:
            fails.append("scoreboard row not printed: %s" % j["id"])
        # the scoreboard's own rule: a joint feeds the rows of the frame's CLAIMS that its `feeds` list names
        fed = [obs[i - 1] for i in sorted(set(j.get("feeds", [])) & claims_a)]
        fed_public = [o for o in fed if "firewalled" not in o]
        nodes.append(dict(id="%s:%s" % (prefix, j["id"]), layer=layer, kind="joint", grade=grade, text=j["name"] + ".",
                          pins=[["docs/TOTAL_INPUTS_SCOREBOARD.md", "| %s | %s | %s |" % (j["id"], j["name"], typ)]],
                          rows=re.findall(r"P-\d+", j.get("register", "") or ""), arcs=[], note="",
                          scoreboard_type=typ, rows_fed=len(fed), rows_fed_names=fed_public, same_as=j.get("same_as", ""), frame=frame))
    for j in sb["shared_block"]:
        joint("S", j, "5 values", "shared")
    for j in sb["frames"]["A"]["joints"]:
        joint("A", j, "5 values", "A")
    for j in sb["frames"]["B"]["joints"]:
        if j["type"] == "FORCED-BY-MAIN":
            joint("FA", j, "5 values", "main's frame, as used by frame B")
    bj = sb["frames"]["B"]["joints"]
    # the scoreboard counts a joint as borrowed when it feeds at least one claimed row; the shared block is included
    claims_b = set(sb["frames"]["B"]["claims"])
    bcount = collections.Counter(j["type"] for j in bj if set(j.get("feeds", [])) & claims_b) + collections.Counter(j["type"] for j in sb["shared_block"])
    borrowed_b = sum(v for k, v in bcount.items() if k not in ("FORCED-BY-MAIN", "VERIFIED-BY-MAIN"))
    nodes.append(dict(id="B:FRAME", layer="5 values", kind="reading", grade="LANE-PROPOSED",
                      text="The agy lane's complete picture claims 23 rows on %d borrowed joints, %d of them refuted on main; none certified by the lane's own counter." % (borrowed_b, bcount.get("REFUTED", 0)),
                      pins=[["docs/TOTAL_INPUTS_SCOREBOARD.md", "**Borrowed joints: %d**" % borrowed_b], ["docs/TOTAL_INPUTS_SCOREBOARD.md", "0 certified by the lane's own counter"]],
                      rows=["P-624", "P-661"], arcs=["B1832"], note="", by_type=dict(bcount)))
    for n in list(nodes):
        if n["id"].startswith(("A:", "S:")):
            edges.append(dict(src="V:SIX", kind="requires", dst=n["id"], grade=n["grade"], note=""))
        if n["id"].startswith("FA:") and n["id"] in ("FA:F1", "FA:F2", "FA:F3", "FA:F4"):
            edges.append(dict(src="V:SIX", kind="requires", dst=n["id"], grade="CONDITIONAL", note="main's frame as banked, conditional on its own givens"))
    # ---- the framing ledger's rows (docs/FRAMING_LEDGER.md): each commitment, with the ledger's own status
    for line in (ROOT / "docs" / "FRAMING_LEDGER.md").read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^\| (\**)(FL-(\d+))\** \| ", line)
        if not m:
            continue
        c = line.split(" | ")
        if len(c) != 6:
            fails.append("framing ledger row %s is not six cells" % m.group(2))
            continue
        cell = c[2]
        hits = sorted((cell.find(w), g) for w, g in FL_WORDS if w in cell)
        if not hits:
            fails.append("framing ledger row %s: no status keyword in '%s'" % (m.group(2), cell[:50]))
            continue
        text = c[1].strip("*")
        text = text if len(text) <= 240 else text[:240].rsplit(" ", 1)[0] + " …"
        nodes.append(dict(id="FL:%02d" % int(m.group(3)), layer="12 framing", kind="framing", grade=hits[0][1], text=text,
                          pins=[["docs/FRAMING_LEDGER.md", "| %s%s%s | " % (m.group(1), m.group(2), m.group(1))]],
                          rows=[], arcs=["B1827"], note="", status_cell=norm(cell)[:110], excludes=norm(c[3])[:200]))
    for a, b in S.FL_BEARS_ON.items():
        edges.append(dict(src=a, kind="bears-on", dst=b, grade="", note=""))
    # ---- the register: live dispositions and the ranked debts
    rows, debts = register()
    for n in nodes:
        live = {}
        for r in n["rows"]:
            if r not in rows:
                fails.append("%s cites %s, which is not a register row" % (n["id"], r))
            else:
                live[r] = rows[r]
        n["rows_live"] = live
    for rank, pid, cls, why in debts:
        nodes.append(dict(id="P:" + pid[2:], layer="15 debts", kind="debt", grade="DEBT", text=why, pins=[["docs/POINT_REGISTER.md", ". %s — " % pid]],
                          rows=[pid], arcs=[], note="", rank=rank, debt_class=cls, rows_live={pid: rows.get(pid, "?")}))
        if pid in S.DEBT_BEARS_ON:
            edges.append(dict(src="P:" + pid[2:], kind="bears-on", dst=S.DEBT_BEARS_ON[pid], grade="DEBT", note=""))
    for pid in S.DEBT_BEARS_ON:
        if pid not in {d[1] for d in debts}:
            notes.append("%s is named in DEBT_BEARS_ON and is no longer an open debt" % pid)
    # ---- weave or thread: every node of the spine carries the label (THE WEAVE's test)
    for n in nodes:
        if n["id"] in S.WT:
            n["weave_or_thread"] = S.WT[n["id"]]
        elif n["id"].startswith(("A:", "S:", "FA:", "B:")):
            n["weave_or_thread"] = "thread"            # a value frame is a thread instrument at one address
        elif n["kind"] in ("debt", "duty", "closure", "framing"):
            n["weave_or_thread"] = "n/a"
        else:
            fails.append("%s has no weave-or-thread label" % n["id"])
    lab = {n["id"]: n.get("weave_or_thread") for n in nodes}
    grade_of = {n["id"]: n["grade"] for n in nodes}
    for e in edges:
        # DERIVED means proved outright: such a node may not REQUIRE anything that is not itself proved outright.
        # A theorem that the programme uses under a premise carries an `applies-under` edge to it (Review 77, the reader)
        if e["kind"] == "requires" and grade_of.get(e["src"]) == "DERIVED" and grade_of.get(e["dst"]) != "DERIVED":
            fails.append("a DERIVED node requires a node that is not DERIVED: %s requires %s (%s)" % (e["src"], e["dst"], grade_of.get(e["dst"])))
        # a result stated about the weave may not rest on a thread: that is the thread-for-weave substitution
        if e["kind"] in ("requires", "applies-under") and lab.get(e["src"]) == "weave" and lab.get(e["dst"]) in ("thread", "list") \
                and grade_of[e["src"]] in ("DERIVED", "CONDITIONAL", "NEGATIVE"):
            fails.append("a weave result rests on a thread: %s requires %s" % (e["src"], e["dst"]))
    # a conditional result names what it is conditional on (B1861's builder found eight that did not)
    has_premise = {e["src"] for e in edges if e["kind"] in ("requires", "applies-under")}
    for n in nodes:
        if n["grade"] in ("CONDITIONAL", "READING") and n["id"] not in has_premise:
            fails.append("a conditional result names no premise: %s" % n["id"])
    # ---- checks
    ids = [n["id"] for n in nodes]
    for i, c in collections.Counter(ids).items():
        if c > 1:
            fails.append("node id repeats: %s" % i)
    idset = set(ids)
    for e in edges:
        for end in (e["src"], e["dst"]):
            if end not in idset:
                fails.append("edge end missing: %s (%s %s %s)" % (end, e["src"], e["kind"], e["dst"]))
    cells = genesis_cells()
    for n in nodes:
        if n["id"].startswith("G:") and n["id"][2:] in cells:
            cell = cells[n["id"][2:]]
            n["genesis_status_cell"] = norm(cell)[:90]
            words = GRADE_WORDS.get(n["grade"])
            if words and not any(w in cell[:140] for w in words):
                fails.append("%s: curated grade %s is not GENESIS's status cell '%s'" % (n["id"], n["grade"], norm(cell)[:60]))
    checked_main = checked_seat = unavailable = 0
    for n in nodes:
        if n["kind"] not in ("closure",) and not n["pins"]:
            fails.append("%s has no pin" % n["id"])
        for p in n["pins"]:
            if len(p) == 2:
                t = main_text(p[0])
                if t is None:
                    fails.append("%s: file missing %s" % (n["id"], p[0]))
                elif norm(p[1]) not in t:
                    fails.append("%s: quote not found in %s: %s" % (n["id"], p[0], p[1][:70]))
                checked_main += 1
            else:
                if re.search(r"\d", p[2]):
                    fails.append("%s: a seat quote must be digit-free: %s" % (n["id"], p[2][:60]))
                t = seat_text(p[0], p[1])
                if t == "UNAVAILABLE":
                    unavailable += 1
                elif t is None:
                    fails.append("%s: no such file at %s: %s" % (n["id"], p[0], p[1]))
                elif norm(p[2]) not in t:
                    fails.append("%s: seat quote not found at %s:%s: %s" % (n["id"], p[0], p[1], p[2][:70]))
                else:
                    checked_seat += 1
    for x in S.QUEUE:
        if x not in idset:
            fails.append("QUEUE names %s, not a node" % x)
        for line in S.QUEUE[x]["known"] + [S.QUEUE[x]["closes"]]:
            for ref in re.findall(r"\(([A-Z]+:[A-Z0-9a-z\-]+(?:, [A-Z]+:[A-Z0-9a-z\-]+)*)\)", line):
                for r in ref.split(", "):
                    if r not in idset:
                        fails.append("QUEUE %s refers to %s, not a node" % (x, r))
    # ---- the closure nodes' loads
    by_id = {n["id"]: n for n in nodes}
    for n in nodes:
        if n["kind"] == "closure":
            members = sorted(e["src"] for e in edges if e["kind"] == "instance-of" and e["dst"] == n["id"])
            duties = sorted(e["dst"] for e in edges if e["kind"] == "blocks" and e["src"] == n["id"])
            fed = sorted({o for m in members for o in by_id[m].get("rows_fed_names", [])})
            n["members"], n["duties_blocked"], n["value_rows_fed"] = members, duties, fed
            n["member_grades"] = dict(collections.Counter(by_id[m]["grade"] for m in members))
    nodes.sort(key=lambda n: (int(n["layer"].split()[0]), n["id"]))
    edges.sort(key=lambda e: (e["src"], e["kind"], e["dst"]))
    stats = dict(nodes=len(nodes), edges=len(edges), by_grade=dict(sorted(collections.Counter(n["grade"] for n in nodes).items())),
                 by_layer=dict(sorted(collections.Counter(n["layer"] for n in nodes).items(), key=lambda kv: int(kv[0].split()[0]))),
                 pins_checked_on_main=checked_main, pins_checked_on_seat_branches=checked_seat, seat_pins_unavailable_in_this_clone=unavailable,
                 register_rows_cited=len({r for n in nodes for r in n["rows"]}), open_debts=len(debts),
                 weave_or_thread=dict(sorted(collections.Counter(n.get("weave_or_thread", "?") for n in nodes).items())))
    return nodes, edges, stats, fails, notes, rows


GRADE_ORDER = ["DERIVED", "CONDITIONAL", "RECORD", "CONFIRMED", "POSTULATED", "TAGGED", "CHOSEN", "UNSTATED", "FITTED", "ANSATZ", "READING", "NEGATIVE", "OPEN", "LANE-REVIEWED",
               "LANE-PROPOSED", "LANE-INPUT", "DUTY", "DEBT", "CLOSURE"]


def where(n):
    out = []
    for p in n["pins"][:1]:
        out.append(p[0] if len(p) == 2 else "%s @ %s" % (p[1].split("/")[-1], p[0]))
    out += n["arcs"][:3]
    out += ["%s (%s)" % (r, n.get("rows_live", {}).get(r, "?")) for r in n["rows"][:3]]
    return "; ".join(out)


def render_map(nodes, edges, stats):
    L = ["# THE CLOSURE MAP — every claim, premise and choice, with its grade and its source",
         "",
         "*Generated by `verification/build_map.py` from `verification/map_source.py` and the record. Do not edit by hand.*",
         "*Documentary: nothing here is a new result, and no held-out value is read or written. Every row's source is pinned",
         "by a quote that the builder checks.*",
         "",
         "## The grades",
         "",
         "| grade | meaning | nodes |",
         "|---|---|---|"]
    meaning = {"DERIVED": "held on the record as proved outright (the map checks the citation, not the proof)",
               "CONDITIONAL": "proved given named premises, a tag or a numerical identification",
               "RECORD": "a fact about the record's own state, checked at its source", "POSTULATED": "assumed by the foundation",
               "TAGGED": "a tagged working postulate (the owner's ruling)", "CHOSEN": "a fork settled by choice, the alternative kept",
               "FITTED": "a continuous input fixed by looking at data", "ANSATZ": "a posited form with no derivation",
               "READING": "passes a sealed screen; not a prediction", "UNSTATED": "a commitment the construction makes without stating it",
               "CONFIRMED": "a registered falsifiable claim that observation has confirmed", "NEGATIVE": "a banked negative, scoped", "OPEN": "not settled",
               "LANE-REVIEWED": "a seat's proof with a non-authoring review inside its lane; not verified on main",
               "LANE-PROPOSED": "a seat's hand proof, count or estimate, unreviewed; not verified on main",
               "LANE-INPUT": "an input the seat's own ledger prices as supplied, unselected or unearned",
               "DUTY": "something the full goal requires and nobody has done", "DEBT": "a result the record uses is owed a check or a correction",
               "CLOSURE": "one missing dependency under several names"}
    for g in GRADE_ORDER:
        if g in stats["by_grade"]:
            L.append("| %s | %s | %d |" % (g, meaning[g], stats["by_grade"][g]))
    layers = collections.OrderedDict()
    for n in nodes:
        layers.setdefault(n["layer"], []).append(n)
    titles = {"0": "The principle", "1": "The grammar", "2": "The states and the root", "3": "The weave, its forks and its gaps",
              "4": "The structural theorem (the McKay cascade on the root)", "5": "The values (the scoreboard's two frames)",
              "6": "The modulus and its read-out", "7": "The scale", "8": "The lanes' conditional model (E₈ on the punctured elliptic curve)",
              "9": "Gravity", "10": "Cosmology", "11": "Predictions and falsifiers", "12": "The framing ledger's commitments",
              "13": "The completion duties (the physical lane's checklist)",
              "14": "The closure nodes", "15": "The register's open debts"}
    for layer, ns in layers.items():
        k = layer.split()[0]
        L += ["", "## %s. %s" % (k, titles.get(k, layer)), ""]
        if k == "14":
            L += ["| id | what it is | members | duties blocked |", "|---|---|---|---|"]
            for n in ns:
                L.append("| %s | %s | %d | %s |" % (n["id"], n["text"], len(n["members"]), ", ".join(n["duties_blocked"])))
        elif k == "15":
            L += ["| rank | row | class | what rests on it |", "|---|---|---|---|"]
            for n in sorted(ns, key=lambda n: n["rank"]):
                L.append("| %d | %s | %s | %s |" % (n["rank"], n["rows"][0], n["debt_class"], n["text"].replace("|", "∣")))
        else:
            L += ["| id | grade | about | statement | where |", "|---|---|---|---|---|"]
            for n in ns:
                L.append("| %s | %s | %s | %s | %s |" % (n["id"], n["grade"], n.get("weave_or_thread", ""), n["text"].replace("|", "∣"), where(n).replace("|", "∣")))
    return "\n".join(L) + "\n"


def render_queue(nodes, edges, stats, rows):
    by_id = {n["id"]: n for n in nodes}
    xs = [n for n in nodes if n["kind"] == "closure"]
    xs.sort(key=lambda n: (-len(n["duties_blocked"]), -len(n["value_rows_fed"]), -len(n["members"]), n["id"]))
    L = ["# THE CLOSURE QUEUE — what is missing, under every name it has, in the order of what it blocks",
         "",
         "*Generated by `verification/build_map.py`. The order is mechanical: duties blocked, then value rows fed, then members.*",
         "*It ranks what is missing. It does not say what is easiest.*",
         "",
         "## The missing dependencies",
         "",
         "| rank | node | duties blocked | value rows fed | members | grades of its members |",
         "|---|---|---|---|---|---|"]
    for i, n in enumerate(xs, 1):
        mg = ", ".join("%s %d" % (g, n["member_grades"][g]) for g in GRADE_ORDER if g in n["member_grades"])
        L.append("| %d | %s | %d | %d | %d | %s |" % (i, n["id"], len(n["duties_blocked"]), len(n["value_rows_fed"]), len(n["members"]), mg))
    for i, n in enumerate(xs, 1):
        q = S.QUEUE[n["id"]]
        L += ["", "### %d. %s" % (i, n["text"]), "", "- **What the record knows:**"]
        L += ["  - " + k for k in q["known"]]
        L += ["- **What would close it:** " + q["closes"],
              "- **Who holds it now:** " + q["owner"] + ".",
              "- **Owed on main:** " + q["duty"] + ".",
              "- **Blocks:** " + ", ".join("%s (%s)" % (d, by_id[d]["text"].split(":")[0]) for d in n["duties_blocked"]) + ".",
              "- **Under these names:** " + ", ".join(n["members"]) + "."]
    # what each headline result rests on: the transitive closure of "requires"
    req = collections.defaultdict(list)
    for e in edges:
        if e["kind"] in ("requires", "applies-under"):
            req[e["src"]].append(e["dst"])
    L += ["", "## What each headline result rests on", "",
          "*Everything upstream of a result along the map's \"requires\" and \"applies-under\" edges, by grade. As physics, a result is as derived as the weakest thing under it.*", "",
          "| result | its own grade | upstream, by grade | not derived, by name |", "|---|---|---|---|"]
    for hid, label in S.HEADLINES:
        seen, stack = set(), list(req[hid])
        while stack:
            x = stack.pop()
            if x not in seen:
                seen.add(x); stack += req[x]
        cnt = collections.Counter(by_id[x]["grade"] for x in seen)
        weak = sorted(x for x in seen if by_id[x]["grade"] not in ("DERIVED", "CONDITIONAL", "RECORD"))
        L.append("| %s — %s | %s | %s | %s |" % (hid, label, by_id[hid]["grade"],
                 ", ".join("%s %d" % (g, cnt[g]) for g in GRADE_ORDER if g in cnt), ", ".join(weak)))
    # weave or thread: what the banked results are stated about
    banked = [n for n in nodes if n["grade"] in ("DERIVED", "CONDITIONAL", "NEGATIVE", "READING") and n.get("weave_or_thread") in ("weave", "thread", "list")]
    L += ["", "## Weave or thread: what the banked results are stated about", "",
          "*THE WEAVE's test (docs/THE_WEAVE.md): a weave result is defined by the joint action of every allowed move, or stated about every thread at once.*",
          "*A thread result is read on one thread, one fibre, one point or one background. A list is a family examined member by member.*",
          "*The builder refuses a weave result that rests on a thread.*", "",
          "| stated about | banked results | which |", "|---|---|---|"]
    for w in ("weave", "thread", "list"):
        ns = [n for n in banked if n["weave_or_thread"] == w]
        L.append("| %s | %d | %s |" % (w, len(ns), ", ".join("%s (%s)" % (n["id"], n["grade"].lower()) for n in ns)))
    L += ["", "| headline result | stated about |", "|---|---|"]
    for hid, label in S.HEADLINES:
        L.append("| %s — %s | %s |" % (hid, label, by_id[hid].get("weave_or_thread")))
    nx = S.NEXT
    L += ["", "## The one next unowned derivation", "", "**%s.**" % nx["title"], ""]
    L += ["- " + s for s in nx["statement"]]
    L += ["- **The three outcomes, stated before computing:**"] + ["  - " + o for o in nx["outcomes"]]
    L += ["- **Why this one:** " + nx["why"], "- **Owner:** " + nx["owner"]]
    L += ["", "## The verification queue (the lanes' work not yet verified on main)", "", "| row | now | what |", "|---|---|---|"]
    reg = (ROOT / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8")
    for pid in ("P-746", "P-747", "P-749", "P-750", "P-752", "P-739", "P-744"):
        m = re.search(r"^\| %s \| [^|]+ \| [^|]+ \| (.*?) \| (DONE|QUEUED|LEAD|OWNER|DECLINED) \| " % re.escape(pid), reg, re.M)
        if m:
            head = m.group(1)
            head = head[:head.index(" (")] if " (" in head[:140] else head[:140]
            L.append("| %s | %s | %s |" % (pid, m.group(2), head.replace("|", "∣")))
    debts = [n for n in nodes if n["kind"] == "debt"]
    L += ["", "## The register's open debts, by class (%d)" % len(debts), "", "| class | debts | the first by load |", "|---|---|---|"]
    cls = collections.OrderedDict()
    for n in sorted(debts, key=lambda n: n["rank"]):
        cls.setdefault(n["debt_class"], []).append(n)
    for c, ns in cls.items():
        L.append("| %s | %d | %s: %s |" % (c, len(ns), ns[0]["rows"][0], ns[0]["text"][:150].replace("|", "∣")))
    return "\n".join(L) + "\n"


def main():
    nodes, edges, stats, fails, notes, rows = build()
    print(json.dumps(stats, indent=1, ensure_ascii=False))
    for n in notes:
        print("NOTE", n)
    if fails:
        print("FAILURES (%d):" % len(fails))
        for f in fails:
            print("  " + f)
        return 1
    if "--write" in sys.argv:
        (ARC / "NODES.json").write_text(json.dumps(nodes, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        (ARC / "EDGES.json").write_text(json.dumps(edges, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        (ARC / "MAP.md").write_text(render_map(nodes, edges, stats), encoding="utf-8")
        (ARC / "CLOSURE_QUEUE.md").write_text(render_queue(nodes, edges, stats, rows), encoding="utf-8")
        print("written: NODES.json, EDGES.json, MAP.md, CLOSURE_QUEUE.md")
    print("ALL PINS CHECK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
