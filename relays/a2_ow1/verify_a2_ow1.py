"""
Pre-Registered Verification Producer for Card A2-OW1:
Open-Flute Gauge-Matter Engine (Delta(2,3,N) Finite Ladder Without m004)
and Unblocked MC:REACH Census (All Punctured-Torus Threads & All 35 Prime Knots <= 8 Crossings).

Strict constraints:
  - 0 of 19 (zero empirical / PDG inputs)
  - Zero float or complex AST literals
  - Zero frontier/ imports
"""

from collections import deque
from fractions import Fraction
import hashlib
import itertools
import json
import math
import pathlib
import sys
import warnings

import mpmath as mp
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

warnings.filterwarnings("ignore")
import snappy


# ---------------------------------------------------------------------------
# Exact integer / rational helpers (zero float literals)
# ---------------------------------------------------------------------------

def mp_rat(p, q=1):
    return mp.mpf(p) / mp.mpf(q)


def perm_mul(p, q):
    """Composition (p o q)(i) = p[q[i]] on 0..d-1."""
    return tuple(p[q[i]] for i in range(len(p)))


def perm_inv(p):
    out = [0] * len(p)
    for i, v in enumerate(p):
        out[v] = i
    return tuple(out)


def perm_order(p):
    d = len(p)
    seen = [False] * d
    ord_val = 1
    for i in range(d):
        if not seen[i]:
            c = 0
            cur = i
            while not seen[cur]:
                seen[cur] = True
                cur = p[cur]
                c += 1
            ord_val = math.lcm(ord_val, c)
    return ord_val


def perm_cycle_type(p):
    d = len(p)
    seen = [False] * d
    lens = []
    for i in range(d):
        if not seen[i]:
            c = 0
            cur = i
            while not seen[cur]:
                seen[cur] = True
                cur = p[cur]
                c += 1
            lens.append(c)
    return tuple(sorted(lens))


def generate_perm_group(gens, deg):
    ident = tuple(range(deg))
    seen = {ident}
    q = deque([ident])
    all_gens = list(gens) + [perm_inv(g) for g in gens]
    while q:
        cur = q.popleft()
        for g in all_gens:
            nxt = perm_mul(cur, g)
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return sorted(seen)


def group_closure_abstract(mul_table, gens, ident):
    seen = {ident}
    q = deque([ident])
    while q:
        cur = q.popleft()
        for g in gens:
            nxt = mul_table[cur][g]
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return frozenset(seen)


def conjugacy_classes_abstract(mul_table, inv_table, n):
    seen = set()
    classes = []
    for x in range(n):
        if x in seen:
            continue
        cls = set()
        for g in range(n):
            c = mul_table[mul_table[g][x]][inv_table[g]]
            cls.add(c)
        seen |= cls
        classes.append(sorted(cls))
    return classes


def enumerate_subgroups_up_to_conj(mul_table, inv_table, n, max_index):
    """Find all subgroups of index <= max_index, one representative per conjugacy class."""
    min_order = (n + max_index - 1) // max_index
    ident = 0
    # BFS over subgroup lattice starting from cyclic subgroups and adding generators
    found = set()
    q = deque([frozenset([ident])])
    found.add(frozenset([ident]))
    while q:
        H = q.popleft()
        for g in range(n):
            if g in H:
                continue
            H2 = group_closure_abstract(mul_table, list(H) + [g], ident)
            if H2 not in found:
                found.add(H2)
                q.append(H2)

    # Deduplicate up to conjugacy and filter by index <= max_index
    reps = []
    seen_all = set()
    for H in sorted(found, key=lambda s: (-len(s), sorted(s))):
        if len(H) < min_order or len(H) == n:
            continue
        if H in seen_all:
            continue
        # Compute conjugacy orbit of H and core of H
        orbit = set()
        core = set(H)
        for g in range(n):
            ginv = inv_table[g]
            Hg = frozenset(mul_table[mul_table[g][h]][ginv] for h in H)
            orbit.add(Hg)
            core &= Hg
        seen_all |= orbit
        reps.append({
            "subgroup": sorted(H),
            "order": len(H),
            "index": n // len(H),
            "core_order": len(core),
            "core_free": (len(core) == 1),
            "num_conjugates": len(orbit),
        })
    return reps


def coset_action_perm(mul_table, H, g, cosets, coset_id):
    return tuple(coset_id[mul_table[g][rep]] for rep in cosets)


# ---------------------------------------------------------------------------
# Berezin-CAR Exterior Fock Space, Centralizer, Anomalies, Kernel, Splitting
# ---------------------------------------------------------------------------

def analyze_involution_gauge_matter(a, b):
    """
    Given involution P on C^d (d = a + b) with eigenvalues (+1)^a, (-1)^b (a >= b >= 1):
    Compute exact C_{su(d)}(P) = s(u(a) + u(b)), hypercharge generator Y on Lambda^{even}(C^d),
    chirality, all 4 gauge+gravitational anomalies, global kernel Z_k, and collar-odd scalar split.
    """
    d = a + b
    g = math.gcd(a, b)
    # Normalized integer hypercharge on fundamental W_d = C^d:
    # traceless: a*(-b/g) + b*(a/g) = 0
    q_plus = -b // g   # charge on (+1)-eigenspace of dim a
    q_minus = a // g   # charge on (-1)-eigenspace of dim b
    # On Lambda^*(W_d), basis states are subsets S of {0..d-1} with |S| even (dim 2^{d-1}).
    # For Berezin-CAR Spin(2d) spinor representation, the U(1) charge of state S is:
    #   Q(S) = sum_{i in S} q_i - (1/2) sum_{i=0}^{d-1} q_i = sum_{i in S} q_i  (since sum q_i = 0!)
    # Wait: verify with Gate F-U1 convention!
    # For a=3, b=2: q_plus = -2, q_minus = +3.
    # Let's list subsets S of {0,1,2 (q=-2), 3,4 (q=+3)} with |S| even:
    #   |S|=0: 1 state, Q = 0
    #   |S|=2: (2 from +): C(3,2)=3 states, Q = -4
    #          (1 from +, 1 from -): 3*2=6 states, Q = +1
    #          (2 from -): C(2,2)=1 state, Q = +6
    #   |S|=4: (3 from +, 1 from -): 1*2=2 states, Q = -6+3 = -3
    #          (2 from +, 2 from -): 3*1=3 states, Q = -4+6 = +2
    # Total multiset for a=3, b=2: [-4^3, -3^2, 0, +1^6, +2^3, +6] — EXACT Gate F-U1 6Y!
    charges_even = []
    # Also track (k_plus, k_minus) for SU(a) x SU(b) reps
    irrep_blocks = []
    for k_even in range(0, d + 1, 2):
        for kp in range(max(0, k_even - b), min(a, k_even) + 1):
            km = k_even - kp
            dim_a = math.comb(a, kp)
            dim_b = math.comb(b, km)
            q_val = kp * q_plus + km * q_minus
            charges_even.extend([q_val] * (dim_a * dim_b))
            irrep_blocks.append((kp, km, dim_a, dim_b, q_val))

    charges_even.sort()
    neg_sorted = sorted([-q for q in charges_even])
    is_chiral = (charges_even != neg_sorted)

    # Exact anomaly sums over Lambda^{even}(C^d)
    tr_Y = sum(charges_even)
    tr_Y3 = sum(q * q * q for q in charges_even)

    # Dynkin index T(Lambda^k C^n) for SU(n):
    # T(Lambda^k C^n) = C(n-2, k-1) / 2 for 1 <= k <= n-1, else 0.
    # Multiply by 2 so everything is an exact integer (2 * Tr(T_a^2 Y)).
    def two_dynkin(n, k):
        if n < 2 or k <= 0 or k >= n:
            return 0
        return math.comb(n - 2, k - 1)

    two_tr_SUa2_Y = sum(two_dynkin(a, kp) * dim_b * q_val for kp, km, dim_a, dim_b, q_val in irrep_blocks)
    two_tr_SUb2_Y = sum(two_dynkin(b, km) * dim_a * q_val for kp, km, dim_a, dim_b, q_val in irrep_blocks)

    all_anomalies_zero = (
        tr_Y == 0
        and tr_Y3 == 0
        and two_tr_SUa2_Y == 0
        and two_tr_SUb2_Y == 0
    )

    # Centralizer dimension in su(d): dim(su(a)) + dim(su(b)) + dim(u(1)) = (a^2 - 1) + (b^2 - 1) + 1
    centralizer_dim = a * a + b * b - 1

    # Exact global kernel order of SU(a) x SU(b) x U(1)_Y acting on Lambda^{even}(C^d):
    # Elements of Z(SU(a)) x Z(SU(b)) x U(1) are (e^{2pi i m/a} I_a, e^{2pi i n/b} I_b, e^{2pi i theta}).
    # On block (kp, km, q_val), phase is exp(2pi i (kp*m/a + km*n/b + q_val*theta)).
    # For faithful U(1) parameterized by exp(2pi i theta * q_val) with theta in [0, 1):
    # Wait: normalize U(1) period to minimal positive integer divisor so theta in [0, 1) acts faithfully on U(1) itself:
    q_gcd = 0
    for q in charges_even:
        q_gcd = math.gcd(q_gcd, abs(q))
    if q_gcd == 0:
        q_gcd = 1
    # Count distinct (m in Z/a, n in Z/b, theta in [0, 1)) acting trivially on ALL blocks!
    # Since theta must satisfy (q_val/q_gcd)*theta + kp*m/a + km*n/b in Z for every (kp, km, q_val):
    # Check using exact Fraction lattice!
    kernel_elems = set()
    # From any block with nonzero q_norm = q_val // q_gcd, theta mod 1 has denominator dividing a*b*abs(q_norm).
    # Even simpler: solve linear congruences directly over Z / (a*b*L)!
    # Pick smallest nonzero |q_val // q_gcd| to enumerate candidate thetas for each (m, n):
    nz_blocks = [(kp, km, q_val // q_gcd) for kp, km, _, _, q_val in irrep_blocks if q_val != 0]
    if nz_blocks:
        kp0, km0, q0 = min(nz_blocks, key=lambda x: abs(x[2]))
        abs_q0 = abs(q0)
        for m in range(a):
            for n in range(b):
                base_phase = Fraction(kp0 * m, a) + Fraction(km0 * n, b)
                # q0 * theta + base_phase in Z => theta = (r - base_phase) / q0 mod 1, r = 0..abs_q0-1
                for r in range(abs_q0):
                    th = (Fraction(r, 1) - base_phase) / Fraction(q0, 1)
                    th = th - math.floor(th)
                    ok = True
                    for kp, km, qn in [(x[0], x[1], x[4] // q_gcd) for x in irrep_blocks]:
                        ph = Fraction(kp * m, a) + Fraction(km * n, b) + Fraction(qn, 1) * th
                        if ph.denominator != 1:
                            ok = False
                            break
                    if ok:
                        kernel_elems.add((m, n, th))
    kernel_order = len(kernel_elems)

    # Collar-odd scalar P Phi = -Phi leaves the (-1)-eigenspace (dim b) and kills (+1)-eigenspace (dim a)
    return {
        "d": d,
        "a_plus": a,
        "b_minus": b,
        "centralizer_dim": centralizer_dim,
        "fock_even_dim": len(charges_even),
        "is_chiral": is_chiral,
        "tr_Y": tr_Y,
        "tr_Y3": tr_Y3,
        "two_tr_SUa2_Y": two_tr_SUa2_Y,
        "two_tr_SUb2_Y": two_tr_SUb2_Y,
        "all_anomalies_zero": all_anomalies_zero,
        "kernel_order": kernel_order,
        "collar_odd_kept_dim": b,
        "collar_odd_killed_dim": a,
        "charges_even": charges_even if d <= 6 else f"len={len(charges_even)}",
        "is_sm_exact": (
            centralizer_dim == 12
            and len(charges_even) == 16
            and is_chiral
            and all_anomalies_zero
            and kernel_order == 6
            and b == 2
            and a == 3
            and charges_even == [-4, -4, -4, -3, -3, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 6]
        ),
    }


# ---------------------------------------------------------------------------
# Task OW1-A: Open-Weave Finite Ladder Delta(2,3,N) (N = 2, 3, 4, 5)
# ---------------------------------------------------------------------------

def build_delta_23N(N):
    """Explicit permutation representation of Delta(2,3,N) = <s, u | s^2 = u^3 = (su)^N = 1>."""
    if N == 2:
        # S_3 on {0,1,2}: s=(0,1), u=(0,1,2) => s*u=(1,2) order 2
        s = (1, 0, 2)
        u = (1, 2, 0)
        deg = 3
    elif N == 3:
        # A_4 on {0,1,2,3}: s=(0,1)(2,3), u=(0,1,2) => s*u=(0,2,3)? Let's check exact order!
        s = (1, 0, 3, 2)
        u = (1, 2, 0, 3)
        deg = 4
    elif N == 4:
        # S_4 on {0,1,2,3}: s=(0,1), u=(1,2,3) => s*u=(0,1,2,3) order 4!
        s = (1, 0, 2, 3)
        u = (0, 2, 3, 1)
        deg = 4
    elif N == 5:
        # A_5 on {0,1,2,3,4}: s=(0,1)(2,3), u=(1,2,4) => s*u=(0,1,3,2,4) order 5!
        s = (1, 0, 3, 2, 4)
        u = (0, 2, 4, 3, 1)
        deg = 5
    else:
        raise ValueError(f"Unsupported finite rung N={N}")

    su = perm_mul(s, u)
    assert perm_order(s) == 2, f"s order != 2 for N={N}"
    assert perm_order(u) == 3, f"u order != 3 for N={N}"
    assert perm_order(su) == N, f"(su) order != {N} (got {perm_order(su)})"
    elems = generate_perm_group([s, u], deg)
    idx = {e: i for i, e in enumerate(elems)}
    n = len(elems)
    mul_table = [[idx[perm_mul(elems[i], elems[j])] for j in range(n)] for i in range(n)]
    inv_table = [idx[perm_inv(elems[i])] for i in range(n)]
    return elems, idx, mul_table, inv_table, idx[s], idx[u], idx[su]


def verify_a5_d5_weyl_identity_and_car():
    """
    Build Z (5-cycle) and P (double transposition) directly inside D_5 < A_5 (zero mention of m004!),
    verify 24 Weyl operators and -(1/2) sum_{v != 0} D(v) = (1/2) I_5 - (5/2) P = diag(-2,-2,-2,+3,+3)
    both algebraically mod Phi_5(zeta) and numerically at 60-digit mpmath precision,
    plus explicit Berezin-CAR Cl(10) anticommutator and Pfaffian verification.
    """
    # Inside A_5 on {0,1,2,3,4}:
    # Z = (0 1 2 3 4) (even permutation, order 5)
    # P = (1 4)(2 3)  (even permutation, order 2, fixes 0)
    Z_perm = (1, 2, 3, 4, 0)
    P_perm = (0, 4, 3, 2, 1)
    assert perm_order(Z_perm) == 5
    assert perm_order(P_perm) == 2
    assert perm_mul(perm_mul(P_perm, Z_perm), P_perm) == perm_inv(Z_perm)
    D5_elems = generate_perm_group([Z_perm, P_perm], 5)
    assert len(D5_elems) == 10

    # Exact cyclotomic ring Q(zeta_5) = Q[w] / (w^4 + w^3 + w^2 + w + 1)
    w = sp.Symbol("w")
    phi5 = w**4 + w**3 + w**2 + w + 1

    def red5(expr):
        return sp.rem(sp.expand(expr), phi5, w)

    # Clock Z_op = diag(1, w, w^2, w^3, w^4), shift X_op |j> = |j+1 mod 5>, parity P_op |j> = |-j mod 5>
    # Notice P_op is literally the permutation matrix of P_perm = (0)(1 4)(2 3)!
    # Check: P_op Z_op P_op = Z_op^{-1}, P_op X_op P_op = X_op^{-1}, Z_op X_op = w X_op Z_op.
    def mat_mul_5(A, B):
        return [[red5(sum(A[i][k] * B[k][j] for k in range(5))) for j in range(5)] for i in range(5)]

    Z_op = [[w**i if i == j else sp.Integer(0) for j in range(5)] for i in range(5)]
    X_op = [[sp.Integer(1) if (i - j) % 5 == 1 else sp.Integer(0) for j in range(5)] for i in range(5)]
    P_op = [[sp.Integer(1) if P_perm[j] == i else sp.Integer(0) for j in range(5)] for i in range(5)]

    # Precompute powers X^a, Z^b
    I5 = [[sp.Integer(1) if i == j else sp.Integer(0) for j in range(5)] for i in range(5)]
    Xp = [I5]
    Zp = [I5]
    for _ in range(4):
        Xp.append(mat_mul_5(Xp[-1], X_op))
        Zp.append(mat_mul_5(Zp[-1], Z_op))

    # Weyl operators D(a, b) = w^{3*a*b} X^a Z^b (since 3 = 2^{-1} mod 5, D(a,b)^dag = D(-a,-b), Tr(D(a,b) P) = 1!)
    inv2_mod5 = 3
    sum_D = [[sp.Integer(0) for _ in range(5)] for _ in range(5)]
    tr_DP_exact_ok = True
    for a in range(5):
        for b in range(5):
            if a == 0 and b == 0:
                continue
            phase = red5(w ** ((inv2_mod5 * a * b) % 5))
            XaZb = mat_mul_5(Xp[a], Zp[b])
            Dab = [[red5(phase * XaZb[i][j]) for j in range(5)] for i in range(5)]
            # Check Tr(Dab * P_op) == 1 mod phi5
            tr_dp = red5(sum(Dab[i][k] * P_op[k][i] for i in range(5) for k in range(5)))
            if tr_dp != sp.Integer(1):
                tr_DP_exact_ok = False
            for i in range(5):
                for j in range(5):
                    sum_D[i][j] = red5(sum_D[i][j] + Dab[i][j])

    # Compute Q_op = -(1/2) * sum_{v != 0} D(v) and compare with (1/2) I_5 - (5/2) P_op
    Q_op = [[red5(-sp.Rational(1, 2) * sum_D[i][j]) for j in range(5)] for i in range(5)]
    target_op = [[red5(sp.Rational(1, 2) * I5[i][j] - sp.Rational(5, 2) * P_op[i][j]) for j in range(5)] for i in range(5)]
    exact_weyl_identity_ok = all(red5(Q_op[i][j] - target_op[i][j]) == 0 for i in range(5) for j in range(5))

    # Diagonalize in exact P-eigenbasis:
    # +1 eigenvectors: e0, (e1+e4)/sqrt(2), (e2+e3)/sqrt(2)
    # -1 eigenvectors: (e1-e4)/sqrt(2), (e2-e3)/sqrt(2)
    s2 = sp.sqrt(2)
    U_P = sp.Matrix([
        [1, 0, 0, 0, 0],
        [0, 1 / s2, 0, 1 / s2, 0],
        [0, 0, 1 / s2, 0, 1 / s2],
        [0, 0, 1 / s2, 0, -1 / s2],
        [0, 1 / s2, 0, -1 / s2, 0],
    ])
    Q_mat = sp.Matrix(Q_op)
    Q_diag = sp.simplify(U_P.T * Q_mat * U_P)
    expected_diag = sp.diag(-2, -2, -2, 3, 3)
    exact_diag_ok = (Q_diag == expected_diag)

    # 60-digit mpmath numerical verification of orthonormality, Tr(D P)=1, and Q_op identity
    mp.mp.dps = 65
    zeta = mp.exp(mp.mpc(0, 2) * mp.pi / mp.mpf(5))
    P_mp = mp.matrix([[mp.mpf(1) if P_perm[j] == i else mp.mpf(0) for j in range(5)] for i in range(5)])
    X_mp = mp.matrix([[mp.mpf(1) if (i - j) % 5 == 1 else mp.mpf(0) for j in range(5)] for i in range(5)])
    Z_mp = mp.matrix([[zeta**i if i == j else mp.mpf(0) for j in range(5)] for i in range(5)])
    D_list = []
    max_tr_dp_err = mp.mpf(0)
    sum_D_mp = mp.zeros(5, 5)
    for a in range(5):
        for b in range(5):
            Dab = (zeta ** ((inv2_mod5 * a * b) % 5)) * (X_mp**a) * (Z_mp**b)
            D_list.append(Dab)
            if not (a == 0 and b == 0):
                sum_D_mp += Dab
                tr_v = sum((Dab * P_mp)[i, i] for i in range(5))
                err_v = abs(tr_v - mp.mpf(1))
                if err_v > max_tr_dp_err:
                    max_tr_dp_err = err_v

    max_ortho_err = mp.mpf(0)
    for idx1, D1 in enumerate(D_list):
        D1H = D1.transpose_conj()
        for idx2, D2 in enumerate(D_list):
            tr_val = sum((D1H * D2)[i, i] for i in range(5)) / mp.mpf(5)
            target = mp.mpf(1) if idx1 == idx2 else mp.mpf(0)
            err = abs(tr_val - target)
            if err > max_ortho_err:
                max_ortho_err = err

    Q_mp = -mp_rat(1, 2) * sum_D_mp
    target_mp = mp_rat(1, 2) * mp.eye(5) - mp_rat(5, 2) * P_mp
    max_weyl_id_err = max(abs(Q_mp[i, j] - target_mp[i, j]) for i in range(5) for j in range(5))

    # Explicit 32-dim Berezin-CAR algebra Cl(10) on Lambda^*(W_5): verify {c_i, c_j^dag} = delta_ij
    dim_f = 32
    c_dag = []
    c_ann = []
    for k in range(5):
        Cd = [[0] * dim_f for _ in range(dim_f)]
        Ca = [[0] * dim_f for _ in range(dim_f)]
        bit = 1 << k
        for mask in range(dim_f):
            if not (mask & bit):
                # sign = (-1)^(number of set bits below k)
                below = bin(mask & (bit - 1)).count("1")
                sgn = -1 if (below % 2 == 1) else 1
                Cd[mask | bit][mask] = sgn
                Ca[mask][mask | bit] = sgn
        c_dag.append(Cd)
        c_ann.append(Ca)

    def mat_mul_int(A, B):
        n = len(A)
        return [[sum(A[i][m] * B[m][j] for m in range(n)) for j in range(n)] for i in range(n)]

    car_errors = 0
    for i in range(5):
        for j in range(5):
            # {c_i, c_j^dag} == delta_ij * I
            ac1 = mat_mul_int(c_ann[i], c_dag[j])
            ac2 = mat_mul_int(c_dag[j], c_ann[i])
            for r in range(dim_f):
                for c in range(dim_f):
                    val = ac1[r][c] + ac2[r][c]
                    exp = 1 if (i == j and r == c) else 0
                    if val != exp:
                        car_errors += 1
            # {c_i, c_j} == 0
            cc1 = mat_mul_int(c_ann[i], c_ann[j])
            cc2 = mat_mul_int(c_ann[j], c_ann[i])
            for r in range(dim_f):
                for c in range(dim_f):
                    if cc1[r][c] + cc2[r][c] != 0:
                        car_errors += 1

    return {
        "d5_order_inside_a5": len(D5_elems),
        "tr_DP_exact_mod_phi5": tr_DP_exact_ok,
        "exact_weyl_identity_mod_phi5": exact_weyl_identity_ok,
        "exact_P_eigenbasis_diag_ok": exact_diag_ok,
        "max_ortho_err_65dps": mp.nstr(max_ortho_err, 12),
        "max_tr_dp_err_65dps": mp.nstr(max_tr_dp_err, 12),
        "max_weyl_id_err_65dps": mp.nstr(max_weyl_id_err, 12),
        "mpmath_lt_1e50": bool(
            max_ortho_err < mp.power(10, -50)
            and max_tr_dp_err < mp.power(10, -50)
            and max_weyl_id_err < mp.power(10, -50)
        ),
        "car_cl10_exact_errors": car_errors,
    }


def run_task_ow1_a():
    # Spherical finiteness check: 1/2 + 1/3 + 1/N > 1 <=> N < 6
    finiteness_table = {}
    for N in range(2, 9):
        lhs = Fraction(1, 2) + Fraction(1, 3) + Fraction(1, N)
        finiteness_table[str(N)] = {
            "angle_sum": f"{lhs.numerator}/{lhs.denominator}",
            "spherical_finite": (lhs > 1),
        }

    ladder_results = {}
    sm_hits = []
    a5_structural = {}
    for N in (2, 3, 4, 5):
        elems, idx, mul_table, inv_table, s_id, u_id, su_id = build_delta_23N(N)
        order_G = len(elems)
        subgroups = enumerate_subgroups_up_to_conj(mul_table, inv_table, order_G, max_index=12)
        cclasses = conjugacy_classes_abstract(mul_table, inv_table, order_G)
        inv_classes = [cls for cls in cclasses if mul_table[cls[0]][cls[0]] == 0 and cls[0] != 0]

        if N == 5:
            # Verify unique conjugacy class of index-5 A_4 subgroups, index-6 D_5 subgroups, and involutions
            idx5_subs = [sg for sg in subgroups if sg["index"] == 5 and sg["core_free"]]
            idx6_subs = [sg for sg in subgroups if sg["index"] == 6 and sg["core_free"]]
            a5_structural = {
                "order_A5": order_G,
                "num_involution_classes": len(inv_classes),
                "involution_class_sizes": [len(c) for c in inv_classes],
                "num_index5_A4_classes": len(idx5_subs),
                "num_index6_D5_classes": len(idx6_subs),
                "index6_D5_order": idx6_subs[0]["order"] if idx6_subs else 0,
                "index6_D5_num_conjugates": idx6_subs[0]["num_conjugates"] if idx6_subs else 0,
            }

        faithful_actions = []
        for sg in subgroups:
            if not sg["core_free"]:
                continue
            H = set(sg["subgroup"])
            # Build left cosets
            seen_g = set()
            coset_reps = []
            coset_id = {}
            for g in range(order_G):
                if g in seen_g:
                    continue
                cid = len(coset_reps)
                coset_reps.append(g)
                for h in H:
                    gh = mul_table[g][h]
                    seen_g.add(gh)
                    coset_id[gh] = cid
            d = len(coset_reps)
            inv_reports = []
            for ic_idx, cls in enumerate(inv_classes):
                P_id = cls[0]
                P_perm = coset_action_perm(mul_table, H, P_id, coset_reps, coset_id)
                ctype = perm_cycle_type(P_perm)
                # Each 1-cycle contributes (+1); each 2-cycle contributes (+1, -1)
                n_fix = ctype.count(1)
                n_pairs = ctype.count(2)
                a_plus = n_fix + n_pairs
                b_minus = n_pairs
                assert a_plus + b_minus == d
                gm = analyze_involution_gauge_matter(a_plus, b_minus)
                rec = {
                    "involution_class": ic_idx,
                    "class_size": len(cls),
                    "cycle_type": list(ctype),
                    "gauge_matter": gm,
                }
                inv_reports.append(rec)
                if gm["is_sm_exact"]:
                    sm_hits.append({
                        "N": N,
                        "degree": d,
                        "subgroup_order": sg["order"],
                        "involution_class": ic_idx,
                        "cycle_type": list(ctype),
                    })
            faithful_actions.append({
                "degree": d,
                "stabilizer_order": sg["order"],
                "num_conjugate_stabilizers": sg["num_conjugates"],
                "involution_analyses": inv_reports,
            })

        ladder_results[str(N)] = {
            "group_order": order_G,
            "num_involution_classes": len(inv_classes),
            "faithful_transitive_actions_d_le_12": faithful_actions,
        }

    weyl_car = verify_a5_d5_weyl_identity_and_car()
    unique_sm_hit = (
        len(sm_hits) == 1
        and sm_hits[0]["N"] == 5
        and sm_hits[0]["degree"] == 5
        and sm_hits[0]["cycle_type"] == [1, 2, 2]
    )
    pass_ow1_a = (
        unique_sm_hit
        and a5_structural.get("num_involution_classes") == 1
        and a5_structural.get("num_index5_A4_classes") == 1
        and a5_structural.get("num_index6_D5_classes") == 1
        and a5_structural.get("index6_D5_order") == 10
        and weyl_car["tr_DP_exact_mod_phi5"]
        and weyl_car["exact_weyl_identity_mod_phi5"]
        and weyl_car["exact_P_eigenbasis_diag_ok"]
        and weyl_car["mpmath_lt_1e50"]
        and weyl_car["car_cl10_exact_errors"] == 0
    )
    return {
        "finiteness_table": finiteness_table,
        "a5_structural": a5_structural,
        "sm_hits_across_all_rungs_d_le_12": sm_hits,
        "unique_sm_hit_is_A5_deg5": unique_sm_hit,
        "weyl_and_car_inside_A5": weyl_car,
        "ladder_details": ladder_results,
        "pass": pass_ow1_a,
    }


# ---------------------------------------------------------------------------
# Exact Finite-Group Homomorphism Engines: D_p, 2T = SL(2, F_3), A_5 = PSL(2, F_5)
# ---------------------------------------------------------------------------

def build_group_Dp(p):
    """D_p of order 2p: element (eps, k) where eps in {0, 1}, k in Z/p.
    Product: (e1, k1)*(e2, k2) = (e1^e2, (k1 + (-1)^e1 * k2) mod p).
    Index i = eps * p + k.
    """
    n = 2 * p
    mul = [[0] * n for _ in range(n)]
    inv = [0] * n
    for e1 in (0, 1):
        for k1 in range(p):
            i = e1 * p + k1
            # inverse of (0, k) is (0, -k); inverse of (1, k) is (1, k)
            inv[i] = ((-k1) % p) if e1 == 0 else i
            for e2 in (0, 1):
                for k2 in range(p):
                    j = e2 * p + k2
                    e3 = e1 ^ e2
                    k3 = (k1 + (k2 if e1 == 0 else -k2)) % p
                    mul[i][j] = e3 * p + k3
    # Aut(D_p) has order p*(p-1): (0,1)->(0, u), (1,0)->(1, s), u in (Z/p)^*, s in Z/p
    aut_order = p * (p - 1)
    return {
        "name": f"D_{p}",
        "p": p,
        "n": n,
        "mul": mul,
        "inv": inv,
        "aut_order": aut_order,
    }


def build_group_2T():
    """2T = SL(2, F_3) of order 24."""
    mats = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    if (a * d - b * c) % 3 == 1:
                        mats.append((a, b, c, d))
    assert len(mats) == 24
    # Put identity (1,0,0,1) at index 0
    mats.remove((1, 0, 0, 1))
    mats = [(1, 0, 0, 1)] + mats
    idx = {m: i for i, m in enumerate(mats)}

    def mm(x, y):
        return (
            (x[0] * y[0] + x[1] * y[2]) % 3,
            (x[0] * y[1] + x[1] * y[3]) % 3,
            (x[2] * y[0] + x[3] * y[2]) % 3,
            (x[2] * y[1] + x[3] * y[3]) % 3,
        )

    mul = [[idx[mm(mats[i], mats[j])] for j in range(24)] for i in range(24)]
    inv = [idx[(mats[i][3], (-mats[i][1]) % 3, (-mats[i][2]) % 3, mats[i][0])] for i in range(24)]
    # |Aut(SL(2, F_3))| = |PGL(2, F_3)| = 24
    # Also compute abelianization cosets: 2T / Q_8 = Z/3
    # Q_8 is the unique Sylow-2 subgroup (elements of order 1, 2, 4)
    ords = []
    for i in range(24):
        cur = i
        o = 1
        while cur != 0:
            cur = mul[cur][i]
            o += 1
        ords.append(o)
    Q8 = {i for i in range(24) if ords[i] in (1, 2, 4)}
    assert len(Q8) == 8
    # Pick an order-3 element g3 -> cosets Q8, g3*Q8, g3^2*Q8
    g3 = next(i for i in range(24) if ords[i] == 3)
    c1 = {mul[g3][h] for h in Q8}
    c2 = {mul[mul[g3][g3]][h] for h in Q8}
    ab_map = [0 if i in Q8 else (1 if i in c1 else 2) for i in range(24)]
    return {
        "name": "2T",
        "n": 24,
        "mul": mul,
        "inv": inv,
        "ords": ords,
        "ab_map": ab_map,
        "aut_order": 24,
    }


def build_group_A5():
    """A_5 = PSL(2, F_5) of order 60."""
    elems, idx, mul, inv, _, _, _ = build_delta_23N(5)
    assert len(elems) == 60
    ords = [perm_order(e) for e in elems]
    # |Aut(A_5)| = |S_5| = 120
    # Compute Aut(A_5) orbits on elements (conjugation in S_5): 1->1, 2->15, 3->20, 5->24
    # In S_5, all 5-cycles are conjugate! So 4 Aut-orbits of non-identity elements? Actually 3: order 2, 3, 5!
    return {
        "name": "A5",
        "n": 60,
        "mul": mul,
        "inv": inv,
        "ords": ords,
        "elems": elems,
        "aut_order": 120,
    }


def precompute_conjugators(G):
    """For group G, conj_to[(x, y)] = list of g in G with g * x * g^-1 == y."""
    n = G["n"]
    mul = G["mul"]
    inv = G["inv"]
    conj = {}
    for x in range(n):
        for g in range(n):
            y = mul[mul[g][x]][inv[g]]
            conj.setdefault((x, y), []).append(g)
    return conj


def eval_word_G(word, gen_vals, G):
    """Evaluate word represented as list of signed 1-based generator indices (+k or -k)."""
    mul = G["mul"]
    inv = G["inv"]
    acc = 0
    for lit in word:
        if lit > 0:
            acc = mul[acc][gen_vals[lit - 1]]
        else:
            acc = mul[acc][inv[gen_vals[-lit - 1]]]
    return acc


def is_surjective_G(gens, G):
    n = G["n"]
    mul = G["mul"]
    seen = {0}
    q = deque([0])
    for g in gens:
        if g not in seen:
            seen.add(g)
            q.append(g)
    while q:
        cur = q.popleft()
        for g in gens:
            nxt = mul[cur][g]
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
                if len(seen) == n:
                    return True
    return len(seen) == n


# ---------------------------------------------------------------------------
# Task OW1-B: Unblocked Punctured-Torus Bundle Census (No G:SE1, No G:SE2)
# ---------------------------------------------------------------------------

def reduce_free_word(w):
    st = []
    for x in w:
        if st and st[-1] == -x:
            st.pop()
        else:
            st.append(x)
    return tuple(st)


def compose_f2_aut(aut2, aut1):
    """Compose aut2 o aut1 on F_2 = <1=a, 2=b>: apply aut1 first, then aut2 to each letter."""
    out = []
    for img in aut1:
        res = []
        for lit in img:
            if lit > 0:
                res.extend(aut2[lit - 1])
            else:
                res.extend([-z for z in reversed(aut2[-lit - 1])])
        out.append(reduce_free_word(res))
    return tuple(out)


# Exact surface automorphisms of F_2 = <a=1, b=2>:
# phi_L: a -> a, b -> b*a  (mat [[1,1],[0,1]], preserves [a,b] = a b a^-1 b^-1)
# phi_R: a -> a*b, b -> b  (mat [[1,0],[1,1]], preserves [a,b])
# phi_P: a -> b, b -> a    (mat [[0,1],[1,0]], reverses [a,b] -> [a,b]^-1)
# phi_S: a -> b^-1, b -> b*a*b^-1 (preserves [a,b])
# phi_negI = phi_S^2: a -> b a^-1 b^-1, b -> b a b^-1 a^-1 b^-1 (mat -I, preserves [a,b])
PHI_ID = ((1,), (2,))
PHI_L = ((1,), (2, 1))
PHI_R = ((1, 2), (2,))
PHI_P = ((2,), (1,))
PHI_S = ((-2,), (2, 1, -2))
PHI_NEGI = compose_f2_aut(PHI_S, PHI_S)


def aut_matrix(phi):
    """Exact 2x2 abelianization matrix M (columns = images of a, b)."""
    c00 = sum(1 if x == 1 else (-1 if x == -1 else 0) for x in phi[0])
    c10 = sum(1 if x == 2 else (-1 if x == -2 else 0) for x in phi[0])
    c01 = sum(1 if x == 1 else (-1 if x == -1 else 0) for x in phi[1])
    c11 = sum(1 if x == 2 else (-1 if x == -2 else 0) for x in phi[1])
    return ((c00, c01), (c10, c11))


def word_to_aut(word_str, branch):
    """Build exact F_2 automorphism for branch in ('+', '-', 'P') and word_str in {L, R}+."""
    phi = PHI_ID
    # Composition: left-to-right matrix product M_1 M_2 ... M_k applies right-to-left on vectors
    if branch == "P":
        phi = compose_f2_aut(PHI_P, phi)
    for ch in reversed(word_str):
        step = PHI_L if ch == "L" else PHI_R
        phi = compose_f2_aut(step, phi)
    if branch == "-":
        phi = compose_f2_aut(PHI_NEGI, phi)
    return phi


def is_primitive_word(w):
    n = len(w)
    for d in range(1, n):
        if n % d == 0 and w[:d] * (n // d) == w:
            return False
    return True


def canonical_cyclic_word(w):
    """Up to cyclic rotation only (keeping mirror/chiral partner distinct if different!)."""
    rots = [w[i:] + w[:i] for i in range(len(w))]
    return min(rots)


def mat_mul_2x2(A, B):
    return (
        (A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
        (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]),
    )


def count_bundle_surjections(phi, G, conj_G):
    """
    Exact count of surjective homomorphisms pi_1(M_phi) ->> G modulo Aut(G),
    where pi_1(M_phi) = <a, b, t | t a t^-1 = phi(a), t b t^-1 = phi(b)>.
    Also check if cusp puncture [a, b] = a b a^-1 b^-1 maps to 0 (identity) in ALL surjections.
    """
    n = G["n"]
    mul = G["mul"]
    inv = G["inv"]
    phi_a, phi_b = phi
    comm_word = (1, 2, -1, -2)

    total_surj = 0
    comm_all_trivial = True
    comm_non_trivial_count = 0

    for ga in range(n):
        for gb in range(n):
            img_a = eval_word_G(phi_a, (ga, gb), G)
            cands_a = conj_G.get((ga, img_a))
            if not cands_a:
                continue
            img_b = eval_word_G(phi_b, (ga, gb), G)
            cands_b = conj_G.get((gb, img_b))
            if not cands_b:
                continue
            # Intersection of conjugators
            sb = set(cands_b)
            common_t = [gt for gt in cands_a if gt in sb]
            if not common_t:
                continue
            for gt in common_t:
                if is_surjective_G((ga, gb, gt), G):
                    total_surj += 1
                    c_val = eval_word_G(comm_word, (ga, gb), G)
                    if c_val != 0:
                        comm_all_trivial = False
                        comm_non_trivial_count += 1

    assert total_surj % G["aut_order"] == 0, (
        f"Total surj {total_surj} not divisible by |Aut({G['name']})|={G['aut_order']}"
    )
    return {
        "total": total_surj,
        "classes": total_surj // G["aut_order"],
        "cusp_comm_all_trivial": (comm_all_trivial if total_surj > 0 else None),
        "cusp_comm_nontrivial_count": comm_non_trivial_count,
    }


def snappy_homology_torsion(M):
    """Exact torsion order from SnapPy AbelianGroup M.homology()."""
    H = M.homology()
    tor = 1
    for e in H.elementary_divisors():
        if e != 0:
            tor *= int(e)
    return tor, str(H)


def run_task_ow1_b(groups_Dp, G_2T, G_A5, conj_map):
    # Verify exact commutator preservation of our F_2 automorphisms first!
    comm = (1, 2, -1, -2)
    for name, phi, expected_img in [
        ("L", PHI_L, comm),
        ("R", PHI_R, comm),
        ("S", PHI_S, comm),
        ("-I", PHI_NEGI, comm),
        ("P", PHI_P, (2, 1, -2, -1)),
    ]:
        # Apply phi to comm
        res = []
        for lit in comm:
            if lit > 0:
                res.extend(phi[lit - 1])
            else:
                res.extend([-z for z in reversed(phi[-lit - 1])])
        assert reduce_free_word(res) == expected_img, f"Commutator check failed for {name}"

    # Enumerate all primitive cyclic words up to length 6
    # Orientable branches '+' and '-': must contain both L and R (length 2..6).
    # Non-orientable branch 'P': any primitive word in {L, R} of length 1..6 (with L*R*P etc., deduplicated by SnapPy trace/word up to cyclic+swap equivalence in GL_2(Z)? Keep ALL primitive words of length 1..6 for '+'/'-', and for 'P' keep all primitive words of length 1..5 where tr(M*P) != 0 so every distinct non-orientable class is included!).
    orient_words = set()
    for L_len in range(2, 7):
        for tup in itertools.product("LR", repeat=L_len):
            w = "".join(tup)
            if "L" not in w or "R" not in w:
                continue
            if not is_primitive_word(w):
                continue
            orient_words.add(canonical_cyclic_word(w))
    orient_words = sorted(orient_words, key=lambda s: (len(s), s))

    # For branch P (det = -1): M(w) * P. Deduplicate exact conjugacy classes in GL_2(Z) via SnapPy manifold isometric check or matrix trace + cyclic/swap!
    # Keep ALL words in {L, R} of length 1..5 up to cyclic rotation of M*P:
    # Note P * L * P = R and P * R * P = L, so (w1 w2 ... wk P) is conjugate to (w2 ... wk (swap w1) P)!
    def swap_lr(s):
        return "".join("R" if c == "L" else "L" for c in s)

    def canonical_nonorient_word(w):
        # Under conjugation by first letter x in {L, R}: x^-1 (x u P) x = u P x = u (swap(x)) P!
        # Also conjugation by P sends (w P) -> swap(w) P!
        orbit = set()
        cur = w
        for _ in range(2 * len(w)):
            orbit.add(cur)
            orbit.add(swap_lr(cur))
            cur = cur[1:] + swap_lr(cur[0])
        return min(orbit)

    nonorient_words = set()
    for L_len in range(1, 6):
        for tup in itertools.product("LR", repeat=L_len):
            w = "".join(tup)
            # Check primitivity of M*P: if w = u + swap(u) + u + ..., (u P)^k has odd k!
            # Exclude odd powers of shorter P-words:
            is_prim = True
            for d in range(1, L_len):
                if L_len % d == 0 and (L_len // d) % 2 == 1:
                    k = L_len // d
                    u = w[:d]
                    built = "".join(u if j % 2 == 0 else swap_lr(u) for j in range(k))
                    if built == w:
                        is_prim = False
                        break
            if is_prim:
                nonorient_words.add(canonical_nonorient_word(w))
    nonorient_words = sorted(nonorient_words, key=lambda s: (len(s), s))

    threads = []
    h1_mismatches = 0

    def process_thread(branch, w):
        nonlocal h1_mismatches
        phi = word_to_aut(w, branch)
        M_mat = aut_matrix(phi)
        det_M = M_mat[0][0] * M_mat[1][1] - M_mat[0][1] * M_mat[1][0]
        tr_M = M_mat[0][0] + M_mat[1][1]
        # Torsion of H_1(M_phi) = |det(M - I)|
        h1_tor_alg = abs((M_mat[0][0] - 1) * (M_mat[1][1] - 1) - M_mat[0][1] * M_mat[1][0])

        snappy_prefix = {"+": "b++", "-": "b+-", "P": "b-+"}[branch]
        snappy_name = snappy_prefix + w
        M_sp = snappy.Manifold(snappy_name)
        tor_sp, h1_str_sp = snappy_homology_torsion(M_sp)
        if tor_sp != h1_tor_alg:
            h1_mismatches += 1
        vol_str = f"{float(M_sp.volume()):.6f}"
        census_ids = [str(x) for x in M_sp.identify()[:2]]
        is_orient = bool(M_sp.is_orientable())
        if is_orient:
            try:
                is_amphi = bool(M_sp.is_isometric_to(M_sp.reverse_orientation()))
            except Exception:
                is_amphi = None
            try:
                cs_val = f"{float(M_sp.chern_simons()):.6f}"
            except Exception:
                cs_val = "unavailable"
        else:
            is_amphi = None
            cs_val = "non_orientable"

        dp_counts = {}
        d5_cusp_trivial = None
        for p in (3, 5, 7, 11, 13):
            res_p = count_bundle_surjections(phi, groups_Dp[p], conj_map[f"D_{p}"])
            dp_counts[str(p)] = res_p["classes"]
            if p == 5:
                d5_cusp_trivial = res_p["cusp_comm_all_trivial"]

        res_2T = count_bundle_surjections(phi, G_2T, conj_map["2T"])
        res_A5 = count_bundle_surjections(phi, G_A5, conj_map["A5"])

        return {
            "branch": branch,
            "word": w,
            "snappy_name": snappy_name,
            "census_ids": census_ids,
            "det_M": det_M,
            "tr_M": tr_M,
            "orientable": is_orient,
            "h1_torsion_alg": h1_tor_alg,
            "h1_torsion_snappy": tor_sp,
            "h1_str": h1_str_sp,
            "volume": vol_str,
            "is_amphichiral": is_amphi,
            "chern_simons": cs_val,
            "D_p_classes": dp_counts,
            "D5_cusp_comm_all_trivial": d5_cusp_trivial,
            "2T_classes": res_2T["classes"],
            "A5_classes": res_A5["classes"],
        }

    for branch in ("+", "-"):
        for w in orient_words:
            threads.append(process_thread(branch, w))
    for w in nonorient_words:
        threads.append(process_thread("P", w))

    # Summarize survival sets
    has_D5 = [t["snappy_name"] for t in threads if t["D_p_classes"]["5"] > 0]
    has_D5_triv_cusp = [
        t["snappy_name"]
        for t in threads
        if t["D_p_classes"]["5"] > 0 and t["D5_cusp_comm_all_trivial"] is True
    ]
    has_2T = [t["snappy_name"] for t in threads if t["2T_classes"] > 0]
    has_both_D5_2T = [
        t["snappy_name"]
        for t in threads
        if t["D_p_classes"]["5"] > 0 and t["2T_classes"] > 0
    ]
    has_both_D5triv_2T = [
        t["snappy_name"]
        for t in threads
        if t["D_p_classes"]["5"] > 0 and t["D5_cusp_comm_all_trivial"] is True and t["2T_classes"] > 0
    ]
    has_A5 = [t["snappy_name"] for t in threads if t["A5_classes"] > 0]
    chiral_with_D5triv_2T = [
        t["snappy_name"]
        for t in threads
        if t["D_p_classes"]["5"] > 0
        and t["D5_cusp_comm_all_trivial"] is True
        and t["2T_classes"] > 0
        and t["is_amphichiral"] is False
    ]

    return {
        "total_threads_tested": len(threads),
        "orient_plus_count": len(orient_words),
        "orient_minus_count": len(orient_words),
        "nonorient_P_count": len(nonorient_words),
        "h1_alg_vs_snappy_mismatches": h1_mismatches,
        "threads_with_D5": has_D5,
        "threads_with_D5_trivial_cusp": has_D5_triv_cusp,
        "threads_with_2T": has_2T,
        "threads_with_both_D5_and_2T": has_both_D5_2T,
        "threads_with_both_D5_triv_cusp_and_2T": has_both_D5triv_2T,
        "threads_with_A5": has_A5,
        "chiral_orientable_threads_with_D5triv_and_2T": chiral_with_D5triv_2T,
        "threads": threads,
        "pass": (h1_mismatches == 0 and len(threads) > 0),
    }


# ---------------------------------------------------------------------------
# Task OW1-C: Unblocked MC:REACH Census of All 35 Prime Knots <= 8 Crossings
# ---------------------------------------------------------------------------

def parse_snappy_word(w_str, gen_index):
    """Parse SnapPy word string ('a', 'b', 'A'=a^-1, 'B'=b^-1, ...) into signed 1-based list."""
    out = []
    for ch in w_str:
        if ch.islower():
            out.append(gen_index[ch] + 1)
        elif ch.isupper():
            out.append(-(gen_index[ch.lower()] + 1))
    return tuple(out)


def abelianization_weights(num_gens, relators):
    """Exact integer weights w_0..w_{n-1} (gcd = 1) generating H_1 = Z."""
    rows = []
    for r in relators:
        row = [0] * num_gens
        for lit in r:
            if lit > 0:
                row[lit - 1] += 1
            else:
                row[-lit - 1] -= 1
        rows.append(row)
    M = sp.Matrix(rows)
    ns = M.nullspace()
    assert len(ns) == 1, f"Expected 1D abelianization for knot, got {len(ns)}D"
    vec = ns[0]
    lcm_den = 1
    for x in vec:
        lcm_den = math.lcm(lcm_den, int(sp.fraction(x)[1]))
    ints = [int(x * lcm_den) for x in vec]
    g = 0
    for x in ints:
        g = math.gcd(g, abs(x))
    ints = [x // g for x in ints]
    return ints


def fox_determinant_at_minus1(num_gens, relators, ab_weights):
    """
    Exact knot determinant |Delta_K(-1)| via Fox free calculus Jacobian at t = -1
    and exact integer Smith Normal Form (product of nonzero invariant factors).
    """
    # Sign of each generator at t = -1
    gen_sgn = [1 if (w % 2 == 0) else -1 for w in ab_weights]
    rows = []
    for r in relators:
        row = [0] * num_gens
        cur_sgn = 1
        for lit in r:
            if lit > 0:
                j = lit - 1
                row[j] += cur_sgn
                cur_sgn *= gen_sgn[j]
            else:
                j = -lit - 1
                cur_sgn *= gen_sgn[j]
                row[j] -= cur_sgn
        rows.append(row)
    J = sp.Matrix(rows)
    snf = smith_normal_form(J, domain=sp.ZZ)
    inv_factors = []
    for i in range(min(snf.rows, snf.cols)):
        v = abs(int(snf[i, i]))
        if v != 0:
            inv_factors.append(v)
    assert len(inv_factors) == num_gens - 1, f"Expected rank {num_gens - 1}, got {len(inv_factors)}"
    det_val = 1
    for v in inv_factors:
        det_val *= v
    return det_val, inv_factors


def count_knot_Dp_surjections(num_gens, relators, ab_weights, lon_word, G_Dp):
    """Exact exhaustive count of pi_1(K) ->> D_p modulo Aut(D_p), plus longitude image check."""
    p = G_Dp["p"]
    mul = G_Dp["mul"]
    # For each generator j, its parity e_j = ab_weights[j] % 2 determines eps_j in {0, 1}!
    parities = [w % 2 for w in ab_weights]
    odd_gens = [j for j, e in enumerate(parities) if e == 1]
    assert len(odd_gens) >= 1
    # Pin first odd generator to (1, 0) using inner/outer conjugation (factor p for shifts in Z/p)
    # Wait: just enumerate all p^{num_gens} tuples with fixed parity, divide by Aut(D_p) = p*(p-1)!
    # Even better: pin odd_gens[0] = (1, 0) (reduces by factor p!). Every surjection has odd_gens[0] = (1, k)
    # and shifting all reflections by -k is an automorphism of D_p fixing rotations, so factor is exactly p!
    pinned_idx = odd_gens[0]
    choices = []
    for j in range(num_gens):
        if j == pinned_idx:
            choices.append([p + 0])  # (1, 0)
        else:
            e = parities[j]
            choices.append([e * p + k for k in range(p)])

    # Sort relators shortest first for quick rejection
    rels_sorted = sorted(relators, key=len)
    surj_pinned = 0
    lon_all_trivial = True
    for vals in itertools.product(*choices):
        # Quick non-abelian check: must have at least one non-(0,0) rotation or distinct reflection from (1,0)
        if all(v in (0, p) for v in vals):
            continue
        ok = True
        for r in rels_sorted:
            if eval_word_G(r, vals, G_Dp) != 0:
                ok = False
                break
        if not ok:
            continue
        if is_surjective_G(vals, G_Dp):
            surj_pinned += 1
            if eval_word_G(lon_word, vals, G_Dp) != 0:
                lon_all_trivial = False

    # Each Aut(D_p) class has p*(p-1) surjections; pinning one reflection reduces by factor p -> leaves (p-1)!
    assert surj_pinned % (p - 1) == 0, f"Pinned count {surj_pinned} not divisible by {p - 1}"
    return {
        "classes": surj_pinned // (p - 1),
        "longitude_all_trivial": (lon_all_trivial if surj_pinned > 0 else None),
    }


def count_knot_2T_surjections(num_gens, relators, ab_weights, G_2T):
    """Exact exhaustive count of pi_1(K) ->> 2T = SL(2, F_3) modulo Aut(2T)."""
    ab_map = G_2T["ab_map"]
    cosets = [[i for i in range(24) if ab_map[i] == c] for c in range(3)]
    rels_sorted = sorted(relators, key=len)

    # Abelianization Z -> Z/3 sends generator j to (s * ab_weights[j]) mod 3 for s in {1, 2}.
    # Notice s=1 and s=2 are swapped by outer automorphism of 2T (|Aut(2T)| = 24, |Inn(2T)| = 12)!
    # Compute BOTH s=1 and s=2 and divide by |Aut(2T)| = 24 for zero-assumption exactness.
    total_surj = 0
    for s in (1, 2):
        choices = [cosets[(s * w) % 3] for w in ab_weights]
        for vals in itertools.product(*choices):
            ok = True
            for r in rels_sorted:
                if eval_word_G(r, vals, G_2T) != 0:
                    ok = False
                    break
            if not ok:
                continue
            if is_surjective_G(vals, G_2T):
                total_surj += 1
    assert total_surj % G_2T["aut_order"] == 0
    return total_surj // G_2T["aut_order"]


def count_knot_A5_surjections(num_gens, relators, G_A5):
    """
    Exact exhaustive count of pi_1(K) ->> A_5 modulo Aut(A_5) = S_5 (order 120).
    For a knot in S^3, all meridians are conjugate, wait: SnapPy's simplified generators
    may not all be meridians, so we fix ONLY the first generator up to Aut(A_5) = S_5 conjugacy!
    In S_5, the non-identity elements of A_5 form EXACTLY 3 orbits:
      - order 2: size 15
      - order 3: size 20
      - order 5: size 24
    And generator 0 could also be identity (size 1, only possible if num_gens >= 3).
    Multiplying each orbit representative's count by its orbit size recovers the EXACT total!
    """
    ords = G_A5["ords"]
    rep0 = 0
    rep2 = next(i for i in range(60) if ords[i] == 2)
    rep3 = next(i for i in range(60) if ords[i] == 3)
    rep5 = next(i for i in range(60) if ords[i] == 5)
    orbit_reps = [(rep0, 1), (rep2, 15), (rep3, 20), (rep5, 24)]
    rels_sorted = sorted(relators, key=len)

    # Pre-split relators by max generator index for fast backtracking when num_gens >= 3
    rel_at_depth = [[] for _ in range(num_gens)]
    for r in rels_sorted:
        mx = max(abs(x) for x in r) - 1
        rel_at_depth[mx].append(r)

    total_surj = 0
    for g0, orb_sz in orbit_reps:
        if g0 == 0 and num_gens <= 2:
            continue
        cur = [0] * num_gens
        cur[0] = g0
        if any(eval_word_G(r, cur, G_A5) != 0 for r in rel_at_depth[0]):
            continue

        cnt_rep = 0

        def dfs(depth):
            nonlocal cnt_rep
            if depth == num_gens:
                if is_surjective_G(cur, G_A5):
                    cnt_rep += 1
                return
            rels_d = rel_at_depth[depth]
            for val in range(60):
                cur[depth] = val
                ok = True
                for r in rels_d:
                    if eval_word_G(r, cur, G_A5) != 0:
                        ok = False
                        break
                if ok:
                    dfs(depth + 1)

        dfs(1)
        total_surj += orb_sz * cnt_rep

    assert total_surj % G_A5["aut_order"] == 0, f"A5 total {total_surj} not div by 120"
    return total_surj // G_A5["aut_order"]


def run_task_ow1_c(groups_Dp, G_2T, G_A5):
    knot_names = (
        ["3_1", "4_1"]
        + [f"5_{i}" for i in range(1, 3)]
        + [f"6_{i}" for i in range(1, 4)]
        + [f"7_{i}" for i in range(1, 8)]
        + [f"8_{i}" for i in range(1, 22)]
    )
    assert len(knot_names) == 35

    results = []
    det_div_mismatches = 0
    for name in knot_names:
        M = snappy.Manifold(name)
        fg = M.fundamental_group()
        gens = fg.generators()
        gidx = {g: i for i, g in enumerate(gens)}
        rels = [parse_snappy_word(r, gidx) for r in fg.relators()]
        periph = fg.peripheral_curves()[0]
        lon_word = parse_snappy_word(periph[1], gidx)
        ab_w = abelianization_weights(len(gens), rels)
        det_val, inv_facs = fox_determinant_at_minus1(len(gens), rels, ab_w)
        assert det_val % 2 == 1, f"Knot {name} determinant {det_val} must be odd!"

        try:
            vol_f = float(M.volume())
        except Exception:
            vol_f = float(0)
        is_hyp = (vol_f > (1 / 1000)) and (M.solution_type() in (
            "all tetrahedra positively oriented",
            "contains negatively oriented tetrahedra",
        ))
        if is_hyp:
            try:
                is_amphi = bool(M.is_isometric_to(M.reverse_orientation()))
            except Exception:
                is_amphi = None
            try:
                cs_str = f"{float(M.chern_simons()):.6f}"
            except Exception:
                cs_str = "unavailable"
        else:
            is_amphi = False  # 3_1, 5_1, 7_1, 8_19 are all chiral torus knots!
            cs_str = "non_hyperbolic"

        dp_counts = {}
        d5_lon_triv = None
        for p in (3, 5, 7, 11, 13):
            res_p = count_knot_Dp_surjections(len(gens), rels, ab_w, lon_word, groups_Dp[p])
            dp_counts[str(p)] = res_p["classes"]
            if p == 5:
                d5_lon_triv = res_p["longitude_all_trivial"]
            # For every knot, pi_1 ->> D_p exists iff p | det_val (since H_1(Sigma_2(K)) has order det_val!)
            if (res_p["classes"] > 0) != (det_val % p == 0):
                det_div_mismatches += 1

        c_2T = count_knot_2T_surjections(len(gens), rels, ab_w, G_2T)
        c_A5 = count_knot_A5_surjections(len(gens), rels, G_A5)

        results.append({
            "knot": name,
            "num_gens": len(gens),
            "det": det_val,
            "snf_inv_factors": inv_facs,
            "is_hyperbolic": is_hyp,
            "volume": f"{vol_f:.6f}",
            "is_amphichiral": is_amphi,
            "chern_simons": cs_str,
            "D_p_classes": dp_counts,
            "D5_longitude_all_trivial": d5_lon_triv,
            "2T_classes": c_2T,
            "A5_classes": c_A5,
        })

    knots_D5 = [r["knot"] for r in results if r["D_p_classes"]["5"] > 0]
    knots_D5_triv_lon = [
        r["knot"] for r in results if r["D_p_classes"]["5"] > 0 and r["D5_longitude_all_trivial"] is True
    ]
    knots_2T = [r["knot"] for r in results if r["2T_classes"] > 0]
    knots_both_D5_2T = [
        r["knot"] for r in results if r["D_p_classes"]["5"] > 0 and r["2T_classes"] > 0
    ]
    knots_chiral_hyp_D5 = [
        r["knot"]
        for r in results
        if r["D_p_classes"]["5"] > 0
        and r["D5_longitude_all_trivial"] is True
        and r["is_hyperbolic"]
        and r["is_amphichiral"] is False
    ]
    knots_chiral_hyp_D5_2T = [
        r["knot"]
        for r in results
        if r["D_p_classes"]["5"] > 0
        and r["D5_longitude_all_trivial"] is True
        and r["2T_classes"] > 0
        and r["is_hyperbolic"]
        and r["is_amphichiral"] is False
    ]
    knots_A5 = [r["knot"] for r in results if r["A5_classes"] > 0]

    return {
        "total_knots_tested": len(results),
        "det_vs_Dp_divisibility_mismatches": det_div_mismatches,
        "knots_with_D5": knots_D5,
        "knots_with_D5_trivial_longitude": knots_D5_triv_lon,
        "knots_with_2T": knots_2T,
        "knots_with_both_D5_and_2T": knots_both_D5_2T,
        "chiral_hyperbolic_knots_passing_D5_triv_lon": knots_chiral_hyp_D5,
        "chiral_hyperbolic_knots_passing_both_D5_and_2T": knots_chiral_hyp_D5_2T,
        "knots_with_A5": knots_A5,
        "knots": results,
        "pass": (len(results) == 35 and det_div_mismatches == 0),
    }


# ---------------------------------------------------------------------------
# Task OW1-D: Four Planted Faults
# ---------------------------------------------------------------------------

def run_task_ow1_d():
    pf1 = analyze_involution_gauge_matter(2, 1)  # S_3, d=3 -> Tr(Y^3) != 0
    pf2 = analyze_involution_gauge_matter(2, 2)  # A_4, d=4 -> vector-like, dim 7 != 12
    pf3 = analyze_involution_gauge_matter(4, 1)  # S_5 \ A_5 transposition -> dim 16 != 12
    pf4 = analyze_involution_gauge_matter(4, 3)  # D_7 -> dim 24 != 12

    caught_1 = (not pf1["all_anomalies_zero"]) and (pf1["tr_Y3"] != 0) and (not pf1["is_sm_exact"])
    caught_2 = (not pf2["is_chiral"]) and (pf2["centralizer_dim"] == 7) and (not pf2["is_sm_exact"])
    caught_3 = (pf3["centralizer_dim"] == 16) and (not pf3["is_sm_exact"])
    caught_4 = (pf4["centralizer_dim"] == 24) and (not pf4["is_sm_exact"])

    return {
        "PF_OW1_1_rung_N2_S3": {"caught": caught_1, "tr_Y3": pf1["tr_Y3"], "dim": pf1["centralizer_dim"]},
        "PF_OW1_2_rung_N3_A4": {"caught": caught_2, "is_chiral": pf2["is_chiral"], "dim": pf2["centralizer_dim"]},
        "PF_OW1_3_odd_S5_transp": {"caught": caught_3, "dim": pf3["centralizer_dim"], "tr_Y3": pf3["tr_Y3"]},
        "PF_OW1_4_higher_D7": {"caught": caught_4, "dim": pf4["centralizer_dim"], "fock_even_dim": pf4["fock_even_dim"]},
        "all_4_planted_faults_caught": bool(caught_1 and caught_2 and caught_3 and caught_4),
        "pass": bool(caught_1 and caught_2 and caught_3 and caught_4),
    }


def main():
    script_path = pathlib.Path(__file__).resolve()
    script_sha = hashlib.sha256(script_path.read_bytes()).hexdigest()

    groups_Dp = {p: build_group_Dp(p) for p in (3, 5, 7, 11, 13)}
    G_2T = build_group_2T()
    G_A5 = build_group_A5()
    conj_map = {f"D_{p}": precompute_conjugators(groups_Dp[p]) for p in (3, 5, 7, 11, 13)}
    conj_map["2T"] = precompute_conjugators(G_2T)
    conj_map["A5"] = precompute_conjugators(G_A5)

    res_a = run_task_ow1_a()
    res_b = run_task_ow1_b(groups_Dp, G_2T, G_A5, conj_map)
    res_c = run_task_ow1_c(groups_Dp, G_2T, G_A5)
    res_d = run_task_ow1_d()

    all_passed = bool(res_a["pass"] and res_b["pass"] and res_c["pass"] and res_d["pass"])
    out = {
        "card": "A2-OW1",
        "empirical_inputs_used": "0 of 19",
        "script_sha256": script_sha,
        "OW1_A_open_weave_ladder": res_a,
        "OW1_B_unblocked_bundle_census": res_b,
        "OW1_C_unblocked_prime_knot_census_le_8": res_c,
        "OW1_D_planted_faults": res_d,
        "all_gates_passed": all_passed,
    }

    out_path = script_path.parent / "verify_a2_ow1_out.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n")
    print("WROTE:", out_path)
    print("ALL_GATES_PASSED:", all_passed)


if __name__ == "__main__":
    main()
