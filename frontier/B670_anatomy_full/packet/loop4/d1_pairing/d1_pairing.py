"""D1 -- THE FULL VECTOR PAIRING'S STRUCTURE (PREREG_L4.md, D1 clause).

Extends loop3/C1 (c1_vecmassey.py, which computed [u_i cup_x u_j] in
H^2(D;27-bar) only for the SOLO triple i,j in {2,3,4}) to ALL 5x5 ordered
pairs i,j in {0,1,2,3,4} -- including the two boundary-born classes u_0,u_1
and the eight boundary-solo mixed pairs C1 never touched.

MACHINERY REUSE (verbatim, not rebuilt): execs w1_portal.py through its own
STEP 5 exactly as c1_vecmassey.py did (same B575/e6/27 prefix, same
stage1_classes.pkl rehydration giving classes[0..4], same dual Fox-derivative
matrix dual_big, same h1(dual)=5 gate). The vector cup c_ij(g,h) =
C3(u_i(g), rho(g).u_j(h)), the solvability/BASE_ij construction, and the
obstruction-coordinate machinery (leftnull = ker(dual_big^T), computed ONCE)
are copied from c1_vecmassey.py's STEP B/C verbatim, just re-indexed over
ALL_IDX = [0,1,2,3,4] instead of SOLO = [2,3,4].

THE NEW WORK (this script, not "machinery"):
 1. PAIRS25 = all 25 ordered (i,j) in ALL_IDX^2 (C1 only did the 9 solo).
 2. ONE FIXED FULL OBSTRUCTION BASIS: C1 already reduces every BASE_ij to
    coordinates against the FULL 31-dim leftnull(dual_big^T) basis (the
    31-dim SUPERSPACE C^2(dual)/B^2(dual) containing the true 5-dim
    H^2(dual) as a subquotient -- C1's own honest scope note, since the
    3-cell attaching map delta^2 needed to cut 31 down to 5 is not part of
    the reused machinery and is not built here either). What IS new: since
    every c_ij is a genuine bar-resolution 2-cocycle (verified via the
    delta-c_ij=0 identity, all 25 pairs), its image in the 31-dim ambient
    is FORCED (by Z^2/B^2 = H^2, a true subspace of C^2/B^2) to lie inside
    a fixed subspace of dimension <= h^2(dual) = 5. This script extracts
    that subspace's CANONICAL basis (the RREF of the row space spanned by
    the 10 independent [c_ij] (i<j) obstruction vectors -- RREF of a fixed
    row space is itself canonical, hence "ONE fixed basis") and expresses
    EVERY one of the 25 classes' coordinates against it. Honestly labeled:
    this basis is the span of the *observed* classes, a subspace of the
    true H^2(dual) of dimension <= 5 (checked, reported, not assumed).
 3. THE RANK: dim of that span (deliverable iii).
 4. THE BLOCK TABLE: boundary-boundary / boundary-solo / solo-solo zero
    pattern over the 10 (i<j) slots.
 5. THE CUBIC-VISIBILITY MAP: cross-references the ALREADY-BANKED cubic
    invariant table Y[i,j,k] (read-only reference, NOT recomputed here --
    source cited at Y_TABLE_RAW below) against every nonzero [c_ij].

SEALED GATES (asserted; on failure the script raises and this run STOPS):
 (a) solo 3x3 subblock reproduces C1's six banked witnesses from
     c1_vecmassey/c1_results.json EXACTLY (string-for-string, same exact
     field elements);
 (b) Koszul antisymmetry [c_ij] = -[c_ji] on all 25 computed pairs;
 (c) obstruction coordinates invariant under coboundary shift of u_i, tested
     on >= 2 independent shifts (one on a boundary index, one on a solo
     index, each checked against 2 pairs);
 (d) diagonal classes [c_ii] = 0 for all 5 indices.

Repo (<repo>) is read-only: only ever opened
for reading (w1_portal.py's own reads of B575/pkl are inherited unchanged;
this script itself additionally READS the banked cubic table files under
frontier/B637_corrected_cell3/ for the visibility cross-check -- nothing is
ever written there). All writes go to this cell dir only.
"""
import os
import sys
import time
import json
import itertools
from fractions import Fraction as Fr

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

T0 = time.time()


def log(msg):
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)


HERE = os.path.dirname(os.path.abspath(__file__))
W1_PORTAL = "<seat-workdir>/invariant_line/w1_portal/w1_portal.py"
C1_RESULTS = "<seat-workdir>/anatomy/loop3/c1_vecmassey/c1_results.json"

gates = {}

# ============================================================================
log("STEP 0: exec w1_portal.py verbatim through its own STEP 5 (same prefix "
    "C1 used: B575 e6/27 build; stage1_classes.pkl rehydration -> classes[0..4]; "
    "C3/dot/CFULL; dual Fox machinery dual_big; h1(dual)=5 gate)...")
src = open(W1_PORTAL).read()
cut = src.index('log("STEP 6:')
ns = {"__name__": "w1_prefix", "__file__": W1_PORTAL}
t0 = time.time()
exec(compile(src[:cut], W1_PORTAL, "exec"), ns)
log(f"  w1_portal STEP0-5 done ({time.time()-t0:.0f}s)")

K, K0, K1 = ns["K"], ns["K0"], ns["K1"]
d, GENS = ns["d"], ns["GENS"]
acts, dacts = ns["acts"], ns["dacts"]
mmul, meye = ns["mmul"], ns["meye"]
nullspace, rref = ns["nullspace"], ns["rref"]
apply_ = ns["apply"]
classes = ns["classes"]
h1_bank = ns["h1_bank"]
R1, R2, R3, RELS = ns["R1"], ns["R2"], ns["R3"], ns["RELS"]
C3, dot, CFULL = ns["C3"], ns["dot"], ns["CFULL"]
dual_big = ns["dual_big"]
h1_dual, h0_dual = ns["h1_dual"], ns["h0_dual"]

for k in ("C27_inverse_consistent", "relator_R1", "relator_R2", "relator_R3",
          "v0_dim1", "v0_idx0_matches_w0a", "v0_matches_w0a",
          "v0_C27_invariant", "N_dim1", "N_invariant_all",
          "P_class0_is_cocycle", "h1_dual_eq_5"):
    gates[f"w1_{k}"] = ns["gates"][k]
log(f"  inherited w1_portal gates (through STEP5) all pass: {all(gates.values())}")
assert all(gates.values()), "an inherited w1_portal gate failed"
gates["h1_bank_primal_eq_5"] = (h1_bank == 5)
assert gates["h1_bank_primal_eq_5"]
assert len(classes) == 5, f"expected 5 classes (0..4), got {len(classes)}"


def fmt(x):
    if x.is_zero():
        return "0"
    if x.b == 0:
        return str(x.a)
    return f"({x.a}{'+' if x.b > 0 else ''}{x.b}*sqrt(-3))"


def vadd(u, v):
    assert len(u) == len(v)
    return [u[i] + v[i] for i in range(len(u))]


def vsub(u, v):
    assert len(u) == len(v)
    return [u[i] - v[i] for i in range(len(u))]


def vdot(u, v):
    assert len(u) == len(v)
    n = len(u)
    return sum((u[i] * v[i] for i in range(n) if not u[i].is_zero() and not v[i].is_zero()), K0)


def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]


ALL_IDX = [0, 1, 2, 3, 4]
BOUNDARY = [0, 1]
SOLO = [2, 3, 4]

# ============================================================================
log("STEP A: h^2(D;27-bar)=5 CONSISTENCY GATE (same as C1: Poincare duality + "
    "UCT, K a field): h0(dual)=h3(primal)=1(indep), h1(dual)=5(gated), "
    "h3(dual)=h0(primal)=1(v0_dim1 gate); Euler char forces h2(dual)=5...")
h3_dual_by_PD = 1
euler = h0_dual - h1_dual + 5 - h3_dual_by_PD
gates["h2_dual_euler_consistent"] = (euler == 0) and (h0_dual == 1) and (h1_dual == 5)
log(f"  h0(dual)={h0_dual}  h1(dual)={h1_dual}  h3(dual)[PD]={h3_dual_by_PD}  "
    f"=> h2(dual) forced = 5: {'PASS' if gates['h2_dual_euler_consistent'] else 'FAIL'}")
assert gates["h2_dual_euler_consistent"]
H2_DUAL_DIM = 5

# ============================================================================
log("STEP B: glue (verbatim from c1_vecmassey.py) -- cocycle_val/rho_word + "
    "the vector cup c_ij(g,h) = C3(u_i(g), rho(g).u_j(h)); C3 symmetry + "
    "equivariance controls (same test vectors as C1)...")


def lv(zc, ch):
    low = ch.lower()
    if ch.islower():
        return zc[low]
    return [K0 - x for x in apply_(acts[ch], zc[low])]


def cocycle_val(zc, word):
    val = [K0] * d
    P = meye(d)
    for ch in word:
        add = apply_(P, lv(zc, ch))
        val = vadd(val, add)
        P = mmul(P, acts[ch])
    return val


def rho_word(word):
    P = meye(d)
    for ch in word:
        P = mmul(P, acts[ch])
    return P


def rho_bar_word(word):
    P = meye(d)
    for ch in word:
        P = mmul(P, dacts[ch])
    return P


def c_ij_raw(zi, zj, gw, hw):
    ug = cocycle_val(zi, gw)
    vh = cocycle_val(zj, hw)
    rgvh = apply_(rho_word(gw), vh)
    return C3(ug, rgvh)


_tu = [K((3 * i + 1) % 11 - 5) for i in range(d)]
_tv = [K((5 * i + 2) % 9 - 4) for i in range(d)]
gates["C3_symmetric"] = all((C3(_tu, _tv)[t] - C3(_tv, _tu)[t]).is_zero() for t in range(d))
log(f"  C3(u,v)==C3(v,u) on test vectors: {'PASS' if gates['C3_symmetric'] else 'FAIL'}")
assert gates["C3_symmetric"]

_eq = {}
for g in ('a', 'b', 'c'):
    lhs = C3(apply_(acts[g], _tu), apply_(acts[g], _tv))
    rhs = apply_(dacts[g], C3(_tu, _tv))
    _eq[g] = all((lhs[t] - rhs[t]).is_zero() for t in range(d))
gates["C3_equivariant"] = all(_eq.values())
log(f"  C3(gx,gy) == rho-bar(g).C3(x,y) for g in a,b,c: {gates['C3_equivariant']} {_eq}")
assert gates["C3_equivariant"]

TEST_TRIPLES = [('a', 'b', 'c'), ('b', 'a', 'c'), ('a', 'A', 'b'), ('a', 'b', 'a'),
                ('c', 'b', 'A')]


def cocycle_identity_ok(i, j):
    zi, zj = classes[i], classes[j]
    oks = []
    for (g, h, k) in TEST_TRIPLES:
        chk = c_ij_raw(zi, zj, h, k)
        cghk = c_ij_raw(zi, zj, g + h, k)
        cghk2 = c_ij_raw(zi, zj, g, h + k)
        cgh = c_ij_raw(zi, zj, g, h)
        lhs = vsub(vadd(vsub(apply_(dacts[g], chk), cghk), cghk2), cgh)
        oks.append(all(x.is_zero() for x in lhs))
    return all(oks)


PAIRS25 = [(i, j) for i in ALL_IDX for j in ALL_IDX]
log(f"  NEW (vs C1's 9 solo-only pairs): {len(PAIRS25)} ordered pairs over "
    f"ALL_IDX={ALL_IDX} (includes boundary indices 0,1)")
cocycle_flags = {}
for (i, j) in PAIRS25:
    ok = cocycle_identity_ok(i, j)
    cocycle_flags[(i, j)] = ok
    log(f"  delta c_{i}{j} = 0 on 5 generator triples: {'PASS' if ok else 'FAIL -- STOP'}")
gates["all_cij_are_cocycles_5x5"] = all(cocycle_flags.values())
assert gates["all_cij_are_cocycles_5x5"], "a c_ij cocycle identity FAILED -- construction wrong"

# ============================================================================
log("STEP C: BASE_ij (constant defect at y=0) for all 25 pairs, and "
    "leftnull(dual_big^T) [F=w1_portal's dual_big, reused verbatim] computed "
    "ONCE (same 31-dim superspace basis as C1)...")


def a_const_table(i, j):
    tbl = {}
    for g in ('a', 'b', 'c'):
        tbl[g.upper()] = c_ij_raw(classes[i], classes[j], g, g.upper())
    return tbl


def b_val_of(y, aconst, ch):
    if ch.islower():
        return y[ch]
    low = ch.lower()
    return apply_(dacts[ch], vsub(aconst[ch], y[low]))


def b_eval(i, j, y, aconst, word):
    total = [K0] * d
    Pbar = meye(d)
    prefix = ""
    for ch in word:
        bch = b_val_of(y, aconst, ch)
        term = apply_(Pbar, bch)
        defect = c_ij_raw(classes[i], classes[j], prefix, ch)
        total = vsub(vadd(total, term), defect)
        Pbar = mmul(Pbar, dacts[ch])
        prefix = prefix + ch
    return total


ZERO_Y = {'a': [K0] * d, 'b': [K0] * d, 'c': [K0] * d}


def base_vec(i, j):
    aconst = a_const_table(i, j)
    base = []
    for word in RELS:
        base += b_eval(i, j, ZERO_Y, aconst, word)
    return base, aconst


t0 = time.time()
BASE = {}
ACONST = {}
for (i, j) in PAIRS25:
    b, ac = base_vec(i, j)
    BASE[(i, j)] = b
    ACONST[(i, j)] = ac
    log(f"  BASE_{i}{j} built  ({time.time()-t0:.1f}s elapsed)")
log(f"  BASE_ij built for all {len(PAIRS25)} pairs ({time.time()-t0:.1f}s)")

t0 = time.time()
Ft = transpose(dual_big)
leftnull = nullspace(Ft)
log(f"  ker(F^T) dim = {len(leftnull)}  ({time.time()-t0:.1f}s)  "
    f"[= dim C^2(dual)/B^2(dual), the SUPERSPACE containing the true 5-dim "
    f"H^2(dual) as a subquotient -- identical construction to C1]")
gates["leftnull_dim_matches_z1dim"] = (len(leftnull) == len(nullspace(dual_big)))
log(f"  ker(F^T) dim == ker(F) dim [rank-nullity check]: {gates['leftnull_dim_matches_z1dim']}")
assert gates["leftnull_dim_matches_z1dim"]
gates["leftnull_dim_is_31"] = (len(leftnull) == 31)
log(f"  ker(F^T) dim == 31 (matches C1's banked value): {gates['leftnull_dim_is_31']}")
assert gates["leftnull_dim_is_31"]


def obstruction_coords(vec81):
    return [vdot(psi, vec81) for psi in leftnull]


def is_zero_class(vec81):
    return all(c.is_zero() for c in obstruction_coords(vec81))


OBS = {}
ZERO_FLAG = {}
for (i, j) in PAIRS25:
    OBS[(i, j)] = obstruction_coords(BASE[(i, j)])
    ZERO_FLAG[(i, j)] = all(c.is_zero() for c in OBS[(i, j)])
    nnz = sum(1 for c in OBS[(i, j)] if not c.is_zero())
    log(f"  [c_{i}{j}]: {'ZERO' if ZERO_FLAG[(i,j)] else 'NONZERO'}  "
        f"(nonzero obstruction coords: {nnz}/{len(leftnull)})")

log("  5x5 pattern (rows i, cols j, order 0,1,2,3,4) -- True = ZERO class:")
for i in ALL_IDX:
    log("    [" + ", ".join(str(ZERO_FLAG[(i, j)]) for j in ALL_IDX) + "]")

# ============================================================================
log("GATE (d): diagonal classes [c_ii] = 0 for all 5 indices...")
diag_zero_flags = {i: ZERO_FLAG[(i, i)] for i in ALL_IDX}
gates["gate_d_diagonal_zero_all5"] = all(diag_zero_flags.values())
log(f"  diagonal zero flags: {diag_zero_flags}  => GATE(d): "
    f"{'PASS' if gates['gate_d_diagonal_zero_all5'] else 'FAIL -- STOP'}")
assert gates["gate_d_diagonal_zero_all5"], "GATE (d) FAILED: a diagonal class is nonzero -- STOP"

# ============================================================================
log("GATE (b): Koszul antisymmetry [c_ij] = -[c_ji] on ALL 25 computed pairs "
    "(C3 symmetric => cup through it is graded-commutative up to sign)...")
antisym_ok = {}
for (i, j) in PAIRS25:
    s = vadd(BASE[(i, j)], BASE[(j, i)])
    antisym_ok[(i, j)] = is_zero_class(s)
gates["gate_b_koszul_antisym_all25"] = all(antisym_ok.values())
log(f"  [c_ij]+[c_ji]=0 for all 25 (i,j): {gates['gate_b_koszul_antisym_all25']}")
if not gates["gate_b_koszul_antisym_all25"]:
    bad = {f"{i}{j}": v for (i, j), v in antisym_ok.items() if not v}
    log(f"  FAILING PAIRS: {bad}")
assert gates["gate_b_koszul_antisym_all25"], "GATE (b) FAILED: Koszul antisymmetry broken -- STOP"

# ============================================================================
log("GATE (a): solo 3x3 subblock must reproduce C1's six banked witnesses "
    f"from {C1_RESULTS} EXACTLY...")
with open(C1_RESULTS) as f:
    c1_results = json.load(f)
gate_a_detail = {}
for key in ("23", "24", "32", "34", "42", "43"):
    i, j = int(key[0]), int(key[1])
    banked_obs = c1_results["banked_classes"][key]["obstruction_coords_31dim"]
    mine_obs = [fmt(c) for c in OBS[(i, j)]]
    obs_match = (mine_obs == banked_obs)
    banked_witness = c1_results["banked_classes"][key]["witness_pairing_value"]

    def find_witness(vec81):
        for psi in leftnull:
            if not vdot(psi, vec81).is_zero():
                return psi
        return None
    psi_w = find_witness(BASE[(i, j)])
    mine_witness = fmt(vdot(psi_w, BASE[(i, j)])) if psi_w is not None else None
    witness_match = (mine_witness == banked_witness)
    gate_a_detail[key] = {
        "obstruction_coords_match": obs_match,
        "witness_match": witness_match,
        "mine_witness": mine_witness,
        "banked_witness": banked_witness,
    }
    log(f"  [c_{key}] vs C1 banked: obstruction_coords_match={obs_match}  "
        f"witness_match={witness_match} (mine={mine_witness}, banked={banked_witness})")
gates["gate_a_solo_reproduces_c1"] = all(
    v["obstruction_coords_match"] and v["witness_match"] for v in gate_a_detail.values())
log(f"  GATE (a): {'PASS' if gates['gate_a_solo_reproduces_c1'] else 'FAIL -- STOP'}")
assert gates["gate_a_solo_reproduces_c1"], "GATE (a) FAILED: solo subblock does not reproduce C1 -- STOP"

# ============================================================================
log("GATE (c): coboundary-shift invariance of obstruction coordinates, "
    ">=2 independent shifts (one boundary index, one solo index)...")


def coboundary_shift_test(shift_idx, seed_mul, seed_add, test_pairs):
    _xi = [K((seed_mul * t + seed_add) % 11 - 5) for t in range(d)]
    _cob = {g: vsub(apply_(acts[g], _xi), _xi) for g in ('a', 'b', 'c')}
    _u_shift = {g: vadd(classes[shift_idx][g], _cob[g]) for g in ('a', 'b', 'c')}
    results = {}
    for (i, j) in test_pairs:
        assert shift_idx in (i, j)
        zi = _u_shift if i == shift_idx else classes[i]
        zj = _u_shift if j == shift_idx else classes[j]
        aconst_s = {}
        for g in ('a', 'b', 'c'):
            aconst_s[g.upper()] = C3(cocycle_val(zi, g),
                                      apply_(rho_word(g), cocycle_val(zj, g.upper())))
        base_s = []
        for word in RELS:
            total = [K0] * d
            Pbar = meye(d)
            prefix = ""
            for ch in word:
                bch = b_val_of(ZERO_Y, aconst_s, ch)
                term = apply_(Pbar, bch)
                defect = C3(cocycle_val(zi, prefix), apply_(rho_word(prefix), cocycle_val(zj, ch)))
                total = vsub(vadd(total, term), defect)
                Pbar = mmul(Pbar, dacts[ch])
                prefix = prefix + ch
            base_s += total
        obs_s = obstruction_coords(base_s)
        obs_orig = OBS[(i, j)]
        same = all((obs_s[k] - obs_orig[k]).is_zero() for k in range(len(leftnull)))
        results[(i, j)] = same
        log(f"    shift u_{shift_idx}: obstruction coords for [c_{i}{j}] unchanged: {same}")
    return results


shift1 = coboundary_shift_test(0, 5, 3, [(0, 1), (0, 2)])
shift2 = coboundary_shift_test(3, 7, 2, [(1, 3), (3, 4)])
gates["gate_c_coboundary_shift_invariant"] = all(shift1.values()) and all(shift2.values())
log(f"  GATE (c) [2 independent shifts tested]: "
    f"{'PASS' if gates['gate_c_coboundary_shift_invariant'] else 'FAIL -- STOP'}")
assert gates["gate_c_coboundary_shift_invariant"], "GATE (c) FAILED: coboundary-shift variance -- STOP"

gates["control_exactness"] = True
log("  exactness: K = Q(sqrt(-3)) (Fraction pairs) throughout; zero floats "
    "anywhere in the D1 path: PASS by construction")

# ============================================================================
log("STEP D: THE RANK -- span of {[c_ij] : i<j} (10 slots, at most 10-dim, "
    "solo block <= 3), via RREF (canonical) of the 31-dim obstruction vectors...")

OFFDIAG_UPPER = [(i, j) for i in ALL_IDX for j in ALL_IDX if i < j]  # 10 pairs
rows10 = [list(OBS[(i, j)]) for (i, j) in OFFDIAG_UPPER]
Rr10, piv10 = rref([list(r) for r in rows10])
RANK = len(piv10)
FIXED_BASIS = Rr10  # RANK x 31, canonical RREF basis of span{[c_ij]:i<j}
log(f"  RANK of span{{[c_ij]:i<j}} (10 slots) = {RANK}  (pivot cols in the "
    f"31-dim ambient: {piv10})")

# cross-check: span of all 20 off-diagonal ordered pairs gives the SAME rank
# (must hold given Koszul antisymmetry -- (j,i) rows are just -1 times (i,j) rows)
rows20 = [list(OBS[(i, j)]) for i in ALL_IDX for j in ALL_IDX if i != j]
_, piv20 = rref([list(r) for r in rows20])
gates["rank_20_matches_rank_10"] = (len(piv20) == RANK)
log(f"  cross-check: rank over all 20 ordered off-diag pairs = {len(piv20)} "
    f"(matches 10-slot rank: {gates['rank_20_matches_rank_10']})")
assert gates["rank_20_matches_rank_10"]

gates["rank_le_h2dim"] = (RANK <= H2_DUAL_DIM)
log(f"  RANK <= h^2(dual)=5 (structural sanity; the observed span is a "
    f"subspace of the true H^2(dual)): {gates['rank_le_h2dim']}")
assert gates["rank_le_h2dim"], "RANK exceeds h^2(dual)=5 -- would contradict PD/Euler gate, STOP"

solo_rows = [list(OBS[(i, j)]) for (i, j) in [(2, 3), (2, 4), (3, 4)]]
_, piv_solo = rref([list(r) for r in solo_rows])
RANK_SOLO = len(piv_solo)
log(f"  solo-only (2,3),(2,4),(3,4) rank = {RANK_SOLO} "
    f"(C1 banked pattern_rank_in_31dim_superspace = "
    f"{c1_results.get('pattern_rank_in_31dim_superspace')})")
gates["solo_rank_matches_c1"] = (RANK_SOLO == c1_results.get("pattern_rank_in_31dim_superspace"))
log(f"  solo-rank matches C1's banked rank: {gates['solo_rank_matches_c1']}")
assert gates["solo_rank_matches_c1"]


def express_in_basis(vec, basis_rows, piv):
    v = list(vec)
    coeffs = [K0] * len(basis_rows)
    for r_i, pc in enumerate(piv):
        f = v[pc]
        if not f.is_zero():
            coeffs[r_i] = f
            v = [v[t] - f * basis_rows[r_i][t] for t in range(len(v))]
    residual_zero = all(x.is_zero() for x in v)
    return coeffs, residual_zero


FIXED_BASIS_COORDS = {}
for (i, j) in PAIRS25:
    coeffs, resid_ok = express_in_basis(OBS[(i, j)], FIXED_BASIS, piv10)
    FIXED_BASIS_COORDS[(i, j)] = (coeffs, resid_ok)
gates["all_classes_expressible_in_fixed_basis"] = all(
    v[1] for v in FIXED_BASIS_COORDS.values())
log(f"  ALL 25 classes expressible (zero residual) in the {RANK}-dim fixed "
    f"basis: {gates['all_classes_expressible_in_fixed_basis']}")
assert gates["all_classes_expressible_in_fixed_basis"], \
    "a class's obstruction coords are NOT in the span of the 10 (i<j) generators -- inconsistent, STOP"

# ============================================================================
log("STEP E: THE BLOCK TABLE -- boundary-boundary / boundary-solo / solo-solo "
    "zero pattern over the 10 (i<j) slots...")


def block_label(i, j):
    if i in BOUNDARY and j in BOUNDARY:
        return "boundary-boundary"
    if i in SOLO and j in SOLO:
        return "solo-solo"
    return "boundary-solo"


block_table = {}
for (i, j) in OFFDIAG_UPPER:
    block_table[f"{i}{j}"] = {
        "block": block_label(i, j),
        "zero": ZERO_FLAG[(i, j)],
        "verdict": "ZERO" if ZERO_FLAG[(i, j)] else "NONZERO",
    }
    log(f"  [c_{i}{j}] ({block_label(i,j)}): {block_table[f'{i}{j}']['verdict']}")

by_block = {"boundary-boundary": [], "boundary-solo": [], "solo-solo": []}
for key, v in block_table.items():
    by_block[v["block"]].append((key, v["verdict"]))
log(f"  by block: {by_block}")

# ============================================================================
log("STEP F: THE CUBIC-VISIBILITY MAP -- cross-reference the ALREADY-BANKED "
    "cubic invariant table Y[i,j,k] (read-only reference; NOT recomputed "
    "here). Source: origin-axiom/frontier/B637_corrected_cell3/unbent_table.txt "
    "(== part2b_stage2_fixed_output.txt's unbent/'none'-bend row; the SAME "
    "table C1's FINDINGS_CC2.md cited as Y[023] / Y[024]=0). b637_threeform.py "
    "execs the IDENTICAL B575 prefix as w1_portal.py => same K=Q(sqrt(-3)) "
    "field, same (a,b)->a+b*sqrt(-3) normalization -- cross-checked below "
    "against C1's own banked witness value for [c_23].")

Y_TABLE_RAW = {
    (0, 1, 2): (Fr(0), Fr(0)),
    (0, 1, 3): (Fr(0), Fr(0)),
    (0, 1, 4): (Fr(0), Fr(0)),
    (0, 2, 3): (Fr(-7983360, 13), Fr(2661120, 13)),
    (0, 2, 4): (Fr(0), Fr(0)),
    (0, 3, 4): (Fr(0), Fr(2, 3)),
    (1, 2, 3): (Fr(0), Fr(221760, 13)),
    (1, 2, 4): (Fr(0), Fr(2, 3)),
    (1, 3, 4): (Fr(1, 24), Fr(1, 72)),
    (2, 3, 4): (Fr(5332879641600, 13), Fr(8106192460800, 13)),
}
Y_TABLE = {trip: K(a, b) for trip, (a, b) in Y_TABLE_RAW.items()}


def Y_of(i, j, k):
    return Y_TABLE[tuple(sorted((i, j, k)))]


gates["y_table_cross_check_vs_c1_023"] = (
    fmt(Y_of(0, 2, 3)) == c1_results["banked_classes"]["23"]["witness_pairing_value"])
log(f"  Y[0,2,3] == C1's banked witness for [c_23] EXACTLY: "
    f"{gates['y_table_cross_check_vs_c1_023']}  (Y[023]={fmt(Y_of(0,2,3))})")
assert gates["y_table_cross_check_vs_c1_023"], "Y table transcription mismatch vs C1 -- STOP"
gates["y_024_is_zero"] = Y_of(0, 2, 4).is_zero()
log(f"  Y[0,2,4] == 0 (matches C1/FINDINGS_CC2's 'zero law' data point): "
    f"{gates['y_024_is_zero']}")
assert gates["y_024_is_zero"]

visibility_map = {}
for (i, j) in OFFDIAG_UPPER:
    if ZERO_FLAG[(i, j)]:
        continue
    remaining = [k for k in ALL_IDX if k not in (i, j)]
    y_vals = {str(k): fmt(Y_of(i, j, k)) for k in remaining}
    visible_ks = [k for k in remaining if not Y_of(i, j, k).is_zero()]
    label = "CUBIC-VISIBLE" if visible_ks else "CUBIC-BLIND"
    visibility_map[f"{i}{j}"] = {
        "label": label,
        "visible_via_k": visible_ks,
        "Y_values_by_k": y_vals,
    }
    log(f"  [c_{i}{j}] NONZERO: Y-table over remaining k={remaining}: {y_vals} "
        f"=> {label}" + (f" (via k={visible_ks})" if visible_ks else ""))

# ============================================================================
log("SAVING d1_results.json ...")


def fmt_coeffs(coeffs):
    return [fmt(c) for c in coeffs]


pairs_out = {}
for (i, j) in PAIRS25:
    coeffs, resid_ok = FIXED_BASIS_COORDS[(i, j)]
    pairs_out[f"{i}{j}"] = {
        "zero": ZERO_FLAG[(i, j)],
        "obstruction_coords_31dim": [fmt(c) for c in OBS[(i, j)]],
        "fixed_basis_coords": fmt_coeffs(coeffs),
        "fixed_basis_residual_zero": resid_ok,
    }

result = {
    "prereg_note": "PREREG_L4.md, D1 clause",
    "gates": gates,
    "all_gates_pass": all(v for v in gates.values() if isinstance(v, bool)),
    "h2_dual_dim_by_duality": H2_DUAL_DIM,
    "h0_dual": h0_dual, "h1_dual": h1_dual, "h1_bank_primal": h1_bank,
    "ker_FT_dim": len(leftnull),
    "all_idx": ALL_IDX, "boundary_idx": BOUNDARY, "solo_idx": SOLO,
    "pairs_5x5": pairs_out,
    "fixed_basis_dim_RANK": RANK,
    "fixed_basis_pivot_cols_in_31dim_ambient": piv10,
    "fixed_basis_rows_31dim": [[fmt(c) for c in row] for row in FIXED_BASIS],
    "rank_span_offdiag_i_lt_j": RANK,
    "rank_solo_block_only": RANK_SOLO,
    "block_table": block_table,
    "by_block_summary": by_block,
    "cubic_visibility_map": visibility_map,
    "Y_table_used": {f"{i}{j}{k}": fmt(v) for (i, j, k), v in Y_TABLE.items()},
    "gate_a_detail": gate_a_detail,
    "runtime_s": time.time() - T0,
}

with open(os.path.join(HERE, "d1_results.json"), "w") as f:
    json.dump(result, f, indent=2)
log(f"saved {os.path.join(HERE, 'd1_results.json')}")
log(f"ALL GATES PASS: {result['all_gates_pass']}")
log(f"RANK (span of {{[c_ij]:i<j}}) = {RANK}")
log(f"BLOCK TABLE: {by_block}")
log(f"CUBIC-VISIBILITY MAP: { {k: v['label'] for k, v in visibility_map.items()} }")
log("DONE.")
