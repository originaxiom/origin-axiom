#!/usr/bin/env python3
"""B884 -- the invariant cubic on the 27, and the SM-graded Yukawa-support table.

The unique e6-invariant in Sym^3(27) (the J3(O) determinant in our frame), solved
EXACTLY over Q from the invariance equations on the weight basis, then graded by
the enhancement-point charges (s1, y, y2): which SM-multiplet triples carry a
nonzero restriction of the cubic = the algebra-allowed coupling table. Structure
only -- which couplings exist, never values. The standard E6-GUT reading of 27^3
is cited context, not a claim.
"""
import json
import os
import random
from fractions import Fraction as Fr

import mpmath
import sympy as sp
from mpmath import mp

HERE = os.path.dirname(os.path.abspath(__file__))
REPJ = json.load(open(os.path.join(HERE, "..", "B883_the_27", "rep27.json")))
REP = {int(k): v for k, v in REPJ["rep"].items()}
WTS = [tuple(w) for w in REPJ["weights"]]

# ---------------------------------------------------------------- the cubic
print("[1] weight-zero triples...")
triples = []
for a in range(27):
    for b in range(a, 27):
        for c in range(b, 27):
            if all(WTS[a][k] + WTS[b][k] + WTS[c][k] == 0 for k in range(6)):
                triples.append((a, b, c))
print(f"    {len(triples)} unordered weight-zero triples")
tidx = {t: i for i, t in enumerate(triples)}


def sym_lookup(a, b, c):
    key = tuple(sorted((a, b, c)))
    return tidx.get(key)


print("[2] invariance equations (12 Chevalley generators), exact...")
# generators: e_i = root vectors of the 6 simple roots, f_i their negatives.
# B854 order: basis 6.. = root vectors in ROOTS order = pos roots first.
# simple roots = the 6 unit tuples; find their indices in the rep basis order:
# REP keys are B854 basis indices; simple e_i = index 6 + IDX6[simple_i].
# We don't have IDX6 here; recover: the rep of h_i is diagonal with the weights,
# and [h_j, e_i] = C[j][i] e_i -- but easier: any generating set works for
# invariance; use ALL 78 basis elements' equations restricted to a random
# subset for assembly, then certify with the full set.
rows = []
GENS = list(range(6, 78))     # all root vectors (h's give weight-zero: automatic)
for gidx in GENS:
    M = REP[gidx]
    # equation index: (a<=b<=c) target triples after action
    eqs = {}
    for (a, b, c) in triples:
        coef = tidx[(a, b, c)]
        for (x, y, z) in ((a, b, c), (b, a, c), (c, a, b)):
            # act on slot holding x: M[k][x] moves x -> k
            for k in range(27):
                if M[k][x]:
                    key = tuple(sorted((k, y, z)))
                    eqs.setdefault(key, {})
                    eqs[key][coef] = eqs[key].get(coef, 0) + M[k][x]
    for key, terms in eqs.items():
        row = [0] * len(triples)
        for coef, val in terms.items():
            row[coef] = val
        if any(row):
            rows.append(row)
print(f"    {len(rows)} equations over {len(triples)} unknowns")
Msp = sp.Matrix(rows)
ns = Msp.nullspace()
print(f"    nullspace dim = {len(ns)}  (uniqueness needs 1)")
assert len(ns) == 1
cub = [sp.nsimplify(x) for x in ns[0]]
den = sp.lcm([sp.Rational(c).q for c in cub])
cub = [sp.Rational(c) * den for c in cub]
gg = sp.gcd([sp.Rational(c).p for c in cub if c != 0])
cub = [int(c / gg) for c in cub]
vals = sorted(set(abs(c) for c in cub if c))
print(f"    integer form: support {sum(1 for c in cub if c)}/{len(triples)}, |coeffs| in {vals}")

# ---------------------------------------------------------------- the grading
print("[3] grade the 27 at the enhancement point...")
mp.dps = 30
import importlib.util
B854 = os.path.normpath(os.path.join(HERE, "..", "B854_centralizer_exact",
                                     "e6_centralizer.py"))
src6 = open(B854, encoding="utf-8").read()
g6 = {"__file__": B854, "__name__": "b854"}
exec(compile(src6, B854, "exec"), g6)
CUBIC = [500716339200, -159667200, -28224, 1]
t1 = sorted(13 * mp.re(r) for r in mpmath.polyroots(
    [mp.mpf(c) for c in CUBIC], maxsteps=200, extraprec=120))[0]


def rho_num(vec78):
    M = mp.zeros(27, 27)
    for p in range(78):
        c = vec78[p]
        if abs(c) < mp.mpf("1e-25"):
            continue
        Rp = REP[p]
        for i in range(27):
            for j in range(27):
                if Rp[i][j]:
                    M[i, j] += c * Rp[i][j]
    return M


inv8 = [mp.mpf(c.numerator) / mp.mpf(c.denominator) for c in g6["INV"][8]]
inv16 = [mp.mpf(c.numerator) / mp.mpf(c.denominator) for c in g6["INV"][16]]
s1 = [inv8[p] + t1 * inv16[p] for p in range(78)]

# y, y2: rebuild the Levi charges (descent pipeline, K1 side) -- adjoint level
DIM = 78


def admat_num(vec):
    A = mp.zeros(DIM, DIM)
    br6 = g6["br"]
    return A  # placeholder unused


# reuse the descent to get y, y2 as 78-vectors: run the minimal chain
exec(open(os.path.join(HERE, "..", "B876_descent", "descent.py")).read()
     .split("def main")[0], g6)  # no-op safe: only imports/constants
# -- instead of re-deriving here, load from a helper run below if present
YFILE = os.path.join(HERE, "levi_charges.json")
if not os.path.exists(YFILE):
    print("    (computing Levi charges via the descent pipeline...)")
    import subprocess
    subprocess.run(["python3", os.path.join(HERE, "make_levi_charges.py")],
                   check=True)
lv = json.load(open(YFILE))
y = [mp.mpc(mp.mpf(v[0]), mp.mpf(v[1])) for v in lv["y"]]
y2 = [mp.mpc(mp.mpf(v[0]), mp.mpf(v[1])) for v in lv["y2"]]

Rs1 = rho_num(s1)
Ry = rho_num(y)
Ry2 = rho_num(y2)
Mmix = Rs1 * mp.mpf("1.0") + Ry * mp.mpf("0.70710678118") \
    + Ry2 * mp.mpf("0.31622776601")
Mc = mp.matrix(27, 27)
for i in range(27):
    for j in range(27):
        Mc[i, j] = mp.mpc(Mmix[i, j])
E2, ER2 = mpmath.eig(Mc, left=False, right=True)
states = []
for i in range(27):
    v = mp.matrix([ER2[j, i] for j in range(27)])
    nv = mp.sqrt(sum(abs(v[j]) ** 2 for j in range(27)))
    v = v * (1 / nv)
    chs = []
    for Rz in (Rs1, Ry, Ry2):
        img = Rz * v
        chs.append(sum(img[j] * mp.conj(v[j]) for j in range(27)))
    states.append((chs, v))
pieces = []
for chs, v in states:
    for grp in pieces:
        if all(abs(chs[k] - grp["chs"][k]) < mp.mpf("1e-8") for k in range(3)):
            grp["vecs"].append(v)
            break
    else:
        pieces.append(dict(chs=chs, vecs=[v]))
pdims = sorted(len(p["vecs"]) for p in pieces)
print(f"    27 pieces: {pdims}")


def cubic_eval(u, v, w):
    tot = mp.mpc(0)
    for (a, b, c), ci in tidx.items():
        coef = cub[ci]
        if not coef:
            continue
        perms = {(a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)}
        for (x, yy, zz) in perms:
            tot += coef * u[x] * v[yy] * w[zz]
    return tot


print("[4] the support table (gap-classified, with calibration control)...")
random.seed(31)
# control: the cubic on random dense unit vectors -- the natural scale
ctrl = []
for _ in range(10):
    u = mp.matrix([mp.mpc(random.uniform(-1, 1), random.uniform(-1, 1))
                   for _ in range(27)])
    u = u * (1 / mp.sqrt(sum(abs(x) ** 2 for x in u)))
    v = mp.matrix([mp.mpc(random.uniform(-1, 1), random.uniform(-1, 1))
                   for _ in range(27)])
    v = v * (1 / mp.sqrt(sum(abs(x) ** 2 for x in v)))
    w = mp.matrix([mp.mpc(random.uniform(-1, 1), random.uniform(-1, 1))
                   for _ in range(27)])
    w = w * (1 / mp.sqrt(sum(abs(x) ** 2 for x in w)))
    ctrl.append(abs(cubic_eval(u, v, w)))
print(f"    control scale (random dense vectors): min {mp.nstr(min(ctrl),3)} max {mp.nstr(max(ctrl),3)}")
support = []
zero_cells = 0
for i in range(len(pieces)):
    for j in range(i, len(pieces)):
        for k in range(j, len(pieces)):
            csum = [pieces[i]["chs"][m] + pieces[j]["chs"][m]
                    + pieces[k]["chs"][m] for m in range(3)]
            vals_ = []
            for _ in range(3):
                u = pieces[i]["vecs"][random.randrange(len(pieces[i]["vecs"]))]
                v = pieces[j]["vecs"][random.randrange(len(pieces[j]["vecs"]))]
                w = pieces[k]["vecs"][random.randrange(len(pieces[k]["vecs"]))]
                vals_.append(abs(cubic_eval(u, v, w)))
            mx = max(vals_)
            support.append(dict(
                dims=[len(pieces[i]["vecs"]), len(pieces[j]["vecs"]),
                      len(pieces[k]["vecs"])],
                charge_norm=float(max(abs(c) for c in csum)),
                max_eval_f=float(mx), max_eval=mp.nstr(mx, 3)))
allv = sorted(s_["max_eval_f"] for s_ in support)
import math
gaps = [(math.log10(allv[i + 1] / max(allv[i], 1e-60)), i)
        for i in range(len(allv) - 1) if allv[i + 1] > 0]
gsize, gi = max(gaps)
thresh = math.sqrt(allv[gi] * allv[gi + 1])
coupled = [s_ for s_ in support if s_["max_eval_f"] > thresh]
zero_cells = len(support) - len(coupled)
print(f"    largest log10-gap {gsize:.1f} at threshold {thresh:.3e}")
print(f"    coupled triples: {len(coupled)}; zero triples: {zero_cells}")
for s_ in sorted(coupled, key=lambda x: -x["max_eval_f"]):
    print(f"      {s_['dims']}  |C| ~ {s_['max_eval']}  chargesum {s_['charge_norm']:.1e}")
support = coupled

res = dict(n_weight_zero_triples=len(triples),
           cubic_support=sum(1 for c in cub if c),
           cubic_coeff_values=vals, nullspace_dim=1,
           piece_dims=pdims, coupled=support, zero_triples=zero_cells)
json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1,
          sort_keys=True, default=str)
print("  results written")
