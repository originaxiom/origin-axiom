"""B1111 -- the W5 scoping, consolidated: per-element rigidity, joint-locus
availability, stabilizer sample -- with the exact Q(sqrt2) certification that
replaced a broken rational-approximation verifier (the banked census as the
positive control). Run from the repo root (~2 min)."""
import importlib.util
from collections import Counter

import numpy as np
import sympy as sp

spec = importlib.util.spec_from_file_location(
    "b1084", "frontier/B1084_g2_cone/float_crosscheck.py")
m = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(m)
except SystemExit:
    pass

S2 = sp.sqrt(2)
CAND = [sp.Integer(0), sp.Integer(1), sp.Integer(-1), sp.Rational(1, 2),
        sp.Rational(-1, 2), S2 / 2, -S2 / 2]


def code(v):
    for e in CAND:
        if abs(v - float(e)) < 1e-9:
            return e
    raise ValueError(v)


def toexact(M):
    return sp.Matrix(7, 7, lambda i, j: code(float(M[i, j])))


seen = {m.key(np.eye(7)): sp.eye(7)}
fr = [(np.eye(7), sp.eye(7))]
while fr:
    Xf, Xe = fr.pop()
    for gf in m.generators:
        Yf = gf @ Xf
        k = m.key(Yf)
        if k not in seen:
            seen[k] = sp.expand(toexact(gf) * Xe)
            fr.append((Yf, seen[k]))
G = list(seen.values())
assert len(G) == 96
I = sp.eye(7)
dims = [7 - (M - I).rank() for M in G]
census = sorted(Counter(dims).items())
print("exact per-element census:", census, "(banked B1084: 1:42, 3:53)")
assert dict(census) == {1: 42, 3: 53, 7: 1}
nt = [M for M, d in zip(G, dims) if d < 7]
jc = Counter()
for i in range(len(nt)):
    Ai = nt[i] - I
    for j in range(i + 1, len(nt)):
        jc[7 - Ai.col_join(nt[j] - I).rank()] += 1
print("exact pairwise joint-V1 dims:", sorted(jc.items()))
assert dict(jc) == {0: 1656, 1: 2556, 3: 253}
print("=> 1656 transversal pairs: isolated JOINT collisions are geometrically")
print("   available; per-element loci remain rigid (screws only empty them).")
