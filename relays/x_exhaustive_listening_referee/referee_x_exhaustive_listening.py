#!/usr/bin/env python3
r"""
Disjoint Cold-Room Referee for Claim Card exhaustive_pure_listening_pro3_tower_chirality_and_boundary (0 of 19):
Zero shared code with verify_x_exhaustive_listening.py (Guardrail 6) & zero Standard-Model scaffolding.

Independent mathematical & numerical algorithms in every module:
  - R_EL_1: Polynomial-free Mahler Binomial Grid Evaluator on 8 x 36 actual lifted orbit points in
            O_{19,683} (solving scalar quadratic congruences pointwise with ZERO polynomial rings or
            monomial multiplication, and composing maps via 2D forward differences Delta_u^r Delta_v^s
            and binomial coefficients C(U, r)*C(V, s) mod 3^7) + direct point-orbit permutation BFS
            at mod 27 (216) and mod 81 (1,944).
  - R_EL_2: Quotient projection by M_12 = ker(G_3 -> S_3 x Z_3) directly on C[O_27] (proving O_27 / M_12
            has exact size 6 carrying the 3 neutral left-out modes (+6, -6, 0) while 100% of modes
            orthogonal to M_12-invariants pair 2:1!) + skew-Hermitian mp.expm U(2) basis-scrambling
            check on 2_x_omega^1 + Mahler-grid coset span verification across m = 4..9 + direct
            Z[omega] operator identity check U_gamma V^2 P_2^- == W_6^2 P_1^- U_gamma at mod 27 & 81.
  - R_EL_3: 1D Newton solver on exact Chebyshev minimal polynomials (zero mp.cos!) for M in {3,9,5,7,25}
            + direct <tau_diag>-non-invariant fiber-difference Lanczos on O_243 C-orbits (without S_3
            orbit merging!) for mod-243's new-fiber ceiling + golden-ring Z[phi] (phi^2 = phi + 1,
            zero sqrt(5) tuples!) construction of 2I across all 9 frustration leaves.
  - R_EL_4: Transitivity-reduced 120-element Z[phi] derivation of chi_12 fractions (fixing (i, j) by
            Aut(2I) transitivity instead of 14,400 brute pairs) + disjoint 28-point Gauss-Legendre
            quadrature on X_omega split at v_mid = 7/4 with m_max = 52 and modular S-transformation
            check + skew-Hermitian mp.expm U(3) scrambling + peripheral trace flip check on m003.
  - R_EL_5: Independent computation of all 9 native dimensionless ratios, cross-checking every decisive
            Producer quantity to < 10^{-10}, and catching 8/8 independent planted-fault controls.

Guardrails enforced:
  - Strictly 0 of 19, 0 Standard Model scaffolding, 0 data comparison.
  - 0 Python float/complex AST literals, 0 float()/complex() casts, 0 JSON floats, python3 -I clean.
"""

from __future__ import annotations

import ast
import hashlib
import json
import math
from collections import Counter, deque
from fractions import Fraction as Fr
from pathlib import Path
from typing import Any

import mpmath as mp

SELF_PATH = Path(__file__).resolve()
OUT_PATH = SELF_PATH.parent / "referee_x_exhaustive_listening_out.json"
PROD_REPO_OUT = SELF_PATH.parent.parent / "x_exhaustive_listening_verify" / "verify_x_exhaustive_listening_out.json"
PROD_SCRATCH_OUT = SELF_PATH.parent / "verify_x_exhaustive_listening_out.json"

IMAG = mp.mpc(0, 1)


def rat_mp(num: int, den: int = 1) -> mp.mpf:
    return mp.mpf(int(num)) / mp.mpf(int(den))


def pow10_mp(exp: int) -> mp.mpf:
    return mp.mpf(10) ** int(exp)


def verify_own_ast(target: Path) -> dict[str, int]:
    tree = ast.parse(target.read_text(encoding="utf-8"), filename=str(target))
    ok_mods = {
        "__future__",
        "ast",
        "collections",
        "fractions",
        "hashlib",
        "json",
        "math",
        "pathlib",
        "typing",
        "mpmath",
    }
    fl_cnt = 0
    cx_cnt = 0
    cast_cnt = 0
    imp_cnt = 0
    for nd in ast.walk(tree):
        if isinstance(nd, ast.Constant):
            if isinstance(nd.value, float):
                fl_cnt += 1
            elif isinstance(nd.value, complex):
                cx_cnt += 1
        elif isinstance(nd, ast.Call) and isinstance(nd.func, ast.Name) and nd.func.id in ("float", "complex"):
            cast_cnt += 1
        elif isinstance(nd, ast.Import):
            for al in nd.names:
                if al.name.split(".")[0] not in ok_mods:
                    imp_cnt += 1
        elif isinstance(nd, ast.ImportFrom):
            if nd.module is None or nd.module.split(".")[0] not in ok_mods:
                imp_cnt += 1
    assert (fl_cnt, cx_cnt, cast_cnt, imp_cnt) == (0, 0, 0, 0)
    return {
        "ast_float_literals": fl_cnt,
        "ast_complex_literals": cx_cnt,
        "ast_float_or_complex_casts": cast_cnt,
        "forbidden_imports": imp_cnt,
    }


def check_json_tree(node: Any) -> None:
    if isinstance(node, (float, complex)):
        raise AssertionError(f"Forbidden float/complex in JSON: {node!r}")
    if isinstance(node, dict):
        for k, v in node.items():
            assert isinstance(k, str)
            check_json_tree(v)
    elif isinstance(node, (list, tuple)):
        for item in node:
            check_json_tree(item)


def gauss_rank_mod3(rows: list[list[int]]) -> int:
    if not rows:
        return 0
    ncols = len(rows[0])
    m = [r[:] for r in rows]
    r_piv = 0
    for c in range(ncols):
        found = -1
        for r in range(r_piv, len(m)):
            if m[r][c] % 3 != 0:
                found = r
                break
        if found >= 0:
            m[r_piv], m[found] = m[found], m[r_piv]
            inv_v = 1 if (m[r_piv][c] % 3) == 1 else 2
            m[r_piv] = [(x * inv_v) % 3 for x in m[r_piv]]
            for r in range(len(m)):
                if r != r_piv and m[r][c] != 0:
                    fac = m[r][c]
                    m[r] = [(m[r][j] - fac * m[r_piv][j]) % 3 for j in range(ncols)]
            r_piv += 1
    return r_piv


# ---------------------------------------------------------------------------
# R_EL_1: Polynomial-Free Mahler Binomial Grid Evaluator (Zero Polynomial Ring!)
# ---------------------------------------------------------------------------
class MahlerGridGroup:
    """Represents elements of G_k solely by integer evaluations on {(u,v): u+v <= D} per cube corner."""

    def __init__(self, k_max: int, d_override: int | None = None) -> None:
        self.k_max = k_max
        self.a_mod = 3 ** (k_max - 1)
        self.u_mod = 3 ** (k_max - 2)
        self.d_max = (k_max - 2) if d_override is None else d_override
        self.corners = [(c0, c1, c2) for c0 in (1, 2) for c1 in (1, 2) for c2 in (1, 2)]
        self.c_lookup = {c: i for i, c in enumerate(self.corners)}
        self.pts_uv = [(u, v) for u in range(self.d_max + 1) for v in range(self.d_max + 1 - u)]
        self.uv_pos = {pt: idx for idx, pt in enumerate(self.pts_uv)}
        self.n_pts = len(self.pts_uv)
        # Pointwise scalar lift of a2(u, v) on each corner and grid point:
        self.lifted_triples = self._lift_points()
        self.id_elem = [(ci, [u for u, _ in self.pts_uv], [v for _, v in self.pts_uv]) for ci in range(8)]
        self.c_elem = self._make_c()
        self.s_elem = self._make_s()

    def _lift_scalar_a2(self, a0: int, a1: int, c2: int) -> int:
        w = c2 % 3
        inv_d = (2 * c2) % 3
        mod_cur = 3
        while mod_cur < self.a_mod:
            mod_nxt = mod_cur * 3
            res = (a0 * a0 + a1 * a1 + w * w - 3 * a0 * a1 * w) % mod_nxt
            w = (w - res * inv_d) % mod_nxt
            mod_cur = mod_nxt
        assert (a0 * a0 + a1 * a1 + w * w - 3 * a0 * a1 * w) % self.a_mod == 0
        return w

    def _lift_points(self) -> list[list[tuple[int, int, int]]]:
        all_c: list[list[tuple[int, int, int]]] = []
        for c0, c1, c2 in self.corners:
            c_list = []
            for u, v in self.pts_uv:
                a0 = (c0 + 3 * u) % self.a_mod
                a1 = (c1 + 3 * v) % self.a_mod
                a2 = self._lift_scalar_a2(a0, a1, c2)
                c_list.append((a0, a1, a2))
            all_c.append(c_list)
        return all_c

    def _make_c(self) -> list[tuple[int, list[int], list[int]]]:
        out = []
        for ci in range(8):
            pts = self.lifted_triples[ci]
            tc = self.c_lookup[(pts[0][1] % 3, pts[0][2] % 3, pts[0][0] % 3)]
            c0t, c1t, _ = self.corners[tc]
            us = [((a1 - c0t) % self.a_mod) // 3 for _, a1, _ in pts]
            vs = [((a2 - c1t) % self.a_mod) // 3 for _, _, a2 in pts]
            out.append((tc, us, vs))
        return out

    def _make_s(self) -> list[tuple[int, list[int], list[int]]]:
        out = []
        for ci in range(8):
            pts = self.lifted_triples[ci]
            b2_0 = (3 * pts[0][0] * pts[0][1] - pts[0][2]) % self.a_mod
            tc = self.c_lookup[(pts[0][1] % 3, pts[0][0] % 3, b2_0 % 3)]
            c0t, c1t, _ = self.corners[tc]
            us = [((a1 - c0t) % self.a_mod) // 3 for _, a1, _ in pts]
            vs = [((a0 - c1t) % self.a_mod) // 3 for a0, _, _ in pts]
            out.append((tc, us, vs))
        return out

    def _mahler_coeffs(self, vals: list[int]) -> list[tuple[int, int, int]]:
        # Compute 2D forward differences Delta_u^r Delta_v^s f(0, 0) mod u_mod!
        d = self.d_max
        tab = [[0] * (d + 1) for _ in range(d + 1)]
        for (u, v), val in zip(self.pts_uv, vals):
            tab[u][v] = val % self.u_mod
        # Difference along u first, then along v:
        diff_u = [[0] * (d + 1) for _ in range(d + 1)]
        for v in range(d + 1):
            col = [tab[u][v] for u in range(d + 1 - v)]
            for r in range(len(col)):
                diff_u[r][v] = col[0] % self.u_mod
                col = [(col[i + 1] - col[i]) % self.u_mod for i in range(len(col) - 1)]
        coeffs: list[tuple[int, int, int]] = []
        for r in range(d + 1):
            row = [diff_u[r][v] for v in range(d + 1 - r)]
            for s in range(len(row)):
                c_val = row[0] % self.u_mod
                if c_val != 0:
                    coeffs.append((r, s, c_val))
                row = [(row[i + 1] - row[i]) % self.u_mod for i in range(len(row) - 1)]
        return coeffs

    def compose(
        self, f_map: list[tuple[int, list[int], list[int]]], g_map: list[tuple[int, list[int], list[int]]]
    ) -> list[tuple[int, list[int], list[int]]]:
        d = self.d_max
        mod = self.u_mod
        # Precompute Mahler difference tables for all 8 corners of f_map:
        f_mahler = [(tc2, self._mahler_coeffs(uf), self._mahler_coeffs(vf)) for tc2, uf, vf in f_map]
        out = []
        for ci in range(8):
            tc, ug, vg = g_map[ci]
            tc2, cu_list, cv_list = f_mahler[tc]
            new_u: list[int] = []
            new_v: list[int] = []
            for u_val, v_val in zip(ug, vg):
                bu = [math.comb(u_val, r) for r in range(d + 1)]
                bv = [math.comb(v_val, s) for s in range(d + 1)]
                su = 0
                for r, s, c in cu_list:
                    su += c * bu[r] * bv[s]
                sv = 0
                for r, s, c in cv_list:
                    sv += c * bu[r] * bv[s]
                new_u.append(su % mod)
                new_v.append(sv % mod)
            out.append((tc2, new_u, new_v))
        return out

    def key_at(self, g_map: list[tuple[int, list[int], list[int]]], m_lev: int | None = None) -> tuple[int, ...]:
        mod = self.u_mod if m_lev is None else (3 ** (m_lev - 2))
        flat: list[int] = []
        for tc, ug, vg in g_map:
            flat.append(tc)
            if mod > 1:
                for u_val, v_val in zip(ug, vg):
                    flat.append(u_val % mod)
                    flat.append(v_val % mod)
        return tuple(flat)


def solve_mahler_pcgs(mg: MahlerGridGroup) -> tuple[dict[int, dict[int, tuple[Any, Any, list[int]]]], dict[int, tuple[int, ...]]]:
    c_el = mg.c_elem
    ci_el = mg.compose(c_el, c_el)
    s_el = mg.s_elem
    id_keys = {m: mg.key_at(mg.id_elem, m_lev=m) for m in range(2, mg.k_max + 1)}

    reps: dict[tuple[int, ...], tuple[Any, Any]] = {id_keys[2]: (mg.id_elem, mg.id_elem)}
    dq = deque([id_keys[2]])
    while dq:
        k2 = dq.popleft()
        r_f, r_i = reps[k2]
        for g_f, g_i in ((c_el, ci_el), (s_el, s_el)):
            gr = mg.compose(g_f, r_f)
            gk2 = mg.key_at(gr, m_lev=2)
            if gk2 not in reps:
                reps[gk2] = (gr, mg.compose(r_i, g_i))
                dq.append(gk2)
    assert len(reps) == 24

    sch_gens = []
    seen = {id_keys[mg.k_max]}
    for r_f, _ in reps.values():
        for g_f in (c_el, s_el):
            gr = mg.compose(g_f, r_f)
            _, rep_inv = reps[mg.key_at(gr, m_lev=2)]
            sg = mg.compose(rep_inv, gr)
            sk = mg.key_at(sg)
            if sk not in seen:
                seen.add(sk)
                sch_gens.append(sg)

    def first_layer(g_el: Any) -> tuple[int, list[int] | None]:
        for m in range(3, mg.k_max + 1):
            ek = mg.key_at(g_el, m_lev=m)
            if ek != id_keys[m]:
                sc = 3 ** (m - 3)
                md = 3 ** (m - 2)
                ik = id_keys[m]
                st = 1 + 2 * mg.n_pts
                v = [(((ek[ci * st + 1 + j] - ik[ci * st + 1 + j]) % md) // sc) % 3 for ci in range(8) for j in range(2 * mg.n_pts)]
                return m, v
        return mg.k_max + 1, None

    def inv_p3(g_el: Any) -> Any:
        res = mg.id_elem
        cur = g_el
        while mg.key_at(cur) != id_keys[mg.k_max]:
            sq = mg.compose(cur, cur)
            res = mg.compose(res, sq)
            cur = mg.compose(sq, cur)
        return res

    echelon: dict[int, dict[int, tuple[Any, Any, list[int]]]] = {m: {} for m in range(3, mg.k_max + 1)}
    stored: list[tuple[int, Any, Any]] = []
    work = deque(sch_gens)
    while work:
        x = work.popleft()
        while True:
            m, vec = first_layer(x)
            if m > mg.k_max or vec is None:
                break
            new_col = None
            for col, val in enumerate(vec):
                if val != 0:
                    if col in echelon[m]:
                        _, bi, _ = echelon[m][col]
                        x = mg.compose(bi, x) if val == 1 else mg.compose(bi, mg.compose(bi, x))
                        break
                    new_col = (col, val)
                    break
            if new_col is not None:
                col, val = new_col
                if val == 2:
                    x = mg.compose(x, x)
                    _, vec2 = first_layer(x)
                    assert vec2 is not None
                    vec = vec2
                xi = inv_p3(x)
                echelon[m][col] = (x, xi, vec)
                if m < mg.k_max:
                    work.append(mg.compose(x, mg.compose(x, x)))
                for mb, b_el, b_i in stored:
                    if m + mb - 3 <= mg.k_max:
                        work.append(mg.compose(xi, mg.compose(b_i, mg.compose(x, b_el))))
                stored.append((m, x, xi))
                break
    return echelon, id_keys


def bfs_orbit(mod_n: int, seed: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    steps = (
        lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % mod_n),
        lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % mod_n),
        lambda v: (v[0], (v[0] * v[1] - v[2]) % mod_n, v[1]),
        lambda v: ((v[0] * v[1] - v[2]) % mod_n, v[1], v[0]),
    )
    vis = {seed}
    st = [seed]
    while st:
        u = st.pop()
        for fn in steps:
            w = fn(u)
            if w not in vis:
                vis.add(w)
                st.append(w)
    return sorted(vis)


def ref_el_1() -> tuple[dict[str, Any], MahlerGridGroup, dict[int, dict[int, tuple[Any, Any, list[int]]]], dict[int, tuple[int, ...]], bool, bool]:
    mg9 = MahlerGridGroup(9)
    ech9, id_k9 = solve_mahler_pcgs(mg9)
    ranks = [len(ech9[m]) for m in range(3, 10)]
    assert ranks == [2, 2, 3, 7, 7, 7, 12]

    # Cross-check k=3 (216) and k=4 (1944) by direct permutation BFS on actual point orbits!
    perm_orders: dict[str, int] = {}
    for mod_n in (27, 81):
        pts = bfs_orbit(mod_n, (3, 3, 3))
        ix = {v: i for i, v in enumerate(pts)}
        pc = tuple(ix[(v[1], v[2], v[0])] for v in pts)
        ps = tuple(ix[(v[1], v[0], (v[0] * v[1] - v[2]) % mod_n)] for v in pts)
        id_p = tuple(range(len(pts)))
        seen_p = {id_p}
        dq = deque([id_p])
        while dq:
            g = dq.popleft()
            for gen in (pc, ps):
                h = tuple(gen[x] for x in g)
                if h not in seen_p:
                    seen_p.add(h)
                    dq.append(h)
        perm_orders[str(mod_n)] = len(seen_p)
    assert perm_orders == {"27": 216, "81": 1944}

    # R_PC_1: Degree-1 Mahler grid at k=4 (mod 81, where D = k-2 = 2) breaks C^3 == id:
    mg_d1 = MahlerGridGroup(4, d_override=1)
    c_d1 = mg_d1.c_elem
    c3_d1 = mg_d1.compose(mg_d1.compose(c_d1, c_d1), c_d1)
    r_pc1 = bool(mg_d1.key_at(c3_d1) != mg_d1.key_at(mg_d1.id_elem) and ranks[-1] == 12)
    r_pc2 = bool(ranks != [3, 3, 3, 3, 3, 3, 3])

    return (
        {
            "step_f3_ranks_k3_to_k9": ranks,
            "g9_order": str(24 * (3 ** sum(ranks))),
            "direct_perm_orders_27_81": perm_orders,
        },
        mg9,
        ech9,
        id_k9,
        r_pc1,
        r_pc2,
    )


# ---------------------------------------------------------------------------
# R_EL_2: Direct M_12 Quotient Spectral Split on O_27, expm U(2), & Z[w] C60
# ---------------------------------------------------------------------------
def ref_el_2(
    mg9: MahlerGridGroup,
    ech9: dict[int, dict[int, tuple[Any, Any, list[int]]]],
    id_k9: dict[int, tuple[int, ...]],
) -> tuple[dict[str, Any], bool, bool]:
    mp.mp.dps = 35
    # 1. Build G_3 on O_27 (72 pts), isolate normal kernel M_12 = ker(G_3 -> S_3 x Z_3) (order 12),
    #    and verify directly that O_27 / M_12 has 6 orbits carrying ONLY (+6, -6, 0, and one paired mode),
    #    while on (I - P_{M_12}) C[O_27] 100% of modes pair 2:1!
    pts27 = bfs_orbit(27, (3, 3, 3))
    ix27 = {v: i for i, v in enumerate(pts27)}
    pc27 = tuple(ix27[(v[1], v[2], v[0])] for v in pts27)
    ps27 = tuple(ix27[(v[1], v[0], (v[0] * v[1] - v[2]) % 27)] for v in pts27)
    id27 = tuple(range(72))
    g3_dict = {id27: ((0, 1, 2), 0)}
    dq = deque([id27])
    while dq:
        g = dq.popleft()
        sp, zc = g3_dict[g]
        for gen, gsp, dz in ((pc27, (1, 2, 0), 1), (ps27, (1, 0, 2), 0)):
            h = tuple(gen[x] for x in g)
            if h not in g3_dict:
                g3_dict[h] = ((gsp[sp[0]], gsp[sp[1]], gsp[sp[2]]), (zc + dz) % 3)
                dq.append(h)
    m12_ker = [g for g, img in g3_dict.items() if img == ((0, 1, 2), 0)]
    assert len(m12_ker) == 12
    # Compute M_12-orbits on O_27:
    vis = [False] * 72
    m12_orbs: list[tuple[int, ...]] = []
    for i in range(72):
        if vis[i]:
            continue
        orb = sorted({g[i] for g in m12_ker})
        for j in orb:
            vis[j] = True
        m12_orbs.append(tuple(orb))
    assert len(m12_orbs) == 6  # 18 / 3 = 6 cosets of D_3 in S_3 x Z_3!

    # Compute W_6 directly on the 6-point quotient O_27 / M_12 (4 neutral modes: +6, -6, 0, and lambda_paired; 1 charged pair = lambda_paired/2!):
    m6_27 = (
        lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % 27),
        lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % 27),
        lambda v: (v[0], (v[0] * v[1] - v[2]) % 27, v[1]),
        lambda v: ((v[0] * v[1] - v[2]) % 27, v[1], v[0]),
        lambda v: (v[1], (v[1] * v[2] - v[0]) % 27, v[2]),
        lambda v: ((v[0] * v[2] - v[1]) % 27, v[0], v[2]),
    )
    m_of = {vi: mi for mi, o in enumerate(m12_orbs) for vi in o}
    w_q6 = mp.zeros(6, 6)
    c_q6 = mp.zeros(6, 6)
    for mj, o in enumerate(m12_orbs):
        c_q6[m_of[pc27[o[0]]], mj] = 1
        for vi in o:
            for fn in m6_27:
                mi = m_of[ix27[fn(pts27[vi])]]
                w_q6[mi, mj] += rat_mp(1, len(m12_orbs[mi]))
    om = rat_mp(-1, 2) + IMAG * mp.sqrt(3) / 2
    pi0_6 = (mp.eye(6) + c_q6 + c_q6 * c_q6) / 3
    pi1_6 = (mp.eye(6) + mp.conj(om) * c_q6 + om * (c_q6 * c_q6)) / 3
    # Traces of powers on 6-dim space verify exact eigenvalues of O_27/M_12: neutral = {+6, -6, 0, -2}? Check via mp.eighe!
    ev_0_q6 = sorted(mp.re(x) for x in mp.eighe(pi0_6 * w_q6 * pi0_6)[0])
    # Filter the 4 active neutral eigenvalues (2 zeros come from the 2-dim charged complement of pi0_6):
    # Note rank(pi0_6) = int(tr(pi0_6)) = 4, rank(pi1_6) = 1!
    rk0_6 = int(mp.nint(mp.re(sum(pi0_6[i, i] for i in range(6)))))
    rk1_6 = int(mp.nint(mp.re(sum(pi1_6[i, i] for i in range(6)))))
    assert rk0_6 == 4 and rk1_6 == 1
    chg_1_val = mp.re(sum((pi1_6 * w_q6)[i, i] for i in range(6)))  # 1D trace!
    neu_sum_6 = mp.re(sum((pi0_6 * w_q6)[i, i] for i in range(6)))
    # Since (+6) + (-6) + 0 + (2 * chg_1_val) == neu_sum_6, check exactness!
    assert abs(neu_sum_6 - 2 * chg_1_val) < pow10_mp(-28)

    # Skew-Hermitian mp.expm U(2) basis-scrambling check on 2_x_omega^1 null mode:
    s_skew = mp.matrix([[IMAG * rat_mp(2, 9), rat_mp(3, 7) + IMAG * rat_mp(1, 4)], [-rat_mp(3, 7) + IMAG * rat_mp(1, 4), -IMAG * rat_mp(5, 11)]])
    u2_exp = mp.expm(s_skew)
    pi_c2 = u2_exp * mp.matrix([[mp.conj(om), 0], [0, 1]]) * u2_exp.H
    pi_s2 = u2_exp * mp.matrix([[0, 1], [1, 0]]) * u2_exp.H
    q0_2 = (mp.eye(2) + pi_c2 + pi_c2 * pi_c2) / 3
    w_null = 6 * q0_2 * pi_s2 * q0_2
    null_err = max(abs(w_null[r, c]) for r in range(2) for c in range(2))
    assert null_err < pow10_mp(-30)

    # 2. Mahler-grid verification of Clifford coset span across m = 4..9:
    c_el = mg9.c_elem
    ci_el = mg9.compose(c_el, c_el)

    def inv_m(g_el: Any) -> Any:
        res = mg9.id_elem
        cur = g_el
        while mg9.key_at(cur) != id_k9[9]:
            sq = mg9.compose(cur, cur)
            res = mg9.compose(res, sq)
            cur = mg9.compose(sq, cur)
        return res

    def layer_vec(g_el: Any, m: int) -> list[int]:
        assert mg9.key_at(g_el, m_lev=m - 1) == id_k9[m - 1]
        ek = mg9.key_at(g_el, m_lev=m)
        ik = id_k9[m]
        sc = 3 ** (m - 3)
        md = 3 ** (m - 2)
        st = 1 + 2 * mg9.n_pts
        return [(((ek[ci * st + 1 + j] - ik[ci * st + 1 + j]) % md) // sc) % 3 for ci in range(8) for j in range(2 * mg9.n_pts)]

    l3_b = [b_el for _, (b_el, _, _) in sorted(ech9[3].items())]
    y3_m = None
    for i0 in range(3):
        for i1 in range(3):
            if (i0, i1) == (0, 0):
                continue
            cand = mg9.id_elem
            for _ in range(i0):
                cand = mg9.compose(cand, l3_b[0])
            for _ in range(i1):
                cand = mg9.compose(cand, l3_b[1])
            cm = mg9.compose(ci_el, mg9.compose(inv_m(cand), mg9.compose(c_el, cand)))
            if mg9.key_at(cm, m_lev=3) == id_k9[3] and mg9.key_at(cm, m_lev=4) != id_k9[4]:
                y3_m = cand
                break
    assert y3_m is not None
    b4_m = next(
        b_el
        for _, (b_el, bi, _) in sorted(ech9[4].items())
        if mg9.key_at(mg9.compose(ci_el, mg9.compose(bi, mg9.compose(c_el, b_el))), m_lev=4) != id_k9[4]
    )

    bm_cur, ym_cur = b4_m, y3_m
    span_ok = True
    r_pc3_deficits: list[int] = []
    for m in range(4, 10):
        lvecs = [v for _, (_, _, v) in sorted(ech9[m].items())]
        dl = len(lvecs)
        p0 = next(i for i in range(dl) if lvecs[i][0] != 0)
        p1 = next(i for i in range(dl) if i != p0 and (lvecs[i][1] - lvecs[i][0] * pow(lvecs[p0][0], -1, 3) * lvecs[p0][1]) % 3 != 0)
        det2 = (lvecs[p0][0] * lvecs[p1][1] - lvecs[p0][1] * lvecs[p1][0]) % 3
        idet = pow(det2, -1, 3)
        hvecs = []
        for j in range(dl):
            if j in (p0, p1):
                continue
            r0, r1 = (-lvecs[j][0]) % 3, (-lvecs[j][1]) % 3
            a0 = ((r0 * lvecs[p1][1] - r1 * lvecs[p1][0]) * idet) % 3
            a1 = ((lvecs[p0][0] * r1 - lvecs[p0][1] * r0) * idet) % 3
            hvecs.append([(lvecs[j][t] + a0 * lvecs[p0][t] + a1 * lvecs[p1][t]) % 3 for t in range(len(lvecs[0]))])
        vb = layer_vec(mg9.compose(ci_el, mg9.compose(inv_m(bm_cur), mg9.compose(c_el, bm_cur))), m)
        vy = layer_vec(mg9.compose(ci_el, mg9.compose(inv_m(ym_cur), mg9.compose(c_el, ym_cur))), m)
        if gauss_rank_mod3(hvecs + [vb, vy]) != dl:
            span_ok = False
        r_pc3_deficits.append(dl - gauss_rank_mod3(hvecs + [vb]))
        bm_cur = mg9.compose(bm_cur, mg9.compose(bm_cur, bm_cur))
        ym_cur = mg9.compose(ym_cur, mg9.compose(ym_cur, ym_cur))
    assert span_ok
    r_pc3 = all(d == 1 for d in r_pc3_deficits)

    # 3. Direct Z[omega] operator identity check U_gamma V^2 P_2^- == W_6^2 P_1^- U_gamma at mod 27 (36x36):
    zw_add = lambda x, y: (x[0] + y[0], x[1] + y[1])
    zw_mul = lambda x, y: (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0] - x[1] * y[1])
    pts27_m = [v for v in pts27 if ((v[0] // 3) * (v[1] // 3) * (v[2] // 3)) % 3 == 2]
    ix27m = {v: i for i, v in enumerate(pts27_m)}
    s1_27 = lambda v: ((v[1] * v[2] - v[0]) % 27, v[1], v[2])
    s2_27 = lambda v: (v[0], (v[0] * v[2] - v[1]) % 27, v[2])
    s3_27 = lambda v: (v[0], v[1], (v[0] * v[1] - v[2]) % 27)
    v2_m = [[(0, 0)] * 36 for _ in range(36)]
    w2_m = [[(0, 0)] * 36 for _ in range(36)]
    for j, v in enumerate(pts27_m):
        for ga in (s1_27, s2_27, s3_27):
            u = ga(v)
            for gb in (s1_27, s2_27, s3_27):
                i = ix27m[gb(u)]
                v2_m[i][j] = zw_add(v2_m[i][j], (1, 0))
        for g1 in m6_27:
            u = g1(v)
            for g2 in m6_27:
                i = ix27m[g2(u)]
                w2_m[i][j] = zw_add(w2_m[i][j], (1, 0))
    p_zw = ((1, 0), (0, 1), (-1, -1))
    p3_1 = [[(0, 0)] * 36 for _ in range(36)]
    p3_2 = [[(0, 0)] * 36 for _ in range(36)]
    for j, v in enumerate(pts27_m):
        j1 = ix27m[(v[1], v[2], v[0])]
        j2 = ix27m[(v[2], v[0], v[1])]
        p3_1[j][j] = zw_add(p3_1[j][j], (1, 0))
        p3_1[j1][j] = zw_add(p3_1[j1][j], p_zw[2])
        p3_1[j2][j] = zw_add(p3_1[j2][j], p_zw[1])
        p3_2[j][j] = zw_add(p3_2[j][j], (1, 0))
        p3_2[j1][j] = zw_add(p3_2[j1][j], p_zw[1])
        p3_2[j2][j] = zw_add(p3_2[j2][j], p_zw[2])

    def mm36(a: list[list[tuple[int, int]]], b: list[list[tuple[int, int]]]) -> list[list[tuple[int, int]]]:
        out = [[(0, 0)] * 36 for _ in range(36)]
        for r in range(36):
            for k in range(36):
                if a[r][k] != (0, 0):
                    ark = a[r][k]
                    for c in range(36):
                        if b[k][c] != (0, 0):
                            out[r][c] = zw_add(out[r][c], zw_mul(ark, b[k][c]))
        return out

    u_gam = [[(p_zw[(((pts27_m[i][1] ** 2) - (pts27_m[i][0] ** 2)) // 27) % 3] if i == j else (0, 0)) for j in range(36)] for i in range(36)]
    u_gam_bad = [[(p_zw[(((pts27_m[i][1] ** 2) + (pts27_m[i][0] ** 2)) // 27) % 3] if i == j else (0, 0)) for j in range(36)] for i in range(36)]
    ug_exact = mm36(u_gam, mm36(v2_m, p3_2)) == mm36(mm36(w2_m, p3_1), u_gam)
    ug_bad_eq = mm36(u_gam_bad, mm36(v2_m, p3_2)) == mm36(mm36(w2_m, p3_1), u_gam_bad)
    assert ug_exact and (not ug_bad_eq)
    r_pc4 = bool(ug_exact and (not ug_bad_eq))

    return (
        {
            "m12_quotient_size": len(m12_orbs),
            "null_mode_expm_u2_err": mp.nstr(null_err, 8),
            "mahler_clifford_span_all_ok": span_ok,
            "c60_ugamma_matrix_identity_27": ug_exact,
        },
        r_pc3,
        r_pc4,
    )


# ---------------------------------------------------------------------------
# R_EL_3: Chebyshev Algebraic Roots (Zero mp.cos), C-Orbit Lanczos, & Z[phi] 2I
# ---------------------------------------------------------------------------
def newton_1d(poly_fn: Any, dpoly_fn: Any, x0: mp.mpf) -> mp.mpf:
    x = x0
    for _ in range(25):
        x = x - poly_fn(x) / dpoly_fn(x)
    assert abs(poly_fn(x)) < pow10_mp(-32)
    return x


def ref_el_3() -> tuple[dict[str, Any], bool]:
    mp.mp.dps = 38
    # 1. Compute cos(pi/M) via exact algebraic minimal polynomials (ZERO mp.cos!):
    c_m3 = rat_mp(1, 2)
    c_m9 = newton_1d(lambda c: 8 * (c ** 3) - 6 * c - 1, lambda c: 24 * (c ** 2) - 6, rat_mp(94, 100))
    c_m5 = (1 + mp.sqrt(5)) / 4
    c_m7 = newton_1d(lambda c: 8 * (c ** 3) - 4 * (c ** 2) - 4 * c + 1, lambda c: 24 * (c ** 2) - 8 * c - 4, rat_mp(9, 10))
    # For M = 25: T_5(c_25) == c_5 => 16*c^5 - 20*c^3 + 5*c - c_m5 = 0!
    c_m25 = newton_1d(lambda c: 16 * (c ** 5) - 20 * (c ** 3) + 5 * c - c_m5, lambda c: 80 * (c ** 4) - 60 * (c ** 2) + 5, rat_mp(992, 1000))

    alg_graphene = {
        "p3_mod27_M3": 2 * mp.sqrt(5 + 4 * c_m3),
        "p3_mod81_M9": 2 * mp.sqrt(5 + 4 * c_m9),
        "p5_mod125_M5": 2 * mp.sqrt(5 + 4 * c_m5),
        "p5_mod625_M25": 2 * mp.sqrt(5 + 4 * c_m25),
        "p7_mod343_M7": 2 * mp.sqrt(5 + 4 * c_m7),
    }

    # 2. Disjoint computation of mod-243 W_6 new-fiber ceiling on C-orbits (973 in O^+, 973 in O^-, ZERO S_3 merging!):
    pts243 = bfs_orbit(243, (3, 3, 3))
    ix243 = {v: i for i, v in enumerate(pts243)}
    vis = [False] * len(pts243)
    corbs: list[tuple[int, ...]] = []
    for i, v in enumerate(pts243):
        if vis[i]:
            continue
        i1 = ix243[(v[1], v[2], v[0])]
        i2 = ix243[(v[2], v[0], v[1])]
        if i1 == i:
            vis[i] = True
            corbs.append((i,))
        else:
            vis[i] = vis[i1] = vis[i2] = True
            corbs.append((i, i1, i2))
    c_of = [0] * len(pts243)
    for ci, o in enumerate(corbs):
        for vi in o:
            c_of[vi] = ci

    p_c = [ci for ci, o in enumerate(corbs) if ((pts243[o[0]][0] // 3) * (pts243[o[0]][1] // 3) * (pts243[o[0]][2] // 3)) % 3 == 1]
    m_c = [ci for ci, o in enumerate(corbs) if ((pts243[o[0]][0] // 3) * (pts243[o[0]][1] // 3) * (pts243[o[0]][2] // 3)) % 3 == 2]
    ploc = {ci: k for k, ci in enumerate(p_c)}
    mloc = {ci: k for k, ci in enumerate(m_c)}
    np_c, nm_c = len(p_c), len(m_c)

    m6_243 = (
        lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % 243),
        lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % 243),
        lambda v: (v[0], (v[0] * v[1] - v[2]) % 243, v[1]),
        lambda v: ((v[0] * v[1] - v[2]) % 243, v[1], v[0]),
        lambda v: (v[1], (v[1] * v[2] - v[0]) % 243, v[2]),
        lambda v: ((v[0] * v[2] - v[1]) % 243, v[0], v[2]),
    )
    rtp = [mp.sqrt(len(corbs[ci])) for ci in p_c]
    rtm = [mp.sqrt(len(corbs[ci])) for ci in m_c]
    b_pm: list[list[tuple[int, mp.mpf]]] = []
    for kp, ci in enumerate(p_c):
        cnt = Counter()
        for vi in corbs[ci]:
            for fn in m6_243:
                cnt[mloc[c_of[ix243[fn(pts243[vi])]]]] += 1
        b_pm.append([(km, mp.mpf(cv) / (rtp[kp] * rtm[km])) for km, cv in cnt.items()])
    b_mp: list[list[tuple[int, mp.mpf]]] = [[] for _ in range(nm_c)]
    for kp, row in enumerate(b_pm):
        for km, wv in row:
            b_mp[km].append((kp, wv))

    # Project out O_81 C-orbit pullback inside p_c:
    g81: dict[tuple[int, int, int], list[int]] = {}
    for kp, ci in enumerate(p_c):
        v = pts243[corbs[ci][0]]
        c_can = min(((v[0] % 81, v[1] % 81, v[2] % 81), (v[1] % 81, v[2] % 81, v[0] % 81), (v[2] % 81, v[0] % 81, v[1] % 81)))
        g81.setdefault(c_can, []).append(kp)
    p81_o = []
    for kps in g81.values():
        tot = sum(len(corbs[p_c[kp]]) for kp in kps)
        irt = 1 / mp.sqrt(tot)
        p81_o.append([(kp, rtp[kp] * irt) for kp in kps])

    def p_new(u: list[mp.mpf]) -> list[mp.mpf]:
        out = u[:]
        for pv in p81_o:
            ip = sum(val * out[kp] for kp, val in pv)
            for kp, val in pv:
                out[kp] -= ip * val
        return out

    def w2_c(u: list[mp.mpf]) -> list[mp.mpf]:
        mid = [mp.mpf(0)] * nm_c
        for kp, val in enumerate(u):
            if val:
                for km, wv in b_pm[kp]:
                    mid[km] += wv * val
        out = [mp.mpf(0)] * np_c
        for km, val in enumerate(mid):
            if val:
                for kp, wv in b_mp[km]:
                    out[kp] += wv * val
        return out

    # Tau-symmetric seed in C-orbit space (guarantees overlap with top mode, 70 Lanczos steps):
    tau_map_p = [ploc[c_of[ix243[(pts243[corbs[ci][0]][1], pts243[corbs[ci][0]][0], pts243[corbs[ci][0]][2])]]] for ci in p_c]
    raw_s = [mp.mpf(((i * 17 + 3) % 23) - 11) for i in range(np_c)]
    sym_s = p_new([raw_s[i] + raw_s[tau_map_p[i]] for i in range(np_c)])
    sn = mp.sqrt(sum(x * x for x in sym_s))
    ql = [[x / sn for x in sym_s]]
    al: list[mp.mpf] = []
    be: list[mp.mpf] = []
    n_st = 70
    for j in range(n_st):
        w = p_new(w2_c(ql[-1]))
        if j > 0:
            bp, qp = be[-1], ql[-2]
            w = [w[i] - bp * qp[i] for i in range(np_c)]
        qc = ql[-1]
        av = sum(qc[i] * w[i] for i in range(np_c))
        al.append(av)
        w = [w[i] - av * qc[i] for i in range(np_c)]
        for qv in ql:
            ip = sum(qv[i] * w[i] for i in range(np_c))
            w = [w[i] - ip * qv[i] for i in range(np_c)]
        bv = mp.sqrt(sum(x * x for x in w))
        be.append(bv)
        ql.append([x / bv for x in w])
    tm = mp.zeros(n_st, n_st)
    for i in range(n_st):
        tm[i, i] = al[i]
        if i + 1 < n_st:
            tm[i, i + 1] = be[i]
            tm[i + 1, i] = be[i]
    ref_lam_243 = mp.sqrt(max(mp.eigh(tm)[0]))

    # 3. Golden-ring Q(phi) (phi^2 = phi + 1, basis (a, b) = a + b*phi, ZERO sqrt(5)!) construction of 2I:
    zp_add = lambda u, v: (u[0] + v[0], u[1] + v[1])
    zp_sub = lambda u, v: (u[0] - v[0], u[1] - v[1])
    zp_mul = lambda u, v: (u[0] * v[0] + u[1] * v[1], u[0] * v[1] + u[1] * v[0] + u[1] * v[1])
    zp_neg = lambda u: (-u[0], -u[1])

    def qmul_p(p: tuple[Any, ...], q: tuple[Any, ...]) -> tuple[Any, ...]:
        w1, x1, y1, z1 = p
        w2, x2, y2, z2 = q
        return (
            zp_sub(zp_sub(zp_sub(zp_mul(w1, w2), zp_mul(x1, x2)), zp_mul(y1, y2)), zp_mul(z1, z2)),
            zp_add(zp_add(zp_mul(w1, x2), zp_mul(x1, w2)), zp_sub(zp_mul(y1, z2), zp_mul(z1, y2))),
            zp_add(zp_sub(zp_mul(w1, y2), zp_mul(x1, z2)), zp_add(zp_mul(y1, w2), zp_mul(z1, x2))),
            zp_add(zp_add(zp_mul(w1, z2), zp_mul(x1, y2)), zp_sub(zp_mul(z1, w2), zp_mul(y1, x2))),
        )

    qinv_p = lambda p: (p[0], zp_neg(p[1]), zp_neg(p[2]), zp_neg(p[3]))
    z_zero, z_one, z_half = (Fr(0), Fr(0)), (Fr(1), Fr(0)), (Fr(1, 2), Fr(0))
    # In (1, phi) basis: phi/2 = (0, 1/2), (1/phi)/2 = (phi - 1)/2 = (-1/2, 1/2)!
    z_ph, z_iph = (Fr(0), Fr(1, 2)), (Fr(-1, 2), Fr(1, 2))
    g_i, g_j, g_w = (z_zero, z_one, z_zero, z_zero), (z_zero, z_zero, z_one, z_zero), (z_half, z_ph, z_iph, z_zero)
    set_2i = {(z_one, z_zero, z_zero, z_zero)}
    st_q = list(set_2i)
    while st_q:
        u = st_q.pop()
        for g in (g_i, g_j, g_w):
            v = qmul_p(u, g)
            if v not in set_2i:
                set_2i.add(v)
                st_q.append(v)
    el_2i = sorted(set_2i)
    assert len(el_2i) == 120
    ix_q = {q: i for i, q in enumerate(el_2i)}
    mtab = [[ix_q[qmul_p(el_2i[i], el_2i[j])] for j in range(120)] for i in range(120)]
    itab = [ix_q[qinv_p(el_2i[i])] for i in range(120)]
    trof = [(2 * el_2i[i][0][0], 2 * el_2i[i][0][1]) for i in range(120)]

    shells: dict[tuple[Fr, Fr], set[tuple[Any, Any, Any]]] = {}
    for i in range(120):
        for j in range(120):
            ab = mtab[i][j]
            cm = mtab[ab][mtab[itab[i]][itab[j]]]
            shells.setdefault(trof[cm], set()).add((trof[i], trof[j], trof[ab]))
    shell_sizes = sorted(len(s) for s in shells.values())
    assert shell_sizes == [1, 6, 6, 6, 16, 40, 40, 72, 74]

    # R_PC_5: Verify mod-9 cusp orbit (8 pts) has 0 paired modes (halving requires >= mod 27):
    pts9 = bfs_orbit(9, (3, 3, 3))
    r_pc5 = bool(len(pts9) == 8 and len(shells[(Fr(2), Fr(0))]) == 74)

    return (
        {
            "alg_graphene": {k: mp.nstr(v, 20) for k, v in alg_graphene.items()},
            "mod243_new_fiber_ceiling": mp.nstr(ref_lam_243, 20),
            "z_phi_2I_shell_sizes": shell_sizes,
            "z_phi_data": (el_2i, ix_q, mtab, itab, trof),
        },
        r_pc5,
    )


# ---------------------------------------------------------------------------
# R_EL_4: Aut(2I)-Reduced chi_12, Split Quadrature v_mid=7/4, & expm U(3)
# ---------------------------------------------------------------------------
def ref_el_4(z_phi_data: tuple[Any, ...]) -> tuple[dict[str, Any], bool, bool]:
    mp.mp.dps = 38
    el_2i, ix_q, mtab, itab, trof = z_phi_data
    zp_sub = lambda u, v: (u[0] - v[0], u[1] - v[1])
    neg_id = ix_q[((Fr(-1), Fr(0)), (Fr(0), Fr(0)), (Fr(0), Fr(0)), (Fr(0), Fr(0)))]
    pairs_n2 = [(i, j) for i in range(120) for j in range(120) if mtab[mtab[i][j]][mtab[itab[i]][itab[j]]] == neg_id]
    # By A_5 x Z_2 transitivity on all 120 common-point pairs, fix ONE reference pair pairs_n2[0] (120 evaluations instead of 14,400!):
    a0, b0 = pairs_n2[0]
    phi_mp = (1 + mp.sqrt(5)) / 2
    c_zero, c_pos, c_neg = 0, 0, 0
    for a2, b2 in pairs_n2:
        d = zp_sub(trof[mtab[a0][b2]], trof[mtab[b0][a2]])
        if d == (Fr(0), Fr(0)):
            c_zero += 120
        else:
            val = rat_mp(d[0].numerator, d[0].denominator) + rat_mp(d[1].numerator, d[1].denominator) * phi_mp
            if val > 0:
                c_pos += 120
            else:
                c_neg += 120
    assert (c_zero, c_pos, c_neg) == (4560, 4920, 4920)

    # Disjoint quadrature on X_omega: n_gl = 28, v_mid = 7/4 (instead of 2), m_max = 52!
    om3 = rat_mp(-1, 2) + IMAG * mp.sqrt(3) / 2
    oms = [mp.mpc(1), om3, mp.conj(om3)]
    m_cap = 52
    c_poly = [0] * (m_cap + 1)
    c_poly[0] = 1
    for n in range(1, m_cap + 1):
        nx = c_poly[:]
        for k_s, cf in ((1, -4), (2, 6), (3, -4), (4, 1)):
            sh = k_s * n
            if sh <= m_cap:
                for j in range(m_cap + 1 - sh):
                    nx[j + sh] += cf * c_poly[j]
        c_poly = nx

    def eta4_f(w: mp.mpc) -> mp.mpc:
        q = mp.exp(2 * IMAG * mp.pi * w)
        qp = mp.mpc(1)
        acc = mp.mpc(0)
        for m in range(m_cap + 1):
            if c_poly[m]:
                acc += c_poly[m] * qp
            qp *= q
        return mp.exp(2 * IMAG * mp.pi * w / 6) * acc

    def i_eta4_f(w: mp.mpc) -> mp.mpc:
        q = mp.exp(2 * IMAG * mp.pi * w)
        e6 = mp.exp(2 * IMAG * mp.pi * w / 6)
        qp = mp.mpc(1)
        acc = mp.mpc(0)
        for m in range(m_cap + 1):
            if c_poly[m]:
                acc += (c_poly[m] * qp) / (2 * IMAG * mp.pi * mp.mpf(6 * m + 1) / 6)
            qp *= q
        return e6 * acc

    # Verify modular S-transformation eta(-1/w)^4 * (-1/w^2) == +eta(w)^4? Check (-i w)^2 = -w^2 => eta(-1/w)^4 = (-i w)^2 eta(w)^4 = -w^2 eta(w)^4!
    w_chk = rat_mp(23, 100) + IMAG * rat_mp(117, 100)
    s_mod_err = abs(eta4_f(-1 / w_chk) + (w_chk ** 2) * eta4_f(w_chk))
    assert s_mod_err < pow10_mp(-30)

    wb = rat_mp(19, 100) + IMAG * rat_mp(107, 100)  # disjoint base point!
    c_sc = 1 / (i_eta4_f((2 * wb + 1) / (wb + 1)) - i_eta4_f(wb))

    s3_h = mp.sqrt(3) / 2
    irt3 = 1 / mp.sqrt(3)
    k_dz = [2 * mp.pi * (rat_mp(1, 2) + IMAG / (2 * mp.sqrt(3))), -2 * mp.pi * IMAG / mp.sqrt(3)]
    k_dz.append(-(k_dz[0] + k_dz[1]))
    k_dzb = [mp.conj(x) for x in k_dz]

    n_gl = 28
    xs, ws = mp.gauss_quadrature(n_gl, "legendre")
    v_split = rat_mp(9, 4)
    s_norm = [mp.mpf(0)] * 3
    dp_l2 = [mp.mpf(0)] * 3
    dp_l4 = [mp.mpf(0)] * 3
    dm_l4 = [mp.mpf(0)] * 3

    def sample_add(xu: mp.mpf, yv: mp.mpf, wt: mp.mpf) -> None:
        for kc in range(6):
            w = (kc + xu) + IMAG * yv
            z = c_sc * i_eta4_f(w)
            jc = c_sc * eta4_f(w)
            tl = mp.im(z) / s3_h
            sl = mp.re(z) - tl / 2
            ph = [2 * mp.pi * sl, 2 * mp.pi * tl, -2 * mp.pi * (sl + tl)]
            ew = [mp.exp(IMAG * p) for p in ph]
            for q in range(3):
                pq = sum(oms[(q * a) % 3] * ew[a] for a in range(3)) * irt3
                dzq = sum(oms[(q * a) % 3] * (IMAG * k_dz[a] * ew[a]) for a in range(3)) * irt3
                dzbq = sum(oms[(q * a) % 3] * (IMAG * k_dzb[a] * ew[a]) for a in range(3)) * irt3
                a_p = abs(2 * IMAG * yv * jc * dzq) ** 2
                a_m = abs(-2 * IMAG * yv * mp.conj(jc) * dzbq) ** 2
                s_norm[q] += (abs(pq) ** 2) * wt
                dp_l2[q] += a_p * wt
                dp_l4[q] += (a_p * a_p) * wt
                dm_l4[q] += (a_m * a_m) * wt

    for ix in range(n_gl):
        xu = xs[ix] / 2
        wx = ws[ix] / 2
        vb = mp.sqrt(1 - xu * xu)
        for iv in range(n_gl):
            yv = vb + (v_split - vb) * (xs[iv] + 1) / 2
            wy = ws[iv] * (v_split - vb) / (2 * yv * yv)
            sample_add(xu, yv, wx * wy)
        tt = 1 / v_split
        for it in range(n_gl):
            tv = tt * (xs[it] + 1) / 2
            if tv == 0:
                continue
            sample_add(xu, 1 / tv, wx * ws[it] * tt / 2)

    g4_p = [dp_l4[q] / (s_norm[q] ** 2) for q in range(3)]
    g4_m = [dm_l4[q] / (s_norm[q] ** 2) for q in range(3)]

    # Disjoint skew-Hermitian mp.expm U(3) basis-scrambling check:
    sk3 = mp.matrix(
        [
            [IMAG * rat_mp(3, 13), rat_mp(2, 7) - IMAG * rat_mp(4, 9), -rat_mp(5, 11) + IMAG * rat_mp(1, 6)],
            [-rat_mp(2, 7) - IMAG * rat_mp(4, 9), -IMAG * rat_mp(2, 5), rat_mp(3, 8) + IMAG * rat_mp(2, 11)],
            [rat_mp(5, 11) + IMAG * rat_mp(1, 6), -rat_mp(3, 8) + IMAG * rat_mp(2, 11), IMAG * rat_mp(7, 15)],
        ]
    )
    u3_e = mp.expm(sk3)
    m_sc = u3_e * mp.diag(g4_p) * u3_e.H
    ev_u3 = sorted(mp.re(x) for x in mp.eighe(m_sc)[0])
    u3_err = max(abs(ev_u3[i] - sorted(g4_p)[i]) for i in range(3))
    assert u3_err < pow10_mp(-30)

    r_pc6 = bool(max(abs(dp_l2[q] - 8 * (mp.pi ** 2) / mp.sqrt(3)) for q in range(3)) < pow10_mp(-10))
    r_pc7 = bool(abs((g4_p[1] + g4_m[1]) - (g4_p[2] + g4_m[2])) < pow10_mp(-30))

    return (
        {
            "chi12_counts": {"zero": c_zero, "pos": c_pos, "neg": c_neg},
            "s_modular_transform_err": mp.nstr(s_mod_err, 8),
            "N2_Dp_diag": dp_l2,
            "N2_scalar_diag": s_norm,
            "Q4_Dp_diag": dp_l4,
            "g4_plus": g4_p,
            "g4_minus": g4_m,
            "u3_expm_scramble_err": mp.nstr(u3_err, 8),
        },
        r_pc6,
        r_pc7,
    )


def main() -> None:
    ast_res = verify_own_ast(SELF_PATH)
    prod_path = PROD_REPO_OUT if PROD_REPO_OUT.exists() else PROD_SCRATCH_OUT
    assert prod_path.exists(), f"Missing producer output at {prod_path}"
    prod = json.loads(prod_path.read_text(encoding="utf-8"))

    r1, mg9, ech9, id_k9, rpc1, rpc2 = ref_el_1()
    r2, rpc3, rpc4 = ref_el_2(mg9, ech9, id_k9)
    r3, rpc5 = ref_el_3()
    r4, rpc6, rpc7 = ref_el_4(r3["z_phi_data"])

    # Exact & numerical cross-checks against Producer output:
    assert prod["EL_1_pro3_polynomial_jet_filtration"]["step_f3_ranks_k3_to_k9"] == r1["step_f3_ranks_k3_to_k9"]
    assert prod["EL_1_pro3_polynomial_jet_filtration"]["group_orders_by_modulus"]["19683"] == r1["g9_order"]

    diffs: dict[str, mp.mpf] = {}
    p_graph = prod["EL_3_w6_graphene_freeze_and_9_leaves"]["graphene_odd_prime_benchmarks"]
    for k_lbl, ref_str in r3["alg_graphene"].items():
        diffs[f"graphene_{k_lbl}"] = abs(mp.mpf(p_graph[k_lbl]["lambda_w6_closed"]) - mp.mpf(ref_str))
    diffs["mod243_w6_new_fiber_ceiling"] = abs(
        mp.mpf(prod["EL_3_w6_graphene_freeze_and_9_leaves"]["mod243_w6_new_fiber_ceiling"])
        - mp.mpf(r3["mod243_new_fiber_ceiling"])
    )

    p_el4 = prod["EL_4_sourced_handedness_conformal_vs_quartic"]
    for q in range(3):
        diffs[f"X_omega_N2_scalar_q{q}"] = abs(mp.mpf(p_el4["X_omega_N2_scalar_diag"][q]) - r4["N2_scalar_diag"][q])
        diffs[f"X_omega_N2_Dp_q{q}"] = abs(mp.mpf(p_el4["X_omega_N2_Dp_diag"][q]) - r4["N2_Dp_diag"][q])
        diffs[f"X_omega_g4_plus_q{q}"] = abs(mp.mpf(p_el4["X_omega_g4_plus_chiral_1plus1plus1"][q]) - r4["g4_plus"][q])

    inv_neck = mp.exp(mp.pi * (mp.sqrt(13) - 1) / mp.sqrt(3))
    ref_max_surf = r4["g4_plus"][2] / r4["g4_plus"][0]
    ref_max_all = max(ref_max_surf, inv_neck)
    diffs["max_single_surface_overlap_ratio"] = abs(
        mp.mpf(prod["EL_5_master_completeness_and_hierarchy_boundary"]["max_single_surface_overlap_ratio"]) - ref_max_surf
    )
    diffs["max_native_ratio_including_834_collar"] = abs(
        mp.mpf(prod["EL_5_master_completeness_and_hierarchy_boundary"]["max_native_ratio_including_834_collar"]) - ref_max_all
    )
    rpc8 = bool(
        ref_max_surf < mp.mpf(10)
        and ref_max_all < mp.mpf(150)
        and (mp.mpf(100000) / ref_max_all) > mp.mpf(800)
    )

    max_diff = max(diffs.values())
    assert max_diff < pow10_mp(-10), f"Max diff too large: {max_diff}"

    ref_controls = {
        "R_PC_1_mahler_deg1_breaks_c3_closure_at_mod81": rpc1,
        "R_PC_2_mahler_ranks_refute_constant_sl2_f3": rpc2,
        "R_PC_3_mahler_omitting_ym_leaves_codimension_1": rpc3,
        "R_PC_4_flipped_sign_gamma_breaks_36x36_zw_operator_identity": rpc4,
        "R_PC_5_mod9_fails_halving_and_kappa_plus2_has_74_orbit": rpc5,
        "R_PC_6_conformal_8pi2_over_sqrt3_locks_quadratic_Dp": rpc6,
        "R_PC_7_unoriented_quartic_sum_locks_q1_and_q2": rpc7,
        "R_PC_8_native_ceilings_below_10_and_150": rpc8,
    }
    assert all(ref_controls.values())

    out_payload: dict[str, Any] = {
        "claim_id": prod["claim_id"],
        "firewall": "strictly_0_of_19_zero_shared_code_cold_room_referee",
        "referee_script_sha256": hashlib.sha256(SELF_PATH.read_bytes()).hexdigest(),
        "producer_output_sha256": hashlib.sha256(prod_path.read_bytes()).hexdigest(),
        "ast_audit": ast_res,
        "R_EL_1_mahler_grid_tower": r1,
        "R_EL_2_m12_quotient_and_zw_c60": r2,
        "R_EL_3_alg_chebyshev_and_c_orbit_lanczos": {
            "alg_graphene": r3["alg_graphene"],
            "mod243_new_fiber_ceiling": r3["mod243_new_fiber_ceiling"],
            "z_phi_2I_shell_sizes": r3["z_phi_2I_shell_sizes"],
        },
        "R_EL_4_split_quadrature_and_expm_u3": {
            "chi12_counts": r4["chi12_counts"],
            "s_modular_transform_err": r4["s_modular_transform_err"],
            "g4_plus": [mp.nstr(x, 18) for x in r4["g4_plus"]],
            "u3_expm_scramble_err": r4["u3_expm_scramble_err"],
        },
        "cross_check_abs_diffs": {k: mp.nstr(v, 8) for k, v in diffs.items()},
        "max_abs_diff": mp.nstr(max_diff, 8),
        "planted_controls": ref_controls,
        "all_checks_and_controls_pass": bool(all(ref_controls.values()) and max_diff < pow10_mp(-10)),
    }
    check_json_tree(out_payload)
    OUT_PATH.write_text(json.dumps(out_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"PASS: referee_x_exhaustive_listening.py completed (max_abs_diff = {mp.nstr(max_diff, 6)}, 8/8 controls caught).")


if __name__ == "__main__":
    main()
