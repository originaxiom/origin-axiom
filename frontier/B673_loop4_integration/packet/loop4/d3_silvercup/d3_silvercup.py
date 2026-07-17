"""D3 -- THE SILVER VECTOR CUP (PREREG_L4.md, D3 clause; K020 on the loop-3
discovery). Compute agent: loop 4 cell D3.

QUESTION: C1 (loop3/c1_vecmassey) proved the GOLDEN vector cup classes
[u_i cup_x u_j] in H^2(D; 27-bar) NONZERO for all six solo off-diagonal pairs
(i,j) in {2,3,4}x{2,3,4}, i!=j (Koszul-antisymmetric, exact witnesses banked).
Does the SILVER object (B649, F4-verified) reproduce this FORM (FORM-MATCH:
structural supra-class coupling) or not (FORM-MISMATCH: golden-specific)?

METHOD (literally C1's method, ported to the silver DOUBLE presentation):
  - GENS_D = 'abcdef' (6 letters), RELATORS_D = 6 relators (the silver
    DOUBLE's presentation, from b649_stage3b_swap.py -- weld + Fox/Z1/cob/reps,
    exec'd verbatim through the SAME cut point w2a_silver.py used).
  - classes[0..4]: the 5 banked H^1(D_silver;27) representative cocycles
    ("reps"), sliced per generator.
  - dacts: the contragredient action rho-bar(g) = transpose(LETS[G]) (same
    convention as w1_portal.py/w2a_silver.py).
  - dual_big: the dual Fox-derivative matrix F (162x162 = 6 relators*27 rows
    x 6 gens*27 cols), built exactly as w2a_silver.py's dual_big.
  - C3: the silver Jordan cross product, REUSED VERBATIM from the BANKED
    cubic_rational.json (B649's rational Cartan cubic) -- NOT re-derived from
    scratch. This is the SAME cubic w2a_silver.py and b3_silver.py already
    gated as N-invariant under all six letters a..f. Stated explicitly per
    protocol: recovered from banked structure, not solved fresh.
  - c_ij(g,h) := C3(u_i(g), rho(g).u_j(h)) -- the vector cup cocycle, valued
    in 27-bar, for classes i,j in {0,...,4} (the split boundary-born/solo is
    UNRESOLVED for silver -- w2a_silver.py's FINDINGS_CC2.md flags the portal
    as upper-triangular, not block-diagonal, with no canonical alignment to
    golden's 2+3 labels -- so per protocol we use the FULL 5-basis, all 5x5
    ordered pairs, mirroring C1's own 3x3 grid computation exactly).
  - Solvability test: [c_ij]=0 iff BASE_ij (the constant defect of the
    bounding-cochain recursion at y=0) lies in im(F); checked by pairing
    against ker(F^T) (computed ONCE, reused for all 25 pairs).

PERFORMANCE NOTE (honest, not mathematics): the reused c1_vecmassey.py-style
b_eval recomputes cocycle_val(zi,prefix) and rho_word(prefix) FROM SCRATCH at
each character of each relator word (O(word_len^2) matrix products). Over the
silver field L=Q(s,i) (deg-8, ~3x costlier per 27x27 product than golden's
K=Q(sqrt(-3)), empirically measured at ~0.65s/product here vs golden's
observed ~0.19s/product), this pattern would cost the same total number of
27x27 products as the golden run scaled up, i.e. a comparable-to-somewhat
longer wall time -- feasible but wasteful. base_vec_fast below computes the
IDENTICAL recursion (same formula, term for term) via incremental prefix
tracking (O(word_len) products per relator instead of O(word_len^2)): the two
running quantities Ui (=cocycle_val(zi,prefix)) and Pg (=rho_word(prefix)) are
updated once per character instead of rebuilt from the start of the word every
time. This is bookkeeping only -- verified against the slow c_ij_raw path on
spot checks below -- not a change to the mathematical construction.

Every number lives in L = Q(s,i) (Fraction-pairs on the {1,s,s^2,s^3} basis,
s^4=8s^2+16, banked field tower). Zero floats anywhere. Repo (origin-axiom)
read-only throughout; all writes confined to this cell directory.
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
B649 = "<repo>/frontier/B649_silver_holonomy"
SWAP = os.path.join(B649, "b649_stage3b_swap.py")

d = 27
gates = {}

# ============================================================================
log("STEP 0: exec b649_stage3b_swap.py prefix (weld + silver DOUBLE "
    "Fox/Z1/cob/reps) -- SAME cut point w2a_silver.py used ('# ---- sigma* "
    "---'). Source READ only, no writes to origin-axiom. ~4-5 min expected.")
src = open(SWAP).read()
cut = src.index("# ---- sigma* ---")
ns = {"__name__": "b649_double_prefix", "__file__": SWAP}
t0 = time.time()
exec(compile(src[:cut], SWAP, "exec"), ns)
log(f"  prefix exec complete ({time.time()-t0:.0f}s)")

L, Lc, L0, L1 = ns["L"], ns["Lc"], ns["L0"], ns["L1"]
meye, mmul, mscale, madd = ns["meye"], ns["mmul"], ns["mscale"], ns["madd"]
mconj27 = ns["mconj27"]
S1, S2, LETS = ns["S1"], ns["S2"], ns["LETS"]
RELATORS_D, GENS_D = ns["RELATORS"], ns["GENS"]
rows27_D = ns["rows27"]
Z1_D = ns["Z1"]
cob_D = ns["cob"]
reps = ns["reps"]
nc_D = ns["nc"]
L_nullspace_basis = ns["L_nullspace_basis"]
Span = ns["Span"]
U27, U27i = ns["U27"], ns["U27i"]

log(f"  double presentation: GENS={GENS_D!r}  RELATORS={RELATORS_D}")
log(f"  relator lengths: {[len(w) for w in RELATORS_D]}  total chars: "
    f"{sum(len(w) for w in RELATORS_D)}")


# ---- generic exact linear algebra over L (verbatim pattern, w2a_silver.py) -
def is_zero_vec(v):
    return all(x.is_zero() for x in v)


def matvec(M, v):
    n = len(v)
    return [sum((M[i][k] * v[k] for k in range(n) if not v[k].is_zero()), L0)
            for i in range(len(M))]


def vadd(u, v):
    assert len(u) == len(v)
    return [u[k] + v[k] for k in range(len(u))]


def vsub(u, v):
    assert len(u) == len(v)
    return [u[k] - v[k] for k in range(len(u))]


def vdot(u, v):
    assert len(u) == len(v)
    n = len(u)
    return sum((u[k] * v[k] for k in range(n)
                if not u[k].is_zero() and not v[k].is_zero()), L0)


def transposeL(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]


def rrefL(rows):
    A = [r[:] for r in rows]
    m = len(A)
    ncols = len(A[0]) if m else 0
    r = 0
    pivs = []
    for c in range(ncols):
        piv = next((k for k in range(r, m) if not A[k][c].is_zero()), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv_inv = A[r][c].inv()
        A[r] = [x * pv_inv for x in A[r]]
        for k in range(m):
            if k != r and not A[k][c].is_zero():
                f = A[k][c]
                A[k] = [x - f * y for x, y in zip(A[k], A[r])]
        pivs.append(c)
        r += 1
        if r == m:
            break
    return A, pivs


def fmtL(x):
    if x.is_zero():
        return "0"

    def poly_str(coeffs, varname):
        terms = []
        for k, c in enumerate(coeffs):
            if c == 0:
                continue
            if k == 0:
                terms.append(f"{c}")
            elif k == 1:
                terms.append(f"{c}*{varname}")
            else:
                terms.append(f"{c}*{varname}^{k}")
        return "+".join(terms) if terms else "0"

    re_s = poly_str(x.re, "s")
    im_s = poly_str(x.im, "s")
    if im_s == "0":
        return re_s
    return f"({re_s}) + i*({im_s})"


# ============================================================================
log("=== GATE 1 (the sealed PREREG D3 gate): reproduce banked silver DOUBLE "
    "dims h0=1, h1=5 from the letters, before any cup work ===")
h0_D = d - nc_D
h1_D = len(Z1_D) - nc_D
gates["double_h0_eq_1"] = (h0_D == 1)
gates["double_h1_eq_5"] = (h1_D == 5)
log(f"  double: dim Z1={len(Z1_D)} rank(cob)={nc_D}  ->  h0(D)={h0_D} h1(D)={h1_D}")
log(f"  GATE (h0=1,h1=5): "
    f"{'PASS' if (gates['double_h0_eq_1'] and gates['double_h1_eq_5']) else 'FAIL -- STOP, no improvisation'}")
if not (gates["double_h0_eq_1"] and gates["double_h1_eq_5"]):
    out = {"verdict": "STOPPED", "reason": "silver h0/h1 gate FAILED", "gates": gates}
    json.dump(out, open(os.path.join(HERE, "d3_results.json"), "w"), indent=2)
    log("STOP: silver h0/h1 gate FAILED -- no improvisation, reporting and exiting.")
    sys.exit(1)

# ============================================================================
log("=== STEP A: build the dual (contragredient) Fox machinery on the "
    "silver DOUBLE (6 generators, 6 relators) -- dacts, dual_big ===")
dacts = {}
for g in GENS_D:
    Gup = g.upper()
    dacts[g] = transposeL(LETS[Gup])
    dacts[Gup] = transposeL(LETS[g])
log(f"  dacts built for {sorted(dacts.keys())}")


def fox_matrices_D(word, actsmap):
    D_ = {g: [[L0] * d for _ in range(d)] for g in GENS_D}
    P = meye(d)
    for ch in word:
        low = ch.lower()
        if ch.islower():
            M = D_[low]
            for i in range(d):
                Pi_ = P[i]
                Mi = M[i]
                for j in range(d):
                    Mi[j] = Mi[j] + Pi_[j]
        else:
            PA = mmul(P, actsmap[ch])
            M = D_[low]
            for i in range(d):
                Mi = M[i]
                PAi = PA[i]
                for j in range(d):
                    Mi[j] = Mi[j] - PAi[j]
        P = mmul(P, actsmap[ch])
    return D_


t0 = time.time()
dual_big = []
for w in RELATORS_D:
    Dw = fox_matrices_D(w, dacts)
    for i in range(d):
        dual_big.append([Dw[g][i][j] for g in GENS_D for j in range(d)])
log(f"  dual Fox-derivative matrix F built ({len(dual_big)}x{len(dual_big[0])}) "
    f"({time.time()-t0:.0f}s)")

t0 = time.time()
Z1_dual = L_nullspace_basis(dual_big, len(GENS_D) * d)
log(f"  dim Z1(dual) = {len(Z1_dual)}  ({time.time()-t0:.0f}s)")

cobs_dual = []
for j in range(d):
    e = [L1 if i == j else L0 for i in range(d)]
    row = []
    for g in GENS_D:
        ge = [e[i] - sum((dacts[g][i][k] * e[k] for k in range(d)
                          if not e[k].is_zero()), L0)
              for i in range(d)]
        row += ge
    cobs_dual.append(row)

span_dual = Span(len(GENS_D) * d)
rank_cob_dual = 0
for cv in cobs_dual:
    if span_dual.add(cv, None):
        rank_cob_dual += 1
h0_dual = d - rank_cob_dual
h1_dual = len(Z1_dual) - rank_cob_dual
gates["h1_dual_eq_5"] = (h1_dual == 5)
log(f"  h0(dual)={h0_dual}  h1(dual)={h1_dual}  [GATE h1_dual==5]: "
    f"{'PASS' if gates['h1_dual_eq_5'] else 'FAIL'}")
assert gates["h1_dual_eq_5"], f"h1(dual)={h1_dual} != 5"

t0 = time.time()
Ft = transposeL(dual_big)
leftnull = L_nullspace_basis(Ft, len(GENS_D) * d)
log(f"  ker(F^T) dim = {len(leftnull)}  ({time.time()-t0:.0f}s)  "
    f"[= dim C^2(dual)/B^2(dual), the superspace containing true H^2(dual)]")
gates["leftnull_dim_matches_z1dim"] = (len(leftnull) == len(Z1_dual))
log(f"  ker(F^T) dim == ker(F) dim [square-matrix rank-nullity check]: "
    f"{gates['leftnull_dim_matches_z1dim']}")
assert gates["leftnull_dim_matches_z1dim"]

# ============================================================================
log("=== STEP B: h^2(D_silver;27bar)=5 CONSISTENCY GATE (Poincare duality + "
    "UCT, L a field): h0(dual)=? h1(dual)=5(gated) h3(dual)=h0(primal)=1 "
    "(gated double_h0_eq_1); Euler char forces h2(dual)=5 ===")
h3_dual_by_PD = 1
euler = h0_dual - h1_dual + 5 - h3_dual_by_PD
gates["h2_dual_euler_consistent"] = (euler == 0) and (h0_dual == 1) and (h1_dual == 5)
log(f"  h0(dual)={h0_dual}  h1(dual)={h1_dual}  h3(dual)[PD from h0(primal)]="
    f"{h3_dual_by_PD}  =>  h2(dual) forced = 5 by Euler(=0) consistency: "
    f"{'PASS' if gates['h2_dual_euler_consistent'] else 'FAIL'}")
assert gates["h2_dual_euler_consistent"]
H2_DUAL_DIM = 5

# ============================================================================
log("=== STEP C: the silver Jordan cross product C3, REUSED from the "
    "BANKED cubic_rational.json (B649's rational Cartan cubic) -- NOT "
    "re-derived from scratch. This is the same object w2a_silver.py / "
    "b3_silver.py already gated N-invariant under all six letters a..f. ===")
CUB = {tuple(map(int, k.split(","))): Fr(v)
       for k, v in json.load(open(os.path.join(B649, "cubic_rational.json"))).items()}
log(f"  cubic_rational.json entries loaded: {len(CUB)} (banked, read-only)")


def C3(u, v):
    cov = [L0] * d
    for (p, q, r_), cval in CUB.items():
        if not u[p].is_zero() and not v[q].is_zero():
            cov[r_] = cov[r_] + Lc(cval) * u[p] * v[q]
    return cov


log("  CONTROL: C3 is exactly SYMMETRIC (C3(u,v)=C3(v,u)) on test vectors...")
_tu = [Lc(Fr((3 * i + 1) % 11 - 5)) for i in range(d)]
_tv = [Lc(Fr((5 * i + 2) % 9 - 4)) for i in range(d)]
gates["C3_symmetric"] = all((C3(_tu, _tv)[t] - C3(_tv, _tu)[t]).is_zero() for t in range(d))
log(f"  C3(u,v)==C3(v,u): {'PASS' if gates['C3_symmetric'] else 'FAIL'}")
assert gates["C3_symmetric"]

log("  CONTROL: C3 equivariance C3(rho(g)x,rho(g)y) = rho-bar(g).C3(x,y) "
    "for ALL SIX silver generators a,b,c,d,e,f (this is what makes the "
    "cup's cocycle identity a general consequence, not a coincidence)...")
_eq = {}
for g in GENS_D:
    lhs = C3(matvec(LETS[g], _tu), matvec(LETS[g], _tv))
    rhs = matvec(dacts[g], C3(_tu, _tv))
    _eq[g] = all((lhs[t] - rhs[t]).is_zero() for t in range(d))
gates["C3_equivariant"] = all(_eq.values())
log(f"  C3(gx,gy) == rho-bar(g).C3(x,y) for g in a..f: {gates['C3_equivariant']} {_eq}")
assert gates["C3_equivariant"]

# ============================================================================
log("=== STEP D: small glue -- cocycle_val/rho_word (same pattern as "
    "c1_vecmassey.py's, silver LETS) + the vector cup "
    "c_ij(g,h) = C3(u_i(g), rho(g).u_j(h)) ===")


def lv(zc, ch):
    low = ch.lower()
    if ch.islower():
        return zc[low]
    return [L0 - x for x in matvec(LETS[ch], zc[low])]


def cocycle_val(zc, word):
    val = [L0] * d
    P = meye(d)
    for ch in word:
        add = matvec(P, lv(zc, ch))
        val = vadd(val, add)
        P = mmul(P, LETS[ch])
    return val


def rho_word(word):
    P = meye(d)
    for ch in word:
        P = mmul(P, LETS[ch])
    return P


def c_ij_raw(zi, zj, gw, hw):
    ug = cocycle_val(zi, gw)
    vh = cocycle_val(zj, hw)
    rgvh = matvec(rho_word(gw), vh)
    return C3(ug, rgvh)


def slice_rep(u162):
    return {g: u162[27 * i:27 * (i + 1)] for i, g in enumerate(GENS_D)}


classes = [slice_rep(r) for r in reps]
NCLS = len(classes)
assert NCLS == 5
log(f"  {NCLS} silver H^1 classes sliced from reps (full basis; split "
    f"UNRESOLVED per w2a_silver.py FINDINGS_CC2.md -- using ALL 5, not a "
    f"restricted solo subset)")

log("  support-pattern context (banked in w2a_silver.py, recomputed here "
    "for cross-check, NOT used to restrict scope):")
split_info = []
for idx, cd in enumerate(classes):
    nz_gens = [g for g in GENS_D if not is_zero_vec(cd[g])]
    split_info.append({"class": idx, "nonzero_generators": nz_gens})
    log(f"    class {idx}: nonzero on generators {nz_gens}")

# ============================================================================
log("=== STEP E: cocycle identity delta c_ij = 0 spot check on generic word "
    "triples (both sides a,b,c / d,e,f + mixed), all 5x5 = 25 pairs ===")
TEST_TRIPLES = [
    ('a', 'b', 'c'), ('b', 'a', 'c'), ('a', 'A', 'b'), ('a', 'b', 'a'),
    ('c', 'b', 'A'), ('d', 'e', 'f'), ('e', 'd', 'f'), ('a', 'd', 'e'),
    ('d', 'a', 'b'), ('c', 'f', 'D'),
]


def cocycle_identity_ok(i, j):
    zi, zj = classes[i], classes[j]
    oks = []
    for (g, h, k) in TEST_TRIPLES:
        chk = c_ij_raw(zi, zj, h, k)
        cghk = c_ij_raw(zi, zj, g + h, k)
        cghk2 = c_ij_raw(zi, zj, g, h + k)
        cgh = c_ij_raw(zi, zj, g, h)
        lhs = vsub(vadd(vsub(matvec(dacts[g], chk), cghk), cghk2), cgh)
        oks.append(all(x.is_zero() for x in lhs))
    return all(oks)


PAIRS25 = [(i, j) for i in range(NCLS) for j in range(NCLS)]
t0 = time.time()
cocycle_flags = {}
for (i, j) in PAIRS25:
    ok = cocycle_identity_ok(i, j)
    cocycle_flags[(i, j)] = ok
gates["all_cij_are_cocycles"] = all(cocycle_flags.values())
log(f"  delta c_ij = 0 on {len(TEST_TRIPLES)} generator triples, all 25 "
    f"pairs: {gates['all_cij_are_cocycles']}  ({time.time()-t0:.0f}s)")
assert gates["all_cij_are_cocycles"], "a c_ij cocycle identity FAILED -- construction wrong"

# ============================================================================
log("=== STEP F: BASE_ij (constant defect of the bounding recursion at y=0) "
    "for all 25 pairs, via base_vec_fast's incremental-prefix optimization "
    "(same recursion as c1_vecmassey.py's b_eval, term for term; verified by "
    "spot-check below against the slow c_ij_raw-based path) ===")

ZERO_Y = {g: [L0] * d for g in GENS_D}


def a_const_table(zi, zj):
    tbl = {}
    for g in GENS_D:
        tbl[g.upper()] = c_ij_raw(zi, zj, g, g.upper())
    return tbl


def b_val_of(y, aconst, ch):
    if ch.islower():
        return y[ch]
    low = ch.lower()
    return matvec(dacts[ch], vsub(aconst[ch], y[low]))


def b_eval_slow(zi, zj, y, aconst, word):
    """The ORIGINAL c1_vecmassey.py-pattern recursion (O(len^2)); used only
    for the spot-check control below, never for the full 25-pair sweep."""
    total = [L0] * d
    Pbar = meye(d)
    prefix = ""
    for ch in word:
        bch = b_val_of(y, aconst, ch)
        term = matvec(Pbar, bch)
        defect = c_ij_raw(zi, zj, prefix, ch)
        total = vsub(vadd(total, term), defect)
        Pbar = mmul(Pbar, dacts[ch])
        prefix = prefix + ch
    return total


def base_vec_fast(zi, zj):
    """Identical recursion to b_eval_slow (defect = c_ij_raw(zi,zj,prefix,ch)
    at each step, y=0 throughout), computed via incremental prefix tracking:
    Ui tracks cocycle_val(zi,prefix), Pg tracks rho_word(prefix), both updated
    by exactly the same one-step recursion cocycle_val/rho_word use
    internally -- O(word_len) matrix products per relator instead of
    O(word_len^2)."""
    aconst = a_const_table(zi, zj)
    base = []
    for word in RELATORS_D:
        total = [L0] * d
        Pbar = meye(d)
        Ui = [L0] * d
        Pg = meye(d)
        for ch in word:
            bch = b_val_of(ZERO_Y, aconst, ch)
            term = matvec(Pbar, bch)
            vjc = lv(zj, ch)                    # cocycle_val(zj, ch), 1 char
            rgvh = matvec(Pg, vjc)               # rho_word(prefix) . vjc
            defect = C3(Ui, rgvh)                # C3(cocycle_val(zi,prefix), .)
            total = vsub(vadd(total, term), defect)
            Ui = vadd(Ui, matvec(Pg, lv(zi, ch)))
            Pg = mmul(Pg, LETS[ch])
            Pbar = mmul(Pbar, dacts[ch])
        base += total
    return base, aconst


log("  spot-check: base_vec_fast == b_eval_slow-based BASE on pair (0,1)...")
_ac_slow = a_const_table(classes[0], classes[1])
_base_slow = []
for _w in RELATORS_D:
    _base_slow += b_eval_slow(classes[0], classes[1], ZERO_Y, _ac_slow, _w)
_base_fast, _ac_fast = base_vec_fast(classes[0], classes[1])
_spotcheck_ok = all((_base_slow[t] - _base_fast[t]).is_zero() for t in range(len(_base_slow)))
gates["base_vec_fast_matches_slow_path"] = _spotcheck_ok
log(f"  base_vec_fast matches the slow (c1_vecmassey.py-pattern) path "
    f"exactly on (0,1): {_spotcheck_ok}")
assert gates["base_vec_fast_matches_slow_path"], "fast/slow BASE mismatch -- optimization unsound"

t0 = time.time()
BASE = {}
ACONST = {}
for (i, j) in PAIRS25:
    b, ac = base_vec_fast(classes[i], classes[j])
    BASE[(i, j)] = b
    ACONST[(i, j)] = ac
log(f"  BASE_ij built for all 25 pairs ({time.time()-t0:.1f}s)")


def obstruction_coords(vec):
    return [vdot(psi, vec) for psi in leftnull]


def is_zero_class(vec):
    return all(c.is_zero() for c in obstruction_coords(vec))


OBS = {}
ZERO_FLAG = {}
for (i, j) in PAIRS25:
    OBS[(i, j)] = obstruction_coords(BASE[(i, j)])
    ZERO_FLAG[(i, j)] = all(c.is_zero() for c in OBS[(i, j)])
    nnz = sum(1 for c in OBS[(i, j)] if not c.is_zero())
    log(f"  [c_{i}{j}]: {'ZERO' if ZERO_FLAG[(i,j)] else 'NONZERO'}  "
        f"(nonzero obstruction coords: {nnz}/{len(leftnull)})")

log("  5x5 pattern (rows i, cols j, order 0,1,2,3,4) -- True = ZERO class:")
for i in range(NCLS):
    log("    [" + ", ".join(str(ZERO_FLAG[(i, j)]) for j in range(NCLS)) + "]")

OFFDIAG = [(i, j) for i in range(NCLS) for j in range(NCLS) if i != j]
nonzero_pairs = [p for p in OFFDIAG if not ZERO_FLAG[p]]
zero_pairs = [p for p in OFFDIAG if ZERO_FLAG[p]]
gates["step1_all_offdiag_zero"] = (len(nonzero_pairs) == 0)
log(f"  off-diagonal nonzero pairs: {len(nonzero_pairs)}/{len(OFFDIAG)}  "
    f"-> {nonzero_pairs}")

# ---- Koszul antisymmetry control --------------------------------------
log("  CONTROL: Koszul graded-commutativity [c_ij] = -[c_ji] (C3 symmetric, "
    "gated above) -- test [c_ij]+[c_ji] = 0 for all 25 pairs (diagonal: "
    "predicts [c_ii]=0)...")
antisym_ok = {}
for (i, j) in PAIRS25:
    s = vadd(BASE[(i, j)], BASE[(j, i)])
    antisym_ok[(i, j)] = is_zero_class(s)
gates["cij_plus_cji_zero_all"] = all(antisym_ok.values())
log(f"  [c_ij]+[c_ji]=0 for all 25 pairs: {gates['cij_plus_cji_zero_all']}  "
    f"(per-pair: {{{', '.join(f'{i}{j}:{antisym_ok[(i,j)]}' for (i,j) in PAIRS25)}}})")
diag_zero = all(ZERO_FLAG[(i, i)] for i in range(NCLS))
gates["diagonal_cii_zero"] = diag_zero
log(f"  diagonal [c_ii]=0 for all i (Koszul self-cup consequence): {diag_zero}")

# ---- coboundary-shift-invariance control -------------------------------
log("  CONTROL: coboundary-shift invariance -- shift class 0 by a primal "
    "coboundary on ALL SIX generators, recompute obstruction coords for "
    "(0,1) and (0,2), verify UNCHANGED exactly...")
_xi = [Lc(Fr((5 * i + 3) % 11 - 5)) for i in range(d)]
_cob = {g: vsub(matvec(LETS[g], _xi), _xi) for g in GENS_D}
_u0_shift = {g: vadd(classes[0][g], _cob[g]) for g in GENS_D}
_shift_ok = []
for j in (1, 2):
    base_s, _ = base_vec_fast(_u0_shift, classes[j])
    obs_s = obstruction_coords(base_s)
    obs_orig = OBS[(0, j)]
    same = all((obs_s[k] - obs_orig[k]).is_zero() for k in range(len(leftnull)))
    _shift_ok.append(same)
    log(f"  obstruction coords for [c_0{j}] unchanged under coboundary "
        f"shift of class 0: {same}")
gates["control_coboundary_shift"] = all(_shift_ok)
assert gates["control_coboundary_shift"]

gates["control_exactness"] = True
log("  exactness: L = Q(s,i) (Fraction-pairs, s^4=8s^2+16) throughout; zero "
    "floats anywhere in the D3 path: PASS by construction")

# ============================================================================
log("=== STEP G: witnesses for nonzero classes + rank of the pattern ===")


def find_witness(vec):
    for psi in leftnull:
        if not vdot(psi, vec).is_zero():
            return psi
    return None


banked = {}
for (i, j) in nonzero_pairs:
    psi_w = find_witness(BASE[(i, j)])
    val = vdot(psi_w, BASE[(i, j)])
    psiF = [vdot(psi_w, [dual_big[r][c] for r in range(len(dual_big))])
            for c in range(len(dual_big[0]))]
    witness_ok = all(x.is_zero() for x in psiF)
    banked[f"{i}{j}"] = {
        "obstruction_coords": [fmtL(c) for c in OBS[(i, j)]],
        "witness_psi_valid_leftnull_of_F": witness_ok,
        "witness_pairing_value": fmtL(val),
    }
    log(f"  witness [c_{i}{j}]: valid={witness_ok}, psi.BASE={fmtL(val)} "
        f"(nonzero, proves [c_{i}{j}]!=0)")

rank_rows = [[c for c in OBS[(i, j)]] for (i, j) in PAIRS25]
_, rank_piv = rrefL([list(r) for r in rank_rows])
pattern_rank = len(rank_piv)
sym_check = all(ZERO_FLAG[(i, j)] == ZERO_FLAG[(j, i)] for (i, j) in PAIRS25)
log(f"  rank of the 25 obstruction-coordinate vectors in the "
    f"{len(leftnull)}-dim superspace: {pattern_rank}")
log(f"  zero-pattern symmetric under (i,j)<->(j,i): {sym_check}")

# ============================================================================
log("=== STEP H: THE K020 VERDICT -- FORM comparison to golden (C1) ===")
GOLDEN_SOLO_PAIRS_NONZERO = ["23", "24", "32", "34", "42", "43"]
GOLDEN_OFFDIAG_TOTAL = 6
GOLDEN_ALL_OFFDIAG_NONZERO = True

silver_offdiag_total = len(OFFDIAG)
silver_nonzero_frac = f"{len(nonzero_pairs)}/{silver_offdiag_total}"
if len(nonzero_pairs) == 0:
    verdict = "DEGENERATE-ZERO: all off-diagonal silver vector cup classes vanish (unlike golden's all-nonzero pattern) -- FORM-MISMATCH"
    form_match = False
elif len(nonzero_pairs) == silver_offdiag_total:
    verdict = "FORM-MATCH: ALL off-diagonal silver vector cup classes (25-basis, 20 ordered off-diag pairs) are NONZERO, exactly the golden pattern (all-nonzero) generalized to the full unresolved-split basis -- the supra-class coupling is STRUCTURAL"
    form_match = True
else:
    verdict = f"PARTIAL/MIXED ({silver_nonzero_frac} off-diagonal pairs nonzero) -- does not cleanly match golden's all-nonzero pattern; reported as-is, not forced"
    form_match = None

log(f"  golden (C1): {GOLDEN_OFFDIAG_TOTAL}/{GOLDEN_OFFDIAG_TOTAL} solo off-diagonal pairs NONZERO "
    f"(pairs {GOLDEN_SOLO_PAIRS_NONZERO})")
log(f"  silver (D3): {silver_nonzero_frac} off-diagonal pairs (full 5-basis) NONZERO "
    f"(pairs {[f'{i}{j}' for (i,j) in nonzero_pairs]})")
log(f"*** THE K020 VERDICT: {verdict} ***")

# ============================================================================
all_gates_pass = all(v for k, v in gates.items() if isinstance(v, bool))
log(f"ALL GATES PASS: {all_gates_pass}")

result = {
    "prereg_note": "PREREG_L4.md, D3 clause (SILVER VECTOR CUP, K020 on the loop-3 discovery)",
    "object": "m136 (B649 silver holonomy, L=Q(s,i), s^4=8s^2+16), DOUBLE presentation (6 gens abcdef, 6 relators)",
    "gates": gates,
    "double_dims": {"h0": h0_D, "h1": h1_D},
    "dual_dims": {"h0_dual": h0_dual, "h1_dual": h1_dual, "h2_dual_forced": H2_DUAL_DIM},
    "ker_FT_dim": len(leftnull),
    "cubic_source": "REUSED VERBATIM from banked cubic_rational.json (B649's rational Cartan cubic); NOT re-derived. Same object already gated N-invariant under all six letters a..f in w2a_silver.py and b3_silver.py.",
    "split_status": "UNRESOLVED (w2a_silver.py FINDINGS_CC2.md: silver portal is upper-triangular, no canonical alignment with golden's boundary-born/solo-inherited 2+3 split) -- used the FULL 5-basis, all 5x5 (25) ordered pairs including diagonal.",
    "support_pattern_context": split_info,
    "pattern_5x5_zero_bool": [[ZERO_FLAG[(i, j)] for j in range(NCLS)] for i in range(NCLS)],
    "nonvanishing_pairs": [f"{i}{j}" for (i, j) in nonzero_pairs],
    "zero_offdiag_pairs": [f"{i}{j}" for (i, j) in zero_pairs],
    "banked_classes": banked,
    "pattern_rank_in_superspace": pattern_rank,
    "pattern_zero_pattern_symmetric": sym_check,
    "koszul_antisym_cij_plus_cji_zero": gates["cij_plus_cji_zero_all"],
    "diagonal_cii_zero": diag_zero,
    "golden_reference": {
        "nonvanishing_pairs": GOLDEN_SOLO_PAIRS_NONZERO,
        "offdiag_total": GOLDEN_OFFDIAG_TOTAL,
        "all_nonzero": GOLDEN_ALL_OFFDIAG_NONZERO,
        "pattern_rank_in_31dim_superspace": 2,
    },
    "silver_vs_golden_form_comparison": {
        "golden_offdiag_nonzero_fraction": f"{GOLDEN_OFFDIAG_TOTAL}/{GOLDEN_OFFDIAG_TOTAL}",
        "silver_offdiag_nonzero_fraction": silver_nonzero_frac,
        "form_match": form_match,
    },
    "verdict": verdict,
    "all_gates_pass": all_gates_pass,
    "runtime_s": time.time() - T0,
}
with open(os.path.join(HERE, "d3_results.json"), "w") as f:
    json.dump(result, f, indent=2)
log(f"saved {os.path.join(HERE, 'd3_results.json')}")
log("DONE.")
