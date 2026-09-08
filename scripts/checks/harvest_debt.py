#!/usr/bin/env python3
"""harvest-debt -- every seat branch is READ within 21 days of a push, and every seat item has a ledger row.

THE FAILURE THIS EXISTS TO STOP (B1307; MASTERPLAN v3.1 section 1 / 1a rule 3)
------------------------------------------------------------------------------
A request or a result that lives on a seat branch reaches main only at a harvest, and nothing
counted the hours in between: three numbering collisions and three relay lags in eight days
(the SM seat's range note unanswered while main issued a numbering relay it never saw; the
cloud's memos 156-189 found by fetching, nine days late; the physics seat's FC_TO_CC relay of
R64-R72 with no RELAY_LEDGER row, because the relay-debt regex named other lanes).

THE RULE
--------
`docs/HARVEST_LEDGER.md` carries a `## Pins` table: per seat, the commit main last READ the
branch up to (a receipt, advanced only by a landing that read that far). This check reads the
local remote-tracking refs (fetching first with --fetch) and reports, per seat:

    NEW       items whose paths changed in pin..head, split into rowed / unrowed
    BACKLOG   ids in the seat's OWN index with no ledger row            (1a rule 3, one side)
    STALE     ledger rows whose ids resolve to no index entry           (1a rule 3, other side)
    RELAYS    seat-branch relay files with no RELAY_LEDGER row
    MIRROR    origin vs codeberg heads, when the branch lives on both

An unrowed NEW item older than STALE_DAYS fails (exit 2) -- the relay-debt ageing applied to the
branch itself. --strict (used by `gates.py review-due`) fails on ANY debt: a review opens with
the number and cannot close with unread seat results. Exit 1 = instrument integrity (pins
missing/malformed, ledger unparseable) or a --selftest control failing.

The check grades nothing. It counts. Reading and grading is the harvest arcs' work.
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import pathlib
import re
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[2]
LEDGER = ROOT / "docs" / "HARVEST_LEDGER.md"
RELAY_LEDGER = ROOT / "docs" / "RELAY_LEDGER.md"
STALE_DAYS = 21
MAIN_REF = "origin/main"
RELAY_FILE_RE = re.compile(r"[A-Z0-9]+_TO_[A-Z0-9_]+_[0-9]{4}-[0-9]{2}-[0-9]{2}[A-Za-z0-9_.\-]*\.md")
AUDIT_DIR = "reports/physical_bridge_2026_09_05"
FC_DIR = "reports/fresh_physics_seat_2026-09-01"
AUDIT_COMPANION = re.compile(r"_(DESIGN|PRIOR|CONTROL[A-Z_]*|REPAIR[A-Z_]*|DERIVATIVE|CHECKS|GATES|FAILURE|PARTIAL_CHECKS|PARTIAL_GATES)$")

# ---- the seats: branch, remotes, how the ledger names them, how their index and item ids are read ----
SEATS = [
    dict(key="sm", label="SM-derivation seat", branch="standard-model-derivation-0qt6ao",
         remotes=("origin", "codeberg"), cell=("sm-derivation", "sm seat", "sm-seat")),
    dict(key="fc", label="physics seat (fc)", branch="physics-seat-evaluation-8dkbrl",
         remotes=("origin", "codeberg"), cell=("(fc)", "physics seat", "fc ")),
    dict(key="codex", label="codex seat", branch="seat-r001",
         remotes=("origin", "codeberg"), cell=("codex",)),
    dict(key="cc3", label="cc3 (paper seat)", branch="structure-genesis-first",
         remotes=("origin", "codeberg"), cell=("cc3",), cell_not=("braver",)),
    dict(key="hostile", label="hostile-review seat", branch="paper-hostile-review-alero0",
         remotes=("golden_gate",), cell=("hostile",)),
    dict(key="cloud", label="cloud seat", branch="outside-bench",
         remotes=("origin", "codeberg"), cell=("cloud",)),
    dict(key="braver", label="cc3 (braver-questions branch)", branch="b775-braver-questions",
         remotes=("origin", "codeberg"), cell=("braver",)),
    dict(key="qor5up", label="consolidation seat (qor5up)", branch="new-session-qor5up",
         remotes=("origin", "codeberg"), cell=("qor5up", "consolidation")),
    dict(key="audit", label="audit seat", branch="physical-bridge-2026-09-05",
         remotes=("origin", "codeberg"), cell=("audit seat", "audit:")),
]


# Seats name their branch by its SHORT name (the last path segment); the remote-tracking ref is resolved at run time
# (`git for-each-ref refs/remotes/<remote>`), so the repo's own convention -- write a seat branch as `<remote>/<short name>` --
# holds in this file, in the ledgers and in the receipts alike.


# ---------------------------------------------------------------- git helpers
def _git(*args, timeout=60):
    try:
        r = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, timeout=timeout)
        return r.returncode, r.stdout
    except Exception as exc:  # git absent / timeout: soft
        return 1, str(exc)


def _remotes():
    rc, out = _git("remote")
    return set(out.split()) if rc == 0 else set()


def _resolve_branch(remote, short, _cache={}):
    """the remote-tracking ref whose last path segment is `short` (unique on every remote here), or None."""
    if remote not in _cache:
        rc, out = _git("for-each-ref", "--format=%(refname:short)", f"refs/remotes/{remote}")
        _cache[remote] = [l.strip() for l in out.splitlines() if l.strip()] if rc == 0 else []
    hits = [r for r in _cache[remote] if r.rsplit("/", 1)[-1] == short]
    return sorted(hits, key=len)[0] if hits else None


def _rev(ref):
    rc, out = _git("rev-parse", "--verify", "--quiet", ref + "^{commit}")
    return out.strip() if rc == 0 and out.strip() else None


def _ls(ref, path="", recursive=False):
    args = ["ls-tree", "--name-only"] + (["-r"] if recursive else []) + [ref, "--", path] if path else \
        ["ls-tree", "--name-only"] + (["-r"] if recursive else []) + [ref]
    rc, out = _git(*args)
    return [l for l in out.splitlines() if l] if rc == 0 else []


def _show(ref, path):
    rc, out = _git("show", f"{ref}:{path}")
    return out if rc == 0 else ""


def _today():
    env = os.environ.get("OA_HARVEST_TODAY")
    return datetime.date.fromisoformat(env) if env else datetime.date.today()


def _expand(a, b):
    a, b = int(a), int(b)
    return list(range(a, b + 1)) if a <= b and b - a < 400 else [a, b]


def _nums(text, pat):
    """all ids matched by pat, with 'N-M' / 'N–M' ranges expanded (pat must have a single group for N)."""
    out = set()
    for m in re.finditer(pat + r"(?:\s*[–—-]\s*(?:[A-Za-z:]*)?(\d+))?", text):
        n = int(m.group(1))
        out.add(n)
        if m.group(2):
            out.update(_expand(n, m.group(2)))
    return out


# ---------------------------------------------------------------- the ledgers
def read_pins(text):
    """`## Pins` table rows: | key | branch | pin | pinned at | by arc |"""
    pins = {}
    sec = re.search(r"^## Pins.*?(?=^## |\Z)", text, re.M | re.S)
    if not sec:
        return None
    for line in sec.group(0).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and re.fullmatch(r"[a-z0-9]+", cells[0]) and re.fullmatch(r"`?[0-9a-f]{7,40}`?", cells[2]):
            pins[cells[0]] = cells[2].strip("`")
    return pins


def read_rows(text):
    """harvest-ledger rows: | # | seat | item | headline | path @ pin | disposition | main arc | date |"""
    rows = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 6 or not re.fullmatch(r"\d+", cells[0]):
            continue
        rows.append(dict(n=int(cells[0]), seat=cells[1], item=cells[2], path=cells[4] if len(cells) > 4 else "",
                         disp=cells[5] if len(cells) > 5 else "", text=" ".join(cells[1:6])))
    return rows


def relay_ledger_names(text):
    """every `NAME.md` named in a row's FIRST cell (rows write `NAME.md` (on the seat's branch @ pin), or a zip's contents)."""
    out = set()
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        first = line.strip().strip("|").split("|")[0]
        out.update(re.findall(r"([A-Za-z0-9_.\-]+\.md)", first))
    return out


def rows_for(seat, rows):
    keys = tuple(k.lower() for k in seat["cell"])
    nots = tuple(k.lower() for k in seat.get("cell_not", ()))
    out = []
    for r in rows:
        s = r["seat"].lower()
        if any(k in s for k in keys) and not any(k in s for k in nots):
            out.append(r)
    return out


# ---------------------------------------------------------------- per-seat index / id maps
def seat_index(seat, head, main_frontier, main_docs):
    """id -> representative path, from the seat's OWN index (1a rule 3)."""
    k = seat["key"]
    idx = {}
    if k == "sm":
        for d in _ls(head, "frontier/"):
            if d not in main_frontier:
                m = re.match(r"frontier/B(\d{4})_", d)
                if m:
                    idx[f"sm:B{m.group(1)}"] = d
        for f in _ls(head, "docs/"):
            if f.endswith(".md") and f not in main_docs:
                idx[pathlib.Path(f).stem] = f
    elif k == "fc":
        for m in re.finditer(r"^\|\s*\*\*R(\d+)\*\*", _show(head, f"{FC_DIR}/INDEX_R56-R72.md"), re.M):
            idx[f"R{int(m.group(1))}"] = f"{FC_DIR}/INDEX_R56-R72.md"
        for d in _ls(head, f"{FC_DIR}/recompute/"):
            m = re.match(rf"{re.escape(FC_DIR)}/recompute/(R|H)(\d+)_", d)
            if m:
                idx[f"{m.group(1)}{int(m.group(2))}"] = d
    elif k == "codex":
        for m in re.finditer(r"^\|\s*(R\d{3}[A-Z]?)\s*\|([^|]*)\|", _show(head, "MANIFEST.md"), re.M):
            idx[m.group(1)] = m.group(2).strip()[:200]
    elif k == "cc3":
        for d in _ls(head, "frontier/"):
            m = re.match(r"frontier/(B8\d{3})_", d)
            if m:
                idx[m.group(1)] = d
    elif k == "hostile":
        man = _show(head, "session_handoff/MANIFEST.md")
        for m in re.finditer(r"^\|\s*(\d+)\s*\|\s*([A-Za-z0-9_\-]+)\.md", man, re.M):
            idx[f"memo {int(m.group(1))}"] = f"session_handoff/memos/{m.group(2)}.md"
        aliased = set(idx.values())
        for f in _ls(head, "session_handoff/memos/"):
            if f.endswith(".md") and f not in aliased:
                idx[pathlib.Path(f).stem] = f
    elif k == "cloud":
        for m in re.finditer(r"^\|\s*(\d+)\s*\|\s*([^|]*)\|", _show(head, "outside_bench/INDEX.md"), re.M):
            idx[f"memo {int(m.group(1))}"] = "outside_bench/" + m.group(2).strip().split()[0] if m.group(2).strip() else "outside_bench/INDEX.md"
    elif k == "braver":
        for d in _ls(head, "frontier/"):
            if d not in main_frontier:
                m = re.match(r"frontier/(B\d{3})_", d)
                idx[m.group(1) if m else d.split("/", 1)[1]] = d
    elif k == "qor5up":
        for d in _ls(head, "frontier/"):
            if d not in main_frontier:
                m = re.match(r"frontier/(B10\d{2})_", d)
                if m:
                    idx[m.group(1)] = d
    elif k == "audit":
        for f in _ls(head, f"{AUDIT_DIR}/"):
            if f.endswith(".md"):
                stem = pathlib.Path(f).stem
                if stem == "README" or AUDIT_COMPANION.search(stem):
                    continue
                idx[stem] = f
    return idx


def path_ids(seat, path, idx):
    """the item id(s) a changed path belongs to; empty = unmapped (reported separately)."""
    k = seat["key"]
    out = set()
    if k == "sm":
        m = re.match(r"frontier/B(\d{4})_", path)
        if m and f"sm:B{m.group(1)}" in idx:
            out.add(f"sm:B{m.group(1)}")
        if path.startswith("docs/") and pathlib.Path(path).stem in idx:
            out.add(pathlib.Path(path).stem)
    elif k == "fc":
        for pat in (rf"{re.escape(FC_DIR)}/R(\d+)_", rf"{re.escape(FC_DIR)}/computations/r(\d+)[a-z]?_",
                    rf"{re.escape(FC_DIR)}/recompute/R(\d+)_"):
            m = re.match(pat, path)
            if m:
                out.add(f"R{int(m.group(1))}")
        m = re.match(rf"{re.escape(FC_DIR)}/recompute/(H\d)_", path)
        if m:
            out.add(m.group(1))
    elif k == "codex":
        m = re.search(r"/r(\d{3})([a-z]?)_", path)
        if m:
            out.add(f"R{m.group(1)}{m.group(2).upper()}")
        for rid, frag in idx.items():
            if path.split("/")[-1] and path.split("/")[-1] in frag:
                out.add(rid)
    elif k == "cc3":
        m = re.match(r"frontier/(B8\d{3})_", path)
        if m:
            out.add(m.group(1))
    elif k == "hostile":
        m = re.match(r"session_handoff/memos/([A-Za-z0-9_\-]+)\.md", path)
        if m:
            for rid, p in idx.items():
                if p == path:
                    out.add(rid)
    elif k == "cloud":
        for rid, p in idx.items():
            if p == path:
                out.add(rid)
        if path.startswith("outside_bench/certificates/") or path.startswith("outside_bench/outputs/"):
            stem = pathlib.Path(path).stem.replace("_out", "")
            for m in re.finditer(r"^\|\s*(\d+)\s*\|[^|]*\|([^|]*)\|", CLOUD_INDEX_CACHE.get("text", ""), re.M):
                if stem in m.group(2):
                    out.add(f"memo {int(m.group(1))}")
    elif k in ("braver", "qor5up"):
        m = re.match(r"frontier/([^/]+)/", path)
        if m:
            d = "frontier/" + m.group(1)
            for rid, p in idx.items():
                if p == d:
                    out.add(rid)
    elif k == "audit":
        m = re.match(rf"{re.escape(AUDIT_DIR)}/([A-Za-z0-9_]+)\.md$", path)
        if m:
            stem = m.group(1)
            base = AUDIT_COMPANION.sub("", stem)
            if base in idx:
                out.add(base)
    return out


CLOUD_INDEX_CACHE = {}


def row_ids(seat, row, idx):
    """the seat item ids a ledger row names (by the seat's id grammar; ranges expanded)."""
    k = seat["key"]
    t = row["text"]
    out = set()
    if k == "sm":
        out |= {f"sm:B{n}" for n in _nums(t, r"(?:sm:B|sB)(\d{4})")}
        for rid in idx:
            if not rid.startswith("sm:B") and rid in t:
                out.add(rid)
    elif k == "fc":
        out |= {f"R{n}" for n in _nums(t, r"\bR(\d{1,2})\b")}
        out |= {m.group(0) for m in re.finditer(r"\bH[12]\b", t)}
    elif k == "codex":
        for m in re.finditer(r"\bR(\d{3})([A-Z]?)\b(?:\s*[–—-]\s*R?(\d{3})\b)?", t):
            out.add(f"R{m.group(1)}{m.group(2)}")
            if m.group(3):
                out |= {f"R{n:03d}" for n in _expand(m.group(1), m.group(3))}
    elif k == "cc3":
        out |= {f"B{n}" for n in _nums(t, r"\bB(8\d{3})\b")}
    elif k == "hostile":
        out |= {f"memo {n}" for n in _nums(t, r"\bmemos?\s*#?(\d{1,2})\b")}
        for rid in idx:
            if not rid.startswith("memo ") and rid in t:
                out.add(rid)
    elif k == "cloud":
        # the cloud's INDEX starts at memo 30; memos 1-29 are the hostile-review seat's (golden_gate) by its own scope note
        out |= {f"memo {n}" for n in _nums(t, r"\bmemos?\s+(\d{1,3})\b") if n >= 30}
    elif k == "braver":
        out |= {f"B{n}" for n in _nums(t, r"\bB(7\d{2})\b")}
        for rid in idx:
            if not rid.startswith("B") and rid in t:
                out.add(rid)
    elif k == "qor5up":
        out |= {f"B{n}" for n in _nums(t, r"\bB(10[2-5]\d)\b")}
    elif k == "audit":
        for rid in idx:
            if re.search(rf"\b{re.escape(rid)}\b", t):
                out.add(rid)
    return out & set(idx) if k in ("sm", "audit", "hostile", "braver") else out


# ---------------------------------------------------------------- the pure reconciliation (selftested)
def reconcile(index_ids, rows_ids, new_ids_age, today_days=None):
    """index_ids: set; rows_ids: list of sets (ids each ledger row names); new_ids_age: {id: age_days}.
    Returns the five lists the controls plant against."""
    rowed = set().union(*rows_ids) if rows_ids else set()
    new_unrowed = sorted(i for i in new_ids_age if i not in rowed)
    new_rowed = sorted(i for i in new_ids_age if i in rowed)
    backlog = sorted(i for i in index_ids if i not in rowed)
    stale = sorted(i for i in rowed if i not in index_ids)
    aged = sorted(i for i in new_unrowed if new_ids_age[i] > STALE_DAYS)
    return dict(new_unrowed=new_unrowed, new_rowed=new_rowed, backlog=backlog, stale_rows=stale, aged=aged)


def selftest():
    fails = []
    r = reconcile({"a", "b", "c"}, [{"a"}, {"b"}], {"c": 3, "b": 1})
    if r["new_unrowed"] != ["c"]:
        fails.append(f"planted NEW unrowed item not reported: {r['new_unrowed']}")
    if "a" in r["new_unrowed"] or "a" in r["new_rowed"]:
        fails.append("harvested unchanged item reported as new")
    r2 = reconcile({"a", "b", "c", "d"}, [{"a"}, {"b"}], {})
    if r2["backlog"] != ["c", "d"] or "d" not in r2["backlog"]:
        fails.append(f"planted missing index id not in BACKLOG: {r2['backlog']}")
    r3 = reconcile({"a", "b"}, [{"a"}, {"z"}], {})
    if r3["stale_rows"] != ["z"]:
        fails.append(f"planted stale row not flagged: {r3['stale_rows']}")
    r4 = reconcile({"c"}, [], {"c": 22})
    r5 = reconcile({"c"}, [], {"c": 20})
    if r4["aged"] != ["c"] or r5["aged"] != []:
        fails.append(f"ageing wrong: 22d -> {r4['aged']}, 20d -> {r5['aged']}")
    # the relay-file grammar sees every lane
    for name in ("SM_TO_CC_2026-09-08_THE_TOWER.md", "FC_TO_CC_2026-09-06_THE_LIFT_AND_THE_THIRD_ROOT.md",
                 "FAB5_TO_CC_2026-09-01_reply.md", "CODEX_TO_CC_2026-09-02_FREE_DECK_CS.md",
                 "CLOUD_TO_CC_2026-09-08_Q1_THE_QUANTUM_FACE.md", "CC3_TO_CC_2026-08-29_THE_MIRROR_IS_c_PAPER_IV_IS_INSIDE_B1200.md"):
        if not RELAY_FILE_RE.fullmatch(name):
            fails.append(f"relay grammar misses {name}")
    for name in ("FINDINGS.md", "HOW_TO_READ.md", "THE_TOWER_2026-09-08.md"):
        if RELAY_FILE_RE.fullmatch(name):
            fails.append(f"relay grammar over-matches {name}")
    # the ledger grammar on a synthetic pins table
    pins = read_pins("# x\n\n## Pins\n\n| seat | branch | pin | pinned at | by arc |\n|---|---|---|---|---|\n| sm | b | `0dffacd4` | 2026-09-09 | B1306 |\n\n## Next\n")
    if pins != {"sm": "0dffacd4"}:
        fails.append(f"pins table not read: {pins}")
    return fails


def named_on_main(names, _cache={}):
    """the subset of relay names that occur anywhere in main's tracked docs/ or frontier/ text (one git grep; no row, but named)."""
    key = tuple(names)
    if key in _cache:
        return _cache[key]
    if not names:
        _cache[key] = set(); return set()
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as fh:
        fh.write("\n".join(names)); tmp = fh.name
    rc, out = _git("grep", "-o", "-h", "-F", "-f", tmp, "HEAD", "--", "docs", "frontier", timeout=120)
    os.unlink(tmp)
    found = set(out.split()) if rc in (0, 1) else set()
    _cache[key] = found
    return found


# ---------------------------------------------------------------- the live run
def run(fetch=False, strict=False):
    t0 = time.time()
    report = dict(today=str(_today()), seats={}, integrity=[], summary={})
    if fetch:
        rc, out = _git("fetch", "--all", "--quiet", timeout=300)
        report["fetched"] = (rc == 0)
    if not LEDGER.is_file():
        report["integrity"].append(f"{LEDGER.relative_to(ROOT)} MISSING")
        return report
    ltext = LEDGER.read_text(encoding="utf-8", errors="ignore")
    pins = read_pins(ltext)
    if pins is None:
        report["integrity"].append("HARVEST_LEDGER has no `## Pins` table")
        return report
    rows = read_rows(ltext)
    rnames = relay_ledger_names(RELAY_LEDGER.read_text(encoding="utf-8", errors="ignore")) if RELAY_LEDGER.is_file() else set()
    remotes = _remotes()
    overrides = dict(kv.split("=", 1) for kv in os.environ.get("OA_HARVEST_PIN_OVERRIDE", "").split(",") if "=" in kv)
    main_ref = MAIN_REF if _rev(MAIN_REF) else "HEAD"
    main_frontier = set(_ls(main_ref, "frontier/"))
    main_docs = set(_ls(main_ref, "docs/"))
    main_relays = {pathlib.Path(p).name for p in _ls(main_ref, "", recursive=True) if RELAY_FILE_RE.fullmatch(pathlib.Path(p).name)}
    today = _today()
    totals = dict(new_unrowed=0, backlog=0, stale_rows=0, relays_unrowed=0, aged=0, index=0, mirror_lag=0, skipped=0)

    for seat in SEATS:
        k = seat["key"]
        s = dict(label=seat["label"], branch=f"{seat['remotes'][0]}/{seat['branch']}")
        report["seats"][k] = s
        canon = seat["remotes"][0]
        if canon not in remotes:
            s["skipped"] = f"remote {canon} not configured here"
            totals["skipped"] += 1
            continue
        ref = _resolve_branch(canon, seat["branch"])
        head = _rev(ref) if ref else None
        if not head:
            s["skipped"] = f"ref {canon}/{seat['branch']} not fetched"
            totals["skipped"] += 1
            if strict:
                report["integrity"].append(f"{k}: {s['skipped']}")
            continue
        pin_short = overrides.get(k, pins.get(k))
        if not pin_short:
            report["integrity"].append(f"{k}: no pin in the `## Pins` table")
            continue
        pin = _rev(pin_short)
        if not pin:
            report["integrity"].append(f"{k}: pin {pin_short} does not resolve")
            continue
        s["head"], s["pin"] = head[:8], pin[:8]
        rc, out = _git("rev-list", "--count", f"{pin}..{head}")
        s["commits_since_pin"] = int(out.strip() or 0) if rc == 0 else None
        # index + rows
        if k == "cloud":
            CLOUD_INDEX_CACHE["text"] = _show(head, "outside_bench/INDEX.md")
        idx = seat_index(seat, head, main_frontier, main_docs)
        srows = rows_for(seat, rows)
        rows_ids = [row_ids(seat, r, idx) for r in srows]
        # NEW: changed paths in pin..head with newest change time
        rc, log = _git("log", "--format=%x1e%ct", "--name-only", f"{pin}..{head}")
        age_by_path = {}
        if rc == 0:
            for block in log.split("\x1e"):
                lines = [l for l in block.strip().splitlines() if l.strip()]
                if not lines:
                    continue
                ct = int(lines[0])
                for p in lines[1:]:
                    age_by_path[p] = max(age_by_path.get(p, 0), ct)
        new_age, unmapped = {}, []
        for p, ct in age_by_path.items():
            ids = path_ids(seat, p, idx)
            age = (today - datetime.date.fromtimestamp(ct)).days
            if ids:
                for i in ids:
                    new_age[i] = min(new_age.get(i, 10 ** 6), age)
            elif not RELAY_FILE_RE.fullmatch(pathlib.Path(p).name):
                unmapped.append(p)
        rec = reconcile(set(idx), rows_ids, new_age)
        s.update(index_size=len(idx), rows=len(srows), changed_paths=len(age_by_path), unmapped_changed=sorted(unmapped)[:12],
                 unmapped_count=len(unmapped), new_unrowed=rec["new_unrowed"], new_rowed=rec["new_rowed"],
                 new_age={i: new_age[i] for i in rec["new_unrowed"]}, backlog=rec["backlog"], stale_rows=rec["stale_rows"], aged=rec["aged"])
        # relays on the seat branch without a RELAY_LEDGER row (seat-only files)
        relays = [p for p in _ls(head, "", recursive=True) if RELAY_FILE_RE.fullmatch(pathlib.Path(p).name)
                  and pathlib.Path(p).name not in main_relays]
        s["relays_on_branch"] = len(relays)
        s["relays_unrowed"] = sorted(pathlib.Path(p).name for p in relays if pathlib.Path(p).name not in rnames)
        s["relays_unrowed_named_on_main"] = sorted(n for n in s["relays_unrowed"] if n in named_on_main(s["relays_unrowed"]))
        # mirror lag
        if len(seat["remotes"]) > 1 and seat["remotes"][1] in remotes:
            oref = _resolve_branch(seat["remotes"][1], seat["branch"])
            other = _rev(oref) if oref else None
            if other and other != head:
                rc1, a = _git("rev-list", "--count", f"{other}..{head}")
                rc2, b = _git("rev-list", "--count", f"{head}..{other}")
                s["mirror_lag"] = f"{seat['remotes'][1]} {a.strip()} behind / {b.strip()} ahead of {canon}"
                totals["mirror_lag"] += 1
            elif not other:
                s["mirror_lag"] = f"{seat['remotes'][1]} has no {seat['branch']}"
        totals["new_unrowed"] += len(rec["new_unrowed"]); totals["backlog"] += len(rec["backlog"])
        totals["stale_rows"] += len(rec["stale_rows"]); totals["relays_unrowed"] += len(s["relays_unrowed"])
        totals["aged"] += len(rec["aged"]); totals["index"] += len(idx)
    report["summary"] = totals
    report["seconds"] = round(time.time() - t0, 1)
    return report


def print_report(rep, verbose=True):
    print(f"  harvest-debt ({rep['today']}): {rep['summary'].get('index', 0)} seat-index ids across {len(rep['seats'])} seats; "
          f"NEW unrowed {rep['summary'].get('new_unrowed', 0)}, BACKLOG {rep['summary'].get('backlog', 0)}, STALE rows {rep['summary'].get('stale_rows', 0)}, "
          f"relays without a row {rep['summary'].get('relays_unrowed', 0)}, aged past {STALE_DAYS}d {rep['summary'].get('aged', 0)}, mirror lag {rep['summary'].get('mirror_lag', 0)}"
          f"{'; skipped ' + str(rep['summary'].get('skipped')) if rep['summary'].get('skipped') else ''} [{rep.get('seconds', '?')}s]")
    for k, s in rep["seats"].items():
        if "skipped" in s:
            print(f"    {k:<8} SKIPPED: {s['skipped']}")
            continue
        print(f"    {k:<8} head {s['head']} pin {s['pin']} (+{s['commits_since_pin']} commits) index {s['index_size']} rows {s['rows']} | "
              f"NEW unrowed {len(s['new_unrowed'])} rowed {len(s['new_rowed'])} | backlog {len(s['backlog'])} | stale {len(s['stale_rows'])} | "
              f"relays unrowed {len(s['relays_unrowed'])}/{s['relays_on_branch']} (named on main without a row: {len(s.get('relays_unrowed_named_on_main', []))})"
              + (f" | {s['mirror_lag']}" if s.get("mirror_lag") else ""))
        if verbose:
            if s["new_unrowed"]:
                print(f"             NEW unrowed: " + ", ".join(f"{i} ({s['new_age'][i]}d)" for i in s["new_unrowed"]))
            if s["new_rowed"]:
                print(f"             NEW but rowed (re-read at the next harvest): " + ", ".join(s["new_rowed"]))
            if s["unmapped_count"]:
                print(f"             changed paths not mapped to an item: {s['unmapped_count']} (e.g. {', '.join(s['unmapped_changed'][:4])})")
            if s["stale_rows"]:
                print(f"             STALE rows (ids in the ledger, not in the seat's index): " + ", ".join(s["stale_rows"][:20]))
            if s["relays_unrowed"]:
                print(f"             relays without a RELAY_LEDGER row: " + ", ".join(s["relays_unrowed"][:6]) + (" …" if len(s["relays_unrowed"]) > 6 else ""))
            if s["aged"]:
                print(f"             AGED (unrowed > {STALE_DAYS}d): " + ", ".join(s["aged"]))
    for line in rep.get("integrity", []):
        print(f"    INTEGRITY: {line}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--strict", action="store_true", help="fail on any debt (review-due)")
    ap.add_argument("--json", metavar="PATH")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        fails = selftest()
        print("  harvest-debt selftest: " + ("PASS (5 planted controls + grammars)" if not fails else "FAIL"))
        for f in fails:
            print(f"    {f}")
        return 1 if fails else 0
    rep = run(fetch=a.fetch, strict=a.strict)
    if a.json:
        pathlib.Path(a.json).write_text(json.dumps(rep, indent=1), encoding="utf-8")
    print_report(rep, verbose=not a.quiet)
    if rep["integrity"]:
        return 1
    t = rep["summary"]
    if a.strict and (t["new_unrowed"] or t["backlog"] or t["stale_rows"] or t["relays_unrowed"]):
        print(f"  harvest-debt --strict: DEBT OPEN — a review cannot close with unread seat results")
        return 1
    if t["aged"]:
        print(f"  harvest-debt: {t['aged']} unrowed seat item(s) older than {STALE_DAYS} days — read the branch or row the item")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
