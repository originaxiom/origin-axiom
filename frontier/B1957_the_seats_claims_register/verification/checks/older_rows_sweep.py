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
reg = {u[0].split(":")[1] for u in json.loads((V / "UNITS.json").read_text())["units"]}
OPEN = re.compile(r"^\**\s*(RECEIVED|REGISTERED|UNREAD|NOT READ)|NOT READ|NOTHING VERIFIED|REGISTERED BY|not read in full|read at name level|by file name", re.I)
stems = set()
for b in [b.strip() for b in git("for-each-ref", "--format=%(refname:short)", "refs/remotes/origin").split("\n") if b.strip()]:
    stems |= {f.split("/")[-1][:-3] for f in git("ls-tree", "-r", "--name-only", b).split("\n") if f.endswith(".md")}
out = collections.OrderedDict()
for l in L:
    m = re.match(r"\| (\d{3,4}) \| ([^|]+) \|", l)
    if not m: continue
    c = l.split(" | ")
    if len(c) < 8 or not OPEN.search(c[5][:400]): continue
    o = out.setdefault(c[1].strip(), {"rows": [], "rows_no_file": [], "files": {}})
    o["rows"].append(int(m.group(1)))
    fs = {f.split("/")[-1][:-3] for f in re.findall(r"[\w][\w./-]*\.md", c[2] + " " + c[3] + " " + c[4])}
    if not fs: o["rows_no_file"].append(int(m.group(1)))
    for s in fs: o["files"][s] = "in the register" if s in reg else ("on a branch, not in the register" if s in stems else "not found")
tot = collections.Counter(); nrows = nnone = 0
for seat, o in sorted(out.items(), key=lambda kv: -len(kv[1]["rows"])):
    st = collections.Counter(o["files"].values()); tot.update(st); nrows += len(o["rows"]); nnone += len(o["rows_no_file"])
    print("S1: %s: rows %d (naming no file %d); files %d: %s" % (seat, len(o["rows"]), len(o["rows_no_file"]), len(o["files"]), dict(sorted(st.items()))))
print("S2: %d seat labels; %d rows; %d of them name no file; files: %s" % (len(out), nrows, nnone, dict(sorted(tot.items()))))
(HERE / "older_rows.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
