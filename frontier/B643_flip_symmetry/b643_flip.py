"""B643 — the flip symmetry on the weld double (prereg 76d64ba0).

tau*: the amphichiral flip phi (a->a, b->baB; B605 family 1, intertwiner
U_phi = [[1, zb6],[0,1]], certified rho(phi x) = +- U_phi conj(rho x)
U_phi^-1) acting PER SIDE with the antilinear companion. Gates F1-F4.
"""
import itertools as it
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
double_Y = mod["double_Y"]
apply_ = mod["apply"]
kconj, mconj, minv, lift_sl2 = (mod["kconj"], mod["mconj"], mod["minv"],
                                mod["lift_sl2"])
meye, mmul = mod["meye"], mod["mmul"]
nullspace = mod["nullspace"]
ns = mod["ns"]
from fractions import Fraction as Fr
A27, B27, A27i, B27i = mod["A27"], mod["B27"], mod["A27i"], mod["B27i"]
UW = mod["U27"]                       # the weld intertwiner lift
UWi = mod["U27i"]

ZB6 = K(Fr(1, 2), Fr(-1, 2))
U_phi = lift_sl2([[K1, ZB6], [K0, K1]])
U_phi_i = minv(U_phi)

Yn, reps, sides_of, side2 = double_Y(None, verbose=False)
lets4 = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i,
         'c': side2.lets['a'], 'd': side2.lets['b'],
         'C': side2.lets['A'], 'D': side2.lets['B']}

# phi on words (per side): a->a, b->baB
def phi_w(wd, lo=("a", "baB")):
    m = {'a': lo[0], 'b': lo[1], 'A': inv(lo[0]), 'B': inv(lo[1])}
    return freduce("".join(m[ch] for ch in wd))


def word_val(z, letters, wd, side_letters):
    """cocycle value on the word wd over given side letter matrices;
    z = (z_x, z_y) the two letter-values for that side."""
    val = [K0] * 27
    P = meye(27)
    for ch in wd:
        if ch == 'a':
            add = apply_(P, z[0])
        elif ch == 'b':
            add = apply_(P, z[1])
        elif ch == 'A':
            add = [K0 - x for x in apply_(mmul(P, side_letters['A']), z[0])]
        else:
            add = [K0 - x for x in apply_(mmul(P, side_letters['B']), z[1])]
        val = [val[t] + add[t] for t in range(27)]
        P = mmul(P, side_letters[ch])
    return val


S1L = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}
S2L = side2.lets


def tau_star(z, J1msign=1):
    """(tau* z)(x) = J_side( z(phi(x)) ), J1 = U_phi . conj (per side 1),
    J2 = UW . conj(J1-pattern) . UWi variant; try the direct same-J both
    sides first (the gates decide)."""
    za = (z[0:27], z[27:54])
    zc = (z[54:81], z[81:108])
    def J1(v):
        return apply_(U_phi, [kconj(x) for x in v])
    # side 1 letter values of tau*z: value at 'a' = J1(z(phi(a)='a')),
    # at 'b' = J1(z(phi(b)='baB'))
    na = J1(word_val(za, None, "a", S1L))
    nb = J1(word_val(za, None, "baB", S1L))
    # side 2: same flip in side-2 letters with the conjugated companion
    J2U = mmul(mmul(UW, mconj(U_phi)), UWi)
    def J2(v):
        return apply_(J2U, [kconj(x) for x in v])
    nc = J2(word_val(zc, None, "a", S2L))
    nd = J2(word_val(zc, None, "baB", S2L))
    if J1msign < 0:
        na = [K0 - x for x in na]
        nb = [K0 - x for x in nb]
        nc = [K0 - x for x in nc]
        nd = [K0 - x for x in nd]
    return list(na) + list(nb) + list(nc) + list(nd)


# cocycle test rows
prim = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd',
        'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
relators = [REL, REL.translate(str.maketrans("abAB", "cdCD")),
            "aC", LONG + LONG.translate(str.maketrans("abAB", "cdCD"))]
rows_all = []
for w_ in relators:
    L = {g: [[K0] * 27 for _ in range(27)] for g in "abcd"}
    Pi = meye(27)
    for ch in w_:
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
    for i in range(27):
        rows_all.append([L[g][i][j] for g in "abcd" for j in range(27)])


def is_cocycle(z):
    for row in rows_all:
        s = sum((row[t] * z[t] for t in range(108) if not z[t].is_zero()),
                K0)
        if not s.is_zero():
            return False
    return True


print("== F1: does tau* act? ==", flush=True)
t0 = tau_star(reps[0])
ok = is_cocycle(t0)
print(f"  tau*(rep0) cocycle (J-choice A): {ok}", flush=True)
if not ok:
    print("  trying the -J variant...", flush=True)
    t0 = tau_star(reps[0], -1)
    ok = is_cocycle(t0)
    print(f"  tau*(rep0) cocycle (J-choice B): {ok}", flush=True)
if not ok:
    print("F1 FAIL: the flip does not act on the double in either "
          "convention — BANKED OBSTRUCTION; stopping per the prereg.",
          flush=True)
else:
    all_ok = all(is_cocycle(tau_star(r)) for r in reps)
    print(f"  all 5: {all_ok}", flush=True)
    # coboundaries + solver
    cob = []
    for j in range(27):
        v = [K1 if t == j else K0 for t in range(27)]
        entry = []
        for g in "abcd":
            gv = apply_(lets4[g], v)
            entry.extend([gv[i] - v[i] for i in range(27)])
        cob.append(entry)
    Solver = ns["Solver"]
    def in_span(vecs, w_):
        try:
            Solver([v[:] for v in vecs]).coords(list(w_))
            return True
        except ValueError:
            return False
    icob = []
    for c in cob:
        if not icob or not in_span(icob, c):
            icob.append(c)
    basis = [r[:] for r in icob] + [list(r) for r in reps]
    S = Solver(basis)
    M = []
    for r in reps:
        co = S.coords(list(tau_star(r)))
        M.append(co[len(icob):])
    print("\n== F2: the tau*-matrix ==", flush=True)
    for i, row in enumerate(M):
        print(f"  tau*[{i}] = " + " ".join(
            ("0" if x.is_zero() else str(x)) for x in row), flush=True)
    sq = all(in_span(icob, [a - b for a, b in
                            zip(tau_star(tau_star(r)), r)]) for r in reps)
    print(f"  tau*^2 = id mod coboundaries: {sq}", flush=True)

    print("\n== F3: the law of Y under tau* ==", flush=True)
    def Yval(zA, zB, zC):
        (a1, a2), (b1, b2), (c1, c2) = map(sides_of, (zA, zB, zC))
        om1 = side1.make_omega(a1, b1, c1)
        om2 = side2.make_omega(a2, b2, c2)
        P1 = freduce("a" + LONG)
        MU2, LAM2 = "a", inv(LONG)
        P2 = freduce("a" + inv(LONG))
        Sa = lambda g, h, gh: side1.S_eval(om1, g, h, gh)
        Sb = lambda g, h, gh: side2.S_eval(om2, g, h, gh)
        return (Sa("a", LONG, P1) - Sa(LONG, "a", P1)) \
             - (Sb(MU2, LAM2, P2) - Sb(LAM2, MU2, P2))
    for (i, j, k2) in [(0, 2, 3), (1, 2, 3), (0, 1, 2)]:
        y = Yval(reps[i], reps[j], reps[k2])
        yt = Yval(tau_star(reps[i]), tau_star(reps[j]),
                  tau_star(reps[k2]))
        yc = kconj(y)
        laws = [nm for nm, v in
                (("minus_conj", (yt + yc).is_zero()),
                 ("plus_conj", (yt - yc).is_zero()),
                 ("minus_id", (yt + y).is_zero()),
                 ("plus_id", (yt - y).is_zero())) if v]
        print(f"  triple {(i,j,k2)}: laws {laws}; Y = {y}; Y(tau*) = {yt}",
              flush=True)
print("\nB643 gates DONE (F4 = the combined-system solve, next stage)",
      flush=True)
