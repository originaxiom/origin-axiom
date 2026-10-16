"""Read-only admission for one prospective experiment; global history is not waived.

This checks exact evidence bindings, not the truth of reviewer attestations.
The receiving seat must verify identity, independence and source completeness.
It does not launch code or replace the ordinary repository compliance aggregate.
"""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess

try:
    from . import gates, provenance_policy as policy
except ImportError:
    import gates
    import provenance_policy as policy

RECEIVER_REF = "refs/remotes/origin/main"
COMMIT = re.compile(r"[0-9a-f]{40}\Z")


def require(condition, message):
    policy._require(condition, message)


def shape(value, keys, label):
    require(isinstance(value, dict) and set(value) == set(keys), "invalid " + label)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def path_name(rel):
    require(nonempty(rel) and "\\" not in rel and not any(ord(c) < 32 for c in rel),
            "invalid path")
    path = PurePosixPath(rel)
    require(not path.is_absolute() and str(path) == rel
            and all(p not in ("", ".", "..") for p in rel.split("/")), "unsafe path")
    return rel


def git(root, *args):
    out = subprocess.run(["git", "-C", str(root), *args], capture_output=True, timeout=30)
    require(out.returncode == 0, "Git evidence unavailable: " + args[0])
    return out.stdout


def commit_id(root, value):
    require(isinstance(value, str) and COMMIT.fullmatch(value), "full commit pin required")
    require(git(root, "rev-parse", "--verify", value + "^{commit}").strip().decode() == value,
            "commit mismatch")
    return value


def blob(root, commit, rel):
    path_name(rel)
    entry = git(root, "ls-tree", "-z", commit, "--", rel).split(b"\0")
    require(len(entry) == 2 and entry[-1] == b"", "missing or ambiguous committed file: " + rel)
    meta, name = entry[0].split(b"\t", 1)
    require(name.decode() == rel and meta.split()[0] in (b"100644", b"100755"),
            "nonregular committed file: " + rel)
    return git(root, "show", commit + ":" + rel)


def pin(root, row, commit, current=False):
    shape(row, ("path", "sha256"), "pin")
    rel = path_name(row["path"])
    require(isinstance(row["sha256"], str) and policy.SHA.fullmatch(row["sha256"]),
            "invalid SHA256")
    data = blob(root, commit, rel)
    require(hashlib.sha256(data).hexdigest() == row["sha256"], "committed pin mismatch: " + rel)
    if current:
        require(policy._bytes(root, rel) == data, "current source differs: " + rel)
    return data


def has_seal(ledger, row):
    latest = {}
    for line in ledger.decode("utf-8").splitlines():
        match = re.match(r"\|\s*\d{4}-\d{2}-\d{2}\s*\|[^|]*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`", line)
        if match:
            latest[match[1]] = match[2]
    require(latest.get(row["path"]) == row["sha256"], "matching seal missing: " + row["path"])


def inspect_admission(root, rel):
    """Bind one specification, separately committed review and main acceptance."""
    root = Path(root).resolve()
    doc = policy._json(policy._bytes(root, path_name(rel)))
    shape(doc, ("schema", "sealed_commit", "specification", "review", "acceptance"), "admission")
    require(type(doc["schema"]) is int and doc["schema"] == 1, "unknown admission schema")
    require(not git(root, "diff", "--name-only", "HEAD", "--").strip(),
            "tracked tree/index must match committed HEAD")
    sealed = commit_id(root, doc["sealed_commit"])
    spec = policy._json(pin(root, doc["specification"], sealed, current=True))
    shape(spec, ("schema", "experiment_id", "authors", "design", "artifacts", "commands",
                 "outputs", "environment"), "specification")
    require(type(spec["schema"]) is int and spec["schema"] == 1, "unknown specification schema")
    require(nonempty(spec["experiment_id"]), "experiment identity required")
    authors = spec["authors"]
    require(isinstance(authors, list) and authors and all(nonempty(a) and a == a.strip() for a in authors)
            and len(authors) == len(set(authors)), "distinct author identities required")
    design = pin(root, spec["design"], sealed, current=True).decode("utf-8")
    for field in policy.FIELDS:
        require(re.search(r"(?m)^" + re.escape(field) + r"[ \t]*[^\s]", design),
                "design missing nonempty literal field: " + field)
    for ledger in (blob(root, sealed, "docs/SEAL_LEDGER.md"),
                   policy._bytes(root, "docs/SEAL_LEDGER.md")):
        has_seal(ledger, spec["design"])
        has_seal(ledger, doc["specification"])
    require(isinstance(spec["artifacts"], list) and spec["artifacts"], "source inventory required")
    paths = {spec["design"]["path"], doc["specification"]["path"]}
    sources, tests, inputs = set(), set(), set()
    for row in spec["artifacts"]:
        shape(row, ("path", "sha256", "role"), "artifact")
        require(row["role"] in ("source", "input", "test"), "unknown artifact role")
        require(row["path"] not in paths, "duplicate artifact")
        pin(root, {k: row[k] for k in ("path", "sha256")}, sealed, current=True)
        paths.add(row["path"])
        {"source": sources, "test": tests, "input": inputs}[row["role"]].add(row["path"])
    require(sources and tests, "source and test inventories required")
    shape(spec["environment"], ("path", "sha256"), "environment pin")
    require(spec["environment"]["path"] in inputs, "environment must be a pinned input")
    pin(root, spec["environment"], sealed, current=True)
    require(isinstance(spec["commands"], list) and spec["commands"], "commands required")
    for command in spec["commands"]:
        shape(command, ("entrypoint", "argv"), "command")
        require(command["entrypoint"] in sources, "undeclared source entrypoint")
        require(isinstance(command["argv"], list) and command["argv"]
                and all(nonempty(x) for x in command["argv"])
                and command["entrypoint"] in command["argv"], "explicit source command required")
    outputs = spec["outputs"]
    require(isinstance(outputs, list) and outputs and all(isinstance(p, str) for p in outputs)
            and len(set(outputs)) == len(outputs), "distinct reserved output paths required")
    for output in outputs:
        path_name(output)
        full = root / output
        require(full.resolve().is_relative_to(root)
                and not any(p.is_symlink() for p in (full, *full.parents) if p != root),
                "unsafe output path")
        require(output not in paths and not full.exists(), "output already exists: " + output)
        require(not git(root, "ls-tree", "-z", sealed, "--", output),
                "output existed at seal: " + output)
    review_ref = doc["review"]
    shape(review_ref, ("commit", "path", "sha256"), "review reference")
    reviewed = commit_id(root, review_ref["commit"])
    require(reviewed != sealed, "review must follow separate sealing")
    review_pin = {k: review_ref[k] for k in ("path", "sha256")}
    review = policy._json(pin(root, review_pin, reviewed))
    shape(review, ("schema", "experiment_id", "sealed_commit", "specification", "reviewer",
                   "nonauthoring", "source_complete", "decision", "unresolved", "scope"), "review")
    require(type(review["schema"]) is int and review["schema"] == 1, "unknown review schema")
    require(review["experiment_id"] == spec["experiment_id"] and review["sealed_commit"] == sealed
            and review["specification"] == doc["specification"], "review binds another specification")
    require(nonempty(review["reviewer"]) and review["reviewer"] == review["reviewer"].strip()
            and review["reviewer"] not in authors and review["nonauthoring"] is True,
            "non-authoring reviewer required")
    require(review["source_complete"] is True and review["decision"] == "APPROVE_EXECUTION"
            and review["unresolved"] == [] and nonempty(review["scope"]), "review does not approve complete sources")
    acceptance_ref = doc["acceptance"]
    shape(acceptance_ref, ("commit", "path", "sha256"), "acceptance reference")
    accepted = commit_id(root, acceptance_ref["commit"])
    require(accepted not in (sealed, reviewed), "acceptance must bind a separate review commit")
    git(root, "merge-base", "--is-ancestor", accepted, RECEIVER_REF)
    acceptance = policy._json(pin(root, {k: acceptance_ref[k] for k in ("path", "sha256")}, accepted))
    shape(acceptance, ("schema", "experiment_id", "sealed_commit", "specification", "review",
                       "receiver", "decision", "verified_independence", "verified_source_completeness"), "acceptance")
    require(type(acceptance["schema"]) is int and acceptance["schema"] == 1, "unknown acceptance schema")
    require(acceptance["experiment_id"] == spec["experiment_id"]
            and acceptance["sealed_commit"] == sealed and acceptance["specification"] == doc["specification"]
            and acceptance["review"] == review_ref, "acceptance binds another packet")
    require(acceptance["receiver"] == "main" and acceptance["decision"] == "ACCEPT_INDEPENDENT_REVIEW"
            and acceptance["verified_independence"] is True
            and acceptance["verified_source_completeness"] is True, "receiver acceptance incomplete")
    return {"experiment_id": spec["experiment_id"], "sealed_commit": sealed,
            "review_commit": reviewed, "acceptance_commit": accepted,
            "commands": spec["commands"], "outputs": outputs}


def evaluate(admission, root=None):
    """Historical seal failures stay visible; any other governance failure blocks."""
    root = root or gates.ROOT
    results = gates.run_all()
    history = results.get("seal-provenance", (False, None))[1]
    historical_valid = (isinstance(history, dict) and set(history) == {"counts", "problems"}
                        and isinstance(history["counts"], dict) and isinstance(history["problems"], list))
    failures = [name for name, (ok, _) in results.items() if name != "seal-provenance" and not ok]
    errors, packet = [], None
    if not historical_valid:
        errors.append("historical seal register unavailable or invalid")
    if failures:
        errors.append("other governance failures: " + ", ".join(failures))
    try:
        packet = inspect_admission(root, admission)
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as exc:
        errors.append(str(exc))
    return {"prospective_admissible": not errors, "global_compliant": all(ok for ok, _ in results.values()),
            "historical_seal_report": history, "governance": results, "packet": packet, "errors": errors,
            "limits": "Evidence binding only; main verifies independence and completeness. No execution or scientific certification."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--admission", required=True, help="repository-relative admission JSON")
    args = parser.parse_args()
    report = evaluate(args.admission)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["prospective_admissible"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
