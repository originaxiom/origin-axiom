"""The N=225 rung — pure data for the phase-map riddle (NO phase prediction registered;
the only registered expectation: a unique invariant 2-state sector exists, ord = 4N/3)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "B372_level45_sweeper"))
from rung135 import projector, projector_dim, invariant
from fp_engine import Level, primes_1_mod, primitive_root

N = 225
primes = primes_1_mod(4 * N, 3, start=10**9)
res = {}
for pi, p in enumerate(primes):
    g = primitive_root(p)
    L = Level(N, p, pow(g, (p - 1) // (4 * N), p))
    W1 = L.W(1)
    o1, pow1 = L.order_powers(W1, cap=1200)
    if pi == 0:
        dims = {a: projector_dim(L, pow1, a) for a in range(o1)}
        mult1 = [a for a in range(1, o1 // 2) if dims[a] == 1 and dims[(o1 - a) % o1] == 1]
        sectors = []
        for a in mult1:
            Pa, Pb = projector(L, pow1, a), projector(L, pow1, (o1 - a) % o1)
            P = [[(Pa[i][j] + Pb[i][j]) % p for j in range(N)] for i in range(N)]
            if invariant(P, L):
                sectors.append((a, (o1 - a) % o1))
        res = dict(order=o1, n_mult1=len(mult1), sectors=sectors)
        print("census:", res, flush=True)
    else:
        for a, b in res["sectors"]:
            Pa, Pb = projector(L, pow1, a), projector(L, pow1, b)
            P = [[(Pa[i][j] + Pb[i][j]) % p for j in range(N)] for i in range(N)]
            assert invariant(P, L), (p, a, b)
        print(f"confirmed mod {p}", flush=True)
res["cross_prime_confirmed"] = True
for a, b in res["sectors"]:
    res[f"phase_deg_{a}"] = 360 * a / res["order"]
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "rung225.json"), "w"), indent=1)
print("DONE", res)
