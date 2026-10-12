"""Replay exact handoff bytes in NEW scratch; do not import science producers.

Resource/runner failures are not mathematical counterexamples. Output is
outside the repository by default. Original files/results are never edited.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
import zipfile

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def stamp():
    return datetime.now(timezone.utc).isoformat()


def git(*args):
    return subprocess.check_output(["git", *args], cwd=REPO).decode().strip()


def file_state():
    names = subprocess.check_output(["git", "ls-files", "-z"], cwd=REPO)
    return {name.decode(): sha((REPO / name.decode()).read_bytes())
            for name in names.split(b"\0") if name}


def require(value, message):
    if not value:
        raise RuntimeError(message)


def validate(label, data):
    """Check named predicates, not merely an author-provided PASS label."""
    expected_exact = {"gate1_primary": 57, "gate1_reference": 17,
                      "gate2_exact": 50, "gate3_exact": 43}
    if label in expected_exact:
        checks = data["checks"]
        require(len(checks) == expected_exact[label], "exact check population")
        require(all(v is True for v in checks.values()), "exact false predicate")
        return {"exact_predicates": len(checks)}
    if label.startswith("gate2_reference_"):
        exact, numeric = data["exact_checks"], data["numerical_checks"]
        require(len(exact) == 8 and len(numeric) == 48, "Gate2 population")
        require(all(v is True for v in exact.values()), "Gate2 exact false")
        require(all(v["passed"] is True for v in numeric), "Gate2 numeric false")
        require(len({v["name"] for v in numeric}) == 48, "Gate2 duplicate name")
        require(data["precision_digits"] == int(label.rsplit("_", 1)[1]),
                "Gate2 precision mismatch")
        return {"exact_predicates": 8, "numerical_checks": 48,
                "max_normalized_residual": data["max_normalized_residual"]}
    require(label == "gate3_numerical_50", "unknown command label")
    checks = data["checks"]
    require(len(checks) == 72 and data["total_checks"] == 72, "Gate3 population")
    require(data["strict_count"] == 64 and data["finite_limit_count"] == 8,
            "Gate3 strict/limit population")
    require(data["dps"] == 50, "Gate3 precision mismatch")
    require(all(v["pass"] is True for v in checks.values()), "Gate3 false")
    return {"numerical_checks": 72, "strict_checks": 64, "finite_limits": 8,
            "max_strict_residual": data["max_strict_residual"],
            "max_finite_limit_residual": data["max_finite_limit_residual"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        help="must be a NEW absolute directory outside the repo")
    args = parser.parse_args()
    if args.output is None:
        out = Path(tempfile.mkdtemp(prefix="oa-joining-replay-"))
    else:
        out = args.output.resolve()
        require(out != REPO and REPO not in out.parents, "output inside repository")
        out.mkdir(parents=True, exist_ok=False)
    print(f"OUTPUT_DIRECTORY={out}", flush=True)
    receipt = {"started_utc": stamp(), "status": "IN_PROGRESS",
               "commands": [], "output_directory": str(out),
               "scope": "unchanged-instrument replay; no global physical acceptance"}
    initial = None
    try:
        require(__debug__, "optimized Python execution forbidden")
        require(not git("status", "--porcelain"), "working tree must be clean")
        import sympy
        import mpmath
        environment = {"python": platform.python_version(),
                       "sympy": sympy.__version__, "mpmath": mpmath.__version__}
        require(environment == {"python": "3.12.1", "sympy": "1.14.0",
                                "mpmath": "1.3.0"}, "unsealed dependency environment")
        receipt.update(environment=environment, executable=sys.executable,
                       seal_commit=git("rev-parse", "HEAD"),
                       branch=git("branch", "--show-current"),
                       runner_sha256=sha(Path(__file__).read_bytes()),
                       inputs_sha256=sha((HERE / "INPUTS.json").read_bytes()),
                       design_sha256=sha((HERE / "DESIGN.md").read_bytes()))
        initial = file_state()
        inputs = json.loads((HERE / "INPUTS.json").read_text())
        archive = REPO / inputs["archive_path"]
        raw = archive.read_bytes()
        require(len(raw) == inputs["archive_bytes"] and
                sha(raw) == inputs["archive_sha256"], "archive custody mismatch")
        candidate = (REPO / inputs["repository_candidate_path"]).read_bytes()
        require(sha(candidate) == inputs["candidate_sha256"], "candidate mismatch")
        blob = hashlib.sha1(b"blob " + str(len(candidate)).encode() + b"\0" + candidate).hexdigest()
        require(blob == inputs["candidate_git_blob"], "candidate Git blob mismatch")
        with zipfile.ZipFile(archive) as z:
            for row in inputs["members"]:
                data = z.read(row["member"])
                require(len(data) == row["bytes"] and sha(data) == row["sha256"],
                        f"member custody mismatch: {row['member']}")
                target = out / row["destination"]
                require(out in target.resolve().parents, "unsafe target")
                target.parent.mkdir(parents=True, exist_ok=True)
                with target.open("xb") as f:
                    f.write(data)
                if target.name == "candidate.json":
                    require(data == candidate, "candidate copies differ")
        commands = [
            ("gate1_primary", "gate1", "verify_bridge.py", []),
            ("gate1_reference", "gate1", "verify_reference.py", []),
            ("gate2_exact", "gate2", "verify_exact.py", []),
            ("gate2_reference_50", "gate2", "verify_reference.py", ["--dps", "50"]),
            ("gate2_reference_80", "gate2", "verify_reference.py", ["--dps", "80"]),
            ("gate3_exact", "gate3", "verify_exact.py", []),
            ("gate3_numerical_50", "gate3", "verify_numerical.py", ["--dps", "50"]),
        ]
        for label, group, name, extra in commands:
            cmd = [sys.executable, "-u", str(out / group / name), *extra]
            run = {"label": label, "command": cmd, "started_utc": stamp(),
                   "timeout_seconds": 900, "status": "IN_PROGRESS"}
            receipt["commands"].append(run)
            print(f"START {label}", flush=True)
            (out / "RUN_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n")
            started = time.monotonic()
            env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
            env.pop("PYTHONOPTIMIZE", None)
            env.pop("PYTHONPATH", None)
            with (out / f"{label}.stdout.log").open("xb") as stdout, \
                    (out / f"{label}.stderr.log").open("xb") as stderr:
                try:
                    process = subprocess.run(cmd, cwd=out / group, env=env,
                                             stdout=stdout, stderr=stderr, timeout=900)
                except subprocess.TimeoutExpired:
                    run.update(status="RESOURCE_UNKNOWN", elapsed_seconds=time.monotonic()-started,
                               finished_utc=stamp())
                    raise RuntimeError(f"resource cap: {label}")
            run.update(exit_code=process.returncode, elapsed_seconds=time.monotonic()-started,
                       finished_utc=stamp())
            require(process.returncode == 0, f"nonzero exit: {label}")
            data = json.loads((out / f"{label}.stdout.log").read_text())
            run.update(validate(label, data), status="PASS")
            print(f"PASS {label} ({run['elapsed_seconds']:.2f}s)", flush=True)
        for row in inputs["members"]:
            require(sha((out / row["destination"]).read_bytes()) == row["sha256"],
                    "executed source changed")
        require(file_state() == initial, "tracked worktree changed during execution")
        require(not git("status", "--porcelain"), "dirty tree during execution")
        receipt["status"] = "REPRODUCED"
        receipt["tracked_worktree_unchanged"] = True
        receipt["executed_sources_unchanged"] = True
    except Exception as exc:
        receipt["error"] = f"{type(exc).__name__}: {exc}"
        receipt["status"] = "STOPPED_NOT_A_PROGRAM_KILL"
        if receipt["commands"] and receipt["commands"][-1]["status"] == "IN_PROGRESS":
            receipt["commands"][-1]["status"] = "FAILED_REPRODUCTION_OR_RUNNER"
        if initial is not None:
            receipt["tracked_worktree_unchanged"] = file_state() == initial
        print(receipt["error"], flush=True)
    finally:
        receipt["finished_utc"] = stamp()
        receipt["files"] = [
            {"path": str(p.relative_to(out)), "bytes": p.stat().st_size,
             "sha256": sha(p.read_bytes())}
            for p in sorted(out.rglob("*"))
            if p.is_file() and p.name != "RUN_RECEIPT.json"
        ]
        (out / "RUN_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n")
        print(f"FINAL_STATUS={receipt['status']}", flush=True)
    return 0 if receipt["status"] == "REPRODUCED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
