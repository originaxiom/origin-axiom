"""B1957: the web seat's section 14 (its check of main's message M53, at 01173b9df), held against main's own register
(data-free; the register's files are read from the commit the seat read, 84fcf1e57, and from the working tree).
 X1  the lane's totals at 84fcf1e57, against the figures the seat gives.
 X2  record web-wa2-05r at that commit: the sentence the seat quotes; where the five lines of W-A2 stand now.
 X3  the records of its 14.3: where each line it names stands now."""
import json, pathlib, subprocess
HERE = pathlib.Path(__file__).resolve().parent; ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()); V = HERE.parent
show = lambda p: subprocess.run(["git", "show", "84fcf1e57:frontier/B1957_the_seats_claims_register/verification/" + p], capture_output=True, text=True, cwd=ROOT).stdout
w = json.loads(show("SUMMARY.json"))["lanes"]["web"]; said = {"files": 137, "statements": 6826, "VERIFIED": 1901, "REFUTED": 2, "CONDITIONAL": 15, "PARTIAL": 429, "SUPERSEDED": 54, "NOTED": 4425, "PENDING": 0}
print("X1: the web lane at 84fcf1e57: %s; the seat's figures agree on every one: %s" % ({k: w[k] for k in said}, all(w[k] == v for k, v in said.items())))
old = json.loads(show("records/web-wa2-05r.json")); units = json.loads((V / "UNITS.json").read_text())["units"]            # each unit: [id, form, kind, hash]; the id ends with the line
owner = {}
for q in (V / "records").glob("*.json"):
    d = json.loads(q.read_text())
    for u in d.get("units", []): owner[u] = (d["id"], d["verdict"])
def where(stem, lines):
    out = {}
    for u in units:
        i = u[0]; head, _, ln = i.rpartition(":")
        if i.startswith("web:") and stem in head and ln.isdigit() and int(ln) in lines and i in owner: out[int(ln)] = owner[i]
    return out
wa2 = where("W-A2_", {110, 112, 114, 116, 187})
print("X2: web-wa2-05r at 84fcf1e57 was %s and said 'NOT ON MAIN: the move under S, and that the signs are real': %s; that record exists now: %s; W-A2's lines 110, 112, 114, 116, 187 now: %s"
      % (old["verdict"], "NOT ON MAIN: the move under S, and that the signs are real" in old["how"], (V / "records" / "web-wa2-05r.json").exists(), sorted(set(wa2.values()))))
items = [("W-F17_SECOND", {98, 99, 100, 101, 103, 102, 121, 211, 247, 265, 277}), ("W-Z1", {53, 59, 106}), ("W-A3_", {27, 167}), ("2026-11-15_W-B2_FRAME_D1S", {48, 51, 64}), ("P-783_THE_GOLDEN", {80, 81, 90, 94, 95}),
         ("W-C3_THE_SM_SEATS", {48, 55, 85, 88, 99, 104, 105}), ("W-C2_THE_AGY-EXP", {23, 101}), ("W-F1_", {55}), ("2026-09-08_SESSION_RELAY", {133})]
still = 0
for stem, lines in items:
    got = where(stem, lines); bad = {l: v for l, v in got.items() if v[1] == "VERIFIED"}; still += len(bad)
    print("X3: %-24s lines %s: %s%s" % (stem, sorted(lines), sorted({v[1] for v in got.values()}), "" if not bad else "  STILL VERIFIED: %s" % bad))
print("X3: lines of its 14.3 still under a verified record: %d" % still)
