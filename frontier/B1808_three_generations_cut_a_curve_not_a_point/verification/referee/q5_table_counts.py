"""Referee B1808, check 5: the table's class counts (|Q| = 6, primitive, coefficients <= 3) and the distinct-det counts
(the author's list is cut at 40 by the script's [:40])."""
import itertools, json, math, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
AUTH = json.loads((HERE.parent / "three_generations_in_f2h.json").read_text())
q2 = json.loads((HERE / "q2_points.json").read_text())
for name in ("LR", "B_4", "B_5", "B_6", "B_7"):
    G = np.array(AUTH[name]["Gram Q"], dtype=int)
    n = {6: 0, -6: 0}
    for c in itertools.product(range(-3, 4), repeat=4):
        if not any(c) or math.gcd(*c) != 1: continue
        v = np.array(c); q = int(v @ G @ v)
        if abs(q) == 6: n[q] += 1
    r = q2[name]
    print(name, "| |chi|=3 classes:", n[6] + n[-6], "(author %s)" % AUTH[name]["classes with |chi| = 3 (coefficients <= 3)"],
          "| Q=-6:", n[-6], "Q=+6:", n[6],
          "| distinct det Gram: exact %d, author's list %d" % (len(r["distinct det Gram(w,u) (exact)"]), len(r["author's 'distinct det' list"])),
          "| distinct det NS (saturated): %d, range %s-%s" % (len(r["distinct det NS (saturated)"]), min(r["distinct det NS (saturated)"]), max(r["distinct det NS (saturated)"])),
          "| u-pairs %d -> points %d" % (r["exact count of u with det Gram(w,u) > 0"], r["distinct points (planes)"]))
