#!/usr/bin/env python3
"""B1494 R0 -- the theorem's hypothesis on every word state: at every character chi of the torsion T = coker(phi - I)
(the characters of pi_1(M) trivial on the peripheral subgroup <[x, y], t>), h^1(M; chi) = 1 for chi != 1 (and b1 = 1 at
chi = 1), so that b1(companion) = sum over T^ of h^1(M; chi) = |T| = ends (Shapiro).  Exact, over F_p with p = 1 mod N
(N the exponent of T), at two primes.  The state's group is the census's algebraic presentation
<x, y, t | t x t^-1 phi(x)^-1, t y t^-1 phi(y)^-1> (architecture_census.monodromy), no holonomy needed."""
import sys, json, pathlib, itertools, math
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "frontier" / "B1434_the_architecture_census" / "verification"))
import architecture_census as ac


def word_letters(w):
    """a free-group word in the census's encoding -> list of (generator index, exponent) with x=0, y=1"""
    out = []
    for g in w:
        if g == ac.X: out.append((0, 1))
        elif g == -ac.X: out.append((0, -1))
        elif g == ac.Y: out.append((1, 1))
        elif g == -ac.Y: out.append((1, -1))
        else: raise ValueError(g)
    return out


def relators(eps, word):
    phi = ac.monodromy(eps, word)
    rels = []
    for i, g in enumerate((ac.X, ac.Y)):
        img = word_letters(phi[g])
        # t g t^-1 (phi(g))^-1  as letters over generators (0 = x, 1 = y, 2 = t)
        r = [(2, 1), (i, 1), (2, -1)] + [(j, -e) for (j, e) in reversed(img)]
        rels.append(r)
    return rels, phi


def torsion_matrix(phi):
    return ac.hmat(phi)


def smith_torsion(A):
    """|T| and the exponent of coker(A - I) for a 2x2 integer matrix A"""
    M = [[A[0][0] - 1, A[0][1]], [A[1][0], A[1][1] - 1]]
    d = abs(M[0][0] * M[1][1] - M[0][1] * M[1][0]); g = math.gcd(math.gcd(abs(M[0][0]), abs(M[0][1])), math.gcd(abs(M[1][0]), abs(M[1][1])))
    return d, (d // g if g else d), g      # |T|, exponent, first invariant factor


def primes_1_mod(N, count=2, start=10 ** 9):
    import sympy
    out = []; p = start
    while len(out) < count:
        p = sympy.nextprime(p)
        if (p - 1) % N == 0: out.append(p)
    return out


def rank_mod_p(rows, p):
    M = [r[:] for r in rows]; rank = 0; cols = len(M[0]) if M else 0
    for c in range(cols):
        piv = next((i for i in range(rank, len(M)) if M[i][c] % p), None)
        if piv is None: continue
        M[rank], M[piv] = M[piv], M[rank]; inv = pow(M[rank][c], p - 2, p)
        M[rank] = [(v * inv) % p for v in M[rank]]
        for i in range(len(M)):
            if i != rank and M[i][c] % p:
                f = M[i][c]; M[i] = [(a - f * b) % p for a, b in zip(M[i], M[rank])]
        rank += 1
    return rank


def fox_row(rel, vals, p):
    """Fox derivatives of a relator at a rank-one character (values vals[g] in F_p): d/dg = sum over occurrences"""
    out = [0, 0, 0]; prefix = 1
    for (g, e) in rel:
        if e == 1: out[g] = (out[g] + prefix) % p; prefix = prefix * vals[g] % p
        else: prefix = prefix * pow(vals[g], p - 2, p) % p; out[g] = (out[g] - prefix) % p
    return out


def characters_of_T(A, N, p, zeta):
    """characters chi on (x, y) with chi(t) = 1 and chi o phi = chi on H1: (a, b) in (Z/N)^2 with (A^T - I)(a, b) = 0 mod N
    (chi(x) = zeta^a, chi(y) = zeta^b; A's columns are the images of x, y so chi(phi(x)) = zeta^(A00 a + A10 b))"""
    out = []
    for a, b in itertools.product(range(N), repeat=2):
        if (A[0][0] * a + A[1][0] * b - a) % N == 0 and (A[0][1] * a + A[1][1] * b - b) % N == 0: out.append((a, b))
    return out


def read_state(eps, word, primes=None):
    rels, phi = relators(eps, word); A = torsion_matrix(phi); size, N, _ = smith_torsion(A)
    if N == 1: return dict(state=("+" if eps > 0 else "-") + word, T=size, N=1, chars=1, h1=[1], all_one=True, primes=[])
    primes = primes or primes_1_mod(N)
    res = dict(state=("+" if eps > 0 else "-") + word, T=size, N=N, primes=primes, h1={})
    for p in primes:
        zeta = None
        for g in range(2, p):
            z = pow(g, (p - 1) // N, p)                      # an N-th root of unity; primitive iff z^(N/q) != 1 for every prime q | N
            if all(pow(z, N // q, p) != 1 for q in sympy_factors(N)): zeta = z; break
        chars = characters_of_T(A, N, p, zeta); assert len(chars) == size, (len(chars), size)
        for (a, b) in chars:
            vals = [pow(zeta, a, p), pow(zeta, b, p), 1]
            triv = (a == 0 and b == 0)
            d0 = sum(1 for v in vals if v % p != 1)   # rank of d0 = 1 unless trivial
            d1 = rank_mod_p([fox_row(r, vals, p) for r in rels], p)
            h1 = 3 - (0 if triv else 1) - d1
            res["h1"].setdefault(str((a, b)), []).append(h1)
    res["all_one"] = all(set(v) == ({1} if k != "(0, 0)" else {1}) for k, v in res["h1"].items())
    res["b1_companion"] = sum(v[0] for v in res["h1"].values()); res["ends"] = size
    return res


def sympy_factors(n):
    import sympy
    return list(sympy.factorint(n).keys())


if __name__ == "__main__":
    maxlen = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    out = []
    for word in ac.states(maxlen):
        for eps in (+1, -1):
            r = read_state(eps, word); out.append(r)
            print(r["state"], "|T| =", r["T"], "N =", r["N"], "h1 at every torsion character = 1:", r["all_one"], "b1(companion) =", r.get("b1_companion", 1), "ends =", r.get("ends", 1), flush=True)
    json.dump(out, open(HERE / f"torsion_characters_len{maxlen}.json", "w"), indent=1)
    print("states", len(out), "all hold:", all(r["all_one"] and r.get("b1_companion", 1) == r.get("ends", 1) for r in out))
