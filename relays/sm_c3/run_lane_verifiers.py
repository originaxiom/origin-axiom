#!/usr/bin/env python3
"""SM-C3: run the fork lane's five verifiers once, as found, and compare their output with what the lane recorded.

The folder reports/genesis_root_review_2026_10_11 is read from the commit below as git objects (git archive) into a
fresh temporary directory; the run refuses if any member's path contains agy_. Each verifier is run from the
extraction's root with the lane's own recorded command (its EXECUTION_RECEIPT.json), with the interpreter named
python3 and -I -B added. The extraction's path in any traceback is replaced by <repo>, as the lane's own public copy
does; the lines of carets and tildes that mark a traceback's failing expression depend on the interpreter's minor version, so a failed
run is also compared with them left out.
By the card (section 2), these runs are facts about the lane's code, not checks of its claims.
Usage: run_lane_verifiers.py <output.json>   (run from inside a clone that has the commit)."""
import difflib
import hashlib
import io
import json
import os
import platform
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time
from pathlib import Path

COMMIT = "0c6570bab3de4c013b73afb206cf80c4f56ccb1a"
ROOT = "reports/genesis_root_review_2026_10_11"
RUNS = [  # (packet, verifier, the lane's recorded output it is compared with)
    ("matter_line_compatibility", "verify.py", "NATIVE_FIRST.json"),
    ("puncture_symmetry", "verify.py", "NATIVE_FIRST.json"),
    ("positive_carrier", "verify.py", "NATIVE_FIRST.txt"),
    ("cohomology_carrier", "verify.py", "NATIVE_FIRST_PUBLIC.txt"),
    ("cohomology_carrier", "verify_v2.py", "NATIVE_SECOND.txt"),
]
sha = lambda b: hashlib.sha256(b).hexdigest()
strip_carets = lambda b: [ln for ln in b.decode().splitlines() if ln.strip(" ^~")]  # traceback marker lines


def main(out_path):
    tar_bytes = subprocess.run(["git", "archive", "--format=tar", COMMIT, ROOT], check=True,
                               capture_output=True).stdout
    with tarfile.open(fileobj=io.BytesIO(tar_bytes)) as tf:
        names = tf.getnames()
        bad = [n for n in names if "agy_" in n]
        if bad:
            raise SystemExit(f"refused: {len(bad)} member paths contain agy_")
        work = tempfile.mkdtemp(prefix="sm_c3_lane_")
        tf.extractall(work, filter="data")
    env = {"LC_ALL": "C", "LANG": "C", "PYTHONDONTWRITEBYTECODE": "1", "PATH": os.environ.get("PATH", "")}
    rows = []
    for packet, verifier, recorded in RUNS:
        rel = f"{ROOT}/{packet}/{verifier}"
        cmd = [sys.executable, "-I", "-B", "-u", rel]
        t0 = time.time()
        p = subprocess.run(cmd, cwd=work, env=env, capture_output=True, timeout=3600)
        secs = round(time.time() - t0, 1)
        stdout, stderr = p.stdout, p.stderr.replace(work.encode(), b"<repo>")
        rec = (Path(work) / ROOT / packet / recorded).read_bytes()
        shown = stdout if p.returncode == 0 else stderr
        rows.append({
            "packet": packet, "verifier": verifier,
            "verifier_sha256": sha((Path(work) / rel).read_bytes()),
            "command": "LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 python3 -I -B -u " + rel,
            "exit": p.returncode, "seconds": secs,
            "stdout_sha256": sha(stdout), "stdout_bytes": len(stdout),
            "stderr_sha256": sha(stderr), "stderr_bytes": len(stderr),
            "recorded_file": recorded, "recorded_sha256": sha(rec),
            "identical_to_recorded": shown == rec,
            "identical_ignoring_caret_only_lines": strip_carets(shown) == strip_carets(rec),
            "last_lines": (stdout if p.returncode == 0 else stderr).decode().strip().splitlines()[-3:],
            "stderr_text_if_failed": stderr.decode() if p.returncode else "",
            "diff_if_not_identical": [] if shown == rec else [
                ln for ln in difflib.unified_diff(rec.decode().splitlines(), shown.decode().splitlines(),
                                                  "recorded", "this_run", lineterm="", n=0)],
        })
    result = {"commit": COMMIT, "folder": ROOT, "members_extracted": len(names), "members_with_agy_": 0,
              "python": platform.python_version(), "sympy": __import__("sympy").__version__,
              "runs": rows}
    shutil.rmtree(work)
    Path(out_path).write_text(json.dumps(result, indent=1) + "\n", encoding="utf-8")
    for r in rows:
        print(r["packet"], r["verifier"], "exit", r["exit"], "identical", r["identical_to_recorded"], r["last_lines"][-1:])


if __name__ == "__main__":
    main(sys.argv[1])
