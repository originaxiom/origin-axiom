#!/usr/bin/env python3
"""The Ledger Desk's index (a proposal's prototype, not an arc; see THE_LEDGER_DESK.md). Read-only over two refs, HEAD
(this seat's branch) and origin/main, it writes one index outside the record. The B arcs and the W register are read
through git; the W rows and the prior cells come from extract_desk_data.py, which reads the checked-out tree, so build
from a clean checkout of HEAD:

  arcs       one row per arc, keyed (seat, id): main's and this seat's B arcs from frontier/*/arc_verdict.json, and the
             W arcs from NOTE's status table. A B directory on origin/main is main's; one only on HEAD is this seat's
             (sm). Each row carries its source path, the ref, the commit, and the file's blob. Each also carries its
             weave_or_thread label, as main's verdict files state it or as this seat's register for W arcs gives it
             (W_VERDICTS.json, docs/workdesk/THE_LABELS_RULE_2026-10-29.md), and its era: after the rule (main's arcs
             from B1491, this seat's B arcs whose verdict file came after docs/THE_WEAVE.md, every W arc) or before.
  edges      depends_on, supersedes and superseded_by from the verdict files, and main's rests_on_seat and cites_seat
             (to sm: ids). A bare id resolves within the citing arc's seat, then at main, then at the other seat; each
             edge says which, or that its target is a directory without a verdict file, or on neither branch.
  relays     each branch's docs/RELAY_LEDGER.md, one row per relay file (the last row for a file wins, as in the
             relay-debt gate, and rows_for_file counts its rows): the first file the row names, its disposition (first
             word), date, age in days at that branch's commit, whether the note carries ESCALATED, and from/to read
             from the file's name where it follows the SEAT_TO_SEAT_date pattern; and whether the relay-debt gate's
             own row pattern matches the row (a row it does not match is one the gate cannot age or escalate).
  cells      W rule priors joined to one-run outcomes (extract_desk_data.py).
  lifecycle  W arc steps read from this branch's commit subjects ("W176's rule", "W176's script", "W176's output",
             "W176's post hoc script", "W176's post hoc output", "W176 recorded"), each with its commit and position.
  flags      any W arc whose steps are out of order (rule < script < output <= recorded; post hoc script < post hoc
             output; output < post hoc script).

Outputs, in --out (never committed): index.sqlite, index.json, manifest.json, and page_index.json (the slice the
prototype page embeds). The manifest names both commits, the schema, the extractors' sha-256 and each table's row count
and sha-256. --check builds twice and requires equal hashes.

    python3 -B docs/workdesk/build_index.py --out /path/outside/the/record --check
"""
import argparse
import hashlib
import json
import re
import sqlite3
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(HERE))
import extract_desk_data as X  # noqa: E402  (W rows, priors, outcomes, the tower plates)

SCHEMA = 3
REFS = {"sm": "HEAD", "main": "origin/main"}
WEAVE_START = "2026-10-07"
MAIN_LABEL_FROM = 1491  # main carries weave_or_thread on every verdict file from B1491 on (its test for B1600)
W_REGISTER = "docs/dossiers/the_weave_2026-10-07/W_VERDICTS.json"
STEPS = [("rule", r"^(W\d+)'s rule\b"), ("script", r"^(W\d+)'s script\b"), ("output", r"^(W\d+)'s output\b"),
         ("posthoc_script", r"^(W\d+)'s (?:labelled )?post hoc script"),
         ("posthoc_output", r"^(W\d+)'s post hoc output"), ("recorded", r"^(W\d+) recorded\b")]


def git(*args, data=None):
    r = subprocess.run(["git", "-C", str(REPO), *args], input=data, capture_output=True)
    if r.returncode != 0:
        raise SystemExit(f"git {' '.join(args)} failed: {r.stderr.decode(errors='replace')[:300]}")
    return r.stdout


def verdict_files(ref):
    """{path: blob} for every frontier/*/arc_verdict.json at ref"""
    out = {}
    for ln in git("ls-tree", "-r", ref, "frontier/").decode().splitlines():
        meta, path = ln.split("\t", 1)
        if path.endswith("/arc_verdict.json"):
            out[path] = meta.split()[2]
    return out


def read_blobs(blobs):
    """{blob: parsed json or None}, read in one cat-file batch"""
    order = sorted(set(blobs))
    raw = git("cat-file", "--batch", data=("\n".join(order) + "\n").encode())
    out, i = {}, 0
    for b in order:
        nl = raw.index(b"\n", i)
        size = int(raw[i:nl].split()[2])
        body = raw[nl + 1:nl + 1 + size]
        i = nl + 1 + size + 1
        try:
            out[b] = json.loads(body)
        except ValueError:
            out[b] = None
    return out


def b_arcs():
    files = {seat: verdict_files(ref) for seat, ref in REFS.items()}
    commits = {seat: git("rev-parse", ref).decode().strip() for seat, ref in REFS.items()}
    blobs = read_blobs(list(files["main"].values()) + list(files["sm"].values()))
    rule_time, added = sm_added_times()
    rows = []
    for seat, paths in (("main", files["main"]), ("sm", {p: b for p, b in files["sm"].items()
                                                       if p not in files["main"]})):
        for path, blob in sorted(paths.items()):
            d = blobs.get(blob) or {}
            dir_id = path.split("/")[1].split("_")[0]
            wot = d.get("weave_or_thread")
            num = int(re.sub(r"\D", "", dir_id) or 0)
            after = num >= MAIN_LABEL_FROM if seat == "main" else added.get(path, 0) >= rule_time
            rows.append({"key": f"{seat}:{dir_id}", "seat": seat, "kind": "B", "id": dir_id,
                         "verdict": d.get("verdict"),
                         "scope": (wot.split()[0] if isinstance(wot, str) and wot else None),
                         "label": wot if isinstance(wot, str) and wot else None,
                         "label_source": "verdict file" if wot else None,
                         "era": "after the rule" if after else "before the rule",
                         "claim": (d.get("claim_one_line") or "")[:300], "source": path, "ref": REFS[seat],
                         "commit": commits[seat], "blob": blob, "_d": d})
    return rows, commits


def sm_added_times():
    """the time the weave rule was adopted on this branch (docs/THE_WEAVE.md added), and each verdict file's first
    commit time on this branch: this seat's B arcs are 'after the rule' when their verdict file came later"""
    rule = git("log", "--diff-filter=A", "--format=%ct", REFS["sm"], "--", "docs/THE_WEAVE.md").decode().split()
    added, t = {}, 0
    for ln in git("log", "--diff-filter=A", "--format=@%ct", "--name-only", REFS["sm"], "--",
                  "frontier/").decode().splitlines():
        if ln.startswith("@"):
            t = int(ln[1:])
        elif ln.endswith("/arc_verdict.json"):
            added[ln] = min(added.get(ln, t), t)
    return int(rule[-1]), added


def frontier_dirs():
    """{seat: {bare id: dir}} for every frontier directory, with or without a verdict file"""
    out = {}
    for seat, ref in REFS.items():
        names = git("ls-tree", "-d", "--name-only", ref, "frontier/").decode().split()
        out[seat] = {n.split("/")[1].split("_")[0]: n for n in names}
    return out


def resolve(bare, seat, keys, dirs):
    """where a bare id points, and how it was resolved: within the citing seat, at main, at the other seat, at a
    directory with no verdict file, or nowhere on either branch"""
    other = "sm" if seat == "main" else "main"
    for s, how in ((seat, "same seat"), ("main", "main"), (other, "other seat")):
        if f"{s}:{bare}" in keys:
            return f"{s}:{bare}", how
    for s in (seat, other):
        if bare in dirs[s]:
            return f"{s}:{bare}", "directory without a verdict file"
    return f"main:{bare}", "missing on both branches"


def b_edges(rows, keys):
    dirs = frontier_dirs()
    out = []
    for r in rows:
        d = r.pop("_d")
        for kind in ("depends_on", "supersedes", "superseded_by"):
            v = d.get(kind)
            for t in (v if isinstance(v, list) else [v] if v else []):
                if isinstance(t, str) and re.fullmatch(r"B\d+[a-z]?", t):
                    dst, how = resolve(t, r["seat"], keys, dirs)
                    out.append({"src": r["key"], "dst": dst, "kind": kind, "resolved": how})
        for kind in ("rests_on_seat", "cites_seat"):
            for t in d.get(kind) or []:
                if isinstance(t, str) and ":" in t:
                    how = "cited by seat" if t in keys else "another seat's id, not indexed"
                    out.append({"src": r["key"], "dst": t, "kind": kind, "resolved": how})
    return sorted(out, key=lambda e: (e["src"], e["kind"], e["dst"]))


def w_rows(head):
    reg = json.loads(git("show", f"{REFS['sm']}:{W_REGISTER}").decode())
    labels = {e["id"]: e for e in reg["arcs"]}
    rows = []
    for arc, status, tag, st, what, line, first, last in X.arcs():
        lab = labels.get(arc, {})
        wot = lab.get("weave_or_thread")
        rows.append({"key": f"sm:{arc}", "seat": "sm", "kind": "W", "id": arc, "verdict": status,
                     "scope": wot.split()[0] if wot else None, "label": wot,
                     "label_source": lab.get("source"), "era": "after the rule", "claim": what[:300],
                     "source": f"docs/dossiers/the_weave_2026-10-07/NOTE.md:{line}", "ref": "HEAD", "commit": head,
                     "blob": None})
    return rows


def lifecycle():
    steps = []
    for k, ln in enumerate(git("log", "--reverse", "--format=%h|%cI|%s", "HEAD").decode().splitlines()):
        h, date, subj = ln.split("|", 2)
        if date[:10] < WEAVE_START:
            continue
        for name, rx in STEPS:
            m = re.match(rx, subj)
            if m:
                steps.append({"arc": f"sm:{m.group(1)}", "step": name, "order": k, "commit": h, "date": date,
                              "subject": subj[:200]})
    first = {}
    for s in steps:
        first.setdefault((s["arc"], s["step"]), s["order"])
    flags = []
    for arc in sorted({s["arc"] for s in steps}):
        f = {n: first[(arc, n)] for n, _ in STEPS if (arc, n) in first}
        seq = [n for n in ("rule", "script", "output", "recorded") if n in f]
        for a, b in zip(seq, seq[1:]):
            if not (f[a] < f[b] or (a == "output" and b == "recorded" and f[a] <= f[b])):
                flags.append({"arc": arc, "before": a, "after": b})
        for a, b in (("posthoc_script", "posthoc_output"), ("output", "posthoc_script")):
            if a in f and b in f and not f[a] < f[b]:
                flags.append({"arc": arc, "before": a, "after": b})
    return steps, flags


def cells():
    p, o = X.priors(), X.outcomes()
    return [{"arc": "sm:" + re.match(r"(W\d+)", rule).group(1), "cell": c, "prior": pr, "held": bool(o[(rule, c)]),
             "source": f"docs/dossiers/the_weave_2026-10-07/{src}"}
            for (rule, c), (pr, _pred, src) in sorted(p.items()) if (rule, c) in o]


LEDGER_DATE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
# the relay-debt gate's own row pattern (scripts/checks/relay_debt.py), copied: a row it does not match is a row the
# gate cannot age or escalate
GATE_ROW = re.compile(r"^\|\s*`?(?P<name>[A-Za-z0-9_.\-]+\.md)`?\s*\|\s*(?P<disp>BANKED|DECLINED|OPEN)\s*\|"
                      r"\s*(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2}|—|-)\s*\|\s*(?P<note>[^|]*)\|")
DIRECTION = re.compile(r"^(?P<frm>[A-Z0-9]+(?:_[A-Z0-9]+)*?)_TO_(?P<to>[A-Z0-9_]+?)_\d{4}-\d{2}-\d{2}")


def relays(commits):
    """each branch's relay ledger, row by row; ages are counted to that branch's commit date, so a build is fixed by
    its commits"""
    import collections
    import datetime
    rows = {}
    for seat, ref in REFS.items():
        day = datetime.date.fromisoformat(git("show", "-s", "--format=%cs", commits[seat]).decode().strip())
        text = git("show", f"{ref}:docs/RELAY_LEDGER.md").decode()
        seen = collections.Counter()
        for line in text.splitlines():
            if not line.startswith("| `"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 4:
                continue
            name = re.match(r"`([^`]+)`", cells[0]).group(1)
            disp = (cells[1].split() or ["?"])[0].strip("*,;")
            when = LEDGER_DATE.search(cells[2])
            date = when.group(0) if when else None
            note = "|".join(cells[3:])
            d = DIRECTION.match(name)
            seen[name] += 1
            rows[f"{seat}:{name}"] = {"key": f"{seat}:{name}", "seat": seat, "file": name, "row": cells[0][:160],
                         "rows_for_file": seen[name],
                         "gate_sees": bool(GATE_ROW.match(line)),
                         "disposition": disp, "date": date,
                         "age_days": (day - datetime.date.fromisoformat(date)).days if date else None,
                         "escalated": "ESCALATED(" in note,
                         "frm": d.group("frm") if d else None, "to": d.group("to") if d else None,
                         "note": note[:240]}
    return sorted(rows.values(), key=lambda r: r["key"])


def build():
    rows, commits = b_arcs()
    w = w_rows(commits["sm"])
    edges = b_edges(rows, {r["key"] for r in rows + w})
    rows += w
    rows.sort(key=lambda r: (r["seat"], r["kind"], int(re.sub(r"\D", "", r["id"]) or 0), r["id"]))
    steps, flags = lifecycle()
    return {"arcs": rows, "edges": edges, "cells": cells(), "lifecycle": steps, "flags": flags,
            "relays": relays(commits)}, commits


def digest(obj):
    text = json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(text.encode()).hexdigest()


def write(tables, commits, out, deterministic):
    out.mkdir(parents=True, exist_ok=True)
    db = out / "index.sqlite"
    if db.exists():
        db.unlink()
    con = sqlite3.connect(db)
    for name, rows in tables.items():
        cols = sorted({k for r in rows for k in r}) or ["empty"]
        quoted = ", ".join('"' + c + '"' for c in cols)
        con.execute(f"CREATE TABLE {name} ({quoted})")
        con.executemany(f"INSERT INTO {name} VALUES ({', '.join('?' * len(cols))})",
                        [[r.get(c) if not isinstance(r.get(c), (dict, list)) else json.dumps(r.get(c)) for c in cols]
                         for r in rows])
    con.commit()
    con.close()
    (out / "index.json").write_text(json.dumps(tables, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    manifest = {"schema": SCHEMA, "built_from": {REFS[s]: c for s, c in commits.items()},
                "extractors_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                      for p in (HERE / "build_index.py", HERE / "extract_desk_data.py")},
                "tables": {n: {"rows": len(r), "sha256": digest(r)} for n, r in tables.items()},
                "deterministic": deterministic}
    (out / "manifest.json").write_text(json.dumps(manifest, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def dependency_cycles(n, dep, nodes):
    """the strongly connected components with more than one arc (Tarjan, iterative): arcs that rest on each other"""
    adj = [[] for _ in range(n)]
    for s_, d_ in dep:
        adj[s_].append(d_)
    index, low, stack, on, out, count = {}, {}, [], set(), [], 0
    for root in range(n):
        if root in index:
            continue
        work = [(root, 0)]
        index[root] = low[root] = count
        count += 1
        stack.append(root)
        on.add(root)
        while work:
            v, i = work[-1]
            if i < len(adj[v]):
                work[-1] = (v, i + 1)
                w = adj[v][i]
                if w not in index:
                    index[w] = low[w] = count
                    count += 1
                    stack.append(w)
                    on.add(w)
                    work.append((w, 0))
                elif w in on:
                    low[v] = min(low[v], index[w])
                continue
            work.pop()
            if work:
                low[work[-1][0]] = min(low[work[-1][0]], low[v])
            if low[v] == index[v]:
                comp = []
                while True:
                    w = stack.pop()
                    on.discard(w)
                    comp.append(w)
                    if w == v:
                        break
                if len(comp) > 1:
                    out.append(sorted(nodes[x][0] for x in comp))
    return sorted(out)


def page_data(tables, manifest):
    """the compact slice the prototype page embeds as DESK.index"""
    import collections
    counts = collections.Counter((a["seat"], a["kind"], a["verdict"] or "none") for a in tables["arcs"])
    how = collections.Counter(e["resolved"] for e in tables["edges"])
    cross = [[e["src"], e["dst"], e["kind"]] for e in tables["edges"]
             if e["src"].split(":")[0] != e["dst"].split(":")[0] and e["resolved"] in ("cited by seat", "other seat")]
    audit = [[e["src"], e["dst"], e["kind"], e["resolved"]] for e in tables["edges"]
             if e["resolved"] in ("directory without a verdict file", "missing on both branches",
                                  "another seat's id, not indexed")]
    life = [[s["arc"], s["step"], s["date"], s["commit"]] for s in tables["lifecycle"]]
    cover = collections.Counter((a["seat"], a["kind"], a["era"], bool(a["label"])) for a in tables["arcs"])
    labels = [[s, k, e, cover[(s, k, e, True)], cover[(s, k, e, True)] + cover[(s, k, e, False)]]
              for s, k, e in sorted({key[:3] for key in cover})]
    w_labels = {a["id"]: [a["scope"], a["label"], a["label_source"]] for a in tables["arcs"] if a["kind"] == "W"}
    # the board: what is open on each seat, and which relays wait
    tag = {a["key"]: (a["scope"] or ("before the rule" if a["era"] == "before the rule" else "unlabelled"))
           for a in tables["arcs"]}
    open_arcs = [[a["key"], tag[a["key"]], a["claim"][:140], a["source"]] for a in tables["arcs"]
                 if (a["verdict"] or "").upper() == "OPEN"]
    by_label = collections.Counter((a["seat"], a["kind"], (a["verdict"] or "none").upper(), tag[a["key"]])
                                   for a in tables["arcs"])
    waiting = [[r["seat"], r["file"], r["date"], r["age_days"], r["escalated"], r["frm"], r["to"], r["note"][:160],
                r["gate_sees"]] for r in tables["relays"] if r["disposition"] == "OPEN"]
    dispositions = collections.Counter((r["seat"], r["disposition"]) for r in tables["relays"])
    # the atlas: every arc and every dependency (depends_on, rests_on_seat); the cones are drawn in the page
    keys = [a["key"] for a in tables["arcs"]]
    at = {k: i for i, k in enumerate(keys)}
    nodes = [[a["key"], (a["verdict"] or "none").upper(), tag[a["key"]], a["claim"][:110]] for a in tables["arcs"]]
    ghosts = sorted({e["dst"] for e in tables["edges"] if e["dst"] not in at})
    for g in ghosts:
        at[g] = len(nodes)
        nodes.append([g, "NOT FOUND", "", ""])
    dep = [[at[e["src"]], at[e["dst"]]] for e in tables["edges"] if e["kind"] in ("depends_on", "rests_on_seat")]
    down = collections.defaultdict(set)
    for s_, d_ in dep:
        down[d_].add(s_)

    def cone(i):
        seen, todo = set(), [i]
        while todo:
            for j in down[todo.pop()]:
                if j not in seen:
                    seen.add(j)
                    todo.append(j)
        return seen
    load = sorted(((len(cone(i)), nodes[i][0]) for i in range(len(nodes))), key=lambda t: (-t[0], t[1]))[:12]
    cycles = dependency_cycles(len(nodes), dep, nodes)
    return {"manifest": manifest, "counts": sorted([list(k) + [v] for k, v in counts.items()]), "labels": labels,
            "w_labels": w_labels,
            "board": {"open": open_arcs, "by_label": sorted([list(k) + [v] for k, v in by_label.items()]),
                      "waiting": waiting, "dispositions": sorted([list(k) + [v] for k, v in dispositions.items()])},
            "atlas": {"nodes": nodes, "dep": dep, "load": [[k, n] for n, k in load], "cycles": cycles},
            "resolved": sorted(how.items(), key=lambda kv: -kv[1]), "cross": cross, "audit": audit, "life": life,
            "flags": tables["flags"]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="a directory outside the record")
    ap.add_argument("--check", action="store_true", help="build twice and require identical table hashes")
    a = ap.parse_args()
    out = Path(a.out).resolve()
    if REPO in out.parents or out == REPO:
        raise SystemExit("--out must lie outside the repository: the index is derived and is never committed")
    tables, commits = build()
    deterministic = None
    if a.check:
        again, _ = build()
        deterministic = all(digest(tables[n]) == digest(again[n]) for n in tables)
        if not deterministic:
            raise SystemExit("not deterministic: two builds differ")
    m = write(tables, commits, out, deterministic)
    (out / "page_index.json").write_text(json.dumps(page_data(tables, m), sort_keys=True, ensure_ascii=False,
                                                    separators=(",", ":")) + "\n", encoding="utf-8")
    print(json.dumps({n: t["rows"] for n, t in m["tables"].items()}), "deterministic:", deterministic)


if __name__ == "__main__":
    main()
