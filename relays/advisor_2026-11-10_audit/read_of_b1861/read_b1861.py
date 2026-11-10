#!/usr/bin/env python3
"""A non-author's read of main's closure programme (B1861) against its closure map (B1858).

Usage:  python3 -B read_b1861.py <path to a checkout of main>

Reads tracked files only and writes nothing. It recomputes, from the programme's and the map's own data files,
the things the programme asks a non-author to try to break: the assignment of each audit finding, the order of
work against the map's edges, and the input budget's kinds. Every number printed is a count over those files.
It runs one of the record's own scripts read-only (the identification ledger's audit) to count the ledger's rows.
"""
import collections
import json
import pathlib
import re
import subprocess
import sys

root = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parents[3]
prog = json.loads((root / "frontier/B1861_the_closure_programme/PROGRAMME.json").read_text(encoding="utf-8"))
nodes = json.loads((root / "frontier/B1858_the_closure_map/NODES.json").read_text(encoding="utf-8"))
edges = json.loads((root / "frontier/B1858_the_closure_map/EDGES.json").read_text(encoding="utf-8"))
by = {n["id"]: n for n in nodes}
pk = {p["id"]: p for p in prog["packages"]}


def head(s):
    print("\n" + s + "\n" + "-" * len(s))


def state(s):
    return "DONE" if s.startswith("DONE") else ("STARTED" if s.startswith("STARTED") else "NOT STARTED")


def upstream_packages(i):
    seen, stack = set(), list(pk[i]["needs_all"])
    while stack:
        x = stack.pop()
        if x not in seen:
            seen.add(x)
            stack += pk[x]["needs_all"]
    return seen


UP = {i: upstream_packages(i) for i in pk}

# ------------------------------------------------------------------ A. the assignment of each finding
head("A. The assignment of each finding")
F = prog["findings"]
listed = collections.Counter(k for p in pk.values() for k in p["findings"])
print("findings:", len(F), "| by state:", dict(sorted(collections.Counter(f["state"] for f in F.values()).items())))
print("A1 a finding whose package does not list it      :", [k for k, f in F.items() if k not in pk[f["wp"]]["findings"]])
print("A2 a finding listed by more than one package      :", [k for k, c in listed.items() if c > 1])
print("A3 a finding listed by no package                 :", [k for k in F if not listed[k]])
print("A4 findings that are nodes of the map             :", sum(1 for k in F if k in by), "of", len(F))
print("A5 a field naming the arcs or nodes a finding touches:", sorted({k for f in F.values() for k in f} - {"note", "short", "state", "was", "wp"}) or "none")
print("A6 a field for the re-audit's verdict on a fix    :", [k for k in ("accepted", "reaudit", "verdict") if any(k in f for f in F.values())] or "none")
print("   FIXED on main's word:", sorted(k for k, f in F.items() if f["state"] == "FIXED"))

# ------------------------------------------------------------------ B. the order of work
head("B. The order of work")
node_pk = {}
for p in prog["packages"]:
    for n in p["nodes"]:
        node_pk.setdefault(n, []).append(p["id"])
print("B1 nodes in a package:", len(node_pk), "| in more than one:", sum(1 for v in node_pk.values() if len(v) > 1))
cyc = [i for i in pk if i in UP[i]]
print("B2 a package upstream of itself by needs          :", cyc)
print("B3 a need not in a strictly earlier wave          :", [(i, n) for i, p in pk.items() for n in p["needs_all"] if pk[n]["wave"] >= p["wave"]])
res = collections.defaultdict(collections.Counter)
no_order = []
for e in edges:
    a, b = node_pk.get(e["src"]), node_pk.get(e["dst"])
    if not a or not b:
        res[e["kind"]]["an end is in no package"] += 1
        continue
    a, b = a[0], b[0]
    if a == b:
        r = "inside one package"
    elif b in UP[a]:
        r = "the source's package needs the target's"
    elif a in UP[b]:
        r = "the target's package needs the source's"
    elif b in pk[a]["given"] or a in pk[b]["given"]:
        r = "held as given"
    else:
        r = "NO ORDER"
        no_order.append((e["kind"], e["src"], a, e["dst"], b))
    res[e["kind"]][r] += 1
print("B4 every edge of the map, projected on the packages:")
for k in sorted(res):
    print("     %-14s %s" % (k, dict(res[k])))
print("   edges between two packages that carry no order :", no_order)
started_early = [(i, n) for i, p in pk.items() if state(p["status"]) != "NOT STARTED" for n in p["needs_all"] if state(pk[n]["status"]) == "NOT STARTED"]
print("B5 'a package cannot be worked before these close': started, with a need not started:", len(started_early))
for i, n in started_early:
    print("     %s (%s) needs %s (%s)" % (i, pk[i]["status"], n, pk[n]["status"]))
print("B6 what the comparison waits on")
for c6 in sorted(i for i, p in pk.items() if p["obligation"] == "C6"):
    notup = sorted(set(pk) - UP[c6] - {c6})
    nf = sum(len(pk[j]["findings"]) for j in notup)
    print("     %s: %d packages upstream; NOT upstream: %d, holding %d of the %d findings" % (c6, len(UP[c6]), len(notup), nf, len(F)))
    for j in notup:
        print("       %-8s %-12s %s | findings: %s | accept: %s" % (j, state(pk[j]["status"]), pk[j]["title"], " ".join(pk[j]["findings"]) or "-", pk[j]["accept"][:110]))
deg = collections.Counter()
kinds_at = collections.defaultdict(collections.Counter)
for e in edges:
    for end in (e["src"], e["dst"]):
        deg[end] += 1
        kinds_at[end][e["kind"]] += 1
debts = [n for n in nodes if n["grade"] == "DEBT"]
with_edge = [n for n in debts if deg[n["id"]]]
print("B7 debts on the map: %d | with any edge: %d | edge kinds at a debt: %s" % (len(debts), len(with_edge), dict(sum((kinds_at[n["id"]] for n in debts), collections.Counter()))))
debt_pk = {d: p["id"] for p in prog["packages"] for d in p["debts"]}
noedge = collections.Counter(debt_pk.get(n["rows"][0], "?") for n in debts if not deg[n["id"]])
print("   debts with no edge, by package:", dict(sorted(noedge.items())))
for j in sorted(noedge):
    if j in pk:
        print("       %-8s %s" % (j, pk[j]["title"]))

# ------------------------------------------------------------------ C. the input budget
head("C. The input budget")
I = prog["inputs"]
print("C1 inputs: %d | items by kind: %d %s | names in the map under them: %d" % (len(I), sum(sum(i["kinds"].values()) for i in I), dict(sorted(sum((collections.Counter(i["kinds"]) for i in I), collections.Counter()).items())), sum(len(i["members"]) for i in I)))
print("C2 fields of an input:", sorted({k for i in I for k in i}))
print("   a field holding the alternatives of a bit or a discrete choice, or their number:", [k for k in ("alternatives", "menu", "options", "size") if any(k in i for i in I)] or "none")
fr = collections.defaultdict(list)
for i in I:
    fr[tuple(sorted({m.split(":")[0] for m in i["members"]}))].append(i["name"])
print("C3 inputs by the families of their names (G foundation, A the candidate frame, FL the framing ledger, T the read-out, SC the scale, MC the structural chain):")
for k in sorted(fr):
    print("     %-12s %d" % ("+".join(k), len(fr[k])))
ident = [i for i in I if "identification" in i["kinds"]]
print("C4 identifications in the budget: %d: %s" % (len(ident), [i["members"] for i in ident]))
out = subprocess.run([sys.executable, "-B", str(root / "scripts/checks/identification_audit.py")], capture_output=True, text=True, cwd=str(root)).stdout
m = {k: re.search(r"^\s*%s\s+(\d+)\s+(.*)$" % k, out, re.M) for k in ("EARNED", "REFUTED", "UNEARNED")}
rows_total = re.search(r"identification ledger: (\d+) rows", out)
print("   the identification ledger, by the record's own script: %s rows; EARNED %s, REFUTED %s, UNEARNED %s" % (rows_total.group(1) if rows_total else "?", *(m[k].group(1) if m[k] else "?" for k in ("EARNED", "REFUTED", "UNEARNED"))))
unearned = m["UNEARNED"].group(2).split() if m["UNEARNED"] else []
blob = {n["id"]: json.dumps(n, ensure_ascii=False) for n in nodes}
named = {u: [i for i, b in blob.items() if re.search(r"\b%s\b" % re.escape(u), b)] for u in unearned}
print("   UNEARNED rows named anywhere in the map's nodes: %d of %d: %s" % (sum(1 for v in named.values() if v), len(unearned), {u: v for u, v in named.items() if v}))
for n in nodes:
    if re.search(r"\d+ ledger rows", n["text"]):
        print("   the map's own sentence about that ledger: %s (%s): %s" % (n["id"], n["grade"], n["text"]))
print("   the price as a node of the map: ", [(n["id"], n["grade"], n["text"]) for n in nodes if n["id"] == "MC:PRICE"])
ex = prog["exits"]
kinds = collections.Counter(v[0] for v in ex.values())
print("C5 exits by kind:", dict(sorted(kinds.items())), "| counted as 'an exit on the table':", prog["stats"]["inputs_with_an_exit_on_the_table"])
for name, v in ex.items():
    if v[0] == "FORCING ARGUED":
        text = " ".join(str(x) for x in v[1:])
        short = bool(re.search(r"clause|removes every departure|no alternative is exhibited", text))
        print("     %-36s %s" % (name, "main's own note names a missing clause or no alternative" if short else "no objection noted"))
c5 = next(i for i in I if "T:CHARGE5" in i["members"])
print("C6 the charge premise at level five is typed:", c5["kinds"])
print("\nread at:", subprocess.run(["git", "-C", str(root), "log", "-1", "--format=%h %ci"], capture_output=True, text=True).stdout.strip())
