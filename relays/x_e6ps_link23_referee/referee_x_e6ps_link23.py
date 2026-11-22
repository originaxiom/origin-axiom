#!/usr/bin/env python3
"""Disjoint Cold-Room Referee for Card X-E6PS-LINK23 (Guardrail 6, 0 of 19).

Independently reconstructs and audits every mathematical-physics theorem of Card X-E6PS-LINK23
using zero shared code, zero imports from the producer script, zero Python `float` or `complex`
AST literals, and genuinely distinct algorithms in every module:

  - REF_1: Bourbaki 6x6 E_6 Cartan matrix + Weyl-orbit BFS in 6D Dynkin labels (no E_8 / R^8!).
  - REF_2: Explicit weight-by-weight summation over all 17*N_gen Cartan states (proving that
           3 x 16_{+1} ALONE fails [Z_3]^3 = 48 == 3 != 0 mod 9 and REQUIRES 3 x chi_{S,-1}!).
  - REF_3: 2-stage order-4 implicit Gauss-Legendre (GL4) solver (N=1000) cross-checked against
           producer's explicit RK4(4000) trajectory to < 10^{-11}.
  - REF_4: Matrix-exponential `mp.expm(i H)` unitary basis scrambling + `mp.eigh(M * M^H)` Takagi.
  - REF_5: Chiral-Weyl 4x4 Clifford basis (gamma^0 = [[0,I],[I,0]]) proving s-wave pseudoscalar
           portal vs p-wave-suppressed (0 at v->0) CP-even scalar portal + full stationary-point
           minimization dV/dv_i = 0 for det(M_{phys,2x2}^2).
  - REF_6: SHA-256 manifest verification (both v1 and v2) + 6 independent planted faults PF_REF_1..6.
"""
from __future__ import annotations

import ast
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

REPO_ROOT = Path(__file__).resolve().parents[2]
V1_SCRIPT_SHA = REPO_ROOT / "relays" / "x_e6ps_link23_verify" / "SCRIPT_SHA256.txt"
V2_SCRIPT = REPO_ROOT / "relays" / "x_e6ps_link23_v2_verify" / "verify_x_e6ps_link23_v2.py"
V2_SCRIPT_SHA = REPO_ROOT / "relays" / "x_e6ps_link23_v2_verify" / "SCRIPT_SHA256.txt"
V2_OUT = REPO_ROOT / "relays" / "x_e6ps_link23_v2_verify" / "verify_x_e6ps_link23_v2_out.json"
V2_OUT_SHA = REPO_ROOT / "relays" / "x_e6ps_link23_v2_verify" / "OUTPUT_SHA256.txt"
OUT_PATH = Path(__file__).resolve().parent / "referee_x_e6ps_link23_out.json"


def rat_mpf(p: int, q: int = 1) -> mp.mpf:
    return mp.mpf(int(p)) / mp.mpf(int(q))


def p10(k: int) -> mp.mpf:
    return mp.power(mp.mpf(10), int(k))


def fstr(x: Fraction) -> str:
    f = Fraction(x)
    return str(f.numerator) if f.denominator == 1 else f"{f.numerator}/{f.denominator}"


def self_ast_scan() -> dict[str, object]:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    bad_lits = [n.lineno for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, (float, complex))]
    bad_calls = [
        n.lineno for n in ast.walk(tree)
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in ("float", "complex")
    ]
    return {
        "float_or_complex_literals": len(bad_lits),
        "binary64_cast_calls": len(bad_calls),
        "ast_clean": len(bad_lits) == 0 and len(bad_calls) == 0,
    }


def sha256_hex(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_manifest_line(manifest_path: Path) -> bool:
    line = manifest_path.read_text(encoding="utf-8").strip()
    parts = line.split()
    if len(parts) != 2:
        return False
    expected_hex, rel_target = parts
    target_path = REPO_ROOT / rel_target
    return target_path.exists() and sha256_hex(target_path) == expected_hex


# ---------------------------------------------------------------------------
# REF_1: Disjoint Bourbaki 6x6 E_6 Dynkin-Label Weyl BFS & Coroot Splitting
# ---------------------------------------------------------------------------

def run_ref1_bourbaki_dynkin_e6(prod: dict[str, object]) -> dict[str, object]:
    # Bourbaki E_6 Cartan matrix (nodes 1-3-4-5-6 along spine, node 2 attached to 4):
    A_e6 = [
        [2, 0, -1, 0, 0, 0],
        [0, 2, 0, -1, 0, 0],
        [-1, 0, 2, -1, 0, 0],
        [0, -1, -1, 2, -1, 0],
        [0, 0, 0, -1, 2, -1],
        [0, 0, 0, 0, -1, 2],
    ]

    def weyl_orbit(hw: tuple[int, ...]) -> list[tuple[int, ...]]:
        seen = {hw}
        stack = [hw]
        while stack:
            w = stack.pop()
            for i in range(6):
                nxt = tuple(w[j] - w[i] * A_e6[i][j] for j in range(6))
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        return sorted(seen)

    roots_72 = weyl_orbit((0, 1, 0, 0, 0, 0))
    w_27 = weyl_orbit((0, 0, 0, 0, 0, 1))
    w_27bar = weyl_orbit((1, 0, 0, 0, 0, 0))
    assert len(roots_72) == 72 and len(w_27) == 27 and len(w_27bar) == 27

    # Integer simple-coroot vectors in Q^v(E_6) = Z^6 (paired directly with Dynkin labels!):
    c1 = (2, 3, 4, 6, 5, 4)   # 3 * varpi_6^v -> Q_psi
    c2 = (0, 0, 0, 0, 1, 0)   # alpha_5^v
    c3 = (2, 3, 4, 6, 3, 0)   # 3*(B-L)-splitting coroot inside D_5

    def pair(w: tuple[int, ...], c: tuple[Fraction | int, ...]) -> Fraction:
        return sum(Fraction(w[i]) * Fraction(c[i]) for i in range(6))

    v1 = tuple(Fraction(x, 6) for x in c1)
    v2 = tuple(Fraction(x, 2) for x in c2)
    v3 = tuple(Fraction(x, 16) for x in c3)

    inv_roots = [r for r in roots_72 if pair(r, v1) % 1 == 0 and pair(r, v2) % 1 == 0 and pair(r, v3) % 1 == 0]
    dim_glr_ref = len(inv_roots) + 5  # 10 + 5 = 15

    sec_27 = Counter((pair(w, v1) % 1, pair(w, v2) % 1, pair(w, v3) % 1) for w in w_27)
    dims_phi_S_D_Dbar = [
        sec_27[(Fraction(2, 3), Fraction(1, 2), Fraction(0, 1))],
        sec_27[(Fraction(2, 3), Fraction(0, 1), Fraction(0, 1))],
        sec_27[(Fraction(2, 3), Fraction(0, 1), Fraction(1, 8))],
        sec_27[(Fraction(2, 3), Fraction(0, 1), Fraction(7, 8))],
    ]
    chiral_16_per_27 = sum(1 for w in w_27 if pair(w, c1) == 1)

    sym2_27bar: Counter[tuple[int, ...]] = Counter()
    for i in range(27):
        for j in range(i, 27):
            sym2_27bar[tuple(w_27bar[i][k] + w_27bar[j][k] for k in range(6))] += 1
    w_351p = sym2_27bar.copy()
    for w in w_27:
        w_351p[w] -= 1
        if w_351p[w] == 0:
            del w_351p[w]
    sec_351p: Counter[tuple[Fraction, Fraction, Fraction]] = Counter()
    for w, m in w_351p.items():
        sec_351p[(pair(w, v1) % 1, pair(w, v2) % 1, pair(w, v3) % 1)] += m

    delR_dim = sec_351p[(Fraction(2, 3), Fraction(0, 1), Fraction(3, 8))]
    delL_dim = sec_351p[(Fraction(2, 3), Fraction(0, 1), Fraction(5, 8))]

    # Independent 6D E_6 quartic trace check on 5 distinct Z^6 coroot probes:
    probes = [
        (3, -2, 5, 1, -4, 2),
        (1, 1, 1, 1, 1, 1),
        (-2, 4, -1, 3, -5, 7),
        (0, 3, -2, 0, 5, -1),
        (5, 0, -3, 2, 1, -4),
    ]
    quartic_ok = all(
        sum(pair(w, h) ** 4 for w in w_27) == Fraction(1, 12) * (sum(pair(w, h) ** 2 for w in w_27) ** 2)
        and sum(pair(r, h) ** 4 for r in roots_72) == Fraction(1, 2) * (sum(pair(w, h) ** 2 for w in w_27) ** 2)
        for h in probes
    )

    # Planted Referee Fault PF_REF_1: coarse denominator 8 on v_3 merges Delta_R_bar with 33 colored states (36 != 3):
    v3_bad8 = tuple(Fraction(x, 8) for x in c3)
    sec_351p_bad8: Counter[tuple[Fraction, Fraction, Fraction]] = Counter()
    for w, m in w_351p.items():
        sec_351p_bad8[(pair(w, v1) % 1, pair(w, v2) % 1, pair(w, v3_bad8) % 1)] += m
    pf_ref_1_merged_dim = sec_351p_bad8[(Fraction(2, 3), Fraction(0, 1), Fraction(3, 4))]

    e1_prod = prod["E1_orbifold_e6_coroot_multiplet_splitting"]
    match_prod = (
        dim_glr_ref == e1_prod["surviving_g_LR_dim"] == 15
        and len(sec_27) == e1_prod["sectors_in_27_count"] == 8
        and dims_phi_S_D_Dbar == e1_prod["isolated_Phi_in_27_S_D3_D3bar_dims"] == [4, 1, 3, 3]
        and 3 * chiral_16_per_27 == e1_prod["chiral_spinor_weights_across_3_families"] == 48
        and sum(w_351p.values()) == e1_prod["constructed_351p_dim"] == 351
        and delR_dim == e1_prod["isolated_Delta_R_bar_dim_in_351p"] == 3
        and delL_dim == e1_prod["isolated_Delta_L_dim_in_351p"] == 3
        and quartic_ok
    )
    pf1_caught = (pf_ref_1_merged_dim == 36 and pf_ref_1_merged_dim != 3)

    return {
        "bourbaki_roots_27_351p_counts": [len(roots_72), len(w_27), sum(w_351p.values())],
        "surviving_g_LR_dim_ref": dim_glr_ref,
        "isolated_Phi_S_D3_D3bar_ref": dims_phi_S_D_Dbar,
        "isolated_DeltaRbar_DeltaL_ref": [delR_dim, delL_dim],
        "quartic_trace_factorization_ref": quartic_ok,
        "pf_ref_1_denom8_merged_dim": pf_ref_1_merged_dim,
        "matches_producer_E1": match_prod,
        "PF_REF_1_caught": pf1_caught,
        "REF_1_passed": bool(match_prod and pf1_caught),
    }


# ---------------------------------------------------------------------------
# REF_2: Explicit 17-State Weight-by-Weight Anomaly Summation & Dark-Matter Lock
# ---------------------------------------------------------------------------

def build_generation_17_states(include_chi_s: bool = True) -> list[tuple[Fraction, Fraction, Fraction, Fraction, Fraction, int]]:
    """Explicit Cartan weights (t3_C, s3_t8_C, t3_L, t3_R, B_minus_L, tau_3) for 1 generation.
    Note s3_t8_C = sqrt(3) * t8_C in {+1/2, +1/2, -1} on 3 and {-1/2, -1/2, +1} on 3bar.
    """
    su3_fund = [(Fraction(1, 2), Fraction(1, 2)), (Fraction(-1, 2), Fraction(1, 2)), (Fraction(0), Fraction(-1, 1))]
    su3_anti = [(-a, -b) for a, b in su3_fund]
    su2_doub = [Fraction(1, 2), Fraction(-1, 2)]
    states: list[tuple[Fraction, Fraction, Fraction, Fraction, Fraction, int]] = []
    # Q = (3, 2, 1, +1/3, +1):
    for t3c, st8 in su3_fund:
        for t3l in su2_doub:
            states.append((t3c, st8, t3l, Fraction(0), Fraction(1, 3), 1))
    # Q^c = (3bar, 1, 2, -1/3, +1):
    for t3c, st8 in su3_anti:
        for t3r in su2_doub:
            states.append((t3c, st8, Fraction(0), t3r, Fraction(-1, 3), 1))
    # L = (1, 2, 1, -1, +1):
    for t3l in su2_doub:
        states.append((Fraction(0), Fraction(0), t3l, Fraction(0), Fraction(-1, 1), 1))
    # L^c = (1, 1, 2, +1, +1):
    for t3r in su2_doub:
        states.append((Fraction(0), Fraction(0), Fraction(0), t3r, Fraction(1, 1), 1))
    if include_chi_s:
        states.append((Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0), -1))
    return states


def check_weight_anomalies(n_gen: int, include_chi_s: bool = True) -> dict[str, int | Fraction]:
    st = build_generation_17_states(include_chi_s=include_chi_s) * n_gen
    # Continuous triangles from explicit Cartan weights:
    su3_cub = sum(s[1] ** 3 for s in st)
    su3_sq_bl = sum((s[0] ** 2) * s[4] for s in st)
    su2L_sq_bl = sum((s[2] ** 2) * s[4] for s in st)
    su2R_sq_bl = sum((s[3] ** 2) * s[4] for s in st)
    bl_cub = sum(s[4] ** 3 for s in st)
    grav_bl = sum(s[4] for s in st)
    # Witten SU(2)_{L,R} doublet counts (= sum 2*t3^2 mod 2):
    wit_L = int(sum(2 * (s[2] ** 2) for s in st)) % 2
    wit_R = int(sum(2 * (s[3] ** 2) for s in st)) % 2
    # Discrete Z_3^{tau_3} residues:
    d_3c = int(sum(2 * (s[0] ** 2) * s[5] for s in st)) % 3
    d_2L = int(sum(2 * (s[2] ** 2) * s[5] for s in st)) % 3
    d_2R = int(sum(2 * (s[3] ** 2) * s[5] for s in st)) % 3
    d_bl = int(sum(((3 * s[4]) ** 2) * s[5] for s in st)) % 3
    d_gr = sum(s[5] for s in st) % 3
    d_cub_mod9 = sum(s[5] ** 3 for s in st) % 9
    return {
        "cont_max": max(abs(x) for x in (su3_cub, su3_sq_bl, su2L_sq_bl, su2R_sq_bl, bl_cub, grav_bl)),
        "witten_max": max(wit_L, wit_R),
        "discrete_linear_max": max(d_3c, d_2L, d_2R, d_bl, d_gr),
        "z3_cubic_mod9": d_cub_mod9,
    }


def run_ref2_weight_anomalies_and_dm_lock(prod: dict[str, object]) -> dict[str, object]:
    surviving = []
    for ng in range(1, 21):
        a = check_weight_anomalies(ng, include_chi_s=True)
        mg_lr = 24 + 17 * ng - 4 * 15
        mg_sm = 10 + 17 * ng - 4 * 12
        if a["cont_max"] == 0 and a["witten_max"] == 0 and a["discrete_linear_max"] == 0 and a["z3_cubic_mod9"] == 0 and mg_lr < 31 and mg_sm < 31:
            surviving.append(ng)

    # Planted Referee Fault PF_REF_2: Omit dark-matter chi_S at N_gen = 3 => [Z_3]^3 = 48 == 3 != 0 mod 9!
    no_dm_n3 = check_weight_anomalies(3, include_chi_s=False)
    pf2_caught = (no_dm_n3["z3_cubic_mod9"] == 3 and no_dm_n3["z3_cubic_mod9"] != 0)

    e2_prod = prod["E2_continuous_witten_discrete_anomalies_and_unique_Ngen3"]
    match_prod = (surviving == e2_prod["unique_surviving_N_gen"] == [3])

    return {
        "unique_surviving_N_gen_ref": surviving,
        "no_chiS_at_N3_z3_cubic_mod9": no_dm_n3["z3_cubic_mod9"],
        "matches_producer_E2": match_prod,
        "PF_REF_2_caught": pf2_caught,
        "REF_2_passed": bool(match_prod and pf2_caught),
    }


# ---------------------------------------------------------------------------
# REF_3: Implicit Order-4 Gauss-Legendre (GL4) 2-Loop Unification Countercheck
# ---------------------------------------------------------------------------

def run_ref3_gl4_unification(prod: dict[str, object]) -> dict[str, object]:
    mp.mp.dps = 42
    # Independent symbolic computation of 1-loop betas & r_LR = 2/5 vs 1-bidoublet planted fault:
    # Chiral G_LR: (U(1)_{B-L}, SU(2)_L, SU(2)_R, SU(3)_C)
    # Fermions (3 gen of Q, Q^c, L, L^c): (2/3)*(6, 6, 6, 6) = (4, 4, 4, 4)
    # Gauge: (0, -22/3, -22/3, -11)
    # Complex scalars: n_bid * (0, 1/3, 1/3, 0) + 1 * Delta_R_bar * ((1/3)*(3*3/2), 0, (1/3)*2, 0) = (3/2, 0, 2/3, 0)
    def chiral_lr_b1(n_bid: int) -> list[Fraction]:
        return [
            Fraction(4, 1) + Fraction(3, 2),
            Fraction(-22, 3) + Fraction(4, 1) + n_bid * Fraction(1, 3),
            Fraction(-22, 3) + Fraction(4, 1) + n_bid * Fraction(1, 3) + Fraction(2, 3),
            Fraction(-11, 1) + Fraction(4, 1),
        ]

    b1_lr_2bid = chiral_lr_b1(2)  # [11/2, -8/3, -2, -7]
    b1_2hdm = [Fraction(21, 5), Fraction(-3, 1), Fraction(-7, 1)]

    def solve_r(b_uv: list[Fraction]) -> Fraction:
        b1_eff = Fraction(3, 5) * b_uv[2] + Fraction(2, 5) * b_uv[0]
        DA = (b_uv[1] - b_uv[3]) - (b1_2hdm[1] - b1_2hdm[2])
        DC = (b1_eff - b_uv[1]) - (b1_2hdm[0] - b1_2hdm[1])
        return Fraction(8, 7 * DA - 5 * DC)

    r_2bid = solve_r(b1_lr_2bid)
    # Planted Referee Fault PF_REF_3: only 1 bidoublet shifts r_LR away from 2/5 (to 8/17):
    r_1bid_bad = solve_r(chiral_lr_b1(1))

    # Independent 2-loop beta matrices:
    b2_lr = [
        [Fraction(61, 2), Fraction(9, 2), Fraction(81, 2), Fraction(4, 1)],
        [Fraction(3, 2), Fraction(37, 3), Fraction(6, 1), Fraction(12, 1)],
        [Fraction(27, 2), Fraction(6, 1), Fraction(31, 1), Fraction(12, 1)],
        [Fraction(1, 2), Fraction(9, 2), Fraction(9, 2), Fraction(-26, 1)],
    ]
    b2_sm2h = [
        [Fraction(104, 25), Fraction(18, 5), Fraction(44, 5)],
        [Fraction(6, 5), Fraction(8, 1), Fraction(12, 1)],
        [Fraction(11, 10), Fraction(9, 2), Fraction(-26, 1)],
    ]
    inv4pi = mp.mpf(1) / (mp.mpf(4) * mp.pi)

    def gl4_step(y: list[mp.mpf], dt: mp.mpf, fn) -> list[mp.mpf]:
        s3 = mp.sqrt(mp.mpf(3))
        a11 = a22 = rat_mpf(1, 4)
        a12 = rat_mpf(1, 4) - s3 / mp.mpf(6)
        a21 = rat_mpf(1, 4) + s3 / mp.mpf(6)
        k1 = fn(y)
        k2 = list(k1)
        n = len(y)
        for _ in range(40):
            nk1 = fn([y[i] + dt * (a11 * k1[i] + a12 * k2[i]) for i in range(n)])
            nk2 = fn([y[i] + dt * (a21 * k1[i] + a22 * k2[i]) for i in range(n)])
            err = max(max(abs(nk1[i] - k1[i]), abs(nk2[i] - k2[i])) for i in range(n))
            k1, k2 = nk1, nk2
            if err < p10(-38):
                break
        return [y[i] + (dt / mp.mpf(2)) * (k1[i] + k2[i]) for i in range(n)]

    def make_rhs(b1_f: list[Fraction], b2_f: list[list[Fraction]]):
        K = len(b1_f)
        b1_m = [rat_mpf(x.numerator, x.denominator) for x in b1_f]
        b2_m = [[rat_mpf(x.numerator, x.denominator) for x in row] for row in b2_f]

        def fn(av: list[mp.mpf]) -> list[mp.mpf]:
            return [
                (av[i] * av[i] / (mp.mpf(2) * mp.pi)) * (b1_m[i] + inv4pi * sum(b2_m[i][j] * av[j] for j in range(K)))
                for i in range(K)
            ]

        return fn

    rhs_uv = make_rhs(b1_lr_2bid, b2_lr)
    rhs_ir = make_rhs(b1_2hdm, b2_sm2h)

    a_uv = [rat_mpf(1, 40)] * 4
    for _ in range(400):
        a_uv = gl4_step(a_uv, -rat_mpf(64, 5) / mp.mpf(400), rhs_uv)
    inv_a1_m = rat_mpf(3, 5) / a_uv[2] + rat_mpf(2, 5) / a_uv[0]
    a_ir = [mp.mpf(1) / inv_a1_m, a_uv[1], a_uv[3]]
    for _ in range(600):
        a_ir = gl4_step(a_ir, -rat_mpf(96, 5) / mp.mpf(600), rhs_ir)
    inv_a_gl4 = [mp.mpf(1) / x for x in a_ir]

    e3_prod = prod["E3_z18_holomorphy_projector_splitting_and_r_2_over_5_unification"]
    prod_inva = [mp.mpf(s) for s in e3_prod["two_loop_inv_alpha_IR_at_aGUT40_L32"]]
    gl4_vs_rk4_rel_diff = max(abs(inv_a_gl4[i] - prod_inva[i]) / prod_inva[i] for i in range(3))

    pf3_caught = (r_2bid == Fraction(2, 5) and r_1bid_bad == Fraction(8, 17) and r_1bid_bad != Fraction(2, 5))
    match_prod = (
        [fstr(x) for x in b1_lr_2bid] == e3_prod["b1_chiral_LR_BL_2L_2R_3C"]
        and fstr(r_2bid) == e3_prod["r_LR_chiral_exact"] == "2/5"
        and gl4_vs_rk4_rel_diff < p10(-11)
    )

    return {
        "r_LR_2bid_ref": fstr(r_2bid),
        "pf_ref_3_1bid_r_LR": fstr(r_1bid_bad),
        "gl4_N1000_inv_alpha_IR": [mp.nstr(x, 14) for x in inv_a_gl4],
        "gl4_vs_producer_rk4_rel_diff": mp.nstr(gl4_vs_rk4_rel_diff, 8),
        "matches_producer_E3": match_prod,
        "PF_REF_3_caught": pf3_caught,
        "REF_3_passed": bool(match_prod and pf3_caught),
    }


# ---------------------------------------------------------------------------
# REF_4: Matrix-Exponential Unitary Scrambling & `eigh(M * M^H)` Takagi Check
# ---------------------------------------------------------------------------

def su3_expm(seed: int) -> mp.matrix:
    iu = mp.mpc(0, 1)
    H = mp.zeros(3, 3)
    d0 = rat_mpf((2 * seed + 1) % 5 - 2, 3)
    d1 = rat_mpf((3 * seed + 2) % 7 - 3, 5)
    H[0, 0], H[1, 1], H[2, 2] = d0, d1, -(d0 + d1)
    for r in range(3):
        for c in range(r + 1, 3):
            z = rat_mpf((4 * seed + r + 3 * c + 1) % 11 - 5, 8) + iu * rat_mpf((7 * seed + 2 * r + c + 3) % 13 - 6, 10)
            H[r, c] = z
            H[c, r] = mp.conj(z)
    return mp.expm(iu * H)


def takagi_eigh_mmh(m_sym: mp.matrix) -> tuple[list[mp.mpf], mp.matrix, mp.mpf]:
    with mp.workdps(45):
        iu = mp.mpc(0, 1)
        mmh = rat_mpf(1, 2) * (m_sym * m_sym.H + (m_sym * m_sym.H).H)
        evs, u_mat = mp.eigh(mmh)
        ord_i = sorted(range(3), key=lambda k: mp.re(evs[k]))
        sv = [mp.sqrt(max(mp.mpf(0), mp.re(evs[k]))) for k in ord_i]
        w_tak = mp.zeros(3, 3)
        for col, k in enumerate(ord_i):
            uk = u_mat[:, k]
            ukc = mp.matrix([mp.conj(uk[r]) for r in range(3)])
            ph = mp.exp(-iu * mp.arg((uk.H * m_sym * ukc)[0, 0]) / mp.mpf(2))
            for r in range(3):
                w_tak[r, col] = ukc[r] * ph
        res_err = mp.norm(w_tak.T * m_sym * w_tak - mp.diag(sv))
        return sv, w_tak, res_err


def run_ref4_expm_seesaw_and_lepto(prod: dict[str, object]) -> dict[str, object]:
    mp.mp.dps = 45
    iu = mp.mpc(0, 1)
    Yu = mp.matrix([
        [rat_mpf(1, 400), rat_mpf(1, 80) + iu * rat_mpf(1, 120), rat_mpf(1, 90)],
        [rat_mpf(1, 90), rat_mpf(1, 18), rat_mpf(1, 22) + iu * rat_mpf(1, 35)],
        [rat_mpf(1, 150), rat_mpf(1, 24), rat_mpf(4, 5)],
    ])
    Yd = mp.matrix([
        [rat_mpf(1, 180), rat_mpf(1, 38), rat_mpf(1, 110) * iu],
        [rat_mpf(1, 40) - iu * rat_mpf(1, 70), rat_mpf(1, 14), rat_mpf(1, 19)],
        [rat_mpf(1, 120), rat_mpf(1, 20), rat_mpf(3, 5)],
    ])
    Ye = mp.matrix([
        [rat_mpf(1, 250), rat_mpf(1, 90), mp.mpf(0)],
        [rat_mpf(1, 95), rat_mpf(1, 16), rat_mpf(1, 25) * iu],
        [mp.mpf(0), rat_mpf(1, 22), rat_mpf(1, 2)],
    ])
    Ynu = mp.matrix([
        [rat_mpf(1, 60), rat_mpf(1, 15) + iu * rat_mpf(1, 18), rat_mpf(1, 12)],
        [rat_mpf(1, 25) - iu * rat_mpf(1, 22), rat_mpf(1, 6), rat_mpf(1, 9) + iu * rat_mpf(1, 11)],
        [rat_mpf(1, 30), rat_mpf(1, 10) - iu * rat_mpf(1, 14), rat_mpf(1, 2)],
    ])
    MR = mp.matrix([
        [rat_mpf(1, 5), rat_mpf(1, 25) * iu, rat_mpf(1, 40)],
        [rat_mpf(1, 25) * iu, rat_mpf(1, 2), rat_mpf(1, 20)],
        [rat_mpf(1, 40), rat_mpf(1, 20), mp.mpf(1)],
    ])

    def left_u_from_her(m: mp.matrix) -> mp.matrix:
        mmh = rat_mpf(1, 2) * (m * m.H + (m * m.H).H)
        evs, u_m = mp.eigh(mmh)
        oi = sorted(range(3), key=lambda k: mp.re(evs[k]))
        return mp.matrix([[u_m[r, oi[c]] for c in range(3)] for r in range(3)])

    def eval_obs(yu_m: mp.matrix, yd_m: mp.matrix, ye_m: mp.matrix, yn_m: mp.matrix, mr_m: mp.matrix) -> dict[str, mp.mpf]:
        uu_a = left_u_from_her(yu_m)
        ud_a = left_u_from_her(yd_m)
        ue_a = left_u_from_her(ye_m)
        vc = uu_a.H * ud_a
        m_nu = -yn_m * (mr_m ** (-1)) * yn_m.T
        s_nu, u_nu, err_nu = takagi_eigh_mmh(m_nu)
        assert err_nu < p10(-38)
        u_nu_c = mp.matrix([[mp.conj(u_nu[r, c]) for c in range(3)] for r in range(3)])
        upmns = ue_a.H * u_nu_c
        s_mr, u_mr, err_mr = takagi_eigh_mmh(mr_m)
        assert err_mr < p10(-38)
        yt = ue_a.H * yn_m * u_mr
        ht = yt.H * yt
        h00 = mp.re(ht[0, 0])
        efl = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
        for j in (1, 2):
            xv = (s_mr[j] / s_mr[0]) ** 2
            gm = mp.re(ht[j, j]) / (mp.mpf(8) * mp.pi)
            dn = (xv - mp.mpf(1)) ** 2 + xv * (gm ** 2)
            f_sv = mp.sqrt(xv) * ((mp.mpf(1) - xv) / dn + mp.mpf(1) - (mp.mpf(1) + xv) * mp.log(mp.mpf(1) + mp.mpf(1) / xv))
            g_os = (mp.mpf(1) - xv) / dn
            for al in range(3):
                p1j = mp.conj(yt[al, 0]) * yt[al, j]
                efl[al] += (mp.im(p1j * ht[0, j]) * f_sv + mp.im(p1j * ht[j, 0]) * g_os) / (mp.mpf(8) * mp.pi * h00)
        pbr = [(abs(yt[a, 0]) ** 2) / h00 for a in range(3)]
        k1 = h00 * rat_mpf(500, 1)
        yb = -rat_mpf(8, 23) * ((efl[0] + efl[1]) / (mp.mpf(1) + (pbr[0] + pbr[1]) * k1) + efl[2] / (mp.mpf(1) + pbr[2] * k1))
        return {
            "det_MR": abs(mp.det(mr_m)),
            "v12": abs(vc[0, 1]),
            "u12": abs(upmns[0, 1]),
            "r23": s_nu[1] / s_nu[2],
            "yb": yb,
        }

    o0 = eval_obs(Yu, Yd, Ye, Ynu, MR)
    UQ, Uu, Ud, UL, Ue = su3_expm(11), su3_expm(12), su3_expm(13), su3_expm(14), su3_expm(15)
    UN = su3_expm(16) * mp.exp(iu * rat_mpf(3, 11))
    UN_c = mp.matrix([[mp.conj(UN[r, c]) for c in range(3)] for r in range(3)])
    oscr = eval_obs(UQ * Yu * Uu.H, UQ * Yd * Ud.H, UL * Ye * Ue.H, UL * Ynu * UN.H, UN_c * MR * UN.H)
    expm_scr_err = max(abs(o0[k] - oscr[k]) for k in o0)

    # Planted Referee Fault PF_REF_4: Non-symmetric Majorana matrix breaks Takagi residual:
    MR_nonsym = MR.copy()
    MR_nonsym[0, 2] = rat_mpf(1, 5)
    _, _, bad_takagi_err = takagi_eigh_mmh(MR_nonsym)
    pf4_caught = (bad_takagi_err > rat_mpf(1, 20))

    e4_prod = prod["E4_full_rank_seesaw_ckm_2flavor_lepto_and_scrambling"]
    prod_diff = max(
        abs(o0["det_MR"] - mp.mpf(e4_prod["abs_det_MR"])),
        abs(o0["v12"] - mp.mpf(e4_prod["ckm_moduli_v12_v23_v13"][0])),
        abs(o0["u12"] - mp.mpf(e4_prod["pmns_moduli_u12_u23_u13"][0])),
        abs(o0["r23"] - mp.mpf(e4_prod["nu_mass_ratios_13_23"][1])),
        abs(o0["yb"] - mp.mpf(e4_prod["yb_2flavor_proxy"])),
    )
    match_prod = (prod_diff < p10(-9) and expm_scr_err < p10(-30))

    return {
        "expm_scramble_max_err": mp.nstr(expm_scr_err, 8),
        "ref_vs_producer_max_abs_diff": mp.nstr(prod_diff, 8),
        "pf_ref_4_nonsymmetric_takagi_residual": mp.nstr(bad_takagi_err, 8),
        "matches_producer_E4": match_prod,
        "PF_REF_4_caught": pf4_caught,
        "REF_4_passed": bool(match_prod and pf4_caught),
    }


# ---------------------------------------------------------------------------
# REF_5: Chiral-Weyl 4x4 Clifford Basis & Stationary-Point Hessian Minimization
# ---------------------------------------------------------------------------

def run_ref5_chiral_clifford_and_stationary_hessian(prod: dict[str, object]) -> dict[str, object]:
    # 1. Full scalar potential V(H_u, H_d, S) solved at dV/dv_i = 0 (no hand-inserted tadpoles!):
    vu, vd, vS, mu2, md2, mS2, muSH, kapS = sp.symbols("vu vd vS mu2 md2 mS2 muSH kapS", positive=True, real=True)
    ru, rd, rS, iu_s, id_s, aS = sp.symbols("ru rd rS iu_s id_s aS", real=True)
    Hu0 = (vu + ru + sp.I * iu_s) / sp.sqrt(2)
    Hd0 = (vd + rd + sp.I * id_s) / sp.sqrt(2)
    Sc = (vS + rS + sp.I * aS) / sp.sqrt(2)
    V_full = sp.expand(
        mu2 * Hu0 * sp.conjugate(Hu0)
        + md2 * Hd0 * sp.conjugate(Hd0)
        + mS2 * Sc * sp.conjugate(Sc)
        - (kapS / 3) * (Sc ** 3 + sp.conjugate(Sc) ** 3)
        - muSH * (Sc * Hu0 * Hd0 + sp.conjugate(Sc * Hu0 * Hd0))
    )
    vac = {ru: 0, rd: 0, rS: 0, iu_s: 0, id_s: 0, aS: 0}
    sol_m2 = sp.solve(
        [
            sp.diff(V_full, ru).subs(vac),
            sp.diff(V_full, rd).subs(vac),
            sp.diff(V_full, rS).subs(vac),
        ],
        [mu2, md2, mS2],
        dict=True,
    )[0]
    V_stat = V_full.subs(sol_m2)
    odd_vars = [id_s, iu_s, aS]
    M_odd_ref = sp.Matrix([[sp.simplify(sp.diff(V_stat, x, y).subs(vac)) for y in odd_vars] for x in odd_vars])
    gold_ok = (sp.simplify(M_odd_ref * sp.Matrix([-vd, vu, 0])) == sp.zeros(3, 1))
    vew = sp.sqrt(vu ** 2 + vd ** 2)
    P_orth = sp.Matrix.hstack(sp.Matrix([vu / vew, vd / vew, 0]), sp.Matrix([0, 0, 1]))
    M_phys_ref = sp.simplify(P_orth.T * M_odd_ref * P_orth)
    det_ref = sp.factor(M_phys_ref.det())
    det_target = 3 * kapS * muSH * (vS ** 2) * (vu ** 2 + vd ** 2) / (2 * vu * vd)

    # 2. Chiral-Weyl 4x4 Clifford representation (gamma^0 = [[0, I_2], [I_2, 0]] != Dirac basis!):
    i2, z2 = sp.eye(2), sp.zeros(2, 2)
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    gam_w = [
        sp.BlockMatrix([[z2, i2], [i2, z2]]).as_explicit(),
        sp.BlockMatrix([[z2, s1], [-s1, z2]]).as_explicit(),
        sp.BlockMatrix([[z2, s2], [-s2, z2]]).as_explicit(),
        sp.BlockMatrix([[z2, s3], [-s3, z2]]).as_explicit(),
    ]
    g5_w = sp.I * gam_w[0] * gam_w[1] * gam_w[2] * gam_w[3]
    c_w = sp.I * gam_w[2] * gam_w[0]
    maj_pscal_ok = ((c_w.inv() * g5_w).T == -(c_w.inv() * g5_w))

    E, p, m, mf, cos_t, Nc, g_ca, g_fa, M_med = sp.symbols("E p m mf cos_t Nc g_ca g_fa M_med", positive=True, real=True)

    def sl_w(v: list[sp.Expr]) -> sp.Matrix:
        return v[0] * gam_w[0] - v[1] * gam_w[1] - v[2] * gam_w[2] - v[3] * gam_w[3]

    ps1 = sl_w([E, sp.Integer(0), sp.Integer(0), p]) + m * sp.eye(4)
    ps2 = sl_w([E, sp.Integer(0), sp.Integer(0), -p]) - m * sp.eye(4)
    kf = sp.sqrt(E ** 2 - mf ** 2)
    ks1 = sl_w([E, kf * sp.sqrt(1 - cos_t ** 2), sp.Integer(0), kf * cos_t]) + mf * sp.eye(4)
    ks2 = sl_w([E, -kf * sp.sqrt(1 - cos_t ** 2), sp.Integer(0), -kf * cos_t]) - mf * sp.eye(4)

    tr_init_pscal = sp.simplify((ps1 * (sp.I * g5_w) * ps2 * (sp.I * g5_w)).trace().subs(m ** 2, E ** 2 - p ** 2))
    tr_fin_pscal = sp.simplify((ks1 * (sp.I * g5_w) * ks2 * (sp.I * g5_w)).trace())
    sv_swave_ref = sp.simplify(
        (sp.Integer(1) / (32 * sp.pi * (E ** 2))) * (kf / E) * sp.Rational(1, 4) * Nc * (g_ca ** 2) * (g_fa ** 2)
        * tr_init_pscal.subs(p, 0) * tr_fin_pscal / ((4 * (E ** 2) - (M_med ** 2)) ** 2)
    ).subs(E, m)
    sv_target = Nc * (g_ca ** 2) * (g_fa ** 2) * m * sp.sqrt(m ** 2 - mf ** 2) / (2 * sp.pi * ((M_med ** 2 - 4 * (m ** 2)) ** 2))

    # Planted Referee Fault PF_REF_5: CP-even scalar vertex (1 instead of i*gamma_5) vanishes at p -> 0 (pure p-wave!):
    tr_init_scalar_p0 = sp.simplify((ps1 * ps2).trace().subs(m ** 2, E ** 2 - p ** 2)).subs(p, 0)
    pf5_caught = (tr_init_scalar_p0 == 0 and tr_init_pscal.subs(p, 0) == 8 * (E ** 2))

    e5_prod = prod["E5_matter_parity_pseudoscalar_portal_and_swave_majorana_dm"]
    det_prod_expr = sp.sympify(
        e5_prod["det_M_phys_2x2_exact"],
        locals={"kapS": kapS, "muSH": muSH, "vS": vS, "vd": vd, "vu": vu},
    )
    match_prod = (
        gold_ok
        and sp.simplify(det_ref - det_target) == 0
        and sp.simplify(det_ref - det_prod_expr) == 0
        and maj_pscal_ok
        and sp.simplify(sv_swave_ref - sv_target) == 0
    )

    return {
        "stationary_goldstone_exact": gold_ok,
        "stationary_det_M_phys_2x2": str(det_ref),
        "chiral_weyl_swave_sigma_v": str(sv_swave_ref),
        "pf_ref_5_cp_even_scalar_trace_at_v0": int(tr_init_scalar_p0),
        "matches_producer_E5": match_prod,
        "PF_REF_5_caught": pf5_caught,
        "REF_5_passed": bool(match_prod and pf5_caught),
    }


# ---------------------------------------------------------------------------
# REF_6: SHA-256 Custody Audit, Casimir, Vissani Scaling, & Z'_psi Tadpole Fault
# ---------------------------------------------------------------------------

def run_ref6_custody_stability_and_ledger(prod: dict[str, object]) -> dict[str, object]:
    mp.mp.dps = 40
    v1_sha_intact = verify_manifest_line(V1_SCRIPT_SHA)
    v2_script_sha_ok = verify_manifest_line(V2_SCRIPT_SHA)
    v2_out_sha_ok = verify_manifest_line(V2_OUT_SHA)

    # Independent computation of Vissani suppression & 6D untwisted Casimir:
    vissani_ref = mp.exp(-rat_mpf(192, 5))
    casimir_6d_ref = 2 * 78 - 2 * (3 * 27)

    # Planted Referee Fault PF_REF_6: Keeping an unbroken 4D U(1)_psi vector Z'_psi at |S| = exp(32) * v_EW
    # generates OW19-B1 Higgs mass-squared shift |delta m_H^2| / v_EW^2 = (g^4 / 24 pi^2) * (|S|/v_EW)^2 * (1/3) >> 10^{20}!
    g_sq_bench = mp.mpf(4) * mp.pi * rat_mpf(1, 40)
    planted_zprime_wall_over_vew2 = ((g_sq_bench ** 2) / (mp.mpf(72) * (mp.pi ** 2))) * mp.exp(mp.mpf(64))
    pf6_caught = (planted_zprime_wall_over_vew2 > p10(22))

    e6_prod = prod["E6_radiative_higgs_stability_6d_casimir_and_guardrail5_ledger"]
    viss_diff = abs(vissani_ref - mp.mpf(e6_prod["vissani_cubic_suppression_at_r_2_5_L32"])) / vissani_ref
    match_prod = (
        v1_sha_intact and v2_script_sha_ok and v2_out_sha_ok
        and casimir_6d_ref == e6_prod["untwisted_6d_bulk_casimir_computed"] == -6
        and viss_diff < p10(-6)
    )

    return {
        "v1_script_sha256_preserved": v1_sha_intact,
        "v2_script_sha256_verified": v2_script_sha_ok,
        "v2_output_sha256_verified": v2_out_sha_ok,
        "untwisted_6d_casimir_ref": casimir_6d_ref,
        "vissani_suppression_ref": mp.nstr(vissani_ref, 8),
        "pf_ref_6_4d_Zprime_wall_over_vew2": mp.nstr(planted_zprime_wall_over_vew2, 6),
        "matches_producer_E6": match_prod,
        "PF_REF_6_caught": pf6_caught,
        "REF_6_passed": bool(match_prod and pf6_caught),
    }


def assert_json_float_free(obj: object) -> None:
    if isinstance(obj, float):
        raise AssertionError(f"JSON float found: {obj!r}")
    if isinstance(obj, dict):
        for v in obj.values():
            assert_json_float_free(v)
    elif isinstance(obj, list):
        for v in obj:
            assert_json_float_free(v)


def main() -> None:
    ast_res = self_ast_scan()
    assert ast_res["ast_clean"], f"Referee AST scan failed: {ast_res}"
    prod = json.loads(V2_OUT.read_text(encoding="utf-8"))

    r1 = run_ref1_bourbaki_dynkin_e6(prod)
    r2 = run_ref2_weight_anomalies_and_dm_lock(prod)
    r3 = run_ref3_gl4_unification(prod)
    r4 = run_ref4_expm_seesaw_and_lepto(prod)
    r5 = run_ref5_chiral_clifford_and_stationary_hessian(prod)
    r6 = run_ref6_custody_stability_and_ledger(prod)

    mods = [r1["REF_1_passed"], r2["REF_2_passed"], r3["REF_3_passed"], r4["REF_4_passed"], r5["REF_5_passed"], r6["REF_6_passed"]]
    pfs = [r1["PF_REF_1_caught"], r2["PF_REF_2_caught"], r3["PF_REF_3_caught"], r4["PF_REF_4_caught"], r5["PF_REF_5_caught"], r6["PF_REF_6_caught"]]

    out = {
        "card": "X-E6PS-LINK23",
        "role": "disjoint_cold_room_referee",
        "empirical_firewall": "0 of 19",
        "self_ast_zero_float_and_complex_scan": ast_res,
        "REF_1_bourbaki_dynkin_e6_splitting_and_quartic_trace": r1,
        "REF_2_explicit_17state_weight_anomalies_and_mod9_dm_lock": r2,
        "REF_3_implicit_gl4_2loop_unification_countercheck": r3,
        "REF_4_matrix_expm_scrambling_and_eigh_takagi_seesaw": r4,
        "REF_5_chiral_weyl_clifford_and_stationary_hessian_dm": r5,
        "REF_6_sha256_custody_casimir_and_zprime_wall_countercheck": r6,
        "all_6_referee_modules_passed": all(mods),
        "referee_planted_faults_caught": sum(1 for x in pfs if x),
        "referee_planted_faults_total": len(pfs),
        "all_6_referee_planted_faults_caught": all(pfs),
    }

    assert_json_float_free(out)
    assert out["all_6_referee_modules_passed"], f"Failed referee modules: {[i for i, ok in enumerate(mods) if not ok]}"
    assert out["all_6_referee_planted_faults_caught"], "Not all referee planted faults caught!"

    OUT_PATH.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_PATH} cleanly (6/6 referee modules passed, 6/6 referee planted faults caught).")


if __name__ == "__main__":
    main()
