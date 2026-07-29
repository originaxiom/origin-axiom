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
ATTR_EXEMPT_PREFIXES = ("legacy/", ".claude/", "audit/",
                        # preserved forensic review artifacts (hash-pinned; quote seat transcript
                        # paths verbatim as provenance pins — editing them would break their seals)
                        "frontier/B742_negatives_hunt_p1/reviews/")
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
    # Cross-seat RELAY files are correspondence, not substrate, and must not be committed
    # LOOSE (at root or in docs/). Relays ARCHIVED INSIDE a frontier arc directory are that
    # arc's evidence record and are allowed — the same distinction the path guard already
    # makes for cc2_packets ("archived cross-seat packet records: history, not live code").
    # One loose relay predates this rule and is grandfathered: GOVERNANCE §12 forbids removing
    # banked paths, so the gate's job is to stop the NEXT one.
    GRANDFATHERED_RELAYS = {"CC3_TO_CC_2026-07-22_p3_complete.md"}
    bad = [f for f in out.splitlines()
           if f.startswith(".github/") or f == "Archive.zip"
           or (f.startswith("papers/flagship/a-self-generating-object") and f.endswith(".pdf"))
           or (re.match(r"(CC_TO_CC3|CC3_TO_CC|CC_TO_CC2|CC2_TO_CC)[^/]*\.md$", f)
               and os.path.basename(f) not in GRANDFATHERED_RELAYS)
           or (f.startswith("docs/")
               and re.search(r"/(CC_TO_CC3|CC3_TO_CC|CC_TO_CC2|CC2_TO_CC)[^/]*\.md$", f))]
    return not bad, bad


# --- the decadal review counter ------------------------------------------------------------
REVIEWS = "docs/progress/REVIEWS.md"
REVIEW_EVERY = 20  # raised from 10 (owner, 2026-07-14): merge cadence densified; ~10 fired too often


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


def gate_review_actions():
    """GOVERNANCE §15: action-item blocks in REVIEWS.md. Any block that is
    NOT the latest must contain zero open `- [ ]` items (resolved `[x]` or
    carried `[>]` only). The latest block's open count is advisory."""
    path = os.path.join(ROOT, REVIEWS)
    if not os.path.exists(path):
        # FAIL-CLOSED (restart-resistance audit): deleting REVIEWS.md silently disabled BOTH
        # this gate and views-fresh. The review register is constitutive (GOVERNANCE §15).
        if os.path.isdir(os.path.dirname(path)):
            return False, "docs/progress/ exists but REVIEWS.md is MISSING -- §15 register gone"
        return True, "no docs/progress/ yet"
    text = _read(REVIEWS)
    blocks = re.findall(r"### Action items \(Review [^)]+\)\n((?:- \[.\][^\n]*\n?)+)",
                        text)
    if not blocks:
        return True, "no action-item blocks yet (pre-§15 reviews)"
    stale_open = 0
    for b in blocks[:-1]:
        stale_open += len(re.findall(r"^- \[ \]", b, re.M))
    if stale_open:
        return False, (f"{stale_open} open item(s) in a superseded review's "
                       "block — resolve [x] or carry [>] them")
    latest_open = len(re.findall(r"^- \[ \]", blocks[-1], re.M))
    return True, f"ok ({latest_open} open in the latest block, advisory)"



# --- gate: navigation-view freshness (owner, 2026-07-29; Review 32) --------------------------
# GOVERNANCE §12 ("freeze the substrate; GENERATE THE VIEWS") + §15 (reviews).
# The decadal review must REFRESH the navigation views, not just the ledgers. Review 32 found
# MASTERPLAN 25 days / ~55 arcs stale, LEAD_REGISTER listing already-closed items as its top
# HIGH targets, and the Maass work off-register for four arcs because nobody could see the
# register was stale. A written rule did not prevent that; this gate does.
VIEWS = (
    "README.md",          # the front door: it described B152–B230 as "the frontier" at Review 32
    "ROADMAP.md",         # the phase ladder / cadences
    "docs/CAMPAIGN_STATUS.md",
    "docs/MASTERPLAN.md",
    "docs/LEAD_REGISTER.md",
    "docs/OPEN_PROBLEMS.md",
    "docs/PRICED_DOORS.md",
    "docs/OPEN_LEADS.md",
)


def gate_views_fresh():
    """Every navigation view must have been touched at or after the LAST review anchor.
    Zero commits touching a view since the anchor == that review did not refresh it."""
    path = os.path.join(ROOT, REVIEWS)
    if not os.path.exists(path):
        # FAIL-CLOSED (restart-resistance audit): deleting REVIEWS.md silently disabled BOTH
        # this gate and views-fresh. The review register is constitutive (GOVERNANCE §15).
        if os.path.isdir(os.path.dirname(path)):
            return False, "docs/progress/ exists but REVIEWS.md is MISSING -- §15 register gone"
        return True, "no docs/progress/ yet"
    anchors = re.findall(r"anchor-commit: `?([0-9a-f]{7,40})`?", _read(REVIEWS))
    if not anchors:
        return True, "no review anchor yet"
    anchor = anchors[-1]
    stale = []
    for v in VIEWS:
        if not os.path.exists(os.path.join(ROOT, v)):
            continue
        rc, out = _git("rev-list", "--count", f"{anchor}..HEAD", "--", v)
        if rc == 0 and int(out.strip() or 0) == 0:
            stale.append(os.path.basename(v))
    if stale:
        return False, ("not refreshed since the last review anchor: "
                       + ", ".join(stale) + " — the review must regenerate the views")
    return True, "ok"


# --- gate: arc-ID collisions (owner, 2026-07-29; Review 32) ----------------------------------
# Five documented collisions (B788 three-way, B793 two-way, B372, L108, and the B569-B574
# renumbering the repo already records). TWO were created in a single session, costing a
# duplicated Step-2 computation and two renumbering rulings.
# Historical collisions predating the gate. GOVERNANCE §12 forbids renaming banked paths
# ("zero file moves"), so these are GRANDFATHERED explicitly rather than fixed — auditable and
# versioned, per this file's design rule. NEW collisions still fail.
GRANDFATHERED_IDS = frozenset({"B58"})


def gate_id_collisions():
    """No NEW frontier arc directory may share a B-number with another.

    Historical collisions are grandfathered (§12 forbids renaming banked paths); the gate's
    job is to stop the next one. Two were created in a single session (2026-07-28/29), costing
    a duplicated Step-2 computation and two renumbering rulings."""
    fdir = os.path.join(ROOT, "frontier")
    if not os.path.isdir(fdir):
        # FAIL-CLOSED (restart-resistance audit): frontier/ is the lab bench; its absence in
        # this repository means a broken checkout, not a repository without arcs.
        return False, "frontier/ is MISSING -- broken checkout, not an empty lab bench"
    seen, dups = {}, []
    for name in sorted(os.listdir(fdir)):
        if not os.path.isdir(os.path.join(fdir, name)):
            continue
        m = re.match(r"(B\d+)[a-z]?_", name)
        if not m:
            continue
        bid = m.group(1)
        if bid in seen:
            if bid not in GRANDFATHERED_IDS:
                dups.append(f"{bid}: {seen[bid]} vs {name}")
        else:
            seen[bid] = name
    if dups:
        return False, "arc-ID collision — " + "; ".join(dups)
    nxt = max((int(k[1:]) for k in seen), default=0) + 1
    return True, f"ok ({len(seen)} arcs, next free B{nxt})"


def gate_knowledge_index():
    """Every knowledge/K*.md must appear in knowledge/INDEX.md, and vice versa.

    INDEX.md is the knowledge layer's only entry point: an explainer missing from it is
    invisible to a reader and effectively unwritten. Four had drifted out (K021-K024,
    caught in the Review 32 sweep) because rows are appended by hand. Checked both ways --
    an indexed row whose file is gone is a dead link, the same defect mirrored."""
    kdir = os.path.join(ROOT, "knowledge")
    index = os.path.join(kdir, "INDEX.md")
    if not os.path.isfile(index):
        # FAIL-CLOSED (2026-07-29 restart-resistance audit): this gate previously PASSED when
        # the very index it guards was deleted -- verified by deleting it in a fresh clone.
        # A gate that goes quiet when its subject vanishes is worse than no gate.
        if os.path.isdir(kdir):
            return False, ("knowledge/ exists but INDEX.md is MISSING -- the layer's only entry "
                           "point is gone")
        return True, "no knowledge/ layer"
    on_disk = {m.group(1) for f in os.listdir(kdir)
               if (m := re.match(r"(K\d{3})_.*\.md$", f))}
    body = _read(index)
    indexed = set(re.findall(r"\bK(\d{3})\b", body))
    indexed = {f"K{n}" for n in indexed}
    missing = sorted(on_disk - indexed)
    dangling = sorted(indexed - on_disk)
    problems = []
    if missing:
        problems.append("not in INDEX: " + ", ".join(missing))
    if dangling:
        problems.append("in INDEX but no file: " + ", ".join(dangling))
    if problems:
        return False, "knowledge index drift — " + "; ".join(problems)
    return True, f"ok ({len(on_disk)} explainers, all indexed)"


def gate_path_refs():
    """Every backticked repo-path cited in a tracked .md must resolve.

    The repo cites its artifacts as backticked paths (~1300) far more than as markdown links
    (~32), so this covers the reference graph a link-checker misses. Resolution is tried
    repo-root-relative AND relative to the citing file's own directory (the B600 packet README
    legitimately cites its own `scripts/engine.py`). Exemptions for append-only history and
    hash-pinned seals live in the checker module, documented there.

    NB the checker lives under scripts/checks/, not scripts/audit/: .gitignore line 11 is a
    bare `audit/`, which is UNANCHORED and so swallows any directory named audit at any
    depth. A scripts/audit/ would be silently untracked and the gate would soft-skip on a
    fresh clone -- passing while checking nothing."""
    sys.path.insert(0, os.path.join(ROOT, "scripts", "checks"))
    try:
        import check_path_references as cpr
    except Exception as exc:
        # FAIL-CLOSED, deliberately. The near-miss above (a scripts/audit/ copy would have been
        # silently gitignored) showed that "module missing" is exactly the state in which this
        # gate must not report ok — a gate that soft-skips when its checker vanishes passes
        # while checking nothing, which is worse than having no gate at all.
        return False, f"path-reference checker missing or unimportable: {exc}"
    finally:
        sys.path.pop(0)
    total, bad = cpr.scan()
    if bad:
        pairs = sorted({f"{r} -> {t}" for r, t in bad})
        return False, f"{len(pairs)} unresolved path citation(s): " + "; ".join(pairs[:5])
    return True, f"ok ({total} citations resolve)"


def gate_test_vacuity():
    """No test may be unconditionally-passing: no NO-ASSERT, no TAUTOLOGY.

    The programme's ledger already carries this failure twice (E31 vacuous verification; MB12
    check-the-criterion-can-fail), and a 2026-07-29 sweep found 8 live instances -- among them a
    'cross-seat check' comparing two hand-typed copies of the same dict, and an F11 'grep-
    verifiable' lock that counted marker hits and then executed `pass`. Every underlying claim
    turned out TRUE, so nothing banked was falsified; the locks simply were not locking.

    Only the two hard classes gate. The checker's BOTH-LITERAL class needs human judgement (a
    deliberate data-lock like `assert 52 + 26 == 78` also cannot fail but is documentation, not
    a defect), so it is reported, not enforced."""
    sys.path.insert(0, os.path.join(ROOT, "scripts", "checks"))
    try:
        import check_test_vacuity as ctv
    except Exception as exc:
        return False, f"vacuity checker missing or unimportable: {exc}"   # fail-closed
    finally:
        sys.path.pop(0)
    total, no_assert, tautology, both_lit = ctv.scan()
    problems = no_assert + tautology
    if problems:
        return False, f"{len(problems)} unconditionally-passing test(s): " + \
                      "; ".join(problems[:5])
    return True, f"ok ({total} tests, 0 vacuous; {len(both_lit)} both-literal for review)"


def gate_views_generated():
    """The generated views under docs/views/ must be current with their sources.

    GOVERNANCE §12 clause two. Unlike `views-fresh` (which asks whether a HAND-maintained view
    was touched recently), this asks whether a GENERATED view still equals what its sources
    produce -- a strictly stronger check, and the one that makes hand-editing detectable."""
    gen = os.path.join(ROOT, "scripts", "views", "generate.py")
    if not os.path.isfile(gen):
        return False, "view generator missing"                 # fail-closed
    vdir = os.path.join(ROOT, "docs", "views")
    before = {}
    if os.path.isdir(vdir):
        for f in sorted(os.listdir(vdir)):
            if f.endswith(".md"):
                before[f] = _read(f"docs/views/{f}")
    r = subprocess.run([sys.executable, gen], capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        return False, f"generator failed: {r.stderr[-200:]}"
    stale = []
    for f, old in before.items():
        if _read(f"docs/views/{f}") != old:
            stale.append(f)
    new = [f for f in os.listdir(vdir) if f.endswith(".md") and f not in before]
    if stale or new:
        return False, ("generated views out of date (regenerate: python3 scripts/views/"
                       "generate.py): " + ", ".join(stale + new))
    return True, f"ok ({len(before)} views current)"


PRACTICES = "docs/PRACTICES.md"


def gate_practices_register():
    """docs/PRACTICES.md and the gate registry must agree, BOTH directions.

    Instituted 2026-07-29. A day of sweeps found six drifted practices and five that held, split
    perfectly by whether a gate existed -- and found that agreed practices had no single home
    (they lived in WORKING_RULES prose, in this file's code, and in conversation, and the
    conversational ones reached neither). PRACTICES.md is that home.

    Direction (2) is the one that matters: a gate added WITHOUT a row in the register would make
    the register quietly incomplete, which is exactly how knowledge/INDEX.md lost four entries."""
    path = os.path.join(ROOT, PRACTICES)
    if not os.path.isfile(path):
        return False, "docs/PRACTICES.md missing -- the practice register is the agreement record"
    text = _read(PRACTICES)
    named = set(re.findall(r"`([a-z0-9-]+)`", text))
    problems = []
    missing = sorted(g for g in GATES if g not in named)
    if missing:
        problems.append("gates absent from the register: " + ", ".join(missing))
    # every GATED row must name a gate that exists
    for line in text.splitlines():
        if "**GATED**" not in line:
            continue
        cited = re.findall(r"`([a-z0-9-]+)`", line)
        if cited and not any(c in GATES for c in cited):
            problems.append(f"GATED row names no live gate: {line.strip()[:70]}")
    if problems:
        return False, "practice register drift -- " + "; ".join(problems[:4])
    return True, f"ok ({len(GATES)} gates all registered)"


def gate_log_changelog_paired():
    """PROGRESS_LOG and CHANGELOG must be updated together.

    A standing rule that cc broke on three of its own commits in a single session (2026-07-29),
    caught only by its own survey. Written rules have a half-life; this one now has a gate.
    Checks that CHANGELOG was touched at or after the last PROGRESS_LOG touch."""
    rc, a = _git("log", "-1", "--format=%ct", "--", "PROGRESS_LOG.md")
    rc2, b = _git("log", "-1", "--format=%ct", "--", "CHANGELOG.md")
    if rc != 0 or rc2 != 0 or not a.strip() or not b.strip():
        return True, "git unavailable -- skipped"
    ta, tb = int(a.strip()), int(b.strip())
    if tb < ta:
        return False, ("PROGRESS_LOG updated after CHANGELOG -- the standing rule is that a banked "
                       "arc updates both in the same or next PR")
    return True, "ok (changelog at or after progress-log)"


GATES = {
    "framing": gate_framing,
    "claims": gate_claims,
    "firewall-oneway": gate_firewall_oneway,
    "append-only": gate_append_only,
    "atlas-fresh": gate_atlas_fresh,
    "attribution": gate_attribution,
    "tracked-forbidden": gate_tracked_forbidden,
    "review-actions": gate_review_actions,
    "views-fresh": gate_views_fresh,
    "id-collisions": gate_id_collisions,
    "knowledge-index": gate_knowledge_index,
    "path-refs": gate_path_refs,
    "test-vacuity": gate_test_vacuity,
    "views-generated": gate_views_generated,
    "practices-register": gate_practices_register,
    "log-changelog-paired": gate_log_changelog_paired,
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
