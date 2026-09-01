#!/usr/bin/env python3
"""
R22 -- B1148 memo-48 chain (6615 -> 4 -> 1), blind recomputation, own construction.

Model (pinned only from B1148 FINDINGS prose + the numbers it banks):
  * 27 of e6 in the trinification frame: A,B,C in 3x3 with 27 = (3,3b,1)+(1,3,3b)+(3b,1,3);
    e6 := stabilizer in gl(27) of the cubic I = det A + det B + det C - tr(ABC)  (own; expect 78).
  * su(3)^3 := the 24 generators A->X1 A - A X2, B->X2 B - B X3, C->X3 C - C X1.
  * the A1 the holonomy closes through: su(2) = upper-left 2x2 block of X1 (27 = 6 doublets + 15 singlets).
  * pi_1 acts on Psi = C^2 (x) 27 via the figure-eight holonomy a=[[1,1],[0,1]], b=[[1,0],[-w,1]]
    (w = e^{2 pi i/3}) on C^2 and through the A1 on the 27; also the 2T control (quaternion units).
  * "trilinears" = the FULL ordered tensor Psi (x) Psi (x) 27, dim 54*54*27 = 78732.
Everything exact (Fractions / sympy over QQ or QQ(w)); the big direct nullspace also mod p.
"""
import itertools, sys, time
from fractions import Fraction
import sympy as sp

t0 = time.time()
def log(*a):
    print(*a); sys.stdout.flush()

# ---------------------------------------------------------------- the 27 and the cubic
# basis index: block s in {0:A,1:B,2:C}, entry (i,j)
def idx(s, i, j): return 9*s + 3*i + j
N = 27
x = sp.symbols('x0:27')
A = sp.Matrix(3, 3, lambda i, j: x[idx(0, i, j)])
B = sp.Matrix(3, 3, lambda i, j: x[idx(1, i, j)])
C = sp.Matrix(3, 3, lambda i, j: x[idx(2, i, j)])
I3 = sp.expand(A.det() + B.det() + C.det() - (A*B*C).trace())
PI = sp.Poly(I3, *x)
log("cubic monomials in I:", len(PI.terms()), " coeffs:", sorted(set(PI.coeffs())))

# ---------------------------------------------------------------- e6 = stabilizer of I in gl(27)
# X in gl(27) acts as derivation: (X.I) = sum_{p,q} X[p,q] x_p dI/dx_q  (x_q -> sum_p X[p,q] x_p ... convention)
# Unknowns X[p,q]; equation: sum_{p,q} X[p,q] * x_p * dI/dx_q == 0 as a polynomial.
cub_monos = {}
rows = {}
Xs = {}
for q in range(N):
    dq = sp.Poly(sp.diff(I3, x[q]), *x)
    for p in range(N):
        pol = sp.Poly(x[p], *x) * dq
        for mono, c in pol.terms():
            r = cub_monos.setdefault(mono, len(cub_monos))
            rows.setdefault(r, {})[(p, q)] = rows.get(r, {}).get((p, q), 0) + c
unk = [(p, q) for p in range(N) for q in range(N)]
uid = {u: k for k, u in enumerate(unk)}
M = sp.zeros(len(rows), len(unk))
for r, d in rows.items():
    for u, c in d.items():
        M[r, uid[u]] = c
log("stabilizer system:", M.shape)
from sympy.polys.matrices import DomainMatrix
DM = DomainMatrix.from_Matrix(M).convert_to(sp.QQ)
ns = DM.nullspace().to_Matrix()
gens_e6 = []
for k in range(ns.rows):
    v = ns.row(k)
    X = sp.zeros(N, N)
    for u, kk in uid.items():
        X[u[0], u[1]] = v[kk]
    gens_e6.append(X)
log("dim stabilizer of I in gl(27) =", len(gens_e6), " (expect 78 = dim e6)   t=%.1fs" % (time.time()-t0))

# derivation action of matrix X on the polynomial ring: x_q -> sum_p X[p,q] x_p, check it kills I
def act_poly(X, f):
    return sp.expand(sum(X[p, q]*x[p]*sp.diff(f, x[q]) for p in range(N) for q in range(N) if X[p, q] != 0))
assert all(act_poly(X, I3) == 0 for X in gens_e6[:5])

# ---------------------------------------------------------------- su(3)^3 generators (own, explicit)
def gl3_basis():
    out = []
    for i in range(3):
        for j in range(3):
            if i != j:
                E = sp.zeros(3, 3); E[i, j] = 1; out.append(E)
    for i in range(2):
        H = sp.zeros(3, 3); H[i, i] = 1; H[i+1, i+1] = -1; out.append(H)
    return out  # 8 traceless
def lin_from_blocks(fA, fB, fC):
    """build 27x27 matrix X from linear maps on A,B,C blocks: new coordinate vector x' = X x"""
    X = sp.zeros(N, N)
    for col in range(N):
        e = [0]*N; e[col] = 1
        Am = sp.Matrix(3, 3, lambda i, j: e[idx(0, i, j)])
        Bm = sp.Matrix(3, 3, lambda i, j: e[idx(1, i, j)])
        Cm = sp.Matrix(3, 3, lambda i, j: e[idx(2, i, j)])
        A2, B2, C2 = fA(Am, Bm, Cm), fB(Am, Bm, Cm), fC(Am, Bm, Cm)
        for i in range(3):
            for j in range(3):
                X[idx(0, i, j), col] = A2[i, j]; X[idx(1, i, j), col] = B2[i, j]; X[idx(2, i, j), col] = C2[i, j]
    return X
Z3 = sp.zeros(3, 3)
gens_su3 = []
for T in gl3_basis():  # X1
    gens_su3.append(lin_from_blocks(lambda a, b, c: T*a, lambda a, b, c: Z3, lambda a, b, c: -c*T))
for T in gl3_basis():  # X2
    gens_su3.append(lin_from_blocks(lambda a, b, c: -a*T, lambda a, b, c: T*b, lambda a, b, c: Z3))
for T in gl3_basis():  # X3
    gens_su3.append(lin_from_blocks(lambda a, b, c: Z3, lambda a, b, c: -b*T, lambda a, b, c: T*c))
# X acts on coordinates as x -> X x ; as derivation on polynomials: x_q -> sum_p X[p,q] x_p. check kills I
assert all(act_poly(X, I3) == 0 for X in gens_su3), "su3^3 does not stabilize I?!"
# check su3^3 inside span(e6 gens)
E6span = sp.Matrix([[X[p, q] for p in range(N) for q in range(N)] for X in gens_e6])
S3span = sp.Matrix([[X[p, q] for p in range(N) for q in range(N)] for X in gens_su3])
assert E6span.rank() == 78 and S3span.rank() == 24 and E6span.col_join(S3span).rank() == 78
log("su(3)^3 (24) sits inside the 78-dim stabilizer: OK")

# Cartan of su3^3 (6 diagonal generators) = weights of the 27 basis vectors
cartan = [g for g in gens_su3 if g.is_diagonal()]
assert len(cartan) == 6
wts = [tuple(int(h[k, k]) for h in cartan) for k in range(N)]
assert len(set(wts)) == 27, "27 weights not distinct"

# ---------------------------------------------------------------- 27 (x) 27 (x) 27: weight-zero ordered triples
triples = [(p, q, r) for p in range(N) for q in range(N) for r in range(N)
           if all(wts[p][k]+wts[q][k]+wts[r][k] == 0 for k in range(6))]
log("weight-zero ORDERED triples in 27^3:", len(triples), " (banked 270); with repeats:",
    sum(1 for t in triples if len(set(t)) < 3))
tid = {t: k for k, t in enumerate(triples)}

def inv_dim_27cube(gens, sym=False):
    """direct nullspace of the invariance system on the weight-zero subspace of 27^{(x)3}
       (tensor T_{pqr}; (X.T)_{pqr} = sum_s X[s,p]... use contragredient-free form: T invariant iff
       sum_s (X[s,p] T_{sqr} + X[s,q] T_{psr} + X[s,r] T_{pqs}) = 0  -- i.e. T in (27^{*})^{(x)3} dual;
       dimension of invariants is the same either way since 27^{(x)3} and its dual have equal Inv dims)"""
    if sym:
        # unknowns = unordered triples (symmetric tensor)
        keys = sorted(set(tuple(sorted(t)) for t in triples))
        kid = {k: i for i, k in enumerate(keys)}
        col = lambda t: kid[tuple(sorted(t))]
        ncol = len(keys)
    else:
        col = lambda t: tid[t]; ncol = len(triples)
    eqs = {}
    for X in gens:
        nz = [(s, p) for s in range(N) for p in range(N) if X[s, p] != 0]
        byp = {}
        for s, p in nz: byp.setdefault(p, []).append(s)
        for (p, q, r) in triples:
            # equation indexed by output slot (p,q,r) in weight-(wt X) space
            row = {}
            for s in byp.get(p, []):
                t = (s, q, r)
                if t in tid: row[col(t)] = row.get(col(t), 0) + X[s, p]
            for s in byp.get(q, []):
                t = (p, s, r)
                if t in tid: row[col(t)] = row.get(col(t), 0) + X[s, q]
            for s in byp.get(r, []):
                t = (p, q, s)
                if t in tid: row[col(t)] = row.get(col(t), 0) + X[s, r]
            row = {k: v for k, v in row.items() if v != 0}
            if row: eqs[len(eqs)] = row
        # note: outputs land in weight != 0 for non-Cartan X; we enumerate rows by input triples and
        # the map's image; equivalently rows indexed by (X, target triple).  Redo properly below.
    return eqs, ncol, col

def inv_dim_direct(gens, sym=False):
    """rows = (generator, target basis tensor); columns = weight-zero unknowns. exact rank over QQ."""
    if sym:
        keys = sorted(set(tuple(sorted(t)) for t in triples))
        kid = {k: i for i, k in enumerate(keys)}
        col = lambda t: kid[tuple(sorted(t))]; ncol = len(keys)
    else:
        col = lambda t: tid[t]; ncol = len(triples)
    rowsd = {}
    for gi, X in enumerate(gens):
        for (p, q, r) in triples:  # source unknown
            c = col((p, q, r))
            for s in range(N):
                if X[s, p] != 0:
                    key = (gi, s, q, r); rowsd.setdefault(key, {}); rowsd[key][c] = rowsd[key].get(c, 0) + X[s, p]
                if X[s, q] != 0:
                    key = (gi, p, s, r); rowsd.setdefault(key, {}); rowsd[key][c] = rowsd[key].get(c, 0) + X[s, q]
                if X[s, r] != 0:
                    key = (gi, p, q, s); rowsd.setdefault(key, {}); rowsd[key][c] = rowsd[key].get(c, 0) + X[s, r]
    Mx = sp.zeros(len(rowsd), ncol)
    for ri, (k, d) in enumerate(rowsd.items()):
        for c, v in d.items(): Mx[ri, c] = v
    DMx = DomainMatrix.from_Matrix(Mx).convert_to(sp.QQ)
    nsx = DMx.nullspace().to_Matrix()
    return nsx.rows, nsx, ncol

d_su3_full, ns_su3, _ = inv_dim_direct(gens_su3)
d_e6_full, ns_e6, _ = inv_dim_direct(gens_e6)
d_su3_sym, _, nsym = inv_dim_direct(gens_su3, sym=True)
d_e6_sym, ns_e6s, _ = inv_dim_direct(gens_e6, sym=True)
log("Inv_{su3^3}(27 x 27 x 27) full ordered tensor : dim =", d_su3_full)
log("Inv_{e6}   (27 x 27 x 27) full ordered tensor : dim =", d_e6_full)
log("Inv_{su3^3}(Sym^3 27), %d unordered triples   : dim = %d" % (nsym, d_su3_sym))
log("Inv_{e6}   (Sym^3 27)                          : dim =", d_e6_sym)
# is the e6 full-tensor survivor automatically symmetric?
v = ns_e6.row(0)
symm = all(v[tid[t]] == v[tid[tuple(t[i] for i in perm)]] for t in triples for perm in itertools.permutations(range(3)))
log("e6 full-tensor survivor automatically symmetric:", symm, "; support", sum(1 for k in range(len(triples)) if v[k] != 0),
    "/", len(triples), "; coefficient set", sorted(set(v)))
# does it equal I (as a tensor, up to scale)?
Iten = {}
for mono, c in PI.terms():
    ids = [k for k in range(N) for _ in range(mono[k])]
    for perm in set(itertools.permutations(ids)): Iten[perm] = c
ratio = set(sp.nsimplify(v[tid[t]] / Iten[t]) for t in triples if t in Iten)
log("survivor / I ratio set (should be a single scalar):", ratio, " ; survivor support == support(I):",
    set(t for t in triples if v[tid[t]] != 0) == set(Iten))
log("t=%.1fs" % (time.time()-t0))

# ---------------------------------------------------------------- the A1: su(2) in the corner of X1
E2 = sp.zeros(3, 3); E2[0, 1] = 1
F2 = sp.zeros(3, 3); F2[1, 0] = 1
H2 = sp.zeros(3, 3); H2[0, 0] = 1; H2[1, 1] = -1
def a1(T): return lin_from_blocks(lambda a, b, c: T*a, lambda a, b, c: Z3, lambda a, b, c: -c*T)
E27, F27, H27 = a1(E2), a1(F2), a1(H2)
assert (E27*F27 - F27*E27 - H27).is_zero_matrix
# decomposition of 27 under this A1 by weights of H27
hw = [int(H27[k, k]) for k in range(N)]
from collections import Counter
log("27 under the A1 (H-weights):", dict(Counter(hw)), "=> doublets:", hw.count(1), " singlets:", hw.count(0) - hw.count(1) + hw.count(1) - hw.count(1))
n2 = hw.count(1); n1 = N - 2*n2
log("   i.e. 27 = %d x (2) + %d x (1)   [B1145/B1148: 6 doublets + 15 singlets]" % (n2, n1))

# ---------------------------------------------------------------- Psi = C^2 (x) 27, trilinears = Psi (x) Psi (x) 27
# generic sl2 element acts on C^2 by (E,F,H) 2x2 and on 27 by (E27,F27,H27); on Psi by Kronecker sum.
e2 = sp.Matrix([[0, 1], [0, 0]]); f2 = sp.Matrix([[0, 0], [1, 0]]); h2 = sp.Matrix([[1, 0], [0, -1]])
def kron_sum(P, Q):  # P (x) 1 + 1 (x) Q
    return sp.kronecker_product(P, sp.eye(Q.rows)) + sp.kronecker_product(sp.eye(P.rows), Q)
EP, FP, HP = kron_sum(e2, E27), kron_sum(f2, F27), kron_sum(h2, H27)
DP = 54
hP = [int(HP[k, k]) for k in range(DP)]
log("Psi (54) H-weights:", dict(Counter(hP)))

# (a) CHARACTER count of sl2-invariants in Psi x Psi x 27 (exact, complete reducibility)
def sl2_mults(hlist):
    c = Counter(hlist); m = {}
    for w in sorted(c, reverse=True):
        if w < 0: break
        m[w] = c[w] - c.get(w+2, 0)
    return m  # spin label n (dim n+1) -> multiplicity
mPsi, m27 = sl2_mults(hP), sl2_mults(hw)
log("Psi = ", {("V%d" % n): k for n, k in mPsi.items() if k}, " ; 27 =", {("V%d" % n): k for n, k in m27.items() if k})
def inv_V3(i, j, k): return 1 if (abs(i-j) <= k <= i+j and (i+j+k) % 2 == 0) else 0
char_count = sum(mPsi[i]*mPsi[j]*m27[k]*inv_V3(i, j, k) for i in mPsi for j in mPsi for k in m27)
log("CHARACTER count dim Inv_{sl2}(Psi x Psi x 27) =", char_count, "  (banked 6615)")

# (b) DIRECT full-tensor nullspace on the 78732-dim space, restricted to H-weight 0, exact mod p (two primes)
#     unknowns: (u,v,w) with hP[u]+hP[v]+hw[w] = 0 ; equations: E.T = 0 and F.T = 0
zero = [(u, v, w) for u in range(DP) for v in range(DP) for w in range(N) if hP[u]+hP[v]+hw[w] == 0]
zid = {t: k for k, t in enumerate(zero)}
log("H-weight-zero unknowns in Psi x Psi x 27:", len(zero), " of", DP*DP*N)
def sparse_cols(Mx):
    d = {}
    for (i, j), v in Mx.todok().items() if hasattr(Mx, 'todok') else [((i, j), Mx[i, j]) for i in range(Mx.rows) for j in range(Mx.cols) if Mx[i, j] != 0]:
        d.setdefault(j, []).append((i, int(v)))
    return d
EPc, FPc, E27c, F27c = sparse_cols(EP), sparse_cols(FP), sparse_cols(E27), sparse_cols(F27)
def build_rows(Xc1, Xc3):
    rowsd = {}
    for (u, v, w) in zero:
        c = zid[(u, v, w)]
        for s, val in Xc1.get(u, []): rowsd.setdefault((s, v, w), {}).__setitem__(c, val)
        for s, val in Xc1.get(v, []):
            key = (u, s, w); rowsd.setdefault(key, {}); rowsd[key][c] = rowsd[key].get(c, 0) + val
        for s, val in Xc3.get(w, []):
            key = (u, v, s); rowsd.setdefault(key, {}); rowsd[key][c] = rowsd[key].get(c, 0) + val
    return list(rowsd.values())
rowsE = build_rows(EPc, E27c); rowsF = build_rows(FPc, F27c)
allrows = rowsE + rowsF
log("equations:", len(allrows), " unknowns:", len(zero))

def rank_modp(rowlist, ncols, p):
    """sparse Gaussian elimination mod p (dict rows), returns rank"""
    pivots = {}  # col -> reduced row (dict) with leading entry 1 at col
    rank = 0
    for r in rowlist:
        row = {k: v % p for k, v in r.items() if v % p}
        while row:
            c = min(row)
            if c in pivots:
                f = row[c]; prow = pivots[c]
                for k, v in prow.items():
                    nv = (row.get(k, 0) - f*v) % p
                    if nv: row[k] = nv
                    else: row.pop(k, None)
            else:
                inv = pow(row[c], p-2, p)
                row = {k: (v*inv) % p for k, v in row.items()}
                pivots[c] = row; rank += 1
                break
    return rank
for p in (1000000007, 998244353):
    rk = rank_modp(allrows, len(zero), p)
    log("DIRECT full-tensor nullspace mod %d : rank %d -> dim Inv = %d   (banked 6615)   t=%.1fs" % (p, rk, len(zero)-rk, time.time()-t0))

# (c) the sl2 invariants are also the invariants of the ACTUAL pi_1 image (figure-eight holonomy, Zariski dense)
#     and of the finite 2T image: checked block-exactly over QQ(w): every block V_i x V_j x V_k (i,j<=2,k<=1)
w = sp.exp(2*sp.pi*sp.I/3)
a_h = sp.Matrix([[1, 1], [0, 1]]); b_h = sp.Matrix([[1, 0], [-w, 1]])
# 2T generators inside SU(2): i and (1+i+j+k)/2 as 2x2 unitaries
qi = sp.Matrix([[sp.I, 0], [0, -sp.I]]); qj = sp.Matrix([[0, 1], [-1, 0]]); qk = qi*qj
t1 = qi; t2 = (sp.eye(2) + qi + qj + qk)/2
assert sp.simplify(t2**6 - sp.eye(2)).is_zero_matrix and sp.simplify(t2**3 + sp.eye(2)).is_zero_matrix
def symrep(g, n):  # Sym^n of a 2x2 matrix, acting on monomials X^{n-k} Y^k
    X, Y = sp.symbols('X Y')
    Xp = g[0, 0]*X + g[1, 0]*Y; Yp = g[0, 1]*X + g[1, 1]*Y
    R = sp.zeros(n+1, n+1)
    for k in range(n+1):
        pol = sp.Poly(sp.expand(Xp**(n-k) * Yp**k), X, Y)
        for l in range(n+1):
            R[l, k] = pol.coeff_monomial(X**(n-l)*Y**l)
    return R
def fixed_dim(mats):
    Mst = sp.Matrix.vstack(*[m - sp.eye(m.rows) for m in mats])
    return Mst.cols - Mst.rank(simplify=True)
tot_pi1 = tot_2T = tot_sl2 = 0
for i in mPsi:
    for j in mPsi:
        for k in m27:
            if mPsi[i]*mPsi[j]*m27[k] == 0: continue
            mult = mPsi[i]*mPsi[j]*m27[k]
            blocks = lambda g: sp.kronecker_product(symrep(g, i), symrep(g, j), symrep(g, k))
            dpi = fixed_dim([blocks(a_h), blocks(b_h)])
            d2T = fixed_dim([blocks(t1), blocks(t2)])
            dsl = inv_V3(i, j, k)
            tot_pi1 += mult*dpi; tot_2T += mult*d2T; tot_sl2 += mult*dsl
            if not (dpi == d2T == dsl):
                log("   block V%d x V%d x V%d: pi1 %d, 2T %d, sl2 %d  <-- DIFFER" % (i, j, k, dpi, d2T, dsl))
log("block-exact totals: pi_1(figure-eight holonomy) =", tot_pi1, "; 2T =", tot_2T, "; sl2 =", tot_sl2)

# planted-positive control for the finite-group step: 2T has an invariant in V6 (degree-6), sl2 has none
d6_2T = fixed_dim([symrep(t1, 6), symrep(t2, 6)]); d6_sl2 = 1 if 6 == 0 else 0
log("control: Inv in V6 -- 2T %d vs sl2 %d (the finite image WOULD differ at spin 3; our blocks stop at spin 5/2)" % (d6_2T, d6_sl2))

# ---------------------------------------------------------------- chain with the gauge algebra added (cumulative)
# joint invariants: X in su3^3 (on the three 27 factors) and sl2 (on both C^2 and the 27s).
# direct: unknowns = H-weight-zero AND su3^3-Cartan-weight-zero tensors; equations: all 24 su3^3 gens + sl2 E,F on Psi.
def joint_inv(gens27, label):
    # weights of Psi basis under the 6 Cartans of su3^3: C^2 is inert
    wPsi = [wts[k % N] for k in range(DP)]
    Z = [(u, v, w_) for (u, v, w_) in zero
         if all(wPsi[u][c] + wPsi[v][c] + wts[w_][c] == 0 for c in range(6))]
    Zid = {t: k for k, t in enumerate(Z)}
    rowsd = {}
    def add(key, c, val):
        rowsd.setdefault(key, {}); rowsd[key][c] = rowsd[key].get(c, 0) + val
    # sl2 E,F on Psi x Psi x 27
    for (Xc1, Xc3, tag) in ((EPc, E27c, 'E'), (FPc, F27c, 'F')):
        for (u, v, w_) in Z:
            c = Zid[(u, v, w_)]
            for s, val in Xc1.get(u, []): add((tag, s, v, w_), c, val)
            for s, val in Xc1.get(v, []): add((tag, u, s, w_), c, val)
            for s, val in Xc3.get(w_, []): add((tag, u, v, s), c, val)
    # gauge gens on 27 factors only: on Psi = C^2 x 27 as 1 (x) X
    for gi, X in enumerate(gens27):
        Xc = sparse_cols(sp.kronecker_product(sp.eye(2), X)); X27c = sparse_cols(X)
        for (u, v, w_) in Z:
            c = Zid[(u, v, w_)]
            for s, val in Xc.get(u, []): add((gi, s, v, w_), c, val)
            for s, val in Xc.get(v, []): add((gi, u, s, w_), c, val)
            for s, val in X27c.get(w_, []): add((gi, u, v, s), c, val)
    rl = list(rowsd.values())
    Mx = sp.zeros(len(rl), len(Z))
    for ri, d in enumerate(rl):
        for c, val in d.items(): Mx[ri, c] = val
    nsx = DomainMatrix.from_Matrix(Mx).convert_to(sp.QQ).nullspace().to_Matrix()
    log("%s: joint (pi_1/sl2 + gauge) DIRECT nullspace on Psi x Psi x 27: unknowns %d, eqs %d -> dim %d" % (label, len(Z), len(rl), nsx.rows))
    return nsx, Z, Zid
ns_g, Zg, Zgid = joint_inv(gens_su3, "su(3)^3")
ns_f, Zf, Zfid = joint_inv(gens_e6, "e6")
# survivor structure: eps (x) C ?  check antisymmetry under Psi-exchange (u<->v) of the e6 survivor
vv = ns_f.row(0)
anti = all(vv[Zfid[(u, v, w_)]] == -vv[Zfid[(v, u, w_)]] for (u, v, w_) in Zf)
log("e6 survivor antisymmetric under fermion (Psi<->Psi) exchange:", anti)
# and factorized: T[(s,p),(t,q),r] = eps[s,t] * I[p,q,r]
eps = {(0, 1): 1, (1, 0): -1}
fac = True; scale = None
for (u, v, w_) in Zf:
    s, p = divmod(u, N); t, q = divmod(v, N)
    val = vv[Zfid[(u, v, w_)]]
    ref = eps.get((s, t), 0) * Iten.get((p, q, w_), 0)
    if ref == 0:
        fac &= (val == 0)
    else:
        if scale is None: scale = val/ref
        fac &= (val == scale*ref)
log("e6 survivor == eps (x) I (up to scale):", fac)
# gauge-only survivors: what are the 9 (or 4)? characterize by symmetric-in-27 content
# count how many of the su3^3 joint survivors are symmetric in the three 27 slots (after stripping eps)
Msym = []
for r in range(ns_g.rows):
    row = ns_g.row(r)
    Msym.append(row)
# project onto the "27-symmetric" subspace: T[(s,p),(t,q),r] symmetric under p<->q (with s<->t) & (q,r) etc. compute dim of symmetric part
def sym_part_rank(nsmat, Z, Zid):
    # restrict to 27-index-symmetric candidates: require T[(s,p),(t,q),r] = T[(s,q),(t,p),r] ... use full S3 on (p,q,r) keeping spinor slots
    rowsc = []
    for r in range(nsmat.rows):
        row = nsmat.row(r)
        rowsc.append(row)
    # dimension of the intersection with the symmetric subspace = dim ns - rank of (antisym constraints on ns)
    cons = []
    for (u, v, w_) in Z:
        s, p = divmod(u, N); t, q = divmod(v, N)
        for (p2, q2, r2) in set(itertools.permutations((p, q, w_))):
            u2, v2 = s*N + p2, t*N + q2
            if (u2, v2, r2) in Zid:
                cons.append([nsmat[r, Zid[(u, v, w_)]] - nsmat[r, Zid[(u2, v2, r2)]] for r in range(nsmat.rows)])
    Mc = sp.Matrix(cons)
    return nsmat.rows - Mc.rank()
log("su(3)^3 joint survivors that are SYMMETRIC in the three 27 indices:", sym_part_rank(ns_g, Zg, Zgid), " (memo-35-style Sym^3 count x eps)")
log("done t=%.1fs" % (time.time()-t0))
