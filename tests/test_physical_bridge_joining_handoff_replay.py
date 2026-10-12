"""Replay plumbing/custody safeguards, not physical/PDE acceptance tests.

Synthetic named predicates test rejection paths; none are represented as
new scientific results. This module never imports archived producers.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import zipfile

import pytest

REPO = Path(__file__).resolve().parents[1]
PACKET = REPO / "reports/physical_bridge_2026_09_05/joining_handoff_replay_2026_10_12"
spec = importlib.util.spec_from_file_location("joining_replay", PACKET / "replay.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


def exact(count=57):
    return {"checks": {f"synthetic_{i}": True for i in range(count)}}


def numeric3():
    return {"checks": {f"synthetic_{i}": {"pass": True} for i in range(72)},
            "total_checks": 72, "strict_count": 64, "finite_limit_count": 8,
            "dps": 50, "max_strict_residual": "synthetic",
            "max_finite_limit_residual": "synthetic"}


def numeric2():
    return {"exact_checks": {f"synthetic_{i}": True for i in range(8)},
            "numerical_checks": [{"name": f"synthetic_{i}", "passed": True}
                                 for i in range(48)],
            "precision_digits": 50, "max_normalized_residual": "synthetic"}


def test_all_eight_exact_source_members_and_current_candidate_match():
    inputs = json.loads((PACKET / "INPUTS.json").read_text())
    data = (REPO / inputs["archive_path"]).read_bytes()
    assert len(data) == inputs["archive_bytes"]
    assert hashlib.sha256(data).hexdigest() == inputs["archive_sha256"]
    assert len(inputs["members"]) == 8
    assert len({r["destination"] for r in inputs["members"]}) == 8
    candidate = (REPO / inputs["repository_candidate_path"]).read_bytes()
    with zipfile.ZipFile(REPO / inputs["archive_path"]) as archive:
        for row in inputs["members"]:
            body = archive.read(row["member"])
            assert len(body) == row["bytes"]
            assert hashlib.sha256(body).hexdigest() == row["sha256"]
            if row["destination"].endswith("candidate.json"):
                assert body == candidate


def test_named_exact_predicates_have_real_pass_and_failure_paths():
    assert runner.validate("gate1_primary", exact()) == {"exact_predicates": 57}
    bad = exact()
    bad["checks"]["synthetic_13"] = False
    with pytest.raises(RuntimeError, match="false predicate"):
        runner.validate("gate1_primary", bad)


def test_pass_status_cannot_replace_missing_checks():
    bad = exact(0)
    bad["status"] = "PASS"
    with pytest.raises(RuntimeError, match="population"):
        runner.validate("gate1_primary", bad)


def test_integer_one_is_not_a_reported_boolean_predicate():
    bad = exact()
    bad["checks"]["synthetic_0"] = 1
    with pytest.raises(RuntimeError, match="false predicate"):
        runner.validate("gate1_primary", bad)


def test_higher_precision_label_must_match_executed_precision():
    data = numeric2()
    assert runner.validate("gate2_reference_50", data)["numerical_checks"] == 48
    with pytest.raises(RuntimeError, match="precision mismatch"):
        runner.validate("gate2_reference_80", data)


def test_duplicate_and_failed_numeric_checks_are_not_masked():
    data = numeric2()
    data["numerical_checks"][-1]["name"] = "synthetic_0"
    with pytest.raises(RuntimeError, match="duplicate"):
        runner.validate("gate2_reference_50", data)
    data = numeric2()
    data["numerical_checks"][2]["passed"] = False
    with pytest.raises(RuntimeError, match="numeric false"):
        runner.validate("gate2_reference_50", data)


def test_strict_and_finite_limit_grades_are_not_merged():
    data = numeric3()
    assert runner.validate("gate3_numerical_50", data)["strict_checks"] == 64
    data["strict_count"], data["finite_limit_count"] = 72, 0
    with pytest.raises(RuntimeError, match="strict/limit"):
        runner.validate("gate3_numerical_50", data)


def test_false_gate3_numeric_predicate_stops_publication():
    data = numeric3()
    data["checks"]["synthetic_71"]["pass"] = False
    with pytest.raises(RuntimeError, match="Gate3 false"):
        runner.validate("gate3_numerical_50", data)


def test_unknown_command_label_is_rejected():
    with pytest.raises(RuntimeError, match="unknown command"):
        runner.validate("future_unsealed_science", numeric3())


def test_default_scratch_path_canonicalizes_directory_alias(tmp_path, monkeypatch):
    real = tmp_path / "actual"
    real.mkdir()
    scratch = real / "fresh"
    scratch.mkdir()
    alias = tmp_path / "alias"
    alias.symlink_to(real, target_is_directory=True)
    monkeypatch.setattr(runner.tempfile, "mkdtemp", lambda **_: str(alias / "fresh"))
    root = runner.new_output_directory(None)
    assert root == scratch.resolve()
    assert root in (root / "gate1" / "verify_bridge.py").resolve().parents
    assert alias / "fresh" not in (root / "gate1" / "verify_bridge.py").resolve().parents
