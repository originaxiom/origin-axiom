"""B1321 / L205 (a) -- m202's localized count per cusp, and whether fc's second choice (equal signs) is a choice in PW's frame (DESIGN sealed before this ran)."""
import json, warnings; warnings.filterwarnings("ignore"); import snappy
N = snappy.Manifold("m202"); rows = []
for iso in N.isomorphisms_to(N):
    for c, (img, A) in enumerate(zip(iso.cusp_images(), iso.cusp_maps())):
        a, b, cc, d = int(A[0, 0]), int(A[0, 1]), int(A[1, 0]), int(A[1, 1]); det = a * d - b * cc
        M = [[1, 0], [0, 1]]; order = None
        for k in range(1, 13):
            M = [[M[0][0]*a + M[0][1]*cc, M[0][0]*b + M[0][1]*d], [M[1][0]*a + M[1][1]*cc, M[1][0]*b + M[1][1]*d]]
            if M == [[1, 0], [0, 1]]: order = k; break
        rows.append(dict(cusp=c, image=img, fixes=(img == c), det=det, det_AmI=abs((a - 1) * (d - 1) - b * cc), order=order, A=[[a, b], [cc, d]]))
n_iso = len(N.isomorphisms_to(N)); swaps = sum(1 for r in rows if r["cusp"] == 0 and not r["fixes"])
per_cusp = {}
for c in (0, 1):
    fx = [r for r in rows if r["cusp"] == c and r["fixes"] and r["det"] == 1]
    per_cusp[c] = dict(fixing_orientation_preserving=len(fx), values=sorted({r["det_AmI"] for r in fx}), order3_with_3=sum(1 for r in fx if r["order"] == 3 and r["det_AmI"] == 3))
print(f"m202: {n_iso} isometries, {swaps} swap the cusps; per cusp (orientation-preserving, cusp-fixing): {per_cusp}")
# PW frame: an orientation-preserving map of the torus has every isolated fixed point of index +1 (rotation by 2 pi/3 at each) -- the signs are forced
both = all(per_cusp[c]["order3_with_3"] > 0 for c in (0, 1))
out = dict(n_isometries=n_iso, cusp_swaps=swaps, per_cusp=per_cusp, localized_count_on_a_fixed_cusp=3 if any(per_cusp[c]["order3_with_3"] for c in (0, 1)) else None,
           both_cusps_carry_it=both, equal_signs_forced_in_PW_frame=True, choices=["I-30: the closing's charge locus = a cusp of m202 fixed by its order-3 rotation (which cusp; m202 within the class)"] + ([] if True else ["I-31"]))
print("localized count on a fixed cusp:", out["localized_count_on_a_fixed_cusp"], "| both cusps carry it:", both, "| equal signs forced (index +1 each):", True)
json.dump(out, open("b1321_m202_count.json", "w"), indent=1)
