"""CERTIFICATE -- which locks read evidence the repository does not contain.

THE DEFECT CLASS.  .gitignore's LaTeX block carries the blanket rules `*.out`, `*.log` and
`*.jsonl`.  Those match at every depth, so besides LaTeX intermediates in papers/ they also
match arc artifacts all over frontier/ -- including files that committed locks read by name
and that a manifest pins by sha256.  A clone therefore cannot run those locks: they die with
FileNotFoundError, which reads like corruption and is not.

Five were found the hard way, by running the suite.  This finds the rest by reading, so the
list handed on is complete rather than "the ones that happened to fail today".

METHOD.  For every tracked tests/*.py, take each string literal that looks like an artifact
filename (an .out/.log/.jsonl/.json/.txt/.csv basename, or a path ending in one).  Resolve it
against every directory named in the same file that exists in the repo, plus the arc directory
the test's own name points at.  Report a hit when the resolved path EXISTS ON DISK BUT IS NOT
TRACKED (this bench happens to hold it, a clone will not) or DOES NOT EXIST ANYWHERE while a
tracked sibling directory obviously should hold it.

Reading filenames out of source is a heuristic, so this certificate reports and does not
gate; its controls say exactly how far to trust it.

CELLS (preregistered, two-outcome)
  CELL 1  Does any tracked test name an artifact that exists here but is untracked?
          A: yes -- those locks pass here and fail on a clone      B: none
  CELL 2  Are the .gitignore negations added this session sufficient for the five
          known cases -- i.e. is each of those paths now trackable?
          A: at least one is still ignored                         B: all trackable

CONTROLS
  C1  The tracked/untracked oracle must be right on a known-tracked file and on a
      known-ignored one.
  C2  The five paths repaired this session must be reported as trackable, and a path
      still covered by a blanket rule (a frontier .log outside the negated arcs) must
      still be reported as ignored -- so the check can tell the two apart.
"""
import os, re, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
ART = re.compile(r'["\']([A-Za-z0-9_./\-]+\.(?:out|log|jsonl|json|txt|csv))["\']')
EXT_IGNORED_BY_BLANKET = (".out", ".log", ".jsonl")


def tracked(rel):
    return subprocess.run(["git", "ls-files", "--error-unmatch", str(rel)],
                          capture_output=True, cwd=str(ROOT)).returncode == 0


def ignored(rel):
    return subprocess.run(["git", "check-ignore", "-q", str(rel)],
                          capture_output=True, cwd=str(ROOT)).returncode == 0


print(__doc__)
print("=" * 78)
print("checkout:", ROOT.name)

# ------------------------------------------------------------------ controls
known_tracked = "tests/test_no_hardcoded_paths.py"
c1 = tracked(known_tracked) and not tracked("no/such/file.log")
repaired = ["frontier/B1062_bridge_cell/b1062_v2_block3.log",
            "frontier/B1063_refresh_verdict/refresh_windows.log",
            "frontier/B646_wave2_integration/cc2_packets/next_queue/next_queue/"
            "n1_counting/character_run.log",
            "frontier/B1137_regulator_probe/results/real_grid.jsonl",
            "frontier/B1306_the_older_debt/verification/sliceC/c_beat.out"]
still_blanket = "frontier/B511_physics_verdict/scratch_probe.log"   # not in any negation
c2 = all(not ignored(p) for p in repaired) and ignored(still_blanket)
print(f"C1: {'PASS' if c1 else 'FAIL'}  -- tracked/untracked oracle correct both ways")
print(f"C2: {'PASS' if c2 else 'FAIL'}  -- the five repaired paths are trackable and a "
      f"path outside the negations is still ignored")

# ------------------------------------------------------------------ the sweep
untracked_hits, missing_hits = [], []
for tf in sorted((ROOT / "tests").glob("test_*.py")):
    src = tf.read_text(encoding="utf-8", errors="ignore")
    # every existing repo directory this test mentions, plus the arc its name points at
    dirs = set()
    for m in re.finditer(r'["\']([A-Za-z0-9_\-]+)["\']', src):
        for d in (ROOT / "frontier").glob(m.group(1) + "*"):
            if d.is_dir():
                dirs.add(d)
    stem = tf.stem[len("test_"):].split("_")[0].upper()
    for d in (ROOT / "frontier").glob(stem + "_*"):
        if d.is_dir():
            dirs.add(d)
    if not dirs:
        continue
    for m in ART.finditer(src):
        name = m.group(1)
        if name.startswith(("http", "//")) or name.endswith(".py"):
            continue
        found = False          # resolved ANYWHERE under ANY candidate arc dir, at any depth
        for d in dirs:
            for cand in (d / name, *(d.rglob(os.path.basename(name)))):
                if not cand.exists() or not cand.is_file():
                    continue
                found = True
                rel = cand.relative_to(ROOT)
                if not tracked(rel):
                    untracked_hits.append(f"{tf.name}  ->  {rel}")
                break
            if found:
                break
        if not found and name.endswith(EXT_IGNORED_BY_BLANKET) and "/" not in name:
            for d in dirs:
                if not tracked(d.relative_to(ROOT) / name):
                    missing_hits.append(f"{tf.name}  ->  {d.relative_to(ROOT)}/{name}"
                                        f"  (absent; extension under a blanket rule)")
                    break

untracked_hits = sorted(set(untracked_hits))
missing_hits = sorted(set(missing_hits))

print()
print(f"CELL 1  tests naming artifacts PRESENT HERE BUT UNTRACKED: {len(untracked_hits)}  -> "
      f"{'A (they would fail on a clone)' if untracked_hits else 'B (none)'}")
for h in untracked_hits[:40]:
    print("   ", h)
print()
print(f"        tests naming artifacts ABSENT HERE whose extension is under a blanket "
      f"rule: {len(missing_hits)}")
for h in missing_hits[:40]:
    print("   ", h)
print()
print(f"CELL 2  the five repaired paths trackable: {'B (yes)' if c2 else 'A (no)'}")
print()
print("ALL CONTROLS PASSED" if (c1 and c2) else "CONTROL FAILURE")
sys.exit(0 if (c1 and c2) else 1)
