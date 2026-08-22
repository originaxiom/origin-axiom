#!/usr/bin/env python3
"""INDEPENDENT VERIFICATION -- "THE GAUGE CLOSING" / cell F-1 (golden_gate cloud seat,
twelfth memo GAUGE_CLOSING.md, commit 943db85). Own-authored sweep/signature code.
VERIFY-DON'T-TRUST discipline. This is the COMPLEMENT of B1134 (already verified two-bench
on this bench): B1134 swept the 48 factor-SWAPPING involutions (two A2 slots swapped, one
fixed) and found the spacetime/Lorentz branch forced into E6(-26). F-1 sweeps the
factor-PRESERVING involutions (all three A2 slots fixed SETWISE, none swapped) and claims
the GAUGE branch closes into E6(-14).

TRUSTED (imported, not rebuilt): the banked+locked Chevalley e6 module
frontier/B1102_exact_hypercharge_solve/e6_bracket_vendored.py (ROOTS, brackets,
Jacobi/antisymmetry already verified upstream; the SAME module the cloud seat's own
certificates import per its own header, and the SAME module B1134's own bench script uses).

REUSED (per the assignment's explicit instruction -- "Read [frontier/B1134.../
verify_simul_closing.py] and REUSE these; you only need to change the involution family
from factor-SWAPPING to factor-PRESERVING"): the DESIGN of B1134's own already-
independently-verified machinery is re-typed here (NOT imported as a running module --
importing it would silently re-execute its own PART 5/9-13 sweep, its B1127-JSON
cross-check, and its result-file write as a side effect on a tracked repo file, which this
read-only verification avoids). Logic reused UNCHANGED from verify_simul_closing.py: the
ad-invariant-form G discovery (own exhaustive derivation over all 78 basis vectors, not
sorted-away), the A2 landing S0/S1/S2 (hatch + orthogonal-complement BFS components), the
W(E6) BFS reflection closure, the diagram-flip brute search over S_6, the GF(2)
TRUE-reduced-row-echelon involutive sign-lift solver (no separate back-substitution pass --
structurally avoids the cloud seat's own logged error #15), dense_nullspace,
signature_of_symmetric.

NEW code here, independent of the cloud seat's certificates/ew_menu.py (read ONLY to
understand the SPEC -- the claimed 128/2000/9+1 numbers -- never copied) and independent of
B1134's own factor-SWAPPING search (a different involution family entirely):
  - PART 4: the FACTOR-PRESERVING involution search (each of S0,S1,S2 fixed SETWISE)
  - PART 8: a GENERALIZED per-slot signature function usable on S0, S1, OR S2 (B1134's
    color_signature is hardcoded to S2/color only; F-1 needs all three slots)
  - PART 9-14: the full sweep, the menu tally, the W-coset sterility check, the (9+1)^3
    factorization + per-slot marginals, the compact-count -> global-character map, the
    one-compact-slot deep-dive (incl. a full 3003-bracket automorphism re-check on a
    representative and a cited compact-dimension cross-check), and the whole-sweep
    checksum.

Run: python3 verify_gauge_closing.py   (set GAUGE_SMOKE=1 for a fast 3-element smoke test)
"""
import importlib.util
import itertools
import os
import random
import time
from fractions import Fraction as Q
from collections import Counter, deque

T0 = time.time()


def log(msg):
    print(f"[{time.time()-T0:8.2f}s] {msg}", flush=True)


SMOKE = os.environ.get("GAUGE_SMOKE") == "1"

# ============================================================ PART 0 -- trusted e6
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VENDORED = os.path.join(REPO, "frontier/B1102_exact_hypercharge_solve/e6_bracket_vendored.py")


def load_trusted_e6():
    spec = importlib.util.spec_from_file_location("e6_trusted_bank_f1", VENDORED)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


E6 = load_trusted_e6()
ROOTS, IDX, N, DIM = E6.ROOTS, E6.IDX, E6.N, E6.DIM
BR, EVEC, HVEC, IP, EPS, CARTAN = E6.br, E6.evec, E6.hvec, E6.ip, E6.eps, E6.A
NR = len(ROOTS)
assert NR == 72 and DIM == 78, "trusted module shape unexpected -- stop"
SIMPLE = [tuple(1 if k == i else 0 for k in range(N)) for i in range(N)]
log(f"trusted e6 loaded: {NR} roots, dim {DIM} (frontier/B1102 vendored module)")


def negroot(r):
    return tuple(-x for x in r)


NEGIDX = {k: IDX[negroot(r)] for k, r in enumerate(ROOTS)}

# ==================================================== PART 1 -- invariant form G
# (reused design, B1134: G(h_i,h_j)=Cartan; G(e_r,e_-r)=c, discovered exhaustively not
# assumed -- own re-derivation here, same method, before trusting it for the sweep below)


def make_G(c_root_pair):
    G = [[Q(0)] * DIM for _ in range(DIM)]
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
        if Gdot(G, BR(x, y), z) + Gdot(G, y, BR(x, z)) != 0:
            bad += 1
    return bad


log("PART 1: re-deriving the sign of G(e_r,e_-r) by exhaustive ad-invariance (own check)")
basis_vecs = [HVEC(i) for i in range(N)] + [EVEC(r) for r in ROOTS]
all_pairs = list(itertools.combinations(range(DIM), 2))
trip_vecs = [(basis_vecs[xi], basis_vecs[j], basis_vecs[k])
             for xi in range(DIM) for j, k in all_pairs]
G_minus = make_G(-1)
G_plus = make_G(+1)
bad_minus = ad_invariance_defect_count(G_minus, trip_vecs)
bad_plus = ad_invariance_defect_count(G_plus, trip_vecs)
log(f"  c=-1 candidate: {bad_minus} ad-invariance failures / {len(trip_vecs)} triples")
log(f"  c=+1 candidate: {bad_plus} failures (negative control)")
assert bad_minus == 0, "own derivation says -1 must be ad-invariant"
assert bad_plus > 0, "the +1 form should FAIL ad-invariance -- unexpected pass"
G = G_minus
Gneg = [[-x for x in row] for row in G]
log("  G(e_r,e_-r) = -1 confirmed exhaustively ad-invariant (matches B1134's own finding)")

# ============================================================ PART 2 -- the A2 landing
log("PART 2: the A2 landing S0 (hatch), S1, S2 (own construction, reused design)")
a0, a2 = SIMPLE[0], SIMPLE[2]
assert IP(a0, a2) == -1, "nodes 0,2 must be adjacent"
S0 = set()
for c1 in (-1, 0, 1):
    for c2 in (-1, 0, 1):
        r = tuple(c1 * a0[k] + c2 * a2[k] for k in range(N))
        if r in IDX:
            S0.add(r)
assert len(S0) == 6

Rperp = [r for r in ROOTS if IP(r, a0) == 0 and IP(r, a2) == 0]
assert len(Rperp) == 12


def connected_components(roots_list):
    remaining = set(roots_list)
    comps = []
    while remaining:
        start = next(iter(remaining))
        comp = {start}
        q = deque([start])
        remaining.discard(start)
        while q:
            u = q.popleft()
            for v in list(remaining):
                if IP(u, v) != 0:
                    comp.add(v)
                    remaining.discard(v)
                    q.append(v)
        comps.append(comp)
    return comps


comps = connected_components(Rperp)
assert len(comps) == 2 and all(len(c) == 6 for c in comps)
S1, S2 = comps
cross_bad = sum(1 for r in S1 for s in S2 if IP(r, s) != 0)
assert cross_bad == 0
SLOTS = [S0, S1, S2]
SLOT_IDX = [frozenset(IDX[r] for r in S) for S in SLOTS]
log(f"  S0={len(S0)} S1={len(S1)} S2={len(S2)}, mutually orthogonal (cross pairs) confirmed")


def find_simple_pair(comp):
    for r, s in itertools.permutations(comp, 2):
        t = tuple(r[k] + s[k] for k in range(N))
        if IP(r, s) == -1 and t in comp:
            return r, s
    raise RuntimeError("no simple pair found")


SLOT_PAIRS = [find_simple_pair(S) for S in SLOTS]
log(f"  slot simple pairs: S0={SLOT_PAIRS[0]}  S1={SLOT_PAIRS[1]}  S2={SLOT_PAIRS[2]}")

# ============================================== PART 3 -- W(E6) + diagram flip (reused)
log("PART 3: W(E6) via reflection closure (own BFS) + diagram automorphism (own search)")


def simple_reflection_perm(i):
    ai = SIMPLE[i]
    perm = [0] * NR
    for k, r in enumerate(ROOTS):
        c = IP(r, ai)
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
iso_bad = sum(1 for i in range(NR) for j in range(i + 1, NR)
              if IP(flip_images[i], flip_images[j]) != IP(ROOTS[i], ROOTS[j]))
assert iso_bad == 0
DELTA = tuple(IDX[im] for im in flip_images)
assert compose(DELTA, DELTA) == IDENT
assert DELTA not in W_set
log(f"  diagram flip (own search): {PI} -> verified bijection/isometry/involution/outer")

AUT_list = list(W_list) + [compose(DELTA, w) for w in W_list]
AUT_inW = [True] * len(W_list) + [False] * len(W_list)
assert len(AUT_list) == 103680
log(f"  |Aut(Phi(E6))| = {len(AUT_list)}")

# ============================================== PART 4 [NEW] -- factor-PRESERVING search
log("PART 4 [NEW]: searching Aut(Phi) for involutions PRESERVING S0, S1 AND S2 setwise "
    "(the complement of B1134's factor-SWAPPING search)")


def image_idx(perm, idxset):
    return frozenset(perm[i] for i in idxset)


FP = []  # list of (g, inW)
for g, inW in zip(AUT_list, AUT_inW):
    if all(image_idx(g, SLOT_IDX[i]) == SLOT_IDX[i] for i in range(3)):
        if compose(g, g) == IDENT:
            FP.append((g, inW))

n_inW = sum(1 for _, inW in FP if inW)
n_outer = len(FP) - n_inW
log(f"  factor-preserving involutions found: {len(FP)}  ({n_inW} in W, {n_outer} in deltaW)")
assert n_inW > 0 and n_outer > 0, "expect both cosets represented"

if SMOKE:
    FP = FP[:2] + [(g, inW) for g, inW in FP if not inW][:2]
    log(f"  ** SMOKE MODE: truncated to {len(FP)} elements for a fast correctness pass **")

# ======================================= PART 5 -- GF(2) sign-lift solver (reused design)
# Same true-RREF design as B1134 (every pivot fully eliminated the moment it's found; no
# separate back-substitution phase) -- structurally avoids the cloud seat's error #15.


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

    assert satisfies(particular), "particular solution fails an ORIGINAL row -- solver bug"
    for kv in kernel:
        assert satisfies(particular ^ kv), "a kernel vector fails an ORIGINAL row -- solver bug"

    return particular, kernel


def all_lift_solutions(phi):
    res = solve_signed_lift(phi)
    if res is None:
        return []
    particular, kernel = res
    sols = []
    for bits in range(1 << len(kernel)):
        x = particular
        for j in range(len(kernel)):
            if (bits >> j) & 1:
                x ^= kernel[j]
        sols.append(x)
    return sols


NEG = tuple(NEGIDX[k] for k in range(NR))

log("PART 5: GF(2) sign-lift solver, own control validation before trusting it")
antipodal_all = all_lift_solutions(NEG)
log(f"  antipodal control: {len(antipodal_all)} involutive sign solutions "
    f"(expect 64=2^6, matches B1134's own control)")
assert len(antipodal_all) == 64 and len(set(antipodal_all)) == 64

# ============================================== PART 6 -- theta + automorphism (reused)


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


def sparse_to_dense(sv):
    out = [Q(0)] * DIM
    for i, c in sv.items():
        out[i] = c
    return out


def theta_dense(theta, v):
    return sparse_to_dense(sp_apply(theta, dense_to_sparse(v)))


def check_theta_squared_is_identity(theta):
    for i in range(DIM):
        v = {i: Q(1)}
        v2 = sp_apply(theta, sp_apply(theta, v))
        if v2 != {i: Q(1)}:
            return False
    return True


def automorphism_spot_check(theta, ntrials, rng):
    for _ in range(ntrials):
        i, j = rng.randrange(DIM), rng.randrange(DIM)
        x, y = basis_vecs[i], basis_vecs[j]
        lhs = theta_dense(theta, BR(x, y))
        rhs = BR(theta_dense(theta, x), theta_dense(theta, y))
        if lhs != rhs:
            return False
    return True


def automorphism_full_3003(theta):
    bad = 0
    for i in range(DIM):
        xi = basis_vecs[i]
        txi = theta_dense(theta, xi)
        for j in range(i + 1, DIM):
            xj = basis_vecs[j]
            lhs = theta_dense(theta, BR(xi, xj))
            rhs = BR(txi, theta_dense(theta, xj))
            if lhs != rhs:
                bad += 1
    return bad


# ============================================ PART 7 -- nullspace/signature core (reused)
def dense_nullspace(cols, nrows=None):
    nrows = DIM if nrows is None else nrows
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


def global_character(theta):
    cols = [theta_dense(theta, basis_vecs[j]) for j in range(DIM)]
    Tminus_cols = [[cols[c][r] - (Q(1) if r == c else Q(0)) for r in range(DIM)] for c in range(DIM)]
    Tplus_cols = [[cols[c][r] + (Q(1) if r == c else Q(0)) for r in range(DIM)] for c in range(DIM)]
    fixb = dense_nullspace(Tminus_cols)
    antib = dense_nullspace(Tplus_cols)
    pf, nf, zf = signature_of_symmetric(fixb, G)
    pa, na, za = signature_of_symmetric(antib, Gneg)
    assert zf == 0 and za == 0, "degenerate restriction of G -- should never happen"
    return (pf + pa) - (nf + na), (pf + pa, nf + na)


# ================================== PART 8 [NEW] -- generalized per-slot signature
# B1134's color_signature is hardcoded to S2 (COLOR_BASIS). F-1 needs the SAME machinery
# on ALL THREE slots (S0, S1, S2) since it claims a per-slot menu, not just a color check.
# Genuinely new code: builds one 8-dim basis (6 root vectors + 2 Cartan-coordinate
# "coroot" vectors from the slot's own found simple pair) PER SLOT, then reuses the
# already-verified nullspace/signature core (Part 7) on each.


def cartan_coord_vec(root_tuple):
    v = [Q(0)] * DIM
    for k in range(N):
        v[k] = Q(root_tuple[k])
    return v


SLOT_BASES = []
for i in range(3):
    r1, s1 = SLOT_PAIRS[i]
    basis_i = [EVEC(r) for r in sorted(SLOTS[i])] + [cartan_coord_vec(r1), cartan_coord_vec(s1)]
    assert len(basis_i) == 8
    SLOT_BASES.append(basis_i)


def solve_coords(v, span_cols):
    """Coordinates of v in span_cols (each a dense DIM-vector), by augmented RREF. Raises
    ValueError if v is not EXACTLY in the span (residual check against the rebuild)."""
    k = len(span_cols)
    M = [[span_cols[c][r] for c in range(k)] + [v[r]] for r in range(DIM)]
    piv_cols = []
    r = 0
    for c in range(k):
        pr = None
        for i in range(r, DIM):
            if M[i][c] != 0:
                pr = i
                break
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        inv = Q(1) / M[r][c]
        if inv != 1:
            M[r] = [x * inv for x in M[r]]
        for i in range(DIM):
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
    rebuilt = [Q(0)] * DIM
    for c in range(k):
        if coeffs[c]:
            cc = coeffs[c]
            col = span_cols[c]
            for row in range(DIM):
                if col[row]:
                    rebuilt[row] += cc * col[row]
    if rebuilt != v:
        raise ValueError("vector escaped the span")
    return coeffs


def to_full(coeffs, span_cols):
    out = [Q(0)] * DIM
    for c, coef in enumerate(coeffs):
        if coef:
            col = span_cols[c]
            for row in range(DIM):
                if col[row]:
                    out[row] += coef * col[row]
    return out


def slot_signature(theta, slot_i):
    """NEW: generalizes B1134's color_signature (S2-only) to ANY of the three A2 slots.
    Returns (preserved: bool, (pos,neg) or None). preserved=False would mean theta does
    NOT actually stabilize this slot's 8-dim span -- should never happen for g in FP by
    construction, but checked (not assumed): solve_coords raises ValueError on any escape."""
    basis = SLOT_BASES[slot_i]
    try:
        tc_cols = [solve_coords(theta_dense(theta, v), basis) for v in basis]
    except ValueError:
        return False, None
    Tm = [[tc_cols[c][r] - (Q(1) if r == c else Q(0)) for r in range(8)] for c in range(8)]
    Tp = [[tc_cols[c][r] + (Q(1) if r == c else Q(0)) for r in range(8)] for c in range(8)]
    fix8 = dense_nullspace(Tm, nrows=8)
    anti8 = dense_nullspace(Tp, nrows=8)
    fixv = [to_full(v, basis) for v in fix8]
    antiv = [to_full(v, basis) for v in anti8]
    pf, nf, zf = signature_of_symmetric(fixv, G)
    pa, na, za = signature_of_symmetric(antiv, Gneg)
    assert zf == 0 and za == 0
    return True, (pf + pa, nf + na)


def evaluate_pair(phi, sign_bits, rng, automorphism_trials=30):
    theta = build_theta(phi, sign_bits)
    ok2 = check_theta_squared_is_identity(theta)
    auto_ok = automorphism_spot_check(theta, automorphism_trials, rng)
    char, gsig = global_character(theta)
    sigs = [slot_signature(theta, i) for i in range(3)]
    return dict(theta2=ok2, auto_spot=auto_ok, char=char, gsig=gsig, sigs=sigs)


log("PART 9 [NEW]: timing ONE full evaluate_pair call (theta^2, auto spot, char, 3 slot sigs)")
_rng0 = random.Random(20260822)
_g0, _inW0 = FP[0]
_sol0 = solve_signed_lift(_g0)
assert _sol0 is not None
_particular0, _kernel0 = _sol0
_t = time.time()
_res0 = evaluate_pair(_g0, _particular0, _rng0)
log(f"  probe FP#0 (inW={_inW0}) result: {_res0}  ({time.time()-_t:.3f}s)")

# ========================================== PART 10 -- THE FULL SWEEP (tasks 1-4)
log(f"PART 10: THE FULL SWEEP -- all {len(FP)} factor-preserving involutions x "
    f"all involutive sign lifts")
_t = time.time()
RNG = random.Random(943085)
no_lift = 0
total_pairs = 0
all_results = []  # (gi, inW, bits, res)
for gi, (g, inW) in enumerate(FP):
    sols = all_lift_solutions(g)
    if not sols:
        no_lift += 1
        continue
    for bits in sols:
        total_pairs += 1
        res = evaluate_pair(g, bits, RNG, automorphism_trials=25)
        assert res["theta2"], f"FP {gi} sol {bits}: theta^2 != I -- solver bug"
        assert res["auto_spot"], f"FP {gi} sol {bits}: FAILED automorphism spot-check"
        all_results.append((gi, inW, bits, res))
    if SMOKE:
        log(f"  ... FP#{gi} (inW={inW}): {len(sols)} lift solutions evaluated")

log(f"  FP elements with NO involutive lift: {no_lift}/{len(FP)}")
log(f"  total (involution, sign-solution) pairs evaluated: {total_pairs}  ({time.time()-_t:.1f}s)")

if SMOKE:
    log("SMOKE MODE complete -- exiting before the full-scale verdict checks (correctness only)")
    raise SystemExit(0)

# ============================================== PART 11 -- THE MENU (task 2)
log("PART 11: THE MENU (own tally)")
menu = Counter()
for gi, inW, bits, res in all_results:
    sigkey = tuple(s[1] if s[0] else ("NOT-PRESERVED",) for s in res["sigs"])
    menu[(sigkey, res["char"])] += 1

FORM = {-78: "E6c", -26: "E6(-26)", -14: "E6(-14)", 2: "E6(2)", 6: "E6(6)"}
NAME = {(0, 8): "su(3)", (4, 4): "su(2,1)", (5, 3): "sl(3,R)", (8, 0): "IMPOSSIBLE"}
for (sigkey, char), cnt in sorted(menu.items(), key=lambda kv: -kv[1]):
    lbl = " | ".join(f"{s}={NAME.get(s,'?')}" for s in sigkey)
    log(f"  {lbl} | char {char:+d} [{FORM.get(char,'?')}] : {cnt}")
assert sum(menu.values()) == total_pairs

not_preserved = sum(v for (sigkey, char), v in menu.items() if ("NOT-PRESERVED",) in sigkey)
log(f"  pairs where some slot's 8-dim span was NOT preserved: {not_preserved} (expect 0)")
assert not_preserved == 0, "a factor-preserving involution failed to preserve a slot span!"

# ============================================== PART 12 -- W-COSET STERILITY (task 3)
log("PART 12: W-coset sterility check")
W_results = [(gi, bits, res) for gi, inW, bits, res in all_results if inW]
DW_results = [(gi, bits, res) for gi, inW, bits, res in all_results if not inW]
log(f"  W-coset pairs: {len(W_results)}   deltaW-coset pairs: {len(DW_results)}")

w_tally = Counter()
for gi, bits, res in W_results:
    sigkey = tuple(s[1] for s in res["sigs"])
    w_tally[(sigkey, res["char"])] += 1
log(f"  W-coset (sig,char) tally: {dict(w_tally)}")
assert set(w_tally.keys()) == {(((5, 3), (5, 3), (5, 3)), 6)}, \
    f"W-coset is NOT uniformly sterile -- found {set(w_tally.keys())}"
log(f"  W-COSET STERILE CONFIRMED: all {len(W_results)} pairs give (sl(3,R))^3, char +6 = E6(6)")

# ============================================ PART 13 -- (9+1)^3 FACTORIZATION (task 4)
log("PART 13: deltaW-coset (9+1)^3 factorization + per-slot marginals + compact-count map")
dw_tally = Counter()
for gi, bits, res in DW_results:
    sigkey = tuple(s[1] for s in res["sigs"])
    dw_tally[(sigkey, res["char"])] += 1
log(f"  deltaW-coset distinct (sig,char) rows: {len(dw_tally)}")
for k, v in sorted(dw_tally.items(), key=lambda kv: -kv[1]):
    log(f"    {k}: {v}")

assert all((5, 3) not in k[0] for k in dw_tally), "sl(3,R) appeared on the flip side!"
assert all(s in {(4, 4), (0, 8)} for k in dw_tally for s in k[0]), \
    "an unexpected slot signature appeared on the flip side!"
log("  CONFIRMED: on deltaW, every slot signature is su(2,1) or su(3) ONLY -- never sl(3,R)")

for i in range(3):
    marg = Counter(res["sigs"][i][1] for gi, bits, res in DW_results)
    log(f"  slot {i} marginal over deltaW ({len(DW_results)} pairs): {dict(marg)}")
    assert marg[(4, 4)] == 900 and marg[(0, 8)] == 100, \
        f"slot {i} marginal is not the claimed 900:100 (9:1) split -- got {dict(marg)}"
log("  PER-SLOT (9+1) MARGINAL CONFIRMED on all three slots independently: "
    "900 su(2,1) : 100 su(3) = 9:1, each slot")

cc_char = Counter()
for gi, bits, res in DW_results:
    cc = sum(1 for s in res["sigs"] if s[1] == (0, 8))
    cc_char[(cc, res["char"])] += 1
log(f"  (compact_count, char) joint tally over deltaW: {dict(cc_char)}")
EXPECT_CC = {(0, 2): 729, (1, -14): 243, (2, 2): 27, (3, -78): 1}
assert dict(cc_char) == EXPECT_CC, f"MISMATCH: {dict(cc_char)} vs expected {EXPECT_CC}"
log(f"  COMPACT-COUNT -> GLOBAL-CHARACTER MAP CONFIRMED: {EXPECT_CC}")
log("  (own binomial cross-check: C(3,0)*9^3=729, C(3,1)*9^2*1=243, C(3,2)*9*1^2=27, "
    "C(3,3)*1^3=1 -- matches the (9+1)^3=1000 multinomial expansion exactly)")

# ==================================== PART 14 -- ONE-COMPACT-SLOT DEEP-DIVE (task 5)
log("PART 14: the ONE-COMPACT-SLOT (k=1, the SM-facing row) deep verification")
k1_results = [(gi, bits, res) for gi, bits, res in DW_results
              if sum(1 for s in res["sigs"] if s[1] == (0, 8)) == 1]
log(f"  k=1 rows: {len(k1_results)} (expect 243 = 81*3)")
assert len(k1_results) == 243

chars_k1 = Counter(res["char"] for _, _, res in k1_results)
log(f"  chars across all k=1 rows: {dict(chars_k1)} (expect ALL -14)")
assert set(chars_k1) == {-14}

other_sigs = Counter()
for gi, bits, res in k1_results:
    others = tuple(sorted((s[1] for s in res["sigs"] if s[1] != (0, 8)), key=str))
    other_sigs[others] += 1
log(f"  the two non-compact slots' signature in k=1 rows: {dict(other_sigs)} "
    f"(expect ALL ((4,4),(4,4)) = (su(2,1),su(2,1)))")
assert set(other_sigs) == {((4, 4), (4, 4))}
log("  CONFIRMED: su(2,1) max-compact = u(2) [pos=4 noncompact, neg=4 compact matches "
    "su(2)+u(1) dim 3+1=4]; its coset dimension (the doublet) = 4 non-compact directions")

# cited cross-check: dim(so(10)) + dim(u(1)) = 45 + 1 = 46 should equal the GLOBAL
# "compact" (neg) count of the E6(-14) representative's (pos,neg) global signature
gcompact = Counter(res["gsig"][1] for _, _, res in k1_results)
log(f"  global compact dim (neg-count of gsig) across k=1 rows: {dict(gcompact)} "
    f"(cited: dim so(10)+u(1) = 45+1 = 46)")
assert set(gcompact) == {46}
log("  GLOBAL HOST E6(-14) CONFIRMED, its compact core's dimension matches so(10)+u(1) "
    "exactly (cited dims, arithmetic cross-check computed here)")

rep_gi, rep_bits, rep_res = k1_results[0]
rep_g, rep_inW = FP[rep_gi]
rep_theta = build_theta(rep_g, rep_bits)
_t = time.time()
bad_pairs = automorphism_full_3003(rep_theta)
log(f"  representative k=1 hit: FULL 3003-pair Chevalley-bracket automorphism check: "
    f"{bad_pairs} failures / 3003  ({time.time()-_t:.1f}s)")
assert bad_pairs == 0, "representative E6(-14) hit FAILS the full automorphism check"
rep_theta2 = check_theta_squared_is_identity(rep_theta)
log(f"  theta^2=I (exact): {rep_theta2}")
assert rep_theta2
log(f"  representative slot sigs: {[s[1] for s in rep_res['sigs']]}, char {rep_res['char']:+d}, "
    f"global (pos,neg)={rep_res['gsig']}")

# which slot is compact varies (frame symmetry) -- report, don't "resolve" (fenced)
compact_slot_positions = Counter()
for gi, bits, res in k1_results:
    pos = [i for i, s in enumerate(res["sigs"]) if s[1] == (0, 8)][0]
    compact_slot_positions[pos] += 1
log(f"  which slot index carries the compact su(3) across the 243 k=1 rows: "
    f"{dict(compact_slot_positions)} (81 each -- the 3-fold position symmetry the memo "
    f"calls a frame choice; NOT adjudicated here, reported as data)")

# ============================================== PART 15 -- CHECKSUM (task 6)
log("PART 15: CHECKSUM -- every global character across the whole sweep")
all_chars = Counter(res["char"] for gi, inW, bits, res in all_results)
log(f"  character histogram across all {total_pairs} pairs: {dict(all_chars)}")
ALLOWED = {6, 2, -14, -26, -78}
assert set(all_chars) <= ALLOWED, f"instrument break: char outside {ALLOWED}: {set(all_chars)}"
log(f"  CHECKSUM CLEAN: every character in {{+6,+2,-14,-26,-78}}; witnessed = {sorted(all_chars)}")
log(f"  NOTE: -26 (E6(-26), the B1134 spacetime host) is NOT witnessed here by construction "
    f"-- F-1 sweeps a DISJOINT involution family (factor-preserving) from B1134's "
    f"(factor-swapping); the two are complementary sub-sweeps of Aut(Phi), not a shared one.")

# bonus cross-check: cited compact-subalgebra dimension for EVERY character witnessed,
# not just the k=1 row (own arithmetic: dim sp(4)=36, su(6)+su(2)=35+3=38, so(10)+u(1)=46,
# f4=52, compact e6=78)
COMPACT_DIM = {6: 36, 2: 38, -14: 46, -26: 52, -78: 78}
mismatches = 0
for gi, inW, bits, res in all_results:
    want = COMPACT_DIM.get(res["char"])
    if want is not None and res["gsig"][1] != want:
        mismatches += 1
log(f"  global compact-dimension cross-check (cited max-compact dims per real form) vs "
    f"computed neg-count: {mismatches} mismatches / {total_pairs}")
assert mismatches == 0
log("  compact-dimension cross-check CLEAN for every pair in the sweep")

# ============================================== RESULTS DUMP (scratchpad only, not repo)
import json as _json_dump


def _tk(t):
    if t is None:
        return "None"
    return ",".join(str(x) for x in t)


_RESULTS = {
    "provenance": "independent verification of golden_gate 943db85 (cloud seat twelfth "
                   "memo, cell F-1, GAUGE_CLOSING.md); own-authored sweep; trusted e6 = "
                   "B1102 vendored module; reused-design infra from B1134's own script",
    "n_factor_preserving_involutions": len(FP),
    "n_inW": n_inW,
    "n_outer": n_outer,
    "n_pairs_total": total_pairs,
    "elements_with_no_lift": no_lift,
    "menu": {f"{sigkey}|{char:+d}": v for (sigkey, char), v in menu.items()},
    "w_coset_sterile_tally": {f"{k}|{c:+d}": v for (k, c), v in w_tally.items()},
    "dw_coset_tally": {f"{k}|{c:+d}": v for (k, c), v in dw_tally.items()},
    "compact_count_to_char": {f"{k}": v for k, v in cc_char.items()},
    "k1_row": {
        "n": len(k1_results),
        "chars": dict(chars_k1),
        "other_slot_sigs": {str(k): v for k, v in other_sigs.items()},
        "global_compact_dim": dict(gcompact),
        "representative_full3003_failures": bad_pairs,
        "compact_slot_positions": dict(compact_slot_positions),
    },
    "checksum_chars_witnessed": dict(all_chars),
    "checksum_compact_dim_mismatches": mismatches,
}
outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "b1135_results.json")
with open(outpath, "w") as f:
    _json_dump.dump(_RESULTS, f, indent=2)
log(f"  results dumped to {outpath}")
log("DONE.")
