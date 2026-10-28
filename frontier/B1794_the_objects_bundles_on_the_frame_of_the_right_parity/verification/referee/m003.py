import snappy
from math import gcd
for name in ["m003"]:
    M = snappy.Manifold(name); print(name, "H1 =", M.homology())
    hits = []
    for p in range(-8, 9):
        for q in range(0, 9):
            if (p, q) == (0, 0) or gcd(abs(p), q) != 1 or (q == 0 and p != 1): continue
            N = snappy.Manifold(name); N.dehn_fill((p, q))
            ed = N.homology().elementary_divisors()
            if any(c == 0 for c in ed): hits.append((p, q))
    print("  b1>0 slopes on grid:", hits)
    for p, q in hits:
        N = snappy.Manifold(name); N.dehn_fill((p, q)); best = N.solution_type()
        for k in range(40):
            if best == "all tetrahedra positively oriented": break
            N.randomize(); best = N.solution_type()
        print("  filling", (p, q), "H1 =", N.homology(), "| solution type:", best, "| volume:", N.volume())
