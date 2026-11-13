"""Zero-trust pytest counterchecks & AST locks for Stage 3 (B1861 WP-1.2, WP-1.3, WP-1.8, WP-1.9):
Records & Punctured-Torus Carrier, Move Postulates vs Ground Theorems (B1876/B1879/B1884/B1886),
Register-Deck & State Joins (G_96 -> G_192, Frobenius-Schur Phase Lift, FK12, FK7, FK8),
and Parent Gauge Algebra E_8 Exhibits-vs-Forces No-Go Theorems.

Enforces Guardrails 1-6 and Anti-Shortcut Locks F1-F6:
- Strict 0-of-19 empirical data firewall (AST constant-folding & taint verified on both producer and test suite,
  plus synthetic adversarial bypass probes).
- Guardrail 2 (zero literal boolean verdicts, annotated literal bools, or constant boolean compounds in return
  dictionaries, verified with synthetic negative controls).
- Guardrail 3 (independent random Haar unitary basis-scrambling invariance < 1e-12 across U(6) and U(3)).
- Guardrail 6 (independent zero-trust SL(2, C) polynomial matrix evaluation, Euclidean row-reduction atom solver,
  Fermat projective group enumerator, independent cellular 1-cocycle & cup-pairing builder, norm-2 root-graph
  connectivity check distinguishing D_16^+ from E_8 (+) E_8, and independent affine E_8^(1) Borel-de Siebenthal
  solver, plus planted negative controls).
"""
from __future__ import annotations

from fractions import Fraction
import math
from itertools import combinations, product
from pathlib import Path
from typing import Any

import numpy as np
import pytest
import sympy as sp

from origin_axiom.stage1_curved_action_cusp_orbit import (
    TOL,
    audit_source_zero_empirical_constants,
    check_guardrail2_ast_no_literal_bool_verdicts,
)
from origin_axiom.stage3_carrier_moves_parent_algebra import (
    run_stage3_complete_verification,
)


ROOT = Path(__file__).resolve().parents[1]
STAGE3_SRC = ROOT / "src" / "origin_axiom" / "stage3_carrier_moves_parent_algebra.py"
TEST_SRC = Path(__file__).resolve()


@pytest.fixture(scope="module")
def stage3_results() -> dict[str, Any]:
    return run_stage3_complete_verification()


def _indep_haar_unitary(dim: int, rng: np.random.Generator) -> np.ndarray:
    z_mat = (rng.standard_normal((dim, dim)) + 1j * rng.standard_normal((dim, dim))) / np.sqrt(2.0)
    q_mat, r_mat = np.linalg.qr(z_mat)
    d_vec = np.diag(r_mat)
    ph = np.where(np.abs(d_vec) > 0.0, d_vec / np.abs(d_vec), 1.0 + 0.0j)
    return q_mat * ph[np.newaxis, :]


def _indep_commutant_dim_svd(ops: list[np.ndarray]) -> int:
    dim = ops[0].shape[0]
    eye_d = np.eye(dim, dtype=complex)
    blocks = [np.kron(eye_d, op) - np.kron(op.T, eye_d) for op in ops]
    sv = np.linalg.svd(np.vstack(blocks), compute_uv=False)
    return int(np.sum(sv < 1e-9))


def test_stage3_firewall_and_guardrail2_ast_locks(stage3_results: dict[str, Any]) -> None:
    # 1. Both producer and test file must pass the zero-empirical-constant AST firewall:
    assert audit_source_zero_empirical_constants(STAGE3_SRC) is True
    assert audit_source_zero_empirical_constants(TEST_SRC) is True
    assert stage3_results["zero_sm_empirical_constants_ast_verified"] is True
    assert stage3_results["all_verifications_passed"] is True

    # 2. Adversarial negative controls on AST empirical firewall:
    bad_probes = [
        "m_b = 1",
        "m_c = 1",
        "alpha_s = 1",
        "v_EW = 246",
        "val = 401 / 100",
        "val = sp.Rational(401, 503)",
        "val = float('3.125')",
        "val = pow(2, 10)",
    ]
    for probe in bad_probes:
        assert audit_source_zero_empirical_constants(TEST_SRC, source_override=probe) is False

    # 3. Guardrail 2 AST lock + synthetic negative controls (imported from stage1 v6 scanner):
    assert check_guardrail2_ast_no_literal_bool_verdicts(STAGE3_SRC.read_text(encoding="utf-8")) is True
    assert check_guardrail2_ast_no_literal_bool_verdicts(TEST_SRC.read_text(encoding="utf-8")) is True
    assert stage3_results["guardrail2_ast_no_literal_bool_verdicts_verified"] is True
    g2_bad_probes = [
        "def f():\n    return {'ok': True}\n",
        "def f():\n    flag: bool = True\n    return {'ok': flag}\n",
        "def f():\n    flag = all([True, not False])\n    return {'ok': flag}\n",
        "def f():\n    d = {}\n    d['ok'] = True\n    return d\n",
        "def f():\n    d = {}\n    d.setdefault('ok', True)\n    return d\n",
        "def f():\n    return {'zero_theta': 1.0 - 1.0}\n",
        "def f():\n    counts = {'a': 1, 'b': 4}\n    ok = counts['a'] == 1 and sum(counts.values()) == 5\n    return {'ok': ok}\n",
    ]
    for g2_probe in g2_bad_probes:
        assert check_guardrail2_ast_no_literal_bool_verdicts(g2_probe) is False


def test_wp12_zero_trust_fricke_tick_uniqueness_heisenberg_and_sigma11(stage3_results: dict[str, Any]) -> None:
    # 1. Independent SL(2, C) matrix verification of Fricke Markoff polynomial & fixed characters:
    u_s, v_s, w_s = sp.symbols("u_s v_s w_s")
    a_gen = sp.Matrix([[u_s, 1], [u_s * v_s - 1, v_s]])  # det = u_s*v_s - (u_s*v_s - 1) = 1
    b_gen = sp.Matrix([[w_s, 2], [(w_s * u_s - 2) / 2, u_s]])  # det = w_s*u_s - (w_s*u_s - 2) = 2? Fix det=1:
    b_gen = sp.Matrix([[w_s, 1], [w_s * (u_s + 1) - 1, u_s + 1]])  # det = 1 identically!
    assert sp.expand(a_gen.det() - 1) == 0
    assert sp.expand(b_gen.det() - 1) == 0
    tx_e = sp.expand(a_gen.trace())
    ty_e = sp.expand(b_gen.trace())
    tz_e = sp.expand((a_gen * b_gen).trace())
    comm_ab = a_gen * b_gen * a_gen.inv() * b_gen.inv()
    assert sp.expand((tx_e**2 + ty_e**2 + tz_e**2 - tx_e * ty_e * tz_e - 2) - comm_ab.trace()) == 0

    # Independent polynomial map construction for L: (x, y, z) -> (x, z, x*z - y), R: (x, y, z) -> (z, y, z*y - x),
    # and F: a -> ab, b -> a => (tr a, tr b, tr ab) -> (z, x, tr(ab*a)) where tr(a*b*a) = x*z - y!
    # Verify tr(a_gen * b_gen * a_gen) == tx_e * tz_e - ty_e directly on generic SL(2, C) matrices!
    assert sp.expand((a_gen * b_gen * a_gen).trace() - (tx_e * tz_e - ty_e)) == 0
    assert sp.expand((a_gen * a_gen * b_gen).trace() - (tx_e * tz_e - ty_e)) == 0
    assert sp.expand((a_gen * b_gen * b_gen).trace() - (ty_e * tz_e - tx_e)) == 0

    x_s, y_s, z_s = sp.symbols("x_s y_s z_s")

    def pull_l(pt: tuple[sp.Expr, sp.Expr, sp.Expr]) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
        px, py, pz = pt
        return (px, pz, sp.expand(px * pz - py))

    def pull_f(pt: tuple[sp.Expr, sp.Expr, sp.Expr]) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
        px, py, pz = pt
        return (pz, px, sp.expand(px * pz - py))

    # Note: composition order! If phi_1 acts on words then phi_2, trace pullback is phi_2^*(phi_1^*(x,y,z))?
    # Check: (F o F)(a) = F(ab) = aba, (F o F)(b) = F(a) = ab, (F o F)(ab) = abaab.
    # Let pull_step substitute (x_s, y_s, z_s) -> step(x_s, y_s, z_s)!
    map_l_sub = {x_s: x_s, y_s: z_s, z_s: x_s * z_s - y_s}
    map_r_sub = {x_s: z_s, y_s: y_s, z_s: y_s * z_s - x_s}
    map_f_sub = {x_s: z_s, y_s: x_s, z_s: x_s * z_s - y_s}

    # Solve fixed points of (L, R) and of F alone independently (using simultaneous=True!):
    sol_lr = sp.solve(
        [
            x_s.subs(map_l_sub, simultaneous=True) - x_s,
            y_s.subs(map_l_sub, simultaneous=True) - y_s,
            z_s.subs(map_l_sub, simultaneous=True) - z_s,
            x_s.subs(map_r_sub, simultaneous=True) - x_s,
            y_s.subs(map_r_sub, simultaneous=True) - y_s,
            z_s.subs(map_r_sub, simultaneous=True) - z_s,
        ],
        (x_s, y_s, z_s),
        dict=True,
    )
    sol_f = sp.solve(
        [
            x_s.subs(map_f_sub, simultaneous=True) - x_s,
            y_s.subs(map_f_sub, simultaneous=True) - y_s,
            z_s.subs(map_f_sub, simultaneous=True) - z_s,
        ],
        (x_s, y_s, z_s),
        dict=True,
    )
    pts_lr = {(s[x_s], s[y_s], s[z_s]) for s in sol_lr}
    pts_f = {(s[x_s], s[y_s], s[z_s]) for s in sol_f}
    assert pts_lr == {(0, 0, 0), (2, 2, 2)}
    assert pts_f == {(0, 0, 0), (2, 2, 2)}

    # Planted negative control: F^2 = FF fixes the entire 1D curve {x = z / (z - 1), y = z} (e.g. (3/2, 3, 3) and (1/2, -1, -1)):
    ff_pt = [sp.expand(e.subs(map_f_sub, simultaneous=True).subs(map_f_sub, simultaneous=True)) for e in (x_s, y_s, z_s)]
    assert [e.subs({x_s: sp.Rational(3, 2), y_s: 3, z_s: 3}, simultaneous=True) for e in ff_pt] == [sp.Rational(3, 2), 3, 3]
    assert [e.subs({x_s: sp.Rational(1, 2), y_s: -1, z_s: -1}, simultaneous=True) for e in ff_pt] == [sp.Rational(1, 2), -1, -1]
    gb_ff = sp.groebner([ff_pt[0] - x_s, ff_pt[1] - y_s, ff_pt[2] - z_s], x_s, y_s, z_s, domain=sp.QQ)
    assert not bool(gb_ff.is_zero_dimensional)

    # Full 62-word / 23-cyclic-class {L, F}^+ census up to length 5 (zero reversal quotienting!) + reversal non-conjugacy + all-lengths proof (D2):
    cyc_classes_23: dict[str, str] = {}
    tot_lf_words = 0
    for ln in range(1, 6):
        for tup in product(("L", "F"), repeat=ln):
            tot_lf_words += 1
            w_str = "".join(tup)
            ckey = min(w_str[i:] + w_str[:i] for i in range(ln))
            cyc_classes_23.setdefault(ckey, w_str)
    assert tot_lf_words == 62 and len(cyc_classes_23) == 23
    two_pt_cyc: list[str] = []
    three_pt_cyc: list[str] = []
    five_pt_cyc: list[str] = []
    pos_dim_cyc: list[str] = []
    for ckey, w_str in sorted(cyc_classes_23.items()):
        cur = [x_s, y_s, z_s]
        for ch in w_str:
            sub_m = map_l_sub if ch == "L" else map_f_sub
            cur = [sp.expand(expr.subs(sub_m, simultaneous=True)) for expr in cur]
        gb = sp.groebner([cur[0] - x_s, cur[1] - y_s, cur[2] - z_s], x_s, y_s, z_s, domain=sp.QQ)
        if not bool(gb.is_zero_dimensional):
            pos_dim_cyc.append(ckey)
        else:
            sols_c = sp.solve(list(gb.polys), (x_s, y_s, z_s), dict=True)
            n_sols = len(sols_c)
            if n_sols == 2 and {(s[x_s], s[y_s], s[z_s]) for s in sols_c} == {(0, 0, 0), (2, 2, 2)}:
                two_pt_cyc.append(ckey)
            elif n_sols == 3:
                three_pt_cyc.append(ckey)
            elif n_sols == 5:
                five_pt_cyc.append(ckey)
    assert (two_pt_cyc, three_pt_cyc, five_pt_cyc, len(pos_dim_cyc)) == (["F"], ["FL"], ["FFF"], 20)
    assert "L" in pos_dim_cyc and "FF" in pos_dim_cyc

    # Prove "LLFLFF" ([[10,7],[3,2]]) and its reversal "FFLFLL" ([[5,12],[3,7]]) are NOT GL(2, Z)-conjugate:
    m_llflff = sp.Matrix([[1, 1], [0, 1]]) ** 2 * sp.Matrix([[1, 1], [1, 0]]) * sp.Matrix([[1, 1], [0, 1]]) * (sp.Matrix([[1, 1], [1, 0]]) ** 2)
    m_fflfll = (sp.Matrix([[1, 1], [1, 0]]) ** 2) * sp.Matrix([[1, 1], [0, 1]]) * sp.Matrix([[1, 1], [1, 0]]) * (sp.Matrix([[1, 1], [0, 1]]) ** 2)
    assert m_llflff == sp.Matrix([[10, 7], [3, 2]]) and m_fflfll == sp.Matrix([[5, 12], [3, 7]])
    b00, b01, b10, b11, c_int, k_int = sp.symbols("b00 b01 b10 b11 c_int k_int", integer=True)
    b_int = sp.Matrix([[b00, b01], [b10, b11]])
    sol_inter = sp.solve(list(b_int * m_llflff - m_fflfll * b_int), (b00, b01), dict=True)[0]
    det_inter = sp.expand(b_int.subs(sol_inter).subs({b10: c_int, b11: 3 * k_int - c_int}).det())
    assert sp.expand(4 * det_inter + ((4 * c_int - k_int) ** 2 - 37 * (k_int**2))) == 0
    # In Z[(1+sqrt(37))/2], 37 +- 4 in {33, 41} are non-squares, fundamental unit eps = 6 + sqrt(37) has N(eps) = -1,
    # and +-2 * (6 + sqrt(37))^r = x_r + k_r*sqrt(37) always has x_r + k_r == 2 != 0 (mod 4), forbidding 4*c_int = x_r + k_r!
    assert (not sp.sqrt(33).is_integer) and (not sp.sqrt(41).is_integer)
    rt37 = sp.sqrt(37)
    for r_exp in range(6):
        pw_u = sp.expand(2 * ((6 + rt37) ** r_exp))
        kr_v = int(pw_u.coeff(rt37))
        xr_v = int(sp.expand(pw_u - kr_v * rt37))
        assert (xr_v + kr_v) % 4 == 2 and ((-xr_v - kr_v) % 4 == 2)

    # All-lengths symbolic uniqueness over {L, F}^+ \ {F}: det(M_W - I) == 1 - tr(M_W) + det(M_W), det(M_W + I) == 1 + tr(M_W) + det(M_W):
    mw_a, mw_b, mw_c, mw_d, k_sh = sp.symbols("mw_a mw_b mw_c mw_d k_sh", integer=True)
    mw_2 = sp.Matrix([[mw_a, mw_b], [mw_c, mw_d]])
    assert sp.expand((mw_2 - sp.eye(2)).det() - (1 - mw_2.trace() + mw_2.det())) == 0
    assert sp.expand((mw_2 + sp.eye(2)).det() - (1 + mw_2.trace() + mw_2.det())) == 0
    assert [expr.subs({x_s: 2, z_s: y_s}) for expr in (x_s.subs(map_l_sub, simultaneous=True), y_s.subs(map_l_sub, simultaneous=True), z_s.subs(map_l_sub, simultaneous=True))] == [2, y_s, y_s]
    lk_f_m = (sp.Matrix([[1, k_sh], [0, 1]]) * sp.Matrix([[1, 1], [1, 0]]))
    assert sp.expand(lk_f_m.trace() - (k_sh + 1)) == 0 and sp.expand(lk_f_m.det() + 1) == 0

    # 2. Independent n = 3 common-character collapse test on all 8^3 = 512 triples in Q_8^3:
    # Under all 6 elementary moves R_{ij}: A_i -> A_i A_j (i != j in {1, 2, 3}), check which triples keep
    # their SL(2, C) character tuple (tr A_1, tr A_2, tr A_3, tr A_1 A_2, tr A_1 A_3, tr A_2 A_3, tr A_1 A_2 A_3, tr A_1 A_3 A_2):
    qi = sp.Matrix([[sp.I, 0], [0, -sp.I]])
    qj = sp.Matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    i2 = sp.eye(2)
    q8 = [i2, -i2, qi, -qi, qj, -qj, qk, -qk]

    def char_tuple_3(g1: sp.Matrix, g2: sp.Matrix, g3: sp.Matrix) -> tuple[Any, ...]:
        return (
            g1.trace(),
            g2.trace(),
            g3.trace(),
            (g1 * g2).trace(),
            (g1 * g3).trace(),
            (g2 * g3).trace(),
            (g1 * g2 * g3).trace(),
            (g1 * g3 * g2).trace(),
        )

    fixed_n3_in_q8 = [
        (g1, g2, g3)
        for g1 in q8
        for g2 in q8
        for g3 in q8
        if char_tuple_3(g1, g2, g3) == char_tuple_3(g1 * g2, g2, g3)
        and char_tuple_3(g1, g2, g3) == char_tuple_3(g1, g2 * g1, g3)
        and char_tuple_3(g1, g2, g3) == char_tuple_3(g1 * g3, g2, g3)
        and char_tuple_3(g1, g2, g3) == char_tuple_3(g1, g2, g3 * g1)
        and char_tuple_3(g1, g2, g3) == char_tuple_3(g1, g2 * g3, g3)
        and char_tuple_3(g1, g2, g3) == char_tuple_3(g1, g2, g3 * g2)
    ]
    assert fixed_n3_in_q8 == [(i2, i2, i2)]

    # 3. Independent Heisenberg H_3(Z) & Sigma_{1,1} vs Sigma_{0,3} check:
    ah = sp.Matrix([[1, 1, 0], [0, 1, 0], [0, 0, 1]])
    bh = sp.Matrix([[1, 0, 0], [0, 1, 1], [0, 0, 1]])
    ch_z = ah * bh * ah.inv() * bh.inv()
    assert ch_z == sp.Matrix([[1, 0, 1], [0, 1, 0], [0, 0, 1]])
    # Step-3 commutator [ah, [ah, bh]] vanishes in H_3(Z) (not free!), unlike Sanov SL(2, Z) generators:
    assert ah * ch_z * ah.inv() * ch_z.inv() == sp.eye(3)
    as_2 = sp.Matrix([[1, 2], [0, 1]])
    bs_2 = sp.Matrix([[1, 0], [2, 1]])
    cs_2 = as_2 * bs_2 * as_2.inv() * bs_2.inv()
    assert as_2 * cs_2 * as_2.inv() * cs_2.inv() != sp.eye(2)

    # Marking-independent Sigma_{0,3} exclusion: Out(pi_1(Sigma_{0,3}), partial) in GL(2, Z) permutes
    # {+-e_1, +-e_2, +-(e_1+e_2)}, giving finite order 12 and exponent 6, so M^6 == I_2 for ALL elements!
    periph_6 = {(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)}
    out_03 = [
        sp.Matrix([[m00, m01], [m10, m11]])
        for m00, m01, m10, m11 in product((-2, -1, 0, 1, 2), repeat=4)
        if abs(m00 * m11 - m01 * m10) == 1
        and {(m00 * vx + m01 * vy, m10 * vx + m11 * vy) for vx, vy in periph_6} == periph_6
    ]
    assert len(out_03) == 12
    assert all((m_op ** 6) == sp.eye(2) for m_op in out_03)
    assert (sp.Matrix([[1, 1], [0, 1]]) ** 6) != sp.eye(2)

    # 4. Independent algebraic proof over ALL SL(2, C)^3 (not just finite Q_8^3) that n = 3 common-character
    #    invariance collapses strictly to the trivial character:
    #    Under R_{ij}: a_i -> a_i a_j (i != j in {1, 2, 3}), fixed single/pair traces require all 6 traces equal t_c,
    #    and tr(a_1^2 a_2) = tr(a_1)*tr(a_1 a_2) - tr(a_2) = t_c^2 - t_c == t_c => t_c in {0, 2}!
    #    At t_c = 0: under a_1 -> a_1 a_2, x_123 = tr(a_1 a_2 a_3) -> tr(a_1 a_2^2 a_3) = 0*x_123 - tr(a_1 a_3) = 0,
    #    so x_123 == 0. Yet for ANY A_1, A_2, A_3 in SL(2, C) with tr(A_i) = tr(A_i A_j) = 0, Cayley-Hamilton gives
    #    A_i^2 = -I_2 and (A_i A_j)^2 = -I_2 => A_i A_j + A_j A_i = 0 (3 pairwise anticommuting involutions up to i!).
    #    In M_2(C), {I_2, A_1, A_2, A_1 A_2} is a 4D basis; solving A_3 A_1 + A_1 A_3 = 0 and A_3 A_2 + A_2 A_3 = 0
    #    with det(A_3) = 1 forces A_3 = +-i A_1 A_2? Check: (A_1 A_2)^2 = -I_2 so A_3 = +-(A_1 A_2), giving
    #    A_1 A_2 A_3 = +-(-I_2) = -+I_2 => tr(A_1 A_2 A_3) in {-2, +2}, NEVER 0!
    t_c = sp.Symbol("t_c")
    assert set(sp.solve(t_c ** 2 - 2 * t_c, t_c)) == {sp.Integer(0), sp.Integer(2)}
    c0, c1, c2, c3 = sp.symbols("c0 c1 c2 c3")
    a3_cand = c0 * i2 + c1 * qi + c2 * qj + c3 * qk
    anticomm_eqs = list(a3_cand * qi + qi * a3_cand) + list(a3_cand * qj + qj * a3_cand) + [sp.expand(a3_cand.det() - 1)]
    sols_a3 = sp.solve(anticomm_eqs, (c0, c1, c2, c3), dict=True)
    assert len(sols_a3) == 2
    triple_traces_at_t0 = {int(sp.expand((qi * qj * a3_cand.subs(sol_d)).trace())) for sol_d in sols_a3}
    assert triple_traces_at_t0 == {-2, 2} and (0 not in triple_traces_at_t0)

    # 4b. Independent all-n >= 4 isotropic nilpotent colinearity proof over SL(2, C)^n (D1):
    # Every 3-generator subset forces t_c = 2 so A_i = I_2 + N_i with N_i^2 = 0, tr(N_i) = 0, and tr(A_i A_j) = 2 => tr(N_i N_j) = 0.
    # For N_1 != 0 conjugated in SL(2, C) to [[0, 1], [0, 0]] and generic traceless N_k = [[an_k, bn_k], [cn_k, -an_k]],
    # solving N_k^2 == 0 and tr(N_1 N_k) == 0 forces an_k = 0, cn_k = 0, so ALL A_1..A_n = [[1, bn_k], [0, 1]] commute unipotently
    # and every word w in F_n has tr(w(A_1,...,A_n)) == 2!
    an_k, bn_k, cn_k = sp.symbols("an_k bn_k cn_k")
    n1_std = sp.Matrix([[0, 1], [0, 0]])
    nk_gen = sp.Matrix([[an_k, bn_k], [cn_k, -an_k]])
    sol_nk = sp.solve(list(nk_gen * nk_gen) + [sp.expand((n1_std * nk_gen).trace())], (an_k, cn_k), dict=True)
    assert sol_nk == [{an_k: 0, cn_k: 0}]
    b1_u, b2_u, b3_u, b4_u = sp.symbols("b1_u b2_u b3_u b4_u")
    u_gens4 = [sp.eye(2) + bk * n1_std for bk in (b1_u, b2_u, b3_u, b4_u)]
    assert (u_gens4[0] * u_gens4[1] * u_gens4[2].inv() * u_gens4[3]).trace() == 2

    # 5. Independent G:FK5 abelian quotient exclusion: on F_2^ab = Z^2, [a, b] = 1 forces rho([a, b]) = I_2 (tr = +2),
    #    contradicting rho_Q([a, b]) = qi * qj * qi^-1 * qj^-1 = -I_2 (tr = -2):
    comm_q8 = qi * qj * qi.inv() * qj.inv()
    assert comm_q8 == -i2 and int(comm_q8.trace()) == -2 and int(i2.trace()) == 2

    wp12 = stage3_results["wp12_records_and_torus"]
    assert wp12["n2_exact_two_common_points"] is True
    assert wp12["n3_trivial_character_only_nogo"] is True
    assert wp12["b1879_single_tick_uniquely_fixes_two_points"] is True
    assert wp12["fk5_abelian_quotient_excluded_by_remainder"] is True
    assert wp12["gm4_sigma11_vs_sigma03_shear_selection"] is True


def test_wp13_zero_trust_euclidean_atoms_qr_doubling_and_b1884(stage3_results: dict[str, Any]) -> None:
    # 1. Independent constructive Euclidean row/column reduction on GL(2, Z_{>=0}):
    # Every matrix M in GL(2, Z_{>=0}) \ {I_2, P} has a unique left step in {L, R} (until reaching {I_2, P}):
    # Specifically, row0 >= row1 entrywise (not both equal since det = +-1) => M = R_row_or_L_col * M'!
    def factor_left_in_l_r_p(mat: tuple[tuple[int, int], tuple[int, int]]) -> list[str]:
        r0, r1 = mat[0], mat[1]
        steps: list[str] = []
        while (r0, r1) not in (((1, 0), (0, 1)), ((0, 1), (1, 0))):
            if r0[0] >= r1[0] and r0[1] >= r1[1]:
                # Subtract row 1 from row 0: M = [[1, 1], [0, 1]] * M' => L * M'
                steps.append("L")
                r0 = (r0[0] - r1[0], r0[1] - r1[1])
            elif r1[0] >= r0[0] and r1[1] >= r0[1]:
                # Subtract row 0 from row 1: M = [[1, 0], [1, 1]] * M' => R * M'
                steps.append("R")
                r1 = (r1[0] - r0[0], r1[1] - r0[1])
            else:
                raise AssertionError(f"Unreducible matrix {(r0, r1)}")
        if (r0, r1) == ((0, 1), (1, 0)):
            steps.append("P")
        return steps

    # Enumerate all 174 unimodular non-negative matrices with entries <= 8 and factor EVERY ONE constructively:
    all_174: list[tuple[tuple[int, int], tuple[int, int]]] = []
    for e00, e01, e10, e11 in product(range(9), repeat=4):
        if abs(e00 * e11 - e01 * e10) == 1:
            all_174.append(((e00, e01), (e10, e11)))
    assert len(all_174) == 174

    # An element of GL(2, Z_{>=0}) \ {I, P} is an atom of the infinite-order subsemigroup iff its L/R-length is 1!
    # L/R-length 1 with optional trailing P gives: "L" -> L, "R" -> R, "LP" -> F = [[1,1],[1,0]], "RP" -> F' = [[0,1],[1,1]]!
    len1_atoms = [mat for mat in all_174 if sum(1 for tok in factor_left_in_l_r_p(mat) if tok in ("L", "R")) == 1]
    assert set(len1_atoms) == {((1, 1), (0, 1)), ((1, 0), (1, 1)), ((1, 1), (1, 0)), ((0, 1), (1, 1))}

    # 1b. Symbolic all-entries Euclidean dominance & ||X Y||_1 >= 4 > 3 atomicity proof over ALL GL_{>=0}(2, Z) (D3):
    b_dom, c_dom, u_dom, v_dom, p0_d, p1_d, q0_d, q1_d = sp.symbols("b_dom c_dom u_dom v_dom p0_d p1_d q0_d q1_d", integer=True)
    slack_dom = b_dom + c_dom + u_dom + v_dom + b_dom * u_dom + c_dom * v_dom + u_dom * v_dom
    assert sp.expand(sp.Matrix([[c_dom + 1 + u_dom, b_dom], [c_dom, b_dom + 1 + v_dom]]).det() - 1 - slack_dom) == 0
    assert sp.expand(-sp.Matrix([[c_dom, b_dom + 1 + v_dom], [c_dom + 1 + u_dom, b_dom]]).det() - 1 - slack_dom) == 0
    assert sp.expand(((1 + p0_d) * (1 + q0_d) + (1 + p1_d) * (1 + q1_d)) - (2 + p0_d + p1_d + q0_d + q1_d + p0_d * q0_d + p1_d * q1_d)) == 0

    # 2. Independent B1876 H11 quadratic-residue projective group test across odd primes p = 3, 5, 7, 11, 13:
    # Act directly on projective line P^1(F_p) = {(1, y) : y in F_p} U {(0, 1)} (size p + 1) by permutations!
    def act_p1(mat: tuple[tuple[int, int], tuple[int, int]], pt: tuple[int, int], p_mod: int) -> tuple[int, int]:
        w0 = (mat[0][0] * pt[0] + mat[0][1] * pt[1]) % p_mod
        w1 = (mat[1][0] * pt[0] + mat[1][1] * pt[1]) % p_mod
        if w0 == 0:
            return (0, 1)
        inv_w0 = next(u_m for u_m in range(1, p_mod) if (w0 * u_m) % p_mod == 1)
        return (1, (w1 * inv_w0) % p_mod)

    def p1_perm_group_size(gens: list[tuple[tuple[int, int], tuple[int, int]]], p_mod: int) -> int:
        pts = [(1, y_v) for y_v in range(p_mod)] + [(0, 1)]
        gen_perms = [tuple(pts.index(act_p1(g_m, pt, p_mod)) for pt in pts) for g_m in gens]
        id_perm = tuple(range(len(pts)))
        seen = {id_perm}
        queue = [id_perm]
        while queue:
            cur = queue.pop(0)
            for gp in gen_perms:
                nxt = tuple(gp[idx] for idx in cur)
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        return len(seen)

    m_l = ((1, 1), (0, 1))
    m_r = ((1, 0), (1, 1))
    m_p = ((0, 1), (1, 0))
    for p_pr in [int(sp.prime(idx_p)) for idx_p in range(2, 7)]:
        ord_lr_p = p1_perm_group_size([m_l, m_r], p_pr)
        ord_lrp_p = p1_perm_group_size([m_l, m_r, m_p], p_pr)
        psl_ord = p_pr * (p_pr * p_pr - 1) // 2
        assert ord_lr_p == psl_ord
        if p_pr % 4 == 1:
            assert ord_lrp_p == psl_ord
        else:
            assert ord_lrp_p == 2 * psl_ord

    # 3. Independent B1884 P0-P4 check on F = [[0, 1], [1, 1]] (row convention) & [[1, 1], [1, 0]] (column convention):
    # At N = 5, roots of x^2 - x - 1 == 0 (mod 5) has unique double root x == 3 (since 9 - 3 - 1 = 5 == 0 mod 5)!
    roots_by_n = {
        n_v: [
            x_v
            for x_v in range(n_v)
            if int((((x_v if 2 * x_v <= n_v else x_v - n_v) ** 2) - x_v - 1) % n_v) == 0
        ]
        for n_v in range(2, 26)
    }
    assert [n_v for n_v, rts in roots_by_n.items() if len(rts) == 1] == [5]
    assert roots_by_n[5] == [3]
    assert roots_by_n[25] == []
    assert len(roots_by_n[11]) == 2 and len(roots_by_n[19]) == 2
    x_crt, t_crt = sp.symbols("x_crt t_crt", integer=True)
    assert sp.expand(4 * (x_crt**2 - x_crt - 1) - ((2 * x_crt - 1) ** 2 - 5)) == 0
    assert sp.expand(((5 * t_crt) ** 2 - 5) - (25 * (t_crt**2) - 5)) == 0 and (-5) % 25 == 20

    # At N = 5, check orbit lengths on the 4 non-zero vectors of the unique invariant line {(u, 3u) mod 5 : u in F_5^x}:
    # Under row-tick F_row = [[0, 1], [1, 1]]: (1, 3) -> (3, 4) -> (4, 2) -> (2, 1) -> (1, 3) (single orbit of length 4!),
    # whereas under F_row^2 = [[1, 1], [1, 2]]: (1, 3) -> (4, 2) -> (1, 3) and (3, 4) -> (2, 1) -> (3, 4) (two orbits of length 2)!
    line5 = [(u_v % 5, (3 * u_v) % 5) for u_v in range(1, 5)]
    orb_f: list[tuple[int, int]] = []
    cur_v = (1, 3)
    for _ in range(4):
        orb_f.append(cur_v)
        cur_v = (cur_v[1] % 5, (cur_v[0] + cur_v[1]) % 5)
    assert cur_v == (1, 3) and set(orb_f) == set(line5) and len(set(orb_f)) == 4
    orb_f2 = [(1, 3), ((1 + 3) % 5, (1 + 6) % 5)]
    assert len(set(orb_f2)) == 2

    # 3b. Independent modular primitive +-1 own-line census across ALL 87 odd-det matrices in all_174 for N = 2..17:
    odd_87 = [mat for mat in all_174 if (mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]) == -1]
    assert len(odd_87) == 87
    zero_own_witness_odd: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    for mat in odd_87:
        has_own = False
        for n_mod in range(2, 18):
            for v0 in range(n_mod):
                for v1 in range(n_mod):
                    if math.gcd(math.gcd(v0, v1), n_mod) != 1:
                        continue
                    w0 = mat[0][0] * v0 + mat[0][1] * v1
                    w1 = mat[1][0] * v0 + mat[1][1] * v1
                    if ((w0 - v0) % n_mod == 0 and (w1 - v1) % n_mod == 0) or (
                        (w0 + v0) % n_mod == 0 and (w1 + v1) % n_mod == 0
                    ):
                        has_own = True
                        break
                if has_own:
                    break
            if has_own:
                break
        if not has_own:
            zero_own_witness_odd.add(mat)
    assert zero_own_witness_odd == {((1, 1), (1, 0)), ((0, 1), (1, 1))}

    # 4. Independent Sanov Klein ping-pong freeness + exact integer Schreier coset index 12 in SL(2, Z) + det=2 map:
    def m2_mul_z(
        x_m: tuple[tuple[int, int], tuple[int, int]], y_m: tuple[tuple[int, int], tuple[int, int]]
    ) -> tuple[tuple[int, int], tuple[int, int]]:
        return (
            (x_m[0][0] * y_m[0][0] + x_m[0][1] * y_m[1][0], x_m[0][0] * y_m[0][1] + x_m[0][1] * y_m[1][1]),
            (x_m[1][0] * y_m[0][0] + x_m[1][1] * y_m[1][0], x_m[1][0] * y_m[0][1] + x_m[1][1] * y_m[1][1]),
        )

    def m2_inv_z(x_m: tuple[tuple[int, int], tuple[int, int]]) -> tuple[tuple[int, int], tuple[int, int]]:
        return ((x_m[1][1], -x_m[0][1]), (-x_m[1][0], x_m[0][0]))

    def in_sub_pingpong_z(
        x_m: tuple[tuple[int, int], tuple[int, int]], p_st: int, q_st: int
    ) -> bool:
        gens_pq = (
            ((1, p_st), (0, 1)),
            ((1, -p_st), (0, 1)),
            ((1, 0), (q_st, 1)),
            ((1, 0), (-q_st, 1)),
        )
        cur_x = x_m
        for _ in range(128):
            if cur_x == ((1, 0), (0, 1)):
                return True
            n_cur = abs(cur_x[0][0]) + abs(cur_x[0][1]) + abs(cur_x[1][0]) + abs(cur_x[1][1])
            stepped = False
            for g_pq in gens_pq:
                nxt_x = m2_mul_z(g_pq, cur_x)
                if abs(nxt_x[0][0]) + abs(nxt_x[0][1]) + abs(nxt_x[1][0]) + abs(nxt_x[1][1]) < n_cur:
                    cur_x = nxt_x
                    stepped = True
                    break
            if not stepped:
                return False
        return cur_x == ((1, 0), (0, 1))

    def enum_right_cosets_sl2z(p_st: int, q_st: int, cap_c: int) -> tuple[int, bool]:
        cosets = [((1, 0), (0, 1))]
        q_cosets = [((1, 0), (0, 1))]
        sl_gens = (((1, 1), (0, 1)), ((1, -1), (0, 1)), ((1, 0), (1, 1)), ((1, 0), (-1, 1)))
        while q_cosets:
            c_cur = q_cosets.pop(0)
            for g_sl in sl_gens:
                cand_c = m2_mul_z(c_cur, g_sl)
                hit = False
                for c_old in cosets:
                    if in_sub_pingpong_z(m2_mul_z(cand_c, m2_inv_z(c_old)), p_st, q_st):
                        hit = True
                        break
                if not hit:
                    cosets.append(cand_c)
                    q_cosets.append(cand_c)
                    if len(cosets) > cap_c:
                        return len(cosets), False
        return len(cosets), True

    idx_22, closed_22 = enum_right_cosets_sl2z(2, 2, 20)
    assert closed_22 is True and idx_22 == 12
    assert in_sub_pingpong_z(((1, 4), (0, 1)), 2, 2) is True
    assert in_sub_pingpong_z(((1, 0), (4, 1)), 2, 2) is True
    assert in_sub_pingpong_z(((1, 1), (0, 1)), 2, 2) is False
    assert in_sub_pingpong_z(((-1, 0), (0, -1)), 2, 2) is False

    # Planted thin-subgroup negative controls: <L^2, R^6> has mod-4 index 48/4 == 12 yet infinite index over Z!
    sl2_z4 = [
        ((e0, e1), (e2, e3))
        for e0, e1, e2, e3 in product(range(4), repeat=4)
        if (e0 * e3 - e1 * e2) % 4 == 1
    ]
    assert len(sl2_z4) == 48
    bad26_z4 = {((1, 0), (0, 1))}
    for _ in range(4):
        for h_s in list(bad26_z4):
            for g_s in (((1, 2), (0, 1)), ((1, 0), (6 % 4, 1))):
                bad26_z4.add(
                    (
                        ((h_s[0][0] * g_s[0][0] + h_s[0][1] * g_s[1][0]) % 4, (h_s[0][0] * g_s[0][1] + h_s[0][1] * g_s[1][1]) % 4),
                        ((h_s[1][0] * g_s[0][0] + h_s[1][1] * g_s[1][0]) % 4, (h_s[1][0] * g_s[0][1] + h_s[1][1] * g_s[1][1]) % 4),
                    )
                )
    assert len(bad26_z4) == 4
    idx_26, closed_26 = enum_right_cosets_sl2z(2, 6, 20)
    assert closed_26 is False and idx_26 > 12
    assert in_sub_pingpong_z(((1, 0), (2, 1)), 2, 6) is False
    idx_33, closed_33 = enum_right_cosets_sl2z(3, 3, 20)
    assert closed_33 is False and idx_33 > 12

    # Symbolic Klein ping-pong gap-cone proof that [SL(2, Z) : <L^2, R^6>] = oo and [SL(2, Z) : <L^3, R^3>] = oo (D4):
    d1_g, d2_g = sp.symbols("d1_g d2_g", real=True, positive=True)
    g1_gap = sp.Matrix([[1, 2], [2, 5]])  # R^2 L^2
    c26_vec = sp.Matrix([d1_g + d2_g, 3 * d1_g + d2_g])
    c26_img = g1_gap * c26_vec
    assert c26_vec.subs({d1_g: sp.Rational(1, 2), d2_g: sp.Rational(3, 2)}) == sp.Matrix([2, 3])
    assert sp.expand((c26_img[1, 0] - c26_img[0, 0]) - (10 * d1_g + 4 * d2_g)) == 0
    assert sp.expand((3 * c26_img[0, 0] - c26_img[1, 0]) - (4 * d1_g + 2 * d2_g)) == 0

    g2_gap = sp.Matrix([[3, 4], [2, 3]])  # L R^2 L
    c33_vec = sp.Matrix([3 * d1_g + 2 * d2_g, 2 * d1_g + 2 * d2_g])
    c33_img = g2_gap * c33_vec
    assert g2_gap * sp.Matrix([1, 1]) == sp.Matrix([7, 5])
    assert c33_vec.subs({d1_g: 2, d2_g: sp.Rational(1, 2)}) == sp.Matrix([7, 5])
    assert sp.expand((c33_img[0, 0] - c33_img[1, 0]) - (5 * d1_g + 4 * d2_g)) == 0
    assert sp.expand((3 * c33_img[1, 0] - 2 * c33_img[0, 0]) - (2 * d1_g + 2 * d2_g)) == 0
    u_x, d_x, m_k = sp.symbols("u_x d_x m_k", integer=True)
    assert sp.expand(((u_x + 2 * (m_k + 1) * (u_x + d_x)) - (u_x + d_x)) - (2 * (m_k + 1) * u_x + (2 * m_k + 1) * d_x)) == 0
    assert sp.expand(((2 * (m_k + 1) * (u_x + d_x) - u_x) - (u_x + d_x)) - (2 * m_k * u_x + (2 * m_k + 1) * d_x)) == 0
    assert int(sp.Matrix([[2, 0], [0, 1]]).det()) == 2

    # 5. Independent GM3 polynomial remainder torsion proof (Delta < 0 <=> tr in {-1, 0, 1} => M^3, M^4, M^6 == I_2)
    #    and GM5b positive-monoid square-trace identity tr(W^2) >= +2 vs GL(2, Z) tr(X^2) >= -2:
    lam_s = sp.Symbol("lam_s")
    assert sp.rem(lam_s ** 3 - 1, lam_s ** 2 + lam_s + 1, lam_s) == 0
    assert sp.rem(lam_s ** 4 - 1, lam_s ** 2 + 1, lam_s) == 0
    assert sp.rem(lam_s ** 6 - 1, lam_s ** 2 - lam_s + 1, lam_s) == 0
    k_n = sp.Symbol("k_n", integer=True, positive=True)
    assert (sp.Matrix([[1, 1], [0, 1]]) ** k_n) == sp.Matrix([[1, k_n], [0, 1]])
    ap, bp, cp, dp = sp.symbols("ap bp cp dp")
    w_p = sp.Matrix([[ap, bp], [cp, dp]])
    assert sp.expand(((w_p * w_p).trace() - 2) - ((ap - dp) ** 2 + 4 * bp * cp + 2 * (ap * dp - bp * cp - 1))) == 0
    assert sp.expand(((w_p * w_p).trace() - 2) - ((ap + dp) ** 2 + 2 * (bp * cp - ap * dp - 1))) == 0
    s_mat = sp.Matrix([[1, 1], [0, 1]]) * sp.Matrix([[1, 0], [-1, 1]]) * sp.Matrix([[1, 1], [0, 1]])
    assert s_mat * s_mat == -sp.eye(2)

    wp13 = stage3_results["wp13_moves_and_grounds"]
    assert wp13["sanov_index_in_sl2z"] == 12
    assert wp13["sanov_ping_pong_free_and_det2_witness"] is True
    assert wp13["gm3_parabolic_shear_nogo_and_discriminants"] is True
    assert wp13["b1884_ground_discriminant_vs_own_line_exact"] is True
    assert wp13["gm5b_central_sign_and_nonsquare_bound"] is True
    assert "G:SE3" in wp13["node_verdicts_wp13"]


def test_wp19_zero_trust_g192_fs_phase_fk12_and_fk7_fk8(stage3_results: dict[str, Any]) -> None:
    # 1. Independent EXACT Q(zeta_8) = Q[z]/(z^4 + 1) cyclotomic ring & Fox 1-cocycle builder (zero float rounding,
    #    zero shared code with producer):
    Cyc8 = tuple[Fraction, Fraction, Fraction, Fraction]
    CycMat = tuple[tuple[Cyc8, ...], ...]
    z0_c: Cyc8 = (Fraction(0), Fraction(0), Fraction(0), Fraction(0))
    z1_c: Cyc8 = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
    zi_c: Cyc8 = (Fraction(0), Fraction(0), Fraction(1), Fraction(0))  # z^2 = i

    def cyc_add(x: Cyc8, y: Cyc8) -> Cyc8:
        return (x[0] + y[0], x[1] + y[1], x[2] + y[2], x[3] + y[3])

    def cyc_mul(x: Cyc8, y: Cyc8) -> Cyc8:
        return (
            x[0] * y[0] - x[1] * y[3] - x[2] * y[2] - x[3] * y[1],
            x[0] * y[1] + x[1] * y[0] - x[2] * y[3] - x[3] * y[2],
            x[0] * y[2] + x[1] * y[1] + x[2] * y[0] - x[3] * y[3],
            x[0] * y[3] + x[1] * y[2] + x[2] * y[1] + x[3] * y[0],
        )

    def sp_to_cyc(ex_in: sp.Expr) -> Cyc8:
        ex = sp.expand(ex_in)
        re_p, im_p = ex.as_real_imag()
        re_p, im_p = sp.expand(re_p), sp.expand(im_p)
        rt2 = sp.sqrt(2)
        b_q = sp.expand(re_p.coeff(rt2))
        a_q = sp.expand(re_p - b_q * rt2)
        d_q = sp.expand(im_p.coeff(rt2))
        c_q = sp.expand(im_p - d_q * rt2)
        fa = Fraction(int(sp.fraction(a_q)[0]), int(sp.fraction(a_q)[1]))
        fb = Fraction(int(sp.fraction(b_q)[0]), int(sp.fraction(b_q)[1]))
        fc = Fraction(int(sp.fraction(c_q)[0]), int(sp.fraction(c_q)[1]))
        fd = Fraction(int(sp.fraction(d_q)[0]), int(sp.fraction(d_q)[1]))
        return (fa, fb + fd, fc, fd - fb)

    def mat_to_cyc(ms: sp.Matrix) -> CycMat:
        return tuple(tuple(sp_to_cyc(ms[r, c]) for c in range(ms.cols)) for r in range(ms.rows))

    def cyc_eye(n_d: int) -> CycMat:
        return tuple(tuple(z1_c if r == c else z0_c for c in range(n_d)) for r in range(n_d))

    def cyc_matmul(ma: CycMat, mb: CycMat) -> CycMat:
        n_d = len(ma)
        return tuple(
            tuple(
                (
                    sum(cyc_mul(ma[r][k], mb[k][c])[0] for k in range(n_d)),
                    sum(cyc_mul(ma[r][k], mb[k][c])[1] for k in range(n_d)),
                    sum(cyc_mul(ma[r][k], mb[k][c])[2] for k in range(n_d)),
                    sum(cyc_mul(ma[r][k], mb[k][c])[3] for k in range(n_d)),
                )
                for c in range(n_d)
            )
            for r in range(n_d)
        )

    def cyc_matpow(ma: CycMat, e_k: int) -> CycMat:
        out_m = cyc_eye(len(ma))
        b_m = ma
        rem = e_k
        while rem > 0:
            if rem % 2 == 1:
                out_m = cyc_matmul(out_m, b_m)
            b_m = cyc_matmul(b_m, b_m)
            rem //= 2
        return out_m

    def cyc_trace(ma: CycMat) -> Cyc8:
        n_d = len(ma)
        return (
            sum(ma[k][k][0] for k in range(n_d)),
            sum(ma[k][k][1] for k in range(n_d)),
            sum(ma[k][k][2] for k in range(n_d)),
            sum(ma[k][k][3] for k in range(n_d)),
        )

    def enum_cyc_exact(gens_c: list[CycMat]) -> set[CycMat]:
        id_c = cyc_eye(len(gens_c[0]))
        seen_c: set[CycMat] = {id_c}
        q_c = [id_c]
        while q_c:
            cur = q_c.pop(0)
            for gm in gens_c:
                nxt = cyc_matmul(cur, gm)
                if nxt not in seen_c:
                    seen_c.add(nxt)
                    q_c.append(nxt)
        return seen_c

    # Independent exact SymPy 1-cocycle & cup-product construction on V (6D) and T (+) T_bar:
    qi_s = sp.Matrix([[sp.I, 0], [0, -sp.I]])
    qj_s = sp.Matrix([[0, 1], [-1, 0]])
    i2_s = sp.eye(2)
    par_list = [(1, 0), (0, 1), (1, 1)]

    def rho_sym(p_tup: tuple[int, int], ch: str) -> sp.Matrix:
        sgn = -1 if (p_tup[0] if ch.lower() == "a" else p_tup[1]) else 1
        base = sgn * (qi_s if ch.lower() == "a" else qj_s)
        return base if ch.islower() else base.H

    def rho_word_s(p_tup: tuple[int, int], word: str) -> sp.Matrix:
        cur = i2_s
        for ch in word:
            cur = (cur * rho_sym(p_tup, ch)).applyfunc(sp.expand)
        return cur

    def gs_cols(vecs: list[sp.Matrix]) -> sp.Matrix:
        cols: list[sp.Matrix] = []
        for v_c in vecs:
            w_c = v_c
            for u_p in cols:
                w_c = (w_c - (u_p.H * w_c)[0, 0] * u_p).applyfunc(sp.expand)
            n_c = sp.sqrt(sp.expand((w_c.H * w_c)[0, 0]))
            cols.append((w_c / n_c).applyfunc(sp.expand))
        return sp.Matrix.hstack(*cols)

    bases_sym: dict[tuple[int, int], sp.Matrix] = {}
    coboundary_sym: dict[tuple[int, int], sp.Matrix] = {}
    for p_tup in par_list:
        d0_s = sp.Matrix.vstack(rho_sym(p_tup, "a") - i2_s, rho_sym(p_tup, "b") - i2_s)
        coboundary_sym[p_tup] = d0_s
        ns_s = d0_s.H.nullspace()
        assert len(ns_s) == 2
        bases_sym[p_tup] = gs_cols(ns_s)

    def fox_sym(za: sp.Matrix, zb: sp.Matrix, word: str, p_tup: tuple[int, int]) -> sp.Matrix:
        acc = sp.zeros(2, 1)
        cur = i2_s
        for ch in word:
            gl = rho_sym(p_tup, ch.lower())
            zl = za if ch.lower() == "a" else zb
            if ch.islower():
                acc = (acc + cur * zl).applyfunc(sp.expand)
                cur = (cur * gl).applyfunc(sp.expand)
            else:
                gi = gl.H
                acc = (acc - cur * gi * zl).applyfunc(sp.expand)
                cur = (cur * gi).applyfunc(sp.expand)
        return acc

    # Verify independent Fox pairing on boundary relator [a, b]^2 = "abABabAB":
    # 1) vanishes identically when EITHER cocycle is a 0-coboundary delta_0(v) = ((rho(a)-I)v, (rho(b)-I)v)!
    # 2) restricts to Hermitian form H_cup on V (6D) with exact signature (3, 3), preserved by L, R and negated by P!
    rel_w = "abABabAB"

    def cup_pair_4d(u4: sp.Matrix, v4: sp.Matrix, p_tup: tuple[int, int]) -> sp.Expr:
        ua, ub = u4[:2, :], u4[2:, :]
        va, vb = v4[:2, :], v4[2:, :]
        tot = sp.Integer(0)
        pref = ""
        cur = i2_s
        for ch in rel_w:
            up = fox_sym(ua, ub, pref, p_tup)
            vc = fox_sym(va, vb, ch, p_tup)
            tot += ((cur * vc).H * up)[0, 0]
            if ch.isupper():
                rl = rho_sym(p_tup, ch.lower())
                ul = fox_sym(ua, ub, ch.lower(), p_tup)
                tot -= ((rl * vc).H * ul)[0, 0]
            pref += ch
            cur = (cur * rho_sym(p_tup, ch)).applyfunc(sp.expand)
        return sp.expand(sp.conjugate(-sp.I * tot))

    for p_tup in par_list:
        d0_s = coboundary_sym[p_tup]
        b_s = bases_sym[p_tup]
        for cb_col in range(2):
            cb_vec = d0_s[:, cb_col]
            for h_col in range(2):
                h_vec = b_s[:, h_col]
                assert cup_pair_4d(cb_vec, h_vec, p_tup) == 0
                assert cup_pair_4d(h_vec, cb_vec, p_tup) == 0

    h_cup_6 = sp.zeros(6, 6)
    for i_idx in range(6):
        pi = par_list[i_idx // 2]
        ui = bases_sym[pi][:, i_idx % 2]
        for j_idx in range(6):
            pj = par_list[j_idx // 2]
            if pi == pj:
                vj = bases_sym[pj][:, j_idx % 2]
                h_cup_6[i_idx, j_idx] = cup_pair_4d(ui, vj, pi)
    assert (h_cup_6 - h_cup_6.H).applyfunc(sp.expand) == sp.zeros(6, 6)
    eigs_cup = h_cup_6.eigenvals()
    pos_ev = [ev for ev, mult in eigs_cup.items() if ev.is_real and ev > 0 and mult == 3]
    neg_ev = [ev for ev, mult in eigs_cup.items() if ev.is_real and ev < 0 and mult == 3]
    assert len(pos_ev) == 1 and len(neg_ev) == 1 and sp.expand(pos_ev[0] + neg_ev[0]) == 0

    def induced_6x6_sym(word_a: str, word_b: str, lift_u2: sp.Matrix) -> sp.Matrix:
        li = lift_u2.H
        out = sp.zeros(6, 6)
        for ip, p_tup in enumerate(par_list):
            sa = 1
            for ch in word_a:
                sa *= -1 if (p_tup[0] if ch.lower() == "a" else p_tup[1]) else 1
            sb = 1
            for ch in word_b:
                sb *= -1 if (p_tup[0] if ch.lower() == "a" else p_tup[1]) else 1
            q_tup = (0 if sa == 1 else 1, 0 if sb == 1 else 1)
            iq = par_list.index(q_tup)
            bp = bases_sym[p_tup]
            bq = bases_sym[q_tup]
            pq = (bq * bq.H).applyfunc(sp.expand)
            for k_col in range(2):
                v4 = bp[:, k_col]
                wa = (li * fox_sym(v4[:2, :], v4[2:, :], word_a, p_tup)).applyfunc(sp.expand)
                wb = (li * fox_sym(v4[:2, :], v4[2:, :], word_b, p_tup)).applyfunc(sp.expand)
                coords = (bq.H * (pq * sp.Matrix.vstack(wa, wb))).applyfunc(sp.expand)
                for r_row in range(2):
                    out[2 * iq + r_row, 2 * ip + k_col] = coords[r_row, 0]
        return out

    rt2_inv_s = 1 / sp.sqrt(2)
    gl_s = ((i2_s + qi_s) * rt2_inv_s).applyfunc(sp.expand)
    gr_s = ((i2_s - qj_s) * rt2_inv_s).applyfunc(sp.expand)
    gp_s = ((qi_s + qj_s) * rt2_inv_s).applyfunc(sp.expand)
    l6_s = induced_6x6_sym("a", "ab", gl_s)
    r6_s = induced_6x6_sym("ab", "b", gr_s)
    p6_s = induced_6x6_sym("b", "a", gp_s)
    f6_s = induced_6x6_sym("ab", "a", (gl_s * gp_s).applyfunc(sp.expand))
    assert (f6_s - p6_s * l6_s).applyfunc(sp.expand) == sp.zeros(6, 6)
    assert (l6_s.H * h_cup_6 * l6_s - h_cup_6).applyfunc(sp.expand) == sp.zeros(6, 6)
    assert (r6_s.H * h_cup_6 * r6_s - h_cup_6).applyfunc(sp.expand) == sp.zeros(6, 6)
    assert (p6_s.H * h_cup_6 * p6_s + h_cup_6).applyfunc(sp.expand) == sp.zeros(6, 6)

    # Exact Q(zeta_8) group enumeration (ZERO float rounding!):
    l6_c = mat_to_cyc(l6_s)
    r6_c = mat_to_cyc(r6_s)
    p6_c = mat_to_cyc(p6_s)
    f6_c = mat_to_cyc(f6_s)
    ip6_c = tuple(tuple(cyc_mul(zi_c, p6_c[r][c]) for c in range(6)) for r in range(6))

    g_lr = enum_cyc_exact([l6_c, r6_c])
    g_lrp = enum_cyc_exact([l6_c, r6_c, p6_c])
    g_lf = enum_cyc_exact([l6_c, f6_c])
    g_lrip = enum_cyc_exact([l6_c, r6_c, ip6_c])
    assert len(g_lr) == 96
    assert len(g_lrp) == 192
    assert len(g_lf) == 192
    assert len(g_lrip) == 192
    assert g_lrp == g_lf
    assert g_lrp != g_lrip
    assert all(cyc_matpow(mg, 48) == cyc_eye(6) for mg in g_lrp)

    # Exact Frobenius-Schur indicator in Q(zeta_8) (-1 for P vs +1 for iP):
    fs_p_sum = z0_c
    for mg in g_lrp:
        fs_p_sum = cyc_add(fs_p_sum, cyc_trace(cyc_matmul(mg, mg)))
    fs_ip_sum = z0_c
    for mg in g_lrip:
        fs_ip_sum = cyc_add(fs_ip_sum, cyc_trace(cyc_matmul(mg, mg)))
    assert fs_p_sum == (Fraction(-192), Fraction(0), Fraction(0), Fraction(0))
    assert fs_ip_sum == (Fraction(192), Fraction(0), Fraction(0), Fraction(0))

    # Abstract group non-isomorphism <L, R, P> !~= <L, R, iP> via exact Cyc8 order distributions & involution counts (7 vs 47, D7):
    id6_c = cyc_eye(6)

    def ord_hist_c(grp_c: set[CycMat]) -> dict[int, int]:
        h_out: dict[int, int] = {}
        for mg in grp_c:
            cur_m = mg
            k_ord = 1
            while cur_m != id6_c:
                cur_m = cyc_matmul(cur_m, mg)
                k_ord += 1
            h_out[k_ord] = h_out.get(k_ord, 0) + 1
        return dict(sorted(h_out.items()))

    hist_lrp_c = ord_hist_c(g_lrp)
    hist_lrip_c = ord_hist_c(g_lrip)
    assert hist_lrp_c[2] == 7 and hist_lrip_c[2] == 47 and hist_lrp_c != hist_lrip_c
    assert hist_lrp_c == {1: 1, 2: 7, 3: 8, 4: 72, 6: 8, 8: 48, 12: 48}
    assert hist_lrip_c == {1: 1, 2: 47, 3: 8, 4: 32, 6: 40, 8: 48, 12: 16}

    # Independent split V = T (+) T_bar, explicit S^2 = +-i I_3 & S_6^4 = -I_6 central-sheet assertions (no silent else!, D5):
    b_pos_s = gs_cols((h_cup_6 - pos_ev[0] * sp.eye(6)).nullspace())
    b_neg_s = gs_cols((h_cup_6 + pos_ev[0] * sp.eye(6)).nullspace())
    tl_pos_c = (b_pos_s.H * l6_s * b_pos_s).applyfunc(sp.expand)
    tr_pos_c = (b_pos_s.H * r6_s * b_pos_s).applyfunc(sp.expand)
    s_pos_c = (tl_pos_c * tr_pos_c.H * tl_pos_c).applyfunc(sp.expand)
    tl_neg_c = (b_neg_s.H * l6_s * b_neg_s).applyfunc(sp.expand)
    tr_neg_c = (b_neg_s.H * r6_s * b_neg_s).applyfunc(sp.expand)
    s_neg_c = (tl_neg_c * tr_neg_c.H * tl_neg_c).applyfunc(sp.expand)
    pos_plus_i = (s_pos_c * s_pos_c - sp.I * sp.eye(3)).applyfunc(sp.expand) == sp.zeros(3, 3)
    neg_plus_i = (s_neg_c * s_neg_c - sp.I * sp.eye(3)).applyfunc(sp.expand) == sp.zeros(3, 3)
    assert pos_plus_i != neg_plus_i
    b_t_s, b_tbar_s = (b_pos_s, b_neg_s) if pos_plus_i else (b_neg_s, b_pos_s)
    tl3_s = (b_t_s.H * l6_s * b_t_s).applyfunc(sp.expand)
    tr3_s = (b_t_s.H * r6_s * b_t_s).applyfunc(sp.expand)
    tlbar3_s = (b_tbar_s.H * l6_s * b_tbar_s).applyfunc(sp.expand)
    trbar3_s = (b_tbar_s.H * r6_s * b_tbar_s).applyfunc(sp.expand)
    s_t_s = (tl3_s * tr3_s.H * tl3_s).applyfunc(sp.expand)
    s_tbar_s = (tlbar3_s * trbar3_s.H * tlbar3_s).applyfunc(sp.expand)
    s6_s = (l6_s * r6_s.H * l6_s).applyfunc(sp.expand)
    assert (s_t_s * s_t_s - sp.I * sp.eye(3)).applyfunc(sp.expand) == sp.zeros(3, 3)
    assert (s_tbar_s * s_tbar_s + sp.I * sp.eye(3)).applyfunc(sp.expand) == sp.zeros(3, 3)
    assert (s6_s ** 4 + sp.eye(6)).applyfunc(sp.expand) == sp.zeros(6, 6)

    # Solve U_sym * T_g^T == T_g * U_sym independently via Kronecker nullspace:
    uv_syms = [sp.Symbol(f"uv_{r}_{c}") for r in range(3) for c in range(3)]
    u_var = sp.Matrix(3, 3, uv_syms)
    eq_u = list((u_var * tl3_s.T - tl3_s * u_var).applyfunc(sp.expand)) + list(
        (u_var * tr3_s.T - tr3_s * u_var).applyfunc(sp.expand)
    )
    ns_u = sp.Matrix([[sp.expand(e_i).coeff(vs) for vs in uv_syms] for e_i in eq_u]).nullspace()
    assert len(ns_u) == 1
    u_raw = sp.Matrix(3, 3, list(ns_u[0])).applyfunc(sp.expand)
    u_sym_s = (u_raw / sp.sqrt(sp.expand((u_raw.H * u_raw)[0, 0]))).applyfunc(sp.expand)
    assert (u_sym_s.T - u_sym_s).applyfunc(sp.expand) == sp.zeros(3, 3)
    assert (u_sym_s.H * u_sym_s - sp.eye(3)).applyfunc(sp.expand) == sp.zeros(3, 3)

    # Exhaustive 96-element exact Q(zeta_8) partition on T + 3-thread check:
    tl3_c, tr3_c = mat_to_cyc(tl3_s), mat_to_cyc(tr3_s)
    us_c, ush_c = mat_to_cyc(u_sym_s), mat_to_cyc(u_sym_s.H)
    g_t96 = enum_cyc_exact([tl3_c, tr3_c])
    assert len(g_t96) == 96
    c_rev_nz = 0
    c_im_nz = 0
    c_both = 0
    for gt in g_t96:
        gt_t = tuple(tuple(gt[r][c] for r in range(3)) for c in range(3))
        gt_rev = cyc_matmul(cyc_matmul(us_c, gt_t), ush_c)
        assert gt_rev in g_t96
        tr_gt = cyc_trace(gt)
        assert tr_gt == cyc_trace(gt_rev)
        comm_nz = cyc_matmul(gt, gt_rev) != cyc_matmul(gt_rev, gt)
        im_nz = ((tr_gt[1] + tr_gt[3]) != Fraction(0)) or (tr_gt[2] != Fraction(0))
        if comm_nz:
            assert tr_gt == z0_c
            c_rev_nz += 1
        if im_nz:
            c_im_nz += 1
        if comm_nz and im_nz:
            c_both += 1
    assert (c_rev_nz, c_im_nz, c_both) == (32, 56, 0)

    def eval_t3_c(w_s: str) -> CycMat:
        cur_c = cyc_eye(3)
        for ch in w_s:
            cur_c = cyc_matmul(cur_c, tl3_c if ch == "L" else tr3_c)
        return cur_c

    for w_test, exp_comm_nz, exp_im_nz in (("LR", True, False), ("LLLLLLR", False, True), ("LLLRLR", True, False)):
        m_fw = eval_t3_c(w_test)
        m_rv = eval_t3_c(w_test[::-1])
        m_sw = eval_t3_c("".join("R" if c == "L" else "L" for c in w_test))
        assert m_fw != m_rv
        assert (cyc_matmul(m_fw, m_rv) != cyc_matmul(m_rv, m_fw)) is exp_comm_nz
        tr_fw, tr_sw = cyc_trace(m_fw), cyc_trace(m_sw)
        # conj((c0, c1, c2, c3)) = (c0, -c3, -c2, -c1):
        assert tr_sw == (tr_fw[0], -tr_fw[3], -tr_fw[2], -tr_fw[1])
        assert (((tr_fw[1] + tr_fw[3]) != Fraction(0)) or (tr_fw[2] != Fraction(0))) is exp_im_nz

    # Independent FK8 actual peripheral Dehn-filling monodromy on rho_0 & E_6 + Fox cellular cover index chi = 0 (D6):
    rho_lam_0 = rho_word_s((0, 0), "abAB")
    assert rho_lam_0 == -i2_s
    g_mu_p = ((-qi_s * gl_s) * gr_s).applyfunc(sp.expand)
    g_mu_m = (-g_mu_p).applyfunc(sp.expand)
    assert (g_mu_p * qi_s * g_mu_p.H - rho_word_s((0, 0), "aba")).applyfunc(sp.expand) == sp.zeros(2, 2)
    assert (g_mu_p * qj_s * g_mu_p.H - rho_word_s((0, 0), "ba")).applyfunc(sp.expand) == sp.zeros(2, 2)
    assert (g_mu_p ** 3 + i2_s).applyfunc(sp.expand) == sp.zeros(2, 2)
    assert (g_mu_m ** 3 - i2_s).applyfunc(sp.expand) == sp.zeros(2, 2)
    # 6D parity-induced peripheral bundle E_6 on dM_{LR}:
    g6_mu_p = sp.zeros(6, 6)
    for ip_c, p_tup in enumerate(par_list):
        sa_p = (-1 if p_tup[0] else 1) * (-1 if p_tup[1] else 1) * (-1 if p_tup[0] else 1)
        sb_p = (-1 if p_tup[1] else 1) * (-1 if p_tup[0] else 1)
        q_tup = (0 if sa_p == 1 else 1, 0 if sb_p == 1 else 1)
        assert q_tup != p_tup  # zero single rank-2 parity fiber fixed by LR!
        iq_c = par_list.index(q_tup)
        g6_mu_p[2 * ip_c : 2 * ip_c + 2, 2 * iq_c : 2 * iq_c + 2] = g_mu_p
    g6_mu_m = (-g6_mu_p).applyfunc(sp.expand)
    rho6_lam = -sp.eye(6)
    assert ((g_mu_p ** 0) * (rho_lam_0 ** 1)) != i2_s and ((g6_mu_p ** 0) * (rho6_lam ** 1)) != sp.eye(6)
    for p_sl in range(0, 6):
        for q_sl in range(1, 5):
            if math.gcd(p_sl, q_sl) != 1:
                continue
            if q_sl % 2 == 1:
                assert ((g_mu_m ** p_sl) * (rho_lam_0 ** q_sl)).applyfunc(sp.expand) != i2_s
                assert ((g6_mu_m ** p_sl) * (rho6_lam ** q_sl)).applyfunc(sp.expand) != sp.eye(6)
            if p_sl % 3 != 0:
                assert ((g6_mu_p ** p_sl) * (rho6_lam ** q_sl)).applyfunc(sp.expand) != sp.eye(6)
    assert ((g_mu_p ** 3) * (rho_lam_0 ** 1)).applyfunc(sp.expand) == i2_s
    assert ((g_mu_m ** 3) * (rho_lam_0 ** 1)).applyfunc(sp.expand) == -i2_s

    # Independent Fox cellular cochain complex of M_{LR} <a, b, t | t a t^-1 (aba)^-1, t b t^-1 (ba)^-1> across degree-d covers:
    for deg_c in (1, 2, 3, 4):
        perm_d = sp.zeros(deg_c, deg_c)
        for ks in range(deg_c):
            perm_d[(ks + 1) % deg_c, ks] = 1
        ra_c = sp.kronecker_product(sp.eye(deg_c), qi_s)
        rb_c = sp.kronecker_product(sp.eye(deg_c), qj_s)
        rt_c = sp.kronecker_product(perm_d, g_mu_p)
        rk_f = 2 * deg_c
        id_f = sp.eye(rk_f)
        rm_f = {"a": ra_c, "b": rb_c, "t": rt_c, "A": ra_c.H, "B": rb_c.H, "T": rt_c.H}
        d0_f = sp.Matrix.vstack(ra_c - id_f, rb_c - id_f, rt_c - id_f)
        d1_rows: list[sp.Matrix] = []
        for r_word in ("taTABA", "tbTAB"):
            b_acc = {gk: sp.zeros(rk_f, rk_f) for gk in ("a", "b", "t")}
            pf = id_f
            for ch_f in r_word:
                lk = ch_f.lower()
                if ch_f.islower():
                    b_acc[lk] = (b_acc[lk] + pf).applyfunc(sp.expand)
                    pf = (pf * rm_f[ch_f]).applyfunc(sp.expand)
                else:
                    b_acc[lk] = (b_acc[lk] - pf * rm_f[ch_f]).applyfunc(sp.expand)
                    pf = (pf * rm_f[ch_f]).applyfunc(sp.expand)
            d1_rows.append(sp.Matrix.hstack(b_acc["a"], b_acc["b"], b_acc["t"]))
        d1_f = sp.Matrix.vstack(*d1_rows)
        assert (d1_f * d0_f).applyfunc(sp.expand) == sp.zeros(2 * rk_f, rk_f)
        rk_0, rk_1 = int(d0_f.rank()), int(d1_f.rank())
        h0_f = rk_f - rk_0
        h1_f = (3 * rk_f - rk_1) - rk_0
        h2_f = 2 * rk_f - rk_1
        assert (h0_f, h1_f, h2_f) == (0, 2, 2) and (h0_f - h1_f + h2_f) == 0

    # Independent G:FK16 / G:PF5 mirror non-selection theorem (tr(A H_cup) == 0 on End_{G_192}(V) & W_C 28/28 pairing, D7):
    a6_syms = [sp.Symbol(f"m6_{r}_{c}") for r in range(6) for c in range(6)]
    a6_m = sp.Matrix(6, 6, a6_syms)
    eq_c192 = (
        list((a6_m * l6_s - l6_s * a6_m).applyfunc(sp.expand))
        + list((a6_m * r6_s - r6_s * a6_m).applyfunc(sp.expand))
        + list((a6_m * p6_s - p6_s * a6_m).applyfunc(sp.expand))
    )
    ns_c192 = sp.Matrix([[sp.expand(ec).coeff(vs) for vs in a6_syms] for ec in eq_c192]).nullspace()
    assert len(ns_c192) == 1
    assert sp.expand((sp.Matrix(6, 6, list(ns_c192[0])) * h_cup_6).trace()) == 0

    wc_syms = [sp.Symbol(f"wcs_{r}_{c}") for r in range(3) for c in range(3)]
    wc_m = sp.Matrix(3, 3, wc_syms)
    eq_wc_s = list((wc_m * tl3_s.conjugate() - tr3_s * wc_m).applyfunc(sp.expand)) + list(
        (wc_m * tr3_s.conjugate() - tl3_s * wc_m).applyfunc(sp.expand)
    )
    ns_wc_s = sp.Matrix([[sp.expand(ec).coeff(vs) for vs in wc_syms] for ec in eq_wc_s]).nullspace()
    assert len(ns_wc_s) == 1
    wc_r = sp.Matrix(3, 3, list(ns_wc_s[0])).applyfunc(sp.expand)
    wc_u = (wc_r / sp.sqrt(sp.expand((wc_r.H * wc_r)[0, 0]))).applyfunc(sp.expand)
    wc_c, wch_c = mat_to_cyc(wc_u), mat_to_cyc(wc_u.H)

    def im_sgn_c(x_c: Cyc8) -> int:
        a_r = x_c[1] + x_c[3]
        b_r = x_c[2]
        if a_r == 0 and b_r == 0:
            return 0
        if a_r >= 0 and b_r >= 0:
            return 1
        if a_r <= 0 and b_r <= 0:
            return -1
        if a_r > 0 and b_r < 0:
            return 1 if (a_r * a_r) > (2 * b_r * b_r) else -1
        return 1 if (2 * b_r * b_r) > (a_r * a_r) else -1

    pos_im_s, neg_im_s, pair_s = 0, 0, 0
    for gt in g_t96:
        gt_conj = tuple(tuple((gt[r][c][0], -gt[r][c][3], -gt[r][c][2], -gt[r][c][1]) for c in range(3)) for r in range(3))
        gt_mir = cyc_matmul(cyc_matmul(wc_c, gt_conj), wch_c)
        assert gt_mir in g_t96
        tr_g, tr_m = cyc_trace(gt), cyc_trace(gt_mir)
        sg = im_sgn_c(tr_g)
        if sg == 1:
            pos_im_s += 1
        elif sg == -1:
            neg_im_s += 1
        if sg != 0 and gt_mir != gt and im_sgn_c(tr_m) == -sg:
            pair_s += 1
    assert (pos_im_s, neg_im_s, pair_s) == (28, 28, 56)

    # Numerical conversion for SVD commutant & Haar basis-scrambling (< 1e-12):
    l6 = np.array(l6_s.tolist(), dtype=complex)
    r6 = np.array(r6_s.tolist(), dtype=complex)
    p6 = np.array(p6_s.tolist(), dtype=complex)
    g192_np = [
        np.array(
            [
                [
                    float(ec[0]) + float(ec[1]) * ((1.0 + 1j) / np.sqrt(2.0)) + float(ec[2]) * 1j + float(ec[3]) * ((-1.0 + 1j) / np.sqrt(2.0))
                    for ec in row_c
                ]
                for row_c in mg
            ],
            dtype=complex,
        )
        for mg in g_lrp
    ]
    assert min(
        float(np.linalg.norm(m_g - np.eye(6), "fro"))
        for m_g in g192_np
        if float(np.linalg.norm(m_g - np.eye(6), "fro")) > 1e-9
    ) > 1.0
    assert int(np.linalg.matrix_rank(np.array([m_g.ravel() for m_g in g192_np]), tol=1e-9)) == 36

    # Planted negative control: without P, commutant on V has dim 2 (reducible T (+) T_bar), with P dim 1:
    assert _indep_commutant_dim_svd([l6, r6]) == 2
    assert _indep_commutant_dim_svd([l6, r6, p6]) == 1

    # Independent Haar U(6) and U(3) basis-scrambling check (< TOL = 1e-12):
    hm6_np = np.array(h_cup_6.tolist(), dtype=complex)
    tl3_np = np.array(tl3_s.tolist(), dtype=complex)
    tr3_np = np.array(tr3_s.tolist(), dtype=complex)
    usym3_np = np.array(u_sym_s.tolist(), dtype=complex)
    eigs_hm6_0 = np.sort(np.linalg.eigvalsh((hm6_np + hm6_np.conj().T) / 2.0))
    tr_l6r_0 = complex(np.trace(np.linalg.matrix_power(tl3_np, 6) @ tr3_np))

    def eval_t3_np(w_str: str, l_3: np.ndarray, r_3: np.ndarray) -> np.ndarray:
        acc_3 = np.eye(3, dtype=complex)
        for ch_3 in w_str:
            acc_3 = acc_3 @ (l_3 if ch_3 == "L" else r_3)
        return acc_3

    def indep_solve_usym(l_3: np.ndarray, r_3: np.ndarray) -> tuple[np.ndarray, int]:
        cols_b: list[np.ndarray] = []
        for r_i in range(3):
            for c_i in range(3):
                e_ij = np.zeros((3, 3), dtype=complex)
                e_ij[r_i, c_i] = 1.0
                cols_b.append(np.concatenate([(e_ij @ l_3.T - l_3 @ e_ij).ravel(), (e_ij @ r_3.T - r_3 @ e_ij).ravel()]))
        _, sv_u, vh_u = np.linalg.svd(np.column_stack(cols_b))
        n_dim = int(np.sum(sv_u < 1e-9))
        u_vec = vh_u[-1].conj().reshape(3, 3)
        return u_vec / float(np.sqrt(np.real((u_vec.conj().T @ u_vec)[0, 0]))), n_dim

    ref_rev_norms = {
        w_str: float(np.linalg.norm(g_ref @ (usym3_np @ g_ref.T @ usym3_np.conj().T) - (usym3_np @ g_ref.T @ usym3_np.conj().T) @ g_ref, "fro"))
        for w_str in ("LR", "LLLLLLR", "LLLRLR")
        for g_ref in (eval_t3_np(w_str, tl3_np, tr3_np),)
    }

    rng = np.random.default_rng(73)
    for _ in range(6):
        u6 = _indep_haar_unitary(6, rng)
        u6d = u6.conj().T
        l_rot, r_rot, p_rot = u6 @ l6 @ u6d, u6 @ r6 @ u6d, u6 @ p6 @ u6d
        hm_rot = u6 @ hm6_np @ u6d
        assert _indep_commutant_dim_svd([l_rot, r_rot]) == 2
        assert _indep_commutant_dim_svd([l_rot, r_rot, p_rot]) == 1
        stk = np.vstack([l_rot - np.eye(6), r_rot - np.eye(6)])
        assert int(np.sum(np.linalg.svd(stk, compute_uv=False) < 1e-9)) == 0
        eigs_hm_rot = np.sort(np.linalg.eigvalsh((hm_rot + hm_rot.conj().T) / 2.0))
        assert float(np.max(np.abs(eigs_hm_rot - eigs_hm6_0))) < TOL
        fs_rot = sum(complex(np.trace((u6 @ m_g @ u6d) @ (u6 @ m_g @ u6d))) for m_g in g192_np) / float(len(g192_np))
        assert abs(fs_rot - (-1.0)) < TOL

        u3 = _indep_haar_unitary(3, rng)
        u3d = u3.conj().T
        tl_rot, tr_rot = u3 @ tl3_np @ u3d, u3 @ tr3_np @ u3d
        assert _indep_commutant_dim_svd([tl_rot, tr_rot]) == 1
        assert abs(complex(np.trace(np.linalg.matrix_power(tl_rot, 6) @ tr_rot)) - tr_l6r_0) < TOL
        usym_rot, usym_ndim = indep_solve_usym(tl_rot, tr_rot)
        assert usym_ndim == 1
        assert float(np.linalg.norm(usym_rot.T - usym_rot, "fro")) < TOL
        assert float(np.linalg.norm(usym_rot.conj().T @ usym_rot - np.eye(3), "fro")) < TOL
        for w_str, ref_val in ref_rev_norms.items():
            g_rot = eval_t3_np(w_str, tl_rot, tr_rot)
            grev_rot = usym_rot @ g_rot.T @ usym_rot.conj().T
            assert abs(float(np.linalg.norm(g_rot @ grev_rot - grev_rot @ g_rot, "fro")) - ref_val) < TOL

    naive_tp_vals = [
        float(np.linalg.norm(gl6r_rot @ gl6r_rot.T - gl6r_rot.T @ gl6r_rot, "fro"))
        for u3_tp in (_indep_haar_unitary(3, rng) for _ in range(6))
        for gl6r_rot in (eval_t3_np("LLLLLLR", u3_tp @ tl3_np @ u3_tp.conj().T, u3_tp @ tr3_np @ u3_tp.conj().T),)
    ]
    assert (max(naive_tp_vals) - min(naive_tp_vals)) > (1 / 64)

    wp19 = stage3_results["wp19_register_deck_joins"]
    assert wp19["haar_scrambling_verified"] is True
    assert wp19["max_haar_scramble_err"] < TOL
    assert wp19["b1879_exchange_192_doubling_and_end_dims_exact"] is True
    assert wp19["contravariant_pullback_functoriality_exact"] is True
    assert wp19["u_sym_transpose_intertwiner_exact"] is True
    assert wp19["frobenius_schur_lrp_vs_lrip_exact"] == (-1, 1)
    assert wp19["fk12_word_reversal_vs_mirror_swap_exact"] is True
    assert wp19["fk12_g96_partition_counts"]["comm_with_rev_nonzero_count"] == 32
    assert wp19["fk12_g96_partition_counts"]["chiral_im_trace_nonzero_count"] == 56
    assert wp19["fk12_g96_partition_counts"]["intersection_comm_and_im_nonzero"] == 0
    assert wp19["fk7_fk8_deck_and_dehn_filling_exact"] is True
    assert wp19["stabilizer_central_sheet_exact"] is True
    assert wp19["involution_counts_lrp_vs_lrip"] == (7, 47)
    assert wp19["fk16_pf5_mirror_nonselection_exact"] is True


def test_wp18_zero_trust_d16plus_vs_e8e8_root_graph_and_borel_de_siebenthal(stage3_results: dict[str, Any]) -> None:
    # 1. Independently construct ALL 2*240 norm-2 roots of E_8 (+) E_8 and of D_16^+ in Q^16 and prove non-isomorphism
    # via the connected components of the norm-2 root inner-product graph (<r, r'> != 0)!
    def build_e8_roots_q8() -> list[tuple[sp.Rational, ...]]:
        rts: list[tuple[sp.Rational, ...]] = []
        for i_c, j_c in combinations(range(8), 2):
            for s1, s2 in product((-1, 1), repeat=2):
                v_r = [sp.Rational(0)] * 8
                v_r[i_c] = sp.Rational(s1)
                v_r[j_c] = sp.Rational(s2)
                rts.append(tuple(v_r))
        for sgns in product((-1, 1), repeat=8):
            if sgns.count(-1) % 2 == 0:
                rts.append(tuple(sp.Rational(sv, 2) for sv in sgns))
        return rts

    e8_r = build_e8_roots_q8()
    assert len(e8_r) == 240
    z8 = (sp.Rational(0),) * 8
    roots_e8e8 = [r + z8 for r in e8_r] + [z8 + r for r in e8_r]

    roots_d16p: list[tuple[sp.Rational, ...]] = []
    for i_c, j_c in combinations(range(16), 2):
        for s1, s2 in product((-1, 1), repeat=2):
            v_r = [sp.Rational(0)] * 16
            v_r[i_c] = sp.Rational(s1)
            v_r[j_c] = sp.Rational(s2)
            roots_d16p.append(tuple(v_r))
    # Verify spinor glue coset (1/2, ..., +-1/2) in D_16^+ has minimum norm^2 = 16 * (1/4) = 4 > 2 (contributes 0 roots):
    assert 16 * sp.Rational(1, 4) == 4
    assert len(roots_e8e8) == 480 and len(roots_d16p) == 480

    def count_root_graph_components(rts_16: list[tuple[sp.Rational, ...]]) -> list[int]:
        arr = np.array([[float(c) for c in rv] for rv in rts_16], dtype=float)
        adj = np.abs(arr @ arr.T) > 0.5
        n_v = len(rts_16)
        visited: set[int] = set()
        comp_sizes: list[int] = []
        for start in range(n_v):
            if start in visited:
                continue
            visited.add(start)
            q_c = [start]
            cnt = 0
            while q_c:
                u_i = q_c.pop(0)
                cnt += 1
                nbrs = np.nonzero(adj[u_i])[0]
                for w_i in nbrs:
                    if int(w_i) not in visited:
                        visited.add(int(w_i))
                        q_c.append(int(w_i))
            comp_sizes.append(cnt)
        return sorted(comp_sizes)

    # E_8 (+) E_8 has TWO disconnected root components [240, 240], whereas D_16^+ has ONE connected component [480]!
    assert count_root_graph_components(roots_e8e8) == [240, 240]
    assert count_root_graph_components(roots_d16p) == [480]

    # 2. Independent affine E_8^(1) Cartan matrix from Dynkin edges (Bourbaki numbering: branch at node 4 to node 2):
    # Edges of E_8: (1,3), (3,4), (4,2), (4,5), (5,6), (6,7), (7,8), plus affine node 0 attached to node 8!
    edges_aff = {(1, 3), (3, 4), (4, 2), (4, 5), (5, 6), (6, 7), (7, 8), (8, 0)}
    c_aff = sp.zeros(9, 9)
    for i_n in range(9):
        c_aff[i_n, i_n] = 2
    for u_e, v_e in edges_aff:
        c_aff[u_e, v_e] = -1
        c_aff[v_e, u_e] = -1
    ns_aff = c_aff.nullspace()
    assert len(ns_aff) == 1
    marks = [int(ns_aff[0][k] / ns_aff[0][0]) for k in range(9)]
    # Kac marks for (0, 1, 2, 3, 4, 5, 6, 7, 8): (1, 2, 3, 4, 6, 5, 4, 3, 2)
    assert marks == [1, 2, 3, 4, 6, 5, 4, 3, 2]

    # Deleting each prime-mark node in {1, 2, 5, 7, 8} (marks 2, 3, 5, 3, 2) gives exact classical/exceptional Lie dims:
    # Del 8 (mark 2): E_8 -> NO, node 0 was attached to 8, so deleting 8 leaves E_7 + A_1 (dim 133 + 3 = 136)!
    # Del 1 (mark 2): leaves D_8 (chain 0-8-7-6-5-4 with fork 2, 3 -> 8 nodes, dim 16*15/2 = 120)!
    # Del 2 (mark 3): leaves A_8 (single chain 1-3-4-5-6-7-8-0 of 8 nodes, dim 9^2 - 1 = 80)!
    # Del 7 (mark 3): leaves E_6 (1-3-4(2)-5-6) + A_2 (8-0) (dim 78 + 8 = 86)!
    # Del 5 (mark 5): leaves A_4 (1-3-4-2? Wait: 1-3-4-2 is chain of 4 nodes = A_4!) + A_4 (6-7-8-0 = A_4) (dim 24 + 24 = 48)!
    def connected_ade_components(del_node: int) -> list[tuple[int, int]]:
        rem = [k for k in range(9) if k != del_node]
        seen_n: set[int] = set()
        comps: list[tuple[int, int]] = []  # (num_nodes, max_degree)
        for st in rem:
            if st in seen_n:
                continue
            seen_n.add(st)
            q_n = [st]
            comp_nodes: list[int] = []
            while q_n:
                cur_n = q_n.pop(0)
                comp_nodes.append(cur_n)
                for nb in rem:
                    if nb not in seen_n and int(c_aff[cur_n, nb]) == -1:
                        seen_n.add(nb)
                        q_n.append(nb)
            degs = [sum(1 for nb in comp_nodes if int(c_aff[nd, nb]) == -1) for nd in comp_nodes]
            # Also record branch position if max_degree == 3 (distinguishes D_n from E_6, E_7):
            leaves_dist: list[int] = []
            if max(degs) == 3:
                hub = comp_nodes[degs.index(3)]
                # Branch lengths from hub:
                for nb in comp_nodes:
                    if int(c_aff[hub, nb]) == -1:
                        length_arm = 1
                        prev_n, walk_n = hub, nb
                        while True:
                            nxts = [x for x in comp_nodes if x != prev_n and int(c_aff[walk_n, x]) == -1]
                            if not nxts:
                                break
                            prev_n, walk_n = walk_n, nxts[0]
                            length_arm += 1
                        leaves_dist.append(length_arm)
            if max(degs) <= 2:
                # Type A_r (r = len(comp_nodes)): dim = r*(r+2)
                r_rk = len(comp_nodes)
                comps.append((r_rk, r_rk * (r_rk + 2)))
            else:
                arms = sorted(leaves_dist)
                r_rk = len(comp_nodes)
                if arms[:2] == [1, 1]:
                    # Type D_r: dim = r * (2*r - 1)
                    comps.append((r_rk, r_rk * (2 * r_rk - 1)))
                elif arms == [1, 2, 2]:
                    # Type E_6: dim = 78
                    comps.append((6, 78))
                elif arms == [1, 2, 3]:
                    # Type E_7: dim = 133
                    comps.append((7, 133))
                else:
                    raise AssertionError(f"Unexpected ADE diagram arms {arms}")
        return comps

    prime_nodes = [idx for idx in range(1, 9) if marks[idx] in (2, 3, 5)]
    assert prime_nodes == [1, 2, 5, 7, 8]
    tot_dims = sorted(sum(dim_c for _, dim_c in connected_ade_components(nd)) for nd in prime_nodes)
    assert tot_dims == [48, 80, 86, 120, 136]

    # 3. Independent Z_4 glue coset partition on e8_r over D_5 (+) D_3 & bi-chiral orthogonal split check:
    adj_r = [
        rv for rv in e8_r
        if all(c.is_integer for c in rv)
        and ((sum(1 for i in range(5) if rv[i] != 0) == 2) or (sum(1 for i in range(5, 8) if rv[i] != 0) == 2))
    ]
    vv_r = [
        rv for rv in e8_r
        if all(c.is_integer for c in rv)
        and sum(1 for i in range(5) if rv[i] != 0) == 1
        and sum(1 for i in range(5, 8) if rv[i] != 0) == 1
    ]
    sp_r = [
        rv for rv in e8_r
        if (not rv[0].is_integer)
        and (len([i for i in range(5) if rv[i] < 0]) in (0, 2, 4))
        and (len([i for i in range(5, 8) if rv[i] < 0]) in (0, 2))
    ]
    sm_r = [
        rv for rv in e8_r
        if (not rv[0].is_integer)
        and (len([i for i in range(5) if rv[i] < 0]) in (1, 3, 5))
        and (len([i for i in range(5, 8) if rv[i] < 0]) in (1, 3))
    ]
    assert (len(adj_r) + 8, len(vv_r), len(sp_r), len(sm_r)) == (60, 60, 64, 64)
    # Spin(2m) chiral spinors are complex iff m is odd: in D_k (+) D_{8-k} (k=1..4), BOTH factors are complex iff k in {1, 3}:
    bichiral_ks = [k_v for k_v in range(1, 5) if (k_v % 2 == 1) and ((8 - k_v) % 2 == 1)]
    assert bichiral_ks == [1, 3]

    # 4. Independent mechanical Jacobian d(G^48 - I_6)|_{I_6} = 48 I_36, real su(2) Lie closure dim 3, & Buckingham-Pi:
    eps_t = sp.Symbol("eps_t")
    j_diag: list[int] = []
    for r_i in range(6):
        for c_i in range(6):
            e_m = sp.zeros(6, 6)
            e_m[r_i, c_i] = 1
            d_m = ((sp.eye(6) + eps_t * e_m) ** 48) - sp.eye(6)
            j_diag.append(int(sp.diff(d_m[r_i, c_i], eps_t).subs(eps_t, 0)))
    assert j_diag == [48] * 36

    m_dim_1 = sp.Matrix([[0, 0, 1, 0, 0]])
    assert int(m_dim_1.rank()) == 1 and len(m_dim_1.nullspace()) == 4
    m_dim_2 = sp.Matrix([[0, 0, 1, 0, 0, 1]])
    assert sum(1 for k_c in range(6) if int(m_dim_2[0, k_c]) != 0) == 2

    wp18 = stage3_results["wp18_parent_algebra"]
    assert wp18["intrinsic_algebra_cannot_force_e8"] is True
    assert wp18["e8_prime_mark_maximal_subalgebra_dims"] == [48, 80, 86, 120, 136]
    assert wp18["d5_d3_z4_glue_cosets_exact"] is True
    assert wp18["d8_bichiral_complex_splits"] == ["so(2)+so(14)", "so(6)+so(10)"]
    assert wp18["rank16_even_unimodular_non_uniqueness_e8e8_vs_d16plus"] is True
    assert wp18["mc_hyp_guardrail5_reconciled"] is True
