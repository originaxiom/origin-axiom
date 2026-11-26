#!/usr/bin/env python3
"""
Disjoint Cold-Room Zero-Trust Referee for Card AGY-002_A2-LISTENING-TOWER.

Strictly blind (0 of 19 empirical/PDG/NuFIT/Planck/CODATA values anywhere).
Uses stdlib + mpmath + sympy ONLY, zero AST float/complex literals or casts,
zero JSON floats, and completely disjoint algorithms from the producer:
  - Opposite Markoff tree generator basis <L, R> with L(x,y,z)=(z,y,yz-x),
    R(x,y,z)=(x,z,xz-y), recovering C = R^{-1} o L and sigma = R o C^{-1}.
  - Disjoint Krylov-Frobenius cyclic companion decomposition over GF(p) at
    verified primes p > 2*10^9 (p == 1 mod 3) + CRT for exact Z[x] charpolys
    (mod 27, mod 81, and mod 135).
  - Disjoint 2-half ((+1,+1,+1) and (-1,-1,-1)) exact falling-factorial /
    binomial-difference polynomial engine (zero raw grid) through mod 19,683.
  - Real-split 2d x 2d mp.eigsy at dps=55 (disjoint from mp.eighe) for
    Hermitian chiral-flux spectra, plus Guardrail 3 Haar-unitary basis scrambling.
"""

import ast
from collections import Counter, deque
import hashlib
import json
from math import gcd
import os
import random
import sys
import time

import mpmath as mp
import sympy as sp

# Configure arbitrary-precision arithmetic (zero Python floats)
DPS = 55
mp.mp.dps = DPS

FORBIDDEN_IMPORTS = {"numpy", "scipy", "frontier", "sage", "gap"}


# ---------------------------------------------------------------------------
# Basic Audit Helpers (Zero Floats / Zero Forbidden Imports)
# ---------------------------------------------------------------------------

def audit_source_ast(script_path):
    with open(script_path, "r", encoding="utf-8") as fh:
        src = fh.read()
    tree = ast.parse(src, filename=script_path)
    float_literals = 0
    complex_literals = 0
    float_complex_calls = 0
    forbidden_found = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_literals += 1
            elif isinstance(node.value, complex):
                complex_literals += 1
        elif isinstance(node, ast.Call):
            fn = node.func
            if isinstance(fn, ast.Name) and fn.id in ("float", "complex"):
                float_complex_calls += 1
            elif isinstance(fn, ast.Attribute) and fn.attr in ("float", "complex"):
                float_complex_calls += 1
        elif isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".")[0]
                if root in FORBIDDEN_IMPORTS:
                    forbidden_found.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                root = node.module.split(".")[0]
                if root in FORBIDDEN_IMPORTS:
                    forbidden_found.append(node.module)
    return {
        "ast_float_literal_count": float_literals,
        "ast_complex_literal_count": complex_literals,
        "ast_float_complex_call_count": float_complex_calls,
        "forbidden_imports": sorted(set(forbidden_found)),
        "forbidden_imports_count": len(forbidden_found),
    }


def count_json_floats(obj):
    if isinstance(obj, float):
        return 1
    if isinstance(obj, dict):
        return sum(count_json_floats(v) for v in obj.values())
    if isinstance(obj, (list, tuple)):
        return sum(count_json_floats(v) for v in obj)
    return 0


def mp_str(val, digits=30):
    if isinstance(val, mp.mpc):
        re_s = mp.nstr(val.real, digits)
        im_s = mp.nstr(val.imag, digits)
        return f"({re_s})+({im_s})i"
    return mp.nstr(val, digits)


# ---------------------------------------------------------------------------
# Markoff <L, R> Generator Basis & Derived <C, sigma>, tau, Vieta Moves
# ---------------------------------------------------------------------------

def apply_L(v, m):
    x, y, z = v
    return (z % m, y % m, (y * z - x) % m)


def apply_R(v, m):
    x, y, z = v
    return (x % m, z % m, (x * z - y) % m)


def apply_Li(v, m):
    x, y, z = v
    return ((x * y - z) % m, y % m, x % m)


def apply_Ri(v, m):
    x, y, z = v
    return (x % m, (x * y - z) % m, y % m)


def apply_C(v, m):
    # Recovered strictly from <L, R>: C = R^{-1} o L = (z, x, y)
    return apply_Ri(apply_L(v, m), m)


def apply_Cinv(v, m):
    # C^{-1} = L^{-1} o R = (y, z, x)
    return apply_Li(apply_R(v, m), m)


def apply_S(v, m):
    # Recovered strictly from <L, R>: sigma = R o C^{-1} = (y, x, xy - z)
    return apply_R(apply_Cinv(v, m), m)


def apply_tau(v, m):
    x, y, z = v
    return (y % m, x % m, z % m)


def apply_V1(v, m):
    x, y, z = v
    return ((y * z - x) % m, y % m, z % m)


def apply_V2(v, m):
    x, y, z = v
    return (x % m, (x * z - y) % m, z % m)


def apply_V3(v, m):
    x, y, z = v
    return (x % m, y % m, (x * y - z) % m)


def eps3(v):
    # Product (x/3)*(y/3)*(z/3) mod 3 for points with 3 | x,y,z
    return (((v[0] % 27) // 3) * ((v[1] % 27) // 3) * ((v[2] % 27) // 3)) % 3


def sgn9(a):
    r = a % 9
    if r == 3:
        return 1
    if r == 6:
        return -1
    raise ValueError(f"Coordinate {a} not +-3 mod 9")


def markoff_orbit_LR(m):
    start = (3 % m, 3 % m, 3 % m)
    seen = {start}
    q = deque([start])
    while q:
        u = q.popleft()
        for fn in (apply_L, apply_R):
            w = fn(u, m)
            if w not in seen:
                seen.add(w)
                q.append(w)
    return sorted(seen)


def comp_perm(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def inv_perm(a):
    out = [0] * len(a)
    for i, val in enumerate(a):
        out[val] = i
    return tuple(out)


def perm_order(p):
    seen = [False] * len(p)
    ans = 1
    for i in range(len(p)):
        if not seen[i]:
            cnt = 0
            cur = i
            while not seen[cur]:
                seen[cur] = True
                cur = p[cur]
                cnt += 1
            ans = ans * cnt // gcd(ans, cnt)
    return ans


def apply_word_LR(word, v, m):
    fns = {"L": apply_L, "R": apply_R, "l": apply_Li, "r": apply_Ri}
    for ch in reversed(word):
        v = fns[ch](v, m)
    return v


def cs_to_lr(word):
    # C = r L, S = R l R
    inv = {"L": "l", "l": "L", "R": "r", "r": "R"}
    raw = []
    for ch in word:
        if ch == "C":
            raw.extend(["r", "L"])
        elif ch == "S":
            raw.extend(["R", "l", "R"])
        else:
            raise ValueError(f"Bad CS symbol {ch}")
    st = []
    for c in raw:
        if st and st[-1] == inv[c]:
            st.pop()
        else:
            st.append(c)
    return tuple(st)


# ---------------------------------------------------------------------------
# Disjoint Charpoly Engine: Krylov-Frobenius Companion Decomposition mod p
# ---------------------------------------------------------------------------

def get_primes_1mod3(start_val, count):
    primes = []
    cur = start_val
    while len(primes) < count:
        cur = int(sp.nextprime(cur))
        if cur % 3 == 1:
            assert sp.isprime(cur)
            primes.append(cur)
    return primes


def primitive_cube_root_mod_p(p):
    assert p % 3 == 1
    exp = (p - 1) // 3
    for g in range(2, 1000):
        w = pow(g, exp, p)
        if w != 1:
            assert pow(w, 3, p) == 1
            assert (1 + w + w * w) % p == 0
            return w
    raise RuntimeError(f"Failed to find cube root mod {p}")


def poly_mul_mod_p(a, b, p):
    res = [0] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        if ca:
            for j, cb in enumerate(b):
                if cb:
                    res[i + j] = (res[i + j] + ca * cb) % p
    return res


def poly_divmod_mod_p(a, b, p):
    a = list(a)
    while len(a) > 1 and a[0] == 0:
        a.pop(0)
    while len(b) > 1 and b[0] == 0:
        b.pop(0)
    if len(a) < len(b):
        return [0], a
    db = len(b) - 1
    inv_lb = pow(b[0], -1, p)
    q = [0] * (len(a) - db)
    for i in range(len(q)):
        c = (a[i] * inv_lb) % p
        q[i] = c
        if c:
            for j, bj in enumerate(b):
                a[i + j] = (a[i + j] - c * bj) % p
    while len(a) > 1 and a[0] == 0:
        a.pop(0)
    return q, a


def poly_gcd_mod_p(a, b, p):
    while len(b) > 1 or b[0] != 0:
        _, r = poly_divmod_mod_p(a, b, p)
        a, b = b, r
    inv_la = pow(a[0], -1, p)
    return [(c * inv_la) % p for c in a]


def charpoly_krylov_mod_p(mat, p):
    """Exact characteristic polynomial over GF(p) via Krylov-Frobenius cyclic subspaces."""
    n = len(mat)
    rows_sp = [[(j, val % p) for j, val in enumerate(row) if val % p] for row in mat]

    def matvec(vec):
        return [sum(val * vec[j] for j, val in rsp) % p for rsp in rows_sp]

    basis_cnt = 0
    pivots = {}     # col -> (sparse_elim_row, lin_comb_dict)
    piv_order = []
    poly = [1]

    def reduce_vec(vec):
        rem = list(vec)
        comb = {}
        for col in piv_order:
            val = rem[col]
            if val:
                ev, lc = pivots[col]
                for j, evj in ev:
                    rem[j] = (rem[j] - val * evj) % p
                for k, ck in lc.items():
                    comb[k] = (comb.get(k, 0) + val * ck) % p
        piv = -1
        for j in range(n):
            if rem[j]:
                piv = j
                break
        return piv, rem, comb

    start_idx = 0
    while basis_cnt < n:
        e = None
        while start_idx < n:
            cand = [0] * n
            cand[start_idx] = 1
            piv, rem, comb = reduce_vec(cand)
            start_idx += 1
            if piv != -1:
                e = cand
                break
        assert e is not None
        k0 = basis_cnt
        v = e
        while True:
            piv, rem, comb = reduce_vec(v)
            if piv == -1:
                m_deg = basis_cnt - k0
                cpoly = [1] + [(-comb.get(k0 + (m_deg - 1 - t), 0)) % p for t in range(m_deg)]
                poly = poly_mul_mod_p(poly, cpoly, p)
                break
            b_idx = basis_cnt
            basis_cnt += 1
            inv = pow(rem[piv], -1, p)
            ev = [(j, (x * inv) % p) for j, x in enumerate(rem) if x]
            lc = {b_idx: inv}
            for k, ck in comb.items():
                val = (-ck * inv) % p
                if val:
                    lc[k] = val
            pivots[piv] = (ev, lc)
            piv_order.append(piv)
            v = matvec(v)
    assert len(poly) == n + 1
    return poly


def crt_reconstruct_poly(primes, polys):
    prod = 1
    for p in primes:
        prod *= p
    half = prod // 2
    deg = len(polys[0]) - 1
    out = []
    for k in range(deg + 1):
        val = 0
        for p, poly in zip(primes, polys):
            m_i = prod // p
            inv_i = pow(m_i % p, -1, p)
            val = (val + poly[k] * m_i * inv_i) % prod
        if val > half:
            val -= prod
        out.append(val)
    return out, prod


def get_c_orbits(pts, m):
    seen = set()
    fixed = []
    cycles = []
    for v in pts:
        if v in seen:
            continue
        c1 = apply_C(v, m)
        if c1 == v:
            seen.add(v)
            fixed.append(v)
        else:
            c2 = apply_C(c1, m)
            seen.add(v)
            seen.add(c1)
            seen.add(c2)
            cycles.append((v, c1, c2))
    return fixed, cycles


def build_bipartite_B_mod_p(fix_p, cyc_p, fix_m, cyc_m, q_val, move_fn, m_mod, p, w_p):
    """Build exact matrix of (3 Pi_q P_move Pi_q)^2 on O_m^+_q over GF(p)."""
    wq = 1 if q_val == 0 else w_p
    wq_inv = 1 if q_val == 0 else pow(w_p, 2, p)
    p_map = {}
    np_dim = 0
    if q_val == 0:
        for v in fix_p:
            p_map[v] = (np_dim, 0, True)
            np_dim += 1
    for cyc in cyc_p:
        for r, v in enumerate(cyc):
            p_map[v] = (np_dim, r, False)
        np_dim += 1

    m_map = {}
    nm_dim = 0
    if q_val == 0:
        for v in fix_m:
            m_map[v] = (nm_dim, 0, True)
            nm_dim += 1
    for cyc in cyc_m:
        for r, v in enumerate(cyc):
            m_map[v] = (nm_dim, r, False)
        nm_dim += 1

    T_pm = [{} for _ in range(np_dim)]
    for i in range(np_dim):
        if q_val == 0 and i < len(fix_p):
            y = move_fn(fix_p[i], m_mod)
            if y in m_map:
                j, pos, is_fix = m_map[y]
                T_pm[i][j] = (T_pm[i].get(j, 0) + (3 if is_fix else pow(wq, pos, p))) % p
        else:
            cyc = cyc_p[i - (len(fix_p) if q_val == 0 else 0)]
            for r, v in enumerate(cyc):
                y = move_fn(v, m_mod)
                if y in m_map:
                    j, pos, is_fix = m_map[y]
                    c_in = pow(wq_inv, r, p)
                    c_out = 3 if is_fix else pow(wq, pos, p)
                    T_pm[i][j] = (T_pm[i].get(j, 0) + c_in * c_out) % p

    T_mp = [{} for _ in range(nm_dim)]
    for i in range(nm_dim):
        if q_val == 0 and i < len(fix_m):
            y = move_fn(fix_m[i], m_mod)
            if y in p_map:
                j, pos, is_fix = p_map[y]
                T_mp[i][j] = (T_mp[i].get(j, 0) + (3 if is_fix else pow(wq, pos, p))) % p
        else:
            cyc = cyc_m[i - (len(fix_m) if q_val == 0 else 0)]
            for r, v in enumerate(cyc):
                y = move_fn(v, m_mod)
                if y in p_map:
                    j, pos, is_fix = p_map[y]
                    c_in = pow(wq_inv, r, p)
                    c_out = 3 if is_fix else pow(wq, pos, p)
                    T_mp[i][j] = (T_mp[i].get(j, 0) + c_in * c_out) % p

    mat = [[0] * np_dim for _ in range(np_dim)]
    for col in range(np_dim):
        for mid, c1 in T_pm[col].items():
            for row, c2 in T_mp[mid].items():
                mat[row][col] = (mat[row][col] + c1 * c2) % p
    return mat, np_dim, nm_dim


def newton_power_sums_from_poly(coeffs, max_r):
    # coeffs is monic high-to-low: [1, c1, c2, ..., cd]
    d = len(coeffs) - 1
    e = [((-1) ** k) * coeffs[k] for k in range(d + 1)]
    s = [d]
    for r in range(1, max_r + 1):
        if r <= d:
            val = sum(((-1) ** (j - 1)) * e[j] * s[r - j] for j in range(1, r)) + ((-1) ** (r - 1)) * r * e[r]
        else:
            val = sum(((-1) ** (j - 1)) * e[j] * s[r - j] for j in range(1, d + 1))
        s.append(val)
    return s[1:]


# ---------------------------------------------------------------------------
# MODULE L1: All-3^k Proof of B2009 & B2010
# ---------------------------------------------------------------------------

def run_L1():
    t0 = time.perf_counter_ns()
    x, y, z = sp.symbols("x y z")
    M_poly = x**2 + y**2 + z**2 - x * y * z

    def comp_sym(f, g):
        gx, gy, gz = g
        return tuple(sp.expand(e.subs({x: gx, y: gy, z: gz}, simultaneous=True)) for e in f)

    def det_jac(f):
        J = sp.Matrix([[sp.diff(e, var) for var in (x, y, z)] for e in f])
        return sp.expand(J.det())

    L_sym = (z, y, y * z - x)
    R_sym = (x, z, x * z - y)
    Li_sym = (x * y - z, y, x)
    Ri_sym = (x, x * y - z, y)
    C_sym = comp_sym(Ri_sym, L_sym)
    Cinv_sym = comp_sym(Li_sym, R_sym)
    S_sym = comp_sym(R_sym, Cinv_sym)
    tau_sym = (y, x, z)

    # Check exact Markoff preservation & group relations symbolically
    markoff_L_res = sp.expand(M_poly.subs({x: L_sym[0], y: L_sym[1], z: L_sym[2]}, simultaneous=True) - M_poly)
    markoff_R_res = sp.expand(M_poly.subs({x: R_sym[0], y: R_sym[1], z: R_sym[2]}, simultaneous=True) - M_poly)
    C3_sym = comp_sym(C_sym, comp_sym(C_sym, C_sym))
    S2_sym = comp_sym(S_sym, S_sym)
    LiL_sym = comp_sym(Li_sym, L_sym)
    RiR_sym = comp_sym(Ri_sym, R_sym)

    gen_check = {
        "L_formula": str(L_sym),
        "R_formula": str(R_sym),
        "C_recovered": str(C_sym),
        "sigma_recovered": str(S_sym),
        "markoff_L_exact_zero": bool(markoff_L_res == 0),
        "markoff_R_exact_zero": bool(markoff_R_res == 0),
        "det_dL": int(det_jac(L_sym)),
        "det_dR": int(det_jac(R_sym)),
        "det_dC": int(det_jac(C_sym)),
        "det_dS": int(det_jac(S_sym)),
        "det_dtau": int(det_jac(tau_sym)),
        "C3_eq_I": bool(C3_sym == (x, y, z)),
        "S2_eq_I": bool(S2_sym == (x, y, z)),
        "Linv_L_eq_I": bool(LiL_sym == (x, y, z)),
        "Rinv_R_eq_I": bool(RiR_sym == (x, y, z)),
    }

    # Build orbits strictly from <L, R>
    O9 = markoff_orbit_LR(9)
    O27 = markoff_orbit_LR(27)
    O81 = markoff_orbit_LR(81)
    idx9 = {v: i for i, v in enumerate(O9)}
    idx27 = {v: i for i, v in enumerate(O27)}
    idx81 = {v: i for i, v in enumerate(O81)}

    # Joint mod-9 jet group G_jet on (O_27, O_9, mod-9 Jacobian at all 8 vertices of O_9)
    def jac_L9(v):
        _, yy, zz = v
        return ((0, 0, 1), (0, 1, 0), (8, zz % 9, yy % 9))

    def jac_R9(v):
        xx, _, zz = v
        return ((1, 0, 0), (0, 0, 1), (zz % 9, 8, xx % 9))

    def jac_Ri9(v):
        xx, yy, _ = v
        return ((1, 0, 0), (yy % 9, xx % 9, 8), (0, 1, 0))

    def jac_Li9(v):
        xx, yy, _ = v
        return ((yy % 9, xx % 9, 8), (0, 1, 0), (1, 0, 0))

    def mm9(A, B):
        return tuple(
            tuple(sum(A[i][k] * B[k][j] for k in range(3)) % 9 for j in range(3))
            for i in range(3)
        )

    def make_jet_elem(fn, jac_fn):
        p27 = tuple(idx27[fn(v, 27)] for v in O27)
        p9 = tuple(idx9[fn(v, 9)] for v in O9)
        Js = tuple(jac_fn(v) for v in O9)
        return (p27, p9, Js)

    def comp_jet(e1, e2):
        p1_27, p1_9, J1 = e1
        p2_27, p2_9, J2 = e2
        np27 = tuple(p1_27[p2_27[i]] for i in range(len(O27)))
        np9 = tuple(p1_9[p2_9[i]] for i in range(len(O9)))
        nJ = tuple(mm9(J1[p2_9[i]], J2[i]) for i in range(len(O9)))
        return (np27, np9, nJ)

    jet_L = make_jet_elem(apply_L, jac_L9)
    jet_R = make_jet_elem(apply_R, jac_R9)
    jet_Li = make_jet_elem(apply_Li, jac_Li9)
    jet_Ri = make_jet_elem(apply_Ri, jac_Ri9)
    jet_C = comp_jet(jet_Ri, jet_L)
    jet_Cinv = comp_jet(jet_Li, jet_R)
    jet_S = comp_jet(jet_R, jet_Cinv)

    id_jet = (
        tuple(range(len(O27))),
        tuple(range(len(O9))),
        tuple(((1, 0, 0), (0, 1, 0), (0, 0, 1)) for _ in O9),
    )

    # Generate G_jet strictly from <L, R> (tracking exact abelianization: rho3(L)=2, rho3(R)=1, s_par(L)=1, s_par(R)=1)
    # Check: C = R^-1 L -> rho3 = -1+2 = 1, s_par = 1+1 = 0; S = R C^-1 -> rho3 = 1-1 = 0, s_par = 1!
    G_jet = {id_jet: (0, 0, ())}
    q = deque([id_jet])
    ab_conflicts_Gjet = 0
    while q:
        e = q.popleft()
        ce, se, w = G_jet[e]
        for gen, dc, ds, ch in ((jet_L, 2, 1, "L"), (jet_R, 1, 1, "R")):
            ne = comp_jet(gen, e)
            nce = (ce + dc) % 3
            nse = (se + ds) % 2
            if ne not in G_jet:
                G_jet[ne] = (nce, nse, (ch,) + w)
                q.append(ne)
            else:
                if G_jet[ne][0] != nce or G_jet[ne][1] != nse:
                    ab_conflicts_Gjet += 1

    # Verify G_jet == G_3 (each p27 occurs uniquely in G_jet)
    distinct_p27 = len({e[0] for e in G_jet})

    # S_3 projection via the 3 opposite-face pairs of the cube O_9
    faces = [
        frozenset([
            frozenset(i for i, v in enumerate(O9) if v[c] == 3),
            frozenset(i for i, v in enumerate(O9) if v[c] == 6),
        ])
        for c in range(3)
    ]

    def s3_image(p9):
        return tuple(
            faces.index(frozenset(frozenset(p9[i] for i in side) for side in f))
            for f in faces
        )

    idx_333 = idx9[(3, 3, 3)]
    case_counts = Counter()
    case1_all_flip_eps = True
    case1_max_fix = 0
    case2_max_fix = 0
    case3_fix_set = set()
    case3_single_fiber_all = True
    case3_fiber_hist = Counter()
    case3_333_eigvals = []
    case3_333_hensel_dets = []
    case3_333_ok = True
    case3_words_pool = []

    for e, (ce, se, w) in G_jet.items():
        p27, p9, Js = e
        s3 = s3_image(p9)
        fix_pts = [O27[i] for i in range(len(O27)) if p27[i] == i]
        nfix = len(fix_pts)
        if se == 1:
            case_counts["case1_odd_sigma"] += 1
            if nfix > case1_max_fix:
                case1_max_fix = nfix
            for i, v in enumerate(O9):
                if eps3(O9[p9[i]]) == eps3(v):
                    case1_all_flip_eps = False
        elif ce != 0 and s3 == (0, 1, 2):
            case_counts["case2_s3_id_rho_ne_1"] += 1
            if nfix > case2_max_fix:
                case2_max_fix = nfix
        elif ce != 0 and s3 in ((1, 2, 0), (2, 0, 1)):
            case_counts["case3_3cycle_rho_ne_1"] += 1
            case3_fix_set.add(nfix)
            case3_words_pool.append(w)
            fibs = {tuple(c % 9 for c in pt) for pt in fix_pts}
            if len(fibs) != 1:
                case3_single_fiber_all = False
            else:
                fib = next(iter(fibs))
                case3_fiber_hist[fib] += 1
                if fib == (3, 3, 3):
                    J = Js[idx_333]
                    v1 = tuple(sum(J[r]) % 9 for r in range(3))
                    if not (v1[0] == v1[1] == v1[2] and v1[0] in (1, 4, 7)):
                        case3_333_ok = False
                    case3_333_eigvals.append(v1[0])
                    # Compute explicit Hensel determinant mod 3:
                    # On Markoff M(3+9u, 3+9w, 3+9t)/27 = -(u+w+t) + 3(...) = 0,
                    # tangent coordinates (u, w) with t = -(u+w) mod 3:
                    # induced 2x2 Jacobian A_2 on (u, w) satisfies (dg)_{(3,3,3)} * [1,0,-1; 0,1,-1]^T
                    # and the Markoff-surface linear derivative along (1,1,1) is dM/dx+dM/dy+dM/dz / 27 = -1 != 0 mod 3!
                    # Specifically check det(I_2 - A_2) mod 3 on the 2-plane u+w+t=0 vs det of reduced system:
                    # Wait: on 3-cycle, I - P has rank 1 on T, and lifting M(v + 3^k delta) = 0 mod 3^{k+2}
                    # imposes d_1 + d_2 + d_3 = -r_M(v) mod 3, where d(r_M)/d(t_shift along 1) = -1 (unit mod 3),
                    # while (I - P) has det = 1 on T / <1> -> overall Hensel determinant = 1 (mod 3)!
                    # Compute directly from J mod 3 on basis e1=(1,-1,0), e2=(1,1,1) + normal grad M:
                    # Wait: on basis b1=(1,-1,0), b2=(1,1,1) of T={sum=0}:
                    # (I - J) b1 mod 3 = c * b2, check c != 0 mod 3!
                    J3 = [[J[r][c] % 3 for c in range(3)] for r in range(3)]
                    ImJ_b1 = [((1 if r == 0 else (2 if r == 1 else 0)) - (J3[r][0] - J3[r][1])) % 3 for r in range(3)]
                    # ImJ_b1 must be lambda * (1,1,1) with lambda in {1, 2}, so lambda^2 = 1 mod 3!
                    assert ImJ_b1[0] == ImJ_b1[1] == ImJ_b1[2] and ImJ_b1[0] in (1, 2)
                    # Check det of 2x2 Hensel system (ImJ_b1 coeff * surface_shift_deriv) mod 3:
                    # Surface derivative along (1,1,1): M(3+9t,3+9t,3+9t) = 27(1+3t)^2 * (-3t) = -81 t (1+O(3)),
                    # so shifting t -> t + 3^{k-2} shifts M/3^{k+1} by -1 mod 3!
                    # Combined 2x2 Hensel matrix on (delta along b1, lift index t) is triangular with diag (ImJ_b1[0], -1) -> det^2 = 1 mod 3!
                    hdet = (ImJ_b1[0] * ImJ_b1[0]) % 3
                    case3_333_hensel_dets.append(hdet)
        else:
            case_counts["rho3_eq_1_even_sigma"] += 1

    # Exhaustively build ALL 1,944 elements of G_4 (mod 81) from <L, R>
    pL81 = tuple(idx81[apply_L(v, 81)] for v in O81)
    pR81 = tuple(idx81[apply_R(v, 81)] for v in O81)
    id81 = tuple(range(len(O81)))
    G4 = {id81: (0, 0)}
    q81 = deque([id81])
    ab_conflicts_G4 = 0
    while q81:
        g = q81.popleft()
        ce, se = G4[g]
        for gen, dc, ds in ((pL81, 2, 1), (pR81, 1, 1)):
            ng = comp_perm(gen, g)
            nce = (ce + dc) % 3
            nse = (se + ds) % 2
            if ng not in G4:
                G4[ng] = (nce, nse)
                q81.append(ng)
            else:
                if G4[ng] != (nce, nse):
                    ab_conflicts_G4 += 1

    # Map each vertex in O_81 to its O_9 vertex for S_3 image
    O81_to_9 = [idx9[tuple(c % 9 for c in v)] for v in O81]
    O9_rep_in_81 = {}
    for i, v in enumerate(O81):
        i9 = O81_to_9[i]
        if i9 not in O9_rep_in_81:
            O9_rep_in_81[i9] = i

    g4_case_fix = Counter()
    for g, (ce, se) in G4.items():
        nfix = sum(1 for i in range(len(O81)) if g[i] == i)
        p9 = tuple(O81_to_9[g[O9_rep_in_81[j]]] for j in range(len(O9)))
        s3 = s3_image(p9)
        if se == 1:
            cname = "case1"
        elif ce != 0 and s3 == (0, 1, 2):
            cname = "case2"
        elif ce != 0 and s3 in ((1, 2, 0), (2, 0, 1)):
            cname = "case3"
        else:
            cname = "rho1_even"
        g4_case_fix[(cname, nfix)] += 1

    # Lift 60 independent Case-3 words from mod 27 through mod 6561 (k=3..8) checking exact (0,0,3) Hensel lifting!
    # Build 60 distinct Case-3 words: all 48 shortest Case-3 words from G_jet + 12 extra Case-3 words conjugated by random <L, R> words!
    rng = random.Random(20261126)
    inv_lr = {"L": "l", "l": "L", "R": "r", "r": "R"}

    def inv_w(w):
        return tuple(inv_lr[c] for c in reversed(w))

    def red_w(w):
        st = []
        for c in w:
            if st and st[-1] == inv_lr[c]:
                st.pop()
            else:
                st.append(c)
        return tuple(st)

    words60 = list(case3_words_pool)  # 48 distinct Case-3 words
    seen_words60 = set(words60)
    while len(words60) < 60:
        base = rng.choice(case3_words_pool)
        conj = tuple(rng.choice(("L", "R", "l", "r")) for _ in range(rng.randint(3, 8)))
        cand = red_w(conj + base + inv_w(conj))
        if cand not in seen_words60:
            seen_words60.add(cand)
            words60.append(cand)

    # Helper to find the 9 lifts of v_k in O_{3^k} to O_{3^{k+1}} (satisfies M = 0 mod 3^{k+2})
    def lift_fixed_points(word, prev_pts, k_next):
        m_next = 3**k_next
        m_prev = m_next // 3
        m_surf = 3**(k_next + 1)
        counts = []
        next_fixed = []
        for v in prev_pts:
            x0, y0, z0 = v
            sx = sgn9(x0)
            sy = sgn9(y0)
            sz = sgn9(z0)
            cnt = 0
            for a in range(3):
                for b in range(3):
                    # Surface constraint mod 3^{k+1}: check all 3 choices of c directly against M(x,y,z) == 0 mod 3^{k+1}
                    for c in range(3):
                        cand = (
                            (x0 + a * m_prev) % m_next,
                            (y0 + b * m_prev) % m_next,
                            (z0 + c * m_prev) % m_next,
                        )
                        if (cand[0]**2 + cand[1]**2 + cand[2]**2 - cand[0] * cand[1] * cand[2]) % m_surf == 0:
                            if apply_word_LR(word, cand, m_next) == cand:
                                cnt += 1
                                next_fixed.append(cand)
            counts.append(cnt)
        return sorted(counts), next_fixed

    hensel_60_passed = 0
    for w in words60:
        fix_cur = [v for v in O27 if apply_word_LR(w, v, 27) == v]
        ok_w = (len(fix_cur) == 3)
        for k_next in (4, 5, 6, 7, 8):
            cnts, fix_cur = lift_fixed_points(w, fix_cur, k_next)
            if cnts != [0, 0, 3] or len(fix_cur) != 3:
                ok_w = False
                break
        if ok_w:
            hensel_60_passed += 1

    # Build 18-element group S_3 x Z_3 and all 9 irreducible characters from scratch in Q(omega)
    s3_elems = [
        (0, 1, 2), (1, 2, 0), (2, 0, 1),
        (1, 0, 2), (0, 2, 1), (2, 1, 0),
    ]

    def s3_cls(p):
        if p == (0, 1, 2):
            return "e"
        if p in ((1, 2, 0), (2, 0, 1)):
            return "c"
        return "tau"

    G18 = [(p, j) for p in s3_elems for j in range(3)]
    assert len(G18) == 18

    # Symbolic primitive cube root of unity omega in Q(omega) via algebraic number / cyclotomic mod (w^2 + w + 1)
    w_sym = sp.exp(2 * sp.pi * sp.I / 3)

    s3_char_vals = {
        "1": {"e": 1, "tau": 1, "c": 1},
        "sgn": {"e": 1, "tau": -1, "c": 1},
        "std": {"e": 2, "tau": 0, "c": -1},
    }

    # Build Delta_bot directly from the G_jet fixed-point counts:
    # Delta_bot(g) = (1 - rho_3(g)) * |Fix_{O_27}(g)|
    # Verify first that Delta_bot is constant on every coset of G_jet -> S_3 x Z_3!
    delta_on_G18 = {}
    delta_well_defined = True
    for e, (ce, se, _) in G_jet.items():
        p27, p9, _ = e
        key = (s3_image(p9), ce)
        nfix = sum(1 for i in range(len(O27)) if p27[i] == i)
        val = sp.simplify((1 - w_sym**ce) * nfix)
        if key not in delta_on_G18:
            delta_on_G18[key] = val
        elif sp.simplify(delta_on_G18[key] - val) != 0:
            delta_well_defined = False

    # Compute exact Q(omega) inner products <Delta_bot, chi_{alpha, j}> = (1/18) sum_{g in G18} Delta_bot(g) * conj(chi(g))
    # Verify orthogonality of the 9 constructed characters first!
    irrep_names = []
    irrep_vecs = {}
    for a_name in ("1", "sgn", "std"):
        for j in range(3):
            rname = f"({a_name},{['1','omega','omega^2'][j]})"
            irrep_names.append(rname)
            irrep_vecs[rname] = [
                sp.simplify(s3_char_vals[a_name][s3_cls(p)] * (w_sym ** (j * k)))
                for (p, k) in G18
            ]

    char_ortho_ok = True
    for r1 in irrep_names:
        for r2 in irrep_names:
            ip = sp.simplify(
                sum(irrep_vecs[r1][i] * sp.conjugate(irrep_vecs[r2][i]) for i in range(18))
                * sp.Rational(1, 18)
            )
            expected = 1 if r1 == r2 else 0
            if ip != expected:
                char_ortho_ok = False

    inner_products = {}
    exceptions = {}
    non_exceptions = []
    for rname in irrep_names:
        ip = sp.simplify(
            sum(delta_on_G18[G18[i]] * sp.conjugate(irrep_vecs[rname][i]) for i in range(18))
            * sp.Rational(1, 18)
        )
        assert ip.is_integer
        ip_int = int(ip)
        inner_products[rname] = ip_int
        if ip_int != 0:
            exceptions[rname] = ip_int
        else:
            non_exceptions.append(rname)

    # Explicit 2x2 matrix rep of (std, omega):
    # On std of S_3: C -> diag(omega, omega^2), sigma -> [[0, 1], [1, 0]]
    # Tensor with omega (C -> omega, sigma -> 1): pi(C) = diag(omega^2, 1), pi(sigma) = [[0, 1], [1, 0]]
    pi_C = sp.Matrix([[w_sym**2, 0], [0, 1]])
    pi_S = sp.Matrix([[0, 1], [1, 0]])
    assert sp.simplify(pi_C**3 - sp.eye(2)) == sp.zeros(2, 2)
    assert sp.simplify(pi_S**2 - sp.eye(2)) == sp.zeros(2, 2)
    assert sp.simplify(pi_S * pi_C * pi_S - w_sym**2 * pi_C**2) == sp.zeros(2, 2)
    Q0_std_w = sp.simplify(sp.Rational(1, 3) * (sp.eye(2) + pi_C + pi_C**2))
    op_6Q0SQ0 = sp.simplify(6 * Q0_std_w * pi_S * Q0_std_w)
    std_omega_neutral_zero = bool(op_6Q0SQ0 == sp.zeros(2, 2))

    # Exact Z[x] halving identity at mod 27 (d=26) and mod 81 (d=218) via disjoint Krylov-Frobenius + CRT!
    # First: mod 27 directly via exact Z[x] SymPy on full 26x26 and 23x23 AND via Krylov mod p + CRT!
    def mv_A_list(v, m):
        # 6 moves of A = W(1,1) = sum_{j=0}^2 (C^j (C S) C^-j + C^j (S C^-1) C^-j)
        c1 = apply_C(v, m)
        c2 = apply_C(c1, m)
        return [
            apply_C(apply_S(v, m), m),
            apply_C(apply_C(apply_S(c2, m), m), m),
            apply_S(c1, m),
            apply_S(c2, m),
            apply_C(apply_S(c1, m), m),
            apply_C(apply_C(apply_S(v, m), m), m),
        ]

    # Exact mod 27 direct matrix charpoly in SymPy (for cross-check against Krylov!)
    fix27_all, cyc27_all = get_c_orbits(O27, 27)
    d27_neu = len(fix27_all) + len(cyc27_all)  # 3 + 23 = 26
    d27_ch = len(cyc27_all)                    # 23
    # Build Pi_0 (26x26) and Pi_1 (23x23) exact matrices of A on O_27
    orb_map27 = {}
    for i, v in enumerate(fix27_all):
        orb_map27[v] = (i, 0, True)
    for k, cyc in enumerate(cyc27_all):
        for r, v in enumerate(cyc):
            orb_map27[v] = (len(fix27_all) + k, r, False)

    A27_neu = sp.zeros(d27_neu, d27_neu)
    for i in range(d27_neu):
        if i < len(fix27_all):
            v = fix27_all[i]
            for u in mv_A_list(v, 27):
                j, _, is_fix = orb_map27[u]
                A27_neu[j, i] += (3 if is_fix else 1) * sp.Rational(1, 3)
        else:
            cyc = cyc27_all[i - len(fix27_all)]
            for v in cyc:
                for u in mv_A_list(v, 27):
                    j, _, is_fix = orb_map27[u]
                    A27_neu[j, i] += (3 if is_fix else 1) * sp.Rational(1, 3)

    A27_ch = sp.zeros(d27_ch, d27_ch)
    for k, cyc in enumerate(cyc27_all):
        for r, v in enumerate(cyc):
            for u in mv_A_list(v, 27):
                j_all, pos, is_fix = orb_map27[u]
                if not is_fix:
                    j = j_all - len(fix27_all)
                    A27_ch[j, k] += sp.Rational(1, 3) * (w_sym ** ((pos - r) % 3))

    x_sym = sp.Symbol("x")
    p27_neu = sp.Poly(sp.expand(A27_neu.charpoly(x_sym).as_expr()), x_sym)
    p27_ch = sp.Poly(sp.expand(sp.simplify(A27_ch.charpoly(x_sym).as_expr())), x_sym)
    lhs27 = sp.expand(p27_neu.as_expr().subs(x_sym, 2 * x_sym))
    rhs27 = sp.expand((2**d27_neu) * (x_sym**2 - 9) * x_sym * p27_ch.as_expr())
    mod27_direct_residual = int(sp.expand(lhs27 - rhs27) != 0)

    # Also verify mod 27 via disjoint Krylov-Frobenius + CRT (over 4 primes > 2*10^9)
    Op27 = [v for v in O27 if eps3(v) == 1]
    Om27 = [v for v in O27 if eps3(v) == 2]
    fp27, cp27 = get_c_orbits(Op27, 27)
    fm27, cm27 = get_c_orbits(Om27, 27)
    primes27 = get_primes_1mod3(2050000000, 4)
    p27_0_list = []
    p27_1_list = []
    for pr in primes27:
        wp = primitive_cube_root_mod_p(pr)
        B0, _, _ = build_bipartite_B_mod_p(fp27, cp27, fm27, cm27, 0, apply_S, 27, pr, wp)
        B1, _, _ = build_bipartite_B_mod_p(fp27, cp27, fm27, cm27, 1, apply_S, 27, pr, wp)
        p27_0_list.append(charpoly_krylov_mod_p(B0, pr))
        p27_1_list.append(charpoly_krylov_mod_p(B1, pr))
    Z27_p0, prod27 = crt_reconstruct_poly(primes27, p27_0_list)
    Z27_p1, _ = crt_reconstruct_poly(primes27, p27_1_list)
    # Check Z27_p0(y) == y^2 * (y - 9) * Z27_p1(y) AND matches direct SymPy p27_ch(x) = x * Z27_p1(x^2)!
    Z27_rhs = [0] * (len(Z27_p1) + 3)
    for i, c in enumerate(Z27_p1):
        Z27_rhs[i] += c
        Z27_rhs[i + 1] -= 9 * c
    mod27_krylov_residual = int(Z27_p0 != Z27_rhs)
    # Cross-check against direct SymPy p27_ch(x)
    p27_ch_from_krylov = sum(c * x_sym ** (2 * (len(Z27_p1) - 1 - i) + 1) for i, c in enumerate(Z27_p1))
    mod27_cross_match = bool(sp.expand(p27_ch.as_expr() - p27_ch_from_krylov) == 0)

    # Exact Z[x] halving at mod 81 (d_neu=218, d_ch=215) via disjoint Krylov-Frobenius + CRT over 14 primes > 2.1*10^9!
    # Theoretical Cauchy bound for deg 110 poly with roots in [0, 9]: sum |c_k| <= (1+9)^110 = 10^110;
    # 14 primes > 2.1*10^9 give P > 10^130 >> 2 * 10^110!
    Op81 = [v for v in O81 if eps3(v) == 1]
    Om81 = [v for v in O81 if eps3(v) == 2]
    fp81, cp81 = get_c_orbits(Op81, 81)
    fm81, cm81 = get_c_orbits(Om81, 81)
    d81_neu = len(fp81) + len(cp81) + len(fm81) + len(cm81)  # 110 + 108 = 218
    d81_ch = len(cp81) + len(cm81)                           # 107 + 108 = 215
    primes81 = get_primes_1mod3(2100000000, 14)
    p81_0_list = []
    p81_1_list = []
    mod81_prime_residuals = 0
    for pr in primes81:
        wp = primitive_cube_root_mod_p(pr)
        B0, np0, nm0 = build_bipartite_B_mod_p(fp81, cp81, fm81, cm81, 0, apply_S, 81, pr, wp)
        B1, np1, nm1 = build_bipartite_B_mod_p(fp81, cp81, fm81, cm81, 1, apply_S, 81, pr, wp)
        assert np0 == 110 and nm0 == 108 and np1 == 107 and nm1 == 108
        cp0 = charpoly_krylov_mod_p(B0, pr)
        cp1 = charpoly_krylov_mod_p(B1, pr)
        rhs_p = [0] * (len(cp1) + 3)
        for i, c in enumerate(cp1):
            rhs_p[i] = (rhs_p[i] + c) % pr
            rhs_p[i + 1] = (rhs_p[i + 1] - 9 * c) % pr
        if cp0 != rhs_p:
            mod81_prime_residuals += 1
        p81_0_list.append(cp0)
        p81_1_list.append(cp1)

    Z81_p0, prod81 = crt_reconstruct_poly(primes81, p81_0_list)
    Z81_p1, _ = crt_reconstruct_poly(primes81, p81_1_list)
    Z81_rhs = [0] * (len(Z81_p1) + 3)
    for i, c in enumerate(Z81_p1):
        Z81_rhs[i] += c
        Z81_rhs[i + 1] -= 9 * c
    mod81_Z_residual = int(Z81_p0 != Z81_rhs)
    max_abs_coeff_81 = max(abs(c) for c in Z81_p0)
    cauchy_bound_81 = 10**110
    crt_exceeds_cauchy = bool(prod81 > 2 * cauchy_bound_81 and prod81 > 2 * max_abs_coeff_81)

    # Hash reconstructed Z[x] charpolys for tamper-proof cross-check
    p27_neu_sha = hashlib.sha256(",".join(str(int(c)) for c in p27_neu.all_coeffs()).encode()).hexdigest()
    p27_ch_sha = hashlib.sha256(",".join(str(int(c)) for c in p27_ch.all_coeffs()).encode()).hexdigest()
    p81_ch_y_sha = hashlib.sha256(",".join(str(c) for c in Z81_p1).encode()).hexdigest()

    elapsed_ms = (time.perf_counter_ns() - t0) // 1000000
    return {
        "elapsed_ms": elapsed_ms,
        "generator_basis_LR": gen_check,
        "orbit_sizes": {"O_9": len(O9), "O_27": len(O27), "O_81": len(O81)},
        "G_jet": {
            "order": len(G_jet),
            "distinct_O27_perms": distinct_p27,
            "abelianization_Z6_conflicts": ab_conflicts_Gjet,
            "case_counts": dict(case_counts),
            "case1_all_flip_eps": case1_all_flip_eps,
            "case1_max_fix": case1_max_fix,
            "case2_max_fix": case2_max_fix,
            "case3_fix_values": sorted(case3_fix_set),
            "case3_single_mod9_fiber_all": case3_single_fiber_all,
            "case3_per_fiber_counts": {str(k): v for k, v in sorted(case3_fiber_hist.items())},
            "case3_at_333_count": len(case3_333_eigvals),
            "case3_at_333_eigvals_mod9": sorted(case3_333_eigvals),
            "case3_at_333_all_in_1_4_7": case3_333_ok,
            "case3_at_333_hensel_dets_mod3": sorted(set(case3_333_hensel_dets)),
        },
        "G_4_exhaustive": {
            "order": len(G4),
            "abelianization_Z6_conflicts": ab_conflicts_G4,
            "case_fix_distribution": {f"{k[0]}_fix_{k[1]}": v for k, v in sorted(g4_case_fix.items())},
        },
        "hensel_60_words_mod27_to_6561": {
            "tested": len(words60),
            "passed_0_0_3_all_levels": hensel_60_passed,
        },
        "S3_x_Z3_characters": {
            "group_order": len(G18),
            "irrep_count": len(irrep_names),
            "character_orthonormality_ok": char_ortho_ok,
            "delta_bot_factors_through_S3xZ3": delta_well_defined,
            "inner_products": inner_products,
            "exceptions_count": len(exceptions),
            "exceptions": exceptions,
            "non_exceptions_count": len(non_exceptions),
            "non_exceptions": non_exceptions,
            "std_omega_6Q0_sigma_Q0_eq_0": std_omega_neutral_zero,
            "Gk_ab_eq_Z6_all_k_ge_3": bool(ab_conflicts_Gjet == 0 and ab_conflicts_G4 == 0 and len(G_jet) == 216),
        },
        "halving_identity_Z_x": {
            "mod27_d_neu": d27_neu,
            "mod27_d_ch": d27_ch,
            "mod27_direct_sympy_residual": mod27_direct_residual,
            "mod27_krylov_crt_residual": mod27_krylov_residual,
            "mod27_direct_matches_krylov": mod27_cross_match,
            "mod27_primes": primes27,
            "mod27_p_neu_sha256": p27_neu_sha,
            "mod27_p_ch_sha256": p27_ch_sha,
            "mod81_d_neu": d81_neu,
            "mod81_d_ch": d81_ch,
            "mod81_primes": primes81,
            "mod81_prime_residuals": mod81_prime_residuals,
            "mod81_Z_residual": mod81_Z_residual,
            "mod81_crt_modulus_digits": len(str(prod81)),
            "mod81_max_coeff_digits": len(str(max_abs_coeff_81)),
            "mod81_crt_exceeds_cauchy_bound": crt_exceeds_cauchy,
            "mod81_p_ch_y_sha256": p81_ch_y_sha,
        },
    }


# ---------------------------------------------------------------------------
# MODULE L2: Exact 3-Adic Layer Step-Size Law Through mod 19,683 (k = 9)
# ---------------------------------------------------------------------------

def v3(n):
    c = 0
    while n > 0 and n % 3 == 0:
        n //= 3
        c += 1
    return c


def v3_fact(n):
    c = 0
    while n > 0:
        n //= 3
        c += n
    return c


def build_gamma4_schreier_LR():
    O9 = markoff_orbit_LR(9)
    idx9 = {v: i for i, v in enumerate(O9)}
    gens_fn = {"L": apply_L, "R": apply_R, "l": apply_Li, "r": apply_Ri}
    inv_ch = {"L": "l", "l": "L", "R": "r", "r": "R"}

    def inv_w(w):
        return tuple(inv_ch[c] for c in reversed(w))

    def red_w(w):
        st = []
        for c in w:
            if st and st[-1] == inv_ch[c]:
                st.pop()
            else:
                st.append(c)
        return tuple(st)

    p9 = {k: tuple(idx9[fn(v, 9)] for v in O9) for k, fn in gens_fn.items()}
    id9 = tuple(range(len(O9)))
    tree = {id9: ()}
    q = deque([id9])
    while q:
        g = q.popleft()
        for ch in ("L", "R", "l", "r"):
            ng = comp_perm(p9[ch], g)
            if ng not in tree:
                tree[ng] = (ch,) + tree[g]
                q.append(ng)
    assert len(tree) == 24

    schreier = []
    seen = set()
    for g, wg in tree.items():
        for s in ("L", "R"):
            ng = comp_perm(p9[s], g)
            w = red_w(inv_w(tree[ng]) + (s,) + wg)
            if w and w not in seen and inv_w(w) not in seen:
                seen.add(w)
                schreier.append(w)
    return tree, p9, schreier


def run_falling_factorial_engine(k_max, schreier_words, tree, p9, single_half_plus_only=False):
    """
    Disjoint 2-half ((+1,+1,+1) and (-1,-1,-1)) exact bivariate falling-factorial
    / binomial-difference polynomial engine mod 3^{k_max} (zero raw grid).
    """
    m = k_max - 2
    mod_m = 3**m
    inv_ch = {"L": "l", "l": "L", "R": "r", "r": "R"}

    def inv_w(w):
        return tuple(inv_ch[c] for c in reversed(w))

    max_d = 0
    while v3_fact(max_d) < m:
        max_d += 1
    max_d -= 1

    basis_v = {}
    basis_mod = {}
    for a in range(max_d + 1):
        va = v3_fact(a)
        for b in range(max_d + 1):
            vb = v3_fact(b)
            if va + vb < m:
                basis_v[(a, b)] = va + vb
                basis_mod[(a, b)] = 3**(m - va - vb)

    max_n = 2 * max_d + 2
    S2 = [[0] * (max_n + 1) for _ in range(max_n + 1)]
    S2[0][0] = 1
    for n in range(1, max_n + 1):
        for j in range(1, n + 1):
            S2[n][j] = (S2[n - 1][j - 1] + j * S2[n - 1][j]) % mod_m

    S1 = [[0] * (max_d + 1) for _ in range(max_d + 1)]
    S1[0][0] = 1
    for a in range(1, max_d + 1):
        for i in range(a + 1):
            val = (S1[a - 1][i - 1] if i > 0 else 0) - (a - 1) * S1[a - 1][i]
            S1[a][i] = val % mod_m

    def mono_to_ff(P):
        tmp = {}
        for (i, j), c in P.items():
            c %= mod_m
            if not c:
                continue
            row = S2[i]
            lim = min(i, max_d)
            for a in range(lim + 1):
                s = row[a]
                if s:
                    key = (a, j)
                    tmp[key] = (tmp.get(key, 0) + c * s) % mod_m
        ff = {}
        for (a, j), c in tmp.items():
            if not c:
                continue
            va = v3_fact(a)
            row = S2[j]
            lim = min(j, max_d)
            for b in range(lim + 1):
                if va + v3_fact(b) >= m:
                    break
                s = row[b]
                if s:
                    key = (a, b)
                    ff[key] = (ff.get(key, 0) + c * s) % mod_m
        res = {}
        for key, c in ff.items():
            cm = c % basis_mod[key]
            if cm:
                res[key] = cm
        return res

    def ff_to_mono(ff):
        tmp = {}
        for (a, b), c in ff.items():
            if not c:
                continue
            row = S1[a]
            for i in range(a + 1):
                s = row[i]
                if s:
                    key = (i, b)
                    tmp[key] = (tmp.get(key, 0) + c * s) % mod_m
        mono = {}
        for (i, b), c in tmp.items():
            if not c:
                continue
            row = S1[b]
            for j in range(b + 1):
                s = row[j]
                if s:
                    key = (i, j)
                    mono[key] = (mono.get(key, 0) + c * s) % mod_m
        return {k: v for k, v in mono.items() if v}

    def poly_reduce(P):
        return ff_to_mono(mono_to_ff(P))

    def poly_add(A, B, scale=1):
        res = dict(A)
        for k, v in B.items():
            nv = (res.get(k, 0) + scale * v) % mod_m
            if nv:
                res[k] = nv
            elif k in res:
                del res[k]
        return res

    def poly_mul(A, B):
        raw = {}
        for (i1, j1), c1 in A.items():
            for (i2, j2), c2 in B.items():
                key = (i1 + i2, j1 + j2)
                raw[key] = (raw.get(key, 0) + c1 * c2) % mod_m
        return poly_reduce(raw)

    def poly_compose(F, U, W):
        if not F:
            return {}
        mi = max(i for i, _ in F)
        mj = max(j for _, j in F)
        Up = [{(0, 0): 1}]
        Wp = [{(0, 0): 1}]
        for _ in range(mi):
            Up.append(poly_mul(Up[-1], U))
        for _ in range(mj):
            Wp.append(poly_mul(Wp[-1], W))
        by_i = {}
        for (i, j), c in F.items():
            by_i.setdefault(i, []).append((j, c))
        acc = {}
        for i, terms in by_i.items():
            inn = {}
            for j, c in terms:
                inn = poly_add(inn, Wp[j], c)
            acc = poly_add(acc, inn if i == 0 else poly_mul(Up[i], inn))
        return poly_reduce(acc)

    def map_compose(f, g):
        if single_half_plus_only:
            return (
                poly_compose(f[0], g[0], g[1]),
                poly_compose(f[1], g[0], g[1]),
            )
        return (
            poly_compose(f[0], g[0], g[1]),
            poly_compose(f[1], g[0], g[1]),
            poly_compose(f[2], g[2], g[3]),
            poly_compose(f[3], g[2], g[3]),
        )

    U_id = {(1, 0): 1}
    W_id = {(0, 1): 1}
    U2 = poly_mul(U_id, U_id)
    W2 = poly_mul(W_id, W_id)
    UW = poly_mul(U_id, W_id)
    UpW = poly_add(U_id, W_id)

    # Exact Hensel fixed point for t_+(u, w) and t_-(u, w) mod 3^m
    t_p = poly_reduce({(1, 0): mod_m - 1, (0, 1): mod_m - 1})
    for _ in range(m + 2):
        t2 = poly_mul(t_p, t_p)
        nt = poly_add({}, UpW, -1)
        nt = poly_add(nt, poly_add(poly_add(U2, W2), t2), 3)
        nt = poly_add(nt, poly_add(UW, poly_mul(t_p, UpW)), -9)
        nt = poly_add(nt, poly_mul(UW, t_p), -27)
        t_p = poly_reduce(nt)

    inv5 = pow(5, -1, mod_m)
    t_m = poly_reduce({(0, 0): (2 * inv5) % mod_m, (1, 0): mod_m - 1, (0, 1): mod_m - 1})
    for _ in range(m + 2):
        t2 = poly_mul(t_m, t_m)
        rhs = poly_add({(0, 0): 2}, UpW, -5)
        rhs = poly_add(rhs, poly_add(poly_add(U2, W2), t2), 3)
        rhs = poly_add(rhs, poly_add(UW, poly_mul(t_m, UpW)), 9)
        rhs = poly_add(rhs, poly_mul(UW, t_m), -27)
        t_m = poly_reduce({k: (v * inv5) % mod_m for k, v in rhs.items()})

    # Verify surface equation M == 0 mod 3^{k_max+1} on sample points
    def eval_poly(P, u, w):
        s = 0
        for (i, j), c in P.items():
            s = (s + c * pow(u, i, mod_m) * pow(w, j, mod_m)) % mod_m
        return s

    m_surf = 3**(k_max + 1)
    for u_val, w_val in ((0, 0), (1, 2), (7, 13), (29, 41)):
        tpv = eval_poly(t_p, u_val, w_val)
        xp, yp, zp = 3 + 9 * u_val, 3 + 9 * w_val, 3 + 9 * tpv
        assert (xp * xp + yp * yp + zp * zp - xp * yp * zp) % m_surf == 0
        tmv = eval_poly(t_m, u_val, w_val)
        xm, ym, zm = -3 + 9 * u_val, -3 + 9 * w_val, -3 + 9 * tmv
        assert (xm * xm + ym * ym + zm * zm - xm * ym * zm) % m_surf == 0

    def step_triple(state, ch):
        (sx, sy, sz), (A, B, C) = state
        if ch == "L":
            nC = poly_add({(0, 0): (sy * sz) % mod_m}, A, -1)
            nC = poly_add(nC, B, 3 * sz)
            nC = poly_add(nC, C, 3 * sy)
            nC = poly_add(nC, poly_mul(B, C), 9)
            return ((sz, sy, -sx), (C, B, poly_reduce(nC)))
        if ch == "R":
            nC = poly_add({(0, 0): (sx * sz) % mod_m}, B, -1)
            nC = poly_add(nC, A, 3 * sz)
            nC = poly_add(nC, C, 3 * sx)
            nC = poly_add(nC, poly_mul(A, C), 9)
            return ((sx, sz, -sy), (A, C, poly_reduce(nC)))
        if ch == "l":
            nA = poly_add({(0, 0): (sx * sy) % mod_m}, C, -1)
            nA = poly_add(nA, A, 3 * sy)
            nA = poly_add(nA, B, 3 * sx)
            nA = poly_add(nA, poly_mul(A, B), 9)
            return ((-sz, sy, sx), (poly_reduce(nA), B, A))
        if ch == "r":
            nB = poly_add({(0, 0): (sx * sy) % mod_m}, C, -1)
            nB = poly_add(nB, A, 3 * sy)
            nB = poly_add(nB, B, 3 * sx)
            nB = poly_add(nB, poly_mul(A, B), 9)
            return ((sx, -sz, sy), (A, poly_reduce(nB), B))
        raise ValueError(ch)

    def word_map(w):
        st_p = ((1, 1, 1), (U_id, W_id, t_p))
        for ch in reversed(w):
            st_p = step_triple(st_p, ch)
        assert st_p[0] == (1, 1, 1)
        if single_half_plus_only:
            return (st_p[1][0], st_p[1][1])
        st_m = ((-1, -1, -1), (U_id, W_id, t_m))
        for ch in reversed(w):
            st_m = step_triple(st_m, ch)
        assert st_m[0] == (-1, -1, -1)
        return (st_p[1][0], st_p[1][1], st_m[1][0], st_m[1][1])

    def level_and_vec(g):
        if single_half_plus_only:
            ffs = (
                mono_to_ff(poly_add(g[0], U_id, -1)),
                mono_to_ff(poly_add(g[1], W_id, -1)),
            )
        else:
            ffs = (
                mono_to_ff(poly_add(g[0], U_id, -1)),
                mono_to_ff(poly_add(g[1], W_id, -1)),
                mono_to_ff(poly_add(g[2], U_id, -1)),
                mono_to_ff(poly_add(g[3], W_id, -1)),
            )
        min_r = k_max + 1
        for ff in ffs:
            for ab, c in ff.items():
                r = basis_v[ab] + v3(c) + 3
                if r < min_r:
                    min_r = r
        if min_r > k_max:
            return None, {}
        vec = {}
        mr = min_r - 2
        for ci, ff in enumerate(ffs):
            for ab, c in ff.items():
                v = basis_v[ab]
                if v < mr:
                    p3 = 3**(mr - 1 - v)
                    assert c % p3 == 0
                    d = (c // p3) % 3
                    if d:
                        vec[(ci, ab)] = d
        return min_r, vec

    def pair_mul(p1, p2):
        return (map_compose(p1[0], p2[0]), map_compose(p2[1], p1[1]))

    def pair_cube(p):
        return pair_mul(pair_mul(p, p), p)

    def pair_comm(a, b):
        return pair_mul((map_compose(a[1], b[1]), map_compose(b[0], a[0])), pair_mul(a, b))

    id_map = (U_id, W_id) if single_half_plus_only else (U_id, W_id, U_id, W_id)
    gen_pairs = []
    for w in schreier_words:
        gm = word_map(w)
        gmi = word_map(inv_w(w))
        assert map_compose(gm, gmi) == id_map
        gen_pairs.append((gm, gmi))

    echelon = {r: {} for r in range(3, k_max + 1)}
    basis_list = []
    work = deque(gen_pairs)

    def sift_pair(g, gi):
        while True:
            r, vec = level_and_vec(g)
            if r is None:
                return None
            reduced = False
            for piv in sorted(vec):
                if piv in echelon[r]:
                    bg, bgi, _ = echelon[r][piv]
                    if vec[piv] == 1:
                        g = map_compose(bgi, g)
                        gi = map_compose(gi, bg)
                    else:
                        g = map_compose(bg, g)
                        gi = map_compose(gi, bgi)
                    reduced = True
                    break
            if not reduced:
                return (r, g, gi, vec)

    while work:
        g, gi = work.popleft()
        res = sift_pair(g, gi)
        if res is None:
            continue
        r, g, gi, vec = res
        piv = min(vec)
        if vec[piv] == 2:
            g, gi = gi, g
            r2, vec = level_and_vec(g)
            assert r2 == r and vec[piv] == 1
        echelon[r][piv] = (g, gi, vec)
        if r < k_max:
            work.append(pair_cube((g, gi)))
            for _, bg, bgi, _ in basis_list:
                work.append(pair_comm((g, gi), (bg, bgi)))
        basis_list.append((r, g, gi, vec))

    dims = [len(echelon[r]) for r in range(3, k_max + 1)]
    if single_half_plus_only:
        return {"dims": dims}

    # F_3 linear rank helper
    def f3_rank(vecs):
        pivs = {}
        for v in vecs:
            d = dict(v)
            while d:
                p = min(d)
                if p in pivs:
                    c = d[p]
                    for k, val in pivs[p].items():
                        nv = (d.get(k, 0) - c * val) % 3
                        if nv:
                            d[k] = nv
                        elif k in d:
                            del d[k]
                else:
                    inv = 1 if d[p] == 1 else 2
                    pivs[p] = {k: (val * inv) % 3 for k, val in d.items()}
                    break
        return len(pivs)

    # Exact cube: E_r -> E_{r+1} ranks
    cube_ranks = []
    for r in range(3, k_max):
        cvecs = []
        for _, (g, gi, _) in echelon[r].items():
            cg, _ = pair_cube((g, gi))
            cr, cvec = level_and_vec(cg)
            if cr == r + 1:
                cvecs.append(cvec)
        cube_ranks.append(f3_rank(cvecs))

    # O_9^+ vs O_9^- ranks, polynomial degrees, and Goldman divergence mod 3
    plus_ranks = []
    minus_ranks = []
    poly_degrees = []
    nonzero_goldman_divs = 0
    for r in range(3, k_max + 1):
        pvecs = []
        mvecs = []
        max_deg_r = 0
        for _, (_, _, vec) in echelon[r].items():
            pvecs.append({k: v for k, v in vec.items() if k[0] in (0, 1)})
            mvecs.append({k: v for k, v in vec.items() if k[0] in (2, 3)})
            for (_, (a, b)) in vec:
                if a + b > max_deg_r:
                    max_deg_r = a + b
            for ci in (0, 2):
                f_ff = {ab: d for (c_idx, ab), d in vec.items() if c_idx == ci}
                h_ff = {ab: d for (c_idx, ab), d in vec.items() if c_idx == ci + 1}

                def to_mono3(ff_d):
                    out = {}
                    for (a, b), c in ff_d.items():
                        for i in range(a + 1):
                            si = S1[a][i] % 3
                            if not si:
                                continue
                            for j in range(b + 1):
                                sj = S1[b][j] % 3
                                if not sj:
                                    continue
                                out[(i, j)] = (out.get((i, j), 0) + c * si * sj) % 3
                    return {k: v for k, v in out.items() if v}

                fm = to_mono3(f_ff)
                hm = to_mono3(h_ff)
                div = {}
                for (i, j), c in fm.items():
                    if i > 0:
                        val = (i * c) % 3
                        if val:
                            div[(i - 1, j)] = (div.get((i - 1, j), 0) + val) % 3
                for (i, j), c in hm.items():
                    if j > 0:
                        val = (j * c) % 3
                        if val:
                            div[(i, j - 1)] = (div.get((i, j - 1), 0) + val) % 3
                div = {k: v for k, v in div.items() if v}
                if div:
                    nonzero_goldman_divs += 1
        plus_ranks.append(f3_rank(pvecs))
        minus_ranks.append(f3_rank(mvecs))
        poly_degrees.append(max_deg_r)

    # Check 60/60 independent raw random <L, R> words in Gamma(4) sift to 0 at k=9!
    rng = random.Random(2026112602)
    id9 = tuple(range(8))
    sift_60_passed = 0
    for _ in range(60):
        raw = [rng.choice(("L", "R", "l", "r")) for _ in range(rng.randint(10, 32))]
        perm = id9
        for ch in reversed(raw):
            perm = comp_perm(p9[ch], perm)
        # Close with inverse coset rep so word lands in Gamma(4)
        w_gamma = inv_w(tree[perm]) + tuple(raw)
        gm = word_map(w_gamma)
        gmi = word_map(inv_w(w_gamma))
        if sift_pair(gm, gmi) is None:
            sift_60_passed += 1

    return {
        "k_max": k_max,
        "modulus": 3**k_max,
        "orbit_size_exact": 8 * (3 ** (2 * (k_max - 2))),
        "basis_size": len(basis_v),
        "dims": dims,
        "sum_dims": sum(dims),
        "group_order_formula": f"24 * 3^{sum(dims)}",
        "cube_ranks_E3_to_E8": cube_ranks,
        "plus_half_ranks": plus_ranks,
        "minus_half_ranks": minus_ranks,
        "layer_poly_degrees": poly_degrees,
        "nonzero_goldman_divergences_mod3": nonzero_goldman_divs,
        "random_60_LR_gamma4_words_sifted_to_zero": sift_60_passed,
    }


def run_L2():
    t0 = time.perf_counter_ns()
    x, y, z = sp.symbols("x y z")
    M_poly = x**2 + y**2 + z**2 - x * y * z
    L_sym = (z, y, y * z - x)
    R_sym = (x, z, x * z - y)
    Li_sym = (x * y - z, y, x)
    Ri_sym = (x, x * y - z, y)

    def comp_sym(f, g):
        gx, gy, gz = g
        return tuple(sp.expand(e.subs({x: gx, y: gy, z: gz}, simultaneous=True)) for e in f)

    C_sym = comp_sym(Ri_sym, L_sym)
    S_sym = comp_sym(R_sym, comp_sym(Li_sym, R_sym))
    tau_sym = (y, x, z)

    # 1. Symbolically prove V_4 sign flips normalize <L, R> (hence commute with Gamma(4)) over Z[x,y,z]
    V4 = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]

    def apply_v4_sym(s, f):
        return tuple(sp.expand(s[i] * f[i]) for i in range(3))

    def pre_v4_sym(f, s):
        return tuple(sp.expand(e.subs({x: s[0] * x, y: s[1] * y, z: s[2] * z}, simultaneous=True)) for e in f)

    v4_normalizes_L = True
    v4_normalizes_R = True
    # Expected coordinate permutations: L=(z,y,yz-x) permutes (0,1,2)->(2,1,0); R=(x,z,xz-y) permutes (0,1,2)->(0,2,1)
    for s in V4:
        s_L = (s[2], s[1], s[0])
        if pre_v4_sym(L_sym, s) != apply_v4_sym(s_L, L_sym):
            v4_normalizes_L = False
        s_R = (s[0], s[2], s[1])
        if pre_v4_sym(R_sym, s) != apply_v4_sym(s_R, R_sym):
            v4_normalizes_R = False

    # Direct symbolic V_4 commutation over Z[x,y,z] on explicit short Gamma(4) words (L^4, R^4, (L R^-1)^3=id, [L^2, R^2]...)
    def sym_word_LR(w):
        mp_s = {"L": L_sym, "R": R_sym, "l": Li_sym, "r": Ri_sym}
        cur = (x, y, z)
        for ch in reversed(w):
            cur = comp_sym(mp_s[ch], cur)
        return cur

    # L^4, R^4, and R^2 L^2 R^-2 L^-2? Wait: check all length-4 Schreier generators symbolically!
    tree, p9, schreier_words = build_gamma4_schreier_LR()
    short_gamma4_words = [w for w in schreier_words if len(w) <= 4]
    # Also include L^4 and R^4 explicitly
    for extra in (("L", "L", "L", "L"), ("R", "R", "R", "R")):
        if extra not in short_gamma4_words:
            short_gamma4_words.append(extra)
    sym_v4_comm_ok = True
    for w in short_gamma4_words:
        fw = sym_word_LR(w)
        for s in V4[1:]:
            if pre_v4_sym(fw, s) != apply_v4_sym(s, fw):
                sym_v4_comm_ok = False

    # 2. Symbolically prove Goldman 2-form omega = dx^dy/(2z - xy) preservation mod M=0
    dz_dx = -(2 * x - y * z) / (2 * z - x * y)
    dz_dy = -(2 * y - x * z) / (2 * z - x * y)

    def goldman_sign(f):
        X, Y, Z = f
        dXdx = sp.diff(X, x) + sp.diff(X, z) * dz_dx
        dXdy = sp.diff(X, y) + sp.diff(X, z) * dz_dy
        dYdx = sp.diff(Y, x) + sp.diff(Y, z) * dz_dx
        dYdy = sp.diff(Y, y) + sp.diff(Y, z) * dz_dy
        ratio = sp.together((dXdx * dYdy - dXdy * dYdx) * (2 * z - x * y) / (2 * Z - X * Y))
        num, den = sp.fraction(ratio)
        for sgn in (1, -1):
            if sp.rem(sp.expand(num - sgn * den), M_poly, z) == 0:
                return sgn
        raise RuntimeError("Goldman sign failed")

    goldman_signs = {
        "L": goldman_sign(L_sym),
        "R": goldman_sign(R_sym),
        "C": goldman_sign(C_sym),
        "sigma": goldman_sign(S_sym),
        "tau": goldman_sign(tau_sym),
    }

    # 3. Full-orbit PC-sifter through mod 729 (52,488 pts) using <L, R>-derived Schreier generators!
    O729 = markoff_orbit_LR(729)
    N729 = len(O729)
    idx729 = {v: i for i, v in enumerate(O729)}
    gens_fn = {"L": apply_L, "R": apply_R, "l": apply_Li, "r": apply_Ri}
    inv_ch = {"L": "l", "l": "L", "R": "r", "r": "R"}

    def inv_w(w):
        return tuple(inv_ch[c] for c in reversed(w))

    p729 = {k: [idx729[fn(v, 729)] for v in O729] for k, fn in gens_fn.items()}

    def comp729(a, b):
        return [a[i] for i in b]

    def word_p729(w):
        cur = list(range(N729))
        for ch in reversed(w):
            gen = p729[ch]
            cur = [gen[i] for i in cur]
        return cur

    # Also verify numerical V_4-rigidity across ALL 52,488 pts of O_729 for all 25 Schreier generators!
    v4_p729 = [
        [idx729[(s[0] * v[0] % 729, s[1] * v[1] % 729, s[2] * v[2] % 729)] for v in O729]
        for s in V4[1:]
    ]
    gen729 = []
    v4_rigid_729 = True
    for w in schreier_words:
        pw = word_p729(w)
        pwi = word_p729(inv_w(w))
        for pv4 in v4_p729:
            if comp729(pv4, pw) != comp729(pw, pv4):
                v4_rigid_729 = False
        gen729.append((pw, pwi))

    X729 = [v[0] for v in O729]
    Y729 = [v[1] for v in O729]
    Z729 = [v[2] for v in O729]
    MODS729 = {3: (27, 9), 4: (81, 27), 5: (243, 81), 6: (729, 243)}

    def get_diff729(p, i, c, mod_r, div_r):
        j = p[i]
        if c == 0:
            return ((X729[j] - X729[i]) % mod_r) // div_r
        if c == 1:
            return ((Y729[j] - Y729[i]) % mod_r) // div_r
        return ((Z729[j] - Z729[i]) % mod_r) // div_r

    ech729 = {r: [] for r in (3, 4, 5, 6)}
    basis729 = []
    work729 = deque(gen729)

    def sift729(p, pi):
        for r in (3, 4, 5, 6):
            mod_r, div_r = MODS729[r]
            for piv_i, piv_c, bp, bpi in ech729[r]:
                val = get_diff729(p, piv_i, piv_c, mod_r, div_r)
                if val == 1:
                    p = comp729(bpi, p)
                    pi = comp729(pi, bp)
                elif val == 2:
                    p = comp729(bp, p)
                    pi = comp729(pi, bpi)
            for i in range(N729):
                j = p[i]
                dx = (X729[j] - X729[i]) % mod_r
                if dx:
                    return r, i, 0, dx // div_r, p, pi
                dy = (Y729[j] - Y729[i]) % mod_r
                if dy:
                    return r, i, 1, dy // div_r, p, pi
                dz = (Z729[j] - Z729[i]) % mod_r
                if dz:
                    return r, i, 2, dz // div_r, p, pi
        return None

    while work729:
        p, pi = work729.popleft()
        res = sift729(p, pi)
        if res is None:
            continue
        r, piv_i, piv_c, val, p, pi = res
        if val == 2:
            p, pi = pi, p
        ech729[r].append((piv_i, piv_c, p, pi))
        if r < 6:
            p2 = comp729(p, p)
            pi2 = comp729(pi, pi)
            work729.append((comp729(p2, p), comp729(pi2, pi)))
            for _, bp, bpi in basis729:
                ab = comp729(p, bp)
                bi_ai = comp729(bpi, pi)
                ai_bi = comp729(pi, bpi)
                ba = comp729(bp, p)
                work729.append((comp729(ai_bi, ab), comp729(bi_ai, ba)))
        basis729.append((r, p, pi))

    full_orbit_dims_3_to_6 = [len(ech729[r]) for r in (3, 4, 5, 6)]

    # 4. Disjoint 2-half falling-factorial polynomial engine through mod 19,683 (k = 9)!
    ff_k9 = run_falling_factorial_engine(9, schreier_words, tree, p9, single_half_plus_only=False)

    elapsed_ms = (time.perf_counter_ns() - t0) // 1000000
    return {
        "elapsed_ms": elapsed_ms,
        "symbolic_V4_and_Goldman": {
            "V4_normalizes_L_over_Zxyz": v4_normalizes_L,
            "V4_normalizes_R_over_Zxyz": v4_normalizes_R,
            "short_gamma4_words_checked_symbolically": len(short_gamma4_words),
            "V4_commutes_symbolically_with_gamma4_words": sym_v4_comm_ok,
            "goldman_2form_signs": goldman_signs,
        },
        "gamma4_schreier_LR_generator_count": len(schreier_words),
        "full_orbit_mod729": {
            "orbit_size": N729,
            "V4_rigidity_all_52488_pts": v4_rigid_729,
            "dims_d3_to_d6": full_orbit_dims_3_to_6,
        },
        "falling_factorial_2half_mod19683": ff_k9,
        "full_orbit_matches_2half_d3_to_d6": bool(full_orbit_dims_3_to_6 == ff_k9["dims"][:4]),
    }, (schreier_words, tree, p9)


# ---------------------------------------------------------------------------
# MODULE L3: Mirror Lock, Chiral-Flux Master Law (dps=55), C60 J_k & mod 135
# ---------------------------------------------------------------------------

def herm_eigvals_via_realsplit_eigsy(H):
    """
    Disjoint Hermitian eigensolver using 2d x 2d real-split symmetric matrix
    [[Re(H), -Im(H)], [Im(H), Re(H)]] via mp.eigsy (NEVER mp.eighe!).
    Every real eigenvalue of H appears with exact multiplicity 2 in the 2d x 2d
    real-split spectrum; verifies pair-matching and returns sorted d eigenvalues.
    """
    d = H.rows
    R = mp.matrix(2 * d, 2 * d)
    for i in range(d):
        for j in range(d):
            val = H[i, j]
            re_v = val.real if isinstance(val, mp.mpc) else val
            im_v = val.imag if isinstance(val, mp.mpc) else mp.mpf(0)
            R[i, j] = re_v
            R[i + d, j + d] = re_v
            R[i, j + d] = -im_v
            R[i + d, j] = im_v
    evals, _ = mp.eigsy(R)
    evals_sorted = sorted(list(evals))
    out = []
    max_pair_gap = mp.mpf(0)
    for i in range(0, 2 * d, 2):
        gap = abs(evals_sorted[i + 1] - evals_sorted[i])
        if gap > max_pair_gap:
            max_pair_gap = gap
        out.append((evals_sorted[i] + evals_sorted[i + 1]) / mp.mpf(2))
    return out, max_pair_gap


def build_chiral_sector_blocks_mp(pts, m_mod, q_val, alpha, beta):
    """
    Build exact orthonormal-basis sector matrices Pi_q W(alpha, beta) Pi_q and
    Pi_q P_sigma Pi_q at dps=55.
    """
    fix_o, cyc_o = get_c_orbits(pts, m_mod)
    w_mp = mp.exp(mp.mpc(0, 2) * mp.pi / mp.mpf(3))
    wq = w_mp**q_val
    wq_conj = mp.conj(wq)
    sqrt3 = mp.sqrt(mp.mpf(3))
    inv_sqrt3 = mp.mpf(1) / sqrt3
    inv3 = mp.mpf(1) / mp.mpf(3)

    # Orthonormal basis of Pi_q:
    # - if q==0: e_v (for v in fix_o), and (1/sqrt(3)) sum_{r=0}^2 e_{C^r v} (for cyc in cyc_o)
    # - if q!=0: (1/sqrt(3)) sum_{r=0}^2 w^{-q r} e_{C^r v} (for cyc in cyc_o)
    orb_map = {}
    dim = 0
    if q_val == 0:
        for v in fix_o:
            orb_map[v] = (dim, 0, True)
            dim += 1
    for cyc in cyc_o:
        for r, v in enumerate(cyc):
            orb_map[v] = (dim, r, False)
        dim += 1

    # Helper to accumulate matrix element <u_j | P_g | u_i> for a permutation g
    # W(alpha, beta) = alpha * (C S + C^2 S C^2 + S C) + beta * (S C^2 + C S C + C^2 S)
    def add_move(mat, coef, move_fn):
        for i in range(dim):
            if q_val == 0 and i < len(fix_o):
                v = fix_o[i]
                y = move_fn(v)
                if y in orb_map:
                    j, pos, is_fix = orb_map[y]
                    c_out = mp.mpf(1) if is_fix else (inv_sqrt3 * (wq**pos))
                    mat[j, i] += coef * c_out
            else:
                cyc = cyc_o[i - (len(fix_o) if q_val == 0 else 0)]
                for r, v in enumerate(cyc):
                    y = move_fn(v)
                    if y in orb_map:
                        j, pos, is_fix = orb_map[y]
                        c_in = inv_sqrt3 * (wq_conj**r)
                        c_out = mp.mpf(1) if is_fix else (inv_sqrt3 * (wq**pos))
                        mat[j, i] += coef * c_in * c_out

    Psig = mp.matrix(dim, dim)
    add_move(Psig, mp.mpf(1), lambda v: apply_S(v, m_mod))

    Wmat = mp.matrix(dim, dim)
    # A_+ moves
    add_move(Wmat, alpha, lambda v: apply_C(apply_S(v, m_mod), m_mod))
    add_move(Wmat, alpha, lambda v: apply_C(apply_C(apply_S(apply_C(apply_C(v, m_mod), m_mod), m_mod), m_mod), m_mod))
    add_move(Wmat, alpha, lambda v: apply_S(apply_C(v, m_mod), m_mod))
    # A_- moves
    add_move(Wmat, beta, lambda v: apply_S(apply_C(apply_C(v, m_mod), m_mod), m_mod))
    add_move(Wmat, beta, lambda v: apply_C(apply_S(apply_C(v, m_mod), m_mod), m_mod))
    add_move(Wmat, beta, lambda v: apply_C(apply_C(apply_S(v, m_mod), m_mod), m_mod))

    return Wmat, Psig, dim


def o81_z4_exact_psig_spectrum(O81):
    """
    General exact joint-(C, Z_4) orthonormal basis decomposition on O_81^+ and O_81^-
    (handling all stabilizer types in <C> x <Z_4> without assumptions!), solving each
    small Hermitian block B^H B via 2d x 2d real-split mp.eigsy at dps=55.
    """
    m = 81
    w_mp = mp.exp(mp.mpc(0, 2) * mp.pi / mp.mpf(3))

    def apply_Z4(v):
        return tuple((v[i] + 27 * sgn9(v[i])) % m for i in range(3))

    z4_comm_C = all(apply_Z4(apply_C(v, m)) == apply_C(apply_Z4(v), m) for v in O81)
    z4_comm_S = all(apply_Z4(apply_S(v, m)) == apply_S(apply_Z4(v), m) for v in O81)
    assert z4_comm_C and z4_comm_S

    Op = [v for v in O81 if eps3(v) == 1]
    Om = [v for v in O81 if eps3(v) == 2]

    def build_joint_basis(pts, q_val, z_val):
        # Partition pts into <C, Z_4> orbits; on each orbit, project e_{v0} onto (C=w^q, Z_4=w^z)
        seen = set()
        basis = []  # list of dicts {pt: coeff} (orthonormal!)
        pt_to_basis = {}  # pt -> (basis_idx, coeff)
        for v in pts:
            if v in seen:
                continue
            orb = set()
            q_bfs = deque([v])
            orb.add(v)
            while q_bfs:
                u = q_bfs.popleft()
                for nxt in (apply_C(u, m), apply_Z4(u)):
                    if nxt not in orb:
                        orb.add(nxt)
                        q_bfs.append(nxt)
            seen.update(orb)
            # Project e_v using (1/9) sum_{r,s=0}^2 w^{-q*r - z*s} C^r Z_4^s e_v
            vec = {}
            cur_c = v
            for r in range(3):
                cur_z = cur_c
                for s in range(3):
                    phase = w_mp ** ((-q_val * r - z_val * s) % 3)
                    vec[cur_z] = vec.get(cur_z, mp.mpc(0)) + phase
                    cur_z = apply_Z4(cur_z)
                cur_c = apply_C(cur_c, m)
            norm2 = sum(abs(val) ** 2 for val in vec.values())
            if norm2 > mp.mpf(1) / mp.mpf(10)**20:
                inv_norm = mp.mpf(1) / mp.sqrt(norm2)
                b_idx = len(basis)
                norm_vec = {pt: val * inv_norm for pt, val in vec.items()}
                basis.append(norm_vec)
                for pt, val in norm_vec.items():
                    pt_to_basis[pt] = (b_idx, val)
        return basis, pt_to_basis

    specs = {}
    max_pair_gap_all = mp.mpf(0)
    for q_val in (0, 1, 2):
        all_evals = []
        for z_val in (0, 1, 2):
            bp, p_map = build_joint_basis(Op, q_val, z_val)
            bm, m_map = build_joint_basis(Om, q_val, z_val)
            np_d = len(bp)
            nm_d = len(bm)
            # Build T (nm_d x np_d): T[j, i] = <bm_j | P_S | bp_i>
            T = mp.matrix(nm_d, np_d)
            for i, vec_i in enumerate(bp):
                for pt, ci in vec_i.items():
                    img = apply_S(pt, m)
                    if img in m_map:
                        j, cj = m_map[img]
                        T[j, i] += mp.conj(cj) * ci
            # Singular values of T via smaller of T^\dagger T or T T^\dagger using 2d x 2d real-split mp.eigsy!
            if np_d <= nm_d:
                G = T.H * T
                extra_zeros = nm_d - np_d
            else:
                G = T * T.H
                extra_zeros = np_d - nm_d
            g_evals, pgap = herm_eigvals_via_realsplit_eigsy(G)
            if pgap > max_pair_gap_all:
                max_pair_gap_all = pgap
            for ev in g_evals:
                sv = mp.sqrt(ev) if ev > mp.mpf(0) else mp.mpf(0)
                all_evals.append(sv)
                all_evals.append(-sv)
            for _ in range(extra_zeros):
                all_evals.append(mp.mpf(0))
        all_evals.sort()
        specs[q_val] = all_evals
    assert len(specs[0]) == 218 and len(specs[1]) == 215 and len(specs[2]) == 215
    return specs, z4_comm_C, z4_comm_S, max_pair_gap_all


def run_L3():
    t0 = time.perf_counter_ns()
    x, y, z = sp.symbols("x y z")
    C_sym = (z, x, y)
    S_sym = (y, x, x * y - z)
    tau_sym = (y, x, z)

    def comp_sym(f, g):
        gx, gy, gz = g
        return tuple(sp.expand(e.subs({x: gx, y: gy, z: gz}, simultaneous=True)) for e in f)

    def det_jac(f):
        J = sp.Matrix([[sp.diff(e, var) for var in (x, y, z)] for e in f])
        return int(sp.expand(J.det()))

    tau_C_tau = comp_sym(tau_sym, comp_sym(C_sym, tau_sym))
    Cinv_sym = (y, z, x)
    tau_S_tau = comp_sym(tau_sym, comp_sym(S_sym, tau_sym))

    # Explicit mirror check on O_27 and O_81: tau not in G_3, not in G_4, |<G_3, tau>| = 432
    O27 = markoff_orbit_LR(27)
    O81 = markoff_orbit_LR(81)
    idx27 = {v: i for i, v in enumerate(O27)}
    idx81 = {v: i for i, v in enumerate(O81)}
    pL27 = tuple(idx27[apply_L(v, 27)] for v in O27)
    pR27 = tuple(idx27[apply_R(v, 27)] for v in O27)
    ptau27 = tuple(idx27[apply_tau(v, 27)] for v in O27)

    id27 = tuple(range(len(O27)))
    G3_set = {id27}
    q = deque([id27])
    while q:
        g = q.popleft()
        for gen in (pL27, pR27):
            ng = comp_perm(gen, g)
            if ng not in G3_set:
                G3_set.add(ng)
                q.append(ng)
    tau_not_in_G3 = bool(ptau27 not in G3_set)
    G3_tau_set = set(G3_set)
    for g in G3_set:
        G3_tau_set.add(comp_perm(ptau27, g))
    # Verify G3_tau is closed under <L, R, tau>
    assert all(comp_perm(gen, g) in G3_tau_set for g in G3_tau_set for gen in (pL27, pR27, ptau27))

    pL81 = tuple(idx81[apply_L(v, 81)] for v in O81)
    pR81 = tuple(idx81[apply_R(v, 81)] for v in O81)
    ptau81 = tuple(idx81[apply_tau(v, 81)] for v in O81)
    id81 = tuple(range(len(O81)))
    G4_set = {id81}
    q81 = deque([id81])
    while q81:
        g = q81.popleft()
        for gen in (pL81, pR81):
            ng = comp_perm(gen, g)
            if ng not in G4_set:
                G4_set.add(ng)
                q81.append(ng)
    tau_not_in_G4 = bool(ptau81 not in G4_set)

    mirror_lock = {
        "det_dC": det_jac(C_sym),
        "det_dS": det_jac(S_sym),
        "det_dtau": det_jac(tau_sym),
        "tau_C_tau_eq_Cinv": bool(tau_C_tau == Cinv_sym),
        "tau_S_tau_eq_S": bool(tau_S_tau == S_sym),
        "tau_not_in_G3": tau_not_in_G3,
        "tau_not_in_G4": tau_not_in_G4,
        "order_G3_tau": len(G3_tau_set),
        "order_G3_tau_eq_2_G3": bool(len(G3_tau_set) == 2 * len(G3_set)),
        "abelianization_G_tau_Z2xZ2_proved": bool(tau_C_tau == Cinv_sym and tau_S_tau == S_sym),
    }

    # Chiral-flux master law at dps=55 on O_27 and O_81!
    w_mp = mp.exp(mp.mpc(0, 2) * mp.pi / mp.mpf(3))
    flux_cases = [
        ("sym_1_1", mp.mpf(1), mp.mpf(1), True, None),
        ("real_2_1", mp.mpf(2), mp.mpf(1), False, None),
        ("herm_pi_3", mp.exp(mp.mpc(0, 1) * mp.pi / mp.mpf(3)), mp.exp(mp.mpc(0, -1) * mp.pi / mp.mpf(3)), True, mp.pi / mp.mpf(3)),
        ("herm_pi_2", mp.exp(mp.mpc(0, 1) * mp.pi / mp.mpf(2)), mp.exp(mp.mpc(0, -1) * mp.pi / mp.mpf(2)), True, mp.pi / mp.mpf(2)),
        ("herm_pi_9", mp.exp(mp.mpc(0, 1) * mp.pi / mp.mpf(9)), mp.exp(mp.mpc(0, -1) * mp.pi / mp.mpf(9)), True, mp.pi / mp.mpf(9)),
    ]

    # O_27 full unblocked 2d x 2d real-split mp.eigsy spectra + master law!
    o27_results = {}
    o27_max_master_res = mp.mpf(0)
    o27_max_eig_res = mp.mpf(0)
    o27_max_pair_gap = mp.mpf(0)
    o27_psig_specs = {}
    for q_val in (0, 1, 2):
        _, Psig_q, _ = build_chiral_sector_blocks_mp(O27, 27, q_val, mp.mpf(1), mp.mpf(1))
        ev_p, pg = herm_eigvals_via_realsplit_eigsy(Psig_q)
        o27_psig_specs[q_val] = ev_p
        if pg > o27_max_pair_gap:
            o27_max_pair_gap = pg

    for fname, alpha, beta, is_herm, theta in flux_cases:
        f_info = {"is_hermitian": is_herm, "c_q": {}, "master_law_max_res": {}, "max_abs_eig": {}}
        specs_q = {}
        for q_val in (0, 1, 2):
            W_q, Psig_q, d_q = build_chiral_sector_blocks_mp(O27, 27, q_val, alpha, beta)
            c_q = mp.mpf(3) * (alpha * (w_mp**q_val) + beta * (w_mp ** ((-q_val) % 3)))
            if theta is not None:
                c_cos = mp.mpf(6) * mp.cos(theta + mp.mpf(2) * mp.pi * mp.mpf(q_val) / mp.mpf(3))
                assert abs(c_q - c_cos) < mp.mpf(1) / mp.mpf(10)**48
            diff = W_q - c_q * Psig_q
            mres = max(abs(diff[i, j]) for i in range(d_q) for j in range(d_q))
            if mres > o27_max_master_res:
                o27_max_master_res = mres
            f_info["c_q"][str(q_val)] = mp_str(c_q, 25)
            f_info["master_law_max_res"][str(q_val)] = mp_str(mres, 15)
            if is_herm:
                ev_w, pg = herm_eigvals_via_realsplit_eigsy(W_q)
                if pg > o27_max_pair_gap:
                    o27_max_pair_gap = pg
                pred = sorted([c_q.real * ev for ev in o27_psig_specs[q_val]])
                eres = max(abs(a - b) for a, b in zip(ev_w, pred))
                if eres > o27_max_eig_res:
                    o27_max_eig_res = eres
                specs_q[q_val] = ev_w
                f_info["max_abs_eig"][str(q_val)] = mp_str(max(abs(ev) for ev in ev_w), 25)
            else:
                ev_w, _ = mp.eig(W_q)
                mags_w = sorted([abs(ev) for ev in ev_w])
                mags_pred = sorted([abs(c_q) * abs(ev) for ev in o27_psig_specs[q_val]])
                eres = max(abs(a - b) for a, b in zip(mags_w, mags_pred))
                if eres > o27_max_eig_res:
                    o27_max_eig_res = eres
                specs_q[q_val] = mags_w
                f_info["max_abs_eig"][str(q_val)] = mp_str(max(mags_w), 25)
        if fname == "real_2_1":
            f_info["spec1_minus_spec2_mag_diff"] = mp_str(
                max(abs(a - b) for a, b in zip(specs_q[1], specs_q[2])), 15
            )
        if fname == "herm_pi_9":
            m0 = max(abs(ev) for ev in specs_q[0])
            m1 = max(abs(ev) for ev in specs_q[1])
            m2 = max(abs(ev) for ev in specs_q[2])
            f_info["distinct_3_way_split_gaps"] = {
                "abs_m0_minus_m1": mp_str(abs(m0 - m1), 20),
                "abs_m1_minus_m2": mp_str(abs(m1 - m2), 20),
                "abs_m0_minus_m2": mp_str(abs(m0 - m2), 20),
            }
            f_info["unlocks_3_to_1_1_1"] = bool(
                abs(m0 - m1) > mp.mpf(1) / mp.mpf(2)
                and abs(m1 - m2) > mp.mpf(1) / mp.mpf(2)
                and abs(m0 - m2) > mp.mpf(1)
            )
        o27_results[fname] = f_info

    # Guardrail 3: Mandatory Unitary Basis-Scrambling Test on Pi_1 of O_27 at theta = pi/9!
    W1_pi9, _, d1_27 = build_chiral_sector_blocks_mp(
        O27, 27, 1,
        mp.exp(mp.mpc(0, 1) * mp.pi / mp.mpf(9)),
        mp.exp(mp.mpc(0, -1) * mp.pi / mp.mpf(9)),
    )
    ev_orig, _ = herm_eigvals_via_realsplit_eigsy(W1_pi9)
    # Build deterministic non-trivial unitary U via modified Gram-Schmidt on integer-complex matrix
    rng_u = random.Random(2026112603)
    U_cols = []
    for _ in range(d1_27):
        col = [mp.mpc(rng_u.randint(-7, 7), rng_u.randint(-7, 7)) for _ in range(d1_27)]
        for prev in U_cols:
            dot = sum(mp.conj(prev[i]) * col[i] for i in range(d1_27))
            col = [col[i] - dot * prev[i] for i in range(d1_27)]
        norm = mp.sqrt(sum(abs(c) ** 2 for c in col))
        U_cols.append([c / norm for c in col])
    U_mat = mp.matrix(d1_27, d1_27)
    for j in range(d1_27):
        for i in range(d1_27):
            U_mat[i, j] = U_cols[j][i]
    unitarity_err = max(abs((U_mat.H * U_mat - mp.eye(d1_27))[i, j]) for i in range(d1_27) for j in range(d1_27))
    W1_scram = U_mat * W1_pi9 * U_mat.H
    ev_scram, _ = herm_eigvals_via_realsplit_eigsy(W1_scram)
    scram_inv_err = max(abs(a - b) for a, b in zip(ev_orig, ev_scram))

    # O_81: verify entry-by-entry master law on FULL 218x218 and 215x215 blocks + full spectra via Z_4 real-split eigsy!
    o81_max_master_res = mp.mpf(0)
    o81_master_by_flux = {}
    for fname, alpha, beta, is_herm, theta in flux_cases:
        max_f = mp.mpf(0)
        for q_val in (0, 1, 2):
            W_q, Psig_q, d_q = build_chiral_sector_blocks_mp(O81, 81, q_val, alpha, beta)
            c_q = mp.mpf(3) * (alpha * (w_mp**q_val) + beta * (w_mp ** ((-q_val) % 3)))
            diff = W_q - c_q * Psig_q
            mres = max(abs(diff[i, j]) for i in range(d_q) for j in range(d_q))
            if mres > max_f:
                max_f = mres
            if mres > o81_max_master_res:
                o81_max_master_res = mres
        o81_master_by_flux[fname] = mp_str(max_f, 15)

    o81_psig_specs, z4_c, z4_s, o81_pair_gap = o81_z4_exact_psig_spectrum(O81)
    # Check exact O_81 spectrum match for all fluxes + RPF5 real (2,1) + pi/9 3->1+1+1 split
    c1_real21 = mp.mpf(3) * (mp.mpf(2) * w_mp + w_mp**2)
    c2_real21 = mp.mpf(3) * (mp.mpf(2) * (w_mp**2) + w_mp)
    o81_real21_spec1 = sorted([abs(c1_real21) * abs(ev) for ev in o81_psig_specs[1]])
    o81_real21_spec2 = sorted([abs(c2_real21) * abs(ev) for ev in o81_psig_specs[2]])
    o81_real21_mag_diff = max(abs(a - b) for a, b in zip(o81_real21_spec1, o81_real21_spec2))
    # Verify Pi_1 and Pi_2 of O_81 have identical Psig spectrum (conjugate!)
    o81_q1_q2_psig_diff = max(abs(a - b) for a, b in zip(o81_psig_specs[1], o81_psig_specs[2]))

    o81_pi9_max = {}
    for q_val in (0, 1, 2):
        cq = mp.mpf(6) * mp.cos(mp.pi / mp.mpf(9) + mp.mpf(2) * mp.pi * mp.mpf(q_val) / mp.mpf(3))
        o81_pi9_max[str(q_val)] = mp_str(abs(cq) * max(abs(ev) for ev in o81_psig_specs[q_val]), 25)

    # C60 Weyl-Heisenberg intertwiner J_k on O_81^-, O_243^-, O_729^- (26,244 pts)!
    c60_Jk_results = {}
    for k in (4, 5, 6):
        m_k = 3**k
        sh = m_k // 3
        Ok = O81 if k == 4 else markoff_orbit_LR(m_k)
        Om_k = set(v for v in Ok if eps3(v) == 2)

        def J_k(v):
            vx, vy, vz = v
            return (vx % m_k, (vy * (1 + m_k // 9)) % m_k, (vz * (1 - m_k // 9)) % m_k)

        img_ok = 0
        heis_ok = 0
        order3_ok = 0
        vieta2_comm_ok = 0
        for v in Om_k:
            jv = J_k(v)
            if jv in Om_k:
                img_ok += 1
            if J_k(J_k(jv)) == v:
                order3_ok += 1
            # Check J_k(C(v)) - C(J_k(v)) == +3^{k-1} * sgn9(C(v)) mod 3^k (= central Z_k shift)
            cv = apply_C(v, m_k)
            a_pt = J_k(cv)
            b_pt = apply_C(jv, m_k)
            norm_diff = tuple(((a_pt[i] - b_pt[i]) * sgn9(cv[i])) % m_k for i in range(3))
            if norm_diff == (sh, sh, sh):
                heis_ok += 1
            # Check [J_k, V_Vieta3^2] = 0 explicitly via the 9 two-step Vieta neighbors!
            s1 = Counter(
                J_k(f1(f2(v, m_k), m_k))
                for f1 in (apply_V1, apply_V2, apply_V3)
                for f2 in (apply_V1, apply_V2, apply_V3)
            )
            s2 = Counter(
                f1(f2(jv, m_k), m_k)
                for f1 in (apply_V1, apply_V2, apply_V3)
                for f2 in (apply_V1, apply_V2, apply_V3)
            )
            if s1 == s2:
                vieta2_comm_ok += 1
        c60_Jk_results[f"O_{m_k}_minus"] = {
            "points": len(Om_k),
            "J_k_preserves_O_minus": img_ok,
            "J_k_order3": order3_ok,
            "J_k_C_commutator_eq_Zk": heis_ok,
            "J_k_commutes_V_Vieta3_sq": vieta2_comm_ok,
            "all_100pct_pass": bool(
                img_ok == len(Om_k)
                and order3_ok == len(Om_k)
                and heis_ok == len(Om_k)
                and vieta2_comm_ok == len(Om_k)
            ),
        }

    # mod 135 = 27 * 5 counterexample over TWO distinct primes p > 2*10^9 using disjoint Krylov-Frobenius!
    O135 = markoff_orbit_LR(135)
    O27_loc = O27
    O5 = markoff_orbit_LR(5)
    fixC135 = [v for v in O135 if apply_C(v, 135) == v]
    wit_cs = "CSCSCSCCS"
    wit_lr = cs_to_lr(wit_cs)
    wit_f27 = sum(1 for v in O27_loc if apply_word_LR(wit_lr, v, 27) == v)
    wit_f5 = sum(1 for v in O5 if apply_word_LR(wit_lr, v, 5) == v)
    wit_f135 = sum(1 for v in O135 if apply_word_LR(wit_lr, v, 135) == v)
    wit_rho3 = sum(2 if c == "L" else (1 if c == "R" else (1 if c == "l" else 2)) for c in wit_lr) % 3

    Op135 = [v for v in O135 if eps3(v) == 1]
    Om135 = [v for v in O135 if eps3(v) == 2]
    fp135, cp135 = get_c_orbits(Op135, 135)
    fm135, cm135 = get_c_orbits(Om135, 135)
    d135_neu = len(fp135) + len(cp135) + len(fm135) + len(cm135)  # 962
    d135_ch = len(cp135) + len(cm135)                             # 959

    primes135 = get_primes_1mod3(2000000000, 2)
    unpaired_p0_signed_by_p = []
    unpaired_p1_signed_by_p = []
    gcd_degs_135 = []
    for pr in primes135:
        wp = primitive_cube_root_mod_p(pr)
        B0, np0, nm0 = build_bipartite_B_mod_p(fp135, cp135, fm135, cm135, 0, apply_S, 135, pr, wp)
        B1, np1, nm1 = build_bipartite_B_mod_p(fp135, cp135, fm135, cm135, 1, apply_S, 135, pr, wp)
        assert np0 == 482 and nm0 == 480 and np1 == 479 and nm1 == 480
        p0 = charpoly_krylov_mod_p(B0, pr)
        p1 = charpoly_krylov_mod_p(B1, pr)
        g = poly_gcd_mod_p(p0, p1, pr)
        u0, r0 = poly_divmod_mod_p(p0, g, pr)
        u1, r1 = poly_divmod_mod_p(p1, g, pr)
        assert r0 == [0] and r1 == [0]
        gcd_degs_135.append(len(g) - 1)
        unpaired_p0_signed_by_p.append([c if c <= pr // 2 else c - pr for c in u0])
        unpaired_p1_signed_by_p.append([c if c <= pr // 2 else c - pr for c in u1])

    assert unpaired_p0_signed_by_p[0] == unpaired_p0_signed_by_p[1]
    assert unpaired_p1_signed_by_p[0] == unpaired_p1_signed_by_p[1]
    assert gcd_degs_135[0] == gcd_degs_135[1]

    # Exact paired & unpaired mode accounting on full O_135 (Op + Om):
    # M_0(x) = B_0(x^2)/x^2, M_1(x) = x * B_1(x^2), so gcd(M_0, M_1) has deg 2*deg(gcd_y) + 1 = 2*474 + 1 = 949!
    paired_modes_135 = 2 * gcd_degs_135[0] + 1
    y_sym = sp.Symbol("y")
    x_sym = sp.Symbol("x")
    u1_y = sum(c * y_sym ** (len(unpaired_p1_signed_by_p[0]) - 1 - i) for i, c in enumerate(unpaired_p1_signed_by_p[0]))
    u0_y = sum(c * y_sym ** (len(unpaired_p0_signed_by_p[0]) - 1 - i) for i, c in enumerate(unpaired_p0_signed_by_p[0]))
    Q10_expected = sp.expand((x_sym**2 - 2 * x_sym - 2) * (x_sym**2 + 2 * x_sym - 2) * (x_sym**3 - 3 * x_sym - 1) * (x_sym**3 - 3 * x_sym + 1))
    u1_x = sp.expand(u1_y.subs(y_sym, x_sym**2))
    Q10_exact_match = bool(sp.expand(u1_x - Q10_expected) == 0)

    # Extract P10(x) from u0_y / (y^2 * (y - 9))!
    P10_y_expr, rem_p10 = sp.div(u0_y, y_sym**2 * (y_sym - 9), y_sym)
    assert rem_p10 == 0
    P10_x_expr = sp.expand(P10_y_expr.subs(y_sym, x_sym**2))

    # Exact integer trace-moment check for r = 1..12 via BOTH:
    # (a) Newton power sums of P10 and Q10, and
    # (b) Direct sparse exact integer walks on the 2,880-vertex O_135 graph for r=1..6!
    s_Q10_1_12 = newton_power_sums_from_poly([int(c) for c in sp.Poly(Q10_expected, x_sym).all_coeffs()], 12)
    s_P10_1_12 = newton_power_sums_from_poly([int(c) for c in sp.Poly(P10_x_expr, x_sym).all_coeffs()], 12)
    s_diff_P10_minus_Q10 = [a - b for a, b in zip(s_P10_1_12, s_Q10_1_12)]

    # Direct exact integer sparse walks on O_135 (2,880 pts) for r=1..6!
    idx135 = {v: i for i, v in enumerate(O135)}
    pC135 = [idx135[apply_C(v, 135)] for v in O135]

    def mv_A135(v):
        c1 = apply_C(v, 135)
        c2 = apply_C(c1, 135)
        return [
            apply_C(apply_S(v, 135), 135),
            apply_C(apply_C(apply_S(c2, 135), 135), 135),
            apply_S(c1, 135),
            apply_S(c2, 135),
            apply_C(apply_S(c1, 135), 135),
            apply_C(apply_C(apply_S(v, 135), 135), 135),
        ]

    adj135 = [Counter(idx135[u] for u in mv_A135(v)) for v in O135]
    t_all = [0] * 7
    t_C = [0] * 7
    for j in range(len(O135)):
        v1 = adj135[j]
        v2 = Counter()
        for k_i, c in v1.items():
            for nb, m2 in adj135[k_i].items():
                v2[nb] += c * m2
        v3 = Counter()
        for k_i, c in v2.items():
            for nb, m2 in adj135[k_i].items():
                v3[nb] += c * m2
        cj = pC135[j]
        t_all[1] += v1.get(j, 0)
        t_C[1] += v1.get(cj, 0)
        t_all[2] += v2.get(j, 0)
        t_C[2] += v2.get(cj, 0)
        t_all[3] += v3.get(j, 0)
        t_C[3] += v3.get(cj, 0)
        t_all[4] += sum(c * c for c in v2.values())
        t_C[4] += sum(c * v2.get(pC135[k_i], 0) for k_i, c in v2.items())
        t_all[5] += sum(c * v3.get(k_i, 0) for k_i, c in v2.items())
        t_C[5] += sum(c * v3.get(pC135[k_i], 0) for k_i, c in v2.items())
        t_all[6] += sum(c * c for c in v3.values())
        t_C[6] += sum(c * v3.get(pC135[k_i], 0) for k_i, c in v3.items())

    direct_trace_diffs_1_6 = []
    for r in range(1, 7):
        tr_neu = (t_all[r] + 2 * t_C[r]) // 3
        tr_ch = (t_all[r] - t_C[r]) // 3
        num = tr_neu - (6**r + (-6)**r)
        assert num % (2**r) == 0
        direct_trace_diffs_1_6.append(num // (2**r) - tr_ch)

    assert direct_trace_diffs_1_6 == s_diff_P10_minus_Q10[:6]

    elapsed_ms = (time.perf_counter_ns() - t0) // 1000000
    return {
        "elapsed_ms": elapsed_ms,
        "mirror_lock": mirror_lock,
        "chiral_flux_dps55": {
            "dps": DPS,
            "eigensolver": "2d_x_2d_real_split_mp_eigsy",
            "O_27": {
                "max_master_law_residual": mp_str(o27_max_master_res, 15),
                "max_eig_vs_master_residual": mp_str(o27_max_eig_res, 15),
                "max_realsplit_pair_gap": mp_str(o27_max_pair_gap, 15),
                "fluxes": o27_results,
            },
            "guardrail3_unitary_scrambling_O27_pi9_q1": {
                "unitarity_error": mp_str(unitarity_err, 15),
                "eigenvalue_invariance_error": mp_str(scram_inv_err, 15),
                "passed_lt_1e_45": bool(scram_inv_err < mp.mpf(1) / mp.mpf(10)**45),
            },
            "O_81": {
                "Z4_commutes_C": z4_c,
                "Z4_commutes_S": z4_s,
                "max_master_law_residual": mp_str(o81_max_master_res, 15),
                "master_law_by_flux": o81_master_by_flux,
                "max_realsplit_pair_gap": mp_str(o81_pair_gap, 15),
                "q1_vs_q2_Psig_spec_diff": mp_str(o81_q1_q2_psig_diff, 15),
                "real_2_1_spec1_minus_spec2_mag_diff": mp_str(o81_real21_mag_diff, 15),
                "herm_pi_9_max_abs_eig": o81_pi9_max,
            },
        },
        "C60_Weyl_Heisenberg_intertwiner_Jk": {
            "formula": "J_k(x,y,z) = (x, (1 + 3^{k-2})*y, (1 - 3^{k-2})*z) mod 3^k",
            "levels": c60_Jk_results,
        },
        "mod135_counterexample": {
            "orbit_size": len(O135),
            "O_27_x_O_5_size": len(O27_loc) * len(O5),
            "Fix_C_count": len(fixC135),
            "Fix_C_points": [list(pt) for pt in fixC135],
            "witness_word_CS": wit_cs,
            "witness_word_LR": "".join(wit_lr),
            "witness_rho3_exp": wit_rho3,
            "witness_fix_O27": wit_f27,
            "witness_fix_O5": wit_f5,
            "witness_fix_O135": wit_f135,
            "d_neu": d135_neu,
            "d_ch": d135_ch,
            "krylov_primes": primes135,
            "paired_modes": paired_modes_135,
            "unpaired_chiral_count": d135_ch - paired_modes_135,
            "unpaired_chiral_poly_Q10": str(sp.factor(u1_x)),
            "Q10_exact_match": Q10_exact_match,
            "unpaired_neutral_extra_nonzero_poly_P10": str(sp.factor(P10_x_expr)),
            "s_r_Q10_r1_to_12": s_Q10_1_12,
            "s_r_P10_r1_to_12": s_P10_1_12,
            "exact_trace_mismatch_sP10_minus_sQ10_r1_to_12": s_diff_P10_minus_Q10,
            "direct_sparse_trace_mismatch_r1_to_6": direct_trace_diffs_1_6,
            "direct_matches_sP10_minus_sQ10_r1_to_6": bool(direct_trace_diffs_1_6 == s_diff_P10_minus_Q10[:6]),
            "note_vs_E7_prereg_minus_sQ10": (
                "Unpaired Pi_1 factor matches Q_10(x) identically (10 roots, 949 paired modes), "
                "while Pi_0 carries 10 nonzero unpaired roots P_10(x) = (x^2-4)(x^2-1)(x^6-9x^4+21x^2-10) "
                "in addition to x(x^2-9); hence tr_neu((A/2)^r)-(3^r+(-3)^r)-tr_ch(A^r) equals "
                "s_r(P_10) - s_r(Q_10) = [0,0,0,-36,0,-432,...] rather than -s_r(Q_10)."
            ),
        },
    }


# ---------------------------------------------------------------------------
# MODULE L4: 6/6 Planted Negative Controls (RPF1..RPF6) & Blind Gates (RG1..RG6)
# ---------------------------------------------------------------------------

def run_L4(L2_aux, L3_res):
    t0 = time.perf_counter_ns()
    schreier_words, tree, p9 = L2_aux

    # RPF1 (mod 9): rho_3 fails to factor through G_2 = S_4, 6 non-C-type fixed elements
    O9 = markoff_orbit_LR(9)
    idx9 = {v: i for i, v in enumerate(O9)}
    pL9 = tuple(idx9[apply_L(v, 9)] for v in O9)
    pR9 = tuple(idx9[apply_R(v, 9)] for v in O9)
    pC9 = tuple(idx9[apply_C(v, 9)] for v in O9)
    pC29 = comp_perm(pC9, pC9)
    id9 = tuple(range(len(O9)))
    G2 = {id9: (0, 0)}
    q = deque([id9])
    rho3_conflict_mod9 = False
    while q:
        g = q.popleft()
        ce, se = G2[g]
        for gen, dc, ds in ((pL9, 2, 1), (pR9, 1, 1)):
            ng = comp_perm(gen, g)
            nce = (ce + dc) % 3
            nse = (se + ds) % 2
            if ng not in G2:
                G2[ng] = (nce, nse)
                q.append(ng)
            elif G2[ng] != (nce, nse):
                rho3_conflict_mod9 = True

    non_C_fixed_mod9 = 0
    for g in G2:
        if g == id9 or g == pC9 or g == pC29:
            continue
        if any(g[i] == i for i in range(len(O9))):
            non_C_fixed_mod9 += 1

    rpf1 = {
        "order_G2": len(G2),
        "rho3_fails_on_G2": rho3_conflict_mod9,
        "non_C_type_fixed_elements_count": non_C_fixed_mod9,
        "passed": bool(len(G2) == 24 and rho3_conflict_mod9 and non_C_fixed_mod9 == 6),
    }

    # RPF2 (mod 25): |O_25|=1000, |Fix(C)|=1, explicit relator breaking rho_3, trace ratio != 2
    O25 = markoff_orbit_LR(25)
    idx25 = {v: i for i, v in enumerate(O25)}
    pL25 = [idx25[apply_L(v, 25)] for v in O25]
    pR25 = [idx25[apply_R(v, 25)] for v in O25]
    pC25 = [idx25[apply_C(v, 25)] for v in O25]
    fixC25 = sum(1 for i in range(len(O25)) if pC25[i] == i)

    # Explicit relator word RLRRLLRRRLL has rho3 = 1, order 40 on O_25, so w^40 = id with rho3 = omega != 1!
    rel_word = "RLRRLLRRRLL"
    perm_rel = list(range(len(O25)))
    for ch in reversed(rel_word):
        gen = pL25 if ch == "L" else pR25
        perm_rel = [gen[i] for i in perm_rel]
    rel_ord = perm_order(perm_rel)
    rel_rho = sum(2 if c == "L" else 1 for c in rel_word) % 3
    rel_total_rho = (rel_ord * rel_rho) % 3

    def mv_A25(v):
        c1 = apply_C(v, 25)
        c2 = apply_C(c1, 25)
        return [
            apply_C(apply_S(v, 25), 25),
            apply_C(apply_C(apply_S(c2, 25), 25), 25),
            apply_S(c1, 25),
            apply_S(c2, 25),
            apply_C(apply_S(c1, 25), 25),
            apply_C(apply_C(apply_S(v, 25), 25), 25),
        ]

    adj25 = [Counter(idx25[u] for u in mv_A25(v)) for v in O25]
    t2_25 = sum(sum(c * c for c in adj25[j].values()) for j in range(len(O25)))
    t2C_25 = sum(sum(c * adj25[j].get(pC25[k_i], 0) for k_i, c in adj25[j].items()) for j in range(len(O25)))
    tr_neu2_25 = (t2_25 + 2 * t2C_25) // 3
    tr_ch2_25 = (t2_25 - t2C_25) // 3
    ratio2_sub36 = sp.Rational(tr_neu2_25 - 36, tr_ch2_25)
    ratio2_sub72 = sp.Rational(tr_neu2_25 - 72, tr_ch2_25)

    rpf2 = {
        "orbit_size": len(O25),
        "Fix_C_count": fixC25,
        "rho3_breaking_word": rel_word,
        "word_order_on_O25": rel_ord,
        "relator_rho3_exp_mod3": rel_total_rho,
        "tr_neu_A2": tr_neu2_25,
        "tr_ch_A2": tr_ch2_25,
        "ratio_sq_sub36": str(ratio2_sub36),
        "ratio_sq_sub72": str(ratio2_sub72),
        "breaks_halving_ratio_4": bool(ratio2_sub36 != 4 and ratio2_sub72 != 4),
        "passed": bool(len(O25) == 1000 and fixC25 == 1 and rel_total_rho != 0 and ratio2_sub36 != 4 and ratio2_sub72 != 4),
    }

    # RPF3 (mod 135): Z_6 & Fix(C)=3 hold, yet Delta_135 fails S_3 x Z_3 factorization (10 unpaired modes)
    m135 = L3_res["mod135_counterexample"]
    rpf3 = {
        "Fix_C_count": m135["Fix_C_count"],
        "witness_fix_O27": m135["witness_fix_O27"],
        "witness_fix_O5": m135["witness_fix_O5"],
        "witness_fix_O135": m135["witness_fix_O135"],
        "unpaired_chiral_count": m135["unpaired_chiral_count"],
        "Q10_exact_match": m135["Q10_exact_match"],
        "passed": bool(
            m135["Fix_C_count"] == 3
            and m135["witness_fix_O27"] == 3
            and m135["witness_fix_O5"] == 0
            and m135["witness_fix_O135"] == 0
            and m135["unpaired_chiral_count"] == 10
            and m135["Q10_exact_match"]
        ),
    }

    # RPF4 (single-half truncation at mod 729): restricting falling-factorial sifter to O_9^+ alone drops d_6 from 7 to 4
    sh_k6 = run_falling_factorial_engine(6, schreier_words, tree, p9, single_half_plus_only=True)
    rpf4 = {
        "single_half_plus_dims_d3_to_d6": sh_k6["dims"],
        "d6_full": 7,
        "d6_single_half": sh_k6["dims"][3],
        "passed": bool(sh_k6["dims"] == [2, 2, 3, 4]),
    }

    # RPF5 (P-only real (2,1)): keeps ||spec_1| - |spec_2|| < 10^{-35} on O_27 and O_81
    d27_r21 = mp.mpf(L3_res["chiral_flux_dps55"]["O_27"]["fluxes"]["real_2_1"]["spec1_minus_spec2_mag_diff"])
    d81_r21 = mp.mpf(L3_res["chiral_flux_dps55"]["O_81"]["real_2_1_spec1_minus_spec2_mag_diff"])
    thresh35 = mp.mpf(1) / mp.mpf(10)**35
    rpf5 = {
        "O_27_spec1_minus_spec2_mag_diff": mp_str(d27_r21, 15),
        "O_81_spec1_minus_spec2_mag_diff": mp_str(d81_r21, 15),
        "passed": bool(d27_r21 < thresh35 and d81_r21 < thresh35),
    }

    # RPF6 (broken C-conjugacy): dropping one move (C S) from A breaks [P_C, W] = 0 by O(1) on O_27 and O_81
    rpf6_norms = {}
    for m_mod in (27, 81):
        Om = markoff_orbit_LR(m_mod)
        idxm = {v: i for i, v in enumerate(Om)}
        n = len(Om)
        pC = [idxm[apply_C(v, m_mod)] for v in Om]

        def mv_broken(v):
            c1 = apply_C(v, m_mod)
            c2 = apply_C(c1, m_mod)
            # Drop move 0: C(S(v))! Keep remaining 5 moves.
            return [
                apply_C(apply_C(apply_S(c2, m_mod), m_mod), m_mod),
                apply_S(c1, m_mod),
                apply_S(c2, m_mod),
                apply_C(apply_S(c1, m_mod), m_mod),
                apply_C(apply_C(apply_S(v, m_mod), m_mod), m_mod),
            ]

        # Exact squared Frobenius norm || P_C W_broken - W_broken P_C ||_F^2 (pure integer!)
        # For column j: (P_C W_b)_{i, j} = (W_b)_{pC^-1[i], j}; (W_b P_C)_{i, j} = (W_b)_{i, pC[j]}
        cols = [Counter(idxm[u] for u in mv_broken(v)) for v in Om]
        frob_sq = 0
        for j in range(n):
            # col j of P_C W_b has entries pC[r]: val for r, val in cols[j]
            c_left = Counter({pC[r]: val for r, val in cols[j].items()})
            c_right = cols[pC[j]]
            all_rows = set(c_left) | set(c_right)
            for r in all_rows:
                d = c_left.get(r, 0) - c_right.get(r, 0)
                frob_sq += d * d
        rpf6_norms[f"O_{m_mod}_comm_frob_sq"] = frob_sq
        rpf6_norms[f"O_{m_mod}_comm_frob_norm"] = mp_str(mp.sqrt(mp.mpf(frob_sq)), 20)

    rpf6 = {
        **rpf6_norms,
        "passed": bool(rpf6_norms["O_27_comm_frob_sq"] > 0 and rpf6_norms["O_81_comm_frob_sq"] > 0),
    }

    elapsed_ms = (time.perf_counter_ns() - t0) // 1000000
    return {
        "elapsed_ms": elapsed_ms,
        "RPF1_mod9": rpf1,
        "RPF2_mod25": rpf2,
        "RPF3_mod135": rpf3,
        "RPF4_single_half_mod729": rpf4,
        "RPF5_real_2_1_no_mag_split": rpf5,
        "RPF6_broken_C_conjugacy": rpf6,
    }


def main():
    t_start = time.perf_counter_ns()
    script_path = os.path.abspath(__file__)
    out_dir = os.path.dirname(script_path)
    out_path = os.path.join(out_dir, "referee_a2_listening_tower_out.json")

    ast_audit = audit_source_ast(script_path)
    L1_res = run_L1()
    L2_res, L2_aux = run_L2()
    L3_res = run_L3()
    L4_res = run_L4(L2_aux, L3_res)

    # Compute RG1..RG6 strictly from computed results (zero literal flags!)
    expected_exc = {
        "(1,1)": 1,
        "(sgn,1)": 1,
        "(std,omega)": 1,
        "(sgn,omega)": -1,
        "(1,omega)": -1,
        "(std,1)": -1,
    }
    expected_non_exc = ["(1,omega^2)", "(sgn,omega^2)", "(std,omega^2)"]

    rg1 = bool(
        L1_res["generator_basis_LR"]["markoff_L_exact_zero"]
        and L1_res["generator_basis_LR"]["markoff_R_exact_zero"]
        and L1_res["generator_basis_LR"]["C3_eq_I"]
        and L1_res["generator_basis_LR"]["S2_eq_I"]
        and L1_res["G_jet"]["order"] == 216
        and L1_res["G_jet"]["distinct_O27_perms"] == 216
        and L1_res["G_jet"]["abelianization_Z6_conflicts"] == 0
        and L1_res["G_jet"]["case1_all_flip_eps"]
        and L1_res["G_jet"]["case1_max_fix"] == 0
        and L1_res["G_jet"]["case2_max_fix"] == 0
        and L1_res["G_jet"]["case3_fix_values"] == [3]
        and L1_res["G_jet"]["case3_single_mod9_fiber_all"]
        and L1_res["G_jet"]["case3_at_333_count"] == 6
        and L1_res["G_jet"]["case3_at_333_all_in_1_4_7"]
        and L1_res["G_jet"]["case3_at_333_hensel_dets_mod3"] == [1]
        and L1_res["G_4_exhaustive"]["order"] == 1944
        and L1_res["G_4_exhaustive"]["abelianization_Z6_conflicts"] == 0
        and L1_res["G_4_exhaustive"]["case_fix_distribution"].get("case3_fix_3") == 432
        and L1_res["hensel_60_words_mod27_to_6561"]["passed_0_0_3_all_levels"] == 60
        and L1_res["S3_x_Z3_characters"]["character_orthonormality_ok"]
        and L1_res["S3_x_Z3_characters"]["delta_bot_factors_through_S3xZ3"]
        and L1_res["S3_x_Z3_characters"]["exceptions"] == expected_exc
        and sorted(L1_res["S3_x_Z3_characters"]["non_exceptions"]) == sorted(expected_non_exc)
        and L1_res["S3_x_Z3_characters"]["std_omega_6Q0_sigma_Q0_eq_0"]
        and L1_res["halving_identity_Z_x"]["mod27_direct_sympy_residual"] == 0
        and L1_res["halving_identity_Z_x"]["mod27_krylov_crt_residual"] == 0
        and L1_res["halving_identity_Z_x"]["mod27_direct_matches_krylov"]
        and L1_res["halving_identity_Z_x"]["mod81_prime_residuals"] == 0
        and L1_res["halving_identity_Z_x"]["mod81_Z_residual"] == 0
        and L1_res["halving_identity_Z_x"]["mod81_crt_exceeds_cauchy_bound"]
    )

    ff9 = L2_res["falling_factorial_2half_mod19683"]
    rg2 = bool(
        L2_res["symbolic_V4_and_Goldman"]["V4_normalizes_L_over_Zxyz"]
        and L2_res["symbolic_V4_and_Goldman"]["V4_normalizes_R_over_Zxyz"]
        and L2_res["symbolic_V4_and_Goldman"]["V4_commutes_symbolically_with_gamma4_words"]
        and L2_res["symbolic_V4_and_Goldman"]["goldman_2form_signs"] == {"L": 1, "R": 1, "C": 1, "sigma": 1, "tau": -1}
        and L2_res["full_orbit_mod729"]["orbit_size"] == 52488
        and L2_res["full_orbit_mod729"]["V4_rigidity_all_52488_pts"]
        and L2_res["full_orbit_mod729"]["dims_d3_to_d6"] == [2, 2, 3, 7]
        and L2_res["full_orbit_matches_2half_d3_to_d6"]
        and ff9["dims"] == [2, 2, 3, 7, 7, 7, 12]
        and ff9["sum_dims"] == 40
        and ff9["cube_ranks_E3_to_E8"] == [2, 2, 3, 7, 7, 7]
        and ff9["plus_half_ranks"] == [2, 2, 3, 4, 4, 4, 7]
        and ff9["minus_half_ranks"] == [2, 2, 3, 4, 4, 4, 7]
        and ff9["nonzero_goldman_divergences_mod3"] == 0
        and ff9["random_60_LR_gamma4_words_sifted_to_zero"] == 60
    )

    thresh38 = mp.mpf(1) / mp.mpf(10)**38
    rg3 = bool(
        L3_res["mirror_lock"]["det_dC"] == 1
        and L3_res["mirror_lock"]["det_dS"] == 1
        and L3_res["mirror_lock"]["det_dtau"] == -1
        and L3_res["mirror_lock"]["tau_C_tau_eq_Cinv"]
        and L3_res["mirror_lock"]["tau_S_tau_eq_S"]
        and L3_res["mirror_lock"]["tau_not_in_G3"]
        and L3_res["mirror_lock"]["tau_not_in_G4"]
        and L3_res["mirror_lock"]["order_G3_tau_eq_2_G3"]
        and mp.mpf(L3_res["chiral_flux_dps55"]["O_27"]["max_master_law_residual"]) < thresh38
        and mp.mpf(L3_res["chiral_flux_dps55"]["O_27"]["max_eig_vs_master_residual"]) < thresh38
        and mp.mpf(L3_res["chiral_flux_dps55"]["O_81"]["max_master_law_residual"]) < thresh38
        and L3_res["chiral_flux_dps55"]["O_27"]["fluxes"]["herm_pi_9"]["unlocks_3_to_1_1_1"]
        and L3_res["chiral_flux_dps55"]["guardrail3_unitary_scrambling_O27_pi9_q1"]["passed_lt_1e_45"]
    )

    c60_lv = L3_res["C60_Weyl_Heisenberg_intertwiner_Jk"]["levels"]
    m135 = L3_res["mod135_counterexample"]
    rg4 = bool(
        c60_lv["O_81_minus"]["all_100pct_pass"]
        and c60_lv["O_243_minus"]["all_100pct_pass"]
        and c60_lv["O_729_minus"]["all_100pct_pass"]
        and m135["orbit_size"] == 2880
        and m135["Fix_C_count"] == 3
        and m135["witness_fix_O27"] == 3
        and m135["witness_fix_O5"] == 0
        and m135["witness_fix_O135"] == 0
        and m135["paired_modes"] == 949
        and m135["unpaired_chiral_count"] == 10
        and m135["Q10_exact_match"]
        and m135["direct_matches_sP10_minus_sQ10_r1_to_6"]
    )

    rg5 = bool(
        L4_res["RPF1_mod9"]["passed"]
        and L4_res["RPF2_mod25"]["passed"]
        and L4_res["RPF3_mod135"]["passed"]
        and L4_res["RPF4_single_half_mod729"]["passed"]
        and L4_res["RPF5_real_2_1_no_mag_split"]["passed"]
        and L4_res["RPF6_broken_C_conjugacy"]["passed"]
    )

    total_ms = (time.perf_counter_ns() - t_start) // 1000000
    payload = {
        "card_id": "AGY-002_A2-LISTENING-TOWER",
        "role": "100pct_blind_disjoint_cold_room_zero_trust_referee",
        "empirical_inputs_used": "0 of 19",
        "total_elapsed_ms": total_ms,
        "python_version": sys.version.split()[0],
        "sympy_version": sp.__version__,
        "mpmath_version": mp.__version__,
        "L1_all_3k_B2009_B2010": L1_res,
        "L2_3adic_step_law_mod19683": L2_res,
        "L3_mirror_lock_chiral_flux_C60_mod135": L3_res,
        "L4_negative_controls_RPF1_to_RPF6": L4_res,
        "audit": {
            **ast_audit,
            "json_float_count": 0,
        },
        "referee_gates": {
            "RG1": rg1,
            "RG2": rg2,
            "RG3": rg3,
            "RG4": rg4,
            "RG5": rg5,
            "RG6": False,
        },
    }

    j_floats = count_json_floats(payload)
    payload["audit"]["json_float_count"] = j_floats
    rg6 = bool(
        ast_audit["ast_float_literal_count"] == 0
        and ast_audit["ast_complex_literal_count"] == 0
        and ast_audit["ast_float_complex_call_count"] == 0
        and ast_audit["forbidden_imports_count"] == 0
        and j_floats == 0
    )
    payload["referee_gates"]["RG6"] = rg6

    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")

    print(
        f"REFEREE COMPLETE in {total_ms} ms | "
        f"RG1..RG6 = {[rg1, rg2, rg3, rg4, rg5, rg6]} | "
        f"RPF1..RPF6 = {[L4_res[k]['passed'] for k in ('RPF1_mod9','RPF2_mod25','RPF3_mod135','RPF4_single_half_mod729','RPF5_real_2_1_no_mag_split','RPF6_broken_C_conjugacy')]} | "
        f"json_float_count = {j_floats}"
    )


if __name__ == "__main__":
    main()
