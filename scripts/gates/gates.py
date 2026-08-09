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
import glob
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
    # R37-1 repair: scan ALL root-level .md files, not a hardcoded name list --
    # the audit injected a banned phrase into WORKING_RULES.md and this gate passed
    # (root files outside the old 8-name list were never scanned).
    files = sorted(n for n in os.listdir(ROOT)
                   if n.endswith(".md") and os.path.isfile(os.path.join(ROOT, n)))
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
    # R37-1 repair: every cited tests/ file anywhere in the ledger must exist --
    # the audit placed a fake E-row citing a nonexistent test in ## Certified data
    # and the old Proven-slice-only scan passed it. (Execution of the tests is BY
    # DESIGN the suite's job -- tests/test_repo_gates.py runs with every merge --
    # this gate owns citation integrity, not test verdicts.)
    for m in re.finditer(r"`(tests/[A-Za-z0-9_./]+\.py)`", text):
        if not os.path.exists(os.path.join(ROOT, m.group(1))):
            problems.append(f"evidence missing: {m.group(1)}")
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
    # R37-1 repair: SET equality, not cardinality -- opposite-direction drift
    # (one stale entry + one missing entry) used to cancel silently.
    data = json.loads(_read("scripts/atlas/atlas_data.json"))
    atlas_ids = set(data["probes"].keys())
    fdir = os.path.join(ROOT, "frontier")
    ids = set()
    for name in os.listdir(fdir):
        m = re.match(r"(B\d+[a-z]?)", name)
        if m and os.path.isfile(os.path.join(fdir, name, "FINDINGS.md")):
            ids.add(m.group(1))
    extra = sorted(atlas_ids - ids)[:5]
    miss = sorted(ids - atlas_ids)[:5]
    ok = not extra and not miss
    return ok, f"atlas-only={extra} dirs-only={miss}" if not ok else "ok"




# --- gate: arc verdicts (R37-1; the B877 lesson) -------------------------------------------
# Every frontier arc with a FINDINGS.md must carry a sibling arc_verdict.json -- Review 37
# found B877's verdict silently missing after a banking chain died mid-way and the retry
# resumed past the failed step. Grandfathered: the 13 arcs predating the verdict convention
# (frozen constants per GOVERNANCE house rule; additions require a logged amendment).
VERDICT_GRANDFATHERED = {
    "B58_stage1", "B834_wave3b", "B835_lock_repairs", "B836_route_negatives",
    "B837_file_drawer_audit", "B838_lexicon_regrounding", "B839_b685_residue",
    "B840_close_loose_ends", "B841_provenance_pass", "B842_face_attachment",
    "B845_spectral_inventory", "B89T_tower_route", "B89_sl4_symbolic_M4L",
    "P3_depth_exposure",   # cc3 stratum harvest 2026-07-22, pre-verdict-convention
}


def gate_arc_verdicts():
    fdir = os.path.join(ROOT, "frontier")
    missing = []
    for name in sorted(os.listdir(fdir)):
        d = os.path.join(fdir, name)
        if not os.path.isdir(d) or name in VERDICT_GRANDFATHERED:
            continue
        if os.path.isfile(os.path.join(d, "FINDINGS.md")) and \
                not os.path.isfile(os.path.join(d, "arc_verdict.json")):
            missing.append(name)
    return not missing, missing[:8] or "ok"


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
    # Split on the block HEADERS and take everything up to the next section, rather than matching a
    # contiguous run of "- [.]" lines. Action items wrap onto continuation lines, and the old regex
    # stopped at the first one -- so for recent reviews it saw ONE item each and reported 0 open
    # items in superseded blocks when the true count was 13 (B844). Fail-open by drift, same class
    # as B827's: the gate was sound when every item fit on one line.
    parts = re.split(r"### Action items \(Review [^)]+\)\n", text)
    blocks = [p.split("\n## ")[0].split("anchor-commit")[0] for p in parts[1:]]
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
    """PROGRESS_LOG and CHANGELOG must be updated together, and there must be ONE progress log.

    A standing rule cc broke on three commits in one session (2026-07-29), so it was gated. The
    gate then FAILED SILENTLY for ten days (B827): entries were going to a shadow
    `docs/PROGRESS_LOG.md` created by accident at 73d07f0e, and this check compared CHANGELOG's
    timestamp against the *canonical* file's. Once the canonical file stopped being written its
    timestamp froze, so every later CHANGELOG commit trivially satisfied "CHANGELOG at or after
    PROGRESS_LOG". A gate that watches a file nobody writes cannot detect that nobody writes it.

    Two checks now, and both can fail:
      (1) NO shadow progress log may exist outside the sanctioned archive dir. This is the one
          that would have caught B827 on day one.
      (2) CHANGELOG may not run more than ONE commit ahead of PROGRESS_LOG -- the standing rule is
          "same or next PR", so a lag of 2+ means the log is being skipped.
    """
    # (1) shadow-file check -- the defect class that hid for ten days
    shadows = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        # `legacy/` is a frozen import of the pre-2026-05-28 repository -- a genuine archive, not
        # a shadow. Excluded by name so the check stays sharp everywhere else rather than being
        # loosened into uselessness.
        dirnames[:] = [d for d in dirnames
                       if d not in (".git", "audit", "legacy", "node_modules", "__pycache__",
                                    "veins")]
        for fn in filenames:
            if fn != "PROGRESS_LOG.md":
                continue
            rel = os.path.relpath(os.path.join(dirpath, fn), ROOT)
            if rel != "PROGRESS_LOG.md":
                shadows.append(rel)
    if shadows:
        return False, (f"shadow progress log(s): {shadows} -- there is exactly ONE progress log "
                       f"(PROGRESS_LOG.md at the repo root); quarterly roll-offs live in "
                       f"docs/progress/PROGRESS_<quarter>.md. A second file with this name "
                       f"silently absorbed 37 entries over ten days (B827)")

    # (2) lag check -- "same or next PR"
    rc, out = _git("log", "-1", "--format=%H", "--", "PROGRESS_LOG.md")
    if rc != 0 or not out.strip():
        return True, "git unavailable -- skipped"
    last_log = out.strip()
    rc2, out2 = _git("rev-list", "--count", f"{last_log}..HEAD", "--", "CHANGELOG.md")
    if rc2 != 0:
        return True, "git unavailable -- skipped"
    lag = int(out2.strip() or 0)
    if lag > 1:
        return False, (f"CHANGELOG is {lag} commits ahead of PROGRESS_LOG -- the standing rule is "
                       f"that a banked arc updates both in the same or next PR")
    return True, f"ok (one progress log; changelog lag {lag})"


CHAIN = "docs/THEOREM_LEDGER.md"


def gate_chain_locks():
    """Every link in THE CHAIN must cite a resolvable test lock -- its OWN admission rule.

    THE CHAIN's stated admission bar is "exact statement + banked computation location + green
    lock". A 2026-07-29 review found four [THEOREM] links citing locks only in PROSE ("the B730
    locks", "test_b734") -- which no gate can verify and no reader can run. This enforces the
    rule the ledger already set for itself; it does not invent a new mandate."""
    if not os.path.isfile(os.path.join(ROOT, CHAIN)):
        return False, "docs/THEOREM_LEDGER.md missing -- THE CHAIN is the theorem bank"
    text = _read(CHAIN)
    blocks = re.split(r"(?=^\*\*C\d+ \[)", text, flags=re.M)
    links = [b for b in blocks if re.match(r"\*\*C\d+ \[", b)]
    bad, missing = [], []
    for b in links:
        cid = re.match(r"\*\*(C\d+) \[([A-Z-]+)", b)
        name, label = cid.group(1), cid.group(2)
        if label == "AXIOM":                      # a declared choice needs a price, not a lock
            continue
        paths = re.findall(r"tests/(test_[A-Za-z0-9_]+\.py)", b)
        if not paths:
            bad.append(f"{name}[{label}]")
            continue
        for pth in paths:
            if not os.path.isfile(os.path.join(ROOT, "tests", pth)):
                missing.append(f"{name} -> tests/{pth}")
    problems = []
    if bad:
        problems.append("links citing no resolvable lock: " + ", ".join(bad))
    if missing:
        problems.append("locks cited but absent: " + ", ".join(missing))
    if problems:
        return False, "THE CHAIN -- " + "; ".join(problems)
    return True, f"ok ({len(links)} links, every non-AXIOM one locked)"


LAW_MAP = "docs/LAW_MAP.md"


def gate_law_map_provenance():
    """LAW_MAP rows must be traceable, and any lock they cite must resolve.

    Review 33 (R33-4) measured LAW_MAP at 113 rows with 5 test locks (4 %) and NO gate touching
    it, then rejected "lock all 113" as an unfunded mandate (108 rows to author). The decided
    posture is UNENFORCED INDEX WITH TRACEABLE PROVENANCE, and these are the two cheap
    invariants that make that posture honest rather than an excuse."""
    if not os.path.isfile(os.path.join(ROOT, LAW_MAP)):
        return False, "docs/LAW_MAP.md missing -- the law index is constitutive"
    text = _read(LAW_MAP)
    rows = [l for l in text.splitlines()
            if l.startswith("|") and l.count("|") >= 4 and "---" not in l
            and not re.match(r"^\|\s*(law|name)", l, re.I)]
    noarc = [r for r in rows if not re.search(r"\bB\d{2,3}\b", r)]
    broken = [m for r in rows for m in re.findall(r"tests/(test_[a-z0-9_]+\.py)", r)
              if not os.path.isfile(os.path.join(ROOT, "tests", m))]
    problems = []
    if noarc:
        problems.append(f"{len(noarc)} row(s) cite no arc: " +
                        "; ".join(r.split("|")[1].strip()[:40] for r in noarc[:3]))
    if broken:
        problems.append("cited locks absent: " + ", ".join(broken[:3]))
    if problems:
        return False, "LAW_MAP provenance -- " + "; ".join(problems)
    locked = sum(1 for r in rows if re.search(r"tests/test_[a-z0-9_]+\.py", r))
    return True, f"ok ({len(rows)} rows all traceable; {locked} locked -- index, not ledger)"


# B806. A HIGH-WATER MARK, not a budget: raising it must be a deliberate, recorded act.
# 19 at measurement -> 20 the moment B806 itself was banked, because the arc DOCUMENTING the
# lexicon's blindness is invisible to the lexicon. The finding demonstrating itself is the
# strongest evidence for it, and the ceiling records that rather than hiding it.
# Blind arcs are TRIAGED, not capped (B823).
#
# B821: a raw blind count conflates thin stubs, instrument arcs and real gaps -- three unlike
# things. B822: capping it is self-referential, because the arc documenting the gate is itself an
# instrument arc and incremented the count it was fixing. There is therefore NO CEILING. Every
# substantial blind arc must carry a disposition in docs/atlas/BLIND_ARCS.md, and this gate fails
# only on UNTRIAGED arcs -- it asks for a judgement, not a number.
LEXICON_MIN_BYTES = 2000
BLIND_REGISTRY = os.path.join("docs", "atlas", "BLIND_ARCS.md")


def gate_atlas_lexicon_current():
    """The atlas lexicon must not go blind: zero-motif probes may not grow.

    B806: the LEXICON is 18 hand-authored regex sets, authored 2026-07-01 and grounded in
    K001..K022. 409 arcs have been banked since; K023-K025 are outside its grounding. An arc
    matching none of the 18 is invisible to the atlas BY CONSTRUCTION -- including B798, which
    defines the programme's own current falsifier.

    The instrument is self-sealing: 18 labels will always report the corpus concentrated in 18
    things. This gate cannot make it discover new motifs; it makes its GOING BLIND detectable,
    which is the property it lacked."""
    import json as _json
    p = os.path.join(ROOT, "scripts", "atlas", "atlas_data.json")
    if not os.path.isfile(p):
        return False, "atlas_data.json missing -- the lexicon check has no input"
    probes = _json.load(open(p, encoding="utf-8"))["probes"]

    reg = os.path.join(ROOT, BLIND_REGISTRY)
    if not os.path.isfile(reg):
        return False, (f"{BLIND_REGISTRY} is MISSING -- the triage registry is this gate's only "
                       f"input; without it no blind arc can be dispositioned")
    reg_text = open(reg, encoding="utf-8").read()

    import glob as _glob
    import re as _re

    def _size(aid):
        for d in _glob.glob(os.path.join(ROOT, "frontier", f"{aid}_*")):
            f = os.path.join(d, "FINDINGS.md")
            if os.path.isfile(f):
                return os.path.getsize(f)
        return 0

    blind_all = [k for k, v in probes.items() if not v.get("motifs")]
    blind = [k for k in blind_all if _size(k) >= LEXICON_MIN_BYTES]
    thin = len(blind_all) - len(blind)

    triaged = {m.group(1): m.group(2)
               for m in _re.finditer(r"^\| `(B\d+)` \| \*?\*?(GAP|INSTRUMENT)", reg_text, _re.M)}
    untriaged = sorted(a for a in blind if a not in triaged)
    if untriaged:
        return False, (f"{len(untriaged)} substantial blind arc(s) NOT triaged in "
                       f"{BLIND_REGISTRY}: {untriaged} -- add a row saying GAP (a real object "
                       f"topic the lexicon misses) or INSTRUMENT (an arc about our own machinery, "
                       f"which an OBJECT atlas is correct to miss)")

    # Stale rows are a defect too: a registry that outlives its arcs stops being readable.
    stale = sorted(a for a in triaged if a not in blind)
    if stale:
        return False, (f"{BLIND_REGISTRY} lists arc(s) that are no longer substantial-and-blind: "
                       f"{stale} -- remove the row (the arc now carries a motif, or shrank)")

    gaps = sorted(a for a, d in triaged.items() if d == "GAP")
    return True, (f"ok ({len(blind)} substantial blind, all triaged; {len(gaps)} open GAP"
                  f"{'s' if len(gaps) != 1 else ''}{': ' + ', '.join(gaps) if gaps else ''}; "
                  f"{thin} thin arcs excluded)")



# B946(b): the banked-identity gate ALREADY existed in docs/TOOLBOX.md as a design pattern,
# and the solo seat's session showed a good intention is not a gate -- they proposed it, then
# skipped it, and spent nine sections computing a quantity their own banked theorem forbade.
# A skipping problem is not fixed by adding another gate; it is fixed by making the existing
# requirement a CHECKABLE FIELD at the one moment it bites: seal time.
SEAL_PROVENANCE_FROM = "2026-08-08"


def gate_seal_provenance():
    """Preregistrations sealed on/after SEAL_PROVENANCE_FROM must name, in the sealed text,
    (i) the banked identity the pipeline reproduces inside itself before any new number is
    read, and (ii) the prior-art / bank grep run at DESIGN time. Older seals are exempt:
    the rule cannot bind text that was sealed before it existed."""
    ledger = _read("docs/SEAL_LEDGER.md")
    missing = []
    for line in ledger.splitlines():
        m = re.match(r"\|\s*(\d{4}-\d{2}-\d{2})\s*\|[^|]*\|\s*`([^`]+)`", line)
        if not m:
            continue
        date, rel = m.group(1), m.group(2)
        if date < SEAL_PROVENANCE_FROM:
            continue
        if not os.path.isfile(os.path.join(ROOT, rel)):
            continue          # branch-side seals are recorded but not present here
        txt = _read(rel)
        if "BANKED IDENTITY:" not in txt or "PRIOR ART:" not in txt:
            missing.append(rel)
    return not missing, missing[:5] or "ok"



# L140 (B965): every fix in the LAW_MAP scope audit was a QUALIFIER LOST when an arc's
# verdict was compressed into a one-line row -- in each case the arc's own verdict was
# correct and properly scoped. The arcs are honest; the summaries leaked. This gate closes
# exactly that step, and it is the first gate here aimed at claim SCOPE rather than at
# numbers, hashes or file presence.
SCOPE_MARKERS = [r"only for\b", r"\bscope\b", r"assumes\b", r"not established",
                 r"conditional", r"\bup to\b", r"one-prime", r"not certified",
                 r"not claimed", r"post-hoc", r"inferred", r"cited not", r"screened",
                 r"necessary, not sufficient", r"\blimits\b", r"does not\b", r"NB \(",
                 r"standard, cited"]
_SCOPE_RX = [re.compile(x, re.I) for x in SCOPE_MARKERS]
SCOPE_HEAVY = 4     # a verdict with >= this many markers is "heavily scoped"


def _scope_count(text):
    return sum(1 for rx in _SCOPE_RX if rx.search(text))


def gate_lawmap_scope():
    """A LAW_MAP row citing a HEAVILY-SCOPED arc verdict must carry a scope marker of its
    own. Calibrated on the B965 audit: it flags all three fixes that audit forced, and
    passes the row that audit adjudicated as already correctly scoped."""
    verdicts = {}
    for path in glob.glob(os.path.join(ROOT, "frontier", "*", "arc_verdict.json")):
        try:
            d = json.load(open(path, encoding="utf-8"))
            verdicts[d["id"]] = d.get("claim_one_line", "")
        except Exception:
            continue
    bad = []
    for line in _read("docs/LAW_MAP.md").splitlines():
        if not line.startswith("| **"):
            continue
        ids = set(re.findall(r"\bB\d{2,4}\b", line))
        worst = max((_scope_count(verdicts[i]) for i in ids if i in verdicts), default=0)
        if worst >= SCOPE_HEAVY and _scope_count(line) == 0:
            bad.append(line.split("**")[1][:48] if "**" in line else line[:48])
    return not bad, bad[:5] or "ok"



# L139 (B965 -> B967): retracting a claim does not retract its INSTANCES. B964 retracted a
# phrasing and wrote a rule; an hour later the LAW_MAP audit found that exact error still
# live in a row written the same day. This gate sweeps every tracked .md for registered
# retracted phrases used as LIVE CLAIMS, allowing them as MENTIONS inside retraction
# records, correction banners and quotations of former claims.
def gate_retraction_sweep():
    """Registered retracted phrases must not appear as live claims in any tracked .md."""
    sys.path.insert(0, os.path.join(ROOT, "scripts", "checks"))
    try:
        import retraction_sweep as rs
    except Exception as exc:
        # FAIL-CLOSED: a missing sweeper is exactly the state in which the corpus rots
        # quietly, which is the failure this gate exists to prevent.
        return False, f"retraction_sweep unimportable: {exc}"
    v = rs.sweep()
    return not v, [f"{r}:{n} {p!r}" for r, n, p in v[:5]] or "ok"



# L143 (B976 -> B977): the third gate. `lawmap-scope` and `retraction-sweep` police the
# CONTENT of rows that exist; neither notices a row that was NEVER WRITTEN. B976 found
# eleven banked cascade arcs cited zero times on any synthesis surface -- including B864,
# which DERIVES hypercharge, while a ledger row written five days later called hypercharge
# "OPEN, the sharpest available target". The repo lost nothing; the summaries forgot.
def gate_relay_debt():
    """B999 -- branch protection preserves FILES; nothing preserved FINDINGS (design: cc3)."""
    import subprocess
    r = subprocess.run([sys.executable, os.path.join(str(ROOT), "scripts", "checks", "relay_debt.py")],
                       capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    if r.returncode != 0:
        return False, out.replace("\n", " | ")[:400]
    return True, "ok"


def gate_doc_currency():
    """B984 -- a living document that no longer reflects the corpus is a silent misinformer."""
    import subprocess
    r = subprocess.run([sys.executable, os.path.join(str(ROOT), "scripts", "checks", "doc_currency.py")],
                       capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    if r.returncode != 0:
        return False, out.replace("\n", " | ")[:400]
    return True, "ok"


def gate_representation_sweep():
    """Every SUBSTANTIAL banked arc cited on no synthesis surface must carry a disposition
    in docs/REPRESENTATION_TRIAGE.md (PENDING / PROCESS / SURFACE)."""
    sys.path.insert(0, os.path.join(ROOT, "scripts", "checks"))
    try:
        import representation_sweep as rsw
    except Exception as exc:
        # FAIL-CLOSED: a missing sweeper is the state in which arcs go quietly unrepresented,
        # which is the failure this gate exists to prevent.
        return False, f"representation_sweep unimportable: {exc}"
    missing = rsw.sweep()
    return not missing, [f"{i} ({v}, claim {n})" for i, v, n in missing[:5]] or "ok"


GATES = {
    "framing": gate_framing,
    "claims": gate_claims,
    "firewall-oneway": gate_firewall_oneway,
    "append-only": gate_append_only,
    "atlas-fresh": gate_atlas_fresh,
    "arc-verdicts": gate_arc_verdicts,
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
    "seal-provenance": gate_seal_provenance,
    "lawmap-scope": gate_lawmap_scope,
    "retraction-sweep": gate_retraction_sweep,
    "representation-sweep": gate_representation_sweep,
    "doc-currency": gate_doc_currency,
    "relay-debt": gate_relay_debt,
    "log-changelog-paired": gate_log_changelog_paired,
    "chain-locks": gate_chain_locks,
    "law-map-provenance": gate_law_map_provenance,
    "atlas-lexicon-current": gate_atlas_lexicon_current,
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
