"""Step 3 (data-free): where the reading lives.  By B1788 the second-generation exponent is reading-blind; the first
generation's (m1/m3) is not.  The leading exponents of every sector under S and S~ on the slopes of the six's family and a
few others (B1788's tropical.predict), and the eight reading assignments' first-generation patterns on alpha = 2/5."""
import sys, json, pathlib, itertools
from fractions import Fraction as Fr
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1788_the_closed_form_of_the_exponents" / "verification"))
import tropical as T
P = {rd: T.polys(rd) for rd in ("S", "St")}
out = {}
for a in (Fr(2, 5), Fr(1, 10), Fr(1, 5), Fr(3, 10), Fr(1, 7), Fr(1, 3)):
    row = {}
    for sec, (l, r) in T.SECTORS.items():
        mu = T.E(T.SIXY[l] * a, T.SIXY[r] * a)
        for rd in ("S", "St"):
            e2, e3 = T.predict(P[rd], mu); row["%s %s" % (sec, rd)] = (str(e2), str(e3))
    out[str(a)] = row
    print("alpha", a, " ".join("%s:(%s,%s)" % (k, v[0], v[1]) for k, v in row.items()))
a = "2/5"
print("\nalpha = 2/5, the eight assignments (up, down, lep) -> first-generation exponents (m1/m3):")
assign = {}
for rds in itertools.product(("S", "St"), repeat=3):
    e = tuple(out[a]["%s %s" % (s, r)][1] for s, r in zip(("up", "down", "lep"), rds))
    assign["/".join(rds)] = e; print("  ", rds, e)
json.dump({"exponents": out, "assignments_2_5": assign}, open(pathlib.Path(__file__).resolve().parent / "reading_exponents.json", "w"), indent=1)
