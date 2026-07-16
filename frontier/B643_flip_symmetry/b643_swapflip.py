"""B643 step 2 — the SIDE-EXCHANGING flip (L93 refined).

Step 1 found phi(LONG) = LONG^{-1} exactly (empty conjugator) and
phi(mu) = mu: the flip is clean on pi_1 but inverts the longitude, so
on the weld double the orientation-reversing flip must EXCHANGE sides
(flip . deck-swap = orientation-preserving, LINEAR companion):

  Phi = s . phi  (a -> c, b -> dcD, c -> a, d -> baB)
  rho(Phi y) = V rho_1(y) V^{-1},  V  = U27 . conj(U_phi27)  (side 1)
  rho(Phi y) = V' rho_2(y) V'^{-1}, V' = U_phi27 . U27i       (side 2)

Pullback z'(y) = V^{-1} z(Phi y) per slot.  Gates F1-F3; a global-
companion diagnostic Q = U_phi^{-1} u conj(u_phi) u at SL(2).
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
ns = mod["ns"]
from fractions import Fraction as Fr
A27, B27, A27i, B27i = mod["A27"], mod["B27"], mod["A27i"], mod["B27i"]
UW, UWi = mod["U27"], mod["U27i"]

ZB6 = K(Fr(1, 2), Fr(-1, 2))
U_phi = lift_sl2([[K1, ZB6], [K0, K1]])
U_phi_i = minv(U_phi)

Yn, reps, sides_of, side2 = double_Y(None, verbose=False)
lets4 = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i,
         'c': side2.lets['a'], 'd': side2.lets['b'],
         'C': side2.lets['A'], 'D': side2.lets['B']}
S1L = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}
S2L = side2.lets


def word_val(z, wd, side_letters):
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


# ---- global-companion diagnostic at SL(2) ----------------------------------
lets2 = mod["lets2"]
uw2 = mod.get("u")
if uw2 is not None:
    def mm2(A, B):
        return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)]
                for i in range(2)]
    def mc2(M):
        return [[kconj(x) for x in row] for row in M]
    def mi2(M):
        return [[M[1][1], K0 - M[0][1]], [K0 - M[1][0], M[0][0]]]
    u_phi2 = [[K1, ZB6], [K0, K1]]
    Q = mm2(mm2(mi2(u_phi2), mm2(uw2, mc2(u_phi2))), uw2)
    print(f"  SL2 global-companion Q = U_phi^-1 u conj(u_phi) u = "
          f"{[[str(x) for x in r] for r in Q]}", flush=True)

# ---- the candidate conventions ----------------------------------------------
V1 = mmul(UW, mconj(U_phi))            # side-1 companion
V2 = mmul(U_phi, UWi)                  # side-2 companion
CONVS = {
    "A(derived: W=V^-1)": (minv(V1), minv(V2)),
    "B(no-inverse: W=V)": (V1, V2),
    "C(cross: W1=V2^-1,W2=V1^-1)": (minv(V2), minv(V1)),
}


def tau_swap(z, W1, W2):
    za = (z[0:27], z[27:54])
    zc = (z[54:81], z[81:108])
    na = apply_(W1, word_val(zc, "a", S2L))       # Phi(a) = c
    nb = apply_(W1, word_val(zc, "baB", S2L))     # Phi(b) = dcD
    nc = apply_(W2, word_val(za, "a", S1L))       # Phi(c) = a
    nd = apply_(W2, word_val(za, "baB", S1L))     # Phi(d) = baB
    return list(na) + list(nb) + list(nc) + list(nd)


# ---- cocycle rows ------------------------------------------------------------
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
        else:
            term = ns["mscale"](K(-1), mmul(Pi, lets4[ch]))
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


print("== F1: which convention acts? ==", flush=True)
winner = None
for nm, (W1, W2) in CONVS.items():
    ok = is_cocycle(tau_swap(reps[0], W1, W2))
    print(f"  {nm}: tau*(rep0) cocycle = {ok}", flush=True)
    if ok and winner is None:
        winner = (nm, W1, W2)

if winner is None:
    print("F1 FAIL for all conventions — the side-exchanging flip does "
          "not act either; BANK the strengthened obstruction.", flush=True)
else:
    nm, W1, W2 = winner
    print(f"\n  winner: {nm}", flush=True)
    all_ok = all(is_cocycle(tau_swap(r, W1, W2)) for r in reps)
    print(f"  all 5 reps: {all_ok}", flush=True)

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
    print("\n== F2: the tau*-matrix (mod coboundaries) ==", flush=True)
    Mrows = []
    for r in reps:
        co = S.coords(list(tau_swap(r, W1, W2)))
        Mrows.append(co[len(icob):])
    for i, row in enumerate(Mrows):
        print(f"  tau*[{i}] = " + " ".join(
            ("0" if x.is_zero() else str(x)) for x in row), flush=True)
    sq = all(in_span(icob, [a - b for a, b in
                            zip(tau_swap(tau_swap(r, W1, W2), W1, W2), r)])
             for r in reps)
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

    for (i, j, k2) in [(0, 2, 3), (1, 2, 3), (0, 1, 2), (2, 3, 4)]:
        y = Yval(reps[i], reps[j], reps[k2])
        yt = Yval(tau_swap(reps[i], W1, W2), tau_swap(reps[j], W1, W2),
                  tau_swap(reps[k2], W1, W2))
        yc = kconj(y)
        laws = [nm2 for nm2, v in
                (("minus_conj", (yt + yc).is_zero()),
                 ("plus_conj", (yt - yc).is_zero()),
                 ("minus_id", (yt + y).is_zero()),
                 ("plus_id", (yt - y).is_zero())) if v]
        ratio = "n/a"
        if not y.is_zero():
            try:
                ratio = str(yt / y)
            except Exception:
                ratio = "div-fail"
        print(f"  triple {(i,j,k2)}: laws {laws}; Y = {y}; "
              f"Y(tau*) = {yt}; ratio = {ratio}", flush=True)

print("\nB643 step 2 DONE", flush=True)
