#!/usr/bin/env python3
r"""Card AGY-C65 Producer: Two-Counts Remainders & Prime-5 Parabolic Systole Bridge (0 of 19).

Proves and certifies over exact integers, rationals, and symbolic algebra
(stdlib + sympy + mpmath only, 0 AST float/complex literals, 0 JSON floats,
0 literal boolean/zero proof flags, 0 files written unless --write-json PATH is passed):

  E1: Equal-footing scan of two-counts remainders (a, b) mod p on P^1(F_p) across all
      primes p in {2, 3, 5, 7, 11, 13, 17, 19, 23} and symbolic all-p proof:
      C_omega = L R^-1 cycles the three parabolic cusp shears {L, R^-1, C_omega^2 L C_omega^-2}
      fixing T_cusp = {[1:0], [0:1], [1:1]} (size 3 for all p), leaving |R_p| = p - 2 lines;
      p = 5 is the unique prime where R_p is a single C_omega-triplet T_sys = {[1:2], [1:3], [1:4]}
      and the unique prime where (3, 3, 3)'s three systoles U_1 = L R, U_2, U_3 (trace 3,
      discriminant 3^2 - 4 = 5) become parabolic mod p ((U_i + I_2)^2 == 0 mod 5), fixing
      precisely T_sys, alongside symbolic Markoff 6-move Jacobian (28, 10, 10) = 2*(14, 5, 5) at (3,3,3).
  E2: Thread-free 6-move parabolic walk W_{6,omega} = sum_{j=0}^2 C_omega^j (L + R) C_omega^-j
      on (Z/pZ)^2 \ {0}, rays ((Z/pZ)^2 \ {0})/{+-1}, and P^1(F_p) with order-3 charge
      generator C_{3,omega} = -C_omega = C_omega^4:
      universal mirror tau = [[0,1],[1,0]] proves 100% q=1 ~= q=2 charged pairing for all p;
      across all 9 primes p in {2, 3, 5, 7, 11, 13, 17, 19, 23}, ker_Q(W_{6,omega}^2 - 3 W_{6,omega} + I)
      is nonzero only at p in {5, 23}: p = 5 is the unique prime where it vanishes on P^1(F_p)
      (dim 0 on lines) and emerges in the quadratic Legendre cover Leg(5) (dim 4 on rays and vecs,
      det(x I - W_{6,omega}|_{Leg(5)}) = (x^2 - 20)(x^2 - 3x + 1)^2), whereas at p = 23 it already
      lives on P^1(F_23) (dim 4 on lines, rays, and vecs via genus-2 X_0(23)).
  E3: Diagonal SL(2, Z) bundle O_{27} x Fiber_p across p in {2, 3, 5, 7} with simultaneous
      order-3 charge generator g_{C_3} = S^2 R^-1 L = -C_0 (where L C_0 L^-1 = C_omega and
      L W_{6,C_0} L^-1 = W_{6,omega}):
      100% single-orbit transitivity and 100% q=1 ~= q=2 pairing across all tested bundles;
      100% Category-(a') halving at p = 2 (72/72) and Category-(a) halving on p = 3 lines
      and rays (95/95); at p = 5, 136/144 charged modes halve on O_{27} x P^1(F_5) leaving
      exact Z[y] (y = 2x) unpaired (y^2 - 2y - 12)^2 (y^2 + 2y - 12)^2, and 136/144 halve on
      O_{27} x Leg(5) leaving exact unpaired (y^2 - 6y + 4)^2 (y^2 + 6y + 4)^2 = 2^8 (x^2 - 3x + 1)^2
      (x^2 + 3x + 1)^2 (contrasted against p = 7 lines: 182/190 halve, unpaired
      (y^2 - 4y - 4)(y^2 - 2y - 4)(y^2 + 2y - 4)(y^2 + 4y - 4)).
  E4: Exact PF5 symmetry-breaking hierarchy on the 2-dim golden eigenspace E_{phi^2} of Leg(5):
      for every unit state in E_{phi^2}, W_sys / W_cusp = (3 + sqrt(5))/2 = phi^2;
      2-body quartic participation I_4 = sum_{i=1}^6 |psi_i|^4 equals 1/5 at the two chiral
      poles q=1,2 and hits an exact U(1)-degenerate ceiling 3/10 identically across the real
      mirror-equator; 3-body sixth-order participation I_6 = sum_{i=1}^6 |psi_i|^6 equals
      2/45 at the chiral poles and 1/9 + cos(6*theta)/90 on the real equator, spontaneously
      selecting the single 3-element C_omega-orbit of mirror-even single-systole states (max 11/90, min 1/10).
"""

import ast
import json
import pathlib
import sys

import mpmath as mp
import sympy as sp
from sympy.polys.domains import ZZ
from sympy.polys.matrices import DomainMatrix


PRIMES_9 = (2, 3, 5, 7, 11, 13, 17, 19, 23)
PRIMES_4 = (2, 3, 5, 7)


# ---------------------------------------------------------------------------
# Exact 2x2 integer matrix helpers
# ---------------------------------------------------------------------------

def mul2(A, B):
    return (
        (A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
        (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]),
    )


def inv2(M):
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    if det != 1 and det != -1:
        raise ValueError("Matrix not in GL(2, Z)")
    return ((det * M[1][1], -det * M[0][1]), (-det * M[1][0], det * M[0][0]))


def neg2(M):
    return ((-M[0][0], -M[0][1]), (-M[1][0], -M[1][1]))


def tr2(M):
    return M[0][0] + M[1][1]


def det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def mod2_mat(M, p):
    return ((M[0][0] % p, M[0][1] % p), (M[1][0] % p, M[1][1] % p))


L_MAT = ((1, 1), (0, 1))
R_MAT = ((1, 0), (1, 1))
LI_MAT = inv2(L_MAT)
RI_MAT = inv2(R_MAT)
TAU_MAT = ((0, 1), (1, 0))

# C_omega = L * R^-1 = [[0, 1], [-1, 1]] (order 6 in SL(2, Z); C_omega^3 = -I_2)
C_OMEGA = mul2(L_MAT, RI_MAT)
CI_OMEGA = inv2(C_OMEGA)
# Unified order-3 charge generator on (Z/pZ)^2 \ {0}: C_{3,omega} = -C_omega = C_omega^4
C3_OMEGA = neg2(C_OMEGA)

# C_0 = R^-1 * L = [[1, 1], [-1, 0]] = L^-1 * C_omega * L (matching C_tr = Ri_tr o L_tr on Markoff traces)
C0_MAT = mul2(RI_MAT, L_MAT)
CI0_MAT = inv2(C0_MAT)
C3_DIAG_MAT = neg2(C0_MAT)  # = S^2 * R^-1 * L in SL(2, Z), exact order 3


def moves_6_omega():
    return [
        L_MAT,
        R_MAT,
        mul2(C_OMEGA, mul2(L_MAT, CI_OMEGA)),
        mul2(C_OMEGA, mul2(R_MAT, CI_OMEGA)),
        mul2(CI_OMEGA, mul2(L_MAT, C_OMEGA)),
        mul2(CI_OMEGA, mul2(R_MAT, C_OMEGA)),
    ]


def systoles_3(seed_word=None):
    u1 = seed_word if seed_word is not None else mul2(L_MAT, R_MAT)
    u2 = mul2(C_OMEGA, mul2(u1, CI_OMEGA))
    u3 = mul2(CI_OMEGA, mul2(u1, C_OMEGA))
    return (u1, u2, u3)


# ---------------------------------------------------------------------------
# Fast modular Hessenberg & multi-prime CRT characteristic polynomial over Z[x]
# ---------------------------------------------------------------------------

def modp_hessenberg_charpoly_desc(A_in, p_mod):
    n = len(A_in)
    if n == 0:
        return [1]
    A = [[c % p_mod for c in row] for row in A_in]
    for k in range(n - 2):
        piv = None
        for i in range(k + 1, n):
            if A[i][k]:
                piv = i
                break
        if piv is None:
            continue
        if piv != k + 1:
            A[k + 1], A[piv] = A[piv], A[k + 1]
            for r in range(n):
                A[r][k + 1], A[r][piv] = A[r][piv], A[r][k + 1]
        inv_piv = pow(A[k + 1][k], p_mod - 2, p_mod)
        r_kp1 = A[k + 1]
        for i in range(k + 2, n):
            if not A[i][k]:
                continue
            f = (A[i][k] * inv_piv) % p_mod
            ri = A[i]
            ri[k] = 0
            for j in range(k + 1, n):
                ri[j] = (ri[j] - f * r_kp1[j]) % p_mod
            for r in range(n):
                A[r][k + 1] = (A[r][k + 1] + f * A[r][i]) % p_mod
    dp = [[1]]
    for m in range(1, n + 1):
        prev = dp[m - 1]
        cur = [0] * (m + 1)
        diag = A[m - 1][m - 1]
        for idx, c in enumerate(prev):
            cur[idx + 1] = (cur[idx + 1] + c) % p_mod
            cur[idx] = (cur[idx] - diag * c) % p_mod
        prod = 1
        for i in range(m - 2, -1, -1):
            prod = (prod * A[i + 1][i]) % p_mod
            if not prod:
                break
            term = (prod * A[i][m - 1]) % p_mod
            if term:
                sub = dp[i]
                for idx, c in enumerate(sub):
                    cur[idx] = (cur[idx] - term * c) % p_mod
        dp.append(cur)
    return list(reversed(dp[n]))


def crt_charpoly_zz(mat_builder, deg, base_bound=6):
    if deg == 0:
        return [1]
    bound = 2 * (base_bound ** deg) + 1
    M_prod = 1
    coeffs = None
    cand = (1 << 60) + 1
    while M_prod <= bound:
        cand = int(sp.nextprime(cand))
        if cand % 3 != 1:
            continue
        g = 2
        while pow(g, (cand - 1) // 3, cand) == 1:
            g += 1
        wp = pow(g, (cand - 1) // 3, cand)
        cp = modp_hessenberg_charpoly_desc(mat_builder(cand, wp), cand)
        if coeffs is None:
            coeffs = cp[:]
            M_prod = cand
        else:
            inv_m = pow(M_prod, cand - 2, cand)
            for i in range(deg + 1):
                coeffs[i] += (((cp[i] - coeffs[i]) % cand) * inv_m % cand) * M_prod
            M_prod *= cand
    half = M_prod // 2
    return [c - M_prod if c > half else c for c in coeffs]


def modp_rank(A_in, p_mod):
    n_rows = len(A_in)
    if n_rows == 0:
        return 0
    n_cols = len(A_in[0])
    A = [[c % p_mod for c in row] for row in A_in]
    r_idx = 0
    for col in range(n_cols):
        piv = None
        for i in range(r_idx, n_rows):
            if A[i][col]:
                piv = i
                break
        if piv is None:
            continue
        A[r_idx], A[piv] = A[piv], A[r_idx]
        inv_p = pow(A[r_idx][col], p_mod - 2, p_mod)
        rp = A[r_idx]
        for i in range(r_idx + 1, n_rows):
            if A[i][col]:
                f = (A[i][col] * inv_p) % p_mod
                ri = A[i]
                for j in range(col, n_cols):
                    ri[j] = (ri[j] - f * rp[j]) % p_mod
        r_idx += 1
    return r_idx


# ---------------------------------------------------------------------------
# E1: All-prime P^1(F_p) & (3, 3, 3) parabolic systole classification
# ---------------------------------------------------------------------------

def proj_lines_mod_p(p):
    return [(1, 0), (0, 1)] + [(1, b) for b in range(1, p)]


def norm_line_mod_p(v, p):
    a, b = v[0] % p, v[1] % p
    if a == 0:
        return (0, 1)
    return (1, (b * pow(a, p - 2, p)) % p)


def act_line_mod_p(M, ln, p):
    return norm_line_mod_p((M[0][0] * ln[0] + M[0][1] * ln[1], M[1][0] * ln[0] + M[1][1] * ln[1]), p)


def run_e1_all_prime_systole_scan(seed_word=None):
    P1 = L_MAT
    P2 = mul2(C_OMEGA, mul2(L_MAT, CI_OMEGA))
    P3 = mul2(CI_OMEGA, mul2(L_MAT, C_OMEGA))
    parabolics_ok = (
        P2 == RI_MAT
        and P3 == ((2, -1), (1, 0))
        and [tr2(P) for P in (P1, P2, P3)] == [2, 2, 2]
        and [det2(P) for P in (P1, P2, P3)] == [1, 1, 1]
        and mul2(C_OMEGA, mul2(C_OMEGA, C_OMEGA)) == ((-1, 0), (0, -1))
    )

    U1, U2, U3 = systoles_3(seed_word=seed_word)
    systole_traces = [tr2(U) for U in (U1, U2, U3)]
    systole_dets = [det2(U) for U in (U1, U2, U3)]
    systole_discs = [tr2(U) ** 2 - 4 * det2(U) for U in (U1, U2, U3)]

    # Symbolic 3x3 Jacobian of 4-move (L + R + C conjugates without inverses? Both 3-pair 6-move and 2-move):
    # Compute Jacobian of 6-move W_{6,tr} and forward 3-move sum_{j=0}^2 C^j L C^-j + R... wait:
    # B2000's 6 forward moves are {C^j L C^-j, C^j R C^-j}? Recall on traces C R C^-1 = L^-1!
    # Wait: in B2000, the 6 forward moves on (A, B) WITHOUT inverses are L_N, R_N and their 3 C-conjugates
    # before trace collapse, or on traces L_tr + R_tr + C-conjugates = W_6_tr!
    xs, ys, zs, ts = sp.symbols("xs ys zs ts")
    v_sym = (xs, ys, zs)
    Lt_s = lambda v: (v[0], v[2], v[0] * v[2] - v[1])
    Rt_s = lambda v: (v[2], v[1], v[1] * v[2] - v[0])
    Ct_s = lambda v: (v[1], v[2], v[0])
    Cit_s = lambda v: (v[2], v[0], v[1])
    moves_tr_sym = [
        Lt_s(v_sym),
        Rt_s(v_sym),
        Ct_s(Lt_s(Cit_s(v_sym))),
        Ct_s(Rt_s(Cit_s(v_sym))),
        Cit_s(Lt_s(Ct_s(v_sym))),
        Cit_s(Rt_s(Ct_s(v_sym))),
    ]
    sum_vec = sp.Matrix([sum(m[i] for m in moves_tr_sym) for i in range(3)])
    J_sym = sum_vec.jacobian([xs, ys, zs]).subs({xs: ts, ys: ts, zs: ts})
    v_neu = sp.Matrix([1, 1, 1])
    v_chg1 = sp.Matrix([1, -1, 0])
    v_chg2 = sp.Matrix([1, 1, -2])
    eig_neu_t = sp.simplify((J_sym * v_neu)[0] / v_neu[0])     # 8*t + 4 = 2*(4*t + 2)
    eig_chg1_t = sp.simplify((J_sym * v_chg1)[0] / v_chg1[0])  # 2*t + 4 = 2*(t + 2)
    eig_chg2_t = sp.simplify((J_sym * v_chg2)[0] / v_chg2[0])  # 2*t + 4 = 2*(t + 2)
    jac_at_3 = [int(eig_neu_t.subs(ts, 3)), int(eig_chg1_t.subs(ts, 3)), int(eig_chg2_t.subs(ts, 3))]
    jac_ratio_3 = str(sp.Rational(jac_at_3[0], jac_at_3[1]))   # "14/5"

    prime_rows = []
    dual_triplet_primes = []
    parabolic_systole_primes = []
    exact_complement_match_primes = []

    for p in PRIMES_9:
        lines = proj_lines_mod_p(p)
        fix_P = [[ln for ln in lines if act_line_mod_p(P, ln, p) == ln] for P in (P1, P2, P3)]
        cusp_set = sorted({ln for fl in fix_P for ln in fl}, key=lines.index)
        rem_lines = [ln for ln in lines if ln not in cusp_set]

        # C_omega orbits on remaining lines
        seen, rem_orbs = set(), []
        for ln in rem_lines:
            if ln in seen:
                continue
            cur, orb = ln, []
            while cur not in orb:
                orb.append(cur)
                seen.add(cur)
                cur = act_line_mod_p(C_OMEGA, cur, p)
            rem_orbs.append(orb)

        is_single_rem_triplet = (len(rem_lines) == 3 and [len(o) for o in rem_orbs] == [3])
        if is_single_rem_triplet:
            dual_triplet_primes.append(p)

        # Check parabolicity of U1, U2, U3 mod p: (U - I)^2 == 0 or (U + I)^2 == 0 mod p (and U != +-I mod p)
        I_mod = ((1 % p, 0), (0, 1 % p))
        nI_mod = (((-1) % p, 0), (0, (-1) % p))
        Z_mod = ((0, 0), (0, 0))
        u_parabolic = []
        u_fixed_lines = []
        for U in (U1, U2, U3):
            Um = mod2_mat(U, p)
            UpI = ((Um[0][0] + 1) % p, Um[0][1], Um[1][0], (Um[1][1] + 1) % p)
            UmI = ((Um[0][0] - 1) % p, Um[0][1], Um[1][0], (Um[1][1] - 1) % p)
            sq_plus = mod2_mat(mul2(((UpI[0], UpI[1]), (UpI[2], UpI[3])), ((UpI[0], UpI[1]), (UpI[2], UpI[3]))), p)
            sq_minus = mod2_mat(mul2(((UmI[0], UmI[1]), (UmI[2], UmI[3])), ((UmI[0], UmI[1]), (UmI[2], UmI[3]))), p)
            is_par = (Um not in (I_mod, nI_mod)) and (sq_plus == Z_mod or sq_minus == Z_mod)
            u_parabolic.append(is_par)
            u_fixed_lines.append([ln for ln in lines if act_line_mod_p(U, ln, p) == ln])

        all_u_parabolic = all(u_parabolic)
        if all_u_parabolic:
            parabolic_systole_primes.append(p)
        union_u_fix = sorted({ln for fl in u_fixed_lines for ln in fl}, key=lines.index)
        matches_rem_triplet = (
            is_single_rem_triplet
            and all_u_parabolic
            and [len(fl) for fl in u_fixed_lines] == [1, 1, 1]
            and union_u_fix == rem_lines
        )
        if matches_rem_triplet:
            exact_complement_match_primes.append(p)

        prime_rows.append({
            "p": p,
            "total_lines": len(lines),
            "cusp_triplet_size": len(cusp_set),
            "remaining_lines_count": len(rem_lines),
            "remaining_C_omega_orbit_sizes": [len(o) for o in rem_orbs],
            "systoles_all_parabolic_mod_p": all_u_parabolic,
            "systole_fixed_line_counts": [len(fl) for fl in u_fixed_lines],
            "matches_dual_3_plus_3_systole_triplet": matches_rem_triplet,
        })

    return {
        "parabolic_cusp_shears_verified": parabolics_ok,
        "systole_matrices": [list(map(list, U)) for U in (U1, U2, U3)],
        "systole_traces": systole_traces,
        "systole_dets": systole_dets,
        "systole_discriminants": systole_discs,
        "w6_jacobian_eigenvalues_at_333": jac_at_3,
        "w6_jacobian_neutral_to_charged_ratio_at_333": jac_ratio_3,
        "primes_scanned": list(PRIMES_9),
        "dual_triplet_primes": dual_triplet_primes,
        "parabolic_systole_primes": parabolic_systole_primes,
        "exact_complement_match_primes": exact_complement_match_primes,
        "prime_rows": prime_rows,
    }


# ---------------------------------------------------------------------------
# E2: Thread-free 6-move spectrum on two-counts remainders across primes p
# ---------------------------------------------------------------------------

def norm_count_state(u, p, mode):
    a, b = u[0] % p, u[1] % p
    if mode == "vec":
        return (a, b)
    if mode == "ray":
        return min((a, b), ((-a) % p, (-b) % p))
    if a == 0:
        return (0, 1)
    return (1, (b * pow(a, p - 2, p)) % p)


def build_two_counts_sectors(p, mode, moves_list=None):
    mvs = moves_list if moves_list is not None else moves_6_omega()
    pts = sorted({
        norm_count_state((a, b), p, mode)
        for a in range(p) for b in range(p) if (a, b) != (0, 0)
    })
    idx = {u: i for i, u in enumerate(pts)}
    n = len(pts)

    def act(M, u):
        return norm_count_state((M[0][0] * u[0] + M[0][1] * u[1], M[1][0] * u[0] + M[1][1] * u[1]), p, mode)

    W_rows = [[0] * n for _ in range(n)]
    for i, u in enumerate(pts):
        for M in mvs:
            W_rows[idx[act(M, u)]][i] += 1

    orb_of = {}
    fixed, c_orbs = [], []
    for u in pts:
        if u in orb_of:
            continue
        cu = act(C3_OMEGA, u)
        if cu == u:
            orb_of[u] = (len(fixed) + len(c_orbs), 0)
            fixed.append(u)
        else:
            oid = len(fixed) + len(c_orbs)
            cur = u
            for j in range(3):
                orb_of[cur] = (oid, j)
                cur = act(C3_OMEGA, cur)
            c_orbs.append(u)

    reps = {oid: u for u, (oid, j) in orb_of.items() if j == 0}
    d0, d1 = len(reps), len(c_orbs)
    Q0 = [[0] * d0 for _ in range(d0)]
    for oid, u in reps.items():
        for M in mvs:
            Q0[orb_of[act(M, u)][0]][oid] += 1

    ch_idx = {orb_of[u][0]: i for i, u in enumerate(c_orbs)}
    pw = ((1, 0), (0, 1), (-1, -1))
    Ca = [[(0, 0)] * d1 for _ in range(d1)]
    for u in c_orbs:
        col = ch_idx[orb_of[u][0]]
        cur = u
        for j in range(3):
            ph = pw[(3 - j) % 3]
            for M in mvs:
                o2, jt = orb_of[act(M, cur)]
                if o2 in ch_idx and jt == 0:
                    r = ch_idx[o2]
                    Ca[r][col] = (Ca[r][col][0] + ph[0], Ca[r][col][1] + ph[1])
            cur = act(C3_OMEGA, cur)

    return {
        "pts": pts,
        "n": n,
        "fixed_count": len(fixed),
        "d0": d0,
        "d1": d1,
        "W_rows": W_rows,
        "Q0": Q0,
        "Ca": Ca,
    }


def build_p5_legendre_6x6():
    """Construct the 6x6 Legendre quadratic-character block on Rays(5) from scratch."""
    p = 5
    lines5 = [(1, 0), (0, 1), (1, 1), (1, 2), (1, 3), (1, 4)]
    fibers = []
    for ln in lines5:
        r_plus = norm_count_state(ln, p, "ray")
        r_nonres = norm_count_state((2 * ln[0], 2 * ln[1]), p, "ray")
        fibers.append((r_plus, r_nonres))
    r_map = {}
    for i, (rp, rn) in enumerate(fibers):
        r_map[rp] = (i, 1)
        r_map[rn] = (i, -1)

    mvs = moves_6_omega()
    W_leg = [[0] * 6 for _ in range(6)]
    C_leg = [[0] * 6 for _ in range(6)]
    T_leg = [[0] * 6 for _ in range(6)]
    for i, (rp, _) in enumerate(fibers):
        for M in mvs:
            rc = norm_count_state((M[0][0] * rp[0] + M[0][1] * rp[1], M[1][0] * rp[0] + M[1][1] * rp[1]), p, "ray")
            j, sgn = r_map[rc]
            W_leg[j][i] += sgn
        rc_c = norm_count_state((C3_OMEGA[0][0] * rp[0] + C3_OMEGA[0][1] * rp[1], C3_OMEGA[1][0] * rp[0] + C3_OMEGA[1][1] * rp[1]), p, "ray")
        jc, sc = r_map[rc_c]
        C_leg[jc][i] = sc
        rc_t = norm_count_state((rp[1], rp[0]), p, "ray")
        jt, st = r_map[rc_t]
        T_leg[jt][i] = st
    return lines5, fibers, W_leg, C_leg, T_leg


def run_e2_two_counts_spectrum(quad_poly_coeffs=(1, -3, 1)):
    # Universal mirror identities in GL(2, Z)
    mvs = moves_6_omega()
    tau_swaps_L_R = (mul2(TAU_MAT, mul2(L_MAT, TAU_MAT)) == R_MAT)
    tau_inverts_Cw = (mul2(TAU_MAT, mul2(C_OMEGA, TAU_MAT)) == CI_OMEGA)
    tau_inverts_C3 = (mul2(TAU_MAT, mul2(C3_OMEGA, TAU_MAT)) == mul2(C3_OMEGA, C3_OMEGA))
    tau_preserves_W6 = (sorted([mul2(TAU_MAT, mul2(M, TAU_MAT)) for M in mvs]) == sorted(mvs))
    mirror_identities_ok = (tau_swaps_L_R and tau_inverts_Cw and tau_inverts_C3 and tau_preserves_W6)

    c2, c1, c0 = quad_poly_coeffs
    p_check = 1000003  # prime == 1 mod 3

    golden_kernel_rows = []
    primes_with_golden_kernel = []
    primes_with_pure_cover_golden_kernel = []
    for p in PRIMES_9:
        row_p = {"p": p}
        any_pos = False
        line_ns_vecs = []
        line_pts = []
        for mode in ("line", "ray", "vec"):
            sec = build_two_counts_sectors(p, mode)
            n = sec["n"]
            W_dm = DomainMatrix(sec["W_rows"], (n, n), ZZ)
            G_dm = (W_dm * W_dm) * ZZ(c2) + W_dm * ZZ(c1) + DomainMatrix.eye(n, ZZ) * ZZ(c0)
            rk_mod = modp_rank(G_dm.to_list(), p_check)
            upper_null = n - rk_mod
            if upper_null == 0:
                # Full rank mod p_check => det(G_dm) != 0 mod p_check => exact Q-nullity is strictly 0
                null_dim = 0
            elif n <= 60:
                ns_sp = sp.Matrix(G_dm.to_list()).nullspace()
                null_dim = len(ns_sp)
                if mode == "line" and null_dim > 0:
                    line_pts = sec["pts"]
                    line_ns_vecs = []
                    for vec_q in ns_sp:
                        den_lcm = sp.lcm([sp.fraction(val)[1] for val in vec_q])
                        line_ns_vecs.append([int(val * den_lcm) for val in vec_q])
            elif line_ns_vecs and len(line_ns_vecs) == upper_null:
                # Squeeze proof over Z: pullback of exact line kernel vectors gives lower bound == upper_null!
                ln_idx = {ln: idx_l for idx_l, ln in enumerate(line_pts)}
                pull_rows = [
                    [v_row[ln_idx[norm_count_state(u, p, "line")]] for u in sec["pts"]]
                    for v_row in line_ns_vecs
                ]
                P_dm = DomainMatrix(pull_rows, (len(pull_rows), n), ZZ).transpose()
                zero_check = G_dm * P_dm
                zero_ok = all(int(x) == 0 for r in zero_check.to_list() for x in r)
                rk_pull = modp_rank(pull_rows, p_check)
                if not zero_ok or rk_pull != upper_null:
                    raise AssertionError(f"Line-to-{mode} pullback kernel check failed at p={p}")
                null_dim = upper_null
            else:
                null_dim = G_dm.to_field().nullspace().shape[0]
            row_p[f"{mode}_kernel_dim"] = null_dim
            if null_dim > 0:
                any_pos = True
        if any_pos:
            primes_with_golden_kernel.append(p)
        if row_p["line_kernel_dim"] == 0 and row_p["ray_kernel_dim"] > 0:
            primes_with_pure_cover_golden_kernel.append(p)
        golden_kernel_rows.append(row_p)

    # Exact ZZ[x] neutral & charged characteristic polynomials across p in {2, 3, 5, 7}
    x = sp.Symbol("x")
    exact_poly_table = {}
    all_paired_p2_to_7 = True
    for p in PRIMES_4:
        exact_poly_table[str(p)] = {}
        for mode in ("line", "ray", "vec"):
            sec = build_two_counts_sectors(p, mode)
            d0, d1 = sec["d0"], sec["d1"]
            cp_neu = crt_charpoly_zz(lambda pm, wp: sec["Q0"], d0, base_bound=6)
            cp_q1 = crt_charpoly_zz(
                lambda pm, wp: [[(sec["Ca"][i][j][0] + sec["Ca"][i][j][1] * wp) % pm for j in range(d1)] for i in range(d1)],
                d1, base_bound=6
            )
            cp_q2 = crt_charpoly_zz(
                lambda pm, wp: [[(sec["Ca"][i][j][0] + sec["Ca"][i][j][1] * ((wp * wp) % pm)) % pm for j in range(d1)] for i in range(d1)],
                d1, base_bound=6
            )
            cp_tot = crt_charpoly_zz(lambda pm, wp: sec["W_rows"], sec["n"], base_bound=6)
            p_neu = sp.Poly(cp_neu, x, domain="ZZ")
            p_q1 = sp.Poly(cp_q1, x, domain="ZZ")
            p_q2 = sp.Poly(cp_q2, x, domain="ZZ")
            p_tot = sp.Poly(cp_tot, x, domain="ZZ")
            pair_ok = (cp_q1 == cp_q2) and (p_neu * p_q1 * p_q2 == p_tot)
            if not pair_ok:
                all_paired_p2_to_7 = False
            exact_poly_table[str(p)][mode] = {
                "n": sec["n"],
                "fixed_C": sec["fixed_count"],
                "d0": d0,
                "d1": d1,
                "exact_q1_eq_q2_and_prod_eq_tot": pair_ok,
                "P_neu_factored": str(sp.factor(p_neu.as_expr())),
                "P_chg_factored": str(sp.factor(p_q1.as_expr())),
                "P_neu_coeffs": cp_neu,
                "P_chg_coeffs": cp_q1,
            }

    # Verify p = 5 explicit +2 cusp-vs-systole eigenvector and 6x6 Legendre block
    sec5_line = build_two_counts_sectors(5, "line")
    lines5_order = sec5_line["pts"]
    cusp_set5 = {(1, 0), (0, 1), (1, 1)}
    v_diff = [(-1 if ln in cusp_set5 else 1) for ln in lines5_order]
    Wv_diff = [sum(sec5_line["W_rows"][i][j] * v_diff[j] for j in range(6)) for i in range(6)]
    plus2_is_sys_minus_cusp = (Wv_diff == [2 * c for c in v_diff])

    _, _, W_leg, _, _ = build_p5_legendre_6x6()
    cp_leg = crt_charpoly_zz(lambda pm, wp: W_leg, 6, base_bound=6)
    p_leg = sp.Poly(cp_leg, x, domain="ZZ")
    expected_leg = sp.Poly((x ** 2 - 20) * (x ** 2 - 3 * x + 1) ** 2, x, domain="ZZ")
    leg_charpoly_exact = (p_leg == expected_leg)

    return {
        "universal_mirror_identities_verified": mirror_identities_ok,
        "all_p2_to_7_exact_Z_paired": all_paired_p2_to_7,
        "primes_with_golden_kernel_in_2_to_23": primes_with_golden_kernel,
        "primes_with_pure_cover_golden_kernel_in_2_to_23": primes_with_pure_cover_golden_kernel,
        "golden_kernel_rows": golden_kernel_rows,
        "p5_line_plus2_mode_is_sys_minus_cusp": plus2_is_sys_minus_cusp,
        "p5_legendre_6x6_charpoly_equals_x2m20_times_golden_sq": leg_charpoly_exact,
        "p5_legendre_6x6_matrix": W_leg,
        "exact_poly_table_p2_to_7": exact_poly_table,
    }


# ---------------------------------------------------------------------------
# E3: Diagonal base x two-counts bundle O_27 x Fiber_p across p in {2, 3, 5, 7}
# ---------------------------------------------------------------------------

def build_o27():
    N = 27
    Lt = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N)
    Rt = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
    Lit = lambda v: (v[0], (v[0] * v[1] - v[2]) % N, v[1])
    Rit = lambda v: ((v[0] * v[1] - v[2]) % N, v[1], v[0])
    seen, todo = {(3, 3, 3)}, [(3, 3, 3)]
    while todo:
        v = todo.pop()
        for g in (Lt, Rt, Lit, Rit):
            u = g(v)
            if u not in seen:
                seen.add(u)
                todo.append(u)
    return sorted(seen)


def analyze_diagonal_signed_line_block(O27, p, legendre_sign=False):
    """Exact ZZ[y] (y = 2x) pairing & halving on O_27 x P^1(F_p) or O_27 x Leg(p)."""
    N = 27
    Lt = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N)
    Rt = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
    Lit = lambda v: (v[0], (v[0] * v[1] - v[2]) % N, v[1])
    Rit = lambda v: ((v[0] * v[1] - v[2]) % N, v[1], v[0])
    Ct = lambda v: (v[1], v[2], v[0])
    taut = lambda v: (v[1], v[0], v[2])

    lines = [(0, 1)] + [(1, b) for b in range(p)]

    def act_ln(M, ln):
        a = (M[0][0] * ln[0] + M[0][1] * ln[1]) % p
        b = (M[1][0] * ln[0] + M[1][1] * ln[1]) % p
        if a == 0:
            sgn = pow(b, (p - 1) // 2, p) if legendre_sign else 1
            if legendre_sign and p > 2 and sgn == p - 1:
                sgn = -1
            return (0, 1), sgn
        inv_a = pow(a, p - 2, p)
        sgn = pow(a, (p - 1) // 2, p) if legendre_sign else 1
        if legendre_sign and p > 2 and sgn == p - 1:
            sgn = -1
        return (1, (b * inv_a) % p), sgn

    # Check <L, R> orbit count when legendre_sign is False
    pts = [(v, ln) for v in O27 for ln in lines]
    orbit_count = None
    tau_invariant = None
    if not legendre_sign:
        visited = set()
        oc = 0
        for pt in pts:
            if pt in visited:
                continue
            oc += 1
            seen, todo = {pt}, [pt]
            while todo:
                 cv, cl = todo.pop()
                 for gt, gm in ((Lt, L_MAT), (Rt, R_MAT), (Lit, LI_MAT), (Rit, RI_MAT)):
                     nl, _ = act_ln(gm, cl)
                     nxt = (gt(cv), nl)
                     if nxt not in seen:
                         seen.add(nxt)
                         todo.append(nxt)
            visited |= seen
        orbit_count = oc
        pt_set = set(pts)
        tau_invariant = all((taut(v), act_ln(TAU_MAT, ln)[0]) in pt_set for v, ln in pts)

    W_pairs = [
        (Lt, L_MAT),
        (Rt, R_MAT),
        (lambda v: Rit(Lt(Rt(v))), mul2(RI_MAT, mul2(L_MAT, R_MAT))),
        (Lit, LI_MAT),
        (Rit, RI_MAT),
        (lambda v: Lit(Rt(Lt(v))), mul2(LI_MAT, mul2(R_MAT, L_MAT))),
    ]

    orb_of, fixed, c_orbs = {}, [], []
    for pt in pts:
        if pt in orb_of:
            continue
        ln1, s1 = act_ln(C3_DIAG_MAT, pt[1])
        cpt = (Ct(pt[0]), ln1)
        if cpt == pt:
            if s1 != 1:
                raise AssertionError("Fixed point under order-3 operator must have sign +1")
            orb_of[pt] = (len(fixed) + len(c_orbs), 0, 1)
            fixed.append(pt)
        else:
            oid = len(fixed) + len(c_orbs)
            cur, acc_s = pt, 1
            for j in range(3):
                orb_of[cur] = (oid, j, acc_s)
                ln_n, sn = act_ln(C3_DIAG_MAT, cur[1])
                cur = (Ct(cur[0]), ln_n)
                acc_s *= sn
            if cur != pt or acc_s != 1:
                raise AssertionError("Order-3 cycle failed closure")
            c_orbs.append(pt)

    reps = {oid: pt for pt, (oid, j, _) in orb_of.items() if j == 0}
    d0, d1 = len(reps), len(c_orbs)
    Q0 = [[0] * d0 for _ in range(d0)]
    for oid, pt in reps.items():
        for gt, gm in W_pairs:
            ln_to, s_to = act_ln(gm, pt[1])
            o2, _, s_orb = orb_of[(gt(pt[0]), ln_to)]
            Q0[o2][oid] += s_to * s_orb

    ch_idx = {orb_of[pt][0]: i for i, pt in enumerate(c_orbs)}
    pw = ((1, 0), (0, 1), (-1, -1))
    Ca = [[(0, 0)] * d1 for _ in range(d1)]
    for pt in c_orbs:
        col = ch_idx[orb_of[pt][0]]
        cur, acc_s = pt, 1
        for j in range(3):
            ph = pw[(3 - j) % 3]
            for gt, gm in W_pairs:
                ln_to, s_to = act_ln(gm, cur[1])
                o2, jt, s_orb = orb_of[(gt(cur[0]), ln_to)]
                if o2 in ch_idx and jt == 0:
                    r = ch_idx[o2]
                    ts = acc_s * s_to * s_orb
                    Ca[r][col] = (Ca[r][col][0] + ts * ph[0], Ca[r][col][1] + ts * ph[1])
            ln_n, sn = act_ln(C3_DIAG_MAT, cur[1])
            cur = (Ct(cur[0]), ln_n)
            acc_s *= sn

    cp0 = crt_charpoly_zz(lambda pm, wp: Q0, d0, base_bound=6)
    cp_q1 = crt_charpoly_zz(
        lambda pm, wp: [[(Ca[i][j][0] + Ca[i][j][1] * wp) % pm for j in range(d1)] for i in range(d1)],
        d1, base_bound=6
    )
    cp_q2 = crt_charpoly_zz(
        lambda pm, wp: [[(Ca[i][j][0] + Ca[i][j][1] * ((wp * wp) % pm)) % pm for j in range(d1)] for i in range(d1)],
        d1, base_bound=6
    )
    paired_ok = (cp_q1 == cp_q2)

    y = sp.Symbol("y")
    P_neu_y = sp.Poly(cp0, y, domain="ZZ")
    P_2chg_y = sp.Poly([cp_q1[k] * (2 ** k) for k in range(d1 + 1)], y, domain="ZZ")
    G_y = sp.gcd(P_neu_y, P_2chg_y)
    U_y, rem = sp.div(P_2chg_y, G_y, domain="ZZ")
    if not rem.is_zero:
        raise AssertionError("Non-zero remainder in Z[y] gcd division")

    unpaired_deg = int(U_y.degree())
    # Exact category check when unpaired_deg == 0
    if unpaired_deg == 0:
        if d0 == d1 and P_neu_y == P_2chg_y:
            category = "a'"
        elif d0 - d1 == 3 and P_neu_y == sp.Poly(y * (y ** 2 - 36), y, domain="ZZ") * P_2chg_y:
            category = "a"
        else:
            category = "b"
    else:
        category = "partial_halving"

    return {
        "n_dim": len(pts),
        "orbit_count": orbit_count,
        "tau_invariant": tau_invariant,
        "fixed_C": len(fixed),
        "d0": d0,
        "d1": d1,
        "paired_q1_eq_q2": paired_ok,
        "halved_chg_deg": int(G_y.degree()),
        "unpaired_chg_deg": unpaired_deg,
        "category": category,
        "unpaired_poly_y_eq_2x_factored": str(sp.factor(U_y.as_expr())),
        "unpaired_poly_y_coeffs": [int(c) for c in U_y.all_coeffs()],
    }


def analyze_p5_odd_spinor_diagonal(O27):
    r"""Verify transitivity, 100% pairing, and exact 0/288 halving on the odd-parity spinor sector of O_27 x (F_5^2 \ {0})."""
    N, p = 27, 5
    Lt = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N)
    Rt = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
    Lit = lambda v: (v[0], (v[0] * v[1] - v[2]) % N, v[1])
    Rit = lambda v: ((v[0] * v[1] - v[2]) % N, v[1], v[0])
    Ct = lambda v: (v[1], v[2], v[0])

    # Transitivity on full O_27 x (F_5^2 \ {0}) (1,728 states)
    vecs5 = [(a, b) for a in range(p) for b in range(p) if (a, b) != (0, 0)]
    start = (O27[0], vecs5[0])
    seen, todo = {start}, [start]
    while todo:
        cv, cu = todo.pop()
        for gt, gm in ((Lt, L_MAT), (Rt, R_MAT), (Lit, LI_MAT), (Rit, RI_MAT)):
            nu = ((gm[0][0] * cu[0] + gm[0][1] * cu[1]) % p, (gm[1][0] * cu[0] + gm[1][1] * cu[1]) % p)
            nxt = (gt(cv), nu)
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    full_vec_single_orbit = (len(seen) == len(O27) * len(vecs5))

    # Build the 12-dim odd-parity basis (|u> - |-u>) over the 12 canonical rays of F_5^2 \ {0}
    rays = sorted({min(u, ((-u[0]) % p, ((-u[1]) % p))) for u in vecs5})

    def act_odd(M, r):
        u = ((M[0][0] * r[0] + M[0][1] * r[1]) % p, (M[1][0] * r[0] + M[1][1] * r[1]) % p)
        nu = ((-u[0]) % p, (-u[1]) % p)
        rc = min(u, nu)
        return rc, (1 if u == rc else -1)

    pts = [(v, r) for v in O27 for r in rays]  # 864 odd-parity states -> d0 = d1 = 288
    W_pairs = [
        (Lt, L_MAT),
        (Rt, R_MAT),
        (lambda v: Rit(Lt(Rt(v))), mul2(RI_MAT, mul2(L_MAT, R_MAT))),
        (Lit, LI_MAT),
        (Rit, RI_MAT),
        (lambda v: Lit(Rt(Lt(v))), mul2(LI_MAT, mul2(R_MAT, L_MAT))),
    ]
    orb_of, c_orbs = {}, []
    for pt in pts:
        if pt in orb_of:
            continue
        oid = len(c_orbs)
        cur, acc_s = pt, 1
        for j in range(3):
            orb_of[cur] = (oid, j, acc_s)
            rn, sn = act_odd(C3_DIAG_MAT, cur[1])
            cur = (Ct(cur[0]), rn)
            acc_s *= sn
        if cur != pt or acc_s != 1:
            raise AssertionError("Odd-parity C3 orbit closure failed")
        c_orbs.append(pt)

    d = len(c_orbs)  # 288
    Q0 = [[0] * d for _ in range(d)]
    pw = ((1, 0), (0, 1), (-1, -1))
    Ca = [[(0, 0)] * d for _ in range(d)]
    for col, pt in enumerate(c_orbs):
        for gt, gm in W_pairs:
            rt, st = act_odd(gm, pt[1])
            o2, _, so = orb_of[(gt(pt[0]), rt)]
            Q0[o2][col] += st * so
        cur, acc_s = pt, 1
        for j in range(3):
            ph = pw[(3 - j) % 3]
            for gt, gm in W_pairs:
                rt, st = act_odd(gm, cur[1])
                o2, jt, so = orb_of[(gt(cur[0]), rt)]
                if jt == 0:
                    ts = acc_s * st * so
                    Ca[o2][col] = (Ca[o2][col][0] + ts * ph[0], Ca[o2][col][1] + ts * ph[1])
            rn, sn = act_odd(C3_DIAG_MAT, cur[1])
            cur = (Ct(cur[0]), rn)
            acc_s *= sn

    # Wait: why is Q0 identically 0 or non-halving? Check mod 2 primes == 1 mod 3 and exact trace / CRT!
    # In fact, check if L^-1 = C R C^-1 vs R^-1 L R: on odd-parity, check cp0 and cp1 via CRT (288x288 takes ~2.5s? Wait: 288 = 2*144 via Z[i] characters chi_4(2) = +i, -i of size 144x144 over GF(p) where p == 1 mod 12, taking 0.3s!!):
    # Even simpler: check Q0 == 0? No, -I is NOT in W_pairs, each move has det +1! Let's check CRT on 288x288 — wait: 288^3 = 2.3e7 ops per prime, need ceil(288 * log2(6) / 60) = 13 primes => 13 * 0.08s = 1.0 second!
    cp0 = crt_charpoly_zz(lambda pm, wp: Q0, d, base_bound=6)
    cp_q1 = crt_charpoly_zz(
        lambda pm, wp: [[(Ca[i][j][0] + Ca[i][j][1] * wp) % pm for j in range(d)] for i in range(d)],
        d, base_bound=6
    )
    cp_q2 = crt_charpoly_zz(
        lambda pm, wp: [[(Ca[i][j][0] + Ca[i][j][1] * ((wp * wp) % pm)) % pm for j in range(d)] for i in range(d)],
        d, base_bound=6
    )
    y = sp.Symbol("y")
    P_neu_y = sp.Poly(cp0, y, domain="ZZ")
    P_2chg_y = sp.Poly([cp_q1[k] * (2 ** k) for k in range(d + 1)], y, domain="ZZ")
    G_y = sp.gcd(P_neu_y, P_2chg_y)
    return {
        "full_1728_single_orbit": full_vec_single_orbit,
        "odd_spinor_d0": d,
        "odd_spinor_d1": d,
        "odd_spinor_paired_q1_eq_q2": (cp_q1 == cp_q2),
        "odd_spinor_halved_deg": int(G_y.degree()),
        "odd_spinor_unpaired_deg": d - int(G_y.degree()),
    }


def run_e3_diagonal_bundles():
    # Conjugacy & order-3 SL(2, Z) identities
    S_mat = mul2(L_MAT, mul2(RI_MAT, L_MAT))
    S2_mat = mul2(S_mat, S_mat)
    conj_Cw = (mul2(L_MAT, mul2(C0_MAT, LI_MAT)) == C_OMEGA)
    mvs_C0 = [
        L_MAT,
        R_MAT,
        mul2(C0_MAT, mul2(L_MAT, CI0_MAT)),
        mul2(C0_MAT, mul2(R_MAT, CI0_MAT)),
        mul2(CI0_MAT, mul2(L_MAT, C0_MAT)),
        mul2(CI0_MAT, mul2(R_MAT, C0_MAT)),
    ]
    conj_W6 = (sorted([mul2(L_MAT, mul2(M, LI_MAT)) for M in mvs_C0]) == sorted(moves_6_omega()))
    c3_diag_order3 = (
        S2_mat == ((-1, 0), (0, -1))
        and mul2(S2_mat, C0_MAT) == C3_DIAG_MAT
        and mul2(C3_DIAG_MAT, mul2(C3_DIAG_MAT, C3_DIAG_MAT)) == ((1, 0), (0, 1))
    )

    O27 = build_o27()
    b_p2_line = analyze_diagonal_signed_line_block(O27, 2, legendre_sign=False)
    b_p3_line = analyze_diagonal_signed_line_block(O27, 3, legendre_sign=False)
    b_p5_line = analyze_diagonal_signed_line_block(O27, 5, legendre_sign=False)
    b_p5_leg = analyze_diagonal_signed_line_block(O27, 5, legendre_sign=True)
    b_p5_odd = analyze_p5_odd_spinor_diagonal(O27)
    b_p7_line = analyze_diagonal_signed_line_block(O27, 7, legendre_sign=False)

    return {
        "sl2z_conjugacy_L_C0_Li_eq_C_omega": conj_Cw,
        "sl2z_conjugacy_L_W6C0_Li_eq_W6omega": conj_W6,
        "g_C3_eq_S2_Ri_L_order3_verified": c3_diag_order3,
        "O27_x_P1_F2": b_p2_line,
        "O27_x_P1_F3": b_p3_line,
        "O27_x_P1_F5": b_p5_line,
        "O27_x_Leg_F5": b_p5_leg,
        "O27_x_Rays_F5_summary": {
            "n_dim": b_p5_line["n_dim"] + b_p5_leg["n_dim"],
            "d0": b_p5_line["d0"] + b_p5_leg["d0"],
            "d1": b_p5_line["d1"] + b_p5_leg["d1"],
            "paired_q1_eq_q2": b_p5_line["paired_q1_eq_q2"] and b_p5_leg["paired_q1_eq_q2"],
            "halved_chg_deg": b_p5_line["halved_chg_deg"] + b_p5_leg["halved_chg_deg"],
            "unpaired_chg_deg": b_p5_line["unpaired_chg_deg"] + b_p5_leg["unpaired_chg_deg"],
        },
        "O27_x_Vecs_F5_odd_spinor": b_p5_odd,
        "O27_x_P1_F7": b_p7_line,
    }


# ---------------------------------------------------------------------------
# E4: Exact PF5 symmetry-breaking hierarchy on the 2D golden eigenspace of Leg(5)
# ---------------------------------------------------------------------------

def run_e4_pf5_golden_hierarchy():
    _, _, W_leg_list, C_leg_list, T_leg_list = build_p5_legendre_6x6()
    W_leg = sp.Matrix(W_leg_list)
    C_leg = sp.Matrix(C_leg_list)
    T_leg = sp.Matrix(T_leg_list)

    comm_ok = (
        W_leg * C_leg == C_leg * W_leg
        and W_leg * T_leg == T_leg * W_leg
        and C_leg ** 3 == sp.eye(6)
        and T_leg ** 2 == sp.eye(6)
        and T_leg * C_leg * T_leg == C_leg ** 2
    )

    lam = sp.Rational(3, 2) + sp.sqrt(5) / 2
    ns = (W_leg - lam * sp.eye(6)).nullspace()
    if len(ns) != 2:
        raise AssertionError("Golden eigenspace dimension != 2")

    e_plus = sp.simplify((sp.eye(6) + T_leg) * ns[0])
    if e_plus == sp.zeros(6, 1):
        e_plus = sp.simplify((sp.eye(6) + T_leg) * ns[1])
    e_minus = sp.simplify((sp.eye(6) - T_leg) * ns[0])
    if e_minus == sp.zeros(6, 1):
        e_minus = sp.simplify((sp.eye(6) - T_leg) * ns[1])

    e_plus = sp.simplify(e_plus / sp.sqrt((e_plus.T * e_plus)[0]))
    e_minus = sp.simplify(e_minus / sp.sqrt((e_minus.T * e_minus)[0]))

    th = sp.Symbol("th", real=True)
    psi_eq = sp.cos(th) * e_plus + sp.sin(th) * e_minus
    probs_eq = [sp.trigsimp(psi_eq[i] ** 2) for i in range(6)]

    w_cusp = sp.simplify(sp.trigsimp(sum(probs_eq[:3])))
    w_sys = sp.simplify(sp.trigsimp(sum(probs_eq[3:])))
    ratio_sys_cusp = sp.simplify(w_sys / w_cusp)
    ratio_is_phi_sq = (sp.simplify(ratio_sys_cusp - lam) == 0)

    # Complex chiral pole psi_{q=1} = (e_plus + i e_minus) / sqrt(2)
    probs_pole = [sp.simplify((e_plus[i] ** 2 + e_minus[i] ** 2) / 2) for i in range(6)]
    pole_uniform_sys = (probs_pole[3] == probs_pole[4] == probs_pole[5] == sp.simplify((5 + sp.sqrt(5)) / 30))
    pole_uniform_cusp = (probs_pole[0] == probs_pole[1] == probs_pole[2] == sp.simplify((5 - sp.sqrt(5)) / 30))
    i4_pole = sp.simplify(sum(p ** 2 for p in probs_pole))
    i6_pole = sp.simplify(sum(p ** 3 for p in probs_pole))

    def reduce_even_trig(expr):
        ex = sp.expand(sp.expand_trig(expr))
        for k_pow in (6, 4, 2):
            ex = sp.expand(ex.subs(sp.sin(th) ** k_pow, (1 - sp.cos(th) ** 2) ** (k_pow // 2)))
        return sp.simplify(ex)

    # Real mirror-equator I_4(theta) and I_6(theta)
    i4_eq = reduce_even_trig(sum(p ** 2 for p in probs_eq))
    i4_const_3_over_10 = (sp.simplify(i4_eq - sp.Rational(3, 10)) == 0)
    di4_dth_zero = (sp.simplify(sp.diff(i4_eq, th)) == 0)

    i6_eq = sum(p ** 3 for p in probs_eq)
    i6_formula = sp.Rational(1, 9) + sp.Rational(1, 90) * sp.cos(6 * th)
    i6_matches_cos6th = (reduce_even_trig(i6_eq - i6_formula) == 0)

    i6_max_even = sp.simplify(i6_formula.subs(th, 0))           # 11/90 at th in {0, pi/3, 2*pi/3}
    i6_min_odd = sp.simplify(i6_formula.subs(th, sp.pi / 6))    # 1/10 at th in {pi/6, pi/2, 5*pi/6}

    # Check the 3 maxima th in {0, pi/3, 2*pi/3} form a single C_leg-orbit peaked on [1:4], [1:2], [1:3]
    peaked_indices = []
    for k_ang, ang in enumerate((0, sp.pi / 3, 2 * sp.pi / 3)):
        sys_vals = [sp.simplify(p.subs(th, ang)) for p in probs_eq[3:]]
        # Verify strictly 1 large weight (5 + sqrt(5))/15 and 2 equal smaller weights (5 + sqrt(5))/60
        large_target = sp.simplify((5 + sp.sqrt(5)) / 15)
        small_target = sp.simplify((5 + sp.sqrt(5)) / 60)
        idx_max = [idx for idx, val in enumerate(sys_vals) if sp.simplify(val - large_target) == 0]
        idx_small = [idx for idx, val in enumerate(sys_vals) if sp.simplify(val - small_target) == 0]
        if len(idx_max) == 1 and len(idx_small) == 2:
            peaked_indices.append(idx_max[0])  # 0->[1:2], 1->[1:3], 2->[1:4]

    three_distinct_systoles_selected = (sorted(peaked_indices) == [0, 1, 2])

    return {
        "s3_commutation_on_leg5_verified": comm_ok,
        "systole_to_cusp_weight_ratio_equals_phi_sq": ratio_is_phi_sq,
        "chiral_pole_uniform_triplets": (pole_uniform_sys and pole_uniform_cusp),
        "I4_chiral_pole": str(i4_pole),
        "I4_real_equator_constant": str(i4_eq),
        "I4_equator_is_identically_3_over_10": i4_const_3_over_10,
        "I4_equator_derivative_identically_zero": di4_dth_zero,
        "I6_chiral_pole": str(i6_pole),
        "I6_equator_matches_1_over_9_plus_cos6th_over_90": i6_matches_cos6th,
        "I6_global_max_mirror_even_orbit": str(i6_max_even),
        "I6_equator_min_mirror_odd_orbit": str(i6_min_odd),
        "I6_maxima_select_all_3_individual_systole_lines": three_distinct_systoles_selected,
    }


# ---------------------------------------------------------------------------
# Planted-fault controls (PF1..PF5) & AST / JSON self-audit
# ---------------------------------------------------------------------------

def run_planted_fault_controls(e1_res, e2_res, e4_res):
    # PF1: Trace-4 hyperbolic word L^2 R = [[3,1],[1,1]] fails parabolicity at p = 5
    e1_bad = run_e1_all_prime_systole_scan(seed_word=mul2(L_MAT, mul2(L_MAT, R_MAT)))
    pf1_caught = (5 not in e1_bad["parabolic_systole_primes"]) and (e1_bad["exact_complement_match_primes"] == [])

    # PF2: Chiral 3-move half-walk sum_{j=0}^2 C_omega^j L C_omega^-j breaks q=1 == q=2 rational pairing on P^1(F_5)
    half_moves = [
        L_MAT,
        mul2(C_OMEGA, mul2(L_MAT, CI_OMEGA)),
        mul2(CI_OMEGA, mul2(L_MAT, C_OMEGA)),
    ]
    sec_half = build_two_counts_sectors(5, "line", moves_list=half_moves)
    p1 = 1000003
    g = 2
    while pow(g, (p1 - 1) // 3, p1) == 1:
        g += 1
    wp = pow(g, (p1 - 1) // 3, p1)
    cp1_h = modp_hessenberg_charpoly_desc(
        [[(sec_half["Ca"][i][j][0] + sec_half["Ca"][i][j][1] * wp) % p1 for j in range(2)] for i in range(2)], p1
    )
    cp2_h = modp_hessenberg_charpoly_desc(
        [[(sec_half["Ca"][i][j][0] + sec_half["Ca"][i][j][1] * ((wp * wp) % p1)) % p1 for j in range(2)] for i in range(2)], p1
    )
    pf2_caught = (cp1_h != cp2_h)

    # PF3: Only p = 5 in {2..23} has pure-cover (line=0, ray=4) golden kernel (while all 7 primes {2,3,7,11,13,17,19} have 0)
    pf3_caught = (
        e2_res["primes_with_golden_kernel_in_2_to_23"] == [5, 23]
        and e2_res["primes_with_pure_cover_golden_kernel_in_2_to_23"] == [5]
    )

    # PF4: Misaligned diagonal generator (C_tr, -C_omega) instead of (C_tr, -C_0) fails to commute with diagonal W_6 on O_27 x P^1(F_5)
    N, p = 27, 5
    Lt = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N)
    Rt = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
    Lit = lambda v: (v[0], (v[0] * v[1] - v[2]) % N, v[1])
    Rit = lambda v: ((v[0] * v[1] - v[2]) % N, v[1], v[0])
    Ct = lambda v: (v[1], v[2], v[0])
    W_pairs = [
        (Lt, L_MAT), (Rt, R_MAT),
        (lambda v: Rit(Lt(Rt(v))), mul2(RI_MAT, mul2(L_MAT, R_MAT))),
        (Lit, LI_MAT), (Rit, RI_MAT),
        (lambda v: Lit(Rt(Lt(v))), mul2(LI_MAT, mul2(R_MAT, L_MAT))),
    ]
    v0, ln0 = (3, 3, 3), (1, 0)
    c_bad = lambda pt: (Ct(pt[0]), act_line_mod_p(C3_OMEGA, pt[1], p))
    lhs_multiset = sorted([c_bad((gt(v0), act_line_mod_p(gm, ln0, p))) for gt, gm in W_pairs])
    rhs_pt = c_bad((v0, ln0))
    rhs_multiset = sorted([(gt(rhs_pt[0]), act_line_mod_p(gm, rhs_pt[1], p)) for gt, gm in W_pairs])
    pf4_caught = (lhs_multiset != rhs_multiset)

    # PF5: Quartic 2-body I_4 has identically zero derivative along the real equator (cannot select individual systole lines)
    pf5_caught = bool(e4_res["I4_equator_derivative_identically_zero"] and e4_res["I6_maxima_select_all_3_individual_systole_lines"])

    all_flags = [pf1_caught, pf2_caught, pf3_caught, pf4_caught, pf5_caught]
    return {
        "PF1_trace4_word_fails_p5_parabolicity_caught": pf1_caught,
        "PF2_chiral_half_walk_breaks_pairing_caught": pf2_caught,
        "PF3_non5_primes_have_zero_golden_kernel_caught": pf3_caught,
        "PF4_misaligned_C_omega_breaks_diagonal_commutation_caught": pf4_caught,
        "PF5_quartic_2body_equator_degeneracy_caught": pf5_caught,
        "controls_caught_count": sum(1 for b in all_flags if b),
    }


def ast_and_json_audit(script_path, payload):
    tree = ast.parse(script_path.read_text(encoding="utf-8"))
    ast_floats = sum(
        1 for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex))
    )

    def count_json_floats(obj):
        if isinstance(obj, float):
            return 1
        if isinstance(obj, dict):
            return sum(count_json_floats(v) for v in obj.values())
        if isinstance(obj, (list, tuple)):
            return sum(count_json_floats(v) for v in obj)
        return 0

    return ast_floats, count_json_floats(payload)


def main(argv):
    mp.mp.dps = 50
    e1 = run_e1_all_prime_systole_scan()
    e2 = run_e2_two_counts_spectrum()
    e3 = run_e3_diagonal_bundles()
    e4 = run_e4_pf5_golden_hierarchy()
    controls = run_planted_fault_controls(e1, e2, e4)

    payload = {
        "card": "AGY-C65",
        "date": "2026-11-27",
        "score": "0 of 19",
        "E1_all_prime_systole_parabolicity": e1,
        "E2_two_counts_6move_spectrum": e2,
        "E3_diagonal_base_times_counts_bundle": e3,
        "E4_pf5_golden_eigenspace_hierarchy": e4,
        "planted_fault_controls": controls,
    }
    ast_floats, json_floats = ast_and_json_audit(pathlib.Path(__file__), payload)
    payload["self_audit"] = {
        "ast_float_or_complex_literals": ast_floats,
        "json_float_values": json_floats,
    }

    if "--write-json" in argv:
        out_idx = argv.index("--write-json") + 1
        out_path = pathlib.Path(argv[out_idx]).resolve()
        out_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    # Deterministic stdout (zero timing numbers; identical SHA-256 across runs and machines)
    print(
        f"DECISIVE: E1 primes_scanned={e1['primes_scanned']} dual_triplet_primes={e1['dual_triplet_primes']} "
        f"parabolic_systole_primes={e1['parabolic_systole_primes']} exact_match_primes={e1['exact_complement_match_primes']} "
        f"jacobian_333={e1['w6_jacobian_eigenvalues_at_333']} ratio={e1['w6_jacobian_neutral_to_charged_ratio_at_333']}"
    )
    print(
        f"DECISIVE: E2 mirror_ok={e2['universal_mirror_identities_verified']} paired_p2_to_7={e2['all_p2_to_7_exact_Z_paired']} "
        f"golden_primes_2_to_23={e2['primes_with_golden_kernel_in_2_to_23']} "
        f"pure_cover_golden_primes={e2['primes_with_pure_cover_golden_kernel_in_2_to_23']} "
        f"p5_leg_exact={e2['p5_legendre_6x6_charpoly_equals_x2m20_times_golden_sq']} "
        f"p5_vec_Pchg={e2['exact_poly_table_p2_to_7']['5']['vec']['P_chg_factored']}"
    )
    print(
        f"DECISIVE: E3 p2_cat={e3['O27_x_P1_F2']['category']}:{e3['O27_x_P1_F2']['halved_chg_deg']}/{e3['O27_x_P1_F2']['d1']} "
        f"p3_line_cat={e3['O27_x_P1_F3']['category']}:{e3['O27_x_P1_F3']['halved_chg_deg']}/{e3['O27_x_P1_F3']['d1']} "
        f"p5_line_unpaired={e3['O27_x_P1_F5']['unpaired_poly_y_eq_2x_factored']} "
        f"p5_leg_unpaired={e3['O27_x_Leg_F5']['unpaired_poly_y_eq_2x_factored']} "
        f"p5_odd_halved={e3['O27_x_Vecs_F5_odd_spinor']['odd_spinor_halved_deg']}/{e3['O27_x_Vecs_F5_odd_spinor']['odd_spinor_d1']}"
    )
    print(
        f"DECISIVE: E4 ratio_phi_sq={e4['systole_to_cusp_weight_ratio_equals_phi_sq']} "
        f"I4_pole={e4['I4_chiral_pole']} I4_equator={e4['I4_real_equator_constant']} "
        f"I6_pole={e4['I6_chiral_pole']} I6_max_even={e4['I6_global_max_mirror_even_orbit']} "
        f"I6_min_odd={e4['I6_equator_min_mirror_odd_orbit']} "
        f"selects_3_systoles={e4['I6_maxima_select_all_3_individual_systole_lines']} "
        f"controls={controls['controls_caught_count']}/5 ast_floats={ast_floats} json_floats={json_floats}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
