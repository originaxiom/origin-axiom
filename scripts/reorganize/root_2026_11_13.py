"""The first physical move under GOVERNANCE section 12 (docs/REORGANIZATIONS.md, its first entry): the stray files at the
repository's root, 2026-11-13. The owner approved moving the front pages on 2026-11-12 (register row P-825) and named
the root's notes and result files as what a first reader should not meet.

Each move is one line below. The three notes between sessions are removed from the tree at the owner's word (git keeps
them in history). A file whose arc already keeps the same bytes is removed (git keeps it in history); a file
that differs from its arc's kept output is placed beside it under a name that says what it is. Nothing a lock reads
moves: every lock reads the arc's own copy (checked before the move).

    python3 scripts/reorganize/root_2026_11_13.py          # make the moves (git mv / git rm), once
    python3 scripts/reorganize/root_2026_11_13.py --check  # say whether the tree is as the moves leave it"""
import subprocess, sys, pathlib, filecmp

ROOT = pathlib.Path(__file__).resolve().parents[2]
MOVES = [
    ("AUDIT_REPORT.md", "docs/archive/AUDIT_REPORT.md"),
    ("b1116_results.json", "frontier/B1116_asymptotic_channel/b1116_results_run_from_the_root.json"),
    ("V3_results.json", "frontier/B1126_identification/V3_results.json"),
    ("results.json", "frontier/B1133_c4_single_end/b1133_results_run_from_the_root.json"),
]
REMOVE_FROM_THE_TREE = [            # notes between sessions: the owner's word of 2026-11-13, git history keeps them
    "CC3_TO_CC_2026-07-22_p3_complete.md",                    # at 5e7f335c9 and every commit before it back to its first
    "CC_TO_ALL_SEATS_2026-09-06_ARC_NUMBER_RESERVATION.md",
    "CC_TO_FC_2026-09-06_THE_QUESTION_MOVED_TO_YOUR_CUSP.md",
]
REMOVE_AS_DUPLICATES = [            # (root file, the arc's copy with the same bytes)
    ("b1109_results.json", "frontier/B1109_selection_cluster/b1109_results.json"),
    ("b1110_results.json", "frontier/B1110_spectral_cluster/b1110_results.json"),
]

def git(*a): subprocess.run(["git", "-C", str(ROOT), *a], check=True)

def check():
    bad = [old for old, new in MOVES if (ROOT / old).exists() or not (ROOT / new).exists()]
    bad += [old for old, keep in REMOVE_AS_DUPLICATES if (ROOT / old).exists() or not (ROOT / keep).exists()]
    bad += [old for old in REMOVE_FROM_THE_TREE if (ROOT / old).exists()]
    return bad

if __name__ == "__main__":
    if "--check" in sys.argv:
        bad = check(); print("as moved" if not bad else "not as moved: %s" % bad); sys.exit(1 if bad else 0)
    for old, keep in REMOVE_AS_DUPLICATES:
        assert filecmp.cmp(ROOT / old, ROOT / keep, shallow=False), (old, "is not the same bytes as", keep)
    for old, new in MOVES:
        (ROOT / new).parent.mkdir(parents=True, exist_ok=True); git("mv", old, new)
    for old, keep in REMOVE_AS_DUPLICATES:
        git("rm", "-q", old)
    for old in REMOVE_FROM_THE_TREE:
        git("rm", "-q", old)
    bad = check(); print("moved" if not bad else "INCOMPLETE: %s" % bad); sys.exit(1 if bad else 0)
