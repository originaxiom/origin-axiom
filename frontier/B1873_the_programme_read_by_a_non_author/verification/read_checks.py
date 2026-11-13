#!/usr/bin/env python3
"""B1873 -- the advisor seat's read of the closure programme as a non-author: its counts recomputed by main from main's own
generated files, before and after the repairs (bookkeeping only; no value is computed).

The read's cause: the seal's rule says nothing open may lie upstream of a value, upstream is read from the map's edges, and
three ledgers were not joined to the map.  This script counts what the read counted, on the programme as it is built now.

    python3 -B frontier/B1873_the_programme_read_by_a_non_author/verification/read_checks.py
"""
import collections
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
say = print
P = json.loads((ROOT / "frontier/B1861_the_closure_programme/PROGRAMME.json").read_text(encoding="utf-8"))
N = {n["id"]: n for n in json.loads((ROOT / "frontier/B1858_the_closure_map/NODES.json").read_text(encoding="utf-8"))}
E = json.loads((ROOT / "frontier/B1858_the_closure_map/EDGES.json").read_text(encoding="utf-8"))
pk = {w["id"]: w for w in P["packages"]}
F = P["findings"]


def upstream(i, seen=None):
    seen = set() if seen is None else seen
    for x in pk[i]["needs_all"]:
        if x not in seen:
            seen.add(x)
            upstream(x, seen)
    return seen


# 1. the debts and the map
debts = [i for i, n in N.items() if n["kind"] == "debt"]
touched = {e["src"] for e in E} | {e["dst"] for e in E}
joined = [d for d in debts if d in touched]
say("1. debts on the map: %d; joined to a node by an edge: %d; joined to nothing: %d (the read, one debt earlier: 79, 17, 62)" % (len(debts), len(joined), len(debts) - len(joined)))
# 2. what the comparison and the sealed card wait on
upc, upk = upstream("WP-6.1"), upstream("WP-5.3")
out6 = sorted(w for w in pk if w not in upc and w != "WP-6.1")
say("2. packages the comparison does not wait on: %s, holding %d findings (the read, before the repair: six packages, 31 findings)" % (out6, sum(1 for f in F.values() if f["wp"] in out6)))
repo = sorted(fid for fid, b in P["bears_on"].items() if "REPOSITORY" in b)
say("   findings that bear on the repository as a whole: %d; every one is in a package upstream of the sealed card: %s" % (len(repo), all(F[fid]["wp"] in upk for fid in repo)))
say("   the sealed card now waits on the suite and on the comparison's own instruments: %s" % ({"WP-0.2", "WP-0.5"} <= set(pk["WP-5.3"]["needs"])))
# 3. started before a need
sb = [(w, x) for w in pk for x in pk[w]["needs_all"] if not pk[w]["status"].startswith("NOT STARTED") and pk[x]["status"].startswith("NOT STARTED")]
say("3. packages marked started while a need has not started: %d %s (the read: five); the same five are now held as given: %s" % (
    len(sb), sb, {k: P["given"][k] for k in ("WP-3.2", "WP-4.1", "WP-4.3")}))
# 4. the findings' fields
fields = sorted({k for f in F.values() for k in f})
say("4. a finding's fields: %s; every finding names what it bears on: %s; with the re-audit's verdict kept apart for %d" % (fields, sorted(P["bears_on"]) == sorted(F), len(P["accepted"])))
by_letter = collections.Counter((fid[0], f["wp"]) for fid, f in F.items())
say("   filed by content and not by the audit's letter: X3 in %s, X4 in %s, W6 and W7 in %s" % (F["X3"]["wp"], F["X4"]["wp"], F["W6"]["wp"]))
# 5. the budget
kinds = collections.Counter()
for i in P["inputs"]:
    for k, v in i["kinds"].items(): kinds[k] += v
ch = next(i for i in P["inputs"] if "charge premise" in i["name"])
say("5. the budget: %d choices, %d items by kind %s; the charge premise at level five is typed %s" % (len(P["inputs"]), sum(kinds.values()), dict(kinds), ch["kinds"]))
ex = collections.Counter(v[0] for v in P["exits"].values())
say("   routes: %s; an exit with no objection on the page: %d (the read: 8, of which 5 are back-edges named and not built)" % (dict(ex), ex["FORCING ARGUED"] + ex["RIGID"] + ex["BACK-EDGE NAMED"]))
# 6. the price script the foundation cites
# CORRECTED 2026-11-13 (Review 81, the SM seat's finding 08): the certificate reads its pages relative to the working
# directory, so it is run from the repository's root; run from this folder it failed differently and item 6 lost its line
r = subprocess.run([sys.executable, "-B", str(ROOT / "outside_bench/certificates/the_price_is_twelve.py")], capture_output=True, text=True, cwd=str(ROOT))
fail = [l.strip() for l in r.stdout.split("\n") if "VERDICT:" in l and "not stated" in l]
used = subprocess.run(["git", "-C", str(ROOT), "grep", "-l", "the_price_is_twelve", "--", "tests", "scripts", ".github"], capture_output=True, text=True).stdout.split()
say("6. the script the foundation cites for the live price exits %d: %s; files under tests, scripts or the workflow that run it: %d" % (r.returncode, fail[0] if fail else "(no failure line)", len(used)))
# 7. what is still not joined
say("7. still not joined to the map, and registered: %d debts with no edge; the identification ledger's unearned rows (one is named on the map); no bit or discrete choice carries its alternatives (fields of an input: %s)" % (
    len(debts) - len(joined), sorted(P["inputs"][0])))
