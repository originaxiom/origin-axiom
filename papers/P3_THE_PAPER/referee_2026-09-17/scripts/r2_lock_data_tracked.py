"""Round-2 referee check: does any manifest lock read a data file that is not tracked?

This is the regression check for the worst round-1 defect. Four locks read
`frontier/B1419_.../verification/arithmetic_census_closed.jsonl`, which `.gitignore`'s blanket
`*.jsonl` rule excluded, so they passed on the author's bench and failed on every fresh clone.
S19 fixed that and claims to have swept for other instances ("found exactly one other, correctly
guarded"). This script checks that claim independently.

Run from the repository root:

    python3 papers/P3_THE_PAPER/referee_2026-09-17/scripts/r2_lock_data_tracked.py

Exit code 1 if any lock reads a present-but-untracked data file.

METHOD, and its limit. Every lock named in MANIFEST.json is scanned for string literals that look
like data filenames (.json/.jsonl/.csv/.txt/.npy/.out). Each basename is resolved against
frontier/*/verification/, frontier/*/ and frontier/*/results/, and any match that exists on disk is
tested with `git ls-files`. A lock that builds its path dynamically -- os.path.join of parts, or a
name computed from a record id -- would escape this scan, so a clean result is evidence and not a
proof. The complementary check is the one the author's own lock now does: assert trackedness from
inside the test (`test_b1424_referee_defects.py::_tracked`), which cannot be evaded that way.
"""
import json
import pathlib
import re
import subprocess
import sys

DATA = re.compile(r'["\']([A-Za-z0-9_./-]+\.(?:json|jsonl|csv|txt|npy|out))["\']')
SEARCH = ("frontier/*/verification/", "frontier/*/", "frontier/*/results/")


def main():
    root = pathlib.Path(".").resolve()
    manifest = root / "papers" / "P3_THE_PAPER" / "verification_package" / "MANIFEST.json"
    if not manifest.exists():
        print("run me from the repository root (no %s)" % manifest)
        return 2

    man = json.loads(manifest.read_text(encoding="utf-8"))
    locks = set()
    for claim in man["claims"]:
        for rec in claim["records"]:
            locks.update(rec.get("locks") or [])
    print("manifest locks: %d" % len(locks))

    tracked = set(subprocess.run(["git", "ls-files"], capture_output=True, text=True).stdout.splitlines())
    print("tracked files:  %d" % len(tracked))

    offenders, scanned, missing_locks = {}, 0, 0
    for lock in sorted(locks):
        path = root / lock
        if not path.exists():
            missing_locks += 1
            continue
        scanned += 1
        src = path.read_text(errors="ignore")
        for m in DATA.finditer(src):
            base = pathlib.Path(m.group(1)).name
            for pattern in SEARCH:
                for hit in root.glob(pattern + base):
                    rel = str(hit.relative_to(root))
                    if rel not in tracked:
                        offenders.setdefault(rel, set()).add(lock)

    print("locks scanned:  %d  (not on disk: %d)" % (scanned, missing_locks))
    print("\ndata files a lock reads, present on disk, NOT tracked: %d" % len(offenders))
    for rel, readers in sorted(offenders.items()):
        why = subprocess.run(["git", "check-ignore", "-v", rel],
                             capture_output=True, text=True).stdout.strip()
        print("  %s" % rel)
        print("     read by:    %s" % ", ".join(sorted(readers)[:3]))
        print("     ignored by: %s" % (why.split("\t")[0] if why else "(not ignored, merely untracked)"))
    if not offenders:
        print("  none -- every data file a lock reads is tracked")
    return 1 if offenders else 0


if __name__ == "__main__":
    sys.exit(main())
