#!/usr/bin/env python3
"""The Ledger Desk's index (see docs/workdesk/README.md). Read-only over one ref, main's (HEAD by default), and
optionally a second, the SM seat's branch (--seat-ref). It writes one index outside the record. The B arcs, the relay
ledger and, with the seat's branch, the W register are read through git; nothing is checked out.

  arcs       one row per arc, keyed (seat, id): main's B arcs from frontier/*/arc_verdict.json and, with --seat-ref, the
             seat's B arcs that main does not hold (seat sm) and its W arcs from NOTE's status table. A number carried
             by several folders (B58) keys its later folders B58#2, B58#3. Each row carries its source path, the ref, the
             commit, and the file's blob. Each also carries its weave_or_thread label (wot is its first word), as main's
             verdict files state it or as the seat's register for W arcs gives it, and its era: after the rule (main's
             arcs from B1491, the seat's B arcs whose verdict file came after docs/THE_WEAVE.md, every W arc) or before.
  edges      depends_on, supersedes and superseded_by from the verdict files, and rests_on_seat and cites_seat (to sm:
             ids). A bare id resolves within the citing arc's seat, then at main, then at the other seat; each edge says
             which, or that its target is a directory without a verdict file, or on no branch read. A seat id whose
             branch is not read is classed "seat branch not read", not as missing.
  relays     each ref's docs/RELAY_LEDGER.md, one row per relay file (the last row for a file wins, as in the relay-debt
             gate, and rows_for_file counts its rows): the first file the row names, its disposition (first word), date,
             age in days at that ref's commit, whether the note carries ESCALATED, and from/to read from the file's name
             where it follows the SEAT_TO_SEAT_date pattern; and whether the relay-debt gate's own row pattern matches
             the row (a row it does not match is one it cannot age or escalate).
  cells      W rule priors joined to one-run outcomes (extract_desk_data.py); with --seat-ref only.
  lifecycle  W arc steps read from the seat branch's commit subjects ("W176's rule", "W176's script", "W176's output",
             "W176's post hoc script", "W176's post hoc output", "W176 recorded"), each with its commit and position;
             with --seat-ref only.
  flags      any W arc whose steps are out of order (rule < script < output <= recorded; post hoc script < post hoc
             output; output < post hoc script).

Outputs, in --out (never committed; it must lie outside the repository or in a path git ignores): index.sqlite,
index.json, manifest.json, and page_index.json (the slice the page embeds). The manifest names the commit read for each
seat, the schema, the extractors' sha-256 and each table's row count and sha-256. --check builds twice and requires
equal hashes.

    python3 -B docs/workdesk/build_index.py [--repo DIR] [--main-ref REF] [--seat-ref REF|auto] --out DIR [--check]
"""
import argparse
import ast
import collections
import hashlib
import io
import json
import re
import sqlite3
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(HERE))
import extract_desk_data as X  # noqa: E402  (W rows, priors, outcomes, the tower plates)

SCHEMA = 4
REFS = {"main": "HEAD"}   # seat -> the ref read; main's HEAD by default, "sm" is added by --seat-ref
SEAT_SUFFIX = "/standard-model-derivation-0qt6ao"   # the SM seat's branch, matched by its name's suffix as harvest_debt does
SEAT_LABEL = {"main": "main", "sm": "the SM seat's branch"}
WEAVE_START = "2026-10-07"
MAIN_LABEL_FROM = 1491  # main carries weave_or_thread on every verdict file from B1491 on (its test for B1600)
DOSSIER = "docs/dossiers/the_weave_2026-10-07"
W_REGISTER = DOSSIER + "/W_VERDICTS.json"
STEPS = [("rule", r"^(W\d+)'s rule\b"), ("script", r"^(W\d+)'s script\b"), ("output", r"^(W\d+)'s output\b"),
         ("posthoc_script", r"^(W\d+)'s (?:labelled )?post hoc script"),
         ("posthoc_output", r"^(W\d+)'s post hoc output"), ("recorded", r"^(W\d+) recorded\b")]
# the one hand-copied table the page carries (P-415's gauge chain, view E) cites these arcs, copied as main stood at
# this commit; the index checks whether any of them has changed since, so the copy cannot go stale unseen
CURATED_ARCS = ("B727", "B1805", "B1812")
CURATED_AT = "965938922"


def git(*args, data=None):
    r = subprocess.run(["git", "-C", str(REPO), *args], input=data, capture_output=True)
    if r.returncode != 0:
        raise SystemExit(f"git {' '.join(args)} failed: {r.stderr.decode(errors='replace')[:300]}")
    return r.stdout


def clip(text, n):
    """text cut to n characters, with an ellipsis where it was cut (a cut that says nothing reads as the whole)"""
    return text if len(text) <= n else text[:n - 1] + "…"


def find_seat_ref():
    """the SM seat's branch, found by the suffix of its name among the local and remote refs (origin's wins)"""
    names = git("for-each-ref", "--format=%(refname)", "refs/remotes", "refs/heads").decode().split()
    hits = sorted((n for n in names if n.endswith(SEAT_SUFFIX)), key=lambda n: (not n.startswith("refs/remotes/origin/"), n))
    if not hits:
        raise SystemExit("no ref ends with the SM seat's branch name; pass --seat-ref REF")
    return hits[0]


def add_args(ap):
    ap.add_argument("--repo", help="the checkout to read (default: the one this script sits in)")
    ap.add_argument("--main-ref", default="HEAD", help="the ref read as main's record (default: HEAD)")
    ap.add_argument("--seat-ref", help="also read the SM seat's branch at this ref ('auto': found by the suffix of its "
                                       "name); its arcs are keyed sm: and its weave dossier feeds the W views")


def setup(a, scratch):
    """point this module and the extractor at the refs the arguments name; the seat's dossier is extracted to scratch"""
    global REPO, REFS
    if a.repo:
        REPO = Path(a.repo).resolve()
    REFS = {"main": a.main_ref}
    X.configure(repo=REPO, log_ref=REFS["main"])
    if a.seat_ref:
        REFS["sm"] = find_seat_ref() if a.seat_ref == "auto" else a.seat_ref
        buf = git("archive", "--format=tar", REFS["sm"], DOSSIER)
        with tarfile.open(fileobj=io.BytesIO(buf)) as tf:
            tf.extractall(scratch, filter="data")
        X.configure(dossier=Path(scratch) / DOSSIER, log_ref=REFS["sm"])
    else:
        # main holds no weave dossier. The page is a function of the refs read, never of the working tree, so the extractor
        # is pointed at a directory that does not exist and reports w_present false
        X.configure(dossier=Path(scratch) / "no_dossier")


def verdict_files(ref):
    """{path: blob} for every frontier/*/arc_verdict.json at ref (the folder's own file: a verdict file inside a harvested
    copy deeper down is not an arc of its own, and scripts/checks/arc_data.py does not read it either)"""
    out = {}
    for ln in git("ls-tree", "-r", ref, "frontier/").decode().splitlines():
        meta, path = ln.split("\t", 1)
        if path.endswith("/arc_verdict.json") and path.count("/") == 2:
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
    blobs = read_blobs([b for f in files.values() for b in f.values()])
    rule_time, added = sm_added_times() if "sm" in REFS else (0, {})
    groups = [("main", files["main"])]
    if "sm" in files:
        groups.append(("sm", {p: b for p, b in files["sm"].items() if p not in files["main"]}))
    rows, used = [], collections.Counter()
    for seat, paths in groups:
        for path, blob in sorted(paths.items()):
            d = blobs.get(blob) or {}
            dir_id = path.split("/")[1].split("_")[0]
            used[(seat, dir_id)] += 1
            key = f"{seat}:{dir_id}" + (f"#{used[(seat, dir_id)]}" if used[(seat, dir_id)] > 1 else "")
            wot = d.get("weave_or_thread")
            num = int(re.sub(r"\D", "", dir_id) or 0)
            after = num >= MAIN_LABEL_FROM if seat == "main" else added.get(path, 0) >= rule_time
            rows.append({"key": key, "seat": seat, "kind": "B", "id": dir_id,
                         "verdict": d.get("verdict"),
                         "wot": (wot.split()[0] if isinstance(wot, str) and wot else None),
                         "label": wot if isinstance(wot, str) and wot else None,
                         "label_source": "verdict file" if wot else None,
                         "era": "after the rule" if after else "before the rule",
                         "claim": clip(d.get("claim_one_line") or "", 300), "source": path, "ref": SEAT_LABEL[seat],
                         "commit": commits[seat], "blob": blob, "_d": d})
    return rows, commits


def sm_added_times():
    """the time the weave rule was adopted on the seat's branch (docs/THE_WEAVE.md added), and each verdict file's first
    commit time on that branch: the seat's B arcs are 'after the rule' when their verdict file came later"""
    rule = git("log", "--diff-filter=A", "--format=%ct", REFS["sm"], "--", "docs/THE_WEAVE.md").decode().split()
    added, t = {}, 0
    for ln in git("log", "--diff-filter=A", "--format=@%ct", "--name-only", REFS["sm"], "--",
                  "frontier/").decode().splitlines():
        if ln.startswith("@"):
            t = int(ln[1:])
        elif ln.endswith("/arc_verdict.json"):
            added[ln] = min(added.get(ln, t), t)
    return (int(rule[-1]) if rule else 0), added


def frontier_dirs():
    """{seat: {bare id: dir}} for every frontier directory, with or without a verdict file"""
    out = {}
    for seat, ref in REFS.items():
        names = git("ls-tree", "-d", "--name-only", ref, "frontier/").decode().split()
        out[seat] = {n.split("/")[1].split("_")[0]: n for n in names}
    return out


def resolve(bare, seat, keys, dirs):
    """where a bare id points, and how it was resolved: within the citing seat, at main, at the other seat, at a
    directory with no verdict file, or nowhere on a branch read"""
    other = "sm" if seat == "main" else "main"
    for s, how in ((seat, "same seat"), ("main", "main"), (other, "other seat")):
        if s in REFS and f"{s}:{bare}" in keys:
            return f"{s}:{bare}", how
    for s in (seat, other):
        if s in REFS and bare in dirs[s]:
            return f"{s}:{bare}", "directory without a verdict file"
    return f"main:{bare}", ("missing on both branches" if len(REFS) > 1 else "missing on main")


def ids(v):
    """a field that may be None, one id, a list, or one string holding several ids ('B234, B235')"""
    raw = [v] if isinstance(v, str) else list(v) if isinstance(v, list) else []
    return [t for chunk in raw if isinstance(chunk, str) for t in re.split(r"[,\s]+", chunk.strip()) if t]


def b_edges(rows, keys):
    dirs = frontier_dirs()
    out = []
    for r in rows:
        d = r.pop("_d")
        for kind in ("depends_on", "supersedes", "superseded_by"):
            for t in ids(d.get(kind)):
                if re.fullmatch(r"B\d+[a-z]?", t):
                    dst, how = resolve(t, r["seat"], keys, dirs)
                    out.append({"src": r["key"], "dst": dst, "kind": kind, "resolved": how})
        for kind in ("rests_on_seat", "cites_seat"):
            for t in d.get(kind) or []:
                if isinstance(t, str) and ":" in t:
                    if t in keys:
                        how = "cited by seat"
                    elif t.split(":")[0] in REFS:
                        how = "missing on the seat's branch"
                    else:
                        how = "seat branch not read"
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
                     "wot": wot.split()[0] if wot else None, "label": wot,
                     "label_source": lab.get("source"), "era": "after the rule", "claim": clip(what, 300),
                     "source": f"{DOSSIER}/NOTE.md:{line}", "ref": SEAT_LABEL["sm"], "commit": head,
                     "blob": None})
    return rows


def lifecycle():
    if "sm" not in REFS:
        return [], []
    steps = []
    for k, ln in enumerate(git("log", "--reverse", "--format=%h|%cI|%s", REFS["sm"]).decode().splitlines()):
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
    if "sm" not in REFS or not X.have_dossier():
        return []
    p, o = X.priors(), X.outcomes()
    return [{"arc": "sm:" + re.match(r"(W\d+)", rule).group(1), "cell": c, "prior": pr, "held": bool(o[(rule, c)]),
             "source": f"{DOSSIER}/{src}"}
            for (rule, c), (pr, _pred, src) in sorted(p.items()) if (rule, c) in o]


LEDGER_DATE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
DIRECTION = re.compile(r"^(?P<frm>[A-Z0-9]+(?:_[A-Z0-9]+)*?)_TO_(?P<to>[A-Z0-9_]+?)_\d{4}-\d{2}-\d{2}")


_GATE = {}


def relay_gate():
    """(row pattern, escalation pattern, stale days, sha-256 of the gate's source) of the relay-debt gate AS IT STANDS AT
    MAIN'S REF: a row it does not match is a row the gate cannot age or escalate, so the pattern must be the gate's own
    and cannot be a copy (the SM seat's copy predated B1307 and saw 9 of main's 80 OPEN rows where the gate sees all 80).
    The three definitions are read from the gate's source at the ref by parsing it, not by running it; if they cannot be
    read the build stops rather than guess."""
    ref = REFS["main"]
    if ref not in _GATE:
        path = "scripts/checks/relay_debt.py"
        src = git("show", f"{ref}:{path}")
        found = {}
        for node in ast.parse(src).body:
            if not (isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name)
                    and node.targets[0].id in ("ROW_RE", "ESCALATED_RE", "STALE_DAYS")):
                continue
            v = node.value
            if isinstance(v, ast.Call) and ast.unparse(v.func) == "re.compile":
                flags = 0
                for extra in v.args[1:]:
                    flags |= getattr(re, extra.attr)           # re.M and the like
                found[node.targets[0].id] = re.compile(ast.literal_eval(v.args[0]), flags)
            elif isinstance(v, ast.Constant):
                found[node.targets[0].id] = v.value
        if set(found) != {"ROW_RE", "ESCALATED_RE", "STALE_DAYS"}:
            raise SystemExit(f"cannot read the relay-debt gate's patterns from {path} at {ref}: the board's 'gate sees it' "
                             "would be a guess")
        _GATE[ref] = (found["ROW_RE"], found["ESCALATED_RE"], found["STALE_DAYS"], hashlib.sha256(src).hexdigest())
    return _GATE[ref]


def relays(commits):
    """each ref's relay ledger, row by row; ages are counted to that ref's commit date, so a build is fixed by its
    commits"""
    import datetime
    row_re, esc_re, _days, _sha = relay_gate()
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
                         "gate_sees": bool(row_re.match(line)),
                         "disposition": disp, "date": date,
                         "age_days": (day - datetime.date.fromisoformat(date)).days if date else None,
                         "escalated": bool(esc_re.search(note)),
                         "frm": d.group("frm") if d else None, "to": d.group("to") if d else None,
                         "note": clip(note, 240)}
    return sorted(rows.values(), key=lambda r: r["key"])


def build():
    rows, commits = b_arcs()
    w = w_rows(commits["sm"]) if "sm" in REFS and X.have_dossier() else []
    edges = b_edges(rows, {r["key"] for r in rows + w})
    rows += w
    rows.sort(key=lambda r: (r["seat"], r["kind"], int(re.sub(r"\D", "", r["id"]) or 0), r["key"]))
    steps, flags = lifecycle()
    return {"arcs": rows, "edges": edges, "cells": cells(), "lifecycle": steps, "flags": flags,
            "relays": relays(commits)}, commits


def digest(obj):
    text = json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(text.encode()).hexdigest()


def make_manifest(tables, commits, deterministic):
    return {"schema": SCHEMA, "mode": "main and the SM seat's branch" if "sm" in REFS else "main only",
            "built_from": dict(commits),
            "extractors_sha256": {**{p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                     for p in (HERE / "build_index.py", HERE / "extract_desk_data.py")},
                                  "relay_debt.py (the gate's row pattern, at main's ref)": relay_gate()[3]},
            "tables": {n: {"rows": len(r), "sha256": digest(r)} for n, r in tables.items()},
            "deterministic": deterministic}


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
    manifest = make_manifest(tables, commits, deterministic)
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


def register_row(pid):
    """{id, disposition (the first word of the row's disposition cell), line} of a point-register row at main's ref, or None"""
    for n, ln in enumerate(git("show", f"{REFS['main']}:docs/POINT_REGISTER.md").decode().splitlines(), 1):
        if ln.startswith(f"| {pid} |"):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            return {"id": pid, "disposition": (cells[4].split() or ["?"])[0] if len(cells) > 4 else "?", "line": n}
    return None


def curated(rows):
    """[arc, verdict, claim, last commit touching its folder, unchanged since the copy (None: not checkable), source]"""
    first = {}
    for r in rows:
        if r["seat"] == "main":
            first.setdefault(r["id"], r)
    out = []
    for arc in CURATED_ARCS:
        r = first.get(arc)
        if r is None:
            out.append([arc, "NOT FOUND", "", "", None, ""])
            continue
        last = git("log", "-1", "--format=%h", REFS["main"], "--", r["source"].rsplit("/", 1)[0]).decode().strip()
        rc = subprocess.run(["git", "-C", str(REPO), "merge-base", "--is-ancestor", last, CURATED_AT],
                            capture_output=True).returncode
        out.append([arc, (r["verdict"] or "none").upper(), clip(r["claim"], 160), last,
                    True if rc == 0 else False if rc == 1 else None, r["source"]])
    return out


NOT_AUDITED = ("cited by seat", "other seat", "seat branch not read")   # resolved, or a branch not read: not "targets not found"


def page_data(tables, manifest):
    """the compact slice the page embeds as DESK.index"""
    counts = collections.Counter((a["seat"], a["kind"], a["verdict"] or "none") for a in tables["arcs"])
    how = collections.Counter(e["resolved"] for e in tables["edges"])
    cross = [[e["src"], e["dst"], e["kind"]] for e in tables["edges"]
             if e["src"].split(":")[0] != e["dst"].split(":")[0] and e["resolved"] in NOT_AUDITED]
    audit = [[e["src"], e["dst"], e["kind"], e["resolved"]] for e in tables["edges"]
             if e["resolved"] in ("directory without a verdict file", "missing on both branches", "missing on main",
                                  "missing on the seat's branch")]
    life = [[s["arc"], s["step"], s["date"], s["commit"]] for s in tables["lifecycle"]]
    cover = collections.Counter((a["seat"], a["kind"], a["era"], bool(a["label"])) for a in tables["arcs"])
    labels = [[s, k, e, cover[(s, k, e, True)], cover[(s, k, e, True)] + cover[(s, k, e, False)]]
              for s, k, e in sorted({key[:3] for key in cover})]
    w_labels = {a["id"]: [a["wot"], a["label"], a["label_source"]] for a in tables["arcs"] if a["kind"] == "W"}
    # the board: what is open on each seat, and which relays wait
    tag = {a["key"]: (a["wot"] or ("before the rule" if a["era"] == "before the rule" else "unlabelled"))
           for a in tables["arcs"]}
    open_arcs = [[a["key"], tag[a["key"]], clip(a["claim"], 140), a["source"]] for a in tables["arcs"]
                 if (a["verdict"] or "").upper() == "OPEN"]
    by_label = collections.Counter((a["seat"], a["kind"], (a["verdict"] or "none").upper(), tag[a["key"]])
                                   for a in tables["arcs"])
    waiting = [[r["seat"], r["file"], r["date"], r["age_days"], r["escalated"], r["frm"], r["to"], clip(r["note"], 160),
                r["gate_sees"]] for r in tables["relays"] if r["disposition"] == "OPEN"]
    dispositions = collections.Counter((r["seat"], r["disposition"]) for r in tables["relays"])
    # the atlas: every arc and every dependency (depends_on, rests_on_seat); the cones are drawn in the page
    keys = [a["key"] for a in tables["arcs"]]
    at = {k: i for i, k in enumerate(keys)}
    nodes = [[a["key"], (a["verdict"] or "none").upper(), tag[a["key"]], clip(a["claim"], 110), a["source"]]
             for a in tables["arcs"]]
    how_of = {}
    for e in tables["edges"]:
        how_of.setdefault(e["dst"], e["resolved"])
    ghosts = sorted({e["dst"] for e in tables["edges"] if e["dst"] not in at})
    for g in ghosts:
        at[g] = len(nodes)
        nodes.append([g, "SEAT (not read)" if how_of[g] == "seat branch not read" else "NOT FOUND", "", "", ""])
    # a key held by several folders is drawn once per folder; an edge to the bare id goes to the first
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
            "board": {"open": open_arcs, "stale_days": relay_gate()[2],
                      "by_label": sorted([list(k) + [v] for k, v in by_label.items()]),
                      "waiting": waiting, "dispositions": sorted([list(k) + [v] for k, v in dispositions.items()])},
            "atlas": {"nodes": nodes, "dep": dep, "load": [[k, n] for n, k in load], "cycles": cycles},
            "resolved": sorted(how.items(), key=lambda kv: -kv[1]), "cross": cross, "audit": audit, "life": life,
            "flags": tables["flags"], "curated": {"copied_at": CURATED_AT, "arcs": curated(tables["arcs"]),
                                                  "register": register_row("P-415")}}


def build_all(check=False):
    """tables, commits, manifest and the page's slice; with check, the build is run twice and must agree"""
    tables, commits = build()
    deterministic = None
    if check:
        again, _ = build()
        deterministic = all(digest(tables[n]) == digest(again[n]) for n in tables)
        if not deterministic:
            raise SystemExit("not deterministic: two builds differ")
    manifest = make_manifest(tables, commits, deterministic)
    return tables, commits, manifest, page_data(tables, manifest)


def main():
    ap = argparse.ArgumentParser()
    add_args(ap)
    ap.add_argument("--out", required=True, help="a directory outside the record, or in a path git ignores")
    ap.add_argument("--check", action="store_true", help="build twice and require identical table hashes")
    a = ap.parse_args()
    with tempfile.TemporaryDirectory() as scratch:
        setup(a, scratch)
        out = Path(a.out).resolve()
        if not X.out_ok(out):
            raise SystemExit("--out must lie outside the repository, or in a path git ignores: the index is derived "
                             "and is never committed")
        tables, commits, manifest, page = build_all(a.check)
        m = write(tables, commits, out, manifest["deterministic"])
        (out / "page_index.json").write_text(json.dumps(page, sort_keys=True, ensure_ascii=False,
                                                        separators=(",", ":")) + "\n", encoding="utf-8")
    print(json.dumps({n: t["rows"] for n, t in m["tables"].items()}), "deterministic:", manifest["deterministic"])


if __name__ == "__main__":
    main()
