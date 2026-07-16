"""Q-AREA — the silver swap chain-defect factor (prereg 299c7a4c).

The fig-8: defect = 2 conj(Y), area 2. The silver: area 4 — is the
defect 4 conj(Y) (the area law) or 2 conj(Y) (universal factor)?
Reuses the 3b-ii machinery verbatim (exec of its head through the Side
construction), then runs the chain-level comparison of B647 cell 2 on
one lawful silver triple.
"""
import json
import os
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
B649 = os.path.join(HERE, "..", "B649_silver_holonomy")

src = open(os.path.join(B649, "b649_stage3b_ii.py")).read()
head = src[:src.index('print("== G2: the 10-triple Y table ==')]
ns = {"__name__": "b654_shared", "__file__": os.path.join(B649, "b649_stage3b_ii.py")}
exec(compile(head, "b649_3bii_head.py", "exec"), ns)

L, Lc, L0, L1 = ns["L"], ns["Lc"], ns["L0"], ns["L1"]
side1, side2 = ns["side1"], ns["side2"]
reps = ns["reps"]
U27 = ns["U27"]
apply27 = ns["apply27"]
freduce, inv = ns["freduce"], ns["inv"]
MU, LAM = ns["MU"], ns["LAM"]

P1s = freduce(MU + LAM)
MU2w, LAM2w = MU, inv(LAM)
P2s = freduce(MU2w + LAM2w)


def sides_of(z):
    return ((z[0:27], z[27:54], z[54:81]),
            (z[81:108], z[108:135], z[135:162]))


def Jvec27(v):
    cv = [x.conj() for x in v]
    return apply27(U27, cv)


def jtrip(zpair3):
    return tuple(Jvec27(v) for v in zpair3)


# banked silver Y values for the tested triples
dY = json.load(open(os.path.join(B649, "silver_Y_L.json")))


def Yof(key):
    v = dY[key]
    return L([Fr(x) for x in v[:4]], [Fr(x) for x in v[4:]])


print("== Q-AREA: the silver chain-defect factor ==", flush=True)
for key, (i, j, k) in (("134", (1, 3, 4)), ("023", (0, 2, 3))):
    (a1, a2), (b1, b2), (c1, c2) = map(sides_of,
                                       (reps[i], reps[j], reps[k]))
    om1 = side1.make_omega(a1, b1, c1)
    om2J = side2.make_omega(jtrip(a1), jtrip(b1), jtrip(c1))
    # the single anomalous slot (B647 cell 2's convention): rev (lam, mu):
    # S2(J z1; lam2, mu2) - conj(S1(z1; lam, mu))
    B1v = side1.S_eval(om1, LAM, MU, P1s)
    A2v = side2.S_eval(om2J, LAM2w, MU2w, P2s)
    defect = A2v - B1v.conj()
    Y = Yof(key)
    for m in (2, 4):
        tgt = Lc(m) * L(Y.re[:], [-x for x in Y.im])
        print(f"  triple {key}: defect == {m}*conj(Y): "
              f"{(defect - tgt).is_zero()}", flush=True)
    print(f"    defect = re{[str(x) for x in defect.re]} "
          f"im{[str(x) for x in defect.im]}", flush=True)

print("\nQ-AREA DONE", flush=True)
