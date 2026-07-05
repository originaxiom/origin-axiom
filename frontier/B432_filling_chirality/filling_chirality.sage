# B432 -- Phase I.1: chirality is INTERFACE-SOURCED. The amphichiral object (CS=0) becomes
# CHIRAL under every sampled hyperbolic Dehn filling: 31/31 fillings have generic CS
# (none in {0,1/2} mod 1). Mechanism: external slope input breaks the self-mirror -- exactly
# the postulate's interface prediction. Bar-honest: confirms the MECHANISM (source exists);
# the slope is free input, so leg (i) FORCED is not cleared by breaking alone; the
# slope-selection question (does the object's arithmetic select a slope? cf. B225's golden 5)
# is the registered follow-on. Method notes: CS must be initialized on the CUSPED manifold
# before filling; sage float % can return negatives (classifier must use x-floor(x)).
import snappy, math, json
M0 = snappy.Manifold('4_1'); cs0 = float(M0.chern_simons())
rows = []
for p in range(0, 8):
    for q in range(1, 8):
        if math.gcd(p, q) != 1: continue
        M = M0.copy(); M.dehn_fill((p, q))
        try:
            v = float(M.volume())
            if v < 0.3: continue
            cs = float(M.chern_simons()); cs = cs - math.floor(cs)
            d = min(cs, 1 - cs, abs(cs - 0.5))
            rows.append(dict(p=p, q=q, vol=round(v, 6), cs=round(cs, 9), chiral=bool(d > 1e-8)))
        except Exception:
            continue
n_ch = sum(1 for r in rows if r["chiral"])
print("cusped CS =", cs0, " fillings:", len(rows), " chiral:", n_ch)
json.dump(dict(cusped_cs=cs0, n=len(rows), n_chiral=n_ch, rows=rows),
          open("frontier/B432_filling_chirality/filling_chirality.json", "w"), indent=1)
