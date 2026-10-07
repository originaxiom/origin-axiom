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
import pathlib
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
# B1226: the gate enforced ONE name out of the set the rule names, so "Anthropic", "Opus",
# "sonnet" and "fable" sat in tracked files looking clean. Word-bounded so ordinary English
# ("philanthropic", "ineffable", "magnum opus") cannot red the gate.
_VENDOR_TOKS = tuple(base64.b64decode(b).decode() for b in
                     (b"Y2xhdWRl", b"YW50aHJvcGlj", b"b3B1cw==", b"c29ubmV0", b"ZmFibGU="))
_VENDOR_RE = re.compile(r"\b(" + "|".join(_VENDOR_TOKS) + r")\b", re.I)


def _load_attr_baseline():
    """B1226 ratchet: the pre-existing occurrences are FROZEN, not forgiven. The gate reds on
    any new file and on any INCREASE in an existing one, so the footprint can only shrink.
    Clearing the backlog means editing append-only history — an owner decision, not a gate's."""
    try:
        with open(os.path.join(ROOT, "docs", "ATTRIBUTION_BASELINE.json")) as fh:
            return json.load(fh).get("frozen", {})
    except Exception:
        return {}


_ATTR_BASELINE = _load_attr_baseline()
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
            n = len(_VENDOR_RE.findall(_read(rel)))
            if n > _ATTR_BASELINE.get(rel, 0):
                hits.append(f"{rel} ({n} vendor tokens, baseline {_ATTR_BASELINE.get(rel, 0)})")
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
    #
    # WIDENED 2026-09-06 (B1290's follow-through). The rule above says "cross-seat relay
    # files"; the REGEX enforced only CC2/CC3 relays, so CC_TO_FC, CC_TO_CLOUD, CC_TO_CODEX
    # and CC_TO_ALL_SEATS were invisible to it. That is B1226's shape exactly ("the gate
    # enforced ONE vendor token of the five the standing rule names"), and it had already
    # cost two violations — BOTH committed by this bench on 2026-09-06, the day it was found.
    # The matcher now keys on a KNOWN SEAT as sender plus the relay convention's DATE stamp,
    # which is what separates a relay from docs/STRUCTURE_TO_NATURE_MASTERPLAN.md. Validated
    # both directions: 53/53 loose relays on disk matched, and the masterplan, README, and
    # arc-archived relays all correctly unmatched.
    #
    # Three loose relays predate the widening and are grandfathered — GOVERNANCE §12 forbids
    # moving banked paths ("locks, hashes, and the atlas depend on path stability"), so the
    # gate's job is to stop the NEXT one, not to relitigate these. NEW relays go inside the
    # arc directory they belong to.
    _SEAT = r"(?:CC|CC2|CC3|CLOUD|CODEX|FC|OWNER)"
    _RELAY_RE = re.compile(
        rf"^(?:docs/)?{_SEAT}(?:_[A-Z0-9]+)?_TO_[A-Z0-9_]+_\d{{4}}-\d{{2}}-\d{{2}}.*\.md$")
    GRANDFATHERED_RELAYS = {
        "CC3_TO_CC_2026-07-22_p3_complete.md",
        "CC_TO_ALL_SEATS_2026-09-06_ARC_NUMBER_RESERVATION.md",
        "CC_TO_FC_2026-09-06_THE_QUESTION_MOVED_TO_YOUR_CUSP.md",
    }
    bad = [f for f in out.splitlines()
           if f.startswith(".github/") or f == "Archive.zip"
           or (f.startswith("papers/flagship/a-self-generating-object") and f.endswith(".pdf"))
           or (_RELAY_RE.match(f) and os.path.basename(f) not in GRANDFATHERED_RELAYS)]
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


def _carry_leaks(text):
    """R50's carry-continuity core (unit-tested in test_review_carry_gate.py).
    For every `- [>]` item in a NON-latest action block whose line names a review key
    (R<nn>-<m>), that key must reappear SOMEWHERE LATER in the file (a later block or a
    later review's body). A [>] whose key never recurs is a SILENT DROP — exactly how
    R48-4..10 vanished (R49 named none of them) and how R46-6/7/11 evaporated (carried
    'to R47-10', whose content was a different item). Enforced from Review 46 onward
    (older blocks predate the key convention)."""
    leaks = []
    for m in re.finditer(r"### Action items \(Review (\d+)\)\n", text):
        rev = int(m.group(1))
        if rev < 46:
            continue
        block_start = m.end()
        nxt = text.find("### Action items (Review", block_start)
        block_end = nxt if nxt != -1 else len(text)
        if nxt == -1:
            continue  # the latest block: its carries are the live queue, not leaks
        block = text[block_start:block_end].split("anchor-commit")[0]
        rest = text[block_end:]
        for line in re.findall(r"^- \[>\].*$", block, re.M):
            for key in re.findall(r"\bR\d+-\d+\b", line):
                # the item's own key (R<rev>-<m>) or a carried ancestor key must recur later
                if key not in rest:
                    leaks.append(f"Review {rev}: carried item key {key} never recurs later — silent drop")
                    break
    return leaks


def gate_review_actions():
    """GOVERNANCE §15: action-item blocks in REVIEWS.md. Any block that is
    NOT the latest must contain zero open `- [ ]` items (resolved `[x]` or
    carried `[>]` only). The latest block's open count is advisory.
    R50 extension: carried `[>]` items must RECUR later by key (see _carry_leaks) —
    the carry chain leaked twice (R46-6/7/11 mis-keyed; R48-4..10 silently dropped)
    while this gate stayed green, because it never verified continuity."""
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
    leaks = _carry_leaks(text)
    if leaks:
        return False, "; ".join(leaks[:4])
    latest_open = len(re.findall(r"^- \[ \]", blocks[-1], re.M))
    return True, f"ok ({latest_open} open in the latest block, advisory; carry chain continuous)"



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


def gate_tracked_deps():
    """Every repo path a tracked test/script names must itself be TRACKED, not merely present.

    E57 (B1238, 2026-09-02): B1237 committed `tests/test_paper_ledger_counts.py` and pushed it
    with the tool it runs, `scripts/checks/paper_ledger_counts.py`, still untracked -- the
    file sat on the bench, so the local suite was green and `path-refs` resolved it; only a
    fresh clone would have redded. This is the complement of `path-refs`: that gate asks
    "does the cited path exist?", this one asks "does git HAVE it?". Scope is tracked .py
    under tests/ and scripts/ (the executable reference graph); a path is checked only when it
    exists on disk (a missing path is `path-refs`' business, or an intentional skipif).
    Fail-closed if git is unavailable -- an index we cannot read is not an index we may vouch for.
    """
    rc, out = _git("ls-files")
    if rc != 0:
        return False, f"git ls-files failed: {out[:80]}"
    tracked = set(out.split("\n"))
    lit = re.compile(r"(?:scripts|frontier|docs|tests|data|paper)/[\w./-]+\.(?:py|sh|json|md|txt|csv)")
    chain = re.compile(r'ROOT(?:\s*/\s*"[^"]+")+')
    bad = {}
    for rel in sorted(tracked):
        if not (rel.startswith(("tests/", "scripts/")) and rel.endswith(".py")):
            continue
        try:
            txt = _read(rel)
        except OSError:
            continue                                   # deleted-but-tracked: not this gate's class
        refs = set(lit.findall(txt))
        for ch in chain.findall(txt):
            refs.add("/".join(re.findall(r'"([^"]+)"', ch)))
        for r in refs:
            if r not in tracked and os.path.isfile(os.path.join(ROOT, r)):
                bad.setdefault(r, rel)
    if bad:
        pairs = [f"{r} <- {src}" for r, src in sorted(bad.items())]
        return False, f"{len(pairs)} untracked-but-referenced path(s): " + "; ".join(pairs[:5])
    return True, "ok"


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
    # R57-3 (2026-09-14): THE_SPINE.md is written by a DIFFERENT generator, and this gate ran only
    # generate.py -- so the one view nothing regenerated could drift for as long as it liked inside
    # the directory the gate scans. It had: 1127 locks on disk against 1216 the generator produces,
    # while its own header read "Regenerated with the views." Same shape as B921-9b, one surface
    # over: the check read what existed and never noticed what was never RUN. Every generator that
    # writes into docs/views/ is listed here.
    gens = [os.path.join(ROOT, "scripts", "views", g) for g in ("generate.py", "spine.py")]
    missing = [g for g in gens if not os.path.isfile(g)]
    if missing:
        return False, "view generator missing: " + ", ".join(os.path.basename(g) for g in missing)
    # A CHECK MUST NOT LEAVE ITS OWN WORK BEHIND (2026-09-16, main's defect report): this gate
    # verified freshness BY REGENERATING IN PLACE and never put the originals back, so an ordinary
    # `pytest` run -- which reaches here through tests/test_repo_gates.py -> gates.run_all() --
    # left tracked files modified in the working tree. Snapshot bytes, regenerate, compare,
    # RESTORE. Strictness is unchanged: the comparison is the same one. Reporting staleness is this
    # gate's job; FIXING it stays the author's, by running the generators deliberately.
    vdir = os.path.join(ROOT, "docs", "views")
    before = {}
    if os.path.isdir(vdir):
        for f in sorted(os.listdir(vdir)):
            if f.endswith(".md"):
                before[f] = (pathlib.Path(vdir) / f).read_bytes()

    def _restore():
        for name, raw in before.items():
            q = pathlib.Path(vdir) / name
            if not q.is_file() or q.read_bytes() != raw:
                q.write_bytes(raw)
        for name in os.listdir(vdir):                       # remove anything the run invented
            if name.endswith(".md") and name not in before:
                try:
                    (pathlib.Path(vdir) / name).unlink()
                except OSError:
                    pass

    try:
        for gen in gens:
            r = subprocess.run([sys.executable, gen], capture_output=True, text=True, timeout=300)
            if r.returncode != 0:
                return False, f"{os.path.basename(gen)} failed: {r.stderr[-200:]}"
        stale = [f for f, raw in before.items()
                 if (pathlib.Path(vdir) / f).read_bytes() != raw]
        new = [f for f in os.listdir(vdir) if f.endswith(".md") and f not in before]
    finally:
        _restore()
    if stale or new:
        return False, ("generated views out of date (regenerate: python3 scripts/views/generate.py "
                       "AND python3 scripts/views/spine.py): " + ", ".join(stale + new))
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
    # widened B\d{2,3} -> B\d{2,4} at R43-7 (B1027's row needed 3-digit lineage cites
    # purely to satisfy the old regex; 4-digit arcs are first-class citizens now)
    noarc = [r for r in rows if not re.search(r"\bB\d{2,4}\b", r)]
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


def _seal_ledger_rows(text):
    """the dated rows of docs/SEAL_LEDGER.md as (date, path, digest-or-None), read by their cells FROM THE RIGHT.

    2026-10-02 (B1456; found by the SM seat's lane and relayed): the two seal gates matched a row with one pattern that
    allowed no "|" inside the description cell, so a row whose description contains one never reached its path cell and
    both gates skipped it silently.  A row is: a date cell first; the digest, if any, is the rightmost cell that is a
    backticked 64-hex string; the path is the nearest cell to its left (or the rightmost cell, when there is no digest)
    that begins with a backticked token."""
    out = []
    for line in text.splitlines():
        if not line.startswith("|"): continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells: continue
        # B1464 (R55-13/R55-15): the ledger has TWO row shapes -- the date first, or the arc id first with the date in a
        # later cell. The old parser read the first only, so 31 of 50 digests were never recomputed and their
        # preregistrations never checked for the provenance markers, while both gates printed "ok".
        if re.match(r"^\d{4}-\d{2}-\d{2}$", cells[0]): date = cells[0]
        elif re.match(r"^B\d{1,4}[a-z]?$", cells[0]):
            dates = [c for c in cells if re.match(r"^\d{4}-\d{2}-\d{2}$", c)]
            if not dates: continue
            date = dates[0]
        else: continue
        digest = None; stop = len(cells)
        for i in range(len(cells) - 1, 0, -1):
            m = re.match(r"^`([0-9a-f]{64})`", cells[i])
            if m: digest, stop = m.group(1), i; break
        rel = None
        for i in range(stop - 1, 0, -1):
            m = re.match(r"^`([^`]*[/.][^`]*)`", cells[i])            # a path, not a short hash
            if m: rel = m.group(1); break
        if rel: out.append((date, rel, digest))
    return out


SEAL_PROVENANCE_FROM_ARC = 995      # the first arc sealed on/after SEAL_PROVENANCE_FROM (2026-08-08)
SEEN_FIRST_FROM_ARC = 1454          # from here a sealed "Seen first" section (WORKING_RULES 2026-10-02) is the prior-art half,
                                    # and a "Disclosed" section states what was known before the run (the banked-identity half)
# B1464 (Review 59; R55-13): the 41 seals of B995-B1451 that carry neither the two markers nor the two sections. Sealed
# text is not repaired; they are listed, the list may only shrink, and every seal after this fix is bound.
SEAL_PROVENANCE_BASELINE = frozenset((
    "B995", "B1000", "B1006", "B1011", "B1015", "B1016", "B1018", "B1024", "B1025", "B1026", "B1027", "B1028", "B1029",
    "B1034", "B1037", "B1039", "B1040", "B1041", "B1042", "B1043", "B1044", "B1062", "B1064", "B1065",
    "B1102", "B1104", "B1410", "B1434", "B1435", "B1439", "B1441", "B1444", "B1445", "B1450", "B1451"))
# R59-2 (B1468, 2026-10-04): six of the 41 state both halves in other words -- attested with verified quotes in
# tests/SEAL_PROVENANCE_ATTESTATIONS.json (B1019, B1033, B1036, B1066, B1071, B1442) and removed from the baseline (35 left).
SEAL_PROVENANCE_ATTESTATIONS = "tests/SEAL_PROVENANCE_ATTESTATIONS.json"


def seal_attestations(root=None):
    p = os.path.join(str(root or ROOT), SEAL_PROVENANCE_ATTESTATIONS)
    if not os.path.isfile(p): return {}
    try: return json.load(open(p, encoding="utf-8"))
    except Exception: return {}


def sealed_files(root=None):
    """every preregistration-style file under frontier/B*/ with its arc number"""
    import glob
    root = str(root or ROOT); out = []
    for pat in ("PREREGISTRATION*.md", "DECLARATION.md"):
        for p in glob.glob(os.path.join(root, "frontier", "B*", pat)):
            m = re.match(r"B(\d+)", os.path.basename(os.path.dirname(p)))
            if m: out.append((int(m.group(1)), os.path.relpath(p, root)))
    return sorted(out)


def seal_provenance_problems(root=None, baseline=SEAL_PROVENANCE_BASELINE):
    """the sealed files from SEAL_PROVENANCE_FROM_ARC on that carry neither (BANKED IDENTITY: and PRIOR ART:) nor, from
    SEEN_FIRST_FROM_ARC on, a 'Seen first' section and a 'Disclosed' section -- except the frozen baseline"""
    root = str(root or ROOT); bad = []
    for arc, rel in sealed_files(root):
        if arc < SEAL_PROVENANCE_FROM_ARC: continue
        txt = open(os.path.join(root, rel), errors="replace").read()
        markers = "BANKED IDENTITY:" in txt and "PRIOR ART:" in txt
        sections = arc >= SEEN_FIRST_FROM_ARC and re.search(r"(?m)^##[^\n]*Seen first", txt) and re.search(r"(?m)^##[^\n]*Disclosed", txt)
        if markers or sections: continue
        if "B%d" % arc in baseline: continue
        att = seal_attestations(root).get("B%d" % arc)
        if att and all(att.get(k) and att[k].strip().lower()[:40] in " ".join(txt.split()).lower() for k in ("banked_identity", "prior_art")): continue
        bad.append(rel)
    return bad


def gate_seal_provenance():
    """Every preregistration-style file sealed from B995 (2026-08-08) on must carry, in the sealed text, the two halves
    of the provenance rule: the banked identity reproduced before any new number, and the prior-art / record sweep run
    at design time -- as the markers BANKED IDENTITY: and PRIOR ART:, or, from B1454 on, as a 'Seen first' section and a
    'Disclosed' section. B1464 (Review 59): until then the gate read the ledger's rows of one shape and never the files,
    so 41 of the 46 seals in range carried neither and the gate said ok; those 41 are a frozen baseline, named above."""
    bad = seal_provenance_problems()
    if bad:
        return False, "sealed without the provenance halves: " + "; ".join(bad[:5])
    return True, "ok (every seal from B995 on carries the two halves, is attested with quotes, or is one of the %d frozen before B1464)" % len(SEAL_PROVENANCE_BASELINE)


def gate_seal_ledger_current():
    """R55-14 (B1464): docs/SEAL_LEDGER.md is a generated view (scripts/seal_ledger.py); its table must list every
    sealed-style file on disk. It was ~530 arcs stale for two months with nothing watching it."""
    ledger = _read("docs/SEAL_LEDGER.md")
    listed = set(re.findall(r"^\| (frontier/B[^ |]+) \|", ledger, re.M))
    missing = [rel for _, rel in sealed_files() if rel not in listed]
    if missing:
        return False, "%d sealed file(s) not in the generated table (run scripts/seal_ledger.py): " % len(missing) + ", ".join(missing[:4])
    return True, "ok (%d sealed files listed)" % len(listed)


def gate_seal_digests():
    """Two digest-corruption routes in two days (E47: retyped at seal; E48: a bulk
    identifier remap rewriting hex inside a digest — see docs/ERROR_LEDGER.md for both
    classes), both invisible to the gate layer while seal-provenance stayed green. The route-agnostic fix, proposed by
    the audit seat and adopted 2026-08-20: RECOMPUTE every recorded digest from the file
    it claims to certify. Append-only semantics: the LAST ledger row per path governs
    (corrected-by-append rows supersede the wrong cells above them). Rows whose path is
    absent from this tree (branch-side seals; path-as-prose supersession notes) are
    skipped. Catches mistyping, remapping, and every route not yet hit, because it does
    not care how a digest got wrong. Recomputes every digest the ledger records for a file present on main, in both
    of the ledger's row shapes (B1464: 46 of 46; before, 19 of 50 -- the arc-first rows were never read, R55-15)."""
    import hashlib
    ledger = _read("docs/SEAL_LEDGER.md")
    latest = {}
    for _date, rel, digest in _seal_ledger_rows(ledger):
        if digest:
            latest[rel] = digest
    bad = []
    for rel, want in latest.items():
        p = os.path.join(ROOT, rel)
        if not os.path.isfile(p):
            continue
        got = hashlib.sha256(open(p, "rb").read()).hexdigest()
        if got != want:
            bad.append(f"{rel}: ledger {want[:12]}… != file {got[:12]}…")
    return not bad, bad[:5] or f"ok ({len(latest)} sealed digests recomputed and matching)"



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


# B921-9b (2026-09-14): the SAME gap as L143, on a second surface. `retraction-sweep` is green
# on a corpus where SEVEN of the twelve RETRACTED arcs have no row in docs/RETRACTIONS.md -- and
# it is right to be: its rule is about the CONTENT of rows that exist. The comment above built
# `relay-debt` for "a row that was never written" -- for RELAYS. Nothing did it for retractions,
# and the lead row that had been sitting on it (B921-9) was itself four weeks old when it was read.
def gate_retraction_debt():
    """B921-9b -- every RETRACTED arc is NAMED in docs/RETRACTIONS.md, or its retraction is invisible."""
    import subprocess
    r = subprocess.run([sys.executable, os.path.join(str(ROOT), "scripts", "checks", "retraction_debt.py")],
                       capture_output=True, text=True, timeout=120)
    out = (r.stdout + r.stderr).strip()
    if r.returncode != 0:
        return False, out.replace("\n", " | ")[:500]
    return True, "ok"


def gate_harvest_debt():
    """B1307 -- every seat branch is READ within 21 days of a push; the harvest ledger is reconciled against each seat's own index
    (MASTERPLAN v3.1 section 1a rule 3). Plain mode = instrument integrity + ageing; `review-due` runs it --strict."""
    import subprocess
    r = subprocess.run([sys.executable, os.path.join(str(ROOT), "scripts", "checks", "harvest_debt.py"), "--quiet"],
                       capture_output=True, text=True, timeout=300)
    out = (r.stdout + r.stderr).strip()
    if r.returncode != 0:
        return False, out.replace("\n", " | ")[:500]
    return True, "ok"


def gate_lead_debt():
    """2026-10-01 -- a deferral lands as a LEAD or as an arc left at verdict OPEN, and nothing aged either (the relay and
    harvest gates age the other two kinds of debt). A ratchet: the stale counts may only shrink. Also fails on a lead number
    carried by two open leads (the E71 class, twice on 2026-09-18)."""
    import subprocess
    r = subprocess.run([sys.executable, os.path.join(str(ROOT), "scripts", "checks", "lead_debt.py")],
                       capture_output=True, text=True, timeout=300)
    out = (r.stdout + r.stderr).strip()
    if r.returncode != 0:
        return False, out.replace("\n", " | ")[:500]
    return True, "ok"


SEEN_FIRST_FROM = 1454


def seen_first_missing(root=None, start=SEEN_FIRST_FROM):
    """arcs numbered `start` and above whose FINDINGS.md lacks a "Seen first" section naming both the repo sweep and the literature"""
    import glob
    root = str(root or ROOT); bad = []
    for d in sorted(glob.glob(os.path.join(root, "frontier", "B*"))):
        m = re.match(r"B(\d+)_", os.path.basename(d))
        if not m or int(m.group(1)) < start: continue
        ff = os.path.join(d, "FINDINGS.md")
        if not os.path.exists(ff): continue
        text = open(ff, errors="replace").read()
        sec = re.search(r"(?ms)^##[^\n]*Seen first[^\n]*\n(.*?)(?=^## |\Z)", text)
        if not sec: bad.append(os.path.basename(d) + " (no 'Seen first' section)"); continue
        body = sec.group(1).lower()
        if "topic-sweep" not in body and "absence-sweep" not in body and "sweep" not in body: bad.append(os.path.basename(d) + " (no repo sweep cited)")
        elif "literature" not in body: bad.append(os.path.basename(d) + " (the literature is not addressed)")
    return bad


def gate_seen_first():
    """2026-10-02, the owner: "make a rule to see the repo first and literature". From B1454 on, an arc's FINDINGS carries a
    section "Seen first" citing the repo sweep it ran and what of the literature it searched and read (WORKING_RULES)."""
    bad = seen_first_missing()
    if bad:
        return False, "arcs without a complete 'Seen first' section: " + "; ".join(bad[:8])
    return True, "ok"


GENESIS_POINTERS = ("README.md", "docs/UNIQUENESS_THEOREM.md", "docs/THEOREM_LEDGER.md", "docs/THE_FRAMEWORK.md", "docs/THE_CLAIM.md",
                    "docs/THE_END_TO_END_CHAIN.md", "philosophy/P019_the_genesis_axiom_chain.md", "philosophy/P000_what_is_not_nothing.md")
GENESIS_ID_RE = re.compile(r"\b(?:PF\d|GM\d[a-d]?|SE\d|T-ROOT|F-[A-Z]{2}|FK\d+|GAP\d)\b")
GENESIS_USERS = ("README.md", "WORKING_RULES.md", "docs/OPEN_LEADS.md", "docs/THE_FOUNDATION_LOCK_PLAN.md", "docs/THE_CLAIM.md",
                 "docs/THE_FRAMEWORK.md", "docs/UNIQUENESS_THEOREM.md", "docs/THEOREM_LEDGER.md", "docs/LAW_MAP.md")


def genesis_problems(root=None):
    """what is wrong with the canonical statement of the foundations and its use: the page missing or without a version
    log entry for its version; a page that used to state the genesis without its pointer; a GENESIS ID used on a living
    surface or in an arc from B1454 on that the page does not define"""
    import glob
    root = str(root or ROOT); bad = []
    gp = os.path.join(root, "GENESIS.md")
    if not os.path.exists(gp): return ["GENESIS.md is missing"]
    g = open(gp, errors="replace").read()
    m = re.search(r"\*\*Version (\d+\.\d+) ·", g)
    if not m: bad.append("GENESIS.md has no version header")
    elif not re.search(r"(?m)^- \*\*v%s · " % re.escape(m.group(1)), g): bad.append("GENESIS.md v%s has no entry in its version log" % m.group(1))
    defined = set(GENESIS_ID_RE.findall(g))
    for rel in GENESIS_POINTERS:
        f = os.path.join(root, rel)
        if not os.path.exists(f) or "GENESIS.md" not in open(f, errors="replace").read(): bad.append(rel + " does not point to GENESIS.md")
    users = [os.path.join(root, r) for r in GENESIS_USERS]
    for d in sorted(glob.glob(os.path.join(root, "frontier", "B*"))):
        mm = re.match(r"B(\d+)_", os.path.basename(d))
        if mm and int(mm.group(1)) >= SEEN_FIRST_FROM: users.append(os.path.join(d, "FINDINGS.md"))
    for f in users:
        if not os.path.exists(f): continue
        undefined = sorted(set(GENESIS_ID_RE.findall(open(f, errors="replace").read())) - defined)
        if undefined: bad.append("%s uses %s, which GENESIS.md does not define" % (os.path.relpath(f, root), ", ".join(undefined)))
    return bad


def gate_genesis_cited():
    """2026-10-02, the owner: lock the genesis once and make every document reflect it. GENESIS.md is the one statement
    of the foundations (WORKING_RULES); the pages that used to state it point to it, and its IDs are used as defined."""
    bad = genesis_problems()
    if bad:
        return False, "; ".join(bad[:6])
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



def gate_theorem_registry():
    """R48-F1's mechanization (2026-08-21). THEOREM_REGISTRY's standing rule -- every
    theorem/law-creating bank adds its row SAME-PR -- went unenforced for 179 arcs
    because no gate read it (the audit seat's verified finding). The naive fix (gate on
    verdict PROVED) would flood the registry with ~600 audit/census rows -- the audit
    seat's sharpening, adopted verbatim: gate on the DECLARED field creates_law in
    arc_verdict.json (a self-declaration a gate reads beats a standing rule nobody
    reads; the field is schema-locked by tests/test_arc_verdict_schema.py, required
    from B1103 on). Rule: every arc declaring creates_law true must appear in
    docs/THEOREM_REGISTRY.md."""
    import glob as _glob
    import json as _json
    reg = open(os.path.join(ROOT, "docs", "THEOREM_REGISTRY.md"), encoding="utf-8").read()
    missing = []
    for f in sorted(_glob.glob(os.path.join(ROOT, "frontier", "*", "arc_verdict.json"))):
        try:
            d = _json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        if d.get("creates_law") is True and d.get("id") not in reg:
            missing.append(d.get("id"))
    ok = not missing
    return ok, ("ok" if ok else f"creates_law arcs missing registry rows: {missing}")

def gate_identification_register():
    """B1231. The programme's dominant error mode is IDENTIFICATION -- gluing two structures whose
    labels match, in different places, without a map. B813, B1223, and TWO of this bench's own in a
    single session (B1228's pi_1-2T-vs-ALE-Gamma; B1230/C-5b's Z/3-vs-module-group, one cell later).
    By B1225 the object CANNOT identify, so an unearned identification is an UNPRICED OBSERVER
    INPUT and the parameter count is a lower bound until it is earned.

    This gate enforces COMPLETENESS, NEVER JUDGMENT. It cannot tell whether a map acts; it only
    enforces that the question was asked and answered somewhere a reader can find it:
      (a) every identification an arc DECLARES has a row in docs/IDENTIFICATION_LEDGER.md;
      (b) the UNEARNED count may not INCREASE against docs/IDENTIFICATION_BASELINE.json.

    A RATCHET, not a blocker -- deliberately. A hard block while anything is UNEARNED would make the
    fastest path to green MARKING THINGS EARNED, pressuring exactly the judgment the gate protects
    (the B1222 shape, turned on ourselves), and would deadlock unrelated work behind a research
    question. UNEARNED is the correct resting state for honest open work; ~300 NEGATIVE arcs red
    nothing. But a NEW unearned identification reds the suite at creation -- which is precisely when
    2026-08-31's two would have been caught.
    """
    import glob as _glob
    import json as _json
    led = os.path.join(ROOT, "docs", "IDENTIFICATION_LEDGER.md")
    base = os.path.join(ROOT, "docs", "IDENTIFICATION_BASELINE.json")
    if not os.path.exists(led):
        return False, "docs/IDENTIFICATION_LEDGER.md missing (B1231 register)"
    text = _read("docs/IDENTIFICATION_LEDGER.md")
    rows, unearned = [], 0
    for line in text.splitlines():
        m = re.match(r"\|\s*(I-\d+)\s*\|(.*)", line)
        if not m:
            continue
        cells = [c.strip().replace("*", "") for c in m.group(2).split("|")]
        st = next((c for c in cells if c in ("EARNED", "REFUTED", "UNEARNED")), "?")
        rows.append(m.group(1))
        unearned += (st == "UNEARNED")
    problems = []
    # (a) declared-but-unregistered
    for f in sorted(_glob.glob(os.path.join(ROOT, "frontier", "*", "arc_verdict.json"))):
        try:
            d = _json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        for ident in (d.get("identifications") or []):
            ref = ident.get("row") if isinstance(ident, dict) else str(ident)
            if ref not in rows:
                problems.append(f"{d.get('id')}: declares {ref!r}, no ledger row")
    # (b) the ratchet
    if os.path.exists(base):
        try:
            b = _json.load(open(base, encoding="utf-8")).get("unearned")
        except Exception:
            b = None
        if b is not None and unearned > b:
            problems.append(f"UNEARNED increased {b} -> {unearned}: a new identification was made "
                            f"without being earned. Earn it, or register what would earn it and "
                            f"raise the baseline DELIBERATELY with a dated reason.")
    ok = not problems
    return ok, ("ok" if ok else problems[:5])


def gate_supersession_backlinks():
    """B1290's follow-through (2026-09-06). E53 is 'the correction never reached the verdict
    file'. The same shape exists one level up, at SUPERSESSION: 43 arcs were claimed superseded
    by a later arc and only ONE said so in its own arc_verdict.json -- so a reader landing on
    B154 from the atlas saw PROVED with no marker that a later arc had replaced it.

    The back-link is DERIVABLE, not a judgement: `supersedes` already carries the forward edge.
    This gate enforces that every forward claim has its back-link, so the corpus cannot silently
    re-accumulate 36 unmarked supersessions. It NEVER touches a verdict -- superseding an arc is
    not retracting it, and the 12 RETRACTED arcs are a separate, deliberate act."""
    import glob as _glob
    import json as _json
    claims, seen = {}, {}
    for f in sorted(_glob.glob(os.path.join(ROOT, "frontier", "*", "arc_verdict.json"))):
        try:
            d = _json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        i = d.get("id")
        if not i:
            continue
        seen[i] = d
        s = d.get("supersedes")
        if s:
            # A forward edge may be a list, a single id, or -- B239 -- ONE STRING HOLDING TWO IDS
            # ("B234, B235"). Review 55 found the gate silently skipping that row: it looked for an
            # arc literally named "B234, B235", found none, and took the not-in-corpus branch,
            # leaving two arcs unmarked. Split on commas/whitespace so a malformed edge is still
            # enforced rather than silently exempted -- a gate that skips what it cannot parse is
            # E66's shape, and this gate was minted the same day E66 was.
            raw = [s] if isinstance(s, str) else list(s)
            for chunk in raw:
                for tgt in re.split(r"[,\s]+", str(chunk).strip()):
                    if tgt:
                        claims.setdefault(tgt, []).append(i)
    silent = []
    for tgt, by in sorted(claims.items()):
        if tgt not in seen:          # forward edge points outside the corpus -- not this gate's business
            continue
        back = seen[tgt].get("superseded_by")
        if not back:
            silent.append(f"{tgt} (superseded by {sorted(set(by))}, says nothing)")
    ok = not silent
    return ok, ("ok" if ok else silent[:5])



# --- B1461: Review 58's governance delta (R58-1; the owner: "yes on all", 2026-10-02) -----------------------------
# Three things the review process could not do to itself: fire, age its carried items, and prove its own checks can
# fail.  GOVERNANCE §15 carries the rule; these gates carry the enforcement.
REVIEW_HARD = 2 * REVIEW_EVERY                      # past twice its period the review fires: the push fails
REVIEW_WAIVER = "docs/progress/REVIEW_WAIVER.md"    # unless the owner has waived it by date, in that file


def review_waiver_covers(n, text):
    """a waiver is one line '- waived <YYYY-MM-DD> by the owner through <N> merges: <reason>'; it covers while n < N"""
    best = 0
    for m in re.finditer(r"^- waived \d{4}-\d{2}-\d{2} by the owner through (\d+) merges", text or "", re.M):
        best = max(best, int(m.group(1)))
    return n < best


def gate_review_fires():
    """GOVERNANCE §15 (amendment 2026-10-03, R58-1 item 1): past twice its period (REVIEW_HARD merges on main's
    first-parent line since the last anchor) the decadal review is not a report but a block, unless the owner has
    waived it by date in REVIEW_WAIVER.  OA_REVIEW_MERGES overrides the count for the failing-path test."""
    n, _due = review_status()
    if os.environ.get("OA_REVIEW_MERGES"):
        n = int(os.environ["OA_REVIEW_MERGES"])
    if n is None:
        return True, "no review anchor yet"
    if n >= REVIEW_HARD:
        wpath = os.path.join(ROOT, REVIEW_WAIVER)
        if review_waiver_covers(n, _read(REVIEW_WAIVER) if os.path.isfile(wpath) else ""):
            return True, f"{n} merges since the last review; waived by the owner ({REVIEW_WAIVER})"
        return False, (f"{n} merges since the last review (>= {REVIEW_HARD}): the review FIRES -- run it "
                       f"(scripts/review/review_tools.py), or the owner waives it by date in {REVIEW_WAIVER}")
    return True, f"{n} merges since the last review (fires at {REVIEW_HARD})"


CARRY_LIMIT = 3                 # at its third carry an item is resolved, declined with its reason, or waived by the owner
CARRY_BASELINE_REVIEW = 58      # the items already past the limit when the rule was switched on (B1461); due at Review 59
CARRY_BASELINE = frozenset(("R55-1", "R55-2", "R55-4", "R55-6", "R55-7", "R55-9", "R55-12", "R55-13", "R55-14", "R55-15",
                            "R56-1", "R56-3", "R54-1", "R54-2", "R54-4"))


def _review_tools():
    import importlib.util
    p = os.path.join(ROOT, "scripts", "review", "review_tools.py")
    spec = importlib.util.spec_from_file_location("review_tools_for_gates", p); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); return m


def carry_age_problems(text, limit=CARRY_LIMIT, baseline_review=CARRY_BASELINE_REVIEW, baseline=CARRY_BASELINE):
    """the carried items of the LATEST action block that have been carried `limit` times or more and carry no
    disposition on their line ('declined' with a reason, or 'waived by the owner').  The baseline items are exempt
    only while the latest review is the one the rule was switched on at; at the next review they are due."""
    loop = _review_tools().action_loop(text)
    latest = loop["review"]
    if latest is None:
        return []
    start = text.rfind("### Action items (Review %d)" % latest)
    block = text[start:] if start >= 0 else ""
    problems = []
    for key, n in loop["carried"]:
        if n < limit:
            continue
        line = next((l for l in block.splitlines() if l.startswith("- [>]") and re.search(r"\b%s\b" % re.escape(key), l)), "")
        low = line.lower()
        if "declined" in low or "waived by the owner" in low:
            continue
        if latest == baseline_review and key in baseline:
            continue
        problems.append(f"{key} carried {n} times with no disposition (resolve it, decline it with a reason, or the owner waives it)")
    return problems


def gate_carry_age():
    """GOVERNANCE §15 (amendment 2026-10-03, R58-1 item 2): carried action items age.  Review 58 found ten items
    carried a fourth time unmoved; a loop that only checks continuity cannot see that."""
    if not os.path.isfile(os.path.join(ROOT, REVIEWS)):
        return True, "no review register yet"
    bad = carry_age_problems(_read(REVIEWS))
    if bad:
        return False, "; ".join(bad[:6])
    return True, "ok"


GATE_CONTROLS = "tests/GATE_CONTROLS.json"      # gate -> 'tests/<file>.py::<test function that makes it FAIL>'


def gate_gate_controls():
    """GOVERNANCE §15 (amendment 2026-10-03, R58-1 item 3a): every gate has a test that makes it fail, named in
    tests/GATE_CONTROLS.json; the named function must exist.  Review 58 counted 15 of 34 gates named by no test and
    twelve whose checker had no failing-path test at all (R58-2); a gate nobody has seen fail may be inert."""
    p = os.path.join(ROOT, GATE_CONTROLS)
    if not os.path.isfile(p):
        return False, f"{GATE_CONTROLS} missing -- the register of failing-path tests is gone"
    try:
        reg = json.loads(_read(GATE_CONTROLS))
    except Exception as exc:
        return False, f"{GATE_CONTROLS} unreadable: {exc}"
    problems = []
    missing = sorted(g for g in GATES if g not in reg)
    if missing:
        problems.append("gates with no registered failing-path test: " + ", ".join(missing))
    for g, ref in sorted(reg.items()):
        if "::" not in ref:
            problems.append(f"{g}: malformed reference {ref!r}"); continue
        f, fn = ref.split("::", 1)
        fp = os.path.join(ROOT, f)
        if not os.path.isfile(fp):
            problems.append(f"{g}: {f} does not exist"); continue
        if not re.search(r"^def %s\(" % re.escape(fn), open(fp, encoding="utf-8", errors="replace").read(), re.M):
            problems.append(f"{g}: {fn} not defined in {f}")
    return (not problems), ("; ".join(problems)[:600] if problems else f"ok ({len(reg)} gates with a registered failing-path test)")


REVIEW_CORE_FROM = 59                                   # binds the first review written after the rule
REVIEW_CORE_LINES = ("fresh-clone:", "sample seed:", "gate controls:")


def review_core_missing(text, start=REVIEW_CORE_FROM, lines=REVIEW_CORE_LINES):
    """for the latest review entry numbered `start` or above: which of the three core lines it lacks"""
    heads = [(int(m.group(1)), m.start()) for m in re.finditer(r"^# Review (\d+) ", text, re.M)]
    if not heads:
        return []
    n, pos = max(heads)
    if n < start:
        return []
    entry = text[pos:]
    return [l for l in lines if l not in entry]


def gate_review_core():
    """GOVERNANCE §15 (amendment 2026-10-03, R58-1 item 3): from Review 59 every review entry states its three core
    checks -- 'fresh-clone: PASS @ <commit>' (gates and the reproduction belt run in a fresh clone,
    review_tools.fresh_clone), 'sample seed: <anchor>' (the arcs read in full are drawn, not chosen), and
    'gate controls: <n> registered' (every gate has a failing-path test)."""
    if not os.path.isfile(os.path.join(ROOT, REVIEWS)):
        return True, "no review register yet"
    missing = review_core_missing(_read(REVIEWS))
    if missing:
        return False, "the latest review entry lacks its core lines: " + ", ".join(missing)
    return True, "ok"



# --- B1464 (R55-9): the pretense phrases, on a ratchet ------------------------------------------------------------
# PROVENANCE §0: all verification is internal. The strong phrases that would say otherwise are banned from living pages;
# "independently verified" is this project's cross-seat language and is grounded by §0, so it is not in the list.
PRETENSE_PHRASES = ("externally verified", "peer-reviewed", "peer reviewed", "third-party verif", "third party verif",
                    "confirmed by experts", "verified by an external", "an external reviewer", "an external audit",
                    "by an external audit")                                 # claimed verification by an outsider; a reader is not a verifier
PRETENSE_NEGATION = ("nothing here is", "nothing is", " not ", " no ", "never", "without", "has not", "have not", "is not", "are not")
PRETENSE_EXEMPT = ("docs/ERROR_LEDGER.md", "docs/RELAY_LEDGER.md", "docs/HARVEST_LEDGER.md", "docs/SEAL_LEDGER.md",
                   "docs/RETRACTED_PHRASES.md", "docs/EARLY_RECORD_INDEX.md", "PROVENANCE.md", "docs/CAMPAIGN_STATUS.md",
                   "CHANGELOG.md", "PROGRESS_LOG.md", "docs/PRACTICES.md")   # ledgers, dated history, and the register that names the rule
PRETENSE_BASELINE = 0                                                   # measured 2026-10-03 after B1464's two fixes


def pretense_hits(root=None):
    import glob
    root = str(root or ROOT); hits = []
    files = sorted(glob.glob(os.path.join(root, "docs", "*.md")) + glob.glob(os.path.join(root, "*.md")))
    for f in files:
        rel = os.path.relpath(f, root)
        if rel in PRETENSE_EXEMPT: continue
        low = open(f, errors="replace").read().lower()
        for p in PRETENSE_PHRASES:
            n = 0
            for m in re.finditer(re.escape(p), low):
                window = low[max(0, m.start() - 48):m.start()]
                if any(neg in window for neg in PRETENSE_NEGATION): continue        # a disclaimer is not a pretense
                n += 1
            if n: hits.append((rel, p, n))
    return hits


def gate_pretense_phrases():
    """R55-9 (B1464): the strong pretense phrases on living pages, held to a frozen baseline that may only shrink
    (Review 55 counted eleven ungrounded "an external reviewer/reader/audit"; two live misnomers fixed in B1464)."""
    hits = pretense_hits(); n = sum(c for _, _, c in hits)
    if n > PRETENSE_BASELINE:
        return False, "%d pretense phrase(s) on living pages (baseline %d): " % (n, PRETENSE_BASELINE) + "; ".join("%s: %s x%d" % h for h in hits[:5])
    return True, "ok (%d on living pages, baseline %d%s)" % (n, PRETENSE_BASELINE, "; lower the baseline" if n < PRETENSE_BASELINE else "")

# --- gate: a negative about one member may not call it "the object" (the owner's rule, 2026-10-04) ------------------
MEMBER_SCOPE_BASELINE = 8      # frozen 2026-10-04 (B1476's landing): B1157, B1338, B1407, B429, B713, B760, B959, B960 -- may only shrink
_MS_WIDE = re.compile(r"\b(family|commensurability class|every member|112|siblings?|all members|members of|the thirteen|m003|t12835|t12839|s958|v2873)\b", re.I)
_MS_OBJ = re.compile(r"(the object (cannot|can not|does not|has no|carries no|makes no|supplies no|never|is not|has none)|impossible on the object|not in the (amphichiral )?object|the object'?s own (impossib|cannot|lacks)|nothing in the object|no [a-z\- ]{0,40} (in|on|of) the object)", re.I)


def member_scope_hits(reader=None):
    """NEGATIVE verdict lines that say 'the object cannot' (or kin) without naming the family or a member: (arc id, phrase)."""
    reader = reader or (lambda rel: _read(rel))
    out = []
    for p in sorted(glob.glob(os.path.join(ROOT, "frontier", "B*", "arc_verdict.json"))):
        try:
            d = json.loads(reader(os.path.relpath(p, ROOT)))
        except Exception:
            continue
        if d.get("verdict") != "NEGATIVE":
            continue
        claim = str(d.get("claim_one_line", ""))
        m = _MS_OBJ.search(claim)
        if m and not _MS_WIDE.search(claim):
            out.append((d.get("id", os.path.basename(os.path.dirname(p))), m.group(0)[:50]))
    return out


def gate_member_scope(reader=None):
    """The owner's rule (2026-10-04, GENESIS v1.11): the object is the family; a negative computed on one member says the
    member's name, not "the object". Held to a frozen baseline of old verdict lines that may only shrink; a new NEGATIVE
    arc that writes 'the object cannot' without naming the family fails."""
    hits = member_scope_hits(reader)
    if len(hits) > MEMBER_SCOPE_BASELINE:
        return False, "%d NEGATIVE verdict lines say 'the object' for one member's result (baseline %d): " % (len(hits), MEMBER_SCOPE_BASELINE) + "; ".join("%s: %s" % h for h in hits[-5:])
    return True, "ok (%d on the record, baseline %d%s)" % (len(hits), MEMBER_SCOPE_BASELINE, "; lower the baseline" if len(hits) < MEMBER_SCOPE_BASELINE else "")

_SEAT_ID_RE = re.compile(r"^(sm:B\d{4}|xB\d{3}|LP\d{2}|R\d{3}[A-Z]?|memo \d+|B8\d{3})$")


def seat_positive_rests(reader=None):
    """every `rests_on_seat` entry of a main arc's verdict file: (arc id, seat item id, has a VERIFIED row, why)."""
    reader = reader or (lambda rel: _read(rel))
    rows = [l for l in reader("docs/HARVEST_LEDGER.md").split("\n") if l.startswith("| ") and not l.startswith("|---")]
    out = []
    for p in sorted(glob.glob(os.path.join(ROOT, "frontier", "B*", "arc_verdict.json"))):
        try:
            d = json.loads(reader(os.path.relpath(p, ROOT)))
        except Exception:
            continue
        for sid in d.get("rests_on_seat", []) or []:
            sid = str(sid)
            if not _SEAT_ID_RE.match(sid):
                out.append((d.get("id", "?"), sid, False, "not a seat item id"))
                continue
            pat = re.compile(r"(?<![A-Za-z0-9:])" + re.escape(sid) + r"(?![0-9])")
            verified = any(pat.search(l) and "**VERIFIED" in l for l in rows)
            out.append((d.get("id", "?"), sid, verified, "ok" if verified else "no VERIFIED row in docs/HARVEST_LEDGER.md"))
    return out


def gate_seat_positive_verified(reader=None):
    """The rule of proper computing for counts (B1487, 2026-10-07): a main arc that BUILDS on another seat's result
    declares it in its verdict file as `rests_on_seat: [...]`, and every such item must have a row in
    docs/HARVEST_LEDGER.md whose disposition is VERIFIED (re-run or re-derived on main). A result read by one seat
    only may be cited; it may not be built on. Declaring is MANUAL; the check is this gate."""
    rests = seat_positive_rests(reader)
    bad = [r for r in rests if not r[2]]
    if bad:
        return False, "%d arc(s) rest on a seat item without a VERIFIED row: " % len(bad) + "; ".join("%s rests on %s (%s)" % (a, s, why) for a, s, _, why in bad[:6])
    return True, "ok (%d declared seat dependencies, all VERIFIED on main)" % len(rests)


GATES = {
    "identification-register": gate_identification_register,
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
    "tracked-deps": gate_tracked_deps,
    "test-vacuity": gate_test_vacuity,
    "views-generated": gate_views_generated,
    "practices-register": gate_practices_register,
    "seal-provenance": gate_seal_provenance,
    "seal-digests": gate_seal_digests,
    "theorem-registry": gate_theorem_registry,
    "lawmap-scope": gate_lawmap_scope,
    "retraction-sweep": gate_retraction_sweep,
    "representation-sweep": gate_representation_sweep,
    "doc-currency": gate_doc_currency,
    "relay-debt": gate_relay_debt,
    "retraction-debt": gate_retraction_debt,
    "harvest-debt": gate_harvest_debt,
    "lead-debt": gate_lead_debt,
    "seen-first": gate_seen_first,
    "genesis-cited": gate_genesis_cited,
    "log-changelog-paired": gate_log_changelog_paired,
    "chain-locks": gate_chain_locks,
    "law-map-provenance": gate_law_map_provenance,
    "atlas-lexicon-current": gate_atlas_lexicon_current,
    "supersession-backlinks": gate_supersession_backlinks,
    "review-fires": gate_review_fires,
    "carry-age": gate_carry_age,
    "gate-controls": gate_gate_controls,
    "review-core": gate_review_core,
    "seal-ledger-current": gate_seal_ledger_current,
    "pretense-phrases": gate_pretense_phrases,
    "member-scope": gate_member_scope,
    "seat-positive-verified": gate_seat_positive_verified,
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
        # B1307: a review opens with the harvest debt and cannot close with unread seat results (--strict)
        r = subprocess.run([sys.executable, os.path.join(str(ROOT), "scripts", "checks", "harvest_debt.py"), "--strict"],
                           capture_output=True, text=True, timeout=300)
        print((r.stdout + r.stderr).rstrip())
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
