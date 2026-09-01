"""R06 blind recomputation of B1134 (simultaneous closing census) and B1135
(gauge closing census). Own code throughout; e6_lib is this cell's own validated
Chevalley basis. No file of the arcs' verification/ or tests/ has been read.

Conventions chosen HERE (independently):
  - A2+A2+A2 subsystem from the extended Dynkin diagram (remove trivalent node 4):
      FA = A2 on {a1, a3}, FB = A2 on {a5, a6}, FC = A2 on {a2, a0=-highest}.
  - "color" slot default FC, swapped pair (FA, FB); census repeated for all three
    color choices to establish labeling-independence.
  - theta acts linearly: h_i -> h_{w(a_i)}, e_a -> s_a e_{w(a)}; real form is the
    fixed algebra of sigma = theta o tau, tau = split (entrywise) conjugation in
    the Chevalley basis. Character chi = Killing signature (pos - neg) of that
    real form; slot signature = same restricted to the 8-dim slot subalgebra,
    reported (pos, neg) = (noncompact, compact).
"""
import json, random, sys, time
import numpy as np
from fractions import Fraction
from itertools import combinations
import e6_lib as E

t0 = time.time()
rng = random.Random(20260901)
ROOTS, RIDX, NEG, SIMPLE = E.ROOTS, E.RIDX, E.NEG, E.SIMPLE
NR = 72
B = E.killing()
ADM = E.ADM
C = E.C
D = 78

def log(*a):
    print(*a, flush=True)

# ---------------- Weyl group as permutations of ROOTS ----------------
def reflect_perm(alpha):
    p = []
    for r in ROOTS:
        c = E.ip(r, alpha)
        p.append(RIDX[tuple(r[k] - c * alpha[k] for k in range(6))])
    return tuple(p)

GENS = [reflect_perm(s) for s in SIMPLE]
IDP = tuple(range(NR))
NEGP = tuple(RIDX[NEG[r]] for r in ROOTS)

def compose(p, q):  # (p o q)[k] = p[q[k]]
    return tuple(p[k] for k in q)

log("BFS over W(E6)...")
W = {IDP}
frontier = [IDP]
while frontier:
    new = []
    for g in frontier:
        for s in GENS:
            h = compose(s, g)
            if h not in W:
                W.add(h)
                new.append(h)
    frontier = new
log("|W| =", len(W), " -1 in W:", NEGP in W, " elapsed", round(time.time()-t0,1))
assert len(W) == 51840 and NEGP not in W

AUT = [(g, True) for g in W] + [(compose(NEGP, g), False) for g in W]

# ---------------- the A2+A2+A2 subsystem ----------------
highest = max(ROOTS, key=E.height)
a0 = NEG[highest]
def a2_factor(r1, r2):
    assert E.ip(r1, r2) == -1
    s = tuple(x + y for x, y in zip(r1, r2))
    fam = [r1, r2, s, NEG[r1], NEG[r2], NEG[s]]
    return frozenset(RIDX[x] for x in fam), (r1, r2)

FA, pairA = a2_factor(SIMPLE[0], SIMPLE[2])   # a1, a3
FB, pairB = a2_factor(SIMPLE[4], SIMPLE[5])   # a5, a6
FC, pairC = a2_factor(SIMPLE[1], a0)          # a2, a0
FACTORS = [FA, FB, FC]
PAIRS = [pairA, pairB, pairC]
UNION = FA | FB | FC
assert len(UNION) == 18
for i, j in combinations(range(3), 2):
    for x in FACTORS[i]:
        for y in FACTORS[j]:
            assert E.ip(ROOTS[x], ROOTS[y]) == 0
log("A2^3 subsystem built, mutually orthogonal.")

# ---------------- classify Aut elements acting on the subsystem ----------------
def factor_action(p):
    """induced map on factors if p preserves the union, else None"""
    img = {}
    for fi, F in enumerate(FACTORS):
        s = frozenset(p[i] for i in F)
        hit = next((fj for fj, G in enumerate(FACTORS) if s == G), None)
        if hit is None:
            return None
        img[fi] = hit
    return (img[0], img[1], img[2])

def is_involution(p):
    return all(p[p[k]] == k for k in range(NR))

union_preservers = []
for p, inW in AUT:
    fa = factor_action(p)
    if fa is not None:
        union_preservers.append((p, inW, fa, is_involution(p)))
induced = sorted(set(fa for _, _, fa, _ in union_preservers))
log("union-preserving elements:", len(union_preservers),
    "induced factor-perms:", induced)

def swappers_for(i, j, kcol):
    return [(p, inW) for p, inW, fa, inv in union_preservers
            if inv and fa == tuple({i: j, j: i, kcol: kcol}[t] for t in range(3))]

def preservers():
    return [(p, inW) for p, inW, fa, inv in union_preservers
            if inv and fa == (0, 1, 2)]

# ---------------- GF(2) involutive-automorphism-lift solver ----------------
SUMPAIRS = []  # (ia, ib, isum) for unordered pairs with root sum
for ia in range(NR):
    for ib in range(ia + 1, NR):
        s = tuple(x + y for x, y in zip(ROOTS[ia], ROOTS[ib]))
        if s in RIDX:
            SUMPAIRS.append((ia, ib, RIDX[s]))
EPS2 = {}
for ia, ib, isum in SUMPAIRS:
    EPS2[(ia, ib)] = E.eps2(ROOTS[ia], ROOTS[ib])
log("sum-pairs:", len(SUMPAIRS))

def gf2_solve(p):
    """All involutive automorphism sign-lifts of root-perm p (p involutive).
    Returns list of sign vectors s in {+-1}^72, or []."""
    rows = []
    rhs = []
    for ia, ib, isum in SUMPAIRS:
        wa, wb = p[ia], p[ib]
        lo, hi = min(wa, wb), max(wa, wb)
        e1 = EPS2[(ia, ib)]
        e2 = EPS2[(lo, hi)]
        # eps2(wa,wb): careful with order: eps2(b,a) = -eps2(a,b)
        if (wa, wb) != (lo, hi):
            e2 = -e2
        r = np.zeros(NR, dtype=np.uint8)
        r[ia] ^= 1; r[ib] ^= 1; r[isum] ^= 1
        rows.append(r); rhs.append(1 if e1 != e2 else 0)
    for ia in range(NR):
        ineg = RIDX[NEG[ROOTS[ia]]]
        if ia < ineg:
            r = np.zeros(NR, dtype=np.uint8); r[ia] ^= 1; r[ineg] ^= 1
            rows.append(r); rhs.append(0)
        iw = p[ia]
        if ia < iw:
            r = np.zeros(NR, dtype=np.uint8); r[ia] ^= 1; r[iw] ^= 1
            rows.append(r); rhs.append(0)
    Amat = np.array(rows, dtype=np.uint8)
    bvec = np.array(rhs, dtype=np.uint8)
    # RREF over GF(2)
    M = np.concatenate([Amat, bvec[:, None]], axis=1)
    nrows, ncols = M.shape
    piv_cols = []
    rrow = 0
    for c in range(NR):
        pr = None
        for r2 in range(rrow, nrows):
            if M[r2, c]:
                pr = r2; break
        if pr is None:
            continue
        M[[rrow, pr]] = M[[pr, rrow]]
        mask = M[:, c].copy(); mask[rrow] = 0
        M[mask == 1] ^= M[rrow]
        piv_cols.append(c)
        rrow += 1
        if rrow == nrows:
            break
    # consistency
    for r2 in range(rrow, nrows):
        if M[r2, NR] and not M[r2, :NR].any():
            return []
    free = [c for c in range(NR) if c not in piv_cols]
    sols = []
    for bits in range(1 << len(free)):
        x = np.zeros(NR, dtype=np.uint8)
        for k, c in enumerate(free):
            x[c] = (bits >> k) & 1
        for r2 in range(len(piv_cols) - 1, -1, -1):
            c = piv_cols[r2]
            v = M[r2, NR] ^ (int(M[r2, :NR] @ x) & 1) ^ x[c]
            x[c] = v
        # verify
        assert not ((Amat @ x + bvec) % 2).any()
        sols.append(np.where(x == 1, -1, 1).astype(np.int64))
    return sols

# ---------------- theta matrix + checks ----------------
def wmat_of(p):
    """action of p on the root lattice in simple-root coordinates (6x6 int)."""
    Wm = np.zeros((6, 6), dtype=np.int64)
    for i in range(6):
        Wm[:, i] = ROOTS[p[RIDX[SIMPLE[i]]]]
    for i, r in enumerate(ROOTS):  # consistency: perm = linear action
        assert tuple(Wm @ np.array(r)) == ROOTS[p[i]]
    return Wm

def theta_matrix(p, s, Wm):
    M = np.zeros((D, D), dtype=np.int64)
    M[:6, :6] = Wm
    for ia in range(NR):
        M[6 + p[ia], 6 + ia] = s[ia]
    return M

def full_bracket_failures(M):
    """number of basis pairs (i<=j) where theta fails [Mx,My]=M[x,y]; exact."""
    T1 = np.tensordot(M, ADM, axes=(1, 1))       # (a,i,c)
    LHS = np.tensordot(T1, M, axes=(2, 0))       # (a,i,d) = (M adm_i M)[a,d]
    LHS = np.transpose(LHS, (1, 0, 2))           # (i,a,d)
    RHS = np.tensordot(M, ADM, axes=(0, 0))      # (i,a,d) = sum_k M[k,i] adm_k
    diff = (LHS != RHS)
    # translate to per-column-pair failures: condition per i is ad(Me_i)=M ad(e_i) M^{-1}
    return int(diff.any(axis=(1, 2)).sum())

def literal_3003_check(M):
    bad = 0
    for i in range(D):
        for j in range(i + 1, D):
            lhs_vec = np.tensordot(np.tensordot(C, M[:, i], axes=(0, 0)), M[:, j], axes=(0, 0))
            rhs_vec = M @ C[i, j, :]
            if not np.array_equal(lhs_vec, rhs_vec):
                bad += 1
    return bad

def frac_rank(Mint):
    rowsM = [[Fraction(int(x)) for x in row] for row in Mint]
    n = len(rowsM); m = len(rowsM[0]); rank = 0
    for c in range(m):
        piv = next((r for r in range(rank, n) if rowsM[r][c] != 0), None)
        if piv is None: continue
        rowsM[rank], rowsM[piv] = rowsM[piv], rowsM[rank]
        pr = rowsM[rank]
        for r in range(n):
            if r != rank and rowsM[r][c] != 0:
                f = rowsM[r][c] / pr[c]
                rowsM[r] = [x - f * y for x, y in zip(rowsM[r], pr)]
        rank += 1
    return rank

def combinatorial_signature(p, s, Wm, root_subset=None, cartan_span=None):
    """(pos, neg) of Killing on the sigma-fixed real form, restricted to the
    subalgebra given by root_subset (list of root indices) + cartan_span
    (list of lattice vectors); None = everything."""
    if root_subset is None:
        root_subset = list(range(NR))
        span = [tuple(1 if k == i else 0 for k in range(6)) for i in range(6)]
    else:
        span = cartan_span
    Sp = np.array(span, dtype=np.int64).T  # 6 x d
    d = Sp.shape[1]
    # action of w on the span: solve Wm Sp = Sp X  (exact; span is w-invariant)
    X = np.zeros((d, d), dtype=object)
    WS = Wm @ Sp
    SpF = [[Fraction(int(Sp[i][j])) for j in range(d)] for i in range(6)]
    for col in range(d):
        target = [Fraction(int(WS[i][col])) for i in range(6)]
        aug = [row[:] + [target[i]] for i, row in enumerate(SpF)]
        # gaussian solve (least: span independent)
        n = 6; rank = 0; piv = []
        for c in range(d):
            pr = next((r for r in range(rank, n) if aug[r][c] != 0), None)
            if pr is None: continue
            aug[rank], aug[pr] = aug[pr], aug[rank]
            for r in range(n):
                if r != rank and aug[r][c] != 0:
                    f = aug[r][c] / aug[rank][c]
                    aug[r] = [x - f * y for x, y in zip(aug[r], aug[rank])]
            piv.append(c); rank += 1
        sol = [Fraction(0)] * d
        for r, c in enumerate(piv):
            sol[c] = aug[r][d] / aug[r][c]
        for r in range(rank, n):
            assert aug[r][d] == 0
        for i in range(d):
            X[i][col] = sol[i]
    XI = [[X[i][j] - (1 if i == j else 0) for j in range(d)] for i in range(d)]
    XP = [[X[i][j] + (1 if i == j else 0) for j in range(d)] for i in range(d)]
    cpos = d - frac_rank(XI)
    cneg = d - frac_rank(XP)
    assert cpos + cneg == d
    pos, neg = cpos, cneg  # Killing pos-def on real Cartan span; iV- flips sign
    seen = set()
    for ia in root_subset:
        if ia in seen: continue
        ineg = RIDX[NEG[ROOTS[ia]]]
        iw = p[ia]
        if iw == ia:
            seen |= {ia, ineg}
            pos += 1; neg += 1
        elif iw == ineg:
            seen |= {ia, ineg}
            if s[ia] == 1: pos += 2
            else: neg += 2
        else:
            orbit = {ia, ineg, iw, RIDX[NEG[ROOTS[iw]]]}
            assert len(orbit) == 4
            seen |= orbit
            pos += 2; neg += 2
    return pos, neg

def exact_form_signature(M, sub_basis=None):
    """independent exact route: congruence signature of Killing on V+ (+B) and
    V- (-B). sub_basis: 78 x d int matrix (columns) or None for full."""
    if sub_basis is None:
        Mres = M; Bres = B
    else:
        S = sub_basis
        # Mres: solve M S = S Mres exactly (columns of S independent)
        SF = [[Fraction(int(S[i][j])) for j in range(S.shape[1])] for i in range(S.shape[0])]
        MS = M @ S
        d = S.shape[1]
        Mres = [[Fraction(0)] * d for _ in range(d)]
        for col in range(d):
            aug = [SF[i][:] + [Fraction(int(MS[i][col]))] for i in range(S.shape[0])]
            n = S.shape[0]; rank = 0; piv = []
            for c in range(d):
                pr = next((r for r in range(rank, n) if aug[r][c] != 0), None)
                if pr is None: continue
                aug[rank], aug[pr] = aug[pr], aug[rank]
                for r in range(n):
                    if r != rank and aug[r][c] != 0:
                        f = aug[r][c] / aug[rank][c]
                        aug[r] = [x - f * y for x, y in zip(aug[r], aug[rank])]
                piv.append(c); rank += 1
            for r in range(rank, n):
                assert aug[r][d] == 0
            for r, c in enumerate(piv):
                Mres[c][col] = aug[r][d] / aug[r][c]
        Bres = S.T @ B @ S
        Mres = np.array([[x for x in row] for row in Mres], dtype=object)
    d = Bres.shape[0]
    I = np.eye(d, dtype=np.int64)
    Pp = np.array(E.column_space_basis((np.array(Mres) + I).T.tolist()), dtype=object).T \
        if sub_basis is not None else None
    # simpler: use column_space_basis on (Mres±I) as float-free lists
    def colspace(Mat):
        return E.column_space_basis(Mat.tolist() if hasattr(Mat, 'tolist') else Mat)
    Vp = colspace((np.array(Mres, dtype=object) + I))
    Vm = colspace((np.array(Mres, dtype=object) - I))
    def gram(Vecs, sign):
        k = len(Vecs)
        G = [[sign * sum(Vecs[a][i] * Fraction(int(Bres[i][j])) * Vecs[b][j]
                         for i in range(d) for j in range(d)) for b in range(k)]
             for a in range(k)]
        return G
    res = [0, 0, 0]
    for Vecs, sgn in ((Vp, 1), (Vm, -1)):
        if not Vecs: continue
        po, ne, ze = E.exact_signature(gram(Vecs, sgn))
        res[0] += po; res[1] += ne; res[2] += ze
    return tuple(res)

# slot sub-bases (78 x 8 int matrices)
def slot_basis(F, pair):
    cols = []
    for r in pair:  # two coroots
        v = np.zeros(D, dtype=np.int64); v[:6] = r
        cols.append(v)
    for ia in sorted(F):
        v = np.zeros(D, dtype=np.int64); v[6 + ia] = 1
        cols.append(v)
    return np.stack(cols, axis=1)

SLOTB = [slot_basis(F, pr) for F, pr in zip(FACTORS, PAIRS)]

# double (so(3,1)) machinery: principal triple of a slot
def principal_triple(pair):
    r1, r2 = pair
    Ev = np.zeros(D, dtype=np.int64); Ev[6 + RIDX[r1]] = 1; Ev[6 + RIDX[r2]] = 1
    Hv = np.zeros(D, dtype=np.int64); Hv[:6] = 2 * (np.array(r1) + np.array(r2))
    Fv = np.zeros(D, dtype=np.int64); Fv[6 + RIDX[NEG[r1]]] = 2; Fv[6 + RIDX[NEG[r2]]] = 2
    # verify sl2 relations
    def br(x, y):
        return np.tensordot(np.tensordot(C, x, axes=(0, 0)), y, axes=(0, 0))
    assert np.array_equal(br(Hv, Ev), 2 * Ev)
    assert np.array_equal(br(Hv, Fv), -2 * Fv)
    assert np.array_equal(br(Ev, Fv), Hv)
    return [Ev, Hv, Fv]

def double_signature(M, triple):
    vs = triple
    G = np.zeros((6, 6), dtype=np.int64)
    for a in range(3):
        for b in range(3):
            va, vb = vs[a], vs[b]
            G[a, b] = (va + M @ va) @ B @ (vb + M @ vb)
            G[3 + a, 3 + b] = -((va - M @ va) @ B @ (vb - M @ vb))
            G[a, 3 + b] = 0; G[3 + b, a] = 0
    return E.exact_signature(G)

# ---------------- candidate evaluation ----------------
def evaluate(p, s, Wm, slots_needed, full_check=True):
    M = theta_matrix(p, s, Wm)
    inv_ok = np.array_equal(M @ M, np.eye(D, dtype=np.int64))
    fails = full_bracket_failures(M) if full_check else None
    gpos, gneg = combinatorial_signature(p, s, Wm)
    chi = gpos - gneg
    slots = []
    for k in slots_needed:
        F, pr = FACTORS[k], PAIRS[k]
        sp, sn = combinatorial_signature(p, s, Wm, root_subset=sorted(F),
                                         cartan_span=list(pr))
        slots.append((sp, sn))
    return M, inv_ok, fails, chi, (gpos, gneg), slots

CHECKSUM_SET = {6, 2, -14, -26, -78}
all_chis = []

results = {"algebra_validation": E.validate_algebra(),
           "induced_factor_perms": [list(x) for x in induced]}

# ============ B1134: the swap census, all three color choices ============
b1134 = {}
for (i, j, kcol), name in [((0, 1, 2), "color=FC(default)"),
                           ((1, 2, 0), "color=FA"),
                           ((0, 2, 1), "color=FB")]:
    sw = swappers_for(i, j, kcol)
    nW = sum(1 for _, inw in sw if inw)
    log(f"[B1134 {name}] swappers: {len(sw)} (W: {nW}, coset: {len(sw)-nW})")
    hist = {}
    hits = []
    pair_count = 0
    per_swapper = []
    chi_by_slot_sig = {}
    hit_swapper_ids = set()
    triple = principal_triple(PAIRS[i])
    for sidx, (p, inw) in enumerate(sw):
        Wm = wmat_of(p)
        sols = gf2_solve(p)
        per_swapper.append(len(sols))
        for s in sols:
            pair_count += 1
            M, inv_ok, fails, chi, gsig, slots = evaluate(p, s, Wm, [kcol])
            assert inv_ok and fails == 0, (sidx, inv_ok, fails)
            all_chis.append(chi)
            key = slots[0]
            hist[key] = hist.get(key, 0) + 1
            chi_by_slot_sig.setdefault(key, set()).add(chi)
            if key == (0, 8):
                dsig = double_signature(M, triple)
                exf = exact_form_signature(M)
                excol = exact_form_signature(M, SLOTB[kcol])
                nfix_color = sum(1 for ia in FACTORS[kcol] if p[ia] == ia)
                hits.append({"swapper_index": sidx, "in_W": inw, "chi": chi,
                             "global_sig": gsig, "double_sig": dsig,
                             "exact_global_crosscheck": exf,
                             "exact_color_crosscheck": excol,
                             "literal_3003_failures": literal_3003_check(M),
                             "color_roots_fixed_by_swapper": nfix_color})
                hit_swapper_ids.add(sidx)
    # exact cross-checks on a random sample of non-hit candidates
    b1134[name] = {"n_swappers": len(sw), "n_swappers_W": nW,
                   "pair_count": pair_count,
                   "lifts_per_swapper": sorted(set(per_swapper)),
                   "color_sig_histogram": {str(k): v for k, v in hist.items()},
                   "chi_by_color_sig": {str(k): sorted(v) for k, v in chi_by_slot_sig.items()},
                   "n_hits": hist.get((0, 8), 0),
                   "hits": hits,
                   "n_distinct_hit_swappers": len(hit_swapper_ids)}
    log(f"  pairs={pair_count} hist={hist}")
    log(f"  chi by color sig: {chi_by_slot_sig}")
    log(f"  distinct hit swappers: {len(hit_swapper_ids)}")

results["B1134"] = b1134
with open("r06_results_partial.json", "w") as f:
    json.dump(results, f, indent=1, default=str)

# ============ B1135: the factor-preserving census ============
pres = preservers()
nWp = sum(1 for _, inw in pres if inw)
log(f"[B1135] factor-preserving involutions: {len(pres)} (W: {nWp}, coset: {len(pres)-nWp})")
rows = []
count = 0
for p, inw in pres:
    Wm = wmat_of(p)
    sols = gf2_solve(p)
    for s in sols:
        count += 1
        # full bracket check on every 10th + all with any compact slot (cheap enough: do all)
        M, inv_ok, fails, chi, gsig, slots = evaluate(p, s, Wm, [0, 1, 2])
        assert inv_ok and fails == 0
        all_chis.append(chi)
        rows.append({"in_W": inw, "chi": chi, "neg": gsig[1],
                     "slots": slots,
                     "n_compact": sum(1 for x in slots if x == (0, 8))})
log(f"[B1135] total conjugations: {count}")
wside = [r for r in rows if r["in_W"]]
fside = [r for r in rows if not r["in_W"]]
b1135 = {"n_preservers": len(pres), "n_preservers_W": nWp,
         "total_conjugations": count,
         "W_side_count": len(wside),
         "W_side_chis": sorted(set(r["chi"] for r in wside)),
         "W_side_slotsigs": sorted(set(str(r["slots"]) for r in wside)),
         "flip_side_count": len(fside)}
from collections import Counter
byk = Counter(r["n_compact"] for r in fside)
chibyk = {k: sorted(set(r["chi"] for r in fside if r["n_compact"] == k)) for k in byk}
slotmarg = [Counter(r["slots"][t] for r in fside) for t in range(3)]
slotset_f = sorted(set(str(sg) for r in fside for sg in r["slots"]))
joint = Counter(tuple(r["slots"]) for r in fside)
b1135.update({"flip_by_compact_count": dict(byk), "flip_chi_by_compact_count":
              {str(k): v for k, v in chibyk.items()},
              "flip_slot_marginals": [ {str(k): v for k, v in m.items()} for m in slotmarg],
              "flip_slot_sig_set": slotset_f,
              "flip_joint_factorizes": all(
                  joint[(a, b, c)] == slotmarg[0][a] * slotmarg[1][b] * slotmarg[2][c] // (len(fside) ** 2 // 1)
                  for a in slotmarg[0] for b in slotmarg[1] for c in slotmarg[2]) if fside else None,
              "compact_dims_seen": sorted(set(r["neg"] for r in rows))})
# proper factorization check: joint == product of marginals / N^2
if fside:
    Nf = len(fside)
    ok = True
    for a in slotmarg[0]:
        for b2 in slotmarg[1]:
            for c2 in slotmarg[2]:
                expect = Fraction(slotmarg[0][a] * slotmarg[1][b2] * slotmarg[2][c2], Nf * Nf)
                if Fraction(joint.get((a, b2, c2), 0)) != expect:
                    ok = False
    b1135["flip_joint_factorizes"] = ok
results["B1135"] = b1135
log("B1135 summary:", {k: v for k, v in b1135.items() if k != "flip_slot_marginals"})
log("flip slot marginals:", b1135["flip_slot_marginals"])

# representative physics-row deep checks: chi=-14 row: k structure
phys = [r for r in fside if r["n_compact"] == 1]
b1135["physics_row_all_chi_minus14"] = all(r["chi"] == -14 for r in phys)
b1135["physics_row_count"] = len(phys)
b1135["physics_row_noncompact_slot_sigs"] = sorted(set(
    str(sg) for r in phys for sg in r["slots"] if sg != (0, 8)))

# ============ controls ============
log("controls...")
controls = {}
# (a) antipodal family: 64 involutive lifts expected; omega = all-minus among them
Wm_neg = wmat_of(NEGP)
sols_neg = gf2_solve(NEGP)
controls["antipodal_n_involutive_lifts"] = len(sols_neg)
fam = []
omega_found = False
for s in sols_neg:
    M, inv_ok, fails, chi, gsig, slots = evaluate(NEGP, s, Wm_neg, [0, 1, 2])
    assert inv_ok and fails == 0
    all_chis.append(chi)
    fam.append((chi, tuple(slots)))
    if all(x == -1 for x in s):
        omega_found = True
        tripleA = principal_triple(PAIRS[0])
        controls["omega"] = {"chi": chi, "slots": [list(x) for x in slots],
                            "exact_global": exact_form_signature(M),
                            "double_sig": double_signature(M, tripleA),
                            "literal_3003_failures": literal_3003_check(M)}
controls["antipodal_family_chis"] = sorted(set(c for c, _ in fam))
controls["omega_found"] = omega_found
# (b) identity lift = split form
M_id = np.eye(D, dtype=np.int64)
gpos, gneg = combinatorial_signature(IDP, np.ones(NR, dtype=np.int64), np.eye(6, dtype=np.int64))
controls["identity_chi"] = gpos - gneg
controls["identity_exact"] = exact_form_signature(M_id)
all_chis.append(gpos - gneg)
# (c) planted FAKE form (E49-style): antipodal perm with a NON-cocycle sign
# pattern (17 positive roots flipped to +1): should give chi=-10, outside the
# checksum set, AND fail the automorphism check.
s_fake = -np.ones(NR, dtype=np.int64)
flip = [RIDX[r] for r in E.POSITIVE[:17]]
for ia in flip:
    s_fake[ia] = 1; s_fake[RIDX[NEG[ROOTS[ia]]]] = 1
M_fake = theta_matrix(NEGP, s_fake, Wm_neg)
gposf, gnegf = combinatorial_signature(NEGP, s_fake, Wm_neg)
controls["fake_form"] = {"chi": gposf - gnegf,
                         "in_checksum_set": (gposf - gnegf) in CHECKSUM_SET,
                         "bracket_failures": full_bracket_failures(M_fake),
                         "exact_crosscheck": exact_form_signature(M_fake)}
# (d) exact cross-checks on random genuine candidates (formula vs congruence)
sample_checks = []
sw_def = swappers_for(0, 1, 2)
for _ in range(8):
    p, inw = sw_def[rng.randrange(len(sw_def))]
    Wm = wmat_of(p)
    sols = gf2_solve(p)
    if not sols: continue
    s = sols[rng.randrange(len(sols))]
    M, inv_ok, fails, chi, gsig, slots = evaluate(p, s, Wm, [2])
    exf = exact_form_signature(M)
    exc = exact_form_signature(M, SLOTB[2])
    sample_checks.append({"combinatorial": [gsig, slots[0]],
                          "exact": [list(exf), list(exc)],
                          "agree": (exf[0], exf[1]) == gsig and (exc[0], exc[1]) == slots[0]
                          and exf[2] == 0 and exc[2] == 0})
controls["random_exact_crosschecks"] = sample_checks
results["controls"] = controls

# ============ checksum ============
results["checksum"] = {"all_chis_in_set": all(c in CHECKSUM_SET for c in all_chis),
                       "witnessed": sorted(set(all_chis)),
                       "n_evaluations": len(all_chis)}
log("checksum:", results["checksum"])
log("controls:", controls)

with open("r06_results.json", "w") as f:
    json.dump(results, f, indent=1, default=str)
log("DONE", round(time.time() - t0, 1), "s")
