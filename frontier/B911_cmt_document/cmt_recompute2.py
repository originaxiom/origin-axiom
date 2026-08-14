#!/usr/bin/env python3
"""B911 -- follow-up cell: the noncompact walls DERIVED from the build (no
normalization hypothesis), then the pairing law, the SST matching, and the
invisible-12 kernel signature, at the fresh prime.

The first cell (cmt_recompute.py) showed dim z = 30 at the banked B880 CUBIC's
roots: the banked cubic lives in a different charge normalization than the raw
B854 invariants (the raw build reproduced the SOLO kappa exactly, lambda = 1).
Here the noncompact degeneration polynomial N(t) of ad(g8 + t*g16) on e6/core
is INTERPOLATED FROM THE BUILD mod p (degree bound 48 proven: 48x48, entries
affine in t; 49 nodes + 6 checks), its roots compared against BOTH mu_solo's
and the banked CUBIC's roots mod p, and the wall suite is run at the true
walls: dim 46 / derived 45 / center 1 (L5's D5+u(1) bookkeeping), the 3x3
pairing table (diag 30 / off-diag 18), the matching vs the exact SST bijection
s*(rho) mod p, nesting, and ker((ad8 + rho*ad16)|M12) = 4 at each true wall.
"""
import json
import os
import time
from fractions import Fraction as Fr

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
B854 = os.path.normpath(os.path.join(HERE, "..", "B854_centralizer_exact",
                                     "e6_centralizer.py"))
T0 = time.time()
RES = {}


def log(m):
    print(f"[{time.time()-T0:7.1f}s] {m}", flush=True)


def save():
    json.dump(RES, open(os.path.join(HERE, "cmt_recompute2_results.json"), "w"),
              indent=1, sort_keys=True, default=str)


log("exec of the banked B854 build ...")
src = open(B854, encoding="utf-8").read()
g = {"__file__": os.path.join(HERE, "b854_rerun2.py"), "__name__": "b854b"}
exec(compile(src, B854, "exec"), g)
DIM, N = g["DIM"], g["N"]
ROOTS, BB, INV, C = g["ROOTS"], g["BB"], g["INV"], g["C"]
if os.path.exists(os.path.join(HERE, "results.json")):
    os.remove(os.path.join(HERE, "results.json"))

triples = {}
for pq in range(DIM):
    for q in range(DIM):
        for r, c in enumerate(BB[pq][q]):
            if c:
                triples.setdefault(pq, []).append((q, r, int(c)))
CH = {n: INV[n] for n in (8, 14, 16, 22)}

p = 40829            # the fresh split prime from cell 1
RES["prime"] = p


def redp(x):
    if isinstance(x, Fr):
        return x.numerator % p * pow(x.denominator % p, p - 2, p) % p
    xr = sp.Rational(x)
    return int(xr.p) % p * pow(int(xr.q) % p, p - 2, p) % p


def admatp(vec):
    A = [[0] * DIM for _ in range(DIM)]
    for pi, vp in enumerate(vec):
        if not vp:
            continue
        vps = redp(vp)
        for q, r, c in triples.get(pi, []):
            A[r][q] = (A[r][q] + vps * c) % p
    return A


def rankp(rows):
    R = [list(r) for r in rows]
    m = len(R)
    n = len(R[0]) if m else 0
    rank = 0
    for col in range(n):
        piv = next((i for i in range(rank, m) if R[i][col] % p), None)
        if piv is None:
            continue
        R[rank], R[piv] = R[piv], R[rank]
        inv = pow(R[rank][col], p - 2, p)
        R[rank] = [x * inv % p for x in R[rank]]
        for i in range(m):
            if i != rank and R[i][col]:
                f = R[i][col]
                R[i] = [(a - f * b) % p for a, b in zip(R[i], R[rank])]
        rank += 1
        if rank == m:
            break
    return rank


def nullspacep(rows):
    m = len(rows)
    n = len(rows[0]) if m else 0
    R = [list(r) for r in rows]
    pivots = []
    rank = 0
    for col in range(n):
        piv = next((i for i in range(rank, m) if R[i][col] % p), None)
        if piv is None:
            continue
        R[rank], R[piv] = R[piv], R[rank]
        inv = pow(R[rank][col], p - 2, p)
        R[rank] = [x * inv % p for x in R[rank]]
        for i in range(m):
            if i != rank and R[i][col]:
                f = R[i][col]
                R[i] = [(a - f * b) % p for a, b in zip(R[i], R[rank])]
        pivots.append(col)
        rank += 1
    free = [c for c in range(n) if c not in pivots]
    out = []
    for fc in free:
        v = [0] * n
        v[fc] = 1
        for r_i, pc in enumerate(pivots):
            v[pc] = (-R[r_i][fc]) % p
        out.append(v)
    return out


def brp(u, v):
    out = [0] * DIM
    for pi, up in enumerate(u):
        if not up:
            continue
        for q, r, c in triples.get(pi, []):
            vq = v[q]
            if vq:
                out[r] = (out[r] + up * vq * c) % p
    return out


def stack_rank(*groups):
    cols = []
    for gg in groups:
        cols.extend(gg)
    return rankp([list(r) for r in zip(*cols)])


def inter_dim(U, V):
    return len(U) + len(V) - stack_rank(U, V)


def matp(A, B, t0):
    return [[(A[i][j] + t0 * B[i][j]) % p for j in range(DIM)]
            for i in range(DIM)]


def detp(rows):
    R = [list(r) for r in rows]
    n = len(R)
    det = 1
    for col in range(n):
        piv = next((i for i in range(col, n) if R[i][col] % p), None)
        if piv is None:
            return 0
        if piv != col:
            R[col], R[piv] = R[piv], R[col]
            det = (-det) % p
        det = det * R[col][col] % p
        inv = pow(R[col][col], p - 2, p)
        for i in range(col + 1, n):
            if R[i][col]:
                f = R[i][col] * inv % p
                R[i] = [(a - f * b) % p for a, b in zip(R[i], R[col])]
    return det % p


def derived_center(cols):
    k = len(cols)
    bracks = []
    for i in range(k):
        for j in range(i + 1, k):
            bracks.append(brp(cols[i], cols[j]))
    dd = rankp(bracks) if bracks else 0
    rows = []
    for j in range(k):
        cij = [brp(cols[a], cols[j]) for a in range(k)]
        for i in range(DIM):
            row = [cij[a][i] for a in range(k)]
            if any(row):
                rows.append(row)
    cd = len(nullspacep(rows)) if rows else k
    return dd, cd


AD8, AD14, AD16, AD22 = (admatp(CH[n]) for n in (8, 14, 16, 22))

# core mod p = ker(ad8) (cell 1: z(g8) = core exactly, dim 30)
core = nullspacep(AD8)
assert len(core) == 30
log(f"core mod p: dim {len(core)}")

# ---- derive the noncompact degeneration polynomial from the build ---------
# complement coordinates for e6/core
rows = [list(r) for r in zip(*core)]        # 30 x 78? no: zip gives 78 rows
# core as columns: build matrix rows = coordinates
Mcore = [list(r) for r in zip(*core)]       # 78 x 30
# pivot coordinates of the column space
R = [row[:] for row in [list(x) for x in zip(*Mcore)]]  # 30 x 78 (transpose)
piv_coords = []
rank = 0
for col in range(DIM):
    piv = next((i for i in range(rank, len(R)) if R[i][col] % p), None)
    if piv is None:
        continue
    R[rank], R[piv] = R[piv], R[rank]
    inv = pow(R[rank][col], p - 2, p)
    R[rank] = [x * inv % p for x in R[rank]]
    for i in range(len(R)):
        if i != rank and R[i][col]:
            f = R[i][col]
            R[i] = [(a - f * b) % p for a, b in zip(R[i], R[rank])]
    piv_coords.append(col)
    rank += 1
comp = [i for i in range(DIM) if i not in piv_coords]
assert len(comp) == 48
# T = [core | e_comp], invertible; quotient block = rows/cols on comp after
# eliminating core columns. Practical route: N(t) = det of the 48x48 matrix
# Q(t)[a][b] = (P * (AD8 + t AD16) * E)[a][b], where E = injection of comp
# coords and P = projection onto comp coords ALONG span(core).
# Build the projection P once: solve [core | e_comp] * y = x  =>  P x = y_comp.
Tm = [[0] * DIM for _ in range(DIM)]
for j in range(30):
    for i in range(DIM):
        Tm[i][j] = core[j][i]
for j, cix in enumerate(comp):
    Tm[cix][30 + j] = 1
# invert Tm mod p
TA = [row[:] + [1 if i == k else 0 for k in range(DIM)]
      for i, row in enumerate(Tm)]
n2 = DIM
for col in range(n2):
    piv = next((i for i in range(col, n2) if TA[i][col] % p), None)
    assert piv is not None, "T not invertible"
    TA[col], TA[piv] = TA[piv], TA[col]
    inv = pow(TA[col][col], p - 2, p)
    TA[col] = [x * inv % p for x in TA[col]]
    for i in range(n2):
        if i != col and TA[i][col]:
            f = TA[i][col]
            TA[i] = [(a - f * b) % p for a, b in zip(TA[i], TA[col])]
Tinv = [row[n2:] for row in TA]
Prow = Tinv[30:]                            # 48 x 78: projection onto comp coords


def quotient_det(t0):
    A = matp(AD8, AD16, t0)
    # Q = Prow * A * E  (E = columns comp of identity)
    Q = [[0] * 48 for _ in range(48)]
    AE = [[A[i][cj] for cj in comp] for i in range(DIM)]   # 78 x 48
    for a in range(48):
        pr = Prow[a]
        for b in range(48):
            Q[a][b] = sum(pr[i] * AE[i][b] for i in range(DIM) if AE[i][b]) % p
    return detp(Q)


log("interpolating N(t) = det(ad(g8 + t g16) | e6/core) mod p, deg <= 48 ...")
nodes = list(range(49))
vals = [quotient_det(t0) for t0 in nodes]
# Lagrange interpolation mod p -> coefficient list
x = sp.symbols('x')


def lagrange_modp(xs, ys):
    npts = len(xs)
    coeffs = [0] * npts
    for i in range(npts):
        num = [1]                          # poly coeffs low..high
        den = 1
        for j in range(npts):
            if j == i:
                continue
            shifted = [0] + num
            scaled = [(-xs[j]) % p * a % p for a in num] + [0]
            num = [(shifted[k] + scaled[k]) % p for k in range(len(shifted))]
            den = den * (xs[i] - xs[j]) % p
        dinv = pow(den % p, p - 2, p)
        for k in range(len(num)):
            coeffs[k] = (coeffs[k] + ys[i] * dinv % p * num[k]) % p
    return coeffs


Nco = lagrange_modp(nodes, vals)
# checks at 6 extra nodes
ok = all(sum(cf * pow(t0, k, p) for k, cf in enumerate(Nco)) % p
         == quotient_det(t0) for t0 in range(-6, 0))
deg = max(k for k, cf in enumerate(Nco) if cf)
log(f"  interpolated degree {deg} (48); extra-node checks: {ok}")
RES["noncompact_quotient_det"] = dict(degree=deg, extra_checks=bool(ok))

roots_N = [t0 for t0 in range(p)
           if sum(cf * pow(t0, k, p) for k, cf in enumerate(Nco)) % p == 0]
log(f"  roots of N(t) in F_p: {roots_N}")
# multiplicity check: N(t) == c * prod (t - ri)^16 ?
c_lead = Nco[deg]
import random as _r
_r.seed(3)
mult_ok = True
for _ in range(8):
    t0 = _r.randrange(p)
    lhs = sum(cf * pow(t0, k, p) for k, cf in enumerate(Nco)) % p
    rhs = c_lead
    for ri in roots_N:
        rhs = rhs * pow((t0 - ri) % p, 16, p) % p
    if lhs != rhs:
        mult_ok = False
log(f"  N(t) == c * prod(t - r_i)^16 at 8 random points: {mult_ok}")
RES["noncompact_quotient_det"]["roots"] = roots_N
RES["noncompact_quotient_det"]["is_c_times_cubic_pow16"] = bool(mult_ok)

# compare against mu_solo and banked CUBIC roots mod p
rho = sp.symbols('rho')
mu_solo = [2197, -4769856, -2075673600, 500716339200]      # low..high
cubic_banked = [1, -28224, -159667200, 500716339200]
mu_roots = sorted(t0 for t0 in range(p)
                  if sum(cf * pow(t0, k, p) for k, cf in enumerate(mu_solo)) % p == 0)
cb_roots = sorted(t0 for t0 in range(p)
                  if sum(cf * pow(t0, k, p) for k, cf in enumerate(cubic_banked)) % p == 0)
log(f"  mu_solo roots mod p: {mu_roots}; banked CUBIC roots: {cb_roots}")
log(f"  N-roots == mu_solo roots: {sorted(roots_N) == mu_roots}")
log(f"  mu_solo roots == 13 * CUBIC roots: "
    f"{sorted(13 * t0 % p for t0 in cb_roots) == mu_roots}")
RES["normalization"] = dict(
    N_roots_equal_mu_solo_roots=sorted(roots_N) == mu_roots,
    mu_solo_roots_equal_13x_banked_roots=(
        sorted(13 * t0 % p for t0 in cb_roots) == mu_roots))
save()

# ---- the true wall suite --------------------------------------------------
kappa_c = [-6859, -56402640, 3033676800, 2771822592000]
s_roots = sorted(t0 for t0 in range(p)
                 if sum(cf * pow(t0, k, p) for k, cf in enumerate(kappa_c)) % p == 0)
log(f"kappa roots mod p: {s_roots}")
Z, zdata = [], []
for tr in sorted(roots_N):
    ker = nullspacep(matp(AD8, AD16, tr))
    dd, cd = derived_center(ker)
    Z.append(ker)
    zdata.append(dict(t=tr, dim=len(ker), derived=dd, center=cd))
    log(f"  noncompact wall t={tr}: dim z = {len(ker)} (46), derived = {dd}"
        f" (45), center = {cd} (1)")
RES["noncompact_walls"] = zdata
W = []
for sr in s_roots:
    ker = nullspacep(matp(AD14, AD22, sr))
    W.append(ker)
    assert len(ker) == 30

table = [[inter_dim(Z[i], W[j]) for j in range(3)] for i in range(3)]
log(f"pairing table = {table}")
RES["pairing_table"] = table
matching = {}
for i in range(3):
    hits = [j for j in range(3) if table[i][j] == 30]
    if len(hits) == 1:
        matching[i] = hits[0]
perm_ok = len(matching) == 3 and sorted(matching.values()) == [0, 1, 2]
log(f"matching (nc wall i -> c wall j): {matching}; perfect: {perm_ok}")
RES["pairing_is_perfect_matching"] = perm_ok
# nesting: matched compact wall contained in noncompact wall centralizer
nest = all(stack_rank(Z[i], W[j]) == 46 for i, j in matching.items())
log(f"nesting z(h*_j) subset z(x_i) on matched pairs: {nest}")
RES["nesting_on_matched_pairs"] = nest

# ---- SST bijection check mod p -------------------------------------------
# s*(rho) = -4997/1257360 - (198911/68107) rho + (560387520/885391) rho^2
def rat(a, b):
    return a % p * pow(b % p, p - 2, p) % p


sst_ok = True
sst_map = {}
for i, tr in enumerate(sorted(roots_N)):
    sv = (rat(-4997, 1257360)
          + rat(-198911, 68107) * tr
          + rat(560387520, 885391) * tr * tr) % p
    sst_map[tr] = sv
    j = matching.get(i)
    if j is None or sv != s_roots[j]:
        sst_ok = False
log(f"SST bijection s*(rho_i) equals the MATCHED kappa root, all three: {sst_ok}")
RES["sst_matches_pairing"] = sst_ok

# ---- invisible 12: kernel signature at the true walls ---------------------
span_cols = W[0] + W[1] + W[2]
# Killing Gram mod p (exact integers, as in cell 1)
K = [[0] * DIM for _ in range(DIM)]
for i in range(N):
    for j in range(N):
        K[i][j] = sum((sum(r[k] * C[i][k] for k in range(N)))
                      * (sum(r[k] * C[j][k] for k in range(N)))
                      for r in ROOTS) % p
for ri, r in enumerate(ROOTS):
    mr = tuple(-x for x in r)
    mi = ROOTS.index(mr)
    tr_ = Fr(0)
    for k in range(DIM):
        w = BB[N + mi][k]
        acc = Fr(0)
        for pdx, wp in enumerate(w):
            if wp:
                acc += wp * BB[N + ri][pdx][k]
        tr_ += acc
    K[N + ri][N + mi] = int(tr_) % p
rowsK = []
for cvec in span_cols:
    rowsK.append([sum(cvec[i] * K[i][j] for i in range(DIM) if cvec[i]) % p
                  for j in range(DIM)])
M12 = nullspacep(rowsK)
log(f"M12 dim = {len(M12)} (12)")
kerdims = []
for tr in sorted(roots_N):
    A = matp(AD8, AD16, tr)
    img = [[sum(A[i][k] * v[k] for k in range(DIM) if v[k]) % p
            for i in range(DIM)] for v in M12]
    kd = len(M12) - rankp(img)
    kerdims.append(dict(t=tr, ker_on_M12=kd))
    log(f"  ker((ad8 + t ad16)|M12) at TRUE wall t={tr}: {kd} (4)")
RES["invisible12_kernel_at_true_walls"] = kerdims
save()
log("DONE.")
