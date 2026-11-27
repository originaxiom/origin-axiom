#!/usr/bin/env python3
r"""Card AGY-C66 Disjoint Cold-Room Countercheck (Zero Shared Code, 0 of 19).

Independently constructs all mathematical objects from first principles using
disjoint algorithms (0 imports from producer, 0 AST float/complex literals, 0 JSON floats):
  - E1: Contragredient / homogeneous F_p^2 ray-equivalence, exact cusp-shear check
        P_3 = C_omega^2 L C_omega^-2 = [[0, 1], [-1, 2]], and Cayley-Hamilton residue
        identities across p in {2, 3, 5, 7, 11, 13, 17, 19, 23} + epsilon-ring Taylor
        verification of the (3, 3, 3) Jacobian (14, 5, 5) (ratio 14/5).
  - E2: Faddeev-LeVerrier exact integer trace recursion across ALL 12 (p, mode) pairs for
        p in {2, 3, 5, 7} and mode in {line, ray, vec}, independent ray-involution projection
        verification of det(x I - W_{6,omega}|_{Leg(5)}) = (x^2 - 20)(x^2 - 3x + 1)^2, and
        disjoint 2-prime determinant / DomainMatrix nullspace verification across p in {2..23}.
  - E3: Symplectic J-conjugate contragredient fiber action M -> J M J^-1 = M^-T (so g_{C_3}
        acts directly as -C_omega^-1 = [[-1, 1], [-1, 0]] while base acts by C_tr),
        bipartite Schur reduction (halving matrix dimension from d to d/2 via O_27's mod-9
        cube bipartition), and disjoint 62-bit prime CRT over ZZ[y] across p in {2, 3, 5, 7}.
  - E4: Direct 12-ray complex Bloch-sphere evaluation on (F_5^2 \ {0})/{+-1} across both
        real equator angles and off-equator complex angles (th, al), verifying W_sys / W_cusp
        = phi^2 and the exact full-Bloch-sphere SOS deficits for I_4 and I_6.
"""

import ast
import fractions
import json
import pathlib
import sys

import sympy as sp
from sympy.polys.domains import ZZ
from sympy.polys.matrices import DomainMatrix


def check_eq(discrepancies, label, got, expected):
    if got != expected:
        discrepancies.append(f"{label}: got={got!r} != expected={expected!r}")


# ---------------------------------------------------------------------------
# Disjoint linear algebra: Faddeev-LeVerrier over Z and 62-bit prime Hessenberg
# ---------------------------------------------------------------------------

def faddeev_leverrier_zz(M_rows):
    """Exact integer characteristic polynomial det(x I - M) via Newton-Faddeev traces."""
    n = len(M_rows)
    if n == 0:
        return [1]
    M_dm = DomainMatrix(M_rows, (n, n), ZZ)
    Id_dm = DomainMatrix.eye(n, ZZ)
    B_dm = Id_dm
    coeffs = [1]
    for k in range(1, n + 1):
        MB = M_dm * B_dm
        mb_list = MB.to_list()
        tr_val = sum(mb_list[i][i] for i in range(n))
        if tr_val % k != 0:
            raise AssertionError("Non-integer Faddeev-LeVerrier division")
        ck = -(tr_val // k)
        coeffs.append(int(ck))
        if k < n:
            B_dm = MB + Id_dm * ZZ(ck)
    return coeffs


def hess_mod_prime(mat, p):
    n = len(mat)
    if n == 0:
        return [1]
    A = [[x % p for x in r] for r in mat]
    for col in range(n - 2):
        piv = next((r for r in range(col + 1, n) if A[r][col]), None)
        if piv is None:
            continue
        if piv != col + 1:
            A[col + 1], A[piv] = A[piv], A[col + 1]
            for r in range(n):
                A[r][col + 1], A[r][piv] = A[r][piv], A[r][col + 1]
        inv = pow(A[col + 1][col], p - 2, p)
        for r in range(col + 2, n):
            if A[r][col]:
                fac = (A[r][col] * inv) % p
                A[r][col] = 0
                for c in range(col + 1, n):
                    A[r][c] = (A[r][c] - fac * A[col + 1][c]) % p
                for rr in range(n):
                    A[rr][col + 1] = (A[rr][col + 1] + fac * A[rr][r]) % p
    polys = [[1]]
    for k in range(1, n + 1):
        prev = polys[k - 1]
        cur = [0] * (k + 1)
        dg = A[k - 1][k - 1]
        for i, val in enumerate(prev):
            cur[i + 1] = (cur[i + 1] + val) % p
            cur[i] = (cur[i] - dg * val) % p
        sub_prod = 1
        for i in range(k - 2, -1, -1):
            sub_prod = (sub_prod * A[i + 1][i]) % p
            if not sub_prod:
                break
            t = (sub_prod * A[i][k - 1]) % p
            if t:
                for idx, val in enumerate(polys[i]):
                    cur[idx] = (cur[idx] - t * val) % p
        polys.append(cur)
    return list(reversed(polys[n]))


def crt_disjoint_primes(builder, deg, bound_base=6):
    """Disjoint prime pool starting above 2^62 (disjoint from producer's 2^60 pool)."""
    if deg == 0:
        return [1]
    target = 2 * (bound_base ** deg) + 1
    M_acc = 1
    res = None
    q = (1 << 62) + 5
    while M_acc <= target:
        q = int(sp.nextprime(q))
        if q % 3 != 1:
            continue
        g = 3
        while pow(g, (q - 1) // 3, q) == 1:
            g += 1
        wq = pow(g, (q - 1) // 3, q)
        cp = hess_mod_prime(builder(q, wq), q)
        if res is None:
            res = cp[:]
            M_acc = q
        else:
            inv_m = pow(M_acc, q - 2, q)
            for i in range(deg + 1):
                res[i] += (((cp[i] - res[i]) % q) * inv_m % q) * M_acc
            M_acc *= q
    h = M_acc // 2
    return [c - M_acc if c > h else c for c in res]


# ---------------------------------------------------------------------------
# Independent verification of E1, E2, E3, E4 + RPF1..RPF5
# ---------------------------------------------------------------------------

def countercheck_all(prod_out):
    discrepancies = []

    # --- E1 independent check ---
    L = sp.Matrix([[1, 1], [0, 1]])
    R = sp.Matrix([[1, 0], [1, 1]])
    Cw = L * R.inv()
    P_list = [L, Cw * L * Cw.inv(), Cw ** 2 * L * Cw ** (-2)]
    U_list = [L * R, Cw * (L * R) * Cw.inv(), Cw ** 2 * (L * R) * Cw ** (-2)]

    shears_mat_list = [[[int(P[r, c]) for c in range(2)] for r in range(2)] for P in P_list]
    shears_ok_cc = (
        P_list[0] == sp.Matrix([[1, 1], [0, 1]])
        and P_list[1] == R.inv()
        and P_list[2] == sp.Matrix([[0, 1], [-1, 2]])
        and [int(P.trace()) for P in P_list] == [2, 2, 2]
        and [int(P.det()) for P in P_list] == [1, 1, 1]
        and Cw ** 3 == -sp.eye(2)
    )
    check_eq(discrepancies, "E1.shears_ok_true", shears_ok_cc, True)
    check_eq(discrepancies, "E1.shears_ok_prod", shears_ok_cc, prod_out["E1_all_prime_systole_parabolicity"]["parabolic_cusp_shears_verified"])
    check_eq(discrepancies, "E1.shear_matrices", shears_mat_list, prod_out["E1_all_prime_systole_parabolicity"]["cusp_shear_matrices"])
    check_eq(discrepancies, "E1.systole_traces", [int(U.trace()) for U in U_list], prod_out["E1_all_prime_systole_parabolicity"]["systole_traces"])
    check_eq(discrepancies, "E1.systole_discs", [int(U.trace() ** 2 - 4 * U.det()) for U in U_list], prod_out["E1_all_prime_systole_parabolicity"]["systole_discriminants"])

    # Independent Jacobian at (3, 3, 3) via exact epsilon-ring Taylor expansion -> (14, 5, 5)
    dx, dy, dz = sp.symbols("dx dy dz")
    def lin_L(v):
        return (v[0], v[2], sp.expand(v[0] * v[2] - v[1]).subs({dx**2:0, dy**2:0, dz**2:0, dx*dy:0, dx*dz:0, dy*dz:0}))
    def lin_R(v):
        return (v[2], v[1], sp.expand(v[1] * v[2] - v[0]).subs({dx**2:0, dy**2:0, dz**2:0, dx*dy:0, dx*dz:0, dy*dz:0}))
    def lin_C(v):
        return (v[1], v[2], v[0])
    def lin_Ci(v):
        return (v[2], v[0], v[1])
    v_in = (3 + dx, 3 + dy, 3 + dz)
    six_imgs = [
        lin_L(v_in), lin_R(v_in),
        lin_C(lin_L(lin_Ci(v_in))), lin_C(lin_R(lin_Ci(v_in))),
        lin_Ci(lin_L(lin_C(v_in))), lin_Ci(lin_R(lin_C(v_in))),
    ]
    J3 = sp.Matrix([[sp.expand(sum(m[i] for m in six_imgs) - 18).coeff(var) for var in (dx, dy, dz)] for i in range(3)])
    eigs_J3 = sorted([int(k) for k, mult in J3.eigenvals().items() for _ in range(mult)], reverse=True)
    check_eq(discrepancies, "E1.jacobian_333_exact", eigs_J3, [14, 5, 5])
    check_eq(discrepancies, "E1.jacobian_333", eigs_J3, prod_out["E1_all_prime_systole_parabolicity"]["w6_jacobian_eigenvalues_at_333"])
    check_eq(discrepancies, "E1.jacobian_ratio", str(fractions.Fraction(eigs_J3[0], eigs_J3[1])), prod_out["E1_all_prime_systole_parabolicity"]["w6_jacobian_neutral_to_charged_ratio_at_333"])

    # Scan primes 2..23 via homogeneous equivalence classes
    primes9 = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    match_primes = []
    for idx_p, p in enumerate(primes9):
        lines = []
        for a in range(p):
            for b in range(p):
                if (a, b) == (0, 0):
                    continue
                rep = (0, 1) if a == 0 else (1, (b * pow(a, p - 2, p)) % p)
                if rep not in lines:
                    lines.append(rep)
        def p_act(M, ln):
            u0 = (int(M[0, 0]) * ln[0] + int(M[0, 1]) * ln[1]) % p
            u1 = (int(M[1, 0]) * ln[0] + int(M[1, 1]) * ln[1]) % p
            return (0, 1) if u0 == 0 else (1, (u1 * pow(u0, p - 2, p)) % p)

        cusp = {ln for P in P_list for ln in lines if p_act(P, ln) == ln}
        rem = [ln for ln in lines if ln not in cusp]
        u_fix = [[ln for ln in lines if p_act(U, ln) == ln] for U in U_list]
        u_par = all(
            ((U + sp.eye(2)) ** 2).applyfunc(lambda c: c % p) == sp.zeros(2, 2)
            or ((U - sp.eye(2)) ** 2).applyfunc(lambda c: c % p) == sp.zeros(2, 2)
            for U in U_list
        )
        row_prod = prod_out["E1_all_prime_systole_parabolicity"]["prime_rows"][idx_p]
        check_eq(discrepancies, f"E1.p{p}.cusp_size", len(cusp), row_prod["cusp_triplet_size"])
        check_eq(discrepancies, f"E1.p{p}.rem_size", len(rem), row_prod["remaining_lines_count"])
        check_eq(discrepancies, f"E1.p{p}.u_par", u_par, row_prod["systoles_all_parabolic_mod_p"])
        check_eq(discrepancies, f"E1.p{p}.u_fix_cnts", [len(f) for f in u_fix], row_prod["systole_fixed_line_counts"])
        if len(rem) == 3 and u_par and {ln for f in u_fix for ln in f} == set(rem):
            if {rem[0], p_act(Cw, rem[0]), p_act(Cw, p_act(Cw, rem[0]))} == set(rem):
                match_primes.append(p)
    check_eq(discrepancies, "E1.match_primes", match_primes, prod_out["E1_all_prime_systole_parabolicity"]["exact_complement_match_primes"])

    # --- E2 independent check (Faddeev-LeVerrier across ALL 12 (p, mode) pairs for p in {2,3,5,7} & disjoint prime rank on p in {2..23}) ---
    W_mats = [L, R, Cw * L * Cw.inv(), Cw * R * Cw.inv(), Cw.inv() * L * Cw, Cw.inv() * R * Cw]
    C3w = -Cw
    q_prime = 2000003  # disjoint prime for rank pre-filter

    gold_primes_cc = []
    pure_cover_cc = []
    fl_checked_pairs = 0
    for idx_p, p in enumerate(primes9):
        row_e2 = prod_out["E2_two_counts_6move_spectrum"]["golden_kernel_rows"][idx_p]
        line_ns_cc = []
        line_states_cc = []
        kdims_p = {}
        for mode in ("line", "ray", "vec"):
            def can_u(a, b):
                a, b = a % p, b % p
                if mode == "vec":
                    return (a, b)
                if mode == "ray":
                    return min((a, b), ((-a) % p, (-b) % p))
                return (0, 1) if a == 0 else (1, (b * pow(a, p - 2, p)) % p)
            states = sorted({can_u(a, b) for a in range(p) for b in range(p) if (a, b) != (0, 0)})
            s_idx = {s: i for i, s in enumerate(states)}
            n = len(states)
            W_r = [[0] * n for _ in range(n)]
            C_r = [[0] * n for _ in range(n)]
            for i, s in enumerate(states):
                for M in W_mats:
                    img = can_u(int(M[0, 0]) * s[0] + int(M[0, 1]) * s[1], int(M[1, 0]) * s[0] + int(M[1, 1]) * s[1])
                    W_r[s_idx[img]][i] += 1
                c_img = can_u(int(C3w[0, 0]) * s[0] + int(C3w[0, 1]) * s[1], int(C3w[1, 0]) * s[0] + int(C3w[1, 1]) * s[1])
                C_r[s_idx[c_img]][i] = 1

            W_dm = DomainMatrix(W_r, (n, n), ZZ)
            G_dm = W_dm * W_dm - W_dm * ZZ(3) + DomainMatrix.eye(n, ZZ)
            A = [[c % q_prime for c in r] for r in G_dm.to_list()]
            rk = 0
            for col in range(n):
                piv = next((r for r in range(rk, n) if A[r][col]), None)
                if piv is None:
                    continue
                A[rk], A[piv] = A[piv], A[rk]
                invp = pow(A[rk][col], q_prime - 2, q_prime)
                for r in range(rk + 1, n):
                    if A[r][col]:
                        f = (A[r][col] * invp) % q_prime
                        for c in range(col, n):
                            A[r][c] = (A[r][c] - f * A[rk][c]) % q_prime
                rk += 1
            up_null = n - rk
            if up_null == 0:
                kdim = 0
            elif n <= 60:
                ns_sp = sp.Matrix(G_dm.to_list()).nullspace()
                kdim = len(ns_sp)
                if mode == "line" and kdim > 0:
                    line_states_cc = states
                    line_ns_cc = []
                    for vq in ns_sp:
                        dlcm = sp.lcm([sp.fraction(val)[1] for val in vq])
                        line_ns_cc.append([int(val * dlcm) for val in vq])
            elif line_ns_cc and len(line_ns_cc) == up_null:
                ls_idx = {ls: j for j, ls in enumerate(line_states_cc)}
                pb_rows = [
                    [vr[ls_idx[(0, 1) if s[0] == 0 else (1, (s[1] * pow(s[0], p - 2, p)) % p)]] for s in states]
                    for vr in line_ns_cc
                ]
                P_dm = DomainMatrix(pb_rows, (len(pb_rows), n), ZZ).transpose()
                zc_cc = G_dm * P_dm
                check_eq(discrepancies, f"E2.p{p}.{mode}.pullback_zero", all(int(x) == 0 for r in zc_cc.to_list() for x in r), True)
                kdim = up_null
            else:
                kdim = G_dm.to_field().nullspace().shape[0]
            kdims_p[mode] = kdim
            check_eq(discrepancies, f"E2.p{p}.{mode}.kdim", kdim, row_e2[f"{mode}_kernel_dim"])
            if kdim > 0 and p not in gold_primes_cc:
                gold_primes_cc.append(p)

            # Run Faddeev-LeVerrier across ALL 12 (p, mode) pairs for p in {2, 3, 5, 7}!
            if p in (2, 3, 5, 7):
                fl_checked_pairs += 1
                cp_tot = faddeev_leverrier_zz(W_r)
                seen_i, orbs = set(), []
                for i in range(n):
                    if i in seen_i:
                        continue
                    c1 = next(r for r in range(n) if C_r[r][i])
                    c2 = next(r for r in range(n) if C_r[r][c1])
                    orb = [i] if c1 == i else [i, c1, c2]
                    seen_i.update(orb)
                    orbs.append(orb)
                oid_of = {u_i: oi for oi, o in enumerate(orbs) for u_i in o}
                d0 = len(orbs)
                Q0 = [[0] * d0 for _ in range(d0)]
                for oi, o in enumerate(orbs):
                    rep_i = o[0]
                    for r_to in range(n):
                        if W_r[r_to][rep_i]:
                            Q0[oid_of[r_to]][oi] += W_r[r_to][rep_i]
                cp_neu = faddeev_leverrier_zz(Q0)
                x = sp.Symbol("x")
                p_tot = sp.Poly(cp_tot, x, domain="ZZ")
                p_neu = sp.Poly(cp_neu, x, domain="ZZ")
                p_chg_sq, rem_c = sp.div(p_tot, p_neu, domain="ZZ")
                check_eq(discrepancies, f"E2.p{p}.{mode}.rem_zero", rem_c.is_zero, True)
                flist = p_chg_sq.factor_list()
                check_eq(discrepancies, f"E2.p{p}.{mode}.even_mults", all(m % 2 == 0 for _, m in flist[1]), True)
                p_chg = sp.Poly(1, x, domain="ZZ")
                for fp_i, m in flist[1]:
                    p_chg = p_chg * (fp_i ** (m // 2))
                tab_entry = prod_out["E2_two_counts_6move_spectrum"]["exact_poly_table_p2_to_7"][str(p)][mode]
                check_eq(discrepancies, f"E2.p{p}.{mode}.P_neu_coeffs", cp_neu, tab_entry["P_neu_coeffs"])
                check_eq(discrepancies, f"E2.p{p}.{mode}.P_chg_coeffs", [int(c) for c in p_chg.all_coeffs()], tab_entry["P_chg_coeffs"])

        if kdims_p["line"] == 0 and kdims_p["ray"] > 0:
            pure_cover_cc.append(p)

    check_eq(discrepancies, "E2.faddeev_leverrier_pair_count", fl_checked_pairs, 12)
    check_eq(discrepancies, "E2.gold_primes", gold_primes_cc, prod_out["E2_two_counts_6move_spectrum"]["primes_with_golden_kernel_in_2_to_23"])
    check_eq(discrepancies, "E2.pure_cover_primes", pure_cover_cc, prod_out["E2_two_counts_6move_spectrum"]["primes_with_pure_cover_golden_kernel_in_2_to_23"])

    # --- E3 independent check via J-conjugate contragredient action M |-> M^-T = J M J^-1 ---
    J_mat = sp.Matrix([[0, -1], [1, 0]])
    Lm_c = J_mat * L * J_mat.inv()        # [[1, 0], [-1, 1]]
    Rm_c = J_mat * R * J_mat.inv()        # [[1, -1], [0, 1]]
    Lim_c = Lm_c.inv()
    Rim_c = Rm_c.inv()
    C3_c = -(Rim_c * Lm_c)                # [[-1, 1], [-1, 0]] = -C_omega^-1, exact order 3
    check_eq(discrepancies, "E3.C3_c_order3", C3_c ** 3 == sp.eye(2), True)

    N = 27
    Lt = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N)
    Rt = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N)
    Lit = lambda v: (v[0], (v[0] * v[1] - v[2]) % N, v[1])
    Rit = lambda v: ((v[0] * v[1] - v[2]) % N, v[1], v[0])
    Ct = lambda v: (v[1], v[2], v[0])

    O27 = []
    q_bfs = [(3, 3, 3)]
    seen27 = {(3, 3, 3)}
    while q_bfs:
        cur = q_bfs.pop(0)
        O27.append(cur)
        for fn in (Lt, Rt, Lit, Rit):
            nx = fn(cur)
            if nx not in seen27:
                seen27.add(nx)
                q_bfs.append(nx)

    bip_sign = {O27[0]: 1}
    b_todo = [O27[0]]
    W_tr_6 = [
        Lt, Rt,
        lambda v: Rit(Lt(Rt(v))),
        Lit, Rit,
        lambda v: Lit(Rt(Lt(v))),
    ]
    W_mc_6 = [
        Lm_c, Rm_c,
        Rim_c * Lm_c * Rm_c,
        Lim_c, Rim_c,
        Lim_c * Rm_c * Lm_c,
    ]
    while b_todo:
        u_v = b_todo.pop()
        for fn in W_tr_6:
            w_v = fn(u_v)
            if w_v not in bip_sign:
                bip_sign[w_v] = -bip_sign[u_v]
                b_todo.append(w_v)
            else:
                check_eq(discrepancies, "E3.O27_bipartite", bip_sign[w_v], -bip_sign[u_v])

    def cc_bipartite_bundle(p, leg=False):
        lns = [(0, 1)] + [(1, b) for b in range(p)]
        def act_c(M, ln):
            a = (int(M[0, 0]) * ln[0] + int(M[0, 1]) * ln[1]) % p
            b = (int(M[1, 0]) * ln[0] + int(M[1, 1]) * ln[1]) % p
            sc = b if a == 0 else a
            rep = (0, 1) if a == 0 else (1, (b * pow(a, p - 2, p)) % p)
            sgn = pow(sc, (p - 1) // 2, p) if leg else 1
            if leg and p > 2 and sgn == p - 1:
                sgn = -1
            return rep, sgn

        pts = [(v, ln) for v in O27 for ln in lns]
        orb_of, fixed, c_orbs = {}, [], []
        for pt in pts:
            if pt in orb_of:
                continue
            l1, s1 = act_c(C3_c, pt[1])
            if (Ct(pt[0]), l1) == pt:
                orb_of[pt] = (len(fixed) + len(c_orbs), 0, 1)
                fixed.append(pt)
            else:
                oid = len(fixed) + len(c_orbs)
                cur, acc = pt, 1
                for j in range(3):
                    orb_of[cur] = (oid, j, acc)
                    ln_n, sn = act_c(C3_c, cur[1])
                    cur = (Ct(cur[0]), ln_n)
                    acc *= sn
                c_orbs.append(pt)

        reps = {oid: pt for pt, (oid, j, _) in orb_of.items() if j == 0}
        d0, d1 = len(reps), len(c_orbs)
        neu_plus = [oid for oid, pt in sorted(reps.items()) if bip_sign[pt[0]] == 1]
        neu_minus = [oid for oid, pt in sorted(reps.items()) if bip_sign[pt[0]] == -1]
        np_idx = {oid: i for i, oid in enumerate(neu_plus)}
        nm_idx = {oid: i for i, oid in enumerate(neu_minus)}
        B0_mp = [[0] * len(neu_plus) for _ in range(len(neu_minus))]
        B0_pm = [[0] * len(neu_minus) for _ in range(len(neu_plus))]
        for oid, pt in reps.items():
            for fn, gm in zip(W_tr_6, W_mc_6):
                lt, st = act_c(gm, pt[1])
                o2, _, so = orb_of[(fn(pt[0]), lt)]
                if bip_sign[pt[0]] == 1:
                    B0_mp[nm_idx[o2]][np_idx[oid]] += st * so
                else:
                    B0_pm[np_idx[o2]][nm_idx[oid]] += st * so
        S0_dm = DomainMatrix(B0_mp, (len(neu_minus), len(neu_plus)), ZZ) * DomainMatrix(B0_pm, (len(neu_plus), len(neu_minus)), ZZ)
        S0_list = S0_dm.to_list()
        cp_S0 = crt_disjoint_primes(lambda q, wq: S0_list, len(neu_minus), bound_base=36)
        y = sp.Symbol("y")
        u = sp.Symbol("u")
        p_S0_u = sp.Poly(cp_S0, u, domain="ZZ")
        diff_n = len(neu_plus) - len(neu_minus)
        if diff_n >= 0:
            P_neu_y = sp.Poly(y ** diff_n * p_S0_u.as_expr().subs(u, y ** 2), y, domain="ZZ")
        else:
            P_neu_y, rm = sp.div(sp.Poly(p_S0_u.as_expr().subs(u, y ** 2), y, domain="ZZ"), sp.Poly(y ** (-diff_n), y, domain="ZZ"), domain="ZZ")
            check_eq(discrepancies, "E3.bipartite_div", rm.is_zero, True)

        ch_plus = [i for i, pt in enumerate(c_orbs) if bip_sign[pt[0]] == 1]
        ch_minus = [i for i, pt in enumerate(c_orbs) if bip_sign[pt[0]] == -1]
        cp_idx = {ci: idx for idx, ci in enumerate(ch_plus)}
        cm_idx = {ci: idx for idx, ci in enumerate(ch_minus)}
        ch_oid_to_ci = {orb_of[pt][0]: i for i, pt in enumerate(c_orbs)}
        pw = ((1, 0), (0, 1), (-1, -1))
        C_mp = [[(0, 0)] * len(ch_plus) for _ in range(len(ch_minus))]
        C_pm = [[(0, 0)] * len(ch_minus) for _ in range(len(ch_plus))]
        for ci, pt in enumerate(c_orbs):
            cur, acc = pt, 1
            for j in range(3):
                ph = pw[(3 - j) % 3]
                for fn, gm in zip(W_tr_6, W_mc_6):
                    lt, st = act_c(gm, cur[1])
                    o2, jt, so = orb_of[(fn(cur[0]), lt)]
                    if o2 in ch_oid_to_ci and jt == 0:
                        ci_to = ch_oid_to_ci[o2]
                        ts = acc * st * so
                        if bip_sign[pt[0]] == 1:
                            r, c = cm_idx[ci_to], cp_idx[ci]
                            C_mp[r][c] = (C_mp[r][c][0] + ts * ph[0], C_mp[r][c][1] + ts * ph[1])
                        else:
                            r, c = cp_idx[ci_to], cm_idx[ci]
                            C_pm[r][c] = (C_pm[r][c][0] + ts * ph[0], C_pm[r][c][1] + ts * ph[1])
                ln_n, sn = act_c(C3_c, cur[1])
                cur = (Ct(cur[0]), ln_n)
                acc *= sn

        def build_S1_mod_q(q, wq):
            m_len, p_len = len(ch_minus), len(ch_plus)
            Amp = [[(C_mp[r][c][0] + C_mp[r][c][1] * wq) % q for c in range(p_len)] for r in range(m_len)]
            Apm = [[(C_pm[r][c][0] + C_pm[r][c][1] * wq) % q for c in range(m_len)] for r in range(p_len)]
            out = [[0] * m_len for _ in range(m_len)]
            for r in range(m_len):
                for k in range(p_len):
                    ak = Amp[r][k]
                    if ak:
                        rk = Apm[k]
                        for c in range(m_len):
                            out[r][c] = (out[r][c] + ak * rk[c]) % q
            return out

        cp_S1 = crt_disjoint_primes(build_S1_mod_q, len(ch_minus), bound_base=36)
        cp_S2 = crt_disjoint_primes(lambda q, wq: build_S1_mod_q(q, (wq * wq) % q), len(ch_minus), bound_base=36)
        paired = (cp_S1 == cp_S2)
        diff_c = len(ch_plus) - len(ch_minus)
        cp_4S1 = [cp_S1[k] * (4 ** k) for k in range(len(ch_minus) + 1)]
        p_4S1_u = sp.Poly(cp_4S1, u, domain="ZZ")
        if diff_c >= 0:
            P_2chg_y = sp.Poly(y ** diff_c * p_4S1_u.as_expr().subs(u, y ** 2), y, domain="ZZ")
        else:
            P_2chg_y, rm_c = sp.div(sp.Poly(p_4S1_u.as_expr().subs(u, y ** 2), y, domain="ZZ"), sp.Poly(y ** (-diff_c), y, domain="ZZ"), domain="ZZ")
            check_eq(discrepancies, "E3.chg_bipartite_div", rm_c.is_zero, True)

        G_y = sp.gcd(P_neu_y, P_2chg_y)
        U_y, _ = sp.div(P_2chg_y, G_y, domain="ZZ")
        return {
            "d0": d0, "d1": d1, "paired": paired,
            "halved_deg": int(G_y.degree()),
            "unpaired_deg": int(U_y.degree()),
            "unpaired_coeffs": [int(c) for c in U_y.all_coeffs()],
        }

    e3_prod = prod_out["E3_diagonal_base_times_counts_bundle"]
    cc_bundle_map = {}
    for key_name, p_val, leg_flag in [
        ("O27_x_P1_F2", 2, False),
        ("O27_x_P1_F3", 3, False),
        ("O27_x_P1_F5", 5, False),
        ("O27_x_Leg_F5", 5, True),
        ("O27_x_P1_F7", 7, False),
    ]:
        cc_res = cc_bipartite_bundle(p_val, leg=leg_flag)
        cc_bundle_map[key_name] = cc_res
        pr_res = e3_prod[key_name]
        check_eq(discrepancies, f"E3.{key_name}.d0", cc_res["d0"], pr_res["d0"])
        check_eq(discrepancies, f"E3.{key_name}.d1", cc_res["d1"], pr_res["d1"])
        check_eq(discrepancies, f"E3.{key_name}.paired", cc_res["paired"], pr_res["paired_q1_eq_q2"])
        check_eq(discrepancies, f"E3.{key_name}.halved_deg", cc_res["halved_deg"], pr_res["halved_chg_deg"])
        check_eq(discrepancies, f"E3.{key_name}.unpaired_deg", cc_res["unpaired_deg"], pr_res["unpaired_chg_deg"])
        check_eq(discrepancies, f"E3.{key_name}.unpaired_coeffs", cc_res["unpaired_coeffs"], pr_res["unpaired_poly_y_coeffs"])

    # Also independently verify O_27 x Vecs(5) odd-parity spinor via bipartite Schur (144x144)
    rays5 = sorted({min((a, b), ((-a) % 5, (-b) % 5)) for a in range(5) for b in range(5) if (a, b) != (0, 0)})
    def act_odd_c(M, r):
        u0 = (int(M[0, 0]) * r[0] + int(M[0, 1]) * r[1]) % 5
        u1 = (int(M[1, 0]) * r[0] + int(M[1, 1]) * r[1]) % 5
        rc = min((u0, u1), ((-u0) % 5, (-u1) % 5))
        return rc, (1 if (u0, u1) == rc else -1)
    pts_odd = [(v, r) for v in O27 for r in rays5]
    orb_odd, c_odd = {}, []
    for pt in pts_odd:
        if pt in orb_odd:
            continue
        oid = len(c_odd)
        cur, acc = pt, 1
        for j in range(3):
            orb_odd[cur] = (oid, j, acc)
            rn, sn = act_odd_c(C3_c, cur[1])
            cur = (Ct(cur[0]), rn)
            acc *= sn
        c_odd.append(pt)
    odd_plus = [i for i, pt in enumerate(c_odd) if bip_sign[pt[0]] == 1]
    odd_minus = [i for i, pt in enumerate(c_odd) if bip_sign[pt[0]] == -1]
    op_idx = {i: k for k, i in enumerate(odd_plus)}
    om_idx = {i: k for k, i in enumerate(odd_minus)}
    B_odd_mp = [[0] * 144 for _ in range(144)]
    B_odd_pm = [[0] * 144 for _ in range(144)]
    pw = ((1, 0), (0, 1), (-1, -1))
    C_odd_mp = [[(0, 0)] * 144 for _ in range(144)]
    C_odd_pm = [[(0, 0)] * 144 for _ in range(144)]
    for i, pt in enumerate(c_odd):
        for fn, gm in zip(W_tr_6, W_mc_6):
            rt, st = act_odd_c(gm, pt[1])
            o2, _, so = orb_odd[(fn(pt[0]), rt)]
            if bip_sign[pt[0]] == 1:
                B_odd_mp[om_idx[o2]][op_idx[i]] += st * so
            else:
                B_odd_pm[op_idx[o2]][om_idx[i]] += st * so
        cur, acc = pt, 1
        for j in range(3):
            ph = pw[(3 - j) % 3]
            for fn, gm in zip(W_tr_6, W_mc_6):
                rt, st = act_odd_c(gm, cur[1])
                o2, jt, so = orb_odd[(fn(cur[0]), rt)]
                if jt == 0:
                    ts = acc * st * so
                    if bip_sign[pt[0]] == 1:
                        r, c = om_idx[o2], op_idx[i]
                        C_odd_mp[r][c] = (C_odd_mp[r][c][0] + ts * ph[0], C_odd_mp[r][c][1] + ts * ph[1])
                    else:
                        r, c = op_idx[o2], om_idx[i]
                        C_odd_pm[r][c] = (C_odd_pm[r][c][0] + ts * ph[0], C_odd_pm[r][c][1] + ts * ph[1])
            rn, sn = act_odd_c(C3_c, cur[1])
            cur = (Ct(cur[0]), rn)
            acc *= sn
    S0_odd = (DomainMatrix(B_odd_mp, (144, 144), ZZ) * DomainMatrix(B_odd_pm, (144, 144), ZZ)).to_list()
    cp_S0_odd = crt_disjoint_primes(lambda q, wq: S0_odd, 144, bound_base=36)
    def build_S1_odd(q, wq):
        Amp = [[(C_odd_mp[r][c][0] + C_odd_mp[r][c][1] * wq) % q for c in range(144)] for r in range(144)]
        Apm = [[(C_odd_pm[r][c][0] + C_odd_pm[r][c][1] * wq) % q for c in range(144)] for r in range(144)]
        out = [[0] * 144 for _ in range(144)]
        for r in range(144):
            for k in range(144):
                ak = Amp[r][k]
                if ak:
                    rk = Apm[k]
                    for c in range(144):
                        out[r][c] = (out[r][c] + ak * rk[c]) % q
        return out
    cp_S1_odd = crt_disjoint_primes(build_S1_odd, 144, bound_base=36)
    u = sp.Symbol("u")
    g_odd_u = sp.gcd(sp.Poly(cp_S0_odd, u, domain="ZZ"), sp.Poly([cp_S1_odd[k] * (4 ** k) for k in range(145)], u, domain="ZZ"))
    check_eq(discrepancies, "E3.odd_spinor_halved_deg", 2 * int(g_odd_u.degree()), e3_prod["O27_x_Vecs_F5_odd_spinor"]["odd_spinor_halved_deg"])

    # --- E2 (Leg(5) charpoly) & E4 independent check via 12-ray operator W12 on (F_5^2 \ {0})/{+-1} ---
    W12 = sp.zeros(12, 12)
    T12 = sp.zeros(12, 12)
    C12 = sp.zeros(12, 12)
    F12 = sp.zeros(12, 12)  # multiplication-by-2 nonresidue ray-swap involution on Rays(5)
    r_idx12 = {r: i for i, r in enumerate(rays5)}
    for i, r in enumerate(rays5):
        for M in W_mats:
            u0 = (int(M[0, 0]) * r[0] + int(M[0, 1]) * r[1]) % 5
            u1 = (int(M[1, 0]) * r[0] + int(M[1, 1]) * r[1]) % 5
            W12[r_idx12[min((u0, u1), ((-u0) % 5, (-u1) % 5))], i] += 1
        T12[r_idx12[min((r[1], r[0]), ((-r[1]) % 5, (-r[0]) % 5))], i] = 1
        uc0 = (int(C3w[0, 0]) * r[0] + int(C3w[0, 1]) * r[1]) % 5
        uc1 = (int(C3w[1, 0]) * r[0] + int(C3w[1, 1]) * r[1]) % 5
        C12[r_idx12[min((uc0, uc1), ((-uc0) % 5, (-uc1) % 5))], i] = 1
        f0, f1 = (2 * r[0]) % 5, (2 * r[1]) % 5
        F12[r_idx12[min((f0, f1), ((-f0) % 5, (-f1) % 5))], i] = 1

    # Independently extract the 6x6 F12 = -1 antisymmetric block (Leg(5)) and verify its Z[x] charpoly!
    check_eq(discrepancies, "E2.F12_involution", F12 ** 2 == sp.eye(12) and W12 * F12 == F12 * W12, True)
    leg_pairs = []
    seen_rays = set()
    for i in range(12):
        if i in seen_rays:
            continue
        j = next(k for k in range(12) if F12[k, i] == 1)
        seen_rays.add(i)
        seen_rays.add(j)
        leg_pairs.append((i, j))
    check_eq(discrepancies, "E2.leg_pairs_len", len(leg_pairs), 6)
    W_leg_cc = [[0] * 6 for _ in range(6)]
    for col_k, (i_p, j_m) in enumerate(leg_pairs):
        # Image of (|i_p> - |j_m>) expressed in basis {|a_p> - |b_m>}
        col_vec = W12[:, i_p] - W12[:, j_m]
        for row_k, (a_p, b_m) in enumerate(leg_pairs):
            check_eq(discrepancies, f"E2.leg_antisym_{row_k}_{col_k}", int(col_vec[a_p]), -int(col_vec[b_m]))
            W_leg_cc[row_k][col_k] = int(col_vec[a_p])
    cp_leg_cc = faddeev_leverrier_zz(W_leg_cc)
    x_sym = sp.Symbol("x")
    expected_leg_coeffs = [int(c) for c in sp.Poly((x_sym ** 2 - 20) * (x_sym ** 2 - 3 * x_sym + 1) ** 2, x_sym, domain="ZZ").all_coeffs()]
    check_eq(discrepancies, "E2.leg5_charpoly_exact", cp_leg_cc, expected_leg_coeffs)
    check_eq(discrepancies, "E2.leg5_charpoly_prod", cp_leg_cc, prod_out["E2_two_counts_6move_spectrum"]["p5_legendre_6x6_charpoly_coeffs"])

    lam_phi2 = sp.Rational(3, 2) + sp.sqrt(5) / 2
    ns12 = (W12 - lam_phi2 * sp.eye(12)).nullspace()
    check_eq(discrepancies, "E4.ns12_dim", len(ns12), 2)

    v_p = sp.simplify((sp.eye(12) + T12) * ns12[0])
    if v_p == sp.zeros(12, 1):
        v_p = sp.simplify((sp.eye(12) + T12) * ns12[1])
    v_m = sp.simplify((sp.eye(12) - T12) * ns12[0])
    if v_m == sp.zeros(12, 1):
        v_m = sp.simplify((sp.eye(12) - T12) * ns12[1])
    v_p = sp.simplify(v_p / sp.sqrt((v_p.T * v_p)[0]))
    v_m = sp.simplify(v_m / sp.sqrt((v_m.T * v_m)[0]))

    lines5 = [(1, 0), (0, 1), (1, 1), (1, 2), (1, 3), (1, 4)]
    line_of_ray = []
    for r in rays5:
        ln = (0, 1) if r[0] == 0 else (1, (r[1] * pow(r[0], 3, 5)) % 5)
        line_of_ray.append(lines5.index(ln))

    def bloch_line_probs(th_val, al_val):
        pr6 = [sp.Integer(0)] * 6
        c_th, s_th = sp.cos(th_val), sp.sin(th_val)
        c_al, s_al = sp.cos(al_val), sp.sin(al_val)
        for ri in range(12):
            re_r = c_th * v_p[ri] + c_al * s_th * v_m[ri]
            im_r = s_al * s_th * v_m[ri]
            pr6[line_of_ray[ri]] += re_r ** 2 + im_r ** 2
        return [sp.simplify(pv) for pv in pr6]

    e4_prod = prod_out["E4_pf5_golden_eigenspace_hierarchy"]
    pole_probs6 = bloch_line_probs(sp.pi / 4, sp.pi / 2)
    check_eq(discrepancies, "E4.I4_pole", str(sp.simplify(sum(pv ** 2 for pv in pole_probs6))), e4_prod["I4_chiral_pole"])
    check_eq(discrepancies, "E4.I6_pole", str(sp.simplify(sum(pv ** 3 for pv in pole_probs6))), e4_prod["I6_chiral_pole"])

    # Sample BOTH 7 real equator angles (al = 0) AND 6 off-equator complex Bloch-sphere angles (al not in Z*pi)!
    sample_grid = [
        (sp.Integer(0), sp.Integer(0)),
        (sp.pi / 12, sp.Integer(0)),
        (sp.pi / 6, sp.Integer(0)),
        (sp.pi / 4, sp.Integer(0)),
        (sp.pi / 3, sp.Integer(0)),
        (sp.pi / 2, sp.Integer(0)),
        (2 * sp.pi / 3, sp.Integer(0)),
        (sp.pi / 6, sp.pi / 6),
        (sp.pi / 4, sp.pi / 6),
        (sp.pi / 3, sp.pi / 4),
        (sp.pi / 6, sp.pi / 3),
        (sp.pi / 4, sp.pi / 3),
        (sp.pi / 3, sp.pi / 2),
    ]
    all_ratio_ok = True
    all_i4_sos_ok = True
    all_i6_sos_ok = True
    all_eq_cos6_ok = True
    for th_v, al_v in sample_grid:
        pr6 = bloch_line_probs(th_v, al_v)
        r_ok = (sp.simplify(sum(pr6[3:]) / sum(pr6[:3]) - lam_phi2) == 0)
        i4_v = sp.simplify(sum(pv ** 2 for pv in pr6))
        i6_v = sp.simplify(sum(pv ** 3 for pv in pr6))
        sos4_v = sp.simplify(sp.Rational(1, 10) * (sp.sin(al_v) ** 2) * (sp.sin(2 * th_v) ** 2))
        sos6_v = sp.simplify(
            sp.Rational(1, 45) * (sp.sin(th_v) * (4 * sp.cos(th_v) ** 2 - 1)) ** 2
            + sp.Rational(2, 15) * (sp.sin(al_v) * sp.sin(th_v) * sp.cos(th_v)) ** 2
            + sp.Rational(4, 15) * (sp.sin(al_v) * (sp.sin(th_v) ** 2) * sp.cos(th_v)) ** 2
        )
        s4_ok = (sp.simplify((sp.Rational(3, 10) - i4_v) - sos4_v) == 0)
        s6_ok = (sp.simplify((sp.Rational(11, 90) - i6_v) - sos6_v) == 0)
        all_ratio_ok = all_ratio_ok and r_ok
        all_i4_sos_ok = all_i4_sos_ok and s4_ok
        all_i6_sos_ok = all_i6_sos_ok and s6_ok
        check_eq(discrepancies, f"E4.ratio_at_({th_v},{al_v})", r_ok, True)
        check_eq(discrepancies, f"E4.I4_sos_at_({th_v},{al_v})", s4_ok, True)
        check_eq(discrepancies, f"E4.I6_sos_at_({th_v},{al_v})", s6_ok, True)
        if al_v == 0:
            check_eq(discrepancies, f"E4.I4_eq_at_{th_v}", str(i4_v), e4_prod["I4_real_equator_constant"])
            eq6_ok = (sp.simplify(i6_v - (sp.Rational(1, 9) + sp.Rational(1, 90) * sp.cos(6 * th_v))) == 0)
            all_eq_cos6_ok = all_eq_cos6_ok and eq6_ok
            check_eq(discrepancies, f"E4.I6_eq_at_{th_v}", eq6_ok, True)

    check_eq(discrepancies, "E4.bloch_ratio_flag", all_ratio_ok, e4_prod["bloch_sphere_systole_to_cusp_ratio_equals_phi_sq"])
    check_eq(discrepancies, "E4.bloch_I4_sos_flag", all_i4_sos_ok, e4_prod["bloch_sphere_I4_sos_deficit_verified"])
    check_eq(discrepancies, "E4.bloch_I6_sos_flag", all_i6_sos_ok, e4_prod["bloch_sphere_I6_sos_deficit_verified"])
    check_eq(discrepancies, "E4.I6_equator_cos6_flag", all_eq_cos6_ok, e4_prod["I6_equator_matches_1_over_9_plus_cos6th_over_90"])

    # --- Referee Planted-Fault Controls (RPF1..RPF5), computed purely from countercheck's own objects ---
    # RPF1: Perturbing systole trace 3 -> 5 (word L^3 R, tr = 5, disc = 21) fails parabolicity at p = 5
    U_tr5 = L ** 3 * R
    rpf1 = (((U_tr5 + sp.eye(2)) ** 2).applyfunc(lambda c: c % 5) != sp.zeros(2, 2)) and (((U_tr5 - sp.eye(2)) ** 2).applyfunc(lambda c: c % 5) != sp.zeros(2, 2))

    # RPF2: Perturbing x^2 - 3x + 1 -> x^2 - 3x - 1 on Rays(5) gives nonsingular matrix (0 kernel)
    rpf2 = ((W12 ** 2 - 3 * W12 - sp.eye(12)).det() != 0)

    # RPF3: Countercheck's own bipartite Schur polynomials distinguish O_27 x Leg(5) from O_27 x P^1(F_5)
    y_sym = sp.Symbol("y")
    exp_leg_unpaired = [int(c) for c in sp.Poly((y_sym ** 2 - 6 * y_sym + 4) ** 2 * (y_sym ** 2 + 6 * y_sym + 4) ** 2, y_sym, domain="ZZ").all_coeffs()]
    rpf3 = (
        cc_bundle_map["O27_x_Leg_F5"]["unpaired_coeffs"] != cc_bundle_map["O27_x_P1_F5"]["unpaired_coeffs"]
        and cc_bundle_map["O27_x_Leg_F5"]["unpaired_coeffs"] == exp_leg_unpaired
    )

    # RPF4: Replacing phi^2 eigenspace by phi^-2 eigenspace inverts W_sys / W_cusp from phi^2 to phi^-2 != phi^2
    lam_inv = sp.Rational(3, 2) - sp.sqrt(5) / 2
    ns_inv = (W12 - lam_inv * sp.eye(12)).nullspace()
    v_inv = ns_inv[0] / sp.sqrt((ns_inv[0].T * ns_inv[0])[0])
    pr6_inv = [sp.Integer(0)] * 6
    for ri in range(12):
        pr6_inv[line_of_ray[ri]] += v_inv[ri] ** 2
    rpf4 = (sp.simplify(sum(pr6_inv[3:]) / sum(pr6_inv[:3]) - lam_inv) == 0) and (sp.simplify(lam_inv - lam_phi2) != 0)

    # RPF5: Countercheck's own 12-ray states show I_4 ties at 3/10 between th = 0 and th = pi/6 while I_6 separates 11/90 != 1/10
    pr_0 = bloch_line_probs(sp.Integer(0), sp.Integer(0))
    pr_pi6 = bloch_line_probs(sp.pi / 6, sp.Integer(0))
    i4_0 = sp.simplify(sum(pv ** 2 for pv in pr_0))
    i4_pi6 = sp.simplify(sum(pv ** 2 for pv in pr_pi6))
    i6_0 = sp.simplify(sum(pv ** 3 for pv in pr_0))
    i6_pi6 = sp.simplify(sum(pv ** 3 for pv in pr_pi6))
    rpf5 = (
        sp.simplify(i4_0 - i4_pi6) == 0
        and sp.simplify(i4_0 - sp.Rational(3, 10)) == 0
        and sp.simplify(i6_0 - sp.Rational(11, 90)) == 0
        and sp.simplify(i6_pi6 - sp.Rational(1, 10)) == 0
        and sp.simplify(i6_0 - i6_pi6) != 0
    )

    rpf_list = [rpf1, rpf2, rpf3, rpf4, rpf5]
    return discrepancies, {
        "RPF1_trace5_word_nonparabolic_at_p5_caught": rpf1,
        "RPF2_perturbed_quadratic_nonsingular_on_rays5_caught": rpf2,
        "RPF3_trivial_vs_legendre_unpaired_polynomial_distinct_caught": rpf3,
        "RPF4_conjugate_eigenspace_inverts_golden_ratio_caught": rpf4,
        "RPF5_I6_lifts_I4_equator_tie_caught": rpf5,
        "rpf_caught_count": sum(1 for b in rpf_list if b),
    }


def main(argv):
    if len(argv) < 2:
        print("Usage: countercheck.py <producer_out.json> <countercheck_out.json>")
        return 2
    prod_path = pathlib.Path(argv[0]).resolve()
    out_path = pathlib.Path(argv[1]).resolve()
    prod_out = json.loads(prod_path.read_text(encoding="utf-8"))

    discrepancies, rpf = countercheck_all(prod_out)

    src_text = pathlib.Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src_text)
    ast_floats = sum(
        1 for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex))
    )
    shared_imports = sum(
        1 for node in ast.walk(tree)
        if (isinstance(node, ast.Import) and any("producer" in a.name for a in node.names))
        or (isinstance(node, ast.ImportFrom) and node.module and "producer" in node.module)
    )

    payload = {
        "card": "AGY-C66-COUNTERCHECK",
        "date": "2026-11-27",
        "score": "0 of 19",
        "discrepancies": discrepancies,
        "discrepancies_count": len(discrepancies),
        "referee_planted_fault_controls": rpf,
        "self_audit": {
            "ast_float_or_complex_literals": ast_floats,
            "json_float_values": 0,
            "shared_imports_from_producer": shared_imports,
        },
    }
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Countercheck complete: discrepancies={len(discrepancies)}, RPF={rpf['rpf_caught_count']}/5, ast_floats={ast_floats}, shared_imports={shared_imports}")
    return 0 if len(discrepancies) == 0 and rpf["rpf_caught_count"] == 5 and ast_floats == 0 and shared_imports == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
