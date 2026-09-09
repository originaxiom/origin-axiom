"""B1302 Q3: SnapPy's 12 isometries of m202: cusp permutations and cusp maps; |Fix| per cusp = |det(A - I)| and chat1's law det(A - I) = 2 - tr A
on every cusp map; the Z/6 of cusp-preserving isometries gives (1, 3, 4) fixed points per cusp for orders (6, 3, 2) -- fc R72 §4."""
import json, warnings
warnings.filterwarnings("ignore")
import snappy, numpy as np
M = snappy.Manifold("m202"); isos = M.isomorphisms_to(M); print("isometries:", len(isos))
rows = []
for iso in isos:
    cm = iso.cusp_maps(); perm = iso.cusp_images()
    dets = []
    for A in cm:
        a = np.array([[int(A[0, 0]), int(A[0, 1])], [int(A[1, 0]), int(A[1, 1])]])
        dets.append((int(round(np.linalg.det(a))), int(np.trace(a)), int(round(np.linalg.det(a - np.eye(2, dtype=int))))))
    rows.append(dict(perm=list(perm), maps=[[[int(A[i, j]) for j in range(2)] for i in range(2)] for A in cm], det_tr_fix=dets))
# orders of the cusp-preserving ones from their cusp maps (finite order in GL(2,Z))
def order(a):
    a = np.array(a); P = np.eye(2, dtype=int)
    for k in range(1, 13):
        P = P @ a
        if (P == np.eye(2, dtype=int)).all(): return k
    return None
law_ok = True; table = {}
for r in rows:
    for (d, t, f), m in zip(r["det_tr_fix"], r["maps"]):
        law_ok &= (f == 2 - t) if d == 1 else True
    if r["perm"] == [0, 1]:
        o = order(r["maps"][0]); table.setdefault(o, set()).add(tuple(abs(f) for _, _, f in r["det_tr_fix"]))
pres = sum(1 for r in rows if r["perm"] == [0, 1]); swaps = len(rows) - pres
print("cusp-preserving:", pres, " cusp-swapping:", swaps, " all cusp maps det +1 (orientation-preserving):", all(d == 1 for r in rows for d, _, _ in r["det_tr_fix"]))
print("|Fix| per cusp by order of the cusp-preserving isometry:", {o: sorted(v) for o, v in table.items()}, " [fc: r:1, r^2:3, r^3:4]")
print("law det(A - I) = 2 - tr A on every det-1 cusp map:", law_ok)
ok = law_ok and table.get(3) == {(3, 3)} and table.get(2) == {(4, 4)} and table.get(6) == {(1, 1)} and table.get(1) == {(0, 0)}
json.dump(dict(rows=rows, table={str(k): sorted(v) for k, v in table.items()}, law=law_ok), open("b1302_cuspmaps.json", "w"))
print("Q3:", "PASS" if ok else "FAIL")
