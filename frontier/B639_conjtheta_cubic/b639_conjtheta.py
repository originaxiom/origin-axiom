"""B639 — C2: the cubic on D_conjtheta(M) (prereg 7075dd63..., sealed).

The twisted double: mu -> mu, lambda -> +lambda (the OPPOSITE sign from
the weld) against the conjugate representation. G1: the intertwiner
exists + GL(27) gates + h1 = 3 (cc2's number, fourth pipeline);
G2: three classes + class-level gates; G3: THE ONE NUMBER
Y_theta = Y(z0, z1, z2) in Q(sqrt-3).
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
A27, B27, A27i, B27i = (mod["A27"], mod["B27"], mod["A27i"], mod["B27i"])
lets1 = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}
lam2 = mod["lam2"]
lets2 = mod["lets2"]
wmat2 = mod["wmat2"]

print("== G1: the lambda -> +lambda intertwiner ==", flush=True)
Ag = lets2['a']
Agc = [[kconj(x) for x in row] for row in Ag]
lam2c = [[kconj(x) for x in row] for row in wmat2(LONG)]
rows_u = []
for (X, Y_) in ((Agc, Ag), (lam2c, lam2)):        # u conj(lam) u^-1 = +lam
    for i in range(2):
        for j in range(2):
            row = [K0] * 4
            for kk in range(2):
                row[i * 2 + kk] = row[i * 2 + kk] + X[kk][j]
                row[kk * 2 + j] = row[kk * 2 + j] - Y_[i][kk]
            rows_u.append(row)
solu = nullspace(rows_u)
print(f"  intertwiner space: dim {len(solu)}", flush=True)
u2 = None
for s_ in solu:
    cand = [[s_[0], s_[1]], [s_[2], s_[3]]]
    det = cand[0][0] * cand[1][1] - cand[0][1] * cand[1][0]
    if not det.is_zero():
        u2 = cand
        break
assert u2 is not None, "G1 FAIL: no invertible +lambda intertwiner"
U27t = lift_sl2(u2)
U27ti = minv(U27t)
s2 = {ch: mmul(mmul(U27t, mconj(lets1[ch])), U27ti) for ch in "abAB"}
lam27 = mod["lam27"] if "lam27" in mod else None
lam27_1 = meye(27)
for ch in LONG:
    lam27_1 = mmul(lam27_1, lets1[ch])
lam27_2 = meye(27)
for ch in LONG:
    lam27_2 = mmul(lam27_2, s2[ch])
g_mu = ns["mzero_p"](ns["msub"](s2['a'], A27))
g_lam = ns["mzero_p"](ns["msub"](lam27_2, lam27_1))
print(f"  GL(27) gates: mu-match {g_mu}, lambda-MATCH(+) {g_lam}",
      flush=True)
assert g_mu and g_lam, "G1 FAIL: lifted gates"

# relators: r, r', aC, LONG(a,b) * inv(LONG(c,d))   [lambda = lambda']
prim = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd',
        'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
c_l = LONG.translate(str.maketrans("abAB", "cdCD"))
relators = [REL, REL.translate(str.maketrans("abAB", "cdCD")),
            "aC", LONG + inv(c_l)]
lets4 = {'a': lets1['a'], 'b': lets1['b'], 'A': lets1['A'], 'B': lets1['B'],
         'c': s2['a'], 'd': s2['b'], 'C': s2['A'], 'D': s2['B']}
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
    assert ns["mzero_p"](ns["msub"](Pi, meye(27))), f"relator fails: {w[:12]}"
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
fixrows = []
for g in "abcd":
    M = lets4[g]
    for i in range(27):
        fixrows.append([M[i][j] - (K1 if i == j else K0) for j in range(27)])
h0 = len(nullspace(fixrows))
Solver = ns["Solver"]
reps, basis = [], [r[:] for r in cob]
for z in Zc:
    try:
        Solver(basis).coords(z)
    except ValueError:
        reps.append(z)
        basis.append(z)
h1 = len(reps)
print(f"  h0(D_conjtheta; 27) = {h0}, h1 = {h1}  "
      f"[cc2's prediction: h1 = 3]", flush=True)

if h1 < 3:
    print("G3 VOID: fewer than 3 classes — no cubic exists; banked.",
          flush=True)
else:
    side2 = Side(s2)
    def sides_of(z):
        return ((z[0:27], z[27:54]), (z[54:81], z[81:108]))
    def Yval(zA, zB, zC):
        (a1, a2), (b1, b2), (c1, c2) = map(sides_of, (zA, zB, zC))
        om1 = side1.make_omega(a1, b1, c1)
        om2 = side2.make_omega(a2, b2, c2)
        P1 = freduce("a" + LONG)
        S1 = lambda g, h, gh: side1.S_eval(om1, g, h, gh)
        S2 = lambda g, h, gh: side2.S_eval(om2, g, h, gh)
        return (S1("a", LONG, P1) - S1(LONG, "a", P1)) \
             - (S2("a", LONG, P1) - S2(LONG, "a", P1))
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
    print(f"  G2 gates: coboundary {gA}, antisymmetry {gB}", flush=True)
    assert gA and gB, "G2 FAIL"
    print(f"\n==== THE NUMBER: Y_theta = "
          f"{'0' if y0.is_zero() else str(y0)} ====", flush=True)
    if h1 > 3:
        import itertools as it
        print(f"  (h1 = {h1} > 3: the full table)", flush=True)
        for (i, j, k) in it.combinations(range(h1), 3):
            y = y0 if (i, j, k) == (0, 1, 2) else Yval(reps[i], reps[j],
                                                       reps[k])
            print(f"  Y[{(i,j,k)}] = {'0' if y.is_zero() else str(y)}",
                  flush=True)
print("B639 DONE", flush=True)
