"""B639 stage 2 — D_conjtheta realized: side 2 = W . conj((rho^T)^-1) . W^-1
(the contragredient-conjugate; W = lift([[0,-1],[1,0]])), lambda inverted.
Gates: mu/lambda GL(27) matches; C-invariance of the side-2 letters (the
contragredient does NOT automatically preserve C — if it fails, banked as
the obstruction); h1 (cc2 predicts 3); class gates; THE NUMBER Y_theta.
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
B637 = os.path.join(HERE, "..", "B637_corrected_cell3")
mod = {"__name__": "b637_module",
       "__file__": os.path.join(B637, "b637_threeform.py")}
exec(compile(open(os.path.join(B637, "b637_threeform.py")).read(),
             "b637_threeform.py", "exec"), mod)
K, K0, K1 = mod["K"], mod["K0"], mod["K1"]
freduce, inv = mod["freduce"], mod["inv"]
LONG, REL = mod["LONG"], mod["REL"]
side1, Side = mod["side1"], mod["Side"]
apply_ = mod["apply"]
kconj, mconj, minv, lift_sl2 = (mod["kconj"], mod["mconj"], mod["minv"],
                                mod["lift_sl2"])
meye, mmul = mod["meye"], mod["mmul"]
nullspace = mod["nullspace"]
ns = mod["ns"]
Cval = mod["Cval"]
A27, B27, A27i, B27i = mod["A27"], mod["B27"], mod["A27i"], mod["B27i"]
lets1 = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}

W27 = lift_sl2([[K0, K(-1)], [K1, K0]])
W27i = minv(W27)


def transpose(M):
    return [[M[j][i] for j in range(27)] for i in range(27)]


def contra_conj(M):
    return mconj(minv(transpose(M)))


s2 = {ch: mmul(mmul(W27, contra_conj(lets1[ch])), W27i) for ch in "abAB"}
lam1 = meye(27)
for ch in LONG:
    lam1 = mmul(lam1, lets1[ch])
lam2m = meye(27)
for ch in LONG:
    lam2m = mmul(lam2m, s2[ch])
g_mu = ns["mzero_p"](ns["msub"](s2['a'], A27))
g_lam = ns["mzero_p"](ns["msub"](mmul(lam1, lam2m), meye(27)))
print(f"G1': mu-match {g_mu}, lambda-inversion {g_lam}", flush=True)
assert g_mu and g_lam

# C-invariance of the side-2 letters
u1 = [K(i % 5 - 2) for i in range(27)]
v1 = [K((2 * i) % 7 - 3) for i in range(27)]
w1 = [K((3 * i) % 4 - 1) for i in range(27)]
lhs = Cval(apply_(s2['a'], u1), apply_(s2['a'], v1), apply_(s2['a'], w1))
rhs = Cval(u1, v1, w1)
c_inv = (lhs - rhs).is_zero()
print(f"G1'': C-invariance of side-2 letters: {c_inv}", flush=True)
if not c_inv:
    print("  BANKED OBSTRUCTION: the contragredient side does not preserve "
          "the cubic C — the twisted double's cubic needs the glued (C, C*) "
          "pair; the naive Y_theta is not defined. Stopping per the prereg.",
          flush=True)
else:
    prim = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd',
            'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
    relators = [REL, REL.translate(str.maketrans("abAB", "cdCD")),
                "aC", LONG + LONG.translate(str.maketrans("abAB", "cdCD"))]
    lets4 = {'a': lets1['a'], 'b': lets1['b'], 'A': lets1['A'],
             'B': lets1['B'], 'c': s2['a'], 'd': s2['b'],
             'C': s2['A'], 'D': s2['B']}
    rows_all = []
    for w in relators:
        L = {g: [[K0] * 27 for _ in range(27)] for g in "abcd"}
        Pi = meye(27)
        for ch in w:
            g = prim[ch]
            if ch.islower():
                term = Pi
                sgn = 1
            else:
                term = mmul(Pi, lets4[ch])
                sgn = -1
            if sgn < 0:
                term = ns["mscale"](K(-1), term)
            L[g] = ns["madd"](L[g], term)
            Pi = mmul(Pi, lets4[ch])
        assert ns["mzero_p"](ns["msub"](Pi, meye(27)))
        for i in range(27):
            rows_all.append([L[g][i][j] for g in "abcd"
                             for j in range(27)])
    Zc = nullspace(rows_all)
    cob = []
    for j in range(27):
        v = [K1 if t == j else K0 for t in range(27)]
        entry = []
        for g in "abcd":
            gv = apply_(lets4[g], v)
            entry.extend([gv[i] - v[i] for i in range(27)])
        cob.append(entry)
    Solver = ns["Solver"]
    reps, basis = [], [r[:] for r in cob]
    for z in Zc:
        try:
            Solver(basis).coords(z)
        except ValueError:
            reps.append(z)
            basis.append(z)
    h1 = len(reps)
    fixrows = []
    for g in "abcd":
        M = lets4[g]
        for i in range(27):
            fixrows.append([M[i][j] - (K1 if i == j else K0)
                            for j in range(27)])
    h0 = len(nullspace(fixrows))
    print(f"h0 = {h0}, h1(D_conjtheta; 27) = {h1}  [cc2: 3]", flush=True)
    if h1 >= 3:
        side2 = Side(s2)
        def sides_of(z):
            return ((z[0:27], z[27:54]), (z[54:81], z[81:108]))
        def Yval(zA, zB, zC):
            (a1, a2), (b1, b2), (c1, c2) = map(sides_of, (zA, zB, zC))
            om1 = side1.make_omega(a1, b1, c1)
            om2 = side2.make_omega(a2, b2, c2)
            P1 = freduce("a" + LONG)
            MU2, LAM2 = "a", inv(LONG)
            P2 = freduce("a" + inv(LONG))
            S1 = lambda g, h, gh: side1.S_eval(om1, g, h, gh)
            S2 = lambda g, h, gh: side2.S_eval(om2, g, h, gh)
            return (S1("a", LONG, P1) - S1(LONG, "a", P1)) \
                 - (S2(MU2, LAM2, P2) - S2(LAM2, MU2, P2))
        def cob_shift(z, jv=5):
            v = [K1 if t == jv else K0 for t in range(27)]
            out = list(z)
            for gi, g in enumerate("abcd"):
                gv = apply_(lets4[g], v)
                for i in range(27):
                    out[gi * 27 + i] = out[gi * 27 + i] + gv[i] - v[i]
            return out
        y0 = Yval(reps[0], reps[1], reps[2])
        gA = (Yval(cob_shift(reps[0]), reps[1], reps[2]) - y0).is_zero()
        gB = (Yval(reps[1], reps[0], reps[2]) + y0).is_zero()
        print(f"class gates: coboundary {gA}, antisymmetry {gB}", flush=True)
        assert gA and gB
        print(f"\n==== Y_theta = {'0' if y0.is_zero() else str(y0)} ====",
              flush=True)
        if h1 > 3:
            import itertools as it
            for (i, j, k) in it.combinations(range(h1), 3):
                if (i, j, k) == (0, 1, 2):
                    continue
                y = Yval(reps[i], reps[j], reps[k])
                print(f"  Y[{(i,j,k)}] = {'0' if y.is_zero() else str(y)}",
                      flush=True)
print("B639 stage 2 DONE", flush=True)
