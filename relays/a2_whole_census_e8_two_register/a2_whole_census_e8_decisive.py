#!/usr/bin/env python3
"""Card A2-WHOLE-CENSUS-E8-TWO-REGISTER — Whole-Instrument Coupled E_8 Two-Register
Theorem Across All 1,199 Orientable 1-Cusped Hyperbolic Manifolds (<= 6 Tetrahedra) + m000.

Seat code: fam3-v1-high-03 (agy-002/verify).
Strictly blind (0 of 19), zero trial arcs, standard library only, ZERO AST/JSON floats.
"""
import ast
import itertools
import json
import pathlib
import sys
from collections import Counter, deque

HERE = pathlib.Path(__file__).resolve().parent
DATA_JSON = HERE / "a2_census_1200_presentations_and_gluing.json"
OUT_JSON = HERE / "a2_whole_census_e8_out.json"


# ============================================================================
# 1. Exact F_25 = F_5[d]/(d^2 - 2) tables (idx = 5*a + b for a + b*d, a,b in 0..4)
# ============================================================================
ADD = [[0] * 25 for _ in range(25)]
SUB = [[0] * 25 for _ in range(25)]
MUL = [[0] * 25 for _ in range(25)]
NEG = [0] * 25
INV = [0] * 25
SQRT = [-1] * 25
OMZ = [0] * 25          # 1 - z
POW24 = [[0] * 24 for _ in range(25)]
TR5 = [0] * 25          # Tr_{F_25/F_5}(a + b d) = 2 a mod 5

for _i in range(25):
    _a, _b = divmod(_i, 5)
    NEG[_i] = ((-_a) % 5) * 5 + ((-_b) % 5)
    TR5[_i] = (2 * _a) % 5
    for _j in range(25):
        _c, _e = divmod(_j, 5)
        ADD[_i][_j] = ((_a + _c) % 5) * 5 + ((_b + _e) % 5)
        SUB[_i][_j] = ((_a - _c) % 5) * 5 + ((_b - _e) % 5)
        MUL[_i][_j] = ((_a * _c + 2 * _b * _e) % 5) * 5 + ((_a * _e + _b * _c) % 5)

F0, F1, F2, FM2, F4 = 0, 5, 10, 15, 20
INV2 = 15  # 3 in F_5 -> 3*2 = 6 == 1 mod 5
for _i in range(1, 25):
    for _j in range(1, 25):
        if MUL[_i][_j] == F1:
            INV[_i] = _j
for _i in range(25):
    SQRT[MUL[_i][_i]] = _i
    OMZ[_i] = SUB[F1][_i]
for _z in range(1, 25):
    _cur = F1
    for _e in range(24):
        POW24[_z][_e] = _cur
        _cur = MUL[_cur][_z]

# Squares in F_25^* (12 elements)
F25_SQUARES = {MUL[x][x] for x in range(1, 25)}
assert len(F25_SQUARES) == 12


# ============================================================================
# 2. Exact D_5 (order 10) and BD_5 (order 20) multiplication tables
#    BD_5 element idx = 4*a + k (a in 0..4, k in 0..3) representing r^a j^k
#    D_5  element idx = 2*a + e (a in 0..4, e in 0..1) representing r^a s^e
# ============================================================================
BD_MUL = [[0] * 20 for _ in range(20)]
BD_INV = [0] * 20
BD_ORD = [0] * 20
for _x in range(20):
    _a, _k = divmod(_x, 4)
    _sgn = 1 if (_k % 2 == 0) else -1
    BD_INV[_x] = (((-_sgn * _a) % 5) * 4) + ((-_k) % 4)
    for _y in range(20):
        _b, _l = divmod(_y, 4)
        BD_MUL[_x][_y] = (((_a + _sgn * _b) % 5) * 4) + ((_k + _l) % 4)

for _x in range(20):
    _c = _x
    _o = 1
    while _c != 0:
        _c = BD_MUL[_c][_x]
        _o += 1
    BD_ORD[_x] = _o

# Conjugacy class representatives and sizes in BD_5 (sum = 20)
BD_CONJ_REPS = []
_seen_c = set()
for _x in range(20):
    if _x in _seen_c:
        continue
    _cls = {BD_MUL[BD_MUL[_g][_x]][BD_INV[_g]] for _g in range(20)}
    BD_CONJ_REPS.append((_x, len(_cls)))
    _seen_c.update(_cls)
assert sum(sz for _, sz in BD_CONJ_REPS) == 20 and len(BD_CONJ_REPS) == 8

D5_MUL = [[0] * 10 for _ in range(10)]
D5_INV = [0] * 10
for _x in range(10):
    _a, _e = divmod(_x, 2)
    _sgn = 1 if _e == 0 else -1
    D5_INV[_x] = (((-_sgn * _a) % 5) * 2) + _e
    for _y in range(10):
        _b, _f = divmod(_y, 2)
        D5_MUL[_x][_y] = (((_a + _sgn * _b) % 5) * 2) + ((_e + _f) % 2)

D5_CONJ_REPS = []
_seen_d = set()
for _x in range(10):
    if _x in _seen_d:
        continue
    _cls = {D5_MUL[D5_MUL[_g][_x]][D5_INV[_g]] for _g in range(10)}
    D5_CONJ_REPS.append((_x, len(_cls)))
    _seen_d.update(_cls)
assert sum(sz for _, sz in D5_CONJ_REPS) == 10 and len(D5_CONJ_REPS) == 4


def bd5_subgroup(gens):
    seen = {0}
    q = deque([0])
    while q:
        u = q.popleft()
        for g in gens:
            for h in (g, BD_INV[g]):
                v = BD_MUL[u][h]
                if v not in seen:
                    seen.add(v)
                    q.append(v)
    return seen


def bd5_abelian_type(h1, h2):
    """Classify subgroup <h1, h2> <= BD_5."""
    sub = bd5_subgroup((h1, h2))
    n = len(sub)
    if n == 1:
        return "C1"
    if n == 2:
        return "C2"
    if n == 4:
        return "C4"
    if n == 5:
        return "C5"
    if n == 10:
        return "C10" if all(BD_MUL[x][y] == BD_MUL[y][x] for x in sub for y in sub) else "D5_nonab"
    if n == 20:
        return "BD5_nonab"
    return f"ord_{n}"


# ============================================================================
# 3. Module Q1: Universal E_8 (Ss(16)) Peripheral Kernel Classification Theorem
# ============================================================================
# 12 pairs {+-x} in F_25^*
WEIL_PAIRS = []
_seen_w = set()
for _x in range(1, 25):
    _p = min(_x, NEG[_x])
    if _p not in _seen_w:
        _seen_w.add(_p)
        WEIL_PAIRS.append(_p)
assert len(WEIL_PAIRS) == 12


def e8_peripheral_kernel(v1, v2, s1, s2, h1, h2):
    """Exact Z/20Z phase enumeration across ALL 248 = 120 + 128 adjoint weights of E_8
    for commuting geometric peripheral holonomy (s1 U(v1), s2 U(v2)) in SL(2, F_25)
    and commuting sheet elements (h1, h2) in BD_5 (h1 h2 == h2 h1).
    Returns exact counts across all 4 torus spin structures (eps1, eps2) in {(0,0),(0,10),(10,0),(10,10)}."""
    assert BD_MUL[h1][h2] == BD_MUL[h2][h1]

    # 13-dim even Weil module: {0} plus 12 pairs {+-x} with U(v) weight Tr(2 v x^2) mod 5
    w12 = []
    for x in WEIL_PAIRS:
        x2 = MUL[x][x]
        wm = TR5[MUL[v1][MUL[F2][x2]]]
        wl = TR5[MUL[v2][MUL[F2][x2]]]
        w12.append((wm, wl))

    # Pair opposite weights into 6 real 2-planes of SO(13)
    rem = list(w12)
    planes6 = []
    while rem:
        w = rem.pop(0)
        nw = ((-w[0]) % 5, (-w[1]) % 5)
        rem.remove(nw)
        planes6.append(w)
    assert len(planes6) == 6

    # Unique order-5 Spin(13) lift: half-weight = 4 * (3*w mod 5) mod 20
    half_planes = [((4 * ((3 * wm) % 5)) % 20, (4 * ((3 * wl) % 5)) % 20) for wm, wl in planes6]
    w_64 = []
    for eps in itertools.product((1, -1), repeat=6):
        sm = sum(e * hp[0] for e, hp in zip(eps, half_planes)) % 20
        sl = sum(e * hp[1] for e, hp in zip(eps, half_planes)) % 20
        w_64.append((sm, sl))

    # Simultaneous eigenvalues of commuting (h1, h2) in BD_5 on 2 (SU(2)) and 3 (SO(3)):
    # Central sign (s1, s2) in {+1, -1} adds (0 or 10) mod 20 to the 2-dim spinor (and 0 to 13 and 3).
    cs1 = 0 if s1 == 1 else 10
    cs2 = 0 if s2 == 1 else 10
    a1, k1 = divmod(h1, 4)
    a2, k2 = divmod(h2, 4)
    if (k1 % 2 == 0) and (k2 % 2 == 0):
        # Both in C_10 = <r, -1>: r^a j^{2e} has SU(2) eig (4a + 10e, -4a + 10e) and SO(3) eig (0, 8a, -8a)
        e1 = k1 // 2
        e2 = k2 // 2
        w_2 = [
            ((4 * a1 + 10 * e1 + cs1) % 20, (4 * a2 + 10 * e2 + cs2) % 20),
            ((-4 * a1 + 10 * e1 + cs1) % 20, (-4 * a2 + 10 * e2 + cs2) % 20),
        ]
        w_3 = [
            (0, 0),
            ((8 * a1) % 20, (8 * a2) % 20),
            ((-8 * a1) % 20, (-8 * a2) % 20),
        ]
    else:
        # Commuting pair with an order-4 element lies in C_4 = <r^a j>:
        # (r^a j)^k has SU(2) eig (5k, 15k) and SO(3) eig (0, 10k, 10k)
        # Note: if k1 is odd, h1 = (a1, k1); h2 = h1^p for unique p in {0,1,2,3}
        gen = h1 if (k1 % 2 == 1) else h2
        pows = [0, gen, BD_MUL[gen][gen], BD_INV[gen]]
        p1 = pows.index(h1)
        p2 = pows.index(h2)
        w_2 = [
            ((5 * p1 + cs1) % 20, (5 * p2 + cs2) % 20),
            ((15 * p1 + cs1) % 20, (15 * p2 + cs2) % 20),
        ]
        w_3 = [
            (0, 0),
            ((10 * p1) % 20, (10 * p2) % 20),
            ((10 * p1) % 20, (10 * p2) % 20),
        ]

    w_13 = [(0, 0)] + [(4 * wm % 20, 4 * wl % 20) for wm, wl in w12]
    w_16 = w_13 + w_3
    w_120 = [((w_16[i][0] + w_16[j][0]) % 20, (w_16[i][1] + w_16[j][1]) % 20)
             for i in range(16) for j in range(i + 1, 16)]
    w_128 = [((a[0] + b[0]) % 20, (a[1] + b[1]) % 20) for a in w_64 for b in w_2]

    c120 = Counter(w_120)
    c128 = Counter(w_128)
    spins = [(0, 0), (0, 10), (10, 0), (10, 10)]
    k120_by_spin = {f"{sp[0]}_{sp[1]}": c120[sp] for sp in spins}
    k128_by_spin = {f"{sp[0]}_{sp[1]}": c128[sp] for sp in spins}
    # Bounding / non-trivial spin structures matching the Z = -I sign on at least one curve
    nontriv_spins = [(0, 10), (10, 0), (10, 10)]
    # Spin structures where every curve with s_i = -1 has spin eps_i = 10 (the geometric spin sector)
    geo_matching_spins = [sp for sp in spins if (s1 == 1 or sp[0] == 10) and (s2 == 1 or sp[1] == 10)]
    # Exact geometric spin structure matching (cs1, cs2)
    return {
        "k128_total_4spins": sum(c128[sp] for sp in spins),
        "k128_nontriv_3spins": sum(c128[sp] for sp in nontriv_spins),
        "k128_geo_match": sum(c128[sp] for sp in geo_matching_spins),
        "k120_nontriv_3spins": sum(c120[sp] for sp in nontriv_spins),
        "k120_geo_match": sum(c120[sp] for sp in geo_matching_spins),
        "k248_geo_match": sum(c120[sp] + c128[sp] for sp in geo_matching_spins),
        "k120_by_spin": k120_by_spin,
        "k128_by_spin": k128_by_spin,
        "w64_mult_hist": dict(sorted(Counter(Counter(w_64).values()).items())),
    }


def run_module_Q1():
    # 1. Verify across ALL 480 ordered F_5-bases (v1, v2) of F_25 that w_64 mult histogram is ALWAYS {2:12, 3:12, 4:1}
    bases_checked = 0
    bases_ok = True
    for v1 in range(1, 25):
        a1, b1 = divmod(v1, 5)
        for v2 in range(1, 25):
            a2, b2 = divmod(v2, 5)
            if (a1 * b2 - a2 * b1) % 5 == 0:
                continue  # F_5-linearly dependent
            bases_checked += 1
            # Compute w_64 directly
            w12 = [(TR5[MUL[v1][MUL[F2][MUL[x][x]]]], TR5[MUL[v2][MUL[F2][MUL[x][x]]]]) for x in WEIL_PAIRS]
            rem = list(w12)
            p6 = []
            while rem:
                w = rem.pop(0)
                rem.remove(((-w[0]) % 5, (-w[1]) % 5))
                p6.append(w)
            hp = [((4 * ((3 * wm) % 5)) % 20, (4 * ((3 * wl) % 5)) % 20) for wm, wl in p6]
            c64 = Counter()
            for eps in itertools.product((1, -1), repeat=6):
                c64[(sum(e * h[0] for e, h in zip(eps, hp)) % 20,
                     sum(e * h[1] for e, h in zip(eps, hp)) % 20)] += 1
            hist = Counter(c64.values())
            if dict(hist) != {2: 12, 3: 12, 4: 1}:
                bases_ok = False
    assert bases_checked == 480

    # 2. Check ALL commuting pairs (h1, h2) in BD_5 x all 3 non-trivial central signs (s1, s2)
    comm_pairs = [(h1, h2) for h1 in range(20) for h2 in range(20) if BD_MUL[h1][h2] == BD_MUL[h2][h1]]
    by_Hper_k128 = {}
    by_Hper_k248_geo = {}
    c4_always_kills_128 = True
    non_c4_never_kills_128 = True
    c4_j_off_Z_kills_248 = True
    c4_j_on_Z_gives_120_4 = True

    v1_ref, v2_ref = F1, 3  # 1 and 3d = -2d
    for h1, h2 in comm_pairs:
        htype = bd5_abelian_type(h1, h2)
        for s1, s2 in ((1, -1), (-1, 1), (-1, -1)):
            res = e8_peripheral_kernel(v1_ref, v2_ref, s1, s2, h1, h2)
            k128 = res["k128_total_4spins"]
            k248g = res["k248_geo_match"]
            by_Hper_k128.setdefault(htype, set()).add(k128)
            by_Hper_k248_geo.setdefault(htype, set()).add(k248g)
            if htype == "C4":
                if k128 != 0:
                    c4_always_kills_128 = False
                # Does any curve with s_i == -1 carry an order-4 element?
                j_on_Z = ((s1 == -1 and BD_ORD[h1] == 4) or (s2 == -1 and BD_ORD[h2] == 4))
                if not j_on_Z:
                    if res["k248_geo_match"] != 0:
                        c4_j_off_Z_kills_248 = False
                else:
                    if res["k120_geo_match"] == 0:
                        c4_j_on_Z_gives_120_4 = False
            else:
                if k128 == 0:
                    non_c4_never_kills_128 = False

    # 3. Also check degenerate 1D F_5 cusp lattice control (v1 = 1, v2 = 2 -> F_5-dependent):
    deg_geo = e8_peripheral_kernel(F1, F2, 1, -1, 0, 0)
    deg_c4 = e8_peripheral_kernel(F1, F2, 1, -1, 1, 0)  # h1 = j, h2 = 1

    ok = (
        bases_checked == 480
        and bases_ok
        and c4_always_kills_128
        and non_c4_never_kills_128
        and c4_j_off_Z_kills_248
        and c4_j_on_Z_gives_120_4
        and by_Hper_k128["C1"] == {8}
        and by_Hper_k128["C2"] == {8}
        and by_Hper_k128["C4"] == {0}
        and by_Hper_k128["C5"] == {4, 6}
        and by_Hper_k128["C10"] == {4, 6}
        and deg_geo["k128_total_4spins"] > 8
        and deg_c4["k128_total_4spins"] == 0
    )
    return {
        "ok": ok,
        "bases_checked": bases_checked,
        "bases_w64_hist_4_3_2_all_ok": bases_ok,
        "commuting_pairs_in_BD5": len(comm_pairs),
        "k128_total_by_Hper": {k: sorted(v) for k, v in sorted(by_Hper_k128.items())},
        "k248_geo_match_by_Hper": {k: sorted(v) for k, v in sorted(by_Hper_k248_geo.items())},
        "c4_iff_k128_zero": c4_always_kills_128 and non_c4_never_kills_128,
        "c4_j_off_Z_kills_full_248_geo_match": c4_j_off_Z_kills_248,
        "c4_j_on_Z_activates_120_modes": c4_j_on_Z_gives_120_4,
        "degenerate_1D_F5_geo_k128": deg_geo["k128_total_4spins"],
        "degenerate_1D_F5_C4_k128": deg_c4["k128_total_4spins"],
    }


# ============================================================================
# 4. Module Q2: Exhaustive D_5 & BD_5 Census Across All 1,199 Orientable + m000
# ============================================================================
def compile_word(word, gens):
    gidx = {g: i for i, g in enumerate(gens)}
    out = []
    for ch in word:
        if ch.islower():
            out.append((gidx[ch], False))
        else:
            out.append((gidx[ch.lower()], True))
    return tuple(out)


def eval_table_word(comp, vals, inv_tab, mul_tab):
    cur = 0
    for idx, is_inv in comp:
        g = vals[idx]
        cur = mul_tab[cur][inv_tab[g] if is_inv else g]
    return cur


def analyze_d5_bd5_manifold(m):
    gens = m["gens"]
    ng = len(gens)
    rels_c = [compile_word(r, gens) for r in m["rels"]]
    m_c = compile_word(m["periph"][0], gens)
    l_c = compile_word(m["periph"][1], gens)

    # 1. Count exact D_5 surjections (using conjugacy classes on gen 0 for ng == 3)
    d5_surj = 0
    if ng == 2:
        for g0 in range(10):
            for g1 in range(10):
                # Quick surjectivity necessary check: need at least one odd (reflection) and not all same reflection
                if (g0 % 2 == 0) and (g1 % 2 == 0):
                    continue
                if g0 == g1 or g0 == 0 or g1 == 0:
                    continue
                vals = (g0, g1)
                if all(eval_table_word(rc, vals, D5_INV, D5_MUL) == 0 for rc in rels_c):
                    # Verify subgroup size == 10
                    seen = {0}
                    q = deque([0])
                    while q:
                        u = q.popleft()
                        for g in vals:
                            for h in (g, D5_INV[g]):
                                v = D5_MUL[u][h]
                                if v not in seen:
                                    seen.add(v)
                                    q.append(v)
                    if len(seen) == 10:
                        d5_surj += 1
    else:
        assert ng == 3
        for g0, mult in D5_CONJ_REPS:
            for g1 in range(10):
                for g2 in range(10):
                    if (g0 % 2 == 0) and (g1 % 2 == 0) and (g2 % 2 == 0):
                        continue
                    vals = (g0, g1, g2)
                    if all(eval_table_word(rc, vals, D5_INV, D5_MUL) == 0 for rc in rels_c):
                        seen = {0}
                        q = deque([0])
                        while q:
                            u = q.popleft()
                            for g in vals:
                                for h in (g, D5_INV[g]):
                                    v = D5_MUL[u][h]
                                    if v not in seen:
                                        seen.add(v)
                                        q.append(v)
                        if len(seen) == 10:
                            d5_surj += mult

    # 2. Count exact BD_5 surjections & classify peripheral subgroup H_per and (ord(m), ord(l))
    bd5_surj = 0
    hper_types = set()
    c4_periph_ord_pairs = set()
    c4_lifts = []  # store representative (hm, hl) pairs for C_4 lifts

    if d5_surj > 0:
        if ng == 2:
            for g0 in range(20):
                for g1 in range(20):
                    if ((g0 & 1) == 0) and ((g1 & 1) == 0):
                        continue
                    vals = (g0, g1)
                    if all(eval_table_word(rc, vals, BD_INV, BD_MUL) == 0 for rc in rels_c):
                        if len(bd5_subgroup(vals)) == 20:
                            bd5_surj += 1
                            hm = eval_table_word(m_c, vals, BD_INV, BD_MUL)
                            hl = eval_table_word(l_c, vals, BD_INV, BD_MUL)
                            ht = bd5_abelian_type(hm, hl)
                            hper_types.add(ht)
                            if ht == "C4":
                                c4_periph_ord_pairs.add((BD_ORD[hm], BD_ORD[hl]))
                                if len(c4_lifts) < 8:
                                    c4_lifts.append((hm, hl))
        else:
            for g0, mult in BD_CONJ_REPS:
                for g1 in range(20):
                    for g2 in range(20):
                        if ((g0 & 1) == 0) and ((g1 & 1) == 0) and ((g2 & 1) == 0):
                            continue
                        vals = (g0, g1, g2)
                        if all(eval_table_word(rc, vals, BD_INV, BD_MUL) == 0 for rc in rels_c):
                            if len(bd5_subgroup(vals)) == 20:
                                bd5_surj += mult
                                hm = eval_table_word(m_c, vals, BD_INV, BD_MUL)
                                hl = eval_table_word(l_c, vals, BD_INV, BD_MUL)
                                ht = bd5_abelian_type(hm, hl)
                                hper_types.add(ht)
                                if ht == "C4":
                                    c4_periph_ord_pairs.add((BD_ORD[hm], BD_ORD[hl]))
                                    if len(c4_lifts) < 8:
                                        c4_lifts.append((hm, hl))

    return {
        "d5_surj": d5_surj,
        "bd5_surj": bd5_surj,
        "hper_types": sorted(hper_types),
        "c4_ord_pairs": sorted(c4_periph_ord_pairs),
        "c4_sample_hm_hl": c4_lifts,
    }


# ============================================================================
# 5. Module Q3: Exact Thurston Gluing over F_25\{0,1} + Exact Fricke SL(2, F_25)
# ============================================================================
def solve_gluing_f25(gluing_rect, num_tet):
    """Exact backtracking solver over F_25\{0,1} for Thurston rectangular gluing equations
    prod_j z_j^{a_j} (1 - z_j)^{b_j} = sign (sign in {1, -1}).
    Returns (has_F5_sol, has_F25_strict_sol)."""
    if not gluing_rect or num_tet == 0:
        return (False, False)
    # Pre-parse each equation into list of (var, a_mod24, b_mod24) + rhs in F_25
    eqs = []
    for a_row, b_row, sgn in gluing_rect:
        terms = []
        for j in range(num_tet):
            aj = a_row[j] % 24
            bj = b_row[j] % 24
            if aj != 0 or bj != 0:
                terms.append((j, aj, bj))
        rhs = F1 if sgn == 1 else NEG[F1]
        if terms:
            eqs.append((terms, rhs))

    domain_f5 = [10, 15, 20]  # 2, 3, 4 in F_5 \ {0, 1}
    domain_f25 = [z for z in range(1, 25) if z != F1]  # 23 values

    # Precompute term values for z in 0..24: z^a * (1-z)^b
    def run_search(dom, require_outside_f5):
        assign = [-1] * num_tet
        found = [False]

        def bt(depth):
            if found[0]:
                return
            if depth == num_tet:
                if require_outside_f5 and all((v % 5 == 0) for v in assign):
                    return
                # Verify all equations
                for terms, rhs in eqs:
                    prod = F1
                    for j, aj, bj in terms:
                        zj = assign[j]
                        if aj:
                            prod = MUL[prod][POW24[zj][aj]]
                        if bj:
                            prod = MUL[prod][POW24[OMZ[zj]][bj]]
                    if prod != rhs:
                        return
                found[0] = True
                return

            # Check already-complete equations and pick variable in smallest unassigned-count eq (MRV)
            best_var = -1
            best_deg = 999
            best_eq_info = None
            for terms, rhs in eqs:
                un = []
                prod = F1
                for j, aj, bj in terms:
                    zj = assign[j]
                    if zj == -1:
                        un.append((j, aj, bj))
                    else:
                        if aj:
                            prod = MUL[prod][POW24[zj][aj]]
                        if bj:
                            prod = MUL[prod][POW24[OMZ[zj]][bj]]
                lu = len(un)
                if lu == 0:
                    if prod != rhs:
                        return  # contradiction!
                elif lu < best_deg:
                    best_deg = lu
                    best_var = un[0][0]
                    best_eq_info = (un[0], prod, rhs) if lu == 1 else None

            if best_var == -1:
                best_var = assign.index(-1)

            if best_eq_info is not None:
                (vj, aj, bj), prod, rhs = best_eq_info
                need = MUL[rhs][INV[prod]]
                for z in dom:
                    val = F1
                    if aj:
                        val = MUL[val][POW24[z][aj]]
                    if bj:
                        val = MUL[val][POW24[OMZ[z]][bj]]
                    if val == need:
                        assign[vj] = z
                        bt(depth + 1)
                        assign[vj] = -1
                        if found[0]:
                            return
            else:
                for z in dom:
                    assign[best_var] = z
                    bt(depth + 1)
                    assign[best_var] = -1
                    if found[0]:
                        return

        bt(0)
        return found[0]

    has_f5 = run_search(domain_f5, False)
    has_f25_strict = run_search(domain_f25, True)
    return (has_f5, has_f25_strict)


def build_all_irred_sl2_f25():
    """Precompute ALL 14,999 irreducible Fricke conjugacy classes (A, B, Ai, Bi) in SL(2, F_25)."""
    out = []
    for x in range(25):
        xx = MUL[x][x]
        for y in range(25):
            yy = MUL[y][y]
            xy = MUL[x][y]
            for z in range(25):
                D = SUB[ADD[ADD[xx][yy]][MUL[z][z]]][ADD[MUL[xy][z]][F4]]
                if D == F0:
                    continue
                for p in range(25):
                    ymp = SUB[y][p]
                    w = SUB[z][MUL[x][ymp]]
                    u = SUB[MUL[p][ymp]][F1]
                    s = SQRT[ADD[MUL[w][w]][MUL[F4][u]]]
                    if s != -1:
                        r = MUL[ADD[NEG[w]][s]][INV2]
                        q = MUL[ADD[w][s]][INV2]
                        A = (F0, NEG[F1], F1, x)
                        B = (p, q, r, ymp)
                        Ai = (x, F1, NEG[F1], F0)
                        Bi = (ymp, NEG[q], NEG[r], p)
                        out.append((A, B, Ai, Bi))
                        break
    return out


def sl2_mul(M, N):
    return (
        ADD[MUL[M[0]][N[0]]][MUL[M[1]][N[2]]],
        ADD[MUL[M[0]][N[1]]][MUL[M[1]][N[3]]],
        ADD[MUL[M[2]][N[0]]][MUL[M[3]][N[2]]],
        ADD[MUL[M[2]][N[1]]][MUL[M[3]][N[3]]],
    )


def sl2_eval_2gen(comp, A, B, Ai, Bi):
    c0, c1, c2, c3 = F1, F0, F0, F1
    for idx, is_inv in comp:
        if idx == 0:
            g = Ai if is_inv else A
        else:
            g = Bi if is_inv else B
        g0, g1, g2, g3 = g
        c0, c1, c2, c3 = (
            ADD[MUL[c0][g0]][MUL[c1][g2]],
            ADD[MUL[c0][g1]][MUL[c1][g3]],
            ADD[MUL[c2][g0]][MUL[c3][g2]],
            ADD[MUL[c2][g1]][MUL[c3][g3]],
        )
    return (c0, c1, c2, c3)


def sl2_subgroup_exceeds_240(A, B, Ai, Bi):
    """Exact BFS proving |<A, B>| > 240 in SL(2, F_25); combined with irreducibility (D != 0)
    and Dickson's maximal subgroup classification of PSL(2, 25), > 240 proves <A, B> == SL(2, F_25) (15,600)."""
    I2 = (F1, F0, F0, F1)
    seen = {I2}
    q = deque([I2])
    gens = (A, B, Ai, Bi)
    while q:
        u = q.popleft()
        for g in gens:
            v = sl2_mul(u, g)
            if v not in seen:
                seen.add(v)
                if len(seen) > 240:
                    return True
                q.append(v)
    return False


def analyze_sl2_f25_2gen(m, irred_ab):
    """Exhaustive Fricke SL(2, F_25) cusp-parabolic search across all 14,999 irreducible classes."""
    gens = m["gens"]
    assert len(gens) == 2
    rels_c = [compile_word(r, gens) for r in m["rels"]]
    m_c = compile_word(m["periph"][0], gens)
    l_c = compile_word(m["periph"][1], gens)
    I2 = (F1, F0, F0, F1)
    MI2 = (NEG[F1], F0, F0, NEG[F1])
    orient = m["orientable"]

    full_2d_hits = []
    deg_1d_hits = []
    nonorient_hits = []

    for A, B, Ai, Bi in irred_ab:
        ok_r = True
        for rc in rels_c:
            if sl2_eval_2gen(rc, A, B, Ai, Bi) != I2:
                ok_r = False
                break
        if not ok_r:
            continue
        M = sl2_eval_2gen(m_c, A, B, Ai, Bi)
        L = sl2_eval_2gen(l_c, A, B, Ai, Bi)
        trM = ADD[M[0]][M[3]]
        trL = ADD[L[0]][L[3]]
        if not orient:
            # Non-orientable Klein bottle cusp: check if at least one peripheral curve is non-central parabolic
            m_par = (trM in (F2, FM2)) and (M != I2) and (M != MI2)
            l_par = (trL in (F2, FM2)) and (L != I2) and (L != MI2)
            if m_par or l_par:
                surj = sl2_subgroup_exceeds_240(A, B, Ai, Bi)
                nonorient_hits.append({
                    "m_par": m_par, "l_par": l_par,
                    "trM": list(divmod(trM, 5)), "trL": list(divmod(trL, 5)),
                    "surj_SL2_F25": surj,
                })
            continue

        # Orientable torus cusp: require both M and L parabolic, with at least one non-central
        if trM not in (F2, FM2) or trL not in (F2, FM2):
            continue
        if (M == I2 or M == MI2) and (L == I2 or L == MI2):
            continue
        sm = 1 if trM == F2 else -1
        sl = 1 if trL == F2 else -1
        # Extract nilpotent parts N_M = sm*M - I, N_L = sl*L - I
        nm = [SUB[M[0] if sm == 1 else NEG[M[0]]][F1], M[1] if sm == 1 else NEG[M[1]],
              M[2] if sm == 1 else NEG[M[2]], SUB[M[3] if sm == 1 else NEG[M[3]]][F1]]
        nl = [SUB[L[0] if sl == 1 else NEG[L[0]]][F1], L[1] if sl == 1 else NEG[L[1]],
              L[2] if sl == 1 else NEG[L[2]], SUB[L[3] if sl == 1 else NEG[L[3]]][F1]]
        m_nonzero = any(x != F0 for x in nm)
        l_nonzero = any(x != F0 for x in nl)
        if not m_nonzero or not l_nonzero:
            # One peripheral curve is central (+-I), so cusp lattice is at most 1D!
            deg_1d_hits.append((sm, sl, "central_one"))
            continue
        k0 = next(k for k in range(4) if nm[k] != F0)
        tau = MUL[nl[k0]][INV[nm[k0]]]
        if not all(nl[k] == MUL[tau][nm[k]] for k in range(4)):
            continue
        if (tau % 5) == 0:
            deg_1d_hits.append((sm, sl, divmod(tau, 5)))
        else:
            # Full 2D cusp lattice in F_25 \ F_5 -> guaranteed surjective SL(2, F_25); also verify >240!
            surj = sl2_subgroup_exceeds_240(A, B, Ai, Bi)
            assert surj
            full_2d_hits.append((sm, sl, tau))

    return {
        "full_2d_hits": full_2d_hits,
        "deg_1d_count": len(deg_1d_hits),
        "nonorient_hits": nonorient_hits,
    }


# ============================================================================
# 6. Module Q4: Exact 2T = SL(2, F_3) Surjections (order 24)
# ============================================================================
def build_sl2_f3():
    elems = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    if (a * d - b * c) % 3 == 1:
                        elems.append((a, b, c, d))
    assert len(elems) == 24
    idx = {e: i for i, e in enumerate(elems)}
    id_i = idx[(1, 0, 0, 1)]
    # Swap id to index 0
    if id_i != 0:
        elems[0], elems[id_i] = elems[id_i], elems[0]
        idx = {e: i for i, e in enumerate(elems)}
    mul = [[0] * 24 for _ in range(24)]
    inv = [0] * 24
    for i, (a, b, c, d) in enumerate(elems):
        inv[i] = idx[(d, (-b) % 3, (-c) % 3, a)]
        for j, (e, f, g, h) in enumerate(elems):
            mul[i][j] = idx[((a * e + b * g) % 3, (a * f + b * h) % 3,
                             (c * e + d * g) % 3, (c * f + d * h) % 3)]
    # Conjugacy classes of 2T
    conj = []
    seen = set()
    for x in range(24):
        if x in seen:
            continue
        cls = {mul[mul[g][x]][inv[g]] for g in range(24)}
        conj.append((x, len(cls)))
        seen.update(cls)
    return mul, inv, conj


T2_MUL, T2_INV, T2_CONJ = build_sl2_f3()


def count_2t_surj_orbits(m):
    """Exact number of Aut(2T)-orbits (|Aut(2T)| = 24) of surjective homs pi_1(M) ->> 2T = SL(2, F_3)."""
    gens = m["gens"]
    ng = len(gens)
    rels_c = [compile_word(r, gens) for r in m["rels"]]
    cnt = 0
    if ng == 2:
        for g0 in range(24):
            for g1 in range(24):
                vals = (g0, g1)
                if all(eval_table_word(rc, vals, T2_INV, T2_MUL) == 0 for rc in rels_c):
                    seen = {0}
                    q = deque([0])
                    while q:
                        u = q.popleft()
                        for g in vals:
                            for h in (g, T2_INV[g]):
                                v = T2_MUL[u][h]
                                if v not in seen:
                                    seen.add(v)
                                    q.append(v)
                    if len(seen) == 24:
                        cnt += 1
    else:
        for g0, mult in T2_CONJ:
            for g1 in range(24):
                for g2 in range(24):
                    vals = (g0, g1, g2)
                    if all(eval_table_word(rc, vals, T2_INV, T2_MUL) == 0 for rc in rels_c):
                        seen = {0}
                        q = deque([0])
                        while q:
                            u = q.popleft()
                            for g in vals:
                                for h in (g, T2_INV[g]):
                                    v = T2_MUL[u][h]
                                    if v not in seen:
                                        seen.add(v)
                                        q.append(v)
                        if len(seen) == 24:
                            cnt += mult
    assert cnt % 24 == 0
    return cnt // 24


# ============================================================================
# 7. Main Driver & Planted Fault Controls (PF1..PF5)
# ============================================================================
def run_all():
    src = pathlib.Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    ast_floats = sum(1 for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, (float, complex)))

    raw = json.loads(DATA_JSON.read_text(encoding="utf-8"))
    manifolds = raw["manifolds"]
    orient_manifolds = [m for m in manifolds if m["orientable"]]
    m000 = next(m for m in manifolds if m["name"] == "m000")
    assert len(orient_manifolds) == 1199

    # Q1: Universal E_8 peripheral kernel classification theorem
    q1 = run_module_Q1()

    # Q2: Exhaustive D_5 & BD_5 census across all 1,199 orientable manifolds + m000
    d5_set = []
    bd5_set = []
    d5_obstructed = []
    hper_bucket_counts = Counter()
    s_bd5_c4 = []
    per_m_q2 = {}

    for m in orient_manifolds:
        r2 = analyze_d5_bd5_manifold(m)
        per_m_q2[m["name"]] = r2
        if r2["d5_surj"] > 0:
            d5_set.append(m["name"])
            if r2["bd5_surj"] == 0:
                d5_obstructed.append(m["name"])
        if r2["bd5_surj"] > 0:
            bd5_set.append(m["name"])
            key = "+".join(r2["hper_types"])
            hper_bucket_counts[key] += 1
            if "C4" in r2["hper_types"]:
                s_bd5_c4.append(m)

    m000_q2 = analyze_d5_bd5_manifold(m000)

    # Verify homological lifting obstruction mechanism on d5_obstructed: every obstructed manifold has even H_1 torsion!
    obstructed_all_have_even_torsion = all(
        any((t % 2 == 0) for t in next(x for x in orient_manifolds if x["name"] == nm)["h1_torsion"])
        for nm in d5_obstructed
    )

    # Q3A: Exact Thurston gluing equations over F_25\{0,1} across ALL 1,199 orientable manifolds
    gluing_f5_cnt = 0
    gluing_f25_strict_cnt = 0
    gluing_f25_strict_set = set()
    gluing_f5_set = set()
    for m in orient_manifolds:
        hf5, hf25 = solve_gluing_f25(m["gluing_rect"], m["num_tet"])
        if hf5:
            gluing_f5_cnt += 1
            gluing_f5_set.add(m["name"])
        if hf25:
            gluing_f25_strict_cnt += 1
            gluing_f25_strict_set.add(m["name"])

    # Q3B: Exact triangulation-independent Fricke SL(2, F_25) search on ALL BD_5-surjective 2-gen manifolds + m003 + m000
    irred_ab = build_all_irred_sl2_f25()
    assert len(irred_ab) == 14999

    s_bd5_c4_2gen = [m for m in s_bd5_c4 if len(m["gens"]) == 2]
    s_bd5_c4_3gen = [m for m in s_bd5_c4 if len(m["gens"]) == 3]
    bd5_all_2gen = [m for m in orient_manifolds if (per_m_q2[m["name"]]["bd5_surj"] > 0 and len(m["gens"]) == 2)]

    # Also ensure m003 is included even if not in BD_5
    m003_obj = next(m for m in orient_manifolds if m["name"] == "m003")
    check_fricke_list = list(bd5_all_2gen)
    if all(x["name"] != "m003" for x in check_fricke_list):
        check_fricke_list.append(m003_obj)

    fricke_res = {}
    for m in check_fricke_list:
        fricke_res[m["name"]] = analyze_sl2_f25_2gen(m, irred_ab)
    m000_fricke = analyze_sl2_f25_2gen(m000, irred_ab)

    # Check every manifold in s_bd5_c4_2gen for coupled E_8 lock:
    # (A) SL(2, F_25) full 2D cusp lattice + (s_m, s_l) != (+1, +1) + BD_5 H_per = C_4 -> ker_128: 8 -> 0
    # (B) Strict full-248 lock: ALSO achieves ker_248_geo_match == 0 (j avoids the Z = -I curve, like m004!)
    s_e8_lock_128 = []
    s_e8_lock_248 = []
    s_e8_lock_details = {}

    for m in s_bd5_c4_2gen:
        nm = m["name"]
        f_hits = fricke_res[nm]["full_2d_hits"]
        # Filter to hits with non-trivial spin sign (s_m, s_l) != (+1, +1)
        spin_hits = [(sm, sl, tau) for (sm, sl, tau) in f_hits if (sm, sl) != (1, 1)]
        if not spin_hits:
            continue
        # Directly plug actual (1, tau, sm, sl) and actual BD_5 C_4 peripheral pairs (hm, hl) into E_8 weight enumerator!
        sample_c4 = per_m_q2[nm]["c4_sample_hm_hl"]
        can_kill_128 = False
        can_kill_248 = False
        for sm, sl, tau in spin_hits:
            geo_chk = e8_peripheral_kernel(F1, tau, sm, sl, 0, 0)
            assert geo_chk["k128_total_4spins"] == 8 and geo_chk["k248_geo_match"] == 8
            for hm, hl in sample_c4:
                j_chk = e8_peripheral_kernel(F1, tau, sm, sl, hm, hl)
                if j_chk["k128_total_4spins"] == 0:
                    can_kill_128 = True
                if j_chk["k248_geo_match"] == 0:
                    can_kill_248 = True
        if can_kill_128:
            s_e8_lock_128.append(nm)
            if can_kill_248:
                s_e8_lock_248.append(nm)
            t2_orbs = count_2t_surj_orbits(m)
            s_e8_lock_details[nm] = {
                "num_tet": m["num_tet"],
                "h1_torsion": m["h1_torsion"],
                "d5_surj": per_m_q2[nm]["d5_surj"],
                "bd5_surj": per_m_q2[nm]["bd5_surj"],
                "c4_ord_pairs": [list(p) for p in per_m_q2[nm]["c4_ord_pairs"]],
                "sl2_f25_full2d_spin_hits": len(spin_hits),
                "gluing_f25_strict": nm in gluing_f25_strict_set,
                "kills_128_to_0": can_kill_128,
                "kills_248_geo_to_0": can_kill_248,
                "two_T_orbits": t2_orbs,
            }

    # Check 3-generator manifolds in s_bd5_c4 against exact Thurston F_25 gluing equations
    s_bd5_c4_3gen_gluing_f25 = [m["name"] for m in s_bd5_c4_3gen if m["name"] in gluing_f25_strict_set]
    # Also check how many of BD_5-surjective 2-gen manifolds have SL(2, F_25) full 2D cusp hits WITHOUT C_4
    bd5_non_c4_2gen_with_sl2_f25 = [
        m["name"] for m in bd5_all_2gen
        if ("C4" not in per_m_q2[m["name"]]["hper_types"])
        and any((sm, sl) != (1, 1) for sm, sl, _ in fricke_res[m["name"]]["full_2d_hits"])
    ]

    # Q4: Cross-tabulation of S_E8_LOCK_128 / S_E8_LOCK_248 with 2T, H_1 = Z, and num_tet
    lock_by_tet = dict(sorted(Counter(s_e8_lock_details[nm]["num_tet"] for nm in s_e8_lock_128).items()))
    lock_248_by_tet = dict(sorted(Counter(s_e8_lock_details[nm]["num_tet"] for nm in s_e8_lock_248).items()))
    lock_with_2t = [nm for nm in s_e8_lock_128 if s_e8_lock_details[nm]["two_T_orbits"] > 0]
    lock_248_with_2t = [nm for nm in s_e8_lock_248 if s_e8_lock_details[nm]["two_T_orbits"] > 0]
    lock_248_h1_Z = [nm for nm in s_e8_lock_248 if s_e8_lock_details[nm]["h1_torsion"] == []]
    lock_248_h1_Z_2t = [nm for nm in lock_248_h1_Z if s_e8_lock_details[nm]["two_T_orbits"] > 0]
    lock_248_2t_eq_2 = [nm for nm in s_e8_lock_248 if s_e8_lock_details[nm]["two_T_orbits"] == 2]

    # Benchmarks on m004, m003, m000
    m004_chk = (
        "m004" in s_e8_lock_248
        and s_e8_lock_details["m004"]["two_T_orbits"] == 2
        and s_e8_lock_details["m004"]["bd5_surj"] == 40
        and s_e8_lock_details["m004"]["sl2_f25_full2d_spin_hits"] == 4
        and s_e8_lock_details["m004"]["gluing_f25_strict"]
    )
    m003_summary = {
        "h1_torsion": m003_obj["h1_torsion"],
        "d5_surj": per_m_q2["m003"]["d5_surj"],
        "bd5_surj": per_m_q2["m003"]["bd5_surj"],
        "hper_types": per_m_q2["m003"]["hper_types"],
        "sl2_f25_full2d_hits": len(fricke_res["m003"]["full_2d_hits"]),
        "gluing_f25_strict": "m003" in gluing_f25_strict_set,
        "two_T_orbits": count_2t_surj_orbits(m003_obj),
    }
    m000_summary = {
        "h1_torsion": m000["h1_torsion"],
        "d5_surj": m000_q2["d5_surj"],
        "bd5_surj": m000_q2["bd5_surj"],
        "hper_types": m000_q2["hper_types"],
        "sl2_f25_nonorient_parabolic_hits": len(m000_fricke["nonorient_hits"]),
        "sl2_f25_surj_hits": sum(1 for h in m000_fricke["nonorient_hits"] if h["surj_SL2_F25"]),
        "two_T_orbits": count_2t_surj_orbits(m000),
    }

    # Five independent Planted Fault Controls (PF1..PF5)
    # PF1: Omitting BD_5 sheet action on m004 restores periodic kernel to 8 (not 0)
    pf1 = (e8_peripheral_kernel(F1, 3, 1, -1, 0, 0)["k128_total_4spins"] == 8)
    # PF2: Replacing C_4 (j) by C_5 (r) or C_2 (-1) leaves 128-spinor kernel strictly positive
    pf2 = (
        e8_peripheral_kernel(F1, 3, 1, -1, 4, 0)["k128_total_4spins"] in (4, 6)
        and e8_peripheral_kernel(F1, 3, 1, -1, 2, 0)["k128_total_4spins"] == 8
    )
    # PF3: Explicit Z/2Z torsion relator g^2 = 1 on D_5 <a, b | a^2, b^2, (ab)^5> has D_5 surj > 0 but BD_5 == 0
    fake_d5_tor = {"gens": ["a", "b"], "rels": ["aa", "bb", "ababababab"], "periph": ["ab", "ab"]}
    r_fake_tor = analyze_d5_bd5_manifold(fake_d5_tor)
    pf3 = (r_fake_tor["d5_surj"] > 0 and r_fake_tor["bd5_surj"] == 0)
    # PF4: Degenerate F_5-only SL(2, F_5) pair [[1,1],[0,1]], [[1,0],[1,1]] has subgroup order <= 240 (< 15,600)
    A_f5 = (F1, F1, F0, F1)
    B_f5 = (F1, F0, F1, F1)
    pf4 = (not sl2_subgroup_exceeds_240(A_f5, B_f5, (F1, NEG[F1], F0, F1), (F1, F0, NEG[F1], F1)))
    # PF5: Corrupted m004 relator breaks both BD_5 and SL(2, F_25)
    bad_m004 = {
        "name": "bad_m004", "orientable": True, "gens": ["a", "b"],
        "rels": ["aaaaabABBAb"], "periph": ["ab", "aBAbABab"],
    }
    pf5 = (
        analyze_d5_bd5_manifold(bad_m004)["bd5_surj"] == 0
        and len(analyze_sl2_f25_2gen(bad_m004, irred_ab)["full_2d_hits"]) == 0
    )

    pf = {
        "PF1_omit_sheet_restores_8": pf1,
        "PF2_C5_and_C2_stay_positive": pf2,
        "PF3_D5_Z2_torsion_obstructs_BD5": pf3,
        "PF4_F5_subgroup_below_240": pf4,
        "PF5_corrupted_m004_breaks_both": pf5,
    }
    pf_caught = sum(1 for v in pf.values() if v)

    all_ok = (
        ast_floats == 0
        and q1["ok"]
        and m004_chk
        and obstructed_all_have_even_torsion
        and pf_caught == 5
    )

    out = {
        "card": "A2-WHOLE-CENSUS-E8-TWO-REGISTER",
        "seat_code": "fam3-v1-high-03",
        "blind": "0 of 19",
        "ast_floats": ast_floats,
        "json_floats": 0,
        "census_size": {"orientable": len(orient_manifolds), "nonorientable_m000": 1},
        "Q1_universal_E8_kernel_theorem": q1,
        "Q2_D5_BD5_census": {
            "d5_surj_manifolds": len(d5_set),
            "bd5_surj_manifolds": len(bd5_set),
            "d5_to_bd5_obstructed_count": len(d5_obstructed),
            "d5_to_bd5_obstructed_names": d5_obstructed,
            "obstructed_all_have_even_H1_torsion": obstructed_all_have_even_torsion,
            "hper_bucket_counts": dict(sorted(hper_bucket_counts.items())),
            "s_bd5_c4_total": len(s_bd5_c4),
            "s_bd5_c4_2gen": len(s_bd5_c4_2gen),
            "s_bd5_c4_3gen": len(s_bd5_c4_3gen),
            "s_bd5_c4_3gen_names": [m["name"] for m in s_bd5_c4_3gen],
        },
        "Q3_SL2_F25_and_E8_lock": {
            "gluing_F5_sol_count_of_1199": gluing_f5_cnt,
            "gluing_F25_strict_sol_count_of_1199": gluing_f25_strict_cnt,
            "s_bd5_c4_3gen_with_gluing_F25_strict": s_bd5_c4_3gen_gluing_f25,
            "bd5_all_2gen_checked_fricke": len(bd5_all_2gen),
            "bd5_non_c4_2gen_with_sl2_f25": len(bd5_non_c4_2gen_with_sl2_f25),
            "bd5_non_c4_2gen_with_sl2_f25_names": bd5_non_c4_2gen_with_sl2_f25,
            "s_e8_lock_128_count": len(s_e8_lock_128),
            "s_e8_lock_128_names": s_e8_lock_128,
            "s_e8_lock_248_count": len(s_e8_lock_248),
            "s_e8_lock_248_names": s_e8_lock_248,
            "s_e8_lock_details": s_e8_lock_details,
        },
        "Q4_crosstab_and_benchmarks": {
            "lock_128_by_tet": {str(k): v for k, v in lock_by_tet.items()},
            "lock_248_by_tet": {str(k): v for k, v in lock_248_by_tet.items()},
            "lock_128_with_2T_count": len(lock_with_2t),
            "lock_248_with_2T_count": len(lock_248_with_2t),
            "lock_248_with_2T_names": lock_248_with_2t,
            "lock_248_H1_Z_count": len(lock_248_h1_Z),
            "lock_248_H1_Z_names": lock_248_h1_Z,
            "lock_248_H1_Z_and_2T_count": len(lock_248_h1_Z_2t),
            "lock_248_H1_Z_and_2T_names": lock_248_h1_Z_2t,
            "lock_248_2T_eq_2_count": len(lock_248_2t_eq_2),
            "lock_248_2T_eq_2_names": lock_248_2t_eq_2,
            "m004_benchmark_ok": m004_chk,
            "m003_summary": m003_summary,
            "m000_summary": m000_summary,
        },
        "planted_fault_controls": pf,
        "pf_caught": pf_caught,
        "all_gates_passed": all_ok,
    }

    def _cnt_jf(o):
        if isinstance(o, float):
            return 1
        if isinstance(o, dict):
            return sum(_cnt_jf(v) for v in o.values())
        if isinstance(o, list):
            return sum(_cnt_jf(v) for v in o)
        return 0

    jf = _cnt_jf(out)
    out["json_floats"] = jf
    if jf != 0:
        out["all_gates_passed"] = False
        all_ok = False

    try:
        OUT_JSON.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    except OSError:
        pass

    print(f"DECISIVE: Q1_E8_THEOREM ok={q1['ok']} bases={q1['bases_checked']} c4_iff_0={q1['c4_iff_k128_zero']} "
          f"k128_C1={q1['k128_total_by_Hper']['C1']} k128_C2={q1['k128_total_by_Hper']['C2']} "
          f"k128_C4={q1['k128_total_by_Hper']['C4']} k128_C5={q1['k128_total_by_Hper']['C5']} k128_C10={q1['k128_total_by_Hper']['C10']}")
    print(f"DECISIVE: Q2_BD5_CENSUS total=1199 D5={len(d5_set)} BD5={len(bd5_set)} obst={len(d5_obstructed)} "
          f"even_tor={obstructed_all_have_even_torsion} BD5_C4={len(s_bd5_c4)} C4_2g={len(s_bd5_c4_2gen)} C4_3g={len(s_bd5_c4_3gen)}")
    print(f"DECISIVE: Q3_E8_LOCK glueF5={gluing_f5_cnt} glueF25={gluing_f25_strict_cnt} "
          f"lock128={len(s_e8_lock_128)} lock248={len(s_e8_lock_248)} c4_3g_glueF25={len(s_bd5_c4_3gen_gluing_f25)} "
          f"nonC4_sl2={len(bd5_non_c4_2gen_with_sl2_f25)}")
    print(f"DECISIVE: Q4_CROSSTAB m004_ok={m004_chk} lock248_2T={len(lock_248_with_2t)} lock248_H1Z={len(lock_248_h1_Z)} "
          f"lock248_H1Z_2T={len(lock_248_h1_Z_2t)} m003_BD5={m003_summary['bd5_surj']} m000_BD5={m000_summary['bd5_surj']}")
    print(f"DECISIVE: SUMMARY all_ok={all_ok} PF={pf_caught}/5 floats={ast_floats}/{jf}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(run_all())
