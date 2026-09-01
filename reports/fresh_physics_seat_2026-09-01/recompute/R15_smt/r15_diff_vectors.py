"""Post-blind diff: run the committed B854 instrument, compare its INV charge
vectors and basis conventions against my stage-1 reconstruction."""
import os, pickle
from fractions import Fraction
B854 = "/home/user/origin-axiom/frontier/B854_centralizer_exact/e6_centralizer.py"
g = {"__file__": B854, "__name__": "b854"}
import io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    exec(compile(open(B854).read(), B854, "exec"), g)
print("B854 ran; last lines of its output:")
print("\n".join(buf.getvalue().strip().splitlines()[-4:]))
INV = g["INV"]; ROOTS = g["ROOTS"]; N = g["N"]

HERE = os.path.dirname(os.path.abspath(__file__))
D = pickle.load(open(HERE + "/r15_e6_data.pkl", "rb"))
basis_mine = D["basis"]
charges = {int(n): {int(k): Fraction(x) for k, x in dic.items()} for n, dic in D["charges"].items()}

# map my basis order to theirs: mine: h0..h5 then sorted(roots); theirs: h0..h5 then ROOTS order
theirs_index = {}
for k, r in enumerate(ROOTS):
    theirs_index[tuple(r)] = N + k
perm = []
for b in basis_mine:
    if b[0] == "h":
        perm.append(b[1])
    else:
        perm.append(theirs_index[tuple(b[1])])

for n in (8, 14, 16, 22):
    v_theirs = INV[n]
    # my vector re-expressed in their order
    mine = [Fraction(0)] * len(v_theirs)
    for k, c in charges[n].items():
        mine[perm[k]] = c
    th = [Fraction(int(c.numerator), int(c.denominator)) for c in v_theirs]
    # ratio (projective comparison)
    ratios = set()
    exact_equal = mine == th
    prop = None
    for a, b in zip(mine, th):
        if (a == 0) != (b == 0):
            prop = "SUPPORT MISMATCH"; break
        if a != 0:
            ratios.add(a / b)
    if prop is None:
        prop = f"proportional, mine = {ratios} * theirs" if len(ratios) == 1 else f"NOT proportional ({len(ratios)} ratios)"
    print(f"charge x{n}: exact-equal={exact_equal}; {prop}")
