#!/usr/bin/env python3
"""The weave's group on the triplet, and the mixing its subgroups give under the residual-symmetry rule (a READING).

The triplet is W4's: the parity-twisted cohomology of the shared fibre, one line per non-zero parity. The moves L, R, P,
-I and the fibre's own inner automorphisms act on it by signed permutations (the_common_point.py, part 3).
  (1) The group they generate: its order, determinants and element orders; its rotations (determinant 1).
  (2) The residual-symmetry rule of flavour physics: a sector that keeps a subgroup K of the flavour group has its mass
      matrix diagonal in K's eigenbasis, so two sectors keeping K1 and K2 mix by U = V1^dagger V2. With K1 = Z3, the
      golden thread's own 3-cycle on the triplet, and K2 a Klein four-group of the weave, |U|^2 up to permutations of
      rows and columns; with K2 a single involution, the one column it fixes.
Which sector keeps which subgroup is not forced by anything here; that is why the result is a reading.

    python3 the_mixing.py   ->  the_mixing.json beside this file"""
import itertools
import json
from collections import Counter
from pathlib import Path

import numpy as np

import the_common_point as C

HERE = Path(__file__).resolve().parent
I3 = np.eye(3, dtype=int)


def group():
    gens = {n: np.array(C.tmat(a), dtype=int) for n, a in
            {"L": C.AUT["L"], "R": C.AUT["R"], "P": C.AUT["P"], "-I": C.AUT["-I"],
             "inner by a": C.inner([1]), "inner by b": C.inner([2])}.items()}
    G = {tuple(map(tuple, I3)): I3}
    fr = [I3]
    while fr:
        nx = []
        for A in fr:
            for g in gens.values():
                B = A @ g
                k = tuple(map(tuple, B))
                if k not in G:
                    G[k] = B
                    nx.append(B)
        fr = nx
    return gens, list(G.values())


def order(A):
    k, X = 1, A.copy()
    while not np.array_equal(X, I3):
        X, k = X @ A, k + 1
    return k


def canon(P):
    best = None
    for pr in itertools.permutations(range(3)):
        for pc in itertools.permutations(range(3)):
            Q = tuple(tuple(round(float(P[pr[i]][pc[j]]), 6) for j in range(3)) for i in range(3))
            best = Q if best is None or Q < best else best
    return best


def main():
    gens, G = group()
    out = {"(1) the weave's group on the triplet": {
        "order": len(G), "determinants": dict(Counter(int(round(np.linalg.det(A))) for A in G)),
        "element orders": dict(sorted(Counter(order(A) for A in G).items())),
        "rotations (determinant 1)": sum(1 for A in G if round(np.linalg.det(A)) == 1),
        "-1 in the group": any(np.array_equal(A, -I3) for A in G)}}
    T = np.array(C.tmat(C.word_aut("LR", 1)), dtype=float)
    w, V = np.linalg.eig(T)
    VT = V / np.linalg.norm(V, axis=0)
    inv = [A for A in G if np.array_equal(A @ A, I3) and not np.array_equal(A, I3) and not np.array_equal(A, -I3)]
    klein = {}
    for A, B in itertools.combinations(inv, 2):
        if np.array_equal(A @ B, B @ A) and not np.array_equal(A @ B, -I3):
            ev, VK = np.linalg.eigh(A + np.e * B)
            klein.setdefault(canon(np.abs(VT.conj().T @ VK) ** 2), 0)
            klein[canon(np.abs(VT.conj().T @ VK) ** 2)] += 1
    cols = Counter()
    for A in inv:
        ev, EV = np.linalg.eigh(A.astype(float))
        vals = list(np.round(ev).astype(int))
        lone = [i for i in range(3) if vals.count(vals[i]) == 1][0]
        cols[tuple(sorted(round(float(x), 6) for x in np.abs(VT.conj().T @ EV[:, lone]) ** 2))] += 1
    out["(2) Z3 = the golden thread's 3-cycle; K = a Klein four-group of the weave: |U|^2 (canonical form) -> pairs"] = {
        str(k): v for k, v in sorted(klein.items())}
    out["(2) Z3 = the golden thread's 3-cycle; K = one involution: the fixed column |U_i|^2 (sorted) -> involutions"] = {
        str(k): v for k, v in sorted(cols.items())}
    tbm = canon(np.array([[2 / 3, 1 / 3, 0], [1 / 6, 1 / 3, 1 / 2], [1 / 6, 1 / 3, 1 / 2]]))
    out["the tri-bimaximal |U|^2 in canonical form"] = str(tbm)
    out["a Klein four-group of the weave gives tri-bimaximal mixing"] = str(tbm) in out[
        "(2) Z3 = the golden thread's 3-cycle; K = a Klein four-group of the weave: |U|^2 (canonical form) -> pairs"]
    (HERE / "the_mixing.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
