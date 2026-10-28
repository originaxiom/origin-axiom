"""unif_note_check (POST HOC, labelled; 2026-10-28): the recount behind UNIF_TEST_RESULT.md's dated note -- the rows whose stored
chi2_nine read-out differs from the search minimum (main's defect, row 1424), the least of them, order 12's least row, and the
G - Z read-out on read-outs and on search minima, from the committed unif_rows.json.  python3 -B unif_note_check.py"""
import json, sys, contextlib, io, importlib.util, pathlib
import numpy as np
from fractions import Fraction as Fr
ZF = pathlib.Path(__file__).resolve().parent.parent / "chat1_2026-10-23_zero_free_frame"
sys.argv = ["x"]
sp = importlib.util.spec_from_file_location("zfc", ZF / "zero_free_census.py"); zfc = importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(zfc)
LN = [(Fr(a), Fr(b)) for (_t, a, b) in zfc.tic.LINES]
d = json.load(open(pathlib.Path(__file__).resolve().parent / "unif_rows.json"))
tasks, rows = d["tasks"], d["rows"]
LOOK = [(Fr(2, 5), Fr(0)), (Fr(2, 5), Fr(3, 5))]
def smin(a):
    return a["chi2_nine"] if a["stage B ran"] else a["stage A minimum"]
for arm in ("Z", "G"):
    aff = [r for r in rows if abs(r[arm]["chi2_nine"] - smin(r[arm])) > 1e-6 * smin(r[arm])]
    lo = min(aff, key=lambda r: smin(r[arm]))
    print(arm, "affected", len(aff), "least search minimum among them %.1f (read-out %.1f) on %s at %s %s" % (smin(lo[arm]), lo[arm]["chi2_nine"], LN[tasks[lo["p"]][0]], tasks[lo["p"]][1:], lo["hor"]))
away = [r for r in rows if LN[tasks[r["p"]][0]] not in LOOK]
print("--- every task off the look's lines (the mirror tau and degenerate rows included):", len(away), "rows")
for lab, f in (("read-out", lambda a: a["chi2_nine"]), ("search minimum", smin)):
    diff = np.array([f(r["G"]) - f(r["Z"]) for r in away])
    print(lab, "G - Z quantiles 10/50/90%%: %.0f %.0f %.0f; G lower on %d of %d" % (*np.quantile(diff, [0.1, 0.5, 0.9]), int((diff < 0).sum()), len(diff)))
# the order-12 lowest
o12 = [r for r in rows if max(LN[tasks[r["p"]][0]][0].denominator, LN[tasks[r["p"]][0]][1].denominator) and __import__("math").lcm(LN[tasks[r["p"]][0]][0].denominator, LN[tasks[r["p"]][0]][1].denominator) == 12]
lo = min(o12, key=lambda r: r["Z"]["chi2_nine"])
print("order 12 at Z: least read-out %.1f (search minimum %.1f) on %s at %s %s" % (lo["Z"]["chi2_nine"], smin(lo["Z"]), LN[tasks[lo["p"]][0]], tasks[lo["p"]][1:], lo["hor"]))
lo2 = min(o12, key=lambda r: smin(r["Z"]))
print("order 12 at Z: least search minimum %.1f" % smin(lo2["Z"]))
print("--- with the cells' filter (not degenerate, Re tau != 0.725, off the look's lines)")
away2 = [r for r in rows if (not r.get("degenerate")) and abs(tasks[r["p"]][1] - 0.725) > 1e-9 and LN[tasks[r["p"]][0]] not in LOOK]
print("rows", len(away2))
for lab, f in (("read-out", lambda a: a["chi2_nine"]), ("search minimum", smin)):
    diff = np.array([f(r["G"]) - f(r["Z"]) for r in away2])
    print(lab, "G - Z quantiles 10/50/90%%: %.0f %.0f %.0f; G lower on %d of %d" % (*np.quantile(diff, [0.1, 0.5, 0.9]), int((diff < 0).sum()), len(diff)))
