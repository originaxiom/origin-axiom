"""B392 P-SCALE -- the m=1 singles at level 135 (fp, 2 primes): frozen 1/4 or running?"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B372_level45_sweeper"))
from fp_engine import primes_1_mod, primitive_root

N, o1 = 135, 180
out = {}
for p in primes_1_mod(4*27*5, 2, start=10**9):
    g = primitive_root(p)
    zN = pow(g, (p-1)//N, p)
    zpow = [1]*N
    for k in range(1, N): zpow[k] = zpow[k-1]*zN % p
    Dexp = [(j*(j-1)//2) % N for j in range(N)]
    iN = pow(N, p-2, p)
    def applyD(v, inv=False):
        s = -1 if inv else 1
        return [v[j]*zpow[(s*Dexp[j]) % N] % p for j in range(N)]
    def applyF(v, inv=False):
        s = -1 if inv else 1
        o = [0]*N
        for i in range(N):
            acc = 0
            ii = (s*i) % N
            for j in range(N):
                if v[j]: acc += zpow[(ii*j) % N]*v[j]
            o[i] = acc % p * (iN if inv else 1) % p
        return o
    def applyW1(v):
        return applyD(applyF(applyD(applyF(v, inv=True), inv=True)))
    # W1 as matrix columns, then par-traces of powers
    cols = []
    for j in range(N):
        e = [0]*N; e[j] = 1
        cols.append(applyW1(e))
    W1 = [[cols[j][i] for j in range(N)] for i in range(N)]
    def mm(A, B):
        Bt = list(zip(*B))
        return [[sum(x*y for x, y in zip(r, c)) % p for c in Bt] for r in A]
    trs = []
    P = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    for j in range(o1):
        trs.append(sum(P[(-x) % N][x] for x in range(N)) % p)
        P = mm(P, W1)
    z180 = pow(g, (p-1)//o1, p)
    inv = pow(o1, p-2, p)
    cells = {}
    quarter = pow(4, p-2, p)
    for a in range(o1):
        t = 0
        for j in range(o1):
            t = (t + pow(z180, (-j*a) % o1, p) * trs[j]) % p
        t = t * inv % p
        if t: cells[a] = ("1/4" if t == quarter else f"other({t})")
    out[str(p)] = cells
    print(p, "nonzero singles:", cells, flush=True)
json.dump(out, open(os.path.join(HERE, "p_scale_135.json"), "w"), indent=1)
print("DONE", flush=True)
