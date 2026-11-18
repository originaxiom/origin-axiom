"""B1957: the web seat's section 12 as corrected (its status page at f975f6ea4), held against main's records after main
took its eight items (2026-11-18).  Nothing of the seat's is run.
 T1  each line the section names in the seat's own notes carries the mark it says (a reading, [J], not computed).
 T2  no VERIFIED record of main's holds any unit the section's eight items and its last paragraph name.
 T3  two figures of main's own check that the section quotes."""
import json, pathlib, re, subprocess
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
V = ROOT / "frontier/B1957_the_seats_claims_register/verification"; HEAD = "f975f6ea4"
show = lambda p: subprocess.run(["git", "show", "%s:%s" % (HEAD, p)], capture_output=True, text=True, cwd=ROOT).stdout.split("\n")
ls = subprocess.run(["git", "ls-tree", "-r", "--name-only", HEAD, "relays"], capture_output=True, text=True, cwd=ROOT).stdout.split("\n")
note = lambda pat: next(f for f in ls if re.search(pat, f) and "/cards/" not in f)
MARK = re.compile(r"\[J\]|a reading|not computed|judgement", re.I)
T1 = {("W-Z1", 54): 0, ("W-Z1", 46): 0, ("W-Z1", 93): 0, ("W-A2_", 110): 0, ("W-A2_", 187): 0, ("W-F17_SECOND", 193): 0, ("W-F17_SECOND", 278): 0, ("W-A3_", 174): 0, ("W-A3_", 54): 0, ("W-A3_", 62): 0, ("W-F24", 87): 0}
if not ls or len(ls) < 5: raise SystemExit("the seat's branch is not fetched here: nothing checked")
for (pat, n) in T1: T1[(pat, n)] = bool(MARK.search(" ".join(show(note(pat))[n - 1:n + 1])))      # the item's first two lines: one item's mark stands on its second
print("T1: lines carrying the mark the section says: %d of %d (%s)" % (sum(T1.values()), len(T1), ", ".join("%s:%d %s" % (p.strip("_"), n, "yes" if v else "NO") for (p, n), v in T1.items())))
units = json.loads((V / "UNITS.json").read_text())["units"]; held = {}
for q in (V / "records").glob("web-*.json"):
    d = json.loads(q.read_text())
    for u in d.get("units", []): held[u] = (d["id"], d["verdict"])
NAMED = {"W-F24": (53, 55, 87), "W-A3_": (54, 62, 145), "VIEW": (315, 316, 318), "W-F17_SECOND": (244, 263, 266, 278), "W-B2": (155,), "W-Z1": (59, 106), "W-A2_": (112, 114, 187)}
bad, n = [], 0
for u in units:
    lane, stem, line = u[0].split(":")[0], ":".join(u[0].split(":")[1:-1]), int(u[0].split(":")[-1])
    if lane != "web" or u[2] != "s": continue
    for pat, lines in NAMED.items():
        if re.search(pat, stem) and "cards" not in stem and line in lines:
            n += 1
            if held.get(u[0], ("", "PENDING"))[1] == "VERIFIED": bad.append((u[0], held[u[0]][0]))
print("T2: units the section names: %d found in the register; of them still under a VERIFIED record: %d %s" % (n, len(bad), bad[:6]))
run = (V / "checks/web_section9_items_run.txt").read_text()
print("T3: main's own run prints the volume ratio's residual as the section quotes it (-4.2e-45): %s; the orders 10, 320, 20,480: %s" % ("-4.2e-45" in run or "4.2e-45" in run, all(x in run.replace(",", "") for x in ("320", "20480"))))
