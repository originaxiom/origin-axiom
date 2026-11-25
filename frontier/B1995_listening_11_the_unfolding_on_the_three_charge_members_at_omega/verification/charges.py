"""Listening card 11 (main, 2026-11-25; data-free): the unfolding W+ = dL + dR and W+- = dL + dL^T + dR + dR^T on the triplet
at the common point, against omega's symmetry s = d(LR^-1) (the cyclic exchange): commutation, the matrices in the charge
basis, overlaps with the modes, and W+-'s long-run share per charge member. Exact (sympy).
    python3 -B charges.py > charges_run.txt"""
import sympy as sp
dL = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]]); dR = sp.Matrix([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
s = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
print("U0: omega's symmetry s = d(LR^-1) at the common point: dL dR^-1 = %s, dR^-1 dL = %s, the cyclic exchange = %s" % ((dL * dR.inv()).tolist(), (dR.inv() * dL).tolist(), s.tolist()))
Wp = dL + dR; Wpm = dL + dL.T + dR + dR.T
for name, W in (("W+", Wp), ("W+-", Wpm)):
    print("U1: %s commutes with s: %s; with s from LR^-1's own linear part: %s" % (name, W * s == s * W, W * (dL * dR.inv()) == (dL * dR.inv()) * W))
w = sp.exp(2 * sp.pi * sp.I / 3)
C = sp.Matrix([[1, 1, 1], [1, w, w ** 2], [1, w ** 2, w]]).T / sp.sqrt(3)   # columns: charge 0, 1, 2 eigenvectors of the cyclic exchange
for k in range(3):
    v = C[:, k]; ev = sp.simplify((s * v)[0] / v[0]) if v[0] != 0 else None
    print("charge member %d: s-eigenvalue %s" % (k, sp.nsimplify(sp.simplify(ev))))
for name, W in (("W+", Wp), ("W+-", Wpm)):
    Wc = sp.simplify(C.H * W * C)
    print("U2: %s in the charge basis (rows and columns charge 0, 1, 2): %s" % (name, [[sp.nsimplify(sp.simplify(e)) for e in row] for row in Wc.tolist()]))
for name, W in (("W+", Wp), ("W+-", Wpm)):
    rows = []
    for val, mult, vecs in W.eigenvects():
        for vec in vecs:
            vec = vec / sp.sqrt(sum(abs(e) ** 2 for e in vec))
            ov = [sp.nsimplify(sp.simplify(abs((C[:, k].H * vec)[0]) ** 2)) for k in range(3)]
            rows.append((sp.nsimplify(val), ov))
    print("U3: %s modes and their overlaps with charge members 0, 1, 2: %s" % (name, rows))
vals = Wpm.eigenvals(); top = max(vals, key=lambda e: abs(complex(e)))
P = sp.zeros(3, 3)
for val, mult, vecs in Wpm.eigenvects():
    if sp.simplify(val - top) == 0:
        B = sp.Matrix.hstack(*vecs); P += B * (B.T * B).inv() * B.T
print("U4: W+- top eigenvalue %s; the long-run share of each charge member <c|P_top|c>: %s" % (top, [sp.nsimplify(sp.simplify((C[:, k].H * P * C[:, k])[0])) for k in range(3)]))
