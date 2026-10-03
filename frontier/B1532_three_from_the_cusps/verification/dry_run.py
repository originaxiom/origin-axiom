"""dry run of read_out.py on SYNTHETIC rows (M2, M3 labels; no instrument output): planted faults must be caught and the
census sums must equal an independent recount"""
import json, hashlib, sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from fractions import Fraction as Fr
from pathlib import Path
import read_out as RO
import cover_lib_t as CT
import tempfile
D = Path(tempfile.mkdtemp(prefix="b1532_dry_"))          # synthetic rows live outside the tree
def h(*a):
    return int(hashlib.sha256(":".join(map(str, a)).encode()).hexdigest(), 16)
rowsT, rowsL = [], []
truth = {}
for n in (2, 3):
    lev = CT.RT.Level(n)
    labels = [f"{Fr(a, lev.N)},{Fr(b, lev.N)}" for a, b in lev.chars]
    for nu in labels:
        for chi in labels:
            # a conjugation-symmetric synthetic term in {0,1}^2, 0 at chi = nu^4 for W
            key = tuple(sorted([(nu, chi), (RO.neg(nu), RO.neg(chi))]))
            w = h("w", n, key) % 2
            l = h("l", n, key) % 2
            if RO.scale(nu, 4) == chi:
                w = 0
            truth[(n, nu, chi)] = (w, l)
            tT = [[w, 0, 1, 1, 1, 0, 2, 2, 1], [l, 0, 2, 2, 2, 0, 2, 3, 2]]
            tL = [RO.to_lsig("T", tT[0]), RO.to_lsig("T", tT[1])]
            rowsT.append({"route": "T", "p": 1, "n": n, "nu": nu, "chi": chi, "kind": "one", "c": tT})
            rowsL.append({"route": "L", "p": 1, "n": n, "nu": nu, "chi": chi, "kind": "one", "c": tL})
# plant: a D5 mismatch, a D6 asymmetry (route T only) and a D7 violation (negative simple W) in route L
rowsL[7]["c"] = [[1 - rowsL[7]["c"][0][0]] + rowsL[7]["c"][0][1:], rowsL[7]["c"][1]]
rowsT[11]["c"][1][0] = 1 - rowsT[11]["c"][1][0]
planted_D7 = rowsL[30]; planted_D7["c"] = [[-1] + planted_D7["c"][0][1:], planted_D7["c"][1]]
for route, rows in (("T", rowsT), ("L", rowsL)):
    with open(D / f"terms_{route}.jsonl", "w") as fh:
        by = {}
        for r in rows:
            by.setdefault((r["n"], r["nu"]), []).append(r)
        for (n, nu), rr in by.items():
            for r in rr:
                fh.write(json.dumps(r) + "\n")
            fh.write(json.dumps({"done": True, "route": route, "n": n, "nu": nu, "rows": len(rr)}) + "\n")
    (D / f"part0_{route}.json").write_text(json.dumps({"passed": True}))
sys.argv = ["read_out.py", "--dir", str(D), "--record"]
out = RO.main()
# independent recount of route T's census: generation-shaped sums from the rows as written
T = {(r["n"], r["nu"], r["chi"]): (r["c"][0][0], r["c"][1][0]) for r in rowsT}
shaped = []
for n in (2, 3):
    lev = CT.RT.Level(n)
    labels = [f"{Fr(a, lev.N)},{Fr(b, lev.N)}" for a, b in lev.chars]
    for nu in labels:
        for B in RO.subgroups(labels):
            sw = sum(T[(n, nu, c)][0] for c in B); sl = sum(T[(n, nu, c)][1] for c in B)
            if sw == sl != 0:
                shaped.append((n, nu, tuple(sorted(B)), -sw))
mine = sorted(shaped)
theirs = sorted((x["n"], x["nu"], tuple(x["B"]), x["N"]) for x in out["census"]["T"]["generation-shaped"])
print("recount equals the read-out's route-T census:", mine == theirs, len(mine))
print("checks:", out["checks"])
print("D5 first:", out["check failures (first 10 each)"].get("D5", [])[:2])
print("D6:", out["check failures (first 10 each)"].get("D6", [])[:2])
print("D7:", out["check failures (first 10 each)"].get("D7", [])[:2])
