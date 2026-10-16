"""Isolated Git evidence tests for admission, not independent scientific review.

The aggregation fixture deliberately uses two gates, including the unchanged
historical seal gate. A separate repository-wide capture tests all real gates.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "gates"))
import gates
import prospective
import provenance_policy as policy


def put(root, path, value):
    data = json.dumps(value, indent=2) if isinstance(value, (dict, list)) else value
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data.encode() if isinstance(data, str) else data)
    return {"path": path, "sha256": hashlib.sha256(target.read_bytes()).hexdigest()}


def current_pin(root, path):
    return {"path": path, "sha256": hashlib.sha256((root / path).read_bytes()).hexdigest()}


def git(root, *args):
    result = subprocess.run(["git", "-C", str(root), *args], capture_output=True, check=False)
    assert result.returncode == 0, result.stderr.decode()
    return result.stdout.decode().strip()


def commit(root, message):
    git(root, "add", "--", "docs", "fixture")
    git(root, "commit", "-q", "--allow-empty", "-m", message)
    return git(root, "rev-parse", "HEAD")


def reseal(state):
    root, spec = state["root"], state["spec"]
    spec["design"] = current_pin(root, spec["design"]["path"])
    specification = put(root, "fixture/SPEC.json", spec)
    ledger = (root / "docs/SEAL_LEDGER.md").read_text()
    for row in (spec["design"], specification):
        ledger += f"| 2026-10-16 | fixture | `{row['path']}` | `{row['sha256']}` |\n"
    put(root, "docs/SEAL_LEDGER.md", ledger)
    sealed = commit(root, "seal exact fixture specification")
    state["admission"].update(sealed_commit=sealed, specification=specification)
    state["review"].update(sealed_commit=sealed, specification=specification)
    state["acceptance"].update(sealed_commit=sealed, specification=specification)


def rereview(state, accept_on_main=True):
    root = state["root"]
    review = put(root, "fixture/REVIEW.json", state["review"])
    reviewed = commit(root, "separate non-authoring review fixture")
    review_ref = {**review, "commit": reviewed}
    state["admission"]["review"] = review_ref
    state["acceptance"]["review"] = review_ref
    acceptance = put(root, "fixture/ACCEPTANCE.json", state["acceptance"])
    accepted = commit(root, "receiver accepts review fixture")
    state["admission"]["acceptance"] = {**acceptance, "commit": accepted}
    if accept_on_main:
        git(root, "update-ref", prospective.RECEIVER_REF, accepted)
    put(root, "ADMISSION.json", state["admission"])


@pytest.fixture
def packet(tmp_path, monkeypatch):
    git(tmp_path, "init", "-q")
    git(tmp_path, "config", "user.name", "originaxiom")
    git(tmp_path, "config", "user.email", "fixture@example.invalid")
    old = put(tmp_path, "fixture/OLD.md", "Historical missing-field design, never amended.\n")
    ev = put(tmp_path, "fixture/OLD_REVIEW.txt", "The original lacks required literal fields.\n")
    put(tmp_path, policy.ROLE_POLICY, {"schema": 1, "authority": "isolated fixture", "records": [
        {**old, "role": "historical_violation", "reason": "preserve failure", "evidence": ev}]})
    put(tmp_path, policy.REF_POLICY, {"schema": 1, "authority": "isolated fixture", "records": []})
    put(tmp_path, "docs/SEAL_LEDGER.md", f"| 2026-10-16 | old | `{old['path']}` | `{old['sha256']}` |\n")
    design = put(tmp_path, "fixture/DESIGN.md", "BANKED IDENTITY: fixture invariant\nPRIOR ART: fixture source read\n")
    source = put(tmp_path, "fixture/probe.py", "print('fixture only; not run by admission')\n")
    test = put(tmp_path, "fixture/check.py", "def check(x):\n    return x == 7\n")
    environment = put(tmp_path, "fixture/ENVIRONMENT.json", {"runtime": "fixture descriptor, not a real execution"})
    state = {"root": tmp_path, "admission": {"schema": 1},
        "spec": {"schema": 1, "experiment_id": "fixture", "authors": ["design_author"], "design": design,
                 "artifacts": [{**source, "role": "source"}, {**test, "role": "test"},
                               {**environment, "role": "input"}],
                 "commands": [{"entrypoint": source["path"], "argv": ["python3", source["path"]]}],
                 "outputs": ["fixture/new-result.json"], "environment": environment},
        "review": {"schema": 1, "experiment_id": "fixture", "reviewer": "separate_reviewer",
                   "nonauthoring": True, "source_complete": True, "decision": "APPROVE_EXECUTION",
                   "unresolved": [], "scope": "synthetic source completeness and independence fixture"},
        "acceptance": {"schema": 1, "experiment_id": "fixture", "receiver": "main",
                       "decision": "ACCEPT_INDEPENDENT_REVIEW", "verified_independence": True,
                       "verified_source_completeness": True}}
    reseal(state)
    rereview(state)
    monkeypatch.setattr(gates, "ROOT", str(tmp_path))
    # Test aggregation with one actual historical gate and one discriminating file gate.
    monkeypatch.setattr(gates, "GATES", {
        "seal-provenance": gates.gate_seal_provenance,
        "fixture-source": lambda: ((tmp_path / source["path"]).is_file(), "source file existence")})
    return state


def inspect(state):
    put(state["root"], "ADMISSION.json", state["admission"])
    return prospective.evaluate("ADMISSION.json")


def test_admission_can_pass_without_forgiving_history(packet):
    before = (packet["root"] / "fixture/OLD.md").read_bytes()
    report = inspect(packet)
    assert report["prospective_admissible"], report
    assert not report["global_compliant"]
    assert not report["governance"]["seal-provenance"][0]
    assert any(p["path"] == "fixture/OLD.md" and p["status"] == "historical_noncompliant"
               for p in report["historical_seal_report"]["problems"])
    assert (packet["root"] / "fixture/OLD.md").read_bytes() == before
    assert not (packet["root"] / "fixture/new-result.json").exists()


@pytest.mark.parametrize("mutation", ["missing_manifest", "malformed_json", "duplicate_key", "unknown_schema",
    "unsafe_manifest", "stale_spec", "fake_seal_commit", "missing_review", "stale_review", "fake_review_commit",
    "missing_acceptance", "stale_acceptance", "unaccepted_review", "wrong_acceptance_packet"])
def test_missing_stale_and_unaccepted_evidence_fails_closed(packet, mutation):
    root, admission = packet["root"], packet["admission"]
    if mutation == "missing_manifest":
        report = prospective.evaluate("MISSING.json")
    elif mutation in ("malformed_json", "duplicate_key"):
        text = "{" if mutation == "malformed_json" else '{"schema":1,"schema":1}'
        put(root, "ADMISSION.json", text)
        report = prospective.evaluate("ADMISSION.json")
    elif mutation == "unsafe_manifest":
        report = prospective.evaluate("../ADMISSION.json")
    else:
        if mutation == "unknown_schema":
            admission["schema"] = True
        elif mutation == "stale_spec":
            admission["specification"]["sha256"] = "0" * 64
        elif mutation == "fake_seal_commit":
            admission["sealed_commit"] = "0" * 40
        elif mutation == "missing_review":
            admission["review"]["path"] = "fixture/ABSENT.json"
        elif mutation == "stale_review":
            admission["review"]["sha256"] = "0" * 64
        elif mutation == "fake_review_commit":
            admission["review"]["commit"] = "0" * 40
        elif mutation == "missing_acceptance":
            admission.pop("acceptance")
        elif mutation == "stale_acceptance":
            admission["acceptance"]["sha256"] = "0" * 64
        elif mutation == "unaccepted_review":
            git(root, "update-ref", prospective.RECEIVER_REF, admission["sealed_commit"])
        elif mutation == "wrong_acceptance_packet":
            packet["acceptance"]["experiment_id"] = "someone_else"
            rereview(packet)
        report = inspect(packet)
    assert not report["prospective_admissible"] and report["errors"], report


@pytest.mark.parametrize("mutation", ["self_review", "denied_nonauthorship", "incomplete_sources", "objection",
    "halt", "wrong_seal", "wrong_spec", "independence_unverified", "completeness_unverified", "wrong_receiver"])
def test_review_attestations_and_receiver_binding_are_required(packet, mutation):
    review, acceptance = packet["review"], packet["acceptance"]
    if mutation == "self_review":
        review["reviewer"] = packet["spec"]["authors"][0]
    elif mutation == "denied_nonauthorship":
        review["nonauthoring"] = False
    elif mutation == "incomplete_sources":
        review["source_complete"] = False
    elif mutation == "objection":
        review["unresolved"] = ["Unpinned imported source"]
    elif mutation == "halt":
        review["decision"] = "HALT"
    elif mutation == "wrong_seal":
        review["sealed_commit"] = "0" * 40
    elif mutation == "wrong_spec":
        review["specification"] = {"path": "fixture/OTHER.json", "sha256": "0" * 64}
    elif mutation == "independence_unverified":
        acceptance["verified_independence"] = False
    elif mutation == "completeness_unverified":
        acceptance["verified_source_completeness"] = False
    elif mutation == "wrong_receiver":
        acceptance["receiver"] = "design_author"
    rereview(packet)
    report = inspect(packet)
    assert not report["prospective_admissible"] and report["errors"], report


@pytest.mark.parametrize("mutation", ["empty_field", "missing_field", "missing_seal", "unknown_role",
    "duplicate_source", "missing_test", "undeclared_entrypoint", "unlisted_environment", "unsafe_output",
    "existing_output", "output_at_seal", "stale_source", "uncommitted_source", "symlink_source"])
def test_sealed_source_complete_specification_is_required(packet, mutation):
    root, spec = packet["root"], packet["spec"]
    if mutation in ("empty_field", "missing_field"):
        text = "BANKED IDENTITY:\nPRIOR ART: source read\n" if mutation == "empty_field" else "PRIOR ART: source read\n"
        put(root, spec["design"]["path"], text)
    elif mutation == "unknown_role":
        spec["artifacts"][0]["role"] = "forgiven"
    elif mutation == "duplicate_source":
        spec["artifacts"].append(deepcopy(spec["artifacts"][0]))
    elif mutation == "missing_test":
        spec["artifacts"] = [p for p in spec["artifacts"] if p["role"] != "test"]
    elif mutation == "undeclared_entrypoint":
        spec["commands"][0]["entrypoint"] = "fixture/OTHER.py"
    elif mutation == "unlisted_environment":
        spec["artifacts"] = [p for p in spec["artifacts"] if p["role"] != "input"]
    elif mutation == "unsafe_output":
        spec["outputs"] = ["../escape.json"]
    elif mutation in ("existing_output", "output_at_seal"):
        put(root, spec["outputs"][0], "original result must not be overwritten")
    elif mutation in ("stale_source", "uncommitted_source"):
        put(root, "fixture/probe.py", "print('changed source')\n")
    elif mutation == "symlink_source":
        target = root / "fixture/probe.py"
        target.unlink()
        target.symlink_to("check.py")
    if mutation not in ("existing_output", "stale_source", "uncommitted_source", "symlink_source"):
        reseal(packet)
        rereview(packet)
    elif mutation in ("stale_source", "symlink_source"):
        commit(root, "changed source remains inadmissible")
    if mutation == "missing_seal":
        put(root, "docs/SEAL_LEDGER.md", "")
        commit(root, "remove current seal fixture")
    if mutation == "output_at_seal":
        git(root, "rm", "--", spec["outputs"][0])
        commit(root, "remove current output but not its sealed history")
    report = inspect(packet)
    assert not report["prospective_admissible"] and report["errors"], report


def test_another_governance_failure_blocks_an_otherwise_admitted_packet(packet):
    report = inspect(packet)
    assert report["prospective_admissible"], report
    (packet["root"] / "fixture/probe.py").unlink()
    commit(packet["root"], "missing source also trips separate gate")
    report = inspect(packet)
    assert not report["prospective_admissible"]
    assert any("other governance failures: fixture-source" in e for e in report["errors"])


def test_invalid_historical_policy_is_not_a_waiver(packet):
    put(packet["root"], policy.ROLE_POLICY, "{}")
    commit(packet["root"], "malformed historical policy fixture")
    report = inspect(packet)
    assert not report["prospective_admissible"]
    assert "historical seal register unavailable or invalid" in report["errors"]


def test_actual_command_reports_scope_and_does_not_execute(packet, monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["prospective.py", "--admission", "ADMISSION.json"])
    assert prospective.main() == 0
    report = json.loads(capsys.readouterr().out)
    assert report["prospective_admissible"] and not report["global_compliant"]
    assert report["packet"]["experiment_id"] == packet["spec"]["experiment_id"]
    assert not (packet["root"] / packet["spec"]["outputs"][0]).exists()
