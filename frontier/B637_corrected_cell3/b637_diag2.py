"""B637 diagnostics round 2: E0 is the shift a cocycle; E1 which eta cell
moves; E2 delta S' = omega' on peripheral cells after the shift."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
mod = {"__name__": "b637_module", "__file__": os.path.join(
    HERE, "b637_threeform.py")}
exec(compile(open(os.path.join(HERE, "b637_threeform.py")).read(),
             "b637_threeform.py", "exec"), mod)

K, K0, K1 = mod["K"], mod["K0"], mod["K1"]
freduce, inv = mod["freduce"], mod["inv"]
LONG = mod["LONG"]
side1 = mod["side1"]
double_Y = mod["double_Y"]
apply_ = mod["apply"]
A27, B27 = mod["A27"], mod["B27"]
meye, mmul = mod["meye"], mod["mmul"]
ns = mod["ns"]
REL = mod["REL"]

Yn, reps, sides_of, side2 = double_Y(None, verbose=False)

# rebuild the amalgam Fox relation matrix (as in double_Y) to test cocycles
lets4 = {'a': A27, 'b': B27, 'A': mod["A27i"], 'B': mod["B27i"],
         'c': side2.lets['a'], 'd': side2.lets['b'],
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
        v = sum((row[t] * z[t] for t in range(108) if not z[t].is_zero()), K0)
        if not v.is_zero():
            return False
    return True


def cob_shift(z, jvec):
    v = [K1 if t == jvec else K0 for t in range(27)]
    out = list(z)
    segs = [(A27, 0), (B27, 27), (side2.lets['a'], 54), (side2.lets['b'], 81)]
    for (M, off) in segs:
        gv = apply_(M, v)
        for i in range(27):
            out[off + i] = out[off + i] + gv[i] - v[i]
    return out


zsh = cob_shift(reps[0], 5)
print(f"(E0) shifted rep0 is a cocycle: {is_cocycle(zsh)}", flush=True)
print(f"(E0) original rep0 is a cocycle: {is_cocycle(reps[0])}", flush=True)

# E1: which eta cell moves under the shift
z0s = sides_of(reps[0])
z1s = sides_of(reps[1])
z2s = sides_of(reps[2])
zss = sides_of(zsh)
MU, LAM, PROD = "a", LONG, freduce("a" + LONG)
MU2, LAM2, PROD2 = "a", inv(LONG), freduce("a" + inv(LONG))


def eta_cells(a_s, b_s, c_s):
    om1 = side1.make_omega(a_s[0], b_s[0], c_s[0])
    om2 = side2.make_omega(a_s[1], b_s[1], c_s[1])
    S1 = lambda g, h, gh: side1.S_eval(om1, g, h, gh)
    S2 = lambda g, h, gh: side2.S_eval(om2, g, h, gh)
    return (S1(MU, LAM, PROD), S1(LAM, MU, PROD),
            S2(MU2, LAM2, PROD2), S2(LAM2, MU2, PROD2))


c_ref = eta_cells(z0s, z1s, z2s)
c_sh = eta_cells(zss, z1s, z2s)
names = ["S1(mu,lam)", "S1(lam,mu)", "S2(mu,lam)", "S2(lam,mu)"]
for nm, r0, r1 in zip(names, c_ref, c_sh):
    d = r1 - r0
    print(f"(E1) {nm}: moved by {'0' if d.is_zero() else str(d)}", flush=True)
Ydiff = (c_sh[0] - c_sh[1] - c_sh[2] + c_sh[3]) \
      - (c_ref[0] - c_ref[1] - c_ref[2] + c_ref[3])
print(f"(E1) total Y shift = {Ydiff}", flush=True)

# E2: delta S' = omega' on peripheral cells (shifted alpha)
om1s = side1.make_omega(zss[0], z1s[0], z2s[0])
S1s = lambda g, h, gh: side1.S_eval(om1s, g, h, gh)
GHK = freduce("a" + LONG + "a")
lhs = (S1s(LAM, MU, PROD) - S1s(PROD, MU, GHK)
       + S1s(MU, PROD, GHK) - S1s(MU, LAM, PROD))
rhs = om1s(MU, LAM, MU)
print(f"(E2) deltaS'=omega' on [mu|lam|mu] side1: {(lhs-rhs).is_zero()}",
      flush=True)
print("diag2 DONE", flush=True)
