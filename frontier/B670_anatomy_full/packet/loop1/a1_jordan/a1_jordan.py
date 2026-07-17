"""A1 -- v0's Jordan identity (PREREG_L1.md sha 247ace23, A1 clause).

The 27 is the exceptional Jordan algebra's underlying space; the unique
cubic invariant N (banked) is the Jordan norm form; the cross product is
its polarization. Setup replicates w1_portal.py's pattern verbatim (see
that file's header): exec the B575 prefix, reuse its Jordan-cubic-N
construction (the unique invariant, gate dim 1) and its
cross-product-via-polarization C3(u,v)[z] = N(u,v,e_z). v0 is
reconstructed as the joint nullspace of (A27-I, B27-I) [W0a result],
cross-checked against w0a_singlet/w0a_v0.json.

Computes:
  1. THE CROSS-SQUARE s = v0 x v0, i.e. s[z] = N(v0,v0,e_z) for all 27
     basis z (one exact dual vector).
  2. N(v0,v0,v0) raw (trilinear; trichotomy only needs zero-vs-nonzero).
  3. dim of G-invariant symmetric bilinear forms B on the 27
     (rho(g)^T B rho(g) = B for g = a,b); if dim=1, T2(v0,v0) exactly.
  4. THE SEALED TRICHOTOMY: s=0 => RANK 1 (Cayley-plane point); s!=0 &
     N(v0)=0 => RANK 2; N(v0)!=0 => RANK 3 (invertible).

Every number lives in K = Q(sqrt(-3)) (Fraction pairs). Zero floats
anywhere in this path. Repo <repo> is
read-only; only exec'd in-memory, nothing is written there.
"""
import os
import sys
import time
import json
from fractions import Fraction as Fr

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

T0 = time.time()
def log(msg):
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)

HERE = os.path.dirname(os.path.abspath(__file__))
B575 = "<repo>/frontier/B575_bridge_obstruction/l51_obstruction.py"
W0A_JSON = "<seat-workdir>/invariant_line/w0a_singlet/w0a_v0.json"
d = 27
gates = {}

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
mmul, meye, rref, nullspace = ns["mmul"], ns["meye"], ns["rref"], ns["nullspace"]
W27, E6_e, E6_f = ns["W27"], ns["E6_e"], ns["E6_f"]


def mt(M):
    return [[M[j][i] for j in range(d)] for i in range(d)]


def apply(M, v):
    return [sum((M[i][k] * v[k] for k in range(d) if not v[k].is_zero()), K0)
            for i in range(d)]


def msub2(X, Y):
    return [[X[i][j] - Y[i][j] for j in range(d)] for i in range(d)]


# ============================================================================
log("STEP 1: v0 = joint nullspace of (A27-I, B27-I)  [W0a result]...")
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
assert all(x.is_zero() for x in apply(AmI, v0)), "(A27-I)v0 != 0"
assert all(x.is_zero() for x in apply(BmI, v0)), "(B27-I)v0 != 0"
log(f"  v0 verified exactly: (A27-I)v0=0, (B27-I)v0=0; normalized idx0={idx0}")

w0a = json.load(open(W0A_JSON))
gates["v0_idx0_matches_w0a"] = (w0a["v0_normalized_idx0"] == idx0)
w0a_v0 = [K(Fr(a_s), Fr(b_s)) for a_s, b_s in w0a["v0_coordinates_full"]]
gates["v0_matches_w0a"] = all((v0[i] - w0a_v0[i]).is_zero() for i in range(d))
log(f"  cross-check vs w0a_v0.json: idx0 match={gates['v0_idx0_matches_w0a']}, "
    f"coordinates match={gates['v0_matches_w0a']}")
assert gates["v0_idx0_matches_w0a"] and gates["v0_matches_w0a"], \
    "v0 does not match the banked W0a result"

v0_support = [i for i in range(d) if not v0[i].is_zero()]
log(f"  v0 support = {v0_support}, values = {[str(v0[i]) for i in v0_support]}")

# ============================================================================
log("STEP 2: the Jordan cubic invariant N (B632 cell2_texture.py method, "
    "verbatim per w1_portal.py STEP 3)...")
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
    for (a, b, c) in support:
        k = SUPIDX[(a, b, c)]
        for (u, v, w) in ((a, b, c), (b, a, c), (c, a, b)):
            for s, t in xent:
                if s == u:
                    key = (gi,) + tuple(sorted((t, v, w)))
                    row = eqs.setdefault(key, {})
                    row[k] = row.get(k, K0) + X[u][t]
rows = [[row.get(k, K0) for k in range(nsup)] for row in eqs.values()
        if any(not cv.is_zero() for cv in row.values())]
log(f"  invariance equations: {len(rows)}")
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
log(f"  nonzero sorted coefficients: "
    f"{sum(1 for k in range(nsup) if not Cvals[k].is_zero())}/{nsup}")


def C3(u, v):
    """The cross product: covector m -> N(u, v, e_m), i.e. u x v in 27-bar."""
    cov = [K0] * d
    for (p, q, r), cval in CFULL.items():
        if not u[p].is_zero() and not v[q].is_zero():
            cov[r] = cov[r] + cval * u[p] * v[q]
    return cov


def dot(f, v):
    return sum((f[t] * v[t] for t in range(d) if not v[t].is_zero()), K0)


u1 = [K(i % 5 - 2) for i in range(d)]
v1 = [K((2 * i) % 7 - 3) for i in range(d)]
w1 = [K((3 * i) % 4 - 1) for i in range(d)]
ninv = {}
for nm, M in (("A27", A27), ("B27", B27)):
    lhs = dot(C3(apply(M, u1), apply(M, v1)), apply(M, w1))
    rhs = dot(C3(u1, v1), w1)
    ninv[nm] = (lhs - rhs).is_zero()
    log(f"  N-invariance under {nm}: {'PASS' if ninv[nm] else 'FAIL'}")
gates["N_invariant_all"] = all(ninv.values())
assert gates["N_invariant_all"], "N is NOT rho-invariant"

# ============================================================================
log("STEP 3: THE CROSS-SQUARE  s = v0 x v0  (s[z] = N(v0,v0,e_z))...")
s = C3(v0, v0)
s_support = [i for i in range(d) if not s[i].is_zero()]
s_is_zero = (len(s_support) == 0)
gates["s_computed"] = True
log(f"  s identically zero: {s_is_zero}")
if not s_is_zero:
    log(f"  s support size = {len(s_support)}, indices = {s_support}")
    for i in s_support:
        log(f"    s[{i}] = {s[i]}")

# ============================================================================
log("STEP 4: N(v0,v0,v0) raw (trilinear value)...")
Nv0 = dot(s, v0)
Nv0_is_zero = Nv0.is_zero()
log(f"  N(v0,v0,v0) = {Nv0}   (raw trilinear; some conventions divide by 6 or 3 "
    f"for the 'norm' -- trichotomy only needs zero-vs-nonzero, invariant under any "
    f"nonzero-scalar convention)")
log(f"  N(v0) zero: {Nv0_is_zero}")

# ============================================================================
log("STEP 5: dim of G-invariant symmetric bilinear forms on 27 "
    "(rho(g)^T B rho(g) = B for g=a,b)...")

idxmap = {}
cnt = 0
for i in range(d):
    for j in range(i, d):
        idxmap[(i, j)] = cnt
        cnt += 1
nvar = cnt
log(f"  symmetric-B unknowns: {nvar}")


def bidx(i, j):
    return idxmap[(i, j)] if i <= j else idxmap[(j, i)]


def build_bilinear_rows(M):
    """Rows of the linear system (M^T B M)_{ij} - B_{ij} = 0, i<=j, in the
    nvar symmetric-B unknowns."""
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
    """Exact incremental Gauss-Jordan elimination (same math as the banked
    rref()/nullspace(), just row-incremental so we can early-exit the instant
    the constraint rank saturates ncols -- at that point the nullspace is
    PROVABLY trivial no matter what the unprocessed rows say)."""
    pivots = []  # list of [col, row] kept in increasing col order (RREF invariant)
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
                f"{ridx + 1}/{len(rows_)} rows ({time.time() - t00:.1f}s) "
                f"-- nullspace provably trivial")
            return pivots, True
        if (ridx + 1) % progress_every == 0:
            log(f"    ...{ridx + 1}/{len(rows_)} rows, rank so far={len(pivots)} "
                f"({time.time() - t00:.1f}s)")
    log(f"    processed all {len(rows_)} rows; final rank={len(pivots)} "
        f"({time.time() - t00:.1f}s)")
    return pivots, (len(pivots) == ncols)


# self-test the incremental method against the banked nullspace() on the
# already-verified (dim=1, gate-passed) cubic-invariant system from STEP 2
log("  self-test: incremental method vs banked nullspace() on the STEP 2 "
    "cubic-invariant system (known dim=1)...")
test_pivots, test_full = incremental_nullspace(rows, nsup, early_exit_at=nsup,
                                                progress_every=10 ** 9)
test_dim = nsup - len(test_pivots) if not test_full else 0
gates["incremental_selftest_matches_banked_nullspace"] = (test_dim == len(sol))
log(f"    incremental dim={test_dim} vs banked nullspace() dim={len(sol)}: "
    f"{'MATCH' if gates['incremental_selftest_matches_banked_nullspace'] else 'MISMATCH'}")
assert gates["incremental_selftest_matches_banked_nullspace"], \
    "incremental elimination self-test FAILED -- do not trust the big run"

t0 = time.time()
bil_rows = build_bilinear_rows(A27) + build_bilinear_rows(B27)
log(f"  built {len(bil_rows)} equations x {nvar} unknowns ({time.time() - t0:.1f}s)")

pivots, full_rank = incremental_nullspace(bil_rows, nvar, early_exit_at=nvar,
                                           progress_every=50)
bilinear_dim = 0 if full_rank else (nvar - len(pivots))
gates["bilinear_computed"] = True
log(f"  invariant symmetric bilinear space dim = {bilinear_dim}")

bilinear_basis = []
T2 = None
T2_v0v0 = None
if bilinear_dim > 0:
    piv_cols = sorted(c for c, _ in pivots)
    row_by_col = {c: r for c, r in pivots}
    free = [c for c in range(nvar) if c not in piv_cols]
    for fc in free:
        vec = [K0] * nvar
        vec[fc] = K1
        for c in piv_cols:
            vec[c] = -row_by_col[c][fc]
        bilinear_basis.append(vec)

    def vec_to_sym(vec):
        Bm = [[K0] * d for _ in range(d)]
        for (i, j), k in idxmap.items():
            Bm[i][j] = vec[k]
            Bm[j][i] = vec[k]
        return Bm

    # verify every basis vector exactly satisfies the invariance equations
    ok_all = True
    for bvi, vec in enumerate(bilinear_basis):
        Bm = vec_to_sym(vec)
        for nm, M in (("A27", A27), ("B27", B27)):
            lhs = mmul(mmul(mt(M), Bm), M)
            diff = [[lhs[i][j] - Bm[i][j] for j in range(d)] for i in range(d)]
            ok = all(x.is_zero() for row_ in diff for x in row_)
            ok_all = ok_all and ok
            log(f"    basis[{bvi}] invariance under {nm}: {'PASS' if ok else 'FAIL'}")
        sym_ok = all((Bm[i][j] - Bm[j][i]).is_zero() for i in range(d) for j in range(d))
        ok_all = ok_all and sym_ok
        log(f"    basis[{bvi}] symmetric: {'PASS' if sym_ok else 'FAIL'}")
    gates["bilinear_basis_verified"] = ok_all
    assert ok_all, "invariant bilinear basis FAILED verification"

    if bilinear_dim == 1:
        T2 = vec_to_sym(bilinear_basis[0])
        T2v0 = apply(T2, v0)
        T2_v0v0 = dot(T2v0, v0)
        log(f"  T2(v0,v0) = {T2_v0v0}")

# ============================================================================
log("STEP 6: THE SEALED TRICHOTOMY...")
if s_is_zero:
    rank_class = 1
    rank_name = "RANK 1 -- a point of the exceptional Jordan geometry (the Cayley plane)"
elif Nv0_is_zero:
    rank_class = 2
    rank_name = "RANK 2"
else:
    rank_class = 3
    rank_name = "RANK 3 (invertible direction)"
log(f"  v0 x v0 {'= 0' if s_is_zero else '!= 0'}; N(v0) {'= 0' if Nv0_is_zero else '!= 0'}")
log(f"  VERDICT: {rank_name}")

# ---- refinement (only meaningful if s != 0): compare s against the dual
# invariant line, i.e. the joint nullspace of (dacts_a - I, dacts_b - I) in
# the contragredient (27-bar) representation, rho-bar(g) = (rho(g)^-1)^T,
# per w1_portal.py STEP 4's dual machinery.
refinement = None
if not s_is_zero:
    log("  s != 0: computing the refinement (dual invariant line comparison)...")

    def transpose(M):
        return [[M[j][i] for j in range(d)] for i in range(d)]

    da = transpose(A27i)
    db = transpose(B27i)
    daI = msub2(da, I)
    dbI = msub2(db, I)
    dual_ns = nullspace(daI + dbI)
    gates["dual_invariant_line_dim"] = len(dual_ns)
    log(f"    dual (contragredient) invariant line dim = {len(dual_ns)}")
    if len(dual_ns) == 1:
        dline_raw = dual_ns[0]
        didx0 = next(i for i, x in enumerate(dline_raw) if not x.is_zero())
        dline = [x * dline_raw[didx0].inv() for x in dline_raw]
        # is s proportional to dline? compare on the common support.
        s_idx0 = s_support[0]
        if not dline[s_idx0].is_zero():
            ratio = s[s_idx0] * dline[s_idx0].inv()
            proportional = all((s[i] - ratio * dline[i]).is_zero() for i in range(d))
        else:
            proportional = False
        refinement = {"dual_line_dim": len(dual_ns),
                      "s_proportional_to_dual_line": proportional}
        log(f"    s proportional to the dual invariant line: {proportional}")
    else:
        refinement = {"dual_line_dim": len(dual_ns),
                      "s_proportional_to_dual_line": "N/A (dual line not 1-dim)"}
else:
    log("  s = 0: refinement N/A (rank-1 case; no nonzero cross-square to compare).")

# ============================================================================
all_gates_pass = all(v for k, v in gates.items() if isinstance(v, bool))
log(f"ALL GATES PASS: {all_gates_pass}")

def kser(x):
    return [str(x.a), str(x.b)]

out = {
    "prereg_sha256": "247ace23f25403c6617e403215560fea8b8b2e1e7e882b2c4210fc7f01bd0870",
    "gates": gates,
    "v0_normalized_idx0": idx0,
    "v0_support_indices": v0_support,
    "v0_coordinates_at_support": {str(i): kser(v0[i]) for i in v0_support},
    "cross_square": {
        "s_is_zero": s_is_zero,
        "s_support_indices": s_support,
        "s_values_at_support": {str(i): kser(s[i]) for i in s_support},
    },
    "N_v0_v0_v0_raw": kser(Nv0),
    "N_v0_is_zero": Nv0_is_zero,
    "invariant_bilinear": {
        "dim": bilinear_dim,
        "T2_v0_v0": kser(T2_v0v0) if T2_v0v0 is not None else None,
    },
    "classification": {
        "rank": rank_class,
        "name": rank_name,
    },
    "refinement_dual_line": refinement,
    "silver_note": "v0_silver's cross-square/N/bilinear invariants NOT computed here "
                    "(a separate cell per prereg instruction) -- flagged for the frontier.",
    "runtime_s": time.time() - T0,
}
with open(os.path.join(HERE, "a1_results.json"), "w") as f:
    json.dump(out, f, indent=2)
log(f"saved {os.path.join(HERE, 'a1_results.json')}")
log("DONE.")
