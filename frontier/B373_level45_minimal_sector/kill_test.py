"""B373 (PD1.1) — the level-45 minimal-sector kill test, executed as pre-registered.

Census of 2-dim invariant {a, -a} sectors of W1@45 under the full Weil image; for each,
the exact metallic traces, the S-hat data, and the dihedral check. Verdict: PINNED (108°,
anyon-shaped) vs MOVED (gapless-trending) vs THIRD OUTCOME (census surprise).
"""
import json
import os
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B372_level45_sweeper"))
from fp_engine import (Level, basis_elements, primes_1_mod, primitive_root,
                       rational_reconstruct, _solve_mod)
from sweep45 import gamma_and_reps

N = 45


def projector(L, powers, a):
    p, o, n = L.p, len(powers), L.N
    zo = pow(L.z, (4 * L.N) // o, p)
    inv = pow(o, p - 2, p)
    P = [[0] * n for _ in range(n)]
    for j in range(o):
        c = pow(zo, (-j * a) % o, p) * inv % p
        Pj = powers[j]
        for i in range(n):
            row = Pj[i]
            Pi = P[i]
            for k in range(n):
                Pi[k] = (Pi[k] + c * row[k]) % p
    return P


def run():
    primes = primes_1_mod(720, 3)
    G, reps, held = gamma_and_reps(N)

    # ---- census at one prime, one embedding (dims + invariance are integer facts) ----
    p0 = primes[0]
    g0 = primitive_root(p0)
    z0 = pow(g0, (p0 - 1) // (4 * N), p0)
    L0 = Level(N, p0, z0)
    W1 = L0.W(1)
    o1, pow1 = L0.order_powers(W1)
    dims = {}
    for a in range(o1):
        P = projector(L0, pow1, a)
        dims[a] = sum(P[i][i] for i in range(N)) % p0        # trace = dim (small int)
    pairs = [(a, (o1 - a) % o1) for a in range(1, o1 // 2)
             if dims[a] == 1 and dims[(o1 - a) % o1] == 1]

    def invariant(P, L):
        n, pp = L.N, L.p
        Pc = [[(1 if i == j else 0) - P[i][j] for j in range(n)] for i in range(n)]
        for G_ in (L.D, L.WR):
            M = L.mmul(L.mmul(Pc, G_), P)
            if any(M[i][j] % pp for i in range(n) for j in range(n)):
                return False
        return True

    sectors = []
    for a, b in pairs:
        Pa, Pb = projector(L0, pow1, a), projector(L0, pow1, b)
        P = [[(Pa[i][j] + Pb[i][j]) % p0 for j in range(N)] for i in range(N)]
        if invariant(P, L0):
            sectors.append((a, b))
    # confirm at two more primes
    for p in primes[1:]:
        g = primitive_root(p)
        z = pow(g, (p - 1) // (4 * N), p)
        L = Level(N, p, z)
        W = L.W(1)
        _, pw = L.order_powers(W)
        for a, b in sectors:
            Pa, Pb = projector(L, pw, a), projector(L, pw, b)
            P = [[(Pa[i][j] + Pb[i][j]) % p for j in range(N)] for i in range(N)]
            assert invariant(P, L), (p, a, b)

    # ---- exact traces on each invariant sector (Gamma-averaged identification) ----
    def sector_data(a, b):
        vals = {}
        for label, mfun in (("A1", 1), ("A2", 2), ("A3", 3), ("A4", 4), ("Shat", None)):
            per_prime = []
            for p in primes:
                g = primitive_root(p)
                z0p = pow(g, (p - 1) // (4 * N), p)
                rows, ys = [], []
                for k in reps + held:
                    acc = 0
                    for gam in G:
                        kk = (k * gam) % (4 * N)
                        L = Level(N, p, pow(z0p, kk, p))
                        W = L.W(1)
                        _, pw = L.order_powers(W)
                        Pa, Pb = projector(L, pw, a), projector(L, pw, b)
                        P = [[(Pa[i][j] + Pb[i][j]) % p for j in range(N)] for i in range(N)]
                        if mfun is not None:
                            M = L.W(mfun)
                        else:
                            M = L.mmul(L.mmul(L.Di, L.WR), L.Di)
                        acc = (acc + sum(L.mmul(P, M)[i][i] for i in range(N))) % p
                    ys.append(acc * pow(len(G), p - 2, p) % p)
                    rows.append(basis_elements(N, p, pow(z0p, k, p)))
                nb = len(reps)
                x = _solve_mod([r for r in rows[:nb]], ys[:nb], p)
                for row, y in zip(rows[nb:], ys[nb:]):
                    assert sum(xi * bi for xi, bi in zip(x, row)) % p == y, "outside span"
                per_prime.append((p, x))
            M_ = 1
            for p, _x in per_prime:
                M_ *= p
            out = []
            for i in range(len(reps)):
                r = 0
                for p, x in per_prime:
                    Mi = M_ // p
                    r = (r + x[i] * Mi * pow(Mi, p - 2, p)) % M_
                out.append(str(rational_reconstruct(r, M_)))
            vals[label] = out
        return vals

    # dihedral at 45, one prime check
    Sh = L0.mmul(L0.mmul(L0.Di, L0.WR), L0.Di)
    WRi = L0.mmul(L0.mmul([[pow(L0.zN, (i*j) % N, p0) for j in range(N)] for i in range(N)], L0.D),
                  [[pow(L0.zN, (-i*j) % N, p0) * pow(N, p0-2, p0) % p0 for j in range(N)] for i in range(N)])
    Shi = L0.mmul(L0.mmul(L0.D, WRi), L0.D)
    lhs = L0.mmul(L0.mmul(Sh, W1), Shi)
    W1i = pow1[o1 - 1]
    dihedral = all(lhs[i][j] == W1i[i][j] for i in range(N) for j in range(N))

    report = dict(order_W1=o1,
                  mult1_pairs=pairs,
                  invariant_sectors=sectors,
                  dihedral_global=dihedral,
                  sector_traces={f"{a},{b}": sector_data(a, b) for a, b in sectors})
    with open(os.path.join(HERE, "kill_test.json"), "w") as fh:
        json.dump(report, fh, indent=1)
    return report


if __name__ == "__main__":
    r = run()
    print("ord(W1) =", r["order_W1"])
    print("mult-1 opposite pairs:", r["mult1_pairs"])
    print("INVARIANT 2-dim sectors:", r["invariant_sectors"])
    print("dihedral S W1 S^-1 = W1^-1 at 45:", r["dihedral_global"])
    for k, v in r["sector_traces"].items():
        print(f"  sector {{{k}}}: tr A1 = {v['A1']}")
        print(f"             tr A2 = {v['A2']}  tr Shat = {v['Shat']}")
