"""Strict tracked-state snapshots; no scientific imports or repository writes.

HEAD/worktree equality alone is insufficient: the index can differ from both.
This is a snapshot under the repository's quiescent-window requirement, not
a filesystem lock or a claim to detect changes made and reverted between checks.
"""
import subprocess


def inspect(root, expected_head=None):
    values, errors = {}, {}
    queries = (
        ("head_before", ("rev-parse", "--verify", "HEAD")),
        ("index_changes", ("diff", "--no-ext-diff", "--name-only", "-z", "--cached", "HEAD", "--")),
        ("worktree_changes", ("diff", "--no-ext-diff", "--name-only", "-z", "--")),
        ("head_after", ("rev-parse", "--verify", "HEAD")),
    )
    for name, args in queries:
        try:
            result = subprocess.run(["git", "-C", str(root), *args],
                                    capture_output=True, timeout=30, check=True)
            if name.endswith("changes"):
                values[name] = [p.decode("utf-8", "backslashreplace")
                                for p in result.stdout.split(b"\0") if p]
            else:
                values[name] = result.stdout.decode("ascii").strip()
        except (OSError, ValueError, subprocess.SubprocessError) as error:
            values[name] = None
            errors[name] = type(error).__name__ + ": " + str(error)
    stable = (not errors and values["head_before"] == values["head_after"]
              and (expected_head is None or values["head_after"] == expected_head))
    return {**values, "errors": errors,
            "clean": bool(stable and not values["index_changes"]
                          and not values["worktree_changes"])}
