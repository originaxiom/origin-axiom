"""B1957: the seats' older deliveries that main's own harvest ledger records as received, registered or not read (2026-11-18,
P-876). The web seat's rule, which the author approved for that seat on 2026-11-18, took into the register every file named by
one of its rows whose disposition opens RECEIVED, REGISTERED or UNREAD or says it was not read; this sweep applies the same test
to every seat's rows, reads which files they name, and whether each is in the register now.
 S1  per seat (the ledger's own seat label): such rows; rows that name no file; the files named, by where they stand: in the
     register, on a branch of the remote (main included) and not in the register, or not found on any branch.
 S2  the totals; the full list is written to older_rows.json beside this script's run."""
import re, json, collections, subprocess, pathlib
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
HERE = pathlib.Path(__file__).resolve().parent; V = HERE.parent; ROOT = V.parents[2]
L = (ROOT / "docs" / "HARVEST_LEDGER.md").read_text().split("\n")
# CORRECTED 2026-11-18, later, at the web seat's section 25.4: register ids keep a file's folders (cards/..., a report's path), and
# the first version compared bare file names with them, so registered files under folders were listed as outside the register
reg = {u[0].split(":")[1].split("/")[-1] for u in json.loads((V / "UNITS.json").read_text())["units"]}
OPEN = re.compile(r"^\**\s*(RECEIVED|REGISTERED|UNREAD|NOT READ)|NOT READ|NOTHING VERIFIED|REGISTERED BY|not read in full|read at name level|by file name", re.I)
# added 2026-11-18, later: files a seat asked to keep out of the harvest lane (extract.py's EXCLUDE_PATTERNS) are their own class
import fnmatch, re as _re
_ex = (V / "extract.py").read_text(); _i = _ex.index("EXCLUDE_PATTERNS = {"); _j = _ex.index("\n}\n", _i)
_g = {}; exec(_ex[_i:_j + 3], _g); _pats = [p for v in _g["EXCLUDE_PATTERNS"].values() for p in v]
# CORRECTED 2026-11-18, later still, at the web seat's section 26.2 (f): matching by the last path segment collides (fourteen
# names, FINDINGS.md and PREREGISTRATION.md among them, are shared by several registered files), so a file of one seat could read
# "in the register" through another seat's file of the same name.  A named file is now resolved by its path: a path with folders
# by suffix at a folder boundary; a bare name only when exactly one path on the remote's branches carries it.  A name several
# paths share, given without a path, is its own class: the row does not say which file it means.
import sys as _sys
_sys.path.insert(0, str(ROOT / "audit" / "claims")); import rec as _rec
regpaths = {u["file"] for u in _rec.FULL["units"]}
paths = set(); kept_paths = set()
for b in [b.strip() for b in git("for-each-ref", "--format=%(refname:short)", "refs/remotes/origin").split("\n") if b.strip()]:
    _fs = [f for f in git("ls-tree", "-r", "--name-only", b).split("\n") if f.endswith(".md")]
    paths |= set(_fs); kept_paths |= {f for f in _fs if any(fnmatch.fnmatch(f, p) for p in _pats)}
    if b == "origin/main": main_paths = set(_fs)
paths |= regpaths
by_name = collections.defaultdict(set)
for f in paths: by_name[f.split("/")[-1]].add(f)
def where(f):
    cand = {q for q in by_name.get(f.split("/")[-1], ()) if q == f or q.endswith("/" + f)} if "/" in f else set(by_name.get(f, ()))
    if not cand: return "not found"
    if cand <= regpaths or ("/" in f and cand & regpaths): return "in the register"
    if len(cand) > 1 and "/" not in f: return "a name several files share, given without its path"
    q = min(cand, key=lambda x: (x not in main_paths, x))      # a path given with its folders, found under several roots: one file
    return "kept out at the seat's request" if q in kept_paths else ("on main's tree, not in the register" if q in main_paths else "on a seat's branch only, not in the register")
out = collections.OrderedDict()
for l in L:
    m = re.match(r"\| (\d{3,4}) \| ([^|]+) \|", l)
    if not m: continue
    c = l.split(" | ")
    if len(c) < 8 or not OPEN.search(c[5][:400]): continue
    o = out.setdefault(c[1].strip(), {"rows": [], "rows_no_file": [], "files": {}})
    o["rows"].append(int(m.group(1)))
    fs = {f.lstrip("./") for f in re.findall(r"[\w][\w./-]*\.md", c[2] + " " + c[3] + " " + c[4])}
    if not fs: o["rows_no_file"].append(int(m.group(1)))
    for s in fs: o["files"][s] = where(s)
tot = collections.Counter(); nrows = nnone = 0
for seat, o in sorted(out.items(), key=lambda kv: -len(kv[1]["rows"])):
    st = collections.Counter(o["files"].values()); tot.update(st); nrows += len(o["rows"]); nnone += len(o["rows_no_file"])
    print("S1: %s: rows %d (naming no file %d); files %d: %s" % (seat, len(o["rows"]), len(o["rows_no_file"]), len(o["files"]), dict(sorted(st.items()))))
print("S2: %d seat labels; %d rows; %d of them name no file; files: %s" % (len(out), nrows, nnone, dict(sorted(tot.items()))))
(HERE / "older_rows.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
