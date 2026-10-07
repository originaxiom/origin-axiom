#!/usr/bin/env python3
"""B1490 -- the subgroup's own abelianisation (Reidemeister-Schreier), independent of SnapPy, to decide which cover is the
subgroup's.  H = the stabiliser of the coset of K under the LEFT action of pi_1(target) on the twelve cosets (so H =
pi_1(target) /\ K).  SnapPy's `cover(perms)` composes permutations in word order (a right action), so the left-action
permutations must be inverted before they are passed -- the sealed run did not, and built the other stabiliser; this check
found it (written after the sealed run; disclosed)."""
import sys, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import common_cover_main as C
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def rs_h1(gens, rels, P, left=True):
    n = len(next(iter(P.values()))); inv = {g: [P[g].index(i) for i in range(n)] for g in gens}
    def act(L, i): return (P[L][i] if L.islower() else inv[L.lower()][i])
    reps = {0: ""}; fr = [0]; tree = set()
    while fr:
        nx = []
        for i in fr:
            for g in gens:
                for L in (g, g.upper()):
                    j = act(L, i)
                    if j not in reps:
                        reps[j] = (L + reps[i]) if left else (reps[i] + L); nx.append(j); tree.add((i, g) if L.islower() else (j, g))
        fr = nx
    names = [(i, g) for i in range(n) for g in gens]; idx = {ng: k for k, ng in enumerate(names)}
    def rewrite(w, start):
        vec = [0] * len(names); i = start
        for L in (reversed(w) if left else w):
            if L.islower(): vec[idx[(i, L)]] += 1; i = act(L, i)
            else:
                g = L.lower(); i2 = act(L, i); vec[idx[(i2, g)]] -= 1; i = i2
        assert i == start; return vec
    rows = [rewrite(r, i) for r in rels for i in range(n)]
    for e in tree: v = [0] * len(names); v[idx[e]] = 1; rows.append(v)
    S = smith_normal_form(Matrix(rows), domain=ZZ); d = [abs(S[k, k]) for k in range(min(S.shape))]
    return dict(rank=len(names) - sum(1 for x in d if x != 0), torsion=[int(x) for x in d if x not in (0, 1)])


if __name__ == "__main__":
    out = {}
    for target in sys.argv[1:]:
        gens, rels, P, _ = C.orbit_perms(target)
        out[target] = dict(orbit=len(next(iter(P.values()))), left_action_stabiliser=rs_h1(gens, rels, P, True), right_action_stabiliser=rs_h1(gens, rels, P, False))
        print(target, out[target], flush=True)
    json.dump(out, open(HERE / "subgroup_h1.json", "w"), indent=1)
