"""B637 stage 3 — the alternating 3-form on the four D_phi involution
doubles (prereg 99815a48) + the unbent-table regeneration.

Per family: side-2 letters from the lifted intertwiner (as in part 2a);
peripheral pair on side 2 = (phi(mu), phi(lambda)) words; the class-level
gates (coboundary invariance slot-0, antisymmetry 01-swap) asserted per
double; then the 10-component table. Certificates use conjugation
peeling + the beam search.
"""
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))
mod = {"__name__": "b637_module", "__file__": os.path.join(
    HERE, "b637_threeform.py")}
exec(compile(open(os.path.join(HERE, "b637_threeform.py")).read(),
             "b637_threeform.py", "exec"), mod)

K, K0, K1 = mod["K"], mod["K0"], mod["K1"]
freduce, inv = mod["freduce"], mod["inv"]
LONG, REL = mod["LONG"], mod["REL"]
Side, side1 = mod["Side"], mod["side1"]
minv, mconj, lift_sl2 = mod["minv"], mod["mconj"], mod["lift_sl2"]
meye, mmul = mod["meye"], mod["mmul"]
apply_ = mod["apply"]
nullspace = mod["nullspace"]
ns = mod["ns"]
A27, B27 = mod["A27"], mod["B27"]
lets1 = {'a': A27, 'b': B27, 'A': mod["A27i"], 'B': mod["B27i"]}

# conjugation-peeling wrapper for certificates on conjugated cores
_base_certify = mod["certify"]


def certify_peeled(word):
    w = freduce(word)
    if w == "":
        return []
    if len(w) >= 2 and w[0] == w[-1].swapcase():
        inner = certify_peeled(w[1:-1])
        return [(freduce(w[0] + u), e) for (u, e) in inner]
    return _base_certify(w)


# patch the module's certify (S_eval resolves it in mod's globals at call time)
mod["certify"] = certify_peeled
assert mod["certify"] is certify_peeled

from fractions import Fraction as Fr
ZB6 = K(Fr(1, 2), Fr(-1, 2))
Z6 = K(Fr(1, 2), Fr(1, 2))
FAMILIES = {
    "phi(a)=a": ("a", "baB", [[K1, ZB6], [K0, K1]]),
    "phi(a)=A": ("A", "bAB", [[K(-1), ZB6], [K0, K1]]),
    "phi(a)=b": ("b", "abA", [[K0, K1], [Z6, K1]]),
    "phi(a)=B": ("B", "aBA", [[K0, K1], [K0 - Z6, K1]]),
}


def phi_word(w, wa, wb):
    m = {'a': wa, 'b': wb, 'A': inv(wa), 'B': inv(wb)}
    return freduce("".join(m[ch] for ch in w))


def build_family(name):
    wa, wb, U = FAMILIES[name]
    g27 = minv(lift_sl2(mconj(U)))
    g27i = minv(g27)
    s2 = {ch: mmul(mmul(g27, mconj(lets1[ch])), g27i) for ch in "abAB"}
    pm = phi_word("a", wa, wb)
    pl = phi_word(LONG, wa, wb)
    return s2, pm, pl


def fox_reps(s2, pm, pl):
    """the amalgam kernel and 5 class representatives for D_phi."""
    lets4 = {'a': lets1['a'], 'b': lets1['b'], 'A': lets1['A'],
             'B': lets1['B'], 'c': s2['a'], 'd': s2['b'],
             'C': s2['A'], 'D': s2['B']}
    prim = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd',
            'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
    c_pm = pm.translate(str.maketrans("abAB", "cdCD"))
    c_pl = pl.translate(str.maketrans("abAB", "cdCD"))
    relators = [REL, REL.translate(str.maketrans("abAB", "cdCD")),
                "a" + inv(c_pm), LONG + inv(c_pl)]
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
            rows_all.append([L[g][i][j] for g in "abcd" for j in range(27)])
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
            if len(reps) == 5:
                break
    assert len(reps) == 5
    return reps, lets4


def sides_of(z):
    return ((z[0:27], z[27:54]), (z[54:81], z[81:108]))


def Yval_general(sideA, sideB, zA, zB, zC, per1, per2):
    (a1, a2), (b1, b2), (c1, c2) = map(sides_of, (zA, zB, zC))
    om1 = sideA.make_omega(a1, b1, c1)
    om2 = sideB.make_omega(a2, b2, c2)
    MU1, LAM1 = per1
    MU2, LAM2 = per2
    P1 = freduce(MU1 + LAM1)
    P2 = freduce(MU2 + LAM2)
    S1 = lambda g, h, gh: sideA.S_eval(om1, g, h, gh)
    S2 = lambda g, h, gh: sideB.S_eval(om2, g, h, gh)
    return (S1(MU1, LAM1, P1) - S1(LAM1, MU1, P1)) \
         - (S2(MU2, LAM2, P2) - S2(LAM2, MU2, P2))


import itertools as it
print("\n==== the D_phi involution doubles ====", flush=True)
for name in FAMILIES:
    t0 = time.time()
    s2, pm, pl = build_family(name)
    side2 = Side(s2)
    reps, lets4 = fox_reps(s2, pm, pl)
    per1 = ("a", LONG)
    per2 = (pm, pl)
    # gates: coboundary slot-0 + antisymmetry on the first triple
    def cob_shift(z, jvec=5):
        v = [K1 if t == jvec else K0 for t in range(27)]
        out = list(z)
        for gi, g in enumerate("abcd"):
            gv = apply_(lets4[g], v)
            for i in range(27):
                out[gi * 27 + i] = out[gi * 27 + i] + gv[i] - v[i]
        return out
    y0 = Yval_general(side1, side2, reps[0], reps[1], reps[2], per1, per2)
    ysh = Yval_general(side1, side2, cob_shift(reps[0]), reps[1], reps[2],
                       per1, per2)
    ysw = Yval_general(side1, side2, reps[1], reps[0], reps[2], per1, per2)
    gA = (ysh - y0).is_zero()
    gB = (ysw + y0).is_zero()
    print(f"  {name}: gates coboundary {gA}, antisymmetry {gB}", flush=True)
    assert gA and gB, f"CLASS-LEVEL GATES FAILED for {name}"
    nz = 0
    for (i, j, k) in it.combinations(range(5), 3):
        y = (y0 if (i, j, k) == (0, 1, 2) else
             Yval_general(side1, side2, reps[i], reps[j], reps[k],
                          per1, per2))
        if not y.is_zero():
            nz += 1
        print(f"    Y[{(i,j,k)}] = {'0' if y.is_zero() else str(y)}",
              flush=True)
    print(f"    nonzero: {nz}/10   ({time.time()-t0:.0f}s)", flush=True)

print("\n==== the unbent weld table (regeneration) ====", flush=True)
Yn, repsN, _, _ = mod["double_Y"](None, verbose=False)
nz = 0
for key in sorted(Yn):
    y = Yn[key]
    if not y.is_zero():
        nz += 1
    print(f"  Y[{key}] = {'0' if y.is_zero() else str(y)}", flush=True)
print(f"nonzero: {nz}/10", flush=True)
print("B637 stage 3 DONE", flush=True)
