"""Referee B1795, r1: audit split_rows.jsonl (read-only).  NaN/None handling, clipped channel weights (2 pi L + c <= 0),
slot-swap invariance of Dn and |det M|, Dn on lines where a pair's twists are integral (the pre-seal peek's reach),
order-5 identity at the spectrum level (not only Dn), and the per-line split statistics at the strip."""
import pathlib as _pl; _ROOT = str(next(q for q in _pl.Path(__file__).resolve().parents if (q / 'frontier').is_dir() and (q / 'GENESIS.md').is_file()))
import json, math, statistics, pathlib
from fractions import Fraction as Fr
V = pathlib.Path(_ROOT + "/frontier/B1795_the_doublet_triplet_split_at_the_canonical_end/verification")
rows = [json.loads(l) for l in (V / "split_rows.jsonl").read_text().splitlines() if l.strip()]
P = ("D", "Dc", "H", "Hc")
print("rows", len(rows), "points", sorted({r["point"] for r in rows}), "lines", len({(r["a"], r["b"]) for r in rows}))
# 1. NaN / None
nan_dn = sum(1 for r in rows for p in P if isinstance(r[p]["Dn"], float) and math.isnan(r[p]["Dn"]))
none_c = [(r["a"], r["b"], r["point"], p, s) for r in rows for p in P for s, v in r[p]["c"].items() if v is None]
print("NaN Dn:", nan_dn, "| None c entries:", len(none_c), "by unit:", {s: sum(1 for x in none_c if x[4] == s) for s in "1ijk"})
# which units are None? (expect '1' since R1 = 0)
# 2. clipped weights: need L.  Recompute from the canonical-cusp column.
col = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.loads(pathlib.Path(_ROOT + "/frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json").read_text())["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
import numpy as np
IM = {"g1": 2.2, "g2": 1.7, "strip": 3.037487672558812}
Ls = {pk: (float(np.interp(y, [q[0] for q in col], [q[1] for q in col])), float(np.interp(y, [q[0] for q in col], [q[2] for q in col]))) for pk, y in IM.items()}
print("L values (L_max, L_2):", Ls, "| column Im range", col[0][0], col[-1][0])
clip = 0
for r in rows:
    for p in P:
        for s, v in r[p]["c"].items():
            if v is None: continue
            for L in Ls[r["point"]]:
                if 2 * math.pi * L + v <= 0: clip += 1
print("clipped channel weights (2 pi L + c <= 0):", clip)
cmin = min(v for r in rows for p in P for v in r[p]["c"].values() if v is not None)
cmax = max(v for r in rows for p in P for v in r[p]["c"].values() if v is not None)
print("c range", cmin, cmax)
# 3. slot swap
sw_dn = max(abs(r[a]["Dn"] - r[b]["Dn"]) / max(r[a]["Dn"], r[b]["Dn"]) for r in rows for a, b in (("D", "Dc"), ("H", "Hc")))
sw_det = max(abs(r[a]["detM|" + h] - r[b]["detM|" + h]) / max(r[a]["detM|" + h], r[b]["detM|" + h]) for r in rows for a, b in (("D", "Dc"), ("H", "Hc")) for h in ("L_max", "L_2"))
print("slot swap: max rel |Dn - Dn'| %.2e, max rel ||detM| - |detM'|| %.2e" % (sw_dn, sw_det))
sw_sv = max(abs(r[a]["sv|%s|%s" % (h, rn)][2] / r[a]["sv|%s|%s" % (h, rn)][0] - r[b]["sv|%s|%s" % (h, rn)][2] / r[b]["sv|%s|%s" % (h, rn)][0]) / (r[a]["sv|%s|%s" % (h, rn)][2] / r[a]["sv|%s|%s" % (h, rn)][0]) for r in rows for a, b in (("D", "Dc"), ("H", "Hc")) for h in ("L_max", "L_2") for rn in ("S", "St"))
print("slot swap: max rel diff of sv3/sv1 (spectrum NOT invariant?) %.2e" % sw_sv)
# R1 sign under swap, other residues
dev_R = 0.0
for r in rows:
    for a, b in (("D", "Dc"), ("H", "Hc")):
        for s in "ijk":
            x, y = complex(*r[a]["R"][s]), complex(*r[b]["R"][s]); dev_R = max(dev_R, abs(x - y) / max(abs(x), 1e-300))
print("slot swap: max rel diff residues i,j,k: %.2e" % dev_R)
# 4. D = 4 det M check, L-independence: |detM| at both horocycles vs |D|/4 ... note detM computed from u = sqrt(2piL + c) R
ldev = max(abs(r[p]["detM|L_max"] - r[p]["detM|L_2"]) / r[p]["detM|L_max"] for r in rows for p in P)
d4 = max(abs(r[p]["detM|L_max"] - abs(complex(*r[p]["D"])) / 4) / r[p]["detM|L_max"] for r in rows for p in P)
print("|detM(L_max)| vs |detM(L_2)| max rel %.2e ; |detM| vs |D|/4 max rel %.2e" % (ldev, d4))
# sum R_s^2 relative
sr = max(abs(sum(complex(*r[p]["R"][s]) ** 2 for s in "1ijk")) / sum(abs(complex(*r[p]["R"][s])) ** 2 for s in "1ijk") for r in rows for p in P)
print("max |sum R_s^2| / sum |R_s|^2 = %.2e  (rank-one residue => L-independence of det M)" % sr)
# 5. integral-twist lines: the pre-seal peek's reach
def integral(a, b, q): return (q * Fr(a)).denominator == 1 and (2 * q * Fr(b)).denominator == 1
for pair, q in (("H", 3), ("D", 2)):
    L = sorted({(r["a"], r["b"]) for r in rows if integral(r["a"], r["b"], q)}, key=lambda x: (Fr(x[0]), Fr(x[1])))
    vals = {pk: sorted({round(r[pair]["Dn"], 6) for r in rows if (r["a"], r["b"]) in L and r["point"] == pk}) for pk in ("g1", "g2", "strip")}
    print("lines where the %s pair's twists are integral (q a in Z, 2 q b in Z): %d %s ; its Dn there: %s" % (pair, len(L), L, vals))
# 6. order-5 identity at the spectrum level
o5 = [r for r in rows if r["order"] in (1, 5)]
spec = max(abs(r["D"]["sv|%s|%s" % (h, rn)][k] - r["H"]["sv|%s|%s" % (h, rn)][k]) / r["D"]["sv|%s|%s" % (h, rn)][0] for r in o5 for h in ("L_max", "L_2") for rn in ("S", "St") for k in range(3))
spec2 = max(min(abs(r["D"]["sv|%s|%s" % (h, rn)][k] - r[p]["sv|%s|%s" % (h, rn)][k]) / r["D"]["sv|%s|%s" % (h, rn)][0] for p in ("H", "Hc")) for r in o5 for h in ("L_max", "L_2") for rn in ("S", "St") for k in range(3))
print("order 1/5 lines: %d rows; max rel diff of sv (D vs H) %.2e; D vs best of H/Hc %.2e" % (len(o5), spec, spec2))
