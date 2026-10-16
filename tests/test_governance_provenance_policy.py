"""Positive and rejecting controls for the actual governance entry points."""
import base64
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "gates"))
import gates
import provenance_policy as policy


def put(root, path, data):
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data.encode() if isinstance(data, str) else data)
    return {"path": path, "sha256": hashlib.sha256(target.read_bytes()).hexdigest()}


def write_policy(root, name, records):
    return put(root, name, json.dumps({"schema": 1, "authority": "isolated test fixture",
                                      "records": records}))


@pytest.fixture
def repo(tmp_path, monkeypatch):
    def git(*args):
        result = subprocess.run(["git", "-C", str(tmp_path), *args], capture_output=True,
                                text=True, check=False)
        return result.returncode, result.stdout
    assert git("init", "-q")[0] == 0
    assert git("-c", "user.name=originaxiom", "-c", "user.email=test@example.invalid",
               "commit", "-q", "--allow-empty", "-m", "fixture")[0] == 0
    monkeypatch.setattr(gates, "ROOT", str(tmp_path))
    monkeypatch.setattr(gates, "_ATTR_BASELINE", {})
    write_policy(tmp_path, policy.ROLE_POLICY, [])
    write_policy(tmp_path, policy.REF_POLICY, [])
    put(tmp_path, "docs/SEAL_LEDGER.md", "")
    return tmp_path, git


def seal(root, path):
    put(root, "docs/SEAL_LEDGER.md", f"| 2026-10-16 | fixture | `{path}` |\n")


def source_record(root, role="source", path="fixture/probe.py", text="x = 1\n"):
    artifact = put(root, path, text)
    evidence = put(root, "fixture/INPUTS.json", json.dumps({"source_files": [artifact]}))
    row = {**artifact, "role": role, "reason": "reviewed fixture role",
           "evidence": {**evidence, "collection": "source_files"}}
    write_policy(root, policy.ROLE_POLICY, [row])
    seal(root, path)
    return row


@pytest.mark.parametrize("role,path,text", [
    ("source", "fixture/probe.py", "x = 1\n"),
    ("data", "fixture/results.json", '{"value": 1}'),
])
def test_explicit_pinned_source_and_data_pass_actual_gate(repo, role, path, text):
    root, _ = repo
    source_record(root, role, path, text)
    ok, report = gates.gate_seal_provenance()
    assert ok and report["counts"][role] == 1 and report["problems"] == []


def test_unknown_role_is_not_an_extension_inference(repo):
    root, _ = repo
    put(root, "fixture/probe.py", "x = 1\n")
    seal(root, "fixture/probe.py")
    ok, report = gates.gate_seal_provenance()
    assert not ok and report["problems"][0]["status"] == "unclassified"


@pytest.mark.parametrize("mutation", ["target", "evidence", "missing_pin", "duplicate_pin",
                                         "unknown_collection", "unknown_role", "duplicate_role"])
def test_invalid_role_evidence_rejected(repo, mutation):
    root, _ = repo
    row = source_record(root)
    if mutation == "target":
        put(root, row["path"], "x = 2\n")
    elif mutation == "evidence":
        put(root, row["evidence"]["path"], "{}")
    elif mutation in {"missing_pin", "duplicate_pin"}:
        pins = [] if mutation == "missing_pin" else [
            {"path": row["path"], "sha256": row["sha256"]}] * 2
        ev = put(root, row["evidence"]["path"], json.dumps({"source_files": pins}))
        row["evidence"].update(ev)
    elif mutation == "unknown_collection":
        row["evidence"]["collection"] = "incidental_text"
    elif mutation == "unknown_role":
        row["role"] = "forgiven"
    records = [row, deepcopy(row)] if mutation == "duplicate_role" else [row]
    write_policy(root, policy.ROLE_POLICY, records)
    ok, detail = gates.gate_seal_provenance()
    assert not ok and "policy invalid" in detail


@pytest.mark.parametrize("path,text", [
    ("fixture/DESIGN.md", "intent"),
    ("fixture/PREREG.py", "x = 1"),
    ("fixture/results.json", 'PREREGISTRATION: future experiment'),
    ("fixture/probe.py", '# BANKED IDENTITY: intentional design'),
])
def test_design_cannot_be_disguised_as_pinned_source_or_data(repo, path, text):
    root, _ = repo
    source_record(root, "source", path, text)
    ok, detail = gates.gate_seal_provenance()
    assert not ok and "design cannot be source/data" in detail


@pytest.mark.parametrize("text,expected", [
    ("BANKED IDENTITY: x\nPRIOR ART: y\n", True),
    ("BANKED IDENTITY: x\n", False),
    ("PRIOR ART: y\n", False),
    ("intent\n", False),
])
def test_design_literal_fields_remain_required(repo, text, expected):
    root, _ = repo
    put(root, "fixture/DESIGN.md", text)
    seal(root, "fixture/DESIGN.md")
    ok, _ = gates.gate_seal_provenance()
    assert ok is expected


def test_recorded_historical_violation_remains_failing(repo):
    root, _ = repo
    artifact = put(root, "fixture/OLD.md", "Original historical text, not amended.\n")
    ev = put(root, "fixture/REVIEW.txt", "Missing original literal fields.\n")
    row = {**artifact, "role": "historical_violation", "reason": "record, not forgive", "evidence": ev}
    write_policy(root, policy.ROLE_POLICY, [row])
    seal(root, artifact["path"])
    ok, report = gates.gate_seal_provenance()
    assert not ok and report["problems"][0]["status"] == "historical_noncompliant"
    assert (root / artifact["path"]).read_text() == "Original historical text, not amended.\n"


@pytest.mark.parametrize("which", [policy.ROLE_POLICY, policy.REF_POLICY])
@pytest.mark.parametrize("bad", [None, "{}", '{"schema":1,"schema":1}',
                                '{"schema":2,"authority":"x","records":[]}'])
def test_missing_and_malformed_policies_fail_closed(repo, which, bad):
    root, _ = repo
    if bad is None:
        (root / which).unlink()
    else:
        put(root, which, bad)
    fn = gates.gate_seal_provenance if which == policy.ROLE_POLICY else gates.gate_attribution
    ok, detail = fn()
    assert not ok and "policy invalid" in detail


def ref_record(root, git):
    # Construct the hunted test token without making this file an attribution exception.
    token = base64.b64decode("Y2xhdWRl").decode()
    ref = ("origin/" + token + "/fixture").encode()
    commit = git("rev-parse", "HEAD")[1].strip()
    data = b"UTF-8 prefix: \xce\xbb\n" + ref + b" " + commit.encode() + b"\n"
    pin = put(root, "fixture/capture.txt", data)
    start = data.index(ref)
    evidence = {**pin, "start": start, "end": len(data), "abbreviation": commit}
    span = {"start": start, "end": start + len(ref), "ref_b64": base64.b64encode(ref).decode(),
            "commit": commit, "evidence": evidence}
    row = {**pin, "refs": [span]}
    write_policy(root, policy.REF_POLICY, [row])
    assert git("add", "--", pin["path"])[0] == 0
    return row, token


def test_exact_git_reference_passes_actual_gate_with_utf8_prefix(repo):
    root, git = repo
    row, _ = ref_record(root, git)
    ok, detail = gates.gate_attribution()
    assert ok, detail
    assert len(policy.git_reference_spans(root, git, gates._VENDOR_RE)[row["path"]]) == 1


def test_ref_name_can_use_another_capture_without_reconstructing_its_old_tip(repo):
    root, git = repo
    row, _ = ref_record(root, git)
    span = row["refs"][0]
    old = (root / row["path"]).read_bytes()
    later = put(root, "fixture/later.txt", old)
    span["evidence"].update(later)
    literal = base64.b64decode(span["ref_b64"])
    row.update(put(root, row["path"], b"Known reference: " + literal + b"\n"))
    span.update(start=17, end=17 + len(literal))
    write_policy(root, policy.REF_POLICY, [row])
    ok, detail = gates.gate_attribution()
    assert ok, detail
    assert span["evidence"]["path"] != row["path"]


@pytest.mark.parametrize("mutation", ["stale_file", "stale_evidence", "fake_commit", "wrong_commit",
    "bad_range", "range_too_wide", "overlap", "duplicate_file", "unbound_ref", "bad_ref_syntax"])
def test_reference_exception_rejects_invalid_evidence(repo, mutation):
    root, git = repo
    row, token = ref_record(root, git)
    span = row["refs"][0]
    if mutation == "stale_file":
        put(root, row["path"], (root / row["path"]).read_bytes() + b"x")
    elif mutation == "stale_evidence":
        span["evidence"]["sha256"] = "0" * 64
    elif mutation == "fake_commit":
        span["commit"] = "0" * 40
    elif mutation == "wrong_commit":
        assert git("-c", "user.name=originaxiom", "-c", "user.email=test@example.invalid",
                   "commit", "-q", "--allow-empty", "-m", "second")[0] == 0
        span["commit"] = git("rev-parse", "HEAD")[1].strip()
    elif mutation == "bad_range":
        span["start"] = -1
    elif mutation == "range_too_wide":
        span["end"] += 1
    elif mutation == "overlap":
        row["refs"].append(deepcopy(span))
    elif mutation == "unbound_ref":
        span["evidence"]["end"] = span["end"]
    elif mutation == "bad_ref_syntax":
        literal = ("origin/" + token + "/bad..ref").encode()
        data = literal + b" " + span["commit"].encode()
        row.update(put(root, row["path"], data))
        span.update(start=0, end=len(literal), ref_b64=base64.b64encode(literal).decode())
        span["evidence"].update({**row, "start": 0, "end": len(data)})
        span["evidence"].pop("refs")
    rows = [row, deepcopy(row)] if mutation == "duplicate_file" else [row]
    write_policy(root, policy.REF_POLICY, rows)
    ok, detail = gates.gate_attribution()
    assert not ok and "policy invalid" in detail


def test_credit_outside_reference_is_not_exempted_even_with_a_fresh_file_pin(repo):
    root, git = repo
    row, token = ref_record(root, git)
    data = (root / row["path"]).read_bytes() + ("Author: " + token + "\n").encode()
    row.update(put(root, row["path"], data))
    row["refs"][0]["evidence"]["sha256"] = row["sha256"]
    write_policy(root, policy.REF_POLICY, [row])
    ok, detail = gates.gate_attribution()
    assert not ok and "1 vendor tokens, baseline 0" in str(detail)


def test_substring_of_a_larger_reference_is_rejected(repo):
    root, git = repo
    row, _ = ref_record(root, git)
    span = row["refs"][0]
    old = (root / row["path"]).read_bytes()
    data = old[:span["start"]] + b"X" + old[span["start"]:]
    row.update(put(root, row["path"], data))
    span["start"] += 1
    span["end"] += 1
    span["evidence"].update(sha256=row["sha256"], start=span["start"], end=len(data))
    write_policy(root, policy.REF_POLICY, [row])
    ok, detail = gates.gate_attribution()
    assert not ok and "substring" in detail


def test_whole_document_cannot_replace_a_bounded_reference_passage(repo):
    root, git = repo
    row, _ = ref_record(root, git)
    data = (root / row["path"]).read_bytes() + b" " * 4096
    row.update(put(root, row["path"], data))
    row["refs"][0]["evidence"].update(sha256=row["sha256"], end=len(data))
    write_policy(root, policy.REF_POLICY, [row])
    ok, detail = gates.gate_attribution()
    assert not ok and "too broad" in detail


def test_git_failure_does_not_silently_skip_attribution(repo, monkeypatch):
    monkeypatch.setattr(gates, "_git", lambda *args: (1, "unavailable"))
    ok, detail = gates.gate_attribution()
    assert not ok and "cannot be verified" in detail


@pytest.mark.parametrize("path", ["../escape.txt", "/absolute.txt", "fixture/../escape.txt"])
def test_evidence_paths_cannot_escape_repository(repo, path):
    root, _ = repo
    with pytest.raises(policy.PolicyError):
        policy._bytes(root, path)
