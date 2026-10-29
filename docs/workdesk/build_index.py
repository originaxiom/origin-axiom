#!/usr/bin/env python3
"""The Ledger Desk's index (a proposal's prototype, not an arc; see THE_LEDGER_DESK.md). Read-only over two refs, HEAD
(this seat's branch) and origin/main, it writes one index outside the record:

  arcs       one row per arc, keyed (seat, id): main's and this seat's B arcs from frontier/*/arc_verdict.json, and the
             W arcs from NOTE's status table. A B directory on origin/main is main's; one only on HEAD is this seat's
             (sm). Each row carries its source path, the ref, the commit, and the file's blob.
  edges      depends_on, supersedes and superseded_by from the verdict files, and main's rests_on_seat and cites_seat
             (to sm: ids). A bare id resolves within the citing arc's seat, then at main, then at the other seat; each
             edge says which, or that its target is a directory without a verdict file, or on neither branch.
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

SCHEMA = 1
REFS = {"sm": "HEAD", "main": "origin/main"}
WEAVE_START = "2026-10-07"
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
    rows = []
    for seat, paths in (("main", files["main"]), ("sm", {p: b for p, b in files["sm"].items()
                                                       if p not in files["main"]})):
        for path, blob in sorted(paths.items()):
            d = blobs.get(blob) or {}
            dir_id = path.split("/")[1].split("_")[0]
            wot = d.get("weave_or_thread")
            rows.append({"key": f"{seat}:{dir_id}", "seat": seat, "kind": "B", "id": dir_id,
                         "verdict": d.get("verdict"),
                         "scope": (wot.split()[0] if isinstance(wot, str) and wot else None),
                         "claim": (d.get("claim_one_line") or "")[:300], "source": path, "ref": REFS[seat],
                         "commit": commits[seat], "blob": blob, "_d": d})
    return rows, commits


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
    rows = []
    for arc, status, tag, st, what, line, first, last in X.arcs():
        rows.append({"key": f"sm:{arc}", "seat": "sm", "kind": "W", "id": arc, "verdict": status,
                     "scope": tag.lower() or None, "claim": what[:300],
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


def build():
    rows, commits = b_arcs()
    w = w_rows(commits["sm"])
    edges = b_edges(rows, {r["key"] for r in rows + w})
    rows += w
    rows.sort(key=lambda r: (r["seat"], r["kind"], int(re.sub(r"\D", "", r["id"]) or 0), r["id"]))
    steps, flags = lifecycle()
    return {"arcs": rows, "edges": edges, "cells": cells(), "lifecycle": steps, "flags": flags}, commits


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
    return {"manifest": manifest, "counts": sorted([list(k) + [v] for k, v in counts.items()]),
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
