"""The restated symmetry lemma for the J-pairing (D5's full demand) + the
J-paired quadratic witnesses (the chain sub-item registered 2026-07-15).

Computes: (i) J's symmetry type c (J^T = c J, forced by Schur); (ii) THE
MOVE-ACROSS LEMMA <Xu, v>_J = -eps_X <u, Xv>_J (verified on all six block
generators); (iii) the forced-zero criterion: <v_m v0, v0>_J = 0 is FORCED
iff eps_m c != -1 — computed for all six m and checked against the criterion;
(iv) the J-paired weld quadratics at m = 4, 8 (word b2, t = 1) — the first
entries of the J-corrected classical family that any future P3 must use.

Run: OA_SLOW=1 python3 lemma_cell.py (~15 min). Nothing to CLAIMS.md.
"""
import importlib.util
import os
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, '..', 'B575_bridge_obstruction',
                        'l51_obstruction.py')).read()
ns = {'__name__': 'l51mod'}
sys.argv = ['l51']
exec(compile(src, 'l51', 'exec'), ns)
K, K0, K1 = ns['K'], ns['K0'], ns['K1']
mmul, nullspace, rref = ns['mmul'], ns['nullspace'], ns['rref']
madd, mscale, meye, mexp_nil = ns['madd'], ns['mscale'], ns['meye'], ns['mexp_nil']
BLOCKS = ns['BLOCKS']
A27, B27 = ns['A27'], ns['B27']
e_pr, f_pr, h_pr = ns['e_pr'], ns['f_pr'], ns['h_pr']

kc = lambda x: K(x.a, -x.b)
mconj = lambda M: [[kc(x) for x in r] for r in M]


def mat_vec(M, v):
    return [sum((M[i][j] * v[j] for j in range(27) if not v[j].is_zero()), K0)
            for i in range(27)]


def fmt(x):
    if x.is_zero():
        return "0"
    if x.b == 0:
        return str(x.a)
    return f"({x.a}{'+' if x.b > 0 else ''}{x.b}w)"


# ---- rebuild J (as in steps3and5; weight-reduced solve) ----
wts = [h_pr[i][i] for i in range(27)]
pairs_idx = [(i, j) for i in range(27) for j in range(27)
             if (wts[i] + wts[j]).is_zero()]
idx_of = {p: k for k, p in enumerate(pairs_idx)}
nunk = len(pairs_idx)
v4 = BLOCKS[4][0]


def add_eq(X, sign, rows):
    for i in range(27):
        for j in range(27):
            row = [K0] * nunk
            nz = False
            for k in range(27):
                if not X[k][i].is_zero() and (k, j) in idx_of:
                    row[idx_of[(k, j)]] = row[idx_of[(k, j)]] + X[k][i]
                    nz = True
                if not X[k][j].is_zero() and (i, k) in idx_of:
                    row[idx_of[(i, k)]] = row[idx_of[(i, k)]] + (K(sign) * X[k][j])
                    nz = True
            if nz:
                rows.append(row)


rows = []
add_eq(e_pr, 1, rows)
add_eq(f_pr, 1, rows)
add_eq(v4, -1, rows)
Js = nullspace(rows)
assert len(Js) == 1
J = [[K0] * 27 for _ in range(27)]
for k, (i, j) in enumerate(pairs_idx):
    J[i][j] = Js[0][k]

# (i) the symmetry type c
cs = set()
for i in range(27):
    for j in range(27):
        if not J[i][j].is_zero():
            if J[j][i].is_zero():
                cs.add(None)
            else:
                cs.add(str((J[j][i] * J[i][j].inv()).a) + "," +
                       str((J[j][i] * J[i][j].inv()).b))
assert len(cs) == 1 and None not in cs
cval = cs.pop()
assert cval == "1,0", f"J symmetry type changed: {cval}"      # D8: symmetric
print(f"(i) J^T = c J with c = {cval}  (Schur-forced)")

# (ii) the move-across lemma on all six block generators
EPS = {1: 1, 5: 1, 7: 1, 11: 1, 4: -1, 8: -1}
pairJ = lambda u, v: sum((u[i] * mat_vec(J, v)[i] for i in range(27)), K0)
import random
random.seed(20260715)
ok = True
for m, vm in ((m, BLOCKS[m][0]) for m in (1, 4, 5, 7, 8, 11)):
    for _ in range(2):
        u = [K(Fr(random.randint(-3, 3))) for _ in range(27)]
        v = [K(Fr(random.randint(-3, 3))) for _ in range(27)]
        lhs = pairJ(mat_vec(vm, u), v)
        rhs = K(-EPS[m]) * pairJ(u, mat_vec(vm, v))
        ok &= (lhs - rhs).is_zero()
assert ok
print("(ii) THE MOVE-ACROSS LEMMA <Xu,v>_J = -eps_X <u,Xv>_J: verified on all")
print("     six block generators x random vectors (exact)")

# (iii) the forced-zero criterion vs the six contractions
Om = madd(madd(mmul(e_pr, f_pr), mmul(f_pr, e_pr)),
          mscale(K(Fr(1, 2)), mmul(h_pr, h_pr)))
v0 = nullspace(Om)[0]
c_num = K(Fr(int(cval.split(",")[0])), Fr(int(cval.split(",")[1])))
print("(iii) the forced-zero criterion: <v_m v0, v0>_J forced 0 iff eps_m*c != -1")
for m in (1, 4, 5, 7, 8, 11):
    vm = BLOCKS[m][0]
    val = pairJ(mat_vec(vm, v0), v0)
    forced = "FORCED" if not (K(EPS[m]) * c_num + K1).is_zero() else "not forced"
    assert val.is_zero(), f"L1-J nonzero at m={m}"                       # D8
    assert (forced == "FORCED") == (EPS[m] == 1), f"criterion split broken at m={m}"
    print(f"    m={m:2d} (eps={EPS[m]:+d}): value = {fmt(val)}   criterion: {forced}")

# (iv) the J-paired weld quadratics at m = 4, 8 (word b2, t = 1)
print("(iv) the J-paired weld values (t = 1, word b2) — the corrected classical entries:")
for m in (4, 8):
    vm = BLOCKS[m][0]
    cmat = mexp_nil(mscale(K(1), vm))
    cinv = mexp_nil(mscale(K(-1), vm))
    b2 = mmul(mmul(cmat, mconj(B27)), cinv)
    val = pairJ(v0, mat_vec(b2, v0))
    expected = {4: (Fr(-536479695357), Fr(536483888640)),
                8: (Fr(536481792003), Fr(-536481792000))}[m]
    assert (val.a, val.b) == expected, f"J-weld changed at m={m}: {val.a},{val.b}"  # D8
    print(f"    m={m}: <v0, b2 v0>_J = {fmt(val)}")
print("DONE")
