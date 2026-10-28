"""Referee B1795, r2: per-line comparison of the H and D pairs (read-only on split_rows.jsonl).  Where are the extreme
light_H / light_D ratios; is the median-1 statistic forced by a relabelling symmetry of the line set (D on lambda*l = H on
l when gcd(order, 6) = 1); do the slope-2/5 lines (the carriers) share the twist's a-component between the two pairs."""
import pathlib as _pl; _ROOT = str(next(q for q in _pl.Path(__file__).resolve().parents if (q / 'frontier').is_dir() and (q / 'GENESIS.md').is_file()))
import json, math, statistics, pathlib
from fractions import Fraction as Fr
V = pathlib.Path(_ROOT + "/frontier/B1795_the_doublet_triplet_split_at_the_canonical_end/verification")
rows = [json.loads(l) for l in (V / "split_rows.jsonl").read_text().splitlines() if l.strip()]
HR = [(h, rn) for h in ("L_max", "L_2") for rn in ("S", "St")]
def r31(s, h, rn): v = s["sv|%s|%s" % (h, rn)]; return v[2] / v[0]
def light(r, ps, h, rn): return min(r31(r[p], h, rn) for p in ps)
def lightall(r, ps): return min(light(r, ps, h, rn) for h, rn in HR)
CARR = {("2/5", "11/12"), ("2/5", "29/60"), ("2/5", "41/60"), ("2/5", "47/60"), ("2/5", "49/60"), ("2/5", "7/60")}
strip = [r for r in rows if r["point"] == "strip"]
# extremes at the strip, per line, min over horocycle and reading
ext = sorted(strip, key=lambda r: math.log10(lightall(r, ("H", "Hc")) / lightall(r, ("D", "Dc"))))
print("strip: lines with the most extreme light_H/light_D (min over horocycles, readings, slot orders):")
for r in ext[:6] + ext[-6:]:
    print("  (%s, %s) order %2d  light_H %.2e  light_D %.2e  ratio 10^%+.2f  Dn_H %.2e Dn_D %.2e" % (r["a"], r["b"], r["order"], lightall(r, ("H", "Hc")), lightall(r, ("D", "Dc")), math.log10(lightall(r, ("H", "Hc")) / lightall(r, ("D", "Dc"))), r["H"]["Dn"], r["D"]["Dn"]))
# per (h, rn) extremes (as pair_compare)
lr = [(math.log10(light(r, ("H", "Hc"), h, rn) / light(r, ("D", "Dc"), h, rn)), r["a"], r["b"], h, rn, light(r, ("H", "Hc"), h, rn), light(r, ("D", "Dc"), h, rn)) for r in strip for h, rn in HR]
lr.sort()
print("strip per (h, rn): min", lr[0], "\n                     max", lr[-1])
# how many lines at the strip have one pair light (< 1e-3) and the other heavy (> 1e-2) in the same (h, rn)?
cnt = {"H light, D heavy": [], "D light, H heavy": []}
for r in strip:
    for h, rn in HR:
        lh, ld = light(r, ("H", "Hc"), h, rn), light(r, ("D", "Dc"), h, rn)
        if lh < 1e-3 and ld > 1e-2: cnt["H light, D heavy"].append((r["a"], r["b"], h, rn, "%.1e" % lh, "%.1e" % ld))
        if ld < 1e-3 and lh > 1e-2: cnt["D light, H heavy"].append((r["a"], r["b"], h, rn, "%.1e" % lh, "%.1e" % ld))
for k, v in cnt.items(): print("strip, %s (light < 1e-3, heavy > 1e-2): %d (line,h,rn) cells on %d lines; e.g. %s" % (k, len(v), len({x[:2] for x in v}), v[:4]))
# the same at the generic points
for pk in ("g1", "g2"):
    c = {"H light, D heavy": 0, "D light, H heavy": 0}; ln = {"H light, D heavy": set(), "D light, H heavy": set()}
    for r in rows:
        if r["point"] != pk: continue
        for h, rn in HR:
            lh, ld = light(r, ("H", "Hc"), h, rn), light(r, ("D", "Dc"), h, rn)
            if lh < 1e-3 and ld > 1e-2: c["H light, D heavy"] += 1; ln["H light, D heavy"].add((r["a"], r["b"]))
            if ld < 1e-3 and lh > 1e-2: c["D light, H heavy"] += 1; ln["D light, H heavy"].add((r["a"], r["b"]))
    print(pk, {k: (v, len(ln[k])) for k, v in c.items()})
# the symmetry: D on line lambda*l equals H on l, lambda = -3/2 mod N, for gcd(N, 6) = 1.  Test at the level of Dn, sv
def canon(a, b):
    a, b = Fr(a) % 1, Fr(b) % 1; m = ((-a) % 1, (-b) % 1); return min((a, b), m)
by = {(canon(r["a"], r["b"]), r["point"]): r for r in rows}
dev, n = 0.0, 0
for r in rows:
    N = r["order"]
    if math.gcd(N, 6) != 1 or N == 1: continue
    lam = (-3 * pow(2, -1, N)) % N
    a, b = Fr(r["a"]), Fr(r["b"]); key = (canon(lam * a, lam * b), r["point"])
    if key not in by: continue
    r2 = by[key]; n += 1
    dev = max(dev, abs(r2["D"]["Dn"] - r["H"]["Dn"]) / r["H"]["Dn"], max(abs(min(r31(r2[p], h, rn) for p in ("D", "Dc")) - min(r31(r[p], h, rn) for p in ("H", "Hc"))) / min(r31(r[p], h, rn) for p in ("H", "Hc")) for h, rn in HR))
print("relabelling symmetry D(lambda l) = H(l), lambda = -3/2 mod N, gcd(N,6)=1: %d rows checked, max rel dev %.2e" % (n, dev))
# which lines fall under it, which not
cover = sum(1 for r in strip if math.gcd(r["order"], 6) == 1)
print("strip rows with gcd(order, 6) = 1: %d of %d" % (cover, len(strip)))
# median contributions: exact ties
ties = sum(1 for x in lr if abs(x[0]) < 1e-9); print("strip per-(h,rn) exact ties |log ratio| < 1e-9: %d of %d" % (ties, len(lr)))
# slope-2/5 lines: shared a-component; the 20 order-60 lines vs others at the strip
def spread(sel):
    v = [abs(math.log10(light(r, ("H", "Hc"), h, rn) / light(r, ("D", "Dc"), h, rn))) for r in strip if sel(r) for h, rn in HR]
    return len(v), statistics.median(v), max(v)
print("strip |log10 ratio| (n, median, max): slope 2/5 order 60:", spread(lambda r: r["a"] == "2/5" and r["order"] == 60),
      "| 5 | denom(a) (a-component shared), order != 1,5:", spread(lambda r: (Fr(r["a"]) * 5).denominator == 1 and r["order"] not in (1, 5)),
      "| the rest:", spread(lambda r: (Fr(r["a"]) * 5).denominator != 1))
for pk in ("g1", "g2"):
    sub = [r for r in rows if r["point"] == pk]
    def spr(sel):
        v = [abs(math.log10(light(r, ("H", "Hc"), h, rn) / light(r, ("D", "Dc"), h, rn))) for r in sub if sel(r) for h, rn in HR]
        return len(v), round(statistics.median(v), 3), round(max(v), 3)
    print(pk, "slope 2/5 o60:", spr(lambda r: r["a"] == "2/5" and r["order"] == 60), "| rest (5 not | denom a):", spr(lambda r: (Fr(r["a"]) * 5).denominator != 1))
# the six carriers vs the other 14 order-60 lines at the strip: the light states
o60 = [r for r in strip if r["order"] == 60]
print("strip, order-60 lines: light_H (L_max,S) range carriers %s / others %s" % (
    ("%.1e-%.1e" % (min(light(r, ("H", "Hc"), "L_max", "S") for r in o60 if (r["a"], r["b"]) in CARR), max(light(r, ("H", "Hc"), "L_max", "S") for r in o60 if (r["a"], r["b"]) in CARR))),
    ("%.1e-%.1e" % (min(light(r, ("H", "Hc"), "L_max", "S") for r in o60 if (r["a"], r["b"]) not in CARR), max(light(r, ("H", "Hc"), "L_max", "S") for r in o60 if (r["a"], r["b"]) not in CARR)))))
# where is min Dn
mH = min(rows, key=lambda r: min(r["H"]["Dn"], r["Hc"]["Dn"])); mD = min(rows, key=lambda r: min(r["D"]["Dn"], r["Dc"]["Dn"]))
print("min Dn_H at (%s,%s) %s order %d: %.4e ; min Dn_D at (%s,%s) %s order %d: %.4e" % (mH["a"], mH["b"], mH["point"], mH["order"], mH["H"]["Dn"], mD["a"], mD["b"], mD["point"], mD["order"], mD["D"]["Dn"]))
# distribution of Dn
for pk in ("g1", "g2", "strip"):
    v = sorted(min(r[p]["Dn"] for p in ("H", "Hc")) for r in rows if r["point"] == pk)
    print(pk, "Dn_H: min %.2e  1%% %.2e  median %.2e" % (v[0], v[len(v) // 100], v[len(v) // 2]))
# S3 at the strip: is the light state common to all lines (pair-independent)?  light_H over all 286 lines at the strip
v = sorted(lightall(r, ("H", "Hc")) for r in strip)
print("strip, all lines: min over (h, rn) of light_H: min %.1e median %.1e max %.1e; fraction < 1e-3: %.2f" % (v[0], v[len(v) // 2], v[-1], sum(x < 1e-3 for x in v) / len(v)))
for pk in ("g1", "g2"):
    v = sorted(lightall(r, ("H", "Hc")) for r in rows if r["point"] == pk)
    print(pk, "all lines: light_H min %.1e median %.1e max %.1e; fraction < 1e-3: %.2f" % (v[0], v[len(v) // 2], v[-1], sum(x < 1e-3 for x in v) / len(v)))
