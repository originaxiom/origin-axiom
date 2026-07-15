"""B602 cell N0 (per the sealed NORM_PREREG.md, sha256 8fd90acc...):
the pre-comparison constants, computed exactly. NO comparison happens here.

  (i)  g_m = (v_m v0)^T J (v_m v0) for m = 4, 8 — the J-Gram of the bent
       state (never computed before; if any g_m = 0 the J-norm cells are
       INVALID-DEGENERATE per the seal);
  (ii) the SU(3)_2 quantum dimensions d_(1,0), d_(2,0) = S_{0,lam}/S_{0,0}
       (the D-norm constants).

Run: OA_SLOW=1 python3 b602_n0_jgram.py   (~15 min, l51 build)
"""
import importlib.util
import os
import sys
from fractions import Fraction as Fr

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, '..', 'B575_bridge_obstruction',
                        'l51_obstruction.py')).read()
ns = {'__name__': 'l51mod'}
sys.argv = ['l51']
exec(compile(src, 'l51', 'exec'), ns)
K = ns['K']; K0 = ns['K0']; K1 = ns['K1']
mmul = ns['mmul']; madd = ns['madd']; mscale = ns['mscale']
nullspace = ns['nullspace']
BLOCKS = ns['BLOCKS']
e_pr = ns['e_pr']; f_pr = ns['f_pr']; h_pr = ns['h_pr']

half = K(Fr(1, 2))
Om = madd(madd(mmul(e_pr, f_pr), mmul(f_pr, e_pr)),
          mscale(half, mmul(h_pr, h_pr)))
v0 = nullspace(Om)[0]
V4 = BLOCKS[4][0]
wts = [h_pr[i][i] for i in range(27)]
pairs_idx = [(i, j) for i in range(27) for j in range(27)
             if (wts[i] + wts[j]).is_zero()]
idx_of = {p: k for k, p in enumerate(pairs_idx)}
nunk = len(pairs_idx)


def add_equations(X, sign, rows_):
    for i in range(27):
        for j in range(27):
            row = [K0] * nunk
            any_nz = False
            for k in range(27):
                if not X[k][i].is_zero() and (k, j) in idx_of:
                    row[idx_of[(k, j)]] = row[idx_of[(k, j)]] + X[k][i]
                    any_nz = True
                if not X[k][j].is_zero() and (i, k) in idx_of:
                    row[idx_of[(i, k)]] = row[idx_of[(i, k)]] + (K(sign) * X[k][j])
                    any_nz = True
            if any_nz:
                rows_.append(row)


rows = []
add_equations(e_pr, 1, rows)
add_equations(f_pr, 1, rows)
add_equations(V4, -1, rows)
Js = nullspace(rows)
assert len(Js) == 1
J = [[K0] * 27 for _ in range(27)]
for k, (i, j) in enumerate(pairs_idx):
    J[i][j] = Js[0][k]
print("J rebuilt (Schur-unique)", flush=True)


def matvec(M, v):
    return [sum((M[i][j] * v[j] for j in range(27) if not v[j].is_zero()), K0)
            for i in range(27)]


for m in (4, 8):
    bent = matvec(BLOCKS[m][0], v0)
    Jb = matvec(J, bent)
    g = sum((bent[i] * Jb[i] for i in range(27) if not bent[i].is_zero()), K0)
    tag = "ZERO (J-norm cells INVALID-DEGENERATE per the seal)" \
        if g.is_zero() else "nonzero"
    print(f"g_{m} = ({g.a}{'+' if g.b >= 0 else ''}{g.b}w)   [{tag}]",
          flush=True)

# (ii) the SU(3)_2 quantum dimensions
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(HERE, "..", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)
w, S, T, cc = b238.su3_data(2)
i0 = w.index((0, 0))
for lam in ((1, 0), (2, 0)):
    d = S[i0, w.index(lam)] / S[i0, i0]
    print(f"d_{lam} = {d.real:+.12f}{d.imag:+.2e}j", flush=True)
phi = (1 + 5 ** 0.5) / 2
print(f"(reference: phi = {phi:.12f})", flush=True)
print("N0 DONE (pre-comparison constants; banked blind before N1)", flush=True)
