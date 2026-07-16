"""B638 — C1: the swap decomposition (prereg a645834a..., sealed first).

sigma: (a,b) <-> (c,d) on pi_1(D); J = Ad(U27) . conj (antilinear).
(sigma* z)(x) = J(z(sigma x)): gates G1-G5 per the prereg.
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
kconj, mconj, minv = mod["kconj"], mod["mconj"], mod["minv"]
meye, mmul = mod["meye"], mod["mmul"]
nullspace = mod["nullspace"]
ns = mod["ns"]
U27 = mod["U27"]
U27i = mod["U27i"]
u = mod["u"]

print("== G1: the involution property ==", flush=True)
# u * conj(u) at SL(2) level
uc = [[kconj(x) for x in row] for row in u]
prod = [[sum((u[i][t] * uc[t][j] for t in range(2)), K0) for j in range(2)]
        for i in range(2)]
print(f"  u*conj(u) = {prod}", flush=True)
is_plus = all((prod[i][j] - (K1 if i == j else K0)).is_zero()
              for i in range(2) for j in range(2))
is_minus = all((prod[i][j] + (K1 if i == j else K0)).is_zero()
               for i in range(2) for j in range(2))
print(f"  = +1: {is_plus};  = -1: {is_minus}", flush=True)


def Jop(v):
    return apply_(U27, [kconj(x) for x in v])


def Jinv(v):
    return [kconj(x) for x in apply_(U27i, v)]


# sigma* on amalgam cocycles z = (za, zb, zc, zd):
# sigma(a) = c, sigma(b) = d, sigma(c) = a, sigma(d) = b
# (sigma* z)(a) = J(z(sigma a)) = J(zc), etc.
def sigma_star(z):
    za, zb, zc, zd = z[0:27], z[27:54], z[54:81], z[81:108]
    return (list(Jop(zc)) + list(Jop(zd)) + list(Jop(za)) + list(Jop(zb)))


Yn, reps, sides_of, side2 = double_Y(None, verbose=False)

# cocycle test rows (rebuild as in stage 3)
lets4 = {'a': mod["A27"], 'b': mod["B27"], 'A': mod["A27i"],
         'B': mod["B27i"], 'c': side2.lets['a'], 'd': side2.lets['b'],
         'C': side2.lets['A'], 'D': side2.lets['B']}
prim = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd',
        'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
relators = [REL, REL.translate(str.maketrans("abAB", "cdCD")),
            "aC", LONG + LONG.translate(str.maketrans("abAB", "cdCD"))]
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
    for i in range(27):
        rows_all.append([L[g][i][j] for g in "abcd" for j in range(27)])


def is_cocycle(z):
    for row in rows_all:
        s = sum((row[t] * z[t] for t in range(108) if not z[t].is_zero()), K0)
        if not s.is_zero():
            return False
    return True


coc_ok = all(is_cocycle(sigma_star(rep)) for rep in reps)
print(f"  sigma*(rep_i) are cocycles, all 5: {coc_ok}", flush=True)

# sigma*^2 = id mod coboundaries
cob = []
for j in range(27):
    v = [K1 if t == j else K0 for t in range(27)]
    entry = []
    for g in "abcd":
        gv = apply_(lets4[g], v)
        entry.extend([gv[i] - v[i] for i in range(27)])
    cob.append(entry)
Solver = ns["Solver"]


def in_span(vecs, w):
    try:
        Solver([v[:] for v in vecs]).coords(list(w))
        return True
    except ValueError:
        return False


# independent coboundary basis (rank 26 of 27)
icob = []
for c in cob:
    if not icob or not in_span(icob, c):
        icob.append(c)
sq_ok = all(in_span(icob,
                    [a - b for a, b in
                     zip(sigma_star(sigma_star(rep)), rep)])
            for rep in reps)
print(f"  sigma*^2 = id mod coboundaries, all 5: {sq_ok}", flush=True)
assert coc_ok, "G1 FAIL: sigma* does not preserve cocycles"

print("\n== G2: the matrix of sigma* on H^1 (antilinear) ==", flush=True)
# express sigma*(rep_i) = sum_j M_ij rep_j mod coboundaries
basis = [r[:] for r in icob] + [list(r) for r in reps]
S = Solver(basis)
M = []
for rep in reps:
    co = S.coords(list(sigma_star(rep)))
    M.append(co[len(icob):])
for i, row in enumerate(M):
    print(f"  sigma*[{i}] = " + " ".join(
        ("0" if x.is_zero() else str(x)) for x in row), flush=True)

print("\n== G3: the transformation law of Y ==", flush=True)


def Yval(zA, zB, zC):
    (a1, a2), (b1, b2), (c1, c2) = map(sides_of, (zA, zB, zC))
    om1 = side1.make_omega(a1, b1, c1)
    om2 = side2.make_omega(a2, b2, c2)
    MU1, LAM1 = "a", LONG
    P1 = freduce("a" + LONG)
    MU2, LAM2 = "a", inv(LONG)
    P2 = freduce("a" + inv(LONG))
    S1 = lambda g, h, gh: side1.S_eval(om1, g, h, gh)
    S2 = lambda g, h, gh: side2.S_eval(om2, g, h, gh)
    return (S1(MU1, LAM1, P1) - S1(LAM1, MU1, P1)) \
         - (S2(MU2, LAM2, P2) - S2(LAM2, MU2, P2))


laws = {"minus_conj": 0, "plus_conj": 0, "minus_id": 0, "plus_id": 0}
for (i, j, k) in [(0, 1, 2), (0, 2, 3), (1, 2, 3)]:
    y = Yval(reps[i], reps[j], reps[k])
    ys = Yval(sigma_star(reps[i]), sigma_star(reps[j]),
              sigma_star(reps[k]))
    yc = kconj(y)
    tests = {"minus_conj": (ys + yc).is_zero(),
             "plus_conj": (ys - yc).is_zero(),
             "minus_id": (ys + y).is_zero(),
             "plus_id": (ys - y).is_zero()}
    print(f"  triple {(i,j,k)}: Y = {y}; Y(sigma*) = {ys}; "
          f"laws: {[k_ for k_, v in tests.items() if v]}", flush=True)
    for k_, v in tests.items():
        laws[k_] += int(v)
print(f"  law tally over 3 triples: {laws}", flush=True)
print("\nB638 gates G1-G3 DONE (G4/G5 analysis follows from the banked "
      "matrix + law)", flush=True)
