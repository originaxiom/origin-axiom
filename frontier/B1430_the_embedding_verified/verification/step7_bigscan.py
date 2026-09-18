"""Bigger, constraint-solved scan of u(1) directions.

For the fixed A2+A1 the conditions on the coweight coordinates
n = (n_1..n_6) are  n_2 = 0, n_4 = 0, n_1 + n_3 + 2 n_5 + n_6 = 0,
so n_1, n_3, n_5 are free and n_6 is determined.  Scan them in a big box.
"""
from fractions import Fraction as F
from rootsys import *
from collections import Counter, defaultdict
from math import gcd
from itertools import product
import json

exec(open("common_e6.py").read())

conds = [[int(x) for x in simple_coeffs(r)] for r in [b1, b2, gam]]
print("conditions:", conds)

M = 20
lines = []
seen = set()
for n1, n3, n5 in product(range(-M, M + 1), repeat=3):
    n = (n1, 0, n3, 0, n5, -(n1 + n3 + 2 * n5))
    for c in conds:
        assert sum(ci * ni for ci, ni in zip(c, n)) == 0
    if all(x == 0 for x in n):
        continue
    g = 0
    for x in n:
        g = gcd(g, abs(x))
    n = tuple(x // g for x in n)
    k = min(n, tuple(-x for x in n))
    if k in seen:
        continue
    seen.add(k)
    lines.append(k)
print("primitive coweight LINES orthogonal to the A2+A1 in the box "
      "|n_1|,|n_3|,|n_5| <= %d : %d" % (M, len(lines)))

sigs = Counter()
smlines = []
unid = 0
for n in lines:
    v = vec_of(n)
    s = branch(v)
    if s is None:
        unid += 1
        continue
    sigs[canon_sig(s)] += 1
    if is_sm(s):
        smlines.append(n)
print("branchings that my minuscule peeling could not identify:", unid)
print("DISTINCT branching signatures of the 27 (up to scale and sign):",
      len(sigs))
print("-> at least that many pairwise NON-CONJUGATE su(3)+su(2)+u(1)")
print("   subalgebras of E6 with this same regular su(3)+su(2).")
print()
print("lines reproducing EXACTLY the Standard-Model branching:", len(smlines))
print("   ", smlines)

# Stab-orbits among the SM lines
vecs = {n: vec_of(n) for n in smlines}
key = {min(v, tuple(-x for x in v)): n for n, v in vecs.items()}
parent = {n: n for n in smlines}


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


for n in smlines:
    for act in stab_lin:
        w = act(vecs[n])
        k = min(w, tuple(-x for x in w))
        if k in key:
            a, b = find(n), find(key[k])
            if a != b:
                parent[a] = b
cls = set(find(n) for n in smlines)
print("Stab_W(A2+A1)-orbits among them:", len(cls))
print("=> number of W(E6)-conjugacy classes of REGULAR su(3)+su(2)+u(1)")
print("   with exactly the SM branching of the 27, found in this box:",
      len(cls))

# the continuum statement, with the actual numbers
print()
print("=== THE CONTINUUM STATEMENT ===")
print("dim V (Cartan directions commuting with the A2+A1) =", 6 - rank_of([b1, b2, gam]))
print("|Stab_W(A2+A1)| =", len(stab))
print("the set of u(1)'s = lines in V = RP^2 (uncountable);")
print("every Stab-orbit has size at most", len(stab), "->",
      "UNCOUNTABLY many W-orbits of su(3)+su(2)+u(1) subalgebras.")

json.dump({"lines": len(lines), "distinct_signatures": len(sigs),
           "sm_lines": len(smlines), "sm_classes": len(cls)},
          open("step7_summary.json", "w"))
