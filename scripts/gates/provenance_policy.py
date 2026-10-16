"""Hash-bound governance roles and literal Git provenance; no scientific imports."""
import base64
import hashlib
import json
from pathlib import Path, PurePosixPath
import re

ROLE_POLICY = "docs/SEAL_ARTIFACT_ROLES.json"
REF_POLICY = "docs/GIT_REFERENCE_PROVENANCE.json"
FIELDS = ("BANKED IDENTITY:", "PRIOR ART:")
SHA = re.compile(r"[0-9a-f]{64}\Z")
ROLES = {"source", "data", "preregistration", "historical_violation"}


class PolicyError(ValueError):
    pass


def _require(condition, message):
    if not condition:
        raise PolicyError(message)


def _bytes(root, rel):
    _require(isinstance(rel, str) and rel and "\\" not in rel, "invalid path")
    path = PurePosixPath(rel)
    _require(not path.is_absolute() and all(x not in (".", "..") for x in rel.split("/"))
             and str(path) == rel, "unsafe or noncanonical path")
    base = Path(root).resolve()
    full = base / rel
    _require(full.resolve().is_relative_to(base), "path escapes repository")
    _require(not any(p.is_symlink() for p in (full, *full.parents) if p != base),
             "symlink evidence is not accepted")
    return full.read_bytes()


def _pinned(root, row):
    digest = row.get("sha256")
    _require(isinstance(digest, str) and SHA.fullmatch(digest), "invalid SHA256")
    data = _bytes(root, row.get("path"))
    _require(hashlib.sha256(data).hexdigest() == digest, "stale pin: " + row["path"])
    return data


def _json(data):
    def unique(pairs):
        out = {}
        for key, value in pairs:
            _require(key not in out, "duplicate JSON key: " + key)
            out[key] = value
        return out
    return json.loads(data, object_pairs_hook=unique)


def _records(root, rel):
    doc = _json(_bytes(root, rel))
    _require(isinstance(doc, dict) and set(doc) == {"schema", "authority", "records"},
             "invalid policy envelope")
    _require(type(doc["schema"]) is int and doc["schema"] == 1, "unknown policy schema")
    _require(isinstance(doc["authority"], str) and doc["authority"].strip(),
             "policy authority required")
    _require(isinstance(doc["records"], list), "records must be a list")
    return doc["records"]


def _design_like(rel, data):
    name = PurePosixPath(rel).name.upper()
    text = data.decode("utf-8")
    return ("DESIGN" in name or "PREREG" in name or name.startswith("SEALED")
            or any(field in text for field in FIELDS)
            or re.search(r"(?im)^\s*(?:[#/*\"']+\s*)?(?:preregistration|experimental design)\s*:", text))


def seal_roles(root):
    """Explicit roles are judgments; pins and conservative design guards are mechanical."""
    roles = {}
    for row in _records(root, ROLE_POLICY):
        _require(isinstance(row, dict) and set(row) ==
                 {"path", "sha256", "role", "reason", "evidence"}, "invalid role record")
        rel, role = row["path"], row["role"]
        _require(isinstance(rel, str) and rel not in roles, "duplicate/invalid role path")
        _require(role in ROLES, "unknown role")
        _require(isinstance(row["reason"], str) and row["reason"].strip(), "role reason required")
        data = _pinned(root, row)
        ev = row["evidence"]
        _require(isinstance(ev, dict), "role evidence required")
        if role in {"source", "data"}:
            _require(not _design_like(rel, data), "design cannot be source/data: " + rel)
            _require(set(ev) == {"path", "sha256", "collection"}, "invalid manifest evidence")
            _require(ev["path"] != rel, "self-certifying role evidence")
            manifest = _json(_pinned(root, ev))
            _require(isinstance(manifest, dict), "pin manifest must be an object")
            _require(ev["collection"] in {"source_files", "frozen_paths"}, "unknown pin collection")
            pins = manifest.get(ev["collection"])
            _require(isinstance(pins, list), "missing pin collection")
            matches = [p for p in pins if isinstance(p, dict) and p.get("path") == rel]
            _require(len(matches) == 1 and matches[0].get("sha256") == row["sha256"],
                     "manifest does not uniquely pin role artifact: " + rel)
        else:
            _require(set(ev) == {"path", "sha256"}, "invalid design evidence")
            _pinned(root, ev)
            if role == "historical_violation":
                _require(not all(f in data.decode("utf-8") for f in FIELDS),
                         "historical violation no longer matches its missing-field record")
        roles[rel] = role
    return roles


def seal_report(root, ledger, cutoff):
    roles = seal_roles(root)  # missing/malformed policy is an error, never an empty exemption
    paths = {}
    for line in ledger.splitlines():
        match = re.match(r"\|\s*(\d{4}-\d{2}-\d{2})\s*\|[^|]*\|\s*`([^`]+)`", line)
        if match and match[1] >= cutoff:
            paths[match[2]] = paths.get(match[2], 0) + 1
    problems, counts = [], {"source": 0, "data": 0, "preregistration": 0,
                            "historical_violation": 0, "unknown": 0, "absent_branch": 0}
    for rel in sorted(paths):
        try:
            data = _bytes(root, rel)
        except FileNotFoundError:
            counts["absent_branch"] += 1  # unchanged ledger treatment; disclosed, not certified
            continue
        text = data.decode("utf-8")
        role = roles.get(rel)
        if role is None:
            role = "preregistration" if _design_like(rel, data) else "unknown"
        counts[role] += 1
        if role == "unknown":
            problems.append({"path": rel, "status": "unclassified", "rows": paths[rel]})
        elif role == "historical_violation":
            problems.append({"path": rel, "status": "historical_noncompliant", "rows": paths[rel]})
        elif role == "preregistration":
            missing = [f for f in FIELDS if f not in text]
            if missing:
                problems.append({"path": rel, "status": "missing_fields", "missing": missing,
                                 "rows": paths[rel]})
    return {"counts": counts, "problems": problems}


def _range(data, start, end):
    _require(type(start) is int and type(end) is int and 0 <= start < end <= len(data),
             "invalid byte range")
    return data[start:end]


def git_reference_spans(root, git, vendor_re):
    """Return only reviewed exact spans; Git evidence does not certify historical timing."""
    accepted = {}
    for row in _records(root, REF_POLICY):
        _require(isinstance(row, dict) and set(row) == {"path", "sha256", "refs"},
                 "invalid Git provenance record")
        rel = row["path"]
        _require(isinstance(rel, str) and rel not in accepted, "duplicate/invalid provenance path")
        data = _pinned(root, row)
        _require(isinstance(row["refs"], list) and row["refs"], "empty reference record")
        spans = []
        for ref in row["refs"]:
            _require(isinstance(ref, dict) and set(ref) ==
                     {"start", "end", "ref_b64", "commit", "evidence"}, "invalid reference record")
            literal = base64.b64decode(ref["ref_b64"], validate=True)
            _require(_range(data, ref["start"], ref["end"]) == literal, "reference bytes changed")
            chars = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._/-"
            _require((ref["start"] == 0 or data[ref["start"] - 1] not in chars)
                     and (ref["end"] == len(data) or data[ref["end"]] not in chars),
                     "reference range is only a substring of a larger name")
            name = literal.decode("ascii")
            _require("/" in name and re.fullmatch(r"[A-Za-z0-9._/-]+", name)
                     and vendor_re.search(name), "not a matched literal Git reference")
            check_name = name if name.startswith("refs/") else "refs/heads/" + name
            rc, _ = git("check-ref-format", check_name)
            _require(rc == 0, "invalid Git ref syntax")
            commit = ref["commit"]
            _require(isinstance(commit, str) and re.fullmatch(r"[0-9a-f]{40}", commit),
                     "full commit pin required")
            ev = ref["evidence"]
            _require(isinstance(ev, dict) and set(ev) ==
                     {"path", "sha256", "start", "end", "abbreviation"}, "invalid ref evidence")
            passage = _range(_pinned(root, ev), ev["start"], ev["end"])
            _require(len(passage) <= 4096, "reference evidence passage is too broad")
            abbr = ev["abbreviation"]
            _require(isinstance(abbr, str) and re.fullmatch(r"[0-9a-f]{7,40}", abbr)
                     and commit.startswith(abbr), "invalid captured commit abbreviation")
            _require(literal in passage and re.search(rb"(?<![0-9a-f])" + abbr.encode() +
                     rb"(?![0-9a-f])", passage), "passage does not bind ref and captured commit")
            rc, resolved = git("rev-parse", "--verify", abbr + "^{commit}")
            _require(rc == 0 and resolved.strip() == commit, "commit absent, ambiguous or mismatched")
            _require(all(ref["end"] <= a or ref["start"] >= b for a, b in spans),
                     "overlapping reference ranges")
            spans.append((ref["start"], ref["end"]))
        accepted[rel] = sorted(spans)
    return accepted


def attribution_count(data, vendor_re, spans):
    """Byte offsets remain correct for UTF-8 prefixes. Outside hits are never swallowed."""
    text = data.decode("utf-8")
    count = 0
    for match in vendor_re.finditer(text):
        start = len(text[:match.start()].encode("utf-8"))
        end = len(text[:match.end()].encode("utf-8"))
        if not any(a <= start and end <= b for a, b in spans):
            count += 1
    return count
