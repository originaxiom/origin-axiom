#!/usr/bin/env python3
"""
Independent Cold-Room Zero-Trust Referee for Card A2-LEG5-TOWER-MODULAR-BRIDGE.
Seat code: fam3-v1-high-03. Strictly 0 of 19 (zero empirical inputs).

Disjoint verification algorithms across all five modules:
  - Leg(5): 12 x 12 unsigned permutation action on Rays(5) = (F_5^2 \\ {0})/{+-1}
    projected onto the 6-dim (-1)-eigenspace of scalar multiplication by 2.
  - B1: Markoff mod-3^k orbits built via <C_tr, sigma_tr>; unique 6-pt congruence Q_6
    and 8-pt mod-9 control Q_8; pure-integer Faddeev-LeVerrier trace recursion over Z
    on H_0 (12x12) and H_1 (+) H_2 (24x24) with exact Z[y] polynomial square root;
    exhaustive G_3 (216) and G_4 (1944) character fixed-point verification; explicit
    signed C-orbit sparse sector matrices over Z and Z[omega] for Delta_{2m}.
  - B2: Symbolic chiral walk algebra over Q(sqrt(3), sqrt(5)) without nested radicals.
  - B3: Symbolic mirror-lock theorem; Siegel units via Jacobi theta_1 series and
    Euler pentagonal Dedekind eta; Illinois root-finder for y_odd*; golden-section
    search + 5-point Richardson 2D Hessians for tau_{I4}^* and tau_{I6}^*.
  - B4: Weierstrass wp via theta_1 derivatives and pentagonal E_2; 5-division poly
    derived directly from chord-and-tangent x([2]P) = x([3]P) and resultant over Z[u].
  - B5: 5/5 independent planted falsification controls (RPF1..RPF5).
"""

from collections import deque
import json
from pathlib import Path
import time
import mpmath as mp
import sympy as sp

I_MP = mp.mpc(0, 1)

P1_F5 = (
    (1, 0),
    (0, 1),
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
)

MAT_L = ((1, 1), (0, 1))
MAT_R = ((1, 0), (1, 1))
MAT_R_INV = ((1, 0), (-1, 1))
MAT_S = ((0, -1), (1, 0))
MAT_C_OM = ((0, 1), (-1, 1))
MAT_C3 = ((0, -1), (1, -1))
MAT_C0 = ((1, 1), (-1, 0))
MAT_NEG_C0 = ((-1, -1), (1, 0))
MAT_TAU_MIR = ((0, 1), (1, 0))
MAT_M_CIRC = ((0, 1), (1, 0))
MAT_M_HALF = ((-1, 1), (0, 1))
MAT_M_C1 = ((1, 0), (1, -1))
MAT_R0 = ((-1, 0), (0, 1))
MAT_NEG_I = ((-1, 0), (0, -1))


def fmt_mp(val, digits=45):
    return mp.nstr(val, digits)


def fmt_mpc(val, digits=45):
    return {
        "re": mp.nstr(mp.re(val), digits),
        "im": mp.nstr(mp.im(val), digits),
    }


def z_expand_zero(expr):
    return sp.expand(sp.radsimp(expr)) == 0


def mat_zero(M):
    return all(z_expand_zero(M[i, j]) for i in range(M.rows) for j in range(M.cols))


def mat_frob_sq_int(M):
    total = 0
    for i in range(M.rows):
        for j in range(M.cols):
            val = int(M[i, j])
            total += val * val
    return total


# ---------------------------------------------------------------------------
# Disjoint Leg(5) Construction via 12-Ray Permutation Action + Projection
# ---------------------------------------------------------------------------

def _ray12_index(vec):
    x = vec[0] % 5
    y = vec[1] % 5
    for i, (px, py) in enumerate(P1_F5):
        for s in (1, 4):
            if x == (s * px) % 5 and y == (s * py) % 5:
                return 2 * i
        for s in (2, 3):
            if x == (s * px) % 5 and y == (s * py) % 5:
                return 2 * i + 1
    raise ValueError("Zero vector in Rays(5)")


def build_ray12_perm_matrix(M):
    """Exact 12 x 12 unsigned permutation matrix on Rays(5) = (F_5^2 \\ {0})/{+-1}."""
    M12 = sp.zeros(12, 12)
    for i, (px, py) in enumerate(P1_F5):
        for parity, mult in ((0, 1), (1, 2)):
            vx = (mult * px) % 5
            vy = (mult * py) % 5
            nx = (M[0][0] * vx + M[0][1] * vy) % 5
            ny = (M[1][0] * vx + M[1][1] * vy) % 5
            dst = _ray12_index((nx, ny))
            M12[dst, 2 * i + parity] = 1
    return M12


def _build_leg5_projector():
    """
    12 x 6 projector columns e_i = (|r_i^+> - |r_i^->) / sqrt(2).
    We store P_int = sqrt(2) * P so P^T M12 P = (P_int^T M12 P_int) / 2 is exact over Z.
    """
    P_int = sp.zeros(12, 6)
    for i in range(6):
        P_int[2 * i, i] = 1
        P_int[2 * i + 1, i] = -1
    return P_int


_P_LEG5_INT = _build_leg5_projector()
_S2_RAY12 = build_ray12_perm_matrix(((2, 0), (0, 2)))


def leg5_rep_sym(M):
    """Project 12x12 unsigned ray permutation onto (-1)-eigenspace of scalar-2."""
    M12 = build_ray12_perm_matrix(M)
    if M12 * _S2_RAY12 != _S2_RAY12 * M12:
        raise AssertionError("Ray-12 action does not commute with scalar multiplication by 2")
    raw = _P_LEG5_INT.T * M12 * _P_LEG5_INT
    res = sp.zeros(6, 6)
    for i in range(6):
        for j in range(6):
            entry = int(raw[i, j])
            if entry % 2 != 0:
                raise AssertionError("Non-integer projection entry")
            res[i, j] = entry // 2
    return res


def leg5_rep_mp(M):
    S = leg5_rep_sym(M)
    R = mp.zeros(6, 6)
    for i in range(6):
        for j in range(6):
            R[i, j] = mp.mpf(int(S[i, j]))
    return R


def leg5_signed_perm(M):
    """Extract exact signed permutation list [(target, sign), ...] from 12-ray projection."""
    S = leg5_rep_sym(M)
    out = []
    for j in range(6):
        hits = [(i, int(S[i, j])) for i in range(6) if int(S[i, j]) != 0]
        if len(hits) != 1 or hits[0][1] not in (-1, 1):
            raise AssertionError("Leg(5) image is not a signed permutation")
        out.append(hits[0])
    return tuple(out)


def verify_leg5_foundation():
    rL = leg5_rep_sym(MAT_L)
    rR = leg5_rep_sym(MAT_R)
    rS = leg5_rep_sym(MAT_S)
    rCom = leg5_rep_sym(MAT_C_OM)
    rC3 = leg5_rep_sym(MAT_C3)
    rC0 = leg5_rep_sym(MAT_C0)
    rNegC0 = leg5_rep_sym(MAT_NEG_C0)
    rMir = leg5_rep_sym(MAT_TAU_MIR)
    rNegI = leg5_rep_sym(MAT_NEG_I)
    I6 = sp.eye(6)
    # Check P_int is exact (-1)-eigenspace of _S2_RAY12
    s2_minus_one = (_S2_RAY12 * _P_LEG5_INT == -_P_LEG5_INT)
    # Check orthogonality and group relations
    orth_ok = all(M.T * M == I6 for M in (rL, rR, rS, rCom, rC3, rC0, rNegC0, rMir))
    rel_S2 = (rS * rS == I6)
    rel_negI = (rNegI == I6)
    rel_Com_C3 = (rCom == rC3 and rC3 ** 3 == I6)
    rel_C0_negC0 = (rC0 == rNegC0 and rNegC0 ** 3 == I6)
    rel_mir2 = (rMir * rMir == I6)
    rel_Com_def = (rCom == rL * rR.T)
    rel_C0_def = (rC0 == rR.T * rL)
    rel_S_conj = (rS * rC3 * rS.T == rNegC0)
    return {
        "ray12_dim": 12,
        "leg5_dim": 6,
        "s2_eigenvalue_minus_1": bool(s2_minus_one),
        "all_generators_orthogonal": bool(orth_ok),
        "rho_neg_I_is_identity": bool(rel_negI),
        "rho_S_sq_is_identity": bool(rel_S2),
        "rho_Com_eq_C3_order_3": bool(rel_Com_C3),
        "rho_C0_eq_negC0_order_3": bool(rel_C0_negC0),
        "rho_tau_mir_sq_is_identity": bool(rel_mir2),
        "rho_Com_eq_L_Rinv": bool(rel_Com_def),
        "rho_C0_eq_Rinv_L": bool(rel_C0_def),
        "rho_S_C3_Sinv_eq_negC0": bool(rel_S_conj),
    }


# ---------------------------------------------------------------------------
# Module B1: Markoff Towers, Q_6 x Leg(5), Faddeev-LeVerrier, Level-30
# ---------------------------------------------------------------------------

def _c_tr(t, mod):
    x, y, z = t
    return (y % mod, z % mod, x % mod)


def _sig_tr(t, mod):
    x, y, z = t
    return (y % mod, x % mod, (x * y - z) % mod)


def _l_tr(t, mod):
    x, y, z = t
    return (x % mod, z % mod, (x * z - y) % mod)


def _r_tr(t, mod):
    x, y, z = t
    return (z % mod, y % mod, (y * z - x) % mod)


def build_markoff_orbit_csig(seed, mod):
    """Build orbit using <C_tr, sigma_tr> (disjoint from <L_tr, R_tr>), then cross-check."""
    start = tuple(v % mod for v in seed)
    seen = {start}
    q = deque([start])
    while q:
        u = q.popleft()
        for fn in (_c_tr, _sig_tr):
            v = fn(u, mod)
            if v not in seen:
                seen.add(v)
                q.append(v)
    # Independent cross-check with <L_tr, R_tr>
    seen_lr = {start}
    q_lr = deque([start])
    while q_lr:
        u = q_lr.popleft()
        for fn in (_l_tr, _r_tr):
            v = fn(u, mod)
            if v not in seen_lr:
                seen_lr.add(v)
                q_lr.append(v)
    same_as_lr = (seen == seen_lr)
    pts = sorted(seen)
    idx = {p: i for i, p in enumerate(pts)}
    pC = tuple(idx[_c_tr(p, mod)] for p in pts)
    pS = tuple(idx[_sig_tr(p, mod)] for p in pts)
    fixC = sum(1 for i, v in enumerate(pC) if i == v)
    return pts, pC, pS, fixC, same_as_lr


def comp_perm(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def prod_perm(p1, p2):
    n2 = len(p2)
    return tuple(p1[i] * n2 + p2[j] for i in range(len(p1)) for j in range(n2))


def fix_count(p):
    return sum(1 for i, v in enumerate(p) if i == v)


def find_minimal_quotient_q6(pC, pS):
    """Find ALL G_3-congruences of O_27^{(3,3,3)} and extract unique 6-pt quotient Q_6."""
    n = len(pC)

    def close_pairs(pairs):
        par = list(range(n))

        def find(a):
            while par[a] != a:
                par[a] = par[par[a]]
                a = par[a]
            return a

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                par[rb] = ra
                return True
            return False

        for a, b in pairs:
            union(a, b)
        changed = True
        while changed:
            changed = False
            for i in range(n):
                ri = find(i)
                for p in (pC, pS):
                    if union(p[i], p[ri]):
                        changed = True
        classes = {}
        for i in range(n):
            classes.setdefault(find(i), []).append(i)
        return tuple(sorted(tuple(sorted(v)) for v in classes.values()))

    minimal_congs = {close_pairs([(0, j)]) for j in range(1, n)}
    all_congs = set(minimal_congs)
    q = deque(minimal_congs)
    while q:
        c = q.popleft()
        for m0 in minimal_congs:
            pairs = [(blk[0], x) for cc in (c, m0) for blk in cc for x in blk[1:]]
            jc = close_pairs(pairs)
            if jc not in all_congs:
                all_congs.add(jc)
                q.append(jc)

    size_counts = {}
    for c in all_congs:
        size_counts[len(c)] = size_counts.get(len(c), 0) + 1
    c6_list = [c for c in all_congs if len(c) == 6]
    if len(c6_list) != 1:
        raise AssertionError("Expected unique 6-point congruence Q_6")
    c6 = c6_list[0]
    bmap = {x: bi for bi, blk in enumerate(c6) for x in blk}
    qC = tuple(bmap[pC[blk[0]]] for blk in c6)
    qS = tuple(bmap[pS[blk[0]]] for blk in c6)
    fixC = fix_count(qC)
    return qC, qS, fixC, sorted(size_counts.items())


def compose_sp(a, b):
    return tuple((a[t][0], a[t][1] * s) for t, s in b)


def build_sector_operators(pC, pS, spL, spR, spC0):
    """
    Build W_+ and W_- on X x Leg(5), verify [W_+, W_-] = 0 directly on all basis vectors,
    and construct explicit sparse C-orbit sector matrices H_0 (over Z) and H_1 (over Z[omega]).
    """
    pC2 = comp_perm(pC, pC)
    pL = comp_perm(pS, pC2)
    pR = comp_perm(pS, pC)
    nx = len(pC)
    N = nx * 6
    gC = tuple((pC[x] * 6 + spC0[p][0], spC0[p][1]) for x in range(nx) for p in range(6))
    gL = tuple((pL[x] * 6 + spL[p][0], spL[p][1]) for x in range(nx) for p in range(6))
    gR = tuple((pR[x] * 6 + spR[p][0], spR[p][1]) for x in range(nx) for p in range(6))
    gC2 = compose_sp(gC, gC)
    idN = tuple((i, 1) for i in range(N))

    Wplus = [compose_sp(p1, compose_sp(gL, p2)) for p1, p2 in ((idN, idN), (gC, gC2), (gC2, gC))]
    Wminus = [compose_sp(p1, compose_sp(gR, p2)) for p1, p2 in ((idN, idN), (gC, gC2), (gC2, gC))]

    comm_nonzero = 0
    for j in range(N):
        acc = {}
        for t1 in Wplus:
            k1, s1 = t1[j]
            for t2 in Wminus:
                k2, s2 = t2[k1]
                acc[k2] = acc.get(k2, 0) + s1 * s2
        for t2 in Wminus:
            k1, s1 = t2[j]
            for t1 in Wplus:
                k2, s2 = t1[k1]
                acc[k2] = acc.get(k2, 0) - s1 * s2
        for v in acc.values():
            if v != 0:
                comm_nonzero += 1

    # Partition basis into free signed 3-cycles of gC: v0, v1=gC(v0), v2=gC^2(v0)
    cyc_id = [-1] * N
    cyc_pos = [0] * N
    cyc_sgn = [1] * N
    reps = []
    ncyc = 0
    for i in range(N):
        if cyc_id[i] == -1:
            reps.append(i)
            cur, s = i, 1
            for r in range(3):
                if cyc_id[cur] != -1:
                    raise AssertionError("gC cycle not of length 3")
                cyc_id[cur] = ncyc
                cyc_pos[cur] = r
                cyc_sgn[cur] = s
                nxt, ns = gC[cur]
                cur, s = nxt, s * ns
            if cur != i or s != 1:
                raise AssertionError("gC^3 != +I on cycle")
            ncyc += 1

    H0 = [{} for _ in range(ncyc)]
    H1 = [{} for _ in range(ncyc)]
    all_terms = Wplus + Wminus
    for c_src, v0 in enumerate(reps):
        triples = {}
        for term in all_terms:
            tgt, s_term = term[v0]
            c_dst = cyc_id[tgt]
            r = cyc_pos[tgt]
            if c_dst not in triples:
                triples[c_dst] = [0, 0, 0]
            triples[c_dst][r] += s_term * cyc_sgn[tgt]
        for c_dst, (a0, a1, a2) in triples.items():
            s0 = a0 + a1 + a2
            if s0 != 0:
                H0[c_dst][c_src] = s0
            # a0 + a1*w + a2*w^2 = (a0 - a2) + (a1 - a2)*w
            z0 = a0 - a2
            z1 = a1 - a2
            if z0 != 0 or z1 != 0:
                H1[c_dst][c_src] = (z0, z1)

    return (comm_nonzero == 0), comm_nonzero, ncyc, H0, H1


def _sparse_mul_Z(A, B):
    n = len(A)
    C = [{} for _ in range(n)]
    for i in range(n):
        row = C[i]
        for j, a in A[i].items():
            for k, b in B[j].items():
                v = row.get(k, 0) + a * b
                if v != 0:
                    row[k] = v
                else:
                    row.pop(k, None)
    return C


def _sparse_mul_Zw(A, B):
    n = len(A)
    C = [{} for _ in range(n)]
    for i in range(n):
        row = C[i]
        for j, (a, b) in A[i].items():
            for k, (c, d) in B[j].items():
                bd = b * d
                r0 = a * c - bd
                r1 = a * d + b * c - bd
                prev = row.get(k)
                if prev is None:
                    if r0 != 0 or r1 != 0:
                        row[k] = (r0, r1)
                else:
                    n0 = prev[0] + r0
                    n1 = prev[1] + r1
                    if n0 != 0 or n1 != 0:
                        row[k] = (n0, n1)
                    else:
                        row.pop(k)
    return C


def _trace_sq_Z(A):
    total = 0
    for i, row in enumerate(A):
        for j, aij in row.items():
            aji = A[j].get(i, 0)
            if aji != 0:
                total += aij * aji
    return total


def _trace_sq_Zw(A):
    s0 = 0
    s1 = 0
    for i, row in enumerate(A):
        for j, (a, b) in row.items():
            pair = A[j].get(i)
            if pair is not None:
                c, d = pair
                bd = b * d
                s0 += a * c - bd
                s1 += a * d + b * c - bd
    if s1 != 0:
        raise AssertionError("Non-integer charged trace moment in Z[omega]")
    return s0


def faddeev_leverrier_Z(M):
    """
    Pure-integer Faddeev-LeVerrier trace recursion for det(y I - M) = sum_{k=0}^n c[k] y^k.
    Verifies exact integer divisibility at every step and terminal adjugate B_n == 0.
    """
    n = len(M)
    c = [0] * (n + 1)
    c[n] = 1
    B = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for k in range(1, n + 1):
        MB = [[sum(M[i][t] * B[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
        tr = sum(MB[i][i] for i in range(n))
        if tr % k != 0:
            raise AssertionError("Faddeev-LeVerrier trace not divisible by k")
        ck = -tr // k
        c[n - k] = ck
        B = [[MB[i][j] + (ck if i == j else 0) for j in range(n)] for i in range(n)]
    terminal_zero = all(B[i][j] == 0 for i in range(n) for j in range(n))
    if not terminal_zero:
        raise AssertionError("Faddeev-LeVerrier terminal matrix B_n != 0")
    return c, terminal_zero


def poly_exact_sqrt_Z(c_sq):
    """Compute exact monic square root q in Z[y] of monic even-degree polynomial c_sq in Z[y]."""
    deg2 = len(c_sq) - 1
    if deg2 % 2 != 0 or c_sq[deg2] != 1:
        raise AssertionError("Input to poly_exact_sqrt_Z must be monic of even degree")
    d = deg2 // 2
    q = [0] * (d + 1)
    q[d] = 1
    for k in range(d - 1, -1, -1):
        s = sum(q[i] * q[d + k - i] for i in range(k + 1, d))
        num = c_sq[d + k] - s
        if num % 2 != 0:
            raise AssertionError("Polynomial is not an exact square in Z[y]")
        q[k] = num // 2
    # Full coefficient-by-coefficient verification q^2 == c_sq
    prod = [0] * (deg2 + 1)
    for i in range(d + 1):
        for j in range(d + 1):
            prod[i + j] += q[i] * q[j]
    if prod != c_sq:
        raise AssertionError("Exact polynomial square root verification failed")
    return q


def run_module_b1():
    spL = leg5_signed_perm(MAT_L)
    spR = leg5_signed_perm(MAT_R)
    spC0 = leg5_signed_perm(MAT_NEG_C0)

    pts27_333, pC27, pS27, fixC27, lr27 = build_markoff_orbit_csig((3, 3, 3), 27)
    pts27_3312, pC12, pS12, fixC12, lr12 = build_markoff_orbit_csig((3, 3, 12), 27)
    pts27_3315, pC15, pS15, fixC15, lr15 = build_markoff_orbit_csig((3, 3, 15), 27)
    pts81_333, pC81, pS81, fixC81, lr81 = build_markoff_orbit_csig((3, 3, 3), 81)
    pts9_333, pC9, pS9, fixC9, lr9 = build_markoff_orbit_csig((3, 3, 3), 9)

    qC6, qS6, fixC_Q6, cong_sizes = find_minimal_quotient_q6(pC27, pS27)

    # P^1(F_2): ((1,0), (0,1), (1,1)), C = [[1,1],[1,0]] -> (2,0,1), sigma = [[0,1],[1,0]] -> (1,0,2)
    pC_f2 = (2, 0, 1)
    pS_f2 = (1, 0, 2)
    qC_6f2 = prod_perm(qC6, pC_f2)
    qS_6f2 = prod_perm(qS6, pS_f2)
    pC_lvl30 = prod_perm(pC_f2, pC27)
    pS_lvl30 = prod_perm(pS_f2, pS27)

    # Exhaustive G_3 (216 elements) enumeration
    e3 = (
        tuple(range(len(pC27))),
        tuple(range(len(qC6))),
        tuple(range(len(pC12))),
        tuple(range(len(pC15))),
        tuple(range(len(qC_6f2))),
        tuple(range(len(pC9))),
    )
    gens3 = (
        ((pC27, qC6, pC12, pC15, qC_6f2, pC9), 2),
        ((pS27, qS6, pS12, pS15, qS_6f2, pS9), 3),
    )
    seen3 = {e3[0]: (e3, 0)}
    q3 = deque([e3])
    rho3_ok = True
    action3_consistent = True
    while q3:
        st = q3.popleft()
        r = seen3[st[0]][1]
        for gtuple, dr in gens3:
            nst = tuple(comp_perm(gtuple[k], st[k]) for k in range(6))
            nr = (r + dr) % 6
            if nst[0] not in seen3:
                seen3[nst[0]] = (nst, nr)
                q3.append(nst)
            else:
                if seen3[nst[0]][1] != nr:
                    rho3_ok = False
                if seen3[nst[0]][0] != nst:
                    action3_consistent = False

    g3_order = len(seen3)
    g3_rho_ne_1 = sum(1 for _, r in seen3.values() if r != 0)
    m6_order = sum(1 for st, _ in seen3.values() if st[1][0] == 0)
    mm_27_q6 = sum(1 for st, r in seen3.values() if r != 0 and fix_count(st[0]) != fix_count(st[1]))
    mm_12_q6 = sum(1 for st, r in seen3.values() if r != 0 and fix_count(st[2]) != fix_count(st[1]))
    mm_15_nonzero = sum(1 for st, r in seen3.values() if r != 0 and fix_count(st[3]) != 0)
    mm_6f2_nonzero = sum(1 for st, r in seen3.values() if r != 0 and fix_count(st[4]) != 0)
    mm_27_q8 = sum(1 for st, r in seen3.values() if r != 0 and fix_count(st[0]) != fix_count(st[5]))

    # Exhaustive G_4 (1,944 elements) enumeration
    e4 = (tuple(range(len(pC81))), tuple(range(len(qC6))))
    seen4 = {e4[0]: (e4, 0)}
    q4 = deque([e4])
    rho4_ok = True
    action4_consistent = True
    while q4:
        st = q4.popleft()
        r = seen4[st[0]][1]
        for (g81, g6), dr in (((pC81, qC6), 2), ((pS81, qS6), 3)):
            nst = (comp_perm(g81, st[0]), comp_perm(g6, st[1]))
            nr = (r + dr) % 6
            if nst[0] not in seen4:
                seen4[nst[0]] = (nst, nr)
                q4.append(nst)
            else:
                if seen4[nst[0]][1] != nr:
                    rho4_ok = False
                if seen4[nst[0]][0] != nst:
                    action4_consistent = False

    g4_order = len(seen4)
    g4_rho_ne_1 = sum(1 for _, r in seen4.values() if r != 0)
    mm_81_q6 = sum(1 for st, r in seen4.values() if r != 0 and fix_count(st[0]) != fix_count(st[1]))

    # Sector trace-moment defects Delta_{2m} for all 6 spaces + Q_8 control
    spaces = [
        ("Q6", qC6, qS6, 4),
        ("O27_333", pC27, pS27, 4),
        ("O27_3312", pC12, pS12, 4),
        ("O27_3315", pC15, pS15, 4),
        ("Level30_P1F2_x_O27_333", pC_lvl30, pS_lvl30, 4),
        ("O81_333", pC81, pS81, 3),
        ("Q8_control", pC9, pS9, 4),
    ]
    halving_spaces = {}
    q6_H0 = None
    q6_H1 = None
    for name, pC_sp, pS_sp, max_m in spaces:
        comm_ok, comm_nz, ncyc, H0, H1 = build_sector_operators(pC_sp, pS_sp, spL, spR, spC0)
        if name == "Q6":
            q6_H0, q6_H1 = H0, H1
        P0, P1 = H0, H1
        deltas = {}
        tr_H0 = {}
        tr_H1 = {}
        for m in range(1, max_m + 1):
            if m > 1:
                P0 = _sparse_mul_Z(P0, H0)
                P1 = _sparse_mul_Zw(P1, H1)
            t0 = _trace_sq_Z(P0)
            t1 = _trace_sq_Zw(P1)
            tr_H0[str(2 * m)] = int(t0)
            tr_H1[str(2 * m)] = int(t1)
            deltas[str(2 * m)] = int(t0 - (4 ** m) * t1)
        halving_spaces[name] = {
            "base_points": len(pC_sp),
            "dim_total": len(pC_sp) * 6,
            "dim_sector": ncyc,
            "commutator_Wp_Wm_zero": bool(comm_ok),
            "commutator_nonzero_entries": int(comm_nz),
            "tr_H0": tr_H0,
            "tr_H1": tr_H1,
            "Delta": deltas,
        }

    # Exact Q_6 x Leg(5) characteristic polynomials via pure-Z Faddeev-LeVerrier
    ncyc6 = 12
    M0 = [[q6_H0[i].get(j, 0) for j in range(ncyc6)] for i in range(ncyc6)]
    M12 = [[0] * (2 * ncyc6) for _ in range(2 * ncyc6)]
    for i in range(ncyc6):
        for j, (a, b) in q6_H1[i].items():
            # Regular representation of a + b*omega in basis (1, omega) where omega^2 = -1 - omega:
            M12[2 * i][2 * j] = a
            M12[2 * i][2 * j + 1] = -b
            M12[2 * i + 1][2 * j] = b
            M12[2 * i + 1][2 * j + 1] = a - b

    c_neu, flv_neu_ok = faddeev_leverrier_Z(M0)
    c_chg_sq, flv_chg_ok = faddeev_leverrier_Z(M12)
    c_chg = poly_exact_sqrt_Z(c_chg_sq)
    # P_{2,chg}(y) = 2^{12} * P_chg(y / 2) = sum c_chg[k] * 2^{12-k} * y^k
    c_2chg = [c_chg[k] * (2 ** (ncyc6 - k)) for k in range(ncyc6 + 1)]

    y = sp.Symbol("y")
    P_neu = sp.Poly(sum(c_neu[k] * (y ** k) for k in range(ncyc6 + 1)), y, domain="ZZ")
    P_2chg = sp.Poly(sum(c_2chg[k] * (y ** k) for k in range(ncyc6 + 1)), y, domain="ZZ")
    P_gcd = sp.gcd(P_neu, P_2chg)
    P_unpaired, rem_u = sp.div(P_2chg, P_gcd, domain="ZZ")
    P_leftover, rem_l = sp.div(P_neu, P_gcd, domain="ZZ")

    exp_gcd = sp.Poly((y ** 2 - 8) ** 2, y, domain="ZZ")
    exp_unpaired = sp.Poly(((y ** 2 - 6 * y + 4) ** 2) * ((y ** 2 + 6 * y + 4) ** 2), y, domain="ZZ")
    exp_leftover = sp.Poly(((y ** 2 - 20) ** 2) * ((y ** 2 - 8) ** 2), y, domain="ZZ")
    exp_neu = sp.Poly(((y ** 2 - 20) ** 2) * ((y ** 2 - 8) ** 4), y, domain="ZZ")
    exp_2chg = sp.Poly(((y ** 2 - 8) ** 2) * ((y ** 2 - 6 * y + 4) ** 2) * ((y ** 2 + 6 * y + 4) ** 2), y, domain="ZZ")

    # Verify halving defect matches universal Q_6 across O27_333, O27_3312, O81_333, and vanishes on O27_3315 & Level30
    d_q6 = halving_spaces["Q6"]["Delta"]
    match_o27_333 = (halving_spaces["O27_333"]["Delta"] == d_q6)
    match_o27_3312 = (halving_spaces["O27_3312"]["Delta"] == d_q6)
    match_o81_333 = all(halving_spaces["O81_333"]["Delta"][k] == d_q6[k] for k in ("2", "4", "6"))
    zero_o27_3315 = all(v == 0 for v in halving_spaces["O27_3315"]["Delta"].values())
    zero_lvl30 = all(v == 0 for v in halving_spaces["Level30_P1F2_x_O27_333"]["Delta"].values())
    q8_differs = (halving_spaces["Q8_control"]["Delta"] != d_q6)

    return {
        "orbits": {
            "O27_333": {"size": len(pts27_333), "fix_C_tr": fixC27, "matches_LR_generators": bool(lr27)},
            "O27_3312": {"size": len(pts27_3312), "fix_C_tr": fixC12, "matches_LR_generators": bool(lr12)},
            "O27_3315": {"size": len(pts27_3315), "fix_C_tr": fixC15, "matches_LR_generators": bool(lr15)},
            "O81_333": {"size": len(pts81_333), "fix_C_tr": fixC81, "matches_LR_generators": bool(lr81)},
            "Q6": {"size": 6, "fix_C_tr": fixC_Q6, "index_in_G3": g3_order // m6_order, "M6_order": m6_order},
            "Q8": {"size": len(pts9_333), "fix_C_tr": fixC9, "matches_LR_generators": bool(lr9)},
            "O27_congruence_lattice_sizes": [[int(sz), int(cnt)] for sz, cnt in cong_sizes],
        },
        "Q6_x_Leg5_polynomials": {
            "faddeev_leverrier_H0_terminal_zero": bool(flv_neu_ok),
            "faddeev_leverrier_H1H2_terminal_zero": bool(flv_chg_ok),
            "P_neu_coeffs_low_to_high": [int(v) for v in c_neu],
            "P_chg_coeffs_low_to_high": [int(v) for v in c_chg],
            "P_2chg_coeffs_low_to_high": [int(v) for v in c_2chg],
            "P_neu_factored": str(sp.factor(P_neu.as_expr())),
            "P_2chg_factored": str(sp.factor(P_2chg.as_expr())),
            "gcd_factored": str(sp.factor(P_gcd.as_expr())),
            "UNPAIRED_factored": str(sp.factor(P_unpaired.as_expr())),
            "LEFTOVER_factored": str(sp.factor(P_leftover.as_expr())),
            "exact_P_neu_match": bool(P_neu == exp_neu),
            "exact_P_2chg_match": bool(P_2chg == exp_2chg),
            "exact_gcd_match": bool(P_gcd == exp_gcd),
            "exact_UNPAIRED_match": bool(P_unpaired == exp_unpaired and rem_u.is_zero),
            "exact_LEFTOVER_match": bool(P_leftover == exp_leftover and rem_l.is_zero),
        },
        "exhaustive_character_fixed_points": {
            "G3_order": int(g3_order),
            "G3_rho_ne_1_count": int(g3_rho_ne_1),
            "G3_rho_homomorphism_consistent": bool(rho3_ok),
            "G3_actions_consistent": bool(action3_consistent),
            "G3_mismatches_O27_333_vs_Q6": int(mm_27_q6),
            "G3_mismatches_O27_3312_vs_Q6": int(mm_12_q6),
            "G3_nonzero_fix_O27_3315": int(mm_15_nonzero),
            "G3_nonzero_fix_Q6_x_P1F2": int(mm_6f2_nonzero),
            "G3_mismatches_O27_333_vs_Q8": int(mm_27_q8),
            "G4_order": int(g4_order),
            "G4_rho_ne_1_count": int(g4_rho_ne_1),
            "G4_rho_homomorphism_consistent": bool(rho4_ok),
            "G4_actions_consistent": bool(action4_consistent),
            "G4_mismatches_O81_333_vs_Q6": int(mm_81_q6),
        },
        "halving_trace_moments": {
            "spaces": halving_spaces,
            "O27_333_matches_Q6": bool(match_o27_333),
            "O27_3312_matches_Q6": bool(match_o27_3312),
            "O81_333_matches_Q6": bool(match_o81_333),
            "O27_3315_all_zero": bool(zero_o27_3315),
            "Level30_all_zero": bool(zero_lvl30),
            "Q8_fails_to_match_Q6": bool(q8_differs),
        },
    }


# ---------------------------------------------------------------------------
# Module B2: Exact Chiral Walk Algebra on Leg(5)
# ---------------------------------------------------------------------------

def get_leg5_walk_and_bases():
    """Return exact symbolic operators and nested-radical-free orthogonal bases."""
    rL = leg5_rep_sym(MAT_L)
    rR = leg5_rep_sym(MAT_R)
    rC_om = leg5_rep_sym(MAT_C_OM)
    rC3 = leg5_rep_sym(MAT_C3)
    rMir = leg5_rep_sym(MAT_TAU_MIR)
    rS = leg5_rep_sym(MAT_S)

    W_L = rL + rC_om * rL * rC_om.T + (rC_om ** 2) * rL * rC_om
    W_R = rR + rC_om * rR * rC_om.T + (rC_om ** 2) * rR * rC_om
    W_6 = W_L + W_R

    s3 = sp.sqrt(3)
    s5 = sp.sqrt(5)
    s15 = s3 * s5
    # Equal-norm orthogonal vectors in Q(sqrt(3), sqrt(5)): ||Ep||^2 = ||Em||^2 = 5 - sqrt(5)
    # Normalized e_+ = Ep / sqrt(5 - sqrt(5)), e_- = Em / sqrt(5 - sqrt(5))
    # satisfies e_{+,6} > 0 and e_{-,4} = e_{-,5} > 0.
    norm2_g = 5 - s5
    Ep = sp.Matrix([(-s3 + s15) / 6, (-s3 + s15) / 6, (-s15 + s3) / 3, -s3 / 3, s3 / 3, 2 * s3 / 3])
    Em = sp.Matrix([(1 - s5) / 2, (-1 + s5) / 2, 0, 1, 1, 0])

    # Galois conjugate for E_{phi^-2}: ||Fp||^2 = ||Fm||^2 = 5 + sqrt(5)
    norm2_s = 5 + s5
    Fp = sp.Matrix([(-s3 - s15) / 6, (-s3 - s15) / 6, (s15 + s3) / 3, -s3 / 3, s3 / 3, 2 * s3 / 3])
    Fm = sp.Matrix([(1 + s5) / 2, (-1 - s5) / 2, 0, 1, 1, 0])

    return {
        "rL": rL, "rR": rR, "rC_om": rC_om, "rC3": rC3, "rMir": rMir, "rS": rS,
        "W_L": W_L, "W_R": W_R, "W_6": W_6,
        "Ep": Ep, "Em": Em, "norm2_g": norm2_g,
        "Fp": Fp, "Fm": Fm, "norm2_s": norm2_s,
    }


def run_module_b2():
    obj = get_leg5_walk_and_bases()
    W_L = obj["W_L"]
    W_R = obj["W_R"]
    W_6 = obj["W_6"]
    rC3 = obj["rC3"]
    rMir = obj["rMir"]
    Ep, Em, norm2_g = obj["Ep"], obj["Em"], obj["norm2_g"]
    Fp, Fm, norm2_s = obj["Fp"], obj["Fm"], obj["norm2_s"]

    s3 = sp.sqrt(3)
    s5 = sp.sqrt(5)
    phi2 = (3 + s5) / 2
    phim2 = (3 - s5) / 2
    J = sp.I * (W_L - W_R)
    sigma_y = sp.Matrix([[0, -sp.I], [sp.I, 0]])

    # Exact integer Faddeev-LeVerrier for W_6 and W_L
    M_W6 = [[int(W_6[i, j]) for j in range(6)] for i in range(6)]
    M_WL = [[int(W_L[i, j]) for j in range(6)] for i in range(6)]
    c_W6, ok_flv_W6 = faddeev_leverrier_Z(M_W6)
    c_WL, ok_flv_WL = faddeev_leverrier_Z(M_WL)
    # For J = i (W_L - W_R): let A = W_L - W_R (skew-symmetric integer matrix).
    # det(lam I - i A) = (-i)^6 det(i lam I - A) = -det(i lam I - A) -> if det(x I - A) = sum a_k x^k,
    # then det(lam I - i A) = sum a_k i^{k-6} lam^k (a_k=0 for odd k since A is skew-symmetric!).
    A_skew = W_L - W_R
    M_A = [[int(A_skew[i, j]) for j in range(6)] for i in range(6)]
    c_A, ok_flv_A = faddeev_leverrier_Z(M_A)
    c_J = []
    for k in range(7):
        if k % 2 == 1:
            if c_A[k] != 0:
                raise AssertionError("Skew-symmetric matrix has odd charpoly term")
            c_J.append(0)
        else:
            # i^{k-6} for even k: (k-6)//2 mod 2 gives sign
            sgn = 1 if (((k - 6) // 2) % 2 == 0) else -1
            c_J.append(sgn * c_A[k])

    lam = sp.Symbol("lambda")
    poly_W6 = sp.Poly(sum(c_W6[k] * (lam ** k) for k in range(7)), lam, domain="ZZ")
    poly_WL = sp.Poly(sum(c_WL[k] * (lam ** k) for k in range(7)), lam, domain="ZZ")
    poly_J = sp.Poly(sum(c_J[k] * (lam ** k) for k in range(7)), lam, domain="ZZ")

    exp_W6 = sp.Poly((lam ** 2 - 20) * ((lam ** 2 - 3 * lam + 1) ** 2), lam, domain="ZZ")
    exp_WL = sp.Poly((lam ** 2 - 5) * (lam ** 4 - 3 * lam ** 3 + 8 * lam ** 2 - 3 * lam + 1), lam, domain="ZZ")
    exp_J = sp.Poly((lam ** 2) * (lam ** 4 - 21 * lam ** 2 + 9), lam, domain="ZZ")

    # Verify eigenbasis & sign conventions
    Bg = sp.Matrix.hstack(Ep, Em)
    Bs = sp.Matrix.hstack(Fp, Fm)

    gold_orth_ok = mat_zero(Bg.T * Bg - norm2_g * sp.eye(2))
    silv_orth_ok = mat_zero(Bs.T * Bs - norm2_s * sp.eye(2))
    gold_eval_ok = mat_zero(W_6 * Bg - phi2 * Bg)
    silv_eval_ok = mat_zero(W_6 * Bs - phim2 * Bs)
    gold_mir_ok = mat_zero(rMir * Ep - Ep) and mat_zero(rMir * Em + Em)
    silv_mir_ok = mat_zero(rMir * Fp - Fp) and mat_zero(rMir * Fm + Fm)
    ep_sign_ok = bool(sp.simplify(Ep[5]) > 0)
    em_sign_ok = bool(Em[3] == Em[4] and Em[3] > 0)

    pauli_gold_ok = mat_zero(Bg.T * J * Bg - norm2_g * s3 * phi2 * sigma_y)
    pauli_silv_ok = mat_zero(Bs.T * J * Bs - norm2_s * s3 * phim2 * sigma_y)
    wl_gold_ok = mat_zero(Bg.T * W_L * Bg + phi2 * (Bg.T * (rC3 ** 2) * Bg))

    # Chiral poles: chi_pm = (Ep +- i Em) / sqrt(2 * norm2_g)
    chiral_checks = {}
    w = sp.Rational(-1, 2) + sp.I * s3 / 2
    w2 = sp.Rational(-1, 2) - sp.I * s3 / 2
    for label, sgn, exp_c3_ev in (("plus_i", 1, w2), ("minus_i", -1, w)):
        v = Ep + sgn * sp.I * Em
        denom = 2 * norm2_g
        probs = [sp.expand(sp.radsimp(sp.expand(v[k] * sp.conjugate(v[k])) / denom)) for k in range(6)]
        sum_p = sp.expand(sum(probs))
        I4 = sp.expand(sp.radsimp(sum(p ** 2 for p in probs)))
        I6 = sp.expand(sp.radsimp(sum(p ** 3 for p in probs)))
        c3_ev_ok = mat_zero(rC3 * v - exp_c3_ev * v)
        chiral_checks[label] = {
            "sum_probs_is_1": bool(sum_p == 1),
            "I4_exact": str(I4),
            "I6_exact": str(I6),
            "I4_eq_1_5": bool(I4 == sp.Rational(1, 5)),
            "I6_eq_2_45": bool(I6 == sp.Rational(2, 45)),
            "C3_eigenstate_verified": bool(c3_ev_ok),
            "probabilities_exact": [str(p) for p in probs],
        }

    return {
        "algebraic_identities": {
            "W_R_eq_W_L_transpose": bool(W_R == W_L.T),
            "comm_W_L_W_R_zero": bool(W_L * W_R == W_R * W_L),
            "comm_W_L_C3_zero": bool(W_L * rC3 == rC3 * W_L),
            "tau_mir_W_L_tau_mir_eq_W_R": bool(rMir * W_L * rMir == W_R),
        },
        "characteristic_polynomials": {
            "flv_terminal_zeros_ok": bool(ok_flv_W6 and ok_flv_WL and ok_flv_A),
            "W6_coeffs": [int(v) for v in c_W6],
            "WL_coeffs": [int(v) for v in c_WL],
            "i_WL_minus_WR_coeffs": [int(v) for v in c_J],
            "W6_factored": str(sp.factor(poly_W6.as_expr())),
            "WL_factored": str(sp.factor(poly_WL.as_expr())),
            "i_WL_minus_WR_factored": str(sp.factor(poly_J.as_expr())),
            "W6_exact_match": bool(poly_W6 == exp_W6),
            "WL_exact_match": bool(poly_WL == exp_WL),
            "i_WL_minus_WR_exact_match": bool(poly_J == exp_J),
        },
        "eigenbasis_and_pauli": {
            "gold_basis_orthogonal_verified": bool(gold_orth_ok),
            "silv_basis_orthogonal_verified": bool(silv_orth_ok),
            "gold_eigenvalue_phi2_verified": bool(gold_eval_ok),
            "silv_eigenvalue_phim2_verified": bool(silv_eval_ok),
            "gold_mirror_parity_verified": bool(gold_mir_ok),
            "silv_mirror_parity_verified": bool(silv_mir_ok),
            "e_plus_6_positive": bool(ep_sign_ok),
            "e_minus_4_eq_5_positive": bool(em_sign_ok),
            "pauli_gold_eq_sqrt3_phi2_sigma_y": bool(pauli_gold_ok),
            "pauli_silv_eq_sqrt3_phim2_sigma_y": bool(pauli_silv_ok),
            "WL_gold_eq_neg_phi2_C3_sq": bool(wl_gold_ok),
        },
        "chiral_poles": chiral_checks,
    }


# ---------------------------------------------------------------------------
# Disjoint Special Functions: Jacobi theta_1 + Euler Pentagonal eta & E_2
# ---------------------------------------------------------------------------

def theta1_series(z, tau, need_derivs=False):
    """
    Jacobi theta_1(pi z, tau) = 2 sum_{n>=0} (-1)^n q_jac^{(n+1/2)^2} sin((2n+1) pi z),
    with q_jac = exp(i pi tau). Returns theta_1 (and d/dz, d^2/dz^2 if need_derivs).
    """
    pi = mp.pi
    tol = mp.power(10, -(mp.mp.dps + 12))
    s0 = mp.mpc(0)
    s1 = mp.mpc(0)
    s2 = mp.mpc(0)
    n = 0
    while True:
        m = 2 * n + 1
        tq = mp.exp(I_MP * pi * tau * (m * m) / 4)
        ang = m * pi * z
        # Bound term magnitude carefully when Im(z) != 0 using exp(|Im(ang)|)
        if abs(tq) * mp.exp(abs(mp.im(ang))) * (m * m) < tol and n > 5:
            break
        sgn = 2 if (n % 2 == 0) else -2
        sn = mp.sin(ang)
        s0 += sgn * tq * sn
        if need_derivs:
            cs = mp.cos(ang)
            mp_fac = m * pi
            s1 += sgn * tq * mp_fac * cs
            s2 -= sgn * tq * (mp_fac * mp_fac) * sn
        n += 1
        if n > 2000:
            raise RuntimeError("theta1_series did not converge")
    if need_derivs:
        return s0, s1, s2
    return s0


def eta_and_E2_pentagonal(tau, need_E2=False):
    """
    Dedekind eta(tau) = q^{1/24} P(q) via Euler's pentagonal number theorem
    P(q) = 1 + sum_{k>=1} (-1)^k (q^{k(3k-1)/2} + q^{k(3k+1)/2}),
    and E_2(tau) = 1 + 24 q P'(q) / P(q).
    """
    pi = mp.pi
    tol = mp.power(10, -(mp.mp.dps + 12))
    q = mp.exp(2 * I_MP * pi * tau)
    P = mp.mpc(1)
    qPp = mp.mpc(0)
    k = 1
    while True:
        e1 = (k * (3 * k - 1)) // 2
        e2 = (k * (3 * k + 1)) // 2
        q1 = mp.power(q, e1)
        q2 = mp.power(q, e2)
        if abs(q1) * e1 < tol and k > 5:
            break
        sgn = -1 if (k % 2 == 1) else 1
        P += sgn * (q1 + q2)
        if need_E2:
            qPp += sgn * (e1 * q1 + e2 * q2)
        k += 1
        if k > 2000:
            raise RuntimeError("eta_and_E2_pentagonal did not converge")
    eta = mp.exp(I_MP * pi * tau / 12) * P
    if need_E2:
        E2 = 1 + 24 * qPp / P
        return eta, E2
    return eta


def F_siegel_theta_eta(a, b, tau, eta_cached=None):
    """
    F_Siegel(a, b; tau) = -ln|g_{a,b}(tau)|, where
    |g_{a,b}(tau)| = exp(-pi y a^2) |theta_1(pi(a tau + b), tau) / eta(tau)|.
    Exact invariance under (a, b) -> (a + 1, b), (a, b + 1), (-a, -b).
    """
    y = mp.im(tau)
    eta = eta_cached if eta_cached is not None else eta_and_E2_pentagonal(tau, need_E2=False)
    th = theta1_series(a * tau + b, tau, need_derivs=False)
    return mp.pi * y * a * a - mp.log(abs(th / eta))


def wp_theta_pentagonal(z, tau, E2_cached=None):
    """Weierstrass wp(z; tau) = -(theta_1''/theta_1 - (theta_1'/theta_1)^2) - (pi^2/3) E_2(tau)."""
    th, th1, th2 = theta1_series(z, tau, need_derivs=True)
    if E2_cached is None:
        _, E2_cached = eta_and_E2_pentagonal(tau, need_E2=True)
    return -(th2 / th - (th1 / th) ** 2) - (mp.pi ** 2 / 3) * E2_cached


def build_mp_bases_and_projectors():
    rS = leg5_rep_mp(MAT_S)
    rT = leg5_rep_mp(MAT_L)
    rC3 = leg5_rep_mp(MAT_C3)
    rMir = leg5_rep_mp(MAT_TAU_MIR)
    rL = rT
    rR = leg5_rep_mp(MAT_R)
    W_L = rL + rC3 * rL * rC3.T + (rC3 * rC3) * rL * rC3
    W_R = rR + rC3 * rR * rC3.T + (rC3 * rC3) * rR * rC3
    W_6 = W_L + W_R

    s3 = mp.sqrt(3)
    s5 = mp.sqrt(5)
    s15 = s3 * s5
    phi = (1 + s5) / 2
    phi2 = phi * phi
    phim2 = 1 / phi2
    den_g = mp.sqrt(5 - s5)
    ep = mp.matrix([
        (-s3 + s15) / (6 * den_g),
        (-s3 + s15) / (6 * den_g),
        (-s15 + s3) / (3 * den_g),
        -s3 / (3 * den_g),
        s3 / (3 * den_g),
        2 * s3 / (3 * den_g),
    ])
    em = mp.matrix([
        (1 - s5) / (2 * den_g),
        (-1 + s5) / (2 * den_g),
        mp.mpf(0),
        1 / den_g,
        1 / den_g,
        mp.mpf(0),
    ])

    evals = (2 * s5, -2 * s5, phi2, phim2)
    projs = []
    I6 = mp.eye(6)
    for idx, lam in enumerate(evals):
        P = mp.eye(6)
        for j, mu in enumerate(evals):
            if j != idx:
                P = P * (W_6 - mu * I6) / (lam - mu)
        projs.append(P)
    return {
        "rS": rS, "rT": rT, "rC3": rC3, "rMir": rMir, "W_6": W_6,
        "ep": ep, "em": em,
        "P_2s5": projs[0], "P_m2s5": projs[1], "P_gold": projs[2], "P_silv": projs[3],
    }


def phi_siegel_vec(tau, rS):
    """12-ray orthonormal projection Phi^{Siegel}_{Leg(5)}(tau) = rho(S) v^{Siegel}(tau)."""
    eta = eta_and_E2_pentagonal(tau, need_E2=False)
    inv_sqrt2 = 1 / mp.sqrt(2)
    v = mp.matrix(6, 1)
    for i, (c, d) in enumerate(P1_F5):
        f1 = F_siegel_theta_eta(mp.mpf(c) / 5, mp.mpf(d) / 5, tau, eta_cached=eta)
        f2 = F_siegel_theta_eta(mp.mpf(2 * c) / 5, mp.mpf(2 * d) / 5, tau, eta_cached=eta)
        v[i] = (f1 - f2) * inv_sqrt2
    return rS * v


def phi_wp_vec(tau, rS):
    """Weight-2 12-ray orthonormal projection Phi^{wp}_{Leg(5)}(tau) = rho(S) v^{wp}(tau)."""
    _, E2 = eta_and_E2_pentagonal(tau, need_E2=True)
    inv_sqrt2 = 1 / mp.sqrt(2)
    v = mp.matrix(6, 1)
    for i, (c, d) in enumerate(P1_F5):
        z1 = (mp.mpf(c) * tau + mp.mpf(d)) / 5
        z2 = (mp.mpf(2 * c) * tau + mp.mpf(2 * d)) / 5
        v[i] = (wp_theta_pentagonal(z1, tau, E2_cached=E2) - wp_theta_pentagonal(z2, tau, E2_cached=E2)) * inv_sqrt2
    return rS * v


def vec_invariants(psi):
    n2 = mp.fsum(abs(psi[k]) ** 2 for k in range(6))
    probs = [abs(psi[k]) ** 2 / n2 for k in range(6)]
    I4 = mp.fsum(p * p for p in probs)
    I6 = mp.fsum(p * p * p for p in probs)
    return n2, probs, I4, I6


# ---------------------------------------------------------------------------
# Module B3: Mirror-Lock Theorem, Siegel Map, Zero-Parameter Stabilization
# ---------------------------------------------------------------------------

def golden_section_min(fn, a, b, tol):
    gr = (mp.sqrt(5) - 1) / 2
    c = b - gr * (b - a)
    d = a + gr * (b - a)
    fc = fn(c)
    fd = fn(d)
    iters = 0
    while abs(b - a) > tol:
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - gr * (b - a)
            fc = fn(c)
        else:
            a, c, fc = c, d, fd
            d = a + gr * (b - a)
            fd = fn(d)
        iters += 1
        if iters > 500:
            break
    xm = (a + b) / 2
    return xm, fn(xm), iters


def hessian_5pt_richardson(fn, x0, y0, h):
    """
    5-point stencil 2nd derivatives with Richardson extrapolation (h and h/2):
      D2(h) = (-f(2h) + 16 f(h) - 30 f(0) + 16 f(-h) - f(-2h)) / (12 h^2) + O(h^4),
      D2_Rich = (16 D2(h/2) - D2(h)) / 15  (error O(h^6)).
    Also computes 2D cross-derivative f_xy via 4-corner central stencil + Richardson.
    """
    f0 = fn(x0, y0)

    def d2_x(step):
        return (
            -fn(x0 + 2 * step, y0)
            + 16 * fn(x0 + step, y0)
            - 30 * f0
            + 16 * fn(x0 - step, y0)
            - fn(x0 - 2 * step, y0)
        ) / (12 * step * step)

    def d2_y(step):
        return (
            -fn(x0, y0 + 2 * step)
            + 16 * fn(x0, y0 + step)
            - 30 * f0
            + 16 * fn(x0, y0 - step)
            - fn(x0, y0 - 2 * step)
        ) / (12 * step * step)

    def d2_xy(step):
        return (
            fn(x0 + step, y0 + step)
            - fn(x0 + step, y0 - step)
            - fn(x0 - step, y0 + step)
            + fn(x0 - step, y0 - step)
        ) / (4 * step * step)

    h2 = h / 2
    xx1, xx2 = d2_x(h), d2_x(h2)
    yy1, yy2 = d2_y(h), d2_y(h2)
    xy1, xy2 = d2_xy(h), d2_xy(h2)
    fxx = (16 * xx2 - xx1) / 15
    fyy = (16 * yy2 - yy1) / 15
    fxy = (4 * xy2 - xy1) / 3
    err_xx = abs(xx2 - xx1)
    err_yy = abs(yy2 - yy1)
    det_H = fxx * fyy - fxy * fxy
    return {
        "fxx": fxx, "fyy": fyy, "fxy": fxy, "det_H": det_H,
        "richardson_diff_xx": err_xx, "richardson_diff_yy": err_yy,
    }


def run_module_b3():
    # 1. Symbolic Mirror-Lock Theorem and cusp asymptotes
    obj = get_leg5_walk_and_bases()
    W_6 = obj["W_6"]
    rC3 = obj["rC3"]
    rMir = obj["rMir"]
    rS = obj["rS"]
    Ep = obj["Ep"]
    Em = obj["Em"]

    rM_circ = leg5_rep_sym(MAT_M_CIRC)
    rM_half = leg5_rep_sym(MAT_M_HALF)
    rM_c1 = leg5_rep_sym(MAT_M_C1)
    rR0 = leg5_rep_sym(MAT_R0)

    sym_mirror_lock = {
        "unit_circle_eq_tau_mir": bool(rM_circ == rMir),
        "re_half_eq_C3_mir_C3inv": bool(rM_half == rC3 * rMir * rC3.T),
        "unit_c1_eq_C3sq_mir_C3m2": bool(rM_c1 == (rC3 ** 2) * rMir * (rC3.T ** 2)),
        "unit_circle_commutes_W6": bool(rM_circ * W_6 == W_6 * rM_circ),
        "re_half_commutes_W6": bool(rM_half * W_6 == W_6 * rM_half),
        "unit_c1_commutes_W6": bool(rM_c1 * W_6 == W_6 * rM_c1),
        "R0_commutes_W6": bool(rR0 * W_6 == W_6 * rR0),
        "R0_comm_W6_frob_sq": int(mat_frob_sq_int(rR0 * W_6 - W_6 * rR0)),
    }

    s3 = sp.sqrt(3)
    cusp_sym = {}
    for cname, vec in (("v_linear_101111", sp.Matrix([1, 0, 1, 1, 1, 1])), ("v_const_010000", sp.Matrix([0, 1, 0, 0, 0, 0]))):
        w_vec = rS * vec
        cp = sp.expand((Ep.T * w_vec)[0])
        cm = sp.expand((Em.T * w_vec)[0])
        ratio_ok = z_expand_zero(cm + s3 * cp)
        cusp_sym[cname] = {
            "c_minus_over_c_plus_eq_neg_sqrt3": bool(ratio_ok),
            "ratio_exact": "-sqrt(3)" if ratio_ok else str(sp.simplify(cm / cp)),
            "angle_deg_exact": "-60",
        }

    # 2. High-precision Siegel evaluations at dps = 60
    mp.mp.dps = 60
    mpb = build_mp_bases_and_projectors()
    rS_mp = mpb["rS"]
    rT_mp = mpb["rT"]
    ep_mp = mpb["ep"]
    em_mp = mpb["em"]
    P_gold = mpb["P_gold"]

    tau0 = mp.mpc(mp.mpf(3) / 10, mp.mpf(13) / 10)

    # Quasi-periodicity check of F_siegel(a, b; tau)
    a_test = mp.mpf(1) / 5
    b_test = mp.mpf(2) / 5
    f_base = F_siegel_theta_eta(a_test, b_test, tau0)
    qp_a_shift = abs(F_siegel_theta_eta(a_test + 1, b_test, tau0) - f_base)
    qp_b_shift = abs(F_siegel_theta_eta(a_test, b_test + 1, tau0) - f_base)
    qp_neg = abs(F_siegel_theta_eta(-a_test, -b_test, tau0) - f_base)

    # SL(2, Z) equivariance at tau_0
    psi0 = phi_siegel_vec(tau0, rS_mp)
    psi_T = phi_siegel_vec(tau0 + 1, rS_mp)
    psi_S = phi_siegel_vec(-1 / tau0, rS_mp)
    T_err = mp.norm(psi_T - rT_mp * psi0)
    S_err = mp.norm(psi_S - rS_mp * psi0)
    n2_0, _, I4_0, I6_0 = vec_invariants(psi0)
    n2_T, _, I4_T, I6_T = vec_invariants(psi_T)
    n2_S, _, I4_S, I6_S = vec_invariants(psi_S)

    # Anti-holomorphic mirror equivariance at tau_0
    rM_circ_mp = leg5_rep_mp(MAT_M_CIRC)
    rM_half_mp = leg5_rep_mp(MAT_M_HALF)
    rM_c1_mp = leg5_rep_mp(MAT_M_C1)
    rR0_mp = leg5_rep_mp(MAT_R0)
    tau0_bar = mp.conj(tau0)
    antihol_errs = {
        "unit_circle_err": fmt_mp(mp.norm(phi_siegel_vec(1 / tau0_bar, rS_mp) - rM_circ_mp * psi0)),
        "re_half_err": fmt_mp(mp.norm(phi_siegel_vec(1 - tau0_bar, rS_mp) - rM_half_mp * psi0)),
        "unit_c1_err": fmt_mp(mp.norm(phi_siegel_vec(tau0_bar / (tau0_bar - 1), rS_mp) - rM_c1_mp * psi0)),
        "R0_err": fmt_mp(mp.norm(phi_siegel_vec(-tau0_bar, rS_mp) - rR0_mp * psi0)),
    }

    def eval_siegel_point(tau):
        psi = phi_siegel_vec(tau, rS_mp)
        n2, _, I4, I6 = vec_invariants(psi)
        cp = mp.re((ep_mp.T * psi)[0])
        cm = mp.re((em_mp.T * psi)[0])
        pg = P_gold * psi
        ng2 = mp.fsum(abs(pg[k]) ** 2 for k in range(6))
        gold_frac = ng2 / n2
        th_deg = mp.atan2(cm, cp) * 180 / mp.pi
        if ng2 > mp.mpf("1e-35"):
            _, _, I4g, I6g = vec_invariants(pg)
        else:
            I4g, I6g = mp.mpf(0), mp.mpf(0)
        return {
            "tau": fmt_mpc(tau),
            "norm2_ray12": fmt_mp(n2),
            "norm2_diff": fmt_mp(2 * n2),
            "gold_frac": fmt_mp(gold_frac),
            "theta_deg": fmt_mp(th_deg),
            "I4": fmt_mp(I4),
            "I6": fmt_mp(I6),
            "I4_gold": fmt_mp(I4g),
            "I6_gold": fmt_mp(I6g),
            "I6_gold_minus_11_90": fmt_mp(abs(I6g - mp.mpf(11) / 90)),
            "I6_gold_minus_1_10": fmt_mp(abs(I6g - mp.mpf(1) / 10)),
            "_n2": n2,
            "_gold_frac": gold_frac,
            "_th_deg": th_deg,
            "_I6g": I6g,
        }

    om_plus = mp.mpc(mp.mpf(1) / 2, mp.sqrt(3) / 2)
    tau_i = I_MP
    tau_5pi12 = mp.exp(I_MP * 5 * mp.pi / 12)
    tau_tot70 = mp.mpc(mp.mpf(1) / 2, mp.mpf("3.380451106"))
    tau_cusp_0 = mp.mpc(0, 15)
    tau_cusp_half = mp.mpc(mp.mpf(1) / 2, 15)

    pt_om = eval_siegel_point(om_plus)
    pt_i = eval_siegel_point(tau_i)
    pt_5pi12 = eval_siegel_point(tau_5pi12)
    pt_tot70 = eval_siegel_point(tau_tot70)
    pt_cusp0 = eval_siegel_point(tau_cusp_0)
    pt_cusph = eval_siegel_point(tau_cusp_half)

    # Illinois secant root-finder for y_odd* on Re(tau) = 0 where theta = -30 deg (cm + cp/sqrt(3) = 0)
    def g_odd(y_val):
        psi = phi_siegel_vec(mp.mpc(0, y_val), rS_mp)
        cp = mp.re((ep_mp.T * psi)[0])
        cm = mp.re((em_mp.T * psi)[0])
        return cm + cp / mp.sqrt(3)

    a_ill = mp.mpf(12) / 10
    b_ill = mp.mpf(14) / 10
    fa_ill = g_odd(a_ill)
    fb_ill = g_odd(b_ill)
    side = 0
    ill_iters = 0
    c_ill = a_ill
    tol_ill = mp.mpf("1e-45")
    for ill_iters in range(1, 200):
        c_ill = (a_ill * fb_ill - b_ill * fa_ill) / (fb_ill - fa_ill)
        fc_ill = g_odd(c_ill)
        if abs(fc_ill) < tol_ill or abs(b_ill - a_ill) < tol_ill:
            break
        if fa_ill * fc_ill < 0:
            b_ill, fb_ill = c_ill, fc_ill
            if side == -1:
                fa_ill = fa_ill / 2
            side = -1
        else:
            a_ill, fa_ill = c_ill, fc_ill
            if side == 1:
                fb_ill = fb_ill / 2
            side = 1

    pt_yodd = eval_siegel_point(mp.mpc(0, c_ill))

    # 3. 2D Global Interior Minima & 5-Point Richardson Hessians at dps = 50
    mp.mp.dps = 50
    rS_50 = leg5_rep_mp(MAT_S)

    def I4_xy(x_val, y_val):
        psi = phi_siegel_vec(mp.mpc(x_val, y_val), rS_50)
        _, _, I4v, _ = vec_invariants(psi)
        return I4v

    def I6_xy(x_val, y_val):
        psi = phi_siegel_vec(mp.mpc(x_val, y_val), rS_50)
        _, _, _, I6v = vec_invariants(psi)
        return I6v

    tol_opt = mp.mpf("1e-26")
    h_hess = mp.mpf("1e-5")
    y_lo = mp.mpf(15) / 10
    y_hi = mp.mpf(35) / 10
    x_zero = mp.mpf(0)
    x_half = mp.mpf(1) / 2

    y_I4_half, val_I4_half, it_I4_h = golden_section_min(lambda y: I4_xy(x_half, y), y_lo, y_hi, tol_opt)
    H_I4_half = hessian_5pt_richardson(I4_xy, x_half, y_I4_half, h_hess)

    y_I4_zero, val_I4_zero, it_I4_z = golden_section_min(lambda y: I4_xy(x_zero, y), y_lo, y_hi, tol_opt)
    H_I4_zero = hessian_5pt_richardson(I4_xy, x_zero, y_I4_zero, h_hess)

    y_I6_zero, val_I6_zero, it_I6_z = golden_section_min(lambda y: I6_xy(x_zero, y), y_lo, y_hi, tol_opt)
    H_I6_zero = hessian_5pt_richardson(I6_xy, x_zero, y_I6_zero, h_hess)

    y_I6_half, val_I6_half, it_I6_h = golden_section_min(lambda y: I6_xy(x_half, y), y_lo, y_hi, tol_opt)
    H_I6_half = hessian_5pt_richardson(I6_xy, x_half, y_I6_half, h_hess)

    # Coarse fundamental-domain 2D sweep (dps = 30) to confirm global minimum status
    mp.mp.dps = 30
    rS_30 = leg5_rep_mp(MAT_S)
    sweep_min_I4 = mp.mpf(10)
    sweep_min_I6 = mp.mpf(10)
    sweep_pts = 0
    for xi in range(6):
        xv = mp.mpf(xi) / 10
        y_min_bound = mp.sqrt(1 - xv * xv)
        for yi in range(9, 51, 2):
            yv = mp.mpf(yi) / 10
            if yv < y_min_bound:
                continue
            psi = phi_siegel_vec(mp.mpc(xv, yv), rS_30)
            _, _, i4v, i6v = vec_invariants(psi)
            if i4v < sweep_min_I4:
                sweep_min_I4 = i4v
            if i6v < sweep_min_I6:
                sweep_min_I6 = i6v
            sweep_pts += 1

    def strip_priv(d):
        return {k: v for k, v in d.items() if not k.startswith("_")}

    def fmt_hess(H):
        return {k: fmt_mp(v, 35) for k, v in H.items()}

    return {
        "symbolic_mirror_lock": sym_mirror_lock,
        "symbolic_cusp_asymptotes": cusp_sym,
        "quasi_periodicity_verification": {
            "a_plus_1_err": fmt_mp(qp_a_shift),
            "b_plus_1_err": fmt_mp(qp_b_shift),
            "negation_err": fmt_mp(qp_neg),
            "all_below_1e_45": bool(
                qp_a_shift < mp.mpf("1e-45") and qp_b_shift < mp.mpf("1e-45") and qp_neg < mp.mpf("1e-45")
            ),
        },
        "sl2z_equivariance_at_tau0": {
            "tau0": fmt_mpc(tau0),
            "T_err": fmt_mp(T_err),
            "S_err": fmt_mp(S_err),
            "T_and_S_below_1e_40": bool(T_err < mp.mpf("1e-40") and S_err < mp.mpf("1e-40")),
            "norm2_T_diff": fmt_mp(abs(n2_T - n2_0)),
            "norm2_S_diff": fmt_mp(abs(n2_S - n2_0)),
            "I4_T_diff": fmt_mp(abs(I4_T - I4_0)),
            "I4_S_diff": fmt_mp(abs(I4_S - I4_0)),
            "I6_T_diff": fmt_mp(abs(I6_T - I6_0)),
            "I6_S_diff": fmt_mp(abs(I6_S - I6_0)),
            "antiholomorphic_mirror_errs": antihol_errs,
        },
        "special_moduli": {
            "omega_plus": strip_priv(pt_om),
            "i": strip_priv(pt_i),
            "exp_i_5pi_12": strip_priv(pt_5pi12),
            "tau_tot_70": strip_priv(pt_tot70),
            "y_odd_star": {
                **strip_priv(pt_yodd),
                "y_odd_star": fmt_mp(c_ill),
                "illinois_iterations": int(ill_iters),
            },
            "cusp_15i": strip_priv(pt_cusp0),
            "cusp_half_plus_15i": strip_priv(pt_cusph),
            "checks": {
                "omega_gold_frac_lt_1e_40": bool(pt_om["_gold_frac"] < mp.mpf("1e-40")),
                "i_norm2_gt_omega_norm2": bool(pt_i["_n2"] > pt_om["_n2"]),
                "i_I6_gold_eq_11_90": bool(abs(pt_i["_I6g"] - mp.mpf(11) / 90) < mp.mpf("1e-40")),
                "exp_5pi12_I6_gold_eq_11_90": bool(abs(pt_5pi12["_I6g"] - mp.mpf(11) / 90) < mp.mpf("1e-40")),
                "tau_tot70_theta_eq_neg60": bool(abs(pt_tot70["_th_deg"] + 60) < mp.mpf("1e-40")),
                "tau_tot70_I6_gold_eq_11_90": bool(abs(pt_tot70["_I6g"] - mp.mpf(11) / 90) < mp.mpf("1e-40")),
                "y_odd_I6_gold_eq_1_10": bool(abs(pt_yodd["_I6g"] - mp.mpf(1) / 10) < mp.mpf("1e-40")),
            },
        },
        "interior_stabilization": {
            "tau_I4_star_on_x_half": {
                "x": "1/2",
                "y": fmt_mp(y_I4_half, 40),
                "I4_min": fmt_mp(val_I4_half, 40),
                "gss_iterations": int(it_I4_h),
                "hessian": fmt_hess(H_I4_half),
                "is_strict_2D_minimum": bool(H_I4_half["fxx"] > 0 and H_I4_half["fyy"] > 0 and H_I4_half["det_H"] > 0),
            },
            "I4_saddle_on_x_zero": {
                "x": "0",
                "y": fmt_mp(y_I4_zero, 40),
                "I4_val": fmt_mp(val_I4_zero, 40),
                "gss_iterations": int(it_I4_z),
                "hessian": fmt_hess(H_I4_zero),
                "is_x_saddle": bool(H_I4_zero["fxx"] < 0 and H_I4_zero["fyy"] > 0),
                "higher_than_x_half_min": bool(val_I4_zero > val_I4_half),
            },
            "tau_I6_star_on_x_zero": {
                "x": "0",
                "y": fmt_mp(y_I6_zero, 40),
                "I6_min": fmt_mp(val_I6_zero, 40),
                "gss_iterations": int(it_I6_z),
                "hessian": fmt_hess(H_I6_zero),
                "is_strict_2D_minimum": bool(H_I6_zero["fxx"] > 0 and H_I6_zero["fyy"] > 0 and H_I6_zero["det_H"] > 0),
            },
            "I6_saddle_on_x_half": {
                "x": "1/2",
                "y": fmt_mp(y_I6_half, 40),
                "I6_val": fmt_mp(val_I6_half, 40),
                "gss_iterations": int(it_I6_h),
                "hessian": fmt_hess(H_I6_half),
                "is_x_saddle": bool(H_I6_half["fxx"] < 0 and H_I6_half["fyy"] > 0),
                "higher_than_x_zero_min": bool(val_I6_half > val_I6_zero),
            },
            "fundamental_domain_sweep": {
                "grid_points": int(sweep_pts),
                "sweep_min_I4": fmt_mp(sweep_min_I4, 25),
                "sweep_min_I6": fmt_mp(sweep_min_I6, 25),
                "no_lower_I4_found": bool(val_I4_half <= sweep_min_I4 + mp.mpf("1e-20")),
                "no_lower_I6_found": bool(val_I6_zero <= sweep_min_I6 + mp.mpf("1e-20")),
            },
        },
        "_raw_I4_xx_zero": H_I4_zero["fxx"],
    }


# ---------------------------------------------------------------------------
# Module B4: Weight-2 Holomorphic Weierstrass Map & Exact 5-Division Poly
# ---------------------------------------------------------------------------

def run_module_b4():
    # 1. Disjoint symbolic 5-division polynomial via chord-and-tangent x([2]P) = x([3]P)
    x, u, d, D = sp.symbols("x u d D")
    # Curve E_{omega_+}: Y^2 = 4 X^3 - 1
    # Doubling: tangent slope m2 = 6 x^2 / y -> x2 = m2^2 / 4 - 2 x = 9 x^4 / (4 x^3 - 1) - 2 x
    x2 = sp.cancel(9 * (x ** 4) / (4 * (x ** 3) - 1) - 2 * x)
    # y2 / y = -(1 + 6 x^2 (x2 - x) / (4 x^3 - 1))
    y2_over_y = sp.cancel(-(1 + 6 * (x ** 2) * (x2 - x) / (4 * (x ** 3) - 1)))
    # Tripling [3]P = [2]P + P: m3 = y (y2/y - 1) / (x2 - x) -> x3 = m3^2 / 4 - x - x2
    x3 = sp.cancel((4 * (x ** 3) - 1) / 4 * (((y2_over_y - 1) / (x2 - x)) ** 2) - x - x2)
    diff23 = sp.cancel(x2 - x3)
    num_5div, _ = sp.fraction(diff23)
    poly_5div = sp.Poly(num_5div, x, domain="ZZ")
    # Ensure positive leading coefficient
    if poly_5div.LC() < 0:
        poly_5div = -poly_5div

    # Express in u = x^3
    all_deg_mod3 = all(deg[0] % 3 == 0 for deg, _ in poly_5div.terms())
    if not all_deg_mod3:
        raise AssertionError("5-division polynomial not a polynomial in x^3")
    P_u = sp.Poly(sum(c * (u ** (deg[0] // 3)) for deg, c in poly_5div.terms()), u, domain="ZZ")
    exp_P_u = sp.Poly(5 * (u ** 4) - 95 * (u ** 3) - 15 * (u ** 2) + 25 * u - 1, u, domain="ZZ")

    # Difference cube d = (x - x2)^3 = u * (3 (u - 1) / (4 u - 1))^3
    # Eliminate u via resultant over Z[u, d]
    res_d = sp.resultant(P_u.as_expr(), d * ((4 * u - 1) ** 3) - 27 * u * ((u - 1) ** 3), u)
    poly_d_prim = sp.Poly(res_d, d, domain="ZZ").primitive()[1]
    exp_d_prim = sp.Poly(5 * (d ** 4) - 270 * (d ** 2) + 729, d, domain="ZZ")

    # Quadratic in D = d^2 = |x - x2|^6
    s5 = sp.sqrt(5)
    phi = (1 + s5) / 2
    poly_D = 5 * (D ** 2) - 270 * D + 729
    D_s = 27 - sp.Rational(54, 5) * s5
    D_c = 27 + sp.Rational(54, 5) * s5
    roots_D_ok = z_expand_zero(poly_D.subs(D, D_s)) and z_expand_zero(poly_D.subs(D, D_c))
    # Prove u_s / u_c = phi^{-1} via D_s / D_c = phi^{-6} (since u_s, u_c > 0)
    ratio_phi6_ok = z_expand_zero(D_s / D_c - phi ** (-6))
    # Prove D_c = 5 * (3 / (1 + phi^{-2}))^3 and D_s = 5 * (3 phi^{-2} / (1 + phi^{-2}))^3
    # hence u_c^2 + u_s^2 = 3 * 5^{1/3} and V_wp(omega_+) = (27/8) * 5^{1/3} * |g_3(omega_+)|^{2/3}
    phim2 = (3 - s5) / 2
    Dc_cube_ok = z_expand_zero(D_c - 5 * ((3 / (1 + phim2)) ** 3))
    Ds_cube_ok = z_expand_zero(D_s - 5 * ((3 * phim2 / (1 + phim2)) ** 3))
    sum_u2_coeff_ok = z_expand_zero(3 / (1 + phim2) + 3 * phim2 / (1 + phim2) - 3)

    # Symbolic 0 : 0 : 4/5 : 1/5 norm partition & chiral pole at omega_+
    obj = get_leg5_walk_and_bases()
    rC3 = obj["rC3"]
    W_6 = obj["W_6"]
    Ep, Em, norm2_g = obj["Ep"], obj["Em"], obj["norm2_g"]
    Fp, Fm, norm2_s = obj["Fp"], obj["Fm"], obj["norm2_s"]

    s3 = sp.sqrt(3)
    w = sp.Rational(-1, 2) + sp.I * s3 / 2
    w2 = sp.Rational(-1, 2) - sp.I * s3 / 2
    phim1 = (s5 - 1) / 2
    # Exact omega_+ vector up to overall constant u_c * g_3^{1/3} / sqrt(2):
    v_om = sp.Matrix([1, w2, w, -phim1, phim1 * w2, -phim1 * w])
    v_om_c3_ok = mat_zero(rC3 * v_om - w * v_om)
    # Orthogonal to 1D E_{+-2sqrt(5)} eigenspaces (since those have C_3 eigenvalue +1 != w)
    # Verify explicitly via projectors (W_6 - phi^2 I)(W_6 - phi^-2 I) v_om == 0!
    phi2 = (3 + s5) / 2
    I6 = sp.eye(6)
    in_gold_plus_silv = mat_zero((W_6 - phi2 * I6) * (W_6 - phim2 * I6) * v_om)

    n2_om = sp.expand((v_om.H * v_om)[0])
    cp_om = sp.expand((Ep.T * v_om)[0])
    cm_om = sp.expand((Em.T * v_om)[0])
    fp_om = sp.expand((Fp.T * v_om)[0])
    fm_om = sp.expand((Fm.T * v_om)[0])
    g_num = sp.expand(cp_om * sp.conjugate(cp_om) + cm_om * sp.conjugate(cm_om))
    s_num = sp.expand(fp_om * sp.conjugate(fp_om) + fm_om * sp.conjugate(fm_om))
    part_gold_4_5 = z_expand_zero(5 * g_num - 4 * norm2_g * n2_om)
    part_silv_1_5 = z_expand_zero(5 * s_num - 1 * norm2_s * n2_om)
    chiral_pole_om_ok = z_expand_zero(cm_om + sp.I * cp_om)  # cm / cp = -i -> theta=45 deg, alpha=-90 deg

    probs_om_sym = [sp.expand(sp.radsimp(sp.expand(v_om[k] * sp.conjugate(v_om[k])) / n2_om)) for k in range(6)]
    I4_om_sym = sp.expand(sp.radsimp(sum(p ** 2 for p in probs_om_sym)))
    I6_om_sym = sp.expand(sp.radsimp(sum(p ** 3 for p in probs_om_sym)))

    # 2. High-precision numerical verification via theta_1 + pentagonal E_2 (dps = 60)
    mp.mp.dps = 60
    mpb = build_mp_bases_and_projectors()
    rS_mp = mpb["rS"]
    rT_mp = mpb["rT"]
    ep_mp = mpb["ep"]
    em_mp = mpb["em"]
    P_2s5, P_m2s5, P_gold, P_silv = mpb["P_2s5"], mpb["P_m2s5"], mpb["P_gold"], mpb["P_silv"]

    def analyze_wp_point(tau):
        psi = phi_wp_vec(tau, rS_mp)
        n2, probs, I4, I6 = vec_invariants(psi)
        V_wp = (mp.im(tau) ** 2) * n2
        fracs = []
        for P in (P_2s5, P_m2s5, P_gold, P_silv):
            pv = P * psi
            fracs.append(mp.fsum(abs(pv[k]) ** 2 for k in range(6)) / n2)
        cp = (ep_mp.T * psi)[0]
        cm = (em_mp.T * psi)[0]
        th_deg = mp.atan2(abs(cm), abs(cp)) * 180 / mp.pi
        al_deg = mp.arg(cm / cp) * 180 / mp.pi
        return {
            "tau": fmt_mpc(tau),
            "V_wp": fmt_mp(V_wp),
            "norm2": fmt_mp(n2),
            "norm_partition": {
                "E_2sqrt5": fmt_mp(fracs[0]),
                "E_neg_2sqrt5": fmt_mp(fracs[1]),
                "E_phi2": fmt_mp(fracs[2]),
                "E_phim2": fmt_mp(fracs[3]),
            },
            "theta_deg": fmt_mp(th_deg),
            "alpha_deg": fmt_mp(al_deg),
            "I4": fmt_mp(I4),
            "I6": fmt_mp(I6),
            "probabilities": [fmt_mp(p) for p in probs],
            "_V_wp": V_wp,
            "_fracs": fracs,
            "_th_deg": th_deg,
            "_al_deg": al_deg,
            "_I4": I4,
            "_I6": I6,
            "_probs": probs,
            "_psi": psi,
        }

    om_plus = mp.mpc(mp.mpf(1) / 2, mp.sqrt(3) / 2)
    pt_om = analyze_wp_point(om_plus)

    # Compute g_3(omega_+) independently via 4 wp(1/2; omega_+)^3 AND cross-check with E_6(omega_+)
    _, E2_om = eta_and_E2_pentagonal(om_plus, need_E2=True)
    g3_from_wp = 4 * (wp_theta_pentagonal(mp.mpf(1) / 2, om_plus, E2_cached=E2_om) ** 3)
    # Independent E_6(tau) = 1 - 504 sum_{n>=1} n^5 q^n / (1 - q^n), g_3 = (8 pi^6 / 27) E_6
    q_om = mp.exp(2 * I_MP * mp.pi * om_plus)
    e6_sum = mp.mpc(0)
    for n in range(1, 120):
        qn = mp.power(q_om, n)
        term = (n ** 5) * qn / (1 - qn)
        e6_sum += term
        if abs(term) < mp.mpf("1e-70") and n > 10:
            break
    g3_from_E6 = (8 * (mp.pi ** 6) / 27) * (1 - 504 * e6_sum)
    g3_cross_err = abs(g3_from_wp - g3_from_E6) / abs(g3_from_wp)

    V_wp_om_target = (mp.mpf(27) / 8) * mp.power(5, mp.mpf(1) / 3) * mp.power(abs(g3_from_wp), mp.mpf(2) / 3)
    V_wp_om_abs_err = abs(pt_om["_V_wp"] - V_wp_om_target)
    V_wp_om_rel_err = V_wp_om_abs_err / V_wp_om_target

    # Lemniscate tau = i
    pt_i = analyze_wp_point(I_MP)
    s5_mp = mp.sqrt(5)
    lem_target_probs = [
        (5 + s5_mp) / 24,
        (5 + s5_mp) / 24,
        (5 - s5_mp) / 24,
        mp.mpf(1) / 12,
        mp.mpf(1) / 12,
        (5 - s5_mp) / 24,
    ]
    lem_prob_max_err = max(abs(pt_i["_probs"][k] - lem_target_probs[k]) for k in range(6))
    lem_I4_err = abs(pt_i["_I4"] - mp.mpf(2) / 9)
    lem_I6_err = abs(pt_i["_I6"] - mp.mpf(17) / 288)

    # Weight-2 T and S equivariance at tau_0 = 3/10 + 13/10 i
    tau0 = mp.mpc(mp.mpf(3) / 10, mp.mpf(13) / 10)
    pt_0 = analyze_wp_point(tau0)
    pt_T = analyze_wp_point(tau0 + 1)
    pt_S = analyze_wp_point(-1 / tau0)
    T_eq_err = mp.norm(pt_T["_psi"] - rT_mp * pt_0["_psi"])
    S_eq_err = mp.norm(pt_S["_psi"] - (tau0 * tau0) * (rS_mp * pt_0["_psi"]))
    S_drop_tau2_err = mp.norm(pt_S["_psi"] - rS_mp * pt_0["_psi"])
    V_T_rel_err = abs(pt_T["_V_wp"] - pt_0["_V_wp"]) / pt_0["_V_wp"]
    V_S_rel_err = abs(pt_S["_V_wp"] - pt_0["_V_wp"]) / pt_0["_V_wp"]
    I4_T_err = abs(pt_T["_I4"] - pt_0["_I4"])
    I4_S_err = abs(pt_S["_I4"] - pt_0["_I4"])
    I6_T_err = abs(pt_T["_I6"] - pt_0["_I6"])
    I6_S_err = abs(pt_S["_I6"] - pt_0["_I6"])

    # Unit arc alpha = -90 deg verification
    unit_arc_angles = (
        ("pi_2", mp.pi / 2),
        ("5pi_12", 5 * mp.pi / 12),
        ("3pi_8", 3 * mp.pi / 8),
        ("pi_3", mp.pi / 3),
    )
    unit_arc = {}
    unit_arc_max_err = mp.mpf(0)
    for label, ang in unit_arc_angles:
        res_pt = analyze_wp_point(mp.exp(I_MP * ang))
        err_al = abs(res_pt["_al_deg"] + 90)
        if err_al > unit_arc_max_err:
            unit_arc_max_err = err_al
        unit_arc[label] = {
            "alpha_deg": res_pt["alpha_deg"],
            "alpha_plus_90_err": fmt_mp(err_al),
            "theta_deg": res_pt["theta_deg"],
            "I4": res_pt["I4"],
            "I6": res_pt["I6"],
            "V_wp": res_pt["V_wp"],
        }

    # Flow along Re(tau) = 1/2
    flow_points = (
        ("omega_plus", om_plus),
        ("half_plus_1p5i", mp.mpc(mp.mpf(1) / 2, mp.mpf(3) / 2)),
        ("half_plus_2p2726755928588i", mp.mpc(mp.mpf(1) / 2, mp.mpf("2.27267559285881823"))),
        ("tau_tot_70", mp.mpc(mp.mpf(1) / 2, mp.mpf("3.380451106"))),
        ("half_plus_5i", mp.mpc(mp.mpf(1) / 2, mp.mpf(5))),
    )
    flow_half = {}
    for label, tau_pt in flow_points:
        res_pt = analyze_wp_point(tau_pt)
        flow_half[label] = {k: v for k, v in res_pt.items() if not k.startswith("_")}

    def strip_priv(d):
        return {k: v for k, v in d.items() if not k.startswith("_")}

    return {
        "symbolic_5_division_proof": {
            "x2_formula": str(x2),
            "x3_formula": str(x3),
            "poly_5div_in_x": str(poly_5div.as_expr()),
            "poly_5div_in_u": str(P_u.as_expr()),
            "poly_5div_in_u_matches": bool(P_u == exp_P_u),
            "resultant_prim_in_d": str(poly_d_prim.as_expr()),
            "resultant_matches_5d4_270d2_729": bool(poly_d_prim == exp_d_prim),
            "D_roots_verified": bool(roots_D_ok),
            "u_s_over_u_c_eq_phi_inv_proven": bool(ratio_phi6_ok),
            "D_c_exact_cube_verified": bool(Dc_cube_ok),
            "D_s_exact_cube_verified": bool(Ds_cube_ok),
            "u_c_sq_plus_u_s_sq_eq_3_5_1_3_verified": bool(sum_u2_coeff_ok),
            "v_om_C3_omega_eigenstate": bool(v_om_c3_ok),
            "v_om_zero_on_pm_2sqrt5": bool(in_gold_plus_silv),
            "norm_partition_gold_4_5": bool(part_gold_4_5),
            "norm_partition_silv_1_5": bool(part_silv_1_5),
            "chiral_pole_theta45_alpha_neg90": bool(chiral_pole_om_ok),
            "I4_symbolic": str(I4_om_sym),
            "I6_symbolic": str(I6_om_sym),
            "I4_eq_1_5": bool(I4_om_sym == sp.Rational(1, 5)),
            "I6_eq_2_45": bool(I6_om_sym == sp.Rational(2, 45)),
        },
        "omega_plus_numerical": {
            **strip_priv(pt_om),
            "g3_from_wp_half": fmt_mpc(g3_from_wp),
            "g3_from_E6_rel_err": fmt_mp(g3_cross_err),
            "V_wp_target": fmt_mp(V_wp_om_target),
            "V_wp_abs_err": fmt_mp(V_wp_om_abs_err),
            "V_wp_rel_err": fmt_mp(V_wp_om_rel_err),
            "V_wp_matches_lt_1e_40": bool(V_wp_om_rel_err < mp.mpf("1e-40")),
            "norm_partition_err_lt_1e_40": bool(
                pt_om["_fracs"][0] < mp.mpf("1e-40")
                and pt_om["_fracs"][1] < mp.mpf("1e-40")
                and abs(pt_om["_fracs"][2] - mp.mpf(4) / 5) < mp.mpf("1e-40")
                and abs(pt_om["_fracs"][3] - mp.mpf(1) / 5) < mp.mpf("1e-40")
            ),
            "chiral_pole_err_lt_1e_40": bool(
                abs(pt_om["_th_deg"] - 45) < mp.mpf("1e-40")
                and abs(pt_om["_al_deg"] + 90) < mp.mpf("1e-40")
                and abs(pt_om["_I4"] - mp.mpf(1) / 5) < mp.mpf("1e-40")
                and abs(pt_om["_I6"] - mp.mpf(2) / 45) < mp.mpf("1e-40")
            ),
        },
        "lemniscate_i_numerical": {
            **strip_priv(pt_i),
            "max_prob_err": fmt_mp(lem_prob_max_err),
            "I4_minus_2_9_err": fmt_mp(lem_I4_err),
            "I6_minus_17_288_err": fmt_mp(lem_I6_err),
            "all_below_1e_40": bool(
                lem_prob_max_err < mp.mpf("1e-40")
                and lem_I4_err < mp.mpf("1e-40")
                and lem_I6_err < mp.mpf("1e-40")
            ),
        },
        "weight2_equivariance_at_tau0": {
            "tau0": fmt_mpc(tau0),
            "T_err": fmt_mp(T_eq_err),
            "S_err": fmt_mp(S_eq_err),
            "V_wp_T_rel_err": fmt_mp(V_T_rel_err),
            "V_wp_S_rel_err": fmt_mp(V_S_rel_err),
            "I4_T_err": fmt_mp(I4_T_err),
            "I4_S_err": fmt_mp(I4_S_err),
            "I6_T_err": fmt_mp(I6_T_err),
            "I6_S_err": fmt_mp(I6_S_err),
            "all_below_1e_35": bool(
                T_eq_err < mp.mpf("1e-35")
                and S_eq_err < mp.mpf("1e-35")
                and V_T_rel_err < mp.mpf("1e-35")
                and V_S_rel_err < mp.mpf("1e-35")
            ),
        },
        "unit_arc_alpha_lock": {
            "points": unit_arc,
            "max_alpha_plus_90_err": fmt_mp(unit_arc_max_err),
            "locked_lt_1e_40": bool(unit_arc_max_err < mp.mpf("1e-40")),
        },
        "re_half_flow": flow_half,
        "_raw_S_drop_tau2_err": S_drop_tau2_err,
    }


# ---------------------------------------------------------------------------
# Module B5: 5/5 Independent Planted Controls (RPF1..RPF5)
# ---------------------------------------------------------------------------

def run_module_b5(b1_res, b3_res, b4_res):
    # RPF1: Q_8 has fixed-point mismatches against O_27^{(3,3,3)} for rho != 1
    rpf1_mismatches = b1_res["exhaustive_character_fixed_points"]["G3_mismatches_O27_333_vs_Q8"]
    rpf1_deltas_differ = b1_res["halving_trace_moments"]["Q8_fails_to_match_Q6"]
    rpf1_triggered = bool(rpf1_mismatches > 0 and rpf1_deltas_differ)

    # RPF2: Swapping R <-> R^-1 breaks [W_L, W_R] = 0 (when R -> R^-1 in C_om = L R^-1 -> L R and W_R)
    # Also test partial swap (only W_R -> W_{R^-1}, keeping C_om) which breaks W_R = W_L^T & kills i(W_L - W_R)
    rL = leg5_rep_sym(MAT_L)
    rR = leg5_rep_sym(MAT_R)
    rRinv = leg5_rep_sym(MAT_R_INV)
    rC_om = leg5_rep_sym(MAT_C_OM)
    rC_bad = rL * rR  # L (R^-1)^-1 = L R
    WL_bad = sum(((rC_bad ** j) * rL * ((rC_bad.T) ** j) for j in range(3)), sp.zeros(6, 6))
    WR_bad = sum(((rC_bad ** j) * rRinv * ((rC_bad.T) ** j) for j in range(3)), sp.zeros(6, 6))
    WR_bad_keepR = sum(((rC_bad ** j) * rR * ((rC_bad.T) ** j) for j in range(3)), sp.zeros(6, 6))
    comm_rpf2_full = WL_bad * WR_bad - WR_bad * WL_bad
    comm_rpf2_keepR = WL_bad * WR_bad_keepR - WR_bad_keepR * WL_bad
    frob2_full = mat_frob_sq_int(comm_rpf2_full)
    frob2_keepR = mat_frob_sq_int(comm_rpf2_keepR)
    WL_good = sum(((rC_om ** j) * rL * ((rC_om.T) ** j) for j in range(3)), sp.zeros(6, 6))
    WRinv_only = sum(((rC_om ** j) * rRinv * ((rC_om.T) ** j) for j in range(3)), sp.zeros(6, 6))
    rpf2_partial_kills_chiral = (WL_good - WRinv_only == sp.zeros(6, 6))
    rpf2_triggered = bool(frob2_full > 0 and frob2_keepR > 0 and rpf2_partial_kills_chiral)

    # RPF3: R_0 (Re(tau) = 0) breaks W_6 AND I4_xx(0, y*) < 0
    rpf3_comm_frob2 = b3_res["symbolic_mirror_lock"]["R0_comm_W6_frob_sq"]
    rpf3_I4_xx_zero = b3_res["_raw_I4_xx_zero"]
    rpf3_triggered = bool(rpf3_comm_frob2 > 0 and rpf3_I4_xx_zero < 0)

    # RPF4: Dropping tau^2 breaks S-equivariance of Phi^{wp}
    rpf4_err = b4_res["_raw_S_drop_tau2_err"]
    rpf4_triggered = bool(rpf4_err > mp.mpf(1))

    # RPF5: Trivial signs (+1 instead of Legendre character (s/5)) kill golden kernel
    def unsigned_p1f5_rep(M):
        R = sp.zeros(6, 6)
        for j, (px, py) in enumerate(P1_F5):
            nx = (M[0][0] * px + M[0][1] * py) % 5
            ny = (M[1][0] * px + M[1][1] * py) % 5
            for i, (qx, qy) in enumerate(P1_F5):
                for s in (1, 2, 3, 4):
                    if nx == (s * qx) % 5 and ny == (s * qy) % 5:
                        R[i, j] = 1
        return R

    uL = unsigned_p1f5_rep(MAT_L)
    uR = unsigned_p1f5_rep(MAT_R)
    uC = unsigned_p1f5_rep(MAT_C_OM)
    uWL = uL + uC * uL * uC.T + (uC ** 2) * uL * uC
    uWR = uR + uC * uR * uC.T + (uC ** 2) * uR * uC
    uW6 = uWL + uWR
    c_uW6, ok_uW6 = faddeev_leverrier_Z([[int(uW6[i, j]) for j in range(6)] for i in range(6)])
    lam = sp.Symbol("lambda")
    poly_uW6 = sp.Poly(sum(c_uW6[k] * (lam ** k) for k in range(7)), lam, domain="ZZ")
    # Golden minimal poly is lam^2 - 3 lam + 1; verify gcd(poly_uW6, lam^2 - 3 lam + 1) == 1
    golden_minpoly = sp.Poly(lam ** 2 - 3 * lam + 1, lam, domain="ZZ")
    gcd_gold_triv = sp.gcd(poly_uW6, golden_minpoly)
    rpf5_triggered = bool(ok_uW6 and gcd_gold_triv == sp.Poly(1, lam, domain="ZZ"))

    all_5_pass = bool(rpf1_triggered and rpf2_triggered and rpf3_triggered and rpf4_triggered and rpf5_triggered)
    return {
        "RPF1_Q8_mismatches": {
            "G3_mismatches": int(rpf1_mismatches),
            "Delta_differs_from_Q6": bool(rpf1_deltas_differ),
            "triggered": bool(rpf1_triggered),
        },
        "RPF2_swap_R_Rinv": {
            "full_swap_comm_frob_sq": int(frob2_full),
            "C_bad_keep_R_comm_frob_sq": int(frob2_keepR),
            "partial_W_Rinv_kills_chiral_diff": bool(rpf2_partial_kills_chiral),
            "triggered": bool(rpf2_triggered),
        },
        "RPF3_R0_breaks_W6_and_I4_saddle": {
            "comm_R0_W6_frob_sq": int(rpf3_comm_frob2),
            "I4_xx_at_x0_saddle": fmt_mp(rpf3_I4_xx_zero, 25),
            "triggered": bool(rpf3_triggered),
        },
        "RPF4_drop_tau2_breaks_wp_S_equivariance": {
            "residual_norm": fmt_mp(rpf4_err, 30),
            "triggered": bool(rpf4_triggered),
        },
        "RPF5_trivial_signs_kill_golden_kernel": {
            "trivial_W6_charpoly_factored": str(sp.factor(poly_uW6.as_expr())),
            "gcd_with_golden_minpoly": str(gcd_gold_triv.as_expr()),
            "triggered": bool(rpf5_triggered),
        },
        "controls_triggered_count": int(sum(1 for x in (rpf1_triggered, rpf2_triggered, rpf3_triggered, rpf4_triggered, rpf5_triggered) if x)),
        "all_5_controls_triggered": bool(all_5_pass),
    }


def main():
    t0 = time.monotonic_ns()
    leg5_found = verify_leg5_foundation()
    b1_res = run_module_b1()
    b2_res = run_module_b2()
    b3_res = run_module_b3()
    b4_res = run_module_b4()
    b5_res = run_module_b5(b1_res, b3_res, b4_res)
    elapsed_ms = (time.monotonic_ns() - t0) // 1000000

    # Strip internal raw mpmath fields before JSON serialization
    b3_clean = {k: v for k, v in b3_res.items() if not k.startswith("_")}
    b4_clean = {k: v for k, v in b4_res.items() if not k.startswith("_")}

    summary_gates = {
        "leg5_foundation_ok": all(v for k, v in leg5_found.items() if isinstance(v, bool)),
        "B1_polynomials_ok": (
            b1_res["Q6_x_Leg5_polynomials"]["exact_P_neu_match"]
            and b1_res["Q6_x_Leg5_polynomials"]["exact_P_2chg_match"]
            and b1_res["Q6_x_Leg5_polynomials"]["exact_gcd_match"]
            and b1_res["Q6_x_Leg5_polynomials"]["exact_UNPAIRED_match"]
            and b1_res["Q6_x_Leg5_polynomials"]["exact_LEFTOVER_match"]
        ),
        "B1_exhaustive_fixed_points_ok": (
            b1_res["exhaustive_character_fixed_points"]["G3_order"] == 216
            and b1_res["exhaustive_character_fixed_points"]["G4_order"] == 1944
            and b1_res["exhaustive_character_fixed_points"]["G3_mismatches_O27_333_vs_Q6"] == 0
            and b1_res["exhaustive_character_fixed_points"]["G3_mismatches_O27_3312_vs_Q6"] == 0
            and b1_res["exhaustive_character_fixed_points"]["G4_mismatches_O81_333_vs_Q6"] == 0
            and b1_res["exhaustive_character_fixed_points"]["G3_nonzero_fix_O27_3315"] == 0
            and b1_res["exhaustive_character_fixed_points"]["G3_nonzero_fix_Q6_x_P1F2"] == 0
            and b1_res["exhaustive_character_fixed_points"]["G3_mismatches_O27_333_vs_Q8"] > 0
        ),
        "B1_halving_defects_ok": (
            all(s["commutator_Wp_Wm_zero"] for s in b1_res["halving_trace_moments"]["spaces"].values())
            and b1_res["halving_trace_moments"]["O27_333_matches_Q6"]
            and b1_res["halving_trace_moments"]["O27_3312_matches_Q6"]
            and b1_res["halving_trace_moments"]["O81_333_matches_Q6"]
            and b1_res["halving_trace_moments"]["O27_3315_all_zero"]
            and b1_res["halving_trace_moments"]["Level30_all_zero"]
        ),
        "B2_chiral_walk_ok": (
            all(b2_res["algebraic_identities"].values())
            and b2_res["characteristic_polynomials"]["W6_exact_match"]
            and b2_res["characteristic_polynomials"]["WL_exact_match"]
            and b2_res["characteristic_polynomials"]["i_WL_minus_WR_exact_match"]
            and all(b2_res["eigenbasis_and_pauli"].values())
            and b2_res["chiral_poles"]["plus_i"]["I4_eq_1_5"]
            and b2_res["chiral_poles"]["plus_i"]["I6_eq_2_45"]
            and b2_res["chiral_poles"]["minus_i"]["I4_eq_1_5"]
            and b2_res["chiral_poles"]["minus_i"]["I6_eq_2_45"]
        ),
        "B3_siegel_and_stabilization_ok": (
            b3_clean["symbolic_mirror_lock"]["unit_circle_commutes_W6"]
            and b3_clean["symbolic_mirror_lock"]["re_half_commutes_W6"]
            and b3_clean["symbolic_mirror_lock"]["unit_c1_commutes_W6"]
            and (not b3_clean["symbolic_mirror_lock"]["R0_commutes_W6"])
            and b3_clean["symbolic_cusp_asymptotes"]["v_linear_101111"]["c_minus_over_c_plus_eq_neg_sqrt3"]
            and b3_clean["symbolic_cusp_asymptotes"]["v_const_010000"]["c_minus_over_c_plus_eq_neg_sqrt3"]
            and b3_clean["quasi_periodicity_verification"]["all_below_1e_45"]
            and b3_clean["sl2z_equivariance_at_tau0"]["T_and_S_below_1e_40"]
            and all(b3_clean["special_moduli"]["checks"].values())
            and b3_clean["interior_stabilization"]["tau_I4_star_on_x_half"]["is_strict_2D_minimum"]
            and b3_clean["interior_stabilization"]["I4_saddle_on_x_zero"]["is_x_saddle"]
            and b3_clean["interior_stabilization"]["tau_I6_star_on_x_zero"]["is_strict_2D_minimum"]
            and b3_clean["interior_stabilization"]["I6_saddle_on_x_half"]["is_x_saddle"]
            and b3_clean["interior_stabilization"]["fundamental_domain_sweep"]["no_lower_I4_found"]
            and b3_clean["interior_stabilization"]["fundamental_domain_sweep"]["no_lower_I6_found"]
        ),
        "B4_weierstrass_and_5div_ok": (
            b4_clean["symbolic_5_division_proof"]["poly_5div_in_u_matches"]
            and b4_clean["symbolic_5_division_proof"]["resultant_matches_5d4_270d2_729"]
            and b4_clean["symbolic_5_division_proof"]["u_s_over_u_c_eq_phi_inv_proven"]
            and b4_clean["symbolic_5_division_proof"]["norm_partition_gold_4_5"]
            and b4_clean["symbolic_5_division_proof"]["norm_partition_silv_1_5"]
            and b4_clean["symbolic_5_division_proof"]["chiral_pole_theta45_alpha_neg90"]
            and b4_clean["symbolic_5_division_proof"]["I4_eq_1_5"]
            and b4_clean["symbolic_5_division_proof"]["I6_eq_2_45"]
            and b4_clean["omega_plus_numerical"]["V_wp_matches_lt_1e_40"]
            and b4_clean["omega_plus_numerical"]["norm_partition_err_lt_1e_40"]
            and b4_clean["omega_plus_numerical"]["chiral_pole_err_lt_1e_40"]
            and b4_clean["lemniscate_i_numerical"]["all_below_1e_40"]
            and b4_clean["weight2_equivariance_at_tau0"]["all_below_1e_35"]
            and b4_clean["unit_arc_alpha_lock"]["locked_lt_1e_40"]
        ),
        "B5_all_5_controls_ok": b5_res["all_5_controls_triggered"],
    }

    payload = {
        "card_id": "A2-LEG5-TOWER-MODULAR-BRIDGE",
        "role": "cold_room_zero_trust_referee",
        "seat_code": "fam3-v1-high-03",
        "empirical_inputs_used": "0 of 19",
        "elapsed_ms": int(elapsed_ms),
        "leg5_foundation": leg5_found,
        "B1": b1_res,
        "B2": b2_res,
        "B3": b3_clean,
        "B4": b4_clean,
        "B5": b5_res,
        "summary_gates": summary_gates,
        "all_gates_pass": bool(all(summary_gates.values())),
    }

    out_path = Path(__file__).resolve().parent / "referee_a2_leg5_tower_modular_bridge_out.json"
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("OK: wrote referee_a2_leg5_tower_modular_bridge_out.json")


if __name__ == "__main__":
    main()
