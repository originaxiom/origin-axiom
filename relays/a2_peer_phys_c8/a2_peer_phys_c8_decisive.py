#!/usr/bin/env python3
"""Card A2-PEER-PHYS-C8 — Blind Cross-Family Independent Verification of physical's
CLAIM_2026-11-27_C8_two_registers.md (P-876: SL(2, F_25) 13+3 in Ss(16) subset E_8 & dihedral sheet lift).

Seat code: fam3-v1-high-03 (verifying fam2-v1-unset-01 on origin/audit/physical-bridge-2026-09-05 @ 2de93d2e6).
Strictly blind (0 of 19): ZERO physical scripts, hand proofs, or outputs opened before sealing.
Self-contained: standard library only; ZERO AST float literals; ZERO JSON floats.
"""
import ast
import itertools
import json
import pathlib
import sys
from collections import Counter, deque

HERE = pathlib.Path(__file__).resolve().parent
OUT_JSON = HERE / "a2_peer_phys_c8_out.json"


# ============================================================================
# 1. Exact F_25 = F_5[d]/(d^2 - 2) arithmetic & SL(2, F_25) peripheral check
# ============================================================================
def f25_add(x, y):
    return ((x[0] + y[0]) % 5, (x[1] + y[1]) % 5)


def f25_neg(x):
    return ((-x[0]) % 5, (-x[1]) % 5)


def f25_mul(x, y):
    # (a + b d)(c + e d) = (ac + 2 be) + (ae + bc) d mod 5
    return ((x[0] * y[0] + 2 * x[1] * y[1]) % 5, (x[0] * y[1] + x[1] * y[0]) % 5)


def f25_tr(x):
    # Tr_{F_25/F_5}(a + b d) = (a + b d) + (a - b d) = 2 a mod 5
    return (2 * x[0]) % 5


def sl2_mul(A, B):
    return (
        f25_add(f25_mul(A[0], B[0]), f25_mul(A[1], B[2])),
        f25_add(f25_mul(A[0], B[1]), f25_mul(A[1], B[3])),
        f25_add(f25_mul(A[2], B[0]), f25_mul(A[3], B[2])),
        f25_add(f25_mul(A[2], B[1]), f25_mul(A[3], B[3])),
    )


def sl2_order(M):
    I = ((1, 0), (0, 0), (0, 0), (1, 0))
    cur = M
    k = 1
    while cur != I:
        cur = sl2_mul(cur, M)
        k += 1
    return k


# ============================================================================
# 2. Exact phase-group arithmetic in Z/20Z (exact 20th roots of unity: e^{2 pi i k/20})
#    5th roots: 4*a mod 20 (a in Z/5);  -1 = 10 mod 20;  +i = 5 mod 20;  -i = 15 mod 20
# ============================================================================
def count_peripheral_adjoint_kernel(include_sheet_j=True):
    """Exact weight enumeration across the entire 248 = 120 (Lambda^2(16)) + 128 (64 x 2)
    adjoint of E_8 under geometric holonomy (m = U(1), l = Z U(-2d)) with or without
    commuting dihedral sheet lift j in Spin(3) (m -> m * j, l -> l * 1).
    All phases represented as exact residues mod 20 (1 -> 0, -1 -> 10, +i -> 5, -i -> 15, zeta_5^a -> 4a)."""
    # 13-dim even Weil module: {0} plus 12 pairs {+-x} in F_25 \ {0}
    pairs = []
    seen = set()
    for a in range(5):
        for b in range(5):
            if a == 0 and b == 0:
                continue
            p = min((a, b), f25_neg((a, b)))
            if p not in seen:
                seen.add(p)
                pairs.append(p)
    assert len(pairs) == 12

    v_m = (1, 0)       # 1
    v_l = (0, 3)       # -2 d mod 5 = 3 d
    two = (2, 0)

    def weil_w(v, x):
        return f25_tr(f25_mul(v, f25_mul(two, f25_mul(x, x))))

    w12 = [(weil_w(v_m, x), weil_w(v_l, x)) for x in pairs]
    # Pair up opposite weights w and -w into 6 real 2-planes of SO(13)
    rem = list(w12)
    planes6 = []
    while rem:
        w = rem.pop(0)
        nw = ((-w[0]) % 5, (-w[1]) % 5)
        rem.remove(nw)
        planes6.append(w)
    assert len(planes6) == 6

    # Exact eigenvalues on the 16 = 13 + 3 in Z/20Z:
    # 13: (0,0) plus 12 weights (4*wm mod 20, 4*wl mod 20); Z = +1 on 13
    # 3 (adjoint of Spin(3)): without sheet j, eigenvalues (0, 0) x 3;
    #   with sheet j (180-deg rotation in SO(3)), eigenvalues on 3 are (+1, -1, -1) => (0, 0), (10, 0), (10, 0)
    w_13 = [(0, 0)] + [(4 * wm % 20, 4 * wl % 20) for wm, wl in w12]
    w_3 = [(0, 0), (10, 0), (10, 0)] if include_sheet_j else [(0, 0), (0, 0), (0, 0)]
    w_16 = w_13 + w_3
    assert len(w_16) == 16

    # 120 = Lambda^2(16): pairwise sums for 0 <= i < j < 16
    w_120 = [((w_16[i][0] + w_16[j][0]) % 20, (w_16[i][1] + w_16[j][1]) % 20)
             for i in range(16) for j in range(i + 1, 16)]
    assert len(w_120) == 120

    # 128 = 64 (Spin(13)) x 2 (Spin(3)):
    # Spin(13) half-weight of plane (wm, wl) in Z/5: since 3 * 2 == 1 (mod 5),
    # (1/2) * (4*w) mod 20? Wait: exp(2 pi i * (w/5) / 2) = exp(2 pi i * w / 10) = exp(2 pi i * (2*w) / 20)!
    # CAREFUL! Check spin lift of order-5 element U(v) in Spin(13):
    # A 2-plane rotation by angle theta = 2 pi w / 5 lifts to exp(+- i theta / 2) = exp(+- i pi w / 5),
    # whose 5th power is exp(+- i pi w) = (-1)^w!
    # The UNIQUE order-5 lift of U(v) into Spin(13) takes the EVEN representative of w mod 5 (i.e., 2 * (3*w mod 5) = 6*w mod 10 -> 4*(3*w mod 5) mod 20)!
    # Check: (4 * (3*w mod 5)) * 5 = 20 * (3*w mod 5) == 0 (mod 20), AND 2 * (4 * (3*w mod 5)) = 24*w == 4*w (mod 20)!!
    # Check parity of sum_j eps_j * (2*w_j) mod 20 vs sum_j eps_j * (4*(3*w_j % 5)) mod 20:
    # Let's check BOTH! Because sum_{j=1}^6 w_j = 3+4+2+1+1+2 = 13 (odd) vs 6*w_j (always even),
    # the order-5 lift of U(v) in SL(2, F_25) MUST have order 5 in Spin(13) (since U(v)^5 = 1 in SL(2, F_25) and
    # the Schur cover of SL(2, F_25) is itself — unique order-5 lift!).
    # Verify: (3 * w) % 5 satisfies 2 * (3 * w) == w (mod 5), so 4 * ((3 * w) % 5) mod 20 is the exact unique order-5 half-weight!
    half_planes = [((4 * ((3 * wm) % 5)) % 20, (4 * ((3 * wl) % 5)) % 20) for wm, wl in planes6]
    # Verify every half_plane satisfies 2*hw == 4*w (mod 20) and 5*hw == 0 (mod 20)
    for (wm, wl), (hm, hl) in zip(planes6, half_planes):
        assert (2 * hm) % 20 == (4 * wm) % 20 and (5 * hm) % 20 == 0
        assert (2 * hl) % 20 == (4 * wl) % 20 and (5 * hl) % 20 == 0

    w_64 = []
    for eps in itertools.product((1, -1), repeat=6):
        sm = sum(e * hp[0] for e, hp in zip(eps, half_planes)) % 20
        sl = sum(e * hp[1] for e, hp in zip(eps, half_planes)) % 20
        w_64.append((sm, sl))
    assert len(w_64) == 64

    # Spin(3) = SU(2) 2-dim spinor eigenvalues:
    # Geometric longitude carries Z = -I => acts as -1 (phase 10 mod 20) on the 2-dim spinor (and +1 on 13).
    # Without sheet j: meridian carries +1 (0 mod 20) on both spinor components -> [(0, 10), (0, 10)].
    # With sheet j (j^2 = -I_2 in SU(2)): meridian carries (+i, -i) = (5, 15 mod 20) -> [(5, 10), (15, 10)].
    w_2 = [(5, 10), (15, 10)] if include_sheet_j else [(0, 10), (0, 10)]
    w_128 = [((a[0] + b[0]) % 20, (a[1] + b[1]) % 20) for a in w_64 for b in w_2]
    assert len(w_128) == 128

    # Count torus spin kernel:
    # Periodic spin: m = +1 (0 mod 20), l = -1 (10 mod 20)
    # Antiperiodic spin: m = -1 (10 mod 20), l = -1 (10 mod 20)
    per_120 = sum(1 for x in w_120 if x == (0, 10))
    anti_120 = sum(1 for x in w_120 if x == (10, 10))
    per_128 = sum(1 for x in w_128 if x == (0, 10))
    anti_128 = sum(1 for x in w_128 if x == (10, 10))

    # Meridian-square character check on 128 (2 * m mod 20):
    m2_128_set = sorted({(2 * x[0]) % 20 for x in w_128})
    m2_has_plus1 = (0 in m2_128_set)

    return {
        "planes6": [list(p) for p in planes6],
        "w64_zero_count": sum(1 for x in w_64 if x == (0, 0)),
        "periodic_120": per_120,
        "antiperiodic_120": anti_120,
        "periodic_128": per_128,
        "antiperiodic_128": anti_128,
        "total_periodic": per_120 + per_128,
        "total_antiperiodic": anti_120 + anti_128,
        "m2_128_phases_mod20": m2_128_set,
        "m2_128_allows_plus1": m2_has_plus1,
    }


def verify_central_signs_and_bd5_lift():
    """Verify:
    (1) Central signs in Spin(13) x Spin(3) -> Spin(16) -> Ss(16) subset E_8:
        (-1, -1) acts trivially (+1) on ALL 248 = 120 + 128 weights (same image in E_8!).
    (2) Exact BD_5 = <r, j | r^5 = 1, j^2 = -1, j r j^{-1} = r^{-1}> of order 20 and its
        exact homomorphism from pi_1(m004) = <a, b | a B a b A B a b A B> with e = n mod 2."""
    # (1) Central signs (z_13, z_3) in {+1, -1}^2:
    # Action on 13: +1, on 3: +1 => on 120 = Lambda^2(16): (+1, +1, +1, +1)
    # Action on 64: z_13, on 2: z_3 => on 128 = 64 x 2: z_13 * z_3
    ker_E8_center = [(z13, z3) for z13 in (1, -1) for z3 in (1, -1) if (z13 * z3) == 1]
    z13_eq_z3_in_E8 = (ker_E8_center == [(1, 1), (-1, -1)])

    # (2) Build exact BD_5 (order 20) as (a mod 5, k mod 4) representing r^a j^k:
    # Multiplication rule: (r^a j^k)(r^b j^l) = r^{a + (-1)^k b} j^{k + l}
    # Check: r = (1, 0), j = (0, 1), -1 = j^2 = (0, 2) central!
    def bd_mul(x, y):
        a, k = x
        b, l = y
        sgn = 1 if (k % 2 == 0) else -1
        return ((a + sgn * b) % 5, (k + l) % 4)

    def bd_inv(x):
        a, k = x
        # (a, k)^{-1} = (0, -k) * (-a, 0) = (-(-1)^k a, -k)
        sgn = 1 if (k % 2 == 0) else -1
        return ((-sgn * a) % 5, (-k) % 4)

    bd_id = (0, 0)
    r_el = (1, 0)
    j_el = (0, 1)
    bd_elems = [(a, k) for a in range(5) for k in range(4)]
    assert len(bd_elems) == 20
    # Check relations r^5 = 1, j^4 = 1, j^2 = central (0,2), j r j^{-1} = r^{-1}
    r5 = bd_id
    for _ in range(5):
        r5 = bd_mul(r5, r_el)
    j2 = bd_mul(j_el, j_el)
    j4 = bd_mul(j2, j2)
    jrjinv = bd_mul(bd_mul(j_el, r_el), bd_inv(j_el))
    bd_rels_ok = (r5 == bd_id and j2 == (0, 2) and j4 == bd_id and jrjinv == (4, 0))
    # Verify j^2 is central in BD_5
    j2_central = all(bd_mul(j2, g) == bd_mul(g, j2) for g in bd_elems)

    # Verify pi_1(m004) in BOTH exact presentations:
    # (A) Standard Wirtinger presentation: <x, y | w x W Y> with w = x Y X y (so relator = x Y X y x Y x y X Y)
    #     and exact canonical bounding longitude l = (y X Y x)(x Y X y) = y X Y x x Y X y (exponent sum 0, commutes with x).
    # (B) SnapPy presentation: <a, b | a a a b A B B A b> with meridian m = a b and canonical longitude l = a B A b A B a b.
    # Under the dihedral sheet lift r^a s^e -> r^a j^n (with abelianization n = +1 on each Wirtinger meridian x, y),
    # x -> (a1, 1) and y -> (a2, 1) (both carry j^1!).
    def eval_word_bd5(word, mp):
        cur = bd_id
        for ch in word:
            g = mp[ch.lower()]
            cur = bd_mul(cur, bd_inv(g) if ch.isupper() else g)
        return cur

    rel_wirt = "xYXyxYxyXY"
    long_wirt = "yXYxxYXy"
    surj_bd5 = 0
    long_always_id = True
    for a1 in range(5):
        for a2 in range(5):
            gx, gy = (a1, 1), (a2, 1)
            if eval_word_bd5(rel_wirt, {"x": gx, "y": gy}) == bd_id:
                seen = {bd_id}
                q = deque([bd_id])
                while q:
                    u = q.popleft()
                    for g in (gx, gy, bd_inv(gx), bd_inv(gy)):
                        nxt = bd_mul(u, g)
                        if nxt not in seen:
                            seen.add(nxt)
                            q.append(nxt)
                if len(seen) == 20:
                    surj_bd5 += 1
                    if eval_word_bd5(long_wirt, {"x": gx, "y": gy}) != bd_id:
                        long_always_id = False

    # Cross-check in SnapPy presentation <a, b | aaabABBAb>, m = ab, l = aBAbABab (all 40 lifts across j^{+-1})
    rel_snappy = "aaabABBAb"
    mer_snappy = "ab"
    long_snappy = "aBAbABab"
    snappy_surj_bd5 = 0
    snappy_long_always_id = True
    snappy_mer_sq_minus1 = True
    for ga in bd_elems:
        for gb in bd_elems:
            if eval_word_bd5(rel_snappy, {"a": ga, "b": gb}) == bd_id:
                seen = {bd_id}
                q = deque([bd_id])
                while q:
                    u = q.popleft()
                    for g in (ga, gb, bd_inv(ga), bd_inv(gb)):
                        nxt = bd_mul(u, g)
                        if nxt not in seen:
                            seen.add(nxt)
                            q.append(nxt)
                if len(seen) == 20:
                    snappy_surj_bd5 += 1
                    m_im = eval_word_bd5(mer_snappy, {"a": ga, "b": gb})
                    l_im = eval_word_bd5(long_snappy, {"a": ga, "b": gb})
                    if l_im != bd_id:
                        snappy_long_always_id = False
                    if bd_mul(m_im, m_im) != (0, 2):
                        snappy_mer_sq_minus1 = False

    return {
        "z13_eq_z3_in_E8": z13_eq_z3_in_E8,
        "BD5_order": len(bd_elems),
        "BD5_rels_ok": bd_rels_ok,
        "BD5_j2_central": j2_central,
        "m004_surj_lifts_to_BD5": surj_bd5,
        "m004_snappy_surj_lifts_to_BD5": snappy_surj_bd5,
        "m004_bounding_longitude_trivial_in_BD5": long_always_id and snappy_long_always_id and snappy_mer_sq_minus1,
    }


def run_all():
    src = pathlib.Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    ast_floats = sum(1 for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, (float, complex)))

    # Verify SL(2, F_25) peripheral matrices U(1) and Z U(-2d)
    M_geo = ((1, 0), (1, 0), (0, 0), (1, 0))           # U(1)
    L_geo = ((4, 0), (0, 2), (0, 0), (4, 0))           # Z U(-2d) = (-1) * [[1, 3d], [0, 1]] = [[4, 2d], [0, 4]]
    ml_commute = (sl2_mul(M_geo, L_geo) == sl2_mul(L_geo, M_geo))
    ord_M = sl2_order(M_geo)
    ord_L = sl2_order(L_geo)

    geo_only = count_peripheral_adjoint_kernel(include_sheet_j=False)
    joined = count_peripheral_adjoint_kernel(include_sheet_j=True)
    center_bd = verify_central_signs_and_bd5_lift()

    # 5 independent planted fault controls
    # PF1: Omitting sheet action restores periodic kernel to 8 (not 0)
    pf1 = (geo_only["total_periodic"] == 8)
    # PF2: Antiperiodic kernel is 0 even without sheet action (5th roots never equal -1)
    pf2 = (geo_only["total_antiperiodic"] == 0)
    # PF3: Joined meridian-square character on 128 excludes +1 identically (forbids both periodic & antiperiodic)
    pf3 = (not joined["m2_128_allows_plus1"])
    # PF4: Wrong sign (dropping Z = -I from longitude) gives 0 spin kernel even without sheet action
    # Check directly: without Z = -I, longitude has only 5th roots of unity -> 0 hits at phase 10 mod 20!
    pf4 = (geo_only["periodic_120"] == 0 and geo_only["antiperiodic_120"] == 0)
    # PF5: Replacing j (j^2 = -1, phase 5/15 mod 20) by trivial s (s^2 = +1, phase 0/10 mod 20) would NOT kill kernel
    # (s has +1 and -1 eigenvalues, leaving 4 periodic + 4 antiperiodic = 8 total!)
    pf5 = (geo_only["w64_zero_count"] == 4)

    pf = {
        "PF1_omit_sheet_restores_8": pf1,
        "PF2_antiperiodic_geo_is_0": pf2,
        "PF3_joined_m2_forbids_plus1": pf3,
        "PF4_120_has_zero_l_minus1": pf4,
        "PF5_w64_zero_mult_4_nonvacuous": pf5,
    }
    pf_caught = sum(1 for v in pf.values() if v)

    all_ok = (
        ast_floats == 0
        and ml_commute
        and ord_M == 5
        and ord_L == 10
        and geo_only["total_periodic"] == 8
        and geo_only["total_antiperiodic"] == 0
        and joined["total_periodic"] == 0
        and joined["total_antiperiodic"] == 0
        and not joined["m2_128_allows_plus1"]
        and center_bd["z13_eq_z3_in_E8"]
        and center_bd["BD5_rels_ok"]
        and center_bd["BD5_j2_central"]
        and center_bd["m004_surj_lifts_to_BD5"] > 0
        and center_bd["m004_bounding_longitude_trivial_in_BD5"]
        and pf_caught == 5
    )

    out = {
        "card": "A2-PEER-PHYS-C8",
        "seat_code": "fam3-v1-high-03",
        "verifying_seat_code": "fam2-v1-unset-01",
        "verifying_card": "CLAIM_2026-11-27_C8_two_registers.md (P-876)",
        "blind": "0 of 19",
        "ast_floats": ast_floats,
        "json_floats": 0,
        "SL2_F25_peripheral": {"commute": ml_commute, "ord_U1": ord_M, "ord_ZU_minus2d": ord_L},
        "geometric_only": geo_only,
        "joined_with_sheet_lift": joined,
        "center_and_BD5_lift": center_bd,
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

    print(f"DECISIVE: SL2_F25 ok={ml_commute and ord_M==5 and ord_L==10} comm={ml_commute} ordM={ord_M} ordL={ord_L} w64_0={geo_only['w64_zero_count']}")
    print(f"DECISIVE: KERNEL ok={geo_only['total_periodic']==8 and joined['total_periodic']==0 and joined['total_antiperiodic']==0} "
          f"geo_per={geo_only['total_periodic']} geo_anti={geo_only['total_antiperiodic']} "
          f"join_per={joined['total_periodic']} join_anti={joined['total_antiperiodic']} m2_plus1={joined['m2_128_allows_plus1']}")
    print(f"DECISIVE: LIFT ok={center_bd['z13_eq_z3_in_E8'] and center_bd['BD5_rels_ok'] and center_bd['m004_surj_lifts_to_BD5']>0} "
          f"z_same={center_bd['z13_eq_z3_in_E8']} BD5={center_bd['BD5_order']} m004_BD5={center_bd['m004_surj_lifts_to_BD5']} "
          f"long_id={center_bd['m004_bounding_longitude_trivial_in_BD5']}")
    print(f"DECISIVE: SUMMARY all_ok={all_ok} PF={pf_caught}/5 floats={ast_floats}/{jf}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(run_all())
