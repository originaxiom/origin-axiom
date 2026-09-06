#!/usr/bin/env python3
"""THE CUBIC MADE EXPLICIT: B308's unique E6 cubic invariant d_abc on the 27, solved exactly from the
repository's own 27 (B883's rep27.json), and the Jordan ranks of the object's own 27-lattice vectors.

(a) d_abc: the unique (up to scale) symmetric cubic form on the 27 annihilated by all 78 generators of e6,
    supported on the 45 zero-sum weight triples (B1271 (d)); solved as a nullspace over Q with the 45
    triple-values as unknowns and the invariance equations of the 72 root vectors.  Result: dim 1, all 45
    values +-1 after normalisation.
(b) THE JORDAN RANKS of the vectors the two faces supply (B1270/B1272): the cubic norm I_3(q) = d_abc q^a q^b q^c
    and the Freudenthal cross product q # q (the adjoint) decide the rank: rank 1 <=> q # q = 0 (I_3 = 0),
    rank 2 <=> q # q != 0, I_3 = 0, rank 3 <=> I_3 != 0.  Every single 27-weight is rank 1 (the Spin(10)
    orbit of B969/B962), every pair-sum is rank <= 2, and every zero-sum triple w1 + w2 + w3 -- in particular
    the triple the object's mirror selects (B1272 section 4) -- is rank 3 with I_3 = +-6: a non-degenerate
    element of the cubic, the kind of charge that carries an entropy (pi sqrt|I_3|) in the E6(6) reading
    (L202), and whose attractor point is the S3-symmetric point (all three charges of equal size).
"""
from __future__ import annotations
import os, sys, json, itertools, collections
from fractions import Fraction as F
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'B1267_spectrum_law_rebuilt', 'verification'))
import e6_instrument as E


def load():
    d = json.load(open(E.REP27))
    wts = d['weights']
    rep = {int(k): [[F(x) for x in row] for row in v] for k, v in d['rep'].items()}
    return wts, rep


def solve_cubic(wts, rep):
    n = 27
    triples = [t for t in itertools.combinations(range(n), 3) if all(wts[t[0]][k] + wts[t[1]][k] + wts[t[2]][k] == 0 for k in range(6))]
    assert len(triples) == 45
    idx = {}
    for j, t in enumerate(triples):
        for p in itertools.permutations(t):
            idx[p] = j
    # invariance: for every generator X and every (a, b, c): sum_a' X[a',a] d_{a'bc} + sum_b' X[b',b] d_{ab'c} + sum_c' X[c',c] d_{abc'} = 0
    rows = []
    for g, X in rep.items():
        for (a, b, c) in itertools.combinations_with_replacement(range(n), 3):
            row = [F(0)] * 45
            nz = False
            for ap in range(n):
                if X[ap][a] != 0 and (ap, b, c) in idx:
                    row[idx[(ap, b, c)]] += X[ap][a]; nz = True
            for bp in range(n):
                if X[bp][b] != 0 and (a, bp, c) in idx:
                    row[idx[(a, bp, c)]] += X[bp][b]; nz = True
            for cp in range(n):
                if X[cp][c] != 0 and (a, b, cp) in idx:
                    row[idx[(a, b, cp)]] += X[cp][c]; nz = True
            if nz and any(row):
                rows.append(row)
    M = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in r] for r in rows])
    ns = M.nullspace()
    return triples, idx, ns


def cubic_tensor(triples, vec):
    d = {}
    for j, t in enumerate(triples):
        for p in itertools.permutations(t):
            d[p] = vec[j]
    return d


def I3(d, q):
    return sum(v * q[a] * q[b] * q[c] for (a, b, c), v in d.items())


def cross(d, q):
    """The adjoint (Freudenthal) q # q in the dual: (q # q)_a = (1/2) sum_bc d_abc q^b q^c, up to normalisation."""
    n = 27
    return [sum(d.get((a, b, c), 0) * q[b] * q[c] for b in range(n) for c in range(n)) for a in range(n)]


def jordan_rank(d, q):
    if any(q):
        if I3(d, q) != 0:
            return 3
        if any(cross(d, q)):
            return 2
        return 1
    return 0


def main():
    wts, rep = load()
    triples, idx, ns = solve_cubic(wts, rep)
    print(f"  zero-sum weight triples: {len(triples)}; invariance nullspace dimension: {len(ns)}   (1: the cubic is unique)")
    ok = len(ns) == 1
    v = ns[0]
    scale = min(abs(x) for x in v if x != 0)
    vec = [sp.nsimplify(x / scale) for x in v]
    vals = collections.Counter(vec)
    print(f"  normalised values of d on the 45 triples: {dict(vals)}")
    ok &= set(vals) <= {sp.Integer(1), sp.Integer(-1)}
    d = cubic_tensor(triples, vec)
    # (b) the Jordan ranks
    e = lambda i: [sp.Integer(1) if k == i else sp.Integer(0) for k in range(27)]
    ranks_single = collections.Counter(jordan_rank(d, e(i)) for i in range(27))
    ranks_pair = collections.Counter(jordan_rank(d, [x + y for x, y in zip(e(i), e(j))]) for i, j in itertools.combinations(range(27), 2))
    ranks_triple0 = collections.Counter(jordan_rank(d, [x + y + z for x, y, z in zip(e(a), e(b), e(c))]) for (a, b, c) in triples)
    I3_triple0 = collections.Counter(I3(d, [x + y + z for x, y, z in zip(e(a), e(b), e(c))]) for (a, b, c) in triples)
    other = [t for t in itertools.combinations(range(27), 3) if t not in set(triples)]
    ranks_other = collections.Counter(jordan_rank(d, [x + y + z for x, y, z in zip(e(t[0]), e(t[1]), e(t[2]))]) for t in other)
    print(f"  Jordan rank of a single weight: {dict(ranks_single)}   (27 x rank 1: the Spin(10) orbit)")
    print(f"  Jordan rank of a sum of two weights: {dict(ranks_pair)}")
    print(f"  Jordan rank of a zero-sum triple w1 + w2 + w3: {dict(ranks_triple0)};  I_3 values: {dict(I3_triple0)}   (the 45 rank-3 charges, |I_3| = 6)")
    print(f"  Jordan rank of a non-zero-sum triple: {dict(ranks_other)}")
    ok &= ranks_single == {1: 27} and ranks_triple0 == {3: 45} and set(abs(k) for k in I3_triple0) == {6}
    print("  -> the triple the object's mirror selects (B1272: three mutually orthogonal weights summing to zero) is a rank-3 element with |I_3| = 6;")
    print("     its three charges are equal in size, so under the attractor reading (L202) its attractor point is the S3-symmetric point of the moduli space")
    return ok


if __name__ == "__main__":
    print("=== the E6 cubic d_abc from the repository's own 27, and the Jordan ranks of the object's lattice vectors ===")
    ok = main()
    print("\nSELFTEST:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
