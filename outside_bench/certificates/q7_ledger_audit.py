#!/usr/bin/env python3
"""Q7 LEDGER AUDIT -- the centroid, the base field, and a hypothesis row that left the tally.

Seal: outside_bench/seals/Q7_LEDGER_AUDIT_PREREG.md (pushed before this file was written).
This audits THIS BENCH'S OWN CHAIN (memos 160/161/162).  Any defect is a bench error.

THE DISCRIMINATOR MEMO 161 DID NOT HAVE.  Its S3-SIMPLE test is "no basis element has centraliser
dimension >= 14, which a whole g2 factor would force" -- a necessary condition against ONE named
alternative.  It does not exclude Res_{L/F}(g2) for L/F quadratic, which has F-dimension 28,
generic centraliser F-dimension 4, and NO proper F-ideal: it passes every test memo 161 ran.

The CENTROID separates them in one computation:
    Gamma(h) = { T in End_F(h) : T[x,y] = [Tx,y] for all x,y }
    dim 1 -> h is CENTRAL over F   (excludes g2(+)g2 AND Res_{L/F}(g2))
    dim 2 -> g2(+)g2 (Gamma = F x F) or Res_{L/F}(g2) (Gamma = L)

Direction of rigour, declared in the seal: reduction mod p can only DROP rank, so
nullity_p >= nullity_F, and a modular 1 PROVES dim_F Gamma <= 1, hence = 1 (scalars are always in
the centroid).  The elimination never needs the equality.

Gate 5 untouched: exact arithmetic and modular reduction; no measured value.
"""
import os, io, sys, time, random, contextlib
from fractions import Fraction as Fr
import numpy as np

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
print(f"    build done in {time.time()-t0:.1f}s", flush=True)

K, K0, K1 = ns["K"], ns["K0"], ns["K1"]
E6 = ns["E6_BASIS"]; N = 27; NB = len(E6)
print(f"    e6 basis: {NB} matrices, {N}x{N}, entries in B575's class K = Q(sqrt-3)")

# ================================================================= CELL B: the base field
print("\n" + "=" * 78)
print("B  THE BASE FIELD -- is B575's e6 basis actually defined over Q?")
print("=" * 78)
tot = irr = 0
for M in E6:
    for row in M:
        for x in row:
            tot += 1
            if x.b != 0:
                irr += 1
print(f"     entries in the e6 basis                    : {tot}")
print(f"     entries with a NONZERO sqrt(-3) component  : {irr}")
B_OUT = "B-RATIONAL" if irr == 0 else "B-TWO-FIELDS"
print(f"     OUTCOME: {B_OUT}")
if irr:
    print("     => memos 161/162 compute over Q(sqrt-3) (the object's TRACE field).")
    print("        Route A's orbit problem (B990/B1093/B1099) is over Q, with its own cubic")
    print("        K = Q[x]/(x^3-12x-5).  TWO DIFFERENT FIELDS, BOTH WRITTEN K in this chain.")

# ================================================================= exact linear algebra over K
def rref(rows, ncols):
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

# ---- the stabilizer, exactly as memo 161 built it (same seed, same pair) --------------
print("\n" + "=" * 78)
print("A  THE CENTROID -- rebuilding memo 161's stabilizer, then asking what memo 161 did not")
print("=" * 78)
random.seed(11)
xv = [K(random.randint(-4, 4)) for _ in range(N)]
yv = [K(random.randint(-4, 4)) for _ in range(N)]
rows = []
for k in range(N):
    rows.append([sum((E6[t][k][j] * xv[j] for j in range(N)), K0) for t in range(NB)])
for k in range(N):
    rows.append([sum((yv[i] * E6[t][i][k] for i in range(N)), K0) for t in range(NB)])
S = nullspace(rows, NB); d = len(S)
print(f"     stabilizer dimension (memo 161's seed 11)  : {d}   {'[reproduces memo 161]' if d==28 else '[DOES NOT REPRODUCE]'}")
assert d == 28, "memo 161's dim-28 result did not reproduce; stop and report that instead"

BAS = [lincomb(v, E6) for v in S]
cols = [[M[i][j] for i in range(N) for j in range(N)] for M in BAS]
BT = [[cols[t][p] for t in range(d)] for p in range(N*N)]
sel, cur = [], []
for p in range(N*N):
    trial = cur + [BT[p][:]]
    rr, _, _ = rref([row[:] for row in trial], d)
    if rr == len(trial):
        cur = trial; sel.append(p)
        if len(sel) == d: break
P = [BT[p][:] for p in sel]
augI = [P[i][:] + [K1 if i == j else K0 for j in range(d)] for i in range(d)]
rI, pivI, RI = rref(augI, 2*d)
assert pivI[:d] == list(range(d))
Pinv = [[RI[i][d + j] for j in range(d)] for i in range(d)]
def coords(M):
    v = [M[sel[t] // N][sel[t] % N] for t in range(d)]
    sol = [sum((Pinv[i][t] * v[t] for t in range(d)), K0) for i in range(d)]
    for p in range(N*N):                       # full-span verification, memo 161's discipline kept
        acc = sum((BT[p][t] * sol[t] for t in range(d)), K0)
        if not (acc - M[p // N][p % N]).is_zero():
            raise AssertionError("bracket left the span -- not a subalgebra")
    return sol

print(f"     solving {d*(d-1)//2} brackets, each verified on all {N*N} coordinates ...", flush=True)
t1 = time.time()
C = [[[K0]*d for _ in range(d)] for _ in range(d)]
for i in range(d):
    for j in range(i + 1, d):
        cij = coords(matsub(matmul(BAS[i], BAS[j]), matmul(BAS[j], BAS[i])))
        C[i][j] = cij
        C[j][i] = [K(0) - x for x in cij]
    if i % 7 == 0: print(f"        row {i}/{d}  ({time.time()-t1:.0f}s)", flush=True)
print(f"     bracket CLOSES in the span for all {d*d} pairs -- subalgebra, proved not assumed")

# ---- A-2: the Killing form, exactly ----------------------------------------------------
def ad(i): return [[C[i][b][a] for b in range(d)] for a in range(d)]
ADS = [ad(i) for i in range(d)]
kil = [[K0]*d for _ in range(d)]
for i in range(d):
    Ai = ADS[i]
    for j in range(i, d):
        Aj = ADS[j]
        s = K0
        for a in range(d):
            for b in range(d):
                if not Ai[a][b].is_zero() and not Aj[b][a].is_zero():
                    s = s + Ai[a][b] * Aj[b][a]
        kil[i][j] = s; kil[j][i] = s
rk, _, _ = rref([r[:] for r in kil], d)
print(f"\n     A-2  KILLING FORM rank (exact, over K)     : {rk} of {d}")
A2 = "A2-NONDEGENERATE" if rk == d else "A2-DEGENERATE"
print(f"          OUTCOME: {A2}   (Cartan: nondegenerate <=> semisimple)")

# ---- A-1: the centroid, modulo two primes ----------------------------------------------
def modmap(p):
    """a ring hom K -> F_p, valid when p = 1 mod 3 (so -3 is a QR mod p)."""
    r = None
    for t in range(2, p):
        if (t * t + 3) % p == 0: r = t; break
    assert r is not None, f"-3 is not a square mod {p}"
    def f(x):
        an, ad_ = x.a.numerator % p, x.a.denominator % p
        bn, bd = x.b.numerator % p, x.b.denominator % p
        assert ad_ and bd, "denominator divisible by p"
        return (an * pow(ad_, p - 2, p) + r * bn * pow(bd, p - 2, p)) % p
    return f, r

def nullity_mod(p):
    f, r = modmap(p)
    Cm = np.zeros((d, d, d), dtype=np.int64)
    for i in range(d):
        for j in range(d):
            for k in range(d):
                Cm[i, j, k] = f(C[i][j][k])
    nv = d * d                                    # T[a][k] -> a*d + k
    eqs = []
    # ALL ordered pairs i != j (the (j,i) constraint is NOT implied by (i,j)); every equation
    # only cuts the solution space, so any subset gives a valid UPPER bound on nullity.
    for i in range(d):
        for j in range(d):
            if i == j: continue
            for a in range(d):
                row = np.zeros(nv, dtype=np.int64)
                row[a * d:(a + 1) * d] += Cm[i, j, :]           # sum_k C[i][j][k] T[a][k]
                row[np.arange(d) * d + i] -= Cm[:, j, a]        # - sum_b C[b][j][a] T[b][i]
                eqs.append(row % p)
    A = np.array(eqs, dtype=np.int64) % p
    # Gaussian elimination mod p
    Amat = A.copy(); nr = Amat.shape[0]; rank = 0
    for c in range(nv):
        piv = None
        nz = np.nonzero(Amat[rank:, c])[0]
        if nz.size == 0: continue
        piv = rank + nz[0]
        Amat[[rank, piv]] = Amat[[piv, rank]]
        inv = pow(int(Amat[rank, c]), p - 2, p)
        Amat[rank] = (Amat[rank] * inv) % p
        col = Amat[:, c].copy(); col[rank] = 0
        nzr = np.nonzero(col)[0]
        if nzr.size:
            Amat[nzr] = (Amat[nzr] - np.outer(col[nzr], Amat[rank])) % p
        rank += 1
        if rank == nr: break
    return nv - rank, rank, nv, r

print(f"\n     A-1  CENTROID  dim_F {{T : T[x,y] = [Tx,y]}}   ({d*d} unknowns, {d*(d-1)*d} equations)")
res = {}
for p in (100003, 1000003):
    t2 = time.time()
    nul, rank, nv, r = nullity_mod(p)
    res[p] = nul
    print(f"          p = {p:>8}  (sqrt(-3) = {r})   rank {rank} of {nv}  ->  nullity {nul}"
          f"   [{time.time()-t2:.0f}s]", flush=True)

nulmin = min(res.values())
A1 = "A-CENTRAL" if nulmin == 1 else "A-NONCENTRAL"
print(f"\n          OUTCOME: {A1}")
if A1 == "A-CENTRAL":
    print("          Reduction can only DROP rank, so nullity_p >= nullity_F; a modular 1 PROVES")
    print("          dim_F Gamma <= 1, and scalars force >= 1.  Hence dim_F Gamma = 1 EXACTLY:")
    print("          the stabilizer is CENTRAL simple over F -- NOT g2(+)g2 and NOT Res_{L/F}(g2).")
    print("          (The proof needs only the bound; no equality is inferred from the modulus.)")
else:
    print("          dim Gamma >= 2: the algebra is NOT central over F.  Memo 161's D4")
    print("          identification and memo 162's group identification BOTH need correction.")

print("\n" + "=" * 78)
print(f"SUMMARY: {A1} | {A2} | {B_OUT}")
print("=" * 78)
