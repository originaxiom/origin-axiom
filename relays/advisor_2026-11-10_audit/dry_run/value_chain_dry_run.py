#!/usr/bin/env python3
"""Dry run of the value-chain certificate on one arc (default B1841, frame A's row on the inputs scoreboard).
Reads only tracked files. Run from the repository root, after tools/lock_census.py:
    python3 relays/advisor_2026-11-10_audit/dry_run/value_chain_dry_run.py [ARC]
Writes value_chain_<ARC>.json beside itself and prints the summary."""
import json, glob, os, re, sys, collections, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT_ARC = sys.argv[1] if len(sys.argv) > 1 else "B1841"
A, folders = {}, collections.defaultdict(list)
for p in sorted(glob.glob("frontier/B*/arc_verdict.json")):
    d = json.load(open(p)); d["_dir"] = os.path.dirname(p)
    folders[d["id"]].append(d["_dir"]); A.setdefault(d["id"], d)
census = json.load(open(os.path.join(HERE, "..", "tools", "lockcensus.json")))
locks = collections.defaultdict(list)
for s in census:
    m = re.match(r"frontier/B(\d+)_", s["f"])
    ids = {m.group(1)} if m else set(re.findall(r"[bB](\d{1,4})(?!\d)", os.path.basename(s["f"])))
    for i in ids: locks["B" + i].append(s["cls"].split(" ")[0])
unshown = set(re.findall(r"\bB\d{2,4}\b", open("docs/SEAL_ORDER_UNSHOWN.md").read()))

def closure(root):
    depth, stack = {}, [(root, 0)]
    while stack:
        k, dep = stack.pop()
        if k in depth and depth[k] <= dep: continue
        depth[k] = dep
        for x in (A.get(k, {}).get("depends_on") or []): stack.append((x, dep + 1))
    return depth

def lock_tier(k):
    c = set(locks.get(k, []))
    if not c: return "NONE"
    if "MATH" in c: return "COMPUTES"
    if "RUNS_SCRIPT" in c: return "RUNS-SCRIPT"
    if c <= {"TEXT_ONLY", "MATH_IMPORT"}: return "TEXT-ONLY"
    return "OTHER"

def seal_files(d):
    return sorted(os.path.basename(f) for f in glob.glob(d + "/*") if re.match(r"(PREREG|SEALED|DECLARATION)", os.path.basename(f)))

def first_commit(path):
    out = subprocess.run(["git", "log", "--diff-filter=A", "--format=%H", "--", path], capture_output=True, text=True).stdout.split()
    return out[-1] if out else None

depth = closure(ROOT_ARC)
rows = []
for k, dep in sorted(depth.items(), key=lambda kv: (kv[1], int(re.sub(r"\D", "", kv[0]) or 0))):
    v = A.get(k)
    if v is None:
        rows.append(dict(id=k, depth=dep, missing=True, folder=[os.path.basename(x) for x in glob.glob("frontier/%s_*" % k)])); continue
    d = v["_dir"]; sc = v.get("scope") if isinstance(v.get("scope"), dict) else {}
    seals = seal_files(d)
    same_commit = None
    if seals and dep <= 2 and os.path.isfile(d + "/FINDINGS.md"):
        same_commit = any(first_commit(d + "/" + s) == first_commit(d + "/FINDINGS.md") for s in seals)
    rows.append(dict(id=k, depth=dep, verdict=v["verdict"], lock=lock_tier(k),
                     script=bool(glob.glob(d + "/**/*.py", recursive=True) or glob.glob(d + "/**/*.sage", recursive=True)),
                     reach=sc.get("reach"), weave_or_thread=v.get("weave_or_thread"),
                     seals=seals, seal_order_unshown=k in unshown, seal_with_findings=same_commit,
                     rests_on_seat=bool(v.get("rests_on_seat")), cites_seat=bool(v.get("cites_seat")),
                     identifications=v.get("identifications") or [], folders=len(folders[k]),
                     claim=v["claim_one_line"][:160]))
json.dump(dict(root=ROOT_ARC, rows=rows), open(os.path.join(HERE, "value_chain_%s.json" % ROOT_ARC), "w"), indent=1)

R = [r for r in rows if not r.get("missing")]
C = collections.Counter
print("root", ROOT_ARC, "| declared closure:", len(rows), "arcs |", "max depth", max(depth.values()))
print("by depth:", sorted(C(depth.values()).items()))
print("ids depended on with no verdict file:", [(r["id"], r["folder"]) for r in rows if r.get("missing")])
print("verdicts:", dict(C(r["verdict"] for r in R)))
print("not PROVED in the closure:", {v: sorted(r["id"] for r in R if r["verdict"] == v)[:40] for v in ("RETRACTED", "OPEN")})
print("lock tier (all):", dict(C(r["lock"] for r in R)))
print("lock tier (PROVED only):", dict(C(r["lock"] for r in R if r["verdict"] == "PROVED")))
print("no script in folder:", sum(1 for r in R if not r["script"]))
print("declares reach:", sum(1 for r in R if r["reach"]), "| declares weave_or_thread:", sum(1 for r in R if r["weave_or_thread"]))
print("weave_or_thread values:", dict(C((r["weave_or_thread"] or "—")[:28] for r in R)).__repr__()[:900])
print("on the seal-order-unshown list:", sorted(r["id"] for r in R if r["seal_order_unshown"]))
print("rests on a seat:", sum(1 for r in R if r["rests_on_seat"]), "| cites a seat:", sum(1 for r in R if r["cites_seat"]))
print("carries identifications:", sorted({i if isinstance(i, str) else json.dumps(i) for r in R for i in r["identifications"]})[:60])
print("\nDEPTH <= 2:")
for r in rows:
    if r["depth"] > 2: continue
    if r.get("missing"): print("  %-6s d%d  NO VERDICT FILE  %s" % (r["id"], r["depth"], r["folder"])); continue
    print("  %-6s d%d %-9s lock=%-11s reach=%-7s w/t=%-22s seals=%s%s%s | %s" % (
        r["id"], r["depth"], r["verdict"], r["lock"], r["reach"] or "—", (r["weave_or_thread"] or "—")[:22],
        ",".join(r["seals"]) or "—", " [with FINDINGS]" if r["seal_with_findings"] else "", " [seat]" if r["rests_on_seat"] else "", r["claim"][:70]))
