"""B1832 § 4 sharpened (2026-11-04): every 'seen_first' citation in the agy audit lane's toe_closure.py at 18c607040,
checked against main, both agy branches (18c607040, 05e6caab) and every other ref in this repository. Needs the agy
commits present locally (the archive tags). Prints each citation's status; no value is read."""
import re, subprocess, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]
def git(*a): return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)
src = git("show", "18c607040:src/origin_axiom/toe_closure.py").stdout
lists = re.findall(r'"seen_first":\s*\[(.*?)\]', src, re.S)
items = sorted({x for L in lists for x in re.findall(r'"([^"]+)"', L)})
refs = ["HEAD", "18c607040", "05e6caab"] + [r for r in git("for-each-ref", "--format=%(refname)", "refs/remotes/origin").stdout.split() if not r.endswith("/HEAD")]
main_arcs = git("ls-tree", "--name-only", "HEAD:frontier").stdout.split()
agy_arcs = git("ls-tree", "--name-only", "05e6caab:frontier").stdout.split() + git("ls-tree", "--name-only", "18c607040:frontier").stdout.split()
counts = {"exact": 0, "other seat's branch": 0, "real number, other title": 0, "exists on no branch": 0}
for it in items:
    status = None
    for r in refs:
        if git("cat-file", "-e", "%s:%s" % (r, it)).returncode == 0 or git("cat-file", "-e", "%s:frontier/%s" % (r, it)).returncode == 0:
            status = "exact" if r in ("HEAD", "18c607040", "05e6caab") else "other seat's branch"; break
    if status is None and re.match(r"B\d+$", it):
        status = "exact" if any(a.startswith(it + "_") for a in main_arcs) else None
    if status is None:
        m = re.match(r"(B\d+)_", it)
        real = [("main", a) for a in main_arcs if m and a.startswith(m.group(1) + "_")] or \
               [("agy", a) for a in agy_arcs if m and a.startswith(m.group(1) + "_")]
        status = "real number, other title" if real else "exists on no branch"
        if real: it = "%s  (%s: %s)" % (it, real[0][0], real[0][1])
    counts[status] += 1
    print("%-26s %s" % (status, it))
print("%d seen_first lists, %d distinct citations: %s" % (len(lists), len(items), counts))
