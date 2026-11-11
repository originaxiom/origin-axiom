#!/usr/bin/env python3
"""One snapshot of where the record stands, for a scoreboard page.  Nothing is typed here.

Every table is read from four files on main at the commit named.  Main's builders write three of them and its gates
compare each with its builder: the closure programme's data (B1861) and the closure map's nodes and edges (B1858).  The
fourth is the scoreboard's data file, which main types and a gate compares with its page.  The one table that is this
seat's own is the planted-violation run, read from the seat's output file; the commit it was run on is carried beside
it.

The relations are main's as well: what each package needs, what each value's joints are, and every edge of the map.

    python3 relays/advisor_2026-11-10_audit/scoreboard/scoreboard_snapshot.py [--ref origin/main] --out FILE

The script refuses to write if main's files do not add up: a grade of the map it does not know, or a count of nodes that
still need a path that is not main's own.  Read-only on the repository.  Standard library."""
import sys, os, re, json, glob, subprocess, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
ref = sys.argv[sys.argv.index("--ref") + 1] if "--ref" in sys.argv else "origin/main"
out = sys.argv[sys.argv.index("--out") + 1]


def git(*a):
    r = subprocess.run(["git", "-C", REPO, *a], capture_output=True, text=True)
    if r.returncode != 0: sys.exit("git %s failed: %s" % (" ".join(a), r.stderr.strip()[:200]))
    return r.stdout


def show(path): return git("show", "%s:%s" % (ref, path))


sha = git("rev-parse", "--short=9", ref).strip(); committed = git("log", "-1", "--format=%cI", ref).strip()
P = json.loads(show("frontier/B1861_the_closure_programme/PROGRAMME.json")); st = P["stats"]
N = json.loads(show("frontier/B1858_the_closure_map/NODES.json"))
E = json.loads(show("frontier/B1858_the_closure_map/EDGES.json"))
SB = json.loads(show("docs/total_inputs_scoreboard.json"))
pk = P["packages"]; pk = list(pk.values()) if isinstance(pk, dict) else pk

# ---- the map: main's grades, sorted the way main's own page sorts them
STATE = {"DERIVED": "settled", "NEGATIVE": "settled", "CONFIRMED": "settled", "RECORD": "settled",
         "CONDITIONAL": "conditional", "READING": "conditional",
         "POSTULATED": "put in", "CHOSEN": "put in", "FITTED": "put in", "ANSATZ": "put in", "TAGGED": "put in", "LANE-INPUT": "put in",
         "OPEN": "open", "UNSTATED": "open", "LANE-PROPOSED": "open", "LANE-REVIEWED": "open", "DUTY": "open",
         "DEBT": "debt", "CLOSURE": "grouping"}
unknown = sorted({n["grade"] for n in N} - set(STATE))
if unknown: sys.exit("refused: the map has grades this script does not know: %s" % ", ".join(unknown))
need = sum(STATE[n["grade"]] in ("put in", "open") for n in N)
if need != st["nodes_needing_a_path"]: sys.exit("refused: %d nodes sort as needing a path; main's builder says %d" % (need, st["nodes_needing_a_path"]))
if sum(STATE[n["grade"]] == "conditional" for n in N) != st["conditional_results"]: sys.exit("refused: the conditional results do not add up to main's count")
short = lambda s, n=230: s if len(s) <= n else s[:n - 1].rstrip() + "…"
nodes = [{"id": n["id"], "layer_no": int(n["layer"].split()[0]), "layer": n["layer"].split(" ", 1)[1], "kind": n["kind"], "grade": n["grade"],
          "state": STATE[n["grade"]], "text": short(n["text"])} for n in N]
byid = {n["id"]: n for n in N}
if len(byid) != len(N): sys.exit("refused: two nodes of the map share an id")
if any(e["src"] not in byid or e["dst"] not in byid for e in E): sys.exit("refused: an edge of the map names a node that is not on it")
edges = [{"src": e["src"], "kind": e["kind"], "dst": e["dst"], "grade": e.get("grade", ""), "note": short(e.get("note", ""), 160)} for e in E]

# ---- the packages and the milestones
state_of = lambda s: "done" if s.startswith("DONE") else ("started" if s.startswith("STARTED") else "not started")
waits = set(st.get("packages_the_sealed_card_must_wait_on_for_that", []))
last = [p for p in pk if str(p.get("obligation")) == "C6"]
if len(last) != 1: sys.exit("refused: the comparison is not one package")
under = set(last[0].get("rests_on", []))
pids = {p["id"] for p in pk}
if not under <= pids or any(not set(p.get("needs_all", [])) <= pids for p in pk): sys.exit("refused: a package needs one that is not in the programme")
packages = [{"id": p["id"], "title": p["title"], "wave": int(p["wave"]), "obligation": str(p.get("obligation")), "status": p["status"], "state": state_of(p["status"]),
             "owner": p.get("owner", ""), "intent": str(p.get("intent", "")).lower(), "question": short(p.get("question", ""), 240),
             "waits": p["id"] in waits, "before_the_reading": p["id"] in under, "needs": " ".join(p.get("needs_all", [])),
             "accept": short(p.get("accept", ""), 320), "nodes": len(p.get("nodes", [])),
             "findings": len(p.get("findings", [])), "debts": len(p.get("debts", []))} for p in pk]


def tally(ps):
    return {"done": sum(p["state"] == "done" for p in ps), "started": sum(p["state"] == "started" for p in ps),
            "not_started": sum(p["state"] == "not started" for p in ps), "total": len(ps)}
ob = lambda *names: [p for p in packages if p["obligation"] in names]
milestones = [dict(key="M1", name="The dependency map is complete", **tally([p for p in packages if p["id"] == "WP-0.6"])),
              dict(key="M2", name="The physical construction is verified", **tally(ob("C0", "C1", "C2", "C3", "C4"))),
              dict(key="M3", name="The predictions are ready for comparison", **tally(ob("C5"))),
              dict(key="C6", name="Calibration and comparison: the final reading", **tally(ob("C6")))]
if sum(m["total"] for m in milestones[1:]) != len(packages): sys.exit("refused: the obligations C0 to C6 do not cover the packages")
card = next((p for p in packages if "sealed card" in p["title"].lower()), None); comp = next((p for p in packages if "comparison" in p["title"].lower()), None)

# ---- the values main's scoreboard lists, and what each frame says of them
A, B = SB["frames"]["A"], SB["frames"]["B"]


def frame_says(F, i):
    if i in F.get("claims", []): return "claimed"
    if i in F.get("held_out", []): return "held out, sealed"
    if i in F.get("graded_input", []): return "graded an input"
    if i in F.get("no_frame", []): return "no frame"
    return "not claimed"
m = re.search(r"(\d+) of (\d+) earned", show("docs/TOTAL_INPUTS_SCOREBOARD.md")); earned, of = int(m.group(1)), int(m.group(2))
if earned != SB["earned"]: sys.exit("refused: the scoreboard's page and its data file disagree on what is earned")
number = {name: i for i, name in enumerate(SB["observables"], 1)}
ORDER = ["put in", "conditional", "open", "settled", "debt", "grouping"]
value_joints = []
for n in N:
    fed = n.get("rows_fed_names") or []
    if fed and n.get("rows_fed") != len(fed): sys.exit("refused: %s feeds %s values by its count and %d by name" % (n["id"], n.get("rows_fed"), len(fed)))
    for name in fed:
        if name not in number: sys.exit("refused: %s feeds a value the scoreboard does not list: %s" % (n["id"], name))
        value_joints.append({"n": number[name], "value": name, "joint": n["id"], "grade": n["grade"].lower(), "state": STATE[n["grade"]],
                             "frame": n.get("frame", ""), "text": short(n["text"], 170)})
value_joints.sort(key=lambda r: (r["n"], ORDER.index(r["state"]), r["joint"]))
per = lambda i, state: sum(r["n"] == i and r["state"] == state for r in value_joints)
values = [{"n": i, "name": name, "part": "the nineteen" if i <= of else "listed beyond the nineteen", "earned": "no" if SB["earned"] == 0 else "see main",
           "candidate": frame_says(A, i), "lanes_picture": frame_says(B, i), "joints": sum(r["n"] == i for r in value_joints),
           "joints_put_in": per(i, "put in"), "joints_conditional": per(i, "conditional"), "joints_open": per(i, "open"), "joints_settled": per(i, "settled")}
          for i, name in enumerate(SB["observables"], 1)]

# ---- what is still put in by hand
inputs = [{"name": x["name"], "kind": ", ".join(("%d × %s" % (v, k)) if v > 1 else k for k, v in sorted(x["kinds"].items())), "items": sum(x["kinds"].values()),
           "about": " and ".join(x.get("weave_or_thread", [])), "settled_by": ", ".join(x.get("packages", [])), "note": short(x.get("note", ""), 200)} for x in P["inputs"]]
budget = [{"kind": k, "now": v} for k, v in sorted(st["budget"].items(), key=lambda kv: -kv[1])]
if sum(b["now"] for b in budget) != st["budget_items"] or len(inputs) != st["independent_choices"]: sys.exit("refused: the input budget does not add up to main's counts")

# ---- the audit, and the seat's planted cases on this commit
F = P["findings"]
findings = [{"id": k, "short": short(v.get("short", ""), 160), "state": v["state"].lower()} for k, v in sorted(F.items(), key=lambda kv: (re.sub(r"\d+", "", kv[0]), int(re.sub(r"\D", "", kv[0]) or 0)))]
planted, suite_commit = [], ""
for path in sorted(glob.glob(os.path.join(HERE, "..", "tools", "planted_violations_main_*_out.txt"))):
    if sha in os.path.basename(path): suite_commit = sha; text = open(path, encoding="utf-8").read()
if not suite_commit:
    paths = sorted(glob.glob(os.path.join(HERE, "..", "tools", "planted_violations_main_*_out.txt")), key=os.path.getmtime)
    if paths: text = open(paths[-1], encoding="utf-8").read(); suite_commit = re.search(r"main_([0-9a-f]+)_out", os.path.basename(paths[-1])).group(1)
if suite_commit:
    for mm in re.finditer(r"^(PV\d+)\s+(\S+)\s+(CAUGHT|NOT CAUGHT)\s+(.*)$", text, flags=re.M):
        planted.append({"id": mm.group(1), "finding": mm.group(2), "result": mm.group(3).lower(), "what": short(mm.group(4).strip(), 160)})
    planted.sort(key=lambda r: int(r["id"][2:]))

conditional = [{"id": k, "text": short(byid[k]["text"], 200) if k in byid else "", "open_choices": v} for k, v in sorted(st.get("open_choices_under_each_conditional_headline", {}).items(), key=lambda kv: -kv[1])]

state = [{"commit": sha, "committed": committed, "built": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
          "earned": earned, "of": of, "identification_price": SB["identification_price"]["count"],
          "sealed_card": (card["status"].lower() if card else "not in the programme"), "comparison": (comp["status"].lower() if comp else "not in the programme"),
          "choices": st["independent_choices"], "choice_items": st["budget_items"], "lanes_inputs": st["lanes_supplied_inputs"],
          "map_nodes": len(N), "map_edges": len(E), "need_path": need, "conditional_results": st["conditional_results"], "debts": st["debts"],
          "fixed_not_reaudited": len(st["fixed_and_not_yet_re_audited"]), "suite_commit": suite_commit}]
snap = {"state": state, "milestones": milestones, "packages": packages, "values": values, "value_joints": value_joints, "nodes": nodes, "edges": edges,
        "inputs": inputs, "budget": budget, "findings": findings, "planted": planted, "conditional": conditional}
json.dump(snap, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("snapshot of %s (%s): %s" % (ref, sha, ", ".join("%s %d" % (k, len(v)) for k, v in snap.items())))
print("written: %d bytes" % os.path.getsize(out))
