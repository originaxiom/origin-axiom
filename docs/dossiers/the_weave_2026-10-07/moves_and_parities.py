#!/usr/bin/env python3
"""W1 of the weave (docs/THE_WEAVE.md): the three from the interaction of the grammar's moves, with no thread chosen.
Exact, mod 2.

The moves on the two records (GENESIS GM2 and the open GM5b, GM5c): L = [[1, 1], [0, 1]], R = [[1, 0], [1, 1]], the swap
P = [[0, 1], [1, 0]], and the sign -I. Mod 2 the records' non-zero parities are three: (1, 0), (0, 1), (1, 1).
  (1) Each single move fixes exactly one non-zero parity and swaps the other two, and L, R and P fix three different
      parities. -I fixes all three.
  (2) Any two different moves among L, R, P generate all six permutations of the three parities (GL(2, F_2) = S_3), and
      their product is a 3-cycle: three comes from the interaction of two moves, never from one.
  (3) Every object the moves generate (every hyperbolic word in L, R and P, with either sign, to length 8) acts on the
      three parities by its word mod 2: the table counts the objects that fix all three, that fix one (a transposition),
      and that cycle all three (a 3-cycle), by determinant. m000 (the Gieseking manifold, LP), m004 (LR) and m003 (-LR)
      are among the third.

    python3 moves_and_parities.py   ->  moves_and_parities.json beside this file"""
import itertools
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
MOVES = {"L": ((1, 1), (0, 1)), "R": ((1, 0), (1, 1)), "P": ((0, 1), (1, 0))}
PAR = [(1, 0), (0, 1), (1, 1)]


def mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def act(M, v):
    return tuple((M[i][0] * v[0] + M[i][1] * v[1]) % 2 for i in range(2))


def perm(M):
    return tuple(PAR.index(act(M, v)) for v in PAR)


def kind(p):
    fixed = sum(1 for i in range(3) if p[i] == i)
    return {3: "fixes all three", 1: "fixes one (a transposition)", 0: "cycles all three (a 3-cycle)"}[fixed]


def closure(gens):
    I = ((1, 0), (0, 1))
    G = {perm(I)}
    fr = [perm(I)]
    gp = [perm(g) for g in gens]
    while fr:
        nx = []
        for p in fr:
            for q in gp:
                r = tuple(q[p[i]] for i in range(3))
                if r not in G:
                    G.add(r)
                    nx.append(r)
        fr = nx
    return G


def canon(w):
    rots = [w[i:] + w[:i] for i in range(len(w))]
    return min(rots)


def main(nmax=8):
    out = {"single moves": {m: {"fixes": [list(PAR[i]) for i in range(3) if perm(M)[i] == i], "kind": kind(perm(M))}
                            for m, M in MOVES.items()}}
    out["pairs of moves: the group generated (order) and the product's kind"] = {
        a + b: {"order": len(closure([MOVES[a], MOVES[b]])), "product": kind(perm(mul(MOVES[a], MOVES[b])))}
        for a, b in itertools.combinations("LRP", 2)}
    seen, tab, named = set(), Counter(), {}
    for n in range(2, nmax + 1):
        for t in itertools.product("LRP", repeat=n):
            w = canon("".join(t))
            if w in seen:
                continue
            seen.add(w)
            M = ((1, 0), (0, 1))
            for c in w:
                M = mul(M, MOVES[c])
            tr, det = M[0][0] + M[1][1], M[0][0] * M[1][1] - M[0][1] * M[1][0]
            for sign in (1, -1):
                trs = sign * tr
                hyperbolic = (abs(trs) > 2) if det == 1 else (trs != 0)   # det -1: hyperbolic iff trace non-zero
                if not hyperbolic:
                    continue
                k = kind(perm(M))
                tab[(det, k)] += 1
                if (w, sign) in {("LR", 1), ("LR", -1), ("LP", 1)}:
                    named[{("LR", 1): "m004 (+LR)", ("LR", -1): "m003 (-LR)", ("LP", 1): "m000 (LP, Gieseking)"}[(w, sign)]] = k
    out[f"every hyperbolic word in L, R, P to length {nmax}, both signs: (determinant, kind) -> objects"] = {
        f"det {d}: {k}": v for (d, k), v in sorted(tab.items())}
    out["the named objects"] = named
    out["-I fixes all three parities"] = perm(((-1, 0), (0, -1))) == (0, 1, 2)
    (HERE / "moves_and_parities.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
