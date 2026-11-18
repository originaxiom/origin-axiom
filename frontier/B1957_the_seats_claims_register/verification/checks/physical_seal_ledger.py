"""B1957: the physical lane's docs/SEAL_LEDGER.md.  The register holds every statement of every file a lane added or
changed, so this file contributes 7,649 statements; but the file is a generated view (one row per sealed document) that
the lane's branch carries from long before the window, and the lane changed it in the window by ten inserted lines.
This check establishes that mechanically, and verifies the three seals those lines state.  Nothing of the lane's is run.
 L1  between the window's base and the lane's head the file differs by insertions only; their number and position.
 L2  each of the three new rows names a file and a sha256: the hash is that of a version of the file in the branch's
     history; which commit, and its place relative to the commit the row's note names.
 L3  the lane's package P-C3 pins two source pages under verification/sources/frontier/: each is byte for byte a
     FINDINGS page of main's own (B1641, B1700), so its statements are main's and not the lane's."""
import subprocess, hashlib, re, pathlib
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
REF, BASE = "origin/audit/physical-bridge-2026-09-05", "1aa76251"
git = lambda *a, raw=False: (lambda r: r.stdout if raw else r.stdout.decode(errors="replace"))(subprocess.run(["git", *a], capture_output=True, cwd=ROOT))

if __name__ == "__main__":
    d = git("diff", "--numstat", BASE, REF, "--", "docs/SEAL_LEDGER.md").split(); body = [l for l in git("diff", "-U0", BASE, REF, "--", "docs/SEAL_LEDGER.md").split("\n") if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    old, new = git("show", BASE + ":docs/SEAL_LEDGER.md").split("\n"), git("show", REF + ":docs/SEAL_LEDGER.md").split("\n")
    print("L1: lines added %s, removed %s; the base's %d lines are the first %d lines of the head's %d, unchanged: %s; inserted lines that are table rows: %d" % (d[0], d[1], len(old), len(old), len(new), new[:len(old) - 1] == old[:-1], sum(l.startswith("+| 2026") for l in body)))
    for l in body:
        m = re.match(r"\+\| (\S+) \| ([^|]+) \| `([^`]+)` \| `([0-9a-f]{64})` \| (.*) \|$", l)
        if not m: continue
        date, stage, path, sha, note = m.groups(); hits = []
        for c in git("log", "--format=%H", REF, "--", path).split():
            if hashlib.sha256(git("show", "%s:%s" % (c, path), raw=True)).hexdigest() == sha: hits.append(c)
        named = re.search(r"at ([0-9a-f]{9})", note); extra = ""
        if named and hits:
            first = hits[-1]; anc = subprocess.run(["git", "merge-base", "--is-ancestor", named.group(1), first], cwd=ROOT).returncode == 0
            extra = "; the commit its note names, %s, is %s that version's first commit" % (named.group(1), "the same as or before" if anc else "NOT before")
        print("L2: %s, sha256 %s...: %s%s" % (path.split("/")[-1], sha[:12], ("the file had this hash in %d commit(s) of the branch, first at %s (%s)" % (len(hits), hits[-1][:9], git("log", "-1", "--format=%ci", hits[-1]).strip()[:16])) if hits else "NO version of the file in the branch's history has this hash", extra))
    D = "reports/physical_bridge_2026_09_05/registered_domain_index_join_2026_11_16/verification/sources/"
    for f in [x for x in git("ls-tree", "-r", "--name-only", REF, "--", D).split("\n") if x]:
        mine = f[len(D):]; a = hashlib.sha256(git("show", "%s:%s" % (REF, f), raw=True)).hexdigest(); same = [c for c in git("log", "--format=%h", "--", mine).split() if hashlib.sha256(git("show", "%s:%s" % (c, mine), raw=True)).hexdigest() == a]
        here = (ROOT / mine).is_file() and hashlib.sha256((ROOT / mine).read_bytes()).hexdigest() == a
        print("L3: %s: identical to main's own file in the working tree: %s; the commits of main at which the file had these bytes: %s" % (mine, here, same))
