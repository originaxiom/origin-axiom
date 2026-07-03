"""B377 (Phase 2, leg i) — the derivation-led FULL census at N = 225.

Rep theory predicts an imprimitive slot (W-(3) tensor W-(5) pulled back) at EVERY 3^a 5^b —
the mult-1 census (B374) could not see a sector whose W1-eigenvalues collide with the
primitive spectrum. THE TEST: for every W1-eigenspace pair (E_a, E_{-a}) regardless of
multiplicity, run module closure (span a vector's orbit under the generators to stability)
and record the minimal invariant-module dimension found. A 2-dim hit = the sector EXISTS at
225, invisible to mult-1 (the existence law repairs to 'always exists; PRIME-POWER = VISIBLE');
no hit across a generous probe set = the death stands and the derivation must explain it.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B372_level45_sweeper"))
from fp_engine import Level, primes_1_mod, primitive_root

N = 225


def run():
    p = primes_1_mod(4 * N, 1, start=10**9)[0]
    g = primitive_root(p)
    L = Level(N, p, pow(g, (p - 1) // (4 * N), p))
    W1 = L.W(1)
    o1, pow1 = L.order_powers(W1, cap=1200)          # 300
    tr = [sum(P[i][i] for i in range(N)) % p for P in pow1]
    zo = pow(L.z, (4 * N) // o1, p)
    invo = pow(o1, p - 2, p)
    dims = {a: sum(pow(zo, (-j * a) % o1, p) * tr[j] for j in range(o1)) % p * invo % p
            for a in range(o1)}

    def eigvec(a, seed):
        """P_a applied to a pseudorandom vector (a vector in E_a), mod p."""
        import random
        rnd = random.Random(seed)
        v = [rnd.randrange(1, p) for _ in range(N)]
        out = [0] * N
        w = v[:]                                      # will hold W1^j v iteratively
        for j in range(o1):
            c = pow(zo, (-j * a) % o1, p) * invo % p
            for i in range(N):
                out[i] = (out[i] + c * w[i]) % p
            # w <- W1 w
            w = [sum(W1[i][k] * w[k] for k in range(N)) % p for i in range(N)]
        return out

    def matvec(M, v):
        return [sum(M[i][k] * v[k] for k in range(N)) % p for i in range(N)]

    def closure_dim(vs, cap=6):
        """Row-echelon module closure under D, WR; returns dim (stops past cap)."""
        basis = []                                    # echelonized rows: (pivot, row)
        def add(v):
            v = v[:]
            for piv, row in basis:
                if v[piv]:
                    f = v[piv]
                    v = [(v[i] - f * row[i]) % p for i in range(N)]
            for i in range(N):
                if v[i]:
                    inv = pow(v[i], p - 2, p)
                    v = [x * inv % p for x in v]
                    basis.append((i, v))
                    basis.sort()
                    return True
            return False
        queue = [v for v in vs]
        for v in queue:
            add(v)
        changed = True
        while changed and len(basis) <= cap:
            changed = False
            current = [row for _piv, row in basis]
            for v in current:
                for G_ in (L.D, L.WR):
                    if add(matvec(G_, v)):
                        changed = True
        return len(basis)

    results = {}
    hits = []
    for a in range(1, o1 // 2 + 1):
        b = (o1 - a) % o1
        da, db = dims[a], dims[b]
        if da == 0 or db == 0 or da > 6:
            continue
        best = None
        # probe vectors: a few independent eigenvectors + sums with the opposite side
        for s in range(3):
            va = eigvec(a, 1000 * a + s)
            vb = eigvec(b, 2000 * a + s)
            for probe in ([va], [vb], [va, vb],
                          [[(x + y) % p for x, y in zip(va, vb)]]):
                d = closure_dim(probe)
                if best is None or d < best:
                    best = d
                if best == 2:
                    break
            if best == 2:
                break
        results[a] = dict(dim_a=da, dim_b=db, min_module=best)
        if best == 2:
            hits.append(a)
            print(f"  2-DIM INVARIANT MODULE at exponents ({a},{b})  [mult {da},{db}]", flush=True)
    rep = dict(order=o1, hits=hits,
               tested={str(a): r for a, r in results.items()})
    json.dump(rep, open(os.path.join(HERE, "full_census_225.json"), "w"), indent=1)
    print("HITS:", hits if hits else "NONE — the death stands")
    return rep


if __name__ == "__main__":
    run()
