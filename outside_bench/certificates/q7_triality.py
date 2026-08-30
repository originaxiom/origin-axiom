#!/usr/bin/env python3
"""Q7 -- THE TRIALITY TEST: decide the group scheme (Spin(8) vs SO(8)) by the 27's decomposition.
Seal: seals/Q7_TRIALITY_PREREG.md.  Gate 5: no measured value.

T-1 invariants (exact, Q(sqrt-3)); T-2 commutant rank (modular, rigorous in the direction that
matters: reduction can only DROP rank, so nullity_p >= nullity_Q and a modular 12 rules out 18).
"""
import os, io, sys, time, random, contextlib
import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
B575 = os.path.join(REPO, "frontier", "B575_bridge_obstruction", "l51_obstruction.py")
src = open(B575).read(); cut = src.index("# ---------------------------------------------------------------- stage 4")
ns = {"__name__": "b575_prefix", "__file__": B575}
t0 = time.time(); print("building e6 in gl(27) (B575 stages 0-3)...", flush=True)
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src[:cut], B575, "exec"), ns)
K, K0, K1 = ns["K"], ns["K0"], ns["K1"]; E6 = ns["E6_BASIS"]; N = 27; NB = 78
print(f"  done {time.time()-t0:.0f}s", flush=True)

def rref(rows, ncols):
    M = [r[:] for r in rows]; piv = []; r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(M)) if not M[i][c].is_zero()), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]; iv = M[r][c].inv(); M[r] = [x*iv for x in M[r]]
        for i in range(len(M)):
            if i != r and not M[i][c].is_zero():
                f = M[i][c]; M[i] = [a - f*b for a, b in zip(M[i], M[r])]
        piv.append(c); r += 1
        if r == len(M): break
    return r, piv, M
def nullspace(rows, ncols):
    r, piv, M = rref(rows, ncols); free = [c for c in range(ncols) if c not in piv]
    out = []
    for fc in free:
        v = [K0]*ncols; v[fc] = K1
        for ri, pc in enumerate(piv): v[pc] = K(0) - M[ri][fc]
        out.append(v)
    return out

# ---- rebuild the stabilizer (same generic pair, seed 11, as memo 161) ----
random.seed(11)
xv = [K(random.randint(-4, 4)) for _ in range(N)]
yv = [K(random.randint(-4, 4)) for _ in range(N)]
rows = []
for k in range(N):
    rows.append([sum((E6[t][k][j]*xv[j] for j in range(N)), K0) for t in range(NB)])
for k in range(N):
    rows.append([sum((yv[i]*E6[t][i][k] for i in range(N)), K0) for t in range(NB)])
S = nullspace(rows, NB); d = len(S)
print(f"stabilizer dim (memo 161 reproduction): {d}")
assert d == 28, f"expected 28, got {d}"
def lincomb(cs, Ms):
    R = [[K0]*N for _ in range(N)]
    for c, M in zip(cs, Ms):
        if c.is_zero(): continue
        for i in range(N):
            Mi, Ri = M[i], R[i]
            for j in range(N):
                if not Mi[j].is_zero(): Ri[j] = Ri[j] + c*Mi[j]
    return R
BAS = [lincomb(v, E6) for v in S]

# ---- T-1: invariants, EXACT ----
print("\nT-1  dim of s-invariant vectors in the 27 (exact over Q(sqrt-3))", flush=True)
inv_rows = []
for M in BAS:
    for i in range(N): inv_rows.append([M[i][j] for j in range(N)])
inv = nullspace(inv_rows, N)
print(f"     dim invariants = {len(inv)}   (Spin(8) pattern 1+1+1+8v+8s+8c predicts 3)")
T1 = "T1-THREE" if len(inv) == 3 else "T1-OTHER"
print(f"     OUTCOME: {T1}")

# ---- T-2: commutant rank, modular ----
print("\nT-2  commutant dim {X in gl(27) : [X,M]=0 for all M in s}", flush=True)
print("     method: modulo primes p = 1 mod 3 (so sqrt(-3) exists). Reduction can only DROP")
print("     rank, so nullity_p >= nullity_Q: a modular 12 PROVES nullity_Q <= 12, ruling out 18.")
def sqrt_m3_mod(p):
    for r in range(2, p):
        if (r*r) % p == (p-3) % p: return r
    return None
def to_mod(M, p, r3):
    A = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        for j in range(N):
            e = M[i][j]
            an, ad = e.a.numerator % p, e.a.denominator % p
            bn, bd = e.b.numerator % p, e.b.denominator % p
            A[i, j] = (an*pow(int(ad), p-2, p) + bn*pow(int(bd), p-2, p)*r3) % p
    return A
def rank_mod(Mat, p):
    A = Mat % p; rows, cols = A.shape; r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if A[i, c] % p: piv = i; break
        if piv is None: continue
        A[[r, piv]] = A[[piv, r]]
        A[r] = (A[r] * pow(int(A[r, c]), p-2, p)) % p
        col = A[:, c].copy(); col[r] = 0
        nz = np.nonzero(col)[0]
        if len(nz): A[nz] = (A[nz] - np.outer(col[nz], A[r])) % p
        r += 1
        if r == rows: break
    return r
results = {}
for p in (10007, 100003, 1000003):
    if p % 3 != 1: continue
    r3 = sqrt_m3_mod(p)
    if r3 is None: continue
    Ms = [to_mod(BAS[i], p, r3) for i in range(d)]
    # X in gl(27): [X,M] = 0  ->  rows from (M^T (x) I - I (x) M) acting on vec(X)
    blocks = []
    for M in Ms[:6]:                      # 6 generators is ample for a simple algebra
        L = np.kron(np.eye(N, dtype=np.int64), M) - np.kron(M.T, np.eye(N, dtype=np.int64))
        blocks.append(L % p)
    A = np.vstack(blocks) % p
    rk = rank_mod(A, p); nullity = N*N - rk
    results[p] = nullity
    print(f"     p = {p:>8}: rank {rk}, commutant dim = {nullity}", flush=True)
vals = set(results.values())
T2 = ("T2-TRIALITY" if vals == {12} else "T2-VECTOR" if vals == {18} else "T2-OTHER")
print(f"\n     commutant dim across primes: {results}")
print(f"     OUTCOME: {T2}")
if T2 == "T2-TRIALITY":
    print("     => three singlets + THREE INEQUIVALENT 8s. The spin representations 8s and 8c")
    print("        are present; they exist for Spin(8) and NOT for SO(8).")

print(f"\n{'='*78}")
print(f"SUMMARY: {T1} | {T2}")
print("""
FENCES (seal section 2), held:
  * this closes ONE hypothesis of five; hypothesis 5 (orbit count = class set) is untouched;
  * B990's UNFAVOURABLE prior stands unrepudiated -- stated with its reason, that homogeneity
    has won every previous time;
  * identifying the acting group is STILL NOT a statement about the INTEGRAL group scheme
    over Z, which is what a class-set argument ultimately needs. That gap is named, not skipped;
  * the modular method proves nullity_Q <= the modular value. That it EQUALS it is inference.
""")
print("="*78)
