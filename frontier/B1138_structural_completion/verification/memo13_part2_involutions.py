#!/usr/bin/env python3
"""INDEPENDENT VERIFICATION -- golden_gate memo 13 "THE Y-SELECTION", PART 2: the gauge
closing's action on the 18 hypercharge directions (the factor-preserving involutions,
sign lifts, slot signatures, and the Cartan action giving anti/fixed Y-sets).

Own-authored code throughout. certificates/g1_yselect.py, g1_followup.py,
g1_followup2.py read for SPEC ONLY (never imported/copied). The group-theoretic /
sign-lift / slot-signature MACHINERY (Aut(Phi) BFS, GF(2) involutive-lift solver,
per-slot signature via nullspace+form) follows the SAME well-defined, standard
procedure already independently built, verified and BANKED on main in
frontier/B1135_gauge_closing/verify_gauge_closing.py (itself an independent
verification of this repo's own memo 12) -- re-typed fresh here (not imported as a
running module), same discipline B1135 itself used relative to B1134. Only
frontier/B1102_exact_hypercharge_solve/e6_bracket_vendored.py is imported.

Loads PART 1 (the 18 directions, the slots, the 27, the W(S1)xW(S2) orbits) by
re-running that script's setup in this process (chained, not duplicated by hand).
"""
import importlib.util, itertools, os, time, json, sys
from fractions import Fraction as Q
from collections import Counter
import sympy as sp

T0 = time.time()
def log(m): print(f"[{time.time()-T0:7.2f}s] {m}", flush=True)

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- chain PART 1's setup (own script, same directory) up to the orbit computation ----
part1_src = open(os.path.join(HERE, "memo13_part1_core.py")).read()
cut = part1_src.index("# ---------------------------------------------------------------- save state")
exec(compile(part1_src[:cut], "memo13_part1_core.py", "exec"))
log("PART 1 setup chained in-process: 18 sols, O1/O2 orbits, S0/S1/S2, cor basis ready")

# ============================================================ Aut(Phi(E6)) = W u dW
log("PART 2a: W(E6) via own BFS reflection closure + own diagram-flip search")

def simple_reflection_perm(i):
    ai = SIMPLE[i]
    perm = [0] * NR
    for k, r in enumerate(ROOTS):
        c = iprr(r, ai)
        rr = tuple(r[t] - c * ai[t] for t in range(N))
        perm[k] = IDX[rr]
    return tuple(perm)

GENS = [simple_reflection_perm(i) for i in range(N)]
IDENT = tuple(range(NR))

def compose(p, q):
    return tuple(p[q[i]] for i in range(NR))

def closure(seed_gens):
    seen = {IDENT}
    frontier = [IDENT]
    elems = [IDENT]
    while frontier:
        nxt = []
        for p in frontier:
            for g in seed_gens:
                r = compose(p, g)
                if r not in seen:
                    seen.add(r)
                    nxt.append(r)
                    elems.append(r)
        frontier = nxt
    return elems, seen

W_list, W_set = closure(GENS)
log(f"  |W(E6)| = {len(W_list)} (textbook 51840)")
assert len(W_list) == 51840

diagram_autos = []
for perm in itertools.permutations(range(N)):
    if all(CARTAN[perm[i]][perm[j]] == CARTAN[i][j] for i in range(N) for j in range(N)):
        diagram_autos.append(perm)
assert len(diagram_autos) == 2
PI = next(p for p in diagram_autos if p != tuple(range(N)))
PI_INV = [0] * N
for i in range(N):
    PI_INV[PI[i]] = i

def apply_diagram_flip_to_root(r):
    return tuple(r[PI_INV[k]] for k in range(N))

flip_images = [apply_diagram_flip_to_root(r) for r in ROOTS]
assert all(im in IDX for im in flip_images)
DELTA = tuple(IDX[im] for im in flip_images)
assert compose(DELTA, DELTA) == IDENT and DELTA not in W_set

AUT_list = list(W_list) + [compose(DELTA, w) for w in W_list]
AUT_inW = [True] * len(W_list) + [False] * len(W_list)
assert len(AUT_list) == 103680
log(f"  |Aut(Phi(E6))| = {len(AUT_list)} (own diagram flip {PI})")

# ============================================================ factor-preserving involutions
log("PART 2b: factor-preserving involutions (own search)")
SLOT_IDX = [frozenset(IDX[r] for r in S) for S in (S0, S1, S2)]

def image_idx(perm, idxset):
    return frozenset(perm[i] for i in idxset)

FP = []
for g, inW in zip(AUT_list, AUT_inW):
    if all(image_idx(g, SLOT_IDX[i]) == SLOT_IDX[i] for i in range(3)):
        if compose(g, g) == IDENT:
            FP.append((g, inW))
n_inW = sum(1 for _, inW in FP if inW)
log(f"  factor-preserving involutions: {len(FP)}  ({n_inW} in W, {len(FP)-n_inW} in dW)  "
    f"(B1135 banked: 128 = 64+64)")
assert len(FP) == 128 and n_inW == 64

# ============================================================ GF(2) sign-lift solver (own)
log("PART 2c: GF(2) involutive sign-lift solver (own true-RREF implementation)")
NEGIDX = {k: IDX[tuple(-x for x in r)] for k, r in enumerate(ROOTS)}
NEG = tuple(NEGIDX[k] for k in range(NR))

def build_lift_rows(phi):
    rows = []
    def add(bits, rhs):
        m = 0
        for b in bits:
            m ^= (1 << b)
        rows.append((m, rhs))
    for ridx in range(NR):
        add((ridx, NEGIDX[ridx]), 0)
        add((ridx, phi[ridx]), 0)
    for a_idx in range(NR):
        ra = ROOTS[a_idx]
        for b_idx in range(a_idx + 1, NR):
            rb = ROOTS[b_idx]
            s = tuple(ra[t] + rb[t] for t in range(N))
            if s in IDX:
                pa, pb = ROOTS[phi[a_idx]], ROOTS[phi[b_idx]]
                ratio = EPS(ra, rb) * EPS(pa, pb)
                add((a_idx, b_idx, IDX[s]), 0 if ratio == 1 else 1)
    return rows

def solve_signed_lift(phi):
    rows = build_lift_rows(phi)
    pivots = {}
    def reduce_fully(mask, rhs):
        prev = None
        while mask != prev:
            prev = mask
            for col, (pm, pr) in pivots.items():
                if (mask >> col) & 1:
                    mask ^= pm
                    rhs ^= pr
        return mask, rhs
    for mask, rhs in rows:
        mask, rhs = reduce_fully(mask, rhs)
        if mask == 0:
            if rhs:
                return None
            continue
        newcol = mask.bit_length() - 1
        pivots[newcol] = (mask, rhs)
        for col in list(pivots):
            if col == newcol:
                continue
            pm, pr = pivots[col]
            if (pm >> newcol) & 1:
                pivots[col] = (pm ^ mask, pr ^ rhs)
    pivot_cols = set(pivots)
    free_cols = [c for c in range(NR) if c not in pivot_cols]
    if len(free_cols) > 16:
        raise RuntimeError(f"implausible kernel dim {len(free_cols)}")
    particular = 0
    for col, (mask, rhs) in pivots.items():
        if rhs:
            particular |= (1 << col)
    kernel = []
    for fc in free_cols:
        v = 1 << fc
        for col, (mask, rhs) in pivots.items():
            if (mask >> fc) & 1:
                v |= (1 << col)
        kernel.append(v)
    def satisfies(x):
        return all(bin(mask & x).count("1") % 2 == rhs for mask, rhs in rows)
    assert satisfies(particular)
    for kv in kernel:
        assert satisfies(particular ^ kv)
    return particular, kernel

def all_lift_solutions(phi):
    res = solve_signed_lift(phi)
    if res is None:
        return []
    particular, kernel = res
    sols_ = []
    for bits in range(1 << len(kernel)):
        x = particular
        for j in range(len(kernel)):
            if (bits >> j) & 1:
                x ^= kernel[j]
        sols_.append(x)
    return sols_

antipodal_all = all_lift_solutions(NEG)
log(f"  antipodal control: {len(antipodal_all)} involutive sign solutions "
    f"(expect 64=2^6, matches B1134/B1135's own control)")
assert len(antipodal_all) == 64 and len(set(antipodal_all)) == 64

# ============================================================ invariant compact form G
log("PART 2d: the compact-form signs (spot-checked ad-invariance -- the sign convention "
    "G(e_r,e_-r)=-1 was already exhaustively re-derived independently in banked B1135; "
    "spot-checked here, not re-proved from scratch, to keep this run fast)")
DIM_ = DIM

def make_G(c_root_pair):
    G = [[Q(0)] * DIM_ for _ in range(DIM_)]
    for i in range(N):
        for j in range(N):
            G[i][j] = Q(CARTAN[i][j])
    for k in range(NR):
        G[N + k][N + NEGIDX[k]] = Q(c_root_pair)
    return G

def Gdot(G, u, v):
    s = Q(0)
    for i, ui in enumerate(u):
        if not ui:
            continue
        Gi = G[i]
        for j, vj in enumerate(v):
            if vj and Gi[j]:
                s += ui * vj * Gi[j]
    return s

def ad_invariance_defect_count(G, triples):
    bad = 0
    for x, y, z in triples:
        lhs = BR(x, y)
        lhs = [Q(a.numerator, a.denominator) for a in lhs]
        yq = [Q(a.numerator, a.denominator) for a in y]
        zq = [Q(a.numerator, a.denominator) for a in z]
        xq = [Q(a.numerator, a.denominator) for a in x]
        img = BR(x, z)
        img = [Q(a.numerator, a.denominator) for a in img]
        if Gdot(G, lhs, zq) + Gdot(G, yq, img) != 0:
            bad += 1
    return bad

basis_vecs = [HVEC(i) for i in range(N)] + [EVEC(r) for r in ROOTS]
import random
rng = random.Random(20260822)
spot_triples = [(basis_vecs[rng.randrange(DIM_)], basis_vecs[rng.randrange(DIM_)],
                  basis_vecs[rng.randrange(DIM_)]) for _ in range(4000)]
G_minus = make_G(-1)
bad_minus = ad_invariance_defect_count(G_minus, spot_triples)
log(f"  c=-1 spot check: {bad_minus} ad-invariance failures / {len(spot_triples)} random triples")
assert bad_minus == 0
G = G_minus
Gneg = [[-x for x in row] for row in G]
log("  G(e_r,e_-r)=-1 spot-confirmed ad-invariant")

# ============================================================ slot signature (own, generalized)
log("PART 2e: per-slot signature machinery (own nullspace + signature code)")
SLOTS = [S0, S1, S2]
SLOT_PAIRS = [(a0, a2), p1, p2]

def cartan_coord_vec(root_tuple):
    v = [Q(0)] * DIM_
    for k in range(N):
        v[k] = Q(root_tuple[k])
    return v

SLOT_BASES = []
for i in range(3):
    r1, s1 = SLOT_PAIRS[i]
    basis_i = [EVEC(r) for r in sorted(SLOTS[i])] + [cartan_coord_vec(r1), cartan_coord_vec(s1)]
    assert len(basis_i) == 8
    SLOT_BASES.append(basis_i)

def to_Qvec(v):
    return [Q(a.numerator, a.denominator) for a in v]

def build_theta(phi, sign_bits):
    theta = {}
    for i in range(N):
        img_root = ROOTS[phi[IDX[SIMPLE[i]]]]
        theta[i] = {k: Q(img_root[k]) for k in range(N) if img_root[k]}
    for r_idx in range(NR):
        c = -1 if (sign_bits >> r_idx) & 1 else 1
        theta[N + r_idx] = {N + phi[r_idx]: Q(c)}
    return theta

def sp_apply(theta, sparse_vec):
    out = {}
    for i, ci in sparse_vec.items():
        for k, v in theta[i].items():
            out[k] = out.get(k, 0) + ci * v
    return {k: v for k, v in out.items() if v != 0}

def dense_to_sparse(v):
    return {i: c for i, c in enumerate(v) if c}

def theta_dense(theta, v):
    sv = sp_apply(theta, dense_to_sparse(v))
    out = [Q(0)] * DIM_
    for i, c in sv.items():
        out[i] = c
    return out

def dense_nullspace(cols, nrows):
    ncols = len(cols)
    M = [[cols[c][r] for c in range(ncols)] for r in range(nrows)]
    piv_cols = []
    r = 0
    for c in range(ncols):
        pr = None
        for i in range(r, nrows):
            if M[i][c] != 0:
                pr = i
                break
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        inv = Q(1) / M[r][c]
        if inv != 1:
            M[r] = [x * inv for x in M[r]]
        for i in range(nrows):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                Mr = M[r]
                M[i] = [xi - f * xc if xc else xi for xi, xc in zip(M[i], Mr)]
        piv_cols.append(c)
        r += 1
        if r == nrows:
            break
    piv_set = set(piv_cols)
    free_cols = [c for c in range(ncols) if c not in piv_set]
    basis = []
    for fc in free_cols:
        v = [Q(0)] * ncols
        v[fc] = Q(1)
        for i, pc in enumerate(piv_cols):
            if M[i][fc] != 0:
                v[pc] = -M[i][fc]
        basis.append(v)
    return basis

def signature_of_symmetric(vecs, form):
    n = len(vecs)
    Mg = [[Gdot(form, vecs[a], vecs[b]) for b in range(n)] for a in range(n)]
    p = ng = z = 0
    i = 0
    while i < n:
        if Mg[i][i] == 0:
            j = None
            for jj in range(i + 1, n):
                if Mg[jj][i] != 0:
                    j = jj
                    break
            if j is None:
                z += 1
                i += 1
                continue
            for k in range(n):
                Mg[i][k] += Mg[j][k]
            for k in range(n):
                Mg[k][i] += Mg[k][j]
        d = Mg[i][i]
        if d > 0:
            p += 1
        else:
            ng += 1
        for j in range(i + 1, n):
            if Mg[j][i] != 0:
                f = Mg[j][i] / d
                for k in range(n):
                    Mg[j][k] -= f * Mg[i][k]
                for k in range(n):
                    Mg[k][j] -= f * Mg[k][i]
        i += 1
    return p, ng, z

def solve_coords(v, span_cols):
    k = len(span_cols)
    M = [[span_cols[c][r] for c in range(k)] + [v[r]] for r in range(DIM_)]
    piv_cols = []
    r = 0
    for c in range(k):
        pr = None
        for i in range(r, DIM_):
            if M[i][c] != 0:
                pr = i
                break
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        inv = Q(1) / M[r][c]
        if inv != 1:
            M[r] = [x * inv for x in M[r]]
        for i in range(DIM_):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                Mr = M[r]
                M[i] = [xi - f * xc if xc else xi for xi, xc in zip(M[i], Mr)]
        piv_cols.append(c)
        r += 1
        if r == k:
            break
    coeffs = [Q(0)] * k
    for i, pc in enumerate(piv_cols):
        coeffs[pc] = M[i][k]
    rebuilt = [Q(0)] * DIM_
    for c in range(k):
        if coeffs[c]:
            cc = coeffs[c]
            col = span_cols[c]
            for row in range(DIM_):
                if col[row]:
                    rebuilt[row] += cc * col[row]
    if rebuilt != v:
        raise ValueError("vector escaped the span")
    return coeffs

def to_full(coeffs, span_cols):
    out = [Q(0)] * DIM_
    for c, coef in enumerate(coeffs):
        if coef:
            col = span_cols[c]
            for row in range(DIM_):
                if col[row]:
                    out[row] += coef * col[row]
    return out

def slot_signature(theta, slot_i):
    basis = SLOT_BASES[slot_i]
    try:
        tc_cols = [solve_coords(theta_dense(theta, v), basis) for v in basis]
    except ValueError:
        return False, None
    Tm = [[tc_cols[c][r] - (Q(1) if r == c else Q(0)) for r in range(8)] for c in range(8)]
    Tp = [[tc_cols[c][r] + (Q(1) if r == c else Q(0)) for r in range(8)] for c in range(8)]
    fix8 = dense_nullspace(Tm, 8)
    anti8 = dense_nullspace(Tp, 8)
    fixv = [to_full(v, basis) for v in fix8]
    antiv = [to_full(v, basis) for v in anti8]
    pf, nf, zf = signature_of_symmetric(fixv, G)
    pa, na, za = signature_of_symmetric(antiv, Gneg)
    assert zf == 0 and za == 0
    return True, (pf + pa, nf + na)

log("  slot-signature machinery ready (8-dim nullspace + signature per slot)")

# ============================================================ Cartan action on cor (root-level only)
log("PART 2f: the Cartan action of each factor-preserving g on the cor 4-dim space "
    "(root-permutation level ONLY -- independent of sign lift, per the memo's own claim)")

def coroot_coords(r):
    for (base, off) in ((p1, 0), (p2, 2)):
        M2 = sp.Matrix([[base[0][k] for k in range(N)], [base[1][k] for k in range(N)]]).T
        v = sp.Matrix([r[k] for k in range(N)])
        solset_ = M2.solve_least_squares(v)
        if M2 * solset_ == v:
            out = [sp.Rational(0)] * 4
            out[off] = solset_[0]
            out[off + 1] = solset_[1]
            return out
    raise RuntimeError("root not in S1 u S2 span")

def cartan_mat4(g):
    cols = []
    for i in range(4):
        gi = ROOTS[g[IDX[cor[i]]]]
        cols.append(coroot_coords(gi))
    return sp.Matrix(4, 4, lambda r, c: cols[c][r])

log("  cartan_mat4 ready")

# ============================================================ the sweep: which g admit gauge row
log(f"PART 2g: THE SWEEP -- for each of the {len(FP)} factor-preserving involutions, does "
    f"ANY sign lift give slot signatures (S0,S1,S2)=((0,8),(4,4),(4,4))?")
_t = time.time()
gauge_admitting = []   # (g, inW, witness_bits)
n_checked_pairs = 0
for gi, (g, inW) in enumerate(FP):
    sols_lift = all_lift_solutions(g)
    found = None
    for bits in sols_lift:
        n_checked_pairs += 1
        theta = build_theta(g, bits)
        ok0, sig0 = slot_signature(theta, 0)
        if not ok0 or sig0 != (0, 8):
            continue
        ok1, sig1 = slot_signature(theta, 1)
        if not ok1 or sig1 != (4, 4):
            continue
        ok2, sig2 = slot_signature(theta, 2)
        if not ok2 or sig2 != (4, 4):
            continue
        found = bits
        break
    if found is not None:
        gauge_admitting.append((gi, g, inW, found, len(sols_lift)))
log(f"  sweep done in {time.time()-_t:.1f}s; (involution,lift) pairs actually evaluated: "
    f"{n_checked_pairs}")
log(f"  factor-preserving involutions admitting a GAUGE-ROW lift: {len(gauge_admitting)}  "
    f"(memo claims 16)")
assert len(gauge_admitting) == 16, f"expected 16, got {len(gauge_admitting)}"
assert all(not inW for _, _, inW, _, _ in gauge_admitting), "expected ALL in dW coset"
log("  ALL 16 are in the dW (outer/flip) coset -- CONFIRMED (reconfirms memo 12/B1135's "
    "'compactness requires the flip')")

# total (involution,lift) PAIRS giving exactly the gauge row (cross-check vs B1135's OWN
# banked b1135_results.json menu row for "S0 compact, S1=S2 su(2,1)")
total_gauge_pairs = 0
for gi, g, inW, found, nlifts in gauge_admitting:
    cnt = 0
    for bits in all_lift_solutions(g):
        theta = build_theta(g, bits)
        ok0, sig0 = slot_signature(theta, 0)
        ok1, sig1 = slot_signature(theta, 1)
        ok2, sig2 = slot_signature(theta, 2)
        if ok0 and ok1 and ok2 and sig0 == (0, 8) and sig1 == (4, 4) and sig2 == (4, 4):
            cnt += 1
    total_gauge_pairs += cnt
log(f"  total (involution,lift) PAIRS realizing this exact gauge row: {total_gauge_pairs}  "
    f"(cross-check: B1135's own banked b1135_results.json 'menu' row "
    f"'(0,8)|(4,4)|(4,4)|char -14' = 81)")

# ============================================================ anti/fixed among the 18
log("PART 2h: for each gauge-admitting involution, anti/fixed sets among the 18 Y's")
stats = Counter()
per_g_anti = {}
for gi, g, inW, found, nlifts in gauge_admitting:
    M4 = cartan_mat4(g)
    anti = [y for y in sols if act(M4, y) == tuple(-v for v in y)]
    fixed = [y for y in sols if act(M4, y) == y]
    stats[(len(anti), len(fixed))] += 1
    per_g_anti[gi] = (g, anti, fixed)

log(f"  distribution of (#anti [compact Y], #fixed [split Y]) over the 16: {dict(stats)}")
assert all(f == 0 for (a, f) in stats), "some involution has a FIXED (split) Y -- FAILS memo claim 2"
log("  CLAIM 2 CONFIRMED: fixed=0 for ALL 16 -- no hypercharge direction is EVER split "
    "by a gauge closing")

anti_sizes = sorted(a for (a, f) in stats.keys() for _ in range(stats[(a, f)]))
log(f"  anti-set sizes across the 16 involutions: {anti_sizes}")
assert anti_sizes == [2]*9 + [6]*6 + [18]*1, f"expected 9x2 + 6x6 + 1x18, got {anti_sizes}"
log("  CLAIM 3 CONFIRMED: the selection hierarchy is 9(anti=2) / 6(anti=6) / 1(anti=18)")

# ---- the 9 generic (anti=2) pairs: straddle + partition ----
pairs = [frozenset(anti) for gi, (g, anti, fixed) in per_g_anti.items() if len(anti) == 2]
log(f"  generic (anti=2) selections found: {len(pairs)}")
assert len(pairs) == 9
O1s, O2s = set(O1), set(O2)
straddle_ok = 0
for pr in pairs:
    a, b = sorted(pr)
    in_O1_a, in_O1_b = a in O1s, b in O1s
    if in_O1_a != in_O1_b:
        straddle_ok += 1
log(f"  pairs straddling the two W-orbits (one from O1, one from O2): {straddle_ok}/9")
assert straddle_ok == 9
log("  CLAIM 4 CONFIRMED: all 9 generic pairs straddle O1/O2 (9/9)")

union_pairs = set().union(*pairs)
disjoint = sum(len(p) for p in pairs) == len(union_pairs)
log(f"  union of the 9 pairs: {len(union_pairs)} of 18;  pairwise disjoint: {disjoint};  "
    f"distinct pairs (as sets): {len(set(pairs))}")
assert disjoint and len(union_pairs) == 18 and len(set(pairs)) == 9
log("  CLAIM 5 CONFIRMED: the 9 pairs are pairwise disjoint and cover all 18 (a perfect "
    "matching / partition)")

# ---- bonus structure: each selected Y annihilates exactly 4 roots (2 per EW slot) ----
log("PART 2i: bonus check -- each selected (anti) Y annihilates exactly 4 roots "
    "(one su(2) candidate per EW slot)")
S1S2 = list(S1) + list(S2)
ann_counts = []
for gi, (g, anti, fixed) in per_g_anti.items():
    for y in anti:
        zs = [r for r in S1S2 if sum(y[i] * iprr(cor[i], r) for i in range(4)) == 0]
        ann_counts.append(len(zs))
log(f"  annihilated-root counts over all selected Y's (16 involutions' anti-sets, "
    f"{len(ann_counts)} total): {sorted(set(ann_counts))}  (memo claims: always 4)")
assert set(ann_counts) == {4}
log("  BONUS CONFIRMED: every selected Y annihilates exactly 4 roots")

# ============================================================ the self-correction (P-closure)
log("PART 2j: the self-correction note -- literal P-mirror-pair closure (B1118's P = "
    "swap-ideals composed-with per-ideal outer flip; in cor-coords, reversal (y0,y1,y2,y3)"
    "->(y3,y2,y1,y0))")
def Pmap(y):
    return (y[3], y[2], y[1], y[0])
p_closed = 0
for pr in pairs:
    a, b = sorted(pr)
    pc = (Pmap(a) in pr) and (Pmap(b) in pr)
    if pc:
        p_closed += 1
log(f"  of the 9 generic pairs, literal-P-closed: {p_closed}/9  (memo's self-correction "
    f"claims exactly 3/9; the retracted eyeballed claim was 9/9)")
assert p_closed == 3, f"expected 3, got {p_closed}"
log("  SELF-CORRECTION CONFIRMED: only 3/9 pairs are literal P-mirror pairs -- the "
    "orbit-straddle invariant (Claim 4) is the correct one, not literal P-conjugacy")

log("PART 2 DONE -- ALL FIVE EXACT FACTS + the bonus structure + the self-correction "
    "reproduce independently, exact, no discrepancy")

RESULT = dict(
    n_hypercharge_directions=len(sols),
    orbit_sizes=[len(O1), len(O2)],
    n_aut_phi=len(AUT_list), n_W=len(W_list),
    n_factor_preserving=len(FP), n_inW=n_inW,
    n_gauge_admitting=len(gauge_admitting),
    gauge_admitting_all_dW=all(not inW for _, _, inW, _, _ in gauge_admitting),
    total_gauge_pairs=total_gauge_pairs,
    anti_fixed_stats={f"anti={a},fixed={f}": v for (a, f), v in stats.items()},
    n_generic_pairs=len(pairs),
    straddle_ok=straddle_ok,
    partition_disjoint=disjoint,
    partition_covers_18=len(union_pairs) == 18,
    annihilated_root_counts=sorted(set(ann_counts)),
    p_closed_pairs=p_closed,
)
json.dump(RESULT, open(os.path.join(HERE, "part2_result.json"), "w"), indent=2)
log(f"result summary dumped to {os.path.join(HERE, 'part2_result.json')}")
