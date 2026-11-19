"""The SM seat's relay of 2026-10-07 (sections 1 to 355), read by main line by line (harvest row 1976): every line's
verdict in verification/sm_relay_reading.json is held here.
 G1  every statement of the relay in the register has exactly one entry, and the entry's verdict is its record's
     (sm-lbl-v, -p, -s, -r, -c, -n)
 G2  every VERIFIED, PARTIAL, SUPERSEDED and REFUTED entry has a ground whose quotation (whitespace and emphasis
     normalised) is within two lines of its line: in main's tree as it stands, or, for a ground in the relay itself, in
     the relay at c9296d14a
 G3  no ground lies in relays/ (except the relay itself, for SUPERSEDED), docs/seats/, this register, or the relay ledger
 G4  the counts by verdict
    python3 -B sm_relay_grounds.py > sm_relay_grounds_run.txt"""
import json, pathlib, re, subprocess, collections
V = pathlib.Path(__file__).resolve().parents[1]; ROOT = V.parents[2]
D = json.loads((V / "sm_relay_reading.json").read_text())
RELAY = D["relay"]; HEAD = D["head"]; P = "sm:" + RELAY.split("/")[-1][:-3] + ":"
norm = lambda s: re.sub(r"\s+", " ", re.sub(r"[*`]", "", s or "")).strip()
rel = subprocess.run(["git", "-C", str(ROOT), "show", "%s:%s" % (HEAD, RELAY)], capture_output=True, text=True).stdout.split("\n")
units = {u[0] for u in json.loads((V / "UNITS.json").read_text())["units"] if u[0].startswith(P) and u[2] == "s"}
owner = {}
for q in (V / "records").glob("*.json"):
    d = json.loads(q.read_text())
    for u in d.get("units", []): owner[u] = (q.stem, d.get("verdict"))
lines = D["lines"]; ids = [e["id"] for e in lines]
g1 = set(ids) == units and len(ids) == len(set(ids)) and all(owner.get(e["id"], ("", ""))[1] == e["verdict"] and owner[e["id"]][0].startswith("sm-lbl-") for e in lines)
print("G1: %d statements in the register, %d entries, one each and each in its sm-lbl record with its verdict: %s" % (len(units), len(ids), g1))
cache = {}
def text(path):
    if path not in cache:
        p = ROOT / path; cache[path] = p.read_text(errors="replace").split("\n") if p.is_file() else None
    return cache[path]
EXCL = ("relays/", "docs/seats/", "frontier/B1957_the_seats_claims_register/", "docs/RELAY_LEDGER.md")
bad2, bad3, n = [], [], 0
for e in lines:
    if e["verdict"] not in ("VERIFIED", "PARTIAL", "SUPERSEDED", "REFUTED"): continue
    n += 1; g = e.get("ground") or {}; path = g.get("path", ""); k = g.get("line"); q = norm(g.get("quote"))
    if path.endswith(" @ " + HEAD):
        L = rel; ok3 = e["verdict"] == "SUPERSEDED"
    else:
        L = text(path); ok3 = not path.startswith(EXCL)
    if not ok3: bad3.append(e["id"])
    ok2 = bool(L) and isinstance(k, int) and len(q) >= 12 and q in norm(" ".join(L[max(0, k - 3):k + 3]))   # lines k-2 to k+3: a quotation may run on past a line break
    if not ok2: bad2.append(e["id"])
print("G2: %d grounds; quotation within two lines of its line: %d; failing: %s" % (n, n - len(bad2), bad2[:5] or "none"))
print("G3: grounds in an excluded place: %s" % (bad3[:5] or "none"))
print("G4: %s" % dict(sorted(collections.Counter(e["verdict"] for e in lines).items())))
print("ALL HOLD:", g1 and not bad2 and not bad3)
