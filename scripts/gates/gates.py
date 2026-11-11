"""Automated repository gates (GOVERNANCE §11, instituted 2026-07-03).

Each gate is a fast, deterministic check of a governance invariant. The suite lock
`tests/test_repo_gates.py` runs them all, so every merge (full suite green) enforces them.
Run manually:  python3 scripts/gates/gates.py            (all gates, verdict per gate)
               python3 scripts/gates/gates.py review-due (the decadal-review counter only)

Design rules: no network, no heavy imports, stdlib only; a gate returns (ok, detail);
whitelists are explicit frozen constants in this file (auditable, versioned).
"""
import ast
import base64
import fnmatch
import hashlib
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


_ORIG_GIT = _git


# --- gate: framing lock (GOVERNANCE §2/§8 + the campaign-banned phrasings) ---------------
BANNED = [
    "the gluing creates causal structure",
    "the universe is a figure-eight knot",
    "we derived Einstein's equations",
    "Fibonacci anyon physics",
    # "toward the full SM" stood here until 2026-11-11. It states an aim, and the owner has ruled that the aim is the goal
    # (the first of the eleven rulings confirmed to main on 2026-11-10; P-758, P-767; B1878).  What stays banned is a
    # statement of arrival: the gate `arrival-phrases`, below.
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
    # B1879 (G10 / PV21): also scan .tex files and match banned phrases case-insensitively.
    files = sorted(n for n in os.listdir(ROOT)
                   if n.endswith((".md", ".tex")) and os.path.isfile(os.path.join(ROOT, n)))
    for d in FRAMING_SCOPE_DIRS:
        for dirpath, _dirs, names in os.walk(os.path.join(ROOT, d)):
            if ".git" in dirpath or "__pycache__" in dirpath:
                continue
            for n in names:
                if n.endswith((".md", ".py", ".txt", ".tex")):
                    files.append(os.path.relpath(os.path.join(dirpath, n), ROOT))
    for rel in files:
        if rel.replace(os.sep, "/") in FRAMING_EXEMPT:
            continue
        try:
            text = _read(rel)
        except Exception:
            continue
        low = text.lower()
        for phrase in BANNED:
            if phrase.lower() in low:
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
    # B1879 (G10 / PV20): every PROVEN row must cite at least one tests/*.py lock.
    if "## Proven" in text:
        psec = text.split("## Proven", 1)[1]
        for stop in LABEL_SECTIONS:
            if stop != "## Proven" and stop in psec:
                psec = psec.split(stop, 1)[0]
        for m in re.finditer(r"^\| (P\d+[a-z]?) \|.*$", psec, flags=re.M):
            if not re.search(r"`tests/[A-Za-z0-9_./]+\.py`", m.group(0)):
                problems.append(f"{m.group(1)}: PROVEN row cites no tests/*.py lock")
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
# G1 of the advisor seat's audit (2026-11-10; reproduced on main, B1861 § 8): this gate compared the working file with the
# same file at HEAD, so it could see an uncommitted change only. A deletion that was COMMITTED passed, and at the push hook's
# clean checkout, where the working file IS HEAD's, the gate could not fail at all. It now also reads history: every commit
# on main's first-parent line after APPEND_ONLY_FROM that touches the log must keep its parent's log as a prefix, or be a
# roll-up whose removed prefix stands verbatim in that commit's own docs/progress/ archives.
APPEND_ONLY_FROM = "f31729801089e2b11e2a586899b6b1336da745fb"     # the rule is checked in history from this commit on (2026-11-10); earlier history is not read
_ORIG_APPEND_ONLY_FROM = APPEND_ONLY_FROM
APPEND_ONLY_WAIVED = {}             # full sha -> the owner's reason. A violating step stays in history; a waiver keeps it visible.
ARCHIVE_IMMUTABLE_FROM = "015be0cc7cfb57a69430a9710fb01c754b53583e"  # B1879 (G1 / a1, P-772(d)): docs/progress/PROGRESS_*.md archives are append-only too
ARCHIVE_IMMUTABLE_WAIVED = {}       # (full sha, path) -> the owner's reason


def _rollup_ok(old, new, archive):
    """the one constitutional exception (GOVERNANCE §9): a PREFIX of dated entries moved verbatim into the archives,
    with any header before the first dated heading preserved (B1879; Review 78 reader addition to P-772(d))."""
    n = 0
    while n < min(len(new), len(old)) and new[-1 - n] == old[-1 - n]:
        n += 1
    retained = old[len(old) - n:]
    removed = old[:len(old) - n]
    if not retained.strip():
        return False, "no common suffix with the earlier log -- not an append, not a roll-up"
    k = removed.find("## 20")
    if k >= 0:
        k_new = new.find("## 20")
        old_hdr = removed[:k].strip()
        new_hdr = (new[:k_new] if k_new >= 0 else new).strip()
        if old_hdr != new_hdr:
            return False, "roll-up: header before the first dated heading was altered"
    moved = removed[k:] if k >= 0 else removed
    ok = bool(moved.strip()) and (moved.strip() in archive)
    return ok, f"roll-up: removed prefix archived verbatim: {ok}"


def append_only_problems(repo, root, waived=(), path="PROGRESS_LOG.md", limit=5):
    """The committed violations of append-only on `repo`'s first-parent line after `root`. A pure function of the commit
    graph: it reads no working file and no date. It FAILS CLOSED: a clone that does not hold `root`, or whose HEAD does not
    descend from it, cannot be verified and is reported so (a shallow clone must not pass with nothing checked)."""
    def git(*a):
        return subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True, timeout=120)
    if git("rev-parse", "--git-dir").returncode != 0:
        return ["cannot verify: not a git repository"], 0
    if git("cat-file", "-e", root + "^{commit}").returncode != 0:
        return [f"cannot verify: the rule's first commit {root[:9]} is not in this clone (shallow or partial)"], 0
    if git("merge-base", "--is-ancestor", root, "HEAD").returncode != 0:
        return [f"cannot verify: HEAD does not descend from the rule's first commit {root[:9]}"], 0
    commits = git("log", "--first-parent", "--reverse", "--format=%H", f"{root}..HEAD", "--", path).stdout.split()
    problems = []
    for c in commits:
        if c in waived:
            continue
        old, new = git("show", f"{c}^:{path}"), git("show", f"{c}:{path}")
        if old.returncode != 0:
            continue                                   # the log did not exist before this commit
        if new.returncode != 0:
            problems.append(f"{c[:9]} deletes {path}")
            continue
        if new.stdout.startswith(old.stdout):
            continue
        # B1879 (Review 78 reader addition to P-772(d)): a roll-up commit must add or extend the archive in that commit itself.
        names = [f for f in git("diff-tree", "--no-commit-id", "--name-only", "--diff-filter=AM", "-r", f"{c}^", c, "--", "docs/progress/").stdout.split("\n") if f.endswith(".md")]
        archive = "".join(git("show", f"{c}:{f}").stdout for f in sorted(names))
        ok, why = _rollup_ok(old.stdout, new.stdout, archive)
        if not ok:
            problems.append(f"{c[:9]} changes or removes earlier text of {path} ({why})")
    return problems[:limit], len(commits)


def archive_append_only_problems(repo, root, waived=(), limit=5):
    """B1879 (G1 / a1, P-772(d)): every commit after `root` touching docs/progress/PROGRESS_*.md must either add a new
    roll-up archive or preserve its parent's content as a strict prefix."""
    def git(*a):
        return subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True, timeout=120)
    if git("rev-parse", "--git-dir").returncode != 0:
        return ["cannot verify: not a git repository"], 0
    if git("cat-file", "-e", root + "^{commit}").returncode != 0:
        return [f"cannot verify: archive rule commit {root[:9]} is not in this clone (shallow or partial)"], 0
    if git("merge-base", "--is-ancestor", root, "HEAD").returncode != 0:
        return [f"cannot verify: HEAD does not descend from archive rule commit {root[:9]}"], 0
    spec = ":(glob)docs/progress/PROGRESS_*.md"
    commits = git("log", "--first-parent", "--reverse", "--format=%H", f"{root}..HEAD", "--", spec).stdout.split()
    problems = []
    for c in commits:
        changed = [f for f in git("diff-tree", "--no-commit-id", "--name-only", "-r", f"{c}^", c, "--", spec).stdout.splitlines() if f.strip()]
        for f in changed:
            if (c, f) in waived or c in waived:
                continue
            old, new = git("show", f"{c}^:{f}"), git("show", f"{c}:{f}")
            if old.returncode != 0:
                continue
            if new.returncode != 0:
                problems.append(f"{c[:9]} deletes archive {f}")
            elif not new.stdout.startswith(old.stdout):
                problems.append(f"{c[:9]} rewrites or truncates archive {f}")
    return problems[:limit], len(commits)


def gate_append_only():
    """Append-only, with the one constitutional exception (GOVERNANCE §9): a quarterly
    roll-up may move a PREFIX of dated entries verbatim into docs/progress/ — the gate
    then requires (a) the live log ends with HEAD's retained suffix and (b) the removed
    prefix appears verbatim inside the docs/progress/ archives.

    Two checks. (1) HISTORY: every commit after APPEND_ONLY_FROM that touches the log is an append or a roll-up
    (`append_only_problems`), and after ARCHIVE_IMMUTABLE_FROM every commit touching docs/progress/PROGRESS_*.md is an
    append or new archive (`archive_append_only_problems`); both fail closed without git or in a shallow clone.
    (2) THE WORKING FILE(S) against HEAD, for an uncommitted change."""
    if _git is _ORIG_GIT:
        problems, n = append_only_problems(ROOT, APPEND_ONLY_FROM, APPEND_ONLY_WAIVED)
        if problems:
            return False, "; ".join(problems)
        arch_root = ARCHIVE_IMMUTABLE_FROM if APPEND_ONLY_FROM == _ORIG_APPEND_ONLY_FROM else APPEND_ONLY_FROM
        arch_problems, n_arch = archive_append_only_problems(ROOT, arch_root, ARCHIVE_IMMUTABLE_WAIVED)
        if arch_problems:
            return False, "; ".join(arch_problems)
        for af in sorted(glob.glob(os.path.join(ROOT, "docs", "progress", "PROGRESS_*.md"))):
            arel = os.path.relpath(af, ROOT).replace(os.sep, "/")
            arc_rc, arc_head = _git("show", f"HEAD:{arel}")
            if arc_rc == 0 and not _read(arel).startswith(arc_head):
                return False, f"working archive {arel} rewrites or truncates HEAD's content"
    else:
        n, n_arch, arch_root = 0, 0, ARCHIVE_IMMUTABLE_FROM
    rc, head = _git("show", "HEAD:PROGRESS_LOG.md")
    if rc != 0:
        return False, "git unavailable: the working log cannot be compared with HEAD's"
    cur = _read("PROGRESS_LOG.md")
    if cur.startswith(head):
        w = APPEND_ONLY_WAIVED                 # the re-audit's a2: a waived commit is not an append, and the sentence must say so
        wa = ARCHIVE_IMMUTABLE_WAIVED
        return True, (f"HEAD prefix preserved; {n} commit(s) since {APPEND_ONLY_FROM[:9]}: {n - len(w)} an append or a roll-up, {len(w)} waived by name"
                      + "".join(f" [{c[:9]}: {why}]" for c, why in sorted(w.items()))
                      + f"; archive commits since {arch_root[:9]}: {n_arch}, archive waived: {len(wa)}"
                      + "".join(f" [{c[:9]} {p}: {why}]" for (c, p), why in sorted(wa.items())))
    arch_dir = os.path.join(ROOT, "docs", "progress")
    archive = ""
    if os.path.isdir(arch_dir):
        for f in sorted(os.listdir(arch_dir)):
            if f.endswith(".md"):
                archive += _read(f"docs/progress/{f}")
    return _rollup_ok(head, cur, archive)


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
        if os.path.isfile(os.path.join(d, "FINDINGS.md")):
            vp = os.path.join(d, "arc_verdict.json")
            if not os.path.isfile(vp):
                missing.append(name)
                continue
            try:
                with open(vp, encoding="utf-8") as fh:
                    obj = json.load(fh)
                if not isinstance(obj, dict):
                    missing.append(f"{name}: arc_verdict.json is not a JSON object")
            except Exception as exc:
                missing.append(f"{name}: corrupt arc_verdict.json ({str(exc)[:60]})")
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


# B1879 (G9 / PV19): inline frozen ceiling so raising docs/ATTRIBUTION_BASELINE.json cannot forgive new tokens.
ATTRIBUTION_CEILING = {
    "CHANGELOG.md": 4,
    "PROGRESS_LOG.md": 6,
    "docs/CAMPAIGN_STATUS.md": 5,
    "docs/CLOSURE_2026-07-11.md": 1,
    "docs/progress/PROGRESS_2026-Q2.md": 4,
    "docs/progress/REVIEWS.md": 5,
    "docs/views/VERDICT_LEDGER.md": 2,
    "frontier/B1010_consolidation_loss/FINDINGS.md": 1,
    "frontier/B1010_consolidation_loss/arc_verdict.json": 1,
    "frontier/B1031_two_thirds_meets_the_voice/FINDINGS.md": 2,
    "frontier/B1031_two_thirds_meets_the_voice/arc_verdict.json": 1,
    "frontier/B1102_exact_hypercharge_solve/PREREGISTRATION.md": 1,
    "frontier/B1134_simultaneous_closing/FINDINGS.md": 1,
    "frontier/B117_interleaving/README.md": 1,
    "frontier/B117_interleaving/probe.py": 1,
    "frontier/B300_cross_chat_sm_attempt/FINDINGS.md": 1,
    "frontier/B300_cross_chat_sm_attempt/cross_chat_sm_attempt.py": 1,
    "frontier/B301_chirality_filter_and_convergence/FINDINGS.md": 1,
    "frontier/B304_gauge_dynamics_skeleton/FINDINGS.md": 1,
    "frontier/B304_gauge_dynamics_skeleton/gauge_dynamics_skeleton.py": 1,
    "frontier/B309_kappa_unification/FINDINGS.md": 1,
    "frontier/B309_kappa_unification/kappa_unification.py": 1,
    "frontier/B310_cascade_realization_exhausted/FINDINGS.md": 1,
    "frontier/B310_cascade_realization_exhausted/cascade_realization_exhausted.py": 1,
    "frontier/B521_audit_integration/FINDINGS.md": 1,
    "frontier/B533_coupling_invariance/FINDINGS.md": 2,
    "frontier/B533_coupling_invariance/audit_fable5_reverify.py": 2,
    "frontier/B562_probation_campaign/PROBATION.md": 4,
    "frontier/B565_gauge_behavior_campaign/PREREGISTRATION.md": 18,
    "frontier/B570_allowed_plays/PREREGISTRATION.md": 12,
    "frontier/B580_chord_program/PREREGISTRATION.md": 1,
    "frontier/B600_level_ladder/packet/LIT_GATE.md": 2,
    "frontier/B656_digest_integration/ORIGINALS_MANIFEST.txt": 1,
    "frontier/B657_invariant_line/ORIGINALS_MANIFEST.txt": 1,
    "frontier/B699_two_object_surgery/PREREG_TWO_OBJECT.md": 1,
    "frontier/B699_two_object_surgery/sa_chain_arithmetic/FINDINGS_CC2.md": 1,
    "frontier/B699_two_object_surgery/sb_whitehead_hearing/FINDINGS_CC2.md": 1,
    "frontier/B705_metallic_hearing_campaign/CAMPAIGN_CLOSE_CC2.md": 1,
    "frontier/B742_negatives_hunt_p1/CAMPAIGN_LEDGER.md": 8,
    "frontier/B742_negatives_hunt_p1/FINDINGS.md": 1,
    "frontier/B742_negatives_hunt_p1/PREREG_ADDENDUM_B_PRIME.md": 1,
    "frontier/B742_negatives_hunt_p1/reviews/S16_REVIEW_4_VERDICT.md": 1,
    "frontier/B742_negatives_hunt_p1/reviews/S16_REVIEW_5_VERDICT.md": 2,
    "frontier/B742_negatives_hunt_p1/reviews/S16_REVIEW_7_VERDICT.md": 1,
    "frontier/B743_rung1_widened/PREREG_RUNG1_WIDENED.md": 3,
    "frontier/B749_genesis_forks/PREREGISTRATION.md": 2,
    "frontier/B756_remaining_doors/PREREG_REMAINING_DOORS.md": 1,
    "frontier/B756_remaining_doors/SYNTHESIS_CC2.md": 1,
    "frontier/B879_selection_cochain/packet/CAMPAIGN_CLOSE.md": 1,
    "frontier/B879_selection_cochain/packet/HANDOFF_CC_SELECTION_COCHAIN.md": 1,
    "frontier/B879_selection_cochain/packet/PREREG_SCC.md": 5,
    "frontier/B879_selection_cochain/packet/STATUS.md": 1,
    "frontier/B879_selection_cochain/packet/w2a_amalgam/FINDINGS_CC3.md": 1,
    "frontier/B879_selection_cochain/packet/w2b_landscape/FINDINGS_CC3.md": 1,
    "frontier/B887_gate_audit/audit_reports.json": 3,
    "frontier/B921_branch_harvest/HARVEST_MANIFEST.md": 2,
    "frontier/B921_branch_harvest/harvested/frontier/B796_coupling_campaign/MASTERPLAN.md": 1,
    "frontier/B921_branch_harvest/harvested/frontier/B796_coupling_campaign/MASTERPLAN_FORWARD.md": 1,
    "frontier/B921_branch_harvest/harvested/frontier/B796_coupling_campaign/context_sweep/sweep_leads_doors.md": 1,
    "frontier/REPO_STATE.md": 3,
    "knowledge/K027_the_convergent_protocol.md": 1,
    "outside_bench/certificates/the_branch_gap.py": 1,
    "outside_bench/certificates/the_chain_right_now.py": 1,
    "outside_bench/certificates/the_jorgensen_number.py": 1,
    "papers/VALIDATION_LEDGER.md": 6,
    "paths/MECHANISM_CLASSES.md": 1,
    "paths/PATHS.md": 1,
    "philosophy/GOVERNANCE.md": 1,
    "philosophy/PHILOSOPHICAL_PATHS.md": 4,
    "tests/test_flagship_paper.py": 2,
    "tests/test_public_surface_scan.py": 3,
    "tests/test_sl4_dehn_filling_paper.py": 2
}
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
        return False, "cannot verify: git unavailable"
    hits = []
    cur_base = _load_attr_baseline()
    if _git is _ORIG_GIT and not os.path.isfile(os.path.join(ROOT, "docs", "ATTRIBUTION_BASELINE.json")):
        hits.append("docs/ATTRIBUTION_BASELINE.json missing")
    for k, v in sorted(cur_base.items()):
        ceil = ATTRIBUTION_CEILING.get(k, 0)
        if v > ceil:
            hits.append(f"ATTRIBUTION_BASELINE raised for {k}: {v} > ceiling {ceil}")
    for rel in out.splitlines():
        if rel.startswith(ATTR_EXEMPT_PREFIXES) or rel in ATTR_EXEMPT_FILES \
                or rel == "scripts/gates/gates.py":
            continue
        if not rel.endswith((".md", ".py", ".txt", ".json", ".yml", ".yaml", ".toml")):
            continue
        try:
            n = len(_VENDOR_RE.findall(_read(rel)))
            allowed = min(cur_base.get(rel, 0), ATTRIBUTION_CEILING.get(rel, 0))
            if n > allowed:
                hits.append(f"{rel} ({n} vendor tokens, baseline {allowed})")
        except Exception:
            continue
    rc2, author = _git("log", "-1", "--format=%an")
    author_ok = (rc2 != 0) or (author.strip() == "originaxiom")
    if not author_ok:
        hits.append(f"last-commit author: {author.strip()}")
    # the owner's ruling R3 (confirmed to main 2026-11-10; the advisor seat's finding G9): the rule is about commits, and this
    # gate read only tracked files and the last commit's author.  It now reads every commit message after ATTRIBUTION_FROM.
    problems, n = attribution_history_problems(ROOT, ATTRIBUTION_FROM)
    hits += problems
    return not hits, (hits[:10] if hits else f"ok ({n} commit(s) since {ATTRIBUTION_FROM[:9]} read: each by originaxiom, no vendor token and no co-author trailer in its message)")


# The rule is read in history AFTER this commit: the most recent one on the first-parent line whose message carries a vendor
# token or a co-author trailer (2026-09-16; 693 commits at or before it do).  The 696 after it, to Review 78, all pass.
ATTRIBUTION_FROM = "da25c4f497adf5b137f95e5f5ee98d6513c159d9"
_TRAILER_RE = re.compile(r"^\s*co-authored-by\s*:", re.I | re.M)


def attribution_history_problems(repo, root, limit=5):
    """(problems, commits read) for the commits on `repo`'s first-parent line after `root`: each is authored `originaxiom` and
    its message carries no vendor token and no co-author trailer.  A pure function of the commit graph.  With no repository it
    reports nothing (the caller says 'skipped'); where a repository is there and the history cannot be read, it fails closed."""
    def git(*a):
        return subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True, timeout=120)
    if git("rev-parse", "--git-dir").returncode != 0:
        return [], 0
    if git("cat-file", "-e", root + "^{commit}").returncode != 0:
        return [f"cannot verify: the commit the attribution rule is read from, {root[:9]}, is not in this clone (shallow or partial)"], 0
    if git("merge-base", "--is-ancestor", root, "HEAD").returncode != 0:
        return [f"cannot verify: HEAD does not descend from {root[:9]}, the commit the attribution rule is read from"], 0
    out = git("log", "--first-parent", "--format=%H%x00%an%x00%B%x01", f"{root}..HEAD").stdout
    problems, n = [], 0
    for rec in out.split("\x01"):
        if "\x00" not in rec:
            continue
        h, an, body = rec.strip("\n").split("\x00", 2)
        n += 1
        if an.strip() != "originaxiom":
            problems.append(f"{h[:9]}: authored by {an.strip()!r}, not originaxiom")
        if _VENDOR_RE.search(body):
            problems.append(f"{h[:9]}: a vendor token in the commit message")
        if _TRAILER_RE.search(body):
            problems.append(f"{h[:9]}: a co-author trailer in the commit message")
    return problems[:limit], n


# --- gate: forbidden tracked artifacts -----------------------------------------------------
def gate_tracked_forbidden():
    rc, out = _git("ls-files")
    if rc != 0:
        return False, "cannot verify: git unavailable"
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
        if rc != 0:
            return False, "cannot verify: git unavailable"
        if int(out.strip() or 0) == 0:
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
# P-420 phase 0 (2026-10-29): the folder pattern below read only a lower-case suffix, so B89T_tower_route (an upper-case
# suffix, carrying "id": "B89") collided with B89_sl4_symbolic_M4L unseen. The pattern now reads either case; B89 is
# historical (both folders banked in June) and is grandfathered beside B58.
GRANDFATHERED_IDS = frozenset({"B58", "B89"})


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
        m = re.match(r"(B\d+)[A-Za-z]?_", name)
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
    if _git("rev-parse", "--git-dir")[0] != 0:
        return False, "cannot verify: git unavailable"
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "checks"))
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


# NAME = Path(__file__).resolve().parent  |  .parents[k]  |  either followed by / "a" / "b" (a base inside another folder)
_FILE_BASE = re.compile(r'^(\w+)\s*=\s*(?:pathlib\.)?Path\(__file__\)(?:\.resolve\(\))?\.(parent|parents\[(\d+)\])'
                        r'((?:\s*/\s*"[^"]+")*)(?=\s*(?:$|;|#))', re.M)


_OS_DIR = r'os\.path\.dirname\(\s*(?:os\.path\.abspath\(\s*__file__\s*\)|__file__)\s*\)'
_OS_BASE = re.compile(r'^(\w+)\s*=\s*(' + _OS_DIR + r'|os\.path\.dirname\(\s*' + _OS_DIR + r'\s*\))\s*$', re.M)


def _ast_file_relative_refs(rel, txt):
    """B1879 (L4 / p2): AST constant-propagation pass resolving multi-step path/string assembly
    (e.g. `RUNS = HERE / "runs"; name = "driver_k1" + ".log"; RUNS / name`)."""
    try:
        tree = ast.parse(txt)
    except Exception:
        return set()
    here = os.path.dirname(rel)
    found = set()

    def _up_dir(base, n):
        p = base
        for _ in range(n):
            p = os.path.dirname(p)
        return p

    def _eval_str(node, senv):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        if isinstance(node, ast.Name) and node.id in senv:
            return senv[node.id]
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            l, r = _eval_str(node.left, senv), _eval_str(node.right, senv)
            return (l + r) if (l is not None and r is not None) else None
        if isinstance(node, ast.JoinedStr):
            parts = []
            for v in node.values:
                s = _eval_str(v.value if isinstance(v, ast.FormattedValue) else v, senv)
                if s is None:
                    return None
                parts.append(s)
            return "".join(parts)
        return None

    # Nodes that are left-operands of an outer `/` or probed only inside `not (<expr>).exists()`
    non_leaf = set()
    neg_exists = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            non_leaf.add(id(node.left))
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
            opnd = node.operand
            if isinstance(opnd, ast.Call) and isinstance(opnd.func, ast.Attribute) and opnd.func.attr in ("exists", "is_file"):
                neg_exists.add(id(opnd.func.value))

    def _record_leaf(node, joined):
        if id(node) in non_leaf or id(node) in neg_exists:
            return
        if "." in os.path.basename(joined):
            found.add(joined)

    def _eval_path(node, penv, senv):
        if isinstance(node, ast.Name) and node.id in penv:
            return penv[node.id]
        # Path(__file__) or pathlib.Path(__file__) or .resolve()
        if isinstance(node, ast.Call):
            fn = node.func
            fname = fn.id if isinstance(fn, ast.Name) else (fn.attr if isinstance(fn, ast.Attribute) else None)
            if fname == "Path" and len(node.args) == 1 and isinstance(node.args[0], ast.Name) and node.args[0].id == "__file__":
                return ("__FILE__", rel)
            if fname == "abspath" and len(node.args) == 1 and isinstance(node.args[0], ast.Name) and node.args[0].id == "__file__":
                return ("__FILE__", rel)
            if fname == "resolve" and not node.args and isinstance(fn, ast.Attribute):
                return _eval_path(fn.value, penv, senv)
            if fname == "dirname" and len(node.args) == 1:
                inner = _eval_path(node.args[0], penv, senv)
                if inner is not None:
                    return ("DIR", _up_dir(inner[1], 1))
                if isinstance(node.args[0], ast.Name) and node.args[0].id == "__file__":
                    return ("DIR", here)
            if fname == "join" and len(node.args) >= 2 and isinstance(fn, ast.Attribute):
                base = _eval_path(node.args[0], penv, senv)
                if base is not None and base[0] in ("DIR", "JOINED"):
                    segs = [_eval_str(a, senv) for a in node.args[1:]]
                    if all(s is not None for s in segs):
                        joined = os.path.normpath(os.path.join(base[1], *segs)).replace(os.sep, "/")
                        _record_leaf(node, joined)
                        return ("JOINED", joined)
        if isinstance(node, ast.Attribute) and node.attr == "parent":
            inner = _eval_path(node.value, penv, senv)
            if inner is not None:
                return ("DIR", _up_dir(inner[1], 1))
        if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Attribute) and node.value.attr == "parents":
            inner = _eval_path(node.value.value, penv, senv)
            idx = node.slice.value if isinstance(node.slice, ast.Constant) and isinstance(node.slice.value, int) else None
            if inner is not None and idx is not None:
                return ("DIR", _up_dir(inner[1], idx + 1))
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            base = _eval_path(node.left, penv, senv)
            seg = _eval_str(node.right, senv)
            if base is not None and base[0] in ("DIR", "JOINED") and seg is not None:
                joined = os.path.normpath(os.path.join(base[1], seg)).replace(os.sep, "/")
                _record_leaf(node, joined)
                return ("JOINED", joined)
        return None

    def _skip_guarded_vars(stmts):
        guarded = set()
        for st in stmts:
            if isinstance(st, ast.If) and isinstance(st.test, ast.UnaryOp) and isinstance(st.test.op, ast.Not):
                opnd = st.test.operand
                if (isinstance(opnd, ast.Call) and isinstance(opnd.func, ast.Attribute)
                        and opnd.func.attr in ("is_file", "exists") and isinstance(opnd.func.value, ast.Name)):
                    if any(isinstance(b, ast.Expr) and isinstance(b.value, ast.Call)
                           and "skip" in (b.value.func.attr if isinstance(b.value.func, ast.Attribute)
                                          else (b.value.func.id if isinstance(b.value.func, ast.Name) else ""))
                           for b in st.body):
                        guarded.add(opnd.func.value.id)
        for sub in ast.walk(ast.Module(body=stmts, type_ignores=[])):
            if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Attribute) and isinstance(sub.func.value, ast.Name):
                if sub.func.attr in ("write_text", "write_bytes", "unlink"):
                    guarded.add(sub.func.value.id)
        return guarded

    def _walk_scope(stmts, penv, senv):
        penv, senv = dict(penv), dict(senv)
        guarded = _skip_guarded_vars(stmts)
        for st in stmts:
            if isinstance(st, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                _walk_scope(st.body, penv, senv)
                continue
            if isinstance(st, ast.Assign) and len(st.targets) == 1 and isinstance(st.targets[0], ast.Name):
                nm = st.targets[0].id
                if nm in guarded:
                    continue
                sv = _eval_str(st.value, senv)
                if sv is not None:
                    senv[nm] = sv
                else:
                    pv = _eval_path(st.value, penv, senv)
                    if pv is not None:
                        penv[nm] = pv
            for sub in ast.walk(st):
                _eval_path(sub, penv, senv)

    _walk_scope(tree.body, {}, {})
    return found


def _file_relative_refs(rel, txt):
    """The paths a file reads relative to ITSELF, in the two idioms the record uses:
    `HERE = pathlib.Path(__file__).resolve().parent`, then `HERE / "a" / "b"`; and
    `HERE = os.path.dirname(os.path.abspath(__file__))`, then `os.path.join(HERE, "a", "b")` (or the dirname inline),
    plus multi-step constant string/path bindings via `_ast_file_relative_refs` (B1879, L4 / p2)."""
    out = set(_ast_file_relative_refs(rel, txt))

    def add(base, parts):
        out.add(os.path.normpath(os.path.join(base, *parts)).replace(os.sep, "/"))
    for m in _FILE_BASE.finditer(txt):
        up = 1 if m.group(2) == "parent" else int(m.group(3)) + 1
        base = rel
        for _ in range(up):
            base = os.path.dirname(base)
        base = os.path.join(base, *re.findall(r'"([^"]+)"', m.group(4)))
        for ch in re.finditer(r'(?<![\w.])%s((?:\s*/\s*"[^"]+")+)' % re.escape(m.group(1)), txt[:m.start()] + txt[m.end():]):
            add(base, re.findall(r'"([^"]+)"', ch.group(1)))
    here = os.path.dirname(rel)
    bases = {}
    for m in _OS_BASE.finditer(txt):
        bases[m.group(1)] = os.path.dirname(here) if m.group(2).count("dirname") == 2 else here
    for name, base in bases.items():
        for ch in re.finditer(r'os\.path\.join\(\s*%s\s*((?:,\s*"[^"]+"\s*)+)\)' % re.escape(name), txt):
            add(base, re.findall(r'"([^"]+)"', ch.group(1)))
    for ch in re.finditer(r'os\.path\.join\(\s*' + _OS_DIR + r'\s*((?:,\s*"[^"]+"\s*)+)\)', txt):
        add(here, re.findall(r'"([^"]+)"', ch.group(1)))
    return out


def _git_would_ignore(paths):
    """which of these repository-relative paths git would ignore, whether or not they exist on disk"""
    if not paths:
        return set()
    import subprocess
    r = subprocess.run(["git", "-C", str(ROOT), "check-ignore", "--no-index", "--stdin"], input="\n".join(sorted(paths)) + "\n",
                       capture_output=True, text=True)
    return {l for l in r.stdout.split("\n") if l}


def gate_tracked_deps(_plant=None):
    """Every repo path a tracked test/script names must itself be TRACKED, not merely present.

    E57 (B1238, 2026-09-02): B1237 committed `tests/test_paper_ledger_counts.py` and pushed it
    with the tool it runs, `scripts/checks/paper_ledger_counts.py`, still untracked -- the
    file sat on the bench, so the local suite was green and `path-refs` resolved it; only a
    fresh clone would have redded. This is the complement of `path-refs`: that gate asks
    "does the cited path exist?", this one asks "does git HAVE it?". Scope is tracked .py
    under tests/ and scripts/ (the executable reference graph); a path is checked only when it
    exists on disk (a missing path is `path-refs`' business, or an intentional skipif).
    Fail-closed if git is unavailable -- an index we cannot read is not an index we may vouch for.

    E94, second scope (Review 77, 2026-11-10): a LOCK -- a tracked test_*.py under tests/ or frontier/ -- is also read for
    the paths it names relative to its own file (`HERE / "run.txt"`).  B1671's three logs (Review 73) and B1854's three
    (Review 77) were read that way and ignored by `*.log`, so each lock passed at home and failed on a fresh clone, and
    this gate saw neither: it read only tests/ and scripts/ and only repo-root paths.  Scripts are left out on purpose:
    a generator may keep an ignored cache; a lock may not depend on one.  `_plant` is the control's door: one more
    (path, text) pair read as if tracked.

    Third scope, the same day (main's own planted run of the advisor seat's PV25): as first widened, the gate flagged a
    lock's path only when the file was ON DISK and untracked, so it could fire on the author's tree and never in a clean
    checkout, which is where the push hook runs it.  A lock's own-directory path that git WOULD IGNORE is now refused
    whether or not the file exists; and the `os.path.join(os.path.dirname(__file__), ...)` idiom is read as well.
    """
    rc, out = _git("ls-files")
    if rc != 0:
        return False, f"git ls-files failed: {out[:80]}"
    tracked = set(out.split("\n"))
    lit = re.compile(r"(?:scripts|frontier|docs|tests|data|paper)/[\w./-]+\.(?:py|sh|json|md|txt|csv)")
    chain = re.compile(r'ROOT(?:\s*/\s*"[^"]+")+')
    bad, absent = {}, {}
    sources = sorted(tracked) + ([_plant[0]] if _plant else [])
    for rel in sources:
        core = rel.startswith(("tests/", "scripts/")) and rel.endswith(".py")
        lock = rel.startswith(("tests/", "frontier/")) and os.path.basename(rel).startswith("test_") and rel.endswith(".py")
        if not (core or lock):
            continue
        try:
            txt = _plant[1] if (_plant and rel == _plant[0]) else _read(rel)
        except OSError:
            continue                                   # deleted-but-tracked: not this gate's class
        refs = set()
        if core:
            refs |= set(lit.findall(txt))
            for ch in chain.findall(txt):
                refs.add("/".join(re.findall(r'"([^"]+)"', ch)))
        own = _file_relative_refs(rel, txt) if lock else set()
        refs |= own
        for r in refs:
            if r not in tracked and os.path.isfile(os.path.join(ROOT, r)):
                bad.setdefault(r, rel)
        for r in own:
            if r not in tracked and not os.path.isdir(os.path.join(ROOT, r)):
                absent.setdefault(r, rel)
    for r in sorted(_git_would_ignore(set(absent) - set(bad))):
        bad.setdefault(r, absent[r] + " (git ignores this path: a clean checkout will not have it)")
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
    if _git("rev-parse", "--git-dir")[0] != 0:
        return False, "cannot verify: git unavailable"
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "checks"))
    try:
        import check_test_vacuity as ctv
    except Exception as exc:
        return False, f"vacuity checker missing or unimportable: {exc}"   # fail-closed
    finally:
        sys.path.pop(0)
    total, no_assert, tautology, both_lit = ctv.scan()
    if total == 0 or not glob.glob(os.path.join(ROOT, "tests", "test_b*.py")):
        return False, "cannot verify: core tests/test_b*.py missing or 0 tests scanned"
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
    # S264b (2026-10-30, P-513): README.md carries a block generate.py fills; it is snapshotted, compared and restored too
    readme = pathlib.Path(ROOT) / "README.md"
    readme_raw = readme.read_bytes() if readme.is_file() else None

    def _restore():
        if readme_raw is not None and readme.read_bytes() != readme_raw:
            readme.write_bytes(readme_raw)
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
        if readme_raw is not None and readme.read_bytes() != readme_raw:
            stale.append("README.md (its state block)")
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
        return False, "cannot verify: git unavailable"
    last_log = out.strip()
    rc2, out2 = _git("rev-list", "--count", f"{last_log}..HEAD", "--", "CHANGELOG.md")
    if rc2 != 0:
        return False, "cannot verify: git unavailable"
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
    if not links:
        return False, "docs/THEOREM_LEDGER.md has 0 C-links -- empty or corrupt ledger"
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
    if not rows:
        return False, "docs/LAW_MAP.md has 0 law rows -- empty or corrupt map"
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
# Review 66 (R65-6, P-123): vocabulary drift defeats a claim-line sweep, so from this arc on a sealed file's 'Seen first'
# section cites a full-text sweep (topic_sweep.py --full prints "full text" on its VERDICT line; the aliases are on by default)
FULL_SWEEP_FROM_ARC = 1685


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
        if sections and arc >= FULL_SWEEP_FROM_ARC:
            seen = re.search(r"(?ms)^##[^\n]*Seen first[^\n]*\n(.*?)(?=^## |\Z)", txt)
            if not (seen and "full text" in seen.group(1).lower()):
                bad.append(rel + " (its Seen-first sweep is not full text)"); continue
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


SEAL_PATTERNS = ("PREREG*", "*DESIGN*.md", "SEALED*.md", "DECLARATION.md", "PRE_RUN_NOTE*.md", "*RULE.md")     # B1879 (G2 / s2, s3): includes PRE_RUN_NOTE*.md, *RULE.md & recursive subdirectories


def sealed_style_files(root=None):
    """every sealed-style file under frontier/B*/**, by the ledger generator's patterns (wider than `sealed_files`, which the
    provenance gate reads)"""
    import glob
    root = str(root or ROOT); out = set()
    for pat in SEAL_PATTERNS:
        for p in glob.glob(os.path.join(root, "frontier", "B*", "**", pat), recursive=True):
            if os.path.isfile(p):
                out.add(os.path.relpath(p, root).replace(os.sep, "/"))
    return sorted(out)


def gate_seal_ledger_current():
    """R55-14 (B1464): docs/SEAL_LEDGER.md is a generated view (scripts/seal_ledger.py); its table must list every
    sealed-style file on disk. It was ~530 arcs stale for two months with nothing watching it.

    The advisor seat's audit, G2 (2026-11-10; its PV6, reproduced on main): the gate checked only that each path was
    listed, so a generated row's hash could be changed by hand and pass. Every generated row is now RECOMPUTED from its
    file; a listed file that is gone fails; and the files required are the generator's own (a seal named PREREG.md or
    *DESIGN*.md was outside the gate's narrower list)."""
    import hashlib
    ledger = _read("docs/SEAL_LEDGER.md")
    rows = dict(re.findall(r"^\| (frontier/B[^ |]+) \| ([0-9a-f]{8}) \|", ledger, re.M))
    listed = set(re.findall(r"^\| (frontier/B[^ |]+) \|", ledger, re.M))
    missing = [rel for rel in sealed_style_files() if rel not in listed]
    if missing:
        return False, "%d sealed file(s) not in the generated table (run scripts/seal_ledger.py): " % len(missing) + ", ".join(missing[:4])
    bad = []
    for rel, h8 in sorted(rows.items()):
        f = os.path.join(ROOT, rel)
        if not os.path.isfile(f):
            bad.append("%s is listed and is not in the tree" % rel)
        elif hashlib.sha256(open(f, "rb").read()).hexdigest()[:8] != h8:
            bad.append("%s: the ledger's hash %s is not the file's" % (rel, h8))
    if bad:
        return False, "; ".join(bad[:4])
    return True, "ok (%d sealed files listed, each row's hash recomputed)" % len(listed)


# The advisor seat's audit, G2, graded critical (2026-11-10; its PV3 to PV5, reproduced on main): an edit of a sealed file
# AFTER its seal was detected for the few files with a hand-written ledger row only. A sentence appended to the candidate's
# pre-registration and committed passed every seal gate; so did deleting a sealed file, and editing one while regenerating
# its ledger row. This gate reads history, as the append-only gate does: after SEAL_IMMUTABLE_FROM no commit on main's
# first-parent line may modify, delete or move a sealed-style file. A seal is ADDED once. An amendment is a new file beside
# it. An exception is a waiver here that names the commit and the path, with the owner's reason.
SEAL_IMMUTABLE_FROM = "76a4ff388b719a15af955e6acd3b99ec676d42a0"     # the rule is read in history from this commit on (2026-11-10)
SEAL_IMMUTABLE_WAIVED = {}                                             # (full sha, path) -> the owner's reason


def seal_immutable_problems(repo, root, waived=(), limit=5):
    """The committed changes to sealed-style files on `repo`'s first-parent line after `root`: (problems, commits read).
    A pure function of the commit graph. It fails closed where the history cannot be read."""
    def git(*a):
        return subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True, timeout=120)
    if git("rev-parse", "--git-dir").returncode != 0:
        return ["cannot verify: not a git repository"], 0
    if git("cat-file", "-e", root + "^{commit}").returncode != 0:
        return [f"cannot verify: the rule's first commit {root[:9]} is not in this clone (shallow or partial)"], 0
    if git("merge-base", "--is-ancestor", root, "HEAD").returncode != 0:
        return [f"cannot verify: HEAD does not descend from the rule's first commit {root[:9]}"], 0
    specs = [":(glob)frontier/B*/**/" + pat for pat in SEAL_PATTERNS]
    commits = git("log", "--first-parent", "--reverse", "--format=%H", f"{root}..HEAD", "--", *specs).stdout.split()
    verbs = {"M": "edits", "D": "deletes", "R": "moves", "T": "changes the type of", "C": "copies over"}
    problems = []
    for c in commits:
        out = git("diff-tree", "--no-commit-id", "--name-status", "-r", "-M", f"{c}^", c, "--", *specs).stdout
        for line in out.splitlines():
            parts = line.split("\t")
            if len(parts) < 2 or parts[0].startswith("A"):
                continue                               # a new sealed file is a seal
            path = parts[1]                            # for a move, the sealed file's own (old) path
            if (c, path) in waived:
                continue
            problems.append(f"{c[:9]} {verbs.get(parts[0][0], 'changes')} the sealed file {path}")
    return problems[:limit], len(commits)


def gate_seal_immutable():
    """A sealed-style file does not change after its seal (the advisor seat's audit, G2). See the note above."""
    problems, n = seal_immutable_problems(ROOT, SEAL_IMMUTABLE_FROM, SEAL_IMMUTABLE_WAIVED)
    if problems:
        return False, "; ".join(problems)
    w = SEAL_IMMUTABLE_WAIVED
    return True, (f"ok ({n} commit(s) since {SEAL_IMMUTABLE_FROM[:9]} touch a sealed-style file, each only adding one, or waived by name; waived: {len(w)}"
                  + "".join(f" [{c[:9]} {p}: {why}]" for (c, p), why in sorted(w.items())) + ")")


# THE SCRIPTS A SEAL HASHED (the advisor seat's second re-audit, 2026-11-10; its planted case s1, measured and gated in B1874).
# A seal names two things: what will count, and the code that will compute it.  The gates above protect the first.  189 folders
# carry a list of hashed files (ARTIFACT_HASHES*.txt) and no gate read one, so a sealed criterion could not be changed after the
# fact and the script that evaluates it could.  Two checks close that:
#   (1) every entry of every tracked list still verifies against the tracked file it names -- except the entries that did not on
#       2026-11-10, frozen below by key as a ceiling that may only shrink (docs/ARTIFACT_HASHES_BROKEN.md says what each one is);
#   (2) a list itself does not change after it is committed: history is read as for the sealed files, from the rule's first commit.
# Together: a listed script cannot be edited (1), and the list cannot be edited to match (2).  A repair is a new list beside the old.
ARTIFACT_HASH_GLOB = "ARTIFACT_HASHES*.txt"
_HEX64 = re.compile(r"(?<![0-9a-f])([0-9a-f]{64})(?![0-9a-f])")
ARTIFACT_HASHES_BROKEN = frozenset((          # 63 entries, as found on 2026-11-10; each is a row of docs/ARTIFACT_HASHES_BROKEN.md
    "02ea635d28e4", "06458ed7c5bb", "06e82ea84734", "09b03b0f5a17", "0f676ba0859b", "1425dd14fa31", "1a0d44019eee", "1d6b5ee7558d",
    "1ec90f1c68fd", "21b857462e0d", "25732c881109", "2eb7fd535c37", "32d25b5ab1c0", "35c825435176", "364bd75c9f7c", "4496610d521a",
    "46b056c1d0cd", "5016a52c4e0c", "5ce1a4764092", "65bf3f5fbacc", "68f916e3c6ff", "6c6c1c530bd1", "6d730200be1c", "6ebd8e4c93f4",
    "6fc7e0fe470f", "6fcddd572169", "740cbb6a1698", "756fcc1dfcbc", "761da67ed455", "7d1d25023434", "7f11b8227c1b", "8edb72a566ef",
    "93a1fa13ed35", "94b613da1a0b", "96d7ceb60570", "9d9af43f0d7a", "a1b557f176e6", "a50ecf35c25c", "a781df3d8c83", "aa706b8423e2",
    "b0784290c658", "b08f5c13fb89", "b172cca70c9d", "b1ee7bcab53b", "bb31a0e7ad28", "c40fd50bc5f9", "c4c204301962", "c74fc59dcb91",
    "cb74650a43c6", "d8ef558d9c73", "da15d6f062e9", "e129fe00f880", "e2df6ca12f6c", "e3b1af50cac7", "e7a0d80c61dc", "e7a0e6996e21",
    "e8640674a562", "ed75482fbcf7", "ed90ccc5013d", "ef83de39507e", "efc217e26982", "f86e2456f4e8", "ffbed605bc39",
))
ARTIFACT_HASHES_IMMUTABLE_FROM = "270a27ee6c500c4f883cdd6a0e33558b89b71e5a"     # the rule is read in history from this commit on (2026-11-10)
ARTIFACT_HASHES_WAIVED = {}                                                # (full sha, path) -> the owner's reason
# A disclosed amendment after this rule: the changed file's new hash goes into a NEW list beside the old one, and the old entry's
# key is named here with the reason.  Every key named here is printed on every run, so an amendment cannot pass unseen.
ARTIFACT_HASHES_AMENDED = {}                                               # key -> where the amendment is disclosed


def _hash_list_entry(line):
    """(sha256, the file name it is recorded for) for one line of a list of hashed files, in any format the record uses;
    None for a line that records no hash; (sha256, None) for a hash with no file name beside it"""
    m = _HEX64.search(line)
    if not m:
        return None
    rest = (line[:m.start()] + " " + line[m.end():]).strip()
    rest = re.sub(r"\bsha256\b\s*[:=]?", " ", rest, flags=re.I)
    names = [t.strip("`'\",;()*:=") for t in rest.split() if "." in t or "/" in t]
    return m.group(1), (names[0] if names else None)


HASH_LIST_ROOT_PREFIXES = (
    "frontier/", "scripts/", "tests/", "docs/", "papers/",
    "outside_bench/", "knowledge/", "philosophy/", "speculations/", "story/", "src/",
)
ARTIFACT_HASHES_BROKEN_DISK = {
    "02ea635d28e4": ("frontier/B628_exterior_comparison/COMPARISON_DESIGN.md", "7b5f2ff77c4b0044dae2a56b6a8ea825a193a75daab9efcc48c19ba2026faac7"),
    "06458ed7c5bb": ("frontier/B656_digest_integration/ORIGINALS_MANIFEST.txt", "aa8bb67d455f2afed1ea886947d20c6da48626038efdb2e9afbb01be0737b5b8"),
    "0f676ba0859b": ("frontier/B1493_the_room_on_the_companions/verification/room.py", "ebcf9aab48d0c890d4b4eec38a14f2cc700598c13411f036ea748e7be15de5ba"),
    "1425dd14fa31": ("frontier/B1490_the_common_cover_verified/verification/common_cover_main.py", "e8bf122371c34f6bc52abbc27f8459310a14e14a5565d4261918ae0c018ddda8"),
    "21b857462e0d": ("frontier/B634_conductor_chord/ERRATUM_1.md", "eda33b8d4048ac013e43b7972ce623be8fdc2045c8d66dbb9048998a7d58d7c2"),
    "25732c881109": ("frontier/B684_loop7_close/FINDINGS.md", "efc8c2a241b3988761c684612bec225521007988850705e1c3d3a4c2bc3641c2"),
    "35c825435176": ("frontier/B682_habiro_dictionary/PHASE0_EXTRACTION_CC.md", "1bf08038bc4450cd7beefb6f76d191c3cd1d46d709391825733a56644667aeca"),
    "364bd75c9f7c": ("frontier/B742_negatives_hunt_p1/FINDINGS.md", "60e48d21ce147aa196915f2f4dfa2923310112bfb720fdb9808ec200f09de82f"),
    "4496610d521a": ("frontier/B1654_the_norm_of_the_boundary_class/verification/before_the_seal/review2/blocks.py", "7506a1851a55eea86810b6e936cf4cba9dc13c5312755df2aacb8c6612162d82"),
    "46b056c1d0cd": ("frontier/B1486_the_two_orders_at_the_silver_members/verification/fused.py", "16fc24457ca399bb5f6253663499522346186f3e9d9bf44baaec69fd25300bf4"),
    "5016a52c4e0c": ("frontier/B1823_step_a_the_tied_heavy_vacuum/verification/search.py", "cdfbffa8cbaa522b6ff7efe48f55f629ff658dc98ef718b2143cb6efe8ec7466"),
    "5ce1a4764092": ("frontier/B1490_the_common_cover_verified/verification/congruence_level.json", "aff4e027108dfc3244406f25b121b254a67aa73c39d7b42c0c77c6daafe9bb22"),
    "68f916e3c6ff": ("frontier/B1494_no_room_on_any_companion/verification/companions.py", "88e3cf7ac3de76c642841f0375b06b6a3b2a56e04dd7ef30f488144484e37862"),
    "6c6c1c530bd1": ("frontier/B1654_the_norm_of_the_boundary_class/verification/before_the_seal/review/pre.py", "d6c19a3bd58112517997aca23246aae01d32eb0a83fa69350ab14410a9484ae0"),
    "6d730200be1c": ("frontier/B1490_the_common_cover_verified/verification/level_recount.json", "c2a570f0b40bc2fb1e5794c83b39cddd549817f8d46c16cee59576bca5758b63"),
    "6ebd8e4c93f4": ("frontier/B697_frobenius_gluing/FINDINGS.md", "7f440f5a45b1007db47a08f875ba2806244752e60abe46460837ecc94396ab14"),
    "6fc7e0fe470f": ("frontier/B1605_the_cover_read_from_the_base/verification/schreier_cover.py", "9e68d659d66f41e232d9511c4331857aaf45e6323e00b3e277f22b66e16fdb02"),
    "740cbb6a1698": ("frontier/B1490_the_common_cover_verified/verification/congruence_level.py", "6e65917ae19fb11e4af7f0974d2da73c58e95316da156675864c926af9672e62"),
    "756fcc1dfcbc": ("frontier/B1493_the_room_on_the_companions/verification/control_m136.json", "6b4b1182b458ce7942bf852e8b709e6c5980620eb0e0c927e706f8f89605b889"),
    "761da67ed455": ("frontier/B1654_the_norm_of_the_boundary_class/verification/before_the_seal/review2/pre2.py", "adc59a7885ca6c0e36c94bda3cd85b349d1be1a1dfbe30430b7b69cf9c18da7b"),
    "7f11b8227c1b": ("frontier/B675_hcusp_sweep/FINDINGS.md", "4748ccdbaa6e0a458c291304f9aebe81b867c9170d5c155818d355d7b1130318"),
    "93a1fa13ed35": ("frontier/B749_genesis_forks/FINDINGS.md", "8b38120e73776063d3da312360ad8036e01c7af8d745baa8a4815b6b5c87480c"),
    "96d7ceb60570": ("frontier/B656_digest_integration/verify_g1_g4.py", "d64c48cb6ee688f0d088dfa246ed44459067bba97de8bb04a0525f8308938fa3"),
    "9d9af43f0d7a": ("frontier/B1486_the_two_orders_at_the_silver_members/verification/fused_cell.py", "f2ecb7c0eb59476c7e600141aa77bbf9573c923d173bba90b1b55ce99b437a82"),
    "a1b557f176e6": ("philosophy/P019_the_genesis_axiom_chain.md", "c6b7139d42336ab2f6fb5cd594f510a94f949050ad39fd394667561e8b5c5e80"),
    "b0784290c658": ("frontier/B1823_step_a_the_tied_heavy_vacuum/verification/search.py", "cdfbffa8cbaa522b6ff7efe48f55f629ff658dc98ef718b2143cb6efe8ec7466"),
    "b08f5c13fb89": ("frontier/B660_structure_campaign/FINDINGS.md", "43800eeb49cfa9a76aee48a02041847caf38d4e4ec0cd77769d9d3e8714543af"),
    "b172cca70c9d": ("frontier/B650_typed_functor/TYPES.md", "6e79e480cfa9973a84edb7e735e2f86da1f0726f33a6253dde6d5a5287598bcf"),
    "b1ee7bcab53b": ("frontier/B1823_step_a_the_tied_heavy_vacuum/verification/step_a_v2.py", "65d895c908d1c6f129ba00d647a504f1d5d51bab777f1f26f135d105f332b6f8"),
    "c40fd50bc5f9": ("frontier/B1495_the_orbit_in_one_module/verification/cross.py", "9e0070ab7ffed5369541ac8ecd1b527e78d2873b4dbd40138c789e66e81ead57"),
    "c4c204301962": ("frontier/B1490_the_common_cover_verified/verification/level_recount.py", "df3af299df4d2c941f8ccd09e2d0386f119792b30fbcf0ae9ed1e7058029b79a"),
    "c74fc59dcb91": ("frontier/B666_leads_campaign/ADDENDUM_1.md", "82d5cd62c8049b65b0a502e6bd51c4ba7f9bbd25f2336c3877aad8c5e16af6e6"),
    "d8ef558d9c73": ("frontier/B679_engine_patch/ARTIFACT_HASHES.txt", "a5ff359c4dc532b9eab458ce8beebe92e2c0a1875d4d3e2a6ee02518d0f93b71"),
    "e129fe00f880": ("frontier/B1601_the_common_point_is_the_geometry_mod_3/verification/meets.py", "086dd6db336e0a28484c1e3f25c919cbd39e856a74ea9e10fc6024a1bc557b0d"),
    "e2df6ca12f6c": ("frontier/B1792_the_offset_recurrence_at_order_60/verification/compare.py", "40435d82631a5e5ef0d561412ff00ea51f7d1fe9dd6fc5180ae46907d45de671"),
    "e3b1af50cac7": ("frontier/B1609_the_even_subweave/verification/even_subweave.py", "c4f5f1497d93f1f11ad40ff4ecbe225e0dd80872bdd2bdc0600ff1808b811e69"),
    "e7a0e6996e21": ("frontier/B1823_step_a_the_tied_heavy_vacuum/verification/model.py", "0c545f5019398bf958cf0c6af69209428595a7f12f7071c8f718d1d5f9938800"),
    "ed75482fbcf7": ("frontier/B1654_the_norm_of_the_boundary_class/verification/before_the_seal/review/s23_names.py", "4f710db8f92a6ce2fd4fe6bd09d75b8668e5cc14ecf0ee0a27c6c329cd076d45"),
    "ed90ccc5013d": ("frontier/B1499_the_fusion_on_the_first_room/verification/fusion.py", "bb54c8fb79e241b144621ca50dc84b08fa85f72ae8c24682d9c11da071cf99ba"),
    "ef83de39507e": ("frontier/B749_genesis_forks/MEASUREMENTS.md", "dbf7e40c86b7a0ae1aae7b3c1f7ca148b048a1ae0b591f99196c999940d81e5d"),
    "f86e2456f4e8": ("philosophy/P019_the_genesis_axiom_chain.md", "c6b7139d42336ab2f6fb5cd594f510a94f949050ad39fd394667561e8b5c5e80"),
}
OTHER_SEAL_HASH_RE = re.compile(
    r"^(?:.*\.(?:sha256|sums)|.*(?:^|_)(?:seals?|hashes|sha256|checksums?|digests?)(?:_.*)?\.txt)$",
    re.I,
)
OTHER_INTAKE_BASENAMES = frozenset((
    "ORIGINALS_MANIFEST.txt", "SHA256_RECEIVED.txt", "SHA256_AS_RECEIVED.txt", "LARGE_OUTPUTS_SHA256.txt",
))
OTHER_HASH_LISTS_BROKEN = frozenset((
    "034b645b167b", "056e1c70e7f9", "070d2632bf1d", "0c62d8571125", "0d185c97629c", "10bb59962f58", "13e6d424a387", "177498568fee",
    "1e522d795e69", "22b73c743760", "23e9bcca2247", "2463dd96ed77", "253215f76bc8", "284456da9b5b", "288114054863", "2a007ac846e2",
    "2d41b36408d2", "2e6f19cb2fcb", "2fe1e5a1d6f4", "3097086db609", "34cf93c58b63", "35f4cf3a9da0", "36d75e8bcb8f", "3996cab5b063",
    "39afcfd30ff2", "3b6ffca9f9a0", "3e6f312595ed", "42f7648b488c", "484a95a8d1ee", "4cc28b746f41", "4e348f7d3216", "502319aba0f6",
    "552160404074", "5696c788e9ad", "56fe09f86f75", "57a57af51f3a", "5d0d129d5632", "5d18a184f2ee", "5ea9035fb7be", "5f6a736b7c7d",
    "62d180797718", "656b45633db5", "659cf444beb9", "65f2dd5ad979", "6643d0d1a531", "682cef6bbfb9", "6ac7315c89fb", "6dc918679ad1",
    "6e0f13750339", "6f6639634851", "6fcaffccef9f", "70347a7e8c3c", "72e4532ba060", "730312cac671", "73c1df3927da", "74881b1c68e8",
    "7bc5ea55c9c2", "7cc5100de543", "7cde81e60aa3", "7d672e5e055a", "7db90fde34a8", "7e1d7e071eff", "7eb6ae187bb4", "8764d3d394b7",
    "8a6caacf7690", "8b586e29b9fc", "8bdcd114fc4d", "8c2a09199243", "908bccd2d9e4", "9446846795c2", "948082a84acc", "9690155da776",
    "96fff6845320", "9760de67e242", "9b34c606b485", "a19e3b0164e8", "a3861486550d", "a3ca2bc40ef6", "a44e8ef17a26", "a4d6a67d98b8",
    "a54cf0d53113", "a6a75f05b346", "a6a867cf635c", "a7bf12d84ef8", "a9f00fc3dd46", "ab6af942650a", "ac4bfaf892b9", "aecdb9ecc937",
    "af5cbfc60022", "b1a51b0bf161", "b239c8ed8b4b", "b5ae17539493", "b634bc022a0c", "b6b98effb0e0", "b6df0830639b", "bb87c5972102",
    "bcb956035a44", "be5b5f07dc9a", "bf0c79dcc514", "c154f851a6a0", "c1be3b7f0c37", "c2c49b575f0a", "c4a1d81e5613", "c7438f5be145",
    "c83f7c914a59", "c923d4aa9ce9", "ca97477e16dd", "cc487f723dfa", "ce58dda1bd08", "d02a3b05e71c", "d054308377f2", "d092d0bd691f",
    "d0c8ea1d29f7", "d14cf9151b8a", "d2dd79e87149", "d4fac13d09dc", "d6ed193fe8c4", "dd2a82515184", "dee9fd6ebfa6", "df3e9b1ea2e9",
    "e01ea768fcc2", "e114ab540add", "e30fd972d6cc", "e38c13088b1b", "e41609ac0e3b", "e46457355d1a", "e7a235cb36d3", "e89eeafa094b",
    "ebe489a824aa", "ef8b7de13129", "f0daae98f760", "f37dfc671b62", "f62fd66ab12c", "f635da8a83c9", "f82a6f4dcff6", "f8364b5f6c79",
    "f94f24198452", "fbb40de74e49", "fdd9de1bf5ca", "ff986108188b",
))
OTHER_HASH_LISTS_BROKEN_DISK = {
    "056e1c70e7f9": ("frontier/B677_morning_packet/anatomy/loop5/e2_silversplit/FINDINGS_CC2.md", "490d81b41fb56fee7ba3de51f96a6fe0a255a3687c078feedce7038075c08f0f"),
    "070d2632bf1d": ("frontier/B677_morning_packet/anatomy/GENERATION_LEG_PLAN_CC2.md", "33c819046d2b35699f5a5f62d94a3a7dc5f4bb1abb4e3ae4b106da120ff69873"),
    "0c62d8571125": ("frontier/B657_invariant_line/packet/w0a_singlet/FINDINGS_CC2.md", "c9102ad4964fb7d182a86f7c42d3d726318d6c45d061faee4638f6be4619f15c"),
    "253215f76bc8": ("frontier/B670_anatomy_full/packet/loop4/PREREG_L4.md", "e9291b314a6bb266b41bdc6e71eb9e8055d5ab8280f36308e2c386e4605ff675"),
    "288114054863": ("frontier/B663_bifocal_anatomy/anatomy_packet/loop1/a1_jordan/FINDINGS_CC2.md", "4109ab4f09d89a1db43967aecd5e4de8a1b767dcd56846a92988618455e9d3f0"),
    "2a007ac846e2": ("frontier/B1305_the_cloud_156_178/DESIGN.md", "84bca2f72d0e7fce2d1ce860e3e5f0144a5f2c7865ce9ac765d21d4dabf71852"),
    "2e6f19cb2fcb": ("frontier/B673_loop4_integration/packet/loop4/PREREG_L4.md", "e9291b314a6bb266b41bdc6e71eb9e8055d5ab8280f36308e2c386e4605ff675"),
    "34cf93c58b63": ("frontier/B663_bifocal_anatomy/anatomy_packet/CHARTER.md", "e3261501aa04162616dfbf2484a7ac5de1f4a26548f37316e1d0f7180cd2e90f"),
    "3996cab5b063": ("frontier/B651_wave3_integration/cc2_packets/promotion_queue/promotion_queue/p4_sectors/FINDINGS_CC2.md", "54eb11aa5fdabffddbbf3e943b27c9992019fda8c572bbc4c8f3483a37327aa4"),
    "42f7648b488c": ("frontier/B673_loop4_integration/packet/FRONTIER.md", "44740a4595418e052b93a172e39ff467d08ef398f7e4d20323d5672ac5aef844"),
    "484a95a8d1ee": ("frontier/B670_anatomy_full/packet/loop2/b2_massey/FINDINGS_CC2.md", "11b57ba1c28a0e299d6490f613f165678be26698f0024582817b3be599cffa1f"),
    "4e348f7d3216": ("frontier/B651_wave3_integration/cc2_packets/finisher_queue/finisher_queue/f3_twisted/f3_twisted.py", "c2e8d5216cb053f05b46dd686494564624f77a91997bee27b341d1a19dc0346c"),
    "552160404074": ("frontier/B663_bifocal_anatomy/anatomy_packet/loop1/a3_stage/FINDINGS_CC2.md", "462be1623c3354cba540b58d3836d249d22d3acac6f24ab9d2001690ada95dfd"),
    "5696c788e9ad": ("frontier/B666_leads_campaign/cell9/cell9_taskB_discrete_id.py", "902b4f6dff2e8dd88d2c4e1b5a17776be3c79a952cdf0499599255dc950f8eaf"),
    "56fe09f86f75": ("frontier/B670_anatomy_full/packet/loop1/a1_jordan/FINDINGS_CC2.md", "4109ab4f09d89a1db43967aecd5e4de8a1b767dcd56846a92988618455e9d3f0"),
    "5d0d129d5632": ("frontier/B673_loop4_integration/packet/loop4/d1_pairing/FINDINGS_CC2.md", "75f2a2da893a1390688f7dd4339a1b730171fc4df270ac3198e50e04aa0dddd3"),
    "5d18a184f2ee": ("frontier/B879_selection_cochain/packet/HANDOFF_CC_SELECTION_COCHAIN.md", "0c9fdd209fd703ff70fca83865b0c5ab3617e0c5dd4945b06c2ca43de59d3d89"),
    "5ea9035fb7be": ("frontier/B663_bifocal_anatomy/anatomy_packet/FRONTIER.md", "c9bcb93ef08686eec84baf2f56eafb5bb99eae41b07aad5dde16444fe5cfd52b"),
    "656b45633db5": ("frontier/B879_selection_cochain/packet/PREREG_SCC.md", "1f07ffc86bb15c43d7e597943ecb1f31666f483b8dd72ba51bcaad4098664397"),
    "659cf444beb9": ("frontier/B660_structure_campaign/packet/s1_gamma5/LIT_GATE_S1.md", "6c5085b249ffd51d4b2632d5f9590f379178d78f1fbfa508e68d4c5e138bca16"),
    "65f2dd5ad979": ("frontier/B670_anatomy_full/packet/loop3/c1_vecmassey/FINDINGS_CC2.md", "1f46cb123c5d68a9a319e5f7b65a12b82c0d804f5a121c05e8dc5ca1f7b1d34d"),
    "6e0f13750339": ("frontier/B660_structure_campaign/packet/s1_gamma5/FINDINGS_S1A.md", "6f8061fcb58674c55e707e843f1c429eae0e7eb28878594736d681fd5df1cc11"),
    "72e4532ba060": ("frontier/B651_wave3_integration/cc2_packets/loops_queue/loops_queue/d5_triality/d5_triality.py", "4041e0ec443e6a73e1082ad3367337eb726ee646fc7ade4c776104fa26b17708"),
    "730312cac671": ("frontier/B677_morning_packet/anatomy/loop5/e1_diag351/FINDINGS_CC2.md", "28a27eb4a972d97d241467f84a490363399b2c45992d523e42652463bcf716d6"),
    "7bc5ea55c9c2": ("frontier/B879_selection_cochain/packet/PREREG_SCC.md", "1f07ffc86bb15c43d7e597943ecb1f31666f483b8dd72ba51bcaad4098664397"),
    "7cc5100de543": ("frontier/B656_digest_integration/packet/g3_mirror/FINDINGS_CC2.md", "4b09c6157c43ecd52523dd31e8af758bf80c06eff8dd0ea36de7d27a4832c861"),
    "7e1d7e071eff": ("frontier/B673_loop4_integration/packet/loop4/d1_pairing/FINDINGS_CC2.md", "75f2a2da893a1390688f7dd4339a1b730171fc4df270ac3198e50e04aa0dddd3"),
    "7eb6ae187bb4": ("frontier/B673_loop4_integration/packet/loop4/PREREG_L4.md", "e9291b314a6bb266b41bdc6e71eb9e8055d5ab8280f36308e2c386e4605ff675"),
    "948082a84acc": ("frontier/B670_anatomy_full/packet/loop4/PREREG_L4.md", "e9291b314a6bb266b41bdc6e71eb9e8055d5ab8280f36308e2c386e4605ff675"),
    "9760de67e242": ("frontier/B666_leads_campaign/cell9/cell9_taskA_verify2.py", "a37003e7f1b6dc07dedd6d705b8bb0c33842bf1e76150e663509b4eaab22e224"),
    "a3ca2bc40ef6": ("frontier/B670_anatomy_full/packet/loop2/b3_silver/FINDINGS_CC2.md", "a5f3c35caba8c9645234f9f42c20e32e22a919767d485d00d2ccbb650efc180a"),
    "a4d6a67d98b8": ("frontier/B666_leads_campaign/cell9/cell9_taskB_branches.py", "5670965585eb1f5b9e844a61162070fc3de00751a25226ced9b0fd1ee194ea8c"),
    "a54cf0d53113": ("frontier/B651_wave3_integration/cc2_packets/loops_queue/loops_queue/d4_su3/FINDINGS_CC2.md", "37b9a410166dd4c92c8dd68003030dc58ddcccb29054cf844bb488daf5b3f7e1"),
    "a6a867cf635c": ("frontier/B673_loop4_integration/packet/loop4/d3_silvercup/FINDINGS_CC2.md", "2f3b4f65e926e1f97ddd8ea7c9c21073e7dab95beb9fb51a050a8f5e119cdc3c"),
    "ac4bfaf892b9": ("frontier/B879_selection_cochain/packet/HANDOFF_CC_SELECTION_COCHAIN.md", "0c9fdd209fd703ff70fca83865b0c5ab3617e0c5dd4945b06c2ca43de59d3d89"),
    "aecdb9ecc937": ("frontier/B677_morning_packet/anatomy/loop5/e1_diag351/FINDINGS_CC2.md", "28a27eb4a972d97d241467f84a490363399b2c45992d523e42652463bcf716d6"),
    "b1a51b0bf161": ("frontier/B670_anatomy_full/packet/loop3/c2_f4split/FINDINGS_CC2.md", "aa4c7999f0d2cba7be8f8c33e621d7452015adf629c33cde698d58c5dfe13752"),
    "b5ae17539493": ("frontier/B670_anatomy_full/packet/loop2/b4_landscape/FINDINGS_CC2.md", "7dcde9b9d38dc4296ce4d5d28211006a5295f9601c4fdc24a9747fe8ddfd2472"),
    "b634bc022a0c": ("frontier/B670_anatomy_full/packet/CHARTER.md", "e3261501aa04162616dfbf2484a7ac5de1f4a26548f37316e1d0f7180cd2e90f"),
    "b6df0830639b": ("frontier/B657_invariant_line/packet/w1_portal/FINDINGS_CC2.md", "0f4b11eafb59860e10825f697b33efe0d2509f0ae06159b1f41e63d673b49de1"),
    "bb87c5972102": ("frontier/B657_invariant_line/packet/w2_silver/FINDINGS_CC2.md", "298a0a70433c70a912ddced1d3b832664f362e063e36903cafa8c81f86847b5a"),
    "bcb956035a44": ("frontier/B660_structure_campaign/packet/s1_gamma5/FINDINGS_CC2.md", "15623a9d4681e8a4013199d632361dc5657c8d16779f7590a83848c3a7dd286d"),
    "c2c49b575f0a": ("frontier/B743_rung1_widened/PREREG_RUNG1_WIDENED.md", "191394438bd9eaad2779ef1dd3959d5e8083945678439c0d37071a141dfa70b4"),
    "c7438f5be145": ("frontier/B670_anatomy_full/packet/loop2/b1_f4/FINDINGS_CC2.md", "2fff23dfef6356fc74e25adac927eb75b4bf484b8c8848cb562bec83716ac8ef"),
    "c83f7c914a59": ("frontier/B651_wave3_integration/cc2_packets/promotion_queue/promotion_queue/p1_milgram/p1_milgram.py", "7d95723614e73e6287fab289077767bd96fbeb21e3de078a77ebe4049aa6d357"),
    "ca97477e16dd": ("frontier/B670_anatomy_full/packet/loop1/a3_stage/FINDINGS_CC2.md", "462be1623c3354cba540b58d3836d249d22d3acac6f24ab9d2001690ada95dfd"),
    "d02a3b05e71c": ("frontier/B756_remaining_doors/RAW_WORKFLOW_OUTPUT.json", "331e1148ade1cc19cad26a2d0cd6ef95df95193d7fdfbc537d54e4db1783e99c"),
    "d092d0bd691f": ("frontier/B651_wave3_integration/cc2_packets/promotion_queue/promotion_queue/p0_s_verify/FINDINGS_CC2.md", "52162142068c12b2ff0d6b0c1aec4c6cb40635ebb9a76507a4e0b376fb191f4d"),
    "d0c8ea1d29f7": ("frontier/B670_anatomy_full/packet/loop3/c3_signtable/FINDINGS_CC2.md", "e8859a666c090f1ec45b7c0b1eb6b59919c302ac566a6c8e369fa6c3adaf841c"),
    "d14cf9151b8a": ("frontier/B666_leads_campaign/cell9/cell9_taskA_exact_tau.py", "92c4831f81a6db4d6d92a4d63720da25c75e3570c8903c0e92a6e94f80d10591"),
    "d2dd79e87149": ("frontier/B670_anatomy_full/packet/loop2/PREREG_L2.md", "c6d4fabdd8eabc6a777d9fc462a404c50511c1cea9abc429d77b2f54a9768926"),
    "dd2a82515184": ("frontier/B670_anatomy_full/packet/FRONTIER.md", "30e13a9fc80ace57b64c0cf65514e7c2ece9706e21e6bc0ce7cb36c3cf01e2ba"),
    "df3e9b1ea2e9": ("frontier/B666_leads_campaign/cell9/cell9_L_arith.py", "f6d8162246879ec8e1d94301ed9c473a07c5b5e549393f5887fa30db6becffed"),
    "e30fd972d6cc": ("frontier/B670_anatomy_full/packet/loop1/a2_phases/FINDINGS_CC2.md", "b6ecfaafaaece2e7f5e7577bf1a3d6862888178463dfd1b656c93777da7dec08"),
    "e38c13088b1b": ("frontier/B670_anatomy_full/packet/loop4/d1_pairing/FINDINGS_CC2.md", "0812e63df128e98ea6ce488479885e2d915630f2f6409eedf576804e5ee28dfe"),
    "e7a235cb36d3": ("frontier/B1298_the_lift_fork/DESIGN.md", "f1fef837668ea16d42c5c5c54ea44361da5de891caceef39f2fc2d4a9253bf11"),
    "e89eeafa094b": ("frontier/B879_selection_cochain/packet/CAMPAIGN_CLOSE.md", "aee51342833178b6082051e28c27b8d127137604b0af3b8e795c4ea963037029"),
    "ebe489a824aa": ("frontier/B660_structure_campaign/packet/s4_massshape/FINDINGS_CC2.md", "61dff42f9c593a79ae5792549f3a5b9403804c31f849781fac596804ca3e69e5"),
    "ef8b7de13129": ("frontier/B670_anatomy_full/packet/loop3/c3_signtable/FINDINGS_CC2.md", "e8859a666c090f1ec45b7c0b1eb6b59919c302ac566a6c8e369fa6c3adaf841c"),
    "f0daae98f760": ("frontier/B663_bifocal_anatomy/anatomy_packet/loop1/a2_phases/FINDINGS_CC2.md", "b6ecfaafaaece2e7f5e7577bf1a3d6862888178463dfd1b656c93777da7dec08"),
    "f62fd66ab12c": ("frontier/B673_loop4_integration/packet/loop4/d2_351/FINDINGS_CC2.md", "55bf6fc0a60f6976fa4d8a3c6be2654bfe4f63fce93f9cd14440ba2ffb4f2f46"),
    "f82a6f4dcff6": ("frontier/B734_m004_is_congruence/cc3_verification/b734_independent_verify.py", "c0fb89c71e3bd39c124ea11963a72e557164f436878e8c1fea6783b44b2865c2"),
    "f8364b5f6c79": ("frontier/B660_structure_campaign/packet/s2_cp/FINDINGS_CC2.md", "c346c4ae97e428e15ddd02a017c9107e0294d8feb08f8fba2f0a16e46d886397"),
    "f94f24198452": ("frontier/B651_wave3_integration/cc2_packets/finisher_queue/finisher_queue/f4_receipt/FINDINGS_CC2.md", "fec429eeb009c7313a216710a067600c4bb583e4383c8ab268e0d1bb8fe9e6c3"),
    "fdd9de1bf5ca": ("frontier/B666_leads_campaign/cell9/cell9_taskB_branches_v2.py", "c15942ae50c45bb6a413bed6bf23cf9ea2d924f8df7fb139f7098ef8510f0181"),
}
OTHER_HASH_LISTS_IMMUTABLE_FROM = "015be0cc7cfb57a69430a9710fb01c754b53583e"  # B1879 (Re-Audit 3, t7)


def _resolve_hash_entry(repo, tracked, lst, h, name):
    """B1879 (Re-Audit 3, t3): canonical resolution without decoy shadowing. Paths starting with a repository top-level
    directory resolve only from ROOT (and return AMBIGUOUS if a local decoy exists beside the list or under verification/).
    Bare/relative names resolve beside the list or in verification/ (and return AMBIGUOUS if tracked in both)."""
    d = os.path.dirname(lst)
    if name is None:
        return None, "NO NAME"
    if name.startswith(HASH_LIST_ROOT_PREFIXES):
        real = os.path.normpath(name).replace(os.sep, "/")
        decoys = [os.path.normpath(os.path.join(d, p)).replace(os.sep, "/")
                  for p in (name, os.path.join("verification", name))]
        if any(c != real and c in tracked for c in dict.fromkeys(decoys)):
            return real, "AMBIGUOUS"
        cands = [real]
        hits = [real] if real in tracked else []
    else:
        cands = list(dict.fromkeys([
            os.path.normpath(os.path.join(d, name)).replace(os.sep, "/"),
            os.path.normpath(os.path.join(d, "verification", name)).replace(os.sep, "/"),
        ]))
        hits = [c for c in cands if c in tracked]
        if len(hits) > 1:
            return hits[0], "AMBIGUOUS"
    if not hits:
        on_disk = any(os.path.exists(os.path.join(repo, c)) for c in cands)
        return name, ("NOT TRACKED" if on_disk else "ABSENT")
    hit = hits[0]
    try:
        now = hashlib.sha256(open(os.path.join(repo, hit), "rb").read()).hexdigest()
    except OSError:
        return name, "ABSENT"
    return hit, ("VERIFIES" if now == h else "MISMATCH")


def _scan_hash_lists(repo, tracked, lists):
    out = []
    for lst in lists:
        try:
            lines = open(os.path.join(repo, lst), encoding="utf-8", errors="replace").read().split("\n")
        except OSError:
            continue
        for line in lines:
            e = _hash_list_entry(line.strip())
            if e is None:
                continue
            h, name = e
            key = hashlib.sha256(f"{lst}|{name}|{h}".encode("utf-8")).hexdigest()[:12]
            hit, st = _resolve_hash_entry(repo, tracked, lst, h, name)
            out.append((key, lst, hit, st))
    return out


def artifact_hash_state(repo=None):
    """Every entry of every tracked ARTIFACT_HASHES*.txt list under `repo`: a list of (key, list path, name, state),
    or None where the tracked files cannot be listed. state is VERIFIES, MISMATCH, NOT TRACKED, ABSENT, NO NAME or AMBIGUOUS."""
    repo = str(repo or ROOT)
    r = subprocess.run(["git", "-C", repo, "ls-files"], capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        return None
    tracked = set(r.stdout.split("\n"))
    lists = sorted(f for f in tracked if fnmatch.fnmatch(os.path.basename(f), ARTIFACT_HASH_GLOB))
    return _scan_hash_lists(repo, tracked, lists)


def _is_other_seal_hash_list(f):
    base = os.path.basename(f)
    return (
        f.startswith(("frontier/", "outside_bench/"))
        and not fnmatch.fnmatch(base, ARTIFACT_HASH_GLOB)
        and base not in OTHER_INTAKE_BASENAMES
        and bool(OTHER_SEAL_HASH_RE.match(base))
    )


def other_hash_list_state(repo=None):
    """B1879 (Re-Audit 3, t7): every entry of every tracked secondary seal hash list (*SEAL*.txt, *SHA256*.txt, *.sha256,
    *HASHES*.txt, *.sums, etc., outside intake manifests)."""
    repo = str(repo or ROOT)
    r = subprocess.run(["git", "-C", repo, "ls-files"], capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        return None
    tracked = set(r.stdout.split("\n"))
    lists = sorted(f for f in tracked if _is_other_seal_hash_list(f))
    return _scan_hash_lists(repo, tracked, lists)


def other_hash_lists_immutable_problems(repo, root, waived=(), limit=5):
    """B1879 (Re-Audit 3, t7): committed edits, deletions or moves of secondary seal hash lists after `root`."""
    def git(*a):
        return subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True, timeout=120)
    if git("rev-parse", "--git-dir").returncode != 0:
        return ["cannot verify: not a git repository"], 0
    if git("cat-file", "-e", root + "^{commit}").returncode != 0:
        return [f"cannot verify: secondary hash-list rule commit {root[:9]} is not in this clone (shallow or partial)"], 0
    if git("merge-base", "--is-ancestor", root, "HEAD").returncode != 0:
        return [f"cannot verify: HEAD does not descend from secondary hash-list rule commit {root[:9]}"], 0
    commits = git("log", "--first-parent", "--reverse", "--format=%H", f"{root}..HEAD", "--", "frontier/", "outside_bench/").stdout.split()
    verbs = {"M": "edits", "D": "deletes", "R": "moves", "T": "changes the type of", "C": "copies over"}
    problems = []
    touched = 0
    for c in commits:
        out = git("diff-tree", "--no-commit-id", "--name-status", "-r", "-M", f"{c}^", c, "--", "frontier/", "outside_bench/").stdout
        c_hit = False
        for line in out.splitlines():
            parts = line.split("\t")
            if len(parts) < 2 or not _is_other_seal_hash_list(parts[1]):
                continue
            c_hit = True
            if parts[0].startswith("A") or (c, parts[1]) in waived:
                continue
            problems.append(f"{c[:9]} {verbs.get(parts[0][0], 'changes')} the secondary list of hashed files {parts[1]}")
        if c_hit:
            touched += 1
    return problems[:limit], touched


def hash_lists_immutable_problems(repo, root, waived=(), limit=5):
    """The committed changes to a list of hashed files on `repo`'s first-parent line after `root`: (problems, commits read).
    A pure function of the commit graph, as seal_immutable_problems is; it fails closed where history cannot be read."""
    def git(*a):
        return subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True, timeout=120)
    if git("rev-parse", "--git-dir").returncode != 0:
        return ["cannot verify: not a git repository"], 0
    if git("cat-file", "-e", root + "^{commit}").returncode != 0:
        return [f"cannot verify: the rule's first commit {root[:9]} is not in this clone (shallow or partial)"], 0
    if git("merge-base", "--is-ancestor", root, "HEAD").returncode != 0:
        return [f"cannot verify: HEAD does not descend from the rule's first commit {root[:9]}"], 0
    spec = ":(glob)**/" + ARTIFACT_HASH_GLOB
    commits = git("log", "--first-parent", "--reverse", "--format=%H", f"{root}..HEAD", "--", spec).stdout.split()
    verbs = {"M": "edits", "D": "deletes", "R": "moves", "T": "changes the type of", "C": "copies over"}
    problems = []
    for c in commits:
        out = git("diff-tree", "--no-commit-id", "--name-status", "-r", "-M", f"{c}^", c, "--", spec).stdout
        for line in out.splitlines():
            parts = line.split("\t")
            if len(parts) < 2 or parts[0].startswith("A"):
                continue                               # a new list is a seal
            if (c, parts[1]) in waived:
                continue
            problems.append(f"{c[:9]} {verbs.get(parts[0][0], 'changes')} the list of hashed files {parts[1]}")
    return problems[:limit], len(commits)


def _check_frozen_disk_locks(repo, rows, disk_map, amended):
    re_edited = []
    for k, lst, name, st in rows:
        if k in amended or k not in disk_map:
            continue
        exp_path, exp_sha = disk_map[k]
        if st != "MISMATCH" or name != exp_path:
            re_edited.append((name or exp_path, f"MODIFIED AFTER FREEZE ({st})", lst))
            continue
        try:
            cur_sha = hashlib.sha256(open(os.path.join(repo, exp_path), "rb").read()).hexdigest()
        except OSError:
            re_edited.append((exp_path, "MODIFIED AFTER FREEZE (ABSENT)", lst))
            continue
        if cur_sha != exp_sha:
            re_edited.append((exp_path, "MODIFIED AFTER FREEZE (MISMATCH)", lst))
    return re_edited


def gate_artifact_hashes(_repo=None, _frozen=None, _root=None, _waived=None, _amended=None):
    """What a seal hashed still has the hash the seal recorded, and the record of the hashes does not change (see the note above)."""
    repo = _repo or ROOT
    frozen = ARTIFACT_HASHES_BROKEN if _frozen is None else _frozen
    amended = ARTIFACT_HASHES_AMENDED if _amended is None else _amended
    waived = ARTIFACT_HASHES_WAIVED if _waived is None else _waived
    state = artifact_hash_state(repo)
    if state is None:
        return False, "cannot verify: the tracked files cannot be listed (not a git repository)"
    broken = [(k, lst, name, st) for (k, lst, name, st) in state if st != "VERIFIES"]
    new = [(k, lst, name, st) for (k, lst, name, st) in broken if k not in frozen and k not in amended]
    if new:
        return False, "; ".join(f"{name or '(no name)'}: {st} against {lst}" for (k, lst, name, st) in new[:5]) + (
            f" (+{len(new) - 5} more)" if len(new) > 5 else "") + " -- a file a seal hashed has changed, or a list names what is not there"
    # B1879 (Re-Audit 3, t4): a pre-existing MISMATCH script frozen by key cannot be edited a second time either.
    re_edited = _check_frozen_disk_locks(repo, broken, ARTIFACT_HASHES_BROKEN_DISK, amended)
    if re_edited:
        return False, "; ".join(f"{nm}: {st} against {lst}" for nm, st, lst in re_edited[:5]) + " -- a frozen broken script changed again after its freeze"
    problems, n = hash_lists_immutable_problems(repo, _root or ARTIFACT_HASHES_IMMUTABLE_FROM, waived)
    if problems:
        return False, "; ".join(problems)
    # B1879 (Re-Audit 3, t7): enforce secondary seal hash lists (*SEAL*.txt, *SHA256*.txt, *.sha256, *HASHES*.txt, *.sums, etc.).
    ostate = other_hash_list_state(repo) or []
    obroken = [(k, lst, name, st) for (k, lst, name, st) in ostate if st != "VERIFIES"]
    ofrozen = OTHER_HASH_LISTS_BROKEN if _frozen is None else (_frozen & OTHER_HASH_LISTS_BROKEN)
    onew = [(k, lst, name, st) for (k, lst, name, st) in obroken if k not in ofrozen and k not in amended]
    if onew:
        return False, "; ".join(f"{name or '(no name)'}: {st} against {lst}" for (k, lst, name, st) in onew[:5]) + " -- a file in a secondary seal hash list changed or is missing"
    ore_edited = _check_frozen_disk_locks(repo, obroken, OTHER_HASH_LISTS_BROKEN_DISK, amended)
    if ore_edited:
        return False, "; ".join(f"{nm}: {st} against {lst}" for nm, st, lst in ore_edited[:5]) + " -- a frozen file in a secondary seal hash list changed again"
    oproblems, on_touch = other_hash_lists_immutable_problems(repo, _root or OTHER_HASH_LISTS_IMMUTABLE_FROM, waived)
    if oproblems:
        return False, "; ".join(oproblems)
    lists = len({lst for (_, lst, _, _) in state})
    distinct = len({k for (k, _, _, _) in broken})
    osec = (f"; secondary seal lists: {len(ostate)} entries ({len(ostate) - len(obroken)} verify, {len(obroken)} frozen, {on_touch} commit(s) since {(_root or OTHER_HASH_LISTS_IMMUTABLE_FROM)[:9]})"
            if ostate or on_touch else "")
    return True, (f"ok ({len(state)} entries in {lists} lists: {len(state) - len(broken)} verify, {len(broken)} do not ({distinct} distinct, each frozen by key "
                  f"as found on 2026-11-10 or amended by name; the ceiling is {len(frozen)}); {n} commit(s) since {(_root or ARTIFACT_HASHES_IMMUTABLE_FROM)[:9]} touch a list, each only adding one"
                  f"{osec}; amended by name: {len(amended)}" + ("".join(f" [{k}: {why}]" for k, why in sorted(amended.items()))) + f"; waived: {len(waived)}"
                  + ("".join(f" [{c[:9]} {p}: {why}]" for (c, p), why in sorted(waived.items()))) + ")")


# THE CLOSURE MAP AND THE CLOSURE PROGRAMME ARE GENERATED FILES (Review 77's R77-7, P-754; made a gate at Review 78).  Each quotes
# the register, the scoreboard, the foundation and the record's pages, so each goes stale whenever one of those moves.  Their
# locks fail when a committed file is not its builder's output -- but the push gate does not run the suite, and for twenty
# landings both were rebuilt by hand, from memory.  This gate runs both builders on every push and compares.
CLOSURE_GENERATED = (
    ("frontier/B1858_the_closure_map", "build_map.py", "the closure map"),
    ("frontier/B1861_the_closure_programme", "build_programme.py", "the closure programme"),
)


def closure_generated_problems(root=None, _read=None):
    """(problems, skipped) for the two generated pages: a builder that refuses, or a committed file that is not its builder's
    output.  The programme quotes two seats at pinned revisions; in a clone that does not hold them its page differs by a
    line saying so, and it is reported as skipped, visibly, not as passed."""
    import importlib.util
    import pathlib as _pl
    root = _pl.Path(root or ROOT)
    read = _read or (lambda f: f.read_text(encoding="utf-8"))
    problems, skipped = [], []
    for arc, script, what in CLOSURE_GENERATED:
        f = root / arc / "verification" / script
        if not f.is_file():
            problems.append(f"{what}'s builder is not there: {arc}/verification/{script}")
            continue
        spec = importlib.util.spec_from_file_location("_gate_" + script[:-3], f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if script == "build_map.py":
            nodes, edges, stats, fails, notes, rows = mod.build()
            files = None if fails else mod.generated(nodes, edges, stats, rows)
            missing = []
        else:
            B = mod.build()
            fails, missing = B["fails"], B["stats"]["not_checked_in_this_clone"]
            files = None if fails else mod.generated(B)
        if fails:
            problems.append(f"{what}'s builder refuses: {fails[0]}" + (f" (+{len(fails) - 1} more)" if len(fails) > 1 else ""))
        elif missing:
            skipped.append(f"{what} (this clone does not hold: {', '.join(missing)})")
        else:
            for name, text in files.items():
                g = root / arc / name
                if not g.is_file() or read(g) != text:
                    problems.append(f"{arc}/{name} is not its builder's output (run verification/{script} --write)")
    return problems, skipped


def gate_closure_generated(_read=None):
    """The closure map and the closure programme, as committed, are what their builders generate (see the note above)."""
    problems, skipped = closure_generated_problems(_read=_read)
    if problems:
        return False, "; ".join(problems[:4]) + (f" (+{len(problems) - 4} more)" if len(problems) > 4 else "")
    if skipped:
        return True, "skipped in part: " + "; ".join(skipped)
    return True, "ok"


# R76-2 (P-601; Review 74's R74-9): the sealed tests whose order git cannot show -- the rule (PREREGISTRATION.md) and the
# record (FINDINGS.md) first committed in one commit, the early practice -- frozen as a CEILING that may only shrink.
# docs/SEAL_ORDER_UNSHOWN.md lists them with each one's commit; the gate recomputes the class from git on every run.
# B1670 is in the class on main, but its order is shown on the kept referee branch: its seal ad3dd5d44 is a strict
# ancestor of its record fecdd63bd (Review 74, P-535). The class is the Lab panel's 'rule-before-record: same commit'.
SEAL_ORDER_UNSHOWN_CEILING = frozenset((
    "P3", "B425", "B435", "B480", "B496", "B497", "B498", "B507", "B508", "B531", "B533", "B535", "B539",
    "B540", "B548", "B549", "B575", "B584", "B585", "B586", "B587", "B588", "B592", "B593", "B594", "B595",
    "B596", "B632", "B640", "B641", "B642", "B643", "B644", "B649", "B654", "B655", "B658", "B709", "B742",
    "B746", "B747", "B748", "B749", "B750", "B751", "B752", "B753", "B754", "B755", "B757", "B758", "B759",
    "B760", "B761", "B762", "B764", "B765", "B766", "B767", "B768", "B769", "B771", "B780", "B781", "B782",
    "B790", "B821", "B822", "B824", "B825", "B830", "B839", "B849", "B850", "B936", "B1065", "B1066", "B1102",
    "B1104",
))
# Added once, 2026-11-10 (B1864; the advisor seat's audit, G4): the same class read under every seal name. These thirty were in
# it all along and outside the gate's sight. The ceiling still may only shrink from here.
SEAL_ORDER_UNSHOWN_CEILING = SEAL_ORDER_UNSHOWN_CEILING | frozenset((
    "B597", "B609", "B629", "B633", "B669", "B675", "B698", "B699", "B700", "B706", "B708", "B743", "B756", "B933", "B1137",
    "B1244", "B1297", "B1298", "B1299", "B1302", "B1303", "B1304", "B1305", "B1307", "B1320", "B1321", "B1322", "B1323",
    "B1324", "B1798",
))
# Added once, 2026-11-11 (B1879; Re-audit 2, s2/s3): the twenty-one historical arcs whose nested sealed packet/design or
# received rule file was first committed in the same commit as FINDINGS.md.
SEAL_ORDER_UNSHOWN_CEILING = SEAL_ORDER_UNSHOWN_CEILING | frozenset((
    "B646", "B651", "B656", "B657", "B660", "B663", "B670", "B673", "B677", "B775", "B879", "B1296",
    "B1674", "B1675", "B1676", "B1679", "B1684", "B1686", "B1817", "B1823", "B1827",
))
# B1879 (G4 / s4, P-772(b)): historical multi-wave / v2 addenda committed after their arc's initial Wave-1 FINDINGS.md.
# Any new sealed-style file committed AFTER its arc's FINDINGS.md fails seal-order-unshown.
SEAL_ORDER_AFTER_CEILING = frozenset((
    "frontier/B469_breath_campaign/PREREG_SIGMA_PARITY.md",
    "frontier/B647_core_mechanism/PREREG_CELL2.md",
    "frontier/B649_silver_holonomy/PREREG_STAGE2A.md",
    "frontier/B649_silver_holonomy/PREREG_STAGE2B.md",
    "frontier/B649_silver_holonomy/PREREG_STAGE3A.md",
    "frontier/B649_silver_holonomy/PREREG_STAGE3B_II.md",
    "frontier/B649_silver_holonomy/PREREG_STAGE3B_SWAP.md",
    "frontier/B650_typed_functor/PREREG_WAVE2.md",
    "frontier/B674_generation_leg/PREREG_W2.md",
    "frontier/B674_generation_leg/PREREG_W3_DECISION.md",
    "frontier/B674_generation_leg/PREREG_W3_DECISION_ADDENDUM_1.md",
    "frontier/B674_generation_leg/PREREG_W3_RUN.md",
    "frontier/B674_generation_leg/W2_DESIGN_NOTE_GAMMA5.md",
    "frontier/B700_fiber_functor/PREREG_CELL2.md",
    "frontier/B700_fiber_functor/PREREG_CELL4.md",
    "frontier/B700_fiber_functor/PREREG_CELL5.md",
    "frontier/B700_fiber_functor/PREREG_CELL6_phase2.md",
    "frontier/B700_fiber_functor/cell3_cc2/PREREG_CELL3_CC2.md",
    "frontier/B700_fiber_functor/phase2_cc2/phase2/PREREG_PHASE2_CC2.md",
    "frontier/B771_phase1_wave1/PREREG_WAVE2.md",
    "frontier/B771_phase1_wave1/PREREG_WAVE5.md",
    "frontier/B775_phase2_wave1/PREREG_WAVE2.md",
    "frontier/B775_phase2_wave1/PREREG_WAVE3.md",
    "frontier/B775_phase2_wave1/PREREG_WAVE4.md",
    "frontier/B775_phase2_wave1/PREREG_WAVE5.md",
    "frontier/B775_phase2_wave1/PREREG_WAVE6.md",
    "frontier/B775_phase2_wave1/cells/P2W2-LATIN/PREREGISTRATION.md",
    "frontier/B1071_sealed_listener/PREREGISTRATION_V2.md",
    "frontier/B1305_the_cloud_156_178/DESIGN_B.md",
    "frontier/B1306_the_older_debt/DESIGN_B.md",
    "frontier/B1306_the_older_debt/DESIGN_C.md",
))
SEAL_ORDER_SHOWN_OFF_MAIN = {"B1670": ("ad3dd5d44", "fecdd63bd")}
SEAL_ORDER_DOC = "docs/SEAL_ORDER_UNSHOWN.md"


def _seal_origins(rev="HEAD"):
    specs = [":(glob)frontier/**/" + pat for pat in SEAL_PATTERNS] + [":(glob)frontier/*/FINDINGS.md"]
    rc, raw = _git("log", "--full-history", "--no-merges", "--topo-order", "--reverse", "-M", "--name-status",
                   "--diff-filter=AR", "--format=%x1e%H", rev, "--", *specs)
    rc2, tree = _git("ls-tree", "-r", "--name-only", rev, "frontier/")
    if rc != 0 or rc2 != 0:
        return None, None
    origin = {}
    for chunk in raw.split("\x1e"):
        if not chunk.strip():
            continue
        head, _, body = chunk.partition("\n")
        sha = head.strip()
        for ln in body.splitlines():
            f = ln.split("\t")
            if f[0].startswith("R") and len(f) == 3:
                origin[f[2]] = origin.get(f[1], sha)
            elif f[0] == "A" and len(f) == 2:
                origin.setdefault(f[1], sha)
    return origin, tree


def seal_order_class(rev="HEAD"):
    """every sealed test on `rev` whose rule and record were first committed in one commit: arc id -> that commit.
    Widened 2026-11-11 (B1879) to read recursive SEAL_PATTERNS under frontier/B*/**."""
    origin, tree = _seal_origins(rev)
    if origin is None:
        return None
    out = {}
    for path in sorted(tree.splitlines()):
        parts = path.split("/")
        if len(parts) < 3 or parts[0] != "frontier":
            continue
        arc_dir, base = parts[1], parts[-1]
        if not any(fnmatch.fnmatch(base, pat) for pat in SEAL_PATTERNS):
            continue
        rule, record = origin.get(path), origin.get("frontier/%s/FINDINGS.md" % arc_dir)
        if rule and record and rule == record:
            aid = arc_dir.split("_")[0]
            if aid not in out or path == "frontier/%s/PREREGISTRATION.md" % arc_dir:
                out[aid] = rule
    return out


_ORIG_SEAL_ORDER_CLASS = seal_order_class


def seal_order_after_problems(rev="HEAD", ceiling=SEAL_ORDER_AFTER_CEILING, strict_ancestor=None):
    """B1879 (G4 / s4, P-772(b)): any sealed-style file committed AFTER its arc's FINDINGS.md (outside the frozen
    historical multi-wave ceiling) fails seal-order-unshown."""
    origin, tree = _seal_origins(rev)
    if origin is None:
        return ["git log failed -- post-record seals cannot be checked"]
    anc = strict_ancestor or _strict_ancestor
    problems = []
    for path in sorted(tree.splitlines()):
        if path in ceiling:
            continue
        parts = path.split("/")
        if len(parts) < 3 or parts[0] != "frontier":
            continue
        arc_dir, base = parts[1], parts[-1]
        if not any(fnmatch.fnmatch(base, pat) for pat in SEAL_PATTERNS):
            continue
        rule, record = origin.get(path), origin.get("frontier/%s/FINDINGS.md" % arc_dir)
        if rule and record and rule != record and anc(record, rule):
            aid = arc_dir.split("_")[0]
            problems.append(f"{aid}: sealed file {path} committed ({rule[:9]}) AFTER FINDINGS.md ({record[:9]})")
    return problems


def seal_order_listed(text):
    """the list's rows: arc id -> the short commit it names"""
    return {m.group(1): m.group(2) for m in re.finditer(r"^\| (B\d+|P\d+) \| [^|\n]* \| `([0-9a-f]{7,40})` \|", text, re.M)}


def _strict_ancestor(a, b):
    if a == b:
        return False
    try:
        r = subprocess.run(["git", "-C", ROOT, "merge-base", "--is-ancestor", a, b], capture_output=True, timeout=30)
        return r.returncode == 0
    except Exception:
        return False


def seal_order_problems(computed, listed, ceiling=SEAL_ORDER_UNSHOWN_CEILING, off_main=SEAL_ORDER_SHOWN_OFF_MAIN,
                        strict_ancestor=_strict_ancestor):
    problems = []
    for a in sorted(set(computed) - set(listed) - set(off_main)):
        problems.append("%s: rule and record first committed together (%s) and not on the list -- seal the rule in its "
                        "own commit before the results" % (a, computed[a][:9]))
    for a in sorted(set(listed) - set(ceiling)):
        problems.append("%s: added to the list, which may only shrink" % a)
    for a in sorted(set(listed) - set(computed)):
        problems.append("%s: listed, but its order now shows on main -- remove its row" % a)
    for a in sorted(set(listed) & set(computed)):
        if not computed[a].startswith(listed[a]):
            problems.append("%s: the list names %s, git %s" % (a, listed[a], computed[a][:9]))
    for a, (seal, record) in sorted(off_main.items()):
        if a in computed and not strict_ancestor(seal, record):
            problems.append("%s: its off-main order (%s before %s) is not shown in this clone" % (a, seal, record))
    return problems


def gate_seal_order_unshown():
    """R76-2 (P-601): the sealed tests whose rule and record git shows only as one commit are a frozen list that may only
    shrink. A new test sealed with its results fails, an entry added beyond the ceiling fails, a listed test whose order
    now shows must leave the list, and B1670's off-main order must still be shown."""
    computed = seal_order_class()
    if computed is None:
        return False, "git log failed -- the class cannot be recomputed"
    if not os.path.isfile(os.path.join(ROOT, SEAL_ORDER_DOC)):
        return False, SEAL_ORDER_DOC + " missing -- the list is gone"
    listed = seal_order_listed(_read(SEAL_ORDER_DOC))
    bad = seal_order_problems(computed, listed)
    if not bad and seal_order_class is _ORIG_SEAL_ORDER_CLASS:
        bad = seal_order_after_problems()
    if bad:
        return False, "; ".join(bad[:4])
    return True, "ok (%d listed, at most %d; B1670's order shown off main)" % (len(listed), len(SEAL_ORDER_UNSHOWN_CEILING))


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
    if _git("rev-parse", "--git-dir")[0] != 0:
        return False, "cannot verify: git unavailable"
    if not os.path.isfile(os.path.join(ROOT, "docs", "RETRACTED_PHRASES.md")):
        return False, "docs/RETRACTED_PHRASES.md missing -- the retraction registry is gone"
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "checks"))
    try:
        import retraction_sweep as rs
    except Exception as exc:
        return False, f"retraction_sweep unimportable: {exc}"
    finally:
        sys.path.pop(0)
    if not rs._phrases():
        return False, "docs/RETRACTED_PHRASES.md yielded 0 phrases"
    v = rs.sweep()
    return not v, [f"{r}:{n} {p!r}" for r, n, p in v[:5]] or "ok"


def _debt_git_env(env_var):
    """B1879 (G5/PV9, G6/PV15, G13/PV22): fail closed without git or on a shallow clone, and pin debt aging to HEAD's commit date."""
    rc, _ = _git("rev-parse", "--git-dir")
    if rc != 0:
        return False, "cannot verify: git unavailable", None
    rcs, sh_out = _git("rev-parse", "--is-shallow-repository")
    if rcs == 0 and sh_out.strip() == "true":
        return False, "cannot verify: shallow clone truncates commit history", None
    rcd, hd = _git("log", "-1", "--format=%cs")
    if rcd != 0 or not hd.strip():
        return False, "cannot verify: HEAD commit date unreadable", None
    env = dict(os.environ)
    env[env_var] = hd.strip()
    return True, "", env



# L143 (B976 -> B977): the third gate. `lawmap-scope` and `retraction-sweep` police the
# CONTENT of rows that exist; neither notices a row that was NEVER WRITTEN. B976 found
# eleven banked cascade arcs cited zero times on any synthesis surface -- including B864,
# which DERIVES hypercharge, while a ledger row written five days later called hypercharge
# "OPEN, the sharpest available target". The repo lost nothing; the summaries forgot.
def gate_relay_debt():
    """B999 -- branch protection preserves FILES; nothing preserved FINDINGS (design: cc3)."""
    ok_env, why_env, env = _debt_git_env("OA_RELAY_TODAY")
    if not ok_env:
        return False, why_env
    r = subprocess.run([sys.executable, os.path.join(str(ROOT), "scripts", "checks", "relay_debt.py")],
                       capture_output=True, text=True, env=env)
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
    ok_env, why_env, env = _debt_git_env("OA_HARVEST_TODAY")
    if not ok_env:
        return False, why_env
    r = subprocess.run([sys.executable, os.path.join(str(ROOT), "scripts", "checks", "harvest_debt.py"), "--quiet"],
                       capture_output=True, text=True, timeout=300, env=env)
    out = (r.stdout + r.stderr).strip()
    if r.returncode != 0:
        return False, out.replace("\n", " | ")[:500]
    return True, "ok"


def gate_lead_debt():
    """2026-10-01 -- a deferral lands as a LEAD or as an arc left at verdict OPEN, and nothing aged either (the relay and
    harvest gates age the other two kinds of debt). A ratchet: the stale counts may only shrink. Also fails on a lead number
    carried by two open leads (the E71 class, twice on 2026-09-18)."""
    ok_env, why_env, env = _debt_git_env("OA_LEAD_TODAY")
    if not ok_env:
        return False, why_env
    r = subprocess.run([sys.executable, os.path.join(str(ROOT), "scripts", "checks", "lead_debt.py")],
                       capture_output=True, text=True, timeout=300, env=env)
    out = (r.stdout + r.stderr).strip()
    if r.returncode != 0:
        return False, out.replace("\n", " | ")[:500]
    return True, "ok"


def gate_inputs_scoreboard():
    """2026-10-29, the owner's ruling (P-418): a total-inputs scoreboard beside '0 of 19' -- each frame's borrowed joints
    counted, the identification price, progress = the totals falling; 2026-11-04 (P-661): a complete picture with its
    borrowed joints named. Fails if the data is malformed (an earned joint without an existing basis) or the page is stale."""
    import subprocess
    r = subprocess.run([sys.executable, os.path.join(str(ROOT), "scripts", "checks", "inputs_scoreboard.py"), "--check"],
                       capture_output=True, text=True, timeout=120)
    out = (r.stdout + r.stderr).strip()
    return r.returncode == 0, (out.splitlines()[-1] if out else "no output")


def gate_point_debt():
    """2026-10-13 -- the owner: "we clarify the picture, but fail to address all the points we made, and get lost to one
    of the multiple things we have to deal with." Every point a review raises has a row in docs/POINT_REGISTER.md with a
    disposition and a queue slot; no row may be deleted; a queued point unmoved for 21 days fails unless escalated."""
    ok_env, why_env, env = _debt_git_env("OA_POINT_TODAY")
    if not ok_env:
        return False, why_env
    r = subprocess.run([sys.executable, os.path.join(str(ROOT), "scripts", "checks", "point_debt.py")],
                       capture_output=True, text=True, timeout=300, env=env)
    out = (r.stdout + r.stderr).strip()
    if r.returncode != 0:
        return False, out.replace("\n", " | ")[:500]
    return True, out.splitlines()[0] if out else "ok"


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
        if "⟦" in body: bad.append(os.path.basename(d) + " (an unfilled placeholder: the sweep's result was never entered)")    # R70 (B1743, B1746)
        elif "topic-sweep" not in body and "absence-sweep" not in body and "sweep" not in body: bad.append(os.path.basename(d) + " (no repo sweep cited)")
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
GENESIS_USERS = ("README.md", "docs/THE_PROGRAMME_SO_FAR.md", "WORKING_RULES.md", "docs/OPEN_LEADS.md", "docs/THE_FOUNDATION_LOCK_PLAN.md", "docs/THE_CLAIM.md",
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


def gate_doc_facts():
    """P-417 (the owner's question of 2026-10-28) -- a front page must not state a current fact its source contradicts;
    doc-currency measures recency and cannot see a stale banner beside a fresh citation."""
    import subprocess
    r = subprocess.run([sys.executable, os.path.join(str(ROOT), "scripts", "checks", "doc_facts.py")],
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
    # (b) the ratchet (fails closed if missing, B1879 / PV10)
    if not os.path.exists(base):
        problems.append("docs/IDENTIFICATION_BASELINE.json missing -- unearned-count ratchet cannot be verified")
    else:
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


def review_waiver_covers(n, text, since=None):
    """a waiver is one line '- waived <YYYY-MM-DD> by the owner through <N> merges: <reason>'; it covers while n < N.
    Review 75 (B1844): a waiver covers only the window it was granted in -- with `since` (the last anchor's date,
    YYYY-MM-DD), a waiver dated before it has expired; without it every line is read (the old behaviour)."""
    best = 0
    for m in re.finditer(r"^- waived (\d{4}-\d{2}-\d{2}) by the owner through (\d+) merges", text or "", re.M):
        if since and m.group(1) < since:
            continue
        best = max(best, int(m.group(2)))
    return n < best


def review_anchor_date():
    """the commit date (YYYY-MM-DD) of the last review's anchor-commit, or None"""
    text = _read(REVIEWS) if os.path.exists(os.path.join(ROOT, REVIEWS)) else ""
    anchors = re.findall(r"anchor-commit: `?([0-9a-f]{7,40})`?", text)
    if not anchors:
        return None
    rc, out = _git("log", "-1", "--format=%cs", anchors[-1])
    return out.strip() if rc == 0 and out.strip() else None


def gate_review_fires():
    """GOVERNANCE §15 (amendment 2026-10-03, R58-1 item 1): past twice its period (REVIEW_HARD merges on main's
    first-parent line since the last anchor) the decadal review is not a report but a block, unless the owner has
    waived it by date in REVIEW_WAIVER.  OA_REVIEW_MERGES overrides the count for the failing-path test."""
    n, _due = review_status()
    if os.environ.get("OA_REVIEW_MERGES"):
        n = int(os.environ["OA_REVIEW_MERGES"])
    elif _git("rev-parse", "--git-dir")[0] != 0:
        return False, "cannot verify: git unavailable"
    if n is None:
        return True, "no review anchor yet"
    if n >= REVIEW_HARD:
        wpath = os.path.join(ROOT, REVIEW_WAIVER)
        if review_waiver_covers(n, _read(REVIEW_WAIVER) if os.path.isfile(wpath) else "", since=review_anchor_date()):
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
    tests/GATE_CONTROLS.json; the named function must exist, must not be skipped/xfailed, and must not be vacuous (B1879, G7 / PV16)."""
    p = os.path.join(ROOT, GATE_CONTROLS)
    if not os.path.isfile(p):
        return False, f"{GATE_CONTROLS} missing -- the register of failing-path tests is gone"
    try:
        reg = json.loads(_read(GATE_CONTROLS))
    except Exception as exc:
        return False, f"{GATE_CONTROLS} unreadable: {exc}"
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "checks"))
    try:
        import check_test_vacuity as ctv
    except Exception as exc:
        return False, f"vacuity checker unimportable for gate-controls: {exc}"
    finally:
        sys.path.pop(0)
    problems = []
    missing = sorted(g for g in GATES if g not in reg)
    if missing:
        problems.append("gates with no registered failing-path test: " + ", ".join(missing))
    parsed_cache = {}
    for g, ref in sorted(reg.items()):
        if "::" not in ref:
            problems.append(f"{g}: malformed reference {ref!r}"); continue
        f, fn = ref.split("::", 1)
        fp = os.path.join(ROOT, f)
        if not os.path.isfile(fp):
            problems.append(f"{g}: {f} does not exist"); continue
        if fp not in parsed_cache:
            try:
                parsed_cache[fp] = ast.parse(open(fp, encoding="utf-8", errors="replace").read())
            except Exception as exc:
                parsed_cache[fp] = exc
        tree = parsed_cache[fp]
        if isinstance(tree, Exception):
            problems.append(f"{g}: {f} syntax error: {tree}"); continue
        fn_node = next((n for n in ast.walk(tree)
                        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == fn), None)
        if fn_node is None:
            problems.append(f"{g}: {fn} not defined in {f}"); continue
        skip_dec = any(
            any(tok in ast.dump(dec) for tok in ("'skip'", "'skipif'", "'xfail'", '"skip"', '"skipif"', '"xfail"'))
            for dec in fn_node.decorator_list
        )
        skip_call = any(
            isinstance(sub, ast.Call) and getattr(sub.func, "attr", None) in ("skip", "xfail")
            for sub in ast.walk(fn_node)
        )
        if skip_dec or skip_call:
            problems.append(f"{g}: {ref} is skipped or xfailed"); continue
        na, ta, _ = ctv.check_function_node(fn_node, f)
        if na or ta:
            problems.append(f"{g}: {ref} is vacuous ({(na + ta)[0]})")
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

# --- the goal may be stated; arrival may not (the owner's ruling R1, confirmed to main 2026-11-10; B1878) --------------------
# GOVERNANCE.md § 1, as amended: the programme's only goal is a parameter-free theory of everything.  A goal says what is sought.
# The framing lock's ceiling is unchanged: no page says or implies that a value, or the Standard Model, HAS BEEN derived.  This
# gate reads the living pages for a sentence of arrival, with a negation window ("no value of the Standard Model is derived" is
# the record's own sentence and passes), held to a frozen baseline of old lines that may only shrink.
ARRIVAL_PHRASES = ("the standard model is derived", "the standard model has been derived", "derives the standard model", "derived the standard model",
                   "we derive the standard model", "is a theory of everything", "the theory of everything is", "a theory of everything has been",
                   "all nineteen are derived", "all nineteen derived", "19 of 19 derived", "19 of 19 earned", "nineteen of nineteen",
                   "the values are derived", "the masses are derived", "the couplings are derived")
ARRIVAL_NEGATION = PRETENSE_NEGATION + ("none", "nothing", "0 of 19", "neither", "nor ", "cannot", "would", "whether", "if ", "until", "goal", "aim", "seek", "sought", "to be ")
ARRIVAL_EXEMPT = PRETENSE_EXEMPT + ("GOVERNANCE.md", "docs/README_HISTORY.md", "docs/POINT_REGISTER.md", "docs/LEAD_REGISTER.md", "docs/OPEN_LEADS.md",
                                    "docs/LOOK_LEDGER.md", "docs/FAILURE_ATLAS.md")      # the page that states the rule; dated history; registers that quote what was said
ARRIVAL_BASELINE = 3      # frozen at B1878 (2026-11-11), may only shrink: a plan of 2026-07-24 ("the program derived the Standard Model's
                          # grammar"), a dated state page ("derives the Standard Model's gauge skeleton ... and derives none of its numbers"),
                          # and the owner's question of 2026-08-09, quoted ("... that our program is a theory of everything ...")


def arrival_hits(root=None):
    import glob
    root = str(root or ROOT); hits = []
    files = sorted(glob.glob(os.path.join(root, "docs", "*.md")) + glob.glob(os.path.join(root, "*.md")))
    for f in files:
        rel = os.path.relpath(f, root)
        if rel in ARRIVAL_EXEMPT: continue
        low = open(f, errors="replace").read().lower()
        for p in ARRIVAL_PHRASES:
            n = 0
            for m in re.finditer(re.escape(p), low):
                window = " " + re.sub(r"\s+", " ", low[max(0, m.start() - 64):m.start()])       # a denial may open a line or a file
                if any(neg in window for neg in ARRIVAL_NEGATION): continue          # a denial, a condition or a statement of aim is not arrival
                n += 1
            if n: hits.append((rel, p, n))
    return hits


def gate_arrival_phrases(_root=None, _baseline=None):
    """The aim may be stated and arrival may not (GOVERNANCE.md § 1 and § 2 as amended at the owner's ruling)."""
    base = ARRIVAL_BASELINE if _baseline is None else _baseline
    hits = arrival_hits(_root); n = sum(c for _, _, c in hits)
    if n > base:
        return False, "%d sentence(s) of arrival on living pages (baseline %d): " % (n, base) + "; ".join("%s: %s x%d" % h for h in hits[:5])
    return True, "ok (%d on living pages, baseline %d%s)" % (n, base, "; lower the baseline" if n < base else "")


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

_SEAT_ID_RE = re.compile(r"^(sm:B\d{4}|sm:W\d{1,3}|xB\d{3}|LP\d{2}|R\d{3}[A-Z]?|memo \d+|B8\d{3})$")   # sm:W<n>: a dossier item (R61-3)


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
            if sid.startswith("sm:W"):
                # a dossier item is rowed by its bare name in the item column of an SM-derivation seat row (R61-3, R62-3)
                w = sid[3:]
                def _is_row(l, w=w):
                    cells = [c.strip() for c in l.split("|")]
                    return len(cells) > 3 and cells[2] == "SM-derivation seat" and re.match(r"^" + re.escape(w) + r"(?![0-9])", cells[3])
                verified = any(_is_row(l) and ("**VERIFIED" in l or "**REPRODUCED" in l) for l in rows)   # REPRODUCED: Review 66, P-125
            else:
                pat = re.compile(r"(?<![A-Za-z0-9:])" + re.escape(sid) + r"(?![0-9])")
                verified = any(pat.search(l) and ("**VERIFIED" in l or "**REPRODUCED" in l) for l in rows)
            out.append((d.get("id", "?"), sid, verified, "ok" if verified else "no VERIFIED row in docs/HARVEST_LEDGER.md"))
    return out


# Review 66 (R65-7, P-124): declaring was manual, and a sealed arc used W59 undeclared (B1656). From this arc on every
# seat id named in a verdict's claim line or scope is declared: in `rests_on_seat` (built on; must be VERIFIED) or in
# `cites_seat` (cited only: credit, a pointer, a comparison, an open question)
SEAT_DECLARED_FROM_ARC = 1685
_SEAT_MENTION_RE = re.compile(r"(?<![A-Za-z0-9:])(sm:B\d{4}|xB\d{3}|LP\d{2}|W\d{1,3})(?![0-9])")


def seat_undeclared(reader=None, start=SEAT_DECLARED_FROM_ARC):
    """(arc id, seat id) for every seat id named in a verdict's claim line or scope but in neither `rests_on_seat` nor
    `cites_seat`, for arcs numbered `start` and above; a bare W<n> is the SM seat's dossier item sm:W<n>"""
    reader = reader or (lambda rel: _read(rel)); out = []
    for p in sorted(glob.glob(os.path.join(ROOT, "frontier", "B*", "arc_verdict.json"))):
        m = re.match(r"B(\d+)_", os.path.basename(os.path.dirname(p)))
        if not m or int(m.group(1)) < start: continue
        try:
            d = json.loads(reader(os.path.relpath(p, ROOT)))
        except Exception:
            continue
        text = (d.get("claim_one_line") or "") + " " + json.dumps(d.get("scope") or {}, ensure_ascii=False)
        declared = {str(x) for x in (d.get("rests_on_seat") or []) + (d.get("cites_seat") or [])}
        for sid in sorted(set(_SEAT_MENTION_RE.findall(text))):
            full = "sm:" + sid if sid.startswith("W") else sid
            if full not in declared and sid not in declared:
                out.append((d.get("id", "?"), full))
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
    und = seat_undeclared(reader)
    if und:
        return False, "%d seat id(s) named in a verdict but declared in neither rests_on_seat nor cites_seat: " % len(und) + "; ".join("%s names %s" % u for u in und[:6])
    return True, "ok (%d declared seat dependencies, all VERIFIED or REPRODUCED on main)" % len(rests)


def gate_arc_data():
    """P-420 phase 0 (the owner's GO, 2026-10-29): the arcs' machine-readable data a generated desk reads must not
    contradict itself. scripts/checks/arc_data.py's defect classes D1-D6 must be empty: a duplicated id (beyond the
    grandfathered), a folder whose number is not its id, a dependency on nothing, on a folder with FINDINGS but no verdict,
    on a non-arc id (a seat id belongs in rests_on_seat or cites_seat), or a one-sided supersession. The resolved cases
    (R1-R5) and the prose-only candidates (D7) are reported, not gated."""
    import importlib.util as _ilu
    sp = _ilu.spec_from_file_location("arc_data", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "checks", "arc_data.py"))
    m = _ilu.module_from_spec(sp); sp.loader.exec_module(m)
    out = m.check(root=ROOT)
    bad = {k: v for k, v in out.items() if (k == "unreadable verdict files" or k[:2] in ("D1", "D2", "D3", "D4", "D5", "D6")) and v}
    if bad:
        return False, "; ".join("%s: %s" % (k, (list(v)[:4] if isinstance(v, dict) else v[:4])) for k, v in bad.items())[:600]
    return True, "ok (%d verdict files; D1-D6 empty; %d prose-only candidates reported)" % (out["verdict files"], len(out["D7 relation in prose only (candidates)"]))


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
    "arc-data": gate_arc_data,
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
    "doc-facts": gate_doc_facts,
    "relay-debt": gate_relay_debt,
    "retraction-debt": gate_retraction_debt,
    "harvest-debt": gate_harvest_debt,
    "lead-debt": gate_lead_debt,
    "point-debt": gate_point_debt,
    "inputs-scoreboard": gate_inputs_scoreboard,
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
    "seal-immutable": gate_seal_immutable,
    "artifact-hashes": gate_artifact_hashes,
    "closure-generated": gate_closure_generated,
    "arrival-phrases": gate_arrival_phrases,
    "seal-order-unshown": gate_seal_order_unshown,
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


# Gates whose passing sentence carries a count the reader must see on every run: waivers and amendments made by name. The
# advisor seat's second re-audit (its cases a2 and s5): a waiver made its violation vanish from the gate's own sentence. Main
# found one thing more when mending it (B1874): the runner printed a bare "ok" for every pass, so a gate's sentence, waivers
# and all, never reached the reader.
PRINTS_ITS_SENTENCE = ("append-only", "seal-immutable", "artifact-hashes")


def result_line(name, ok, detail):
    """the one line the runner prints for a gate. A gate that passed by checking nothing is printed SKIP with its own words,
    never a bare "ok" (the advisor seat's audit, G5; main's planted run found five gates that skip without git and print ok).
    A gate that holds waivers or amendments by name prints its whole sentence when it passes."""
    skipped = ok and isinstance(detail, str) and ("skipped" in detail or "unavailable" in detail or "no review anchor" in detail)
    if skipped:
        return f"  SKIP  {name}: {detail}"
    if ok and name in PRINTS_ITS_SENTENCE and isinstance(detail, str) and detail:
        return f"  PASS  {name}: {detail}"
    return f"  {'PASS' if ok else 'FAIL'}  {name}: {detail if not ok else 'ok'}"


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "review-due":
        n, due = review_status()
        print(f"merges since last review: {n}; due (>= {REVIEW_EVERY}): {due}")
        # B1307: a review opens with the harvest debt and cannot close with unread seat results (--strict)
        r = subprocess.run([sys.executable, os.path.join(str(ROOT), "scripts", "checks", "harvest_debt.py"), "--strict"],
                           capture_output=True, text=True, timeout=300)
        print((r.stdout + r.stderr).rstrip())
        # Review 66 (R65-8, P-126): the rule "a review cannot close with unread seat results" is enforced, not advisory
        sys.exit(r.returncode)
    res = run_all()
    worst = 0
    for name, (ok, detail) in res.items():
        print(result_line(name, ok, detail))
        worst = max(worst, 0 if ok else 1)
    n, due = review_status()
    print(f"  review-due: {n} merges since last review "
          f"({'DUE — run the decadal review' if due else 'not due'})")
    # the owner, 2026-10-13: the open points and the next queue slot are shown on every push, so none is lost
    import subprocess
    pr = subprocess.run([sys.executable, os.path.join(str(ROOT), "scripts", "checks", "point_debt.py")],
                        capture_output=True, text=True, timeout=300)
    if pr.stdout.strip():
        print("  " + pr.stdout.strip().splitlines()[0] + " (docs/POINT_REGISTER.md)")
    # the owner's ruling of 2026-10-29 (P-418): the total-inputs scoreboard is printed beside '0 of 19' on every run
    sb = subprocess.run([sys.executable, os.path.join(str(ROOT), "scripts", "checks", "inputs_scoreboard.py")],
                        capture_output=True, text=True, timeout=120)
    if sb.stdout.strip():
        print("  " + sb.stdout.strip().splitlines()[-1] + " (docs/TOTAL_INPUTS_SCOREBOARD.md)")
    sys.exit(worst)
