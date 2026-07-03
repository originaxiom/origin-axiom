"""B374 (PD2.2, rung 3) — the level-135 census against B373's pre-registered prediction.

PREDICTION (committed in B373's FINDINGS before this run): the unique invariant two-state
sector of W1@135 sits at exponents +-6 of ord(W1) = 180 (quasi-energy +-12 degrees); the
global dihedral relation persists. KILL: any deviation refutes the pinned-exponent law.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B372_level45_sweeper"))
from fp_engine import Level, primes_1_mod, primitive_root

N = 135


def projector_dim(L, powers, a):
    p, o = L.p, len(powers)
    zo = pow(L.z, (4 * L.N) // o, p)
    inv = pow(o, p - 2, p)
    # dim = tr P_a = (1/o) sum_j zeta^{-ja} tr(W^j)
    tr = [sum(P[i][i] for i in range(L.N)) % p for P in powers]
    return sum(pow(zo, (-j * a) % o, p) * tr[j] for j in range(o)) % p * inv % p


def projector(L, powers, a):
    p, o, n = L.p, len(powers), L.N
    zo = pow(L.z, (4 * L.N) // o, p)
    inv = pow(o, p - 2, p)
    P = [[0] * n for _ in range(n)]
    for j in range(o):
        c = pow(zo, (-j * a) % o, p) * inv % p
        Pj = powers[j]
        for i in range(n):
            row, Pi = Pj[i], P[i]
            for k in range(n):
                Pi[k] = (Pi[k] + c * row[k]) % p
    return P


def invariant(P, L):
    n, pp = L.N, L.p
    Pc = [[(1 if i == j else 0) - P[i][j] for j in range(n)] for i in range(n)]
    for G_ in (L.D, L.WR):
        M = L.mmul(L.mmul(Pc, G_), P)
        if any(M[i][j] % pp for i in range(n) for j in range(n)):
            return False
    return True


def run():
    primes = primes_1_mod(4 * N * 4, 3, start=10**9)   # p = 1 mod 2160
    p0 = primes[0]
    g = primitive_root(p0)
    L = Level(N, p0, pow(g, (p0 - 1) // (4 * N), p0))
    W1 = L.W(1)
    o1, pow1 = L.order_powers(W1, cap=800)
    dims = {a: projector_dim(L, pow1, a) for a in range(o1)}
    mult1 = [a for a in range(1, o1 // 2) if dims[a] == 1 and dims[(o1 - a) % o1] == 1]
    sectors = []
    for a in mult1:
        Pa = projector(L, pow1, a)
        Pb = projector(L, pow1, (o1 - a) % o1)
        P = [[(Pa[i][j] + Pb[i][j]) % p0 for j in range(N)] for i in range(N)]
        if invariant(P, L):
            sectors.append((a, (o1 - a) % o1))
    # dihedral at 135
    Sh = L.mmul(L.mmul(L.Di, L.WR), L.Di)
    F = [[pow(L.zN, (i * j) % N, p0) for j in range(N)] for i in range(N)]
    Fi = [[pow(L.zN, (-i * j) % N, p0) * pow(N, p0 - 2, p0) % p0 for j in range(N)] for i in range(N)]
    WRi = L.mmul(L.mmul(F, L.D), Fi)
    Shi = L.mmul(L.mmul(L.D, WRi), L.D)
    lhs = L.mmul(L.mmul(Sh, W1), Shi)
    dihedral = all(lhs[i][j] == pow1[o1 - 1][i][j] for i in range(N) for j in range(N))
    # confirm the found sectors at two more primes
    confirmed = True
    for p in primes[1:]:
        gp = primitive_root(p)
        Lp = Level(N, p, pow(gp, (p - 1) // (4 * N), p))
        Wp = Lp.W(1)
        _, pwp = Lp.order_powers(Wp, cap=800)
        for a, b in sectors:
            Pa, Pb = projector(Lp, pwp, a), projector(Lp, pwp, b)
            P = [[(Pa[i][j] + Pb[i][j]) % p for j in range(N)] for i in range(N)]
            if not invariant(P, Lp):
                confirmed = False
    rep = dict(order_W1=o1, n_mult1_pairs=len(mult1), invariant_sectors=sectors,
               dihedral_global=dihedral, cross_prime_confirmed=confirmed,
               prediction_hit=(o1 == 180 and sectors == [(6, 174)] and dihedral and confirmed))
    with open(os.path.join(HERE, "rung135.json"), "w") as fh:
        json.dump(rep, fh, indent=1)
    return rep


if __name__ == "__main__":
    r = run()
    for k, v in r.items():
        print(f"  {k}: {v}")
