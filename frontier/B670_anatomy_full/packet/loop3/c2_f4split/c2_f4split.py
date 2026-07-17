"""C2 -- h1 against the F4 split (PREREG_L3.md sha f32fbfff, C2 clause).

Project the local system (the 27, action of the solo-manifold group
M = <a, b | REL>) onto the F4 blocks 1 + 26: the singlet = v0's line (the
unique invariant line, gate dim 1); the 26 = its T2-orthogonal complement
w.r.t. an invariant symmetric bilinear form B, built exactly from banked
invariants and verified invariant.

THE CANONICAL FORM: the A1 agent (a1_jordan.py) found the space of
G-invariant symmetric bilinear forms on the 27 has dim 3, but did not bank a
basis (T2_v0_v0 is null in a1_results.json because that script only banks
T2 when dim==1). Per prereg instruction we (a) recompute the 3-dim space by
the same incremental method for cross-reference, and (b) construct the
canonical member directly: B(x,y) := N(x,y,v0), the polarization of the
G-invariant Jordan cubic norm N at the G-fixed vector v0. This is
automatically symmetric (N symmetric trilinear) and automatically
G-invariant (both N and v0 are G-invariant/G-fixed) -- it is the
"trace-form-at-v0" analogue of the standard Jordan trace pairing
T(x,y) = N(x,y,e) built from the identity element e, with v0 (the unique
invariant line) playing e's structural role here. Hence it is the
Jordan-adjoint-identity-compatible choice, not an arbitrary pick. We verify
it lies exactly in the banked 3-dim space and that B(v0,v0) = N(v0,v0,v0)
= -6 != 0 (matching a1's banked value).

THE SPLIT: P_1(x) = B(v0,x)/B(v0,v0) * v0; P_26 = I - P_1. Both are checked
to commute exactly with rho(a), rho(b) (automatic from invariance of B and
fixedness of v0 -- verified anyway).

THE COMPUTATION: per block (1-dim singlet, 26-dim complement): h0 = joint
fixed-space dim; h1 via 2-generator Fox calculus on REL (solo relator),
reproducing the machinery of w0b_blocks.py (same manifold, principal-sl2
1/9/17 split) adapted to the F4 (1,26) split.

CROSS-SPLIT: reproduce the principal-sl2 chain basis (block dims 17,9,1)
verbatim per cell3b_stage1.py / w0b_blocks.py; verify the dim-1 principal
block IS v0's line (proportional) and that the 17+9 principal-block span is
EXACTLY B-orthogonal to v0 (hence exactly ker(P_1), not merely isomorphic to
it); compute h1 for the 17 and 9 blocks independently and compare their sum
against the F4-26's h1; bank the explicit 26x26 change-of-basis matrix
relating the two bases of the same 26-dim complement.

Repo <repo> is read-only; only exec'd
in-memory, nothing is written there.
"""
import os
import json
import time

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

HERE = os.path.dirname(os.path.abspath(__file__))
B575 = "<repo>/frontier/B575_bridge_obstruction/l51_obstruction.py"
A1_JSON = "<seat-workdir>/anatomy/loop1/a1_jordan/a1_results.json"
W0B_JSON = "<seat-workdir>/invariant_line/w0b_blocks/w0b_blocks.json"
LOG_PATH = os.path.join(HERE, "c2_run.log")
JSON_PATH = os.path.join(HERE, "c2_results.json")

T0 = time.time()
_log_f = open(LOG_PATH, "w")
def log(msg):
    line = f"[{time.time()-T0:7.1f}s] {msg}"
    print(line, flush=True)
    _log_f.write(line + "\n")
    _log_f.flush()

gates = {}
d = 27

# ============================================================================
log("STEP 0: exec B575 prefix (stages 0-3; exact e6 + 27 build)...")
src = open(B575).read()
cut = src.index("# ---------------------------------------------------------------- stage 4")
ns = {"__name__": "b575_prefix", "__file__": B575}
t0 = time.time()
exec(compile(src[:cut], B575, "exec"), ns)
log(f"  B575 prefix done ({time.time()-t0:.0f}s)")

K, K0, K1 = ns["K"], ns["K0"], ns["K1"]
A27, B27, A27i, B27i = ns["A27"], ns["B27"], ns["A27i"], ns["B27i"]
meye, mmul, rref, nullspace = ns["meye"], ns["mmul"], ns["rref"], ns["nullspace"]
Solver = ns["Solver"]
e_pr, f_pr, h_pr = ns["e_pr"], ns["f_pr"], ns["h_pr"]
W27, E6_e, E6_f = ns["W27"], ns["E6_e"], ns["E6_f"]
REL = ns["REL"]
log(f"  REL (solo relator) = {REL!r}")


def mt(M):
    return [[M[j][i] for j in range(d)] for i in range(d)]


def apply(M, v):
    return [sum((M[i][k] * v[k] for k in range(d) if not v[k].is_zero()), K0)
            for i in range(d)]


def msub2(X, Y):
    return [[X[i][j] - Y[i][j] for j in range(d)] for i in range(d)]


def matequal(X, Y):
    return all((X[i][j] - Y[i][j]).is_zero() for i in range(len(X)) for j in range(len(X[0])))


def dot(f, v):
    return sum((f[t] * v[t] for t in range(d) if not v[t].is_zero()), K0)


def kser(x):
    return [str(x.a), str(x.b)]


# ============================================================================
log("STEP 1: v0 = joint nullspace of (A27-I, B27-I)  [W0a/A1 result]...")
I = meye(d)
AmI = msub2(A27, I)
BmI = msub2(B27, I)
ns_basis = nullspace(AmI + BmI)
gates["v0_dim1"] = (len(ns_basis) == 1)
log(f"  joint nullspace dim = {len(ns_basis)}  [HARD GATE dim=1]: "
    f"{'PASS' if gates['v0_dim1'] else 'FAIL'}")
assert gates["v0_dim1"], f"v0 nullspace dim {len(ns_basis)} != 1"

v0_raw = ns_basis[0]
idx0 = next(i for i, x in enumerate(v0_raw) if not x.is_zero())
scale = v0_raw[idx0].inv()
v0 = [scale * x for x in v0_raw]
assert (v0[idx0] - K1).is_zero()
gates["v0_fixed_exact"] = all(x.is_zero() for x in apply(AmI, v0)) and all(x.is_zero() for x in apply(BmI, v0))
assert gates["v0_fixed_exact"], "v0 not exactly fixed"
v0_support = [i for i in range(d) if not v0[i].is_zero()]
log(f"  v0 verified exactly fixed; support = {v0_support}")

a1 = json.load(open(A1_JSON))
gates["v0_matches_a1"] = (a1["v0_normalized_idx0"] == idx0 and
                           a1["v0_support_indices"] == v0_support)
log(f"  cross-check vs a1_results.json: idx0/support match = {gates['v0_matches_a1']}")
assert gates["v0_matches_a1"], "v0 does not match the banked A1 result"

# ============================================================================
log("STEP 2: the Jordan cubic invariant N (same method as a1_jordan.py STEP 2)...")
support, SUPIDX = [], {}
for p in range(d):
    for q in range(p, d):
        for r in range(q, d):
            if all(W27[p][k] + W27[q][k] + W27[r][k] == 0 for k in range(6)):
                SUPIDX[(p, q, r)] = len(support)
                support.append((p, q, r))
nsup = len(support)
log(f"  zero-weight-sum sorted triples: {nsup}")

eqs = {}
for gi, X in enumerate(list(E6_e) + list(E6_f)):
    xent = [(s, t) for s in range(d) for t in range(d) if not X[s][t].is_zero()]
    for (a_, b_, c_) in support:
        k = SUPIDX[(a_, b_, c_)]
        for (u, v, w) in ((a_, b_, c_), (b_, a_, c_), (c_, a_, b_)):
            for s, t in xent:
                if s == u:
                    key = (gi,) + tuple(sorted((t, v, w)))
                    row = eqs.setdefault(key, {})
                    row[k] = row.get(k, K0) + X[u][t]
rows = [[row.get(k, K0) for k in range(nsup)] for row in eqs.values()
        if any(not cv.is_zero() for cv in row.values())]
sol = nullspace(rows)
gates["N_dim1"] = (len(sol) == 1)
log(f"  cubic invariant space dim = {len(sol)}  [GATE: must equal 1]: "
    f"{'PASS' if gates['N_dim1'] else 'FAIL'}")
assert gates["N_dim1"], f"cubic invariant dim {len(sol)} != 1"
Cvals = sol[0]
CFULL = {}
for (p, q, r), k in SUPIDX.items():
    if not Cvals[k].is_zero():
        for perm in {(p, q, r), (p, r, q), (q, p, r), (q, r, p), (r, p, q), (r, q, p)}:
            CFULL[perm] = Cvals[k]


def C3(u, v):
    """The cross product: covector m -> N(u, v, e_m)."""
    cov = [K0] * d
    for (p, q, r), cval in CFULL.items():
        if not u[p].is_zero() and not v[q].is_zero():
            cov[r] = cov[r] + cval * u[p] * v[q]
    return cov


u1 = [K(i % 5 - 2) for i in range(d)]
v1 = [K((2 * i) % 7 - 3) for i in range(d)]
w1 = [K((3 * i) % 4 - 1) for i in range(d)]
ninv = {}
for nm, M in (("A27", A27), ("B27", B27)):
    lhs = dot(C3(apply(M, u1), apply(M, v1)), apply(M, w1))
    rhs = dot(C3(u1, v1), w1)
    ninv[nm] = (lhs - rhs).is_zero()
gates["N_invariant_all"] = all(ninv.values())
log(f"  N-invariance under A27/B27: {ninv}  [GATE]: "
    f"{'PASS' if gates['N_invariant_all'] else 'FAIL'}")
assert gates["N_invariant_all"], "N is NOT rho-invariant"

s = C3(v0, v0)
Nv0 = dot(s, v0)
gates["Nv0_matches_a1"] = (kser(Nv0) == a1["N_v0_v0_v0_raw"])
log(f"  N(v0,v0,v0) = {Nv0}  (cross-check vs a1_results.json: {gates['Nv0_matches_a1']})")
assert gates["Nv0_matches_a1"], "N(v0,v0,v0) mismatch vs banked A1 result"

# ============================================================================
log("STEP 3: THE CANONICAL FORM  B(x,y) := N(x,y,v0)  "
    "(polarization of N at the fixed vector v0)...")
Bmat = [[K0] * d for _ in range(d)]
for (p, q, r), cval in CFULL.items():
    if not v0[r].is_zero():
        Bmat[p][q] = Bmat[p][q] + cval * v0[r]

gates["B_symmetric"] = all((Bmat[i][j] - Bmat[j][i]).is_zero() for i in range(d) for j in range(d))
log(f"  B symmetric exactly: {gates['B_symmetric']}")
assert gates["B_symmetric"], "B(x,y) := N(x,y,v0) is NOT symmetric"

binv = {}
for nm, M in (("A27", A27), ("B27", B27)):
    lhs = mmul(mmul(mt(M), Bmat), M)
    binv[nm] = matequal(lhs, Bmat)
gates["B_invariant_all"] = all(binv.values())
log(f"  B invariance under A27/B27 (M^T B M == B, exact): {binv}  [GATE]: "
    f"{'PASS' if gates['B_invariant_all'] else 'FAIL'}")
assert gates["B_invariant_all"], "chosen B is NOT G-invariant"

Bv0_full = apply(Bmat, v0)          # B(v0, e_j) for all j
Bv0v0 = dot(Bv0_full, v0)
gates["Bv0v0_matches_Nv0"] = (Bv0v0 - Nv0).is_zero()
gates["Bv0v0_nonzero"] = not Bv0v0.is_zero()
log(f"  B(v0,v0) = {Bv0v0}  (matches N(v0,v0,v0): {gates['Bv0v0_matches_Nv0']}; "
    f"!= 0: {gates['Bv0v0_nonzero']})")
assert gates["Bv0v0_matches_Nv0"] and gates["Bv0v0_nonzero"], "B(v0,v0) check failed"

# ============================================================================
log("STEP 4: recompute the 3-dim invariant symmetric bilinear space "
    "(incremental method, verbatim per a1_jordan.py STEP 5) for cross-reference...")
idxmap = {}
cnt = 0
for i in range(d):
    for j in range(i, d):
        idxmap[(i, j)] = cnt
        cnt += 1
nvar = cnt


def bidx(i, j):
    return idxmap[(i, j)] if i <= j else idxmap[(j, i)]


def build_bilinear_rows(M):
    rows_ = []
    for i in range(d):
        for j in range(i, d):
            row = [K0] * nvar
            for p in range(d):
                Mpi = M[p][i]
                if Mpi.is_zero():
                    continue
                for q in range(d):
                    Mqj = M[q][j]
                    if Mqj.is_zero():
                        continue
                    coeff = Mpi * Mqj
                    bi = bidx(p, q)
                    row[bi] = row[bi] + coeff
            bij = bidx(i, j)
            row[bij] = row[bij] - K1
            rows_.append(row)
    return rows_


def incremental_nullspace(rows_, ncols, early_exit_at=None, progress_every=100):
    pivots = []
    t00 = time.time()
    for ridx, row in enumerate(rows_):
        r = row[:]
        for col, prow in pivots:
            if not r[col].is_zero():
                f = r[col]
                r = [r[j] - f * prow[j] for j in range(ncols)]
        nzcol = next((j for j in range(ncols) if not r[j].is_zero()), None)
        if nzcol is not None:
            invp = r[nzcol].inv()
            r = [x * invp for x in r]
            for k in range(len(pivots)):
                col, prow = pivots[k]
                if not prow[nzcol].is_zero():
                    f = prow[nzcol]
                    pivots[k] = [col, [prow[j] - f * r[j] for j in range(ncols)]]
            pivots.append([nzcol, r])
            pivots.sort(key=lambda t: t[0])
        if early_exit_at is not None and len(pivots) >= early_exit_at:
            log(f"    early exit: rank reached {len(pivots)} (=ncols) after "
                f"{ridx + 1}/{len(rows_)} rows ({time.time() - t00:.1f}s)")
            return pivots, True
        if (ridx + 1) % progress_every == 0:
            log(f"    ...{ridx + 1}/{len(rows_)} rows, rank so far={len(pivots)} "
                f"({time.time() - t00:.1f}s)")
    log(f"    processed all {len(rows_)} rows; final rank={len(pivots)} "
        f"({time.time() - t00:.1f}s)")
    return pivots, (len(pivots) == ncols)


t0 = time.time()
bil_rows = build_bilinear_rows(A27) + build_bilinear_rows(B27)
log(f"  built {len(bil_rows)} equations x {nvar} unknowns ({time.time() - t0:.1f}s)")
pivots, full_rank = incremental_nullspace(bil_rows, nvar, early_exit_at=nvar, progress_every=50)
bilinear_dim = 0 if full_rank else (nvar - len(pivots))
gates["bilinear_dim3"] = (bilinear_dim == 3)
log(f"  invariant symmetric bilinear space dim = {bilinear_dim}  "
    f"[GATE: matches banked A1 dim 3]: {'PASS' if gates['bilinear_dim3'] else 'FAIL'}")
assert gates["bilinear_dim3"], f"bilinear dim {bilinear_dim} != 3 (banked A1 value)"

piv_cols = sorted(c for c, _ in pivots)
row_by_col = {c: r for c, r in pivots}
free = [c for c in range(nvar) if c not in piv_cols]
bilinear_basis = []
for fc in free:
    vec = [K0] * nvar
    vec[fc] = K1
    for c in piv_cols:
        vec[c] = -row_by_col[c][fc]
    bilinear_basis.append(vec)

Bvec = [K0] * nvar
for (i, j), k in idxmap.items():
    Bvec[k] = Bmat[i][j]

solver3 = Solver(bilinear_basis)
try:
    coeffs = solver3.coords(Bvec)
    gates["B_in_span_of_3dim_space"] = True
except ValueError:
    coeffs = None
    gates["B_in_span_of_3dim_space"] = False
log(f"  chosen B expressed in the 3-dim basis: coeffs = "
    f"{[str(c) for c in coeffs] if coeffs else None}  [GATE]: "
    f"{'PASS' if gates['B_in_span_of_3dim_space'] else 'FAIL'}")
assert gates["B_in_span_of_3dim_space"], "chosen B is NOT in the banked 3-dim invariant space"

# ============================================================================
log("STEP 5: THE PROJECTORS  P_1(x) = B(v0,x)/B(v0,v0) * v0,  P_26 = I - P_1...")
Bv0v0_inv = Bv0v0.inv()
P1 = [[v0[i] * Bv0_full[j] * Bv0v0_inv for j in range(d)] for i in range(d)]
P26 = [[(K1 if i == j else K0) - P1[i][j] for j in range(d)] for i in range(d)]

gates["P1_idempotent"] = matequal(mmul(P1, P1), P1)
gates["P1_fixes_v0"] = all((apply(P1, v0)[i] - v0[i]).is_zero() for i in range(d))
comm = {}
for nm, M in (("A27", A27), ("B27", B27)):
    comm[nm] = matequal(mmul(P1, M), mmul(M, P1))
gates["P1_commutes_all"] = all(comm.values())
gates["P26_idempotent"] = matequal(mmul(P26, P26), P26)
log(f"  P1 idempotent: {gates['P1_idempotent']}; P1(v0)==v0: {gates['P1_fixes_v0']}; "
    f"P1 commutes with A27/B27: {comm}; P26 idempotent: {gates['P26_idempotent']}")
assert all([gates["P1_idempotent"], gates["P1_fixes_v0"], gates["P1_commutes_all"],
            gates["P26_idempotent"]]), "projector gates FAILED"

# ============================================================================
log("STEP 6: F4 split via the literal projector -- generic basis of ker(P_1) "
    "(nullspace of the single row B(v0,-)) ...")
generic_basis = nullspace([Bv0_full])
gates["generic_basis_dim26"] = (len(generic_basis) == 26)
log(f"  ker(P_1) basis dim = {len(generic_basis)}  [GATE ==26]: "
    f"{'PASS' if gates['generic_basis_dim26'] else 'FAIL'}")
assert gates["generic_basis_dim26"], f"ker(P_1) dim {len(generic_basis)} != 26"

Pcob = [[K0] * d for _ in range(d)]
for i in range(d):
    Pcob[i][0] = v0[i]
for col, vec in enumerate(generic_basis, start=1):
    for i in range(d):
        Pcob[i][col] = vec[i]
aug = [list(Pcob[i]) + [K1 if k == i else K0 for k in range(d)] for i in range(d)]
Rr, piv = rref(aug)
assert len(piv) == d, "F4 change-of-basis singular"
Pcob_inv = [[Rr[i][d + j] for j in range(d)] for i in range(d)]

A_f4 = mmul(mmul(Pcob_inv, A27), Pcob)
B_f4 = mmul(mmul(Pcob_inv, B27), Pcob)
Ai_f4 = mmul(mmul(Pcob_inv, A27i), Pcob)
Bi_f4 = mmul(mmul(Pcob_inv, B27i), Pcob)

f4_block_slices = [(0, 1), (1, 27)]
off_ok = True
for M_ in (A_f4, B_f4):
    for (lo_p, hi_p) in f4_block_slices:
        for (lo_q, hi_q) in f4_block_slices:
            if (lo_p, hi_p) == (lo_q, hi_q):
                continue
            for i in range(lo_p, hi_p):
                for j in range(lo_q, hi_q):
                    if not M_[i][j].is_zero():
                        off_ok = False
gates["f4_block_diagonal_exact"] = off_ok
log(f"  F4 split (1,26) block-diagonal exact: {off_ok}  [GATE]")
assert gates["f4_block_diagonal_exact"], "F4 split is NOT exactly block-diagonal"

# ============================================================================
log("STEP 7: per-block Fox h0/h1 for the F4 split (solo REL) "
    "(fox_matrices_2gen pattern verbatim per w0b_blocks.py)...")
GENS2 = ['a', 'b']


def fox_matrices_2gen(word, acts_V, dV):
    D_ = {g: [[K0] * dV for _ in range(dV)] for g in GENS2}
    Pw = meye(dV)
    for ch in word:
        low = ch.lower()
        if ch.islower():
            M = D_[low]
            for i in range(dV):
                Pi_ = Pw[i]
                Mi = M[i]
                for j in range(dV):
                    Mi[j] = Mi[j] + Pi_[j]
        else:
            PA = mmul(Pw, acts_V[ch])
            M = D_[low]
            for i in range(dV):
                Mi = M[i]
                PAi = PA[i]
                for j in range(dV):
                    Mi[j] = Mi[j] - PAi[j]
        Pw = mmul(Pw, acts_V[ch])
    return D_


def block_h0(A_V, B_V, dV):
    AmI_ = [[A_V[i][j] - (K1 if i == j else K0) for j in range(dV)] for i in range(dV)]
    BmI_ = [[B_V[i][j] - (K1 if i == j else K0) for j in range(dV)] for i in range(dV)]
    return len(nullspace(AmI_ + BmI_))


def fox_h0_h1(A_V, B_V, Ai_V, Bi_V, dV, word=REL):
    acts_V = {'a': A_V, 'A': Ai_V, 'b': B_V, 'B': Bi_V}
    assert all((sum((A_V[i][k] * Ai_V[k][j] for k in range(dV)), K0) - (K1 if i == j else K0)).is_zero()
               for i in range(dV) for j in range(dV)), "A_V not invertible via Ai_V"
    assert all((sum((B_V[i][k] * Bi_V[k][j] for k in range(dV)), K0) - (K1 if i == j else K0)).is_zero()
               for i in range(dV) for j in range(dV)), "B_V not invertible via Bi_V"
    h0 = block_h0(A_V, B_V, dV)
    Dw = fox_matrices_2gen(word, acts_V, dV)
    big = []
    for i in range(dV):
        big.append([Dw['a'][i][j] for j in range(dV)] + [Dw['b'][i][j] for j in range(dV)])
    sols1 = nullspace(big)
    z1dim = len(sols1)
    cobs = []
    for j in range(dV):
        e = [K1 if i == j else K0 for i in range(dV)]
        row = []
        for g in GENS2:
            ge = [e[i] - sum((acts_V[g][i][k] * e[k] for k in range(dV) if not e[k].is_zero()), K0)
                  for i in range(dV)]
            row += ge
        cobs.append(row)
    _, pivc = rref([list(r) for r in cobs]) if cobs else ([], [])
    rank_cob = len(pivc)
    h1 = z1dim - rank_cob
    consistent = (h0 == dV - rank_cob)
    return {"dim": dV, "h0": h0, "h1": h1, "z1_dim": z1dim,
            "coboundary_rank": rank_cob, "h0_eq_dim_minus_cobrank": consistent}


f4_blocks = []
for bi, (lo, hi) in enumerate(f4_block_slices):
    dV = hi - lo
    A_V = [row[lo:hi] for row in A_f4[lo:hi]]
    B_V = [row[lo:hi] for row in B_f4[lo:hi]]
    Ai_V = [row[lo:hi] for row in Ai_f4[lo:hi]]
    Bi_V = [row[lo:hi] for row in Bi_f4[lo:hi]]
    res = fox_h0_h1(A_V, B_V, Ai_V, Bi_V, dV)
    res["block"] = bi
    res["slice"] = [lo, hi]
    f4_blocks.append(res)
    log(f"  F4 block {bi} (dim {dV}): h0={res['h0']}  h1={res['h1']}  "
        f"(Z1={res['z1_dim']}, B1={res['coboundary_rank']})")

sum_h0_f4 = sum(b["h0"] for b in f4_blocks)
sum_h1_f4 = sum(b["h1"] for b in f4_blocks)
gates["gate_sum_h0_eq_1"] = (sum_h0_f4 == 1)
gates["gate_sum_h1_eq_3"] = (sum_h1_f4 == 3)
singlet = f4_blocks[0]
gates["gate_singlet_1_1"] = (singlet["h0"] == 1 and singlet["h1"] == 1)
block26 = f4_blocks[1]
gates["gate_26_is_0_2"] = (block26["h0"] == 0 and block26["h1"] == 2)
log(f"  SUM h0={sum_h0_f4} (gate==1: {gates['gate_sum_h0_eq_1']}); "
    f"SUM h1={sum_h1_f4} (gate==3: {gates['gate_sum_h1_eq_3']})")
log(f"  singlet (h0,h1)=({singlet['h0']},{singlet['h1']}) (gate==(1,1): {gates['gate_singlet_1_1']}); "
    f"26-block (h0,h1)=({block26['h0']},{block26['h1']}) "
    f"(SEALED EXPECTATION (0,2): {gates['gate_26_is_0_2']})")
assert gates["gate_sum_h0_eq_1"] and gates["gate_sum_h1_eq_3"] and gates["gate_singlet_1_1"], \
    "hard gates FAILED"

# ============================================================================
log("STEP 8: cross-split -- reproduce the principal-sl2 chain basis "
    "(cell3b_stage1.py / w0b_blocks.py pattern, block dims 17,9,1)...")


def eigvecs(t):
    rows_ = [[h_pr[i][j] - (K(t) if i == j else K0) for j in range(d)] for i in range(d)]
    return nullspace(rows_)


chains = []
for s_ in (8, 4, 0):
    top = eigvecs(2 * s_)
    cols = [apply(e_pr, list(v)) for v in top]
    rows_ = [[cols[c][i] for c in range(len(top))] for i in range(d)]
    ker = nullspace(rows_)
    assert len(ker) == 1, f"HW combo at 2s={2*s_}: got {len(ker)}"
    v = [sum((ker[0][c] * top[c][i] for c in range(len(top)) if not ker[0][c].is_zero()), K0)
         for i in range(d)]
    chain = [v]
    for _ in range(2 * s_):
        v = apply(f_pr, v)
        chain.append(v)
    chains.append(chain)

P_pr = [[K0] * d for _ in range(d)]
col = 0
pr_block_slices = []
for chain in chains:
    pr_block_slices.append((col, col + len(chain)))
    for v in chain:
        for i in range(d):
            P_pr[i][col] = v[i]
        col += 1
assert col == d
pr_block_dims = [hi - lo for (lo, hi) in pr_block_slices]
log(f"  principal block dims = {pr_block_dims}  slices = {pr_block_slices}")
w0b = json.load(open(W0B_JSON))
gates["pr_block_dims_match_w0b"] = (pr_block_dims == w0b["block_dims"])
assert gates["pr_block_dims_match_w0b"], "principal block dims mismatch vs banked W0b"

aug_pr = [list(P_pr[i]) + [K1 if k == i else K0 for k in range(d)] for i in range(d)]
Rr_pr, piv_pr = rref(aug_pr)
assert len(piv_pr) == d
Pinv_pr = [[Rr_pr[i][d + j] for j in range(d)] for i in range(d)]
A_pr = mmul(mmul(Pinv_pr, A27), P_pr)
B_pr = mmul(mmul(Pinv_pr, B27), P_pr)
Ai_pr = mmul(mmul(Pinv_pr, A27i), P_pr)
Bi_pr = mmul(mmul(Pinv_pr, B27i), P_pr)

off_ok_pr = True
for M_ in (A_pr, B_pr):
    for (lo_p, hi_p) in pr_block_slices:
        for (lo_q, hi_q) in pr_block_slices:
            if (lo_p, hi_p) == (lo_q, hi_q):
                continue
            for i in range(lo_p, hi_p):
                for j in range(lo_q, hi_q):
                    if not M_[i][j].is_zero():
                        off_ok_pr = False
gates["pr_block_diagonal_exact"] = off_ok_pr
log(f"  principal split block-diagonal exact: {off_ok_pr}  [GATE]")
assert gates["pr_block_diagonal_exact"], "principal split is NOT exactly block-diagonal"

# ---- identify the dim-1 principal block with v0's line
lo1, hi1 = pr_block_slices[2]
assert hi1 - lo1 == 1
w1dim = [P_pr[i][lo1] for i in range(d)]
fixed_w1 = all(x.is_zero() for x in apply(AmI, w1dim)) and all(x.is_zero() for x in apply(BmI, w1dim))
gates["w1dim_is_fixed"] = fixed_w1
ridx = v0_support[0]
cscale = w1dim[ridx] * v0[ridx].inv()
proportional = all((w1dim[i] - cscale * v0[i]).is_zero() for i in range(d))
gates["principal_1block_is_v0_line"] = fixed_w1 and proportional
log(f"  principal dim-1 block fixed: {fixed_w1}; proportional to v0 (scale={cscale}): "
    f"{proportional}  [GATE]: {'PASS' if gates['principal_1block_is_v0_line'] else 'FAIL'}")
assert gates["principal_1block_is_v0_line"], "principal 1-block is NOT v0's line"

# ---- verify the 17+9 principal span is EXACTLY B-orthogonal to v0 (== ker(P_1))
lo01, hi01 = pr_block_slices[0][0], pr_block_slices[1][1]   # 0..26 (17+9)
principal_union_basis = [[P_pr[i][col] for i in range(d)] for col in range(lo01, hi01)]
orth_checks = [dot(Bv0_full, cv).is_zero() for cv in principal_union_basis]
gates["principal_17_9_orthogonal_to_v0"] = all(orth_checks)
log(f"  all {len(principal_union_basis)} principal (17+9) chain vectors B-orthogonal "
    f"to v0 (exact): {gates['principal_17_9_orthogonal_to_v0']}  [GATE]")
assert gates["principal_17_9_orthogonal_to_v0"], \
    "principal 17+9 span is NOT exactly ker(P_1) -- B-orthogonality failed"
log("  => span(principal blocks 17,9) == ker(P_1) == F4's 26-complement EXACTLY "
    "(same 26-dim subspace, both dimension 26 and one contained in the other)")

# ---- independent h1 for the 17 and 9 principal blocks (cross-check vs banked w0b)
pr_blocks_indep = []
for bi in (0, 1):
    lo, hi = pr_block_slices[bi]
    dV = hi - lo
    A_V = [row[lo:hi] for row in A_pr[lo:hi]]
    B_V = [row[lo:hi] for row in B_pr[lo:hi]]
    Ai_V = [row[lo:hi] for row in Ai_pr[lo:hi]]
    Bi_V = [row[lo:hi] for row in Bi_pr[lo:hi]]
    res = fox_h0_h1(A_V, B_V, Ai_V, Bi_V, dV)
    res["block"] = bi
    pr_blocks_indep.append(res)
    log(f"  principal block {bi} (dim {dV}): h0={res['h0']}  h1={res['h1']} "
        f"(banked w0b: h0={w0b['per_block'][bi]['h0']}, h1={w0b['per_block'][bi]['h1']})")

gates["pr_17_9_match_banked_w0b"] = all(
    pr_blocks_indep[bi]["h0"] == w0b["per_block"][bi]["h0"] and
    pr_blocks_indep[bi]["h1"] == w0b["per_block"][bi]["h1"] for bi in (0, 1))
assert gates["pr_17_9_match_banked_w0b"], "independent 17/9 recompute mismatches banked W0b"

h1_17 = pr_blocks_indep[0]["h1"]
h1_9 = pr_blocks_indep[1]["h1"]
gates["h1_26_eq_h1_17_plus_h1_9"] = (block26["h1"] == h1_17 + h1_9)
log(f"  h1(F4-26) = {block26['h1']}; h1(17)+h1(9) = {h1_17}+{h1_9} = {h1_17+h1_9}  "
    f"[GATE: exactly equal]: {'PASS' if gates['h1_26_eq_h1_17_plus_h1_9'] else 'FAIL'}")
assert gates["h1_26_eq_h1_17_plus_h1_9"], "26's h1 does NOT equal 17-class + 9-class"

# ============================================================================
log("STEP 9: the change-of-split matrix (generic ker(P_1) basis vs "
    "principal 17+9 union basis, both bases of the SAME 26-dim subspace)...")
solver26 = Solver(principal_union_basis)
change_of_split = []
change_ok = True
for gv in generic_basis:
    try:
        coeffs26 = solver26.coords(gv)
        change_of_split.append(coeffs26)
    except ValueError:
        change_ok = False
        change_of_split.append(None)
gates["change_of_split_matrix_exact"] = change_ok
log(f"  every generic ker(P_1) basis vector expressed exactly in the principal "
    f"17+9 basis: {change_ok}  [GATE]")
assert gates["change_of_split_matrix_exact"], "change-of-split matrix computation FAILED"

all_gates_pass = all(v for v in gates.values() if isinstance(v, bool))
log(f"ALL GATES PASS: {all_gates_pass}")

# ============================================================================
out = {
    "prereg_sha256": "f32fbfff645c9fa0412a57da7090e34422a4c1068810536b4dc35b9eaee34c47",
    "clause": "C2",
    "REL": REL,
    "gates": gates,
    "all_gates_pass": all_gates_pass,
    "chosen_form": {
        "definition": "B(x,y) := N(x,y,v0), polarization of the invariant Jordan cubic norm N "
                       "at the G-fixed vector v0 (Jordan-adjoint-identity compatible: the "
                       "trace-form-at-v0 analogue of T(x,y)=N(x,y,e))",
        "B_v0_v0": kser(Bv0v0),
        "coeffs_in_3dim_basis": [str(c) for c in coeffs],
    },
    "v0_support_indices": v0_support,
    "f4_split": {
        "block_slices": f4_block_slices,
        "per_block": [{"block": b["block"], "dim": b["dim"], "h0": b["h0"], "h1": b["h1"],
                       "z1_dim": b["z1_dim"], "coboundary_rank": b["coboundary_rank"]}
                      for b in f4_blocks],
        "sum_h0": sum_h0_f4, "sum_h1": sum_h1_f4,
    },
    "principal_split_cross_check": {
        "block_dims": pr_block_dims,
        "block_slices": pr_block_slices,
        "per_block_17_9": [{"block": r["block"], "dim": r["dim"], "h0": r["h0"], "h1": r["h1"]}
                            for r in pr_blocks_indep],
        "dim1_block_is_v0_line": gates["principal_1block_is_v0_line"],
        "block17_9_equals_ker_P1_exact": gates["principal_17_9_orthogonal_to_v0"],
        "h1_26_eq_h1_17_plus_h1_9": gates["h1_26_eq_h1_17_plus_h1_9"],
    },
    "change_of_split_matrix": {
        "note": "rows = generic ker(P_1) basis vectors (from nullspace of the single row "
                 "B(v0,-)), expressed as exact K-coefficients (Fraction pairs a,b with "
                 "value a+b*sqrt(-3)) against the columns = principal 17+9 chain-basis "
                 "vectors (same order as pr_block_slices[0:2] concatenated).",
        "matrix": [[kser(c) for c in row] for row in change_of_split],
    },
    "runtime_s": time.time() - T0,
}
with open(JSON_PATH, "w") as f:
    json.dump(out, f, indent=2)
log(f"saved {JSON_PATH}")
log("DONE.")
_log_f.close()
