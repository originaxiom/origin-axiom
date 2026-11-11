"""B1879 -- unit and integration locks for Re-Audit 2, Re-Audit 3 (t3, t4, t7, j4, leaf PV14),
Review 78 reader additions on append-only, P-154 retraction-sweep Format 3, X3 live price
certificate, L6/L10 suite repairs, and the P-670 holomorphic quarter-nome jtheta sweep."""
from __future__ import annotations

import ast
import base64
import hashlib
import importlib.util
import json
import pathlib
import subprocess
import sys

import mpmath as mp

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load_gates():
    spec = importlib.util.spec_from_file_location("gates_b1879", ROOT / "scripts" / "gates" / "gates.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _init_git_repo(tmp_path: pathlib.Path):
    def git(*args):
        return subprocess.run(
            ["git", "-C", str(tmp_path), "-c", "user.name=originaxiom",
             "-c", "user.email=originaxiom@users.noreply.github.com", *args],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    git("init", "-q", "-b", "main")
    return git


# --- Re-Audit 3: t3 (decoy shadowing), t4 (frozen broken re-edit), t7 (SEAL_SHA256.txt) ---

def test_reaudit3_t3_decoy_shadowing_and_ambiguous_bare_name_refused(tmp_path):
    """t3: (1) a list entry starting with 'frontier/' resolves ONLY from ROOT, so planting a decoy
    at list_dir/frontier/... cannot hide editing the real script; (2) a bare filename present in
    both list_dir and list_dir/verification fails closed with AMBIGUOUS."""
    g = _load_gates()
    git = _init_git_repo(tmp_path)

    real = tmp_path / "frontier" / "B9100_t3" / "verification" / "run.py"
    real.parent.mkdir(parents=True)
    orig_bytes = b"print('sealed')\n"
    real.write_bytes(orig_bytes)
    orig_sha = hashlib.sha256(orig_bytes).hexdigest()

    # Decoy placed inside list_dir/frontier/... holding the original hash while real is tampered
    decoy = tmp_path / "frontier" / "B9100_t3" / "frontier" / "B9100_t3" / "verification" / "run.py"
    decoy.parent.mkdir(parents=True)
    decoy.write_bytes(orig_bytes)
    real.write_bytes(b"print('tampered after seal')\n")

    lst = tmp_path / "frontier" / "B9100_t3" / "ARTIFACT_HASHES.txt"
    lst.write_text(f"{orig_sha}  frontier/B9100_t3/verification/run.py\n", encoding="utf-8")
    git("add", "-A")
    git("commit", "-q", "-m", "t3 decoy plant")
    base = git("rev-parse", "HEAD")

    ok, why = g.gate_artifact_hashes(_repo=str(tmp_path), _frozen=frozenset(), _root=base)
    assert not ok and ("AMBIGUOUS" in why or "MISMATCH" in why), why

    # Case 2: bare filename 'ambig.py' present in BOTH arc dir and arc/verification -> AMBIGUOUS
    repo2 = tmp_path / "r2"
    repo2.mkdir()
    git2 = _init_git_repo(repo2)
    d2 = repo2 / "frontier" / "B9101_ambig"
    (d2 / "verification").mkdir(parents=True)
    (d2 / "ambig.py").write_bytes(orig_bytes)
    (d2 / "verification" / "ambig.py").write_bytes(orig_bytes)
    (d2 / "ARTIFACT_HASHES.txt").write_text(f"{orig_sha}  ambig.py\n", encoding="utf-8")
    git2("add", "-A")
    git2("commit", "-q", "-m", "ambiguous bare name")
    base2 = git2("rev-parse", "HEAD")

    ok2, why2 = g.gate_artifact_hashes(_repo=str(repo2), _frozen=frozenset(), _root=base2)
    assert not ok2 and "AMBIGUOUS" in why2, why2


def test_reaudit3_t4_re_editing_frozen_broken_script_refused(tmp_path, monkeypatch):
    """t4: a broken entry frozen by key in ARTIFACT_HASHES_BROKEN is also pinned to its disk SHA-256
    at freeze time, so editing it a second time fails with MODIFIED AFTER FREEZE."""
    g = _load_gates()
    git = _init_git_repo(tmp_path)

    arc = tmp_path / "frontier" / "B9102_t4"
    arc.mkdir(parents=True)
    scr = arc / "script.py"
    seal_sha = hashlib.sha256(b"v0_sealed\n").hexdigest()
    v1_bytes = b"v1_broken_at_freeze\n"
    v1_sha = hashlib.sha256(v1_bytes).hexdigest()
    scr.write_bytes(v1_bytes)
    rel_lst = "frontier/B9102_t4/ARTIFACT_HASHES.txt"
    (tmp_path / rel_lst).write_text(f"{seal_sha}  script.py\n", encoding="utf-8")
    git("add", "-A")
    git("commit", "-q", "-m", "freeze state")
    base = git("rev-parse", "HEAD")

    key = hashlib.sha256(f"{rel_lst}|script.py|{seal_sha}".encode("utf-8")).hexdigest()[:12]
    monkeypatch.setattr(g, "ARTIFACT_HASHES_BROKEN_DISK", {key: ("frontier/B9102_t4/script.py", v1_sha)})

    # At freeze SHA, passes when key is in _frozen
    ok0, why0 = g.gate_artifact_hashes(_repo=str(tmp_path), _frozen=frozenset({key}), _root=base)
    assert ok0, why0

    # Re-editing the broken script a second time -> refused!
    scr.write_bytes(b"v2_edited_again_silently\n")
    ok1, why1 = g.gate_artifact_hashes(_repo=str(tmp_path), _frozen=frozenset({key}), _root=base)
    assert not ok1 and "MODIFIED AFTER FREEZE" in why1, why1


def test_reaudit3_t7_secondary_seal_sha256_list_enforced_and_immutable(tmp_path):
    """t7: secondary seal hash lists (SEAL_SHA256.txt, etc.) verify their listed files AND refuse
    post-seal edits or deletions to the secondary hash list itself."""
    g = _load_gates()
    git = _init_git_repo(tmp_path)

    arc = tmp_path / "frontier" / "B9103_t7"
    arc.mkdir(parents=True)
    prereg = arc / "PREREGISTRATION.md"
    p_bytes = b"# Sealed rule\n"
    p_sha = hashlib.sha256(p_bytes).hexdigest()
    prereg.write_bytes(p_bytes)
    seal_lst = arc / "SEAL_SHA256.txt"
    seal_lst.write_text(f"{p_sha}  PREREGISTRATION.md\n", encoding="utf-8")
    git("add", "-A")
    git("commit", "-q", "-m", "seal secondary list")
    base = git("rev-parse", "HEAD")

    ok0, why0 = g.gate_artifact_hashes(_repo=str(tmp_path), _frozen=frozenset(), _root=base)
    assert ok0 and "secondary seal lists: 1 entries (1 verify" in why0, why0

    # Tamper with the file pinned in SEAL_SHA256.txt
    prereg.write_bytes(b"# Tampered rule\n")
    ok1, why1 = g.gate_artifact_hashes(_repo=str(tmp_path), _frozen=frozenset(), _root=base)
    assert not ok1 and "SEAL_SHA256.txt" in why1 and "MISMATCH" in why1, why1

    # Restore file, then commit an edit to SEAL_SHA256.txt itself after base -> refused!
    prereg.write_bytes(p_bytes)
    new_bytes = b"# Re-hashed tampered rule\n"
    prereg.write_bytes(new_bytes)
    seal_lst.write_text(f"{hashlib.sha256(new_bytes).hexdigest()}  PREREGISTRATION.md\n", encoding="utf-8")
    git("add", "-A")
    git("commit", "-q", "-m", "rewrite SEAL_SHA256.txt")
    ok2, why2 = g.gate_artifact_hashes(_repo=str(tmp_path), _frozen=frozenset(), _root=base)
    assert not ok2 and "SEAL_SHA256.txt" in why2, why2


# --- Review 78 reader additions on append-only + archive append-only (P-772(d)) ---

def test_archive_append_only_refuses_rewrite_and_review78_append_only_edges(tmp_path, monkeypatch):
    g = _load_gates()
    git = _init_git_repo(tmp_path)
    arch = tmp_path / "docs" / "progress"
    arch.mkdir(parents=True)
    p = arch / "PROGRESS_2026-07.md"
    p.write_text("# Archive\nline 1\nline 2\n", encoding="utf-8")
    log = tmp_path / "PROGRESS_LOG.md"
    v1 = "# Header preamble\nKeep this header intact.\n\n## 2026-07-01 -- A\nold body\n\n## 2026-08-01 -- B\nnew body\n"
    log.write_text(v1, encoding="utf-8")
    git("add", "-A")
    git("commit", "-q", "-m", "init")
    base = git("rev-parse", "HEAD")

    # 1. Archive rewrite refused (a1)
    p.write_text("# Archive\nREWRITTEN LINE\nline 2\n", encoding="utf-8")
    git("add", "-A")
    git("commit", "-q", "-m", "rewrite archive")
    probs, n_c = g.archive_append_only_problems(str(tmp_path), base)
    assert len(probs) == 1 and n_c == 1 and "PROGRESS_2026-07.md" in probs[0]

    # 2. Pre-existing archive reuse without touching docs/progress/ in the roll-up commit -> refused
    repo2 = tmp_path / "r_pre"
    repo2.mkdir()
    git2 = _init_git_repo(repo2)
    (repo2 / "docs" / "progress").mkdir(parents=True)
    moved = "## 2026-07-01 -- A\nold body\n\n"
    (repo2 / "docs" / "progress" / "PROGRESS_2026-Q3.md").write_text("# Q3\n\n" + moved, encoding="utf-8")
    (repo2 / "PROGRESS_LOG.md").write_text(v1, encoding="utf-8")
    git2("add", "-A")
    git2("commit", "-q", "-m", "root with pre-existing archive")
    root2 = git2("rev-parse", "HEAD")
    kept = "# Header preamble\nKeep this header intact.\n\n## 2026-08-01 -- B\nnew body\n"
    (repo2 / "PROGRESS_LOG.md").write_text(kept, encoding="utf-8")
    git2("add", "-A")
    git2("commit", "-q", "-m", "roll-up without touching archive in commit")
    probs2, _ = g.append_only_problems(str(repo2), root2)
    assert len(probs2) == 1 and "archived verbatim: False" in probs2[0]

    # 3. Roll-up altering header before first '## 20' -> refused
    repo3 = tmp_path / "r_hdr"
    repo3.mkdir()
    git3 = _init_git_repo(repo3)
    (repo3 / "docs" / "progress").mkdir(parents=True)
    (repo3 / "PROGRESS_LOG.md").write_text(v1, encoding="utf-8")
    git3("add", "-A")
    git3("commit", "-q", "-m", "root3")
    root3 = git3("rev-parse", "HEAD")
    bad_hdr = "# TAMPERED HEADER\n\n## 2026-08-01 -- B\nnew body\n"
    (repo3 / "PROGRESS_LOG.md").write_text(bad_hdr, encoding="utf-8")
    (repo3 / "docs" / "progress" / "PROGRESS_2026-Q3.md").write_text("# Q3\n\n" + moved, encoding="utf-8")
    git3("add", "-A")
    git3("commit", "-q", "-m", "roll-up tampering header")
    probs3, _ = g.append_only_problems(str(repo3), root3)
    assert len(probs3) == 1 and "header before the first dated heading was altered" in probs3[0]

    # 4. Committed deletion AND committed rename of PROGRESS_LOG.md -> refused; module-level APPEND_ONLY_WAIVED tested
    repo4 = tmp_path / "r_del"
    repo4.mkdir()
    git4 = _init_git_repo(repo4)
    (repo4 / "PROGRESS_LOG.md").write_text(v1, encoding="utf-8")
    git4("add", "-A")
    git4("commit", "-q", "-m", "root4")
    root4 = git4("rev-parse", "HEAD")
    git4("mv", "PROGRESS_LOG.md", "PROGRESS_LOG_MOVED.md")
    git4("commit", "-q", "-m", "rename log")
    ren_sha = git4("rev-parse", "HEAD")
    probs4, _ = g.append_only_problems(str(repo4), root4)
    assert len(probs4) == 1 and "deletes PROGRESS_LOG.md" in probs4[0]

    # Restore log, waive both rename & restore via module-level APPEND_ONLY_WAIVED, and check gate_append_only() sentence
    (repo4 / "PROGRESS_LOG.md").write_text(v1 + "\n## 2026-09-01 -- C\nappend\n", encoding="utf-8")
    git4("add", "-A")
    git4("commit", "-q", "-m", "restore log")
    monkeypatch.setattr(g, "ROOT", str(repo4))
    monkeypatch.setattr(g, "APPEND_ONLY_FROM", root4)
    monkeypatch.setattr(g, "ARCHIVE_IMMUTABLE_FROM", root4)
    monkeypatch.setattr(g, "APPEND_ONLY_WAIVED", {ren_sha: "test rename waiver"})
    ok4, why4 = g.gate_append_only()
    assert ok4 and "1 waived by name" in why4 and "test rename waiver" in why4, why4


# --- Leaf PV14 (unreferenced leaf arc_verdict.json JSON corruption) ---

def test_leaf_arc_verdict_json_corruption_refused_by_both_gates(tmp_path, monkeypatch):
    """Leaf PV14 (6ab743907): truncating arc_verdict.json on a leaf arc that no downstream arc
    depends on must fail BOTH gate_arc_verdicts and scripts/checks/arc_data.py."""
    g = _load_gates()
    leaf = tmp_path / "frontier" / "B9999_leaf"
    leaf.mkdir(parents=True)
    (leaf / "FINDINGS.md").write_text("# B9999\n", encoding="utf-8")
    (leaf / "arc_verdict.json").write_text('{"id": "B9999", "verdict": ', encoding="utf-8")
    monkeypatch.setattr(g, "ROOT", str(tmp_path))
    ok, why = g.gate_arc_verdicts()
    assert not ok and "B9999" in str(why)

    sys.path.insert(0, str(ROOT / "scripts" / "checks"))
    try:
        import arc_data as ad
    finally:
        sys.path.pop(0)
    out = ad.check(root=str(tmp_path), branches=False)
    assert any("B9999_leaf" in r[0] for r in out["unreadable verdict files"])


# --- Re-Audit 2 & PV9..PV24, p2, X3, L6/L10, P-670 ---

def test_seal_order_after_refuses_rule_committed_after_record(tmp_path, monkeypatch):
    g = _load_gates()
    git = _init_git_repo(tmp_path)
    arc = tmp_path / "frontier" / "B9002_planted"
    arc.mkdir(parents=True)
    (arc / "FINDINGS.md").write_text("# FINDINGS\nResult first.\n", encoding="utf-8")
    git("add", "-A")
    git("commit", "-q", "-m", "record first")
    (arc / "PREREGISTRATION.md").write_text("# PREREG\nRule after.\n", encoding="utf-8")
    git("add", "-A")
    git("commit", "-q", "-m", "rule second")
    monkeypatch.setattr(g, "ROOT", str(tmp_path))
    probs = g.seal_order_after_problems()
    assert len(probs) == 1 and "frontier/B9002_planted/PREREGISTRATION.md" in probs[0]


def test_recursive_seal_discovery_sees_nested_and_prerun_note(tmp_path):
    g = _load_gates()
    (tmp_path / "frontier" / "B9010_nested" / "verification").mkdir(parents=True)
    (tmp_path / "frontier" / "B9010_nested" / "PRE_RUN_NOTE.md").write_text("# Note\n", encoding="utf-8")
    (tmp_path / "frontier" / "B9010_nested" / "verification" / "DESIGN.md").write_text("# Design\n", encoding="utf-8")
    (tmp_path / "frontier" / "B9010_nested" / "verification" / "W99_RULE.md").write_text("# Rule\n", encoding="utf-8")
    found = g.sealed_style_files(str(tmp_path))
    assert found == [
        "frontier/B9010_nested/PRE_RUN_NOTE.md",
        "frontier/B9010_nested/verification/DESIGN.md",
        "frontier/B9010_nested/verification/W99_RULE.md",
    ]


def test_fail_closed_without_git_and_missing_baselines(tmp_path, monkeypatch):
    g = _load_gates()
    (tmp_path / "docs" / "progress").mkdir(parents=True)
    monkeypatch.setattr(g, "ROOT", str(tmp_path))
    for fn in (
        g.gate_attribution,
        g.gate_tracked_forbidden,
        g.gate_log_changelog_paired,
        g.gate_views_fresh,
        g.gate_path_refs,
        g.gate_test_vacuity,
        g.gate_retraction_sweep,
        g.gate_review_fires,
        g.gate_harvest_debt,
        g.gate_identification_register,
        g.gate_law_map_provenance,
        g.gate_chain_locks,
    ):
        ok, _ = fn()
        assert ok is False, fn.__name__


def test_gate_controls_refuses_skip_and_vacuous_control(tmp_path, monkeypatch):
    g = _load_gates()
    (tmp_path / "tests").mkdir()
    tfile = tmp_path / "tests" / "test_ctrl.py"
    tfile.write_text("import pytest\n@pytest.mark.skip\ndef test_skipped():\n    assert 1 == 1\n", encoding="utf-8")
    reg = {k: "tests/test_ctrl.py::test_skipped" for k in g.GATES}
    (tmp_path / "tests" / "GATE_CONTROLS.json").write_text(json.dumps(reg), encoding="utf-8")
    monkeypatch.setattr(g, "ROOT", str(tmp_path))
    ok, why = g.gate_gate_controls()
    assert not ok and "skipped or xfailed" in why


def test_retraction_sweep_parses_all_three_table_shapes():
    sys.path.insert(0, str(ROOT / "scripts" / "checks"))
    try:
        import retraction_sweep as rs
    finally:
        sys.path.pop(0)
    phrases = rs._phrases()
    assert len(phrases) >= 47 and all(isinstance(p, str) for p in phrases)
    needle = base64.b64decode(b"bWlycm9yLWludmFyaWFudCBzcGluIHN0cnVjdHVyZQ==").decode()
    assert any(needle in p.lower() for p in phrases)


def test_attribution_ceiling_refuses_raised_baseline(monkeypatch):
    g = _load_gates()
    monkeypatch.setattr(g, "_load_attr_baseline", lambda: {"CHANGELOG.md": 99})
    ok, why = g.gate_attribution()
    assert not ok and "ATTRIBUTION_BASELINE raised for CHANGELOG.md" in str(why)


def test_claims_proven_lock_and_framing_tex_case_insensitive(tmp_path, monkeypatch):
    g = _load_gates()
    (tmp_path / "papers").mkdir()
    phrase = g.BANNED[0]
    (tmp_path / "papers" / "draft.tex").write_text(f"We claim {phrase.upper()} here.\n", encoding="utf-8")
    (tmp_path / "CLAIMS.md").write_text(
        "## Proven\n| P99 | Fake proven row | (no lock) |\n## Conditional\n## Open\n## Dead\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(g, "ROOT", str(tmp_path))
    ok_f, why_f = g.gate_framing()
    assert not ok_f and any("papers/draft.tex" in h[0] for h in why_f)
    ok_c, why_c = g.gate_claims()
    assert not ok_c and any("P99" in msg for msg in why_c)


def test_vacuity_catches_pure_both_literal_test_function():
    sys.path.insert(0, str(ROOT / "scripts" / "checks"))
    try:
        import check_test_vacuity as ctv
    finally:
        sys.path.pop(0)
    tree = ast.parse("def test_const():\n    x = 2\n    assert x != 3\n")
    no_a, taut, _ = ctv.check_function_node(tree.body[0], "tests/test_fake.py")
    assert no_a == [] and len(taut) == 1 and "pure both-literal function" in taut[0]


def test_tracked_deps_catches_two_step_string_concat():
    g = _load_gates()
    src = (
        'from pathlib import Path\nHERE = Path(__file__).parent\nRUNS = HERE / "runs"\n'
        'def test_b():\n    name = "driver_k1" + ".log"\n    assert "ok" in (RUNS / name).read_text()\n'
    )
    ok, why = g.gate_tracked_deps(_plant=("frontier/B1857_the_read_out_by_a_state_checked/verification/test_p2.py", src))
    assert not ok and "runs/driver_k1.log" in why and "git ignores this path" in why


def test_the_price_is_twelve_exits_zero_and_p670_quarter_nome_law():
    r = subprocess.run(
        [sys.executable, str(ROOT / "outside_bench" / "certificates" / "the_price_is_twelve.py")],
        cwd=str(ROOT), capture_output=True, text=True, timeout=60,
    )
    assert r.returncode == 0 and "LIVE PRICE: 4 axioms + 9 irreducible sources = 13" in r.stdout

    sweep_json = json.loads(
        (ROOT / "frontier" / "B1879_reaudit3_enforcement_and_p670_closure" / "verification" / "p670_variable_order_sweep.json").read_text(encoding="utf-8")
    )
    assert sweep_json["summary"]["unfixed_exposures"] == []
    assert sweep_json["summary"]["max_sheet_law_residual"] < 1e-12
    assert sweep_json["summary"]["b1678_s5_theta_repaired_verified"] is True

    # Independent @referee check of quarter-nome holomorphy across Re(2*tau) = 1.2 > 1 and Re(tau) = 1.3 > 1
    spec = importlib.util.spec_from_file_location(
        "b1678_s5_theta",
        ROOT / "frontier" / "B1678_the_lifted_register_verified" / "verification" / "main_check" / "s5_theta.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mp.mp.dps = 40
    tau = mp.mpc("0.6", "1.1")
    z = mp.mpc("0.23", "-0.14")
    val_holo = mod.analytic_jtheta(2, z, tau)
    val_naive = mp.jtheta(2, mp.pi * z, mp.exp(1j * mp.pi * tau))
    assert float(abs(val_holo - val_naive)) < 1e-30
    val_holo_2 = mod.analytic_jtheta(2, z, 2 * tau)
    val_naive_2 = mp.jtheta(2, mp.pi * z, mp.exp(1j * mp.pi * (2 * tau)))
    assert float(abs(val_naive_2 - (-1j) * val_holo_2)) < 1e-30
