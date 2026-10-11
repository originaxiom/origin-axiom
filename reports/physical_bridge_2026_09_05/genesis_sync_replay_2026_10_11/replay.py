"""Custody-first replay of five unchanged, pinned genesis producers."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
spec = json.loads((HERE / "SOURCES.json").read_text())
source = Path(sys.argv[1]).resolve()
head = subprocess.check_output(["git", "-C", str(source), "rev-parse", "HEAD"], text=True).strip()
assert head == spec["source_commit"], ("wrong source HEAD", head)
for row in spec["source_files"]:
    data = (source / row["path"]).read_bytes()
    assert len(data) == row["bytes"], ("size", row["path"])
    assert hashlib.sha256(data).hexdigest() == row["sha256"], ("hash", row["path"])
print("PASS source custody:", len(spec["source_files"]), "pinned files", flush=True)
base = "reports/genesis_root_review_2026_10_11/"
env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", LC_ALL="C", LANG="C")
jobs = [
    ("word_lifts/verify.py", 4133, "checks"),
    ("bundle_transport/verify.py", 371, "exact_checks"),
    ("positive_carrier/verify.py", 8234, None),
    ("cohomology_carrier/verify_v2.py", 3626, None),
    ("cusp_connection/verify.py", 136, None),
]
for path, expected, key in jobs:
    print("RUN unchanged producer:", path, flush=True)
    result = subprocess.run([sys.executable, str(source / base / path)],
                            cwd=source, env=env, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    sys.stdout.buffer.write(result.stdout)
    sys.stdout.flush()
    assert result.returncode == 0, ("producer exit", path, result.returncode)
    if key is not None:
        parsed = json.loads(result.stdout)
        assert parsed["status"] == "PASS" and parsed[key] == expected, ("count/status", path)
    else:
        first = result.stdout.decode().splitlines()[0]
        assert first.startswith("PASS: "+str(expected)+" exact "), ("count/status", path, first)
print("PASS all five unchanged producers; no full-suite or physical identification certificate.", flush=True)

