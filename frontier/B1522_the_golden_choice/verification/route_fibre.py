#!/usr/bin/env python3
"""B1522 -- route F (the fibre model): the count-odd stabiliser of every vacuum of the harmonic family on the level M_n.

Model (B1511's conventions, B1512's lemmas I, E, A; re-derived in route R):
  T_n = Z^2 / (Phi^n - I) Z^2 with Phi = [[0, -1], [1, 3]] (columns: the images of x = n m^-1 and y = m n m^-2).
  A character of T_n is a row vector v = (a, b) mod N with v (Phi^n - I) = 0 mod N (N the exponent of T_n); nu_F(x) = zeta_N^a.
  A vacuum is V = nu (x) rho_q restricted to pi_n, nu = (v, lam), q > 0, q != 1.
  The lifted symmetries act on characters by pullback, v -> v B, lam -> lam^sigma:
      iota  (hyperelliptic)   B = -I                       sigma = +1   rho_q o iota  = rho_q          (d = 0)
      eps   (strong inversion) B = S = [[0, 1], [1, 0]]     sigma = -1   rho_q o eps   = rho_{1/q}      (d = 1)
      alpha (amphichiral)     B = M = [[2, 1], [-1, -1]]   sigma = +1   rho_q o alpha = rho_{1/q}      (d = 1)
      tau   (deck)            B = Phi                       sigma = +1   rho_q o tau   = rho_q          (d = 0)
  Composition: nu o (b1 b2) has row vector v B1 B2, sigma1 sigma2, d1 + d2 mod 2.
  A count-odd map is V -> (V o b)^* for a dualising b (d = 1), possibly followed by complex conjugation of the twist (Galois,
  count-even; rho_q is real). On nu it acts as (v, lam) -> (-v B, lam^-sigma), and with conjugation (v B, conj(lam^-sigma)).

Criterion (PREREGISTRATION Lemma C): a vacuum (v, lam) is fixed by a count-odd map
  - at generic or real lam (lam not on the unit circle):  iff  E(v): v B = v for some dualising B with sigma = -1;
  - at unitary lam (|lam| = 1, lam = +-1 included):       iff  E(v) or A(v): v B = v for some dualising B with sigma = +1.
(The sign of B is free because iota, B = -I, is count-even and commutes with everything.)

This file computes, for each level n, the group generated on T_n^ (as matrices mod N with sigma and d), checks its order, and
returns per character the flags E and A. No outcome is read on import."""
import itertools
import math
from functools import reduce

PHI = ((0, -1), (1, 3))
S = ((0, 1), (1, 0))
M = ((2, 1), (-1, -1))
I2 = ((1, 0), (0, 1))
NEG = ((-1, 0), (0, -1))
GENERATORS = {  # name: (B, sigma, d)
    "iota": (NEG, 1, 0),
    "eps": (S, -1, 1),
    "alpha": (M, 1, 1),
    "tau": (PHI, 1, 0),
}


def matmul(A, B, N=None):
    out = tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    if N:
        out = tuple(tuple(x % N for x in row) for row in out)
    return out


def matpow(A, e):
    R = I2
    for _ in range(e):
        R = matmul(R, A)
    return R


def snf_diag(A):
    """the invariant factors of a 2x2 integer matrix (absolute values, in order), by gcds of minors"""
    a, b = A[0]
    c, d = A[1]
    g1 = reduce(math.gcd, [abs(a), abs(b), abs(c), abs(d)])
    det = abs(a * d - b * c)
    if g1 == 0:
        return [0, 0]
    return [g1, det // g1]


def torsion(n):
    A = tuple(tuple(x - (1 if i == j else 0) for j, x in enumerate(row)) for i, row in enumerate(matpow(PHI, n)))
    d1, d2 = snf_diag(A)
    inv = [x for x in (d1, d2) if x != 1]
    order = d1 * d2
    N = reduce(lambda u, w: u * w // math.gcd(u, w), inv, 1)
    return inv, order, N, A


def characters(n):
    inv, order, N, A = torsion(n)
    if order == 1:
        return [(0, 0)], 1, 1
    chars = []
    for a, b in itertools.product(range(N), repeat=2):
        if (a * A[0][0] + b * A[1][0]) % N == 0 and (a * A[0][1] + b * A[1][1]) % N == 0:
            chars.append((a, b))
    assert len(chars) == order, (n, len(chars), order)
    return chars, order, N


def act(v, B, N):
    a, b = v
    return ((a * B[0][0] + b * B[1][0]) % N, (a * B[0][1] + b * B[1][1]) % N)


def group(n):
    """the group generated on T_n^ by the four lifts, as {action-key: (B mod N, sigma, d)}; the key is the permutation of the
    characters together with sigma and d, so elements acting identically are identified"""
    chars, order, N = characters(n)
    index = {c: i for i, c in enumerate(chars)}

    def key(B, sigma, d):
        return (tuple(index[act(c, B, N)] for c in chars), sigma, d)
    start = (tuple(tuple(x % N for x in row) for row in I2), 1, 0)
    elems = {key(*start): start}
    frontier = [start]
    gens = [(tuple(tuple(x % N for x in row) for row in B), s, d) for (B, s, d) in GENERATORS.values()]
    while frontier:
        nxt = []
        for (B, s, d) in frontier:
            for (G, gs, gd) in gens:
                el = (matmul(B, G, N), s * gs, (d + gd) % 2)
                k = key(*el)
                if k not in elems:
                    elems[k] = el
                    nxt.append(el)
        frontier = nxt
    return chars, order, N, list(elems.values())


def flags(n):
    """per character v: E (fixed by a dualising element with sigma = -1), A (by a dualising element with sigma = +1)"""
    chars, order, N, G = group(n)
    E_mats = [B for (B, s, d) in G if d == 1 and s == -1]
    A_mats = [B for (B, s, d) in G if d == 1 and s == 1]
    out = {}
    for v in chars:
        e = any(act(v, B, N) == v for B in E_mats)
        a = any(act(v, B, N) == v for B in A_mats)
        out[v] = {"E": e, "A": a}
    return {"n": n, "order": order, "N": N, "group_order": len(G), "n_E": len(E_mats), "n_A": len(A_mats), "flags": out}


def summary(n):
    f = flags(n)
    fl = f["flags"]
    generic_unfixed = sorted(v for v, x in fl.items() if not x["E"])
    unitary_unfixed = sorted(v for v, x in fl.items() if not (x["E"] or x["A"]))
    return {"n": n, "order": f["order"], "N": f["N"], "group_order": f["group_order"],
            "generic_unfixed": len(generic_unfixed), "unitary_unfixed": len(unitary_unfixed),
            "generic_unfixed_list": generic_unfixed if len(generic_unfixed) <= 64 else None,
            "unitary_unfixed_list": unitary_unfixed if len(unitary_unfixed) <= 64 else None,
            "flags": {f"{v[0]},{v[1]}": x for v, x in fl.items()}}
