#!/usr/bin/env python3
"""Self-contained clean-tree audit of the B1147 reproduction-evidence lock.

The two vendored inputs are byte-for-byte extractions from Origin Axiom commit
9d6979db424c0b878c62541a3f21e0a2ca39f274.  One is the test; the other is the
sorted `git ls-tree -r --name-only` result for the B1147 frontier directory.
"""

from hashlib import sha256
from pathlib import Path

HERE = Path(__file__).resolve().parent
VENDOR = HERE / "vendor"
TEST = VENDOR / "b1147_test_b1147_clane_harvest.py"
TREE = VENDOR / "b1147_tree_paths.txt"
SOURCE_COMMIT = "9d6979db424c0b878c62541a3f21e0a2ca39f274"

expected_hashes = {
    TEST: "5713e542905a12c0343dcb7058984b749bffe0ac56d887d07190c76c3284378a",
    TREE: "eb70e098d918b7dbfa350ff93a40bb1641cb251a5db4dc129e054aadaf427dd7",
}
for path, expected in expected_hashes.items():
    actual = sha256(path.read_bytes()).hexdigest()
    assert actual == expected, (path.name, expected, actual)

test_text = TEST.read_text(encoding="utf-8")
tree_paths = set(TREE.read_text(encoding="utf-8").splitlines())
required = "frontier/B1147_clane_harvest/verification/reproduce.log"

assert 'ARC / "verification" / "reproduce.log"' in test_text
assert 'log.count("REPRODUCES") == 10' in test_text
assert '"REPRODUCE_DONE" in log' in test_text
assert required not in tree_paths

print("source_commit =", SOURCE_COMMIT)
print("test_sha256 =", expected_hashes[TEST])
print("tree_manifest_sha256 =", expected_hashes[TREE])
print("required_by_test =", required)
print("present_in_clean_tree =", required in tree_paths)
print("RESULT B1147 clean-checkout lock is not self-contained: required reproduce.log is absent")
print("SCOPE record/lock defect only; the eleven mathematical verdicts require separate reproduction")
