#!/usr/bin/env python3
"""
Independent Cold-Room Zero-Trust Referee for Card A2-WHOLE-CENSUS-E8-TWO-REGISTER.

Discipline:
  - Strictly blind: 0 of 19 empirical inputs, Rule D5 clean.
  - Zero shared code with Producer: never imports or calls any Producer function.
  - Zero AST floats and zero JSON floats (self-audited).
  - Independent algebraic constructions:
      * F_25 built via 2x2 companion matrices over F_5 for t^2 - 3 = 0 (NOT d^2 - 2).
      * BD_5 built via explicit 2x2 matrices in SL(2, F_11) (order 20), D_5 = BD_5 / {+-I}.
      * 248 = 120 + 128 E_8 peripheral weights explicitly enumerated in (Z/20Z)^2.
      * 30-matrix adversarial SL(2, Z) peripheral basis-scrambling (det = +1, |entry| <= 10).
      * SL(2, F_25) Fricke search in independent B-gauge B = [[3y+1, 1], [4y^2-2, 3y-1]]
        plus explicit BFS subgroup-order verification (> 240, and exact 15,600 on benchmarks).
      * Gluing equation solver over F_25 \\ {0, 1} via algebraic row-reduction + direct
        constraint-propagating backtracking/substitution (NO discrete log / NO MITM).
      * Independent 2T = SL(2, F_3) surjection enumeration & Aut(2T) orbit verification.
      * Live SnapPy 3.3.2 census cross-check & pure-topology M.identify() inspection.
      * Producer SHA256 verification, standalone exit-1 control check under python3 -I,
        and 5 independent Referee Planted Fault Controls (RPF1..RPF5).
"""

import ast
import hashlib
import json
import os
import subprocess
import sys
import time
import warnings

warnings.filterwarnings("ignore", category=UserWarning)
import snappy  # noqa: E402


REPO_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..")
)
PRODUCER_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REFEREE_DIR = os.path.abspath(os.path.dirname(__file__))

CENSUS_DATA_PATH = os.path.join(
    PRODUCER_DIR, "a2_census_1200_presentations_and_gluing.json"
)
PRODUCER_OUT_PATH = os.path.join(PRODUCER_DIR, "a2_whole_census_e8_out.json")
PRODUCER_CONTROL_PATH = os.path.join(
    PRODUCER_DIR, "a2_whole_census_e8_control.py"
)
REFEREE_OUT_PATH = os.path.join(
    REFEREE_DIR, "referee_whole_census_e8_out.json"
)


# =============================================================================
# 1. INDEPENDENT FINITE FIELD F_25 = F_5[t] / (t^2 - 3) VIA 2x2 COMPANION MATRICES
# =============================================================================
# Element idx = a + 5*b corresponds to companion matrix [[a, 3*b], [b, a]] mod 5.
# Thus F_5 = {0, 1, 2, 3, 4} with 0=0, 1=1, 2=+2, 3=-2, 4=-1 mod 5.

def _build_f25_companion():
    mats = []
    mat_to_idx = {}
    for b in range(5):
        for a in range(5):
            idx = a + 5 * b
            m = (a, (3 * b) % 5, b, a)
            mats.append((idx, m))
            mat_to_idx[m] = idx
    mats.sort(key=lambda pair: pair[0])
    mat_list = [m for _, m in mats]

    add_tbl = [[0] * 25 for _ in range(25)]
    sub_tbl = [[0] * 25 for _ in range(25)]
    mul_tbl = [[0] * 25 for _ in range(25)]
    neg_tbl = [0] * 25
    inv_tbl = [0] * 25
    tr_f5 = [0] * 25
    frob_tbl = [0] * 25
    sqrt_tbl = [-1] * 25

    for i in range(25):
        a0, a1, a2, a3 = mat_list[i]
        tr_f5[i] = (a0 + a3) % 5
        neg_m = ((-a0) % 5, (-a1) % 5, (-a2) % 5, (-a3) % 5)
        neg_tbl[i] = mat_to_idx[neg_m]
        for j in range(25):
            b0, b1, b2, b3 = mat_list[j]
            add_m = (
                (a0 + b0) % 5,
                (a1 + b1) % 5,
                (a2 + b2) % 5,
                (a3 + b3) % 5,
            )
            sub_m = (
                (a0 - b0) % 5,
                (a1 - b1) % 5,
                (a2 - b2) % 5,
                (a3 - b3) % 5,
            )
            mul_m = (
                (a0 * b0 + a1 * b2) % 5,
                (a0 * b1 + a1 * b3) % 5,
                (a2 * b0 + a3 * b2) % 5,
                (a2 * b1 + a3 * b3) % 5,
            )
            add_tbl[i][j] = mat_to_idx[add_m]
            sub_tbl[i][j] = mat_to_idx[sub_m]
            mul_tbl[i][j] = mat_to_idx[mul_m]

    # Verify companion polynomial t^2 = 3 (idx 5 is t = 0 + 1*t)
    assert mul_tbl[5][5] == 3
    for i in range(1, 25):
        found = 0
        for j in range(1, 25):
            if mul_tbl[i][j] == 1:
                inv_tbl[i] = j
                found += 1
        assert found == 1

    # Frobenius u -> u^5 and square roots directly from multiplication table
    for i in range(25):
        sq = mul_tbl[i][i]
        if sqrt_tbl[sq] == -1:
            sqrt_tbl[sq] = i
        p = i
        p = mul_tbl[p][p]  # u^2
        p = mul_tbl[p][p]  # u^4
        p = mul_tbl[p][i]  # u^5
        frob_tbl[i] = p
        # Check u^25 == u
        p2 = p
        p2 = mul_tbl[p2][p2]
        p2 = mul_tbl[p2][p2]
        p2 = mul_tbl[p2][p]
        assert p2 == i

    return add_tbl, sub_tbl, mul_tbl, neg_tbl, inv_tbl, tr_f5, frob_tbl, sqrt_tbl


ADD, SUB, MUL, NEG, INV, TR_F5, FROB, SQRT = _build_f25_companion()


def f25_pow(u, e):
    if e == 0:
        return 1
    if e < 0:
        u = INV[u]
        e = -e
    res = 1
    base = u
    while e > 0:
        if e & 1:
            res = MUL[res][base]
        base = MUL[base][base]
        e >>= 1
    return res


def sl2_f25_mul(m1, m2):
    a0, a1, a2, a3 = m1
    b0, b1, b2, b3 = m2
    return (
        ADD[MUL[a0][b0]][MUL[a1][b2]],
        ADD[MUL[a0][b1]][MUL[a1][b3]],
        ADD[MUL[a2][b0]][MUL[a3][b2]],
        ADD[MUL[a2][b1]][MUL[a3][b3]],
    )


def sl2_f25_inv(m):
    return (m[3], NEG[m[1]], NEG[m[2]], m[0])


def sl2_f25_det(m):
    return SUB[MUL[m[0]][m[3]]][MUL[m[1]][m[2]]]


def sl2_f25_pow(m, e):
    if e == 0:
        return (1, 0, 0, 1)
    if e < 0:
        m = sl2_f25_inv(m)
        e = -e
    res = (1, 0, 0, 1)
    base = m
    while e > 0:
        if e & 1:
            res = sl2_f25_mul(res, base)
        base = sl2_f25_mul(base, base)
        e >>= 1
    return res


# =============================================================================
# 2. INDEPENDENT BD_5 IN SL(2, F_11) (ORDER 20) AND D_5 = BD_5 / {+-I} (ORDER 10)
# =============================================================================

def _sl2_f11_mul(m1, m2):
    return (
        (m1[0] * m2[0] + m1[1] * m2[2]) % 11,
        (m1[0] * m2[1] + m1[1] * m2[3]) % 11,
        (m1[2] * m2[0] + m1[3] * m2[2]) % 11,
        (m1[2] * m2[1] + m1[3] * m2[3]) % 11,
    )


def _sl2_f11_inv(m):
    return (m[3], (-m[1]) % 11, (-m[2]) % 11, m[0])


def _sl2_f11_neg(m):
    return ((-m[0]) % 11, (-m[1]) % 11, (-m[2]) % 11, (-m[3]) % 11)


def _build_bd5_and_d5():
    ident = (1, 0, 0, 1)
    neg_ident = (10, 0, 0, 10)
    r_mat = (4, 0, 0, 3)    # 4^5 = 1024 = 1 mod 11, det = 12 = 1 mod 11
    j_mat = (0, 10, 1, 0)   # J^2 = -I, J R J^-1 = R^-1

    # Verify defining relations directly from matrices
    r5 = ident
    for _ in range(5):
        r5 = _sl2_f11_mul(r5, r_mat)
    assert r5 == ident
    assert _sl2_f11_mul(j_mat, j_mat) == neg_ident
    assert _sl2_f11_mul(_sl2_f11_mul(j_mat, r_mat), _sl2_f11_inv(j_mat)) == _sl2_f11_inv(r_mat)

    # Generate BD_5 by BFS closure
    seen = {ident}
    queue = [ident]
    gens = [r_mat, j_mat, _sl2_f11_inv(r_mat), _sl2_f11_inv(j_mat)]
    while queue:
        u = queue.pop()
        for g in gens:
            v = _sl2_f11_mul(u, g)
            if v not in seen:
                seen.add(v)
                queue.append(v)
    bd5_mats = sorted(seen)
    assert len(bd5_mats) == 20
    # Put identity at index 0
    bd5_mats.remove(ident)
    bd5_mats.insert(0, ident)
    bd5_idx = {m: i for i, m in enumerate(bd5_mats)}

    bd5_mul = [[0] * 20 for _ in range(20)]
    bd5_inv = [0] * 20
    bd5_neg = [0] * 20
    bd5_ord = [0] * 20
    for i, m1 in enumerate(bd5_mats):
        bd5_inv[i] = bd5_idx[_sl2_f11_inv(m1)]
        bd5_neg[i] = bd5_idx[_sl2_f11_neg(m1)]
        cur = m1
        o = 1
        while cur != ident:
            cur = _sl2_f11_mul(cur, m1)
            o += 1
        bd5_ord[i] = o
        for j, m2 in enumerate(bd5_mats):
            bd5_mul[i][j] = bd5_idx[_sl2_f11_mul(m1, m2)]

    # Build quotient D_5 = BD_5 / {+-I}
    d5_reps = []
    bd5_to_d5 = [0] * 20
    d5_lifts = []
    seen_coset = set()
    for i in range(20):
        c = min(i, bd5_neg[i])
        if c not in seen_coset:
            seen_coset.add(c)
            d5_id = len(d5_reps)
            d5_reps.append(c)
            d5_lifts.append((c, bd5_neg[c]))
        bd5_to_d5[i] = d5_reps.index(c)
    assert len(d5_reps) == 10

    d5_mul = [[0] * 10 for _ in range(10)]
    d5_inv = [0] * 10
    for i in range(10):
        ri = d5_reps[i]
        d5_inv[i] = bd5_to_d5[bd5_inv[ri]]
        for j in range(10):
            rj = d5_reps[j]
            d5_mul[i][j] = bd5_to_d5[bd5_mul[ri][rj]]

    # Precompute subgroup order for 2-element sets in BD_5 and D_5
    def closure_size(mul_t, inv_t, elements):
        s = {0}
        q = [0]
        gs = []
        for x in elements:
            gs.append(x)
            gs.append(inv_t[x])
        while q:
            u = q.pop()
            for g in gs:
                v = mul_t[u][g]
                if v not in s:
                    s.add(v)
                    q.append(v)
        return len(s)

    d5_surj2 = [[closure_size(d5_mul, d5_inv, (i, j)) == 10 for j in range(10)] for i in range(10)]
    bd5_surj2 = [[closure_size(bd5_mul, bd5_inv, (i, j)) == 20 for j in range(20)] for i in range(20)]

    # Discrete log map in Z/20Z for diagonal entries (+-4^m mod 11)
    f11_diag_log20 = {}
    val_r = 1
    for m in range(5):
        f11_diag_log20[val_r] = (4 * m) % 20
        f11_diag_log20[(-val_r) % 11] = (10 + 4 * m) % 20
        val_r = (val_r * 4) % 11
    assert len(f11_diag_log20) == 10

    return {
        "mats": bd5_mats,
        "idx": bd5_idx,
        "mul": bd5_mul,
        "inv": bd5_inv,
        "neg": bd5_neg,
        "ord": bd5_ord,
        "surj2": bd5_surj2,
        "to_d5": bd5_to_d5,
        "d5_lifts": d5_lifts,
        "d5_mul": d5_mul,
        "d5_inv": d5_inv,
        "d5_surj2": d5_surj2,
        "f11_diag_log20": f11_diag_log20,
        "closure_size": closure_size,
        "r_idx": bd5_idx[r_mat],
        "j_idx": bd5_idx[j_mat],
        "neg_id_idx": bd5_idx[neg_ident],
    }


BD5 = _build_bd5_and_d5()


def bd5_pow(g_idx, e):
    if e == 0:
        return 0
    if e < 0:
        g_idx = BD5["inv"][g_idx]
        e = -e
    res = 0
    base = g_idx
    mul = BD5["mul"]
    while e > 0:
        if e & 1:
            res = mul[res][base]
        base = mul[base][base]
        e >>= 1
    return res


def bd5_commuting_eigenphases(h1_idx, h2_idx):
    """
    Directly extract simultaneous eigenphases in (Z/20Z)^2 on the 2-dim Spin(3)
    representation and 3-dim SO(3) = Sym^2(2) representation for a commuting pair
    (H1, H2) in BD_5 <= SL(2, F_11).
    """
    assert BD5["mul"][h1_idx][h2_idx] == BD5["mul"][h2_idx][h1_idx]
    m1 = BD5["mats"][h1_idx]
    m2 = BD5["mats"][h2_idx]

    # Compute exact subgroup H_per = <h1, h2>
    sub_size = BD5["closure_size"](BD5["mul"], BD5["inv"], (h1_idx, h2_idx))
    hper_label = "C" + str(sub_size)

    # Case 1: both matrices diagonal (H_per <= C_10)
    if m1[1] == 0 and m1[2] == 0 and m2[1] == 0 and m2[2] == 0:
        dlog = BD5["f11_diag_log20"]
        p0 = (dlog[m1[0]], dlog[m2[0]])
        p1 = (dlog[m1[3]], dlog[m2[3]])
        phases_2 = [p0, p1]
    else:
        # Case 2: H_per = C_4 generated by an order-4 element g
        assert sub_size == 4
        g = h1_idx if BD5["ord"][h1_idx] == 4 else h2_idx
        assert BD5["ord"][g] == 4
        # Find exact exponents k1, k2 in {0, 1, 2, 3} with h_i = g^{k_i}
        pows = [0, g, BD5["mul"][g][g], BD5["mul"][BD5["mul"][g][g]][g]]
        k1 = pows.index(h1_idx)
        k2 = pows.index(h2_idx)
        # Eigenvalues of order-4 element g in SU(2) are +i, -i => phases 5, 15 mod 20
        phases_2 = [
            ((5 * k1) % 20, (5 * k2) % 20),
            ((15 * k1) % 20, (15 * k2) % 20),
        ]

    # Sym^2(2) = 3 of SO(3) has weights 2*w0, w0+w1, 2*w1
    w0, w1 = phases_2[0], phases_2[1]
    phases_3 = [
        ((2 * w0[0]) % 20, (2 * w0[1]) % 20),
        ((w0[0] + w1[0]) % 20, (w0[1] + w1[1]) % 20),
        ((2 * w1[0]) % 20, (2 * w1[1]) % 20),
    ]
    return hper_label, phases_2, phases_3


# =============================================================================
# 3. EXPLICIT 248 = 120 + 128 E_8 WEIGHT ENUMERATOR IN (Z/20Z)^2
# =============================================================================

def _square_pairs_f25():
    squares = sorted({MUL[u][u] for u in range(1, 25)})
    assert len(squares) == 12
    reps = []
    seen = set()
    for s in squares:
        if s not in seen:
            reps.append(s)
            seen.add(s)
            seen.add(NEG[s])
    assert len(reps) == 6
    return reps


SQ_REPS_6 = _square_pairs_f25()


def evaluate_e8_248_kernels(v1, v2, alpha_z, h1_idx, h2_idx):
    """
    Explicitly enumerate ALL 248 = 120 + 128 weights of E_8 (via Spin(13) x Spin(3) -> Ss(16))
    in exact (Z/20Z)^2 phase arithmetic, returning exact kernel dimensions on all 4 torus
    spin structures sp in {(0,0), (1,0), (0,1), (1,1)}.
    """
    _, phases_2, phases_3 = bd5_commuting_eigenphases(h1_idx, h2_idx)
    a1, a2 = alpha_z  # each in {0, 1}, representing central sign (-1)^a_i

    # 6 orthogonal rotation planes of SO(13) from the 6 nonzero square pairs {+-s_k}
    angles_f5 = [
        (TR_F5[MUL[v1][sk]], TR_F5[MUL[v2][sk]]) for sk in SQ_REPS_6
    ]

    # 13 weights of SO(13) vector representation in (Z/20Z)^2
    w13 = [(0, 0)]
    for t1, t2 in angles_f5:
        p1 = (4 * t1) % 20
        p2 = (4 * t2) % 20
        w13.append((p1, p2))
        w13.append(((-p1) % 20, (-p2) % 20))
    assert len(w13) == 13

    # 120 = (78, 1) + (13, 3) + (1, 3)
    w120 = []
    # (78, 1) = Lambda^2(13)
    for i in range(13):
        x1, y1 = w13[i]
        for j in range(i + 1, 13):
            x2, y2 = w13[j]
            w120.append(((x1 + x2) % 20, (y1 + y2) % 20))
    # (13, 3)
    for x1, y1 in w13:
        for x2, y2 in phases_3:
            w120.append(((x1 + x2) % 20, (y1 + y2) % 20))
    # (1, 3)
    for x2, y2 in phases_3:
        w120.append((x2 % 20, y2 % 20))
    assert len(w120) == 120

    # 64 weights of Spin(13) spinor in (Z/20Z)^2:
    # Unique order-5 lift of 4*t_k mod 20 has half-angle 12*t_k mod 20 (since 2*12=24=4 mod 20, 5*12=0 mod 20)
    half_angles = [((12 * t1) % 20, (12 * t2) % 20) for t1, t2 in angles_f5]
    w64 = []
    for mask in range(64):
        s1 = (10 * a1) % 20
        s2 = (10 * a2) % 20
        for k in range(6):
            h1k, h2k = half_angles[k]
            if (mask >> k) & 1:
                s1 = (s1 + h1k) % 20
                s2 = (s2 + h2k) % 20
            else:
                s1 = (s1 - h1k) % 20
                s2 = (s2 - h2k) % 20
        w64.append((s1, s2))
    assert len(w64) == 64

    # 128 = (64, 2)
    w128 = []
    for x1, y1 in w64:
        for x2, y2 in phases_2:
            w128.append(((x1 + x2) % 20, (y1 + y2) % 20))
    assert len(w128) == 128
    assert len(w120) + len(w128) == 248

    k120_by_sp = {}
    k128_by_sp = {}
    k248_by_sp = {}
    for sp1 in (0, 1):
        for sp2 in (0, 1):
            target = (10 * sp1, 10 * sp2)
            c120 = sum(1 for w in w120 if w == target)
            c128 = sum(1 for w in w128 if w == target)
            k120_by_sp[(sp1, sp2)] = c120
            k128_by_sp[(sp1, sp2)] = c128
            k248_by_sp[(sp1, sp2)] = c120 + c128

    return k120_by_sp, k128_by_sp, k248_by_sp


# =============================================================================
# 4. Q1 — UNIVERSAL E_8 PERIPHERAL KERNEL THEOREM + 30-MATRIX SL(2, Z) SCRAMBLING
# =============================================================================

def run_q1_universal_theorem():
    # (a) Check ALL 480 ordered F_5-bases of F_25 give {2: 12, 3: 12, 4: 1}
    bases = []
    for v1 in range(1, 25):
        inv_v1 = INV[v1]
        for v2 in range(1, 25):
            if MUL[v2][inv_v1] >= 5:  # v2 / v1 not in F_5
                bases.append((v1, v2))
    assert len(bases) == 480

    all_hist_ok = True
    for v1, v2 in bases:
        half_f5 = [
            ((3 * TR_F5[MUL[v1][sk]]) % 5, (3 * TR_F5[MUL[v2][sk]]) % 5)
            for sk in SQ_REPS_6
        ]
        counts = {}
        for mask in range(64):
            s1 = 0
            s2 = 0
            for k in range(6):
                h1k, h2k = half_f5[k]
                if (mask >> k) & 1:
                    s1 = (s1 + h1k) % 5
                    s2 = (s2 + h2k) % 5
                else:
                    s1 = (s1 - h1k) % 5
                    s2 = (s2 - h2k) % 5
            pt = (s1, s2)
            counts[pt] = counts.get(pt, 0) + 1
        hist = {}
        for mult in counts.values():
            hist[mult] = hist.get(mult, 0) + 1
        if len(counts) != 25 or counts.get((0, 0), 0) != 4 or hist != {2: 12, 3: 12, 4: 1}:
            all_hist_ok = False
            break

    # (b) Enumerate ALL commuting pairs in BD_5 x 3 non-trivial central signs
    comm_pairs = []
    for i in range(20):
        for j in range(20):
            if BD5["mul"][i][j] == BD5["mul"][j][i]:
                comm_pairs.append((i, j))
    assert len(comm_pairs) == 160

    nontrivial_alphas = [(1, 0), (0, 1), (1, 1)]
    k128_by_hper = {}
    k248_alpha_by_hper = {}
    c4_iff_k128_zero = True
    c4_ne_gives_0 = True
    c4_eq_gives_4 = True
    c4_c0_antiperiodic_ok = True

    # Test on canonical F_5-basis (1, t) = (1, 5) across ALL 160 * 3 = 480 cases
    v1_ref, v2_ref = 1, 5
    for h1, h2 in comm_pairs:
        hper, _, _ = bd5_commuting_eigenphases(h1, h2)
        for alpha_z in nontrivial_alphas:
            k120_sp, k128_sp, k248_sp = evaluate_e8_248_kernels(
                v1_ref, v2_ref, alpha_z, h1, h2
            )
            k128_tot = sum(k128_sp.values())
            k248_az = k248_sp[alpha_z]
            k128_by_hper.setdefault(hper, set()).add(k128_tot)
            k248_alpha_by_hper.setdefault(hper, set()).add(k248_az)

            if (hper == "C4") != (k128_tot == 0):
                c4_iff_k128_zero = False
            if hper == "C4":
                beta_j = (
                    1 if BD5["ord"][h1] == 4 else 0,
                    1 if BD5["ord"][h2] == 4 else 0,
                )
                assert beta_j != (0, 0)
                # Unique primitive j-trivial slope c0 = ker(beta_j) in (Z/2Z)^2
                if beta_j == (1, 0):
                    c0 = (0, 1)
                elif beta_j == (0, 1):
                    c0 = (1, 0)
                else:
                    c0 = (1, 1)
                antiper_sps = [
                    sp for sp in ((0, 0), (1, 0), (0, 1), (1, 1))
                    if (sp[0] * c0[0] + sp[1] * c0[1]) % 2 == 1
                ]
                assert len(antiper_sps) == 2
                if any(k248_sp[sp] != 0 for sp in antiper_sps):
                    c4_c0_antiperiodic_ok = False
                if alpha_z != beta_j:
                    if k248_az != 0:
                        c4_ne_gives_0 = False
                else:
                    if k248_az != 4 or k120_sp[alpha_z] != 4:
                        c4_eq_gives_4 = False

    # (c) Degenerate 1D F_5 control case: all (v1, v2) in F_5^2 \ {(0,0)}
    deg_geo_vals = set()
    deg_c4_vals = set()
    for v1 in range(5):
        for v2 in range(5):
            if v1 == 0 and v2 == 0:
                continue
            _, k128_g, _ = evaluate_e8_248_kernels(v1, v2, (0, 1), 0, 0)
            _, k128_c, _ = evaluate_e8_248_kernels(v1, v2, (0, 1), BD5["j_idx"], 0)
            deg_geo_vals.add(sum(k128_g.values()))
            deg_c4_vals.add(sum(k128_c.values()))
    assert deg_geo_vals == {24}
    assert deg_c4_vals == {0}

    # (d) Adversarial 30-matrix deterministic pseudo-random SL(2, Z) basis-scrambling
    #     det = +1, entries up to +-10, testing explicit matrix powers in SL(2, F_25) & BD_5
    sl2z_mats = []
    seen_u = set()
    state = 20261128
    while len(sl2z_mats) < 30:
        # Build unimodular matrix from 3..5 elementary shear factors with |entry| <= 10
        p, q, r, s = 1, 0, 0, 1
        steps = 3 + (state % 4)
        for _ in range(steps):
            state = (1103515245 * state + 12345) & 0x7FFFFFFF
            k = (state % 5) - 2
            if k == 0:
                k = 1
            if (state >> 4) & 1:
                # Left multiply by [[1, k], [0, 1]]
                np, nq, nr, ns = p + k * r, q + k * s, r, s
            else:
                # Left multiply by [[1, 0], [k, 1]]
                np, nq, nr, ns = p, q, r + k * p, s + k * q
            if max(abs(np), abs(nq), abs(nr), abs(ns)) <= 10:
                p, q, r, s = np, nq, nr, ns
        u = (p, q, r, s)
        assert p * s - q * r == 1
        if u not in seen_u and u != (1, 0, 0, 1) and max(abs(p), abs(q), abs(r), abs(s)) >= 2:
            seen_u.add(u)
            sl2z_mats.append(u)

    max_entry_used = max(max(abs(x) for x in u) for u in sl2z_mats)
    assert max_entry_used <= 10 and max_entry_used >= 5

    # Test invariance across 6 distinct peripheral configurations (C4 unlocked, C4 locked/obstructed, C5, C10, C2, C1)
    test_configs = [
        (1, 5, (0, 1), BD5["j_idx"], 0),                    # C4, alpha != beta -> k248=0
        (1, 5, (1, 0), BD5["j_idx"], 0),                    # C4, alpha == beta -> k248=4
        (2, 11, (1, 1), BD5["j_idx"], BD5["j_idx"]),        # C4, (4,4) alpha == beta
        (2, 11, (0, 1), BD5["j_idx"], BD5["j_idx"]),        # C4, (4,4) alpha != beta
        (1, 5, (0, 1), BD5["r_idx"], 0),                    # C5
        (1, 5, (1, 0), BD5["neg_id_idx"], BD5["r_idx"]),    # C10
    ]
    sl2z_all_ok = True
    for v1, v2, az, h1, h2 in test_configs:
        _, k128_ref, k248_ref = evaluate_e8_248_kernels(v1, v2, az, h1, h2)
        ref_k128_tot = sum(k128_ref.values())
        ref_k248_az = k248_ref[az]
        ref_multiset = sorted(k248_ref.values())

        # Explicit 2x2 parabolic matrices M, L in SL(2, F_25)
        s1 = 1 if az[0] == 0 else 4
        s2 = 1 if az[1] == 0 else 4
        m_mat = (s1, MUL[s1][v1], 0, s1)
        l_mat = (s2, MUL[s2][v2], 0, s2)

        for p, q, r, s in sl2z_mats:
            m_new = sl2_f25_mul(sl2_f25_pow(m_mat, p), sl2_f25_pow(l_mat, q))
            l_new = sl2_f25_mul(sl2_f25_pow(m_mat, r), sl2_f25_pow(l_mat, s))
            assert m_new[2] == 0 and l_new[2] == 0
            s1_n = m_new[0]
            s2_n = l_new[0]
            assert s1_n in (1, 4) and s2_n in (1, 4)
            v1_n = MUL[s1_n][m_new[1]]
            v2_n = MUL[s2_n][l_new[1]]
            az_n = (0 if s1_n == 1 else 1, 0 if s2_n == 1 else 1)

            h1_n = BD5["mul"][bd5_pow(h1, p)][bd5_pow(h2, q)]
            h2_n = BD5["mul"][bd5_pow(h1, r)][bd5_pow(h2, s)]

            _, k128_n, k248_n = evaluate_e8_248_kernels(v1_n, v2_n, az_n, h1_n, h2_n)
            if (
                sum(k128_n.values()) != ref_k128_tot
                or k248_n[az_n] != ref_k248_az
                or sorted(k248_n.values()) != ref_multiset
            ):
                sl2z_all_ok = False
                break

    return {
        "field_model": "F_5[t]/(t^2 - 3) via 2x2 companion matrices",
        "bd5_model": "explicit 2x2 matrices in SL(2, F_11)",
        "bases_checked": len(bases),
        "bases_w64_hist_4_3_2_all_ok": all_hist_ok,
        "commuting_pairs_in_BD5": len(comm_pairs),
        "k128_total_by_Hper": {k: sorted(v) for k, v in sorted(k128_by_hper.items())},
        "k248_at_alpha_Z_by_Hper": {k: sorted(v) for k, v in sorted(k248_alpha_by_hper.items())},
        "c4_iff_k128_zero": c4_iff_k128_zero,
        "c4_alpha_ne_beta_gives_k248_zero": c4_ne_gives_0,
        "c4_alpha_eq_beta_gives_k248_4": c4_eq_gives_4,
        "c4_c0_antiperiodic_vanishing_ok": c4_c0_antiperiodic_ok,
        "degenerate_1D_F5_geo_k128": 24,
        "degenerate_1D_F5_C4_k128": 0,
        "sl2z_30_matrix_basis_scrambling_ok": sl2z_all_ok,
        "sl2z_matrices_tested": len(sl2z_mats),
        "sl2z_max_abs_entry": max_entry_used,
        "ok": (
            all_hist_ok
            and c4_iff_k128_zero
            and c4_ne_gives_0
            and c4_eq_gives_4
            and c4_c0_antiperiodic_ok
            and sl2z_all_ok
        ),
    }


# =============================================================================
# 5. Q2 — EXHAUSTIVE 1,199 + m000 D_5 / BD_5 / H_per CENSUS
# =============================================================================

def _compile_word_indices(word, gens):
    """Compile word over gens (e.g. ['a','b'] or ['a','b','c']) to tuple of ints 0..2k-1."""
    cmap = {}
    for idx, g in enumerate(gens):
        cmap[g] = 2 * idx
        cmap[g.upper()] = 2 * idx + 1
    return tuple(cmap[ch] for ch in word)


def _eval_group_word(mul_t, w_code, g_and_invs):
    cur = 0
    for c in w_code:
        cur = mul_t[cur][g_and_invs[c]]
    return cur


def analyze_d5_bd5_manifold(m_rec):
    gens = m_rec["gens"]
    k = len(gens)
    rels_c = [_compile_word_indices(r, gens) for r in m_rec["rels"]]
    pm_c = _compile_word_indices(m_rec["periph"][0], gens)
    pl_c = _compile_word_indices(m_rec["periph"][1], gens)

    d5_mul = BD5["d5_mul"]
    d5_inv = BD5["d5_inv"]
    bd5_mul = BD5["mul"]
    bd5_inv = BD5["inv"]
    bd5_ord = BD5["ord"]
    d5_surj2 = BD5["d5_surj2"]
    bd5_surj2 = BD5["surj2"]
    d5_lifts = BD5["d5_lifts"]
    closure_size = BD5["closure_size"]

    d5_surj = 0
    bd5_surj = 0
    hper_types = set()
    c4_ord_pairs = set()
    c4_betas = set()
    c4_sample_by_beta = {}  # beta_j -> (h_m, h_l) for concrete 248-weight test

    if k == 2:
        # Direct exhaustive D_5 over all 10^2 = 100 pairs
        for ga in range(10):
            ga_i = d5_inv[ga]
            row_s = d5_surj2[ga]
            for gb in range(10):
                if not row_s[gb]:
                    continue
                gi = (ga, ga_i, gb, d5_inv[gb])
                ok = True
                for rc in rels_c:
                    if _eval_group_word(d5_mul, rc, gi) != 0:
                        ok = False
                        break
                if ok:
                    d5_surj += 1

        # Direct exhaustive BD_5 over all 20^2 = 400 pairs (independent of D_5!)
        for ga in range(20):
            ga_i = bd5_inv[ga]
            row_s = bd5_surj2[ga]
            for gb in range(20):
                if not row_s[gb]:
                    continue
                gi = (ga, ga_i, gb, bd5_inv[gb])
                ok = True
                for rc in rels_c:
                    if _eval_group_word(bd5_mul, rc, gi) != 0:
                        ok = False
                        break
                if ok:
                    bd5_surj += 1
                    hm = _eval_group_word(bd5_mul, pm_c, gi)
                    hl = _eval_group_word(bd5_mul, pl_c, gi)
                    if m_rec["orientable"]:
                        assert bd5_mul[hm][hl] == bd5_mul[hl][hm]
                    sub_sz = closure_size(bd5_mul, bd5_inv, (hm, hl))
                    ht = "C" + str(sub_sz)
                    hper_types.add(ht)
                    if sub_sz == 4:
                        om = bd5_ord[hm]
                        ol = bd5_ord[hl]
                        bj = (1 if om == 4 else 0, 1 if ol == 4 else 0)
                        c4_ord_pairs.add((om, ol))
                        c4_betas.add(bj)
                        if bj not in c4_sample_by_beta:
                            c4_sample_by_beta[bj] = (hm, hl)
    elif k == 3:
        # Exhaustive D_5 over all 10^3 = 1,000 triples, then lift all 2^3 = 8 sign choices to BD_5
        # (Every surjection -> BD_5 necessarily projects to a surjection -> D_5)
        d5_hits = []
        for ga in range(10):
            ga_i = d5_inv[ga]
            for gb in range(10):
                gb_i = d5_inv[gb]
                ab_surj = d5_surj2[ga][gb]
                for gc in range(10):
                    if not (ab_surj or d5_surj2[ga][gc] or d5_surj2[gb][gc]):
                        # If no pair generates D_5, can all 3 generate D_5?
                        # Check explicitly via closure_size!
                        if closure_size(d5_mul, d5_inv, (ga, gb, gc)) != 10:
                            continue
                    gi = (ga, ga_i, gb, gb_i, gc, d5_inv[gc])
                    ok = True
                    for rc in rels_c:
                        if _eval_group_word(d5_mul, rc, gi) != 0:
                            ok = False
                            break
                    if ok:
                        d5_surj += 1
                        d5_hits.append((ga, gb, gc))

        for ga0, gb0, gc0 in d5_hits:
            for ga in d5_lifts[ga0]:
                ga_i = bd5_inv[ga]
                for gb in d5_lifts[gb0]:
                    gb_i = bd5_inv[gb]
                    for gc in d5_lifts[gc0]:
                        if closure_size(bd5_mul, bd5_inv, (ga, gb, gc)) != 20:
                            continue
                        gi = (ga, ga_i, gb, gb_i, gc, bd5_inv[gc])
                        ok = True
                        for rc in rels_c:
                            if _eval_group_word(bd5_mul, rc, gi) != 0:
                                ok = False
                                break
                        if ok:
                            bd5_surj += 1
                            hm = _eval_group_word(bd5_mul, pm_c, gi)
                            hl = _eval_group_word(bd5_mul, pl_c, gi)
                            if m_rec["orientable"]:
                                assert bd5_mul[hm][hl] == bd5_mul[hl][hm]
                            sub_sz = closure_size(bd5_mul, bd5_inv, (hm, hl))
                            ht = "C" + str(sub_sz)
                            hper_types.add(ht)
                            if sub_sz == 4:
                                om = bd5_ord[hm]
                                ol = bd5_ord[hl]
                                bj = (1 if om == 4 else 0, 1 if ol == 4 else 0)
                                c4_ord_pairs.add((om, ol))
                                c4_betas.add(bj)
                                if bj not in c4_sample_by_beta:
                                    c4_sample_by_beta[bj] = (hm, hl)
    else:
        raise ValueError("Unexpected generator count: " + str(k))

    return {
        "d5_surj": d5_surj,
        "bd5_surj": bd5_surj,
        "hper_types": sorted(hper_types),
        "c4_ord_pairs": [list(p) for p in sorted(c4_ord_pairs)],
        "c4_betas": sorted(c4_betas),
        "c4_sample_by_beta": c4_sample_by_beta,
    }


def run_q2_census(manifolds):
    per_manifold = {}
    d5_names = []
    bd5_names = []
    obstructed_names = []
    hper_buckets = {}
    s_bd5_c4_2gen = []
    s_bd5_c4_3gen = []
    bd5_all_2gen = []
    bd5_non_c4_2gen = []

    for m in manifolds:
        res = analyze_d5_bd5_manifold(m)
        nm = m["name"]
        per_manifold[nm] = res
        if not m["orientable"]:
            continue
        if res["d5_surj"] > 0:
            d5_names.append(nm)
        if res["bd5_surj"] > 0:
            bd5_names.append(nm)
            bkey = "+".join(res["hper_types"])
            hper_buckets[bkey] = hper_buckets.get(bkey, 0) + 1
            if len(m["gens"]) == 2:
                bd5_all_2gen.append(nm)
            if "C4" in res["hper_types"]:
                if len(m["gens"]) == 2:
                    s_bd5_c4_2gen.append(nm)
                else:
                    s_bd5_c4_3gen.append(nm)
            else:
                if len(m["gens"]) == 2:
                    bd5_non_c4_2gen.append(nm)
        elif res["d5_surj"] > 0:
            obstructed_names.append(nm)

    by_name = {m["name"]: m for m in manifolds}
    obs_all_even = all(
        any(t % 2 == 0 for t in by_name[nm]["h1_torsion"])
        for nm in obstructed_names
    )

    return {
        "per_manifold": per_manifold,
        "d5_surj_manifolds": len(d5_names),
        "bd5_surj_manifolds": len(bd5_names),
        "d5_to_bd5_obstructed_count": len(obstructed_names),
        "d5_to_bd5_obstructed_names": sorted(obstructed_names),
        "obstructed_all_have_even_H1_torsion": obs_all_even,
        "hper_bucket_counts": dict(sorted(hper_buckets.items())),
        "s_bd5_c4_total": len(s_bd5_c4_2gen) + len(s_bd5_c4_3gen),
        "s_bd5_c4_2gen": len(s_bd5_c4_2gen),
        "s_bd5_c4_2gen_names": sorted(s_bd5_c4_2gen),
        "s_bd5_c4_3gen": len(s_bd5_c4_3gen),
        "s_bd5_c4_3gen_names": sorted(s_bd5_c4_3gen),
        "bd5_all_2gen_names": sorted(bd5_all_2gen),
        "bd5_non_c4_2gen_names": sorted(bd5_non_c4_2gen),
    }


# =============================================================================
# 6. Q3A — DISJOINT SL(2, F_25) SEARCH IN INDEPENDENT B-GAUGE
# =============================================================================
# Independent matrix gauge (NOT A = [[0, -1], [1, x]]):
#   B = [[3y + 1, 1], [4y^2 - 2, 3y - 1]]  (det = 1, tr = y, never scalar)
#   A = [[a, b], [c, x - a]] solved via quadratic discriminant over F_5[t]/(t^2 - 3)

def _build_fricke_b_gauge_table():
    b_mats = []
    b_invs = []
    w_vals = []
    for y in range(25):
        y3 = MUL[3][y]
        b0 = ADD[y3][1]
        b1 = 1
        y2 = MUL[y][y]
        b2 = SUB[MUL[4][y2]][2]
        b3 = SUB[y3][1]
        bm = (b0, b1, b2, b3)
        assert sl2_f25_det(bm) == 1
        assert ADD[b0][b3] == y
        b_mats.append(bm)
        b_invs.append(sl2_f25_inv(bm))
        w_vals.append(b2)

    # Build ALL 14,999 irreducible triples (x, y, z) with D != 0
    triples = []  # (x, y, z, A, A_inv, B, B_inv, is_frob_rep, frob_partner_xyz)
    xyz_to_entry = {}
    for x in range(25):
        x2 = MUL[x][x]
        for y in range(25):
            y2 = MUL[y][y]
            xy = MUL[x][y]
            xy3 = MUL[3][xy]
            w_y = w_vals[y]
            bm = b_mats[y]
            bi = b_invs[y]
            x2_y2_m4 = SUB[ADD[x2][y2]][4]
            for z in range(25):
                # D = x^2 + y^2 + z^2 - xyz - 4
                disc_fricke = SUB[ADD[x2_y2_m4][MUL[z][z]]][MUL[xy][z]]
                if disc_fricke == 0:
                    continue
                # Solve for A = [[a, b], [c, x - a]] with tr(AB) = z, det(A) = 1
                # K = z + x - 3xy, c = K - 2a - b*w_y
                k_val = SUB[ADD[z][x]][xy3]
                a_mat = None
                for b in range(25):
                    s_coef = ADD[x][MUL[2][b]]
                    p_coef = SUB[ADD[1][MUL[b][k_val]]][MUL[MUL[b][b]][w_y]]
                    # disc = S^2 - 4*P = S^2 + P in F_25
                    d_quad = ADD[MUL[s_coef][s_coef]][p_coef]
                    r_sq = SQRT[d_quad]
                    if r_sq != -1:
                        a = MUL[3][ADD[s_coef][r_sq]]
                        c = SUB[SUB[k_val][MUL[2][a]]][MUL[b][w_y]]
                        am = (a, b, c, SUB[x][a])
                        a_mat = am
                        break
                assert a_mat is not None
                assert sl2_f25_det(a_mat) == 1
                assert ADD[a_mat[0]][a_mat[3]] == x
                ab = sl2_f25_mul(a_mat, bm)
                assert ADD[ab[0]][ab[3]] == z

                ai = sl2_f25_inv(a_mat)
                frob_xyz = (FROB[x], FROB[y], FROB[z])
                entry = (x, y, z, a_mat, ai, bm, bi, (x, y, z) <= frob_xyz, frob_xyz)
                xyz_to_entry[(x, y, z)] = entry
                triples.append(entry)

    assert len(triples) == 14999
    frob_reps = [e for e in triples if e[7]]
    return triples, frob_reps, xyz_to_entry


def _eval_sl2_f25_word(w_code, mats4):
    a = ADD
    m = MUL
    c0, c1, c2, c3 = mats4[w_code[0]]
    for idx in w_code[1:]:
        b0, b1, b2, b3 = mats4[idx]
        nc0 = a[m[c0][b0]][m[c1][b2]]
        nc1 = a[m[c0][b1]][m[c1][b3]]
        nc2 = a[m[c2][b0]][m[c3][b2]]
        nc3 = a[m[c2][b1]][m[c3][b3]]
        c0, c1, c2, c3 = nc0, nc1, nc2, nc3
    return (c0, c1, c2, c3)


def subgroup_order_sl2_f25(a_mat, b_mat, cap=241):
    """Explicit BFS subgroup order in SL(2, F_25), stopping once len > cap-1 (or exact if cap >= 15600)."""
    ident = (1, 0, 0, 1)
    seen = {ident}
    queue = [ident]
    gens = (a_mat, sl2_f25_inv(a_mat), b_mat, sl2_f25_inv(b_mat))
    a = ADD
    m = MUL
    while queue:
        c0, c1, c2, c3 = queue.pop()
        for b0, b1, b2, b3 in gens:
            nxt = (
                a[m[c0][b0]][m[c1][b2]],
                a[m[c0][b1]][m[c1][b3]],
                a[m[c2][b0]][m[c3][b2]],
                a[m[c2][b1]][m[c3][b3]],
            )
            if nxt not in seen:
                seen.add(nxt)
                if len(seen) >= cap:
                    return len(seen)
                queue.append(nxt)
    return len(seen)


def _classify_parabolic_pair(m_mat, l_mat):
    """
    Verify M, L are commuting non-central parabolics in SL(2, F_25).
    Extract spin sign alpha_Z and basis-free cusp ratio tau_cusp (N_l = tau_cusp * N_m).
    Returns None if not genuinely parabolic, else (alpha_z, tau_cusp, is_full2d).
    """
    tr_m = ADD[m_mat[0]][m_mat[3]]
    tr_l = ADD[l_mat[0]][l_mat[3]]
    if tr_m not in (2, 3) or tr_l not in (2, 3):
        return None
    sm = 1 if tr_m == 2 else 4  # +1 or -1 in F_5
    sl = 1 if tr_l == 2 else 4
    # Check non-scalar (genuinely parabolic)
    sm_i = (sm, 0, 0, sm)
    sl_i = (sl, 0, 0, sl)
    if m_mat == sm_i or l_mat == sl_i:
        return None
    # Verify commuting
    if sl2_f25_mul(m_mat, l_mat) != sl2_f25_mul(l_mat, m_mat):
        return None
    # Nilpotent parts N_m = s_m * M - I, N_l = s_l * L - I
    nm = (
        SUB[MUL[sm][m_mat[0]]][1],
        MUL[sm][m_mat[1]],
        MUL[sm][m_mat[2]],
        SUB[MUL[sm][m_mat[3]]][1],
    )
    nl = (
        SUB[MUL[sl][l_mat[0]]][1],
        MUL[sl][l_mat[1]],
        MUL[sl][l_mat[2]],
        SUB[MUL[sl][l_mat[3]]][1],
    )
    # Verify N_m^2 == 0 and N_l^2 == 0
    zero_m = (0, 0, 0, 0)
    if sl2_f25_mul(nm, nm) != zero_m or sl2_f25_mul(nl, nl) != zero_m:
        return None
    # Find unique tau_cusp with N_l == tau_cusp * N_m
    tau = None
    for idx in range(4):
        if nm[idx] != 0:
            tau = MUL[nl[idx]][INV[nm[idx]]]
            break
    if tau is None or tau == 0:
        return None
    for idx in range(4):
        if nl[idx] != MUL[tau][nm[idx]]:
            return None
    alpha_z = (0 if sm == 1 else 1, 0 if sl == 1 else 1)
    is_full2d = tau >= 5  # tau not in F_5 = {0, 1, 2, 3, 4}
    return alpha_z, tau, is_full2d


def search_sl2_f25_orientable(m_rec, frob_reps, xyz_to_entry, full_order_check=False):
    """
    Exhaustive SL(2, F_25) parabolic search across all 14,999 irreducible Fricke triples
    using Frobenius-orbit acceleration (verifying BOTH conjugates directly via explicit B-gauge matrices).
    """
    gens = m_rec["gens"]
    assert len(gens) == 2
    rels_c = [_compile_word_indices(r, gens) for r in m_rec["rels"]]
    pm_c = _compile_word_indices(m_rec["periph"][0], gens)
    pl_c = _compile_word_indices(m_rec["periph"][1], gens)
    ident = (1, 0, 0, 1)

    # Pick shortest peripheral word for lossless pre-filter tr(w) in {2, 3}
    pw_m = m_rec["periph"][0]
    pw_l = m_rec["periph"][1]
    short_w, short_c = (pw_m, pm_c) if len(pw_m) <= len(pw_l) else (pw_l, pl_c)

    # Fast exact trace check when shortest peripheral word has length 1 or 2
    mode = 0
    if short_w in ("a", "A"):
        mode = 1
    elif short_w in ("b", "B"):
        mode = 2
    elif short_w in ("ab", "ba", "AB", "BA"):
        mode = 3
    elif short_w in ("aB", "Ab", "bA", "Ba"):
        mode = 4
    elif len(rels_c[0]) < len(short_c):
        mode = 5

    candidates = []
    a_tbl = ADD
    s_tbl = SUB
    m_tbl = MUL
    for entry in frob_reps:
        x, y, z, am, ai, bm, bi, _, frob_xyz = entry
        if mode == 1:
            if x != 2 and x != 3:
                continue
        elif mode == 2:
            if y != 2 and y != 3:
                continue
        elif mode == 3:
            if z != 2 and z != 3:
                continue
        elif mode == 4:
            tr_abinv = s_tbl[m_tbl[x][y]][z]
            if tr_abinv != 2 and tr_abinv != 3:
                continue
        elif mode == 5:
            mats4 = (am, ai, bm, bi)
            if _eval_sl2_f25_word(rels_c[0], mats4) != ident:
                continue
        else:
            mats4 = (am, ai, bm, bi)
            wm = _eval_sl2_f25_word(short_c, mats4)
            tr_w = a_tbl[wm[0]][wm[3]]
            if tr_w != 2 and tr_w != 3:
                continue

        # Candidate survived shortest-word filter; check relators directly
        mats4 = (am, ai, bm, bi)
        ok = True
        for rc in rels_c:
            if _eval_sl2_f25_word(rc, mats4) != ident:
                ok = False
                break
        if ok:
            candidates.append(entry)
            if frob_xyz != (x, y, z):
                candidates.append(xyz_to_entry[frob_xyz])

    full2d_any = 0
    full2d_spin = 0
    f5_only = 0
    alphas_spin = set()
    sample_spin_hit = None
    exact_15600_verified = False

    for x, y, z, am, ai, bm, bi, _, _ in candidates:
        mats4 = (am, ai, bm, bi)
        # Re-verify ALL relators explicitly (including for Frobenius partner!)
        for rc in rels_c:
            assert _eval_sl2_f25_word(rc, mats4) == ident
        m_mat = _eval_sl2_f25_word(pm_c, mats4)
        l_mat = _eval_sl2_f25_word(pl_c, mats4)
        cls = _classify_parabolic_pair(m_mat, l_mat)
        if cls is None:
            continue
        alpha_z, tau, is_full2d = cls
        if is_full2d:
            # Independent subgroup order verification (> 240 implies full SL(2, F_25) by Dickson)
            ord_check = subgroup_order_sl2_f25(am, bm, cap=241)
            assert ord_check > 240
            if full_order_check and not exact_15600_verified:
                full_ord = subgroup_order_sl2_f25(am, bm, cap=16000)
                assert full_ord == 15600
                exact_15600_verified = True
            full2d_any += 1
            if alpha_z != (0, 0):
                full2d_spin += 1
                alphas_spin.add(alpha_z)
                if sample_spin_hit is None:
                    sample_spin_hit = (alpha_z, tau)
        else:
            f5_only += 1

    return {
        "full2d_any": full2d_any,
        "full2d_spin": full2d_spin,
        "f5_only": f5_only,
        "alphas_spin": sorted(alphas_spin),
        "sample_spin_hit": sample_spin_hit,
        "exact_15600_verified": exact_15600_verified,
    }


def search_sl2_f25_m000(m000_rec, all_triples):
    """Exhaustively check ALL 14,999 irreducible Fricke triples on non-orientable m000."""
    gens = m000_rec["gens"]
    rels_c = [_compile_word_indices(r, gens) for r in m000_rec["rels"]]
    pm_c = _compile_word_indices(m000_rec["periph"][0], gens)
    pl_c = _compile_word_indices(m000_rec["periph"][1], gens)
    ident = (1, 0, 0, 1)

    total_irred_hits = 0
    surj_hits = 0
    nonorient_parabolic_hits = 0
    for _, _, _, am, ai, bm, bi, _, _ in all_triples:
        mats4 = (am, ai, bm, bi)
        ok = True
        for rc in rels_c:
            if _eval_sl2_f25_word(rc, mats4) != ident:
                ok = False
                break
        if not ok:
            continue
        total_irred_hits += 1
        ord_sub = subgroup_order_sl2_f25(am, bm, cap=241)
        if ord_sub > 240:
            surj_hits += 1
            m_mat = _eval_sl2_f25_word(pm_c, mats4)
            l_mat = _eval_sl2_f25_word(pl_c, mats4)
            tr_m = ADD[m_mat[0]][m_mat[3]]
            tr_l = ADD[l_mat[0]][l_mat[3]]
            if tr_m in (2, 3) and tr_l in (2, 3):
                nonorient_parabolic_hits += 1

    return {
        "total_irred_hits": total_irred_hits,
        "sl2_f25_surj_hits": surj_hits,
        "sl2_f25_nonorient_parabolic_hits": nonorient_parabolic_hits,
    }


# =============================================================================
# 7. Q3B — DISJOINT DIRECT BACKTRACKING / SUBSTITUTION GLUING SOLVER OVER F_25\{0,1}
# =============================================================================
# Completely disjoint from discrete-log Meet-in-the-Middle:
# Uses exact algebraic multiplication/division of gluing equations to derive sparse
# redundant equations, then runs direct F_25 constraint-propagating backtracking &
# unit-clause algebraic substitution, verifying every solution against all raw equations.

DOM_F25 = tuple(range(2, 25))  # 23 elements of F_25 \ {0, 1}
DOM_F5 = (2, 3, 4)             # 3 elements of F_5 \ {0, 1}
ONE_MINUS_Z = [SUB[1][z] for z in range(25)]


def _verify_gluing_solution(gluing_rect, assign):
    for a_row, b_row, c_sign in gluing_rect:
        rhs = 1 if c_sign == 1 else 4
        prod = 1
        for k, z in enumerate(assign):
            ak = a_row[k]
            bk = b_row[k]
            if ak != 0:
                prod = MUL[prod][f25_pow(z, ak)]
            if bk != 0:
                prod = MUL[prod][f25_pow(ONE_MINUS_Z[z], bk)]
        if prod != rhs:
            return False
    return True


def _factor_table_cached(ab_cache, ak, bk):
    key = (ak % 24, bk % 24)
    if key in ab_cache:
        return ab_cache[key]
    a_r, b_r = key
    vals = [0] * 25
    inv_map = {}
    all_one = True
    for z in DOM_F25:
        v = MUL[f25_pow(z, a_r)][f25_pow(ONE_MINUS_Z[z], b_r)]
        vals[z] = v
        if v != 1:
            all_one = False
        inv_map.setdefault(v, []).append(z)
    entry = (all_one, tuple(vals), {v: tuple(zs) for v, zs in inv_map.items()})
    ab_cache[key] = entry
    return entry


_AB_CACHE = {}


def _derive_sparse_equations(gluing_rect, n_vars):
    """
    Pure algebraic combination E_i * E_j and E_i / E_j (no discrete log)
    to create logically implied sparser equations that accelerate unit propagation.
    """
    def normalize_eq(a_row, b_row, rhs):
        ar = tuple(x % 24 for x in a_row)
        br = tuple(x % 24 for x in b_row)
        supp = 0
        for k in range(n_vars):
            all_one, _, _ = _factor_table_cached(_AB_CACHE, ar[k], br[k])
            if not all_one:
                supp += 1
        return (ar, br, rhs, supp)

    base = []
    seen = set()
    for a_row, b_row, c_sign in gluing_rect:
        rhs = 1 if c_sign == 1 else 4
        eq = normalize_eq(a_row, b_row, rhs)
        key = (eq[0], eq[1], eq[2])
        if key not in seen:
            seen.add(key)
            base.append(eq)

    derived = list(base)
    # Two rounds of pairwise multiply/divide keeping strictly sparser implied equations
    for _ in range(2):
        added = []
        cur_len = len(derived)
        for i in range(cur_len):
            a1, b1, r1, s1 = derived[i]
            for j in range(i + 1, cur_len):
                a2, b2, r2, s2 = derived[j]
                limit = min(s1, s2)
                for sgn in (1, -1):
                    na = tuple((a1[k] + sgn * a2[k]) % 24 for k in range(n_vars))
                    nb = tuple((b1[k] + sgn * b2[k]) % 24 for k in range(n_vars))
                    nr = MUL[r1][r2]  # r2 in {1, 4} so r2 == r2^{-1}
                    eq = normalize_eq(na, nb, nr)
                    if 1 <= eq[3] < limit and eq[3] <= 4:
                        key = (eq[0], eq[1], eq[2])
                        if key not in seen:
                            seen.add(key)
                            added.append(eq)
        added.sort(key=lambda e: e[3])
        derived.extend(added[:16])
    return derived


def solve_gluing_direct_backtrack(gluing_rect, domain_vals, require_strict_f25=False):
    """
    Direct constraint-propagating backtracking & unit-substitution solver over F_25 \\ {0, 1}.
    Returns a verified solution tuple or None.
    """
    if not gluing_rect:
        return None
    n_vars = len(gluing_rect[0][0])
    eq_list = _derive_sparse_equations(gluing_rect, n_vars)

    # Compile each equation into active variables, factor tables, and inverse-lookup maps
    compiled_eqs = []
    for ar, br, rhs, _ in eq_list:
        active = []
        ftabs = {}
        imaps = {}
        for k in range(n_vars):
            all_one, vals, imap = _factor_table_cached(_AB_CACHE, ar[k], br[k])
            if not all_one:
                active.append(k)
                ftabs[k] = vals
                imaps[k] = imap
        if not active:
            if rhs != 1:
                return None
            continue
        compiled_eqs.append((tuple(active), ftabs, imaps, rhs))

    # Build initial domain sets (filtered by unary equations)
    dom_set = set(domain_vals)
    init_domains = [set(dom_set) for _ in range(n_vars)]
    for active, _, imaps, rhs in compiled_eqs:
        if len(active) == 1:
            k = active[0]
            allowed = set(imaps[k].get(rhs, ()))
            init_domains[k] &= allowed
            if not init_domains[k]:
                return None

    var_eqs = [[] for _ in range(n_vars)]
    for e_idx, (active, _, _, _) in enumerate(compiled_eqs):
        for k in active:
            var_eqs[k].append(e_idx)

    def propagate_and_search(domains, assign):
        # Fixed-point unit-clause substitution & constraint propagation
        changed = True
        while changed:
            changed = False
            # Assign any singleton domain
            for k in range(n_vars):
                if assign[k] is None:
                    dk = domains[k]
                    if not dk:
                        return None
                    if len(dk) == 1:
                        assign[k] = next(iter(dk))
                        changed = True

            # Check all equations: 0-unassigned -> verify; 1-unassigned -> direct substitution
            for active, ftabs, imaps, rhs in compiled_eqs:
                unassigned_k = -1
                unassigned_cnt = 0
                prod = 1
                for k in active:
                    ak_val = assign[k]
                    if ak_val is None:
                        unassigned_cnt += 1
                        unassigned_k = k
                        if unassigned_cnt > 1:
                            break
                    else:
                        prod = MUL[prod][ftabs[k][ak_val]]
                if unassigned_cnt == 0:
                    if prod != rhs:
                        return None
                elif unassigned_cnt == 1:
                    need = MUL[rhs][INV[prod]]
                    allowed = imaps[unassigned_k].get(need, ())
                    if not allowed:
                        return None
                    dk = domains[unassigned_k]
                    new_dk = dk.intersection(allowed)
                    if not new_dk:
                        return None
                    if len(new_dk) < len(dk):
                        domains[unassigned_k] = new_dk
                        changed = True
                        if len(new_dk) == 1:
                            assign[unassigned_k] = next(iter(new_dk))

        # Check completion
        unassigned = [k for k in range(n_vars) if assign[k] is None]
        if not unassigned:
            sol = tuple(assign)
            if require_strict_f25 and all(z < 5 for z in sol):
                return None
            if _verify_gluing_solution(gluing_rect, sol):
                return sol
            return None

        # Choose branching variable: prefer smallest remaining equation arity, then smallest domain
        best_k = unassigned[0]
        best_score = (999, 999, 0)
        for k in unassigned:
            min_arity = 999
            for e_idx in var_eqs[k]:
                active = compiled_eqs[e_idx][0]
                ar = sum(1 for j in active if assign[j] is None)
                if ar < min_arity:
                    min_arity = ar
            score = (min_arity, len(domains[k]), -len(var_eqs[k]))
            if score < best_score:
                best_score = score
                best_k = k

        # Order domain values: try strict F_25 \ F_5 first if require_strict_f25
        vals_order = sorted(
            domains[best_k],
            key=lambda z: (0 if (require_strict_f25 and z >= 5) else 1, z),
        )
        for val in vals_order:
            new_domains = [set(d) for d in domains]
            new_domains[best_k] = {val}
            new_assign = list(assign)
            new_assign[best_k] = val
            res = propagate_and_search(new_domains, new_assign)
            if res is not None:
                return res
        return None

    return propagate_and_search(init_domains, [None] * n_vars)


# =============================================================================
# 8. Q4 — INDEPENDENT 2T = SL(2, F_3) SURJECTION & Aut(2T) ORBIT COUNTER
# =============================================================================

def _build_sl2_f3():
    mats = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    if (a * d - b * c) % 3 == 1:
                        mats.append((a, b, c, d))
    assert len(mats) == 24
    ident = (1, 0, 0, 1)
    mats.remove(ident)
    mats.insert(0, ident)
    idx_map = {m: i for i, m in enumerate(mats)}

    def m3(x, y):
        return (
            (x[0] * y[0] + x[1] * y[2]) % 3,
            (x[0] * y[1] + x[1] * y[3]) % 3,
            (x[2] * y[0] + x[3] * y[2]) % 3,
            (x[2] * y[1] + x[3] * y[3]) % 3,
        )

    def i3(x):
        return (x[3], (-x[1]) % 3, (-x[2]) % 3, x[0])

    mul_t = [[idx_map[m3(x, y)] for y in mats] for x in mats]
    inv_t = [idx_map[i3(x)] for x in mats]

    # Build GL(2, F_3) conjugation action = Aut(SL(2, F_3)) (order 24 = |PGL(2, F_3)|)
    gl_mats = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    det = (a * d - b * c) % 3
                    if det in (1, 2):
                        gl_mats.append((a, b, c, d, det))
    aut_perms = set()
    for a, b, c, d, det in gl_mats:
        inv_det = det  # 1^-1 = 1, 2^-1 = 2 mod 3
        g = (a, b, c, d)
        gi = ((d * inv_det) % 3, ((-b) * inv_det) % 3, ((-c) * inv_det) % 3, (a * inv_det) % 3)
        perm = tuple(idx_map[m3(m3(g, x), gi)] for x in mats)
        aut_perms.add(perm)
    assert len(aut_perms) == 24

    # Precompute all surjective pairs in SL(2, F_3)^2
    surj_pairs = []
    for i in range(24):
        for j in range(24):
            seen = {0}
            q = [0]
            gs = (i, inv_t[i], j, inv_t[j])
            while q:
                u = q.pop()
                for g in gs:
                    v = mul_t[u][g]
                    if v not in seen:
                        seen.add(v)
                        q.append(v)
            if len(seen) == 24:
                surj_pairs.append((i, j))
    assert len(surj_pairs) == 384

    return mul_t, inv_t, surj_pairs, sorted(aut_perms)


SL2_F3_MUL, SL2_F3_INV, SL2_F3_SURJ_PAIRS, SL2_F3_AUTS = _build_sl2_f3()


def count_2t_orbits_2gen(m_rec):
    gens = m_rec["gens"]
    assert len(gens) == 2
    rels_c = [_compile_word_indices(r, gens) for r in m_rec["rels"]]
    hits = set()
    for ga, gb in SL2_F3_SURJ_PAIRS:
        gi = (ga, SL2_F3_INV[ga], gb, SL2_F3_INV[gb])
        ok = True
        for rc in rels_c:
            if _eval_group_word(SL2_F3_MUL, rc, gi) != 0:
                ok = False
                break
        if ok:
            hits.add((ga, gb))
    # Partition hits directly into exact Aut(2T) orbits
    unvisited = set(hits)
    orbits = 0
    while unvisited:
        ga, gb = next(iter(unvisited))
        orb = {(perm[ga], perm[gb]) for perm in SL2_F3_AUTS}
        assert len(orb) == 24 and orb.issubset(hits)
        unvisited -= orb
        orbits += 1
    assert orbits * 24 == len(hits)
    return orbits, len(hits)


# =============================================================================
# 9. LIVE SNAPPY CROSS-CHECK & PURE-TOPOLOGY INSPECTION
# =============================================================================

def run_snappy_integrity_and_topology(by_name):
    # Independently query OrientableCuspedCensus for num_cusps == 1, num_tet <= 6
    tet_counts = {}
    total_orient = 0
    for k in range(2, 7):
        c = snappy.OrientableCuspedCensus(cusps=1, tets=k)
        n_k = len(c)
        tet_counts[str(k)] = n_k
        total_orient += n_k
    census_count_ok = (total_orient == 1199)

    spot_names = [
        "m004", "m003", "m000", "m045", "m191", "m266",
        "s136", "s447", "s560", "s758", "s850",
    ]
    spot_checks = {}
    spot_all_ok = True
    for nm in spot_names:
        rec = by_name[nm]
        m = snappy.Manifold(nm)
        g = m.fundamental_group()
        h = m.homology()
        sn_gens = list(g.generators())
        sn_rels = list(g.relators())
        sn_periph = list(g.peripheral_curves()[0])
        sn_betti = int(h.betti_number())
        sn_tors = [int(d) for d in h.elementary_divisors() if int(d) != 0]
        sn_orient = bool(m.is_orientable())
        sn_tet = int(m.num_tetrahedra())
        if sn_orient:
            sn_gluing = [[list(a), list(b), int(c)] for (a, b, c) in m.gluing_equations("rect")]
            gluing_match = (rec["gluing_rect"] == sn_gluing)
        else:
            gluing_match = (rec["gluing_rect"] == [])
        match = (
            rec["orientable"] == sn_orient
            and rec["num_tet"] == sn_tet
            and rec["gens"] == sn_gens
            and rec["rels"] == sn_rels
            and rec["periph"] == sn_periph
            and rec["betti1"] == sn_betti
            and rec["h1_torsion"] == sn_tors
            and gluing_match
        )
        spot_checks[nm] = {
            "exact_match": match,
            "orientable": sn_orient,
            "num_tet": sn_tet,
            "gluing_match": gluing_match,
        }
        if not match:
            spot_all_ok = False

    # Pure-topology inspection of the 6 lock_248_H1_Z_and_2T manifolds (ZERO floats!)
    six_names = ["m004", "m266", "s136", "s447", "s560", "s850"]
    six_topology = {}
    for nm in six_names:
        m = snappy.Manifold(nm)
        sg = m.symmetry_group()
        six_topology[nm] = {
            "identify": [str(x) for x in m.identify()],
            "symmetry_group": str(sg),
            "symmetry_order": int(sg.order()),
            "is_amphicheiral": bool(sg.is_amphicheiral()),
            "homology": str(m.homology()),
            "num_tet": int(m.num_tetrahedra()),
            "num_gens": int(len(m.fundamental_group().generators())),
            "solution_type": str(m.solution_type()),
            "volume_str": str(m.volume()),
        }

    # Deterministic diagnostic on s758 (default SnapPy triangulation)
    m758 = snappy.Manifold("s758")
    s758_default_gluing = [[list(a), list(b), int(c)] for (a, b, c) in m758.gluing_equations("rect")]
    s758_default_strict = solve_gluing_direct_backtrack(s758_default_gluing, DOM_F25, True) is not None
    s758_default_f5 = solve_gluing_direct_backtrack(s758_default_gluing, DOM_F5, False) is not None

    return {
        "snappy_version": str(snappy.__version__),
        "orientable_1cusp_le6_count": total_orient,
        "orientable_by_tet": tet_counts,
        "census_count_ok": census_count_ok,
        "spot_checks_11_manifolds": spot_checks,
        "spot_checks_all_ok": spot_all_ok,
        "lock_248_H1_Z_and_2T_topology": six_topology,
        "s758_diagnostic": {
            "default_triangulation_strict_f25_gluing": s758_default_strict,
            "default_triangulation_f5_gluing": s758_default_f5,
            "solution_type": str(m758.solution_type()),
            "num_tet": int(m758.num_tetrahedra()),
        },
        "ok": census_count_ok and spot_all_ok,
    }


# =============================================================================
# 10. PRODUCER HASHES, STANDALONE CONTROL, & 5 REFEREE PLANTED FAULTS (RPF1..RPF5)
# =============================================================================

def verify_producer_hashes_and_control():
    sha_files = ["DATA_SHA256.txt", "SCRIPT_SHA256.txt", "OUTPUT_SHA256.txt"]
    hash_results = {}
    all_hashes_ok = True
    for sf in sha_files:
        sf_path = os.path.join(PRODUCER_DIR, sf)
        with open(sf_path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                expected_hex, fname = line.split(None, 1)
                fname = fname.strip()
                fpath = os.path.join(PRODUCER_DIR, fname)
                with open(fpath, "rb") as target:
                    actual_hex = hashlib.sha256(target.read()).hexdigest()
                ok = (actual_hex == expected_hex)
                hash_results[fname] = {
                    "sha_file": sf,
                    "expected": expected_hex,
                    "actual": actual_hex,
                    "match": ok,
                }
                if not ok:
                    all_hashes_ok = False

    # Run Producer's standalone exit-1 control under python3 -I
    proc = subprocess.run(
        [sys.executable, "-I", PRODUCER_CONTROL_PATH],
        capture_output=True,
        cwd=PRODUCER_DIR,
    )
    control_ok = (proc.returncode == 1 and len(proc.stderr) == 0)

    return {
        "producer_sha256_checks": hash_results,
        "all_producer_hashes_ok": all_hashes_ok,
        "producer_control_returncode": int(proc.returncode),
        "producer_control_stderr_bytes": int(len(proc.stderr)),
        "producer_control_stdout": proc.stdout.decode("utf-8", "replace").strip(),
        "producer_control_ok": control_ok,
        "ok": all_hashes_ok and control_ok,
    }


def run_referee_planted_faults(by_name, frob_reps, xyz_to_entry):
    # RPF1: Omit BD_5 sheet action on m004 (H_per = C1) => k128_total == 8, k248(alpha_Z) == 8
    _, k128_rpf1, k248_rpf1 = evaluate_e8_248_kernels(1, 5, (0, 1), 0, 0)
    rpf1_ok = (sum(k128_rpf1.values()) == 8 and k248_rpf1[(0, 1)] == 8)

    # RPF2: Replace C4 by C5, C2, C10 on m004 => k128_total strictly positive (never 0)
    _, k128_c5, _ = evaluate_e8_248_kernels(1, 5, (0, 1), BD5["r_idx"], 0)
    _, k128_c2, _ = evaluate_e8_248_kernels(1, 5, (0, 1), BD5["neg_id_idx"], 0)
    _, k128_c10, _ = evaluate_e8_248_kernels(1, 5, (0, 1), BD5["neg_id_idx"], BD5["r_idx"])
    rpf2_ok = (
        sum(k128_c5.values()) in (4, 6)
        and sum(k128_c2.values()) == 8
        and sum(k128_c10.values()) in (4, 6)
    )

    # RPF3: Cohomology alignment fault alpha_Z == beta_j => k128 == 0 but k120(alpha_Z) == 4, k248 == 4
    k120_rpf3, k128_rpf3, k248_rpf3 = evaluate_e8_248_kernels(
        1, 5, (0, 1), 0, BD5["j_idx"]
    )
    rpf3_ok = (
        sum(k128_rpf3.values()) == 0
        and k120_rpf3[(0, 1)] == 4
        and k248_rpf3[(0, 1)] == 4
    )

    # RPF4: (a) Degenerate F_5 parabolic pair fails full-2D gate & has |<A,B>| <= 240
    #       (b) Explicitly D_5->BD_5 obstructed manifold m009 has d5_surj > 0 and bd5_surj == 0
    a_f5 = (1, 1, 0, 1)
    b_f5 = (1, 0, 1, 1)
    ord_f5 = subgroup_order_sl2_f25(a_f5, b_f5, cap=241)
    cls_deg = _classify_parabolic_pair((4, 4, 0, 4), (1, 2, 0, 1))
    m009_res = analyze_d5_bd5_manifold(by_name["m009"])
    rpf4_ok = (
        ord_f5 == 120
        and cls_deg is not None
        and cls_deg[2] is False
        and m009_res["d5_surj"] > 0
        and m009_res["bd5_surj"] == 0
    )

    # RPF5: (a) Corrupted m004 relator breaks both BD_5 and SL(2, F_25)
    #       (b) Sign-flipped gluing equation on m004 yields 0 gluing solutions
    m004_bad = dict(by_name["m004"])
    m004_bad["rels"] = ["aaabABBA"]  # dropped final 'b'
    bad_bd5 = analyze_d5_bd5_manifold(m004_bad)
    bad_sl2 = search_sl2_f25_orientable(m004_bad, frob_reps, xyz_to_entry)
    m004_bad_gluing = [list(r) for r in by_name["m004"]["gluing_rect"]]
    m004_bad_gluing[0] = [m004_bad_gluing[0][0], m004_bad_gluing[0][1], -m004_bad_gluing[0][2]]
    bad_glue_sol = solve_gluing_direct_backtrack(m004_bad_gluing, DOM_F25, True)
    rpf5_ok = (
        bad_bd5["bd5_surj"] == 0
        and bad_sl2["full2d_any"] == 0
        and bad_glue_sol is None
    )

    controls = {
        "RPF1_drop_sheet_restores_8": rpf1_ok,
        "RPF2_C5_C2_C10_leave_k128_positive": rpf2_ok,
        "RPF3_alpha_eq_beta_activates_4_in_120": rpf3_ok,
        "RPF4_F5_degenerate_and_m009_obstructed": rpf4_ok,
        "RPF5_corrupted_m004_relator_and_gluing": rpf5_ok,
    }
    return controls, sum(1 for v in controls.values() if v)


# =============================================================================
# 11. AST FLOAT & JSON FLOAT SELF-AUDIT
# =============================================================================

def count_ast_floats(py_path):
    with open(py_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read(), filename=py_path)
    cnt = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            cnt += 1
    return cnt


def count_json_floats(obj):
    if isinstance(obj, float):
        return 1
    if isinstance(obj, dict):
        return sum(count_json_floats(v) for v in obj.values())
    if isinstance(obj, (list, tuple)):
        return sum(count_json_floats(v) for v in obj)
    return 0


# =============================================================================
# 12. MAIN REFEREE DRIVER & ZERO-TRUST PRODUCER COMPARISON
# =============================================================================

def main():
    t0_ns = time.perf_counter_ns()

    with open(CENSUS_DATA_PATH, "r", encoding="utf-8") as fh:
        census_data = json.load(fh)
    with open(PRODUCER_OUT_PATH, "r", encoding="utf-8") as fh:
        prod = json.load(fh)

    manifolds = census_data["manifolds"]
    by_name = {m["name"]: m for m in manifolds}
    discrepancies = []

    def check_eq(label, got, expected):
        if got != expected:
            discrepancies.append({
                "check": label,
                "referee": got,
                "producer": expected,
            })

    # Step 0: Producer SHA256 hashes & standalone exit-1 control
    integrity = verify_producer_hashes_and_control()
    if not integrity["ok"]:
        discrepancies.append({"check": "producer_integrity_or_control", "detail": integrity})

    # Step 1: Live SnapPy cross-check & pure-topology inspection
    snappy_check = run_snappy_integrity_and_topology(by_name)
    if not snappy_check["ok"]:
        discrepancies.append({"check": "live_snappy_integrity", "detail": snappy_check})

    # Step 2: Independent Q1
    q1 = run_q1_universal_theorem()
    pq1 = prod["Q1_universal_E8_kernel_theorem"]
    check_eq("Q1.bases_checked", q1["bases_checked"], pq1["bases_checked"])
    check_eq("Q1.bases_w64_hist_4_3_2_all_ok", q1["bases_w64_hist_4_3_2_all_ok"], pq1["bases_w64_hist_4_3_2_all_ok"])
    check_eq("Q1.commuting_pairs_in_BD5", q1["commuting_pairs_in_BD5"], pq1["commuting_pairs_in_BD5"])
    check_eq("Q1.k128_total_by_Hper", q1["k128_total_by_Hper"], pq1["k128_total_by_Hper"])
    check_eq("Q1.k248_at_alpha_Z_by_Hper", q1["k248_at_alpha_Z_by_Hper"], pq1["k248_at_alpha_Z_by_Hper"])
    check_eq("Q1.c4_iff_k128_zero", q1["c4_iff_k128_zero"], pq1["c4_iff_k128_zero"])
    check_eq("Q1.c4_alpha_ne_beta_gives_k248_zero", q1["c4_alpha_ne_beta_gives_k248_zero"], pq1["c4_alpha_ne_beta_gives_k248_zero"])
    check_eq("Q1.c4_alpha_eq_beta_gives_k248_4", q1["c4_alpha_eq_beta_gives_k248_4"], pq1["c4_alpha_eq_beta_gives_k248_4"])
    check_eq("Q1.degenerate_1D_F5_geo_k128", q1["degenerate_1D_F5_geo_k128"], pq1["degenerate_1D_F5_geo_k128"])
    check_eq("Q1.degenerate_1D_F5_C4_k128", q1["degenerate_1D_F5_C4_k128"], pq1["degenerate_1D_F5_C4_k128"])
    check_eq("Q1.sl2z_30_matrix_basis_scrambling_ok", q1["sl2z_30_matrix_basis_scrambling_ok"], True)

    # Step 3: Independent Q2 across ALL 1,199 orientable + m000
    q2 = run_q2_census(manifolds)
    pq2 = prod["Q2_D5_BD5_census"]
    check_eq("Q2.d5_surj_manifolds", q2["d5_surj_manifolds"], pq2["d5_surj_manifolds"])
    check_eq("Q2.bd5_surj_manifolds", q2["bd5_surj_manifolds"], pq2["bd5_surj_manifolds"])
    check_eq("Q2.d5_to_bd5_obstructed_count", q2["d5_to_bd5_obstructed_count"], pq2["d5_to_bd5_obstructed_count"])
    check_eq("Q2.d5_to_bd5_obstructed_names", q2["d5_to_bd5_obstructed_names"], pq2["d5_to_bd5_obstructed_names"])
    check_eq("Q2.obstructed_all_have_even_H1_torsion", q2["obstructed_all_have_even_H1_torsion"], pq2["obstructed_all_have_even_H1_torsion"])
    check_eq("Q2.hper_bucket_counts", q2["hper_bucket_counts"], pq2["hper_bucket_counts"])
    check_eq("Q2.s_bd5_c4_total", q2["s_bd5_c4_total"], pq2["s_bd5_c4_total"])
    check_eq("Q2.s_bd5_c4_2gen", q2["s_bd5_c4_2gen"], pq2["s_bd5_c4_2gen"])
    check_eq("Q2.s_bd5_c4_3gen", q2["s_bd5_c4_3gen"], pq2["s_bd5_c4_3gen"])
    check_eq("Q2.s_bd5_c4_3gen_names", q2["s_bd5_c4_3gen_names"], pq2["s_bd5_c4_3gen_names"])
    check_eq("Q2.m003_d5_bd5", (q2["per_manifold"]["m003"]["d5_surj"], q2["per_manifold"]["m003"]["bd5_surj"]), (0, 0))
    check_eq("Q2.m000_d5_bd5", (q2["per_manifold"]["m000"]["d5_surj"], q2["per_manifold"]["m000"]["bd5_surj"]), (0, 0))

    # Step 4: Independent Q3A (SL(2, F_25) in independent B-gauge) across ALL 235 BD_5 2-gen + m003 + m000
    all_triples, frob_reps, xyz_to_entry = _build_fricke_b_gauge_table()
    full_15600_targets = {"m004", "m266", "s136", "s447", "s560", "s850", "s758", "m003"}

    sl2_results = {}
    for nm in q2["bd5_all_2gen_names"]:
        sl2_results[nm] = search_sl2_f25_orientable(
            by_name[nm], frob_reps, xyz_to_entry, full_order_check=(nm in full_15600_targets)
        )
    sl2_m003 = search_sl2_f25_orientable(
        by_name["m003"], frob_reps, xyz_to_entry, full_order_check=True
    )
    sl2_m000 = search_sl2_f25_m000(by_name["m000"], all_triples)

    non_c4_sl2_spin = sorted(
        nm for nm in q2["bd5_non_c4_2gen_names"] if sl2_results[nm]["full2d_spin"] > 0
    )
    non_c4_sl2_any = sorted(
        nm for nm in q2["bd5_non_c4_2gen_names"] if sl2_results[nm]["full2d_any"] > 0
    )

    lock128_names = []
    lock248_names = []
    cohom120_names = []
    lock_details = {}
    concrete_248_evals_checked = 0

    for nm in q2["s_bd5_c4_2gen_names"]:
        sr = sl2_results[nm]
        if sr["full2d_spin"] == 0:
            continue
        lock128_names.append(nm)
        qr = q2["per_manifold"][nm]
        alphas = sr["alphas_spin"]
        betas = qr["c4_betas"]
        has_unlocked = any(az != bj for az in alphas for bj in betas)
        if has_unlocked:
            lock248_names.append(nm)
        else:
            cohom120_names.append(nm)

        # Directly evaluate ALL 248 weights on a concrete realized (tau, alpha_Z, H_m, H_l) pair!
        sample_az, sample_tau = sr["sample_spin_hit"]
        chosen_az = sample_az
        chosen_bj = betas[0]
        if has_unlocked:
            for az in alphas:
                for bj in betas:
                    if az != bj:
                        chosen_az = az
                        chosen_bj = bj
                        break
                if chosen_az != chosen_bj:
                    break
        sample_hm, sample_hl = qr["c4_sample_by_beta"][chosen_bj]
        _, k128_m, k248_m = evaluate_e8_248_kernels(1, sample_tau, chosen_az, sample_hm, sample_hl)
        assert sum(k128_m.values()) == 0
        if has_unlocked:
            assert k248_m[chosen_az] == 0
        else:
            assert k248_m[chosen_az] == 4
        concrete_248_evals_checked += 1

        # Independent direct backtracking gluing check on every lock128 manifold
        glue_strict = solve_gluing_direct_backtrack(by_name[nm]["gluing_rect"], DOM_F25, True) is not None
        glue_f5 = solve_gluing_direct_backtrack(by_name[nm]["gluing_rect"], DOM_F5, False) is not None

        # Independent 2T = SL(2, F_3) orbit check
        two_t_orb, two_t_raw = count_2t_orbits_2gen(by_name[nm])

        lock_details[nm] = {
            "num_tet": by_name[nm]["num_tet"],
            "h1_torsion": by_name[nm]["h1_torsion"],
            "d5_surj": qr["d5_surj"],
            "bd5_surj": qr["bd5_surj"],
            "c4_ord_pairs": qr["c4_ord_pairs"],
            "sl2_f25_full2d_spin_hits": sr["full2d_spin"],
            "kills_128_to_0": True,
            "kills_248_basis_inv_to_0": has_unlocked,
            "alpha_Z_eq_beta_j_obstructed": not has_unlocked,
            "gluing_f25_strict": glue_strict,
            "gluing_f5": glue_f5,
            "two_T_orbits": two_t_orb,
            "two_T_raw": two_t_raw,
            "exact_15600_verified": sr["exact_15600_verified"],
        }

    lock128_names.sort()
    lock248_names.sort()
    cohom120_names.sort()

    # Step 5: Independent gluing verification on ALL 18 3-gen S_BD5_C4 + m003 + 40 deterministic samples
    three_gen_gluing = {}
    three_gen_strict_names = []
    for nm in q2["s_bd5_c4_3gen_names"]:
        g_strict = solve_gluing_direct_backtrack(by_name[nm]["gluing_rect"], DOM_F25, True) is not None
        g_f5 = solve_gluing_direct_backtrack(by_name[nm]["gluing_rect"], DOM_F5, False) is not None
        three_gen_gluing[nm] = {"gluing_f25_strict": g_strict, "gluing_f5": g_f5}
        if g_strict:
            three_gen_strict_names.append(nm)
    three_gen_strict_names.sort()

    m003_gluing_strict = solve_gluing_direct_backtrack(by_name["m003"]["gluing_rect"], DOM_F25, True) is not None
    m003_2t_orb, m003_2t_raw = count_2t_orbits_2gen(by_name["m003"])
    m000_2t_orb, m000_2t_raw = count_2t_orbits_2gen(by_name["m000"])

    # 40 deterministic sample manifolds from the rest of the orientable census
    covered = set(lock128_names) | set(q2["s_bd5_c4_3gen_names"]) | {"m003"}
    rest_orient = sorted(m["name"] for m in manifolds if m["orientable"] and m["name"] not in covered)
    step = len(rest_orient) // 40
    sample40_names = [rest_orient[i * step] for i in range(40)]
    sample40_strict_count = 0
    sample40_f5_count = 0
    for nm in sample40_names:
        if solve_gluing_direct_backtrack(by_name[nm]["gluing_rect"], DOM_F25, True) is not None:
            sample40_strict_count += 1
        if solve_gluing_direct_backtrack(by_name[nm]["gluing_rect"], DOM_F5, False) is not None:
            sample40_f5_count += 1

    # Compare Q3 against Producer v4
    pq3 = prod["Q3_SL2_F25_and_E8_lock"]
    check_eq("Q3.bd5_all_2gen_checked_fricke", len(q2["bd5_all_2gen_names"]), pq3["bd5_all_2gen_checked_fricke"])
    check_eq("Q3.bd5_non_c4_2gen_with_sl2_f25", len(non_c4_sl2_spin), pq3["bd5_non_c4_2gen_with_sl2_f25"])
    check_eq("Q3.bd5_non_c4_2gen_with_sl2_f25_names", non_c4_sl2_spin, pq3["bd5_non_c4_2gen_with_sl2_f25_names"])
    check_eq("Q3.s_e8_lock_128_count", len(lock128_names), pq3["s_e8_lock_128_count"])
    check_eq("Q3.s_e8_lock_128_names", lock128_names, pq3["s_e8_lock_128_names"])
    check_eq("Q3.s_e8_lock_248_count", len(lock248_names), pq3["s_e8_lock_248_count"])
    check_eq("Q3.s_e8_lock_248_names", lock248_names, pq3["s_e8_lock_248_names"])
    check_eq("Q3.s_e8_cohom_obstructed_120_count", len(cohom120_names), pq3["s_e8_cohom_obstructed_120_count"])
    check_eq("Q3.s_e8_cohom_obstructed_120_names", cohom120_names, pq3["s_e8_cohom_obstructed_120_names"])
    check_eq("Q3.s_bd5_c4_3gen_with_gluing_F25_strict", three_gen_strict_names, pq3["s_bd5_c4_3gen_with_gluing_F25_strict"])

    # Per-manifold field-by-field comparison on ALL 57 lock128 manifolds
    pdet = pq3["s_e8_lock_details"]
    check_eq("Q3.s_e8_lock_details.keys", sorted(lock_details.keys()), sorted(pdet.keys()))
    detail_fields = [
        "alpha_Z_eq_beta_j_obstructed",
        "bd5_surj",
        "c4_ord_pairs",
        "d5_surj",
        "gluing_f25_strict",
        "h1_torsion",
        "kills_128_to_0",
        "kills_248_basis_inv_to_0",
        "num_tet",
        "sl2_f25_full2d_spin_hits",
        "two_T_orbits",
    ]
    for nm in sorted(set(lock_details.keys()) & set(pdet.keys())):
        for fld in detail_fields:
            check_eq("Q3.detail." + nm + "." + fld, lock_details[nm][fld], pdet[nm][fld])

    # Confirm s758 specifically
    if "s758" in lock_details:
        check_eq("Q3.s758.gluing_f25_strict", lock_details["s758"]["gluing_f25_strict"], False)
        check_eq("Q3.s758.sl2_f25_full2d_spin_hits", lock_details["s758"]["sl2_f25_full2d_spin_hits"], 4)
    else:
        discrepancies.append({"check": "Q3.s758.present_in_lock128", "referee": False, "producer": True})

    # Step 6: Independent Q4 cross-tabulations
    lock128_by_tet = {}
    lock248_by_tet = {}
    for nm in lock128_names:
        tk = str(lock_details[nm]["num_tet"])
        lock128_by_tet[tk] = lock128_by_tet.get(tk, 0) + 1
    for nm in lock248_names:
        tk = str(lock_details[nm]["num_tet"])
        lock248_by_tet[tk] = lock248_by_tet.get(tk, 0) + 1

    lock128_with_2t = sorted(nm for nm in lock128_names if lock_details[nm]["two_T_orbits"] > 0)
    lock248_with_2t = sorted(nm for nm in lock248_names if lock_details[nm]["two_T_orbits"] > 0)
    lock248_h1z = sorted(nm for nm in lock248_names if lock_details[nm]["h1_torsion"] == [])
    lock248_h1z_2t = sorted(nm for nm in lock248_h1z if lock_details[nm]["two_T_orbits"] > 0)
    lock248_2t_eq_2 = sorted(nm for nm in lock248_names if lock_details[nm]["two_T_orbits"] == 2)

    pq4 = prod["Q4_crosstab_and_benchmarks"]
    check_eq("Q4.lock_128_by_tet", dict(sorted(lock128_by_tet.items())), pq4["lock_128_by_tet"])
    check_eq("Q4.lock_248_by_tet", dict(sorted(lock248_by_tet.items())), pq4["lock_248_by_tet"])
    check_eq("Q4.lock_128_with_2T_count", len(lock128_with_2t), pq4["lock_128_with_2T_count"])
    check_eq("Q4.lock_248_with_2T_count", len(lock248_with_2t), pq4["lock_248_with_2T_count"])
    check_eq("Q4.lock_248_with_2T_names", lock248_with_2t, pq4["lock_248_with_2T_names"])
    check_eq("Q4.lock_248_H1_Z_count", len(lock248_h1z), pq4["lock_248_H1_Z_count"])
    check_eq("Q4.lock_248_H1_Z_names", lock248_h1z, pq4["lock_248_H1_Z_names"])
    check_eq("Q4.lock_248_H1_Z_and_2T_count", len(lock248_h1z_2t), pq4["lock_248_H1_Z_and_2T_count"])
    check_eq("Q4.lock_248_H1_Z_and_2T_names", lock248_h1z_2t, pq4["lock_248_H1_Z_and_2T_names"])
    check_eq("Q4.lock_248_2T_eq_2_count", len(lock248_2t_eq_2), pq4["lock_248_2T_eq_2_count"])
    check_eq("Q4.lock_248_2T_eq_2_names", lock248_2t_eq_2, pq4["lock_248_2T_eq_2_names"])

    # m003 and m000 benchmarks
    check_eq("Q4.m003.gluing_f25_strict", m003_gluing_strict, pq4["m003_summary"]["gluing_f25_strict"])
    check_eq("Q4.m003.sl2_f25_full2d_hits", sl2_m003["full2d_any"], pq4["m003_summary"]["sl2_f25_full2d_hits"])
    check_eq("Q4.m003.two_T_orbits", m003_2t_orb, pq4["m003_summary"]["two_T_orbits"])
    check_eq("Q4.m000.sl2_f25_surj_hits", sl2_m000["sl2_f25_surj_hits"], pq4["m000_summary"]["sl2_f25_surj_hits"])
    check_eq("Q4.m000.sl2_f25_nonorient_parabolic_hits", sl2_m000["sl2_f25_nonorient_parabolic_hits"], pq4["m000_summary"]["sl2_f25_nonorient_parabolic_hits"])
    check_eq("Q4.m000.two_T_orbits", m000_2t_orb, pq4["m000_summary"]["two_T_orbits"])

    # Step 7: 5 Independent Referee Planted Fault Controls (RPF1..RPF5)
    rpf_controls, rpf_caught = run_referee_planted_faults(by_name, frob_reps, xyz_to_entry)
    if rpf_caught != 5:
        discrepancies.append({"check": "RPF_controls", "caught": rpf_caught, "details": rpf_controls})

    t1_ns = time.perf_counter_ns()
    runtime_ms = (t1_ns - t0_ns) // 1000000
    ast_floats = count_ast_floats(os.path.abspath(__file__))

    verdict = "PASS" if (len(discrepancies) == 0 and ast_floats == 0 and rpf_caught == 5) else "FAIL"

    out = {
        "card": "A2-WHOLE-CENSUS-E8-TWO-REGISTER",
        "role": "Cold-Room Zero-Trust Referee",
        "blind": "0 of 19",
        "verdict": verdict,
        "discrepancies_count": len(discrepancies),
        "discrepancies": discrepancies,
        "runtime_ms": runtime_ms,
        "ast_floats": ast_floats,
        "json_floats": 0,
        "producer_integrity_and_control": integrity,
        "live_snappy_crosscheck": snappy_check,
        "Q1_referee": q1,
        "Q2_referee": {
            "d5_surj_manifolds": q2["d5_surj_manifolds"],
            "bd5_surj_manifolds": q2["bd5_surj_manifolds"],
            "d5_to_bd5_obstructed_count": q2["d5_to_bd5_obstructed_count"],
            "obstructed_all_have_even_H1_torsion": q2["obstructed_all_have_even_H1_torsion"],
            "hper_bucket_counts": q2["hper_bucket_counts"],
            "s_bd5_c4_total": q2["s_bd5_c4_total"],
            "s_bd5_c4_2gen": q2["s_bd5_c4_2gen"],
            "s_bd5_c4_3gen": q2["s_bd5_c4_3gen"],
            "s_bd5_c4_3gen_names": q2["s_bd5_c4_3gen_names"],
        },
        "Q3_referee": {
            "bd5_all_2gen_checked_fricke": len(q2["bd5_all_2gen_names"]),
            "bd5_non_c4_2gen_with_sl2_f25_spin": len(non_c4_sl2_spin),
            "bd5_non_c4_2gen_with_sl2_f25_any": len(non_c4_sl2_any),
            "bd5_non_c4_2gen_with_sl2_f25_names": non_c4_sl2_spin,
            "s_e8_lock_128_count": len(lock128_names),
            "s_e8_lock_128_names": lock128_names,
            "s_e8_lock_248_count": len(lock248_names),
            "s_e8_lock_248_names": lock248_names,
            "s_e8_cohom_obstructed_120_count": len(cohom120_names),
            "s_e8_cohom_obstructed_120_names": cohom120_names,
            "concrete_248_evals_checked": concrete_248_evals_checked,
            "s_bd5_c4_3gen_gluing_checked": len(three_gen_gluing),
            "s_bd5_c4_3gen_with_gluing_F25_strict": three_gen_strict_names,
            "sample40_gluing_checked": len(sample40_names),
            "sample40_gluing_strict_f25_count": sample40_strict_count,
            "sample40_gluing_f5_count": sample40_f5_count,
            "s758_check": {
                "sl2_f25_full2d_spin_hits": lock_details["s758"]["sl2_f25_full2d_spin_hits"],
                "gluing_f25_strict": lock_details["s758"]["gluing_f25_strict"],
                "gluing_f5": lock_details["s758"]["gluing_f5"],
                "exact_15600_verified": lock_details["s758"]["exact_15600_verified"],
            },
            "m003_check": {
                "d5_surj": q2["per_manifold"]["m003"]["d5_surj"],
                "bd5_surj": q2["per_manifold"]["m003"]["bd5_surj"],
                "sl2_f25_full2d_any": sl2_m003["full2d_any"],
                "sl2_f25_full2d_spin": sl2_m003["full2d_spin"],
                "gluing_f25_strict": m003_gluing_strict,
                "two_T_orbits": m003_2t_orb,
                "two_T_raw": m003_2t_raw,
                "exact_15600_verified": sl2_m003["exact_15600_verified"],
            },
            "m000_check": {
                "d5_surj": q2["per_manifold"]["m000"]["d5_surj"],
                "bd5_surj": q2["per_manifold"]["m000"]["bd5_surj"],
                "total_irred_sl2_f25_hits": sl2_m000["total_irred_hits"],
                "sl2_f25_surj_hits": sl2_m000["sl2_f25_surj_hits"],
                "sl2_f25_nonorient_parabolic_hits": sl2_m000["sl2_f25_nonorient_parabolic_hits"],
                "two_T_orbits": m000_2t_orb,
                "two_T_raw": m000_2t_raw,
            },
        },
        "Q4_referee": {
            "lock_128_by_tet": dict(sorted(lock128_by_tet.items())),
            "lock_248_by_tet": dict(sorted(lock248_by_tet.items())),
            "lock_128_with_2T_count": len(lock128_with_2t),
            "lock_248_with_2T_count": len(lock248_with_2t),
            "lock_248_with_2T_names": lock248_with_2t,
            "lock_248_H1_Z_count": len(lock248_h1z),
            "lock_248_H1_Z_names": lock248_h1z,
            "lock_248_H1_Z_and_2T_count": len(lock248_h1z_2t),
            "lock_248_H1_Z_and_2T_names": lock248_h1z_2t,
            "lock_248_2T_eq_2_count": len(lock248_2t_eq_2),
            "lock_248_2T_eq_2_names": lock248_2t_eq_2,
        },
        "referee_planted_fault_controls": rpf_controls,
        "rpf_caught": rpf_caught,
    }

    j_floats = count_json_floats(out)
    out["json_floats"] = j_floats
    assert j_floats == 0
    assert ast_floats == 0

    with open(REFEREE_OUT_PATH, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, sort_keys=True)
        fh.write("\n")

    print("VERDICT:", verdict)
    print("DISCREPANCIES:", len(discrepancies))
    print("RUNTIME_MS:", runtime_ms)
    print("RPF_CAUGHT:", rpf_caught, "/ 5")
    print("AST_FLOATS:", ast_floats, "JSON_FLOATS:", j_floats)
    sys.exit(0 if verdict == "PASS" else 1)


if __name__ == "__main__":
    main()
