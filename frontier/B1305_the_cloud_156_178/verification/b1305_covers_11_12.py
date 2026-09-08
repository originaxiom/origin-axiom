"""B1305 Q2(b) -- six-cusp reachability with main's own code (DESIGN sealed 7e1a7420): SnapPy covers of m004 of degree 2..12, cusp
counts per degree; degrees 2-10 must reproduce main's B1295 (87 covers, 201 cusps) as the positive control; degrees 11-12 are the
extension the cloud's memo 170 addendum computed (predicted 26 covers max 4 cusps; 62 covers max 4 cusps; zero with >= 6)."""
import json, sys, time, warnings
from collections import Counter
warnings.filterwarnings("ignore")
import snappy
t0 = time.time(); M = snappy.Manifold("m004"); rows = {}
for d in range(2, 13):
    cs = [C.num_cusps() for C in M.covers(d)]
    rows[d] = dict(covers=len(cs), cusps_total=sum(cs), max_cusps=max(cs), by_cusps=dict(sorted(Counter(cs).items())))
    print(f"  degree {d:2d}: {len(cs):3d} covers, {sum(cs):4d} cusps, max {max(cs)}, by cusp count {rows[d]['by_cusps']}   ({time.time()-t0:.0f} s)")
pred_b1295 = {2: (1, 1), 3: (1, 1), 4: (2, 2), 5: (4, 3), 6: (11, 2), 7: (9, 3), 8: (10, 2), 9: (11, 3), 10: (38, 5)}
ok_ctrl = all((rows[d]["covers"], rows[d]["max_cusps"]) == pred_b1295[d] for d in pred_b1295) and sum(rows[d]["covers"] for d in range(2, 11)) == 87 and sum(rows[d]["cusps_total"] for d in range(2, 11)) == 201
print(f"  POSITIVE CONTROL (degrees 2-10 = B1295: 87 covers, 201 cusps, per-degree counts and max cusps): {'PASS' if ok_ctrl else 'FAIL'}")
ok_ext = (rows[11]["covers"], rows[11]["max_cusps"]) == (26, 4) and (rows[12]["covers"], rows[12]["max_cusps"]) == (62, 4)
six = sum(1 for d in rows for k, v in rows[d]["by_cusps"].items() if k >= 6)
print(f"  degrees 11-12 as the cloud's memo 170 addendum: {'PASS' if ok_ext else 'FAIL'}; covers with >= 6 cusps to degree 12: {six}")
json.dump(dict(rows=rows, control=ok_ctrl, extension=ok_ext, six_or_more=six, seconds=round(time.time() - t0)), open("b1305_covers_11_12.json", "w"), indent=1)
print("Q2(b):", "PASS" if (ok_ctrl and ok_ext and six == 0) else "FAIL"); sys.exit(0 if (ok_ctrl and ok_ext and six == 0) else 1)
