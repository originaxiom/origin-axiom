"""Referee B1795, r6: (i) uniqueness of (line, point) rows; (ii) S3 by reading: the H pair's lightest at the strip on the
carriers and on all lines, reading S vs S~; (iii) the multiset symmetry: sorted light_H vs sorted light_D per (point, h, rn)
over the census; (iv) the FINDINGS table's S, L_2 row (missing)."""
import pathlib as _pl; _ROOT = str(next(q for q in _pl.Path(__file__).resolve().parents if (q / 'frontier').is_dir() and (q / 'GENESIS.md').is_file()))
import json, math, pathlib, statistics
V = pathlib.Path(_ROOT + "/frontier/B1795_the_doublet_triplet_split_at_the_canonical_end/verification")
rows = [json.loads(l) for l in (V / "split_rows.jsonl").read_text().splitlines() if l.strip()]
print("unique (line, point):", len({(r["line"], r["point"]) for r in rows}), "of", len(rows), "| unique (a,b):", len({(r["a"], r["b"]) for r in rows}))
CARR = {("2/5", "11/12"), ("2/5", "29/60"), ("2/5", "41/60"), ("2/5", "47/60"), ("2/5", "49/60"), ("2/5", "7/60")}
def lt(r, ps, h, rn): return min(r[p]["sv|%s|%s" % (h, rn)][2] / r[p]["sv|%s|%s" % (h, rn)][0] for p in ps)
for sel_name, sel in (("carriers", lambda r: (r["a"], r["b"]) in CARR), ("all lines", lambda r: True)):
    st = [r for r in rows if r["point"] == "strip" and sel(r)]
    for h in ("L_max", "L_2"):
        for rn in ("S", "St"):
            vH = [lt(r, ("H", "Hc"), h, rn) for r in st]; vD = [lt(r, ("D", "Dc"), h, rn) for r in st]
            print("strip %-9s %-5s %-2s: light_H %.1e - %.1e (frac < 1e-3: %.2f) | light_D %.1e - %.1e" % (sel_name, h, rn, min(vH), max(vH), sum(v < 1e-3 for v in vH) / len(vH), min(vD), max(vD)))
dev = 0.0
for pk in ("g1", "g2", "strip"):
    for h in ("L_max", "L_2"):
        for rn in ("S", "St"):
            a = sorted(lt(r, ("H", "Hc"), h, rn) for r in rows if r["point"] == pk); b = sorted(lt(r, ("D", "Dc"), h, rn) for r in rows if r["point"] == pk)
            d = max(abs(math.log10(x / y)) for x, y in zip(a, b)); dev = max(dev, d)
            qa = [a[int(q * len(a))] for q in (0.1, 0.5, 0.9)]; qb = [b[int(q * len(b))] for q in (0.1, 0.5, 0.9)]
print("multiset symmetry: max |log10| between sorted light_H and sorted light_D over the census, any (point, h, rn): %.3f" % dev)
for pk in ("g1", "g2", "strip"):
    a = sorted(min(r["H"]["Dn"], r["Hc"]["Dn"]) for r in rows if r["point"] == pk); b = sorted(min(r["D"]["Dn"], r["Dc"]["Dn"]) for r in rows if r["point"] == pk)
    print(pk, "sorted Dn_H vs Dn_D: max |log10| %.3f" % max(abs(math.log10(x / y)) for x, y in zip(a, b)))
