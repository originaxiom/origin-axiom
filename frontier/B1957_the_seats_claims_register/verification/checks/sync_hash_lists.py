"""agy-002-sync (the branch agy/stage4-sync-2026-11-11 at d37c773d6): its page docs/OTHER_HASH_LISTS.md, section 2, lists the
entries of secondary seal hash lists that did not verify at main's 015be0cc7, each as ABSENT, MISMATCH or NO NAME.  Main
recomputes every row from git at 015be0cc7 (nothing of the seat's is run): the list file holds a line whose hash begins with
the key; the entry's file, resolved beside the list or from the repository root, is absent, or present with another SHA-256;
NO NAME: the line carries a hash and no file name.
 H1  per row: the state main finds, against the seat's; totals."""
import re, subprocess, hashlib, posixpath, collections
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
AT = "015be0cc7"
tree = set(git("ls-tree", "-r", "--name-only", AT).split("\n"))
page = git("show", "d37c773d6:docs/OTHER_HASH_LISTS.md").split("\n")
rows = []
for n, l in enumerate(page, 1):
    m = re.match(r"\| `([0-9a-f]{12})` \| `([^`]+)` \| (.+?) \| `([A-Z ]+)` \|$", l)
    if m: rows.append((n, m.group(1), m.group(2), m.group(3).strip().strip("`"), m.group(4)))
def blob_sha256(path):
    return hashlib.sha256(subprocess.run(["git", "show", "%s:%s" % (AT, path)], capture_output=True).stdout).hexdigest()
ROOTS = ("frontier/", "scripts/", "tests/", "docs/", "papers/", "outside_bench/", "knowledge/", "philosophy/", "speculations/", "story/", "src/")
HEX = re.compile(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])")
def entry(line):                       # the seat's rule, rebuilt from its text: (hash, name or None) or None
    m = HEX.search(line)
    if not m: return None
    rest = (line[:m.start()] + " " + line[m.end():]).strip()
    rest = re.sub(r"\bsha256\b\s*[:=]?", " ", rest, flags=re.I)
    names = [t.strip("`'\",;()*:=") for t in rest.split() if "." in t or "/" in t]
    return m.group(0), (names[0] if names else None)
def resolve(lst, h, name):
    d = posixpath.dirname(lst)
    if name is None: return None, "NO NAME"
    if name.startswith(ROOTS):
        real = posixpath.normpath(name); return (real, ("VERIFIES" if blob_sha256(real) == h else "MISMATCH")) if real in tree else (name, "ABSENT")
    hits = [c for c in dict.fromkeys([posixpath.normpath(posixpath.join(d, name)), posixpath.normpath(posixpath.join(d, "verification", name))]) if c in tree]
    if len(hits) > 1: return hits[0], "AMBIGUOUS"
    if not hits: return name, "ABSENT (or not tracked)"
    return hits[0], ("VERIFIES" if blob_sha256(hits[0]) == h else "MISMATCH")
keys = {r[1]: r for r in rows}; found = {}
for lst in sorted({r[2] for r in rows}):
    if lst not in tree: continue
    for line in git("show", "%s:%s" % (AT, lst)).split("\n"):
        e = entry(line.strip())
        if e is None: continue
        h, name = e; k = hashlib.sha256(("%s|%s|%s" % (lst, name, h)).encode()).hexdigest()[:12]
        if k in keys: found[k] = resolve(lst, h, name)
res = []
for n, key, lst, ent, state in rows:
    if key not in found: res.append((n, key, state, "KEY NOT FOUND")); continue
    st = found[key][1]; res.append((n, key, state, "ABSENT" if st.startswith("ABSENT") and state in ("ABSENT", "NOT TRACKED") else ("NOT TRACKED" if st.startswith("ABSENT") and state == "NOT TRACKED" else st)))
agree = [r for r in res if r[2] == r[3]]; dis = [r for r in res if r[2] != r[3]]
print("H1: rows %d; the seat's states %s; main's %s; agree %d; disagree %d %s"
      % (len(rows), dict(collections.Counter(r[4] for r in rows)), dict(collections.Counter(r[3] for r in res)), len(agree), len(dis), dis[:8]))
