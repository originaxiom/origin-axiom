"""B1984 (main, 2026-11-25; data-free): the Fricke maps L, R acting together on (Z/N)^3 for every N from 2 to 64; on the
cusp's leaf (kappa = x^2 + y^2 + z^2 - xyz - 2 = -2 mod N) the orbits and the points every move fixes; per N the number of
leaves left in several pieces. Exact. See ../CARD.md.
    python3 -B listen2.py > listen2_run.txt"""
import json, pathlib, time
def run(N):
    L = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N)
    R = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
    pts = [(x, y, z) for x in range(N) for y in range(N) for z in range(N)]
    kap = {v: (v[0] * v[0] + v[1] * v[1] + v[2] * v[2] - v[0] * v[1] * v[2] - 2) % N for v in pts}
    for f in (L, R):
        img = [f(v) for v in pts]; assert len(set(img)) == len(pts) and all(kap[w] == kap[v] for v, w in zip(pts, img))
    seen, by = set(), {}
    for v in pts:
        if v in seen: continue
        orb, st = {v}, [v]
        while st:
            u = st.pop()
            for f in (L, R):
                w = f(u)
                if w not in orb: orb.add(w); st.append(w)
        seen |= orb; by.setdefault(kap[v], []).append(len(orb))
    fixed = [v for v in pts if L(v) == v and R(v) == v]
    cusp = sorted(by.get((-2) % N, []), reverse=True)
    split = sum(1 for k, s in by.items() if sum(1 for x in s if x > 1) > 1)
    return cusp, fixed, split, len(by)
t0 = time.time(); res = {}
for N in range(2, 65):
    cusp, fixed, split, leaves = run(N)
    big = [s for s in cusp if s > 1]
    res[N] = dict(cusp=cusp, fixed=fixed, split=split, leaves=leaves, connected=len(big) == 1)
    print("N = %2d: cusp leaf: %d points, orbits of size > 1 %s, singletons %d; fixed by every move %s; leaves in several pieces %d of %d  [%.0f s]" % (
        N, sum(cusp), big[:8] + (["..."] if len(big) > 8 else []), sum(1 for s in cusp if s == 1), fixed[:6], split, leaves, time.time() - t0), flush=True)
json.dump({str(k): v for k, v in res.items()}, open(pathlib.Path(__file__).with_name("listen2_run.json"), "w"))
cop = [N for N in range(2, 65) if N % 2 and N % 3]
print("SUMMARY F1: N coprime to 6 with the cusp's leaf one orbit apart from fixed points: %d of %d; not: %s" % (sum(res[N]["connected"] for N in cop), len(cop), [N for N in cop if not res[N]["connected"]]))
print("SUMMARY: N whose cusp leaf is NOT one orbit (apart from singletons): %s" % [N for N in range(2, 65) if not res[N]["connected"]])
print("SUMMARY C1: primes 5..47 connected: %s; N = 3 cusp leaf %s" % (all(res[p]["connected"] for p in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)), res[3]["cusp"]))
