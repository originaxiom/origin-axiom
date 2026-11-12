"""Reader A, own code.  B1893's lock test_a_ceiling_that_falls_and_rises_back_is_still_not_seen says: 'When the seat closes it, the
first assertion of each pair fails'.  For the attribution half the first assertion is
    g.ceiling_rises("x", {"a.md": 4}, {"a.md": 4}, "the anchor", {}) == (None, "")
Here a hypothetical mend is written that reads the attribution baseline along the history (every upward step since the anchor
needs its record).  With the mend, the fall-and-rise plant (4 -> 2 -> 4) is seen; the lock's assertion above still holds."""
import importlib.util, json, pathlib, subprocess, sys, tempfile
EXT = pathlib.Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("g", EXT / "scripts/gates/gates.py"); g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
def git(repo, *a):
    return subprocess.run(["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@example.invalid", *a], capture_output=True, text=True).stdout.strip()
def commit(repo, msg, counts):
    p = repo / "docs" / "ATTRIBUTION_BASELINE.json"; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps({"frozen": counts}) + "\n"); git(repo, "add", "-A"); git(repo, "commit", "-q", "-m", msg); return git(repo, "rev-parse", "HEAD")
def mended(anchor, repo):
    """a mend of the kind the page names: every upward step since the anchor is held, not only anchor vs now"""
    revs = git(repo, "rev-list", "--reverse", "%s..HEAD" % anchor).split()
    prev = json.loads(git(repo, "show", "%s:docs/ATTRIBUTION_BASELINE.json" % anchor))["frozen"]
    for r in revs:
        now = json.loads(git(repo, "show", "%s:docs/ATTRIBUTION_BASELINE.json" % r))["frozen"]
        prob, _ = g.ceiling_rises("docs/ATTRIBUTION_BASELINE.json", now, prev, r[:9], {})
        if prob: return prob, ""
        prev = now
    return None, ""
with tempfile.TemporaryDirectory() as d:
    repo = pathlib.Path(d) / "small"; repo.mkdir(); git(repo, "init", "-q")
    anchor = commit(repo, "anchor", {"a.md": 4}); commit(repo, "lowered", {"a.md": 2}); commit(repo, "raised back", {"a.md": 4})
    g._load_attr_baseline = lambda: json.loads((repo / "docs/ATTRIBUTION_BASELINE.json").read_text())["frozen"]
    print("series as landed, the plant 4 -> 2 -> 4:", g.attribution_baseline_rise(anchor, repo))
    print("with a history-reading mend, the same plant:", str(mended(anchor, repo))[:120])
print("the lock's first assertion of the attribution pair, unchanged by such a mend:",
      g.ceiling_rises("x", {"a.md": 4}, {"a.md": 4}, "the anchor", {}) == (None, ""))
