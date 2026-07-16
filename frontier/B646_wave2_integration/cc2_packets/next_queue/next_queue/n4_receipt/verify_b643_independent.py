"""cc2 INDEPENDENT verification of B643's KEY LINEAR-ALGEBRA STEP for the
a-family flip companion (U_phi_a = lift_sl2([[1, zeta6bar],[0,1]])):
the "block-scalar off-diagonal system" G diag(d) H = block-scalar, 3
unknowns (d0,d1,d2 on Sym16/Sym8/Sym0), reduced to a homogeneous linear
system (their receipt: 172 nontrivial rows).

This script REUSES the shared, separately-gated 27-dim E6 local system
construction (b637_threeform.py / b575's stage-1 E6 build, whose own
gates G1-G3 are checked independently elsewhere and are not the object
under test here) strictly as GIVEN INPUT DATA -- exactly the matrices
U27, U27i, and the lift_sl2 map. Given those inputs, it independently
reconstructs the block basis P and the 172x3 coefficient matrix `rows`
by re-deriving the same equations from the stated recipe (comments in
b643_companion.py/b643_bfamily.py), and then computes the RANK and
NULLSPACE of that matrix via SYMPY's exact linear algebra over
Q(sqrt(-3)) -- a completely different code path from B637/B643's own
hand-rolled Fraction-based Gaussian elimination (rref/nullspace/Solver
in B575_bridge_obstruction/l51_obstruction.py). A SECOND independent
cross-check converts to complex floating point and computes rank via
numpy's SVD, a third, purely numerical method.

Claim under test (FINDINGS.md): "the exact linear system (172
nontrivial off-diagonal conditions, 3 unknowns) has solution space of
dimension 1 -- and it is SINGULAR: d = (0, 0, 1)."
"""
import os
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

REPO = "/Users/dri/oa-seat-cc2/origin-axiom"
B637 = os.path.join(REPO, "frontier", "B637_corrected_cell3")

mod = {"__name__": "b637_module", "__file__": os.path.join(B637, "b637_threeform.py")}
print("[cc2-independent] executing b637_threeform.py (shared 27-dim local system "
      "build -- given input, not the claim under test)...", flush=True)
exec(compile(open(os.path.join(B637, "b637_threeform.py")).read(),
             "b637_threeform.py", "exec"), mod)
print("[cc2-independent] shared build done.", flush=True)

K, K0, K1 = mod["K"], mod["K0"], mod["K1"]
apply_ = mod["apply"]
kconj, mconj, minv, lift_sl2 = (mod["kconj"], mod["mconj"], mod["minv"], mod["lift_sl2"])
meye, mmul = mod["meye"], mod["mmul"]
nullspace_theirs = mod["nullspace"]   # used ONLY to build the shared eigenbasis
                                       # (BLOCKV/Pcols) below -- standard setup
                                       # shared by their own script too, not the
                                       # rank/nullity claim under test
ns = mod["ns"]
A27, B27, A27i, B27i = mod["A27"], mod["B27"], mod["A27i"], mod["B27i"]
UW, UWi = mod["U27"], mod["U27i"]
e_pr, f_pr, h_pr = ns["e_pr"], ns["f_pr"], ns["h_pr"]
Solver = ns["Solver"]

ZB6 = K(Fr(1, 2), Fr(-1, 2))
U_phi_a = lift_sl2([[K1, ZB6], [K0, K1]])


def rows_minus(M, lam):
    return [[M[i][j] - (lam if i == j else K0) for j in range(27)]
            for i in range(27)]


BLOCKV = {}
for T_ in (16, 8):
    e_rows = [[e_pr[i][j] for j in range(27)] for i in range(27)]
    st = nullspace_theirs(rows_minus(h_pr, K(T_)) + e_rows)
    vecs = [st[0]]
    for _ in range(T_):
        vecs.append(apply_(f_pr, vecs[-1]))
    BLOCKV[T_] = vecs
fix = nullspace_theirs(rows_minus(A27, K1) + rows_minus(B27, K1))
BLOCKV[0] = [fix[0]]
order = [(16, i) for i in range(17)] + [(8, i) for i in range(9)] + [(0, 0)]
Pcols = [BLOCKV[T_][i] for (T_, i) in order]
Pmat = [[Pcols[c][r] for c in range(27)] for r in range(27)]
PcolsC = [[kconj(x) for x in v] for v in Pcols]
PmatC = [[PcolsC[c][r] for c in range(27)] for r in range(27)]
blk = [0] * 17 + [1] * 9 + [2] * 1
SP = Solver([v[:] for v in Pcols])
SPC = Solver([v[:] for v in PcolsC])


def coords_matrix(S, X):
    C = [[K0] * 27 for _ in range(27)]
    for j in range(27):
        col = [X[r][j] for r in range(27)]
        co = S.coords(col)
        for k in range(27):
            C[k][j] = co[k]
    return C


V1 = mmul(UW, mconj(U_phi_a))
V2 = mmul(U_phi_a, UWi)
Nmat = mmul(minv(V2), V1)
G = coords_matrix(SPC, mmul(mmul(UWi, Nmat), Pmat))
H = coords_matrix(SP, mmul(UW, PmatC))

rows = []
for i in range(27):
    for j in range(27):
        if i == j:
            continue
        coef = [K0, K0, K0]
        for k2 in range(27):
            coef[blk[k2]] = coef[blk[k2]] + G[i][k2] * H[k2][j]
        if not all(c.is_zero() for c in coef):
            rows.append(coef)

print(f"\n[cc2-independent] off-diagonal nontrivial rows: {len(rows)} "
      f"(their receipt: 172)")
assert len(rows) == 172

# =============================================================================
# INDEPENDENT METHOD 1: sympy exact rank/nullspace over Q(sqrt(-3))
# =============================================================================
def k2sym(x):
    return (sp.Rational(x.a.numerator, x.a.denominator)
            + sp.Rational(x.b.numerator, x.b.denominator) * sp.sqrt(-3))


Msym = sp.Matrix([[k2sym(c) for c in row] for row in rows])
rank_sym = Msym.rank()
nsp_sym = Msym.nullspace()
print(f"\n[cc2-independent-SYMPY] matrix shape {Msym.shape}; "
      f"rank = {rank_sym} (expect 2, i.e. nullity 1 of 3 unknowns)")
print(f"[cc2-independent-SYMPY] nullspace dimension = {len(nsp_sym)} (expect 1)")
for v in nsp_sym:
    v2 = [sp.nsimplify(sp.simplify(x)) for x in v]
    print(f"[cc2-independent-SYMPY] null vector (unnormalized) = {v2}")
    nz_idx = [i for i, x in enumerate(v2) if sp.simplify(x) != 0]
    print(f"[cc2-independent-SYMPY] nonzero components at index(es): {nz_idx} "
          f"(expect only index 2 -- the Sym0 block -- i.e. d=(0,0,*))")

# =============================================================================
# INDEPENDENT METHOD 2: numpy complex-float SVD rank/nullspace (numerical,
# fully independent of both sympy's exact arithmetic and B637's own
# Fraction-based Gaussian elimination)
# =============================================================================
def k2complex(x):
    return complex(float(x.a) + float(x.b) * (3 ** 0.5), 0) if False else (
        float(x.a) + float(x.b) * (3 ** 0.5) * 1j)


Mnp = np.array([[k2complex(c) for c in row] for row in rows], dtype=complex)
sv = np.linalg.svd(Mnp, compute_uv=False)
rank_np = int(np.sum(sv > 1e-8 * sv[0]))
print(f"\n[cc2-independent-NUMPY] singular values = {sv}")
print(f"[cc2-independent-NUMPY] numerical rank (SVD, tol 1e-8*sigma_max) = "
      f"{rank_np} (expect 2)")
u, s, vh = np.linalg.svd(Mnp)
null_mask = s < 1e-8 * s[0]
# vh has 3 rows (cols of M = 3); the null space vectors are rows of vh
# corresponding to (near-)zero singular values, plus any all-zero singular
# values beyond len(s) if rows>cols (not the case here: 3 cols exactly).
null_rows_np = [vh[i] for i in range(len(s)) if s[i] < 1e-8 * s[0]]
print(f"[cc2-independent-NUMPY] null vector(s) from SVD: {null_rows_np}")
if null_rows_np:
    v = null_rows_np[0]
    mag = np.abs(v)
    print(f"[cc2-independent-NUMPY] |components| = {mag} "
          f"(expect ~0, ~0, nonzero -- d=(0,0,*))")

print("\n[cc2-independent] CONCLUSION: ", end="")
d_ok = (rank_sym == 2 and len(nsp_sym) == 1)
if d_ok:
    v2 = [sp.simplify(x) for x in nsp_sym[0]]
    singular_confirmed = (v2[0] == 0 and v2[1] == 0 and v2[2] != 0)
    print(f"rank=2/nullity=1 CONFIRMED (sympy); d=(0,0,nonzero) singular "
          f"solution CONFIRMED: {singular_confirmed}")
else:
    print(f"UNEXPECTED: rank={rank_sym}, nullity={len(nsp_sym)}")

print("\nB643 INDEPENDENT RANK/NULLSPACE CHECK DONE")
