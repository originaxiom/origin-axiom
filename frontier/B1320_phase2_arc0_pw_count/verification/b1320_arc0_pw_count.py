"""B1320 / Phase 2 Arc 0 -- Pantev-Wijnholt's localized count on the cyclic descent (DESIGN sealed b1f71f45 before this ran).
For the cyclic covers C_3 and C_4 of m004 (SnapPy `covers(d)`, the cyclic ones identified by `cover_info` and by H_1): every isometry (both orientations),
its matrix A on H_1 of the cusp it fixes, |det(A - I)|; the PW localized count of an orientation-preserving cusp-fixing involution is its isolated
fixed-point count |det(A - I)| when non-zero (every isolated fixed point of an orientation-preserving map of the torus has index +1), else 0.
Pre-registered: values on C_3, C_4 subset of {0, 2, 4}; prior 0.95 for exactly {0, 4}; 3 or 6 = the finding. Controls: m004 itself ({0, 4}, the D4 group);
a census manifold with an order-3 cusp rotation must show |det(A - I)| = 3 on the same code path (the positive control)."""
import json, warnings, itertools
warnings.filterwarnings("ignore")
import snappy
def cusp_fixing(N):
    rows = []
    for iso in N.isomorphisms_to(N):
        imgs = iso.cusp_images(); maps = iso.cusp_maps()
        for c, (img, A) in enumerate(zip(imgs, maps)):
            if img != c: continue
            a, b, cc, d = int(A[0, 0]), int(A[0, 1]), int(A[1, 0]), int(A[1, 1]); det = a * d - b * cc; dAmI = abs((a - 1) * (d - 1) - b * cc)
            # order of A
            M = [[1, 0], [0, 1]]; order = None
            for k in range(1, 13):
                M = [[M[0][0]*a + M[0][1]*cc, M[0][0]*b + M[0][1]*d], [M[1][0]*a + M[1][1]*cc, M[1][0]*b + M[1][1]*d]]
                if M == [[1, 0], [0, 1]]: order = k; break
            rows.append(dict(cusp=c, det=det, det_AmI=dAmI, order=order, A=[[a, b], [cc, d]]))
    return rows
def summarize(rows):
    out = {}
    for r in rows:
        key = f"{r['det_AmI']}|det{r['det']:+d}"; out[key] = out.get(key, 0) + 1
    return out
M = snappy.Manifold("m004"); result = dict(design="b1f71f45", base={}, covers={}, control={})
rows = cusp_fixing(M); result["base"] = dict(name="m004", H1=str(M.homology()), n_isometries=len(M.isomorphisms_to(M)), summary=summarize(rows))
print("m004:", result["base"])
for d in (3, 4):
    for i, C in enumerate(M.covers(d)):
        info = C.cover_info(); typ = info.get("type"); H = str(C.homology())
        rows = cusp_fixing(C); s = summarize(rows); vals = sorted({r["det_AmI"] for r in rows}); pres = sorted({r["det_AmI"] for r in rows if r["det"] == 1})
        result["covers"][f"deg{d}_{i}"] = dict(degree=d, index=i, type=typ, H1=H, cusps=C.num_cusps(), n_isometries=len(C.isomorphisms_to(C)), summary=s,
                                             values=vals, values_orientation_preserving=pres, max_order=max([r["order"] or 0 for r in rows] or [0]))
        print(f"degree {d} cover {i}: type {typ}, H1 {H}, cusps {C.num_cusps()}, isometries {len(C.isomorphisms_to(C))}, |det(A-I)| by orientation {s}, orientation-preserving values {pres}")
# the positive control: a census manifold with an order-3 rotation on a cusp it fixes
found = None
for N in (N for k in range(2, 8) for N in snappy.OrientableCuspedCensus(tets=k)):
    rows = cusp_fixing(N)
    hit = [r for r in rows if r["det_AmI"] == 3]
    if hit:
        found = dict(name=N.name(), H1=str(N.homology()), cusps=N.num_cusps(), example=hit[0], summary=summarize(rows)); break
result["control"] = found; print("positive control (first census manifold with |det(A-I)| = 3 on a fixed cusp):", found)
cyc = {k: v for k, v in result["covers"].items() if v["type"] == "cyclic"}
allvals = sorted({x for v in cyc.values() for x in v["values"]})
result["cyclic_values"] = allvals; result["pass"] = set(allvals) <= {0, 2, 4} and found is not None and found["example"]["det_AmI"] == 3
print("cyclic covers:", {k: (v["H1"], v["values"]) for k, v in cyc.items()}); print("PW localized count on the cyclic descent takes the values", allvals, "->", "PASS (subset of {0,2,4}; the control sees a 3)" if result["pass"] else "FAIL")
json.dump(result, open("b1320_arc0_pw_count.json", "w"), indent=1, default=str)
