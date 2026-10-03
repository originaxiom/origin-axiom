"""dry run 2 of read_out.py on SYNTHETIC rows: one two-class member on M3 with special classes (a shared one), both routes in
their own s-coordinate (s_L = 3 s_T + 5); special-class sums against an independent recount; D2/D3/D4/D5/coincidence checks"""
import json, hashlib, sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from fractions import Fraction as Fr
from pathlib import Path
import read_out as RO
import cover_lib_t as CT
import tempfile
D = Path(tempfile.mkdtemp(prefix="b1532_dry_"))          # synthetic rows live outside the tree
n = 3
lev = CT.RT.Level(n)
labels = [f"{Fr(a, lev.N)},{Fr(b, lev.N)}" for a, b in lev.chars]
nu2 = labels[5]
chis = sorted(labels)
spec = {chis[3]: 12345, chis[7]: 12345, chis[9]: 777}           # chi -> special point (route T coordinate)
def gen_term(w, l):
    return [[w, 0, 1, 1, 0, 0, 1, 2, 1], [l, 0, 1, 2, 1, 0, 1, 3, 2]]
def spec_term(w, l):
    return [[w, 0, 2, 1, 0, 0, 1, 2, 1], [l, 0, 1, 2, 1, 0, 1, 3, 2]]
pen = lambda pts: {"E": [1, 1, 1, pts, 0, 0], "E*": [1, 1, 1, [], 0, 0], "L2E": [1, 1, 1, [], 0, 0], "L2E*": [1, 1, 1, [], 0, 0]}
rows = {"T": [], "L": []}
truth = {}
for nu in labels:
    for chi in labels:
        for route in ("T", "L"):
            conv = (lambda t: t) if route == "T" else (lambda t: [RO.to_lsig("T", t[0]), RO.to_lsig("T", t[1])])
            if nu == nu2:
                w = 1 if chi in (chis[1], chis[2]) else 0
                r = {"route": route, "p": 1, "n": n, "nu": nu, "chi": chi, "kind": "two", "int": conv([[0] * 9, [0] * 9]),
                     "gen": [99, conv(gen_term(w, 0))], "special": []}
                pts = []
                if chi in spec:
                    s = spec[chi] if route == "T" else 3 * spec[chi] + 5
                    pts = [["r", s]]
                    r["special"] = [[["r", s], ["E"], conv(spec_term(w - 1, -1))]]
                r["pencils"] = pen(pts)
                truth[(chi, "gen")] = (w, 0)
                truth[(chi, "spec")] = (w - 1, -1) if chi in spec else None
            else:
                r = {"route": route, "p": 1, "n": n, "nu": nu, "chi": chi, "kind": "one", "c": conv([[0] * 9, [0] * 9])}
            rows[route].append(r)
for route in ("T", "L"):
    with open(D / f"terms_{route}.jsonl", "w") as fh:
        by = {}
        for r in rows[route]:
            by.setdefault((r["n"], r["nu"]), []).append(r)
        for (nn, nu), rr in by.items():
            for r in rr:
                fh.write(json.dumps(r) + "\n")
            fh.write(json.dumps({"done": True, "route": route, "n": nn, "nu": nu, "rows": len(rr)}) + "\n")
    (D / f"part0_{route}.json").write_text(json.dumps({"passed": True}))
sys.argv = ["read_out.py", "--dir", str(D), "--record"]
out = RO.main()
# independent recount at the two special classes of nu2 (route T coordinates)
subs = RO.subgroups(labels)
mine = []
for pt in (12345, 777):
    hitset = {c for c, s in spec.items() if s == pt}
    for B in subs:
        hit = [c for c in B if c in hitset]
        if not hit:
            continue
        sw = sum(truth[(c, "gen")][0] for c in B) + sum(truth[(c, "spec")][0] - truth[(c, "gen")][0] for c in hit)
        sl = sum(truth[(c, "gen")][1] for c in B) + sum(truth[(c, "spec")][1] - truth[(c, "gen")][1] for c in hit)
        if sw == sl != 0:
            mine.append((tuple(sorted(B)), -sw, tuple(sorted(hit))))
theirs = sorted((tuple(x["B"]), x["N"], tuple(x["class"][2])) for x in out["census"]["T"]["generation-shaped"]
                if not isinstance(x["class"], str))
print("special-class recount equals the read-out:", sorted(mine) == theirs, len(mine), theirs[:3])
print("checks:", out["checks"], "coincidence differs:", out["coincidence structure differs (members)"])
print("censuses agree:", out["censuses agree"])
