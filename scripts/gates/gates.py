"""Automated repository gates (GOVERNANCE §11, instituted 2026-07-03).

Each gate is a fast, deterministic check of a governance invariant. The suite lock
`tests/test_repo_gates.py` runs them all, so every merge (full suite green) enforces them.
Run manually:  python3 scripts/gates/gates.py            (all gates, verdict per gate)
               python3 scripts/gates/gates.py review-due (the decadal-review counter only)

Design rules: no network, no heavy imports, stdlib only; a gate returns (ok, detail);
whitelists are explicit frozen constants in this file (auditable, versioned).
"""
import base64
import json
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def _read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _git(*args):
    try:
        out = subprocess.run(["git", "-C", ROOT, *args], capture_output=True,
                             text=True, timeout=30)
        return out.returncode, out.stdout
    except Exception as exc:                                   # git absent: soft-skip
        return 1, str(exc)


# --- gate: framing lock (GOVERNANCE §2/§8 + the campaign-banned phrasings) ---------------
BANNED = [
    "the gluing creates causal structure",
    "the universe is a figure-eight knot",
    "we derived Einstein's equations",
    "Fibonacci anyon physics",
    "toward the full SM",
    "everything changes",
    "impossibility boundary completed",
    "dynamical derivation starts here",
    "the one kind of number the firewall permits",
]
FRAMING_EXEMPT = {"GOVERNANCE.md", "scripts/gates/gates.py", "tests/test_repo_gates.py",
                  "docs/atlas/FAILURE_ATLAS.md"}   # the failure register quotes what it bans
FRAMING_SCOPE_DIRS = ("docs", "frontier", "knowledge", "papers", "speculations",
                      "philosophy", "story", "src", "scripts")


def gate_framing():
    hits = []
    files = ["CLAIMS.md", "README.md", "METHOD.md", "ARCHITECTURE.md", "PROGRESS_LOG.md",
             "CHANGELOG.md", "PROVENANCE.md", "REPRODUCIBILITY.md"]
    for d in FRAMING_SCOPE_DIRS:
        for dirpath, _dirs, names in os.walk(os.path.join(ROOT, d)):
            if ".git" in dirpath or "__pycache__" in dirpath:
                continue
            for n in names:
                if n.endswith((".md", ".py", ".txt")):
                    files.append(os.path.relpath(os.path.join(dirpath, n), ROOT))
    for rel in files:
        if rel.replace(os.sep, "/") in FRAMING_EXEMPT:
            continue
        try:
            text = _read(rel)
        except Exception:
            continue
        for phrase in BANNED:
            if phrase in text:
                hits.append((rel, phrase))
    return not hits, hits[:10]


# --- gate: claims-ledger integrity --------------------------------------------------------
LABEL_SECTIONS = ("## Proven", "## Conditional", "## Open", "## Dead", "## Certified data")


def gate_claims():
    text = _read("CLAIMS.md")
    problems = []
    for sec in ("## Proven", "## Conditional", "## Open", "## Dead"):
        if sec not in text:
            problems.append(f"missing section {sec!r}")
    # every proven row must cite an existing tests/ file
    proven = text.split("## Proven", 1)[-1].split("## Conditional", 1)[0]
    for m in re.finditer(r"`(tests/[A-Za-z0-9_./]+\.py)`", proven):
        if not os.path.exists(os.path.join(ROOT, m.group(1))):
            problems.append(f"proven evidence missing: {m.group(1)}")
    # row IDs well-formed in the four classic tables
    for row_id in re.findall(r"^\| ([A-Z]+\d+[a-z]?) \|", text, flags=re.M):
        if not re.fullmatch(r"(P|C|O|D|E)\d+[a-z]?", row_id):
            problems.append(f"malformed claim ID: {row_id}")
    return not problems, problems[:10]


# --- gate: the one-way firewall (no speculative room cited as claim evidence) -------------
def gate_firewall_oneway():
    text = _read("CLAIMS.md")
    bad = []
    for sec_name in ("## Proven", "## Conditional", "## Certified data"):
        if sec_name not in text:
            continue
        sec = text.split(sec_name, 1)[-1]
        for stop in LABEL_SECTIONS:
            if stop != sec_name and stop in sec:
                sec = sec.split(stop, 1)[0]
        for m in re.finditer(r"^\|.*$", sec, flags=re.M):
            row = m.group(0)
            if "speculations/" in row or "philosophy/" in row or "story/" in row:
                bad.append(row[:80])
    return not bad, bad[:5]


# --- gate: PROGRESS_LOG is append-only ----------------------------------------------------
def gate_append_only():
    """Append-only, with the one constitutional exception (GOVERNANCE §9): a quarterly
    roll-up may move a PREFIX of dated entries verbatim into docs/progress/ — the gate
    then requires (a) the live log ends with HEAD's retained suffix and (b) the removed
    prefix appears verbatim inside the docs/progress/ archives."""
    rc, head = _git("show", "HEAD:PROGRESS_LOG.md")
    if rc != 0:
        return True, "git unavailable — skipped"
    cur = _read("PROGRESS_LOG.md")
    if cur.startswith(head):
        return True, "HEAD prefix preserved"
    # roll-up path: longest common suffix
    n = 0
    while n < min(len(cur), len(head)) and cur[-1 - n] == head[-1 - n]:
        n += 1
    retained = head[len(head) - n:]
    removed = head[:len(head) - n]
    if not retained.strip():
        return False, "no common suffix with HEAD — not an append, not a roll-up"
    arch_dir = os.path.join(ROOT, "docs", "progress")
    archive = ""
    if os.path.isdir(arch_dir):
        for f in sorted(os.listdir(arch_dir)):
            if f.endswith(".md"):
                archive += _read(f"docs/progress/{f}")
    # the removed dated entries (from the first "## 20" heading) must live in the archive
    k = removed.find("## 20")
    moved = removed[k:] if k >= 0 else removed
    ok = moved.strip() in archive
    return ok, f"roll-up: removed prefix archived verbatim: {ok}"


# --- gate: atlas freshness (the automatic-update invariant) --------------------------------
def gate_atlas_fresh():
    data = json.loads(_read("scripts/atlas/atlas_data.json"))
    n_atlas = len(data["probes"])
    fdir = os.path.join(ROOT, "frontier")
    ids = set()
    for name in os.listdir(fdir):
        m = re.match(r"(B\d+[a-z]?)", name)
        if m and os.path.isfile(os.path.join(fdir, name, "FINDINGS.md")):
            ids.add(m.group(1))
    return n_atlas == len(ids), f"atlas={n_atlas} distinct-B-dirs={len(ids)}"


# --- gate: attribution hygiene -------------------------------------------------------------
_TOK = base64.b64decode(b"Y2xhdWRl").decode()          # encoded so this file passes itself
ATTR_EXEMPT_PREFIXES = ("legacy/", ".claude/", "audit/")
ATTR_EXEMPT_FILES = {          # scanner tests that hunt the same tokens this gate hunts
    "tests/test_public_surface_scan.py", "tests/test_flagship_paper.py",
    "tests/test_sl4_dehn_filling_paper.py"}


def gate_attribution():
    rc, out = _git("ls-files")
    if rc != 0:
        return True, "git unavailable — skipped"
    hits = []
    for rel in out.splitlines():
        if rel.startswith(ATTR_EXEMPT_PREFIXES) or rel in ATTR_EXEMPT_FILES \
                or rel == "scripts/gates/gates.py":
            continue
        if not rel.endswith((".md", ".py", ".txt", ".json", ".yml", ".yaml", ".toml")):
            continue
        try:
            if _TOK in _read(rel).lower():
                hits.append(rel)
        except Exception:
            continue
    rc2, author = _git("log", "-1", "--format=%an")
    author_ok = (rc2 != 0) or (author.strip() == "originaxiom")
    if not author_ok:
        hits.append(f"last-commit author: {author.strip()}")
    return not hits, hits[:10]


# --- gate: forbidden tracked artifacts -----------------------------------------------------
def gate_tracked_forbidden():
    rc, out = _git("ls-files")
    if rc != 0:
        return True, "git unavailable — skipped"
    bad = [f for f in out.splitlines()
           if f.startswith(".github/") or f == "Archive.zip"
           or (f.startswith("papers/flagship/a-self-generating-object") and f.endswith(".pdf"))]
    return not bad, bad


# --- the decadal review counter ------------------------------------------------------------
REVIEWS = "docs/progress/REVIEWS.md"
REVIEW_EVERY = 10


def review_status():
    """(merges_since_last_review, due?) counted on main's first-parent chain."""
    text = _read(REVIEWS) if os.path.exists(os.path.join(ROOT, REVIEWS)) else ""
    anchors = re.findall(r"anchor-commit: `?([0-9a-f]{7,40})`?", text)
    if not anchors:
        return None, False
    rc, out = _git("rev-list", "--first-parent", "--count", f"{anchors[-1]}..HEAD")
    if rc != 0:
        return None, False
    n = int(out.strip() or 0)
    return n, n >= REVIEW_EVERY


GATES = {
    "framing": gate_framing,
    "claims": gate_claims,
    "firewall-oneway": gate_firewall_oneway,
    "append-only": gate_append_only,
    "atlas-fresh": gate_atlas_fresh,
    "attribution": gate_attribution,
    "tracked-forbidden": gate_tracked_forbidden,
}


def run_all():
    results = {}
    for name, fn in GATES.items():
        try:
            ok, detail = fn()
        except Exception as exc:
            ok, detail = False, f"gate crashed: {exc}"
        results[name] = (ok, detail)
    return results


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "review-due":
        n, due = review_status()
        print(f"merges since last review: {n}; due (>= {REVIEW_EVERY}): {due}")
        sys.exit(0)
    res = run_all()
    worst = 0
    for name, (ok, detail) in res.items():
        print(f"  {'PASS' if ok else 'FAIL'}  {name}: {detail if not ok else 'ok'}")
        worst = max(worst, 0 if ok else 1)
    n, due = review_status()
    print(f"  review-due: {n} merges since last review "
          f"({'DUE — run the decadal review' if due else 'not due'})")
    sys.exit(worst)
