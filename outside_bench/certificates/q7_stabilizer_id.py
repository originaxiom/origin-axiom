#!/usr/bin/env python3
"""Q7 continued -- COMPUTE the stabilizer of a pair in e6, do not guess it.
Seal: seals/Q7_STABILIZER_ID_PREREG.md.  Reuses B575's exact e6-in-gl(27) build (the prefix-exec
B632 uses) and works in B575's own exact Q(sqrt-3) class -- no floating point anywhere.

FENCE (seal section 2): even S3-SIMPLE closes ONE hypothesis of five; a Lie-algebra identification
is not a group-scheme identification; B990's unfavourable prior stands.  Gate 5: no measured value.
"""
import os, io, sys, time, random, contextlib
from fractions import Fraction as Fr

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
B575 = os.path.join(REPO, "frontier", "B575_bridge_obstruction", "l51_obstruction.py")
src = open(B575).read()
cut = src.index("# ---------------------------------------------------------------- stage 4")
ns = {"__name__": "b575_prefix", "__file__": B575}
t0 = time.time()
print("executing B575 stages 0-3 (exact e6-in-gl(27) build, its own gates)...", flush=True)
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    exec(compile(src[:cut], B575, "exec"), ns)
for ln in buf.getvalue().splitlines():
    if "PASS" in ln or "complete" in ln: print("   ", ln.strip())
print(f"    build done in {time.time()-t0:.1f}s", flush=True)

K, K0, K1 = ns["K"], ns["K0"], ns["K1"]
E6 = ns["E6_BASIS"]; N = 27; NB = len(E6)
print(f"    e6 basis: {NB} matrices, {len(E6[0])}x{len(E6[0][0])}, entries in Q(sqrt-3)")

# ---------- exact linear algebra over K ----------
def rref(rows, ncols):
    """returns (rank, pivot_cols, reduced rows) -- exact, in K."""
    M = [r[:] for r in rows]; piv = []; r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(M)) if not M[i][c].is_zero()), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        iv = M[r][c].inv()
        M[r] = [x * iv for x in M[r]]
        for i in range(len(M)):
            if i != r and not M[i][c].is_zero():
                f = M[i][c]; M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c); r += 1
        if r == len(M): break
    return r, piv, M

def nullspace(rows, ncols):
    r, piv, M = rref(rows, ncols)
    free = [c for c in range(ncols) if c not in piv]
    out = []
    for fc in free:
        v = [K0] * ncols; v[fc] = K1
        for ri, pc in enumerate(piv): v[pc] = K(0) - M[ri][fc]
        out.append(v)
    return out

def matmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(N)), K0) for j in range(N)] for i in range(N)]
def matsub(A, B): return [[A[i][j] - B[i][j] for j in range(N)] for i in range(N)]
def lincomb(cs, Ms):
    R = [[K0]*N for _ in range(N)]
    for c, M in zip(cs, Ms):
        if c.is_zero(): continue
        for i in range(N):
            Mi, Ri = M[i], R[i]
            for j in range(N):
                if not Mi[j].is_zero(): Ri[j] = Ri[j] + c * Mi[j]
    return R

# ---------- S-1: the stabilizer's dimension ----------
print("\nS-1  stabilizer of a pair (x in 27, y in 27*) as an EXACT nullspace")
def stab(seed):
    random.seed(seed)
    xv = [K(random.randint(-4, 4)) for _ in range(N)]
    yv = [K(random.randint(-4, 4)) for _ in range(N)]
    rows = []
    for k in range(N):                       # (A x)_k = 0
        rows.append([sum((E6[t][k][j] * xv[j] for j in range(N)), K0) for t in range(NB)])
    for k in range(N):                       # (y A)_k = 0
        rows.append([sum((yv[i] * E6[t][i][k] for i in range(N)), K0) for t in range(NB)])
    return nullspace(rows, NB)

S = stab(11); d = len(S)
print(f"     seed 11: dim = {d}")
S_ctrl = stab(29)
print(f"     seed 29 (control on 'generic'): dim = {len(S_ctrl)}"
      f"   {'same' if len(S_ctrl)==d else 'DIFFERENT -- not a generic value'}")
S1 = "S1-28" if d == 28 and len(S_ctrl) == 28 else "S1-OTHER"
print(f"     OUTCOME: {S1}   (memo 160 predicted 28 by subtraction; this is by construction)")
if d == 0: sys.exit(0)

# ---------- structure constants ----------
print(f"\nS-2/S-3  the stabilizer's own structure, from its bracket")
BAS = [lincomb(v, E6) for v in S]
cols = [[M[i][j] for i in range(N) for j in range(N)] for M in BAS]   # d vectors of length 729
BT = [[cols[t][p] for t in range(d)] for p in range(N*N)]             # 729 x d
# SPEED, without losing exactness: pick d independent ROWS of BT once, invert that dxd block once,
# then every bracket is solved by one small multiply instead of a 729-row rref. The full-span check
# is preserved by VERIFYING the reconstruction on all 729 coordinates for every bracket.
aug = [BT[p][:] + [K(p)] for p in range(N*N)]      # tag rows to recover their indices
r0, piv0, R0 = rref([row[:d] for row in BT], d)
assert r0 == d, "the stabilizer basis is not independent"
# recover d independent row indices greedily
sel, cur = [], []
for p in range(N*N):
    trial = cur + [BT[p][:]]
    rr, _, _ = rref([row[:] for row in trial], d)
    if rr == len(trial):
        cur = trial; sel.append(p)
        if len(sel) == d: break
assert len(sel) == d, "could not find d independent coordinate rows"
P = [BT[p][:] for p in sel]
# invert P by rref on [P | I]
augI = [P[i][:] + [K1 if i == j else K0 for j in range(d)] for i in range(d)]
rI, pivI, RI = rref(augI, 2*d)
assert pivI[:d] == list(range(d)), "pivot block not invertible"
Pinv = [[RI[i][d + j] for j in range(d)] for i in range(d)]
def coords(M):
    v = [M[sel[t] // N][sel[t] % N] for t in range(d)]
    sol = [sum((Pinv[i][t] * v[t] for t in range(d)), K0) for i in range(d)]
    # VERIFY on all 729 coordinates -- this is the closure check, not an assumption
    for p in range(N*N):
        acc = sum((BT[p][t] * sol[t] for t in range(d)), K0)
        if not (acc - M[p // N][p % N]).is_zero():
            raise AssertionError("bracket left the span -- not a subalgebra")
    return sol
print(f"     solving {d*(d-1)//2} brackets (antisymmetry), each verified on all 729 coords ...",
      flush=True)
C = [[[K0]*d for _ in range(d)] for _ in range(d)]
for i in range(d):
    for j in range(i + 1, d):
        cij = coords(matsub(matmul(BAS[i], BAS[j]), matmul(BAS[j], BAS[i])))
        C[i][j] = cij
        C[j][i] = [K(0) - x for x in cij]
    if i % 7 == 0: print(f"        row {i}/{d}", flush=True)
print(f"     bracket CLOSES in the span for all {d*d} pairs -- it is a subalgebra")

def ad(i): return [[C[i][b][a] for b in range(d)] for a in range(d)]
def rank_sq(M):
    r, _, _ = rref([row[:] for row in M], d); return r

random.seed(5)
gencoef = [K(random.randint(-3, 3)) for _ in range(d)]
adg = [[K0]*d for _ in range(d)]
for i in range(d):
    if gencoef[i].is_zero(): continue
    Ai = ad(i)
    for a in range(d):
        for b in range(d): adg[a][b] = adg[a][b] + gencoef[i] * Ai[a][b]
rank_alg = d - rank_sq(adg)
print(f"     rank (centraliser dim of a generic element) = {rank_alg}")
S2 = "S2-RANK4" if rank_alg == 4 else "S2-OTHER"
print(f"     OUTCOME: {S2}")

cents = [d - rank_sq(ad(i)) for i in range(d)]
big = [c for c in cents if c >= 14]
print(f"     centraliser dims across the basis: min {min(cents)}, max {max(cents)}")
print(f"     elements whose centraliser is >= 14 (a whole g2 factor would force this): {len(big)}")
S3 = "S3-SIMPLE" if not big else "S3-DECOMPOSABLE"
print(f"     OUTCOME: {S3}   (so(8) is simple; g2 (+) g2 is not)")

print(f"\n{'='*78}")
print(f"SUMMARY: {S1} | {S2} | {S3}")
print("""
FENCE (seal section 2), held:
  * even S3-SIMPLE closes ONE hypothesis of five -- hypothesis 5 (orbit count = class set)
    is untouched;
  * this identifies a LIE ALGEBRA, not a GROUP SCHEME: so(8) is compatible with Spin(8),
    SO(8) and PGO(8), and ONLY the simply connected Spin(8) gives strong approximation;
  * B990's declared UNFAVOURABLE prior stands unrepudiated.
""")
print("="*78)
