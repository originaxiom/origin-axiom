#!/usr/bin/env python3
"""B1493 -- the 512 characters mu_8^3 of L8a15 (H_1 = Z^3 on (a, b, c)) sorted into orbits under the isometry group's action
on H_1 (12 elements, from the cusp maps; the meridians are a basis, det -1) and Galois conjugation zeta -> zeta^k; writes
orbits_L8a15.json: one representative per orbit with its order, its orbit, and the ends on which it is trivial."""
import json, math, itertools, pathlib
import numpy as np, snappy
HERE = pathlib.Path(__file__).resolve().parent
M = snappy.Manifold("L8a15"); G = M.fundamental_group()
def ev(w):
    v = [0] * 3
    for ch in w: v["abc".index(ch.lower())] += 1 if ch.islower() else -1
    return np.array(v)
cusps = G.peripheral_curves(); MU = [ev(m) for m, l in cusps]; LA = [ev(l) for m, l in cusps]
B = np.array(MU).T; assert abs(round(np.linalg.det(B))) == 1; Binv = np.linalg.inv(B)
grp = set()
for iso in M.is_isometric_to(M, return_isometries=True):
    imgs = iso.cusp_images(); maps = iso.cusp_maps()
    X = [np.array([[int(maps[i][r][c]) for c in range(2)] for r in range(2)]) for i in range(3)]
    A = np.rint(np.array([X[i][0, 0] * MU[imgs[i]] + X[i][1, 0] * LA[imgs[i]] for i in range(3)]).T @ Binv).astype(int)
    ok = all(np.array_equal(A @ LA[i], X[i][0, 1] * MU[imgs[i]] + X[i][1, 1] * LA[imgs[i]]) for i in range(3))
    if ok and abs(round(np.linalg.det(A))) == 1: grp.add(tuple(tuple(int(x) for x in row) for row in A))
assert len(grp) == 12
inv = {m: tuple(map(tuple, np.rint(np.linalg.inv(np.array(m))).astype(int))) for m in grp}
def order(c): return 1 if not any(c) else max(8 // math.gcd(8, x) for x in c if x)
def trivial_ends(c):
    out = []
    for i in range(3): out.append(bool(int(np.dot(c, MU[i])) % 8 == 0 and int(np.dot(c, LA[i])) % 8 == 0))
    return out
seen = set(); orbits = []
for c in sorted(itertools.product(range(8), repeat=3)):
    if c in seen: continue
    orb = set()
    for m in grp:
        v = np.array(c) @ np.array(inv[m])
        for k in (1, 3, 5, 7): orb.add(tuple(int(x) % 8 for x in k * v))
    seen |= orb; rep = tuple(int(x) for x in min(orb)); orbits.append(dict(rep=rep, order=order(rep), size=len(orb), trivial_ends=trivial_ends(rep), orbit=[[int(x) for x in c] for c in sorted(orb)]))
json.dump(dict(group_on_H1=sorted(grp), orbits=orbits, count=len(orbits), by_order={o: sum(1 for x in orbits if x["order"] == o) for o in (1, 2, 4, 8)}), open(HERE / "orbits_L8a15.json", "w"), indent=1)
print(len(orbits), {o: sum(1 for x in orbits if x["order"] == o) for o in (1, 2, 4, 8)})
