"""Step 3 (data-free): does the frame's mirror (tau, alpha, b) -> (1 - conj tau, alpha, -alpha - b), i.e. w -> -conj w, preserve
each sector's reading (S stays S) or flip it (S <-> S~)?  B1726's compute() at a point and at its mirror; compare every
sector's (m2/m3, m1/m3) for the same and for the flipped reading.  Also the conjugation identity of S's components."""
import sys, json, pathlib, math
from fractions import Fraction as Fr
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification"))
import census as C
pts = [(0.3, 3.0, Fr(2, 5), Fr(1, 10)), (0.27, 3.04, Fr(2, 5), Fr(23, 30)), (0.6, 2.5, Fr(1, 7), Fr(2, 7)), (0.15, 3.3, Fr(1, 3), Fr(1, 6)), (0.45, 2.8, Fr(3, 10), Fr(1, 5))]
out = []
for re, im, a, b in pts:
    A = C.compute(re, im, a, b)
    bm = (-a - b) % 1
    B = C.compute(1 - re, im, a, bm)
    row = {"point": [re, im, str(a), str(b)], "mirror": [1 - re, im, str(a), str(bm)]}
    for sec in ("up", "down", "lep"):
        for h in ("L_max", "L_2"):
            for rd in ("S", "St"):
                fl = "St" if rd == "S" else "S"
                x = A["%s|%s|%s" % (sec, h, rd)]; same = B["%s|%s|%s" % (sec, h, rd)]; flip = B["%s|%s|%s" % (sec, h, fl)]
                d_same = max(abs(math.log(p / q)) for p, q in zip(x, same))
                d_flip = max(abs(math.log(p / q)) for p, q in zip(x, flip))
                row["%s|%s|%s" % (sec, h, rd)] = [d_same, d_flip]
    out.append(row)
    worst_same = max(v[0] for k, v in row.items() if "|" in k); worst_flip = max(v[1] for k, v in row.items() if "|" in k)
    print(row["point"], "-> mirror", row["mirror"], "| worst ln-deviation, same reading %.2e, flipped reading %.2e" % (worst_same, worst_flip))
json.dump(out, open(pathlib.Path(__file__).resolve().parent / "mirror.json", "w"), indent=1)
