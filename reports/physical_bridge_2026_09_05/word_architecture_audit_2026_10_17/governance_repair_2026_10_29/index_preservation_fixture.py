"""Synthetic Git-only preservation check; no scientific imports or data."""
import json
import os
from pathlib import Path
import subprocess
import tempfile


def main():
    root = Path(tempfile.mkdtemp(prefix="oa-index-preservation-fixture-"))

    def git(*args, env=None, data=None):
        result = subprocess.run(["git", "-C", str(root), *args], input=data,
                                capture_output=True, env=env)
        if result.returncode:
            raise RuntimeError(result.stderr.decode())
        return result.stdout

    git("init", "-q")
    git("config", "user.name", "originaxiom")
    git("config", "user.email", "fixture@example.invalid")
    base = b"old row\n" + b"".join(b"context %d\n" % i for i in range(15))
    (root / "ledger.md").write_bytes(base)
    (root / "other.txt").write_bytes(b"base\n")
    git("add", "ledger.md", "other.txt")
    git("commit", "-qm", "base")
    (root / "ledger.md").write_bytes(base + b"user staged row\n")
    (root / "other.txt").write_bytes(b"user staged other\n")
    git("add", "ledger.md", "other.txt")
    (root / "ledger.md").write_bytes(base + b"user staged row\nuser unstaged row\n")

    old_head = git("show", "HEAD:ledger.md")
    old_index = git("show", ":ledger.md")
    old_work = (root / "ledger.md").read_bytes()
    old_other = git("show", ":other.txt")
    old_patch = git("diff", "--cached", "--binary")
    old, new = b"old row\n", b"old row ESCALATED named next action\n"

    def replace_once(data):
        if data.count(old) != 1 or new in data:
            raise ValueError("row missing, ambiguous or already modified")
        return data.replace(old, new, 1)

    rejected = 0
    for bad in [b"row disappeared\n", old + old, new]:
        try:
            replace_once(bad)
        except ValueError:
            rejected += 1
    assert rejected == 3

    alternate_index = root / ".git" / "task-index"
    env = dict(os.environ, GIT_INDEX_FILE=str(alternate_index))
    git("read-tree", "HEAD", env=env)
    head_blob = git("hash-object", "-w", "--stdin", data=replace_once(old_head)).decode().strip()
    index_blob = git("hash-object", "-w", "--stdin", data=replace_once(old_index)).decode().strip()
    git("update-index", "--add", "--cacheinfo", "100644," + head_blob + ",ledger.md", env=env)
    git("update-index", "--cacheinfo", "100644," + index_blob + ",ledger.md")
    (root / "ledger.md").write_bytes(replace_once(old_work))
    git("commit", "-qm", "owned escalation only", env=env)

    assert git("show", "HEAD:ledger.md") == replace_once(old_head)
    assert git("show", ":ledger.md") == replace_once(old_index)
    assert (root / "ledger.md").read_bytes() == replace_once(old_work)
    assert git("show", ":other.txt") == old_other
    assert b"user staged row" not in git("show", "HEAD:ledger.md")
    for actual, original in [(git("show", "HEAD:ledger.md"), old_head),
                             (git("show", ":ledger.md"), old_index),
                             ((root / "ledger.md").read_bytes(), old_work)]:
        assert actual.count(new) == 1
        assert actual.replace(new, old, 1) == original
    new_patch = git("diff", "--cached", "--binary")
    # Blob identity lines must differ after editing the same file. Compare
    # the unchanged staged hunks separately from those expected object IDs.
    without_ids = lambda p: b"\n".join(line for line in p.splitlines()
                                        if not line.startswith(b"index "))
    assert new_patch != old_patch
    assert without_ids(new_patch) == without_ids(old_patch)
    print(json.dumps({"scope": "synthetic Git-only fixture", "owned_commit_only": True,
                      "staged_and_unstaged_bytes_recover_exactly": True,
                      "unrelated_index_entry_unchanged": True,
                      "staged_hunks_unchanged_except_expected_blob_ids": True,
                      "rejecting_cases": rejected, "scientific_execution": False}))


if __name__ == "__main__":
    main()
