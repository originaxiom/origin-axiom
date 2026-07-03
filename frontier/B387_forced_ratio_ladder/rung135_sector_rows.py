"""B387 continuation (named in the prereg's KILL branch): the 135 rung's sector rows.

The banked 135 value sector sits at W1-exponents {54,126} of ord(W1@135)=180 (B374), phase
+-108 deg. Compute the slot-analog graded cells t(54,b), t(126,b), b in {2,10}, at level 135
mod 3 primes (fp CRT), and decide: nonzero (ladder lives; identify exactly and compare) or
zero (the seam leaves the value sector above 15 -- a structural verdict).
Route: C-table = par-traces of W1^j W2^l over the 180x12 grid mod p; DFT the four cells;
report zero/nonzero per prime (agreement across 3 primes = the verdict; identification only
if nonzero)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B372_level45_sweeper"))
from fp_engine import primes_1_mod, primitive_root

N = 135
def run():
    primes = primes_1_mod(4 * 27 * 5, 3, start=10**9)   # zeta_{540} needs: 4*135=540 | p-1
    out = {}
    for p in primes:
        g = primitive_root(p)
        zN = pow(g, (p - 1) // N, p)
        # theta model at 135: D = diag zN^{j(j-1)/2}; WR = F D^{-1} F^{-1}; W_m = WR^m D^m
        Dexp = [ (j*(j-1)//2) % N for j in range(N) ]
        iN = pow(N, p - 2, p)
        zpow = [1]*N
        for k in range(1, N): zpow[k] = zpow[k-1]*zN % p
        def applyD(v, m=1, inv=False):
            s = -m if inv else m
            return [v[j]*zpow[(s*Dexp[j]) % N] % p for j in range(N)]
        def applyF(v, inv=False):
            s = -1 if inv else 1
            out_ = [0]*N
            for i in range(N):
                acc = 0
                ii = (s*i) % N
                for j in range(N):
                    if v[j]: acc += zpow[(ii*j) % N]*v[j]
                out_[i] = acc % p * (iN if inv else 1) % p
            return out_
        def applyW(v, m):
            for _ in range(m):
                v = applyF(applyD(applyF(v, inv=True), 1, inv=True))
            return applyD(v, m)
        # build W1, W2 as matrices via columns (135 columns x a few applies) -- fine
        def mat_of(mfun):
            cols = []
            for j in range(N):
                e = [0]*N; e[j] = 1
                cols.append(mfun(e))
            return [[cols[j][i] for j in range(N)] for i in range(N)]
        W1 = mat_of(lambda v: applyW(v, 1))
        W2 = mat_of(lambda v: applyW(v, 2))
        def mm(A, B):
            Bt = list(zip(*B))
            return [[sum(x*y for x, y in zip(r, c)) % p for c in Bt] for r in A]
        # C-table par traces over j in Z180, l in Z12: iterate powers
        o1, o2 = 180, 12
        # precompute W2 powers (12), then walk W1 powers once, tracing par(W1^j W2^l)
        W2p = [[[1 if i == j else 0 for j in range(N)] for i in range(N)]]
        for _ in range(o2 - 1): W2p.append(mm(W2p[-1], W2))
        C = {}
        P = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
        for j in range(o1):
            for l in range(o2):
                # tr(Par * P * W2^l) = sum_{x,y} P[-x, y] * W2p[l][y, x]  -- O(N^2), no mmul
                B = W2p[l]
                t = 0
                for x in range(N):
                    Prow = P[(-x) % N]
                    t = (t + sum(Prow[y] * B[y][x] for y in range(N))) % p
                C[(j, l)] = t
            P = mm(P, W1)
            if (j + 1) % 30 == 0:
                print(f"  prime {p}: row {j+1}/180 done", flush=True)
        # DFT the four cells
        z180 = pow(g, (p-1)//180, p); z12 = pow(g, (p-1)//12, p)
        inv = pow(o1*o2, p-2, p)
        res = {}
        for a in (54, 126):
            for b in (2, 10):
                t = 0
                for j in range(o1):
                    za = pow(z180, (-j*a) % 180, p)
                    for l in range(o2):
                        t = (t + za * pow(z12, (-l*b) % 12, p) * C[(j, l)]) % p
                res[f"{a},{b}"] = t * inv % p
        out[str(p)] = {k: ("zero" if v == 0 else "NONZERO") for k, v in res.items()}
        print(p, out[str(p)], flush=True)
    json.dump(out, open(os.path.join(HERE, "rung135_sector_rows.json"), "w"), indent=1)
    print("DONE", flush=True)

run()
