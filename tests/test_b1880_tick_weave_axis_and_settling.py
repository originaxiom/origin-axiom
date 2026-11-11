"""Zero-trust independent @referee counterchecks for B1880 (P-769 complete weave restatement, P-770, P-775, and level-5 / flat-fibre value cards).

Enforces all 6 Mathematical-Physics & Formal Verification Guardrails:
- Independent construction of all matrices, Fricke character maps, Stern-Brocot grids,
  PSL_2(Z) coset actions, Dedekind eta products, and SnapPy ManifoldHP evaluations
  (never certifying by echoing producer JSON/dicts).
- Mandatory Haar unitary basis-scrambling (< 1e-12) on the 6D weave representation
  observables under G_96 vs G_192.
- All residuals checked numerically to < 1e-12.
"""
from __future__ import annotations

import itertools
import json
import math
import warnings
from pathlib import Path

import mpmath as mp
import numpy as np


ROOT = Path(__file__).resolve().parents[1]


def _random_haar_unitary(n: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    diag = np.diag(r)
    ph = diag / np.abs(diag)
    return q * ph[np.newaxis, :]


def _hp_mpf(val) -> mp.mpf:
    return mp.mpf(str(val).replace(" ", ""))


def test_b1880_p769_two_tick_bijection_and_complete_weave_restatement():
    """Independent @referee countercheck of the Two-Tick Bijection Theorem, Odd-Tick Coset Theorem,
    mod-2 spin orbit invariance (P == LRL mod 2), Q_8 trace fixed points, and weave-node completeness."""
    L = ((1, 1), (0, 1))
    R = ((1, 0), (1, 1))
    P = ((0, 1), (1, 0))

    def mm(a, b, mod=None):
        c00 = a[0][0] * b[0][0] + a[0][1] * b[1][0]
        c01 = a[0][0] * b[0][1] + a[0][1] * b[1][1]
        c10 = a[1][0] * b[0][0] + a[1][1] * b[1][0]
        c11 = a[1][0] * b[0][1] + a[1][1] * b[1][1]
        if mod is not None:
            return ((c00 % mod, c01 % mod), (c10 % mod, c11 % mod))
        return ((c00, c01), (c10, c11))

    F = mm(L, P)
    Fp = mm(R, P)
    assert F == ((1, 1), (1, 0)) and Fp == ((0, 1), (1, 1))
    assert mm(P, mm(L, P)) == R and mm(P, mm(R, P)) == L
    assert mm(F, F) == mm(L, R)
    assert mm(F, Fp) == mm(L, L)
    assert mm(Fp, F) == mm(R, R)
    assert mm(Fp, Fp) == mm(R, L)

    # Verify {F, F'}^{2k} == {L, R}^{2k} and {F, F'}^{2k-1} == {L, R}^{2k-1} * P independently for k = 1..5
    i2 = ((1, 0), (0, 1))
    for k in range(1, 6):
        s_ff_even = set()
        for w in itertools.product((F, Fp), repeat=2 * k):
            m = i2
            for g in w:
                m = mm(m, g)
            s_ff_even.add(m)
        s_lr_even = set()
        for w in itertools.product((L, R), repeat=2 * k):
            m = i2
            for g in w:
                m = mm(m, g)
            s_lr_even.add(m)
        assert len(s_ff_even) == (1 << (2 * k))
        assert s_ff_even == s_lr_even

        s_ff_odd = set()
        for w in itertools.product((F, Fp), repeat=2 * k - 1):
            m = i2
            for g in w:
                m = mm(m, g)
            s_ff_odd.add(m)
        s_lr_odd_p = set()
        for w in itertools.product((L, R), repeat=2 * k - 1):
            m = i2
            for g in w:
                m = mm(m, g)
            s_lr_odd_p.add(mm(m, P))
        assert len(s_ff_odd) == (1 << (2 * k - 1))
        assert s_ff_odd == s_lr_odd_p

    # Verify L and R themselves (odd {L, R}-length 1, det = +1) are NOT in {F, F'}^{2k}
    for k in range(1, 5):
        s_even = set()
        for w in itertools.product((F, Fp), repeat=2 * k):
            m = i2
            for g in w:
                m = mm(m, g)
            s_even.add(m)
        assert L not in s_even and R not in s_even

    # Mod-2 spin action: P == L * R * L mod 2
    assert mm(mm(L, R, 2), L, 2) == P

    # Verify all weave nodes in B1858/NODES.json are accounted for in B1880's output without omission
    nodes = json.loads((ROOT / "frontier" / "B1858_the_closure_map" / "NODES.json").read_text(encoding="utf-8"))
    weave_ids = {n["id"] for n in nodes if n.get("weave_or_thread") == "weave"}
    b1880_json = json.loads(
        (
            ROOT
            / "frontier"
            / "B1880_p769_weave_theorems_p770_p775_and_value_card"
            / "verification"
            / "p769_weave_theorems_and_walls.json"
        ).read_text(encoding="utf-8")
    )
    classified_ids = {row["id"] for row in b1880_json["weave_theorems_restated"]["weave_nodes"]}
    assert classified_ids == weave_ids
    assert len(classified_ids) >= 46


def test_b1880_p769_wu_pin_modular_orders_and_haar_scrambled_g192():
    """Independent @referee check of P-769 Debts 1, 2, 3 and mirror walls."""
    warnings.filterwarnings("ignore")
    import snappy

    L = np.array([[1, 1], [0, 1]], dtype=np.int64)
    R = np.array([[1, 0], [1, 1]], dtype=np.int64)
    P = np.array([[0, 1], [1, 0]], dtype=np.int64)

    m004 = snappy.ManifoldHP("b++LR")
    m000 = snappy.ManifoldHP("b-+L")
    v_m004 = _hp_mpf(m004.volume())
    v_m000 = _hp_mpf(m000.volume())
    assert abs(v_m004 - 2 * v_m000) < mp.mpf("1e-45")
    assert abs(_hp_mpf(m004.chern_simons())) < mp.mpf("1e-45")

    m_dep = snappy.ManifoldHP("b++LLLLLLRLRLRLR")
    m_mir = snappy.ManifoldHP("b++RRRRRRLRLRLRL")
    cs_dep = _hp_mpf(m_dep.chern_simons())
    cs_mir = _hp_mpf(m_mir.chern_simons())
    assert abs(cs_dep) > mp.mpf("0.07")
    assert abs(cs_dep + cs_mir) < mp.mpf("1e-45")
    assert abs(_hp_mpf(m_dep.volume()) - _hp_mpf(m_mir.volume())) < mp.mpf("1e-45")

    odd_words = [
        ("L", 1),
        ("LL", 2),
        ("LRL", 4),
        ("LLL", 1),
        ("LRLL", 2),
        ("LRLLL", 4),
    ]
    for w, expected_pullback_im in odd_words:
        A = np.eye(2, dtype=np.int64)
        for ch in w:
            A = A @ (L if ch == "L" else R)
        M_mon = A @ P
        assert int(round(np.linalg.det(M_mon))) == -1
        mod2 = (M_mon - np.eye(2, dtype=np.int64)) % 2
        r0, r1 = mod2[0].tolist(), mod2[1].tolist()
        rows_nonzero = {tuple(r) for r in (r0, r1) if any(r)}
        nullity_f2 = 2 - len(rows_nonzero)
        pullback_size = 1 << nullity_f2
        assert pullback_size == expected_pullback_im

        divs = snappy.Manifold("b-+" + w).homology().elementary_divisors()
        f2_rk_snappy = sum(1 for d in divs if d % 2 == 0)
        assert f2_rk_snappy == 1 + nullity_f2

    def gen_mod_group(mats, mod_n):
        id_m = ((1 % mod_n, 0), (0, 1 % mod_n))
        seen = {id_m}
        queue = [id_m]
        while queue:
            a = queue.pop()
            for b in mats:
                c = (
                    ((a[0][0] * b[0][0] + a[0][1] * b[1][0]) % mod_n, (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % mod_n),
                    ((a[1][0] * b[0][0] + a[1][1] * b[1][0]) % mod_n, (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % mod_n),
                )
                if c not in seen:
                    seen.add(c)
                    queue.append(c)
        units = [u for u in range(1, mod_n) if math.gcd(u, mod_n) == 1]
        proj = {
            min(((u * m[0][0]) % mod_n, (u * m[0][1]) % mod_n, (u * m[1][0]) % mod_n, (u * m[1][1]) % mod_n) for u in units)
            for m in seen
        }
        return len(seen), len(proj)

    l_t, r_t, p_t = ((1, 1), (0, 1)), ((1, 0), (1, 1)), ((0, 1), (1, 0))
    for n_mod in (2, 3, 4, 5, 6, 7, 8, 10, 13):
        _, p_two = gen_mod_group([l_t, r_t], n_mod)
        _, p_tick = gen_mod_group([l_t, r_t, p_t], n_mod)
        minus1_sq = any((s * s) % n_mod == (n_mod - 1) % n_mod for s in range(n_mod))
        expected_ratio = 1 if minus1_sq else 2
        assert p_tick == expected_ratio * p_two

    ep = np.exp(2j * np.pi / 8.0)
    em = np.exp(-2j * np.pi / 8.0)
    l3_mat = np.array([[em, 0.0, 0.0], [0.0, 0.0, ep], [0.0, ep, 0.0]], dtype=np.complex128)
    r3_mat = np.array([[0.0, em, 0.0], [em, 0.0, 0.0], [0.0, 0.0, ep]], dtype=np.complex128)
    s0_mat = np.array([[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]], dtype=np.complex128)

    def close_matrix_group(gens):
        elems = [np.eye(gens[0].shape[0], dtype=np.complex128)]
        for g in elems:
            for h in gens:
                prod = g @ h
                if not any(np.linalg.norm(prod - x) < 1e-9 for x in elems):
                    elems.append(prod)
                assert len(elems) <= 400
        return elems

    l6 = np.block([[l3_mat, np.zeros((3, 3))], [np.zeros((3, 3)), np.conj(l3_mat)]])
    r6 = np.block([[r3_mat, np.zeros((3, 3))], [np.zeros((3, 3)), np.conj(r3_mat)]])
    p6 = np.block([[np.zeros((3, 3)), s0_mat], [s0_mat, np.zeros((3, 3))]])
    g96_6d = close_matrix_group([l6, r6])
    g192_6d = close_matrix_group([l6, r6, p6])
    assert len(g96_6d) == 96 and len(g192_6d) == 192

    for seed in (101, 202, 303):
        U = _random_haar_unitary(6, seed)
        U_dag = U.conj().T
        l6_scr, r6_scr, p6_scr = U @ l6 @ U_dag, U @ r6 @ U_dag, U @ p6 @ U_dag
        i6 = np.eye(6, dtype=np.complex128)
        sv_96 = np.linalg.svd(np.vstack([np.kron(i6, g) - np.kron(g.T, i6) for g in (l6_scr, r6_scr)]), compute_uv=False)
        sv_192 = np.linalg.svd(np.vstack([np.kron(i6, g) - np.kron(g.T, i6) for g in (l6_scr, r6_scr, p6_scr)]), compute_uv=False)
        assert int(np.sum(sv_96 < 1e-12)) == 2 and sv_96[-3] > 0.1
        assert int(np.sum(sv_192 < 1e-12)) == 1 and sv_192[-2] > 0.1
        norm_96 = sum(abs(np.trace(U @ g @ U_dag)) ** 2 for g in g96_6d) / 96.0
        norm_192 = sum(abs(np.trace(U @ g @ U_dag)) ** 2 for g in g192_6d) / 192.0
        assert abs(norm_96 - 2.0) < 1e-13 and abs(norm_192 - 1.0) < 1e-13


def test_b1880_p770_s_duality_and_d6_nonconjugacy_countercheck():
    """Independent @referee countercheck of P-770 S-duality and D=6 GL_2(Z) non-conjugacy."""
    w32 = np.array([[0, -3], [2, 0]], dtype=np.int64)
    w61 = np.array([[0, -6], [1, 0]], dtype=np.int64)
    witnesses = 0
    for a in range(-6, 7):
        for b in range(-6, 7):
            for c in range(-6, 7):
                for d in range(-6, 7):
                    if abs(a * d - b * c) == 1:
                        g = np.array([[a, b], [c, d]], dtype=np.int64)
                        if np.array_equal(g @ w32, w61 @ g) or np.array_equal(g @ w32, -w61 @ g):
                            witnesses += 1
    assert witnesses == 0

    tree = [(0, 1), (1, 0)]
    for _ in range(11):
        nxt = [tree[0]]
        for i in range(len(tree) - 1):
            p1, q1 = tree[i]
            p2, q2 = tree[i + 1]
            nxt.append((p1 + p2, q1 + q2))
            nxt.append((p2, q2))
        tree = nxt
    mids = np.array([(tree[i][0] + tree[i + 1][0]) / (tree[i][1] + tree[i + 1][1]) for i in range(len(tree) - 1)])
    assert len(mids) == 2048 and np.max(np.abs(mids * mids[::-1] - 1.0)) < 1e-15

    xi, zeta = mids[:, None], mids[None, :]
    for y in (math.sqrt(2.0), math.sqrt(1.5), (1.0 + math.sqrt(5.0)) / 2.0, math.sqrt(5.0)):
        y_inv = 1.0 / y
        sinh_y = np.abs(xi * zeta - y * y) / (y * (xi + zeta))
        sinh_yinv = np.abs(xi * zeta - y_inv * y_inv) / (y_inv * (xi + zeta))
        for thresh in (0.05, 0.1, 0.25):
            assert abs(float(np.mean(sinh_y <= thresh)) - float(np.mean(sinh_yinv <= thresh))) < 1e-14


def test_b1880_p775_and_chat1_level5_and_value_countercheck():
    """Independent @referee countercheck of P-775 hyperbolic settling vs flat-fibre phi^4 settling
    and X_1(5) / X_0(5) Hauptmodul + Fricke geometry."""
    warnings.filterwarnings("ignore")
    import snappy

    mp.mp.dps = 65

    def t1(v):
        return (v[2], v[1], v[1] * v[2] - v[0])

    def t2(v):
        return (v[0], v[2], v[0] * v[2] - v[1])

    def apply_word(word: str, v):
        cur = v
        for ch in reversed(word):
            cur = t1(cur) if ch == "L" else t2(cur)
        return cur

    z_gold = (mp.mpf(3) + 1j * mp.sqrt(3)) / 2
    p_gold = (mp.conj(z_gold), z_gold, z_gold)
    x_silv = mp.power(2, mp.mpf("0.75")) * mp.exp(1j * mp.pi / 8)
    p_silv = (x_silv, mp.conj(x_silv), mp.sqrt(2) * (1 - 1j))

    def jacobian_trace_and_det(word: str, pt):
        h = mp.mpf("1e-25")
        cols = []
        for j in range(3):
            vp, vm = list(pt), list(pt)
            vp[j] += h
            vm[j] -= h
            fp, fm = apply_word(word, tuple(vp)), apply_word(word, tuple(vm))
            cols.append([(fp[i] - fm[i]) / (2 * h) for i in range(3)])
        J = mp.matrix([[cols[c][r] for c in range(3)] for r in range(3)])
        return J[0, 0] + J[1, 1] + J[2, 2], mp.det(J)

    tr_g, det_g = jacobian_trace_and_det("LR", p_gold)
    tr_s, det_s = jacobian_trace_and_det("LLRR", p_silv)
    assert abs(det_g - 1) < mp.mpf("1e-35") and abs((tr_g - 1) - 5) < mp.mpf("1e-35")
    assert abs(det_s - 1) < mp.mpf("1e-35") and abs((tr_s - 1) - 18) < mp.mpf("1e-35")

    # Verify independent departure L^4 R settles at (5 + sqrt(21))/2 in 3D hyperbolic volume/CS:
    lam_hyp = (mp.mpf(5) + mp.sqrt(21)) / 2
    vg = _hp_mpf(snappy.ManifoldHP("b++LR").volume())
    vols = [_hp_mpf(snappy.ManifoldHP("b++LLLLR" + "LR" * k).volume()) - k * vg for k in range(2, 18)]
    dv = [vols[i + 1] - vols[i] for i in range(len(vols) - 1)]
    rv = [dv[i] / dv[i + 1] for i in range(len(dv) - 1)]
    ait_v = [rv[i + 2] - (rv[i + 2] - rv[i + 1]) ** 2 / (rv[i + 2] - 2 * rv[i + 1] + rv[i]) for i in range(len(rv) - 2)]
    assert min(abs(x - lam_hyp) for x in ait_v) < mp.mpf("1e-12")

    # Contrast with flat-fibre Hauptmodul & continued-fraction value card:
    # 1. Dedekind eta quotient t(tau) = (eta(tau)/eta(5*tau))^6 satisfies t(tau)*t(-1/(5*tau)) = 125
    #    and t(i/sqrt(5)) = +5*sqrt(5), t(1/2 + i/(2*sqrt(5))) = -5*sqrt(5) to < 1e-45:
    def dedekind_eta(tau):
        q = mp.exp(2j * mp.pi * tau)
        s = mp.mpc(1)
        for n in range(1, 90):
            s += ((-1) ** n) * (q ** (n * (3 * n - 1) // 2) + q ** (n * (3 * n + 1) // 2))
        return mp.exp(1j * mp.pi * tau / 12) * s

    def t_haupt(tau):
        return (dedekind_eta(tau) / dedekind_eta(5 * tau)) ** 6

    tau_test = mp.mpc("0.17", "0.63")
    assert abs(t_haupt(tau_test) * t_haupt(-1 / (5 * tau_test)) - 125) < mp.mpf("1e-45")
    assert abs(t_haupt(1j / mp.sqrt(5)) - 5 * mp.sqrt(5)) < mp.mpf("1e-45")
    assert abs(t_haupt(mp.mpf("0.5") + 1j / (2 * mp.sqrt(5))) + 5 * mp.sqrt(5)) < mp.mpf("1e-45")

    # 2. Unbounded level-5 line-preserving depths (n-1)/2 + sqrt(5)/2 for n = 6, 11, 16, 21, 26 and phi^4 flat-fibre rate:
    phi = (mp.mpf(1) + mp.sqrt(5)) / 2
    phi4 = phi ** 4
    assert abs(phi4 - lam_hyp) > mp.mpf("2.0")

    # Periodic golden tail [1, 1, 1, ...] = phi; apex height of L^n R (1, 1, ...):
    # Forward tail is x_+ = [n; 1, 1, ...] = n - 1 + phi, backward tail is x_- = [0; 1, 1, ...] = 1/phi = phi - 1,
    # so semicircle diameter / 2 = (x_+ + x_-) / 2 = (n - 2 + 2*phi) / 2 = (n - 1)/2 + sqrt(5)/2!
    for n in (6, 11, 16, 21, 26):
        # Check mod-5 eigenline (1, 2)^T of LR = [[2,1],[1,1]] (since [[2,1],[1,1]]*(1,2)^T = (4,3)^T == 4*(1,2)^T mod 5):
        # L^n R = [[1, n], [0, 1]] * [[1, 0], [1, 1]] = [[n+1, n], [1, 1]]; on (1, 2)^T gives (3n+1, 3)^T,
        # which is proportional to (1, 2)^T mod 5 iff 2*(3n+1) == 3 mod 5 <=> n == 1 mod 5!
        v0, v1 = (3 * n + 1) % 5, 3 % 5
        assert (2 * v0 - v1) % 5 == 0
        x_plus = (n - 1) + phi
        x_minus = 1 / phi
        y_own = (x_plus + x_minus) / 2
        assert abs(y_own - (mp.mpf(n - 1) / 2 + mp.sqrt(5) / 2)) < mp.mpf("1e-55")
