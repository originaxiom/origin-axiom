#!/usr/bin/env python3
"""How far the record is from the final reading, read from main's OWN generated files at a commit.

Nothing is typed here.  Every number is taken from files that main's builders write and its gates compare with those
builders: the closure programme's data (B1861), the closure map (B1858) and the scoreboard's data file.  The one number
that is this seat's is the count of planted violations caught, taken from the seat's last run on main.

    python3 relays/advisor_2026-11-10_audit/tools/where_we_stand.py [--ref origin/main]

Read-only.  Standard library."""
import sys, os, re, json, glob, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
ref = sys.argv[sys.argv.index("--ref") + 1] if "--ref" in sys.argv else "origin/main"


def show(path):
    r = subprocess.run(["git", "-C", REPO, "show", "%s:%s" % (ref, path)], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


sha = subprocess.run(["git", "-C", REPO, "rev-parse", "--short=9", ref], capture_output=True, text=True).stdout.strip()
prog = show("frontier/B1861_the_closure_programme/PROGRAMME.json")
if prog is None: sys.exit("%s (%s) has no closure programme: nothing to read" % (ref, sha))
P = json.loads(prog); st = P["stats"]; pk = P["packages"]; pk = list(pk.values()) if isinstance(pk, dict) else pk
nodes = json.loads(show("frontier/B1858_the_closure_map/NODES.json") or "[]")
sb = show("docs/TOTAL_INPUTS_SCOREBOARD.md") or ""
m = re.search(r"(\d+) of (\d+) earned", sb); earned = "%s of %s" % m.groups() if m else "not found"


def tally(ps):
    d = sum(p["status"].startswith("DONE") for p in ps); s = sum(p["status"].startswith("STARTED") for p in ps)
    return d, s, len(ps) - d - s
def line(label, value): print("   %-52s %s" % (label, value))
def state(pid):
    p = next((p for p in pk if p["id"] == pid), None); return "%s  (%s)" % (p["status"], p["title"]) if p else "not in the programme"
by_ob = {}
for p in pk: by_ob.setdefault(str(p.get("obligation")), []).append(p)
ob = lambda *names: [p for n in names for p in by_ob.get(n, [])]

print("WHERE THE RECORD STANDS, read from main's own generated files at %s (%s)\n" % (ref, sha))
print("1. THE FINAL READING: a sealed prediction set beside measurement")
line("values earned (the scoreboard's line)", earned)
card = next((p for p in pk if "sealed card" in p["title"].lower()), None)
comp = next((p for p in pk if "comparison" in p["title"].lower()), None)
if card: line("the sealed card (%s)" % card["id"], card["status"])
if comp: line("calibration and comparison (%s)" % comp["id"], comp["status"])
wait = st.get("packages_the_sealed_card_must_wait_on_for_that", [])
if wait:
    d, s, n = tally([p for p in pk if p["id"] in wait])
    line("hygiene packages the card must wait on", "%d: done %d, started %d, not started %d" % (len(wait), d, s, n))
m1 = [p for p in pk if p["id"] == "WP-0.6"]; m2 = ob("C0", "C1", "C2", "C3", "C4"); m3 = ob("C5")
line("milestone 1, the dependency map is complete", "%d of %d packages done" % (tally(m1)[0], len(m1)))
line("milestone 2, the physical construction is verified", "%d of %d" % (tally(m2)[0], len(m2)))
line("milestone 3, the predictions are ready for comparison", "%d of %d" % (tally(m3)[0], len(m3)))

print("\n2. THE WORK ORDER")
d, s, n = tally(pk)
line("packages", "%d: done %d, started %d, not started %d; with no owner %d" % (len(pk), d, s, n, len(st.get("unowned", []))))
for name in sorted(by_ob):
    d, s, n = tally(by_ob[name]); line("   obligation %s" % name, "%2d: done %d, started %d, not started %d" % (len(by_ob[name]), d, s, n))
line("nodes of the map that still need a path", "%s of %s" % (st.get("nodes_needing_a_path"), st.get("map_nodes", len(nodes))))
line("debts on the map", "%s (joined to nothing: %s)" % (st.get("debts"), st.get("debts_on_the_map_joined_to_nothing")))

print("\n3. WHAT IS STILL PUT IN BY HAND")
b = st.get("budget", {})
line("independent choices on main's spine", "%s, which are %s items: %s" % (st.get("independent_choices"), st.get("budget_items"), ", ".join("%s %s" % (v, k) for k, v in sorted(b.items()))))
line("supplied in addition by the lanes' model", st.get("lanes_supplied_inputs"))
line("inputs with an exit on the table", st.get("inputs_with_an_exit_on_the_table"))
oc = st.get("open_choices_under_each_conditional_headline", {})
line("headline results that are conditional", "%d: %s" % (len(oc), ", ".join("%s on %s open choices" % kv for kv in sorted(oc.items()))))
line("conditional results in all", st.get("conditional_results"))

print("\n4. THE AUDIT OF 2026-11-10 (%s findings)" % st.get("audit_findings"))
f = st.get("audit_findings_by_state", {})
line("by main's state", ", ".join("%s %s" % (k.lower(), v) for k, v in sorted(f.items(), key=lambda kv: -kv[1])))
line("with a verdict of the re-audit", st.get("findings_with_a_re_audit_verdict"))
line("fixed and not yet re-audited, by main's file", ", ".join(st.get("fixed_and_not_yet_re_audited", [])) or "none")
outs = sorted(glob.glob(os.path.join(HERE, "planted_violations_main_*_out.txt")), key=os.path.getmtime)
if outs:
    t = open(outs[-1], encoding="utf-8").read(); nc = re.search(r"NOT CAUGHT: (\d+)", t)
    auto = len(re.findall(r"^PV\d+\s+\S+\s+(?:CAUGHT|NOT CAUGHT)", t, flags=re.M))
    if nc and auto: line("planted violations caught (this seat's last run on main)", "%d of %d  (%s)" % (auto - int(nc.group(1)), auto, os.path.basename(outs[-1])))

print("\n5. THE SCOREBOARD ITSELF")
wp = next((p for p in pk if "count as an output" in p["title"].lower()), None)
if wp: line("%s, %s" % (wp["id"], wp["title"].lower()), wp["status"])
line("the map and the programme", "generated; a gate compares them with their builders")
line("the headline count", "printed from a typed data file; not yet computed from a value's ancestry")
