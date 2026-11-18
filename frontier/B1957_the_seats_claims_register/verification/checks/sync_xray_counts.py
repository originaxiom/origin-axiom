"""agy-002-sync: its report 01_REPO_CRYSTAL_CLEAR_XRAY.md (2026-11-10) states counts of main at f452d8cb0 as exact verified values.
Main recounts from git those that git decides (nothing of the seat's is run).
 X1  tracked files, and those under frontier/, tests/, docs/; commits reachable; B folders (a folder named B<number> with or
     without a suffix letter), distinct numbers, repeated numbers, numbers absent up to the largest; test_*.py modules; the
     package's .py files; core/claims .md files.  The same at 9b3ae6f33, its later fetch."""
import subprocess, re, collections
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
for AT in ("f452d8cb0", "9b3ae6f33"):
    files = [f for f in git("ls-tree", "-r", "--name-only", AT).split("\n") if f]
    tops = sorted({f.split("/")[1] for f in files if f.startswith("frontier/") and f.count("/") >= 2})
    bd = [d for d in tops if re.match(r"B\d+[A-Z]?(_|$)", d)]; ids = collections.Counter(int(re.match(r"B(\d+)", d).group(1)) for d in bd)
    print("X1 at %s: tracked %d (frontier/ %d, tests/ %d, docs/ %d); commits %s; B folders %d over %d numbers, repeated %s, absent up to %d: %d; test_*.py modules %d; src/origin_axiom .py %d; core/claims .md %d"
          % (AT, len(files), sum(f.startswith("frontier/") for f in files), sum(f.startswith("tests/") for f in files), sum(f.startswith("docs/") for f in files), git("rev-list", "--count", AT).strip(),
             len(bd), len(ids), {k: v for k, v in ids.items() if v > 1}, max(ids), len([i for i in range(1, max(ids) + 1) if i not in ids]),
             len([f for f in files if re.search(r"(^|/)test_[^/]*\.py$", f)]), len([f for f in files if f.startswith("src/origin_axiom/") and f.endswith(".py")]), len([f for f in files if f.startswith("core/claims/") and f.endswith(".md")])))
