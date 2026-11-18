#!/usr/bin/env python3
"""W-P1, step 2 (W-P1b), a follow-up to wp1b_class_test.py's C2, written after its run: how the labels move.

    python3 -I wp1b_labels.py

wp1b_class_test.py found that, with the Heisenberg labels D(p, q) fixed, the two classes move the labels differently
and neither moves them as g acts on (p, q). Here, for each class a and each g: the matrix A_a(g) in GL(2, F_5) with
pi_a(g)(v) = A_a(g) v for all 25 labels, if one exists; whether A_a(g) = K_a g K_a^-1 for one fixed K_a for all g, and
for which K_a (all solutions in GL(2, F_5)); and the determinant classes of those K_a (residue or not mod 5).
"""
import itertools
import numpy as np

src = open(__file__.replace("wp1b_labels.py", "wp1b_class_test.py")).read()
g = {"__name__": "lib"}
exec(src[:src.index("Gs = {a: group(a)")], g)
group, label_action, key = g["group"], g["label_action"], g["key"]
SQ = {1, 4}
for a in (1, 2):
    G = group(a)[0]
    A = {}
    for k, (gm, M) in G.items():
        act = label_action(M)
        found = None
        for m in itertools.product(range(5), repeat=4):
            Am = np.array(m).reshape(2, 2)
            if round(np.linalg.det(Am)) % 5 == 0:
                continue
            if all(act[v][0] == tuple((Am @ np.array(v)) % 5) for v in act):
                found = Am; break
        A[k] = (gm, found)
    linear = all(f is not None for _, f in A.values())
    Ks = []
    for m in itertools.product(range(5), repeat=4):
        K = np.array(m).reshape(2, 2)
        d = round(np.linalg.det(K)) % 5
        if d == 0:
            continue
        Ki = (np.round(np.linalg.inv(K) * np.linalg.det(K)).astype(int) * pow(d, -1, 5)) % 5
        if all(np.array_equal((K @ gm @ Ki) % 5, f % 5) for gm, f in A.values()):
            Ks.append((K.tolist(), d, "residue" if d in SQ else "non-residue"))
    print("a=%d: the labels move linearly, v -> A_a(g) v, for every g: %s; K with A_a(g) = K g K^-1 for all g: %d of them;"
          " their determinants: %s" % (a, linear, len(Ks), sorted({(d, c) for _, d, c in Ks})))
    print("a=%d: first such K: %s" % (a, Ks[0][0] if Ks else None))
