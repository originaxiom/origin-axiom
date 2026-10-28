"""Referee B1799, checks 2-4 on the stored rows (majorana_rows.jsonl) and a reproduction sample.
Read-only; imports B1795's split.py and B1799's majorana.py (the latter only for its sym() on the sample)."""
import pathlib as _pl; _ROOT = str(next(q for q in _pl.Path(__file__).resolve().parents if (q / 'frontier').is_dir() and (q / 'GENESIS.md').is_file()))
import sys, math, json, pathlib, importlib.util, random
from fractions import Fraction as Fr
from collections import Counter
import numpy as np
ROOT = pathlib.Path(_ROOT + "")
ARC = ROOT / "frontier/B1799_the_neutrinos_self_pairing_at_the_canonical_end/verification"
spec = importlib.util.spec_from_file_location("split", ROOT / "frontier/B1795_the_doublet_triplet_split_at_the_canonical_end/verification/split.py")
SP = importlib.util.module_from_spec(spec); spec.loader.exec_module(SP)
spec2 = importlib.util.spec_from_file_location("maj", ARC / "majorana.py")
MJ = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(MJ)
rows = [json.loads(l) for l in (ARC / "majorana_rows.jsonl").read_text().splitlines() if l.strip()]
print("rows %d; distinct (line, point) %d; lines %d; points %s" % (len(rows), len({(r["line"], r["point"]) for r in rows}), len({r["line"] for r in rows}), Counter(r["point"] for r in rows)))
print("nucnuc present on", [(r["line"], r["point"]) for r in rows if "nucnuc" in r])
# lines vs SP.lines()
L = SP.lines(); bad = [r for r in rows if (str(L[r["line"]][0]), str(L[r["line"]][1])) != (r["a"], r["b"])]
print("row (a, b) against split.lines():", len(bad), "mismatches")
def order(q, a, b): return math.lcm(((q * Fr(a)) % 1).denominator, ((q * Fr(b)) % 1).denominator)
# 2. the Dirac zeros
Z = 1e-10
zl = sorted({(r["a"], r["b"]) for r in rows if r["Lnuc"]["Dn"] < Z})
pl = sorted({(str(a), str(b)) for (a, b) in L if order(-3, a, b) == 4})
print("Dirac zero lines %d; lines with -3w of exact order 4: %d; equal sets: %s" % (len(zl), len(pl), zl == pl))
print("  orders of the zero lines:", Counter(order(1, Fr(a), Fr(b)) for a, b in zl))
print("  zero rows per point:", Counter(r["point"] for r in rows if r["Lnuc"]["Dn"] < Z))
zD = [r["Lnuc"]["Dn"] for r in rows if r["Lnuc"]["Dn"] < Z]; nzD = [r["Lnuc"]["Dn"] for r in rows if r["Lnuc"]["Dn"] >= Z]
print("  Dn at zeros max %.1e; Dn elsewhere min %.2e" % (max(zD), min(nzD)))
# the law's 'right twist <= 2' arm: the alternative (left <= 2, right exactly 4) can never fire with q_R = 0
# the charged-lepton sector L e (-3, 6) has the same predicted zero set:
pl_e = sorted({(str(a), str(b)) for (a, b) in L if order(-3, a, b) == 4 and order(6, a, b) <= 2})
print("  the charged-lepton sector's predicted zero lines (L e, -3, 6) on the same census: %d; same set as the Dirac's: %s" % (len(pl_e), pl_e == pl))
# 3. Dirac: det Y_D = 4 det S det M tr(eps S M^T) -- the other two factors on the non-zero rows
trs = []
for r in rows:
    s = r["Lnuc"]
    if s["Dn"] < Z: continue
    for h in ("L_max", "L_2"):
        for rn in ("S", "St"):
            sv = s["sv|%s|%s" % (h, rn)]; trs.append((sv[2] / sv[0], s["tr|%s|%s" % (h, rn)] / sv[0], r["a"], r["b"], r["point"], h, rn))
trs.sort()
print("Dirac non-zero rows: least sv3/sv1 %.2e at %s;  least |tr(eps S M^T)|/sv1 %.2e" % (trs[0][0], trs[0][2:], min(x[1] for x in trs)))
# Majorana: where is the least sv3/sv1?
for nm in ("LL", "nucnuc"):
    best = min(((r[nm]["sv|%s|%s" % (h, rn)][2] / r[nm]["sv|%s|%s" % (h, rn)][0], r["a"], r["b"], r["point"], h, rn) for r in rows if nm in r for h in ("L_max", "L_2") for rn in ("S", "St")))
    strip = min((r[nm]["sv|%s|%s" % (h, rn)][2] / r[nm]["sv|%s|%s" % (h, rn)][0] for r in rows if nm in r and r["point"] == "strip" for h in ("L_max", "L_2") for rn in ("S", "St")))
    g = min((r[nm]["sv|%s|%s" % (h, rn)][2] / r[nm]["sv|%s|%s" % (h, rn)][0] for r in rows if nm in r and r["point"] != "strip" for h in ("L_max", "L_2") for rn in ("S", "St")))
    print("%s: least sv3/sv1 %.2e at %s; at the strip %.2e; at g1/g2 %.2e;  min Dn %.2e at %s" % (nm, best[0], best[1:], strip, g, min(r[nm]["Dn"] for r in rows if nm in r), min(((r[nm]["Dn"], r["a"], r["b"], r["point"]) for r in rows if nm in r))[1:]))
# 4. slope-2/5 rows and the six's carriers
six = [r for r in rows if r["a"] == "2/5"]
print("slope-2/5 rows %d, lines %d: orders %s" % (len(six), len({r["b"] for r in six}), Counter(order(1, Fr(r["a"]), Fr(r["b"])) for r in six if r["point"] == "g1")))
car = SP.CARRIERS; present = {(r["a"], r["b"]) for r in rows}
print("B1792's six order-60 carriers present:", all(c in present for c in car))
for pkey in ("g1", "g2", "strip"):
    ss = [r for r in six if r["point"] == pkey]
    print("  %s: Dirac min Dn %.2e, LL min Dn %.2e, Dirac exact zeros %d" % (pkey, min(r["Lnuc"]["Dn"] for r in ss), min(r["LL"]["Dn"] for r in ss), sum(r["Lnuc"]["Dn"] < Z for r in ss)))
# slope-2/5 lines of order 15, 20, 30 (carriers at those orders per B1792's base rate) are absent:
absent = [(Fr(2, 5), Fr(k, N)) for N in (15, 20, 30) for k in range(N) if order(1, Fr(2, 5), Fr(k, N)) == N]
print("slope-2/5 lines of exact order 15, 20, 30: %d, of which in the census: %d" % (len(absent), sum((str(a), str(b)) in present for a, b in absent)))
# LL vs B1795's H pair on lines of order dividing 6 (the overlap the arc discloses)
sp_rows = {(r["line"], r["point"]): r for r in (json.loads(l) for l in (ROOT / "frontier/B1795_the_doublet_triplet_split_at_the_canonical_end/verification/split_rows.jsonl").read_text().splitlines() if l.strip())}
dev = []
for r in rows:
    if 6 % r["order"] == 0:
        s = sp_rows[(r["line"], r["point"])]; dev.append(abs(r["LL"]["Dn"] - min(s["H"]["Dn"], s["Hc"]["Dn"])) / r["LL"]["Dn"])
print("LL Dn against B1795's H pair on %d rows of order | 6: max rel dev %.1e" % (len(dev), max(dev)))
# reproduction of a random sample of rows
random.seed(7104); samp = random.sample(rows, 10); worst = 0.0
for r in samp:
    rr = MJ.task((r["line"], r["point"]))
    for nm in ("LL", "Lnuc", "nucnuc"):
        if nm not in r: continue
        for k, v in r[nm].items():
            if isinstance(v, list) and k.startswith("sv"): worst = max(worst, max(abs(p - q) / max(abs(q), 1e-300) for p, q in zip(rr[nm][k], v)))
            elif k == "Dn": worst = max(worst, abs(rr[nm][k] - v) / max(v, 1e-300) if v > 1e-10 else abs(rr[nm][k] - v))
print("reproduction of 10 random rows (sv and Dn, relative): max dev %.1e" % worst)
print("r4 exit 0")
