"""B360 -- the selection-rule prediction test (pre-registered in B359):
   (1,4) BRIGHT ; (3,5) DARK ; and (2,4) discriminates the rule's two readings
   ("contains an even seed" => bright  vs  "opposite parity" => dark).
Theta lift, exact Fraction arithmetic; fast O(N^2) Par-trace path."""
from fractions import Fraction as Fr
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "B358_seam_certification"))
from cyclo_engine import (DEG, add, sub, scal, mul, ZERO, ONE, zeta, e15,
                        SQRT5, SQRTm3, SQRTm15, mmul, SQRT15)

N = 15


def is_identity(M):
    for i in range(N):
        for j in range(N):
            if M[i][j] != (ONE if i == j else ZERO):
                return False
    return True


def theta_gens():
    D = [[ZERO for _ in range(N)] for _ in range(N)]
    Di = [[ZERO for _ in range(N)] for _ in range(N)]
    for j in range(N):
        t = (j * (j - 1)) // 2
        D[j][j] = e15(t)
        Di[j][j] = e15(-t)
    INV_SQRT15 = scal(Fr(1, 15), SQRT15)
    F = [[mul(e15(i * j), INV_SQRT15) for j in range(N)] for i in range(N)]
    Fi = [[mul(e15(-i * j), INV_SQRT15) for j in range(N)] for i in range(N)]
    WR = mmul(mmul(F, Di), Fi)
    return WR, D


def word_power(base, m):
    out = base
    for _ in range(m - 1):
        out = mmul(out, base)
    return out


def powers(W, nmax=64):
    """powers until identity; returns list [I, W, ..., W^{n-1}] with W^n = I."""
    out = [[[ONE if i == j else ZERO for j in range(N)] for i in range(N)]]
    cur = W
    for _ in range(nmax):
        out.append(cur)
        nxt = mmul(cur, W)
        if is_identity(nxt):
            return out
        cur = nxt
    raise AssertionError("order > nmax")


def par_trace_fast(A, B):
    """tr(Par * A * B) = sum_{x,y} A[-x,y] B[y,x]  -- O(N^2) entry products."""
    t = ZERO
    for x in range(N):
        Ax = A[(-x) % N]
        for y in range(N):
            a = Ax[y]
            if any(a):
                b = B[y][x]
                if any(b):
                    t = add(t, mul(a, b))
    return t


GAL_H = [1, 19, 31, 49]


def sigma(a, c):
    out = [Fr(0)] * DEG
    for k in range(DEG):
        if a[k]:
            out = add(out, scal(a[k], zeta((c * k) % 60)))
    return out


def solve_H(t):
    cols = [ONE, SQRT5, SQRTm3, SQRTm15]
    Ab = [[cols[c][row] for c in range(4)] + [t[row]] for row in range(DEG)]
    r = 0
    piv = []
    for c in range(4):
        p = next((i for i in range(r, DEG) if Ab[i][c] != 0), None)
        if p is None:
            continue
        Ab[r], Ab[p] = Ab[p], Ab[r]
        pv = Ab[r][c]
        Ab[r] = [v / pv for v in Ab[r]]
        for i in range(DEG):
            if i != r and Ab[i][c] != 0:
                f = Ab[i][c]
                Ab[i] = [Ab[i][j] - f * Ab[r][j] for j in range(5)]
        piv.append(c)
        r += 1
    sol = [Fr(0)] * 4
    for i, c in enumerate(piv):
        sol[c] = Ab[i][4]
    for i in range(r, DEG):
        if Ab[i][4] != 0:
            return None
    return tuple(sol)


ZEXP = {20: 3, 12: 5, 10: 6, 6: 10, 5: 12, 4: 15, 2: 30, 3: 20, 15: 4, 30: 2, 60: 1}


def pair_readout(Wa_p, Wb_p):
    na, nb = len(Wa_p), len(Wb_p)
    za, zb = ZEXP[na], ZEXP[nb]
    C = [[par_trace_fast(Wa_p[j], Wb_p[l]) for l in range(nb)] for j in range(na)]
    out = {}
    for a in range(na):
        for b in range(nb):
            t = ZERO
            for j in range(na):
                zja = zeta((-za * j * a) % 60)
                for l in range(nb):
                    t = add(t, mul(mul(zja, zeta((-zb * l * b) % 60)), C[j][l]))
            t = scal(Fr(1, na * nb), t)
            if t == ZERO:
                continue
            avg = ZERO
            for c in GAL_H:
                avg = add(avg, sigma(t, c))
            sol = solve_H(scal(Fr(1, 4), avg))
            assert sol is not None, (a, b)
            out[(a, b)] = sol
    return out


def main():
    WR, WL = theta_gens()
    seeds = {}
    for m in (1, 2, 3, 4, 5):
        Wm = mmul(word_power(WR, m), word_power(WL, m))
        seeds[m] = powers(Wm)
        print(f"seed {m}: operator order {len(seeds[m])}", flush=True)

    results = {}
    for (a, b) in ((1, 4), (3, 5), (2, 4)):
        t = pair_readout(seeds[a], seeds[b])
        seam = {k: v for k, v in t.items() if v[3] != 0}
        svals = sorted({str(v[3]) for v in seam.values()})
        results[f"{a},{b}"] = dict(nonzero=len(t), seam=len(seam), svals=svals,
                                   sample={str(k): [str(x) for x in v] for k, v in list(seam.items())[:4]})
        print(f"pair ({a},{b}): nonzero {len(t)} | seam-bearing {len(seam)} | s-values {svals}", flush=True)
    json.dump(results, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "seam_predict.json"), "w"))
    print("saved seam_predict.json", flush=True)


if __name__ == "__main__":
    main()


def load_banked():
    import os as _os
    here=_os.path.dirname(_os.path.abspath(__file__))
    return json.load(open(_os.path.join(here,"seam_predict.json")))
