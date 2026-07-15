"""B603 — the J-isotropy mechanism + the center alignment (failure-enforcing
on identities; measurements printed).

REGISTERED BEFORE RUNNING (MB12 triple-check):
  P-A (prediction, CAN fail): g_m = (v_m v0)^T J (v_m v0) = 0 at ALL six
      blocks m in {1,4,5,7,8,11} — extending N0's two zeros (the even
      blocks could genuinely be nonzero; nothing yet forces them).
  P-B (identity + mechanism): the move-across lemma gives
      g_m = -eps_m * <v0, v_m^2 v0>_J exactly (verified per block), and
      the vanishing mechanism candidate is WEIGHT SELECTION: v_m has
      h-weight +2m, so v_m^2 v0 lives at weights (mu + 4m); J pairs only
      weight-opposite pairs; the contraction is empty iff v0 has no
      component pair (mu, -mu-4m) with J-coupling. The script computes
      the weight supports and reports whether the zero is weight-FORCED
      or genuine per block (both outcomes meaningful; not gated).
  P-C (measurement, no prior): the Z3 center charges of the nine E6_2
      primaries (triality of the weight), the charges of the three odd
      pairs, and whether the V3 real channel (eigenvalue -1 eigenvector
      of the odd form B) is supported on a single charge sector.
      Registered as a MEASUREMENT — either outcome banks as data.

Run: OA_SLOW=1 python3 isotropy_mechanism.py   (~15 min, l51 build)
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


def jp(u, v):
    Jv = matvec(J, v)
    return sum((u[i] * Jv[i] for i in range(27) if not u[i].is_zero()), K0)


EPS = {1: 1, 4: -1, 5: 1, 7: 1, 8: -1, 11: 1}
v0_supp = {int(wts[i].a) for i in range(27) if not v0[i].is_zero()}
print(f"v0 weight support: {sorted(v0_supp)}", flush=True)

print("\nP-A/P-B — the isotropy law and its mechanism:", flush=True)
allid = True
for m in sorted(BLOCKS):
    v = BLOCKS[m][0]
    bent = matvec(v, v0)
    g = jp(bent, bent)
    inner = jp(v0, matvec(v, matvec(v, v0)))
    # the move-across identity g = -eps * <v0, v^2 v0>_J
    ident = (g - (K(-EPS[m]) * inner)).is_zero()
    allid &= ident
    # weight-forcing: does v0 contain a pair (mu, -mu-4m)?
    forced = not any((-mu - 4 * m) in v0_supp for mu in v0_supp)
    print(f"  m={m:2d}: g_m = {'0' if g.is_zero() else 'NONZERO'};  "
          f"move-across identity [{ident}];  "
          f"weight-FORCED zero: {forced}", flush=True)
assert allid, "move-across identity failed"

# ---- P-C: the E6_2 center charges and the V3 channel ------------------------
spec = importlib.util.spec_from_file_location(
    "c3", os.path.join(HERE, "..", "B570_allowed_plays",
                       "c3_e6_level2_monodromy.py"))
c3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c3)
W, eps_signs = c3.weyl_group()
rho_w = c3.root_coords([1] * 6)
shifted = [c3.root_coords(p) + rho_w for p in c3.PRIM]
S = np.zeros((9, 9), dtype=complex)
Wl = np.einsum('wij,lj->wli', W.astype(float), np.array(shifted))
for a in range(9):
    for b in range(a, 9):
        ips = Wl[:, a, :] @ (c3.C @ shifted[b])
        S[a, b] = S[b, a] = np.sum(eps_signs * np.exp(-2j * np.pi * ips / c3.KH))
S /= np.sqrt((S @ S.conj().T)[0, 0].real)
if S[0, 0].real < 0:
    S = -S
ipf = lambda x, y: float(x @ (c3.C @ y))
cc = 2 * 78 / c3.KH
hs = [ipf(c3.root_coords(p), c3.root_coords(p) + 2 * rho_w) / (2 * c3.KH)
      for p in c3.PRIM]
T = np.diag([np.exp(2j * np.pi * (h - cc / 24)) for h in hs])
rho = T @ T @ S @ T
Cm = (S @ S).real
pairs = [(1, 2, "27"), (3, 4, "351'"), (7, 8, "351")]
U = np.zeros((9, 3))
for j, (a, b, _) in enumerate(pairs):
    U[a, j], U[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
B = U.T @ (Cm @ rho) @ U

# the center charges, convention-independently: the simple currents are the
# primaries with quantum dimension 1 (vacuum aside); for a simple current
# sigma, S_{sigma,p} = e^{2 pi i Q(p)} S_{0,p} — Q is the Z3 charge.
i0 = 0                                      # c3.PRIM[0] is the vacuum row?
d = np.array([S[i0, k] / S[i0, i0] for k in range(9)])
# locate the vacuum robustly: the row with all S_{0,p} > 0
for cand in range(9):
    dd = S[cand, :] / S[cand, cand]
    if np.all(dd.real > -1e-9) and abs(dd[cand] - 1) < 1e-9:
        i0 = cand
        d = dd
        break
print(f"\nP-C — quantum dimensions (vacuum = primary {i0}):", flush=True)
for k in range(9):
    print(f"  primary {k}: {tuple(c3.PRIM[k])}  d = {d[k].real:+.6f}",
          flush=True)
currents = [k for k in range(9) if k != i0 and abs(d[k] - 1) < 1e-6]
print(f"simple currents (d = 1, non-vacuum): {currents}", flush=True)
if currents:
    sig = currents[0]
    Q = np.angle(S[sig, :] / S[i0, :]) * 3 / (2 * np.pi)
    Qr = [int(round(q)) % 3 for q in Q]
    print(f"Z3 charges Q(p) (from sigma = {sig}): {Qr}", flush=True)
    for a, b, nm in pairs:
        print(f"  odd pair {nm:>4} = ({a},{b}): charges ({Qr[a]}, {Qr[b]})",
              flush=True)
lams, vecs = np.linalg.eig(B)
print("odd-form eigenvalues:", "  ".join(f"{z:+.6f}" for z in lams), flush=True)
real_idx = min(range(3), key=lambda i: abs(lams[i].imag))
vr = vecs[:, real_idx]
print(f"the V3 real channel (lambda = {lams[real_idx]:+.6f}) eigenvector "
      f"|components| in (27, 351', 351): "
      + "  ".join(f"{abs(x):.6f}" for x in vr), flush=True)
print("\nB603 DONE", flush=True)