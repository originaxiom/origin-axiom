"""Real-Git custody regressions and synthetic admission, never science."""
from pathlib import Path
import subprocess
import sys
from unittest.mock import patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "gates"))
import prospective_strict
import tracked_state
from test_prospective_experiment_gate import packet, put


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


@pytest.fixture
def repository(tmp_path):
    git(tmp_path, "init", "-q")
    git(tmp_path, "config", "user.name", "Custody Fixture")
    git(tmp_path, "config", "user.email", "fixture@example.invalid")
    git(tmp_path, "config", "commit.gpgsign", "false")
    (tmp_path / "sentinel.txt").write_text("A\n")
    git(tmp_path, "add", "sentinel.txt")
    git(tmp_path, "commit", "-qm", "baseline fixture")
    return tmp_path


def hidden_index_change(root, name):
    path = root / name
    original = path.read_bytes()
    path.write_bytes(original + b"changed in index\n")
    git(root, "add", "--", name)
    path.write_bytes(original)
    assert git(root, "diff", "--name-only", "HEAD", "--") == ""


def test_clean_real_repository_and_wrong_head(repository):
    assert tracked_state.inspect(repository)["clean"]
    assert not tracked_state.inspect(repository, expected_head="0" * 40)["clean"]


@pytest.mark.parametrize("change", ["unstaged", "staged", "hidden_index"])
def test_separate_index_and_worktree_differences_fail(repository, change):
    if change == "hidden_index":
        hidden_index_change(repository, "sentinel.txt")
    else:
        (repository / "sentinel.txt").write_text("B\n")
        if change == "staged":
            git(repository, "add", "sentinel.txt")
    report = tracked_state.inspect(repository)
    assert not report["clean"]
    if change != "unstaged":
        assert report["index_changes"] == ["sentinel.txt"]
    if change != "staged":
        assert report["worktree_changes"] == ["sentinel.txt"]


def test_git_unavailable_fails_closed(tmp_path):
    report = tracked_state.inspect(tmp_path)
    assert not report["clean"] and len(report["errors"]) == 4


def test_unchanged_real_admission_keeps_history_noncompliant(packet):
    report = prospective_strict.evaluate("ADMISSION.json", root=packet["root"])
    assert report["prospective_admissible"] and not report["global_compliant"]
    assert report["tracked_state_before"]["clean"] and report["tracked_state_after"]["clean"]
    assert report["historical_seal_report"]["problems"]


def test_hidden_index_rejected_before_base_gate(packet):
    hidden_index_change(packet["root"], "fixture/probe.py")
    with patch.object(prospective_strict.prospective, "evaluate") as base:
        report = prospective_strict.evaluate("ADMISSION.json", root=packet["root"])
    base.assert_not_called()
    assert not report["prospective_admissible"]
    assert report["tracked_state_before"]["index_changes"] == ["fixture/probe.py"]


def test_changed_state_during_base_gate_cannot_pass(packet):
    original = prospective_strict.prospective.evaluate
    def base_then_change(*args, **kwargs):
        report = original(*args, **kwargs)
        assert report["prospective_admissible"]
        hidden_index_change(packet["root"], "fixture/probe.py")
        return report
    with patch.object(prospective_strict.prospective, "evaluate", side_effect=base_then_change):
        report = prospective_strict.evaluate("ADMISSION.json", root=packet["root"])
    assert not report["prospective_admissible"]
    assert not report["tracked_state_after"]["clean"]


def test_strict_guard_never_overrides_base_rejection(packet):
    put(packet["root"], "ADMISSION.json", "{")
    report = prospective_strict.evaluate("ADMISSION.json", root=packet["root"])
    assert not report["prospective_admissible"] and report["errors"]
