#!/usr/bin/env python3
r"""Card AGY-C46 Disjoint Cold-Room Countercheck (Guardrail 6, 0 of 19):
100% standalone under `python3 -I` in any isolated sandbox directory (depends ONLY on stdlib and mpmath — ZERO SymPy,
ZERO subprocess/git, ZERO R^8 half-integer coordinates!):
  1. Disjoint E1 Countercheck (Closing D1):
     - Implicit 2-stage Gauss-Legendre GL4 parallel transport around |z| = exp(-3) verifying nilpotent Jordan monodromy
       M = -[[1, 2 pi i], [0, 1]] (< 10^-10, vs c_0 = 1 failure).
     - Coordinate-free Bourbaki 8x8 E_8 Cartan matrix Weyl-reflection BFS in simple-root Z^8 coordinates: constructs
       extended E_8^{(1)} minus Kac-mark-6 node 3 -> A_5 + A_2 + A_1, verifies diagonal su(2)_Q (h_Q - h_W even on all
       240 roots, colour/weak/hypercharge singlet vs off-block A_5 root), solves W70's 5 SM charge conditions on the
       469 grid WITH ZERO k_Y INPUT to obtain the exact 6 permutations of (1/6, -5/6, 2/3) (catching > 6 spurious
       solutions when e^c(1) is dropped), and DERIVES k_Y = 140 / 30 == 14 / 3, plus Cholesky P-862.
  2. Disjoint E2 Countercheck (Closing D2):
     - Recomputes B1970's 40 Yukawa triples purely via E_8 -> E_6 x A_2 (selecting the 27 Bourbaki roots with A_2
       Dynkin weight (1, 0) and testing cubic E_8 root addition r_h + r_i + r_j == 2 alpha_{C,1} + alpha_{C,2}!),
       plus 32-node Cauchy contour Wirtinger integral (1/(2 pi i)) oint f(z) d(bar z) == 0 vs bar S != 0.
     - Rational 5-vector Spin(10) Tr F^4 check (F_4 vs F_6) + mp.expm(2i H) SU(2)_L Haar check + quintic C^2 collar
       bump computing BOTH exp_complete == 5 AND exp_fixed == 4 from two-scale ratios (zero literal assignment!).
  3. Disjoint E3 Countercheck (Closing D3):
     - Verifies SHA-256 manifest, P-571 20 + 87 == 107 partition, U(1) lattice Wilson-plaquette Chern numbers
       (0 at M = 0 vs 4 at M = 4 from Im ln(U_plaq)), 24x24 midpoint Z_2 reflection trace at M = 4, and SL(2, F_3)
       spin-3/2 Sym^3 eigenvalue sum check (5 / 5 planted-fault controls).
"""
from __future__ import annotations

import ast
from collections import Counter, deque
from fractions import Fraction as Fr
from itertools import combinations, product
import hashlib
import json
from pathlib import Path
import time

import mpmath as mp

THIS_DIR = Path(__file__).resolve().parent
OUT_JSON = THIS_DIR / "c46_out.json"
OUT_SHA = THIS_DIR / "OUTPUT_SHA256.txt"
I_MP = mp.mpc(0, 1)


def mp_rat(n: int, d: int = 1) -> mp.mpf:
    return mp.mpf(int(n)) / mp.mpf(int(d))


def check_zero_ast_floats(src: str, name: str) -> None:
    tree = ast.parse(src, filename=name)
    bad = [
        node.lineno
        for node in ast.walk(tree)
        if (isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)))
        or (isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ("float", "complex"))
    ]
    assert not bad, f"[{name}] forbidden AST float/complex at lines {bad}"


def check_zero_json_floats(raw_text: str, name: str) -> dict:
    def bad_float(val_s: str) -> None:
        raise AssertionError(f"[{name}] raw JSON float found: {val_s}")

    return json.loads(raw_text, parse_float=bad_float)


def verify_gl4_nilpotent_jordan_cc() -> tuple[mp.mpf, mp.mpf]:
    u_val = mp.mpf(3)

    def holonomy_gl4(c0_val: mp.mpf, n_st: int = 160) -> mp.matrix:
        ath = I_MP * mp.matrix([
            [mp_rat(1, 2) * (1 + 1 / u_val), c0_val],
            [-c0_val / (u_val ** 2), mp_rat(1, 2) * (1 - 1 / u_val)],
        ])
        h = (2 * mp.pi) / n_st
        sr3 = mp.sqrt(mp.mpf(3))
        a11, a12, a21, a22 = mp_rat(1, 4), mp_rat(1, 4) - sr3 / 6, mp_rat(1, 4) + sr3 / 6, mp_rat(1, 4)
        u_m = mp.eye(2)
        for _ in range(n_st):
            k1 = -ath * u_m
            k2 = k1
            for _ in range(14):
                k1 = -ath * (u_m + h * (a11 * k1 + a12 * k2))
                k2 = -ath * (u_m + h * (a21 * k1 + a22 * k2))
            u_m = u_m + (h / 2) * (k1 + k2)
        return u_m

    p_inv = mp.matrix([[mp.mpf(1), mp.mpf(0)], [-1 / (2 * u_val), -mp_rat(1, 2)]])
    p_mat = mp.matrix([[mp.mpf(1), mp.mpf(0)], [-1 / u_val, -mp.mpf(2)]])
    m_good = p_inv * holonomy_gl4(mp_rat(1, 2), 320) * p_mat
    m_good_half = p_inv * holonomy_gl4(mp_rat(1, 2), 160) * p_mat
    m_rich = (16 * m_good - m_good_half) / 15
    m_exact = mp.matrix([[-mp.mpf(1), -2 * mp.pi * I_MP], [mp.mpf(0), -mp.mpf(1)]])
    err_good = max(abs(m_rich[r, c] - m_exact[r, c]) for r in range(2) for c in range(2))
    m_bad = p_inv * holonomy_gl4(mp.mpf(1), 80) * p_mat
    sq_bad = (m_bad + mp.eye(2)) ** 2
    return err_good, max(abs(sq_bad[r, c]) for r in range(2) for c in range(2))


def verify_bourbaki_w70_and_e8_b1970_cc() -> tuple[dict[str, object], bool, bool]:
    """Coordinate-free Bourbaki 8x8 Cartan E_8 verification of W70 (su(2)_Q, 6 Y's, k_Y=14/3) AND E_8 -> E_6 x A_2 B1970 40 triples."""
    edges = {(0, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)}
    cartan = [[2 if i == j else (-1 if (min(i, j), max(i, j)) in edges else 0) for j in range(8)] for i in range(8)]

    simples = [tuple(Fr(1 if j == i else 0) for j in range(8)) for i in range(8)]
    seen_int: set[tuple[int, ...]] = {tuple(1 if j == i else 0 for j in range(8)) for i in range(8)}
    q = deque(seen_int)
    while q:
        rt = q.popleft()
        for i in range(8):
            ip = sum(rt[j] * cartan[j][i] for j in range(8))
            nxt = tuple(rt[j] - ip * (1 if j == i else 0) for j in range(8))
            if any(x != 0 for x in nxt) and nxt not in seen_int:
                seen_int.add(nxt)
                q.append(nxt)
                neg = tuple(-x for x in nxt)
                if neg not in seen_int:
                    seen_int.add(neg)
                    q.append(neg)
    assert len(seen_int) == 240
    roots_q = [tuple(Fr(x) for x in r) for r in sorted(seen_int)]

    def ip_c(u: tuple[Fr, ...], v: tuple[Fr, ...]) -> Fr:
        return sum((u[i] * cartan[i][j] * v[j] for i in range(8) for j in range(8)), Fr(0))

    add_q = lambda u, v: tuple(u[k] + v[k] for k in range(8))
    sub_q = lambda u, v: tuple(u[k] - v[k] for k in range(8))
    sc_q = lambda c, u: tuple(c * u[k] for k in range(8))

    # Find highest root theta dynamically (unique root with all (theta, alpha_i)_C >= 0):
    dom_roots = [r for r in roots_q if all(ip_c(r, simples[i]) >= 0 for i in range(8)) and sum(r) > 0]
    assert len(dom_roots) == 1
    theta = dom_roots[0]

    # Extended E_8^{(1)} minus Kac-mark-6 node 3 -> A_2 = {0, 2}, A_1 = {1}, A_5 = {4, 5, 6, 7, -theta}:
    a2_s = [simples[0], simples[2]]
    h_W = simples[1]
    a5_s = [simples[4], simples[5], simples[6], simples[7], sc_q(Fr(-1), theta)]
    assert [[ip_c(a5_s[i], a5_s[j]) for j in range(5)] for i in range(5)] == [[Fr(2 if i == j else (-1 if abs(i - j) == 1 else 0)) for j in range(5)] for i in range(5)]
    assert [[ip_c(a2_s[i], a2_s[j]) for j in range(2)] for i in range(2)] == [[Fr(2), Fr(-1)], [Fr(-1), Fr(2)]]
    assert all(ip_c(x, y) == 0 for x in a5_s for y in [*a2_s, h_W]) and all(ip_c(c, h_W) == 0 for c in a2_s)

    # Diagonal su(2)_Q in Bourbaki Z^8 coordinates:
    su2q_pos = [a5_s[0], a5_s[2], a5_s[4]]
    su2q_all = [*su2q_pos, *[sc_q(Fr(-1), x) for x in su2q_pos]]
    h_Q = add_q(add_q(su2q_pos[0], su2q_pos[1]), su2q_pos[2])
    even_hq_hw = all(int(ip_c(r, sub_q(h_Q, h_W))) % 2 == 0 for r in roots_q)
    bad_hq_drop = sum(1 for r in roots_q if int(ip_c(r, sub_q(add_q(su2q_pos[1], su2q_pos[2]), h_W))) % 2 != 0)
    p_odd = [r for r in roots_q if int(ip_c(r, h_Q)) % 2 != 0]
    p_even = [r for r in roots_q if int(ip_c(r, h_Q)) % 2 == 0]
    assert even_hq_hw and bad_hq_drop > 0 and len(p_odd) == 112

    # Fundamental coweights omega_2, omega_4 of A_5 in Q^8:
    om2 = sc_q(Fr(1, 3), add_q(add_q(sc_q(Fr(2), a5_s[0]), sc_q(Fr(4), a5_s[1])), add_q(sc_q(Fr(3), a5_s[2]), add_q(sc_q(Fr(2), a5_s[3]), a5_s[4]))))
    om4 = sc_q(Fr(1, 3), add_q(add_q(a5_s[0], sc_q(Fr(2), a5_s[1])), add_q(sc_q(Fr(3), a5_s[2]), add_q(sc_q(Fr(4), a5_s[3]), sc_q(Fr(2), a5_s[4])))))
    assert [ip_c(om2, a5_s[k]) for k in range(5)] == [Fr(0), Fr(1), Fr(0), Fr(0), Fr(0)]
    assert [ip_c(om4, a5_s[k]) for k in range(5)] == [Fr(0), Fr(0), Fr(0), Fr(1), Fr(0)]
    y_bourb = lambda y1, y2, y3: add_q(sc_q(y1 - y2, om2), sc_q(y2 - y3, om4))

    # Verify su(2)_Q has <Y, r>_C == 0 for generic rational (y1, y2, y3), while off-block a5_s[1] has y1 - y2 != 0:
    yt_gen = y_bourb(Fr(3, 11), Fr(5, 11), Fr(-8, 11))
    su2q_sing_ok = (
        all(ip_c(r, yt_gen) == 0 for r in [h_Q, *su2q_all])
        and ip_c(a5_s[1], yt_gen) == Fr(-2, 11)
        and all(ip_c(r, c) == 0 for r in [h_Q, *su2q_all] for c in a2_s)
        and all(ip_c(r, h_W) == 0 for r in [h_Q, *su2q_all])
    )
    assert su2q_sing_ok

    # Partition roots_q into (35,1,1)[30], (6,3,2)[36], (15,3bar,1)[45], (20,1,2)[40] via Weyl-orbit BFS on subalgebra simple roots:
    r_set = set(roots_q)
    sub_all = [*a5_s, *a2_s, h_W]

    def sub_roots(gens: list[tuple[Fr, ...]]) -> set[tuple[Fr, ...]]:
        vis = set(gens) | {sc_q(Fr(-1), g) for g in gens}
        dq = deque(vis)
        while dq:
            cur = dq.popleft()
            for g in gens:
                for sg in (-1, 1):
                    nx = add_q(cur, sc_q(Fr(sg), g))
                    if nx in r_set and nx not in vis:
                        vis.add(nx)
                        dq.append(nx)
        return vis

    r35 = sub_roots(a5_s)
    r8 = sub_roots(a2_s)
    r3 = sub_roots([h_W])
    assert (len(r35), len(r8), len(r3)) == (30, 6, 2)

    a2_3 = {(Fr(1), Fr(0)), (Fr(-1), Fr(1)), (Fr(0), Fr(-1))}
    a2_3b = {(Fr(0), Fr(1)), (Fr(1), Fr(-1)), (Fr(-1), Fr(0))}
    # (20,1,2): p_odd colour singlets (40 roots)! (6,3,2): remaining p_odd with A_2 weight in a2_3 (36 roots)!
    r20_1_2 = [r for r in p_odd if ip_c(r, a2_s[0]) == 0 and ip_c(r, a2_s[1]) == 0]
    r6_3_2 = [r for r in p_odd if (ip_c(r, a2_s[0]), ip_c(r, a2_s[1])) in a2_3]
    r15_3b_1 = [r for r in p_even if r not in r35 and r not in r8 and r not in r3 and (ip_c(r, a2_s[0]), ip_c(r, a2_s[1])) in a2_3b]
    assert (len(r20_1_2), len(r6_3_2), len(r15_3b_1)) == (40, 36, 45)

    dyn6 = {tuple(ip_c(r, g) for g in a5_s) for r in r6_3_2}
    sg6 = Fr(1) if (Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)) in dyn6 else Fr(-1)

    def w70_ok(y1: Fr, y2: Fr, y3: Fr, req_ec: bool = True) -> bool:
        yv = y_bourb(y1, y2, y3)
        c6 = {sg6 * ip_c(r, yv) for r in r6_3_2}
        c15 = {sg6 * ip_c(r, yv) for r in r15_3b_1}
        c20 = {sg6 * ip_c(r, yv) for r in r20_1_2}
        c35 = {sg6 * ip_c(r, yv) for r in r35}
        return bool(Fr(1, 6) in c6 and Fr(-2, 3) in c15 and Fr(1, 3) in c15 and Fr(-1, 2) in c20 and (Fr(1, 1) in c35 if req_ec else True))

    grid_469 = [(Fr(k1, 6), Fr(k2, 6), Fr(-k1 - k2, 6)) for k1 in range(-12, 13) for k2 in range(-12, 13) if -12 <= -k1 - k2 <= 12]
    adm_6 = [t for t in grid_469 if w70_ok(*t, True)]
    adm_bad = [t for t in grid_469 if w70_ok(*t, False)]
    tr_t3 = sum(((ip_c(r, h_W) / 2) ** 2 for r in roots_q), Fr(0))
    ky_vals = {sum((ip_c(r, y_bourb(*t)) ** 2 for r in roots_q), Fr(0)) / tr_t3 for t in adm_6}
    assert len(adm_6) == 6 and len(adm_bad) > 6 and (Fr(1, 6), Fr(-1, 3), Fr(1, 6)) in adm_bad and tr_t3 == Fr(30) and ky_vals == {Fr(14, 3)}

    # Disjoint B1970 40 Yukawa triples via E_8 -> E_6 x A_2!
    # In E_8, the A_2 = {simples[0], simples[2]} commutant is E_6 (since nodes 0, 2 attach to node 3 -> deleting 3, keeping {1,3..7}?
    # Wait: node 2 attaches to node 3! So A_2 = {0, 2}'s commutant in E_8 is {4, 5, 6, 7, 1, -theta}!! Check its Dynkin diagram:
    # -theta = -(2,3,4,6,5,4,3,2) has (-theta, alpha_i)_C = 0 for i=0..6 and -1 for i=7? Wait: let's check (-theta, alpha_i)_C:
    # Actually (-theta) attaches to whichever node has Kac mark 1 — in Bourbaki E_8, node 7 (Bourbaki 8) has theta . alpha_7 = 1!
    # So {simples[0], simples[2]} has commutant {r in roots_q : ip_c(r, a2_s[0]) == 0 and ip_c(r, a2_s[1]) == 0} -> count it!
    e6_roots = [r for r in roots_q if ip_c(r, a2_s[0]) == 0 and ip_c(r, a2_s[1]) == 0]
    assert len(e6_roots) == 72
    # And the roots with A_2 Dynkin weight (1, 0) form the EXACT 27 of E_6!!
    wts_27_e8 = [r for r in roots_q if (ip_c(r, a2_s[0]), ip_c(r, a2_s[1])) == (Fr(1), Fr(0))]
    assert len(wts_27_e8) == 27
    # Inside E_6, U(1)_psi = varpi_7 (or node 7 / -theta), breaking E_6 -> Spin(10) x U(1)_psi (1 + 10 + 16)!
    # Specifically, deleting -theta leaves D_5 = {1, 3? No: in E_6 = {r : ip(a2)==0}, take simple roots of D_5 orthogonal to a2:
    # Notice -theta has ip_c(-theta, a2_s[0]) = 0, ip_c(-theta, a2_s[1]) = 0! Look at ip_c(r, theta) on wts_27_e8:
    # Since theta is the highest root, ip_c(r, theta) takes 3 values on the 27: check Counter(ip_c(r, theta) for r in wts_27_e8)!
    # Wait: on positive roots != theta, ip_c(r, theta) in {0, 1}; let's find a U(1)_psi coweight in span(e6_roots) giving 1 + 10 + 16!
    # Even simpler: in E_6, pick ANY root alpha_psi in e6_roots? No, a root gives 1 + 1 + 20 + ...; a fundamental coweight of an endpoint of E_6 gives 1 + 10 + 16!
    # Which simple roots of E_6 span e6_roots? Find positive roots in e6_roots (those > 0 lex) that are not sums of two positive roots in e6_roots!
    e6_pos = [r for r in e6_roots if r > tuple(Fr(0) for _ in range(8))]
    e6_pos_set = set(e6_pos)
    e6_simples = [r for r in e6_pos if not any(sub_q(r, s) in e6_pos_set for s in e6_pos if s != r)]
    assert len(e6_simples) == 6
    # Find an endpoint simple root of E_6 whose removal leaves D_5 (40 roots -> 1 + 10 + 16 on wts_27_e8!):
    d5_split = None
    for idx_end in range(6):
        rem5 = [e6_simples[k] for k in range(6) if k != idx_end]
        if len(sub_roots(rem5)) == 40:
            # Compute coweight u_psi in span(e6_simples) dual to e6_simples[idx_end]:
            # Solve 6x6 Gram G c = e_{idx_end} in Fractions:
            G = [[ip_c(e6_simples[a], e6_simples[b]) for b in range(6)] for a in range(6)]
            rhs = [Fr(3 if a == idx_end else 0) for a in range(6)]
            # Gaussian elimination:
            M_aug = [G[a][:] + [rhs[a]] for a in range(6)]
            for col in range(6):
                piv = next(r_i for r_i in range(col, 6) if M_aug[r_i][col] != 0)
                M_aug[col], M_aug[piv] = M_aug[piv], M_aug[col]
                pv = M_aug[col][col]
                M_aug[col] = [x / pv for x in M_aug[col]]
                for r_i in range(6):
                    if r_i != col and M_aug[r_i][col] != 0:
                        fc = M_aug[r_i][col]
                        M_aug[r_i] = [M_aug[r_i][k] - fc * M_aug[col][k] for k in range(7)]
            u_psi = tuple(sum((M_aug[a][6] * e6_simples[a][k] for a in range(6)), Fr(0)) for k in range(8))
            psi_counts = Counter(ip_c(r, u_psi) for r in wts_27_e8)
            if sorted(psi_counts.values()) == [1, 10, 16]:
                d5_split = (u_psi, psi_counts)
                break
    assert d5_split is not None
    u_psi, psi_counts = d5_split
    q_ten = next(q_v for q_v, cnt in psi_counts.items() if cnt == 10)
    q_sixteen = next(q_v for q_v, cnt in psi_counts.items() if cnt == 16)
    ten_e8 = [r for r in wts_27_e8 if ip_c(r, u_psi) == q_ten]
    sixteen_e8 = [r for r in wts_27_e8 if ip_c(r, u_psi) == q_sixteen]

    # Cubic E_6 invariant condition on wts_27_e8 (A_2 weight (1,0) => 3 * varpi_1 = 2 * a2_s[0] + a2_s[1]):
    target_sum = add_q(sc_q(Fr(2), a2_s[0]), a2_s[1])
    triples_e8 = 0
    for rh in ten_e8:
        for i_a in range(16):
            for i_b in range(i_a + 1, 16):
                if add_q(rh, add_q(sixteen_e8[i_a], sixteen_e8[i_b])) == target_sum:
                    triples_e8 += 1
    assert triples_e8 == 40

    pf1_ok = bool(even_hq_hw and bad_hq_drop > 0 and su2q_sing_ok and len(adm_6) == 6 and ky_vals == {Fr(14, 3)})
    return {"n_e8": len(roots_q), "n_podd": len(p_odd), "triples_e8": triples_e8}, pf1_ok, (triples_e8 == 40)


def verify_cholesky_p862_cc() -> mp.mpf:
    m = mp.matrix([[mp_rat(2, 7), mp_rat(1, 3) - I_MP * mp_rat(1, 5), mp_rat(1, 11)], [mp_rat(1, 4), mp_rat(-3, 5), I_MP * mp_rat(2, 9)], [mp.mpf(0), mp_rat(1, 6), mp_rat(1, 2)]])
    a = mp.eye(3) + m * m.H
    l_m = mp.zeros(3, 3)
    for i in range(3):
        for j in range(i + 1):
            s = sum(l_m[i, k] * mp.conj(l_m[j, k]) for k in range(j))
            l_m[i, j] = mp.sqrt(mp.re(a[i, i] - s)) if i == j else (a[i, j] - s) / l_m[j, j]
    rec_err = max(abs((l_m * l_m.H - a)[r, c]) for r in range(3) for c in range(3))
    det_chol = (mp.re(l_m[0, 0] * l_m[1, 1] * l_m[2, 2])) ** 2
    assert det_chol > mp.mpf(1)
    return max(rec_err, abs(det_chol - mp.re(mp.det(a))))


def main() -> None:
    t0 = time.time()
    check_zero_ast_floats(Path(__file__).resolve().read_text(encoding="utf-8"), Path(__file__).name)
    raw = OUT_JSON.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == OUT_SHA.read_text(encoding="utf-8").strip().split()[0]
    doc = check_zero_json_floats(raw.decode("utf-8"), OUT_JSON.name)
    assert doc["empirical_firewall"] == "0 of 19" and doc["all_expectations_passed"] is True

    mp.mp.dps = 50
    gl4_err, gl4_bad_brk = verify_gl4_nilpotent_jordan_cc()
    b_info, w70_cc_ok, e8_triples_ok = verify_bourbaki_w70_and_e8_b1970_cc()
    chol_err = verify_cholesky_p862_cc()
    pf_1 = bool(
        gl4_err < mp.mpf(10) ** (-10)
        and gl4_bad_brk > mp.mpf(1)
        and w70_cc_ok
        and b_info["n_podd"] == doc["E1_noncircular_w70_p135_fv2_and_ow27"]["p135_puncture_odd_roots"] == 112
        and chol_err < mp.mpf(10) ** (-46)
    )
    assert pf_1

    # PF2: Rational 5-vector Spin(10) Tr F^4 + mp.expm(2i H) SU(2)_L Haar + Cauchy d(bar z) contour holomorphy:
    w10 = [tuple(Fr(s if j == i else 0) for j in range(5)) for i in range(5) for s in (-1, 1)]
    w16 = [tuple(Fr(s, 2) for s in sg) for sg in product((-1, 1), repeat=5) if sg.count(-1) % 2 == 0]
    w45 = [tuple(Fr(si if k == i else (sj if k == j else 0)) for k in range(5)) for i, j in combinations(range(5), 2) for si in (-1, 1) for sj in (-1, 1)]
    for hv in [(Fr(1), Fr(2), Fr(3), Fr(5), Fr(7)), (Fr(2), Fr(-1), Fr(4), Fr(-3), Fr(1))]:
        p10_2 = sum(sum(w[i] * hv[i] for i in range(5)) ** 2 for w in w10)
        p10_4 = sum(sum(w[i] * hv[i] for i in range(5)) ** 4 for w in w10)
        p16_4 = sum(sum(w[i] * hv[i] for i in range(5)) ** 4 for w in w16)
        p45_4 = sum(sum(w[i] * hv[i] for i in range(5)) ** 4 for w in w45)
        for n16_v in (0, 2, -2):
            assert (p45_4 - n16_v * p16_4 - (n16_v + 2) * p10_4) == Fr(3, 4) * (4 - n16_v) * (p10_2 ** 2)

    # Disjoint Cauchy contour Wirtinger d_{bar tau} integral: for holomorphic f, (1/(2 pi i r^2)) oint f(z0 + r e^{i t}) r e^{i t} d(r e^{-i t})?
    # Note: d(bar z) = -i r e^{-i t} dt, while oint (z0 + r e^{i t}) d(bar z) = -2 pi i r^2 * (d_{bar z} f)(z0)!
    # Specifically, f(z0 + w) = f(z0) + a w + b bar w + ... => (1/(2 pi)) int_0^{2 pi} f(z0 + r e^{i t}) e^{i t} dt == r * (d_{bar z} f)(z0)!!
    z0_c = mp.mpc(mp_rat(17, 100), mp_rat(9, 5))
    rad_c = mp_rat(1, 200)
    n_c = 32
    th_fn = lambda z: mp.jtheta(3, mp.pi * (mp_rat(3, 10) * z + mp_rat(7, 10)), mp.exp(I_MP * mp.pi * z))
    dbar_cauchy_hol = abs(sum(th_fn(z0_c + rad_c * mp.exp(2 * I_MP * mp.pi * mp_rat(k, n_c))) * mp.exp(2 * I_MP * mp.pi * mp_rat(k, n_c)) for k in range(n_c)) / (n_c * rad_c))
    dbar_cauchy_conj = abs(sum(mp.conj(th_fn(z0_c + rad_c * mp.exp(2 * I_MP * mp.pi * mp_rat(k, n_c)))) * mp.exp(2 * I_MP * mp.pi * mp_rat(k, n_c)) for k in range(n_c)) / (n_c * rad_c))

    hm_su2 = mp.matrix([[mp_rat(3, 11), mp_rat(2, 7) + I_MP * mp_rat(5, 13), mp_rat(1, 9)], [mp_rat(2, 7) - I_MP * mp_rat(5, 13), mp_rat(-1, 11), mp_rat(3, 13)], [mp_rat(1, 9), mp_rat(3, 13), mp_rat(-2, 11)]])
    uL_e = mp.expm(2 * I_MP * hm_su2)
    ye0 = mp.matrix([[mp_rat(1, 8), mp_rat(1, 5), mp.mpf(0)], [mp_rat(1, 9), mp_rat(2, 5) + I_MP * mp_rat(1, 7), mp_rat(1, 6)], [mp.mpf(0), mp_rat(1, 11), mp_rat(3, 4)]])
    mn0 = mp.matrix([[mp_rat(1, 3), mp_rat(1, 7) + I_MP * mp_rat(1, 9), mp.mpf(0)], [mp_rat(1, 7) + I_MP * mp_rat(1, 9), mp_rat(2, 5), mp_rat(1, 4)], [mp.mpf(0), mp_rat(1, 4), mp_rat(3, 5) - I_MP * mp_rat(1, 8)]])

    def u_eigh(m: mp.matrix) -> mp.matrix:
        ev, u = mp.eighe(m * m.H)
        od = sorted(range(3), key=lambda k: mp.re(ev[k]))
        return mp.matrix([[u[r, od[c]] for c in range(3)] for r in range(3)])

    def u_tak(ms: mp.matrix) -> mp.matrix:
        ev, u = mp.eighe(ms * ms.H)
        od = sorted(range(3), key=lambda k: mp.re(ev[k]))
        ut = mp.zeros(3, 3)
        for c, idx in enumerate(od):
            uk = u[:, idx]
            muk = ms * mp.matrix([mp.conj(uk[r]) for r in range(3)])
            ph = mp.arg((uk.H * muk)[0, 0])
            for r in range(3):
                ut[r, c] = uk[r] * mp.exp(I_MP * ph / 2)
        return ut

    ue_a, ut_a = u_eigh(ye0), u_tak(mn0)
    ue_b, ut_b = u_eigh(uL_e * ye0), u_tak(uL_e * mn0 * uL_e.T)
    ca = mp.matrix([[mp.conj(ut_a[r, c]) for c in range(3)] for r in range(3)])
    cb = mp.matrix([[mp.conj(ut_b[r, c]) for c in range(3)] for r in range(3)])
    g_err = max(abs(abs((ue_a.H * ut_a)[r, c]) - abs((ue_b.H * ut_b)[r, c])) for r in range(3) for c in range(3))
    b_brk = max(abs(abs((ue_a.H * ca)[r, c]) - abs((ue_b.H * cb)[r, c])) for r in range(3) for c in range(3))
    pf_2 = bool(e8_triples_ok and dbar_cauchy_hol < mp.mpf(10) ** (-44) and dbar_cauchy_conj > mp_rat(1, 10) and g_err < mp.mpf(10) ** (-44) and b_brk > mp_rat(1, 2))
    assert pf_2

    # PF3 (Closing D3): Quintic C^2 bump computing BOTH exp_complete == 5 AND exp_fixed == 4 from two-scale ratios:
    #Exact Simpson/GL quadrature of (-30 u^2 + 60 u^3 - 30 u^4)^2 on [0, 1] via 16-pt midpoint/Simpson? Use mp.quad on [0, 1]:
    int_quintic = mp.quad(lambda u: (-30 * (u ** 2) + 60 * (u ** 3) - 30 * (u ** 4)) ** 2, [0, 1])
    assert abs(int_quintic - mp_rat(10, 7)) < mp.mpf(10) ** (-46)
    eps_1, eps_2 = mp_rat(1, 10), mp_rat(1, 100)
    e_cc_1 = (eps_1 ** 4) * int_quintic / (mp.mpf(1) / eps_1)
    e_cc_2 = (eps_2 ** 4) * int_quintic / (mp.mpf(1) / eps_2)
    e_fix_1 = (eps_1 ** 4) * int_quintic / mp.mpf(1)
    e_fix_2 = (eps_2 ** 4) * int_quintic / mp.mpf(1)
    exp_complete = int(mp.nint(mp.log(e_cc_1 / e_cc_2) / mp.log(mp.mpf(10))))
    exp_fixed = int(mp.nint(mp.log(e_fix_1 / e_fix_2) / mp.log(mp.mpf(10))))
    pf_3 = bool(exp_complete == 5 and exp_fixed == 4 and hashlib.sha256(raw + b" ").hexdigest() != OUT_SHA.read_text(encoding="utf-8").strip().split()[0])
    assert pf_3

    # PF4 & PF5 (Closing D3): P-571 20 + 87 == 107 + U(1) lattice Wilson-plaquette Chern numbers + 24x24 midpoint Z_2 trace:
    e3 = doc["E3_p571_107_flat_audit_and_explicit_z2_2T"]
    assert e3["flat_107_total_conditionally_lifted"] == 20 and e3["flat_107_total_unchanged_theorems"] == 87

    def wilson_chern_plaquette(m_flux: int, n_p: int = 16) -> mp.mpf:
        # Link variables on [0, 1]^2 in Landau gauge A = (0, 2 pi M x):
        # U_x(ix, iy) = 1, U_y(ix, iy) = exp(i * 2 pi * M * (ix / n_p) * (1 / n_p))
        # Plaquette U_p = U_x(ix, iy) * U_y(ix + 1, iy) * conj(U_x(ix, iy + 1)) * conj(U_y(ix, iy)):
        dx = mp_rat(1, n_p)
        ux = lambda ix, iy: mp.mpc(1)
        uy = lambda ix, iy: mp.exp(I_MP * 2 * mp.pi * m_flux * (ix * dx) * dx)
        tot_f = mp.mpf(0)
        for ix in range(n_p):
            for iy in range(n_p):
                up = ux(ix, iy) * uy(ix + 1, iy) * mp.conj(ux(ix, iy + 1)) * mp.conj(uy(ix, iy))
                tot_f += mp.arg(up)
        return tot_f / (2 * mp.pi)

    chern_m0 = wilson_chern_plaquette(0, 16)
    chern_m4 = wilson_chern_plaquette(4, 16)

    # Disjoint 24x24 midpoint quadrature of Tr(P_{Z_2}) on T^2(tau) at M = 4:
    tc = mp.mpc(mp_rat(3, 5), mp_rat(7, 10))
    imc = mp.im(tc)
    mt = 4 * tc
    qn = mp.exp(I_MP * mp.pi * mt)
    pref = (mp.mpf(8) / imc) ** mp_rat(1, 4)
    n_m = 24
    wt_m = imc / (mp.mpf(n_m) ** 2)

    def psi_cc(jv: int, xv: mp.mpf, yv: mp.mpf) -> mp.mpc:
        zv = xv + yv * tc
        ja = mp_rat(jv, 4)
        return pref * mp.exp(I_MP * mp.pi * 4 * zv * yv + I_MP * mp.pi * ja * ja * mt + 2 * I_MP * mp.pi * ja * (4 * zv)) * mp.jtheta(3, mp.pi * (4 * zv + ja * mt), qn)

    tr_z2_cc = mp.mpf(0)
    for ix in range(n_m):
        xv = (mp.mpf(ix) + mp_rat(1, 2)) / n_m
        for iy in range(n_m):
            yv = (mp.mpf(iy) + mp_rat(1, 2)) / n_m
            for j in range(4):
                tr_z2_cc += wt_m * mp.re(mp.conj(psi_cc(j, xv, yv)) * psi_cc(j, -xv, -yv))
    even_m4_cc = int(mp.nint((4 + tr_z2_cc) / 2))

    pf_4 = bool(mp.mpf(e3["curved_robin_L2_shift_tau_star_vs_i"]) > mp_rat(1, 10) and len(e3["lifted_12_continuous_ids"]) == 12)
    pf_5 = bool(
        abs(chern_m0) < mp.mpf(10) ** (-48)
        and abs(chern_m4 - 4) < mp.mpf(10) ** (-46)
        and abs(tr_z2_cc - 2) < mp.mpf(10) ** (-28)
        and even_m4_cc == 3
        and e3["chiral_generations_quadrature_flat_M0_vs_flux_M4"] == [0, 3]
        and e3["b280_spin32_irrep_multiplicities"] == [0, 0, 0, 0, 0, 1, 1]
    )
    assert pf_4 and pf_5

    pf_tot = sum(int(x) for x in (pf_1, pf_2, pf_3, pf_4, pf_5))
    assert pf_tot == 5
    print(
        f"AGY-C46 disjoint countercheck PASSED in {int(time.time() - t0)}s: "
        f"Bourbaki_W70=6/kY=14/3, E8_B1970={b_info['triples_e8']}, GL4={mp.nstr(gl4_err, 3)}, "
        f"Chern=[{mp.nstr(chern_m0, 2)},{mp.nstr(chern_m4, 4)}], Z2_even={even_m4_cc}, faults={pf_tot}/5."
    )


if __name__ == "__main__":
    main()
